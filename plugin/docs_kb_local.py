#!/usr/bin/env python3
"""docs-kb local: instala, actualiza y ejecuta el servidor MCP de docs-kb en tu equipo.

La documentación y el índice semántico se descargan de GitHub (Release "datos" del
repositorio https://github.com/adolfo-s-rey-b/docs-kb), que GitHub Actions publica
cada semana. No hace falta ningún servidor: todo corre localmente.

Uso:
  python3 docs_kb_local.py install     Primera instalación (descarga ~150 MB + entorno Python + modelo)
  python3 docs_kb_local.py update      Actualiza si hay una versión publicada más nueva
  python3 docs_kb_local.py status      Versión instalada y versión disponible
  python3 docs_kb_local.py serve       Servidor MCP por stdio (lo ejecuta Claude Code)
  python3 docs_kb_local.py ensure      Instala o actualiza si hace falta (hook de inicio de sesión)
  python3 docs_kb_local.py check       Prueba end-to-end del servidor local (12 pruebas)
  python3 docs_kb_local.py uninstall   Borra los datos locales

Directorio de datos: $DOCS_KB_HOME, o ${CLAUDE_PLUGIN_DATA} dentro del plugin, o
~/.local/share/docs-kb (macOS: ~/Library/Application Support/docs-kb; Windows: %LOCALAPPDATA%/docs-kb).

Solo usa la biblioteca estándar de Python (3.10+). Las dependencias del servidor
(mcp, fastembed, faiss-cpu...) se instalan en un entorno virtual propio.
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = os.environ.get("DOCS_KB_REPO", "adolfo-s-rey-b/docs-kb")
RELEASE_TAG = os.environ.get("DOCS_KB_RELEASE", "datos")
RELEASE_URL = f"https://github.com/{REPO}/releases/download/{RELEASE_TAG}"
VERSION_URL = f"{RELEASE_URL}/version.json"
UA = "docs-kb-local/1.0 (+https://github.com/adolfo-s-rey-b/docs-kb)"
CHECK_EVERY_HOURS = 12
KEEP_VERSIONS = 2
FORMAT_SUPPORTED = 1


# ---------------------------------------------------------------------------
# Rutas
# ---------------------------------------------------------------------------

def home() -> Path:
    if os.environ.get("DOCS_KB_HOME"):
        return Path(os.environ["DOCS_KB_HOME"]).expanduser()
    if os.environ.get("CLAUDE_PLUGIN_DATA"):  # plugin: el mismo directorio en hook, MCP y comandos
        return Path(os.environ["CLAUDE_PLUGIN_DATA"])
    system = platform.system()
    if system == "Windows":
        return Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "docs-kb"
    if system == "Darwin":
        return Path.home() / "Library" / "Application Support" / "docs-kb"
    return Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share")) / "docs-kb"


H = home()
VENV = H / "venv"
VERSIONS = H / "versiones"
CURRENT = H / "actual"            # texto: nombre del directorio de la versión activa
STATE = H / "estado.json"
LOCK = H / "instalando.lock"
LOGFILE = H / "docs-kb.log"
MODELS = H / "modelos"


def venv_python() -> Path:
    return VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def log(msg: str) -> None:
    """Siempre a stderr (stdout es el canal MCP en `serve`) y al log."""
    line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {msg}"
    print(line, file=sys.stderr, flush=True)
    try:
        H.mkdir(parents=True, exist_ok=True)
        with open(LOGFILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


def read_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def write_json(path: Path, data) -> None:
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp.replace(path)


def current_dir() -> Path | None:
    try:
        d = VERSIONS / CURRENT.read_text(encoding="utf-8").strip()
    except OSError:
        return None
    return d if (d / "mcp_server.py").exists() else None


def local_version() -> dict | None:
    d = current_dir()
    return read_json(d / "version.json") if d else None


def is_ready() -> bool:
    d = current_dir()
    return bool(d and venv_python().exists() and (d / "index" / "embeddings.faiss").exists()
                and (VENV / ".docs-kb-reqs").exists())


# ---------------------------------------------------------------------------
# Descarga
# ---------------------------------------------------------------------------

def http_get(url: str, timeout: int = 60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=timeout)


def remote_version() -> dict:
    with http_get(VERSION_URL, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def download(url: str, dest: Path, expected_sha256: str, size: int = 0) -> None:
    h = hashlib.sha256()
    done, next_report = 0, 0.1
    with http_get(url, timeout=120) as r, open(dest, "wb") as f:
        total = size or int(r.headers.get("Content-Length") or 0)
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            f.write(chunk)
            h.update(chunk)
            done += len(chunk)
            if total and done / total >= next_report:
                log(f"  descargado {done / 1e6:.0f}/{total / 1e6:.0f} MB")
                next_report += 0.1
    if h.hexdigest() != expected_sha256:
        dest.unlink(missing_ok=True)
        raise RuntimeError("la descarga no coincide con el sha256 publicado (¿se estaba actualizando el Release?); reintenta más tarde")


def safe_extract(tar_path: Path, dest: Path) -> None:
    with tarfile.open(tar_path, "r:gz") as tf:
        root = dest.resolve()
        for m in tf.getmembers():
            target = (dest / m.name).resolve()
            if not str(target).startswith(str(root)) or m.issym() or m.islnk() or m.isdev():
                raise RuntimeError(f"entrada no permitida en el paquete: {m.name}")
        if sys.version_info >= (3, 12):
            tf.extractall(dest, filter="data")
        else:
            tf.extractall(dest)


def install_version(rv: dict) -> Path:
    if int(rv.get("formato", 1)) > FORMAT_SUPPORTED:
        raise RuntimeError("esta versión de docs_kb_local.py es antigua para los datos publicados: actualiza el plugin")
    name = rv["commit"][:12]
    target = VERSIONS / name
    VERSIONS.mkdir(parents=True, exist_ok=True)
    if not (target / "mcp_server.py").exists():
        log(f"Descargando docs-kb {name} ({rv.get('paginas', '?')} páginas, {int(rv.get('bytes', 0)) / 1e6:.0f} MB)...")
        with tempfile.TemporaryDirectory(dir=H) as tmp:
            tar = Path(tmp) / rv["archivo"]
            download(f"{RELEASE_URL}/{rv['archivo']}", tar, rv["sha256"], int(rv.get("bytes", 0)))
            staging = Path(tmp) / "extraido"
            staging.mkdir()
            safe_extract(tar, staging)
            write_json(staging / "version.json", rv)
            if target.exists():
                shutil.rmtree(target)
            staging.rename(target)
    tmpcur = CURRENT.with_suffix(".tmp")
    tmpcur.write_text(name, encoding="utf-8")
    tmpcur.replace(CURRENT)
    # conservar la versión activa y la anterior (un servidor ya abierto puede seguir usándola)
    versions = sorted((p for p in VERSIONS.iterdir() if p.is_dir()), key=lambda p: p.stat().st_mtime, reverse=True)
    for old in [p for p in versions if p.name != name][KEEP_VERSIONS - 1:]:
        shutil.rmtree(old, ignore_errors=True)
    return target


# ---------------------------------------------------------------------------
# Entorno Python y modelo
# ---------------------------------------------------------------------------

def run(cmd: list, **kw) -> None:
    log("  $ " + " ".join(str(c) for c in cmd))
    with open(LOGFILE, "a", encoding="utf-8") as lf:
        subprocess.run(cmd, check=True, stdout=lf, stderr=lf, **kw)


def ensure_venv(data_dir: Path) -> None:
    reqs = data_dir / "requirements-local.txt"
    want = hashlib.sha256(reqs.read_bytes()).hexdigest()
    marker = VENV / ".docs-kb-reqs"
    if venv_python().exists() and marker.exists() and marker.read_text().strip() == want:
        return
    log("Preparando el entorno Python (mcp, fastembed, faiss-cpu)... puede tardar unos minutos")
    uv = shutil.which("uv")
    if not venv_python().exists():
        if uv:
            run([uv, "venv", "--python", sys.executable, str(VENV)])
        else:
            try:
                run([sys.executable, "-m", "venv", str(VENV)])
            except subprocess.CalledProcessError:
                raise RuntimeError("no se pudo crear el entorno virtual. En Debian/Ubuntu instala `python3-venv` "
                                   "(o instala `uv`: https://docs.astral.sh/uv/) y reintenta")
    if uv:
        run([uv, "pip", "install", "--python", str(venv_python()), "-r", str(reqs)])
    else:
        run([str(venv_python()), "-m", "pip", "install", "--disable-pip-version-check", "-q", "-r", str(reqs)])
    marker.write_text(want)


def server_env(data_dir: Path) -> dict:
    env = dict(os.environ)
    env["DOCS_KB_PATH"] = str(data_dir)
    env["FASTEMBED_CACHE_PATH"] = str(MODELS)
    env.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")
    # Firecrawl solo si el usuario tiene uno propio; si no, docs_fetch_live descarga directo
    env.pop("FIRECRAWL_URL", None)
    if os.environ.get("DOCS_KB_FIRECRAWL_URL"):
        env["FIRECRAWL_URL"] = os.environ["DOCS_KB_FIRECRAWL_URL"]
    return env


def ensure_model(data_dir: Path) -> None:
    info = read_json(data_dir / "index" / "embeddings-info.json", {})
    model = info.get("model", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    flag = MODELS / (hashlib.sha1(model.encode()).hexdigest()[:12] + ".ok")
    if flag.exists():
        return
    log(f"Descargando el modelo de embeddings {model} (~220 MB, una sola vez)...")
    MODELS.mkdir(parents=True, exist_ok=True)
    run([str(venv_python()), "-c",
         "import sys; from fastembed import TextEmbedding; TextEmbedding(model_name=sys.argv[1])", model],
        env=server_env(data_dir))
    flag.write_text(model)


# ---------------------------------------------------------------------------
# Lock (una sola instalación a la vez)
# ---------------------------------------------------------------------------

class InstallLock:
    def __enter__(self):
        H.mkdir(parents=True, exist_ok=True)
        try:
            if LOCK.exists() and time.time() - LOCK.stat().st_mtime > 3 * 3600:
                LOCK.unlink()  # lock huérfano de una instalación interrumpida
            self.fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(self.fd, str(os.getpid()).encode())
            return self
        except FileExistsError:
            raise BlockingIOError("ya hay una instalación/actualización en curso")

    def __exit__(self, *exc):
        os.close(self.fd)
        LOCK.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# Comandos
# ---------------------------------------------------------------------------

def cmd_install(force: bool = False, quiet: bool = False) -> int:
    try:
        with InstallLock():
            rv = remote_version()
            lv = local_version()
            if force or not lv or lv.get("commit") != rv.get("commit") or not current_dir():
                d = install_version(rv)
            else:
                d = current_dir()
                if not quiet:
                    log(f"docs-kb ya está en la última versión ({rv['commit'][:12]}, {rv.get('fecha', '')[:10]})")
            ensure_venv(d)
            ensure_model(d)
            state = read_json(STATE, {}) or {}
            state.update(ultima_revision=time.time(), version=rv["commit"][:12])
            write_json(STATE, state)
            log(f"docs-kb listo: {rv.get('paginas', '?')} páginas de {rv.get('tecnologias', '?')} tecnologías, "
                f"versión {rv['commit'][:12]} ({rv.get('fecha', '')[:10]}). Datos en {H}")
            return 0
    except BlockingIOError as e:
        if not quiet:
            log(f"docs-kb: {e}")
        return 0
    except Exception as e:
        log(f"docs-kb: ERROR en la instalación: {e}")
        return 1


def needs_check() -> bool:
    state = read_json(STATE, {}) or {}
    return time.time() - float(state.get("ultima_revision", 0)) > CHECK_EVERY_HOURS * 3600


def spawn_background(*args: str) -> None:
    H.mkdir(parents=True, exist_ok=True)
    kw = {"stdin": subprocess.DEVNULL, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL, "close_fds": True}
    if os.name == "nt":
        kw["creationflags"] = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    else:
        kw["start_new_session"] = True
    subprocess.Popen([sys.executable, str(Path(__file__).resolve()), *args], **kw)


def cmd_ensure() -> int:
    """Hook de inicio de sesión: instala si falta, o actualiza si pasó el intervalo."""
    if not is_ready():
        if not LOCK.exists():
            print("docs-kb: instalando la documentación local en segundo plano (primera vez, ~5 min). "
                  "Cuando termine, reconecta el servidor con /mcp.")
        return cmd_install(quiet=True)
    if needs_check():
        return cmd_install(quiet=True)
    return 0


def cmd_status() -> int:
    lv = local_version()
    print(f"Datos: {H}")
    print(f"Instalado: {lv['commit'][:12] + ' (' + lv.get('fecha', '')[:10] + ')' if lv else 'no'}"
          f"{'' if is_ready() else '  [incompleto: ejecuta install]'}")
    try:
        rv = remote_version()
        print(f"Publicado: {rv['commit'][:12]} ({rv.get('fecha', '')[:10]}), {rv.get('paginas', '?')} páginas, "
              f"{rv.get('vectores', '?')} vectores, {int(rv.get('bytes', 0)) / 1e6:.0f} MB")
        print("Al día." if lv and lv.get("commit") == rv.get("commit") else "Hay una actualización: ejecuta update")
    except Exception as e:
        print(f"No se pudo consultar GitHub: {e}")
    if LOCK.exists():
        print("Instalación/actualización en curso (ver docs-kb.log)")
    return 0


def fallback_server() -> int:
    """Servidor MCP mínimo (solo stdlib) mientras la instalación no termina."""
    def reply(msg_id, result=None, error=None):
        out = {"jsonrpc": "2.0", "id": msg_id}
        out["error" if error else "result"] = error or result
        sys.stdout.write(json.dumps(out) + "\n")
        sys.stdout.flush()

    def progress() -> str:
        try:
            tail = LOGFILE.read_text(encoding="utf-8").splitlines()[-4:]
        except OSError:
            tail = []
        return ("docs-kb se está instalando en este equipo (documentación + índice semántico desde GitHub). "
                "Cuando termine, reconecta el servidor con /mcp (o reinicia la sesión).\n\nÚltimas líneas del log:\n"
                + "\n".join(tail))

    tool = {"name": "docs_status", "description": "Estado de docs-kb (instalación en curso).",
            "inputSchema": {"type": "object", "properties": {}}}
    for line in sys.stdin:
        try:
            msg = json.loads(line)
        except ValueError:
            continue
        method, msg_id = msg.get("method"), msg.get("id")
        if msg_id is None:
            continue  # notificación
        if method == "initialize":
            reply(msg_id, {"protocolVersion": msg.get("params", {}).get("protocolVersion", "2024-11-05"),
                           "capabilities": {"tools": {}},
                           "serverInfo": {"name": "docs-kb", "version": "instalando"},
                           "instructions": "docs-kb se está instalando; usa docs_status para ver el avance."})
        elif method == "tools/list":
            reply(msg_id, {"tools": [tool]})
        elif method == "tools/call":
            reply(msg_id, {"content": [{"type": "text", "text": progress()}]})
        elif method == "ping":
            reply(msg_id, {})
        else:
            reply(msg_id, error={"code": -32601, "message": f"método no disponible durante la instalación: {method}"})
    return 0


def cmd_serve() -> int:
    if not is_ready():
        if not LOCK.exists():
            spawn_background("install", "--quiet")
        return fallback_server()
    if needs_check():
        spawn_background("update", "--quiet")
    d = current_dir()
    cmd = [str(venv_python()), str(d / "mcp_server.py")]
    if os.name == "nt":
        return subprocess.call(cmd, env=server_env(d))
    os.execve(cmd[0], cmd, server_env(d))
    return 0


# ---------------------------------------------------------------------------
# Prueba end-to-end (cliente MCP mínimo por stdio)
# ---------------------------------------------------------------------------

class StdioClient:
    def __init__(self):
        self.p = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "serve"],
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                  text=True, encoding="utf-8")
        self.msgs, self.id = {}, 0
        threading.Thread(target=self._reader, daemon=True).start()

    def _reader(self):
        for line in self.p.stdout:
            try:
                m = json.loads(line)
            except ValueError:
                continue
            if "id" in m:
                self.msgs[m["id"]] = m

    def request(self, method, params=None, timeout=180):
        self.id += 1
        self.p.stdin.write(json.dumps({"jsonrpc": "2.0", "id": self.id, "method": method, "params": params or {}}) + "\n")
        self.p.stdin.flush()
        t0 = time.time()
        while self.id not in self.msgs:
            if time.time() - t0 > timeout or self.p.poll() is not None:
                raise TimeoutError(f"sin respuesta a {method}")
            time.sleep(0.05)
        return self.msgs.pop(self.id), time.time() - t0

    def notify(self, method):
        self.p.stdin.write(json.dumps({"jsonrpc": "2.0", "method": method}) + "\n")
        self.p.stdin.flush()

    def call(self, name, args=None):
        m, dt = self.request("tools/call", {"name": name, "arguments": args or {}})
        if "error" in m:
            return "ERROR: " + str(m["error"].get("message")), dt
        r = m["result"]
        text = "\n".join(c.get("text", "") for c in r.get("content", []))
        return ("ERROR: " if r.get("isError") else "") + text, dt

    def close(self):
        try:
            self.p.stdin.close()
            self.p.wait(timeout=10)
        except Exception:
            self.p.kill()


def cmd_check() -> int:
    import re
    if not is_ready():
        print("docs-kb no está instalado o la instalación no terminó: ejecuta `install` primero.")
        return 1
    c = StdioClient()
    results = []

    def rec(n, name, ok, detail, dt):
        results.append(ok)
        print(f"{n:<3} {name:<38} {'PASS' if ok else 'FAIL'}  {dt:6.2f}s  {detail}")

    try:
        m, dt = c.request("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                                         "clientInfo": {"name": "docs-kb-check", "version": "1"}})
        c.notify("notifications/initialized")
        print(f"docs-kb local @ {current_dir()}  (init {dt:.1f}s)\n" + "-" * 80)
        m, dt = c.request("tools/list")
        names = [t["name"] for t in m["result"]["tools"]]
        rec(1, "8 tools registrados", len(names) == 8, f"{len(names)}/8", dt)
        t, dt = c.call("docs_status")
        rec(2, "docs_status (FAISS activo)", "Active (" in t, (re.search(r"Active \([^)]*\)", t) or [""])[0], dt)
        t, dt = c.call("docs_list_technologies")
        n = len(re.findall(r"\| +[0-9]+ pages", t)); z = len(re.findall(r"\| +0 pages", t))
        rec(3, "docs_list_technologies", n > 0 and "Error" not in t, f"{n} techs, {z} sin recolectar", dt)
        t, dt = c.call("docs_search", {"query": "str_detect", "technology": "stringr"})
        rec(4, "docs_search keyword (str_detect)", "[stringr]" in t, (re.search(r"Found \d+ result", t) or [""])[0], dt)
        t, dt = c.call("docs_search", {"query": "combinar tablas por columna comun"})
        top = re.findall(r"^--- Result [123]: \[([^\]]+)\]", t, re.M)
        rec(5, "docs_search semántica (español)", any(x in ("pandas", "dplyr", "tidyr") for x in top), f"top: {top}", dt)
        t, dt = c.call("docs_get_section", {"technology": "stringr", "slug": "articles-stringr"})
        sec = (re.findall(r"^ *#+ (.+) \(lines", t, re.M) or [None])[0]
        rec(6, "docs_get_section (TOC)", bool(sec), f"primera sección: {sec}", dt)
        t, dt = c.call("docs_get_section", {"technology": "stringr", "slug": "articles-stringr", "section": sec or ""})
        rec(7, "docs_get_section (sección)", len(t) > 100 and not t.startswith("ERROR"), f"{len(t)} chars", dt)
        t, dt = c.call("docs_generate_context", {"technologies": "numpy", "context_type": "summary"})
        rec(8, "docs_generate_context (summary)", bool(re.search(r"Pages:\**\s*[1-9]", t)), t.splitlines()[2][:60] if len(t.splitlines()) > 2 else "", dt)
        t, dt = c.call("docs_generate_context", {"technologies": "pandas", "context_type": "cheatsheet"})
        rec(9, "docs_generate_context (cheatsheet)", len("".join(t.split("\n")[2:]).strip()) > 200, f"{len(t)} chars", dt)
        t, dt = c.call("docs_version_history", {"technology": "stringr"})
        rec(10, "docs_version_history", "Current:" in t, (re.search(r"Current: .*", t) or [""])[0], dt)
        t, dt = c.call("docs_changelog", {"days": 30})
        rec(11, "docs_changelog (30 días)", "No changes" in t or "changes (" in t, t.splitlines()[0][:60], dt)
        t, dt = c.call("docs_fetch_live", {"url": "https://stringr.tidyverse.org/reference/str_detect.html", "query": "pattern"})
        rec(12, "docs_fetch_live (directo)", "str_detect" in t, f"{len(t)} chars", dt)
    except Exception as e:
        print(f"ERROR: {e}")
        results.append(False)
    finally:
        c.close()
    ok = sum(results)
    print("-" * 80 + f"\nResultado: {ok} PASS / {len(results) - ok} FAIL")
    return 0 if all(results) else 1


def cmd_uninstall(yes: bool) -> int:
    if not yes:
        print(f"Esto borra {H}. Repite con --yes para confirmar.")
        return 1
    shutil.rmtree(H, ignore_errors=True)
    print(f"Borrado {H}")
    return 0


def main() -> int:
    if sys.version_info < (3, 10):
        print("docs-kb necesita Python 3.10 o superior", file=sys.stderr)
        return 1
    args = sys.argv[1:]
    cmd = args[0] if args else "help"
    flags = set(args[1:])
    if cmd == "install":
        return cmd_install(force="--force" in flags, quiet="--quiet" in flags)
    if cmd == "update":
        return cmd_install(quiet="--quiet" in flags)
    if cmd == "ensure":
        return cmd_ensure()
    if cmd == "serve":
        return cmd_serve()
    if cmd == "status":
        return cmd_status()
    if cmd == "check":
        return cmd_check()
    if cmd == "uninstall":
        return cmd_uninstall("--yes" in flags)
    print(__doc__)
    return 0 if cmd in ("help", "-h", "--help") else 1


if __name__ == "__main__":
    sys.exit(main())
