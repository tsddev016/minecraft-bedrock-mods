#!/usr/bin/env python3
"""Decodifica releases_b64/*.b64 para releases/"""
import base64
from pathlib import Path
src = Path("releases_b64")
dst = Path("releases")
dst.mkdir(exist_ok=True)
for p in src.glob("*.b64"):
    name = p.name[:-4]
    (dst / name).write_bytes(base64.b64decode(p.read_text()))
    print("OK", name)
