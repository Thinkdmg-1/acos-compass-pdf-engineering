# PFE 601 rerun receipt — 2026-10-06

**Purpose:** independently rerun the local object-model and cross-reference-repair labs from source, preserving the current execution result separately from the original lab receipts.

## Method

Using the bundled Python runtime, executed:

- `labs/pfe601_object_model_lab.py`
- `labs/pfe601_xref_repair_lab.py`

The rerun recreated the teaching PDFs and rewrote their JSON receipts. The xref result was then reopened with pypdf in strict mode.

## Receipt

```json
{
  "object_lab_status": "OBSERVED_AND_VERIFIED_FOR_THIS_FIXTURE",
  "xref_lab_status": "OBSERVED_AND_VERIFIED_FOR_THIS_FIXTURE",
  "parser_recovered_corrupt_fixture": true,
  "strict_reopen_repaired_fixture": true,
  "repaired_pages": 1
}
```

## Boundary

This confirms source-level reproducibility for the five-object teaching fixture. It does not generalize to cross-reference streams, hybrid references, incremental-update chains, encryption, malformed content streams, or production PDF validity. The current entry diagnostic and Year 1 gate remain limited.
