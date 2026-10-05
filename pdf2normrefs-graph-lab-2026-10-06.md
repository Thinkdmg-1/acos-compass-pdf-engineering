# PDF 2.0 normative-reference graph lab — 2026-10-06

**Purpose:** exercise dependency-graph reasoning for the PDF 2.0 curriculum using the PDF Association's public normative-reference dataset. This is source-custody and research-method evidence, not a replacement for any ISO standard.

## Pinned input

- Repository: <https://github.com/pdf-association/PDF2NormRefs>
- Local checkout: `work/pdf2normrefs-20261006/repo`
- Commit: `1f66edd831870c4e2481a576e2a32e200929b042`
- Dataset: `data/referencesGraph.json`
- Dataset SHA-256: `981f6367122d8a1344267301097a601730b93f4b8088337545c46dc3468ba8b7`

## Method

A fresh Python process parsed the JSON graph, asserted that the root document has ID `0`, traversed all `refs` edges from the root, checked that every target ID exists, compared reverse `referencedBy` edges, and counted statuses and reachable levels.

## Receipt

```json
{
  "records": 1173,
  "root_title": "Document management - Portable Document Format - Part 2: PDF 2.0",
  "root_refs": 79,
  "edges": 2572,
  "missing_ref_targets": 0,
  "back_reference_mismatches": 2,
  "reachable_from_root": 1173,
  "max_reachable_level": 6,
  "status_counts": {
    "active": 976,
    "in development": 5,
    "update": 57,
    "obsolete": 128,
    "not available": 1,
    "withdrawn": 6
  }
}
```

The two reverse-edge mismatches are retained as observed dataset warnings rather than silently repaired. They involve record `361` and targets `19` and `454`; the source repository's annotations remain authoritative for the dataset as published.

## Interpretation

The graph is internally traversable from PDF 2.0 to all 1,173 records, with no dangling reference targets and a maximum reachable depth of six. The dataset exposes a nontrivial dependency surface and status mix that must be considered when building a doctoral source map. It does not grant access to the underlying standards, prove that every reference is current, or establish any PDF profile conformance result.
