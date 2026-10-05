"""PFE 601 lab: construct and inspect a minimal PDF object graph.

This is a teaching fixture, not a production PDF writer. It deliberately keeps
the object model small enough to inspect by hand and records the boundaries.
"""
from pathlib import Path
from pypdf import PdfReader
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "pfe601-minimal.pdf"
RESULT = ROOT / "pfe601-object-lab-results.json"

objects = {
    1: b"<< /Type /Catalog /Pages 2 0 R >>",
    2: b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
    3: b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
    4: b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    5: b"<< /Length 44 >>\nstream\nBT /F1 24 Tf 72 720 Td (PFE 601) Tj ET\nendstream",
}

parts = [b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"]
offsets = [0]
for number in range(1, 6):
    offsets.append(sum(len(x) for x in parts))
    parts.append(f"{number} 0 obj\n".encode() + objects[number] + b"\nendobj\n")
xref_offset = sum(len(x) for x in parts)
xref = [b"xref\n0 6\n", b"0000000000 65535 f \n"]
for off in offsets[1:]:
    xref.append(f"{off:010d} 00000 n \n".encode())
parts.append(b"".join(xref))
parts.append(f"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode())
OUT.write_bytes(b"".join(parts))

reader = PdfReader(OUT)
page = reader.pages[0]
text = page.extract_text().strip()
raw = OUT.read_bytes()
result = {
    "artifact": OUT.name,
    "sha256": hashlib.sha256(raw).hexdigest(),
    "pdf_header": raw[:8].decode("latin1"),
    "objects_written": 5,
    "objects_seen_by_regex": len(re.findall(rb"\n[1-5] 0 obj\n", raw)),
    "pages": len(reader.pages),
    "media_box_pt": [float(page.mediabox.width), float(page.mediabox.height)],
    "extracted_text": text,
    "root_type": str(reader.trailer["/Root"]["/Type"]),
    "independent_parser": "pypdf",
    "status": "OBSERVED_AND_VERIFIED_FOR_THIS_FIXTURE",
    "limits": [
        "No compression, transparency, Unicode font, tagging, annotations, signatures, encryption, incremental update, or PDF 2.0 feature is exercised.",
        "The Type1 Helvetica resource is a teaching fixture and is not a production font-embedding recommendation.",
        "Parser acceptance and text extraction do not establish visual, accessibility, print, archival, or security conformance."
    ]
}
RESULT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
