#!/usr/bin/env python3
from pathlib import Path
import base64, tarfile, io
Path("releases").mkdir(exist_ok=True)
for prefix in ("part1", "part2"):
    parts = sorted(Path("releases_parts").glob(prefix + "_*.txt"), key=lambda p: p.name)
    if not parts:
        continue
    b64 = "".join(p.read_text() for p in parts)
    data = base64.b64decode(b64)
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        tar.extractall("releases")
    print(prefix, "OK")
print("releases:", [p.name for p in Path("releases").iterdir()])
