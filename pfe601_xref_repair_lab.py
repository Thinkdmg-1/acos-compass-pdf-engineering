"""PFE 601 lab: distinguish parser recovery from an actual xref repair."""
from pathlib import Path
from pypdf import PdfReader
import json, re, hashlib

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "pfe601-minimal.pdf"
corrupt = ROOT / "pfe601-corrupt-xref.pdf"
repaired = ROOT / "pfe601-repaired-xref.pdf"
result_path = ROOT / "pfe601-xref-repair-results.json"

original = source.read_bytes()
# Deliberately change object 1's xref offset to an invalid nonzero location.
corrupt_bytes = original.replace(b"0000000015 00000 n ", b"0000000001 00000 n ", 1)
corrupt.write_bytes(corrupt_bytes)

recovery = {}
try:
    recovered_reader = PdfReader(corrupt, strict=False)
    recovery = {"parser_recovered": True, "pages": len(recovered_reader.pages), "text": recovered_reader.pages[0].extract_text().strip()}
except Exception as exc:
    recovery = {"parser_recovered": False, "error": type(exc).__name__ + ": " + str(exc)}

# Independent repair: locate every object header and rebuild the xref section.
object_offsets = {int(m.group(1)): m.start() for m in re.finditer(rb"(?m)^(\d+) 0 obj\n", corrupt_bytes)}
xref_start = corrupt_bytes.index(b"xref\n")
trailer_start = corrupt_bytes.index(b"trailer\n", xref_start)
prefix = corrupt_bytes[:xref_start]
trailer = corrupt_bytes[trailer_start:]
lines = [b"xref\n0 6\n", b"0000000000 65535 f \n"]
for number in range(1, 6):
    lines.append(f"{object_offsets[number]:010d} 00000 n \n".encode())
new_xref_start = len(prefix)
repaired_bytes = prefix + b"".join(lines) + trailer
# Replace the stale startxref value with the new xref offset.
repaired_bytes = re.sub(rb"startxref\n\d+\n", f"startxref\n{new_xref_start}\n".encode(), repaired_bytes)
repaired.write_bytes(repaired_bytes)

repaired_reader = PdfReader(repaired, strict=True)
result = {
    "source": source.name,
    "corrupt": corrupt.name,
    "repaired": repaired.name,
    "corrupt_sha256": hashlib.sha256(corrupt_bytes).hexdigest(),
    "repaired_sha256": hashlib.sha256(repaired_bytes).hexdigest(),
    "parser_recovery": recovery,
    "independent_object_offsets": object_offsets,
    "repaired_pages": len(repaired_reader.pages),
    "repaired_text": repaired_reader.pages[0].extract_text().strip(),
    "strict_reopen": True,
    "status": "OBSERVED_AND_VERIFIED_FOR_THIS_FIXTURE",
    "limits": [
        "The exercise uses a five-object teaching file and does not represent all cross-reference streams, hybrid-reference files, incremental updates, encryption, or damaged stream recovery.",
        "A parser's ability to recover malformed xref data is not proof that the source file is valid or safely repaired.",
        "A rebuilt xref does not validate the document's semantics, accessibility, rendering, print, archive, or security properties."
    ]
}
result_path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
