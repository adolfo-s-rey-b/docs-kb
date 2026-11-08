#!/usr/bin/env python3
"""Genera changelog/AAAA-MM-DD.jsonl (formato de docs_changelog) a partir del historial
de git de sources/*/markdown en los últimos N días (por defecto 90). Lo usa el workflow
datos.yml para que el paquete local tenga changelog sin depender de ningún servidor."""
import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

days = int(sys.argv[1]) if len(sys.argv) > 1 else 90
out = subprocess.run(
    ["git", "log", f"--since={days} days ago", "--name-status", "--format=@@%H|%cI", "--", "sources/"],
    check=True, capture_output=True, text=True).stdout
by_day, ts = defaultdict(list), None
for line in out.splitlines():
    if line.startswith("@@"):
        ts = line[2:].split("|", 1)[1]
        continue
    parts = line.split("\t")
    if len(parts) < 2 or not ts:
        continue
    status, path = parts[0][0], parts[-1]
    p = Path(path)
    if len(p.parts) != 4 or p.parts[2] != "markdown" or p.suffix != ".md":
        continue
    by_day[ts[:10]].append({"ts": ts, "tech": p.parts[1], "slug": p.stem,
                            "old_hash": None, "new_hash": {"A": "added", "M": "modified", "D": "removed"}.get(status, status),
                            "version_change": False})
Path("changelog").mkdir(exist_ok=True)
for day, entries in by_day.items():
    with open(f"changelog/{day}.jsonl", "w", encoding="utf-8") as f:
        for e in entries:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
print(f"changelog: {sum(map(len, by_day.values()))} entradas en {len(by_day)} días")
