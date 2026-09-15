#!/usr/bin/env python3
"""Create a publication-safe copy of a DOCX template.

Removes custom XML, comments, author metadata, and relationships to removed parts.
It deliberately does not replace visible personal content; the calling workflow must
replace visible text with placeholders and render the result for review.
"""

from __future__ import annotations

import argparse
import re
import shutil
import tempfile
import zipfile
from pathlib import Path


REMOVED_PREFIXES = (
    "customXml/",
    "customXML/",
    "word/comments",
    "word/people",
)


def sanitize_xml(name: str, data: bytes) -> bytes:
    text = data.decode("utf-8")

    if name.endswith(".rels"):
        text = re.sub(
            r'<Relationship\b[^>]*Target="[^"]*(?:customXml|customXML|comments|people)[^"]*"[^>]*/>',
            "",
            text,
            flags=re.IGNORECASE,
        )

    if name == "[Content_Types].xml":
        text = re.sub(
            r'<Override\b[^>]*PartName="/(?:customXml|customXML|word/comments|word/people)[^"]*"[^>]*/>',
            "",
            text,
            flags=re.IGNORECASE,
        )

    if name == "docProps/core.xml":
        text = re.sub(r"<dc:creator>.*?</dc:creator>", "<dc:creator></dc:creator>", text)
        text = re.sub(
            r"<cp:lastModifiedBy>.*?</cp:lastModifiedBy>",
            "<cp:lastModifiedBy></cp:lastModifiedBy>",
            text,
        )
        text = re.sub(r"<cp:keywords>.*?</cp:keywords>", "", text)
        text = re.sub(r"<cp:category>.*?</cp:category>", "", text)

    return text.encode("utf-8")


def sanitize(source: Path, destination: Path) -> None:
    if source.resolve() == destination.resolve():
        raise ValueError("Destination must differ from source; originals are immutable.")
    if not zipfile.is_zipfile(source):
        raise ValueError(f"Not a valid DOCX/ZIP file: {source}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as handle:
        temporary = Path(handle.name)

    try:
        with zipfile.ZipFile(source, "r") as incoming, zipfile.ZipFile(
            temporary, "w", zipfile.ZIP_DEFLATED
        ) as outgoing:
            for item in incoming.infolist():
                if item.filename.startswith(REMOVED_PREFIXES):
                    continue
                data = incoming.read(item.filename)
                if item.filename.endswith((".xml", ".rels")):
                    data = sanitize_xml(item.filename, data)
                outgoing.writestr(item, data)
        shutil.move(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    sanitize(args.source, args.destination)
    print(f"Sanitized template: {args.destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
