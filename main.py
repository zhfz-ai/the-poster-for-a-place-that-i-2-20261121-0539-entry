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
import zlib
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


# Colour type -> samples per pixel (PNG spec, table 11.1). Interlaced or
# sub-byte images are not part of this entry, so they are rejected below.
SAMPLES_PER_PIXEL = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}


def validate_png_structure(data: bytes) -> None:
    """Walk the whole chunk chain and prove the pixel data is intact.

    The shallow checks (magic, size, IHDR) would wave through a truncated
    or CRC-corrupt file. This walks every chunk verifying its CRC32,
    requires a terminating IEND with no trailing bytes, and decompresses
    the IDAT stream to confirm it holds exactly the raw scanlines the
    IHDR promises (one filter byte plus width*samples bytes per row).
    """
    width, height = png_dimensions(data)
    bit_depth, colour_type = data[24], data[25]
    if bit_depth != 8 or colour_type not in SAMPLES_PER_PIXEL:
        raise SystemExit(
            f"entry.png bit depth {bit_depth} / colour type {colour_type} "
            "is not a plain 8-bit image"
        )
    if data[28] != 0:  # interlace method byte in IHDR
        raise SystemExit("entry.png is interlaced; expected a plain image")

    idat = bytearray()
    offset = 8  # past the 8-byte PNG signature
    seen_iend = False
    while offset < len(data):
        if offset + 8 > len(data):
            raise SystemExit("entry.png ends inside a chunk header")
        (length,) = struct.unpack(">I", data[offset : offset + 4])
        chunk_type = data[offset + 4 : offset + 8]
        chunk_data = data[offset + 8 : offset + 8 + length]
        if len(chunk_data) != length or offset + 12 + length > len(data):
            raise SystemExit(f"entry.png chunk {chunk_type!r} is truncated")
        (stored_crc,) = struct.unpack(
            ">I", data[offset + 8 + length : offset + 12 + length]
        )
        if zlib.crc32(chunk_type + chunk_data) & 0xFFFFFFFF != stored_crc:
            raise SystemExit(f"entry.png chunk {chunk_type!r} fails its CRC32")
        if chunk_type == b"IDAT":
            idat += chunk_data
        elif chunk_type == b"IEND":
            seen_iend = True
            offset += 12 + length
            break
        offset += 12 + length

    if not seen_iend:
        raise SystemExit("entry.png has no IEND chunk; not a whole PNG")
    if offset != len(data):
        raise SystemExit("entry.png has trailing bytes after IEND")
    if not idat:
        raise SystemExit("entry.png has no IDAT chunks; no pixel data")

    try:
        raw = zlib.decompress(bytes(idat))
    except zlib.error as exc:
        raise SystemExit(f"entry.png IDAT does not decompress: {exc}")
    row_bytes = 1 + width * SAMPLES_PER_PIXEL[colour_type]  # filter byte + row
    if len(raw) != row_bytes * height:
        raise SystemExit(
            f"entry.png decompresses to {len(raw)} bytes, "
            f"expected {row_bytes * height} for {width}x{height}"
        )


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
    validate_png_structure(data)

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
