#!/usr/bin/env bash
# chequeo_remoto.sh — Ejecuta las 12 pruebas remotas de docs-kb (GuiaMCP.md) vía JSON-RPC
# sobre streamable-http, contra el endpoint público con Bearer token.
#
# Uso:
#   ./chequeo_remoto.sh                 # tabla de resultados en terminal
#   ./chequeo_remoto.sh --md [archivo]  # además escribe un reporte markdown
#                                       # (por defecto resultados/chequeo-AAAA-MM-DD.md)
#
# Requiere: bash, curl, python3. Lee DOCS_KB_TOKEN y DOCS_KB_URL de .env (junto al script)
# o del entorno. Código de salida = número de pruebas en FAIL.

set -uo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$DIR/.env" ]]; then set -a; . "$DIR/.env"; set +a; fi
: "${DOCS_KB_TOKEN:?Falta DOCS_KB_TOKEN (defínelo en .env o en el entorno)}"
URL="${DOCS_KB_URL:-https://mcp-documentacion.adolfo-s-rey-b.com/mcp}"

MD=""
if [[ "${1:-}" == "--md" ]]; then
  MD="${2:-$DIR/resultados/chequeo-$(date +%F).md}"
  mkdir -p "$(dirname "$MD")"
fi

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
HDR=(-H "Content-Type: application/json"
     -H "Accept: application/json, text/event-stream"
     -H "Authorization: Bearer $DOCS_KB_TOKEN")
SESSION=""
ID=0

# Extrae el texto útil de una respuesta SSE/JSON-RPC.
extract() {
  python3 -I -c '
import json, sys
raw = sys.stdin.read()
lines = [l[5:].strip() for l in raw.splitlines() if l.startswith("data:")]
try:
    d = json.loads(lines[-1] if lines else raw)
except Exception:
    print("ERROR: respuesta no JSON: " + raw[:200]); sys.exit()
if "error" in d:
    print("ERROR: " + str(d["error"].get("message", d["error"]))); sys.exit()
r = d.get("result", {})
if "tools" in r:
    print("\n".join(t["name"] for t in r["tools"])); sys.exit()
txt = "\n".join(c.get("text", "") for c in r.get("content", []))
print(("ERROR: " if r.get("isError") else "") + txt)
'
}

# rpc <método> <params-json>  → deja el texto en $TMP/out y el tiempo en $TMP/time
rpc() {
  ID=$((ID + 1))
  local body
  body=$(printf '{"jsonrpc":"2.0","method":"%s","params":%s,"id":%d}' "$1" "$2" "$ID")
  curl -s --max-time 120 -X POST "$URL" "${HDR[@]}" -H "mcp-session-id: $SESSION" \
       -w '\n%{time_total}' -d "$body" > "$TMP/raw"
  tail -n1 "$TMP/raw" > "$TMP/time"
  sed '$d' "$TMP/raw" | extract > "$TMP/out"
}
tool() { rpc "tools/call" "{\"name\":\"$1\",\"arguments\":$2}"; }

# ---------------------------------------------------------------------------
# Sesión
# ---------------------------------------------------------------------------
INIT=$(curl -s -D "$TMP/h" --max-time 30 -o /dev/null -w '%{http_code} %{time_total}' -X POST "$URL" "${HDR[@]}" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"chequeo_remoto","version":"1.0"}},"id":0}')
SESSION=$(grep -i '^mcp-session-id:' "$TMP/h" | awk '{print $2}' | tr -d '\r')
HTTP=${INIT% *}; T_INIT=${INIT#* }
if [[ -z "$SESSION" ]]; then
  echo "No se pudo iniciar sesión MCP (HTTP $HTTP). 401=sin token, 403=token incorrecto, 000=servidor/túnel caído."
  exit 99
fi
curl -s --max-time 15 -X POST "$URL" "${HDR[@]}" -H "mcp-session-id: $SESSION" \
  -d '{"jsonrpc":"2.0","method":"notifications/initialized"}' > /dev/null

# ---------------------------------------------------------------------------
# Registro de resultados
# ---------------------------------------------------------------------------
declare -a ROWS
FAILS=0
record() {  # record <n> <prueba> <estado> <detalle>
  local t; t=$(cat "$TMP/time" 2>/dev/null || echo "-")
  local d="${4//|//}"
  ROWS+=("$1|$2|$3|$d|${t}s")
  [[ "$3" == "FAIL" ]] && FAILS=$((FAILS + 1))
  printf '%-3s %-40s %-5s %6ss  %s\n' "$1" "$2" "$3" "$t" "$4"
  if [[ -n "$MD" ]]; then
    { echo "#### Prueba $1 — $2 ($3)"; echo; echo '```text'; head -c 900 "$TMP/out"; echo; echo '```'; echo; } >> "$TMP/detail.md"
  fi
}
has() { grep -qE "$1" "$TMP/out"; }
first() { grep -oE "$1" "$TMP/out" | head -1; }

echo "docs-kb @ $URL  (HTTP $HTTP, init ${T_INIT}s, sesión $SESSION)"
echo "--------------------------------------------------------------------------------"

# 1. tools/list
rpc "tools/list" "{}"
N=$(grep -c '^docs_' "$TMP/out")
[[ "$N" -eq 8 ]] && record 1 "8 tools registrados" PASS "$N/8 tools" \
                 || record 1 "8 tools registrados" FAIL "$N/8 tools"

# 2. docs_status
tool docs_status '{}'
TECH=$(first 'Technologies: +[0-9]+ configured \| [0-9]+ collected' | tr -s ' ')
VEC=$(first 'Active \([0-9]+ vectors')
if has 'FAISS Search: +Active'; then record 2 "docs_status (FAISS activo)" PASS "$VEC; $TECH"
else record 2 "docs_status (FAISS activo)" FAIL "FAISS no activo; $TECH"; fi

# 3. docs_list_technologies
tool docs_list_technologies '{}'
if has '^ERROR|Error executing'; then record 3 "docs_list_technologies" FAIL "$(head -c 120 "$TMP/out")"
else
  TOT=$(grep -cE '\| +[0-9]+ pages' "$TMP/out"); LOC=$(grep -c '\[local\]' "$TMP/out")
  ZERO=$(grep -cE '\| +0 pages' "$TMP/out")
  record 3 "docs_list_technologies" PASS "$TOT techs, $LOC [local], $ZERO sin recolectar"
fi

# 4. Búsqueda keyword
tool docs_search '{"query":"str_detect","technology":"stringr"}'
if has 'Found [1-9][0-9]* result' && has '\[stringr\]'; then record 4 "docs_search keyword (str_detect)" PASS "$(first 'Found [0-9]+ result')"
else record 4 "docs_search keyword (str_detect)" FAIL "sin resultados de stringr"; fi

# 5. Búsqueda semántica en español (sin las palabras merge/join)
tool docs_search '{"query":"combinar tablas por columna comun"}'
TOP=$(grep -oE '^--- Result [0-9]+: \[[^]]+\]' "$TMP/out" | grep -oE '\[[^]]+\]' | tr '\n' ' ')
if grep -E '^--- Result [123]:' "$TMP/out" | grep -qE '\[(pandas|dplyr|tidyr)\]'; then
  record 5 "docs_search semántica (español)" PASS "top: $TOP"
else record 5 "docs_search semántica (español)" WARN "sin pandas/dplyr en top-3: $TOP"; fi

# 6. TOC de una página
tool docs_get_section '{"technology":"stringr","slug":"articles-stringr"}'
SEC=$(grep -oE '^ *#+ (.+) \(lines' "$TMP/out" | head -1 | sed -E 's/^ *#+ //; s/ \(lines$//')
if has 'Table of contents' && [[ -n "$SEC" ]]; then record 6 "docs_get_section (TOC)" PASS "primera sección: $SEC"
else record 6 "docs_get_section (TOC)" FAIL "sin TOC"; fi

# 7. Sección específica (la primera del TOC real)
if [[ -n "$SEC" ]]; then
  ARGS=$(python3 -I -c 'import json,sys; print(json.dumps({"technology":"stringr","slug":"articles-stringr","section":sys.argv[1]}))' "$SEC")
  tool docs_get_section "$ARGS"
  LEN=$(wc -c < "$TMP/out")
  if ! has '^ERROR' && [[ "$LEN" -gt 100 ]]; then record 7 "docs_get_section (sección)" PASS "\"$SEC\": $LEN chars"
  else record 7 "docs_get_section (sección)" FAIL "\"$SEC\": $(head -c 100 "$TMP/out")"; fi
else echo "-" > "$TMP/time"; : > "$TMP/out"; record 7 "docs_get_section (sección)" FAIL "sin sección de la prueba 6"; fi

# 8. Summary de una tecnología (numpy)
tool docs_generate_context '{"technologies":"numpy","context_type":"summary"}'
PAG=$(first 'Pages:\** [0-9]+' | tr -d '*'); UPD=$(first 'Updated:\** [0-9-]+' | tr -d '*')
if [[ -n "$PAG" && "$PAG" != "Pages: 0" ]]; then
  AGE=$(( ( $(date +%s) - $(date -d "${UPD#Updated: }" +%s 2>/dev/null || date +%s) ) / 86400 ))
  if [[ "$AGE" -gt 30 ]]; then record 8 "docs_generate_context (summary)" WARN "$PAG, $UPD (hace $AGE días)"
  else record 8 "docs_generate_context (summary)" PASS "$PAG, $UPD"; fi
else record 8 "docs_generate_context (summary)" FAIL "sin páginas"; fi

# 9. Cheatsheet pandas
tool docs_generate_context '{"technologies":"pandas","context_type":"cheatsheet"}'
BODY=$(sed '1,2d' "$TMP/out" | tr -d '[:space:]' | wc -c)
if [[ "$BODY" -gt 200 ]]; then record 9 "docs_generate_context (cheatsheet)" PASS "$BODY chars de contenido"
else record 9 "docs_generate_context (cheatsheet)" WARN "cheatsheet vacío ($BODY chars)"; fi

# 10. Historial de versiones
tool docs_version_history '{"technology":"stringr"}'
if has 'Current:'; then record 10 "docs_version_history" PASS "$(first 'Current: .*')"
else record 10 "docs_version_history" FAIL "$(head -c 100 "$TMP/out")"; fi

# 11. Changelog
tool docs_changelog '{"days":30}'
if has 'No changes|changes \('; then record 11 "docs_changelog (30 días)" PASS "$(head -1 "$TMP/out" | head -c 80)"
else record 11 "docs_changelog (30 días)" FAIL "$(head -c 100 "$TMP/out")"; fi

# 12. Fetch live (Firecrawl)
tool docs_fetch_live '{"url":"https://stringr.tidyverse.org/reference/str_detect.html","query":"pattern"}'
if has 'fetch failed|^ERROR'; then record 12 "docs_fetch_live (Firecrawl)" WARN "$(head -c 100 "$TMP/out")"
elif has 'str_detect'; then record 12 "docs_fetch_live (Firecrawl)" PASS "$(wc -c < "$TMP/out") chars"
else record 12 "docs_fetch_live (Firecrawl)" FAIL "contenido inesperado"; fi

# ---------------------------------------------------------------------------
P=0; W=0
for r in "${ROWS[@]}"; do case "$r" in *"|PASS|"*) P=$((P+1));; *"|WARN|"*) W=$((W+1));; esac; done
echo "--------------------------------------------------------------------------------"
echo "Resultado: $P PASS / $W WARN / $FAILS FAIL"

if [[ -n "$MD" ]]; then
  {
    echo "# Chequeo remoto docs-kb — $(date '+%F %H:%M')"
    echo
    echo "Endpoint: \`$URL\` · HTTP $HTTP · init ${T_INIT}s"
    echo
    echo "| # | Prueba | Estado | Detalle | Tiempo |"
    echo "|---|---|---|---|---|"
    for r in "${ROWS[@]}"; do echo "| ${r//|/ | } |"; done
    echo
    echo "**Resultado:** $P PASS / $W WARN / $FAILS FAIL"
    echo
    echo "## Salidas (recortadas)"
    echo
    cat "$TMP/detail.md"
  } > "$MD"
  echo "Reporte: $MD"
fi
exit "$FAILS"
