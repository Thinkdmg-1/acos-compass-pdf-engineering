# Arlington object-model lab — 2026-10-06

**Purpose:** exercise a public, specification-derived machine-readable PDF object model against the repaired PDF/A-4 teaching fixture. This is object-model evidence, not an ISO conformance claim.

## Pinned input

- Repository: <https://github.com/pdf-association/arlington-pdf-model>
- Local checkout: `work/arlington-pdf-model-20261006/repo`
- Commit: `c48b363e9b78902deea03e958693c09339248a3a`
- Commit date: `2026-09-17T10:09:59+10:00`
- Latest TSV files inspected: 613
- Fixture: `reports/production-pdfa4-2026-10-05/fixture-repaired2.pdf`
- Fixture SHA-256: `c027477c49ffbb7f055a3c7ed37a804ef3423c3d6c1a0ad4faaa5f1a916f8c73`

## Method

1. Read `tsv/latest/Catalog.tsv` with a fresh Python process and extracted rows whose `Required` field is `TRUE`.
2. Parsed the fixture catalog with pypdf 6.10.0 and compared the observed catalog keys with the model's required-key set.
3. Checked the fixture catalog independently for `/StructTreeRoot` and recorded its presence or absence.
4. Preserved the model's own limitation: the Arlington documentation says it is specification-derived, does not replace ISO 32000-2, and does not define content streams or file-structure/layout rules.

## Receipt

```json
{
  "model_commit": "c48b363e9b78902deea03e958693c09339248a3a",
  "model_tsv_files": 613,
  "catalog_required_keys": ["Type", "Pages"],
  "catalog_observed_keys": ["Metadata", "OutputIntents", "Pages", "Type"],
  "missing_required_keys": [],
  "struct_tree_present": false,
  "fixture_pages": 1,
  "fixture_sha256": "c027477c49ffbb7f055a3c7ed37a804ef3423c3d6c1a0ad4faaa5f1a916f8c73"
}
```

## Interpretation

The fixture satisfies the Arlington model's two required catalog keys observed in this bounded comparison, while the independent parser confirms that no structure tree is present. This supports the existing PDF/UA limitation and provides a reproducible object-model exercise. It does not prove PDF 2.0, PDF/A-4, or PDF/UA-2 conformance because the model is not the complete normative text and this check excludes content streams, file structure, profile-specific requirements, and human accessibility review.
