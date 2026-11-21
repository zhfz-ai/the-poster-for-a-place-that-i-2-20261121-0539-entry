"""The Poster for a Place That Isn't There — entry program.

Writes one travel poster to /output/entry.png: "ONDINE", an invented
glass-desert destination with a mirrored obelisk under a huge low sun.
The poster bytes live beside this file as entry.png; the program
validates them with the standard library only (whole PNG, at most
1 MiB, 1024x1024) and copies them to the output directory, so the
bytes the judge sees are exactly the bytes in the repository.

Run locally:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import struct
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

MAX_BYTES = 1_048_576  # the gate's limit: at most 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
EXPECTED_SIZE = (1024, 1024)


def png_dimensions(data: bytes) -> tuple[int, int]:
    """Read width/height from a PNG's IHDR chunk (bytes 16..24)."""
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk; not a whole PNG")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def sha256_hex(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG")
    if png_dimensions(data) != EXPECTED_SIZE:
        raise SystemExit(f"entry.png is {png_dimensions(data)}, expected {EXPECTED_SIZE}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(OUTPUT_DIR, 0o755)
    except OSError:
        pass
    target = OUTPUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    os.chmod(target, 0o644)
    if sha256_hex(target) != sha256_hex(SOURCE):
        raise SystemExit("copied entry.png does not match the source bytes")


if __name__ == "__main__":
    main()
