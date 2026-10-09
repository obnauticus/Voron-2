"""Hash the local HTML, stylesheet and illustrations used by the PDF export."""
from pathlib import Path
import hashlib


def pdf_input_sha256(site: Path) -> str:
    inputs = [site / "print.html", site / "style.css"]
    inputs.extend(sorted((site / "assets").rglob("*")))
    digest = hashlib.sha256()
    for path in inputs:
        if path.is_file():
            digest.update(path.relative_to(site).as_posix().encode("utf-8"))
            digest.update(b"\0")
            digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()
