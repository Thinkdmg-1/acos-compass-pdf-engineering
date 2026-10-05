# Independent check of fresh veraPDF reports — 2026-10-06

**Status:** `PASS / INDEPENDENT CHECK`

[`check.py`](check.py) is a separate parser and assertion path from the report-generation shell command. It reopened each fresh JSON report, recomputed the four compliance/count tuples, recomputed both fixture SHA-256 digests, and searched the saved profile inventory for PDF/A-4, PDF/UA-2, and the absence of PDF/X-6. The machine-readable receipt is [`results.json`](results.json).

The check passed. It verifies report integrity and claim-to-output alignment. It does not independently validate the ISO requirements, replace a PDF/X-6 engine, or perform human accessibility testing.
