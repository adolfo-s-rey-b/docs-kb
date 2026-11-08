#!/usr/bin/env python3
"""Empaqueta lo que necesita el servidor MCP local (plugin/docs_kb_local.py) en
dist/docs-kb-datos.tar.gz y escribe dist/version.json (commit, sha256, tamaño...).
Contenido: mcp_server.py, config.json, requirements-local.txt, LICENSE, ATTRIBUTION.md,
sources/*/markdown/*.md, sources/*/manifest.json, index/ (sin la caché de embeddings)
y changelog/."""
import hashlib
import json
import subprocess
import tarfile
from datetime import datetime, timezone
from pathlib import Path

ARCHIVO = "docs-kb-datos.tar.gz"
INDEX_FILES = ["embeddings.faiss", "embeddings-meta.json", "embeddings-info.json",
               "section-index.json", "tech-map.json"]

dist = Path("dist")
dist.mkdir(exist_ok=True)
files = [Path(p) for p in ("mcp_server.py", "config.json", "requirements-local.txt", "LICENSE", "ATTRIBUTION.md")]
files += [Path("index") / f for f in INDEX_FILES]
missing = [str(f) for f in files if not f.exists()]
if missing:
    raise SystemExit(f"faltan archivos: {missing}")
techs = sorted(p.name for p in Path("sources").iterdir() if (p / "markdown").is_dir())
pages = 0
for t in techs:
    md = sorted((Path("sources") / t / "markdown").glob("*.md"))
    pages += len(md)
    files += md
    if (Path("sources") / t / "manifest.json").exists():
        files.append(Path("sources") / t / "manifest.json")
files += sorted(Path("changelog").glob("*.jsonl")) if Path("changelog").is_dir() else []

with tarfile.open(dist / ARCHIVO, "w:gz", compresslevel=6) as tf:
    for f in files:
        tf.add(f, arcname=str(f), recursive=False)

h = hashlib.sha256()
with open(dist / ARCHIVO, "rb") as fh:
    for chunk in iter(lambda: fh.read(1 << 20), b""):
        h.update(chunk)
info = json.loads(Path("index/embeddings-info.json").read_text())
version = {
    "formato": 1,
    "commit": subprocess.run(["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip(),
    "fecha": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "archivo": ARCHIVO,
    "sha256": h.hexdigest(),
    "bytes": (dist / ARCHIVO).stat().st_size,
    "tecnologias": len(techs),
    "paginas": pages,
    "vectores": info.get("vectors"),
    "modelo": info.get("model"),
    "indice": info.get("index_type", "flat"),
}
(dist / "version.json").write_text(json.dumps(version, indent=2, ensure_ascii=False))
print(json.dumps(version, indent=2, ensure_ascii=False))
