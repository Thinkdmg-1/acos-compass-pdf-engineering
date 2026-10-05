# PDF 2.0 examples lab — 2026-10-06

**Purpose:** inspect a public set of deliberately small PDF 2.0 examples with two independent readers. This exercises version headers, incremental updates, non-zero file offsets, UTF-8 strings, output intents, and structure trees without confusing examples with a conformance test suite.

## Pinned input

- Repository: <https://github.com/pdf-association/pdf20examples>
- Local checkout: `work/pdf20examples-20261006/repo`
- Commit: `c20f2c17bfcc4baab7cfe62e70fae64caf14d5fa`
- Commit date: `2025-01-13T12:27:20+11:00`

## Independent method

1. A fresh pypdf 6.10.0 process opened every PDF, recorded file hash, page count, header, catalog keys, metadata, output intents, and structure-tree presence.
2. Poppler `pdfinfo` independently checked page count, PDF version, page geometry, tagged status, encryption, and metadata.
3. Warnings from either reader were retained rather than treated as failures or silently repaired.

## Receipt

| Example | pypdf observation | Poppler observation |
|---|---|---|
| PDF 2.0 UTF-8 string and annotation | `%PDF-2.0`, 1 page, metadata stream | PDF 2.0, 1 page, untagged |
| PDF 2.0 image with BPC | `%PDF-2.0`, 1 page, metadata stream | PDF 2.0, 1 page, untagged |
| PDF 2.0 via incremental save | `%PDF-1.7` header with catalog `/Version`; parser warned about xref recovery | Poppler reports PDF 2.0, 1 page |
| PDF 2.0 with offset start | nonstandard leading bytes before PDF data; pypdf reports invalid header and xref warning but opens 1 page | Poppler reports PDF 2.0, 1 page |
| PDF 2.0 with page level output intent | `%PDF-2.0`, 2 pages, document output intents | PDF 2.0, 2 pages |
| Simple PDF 2.0 file | `%PDF-2.0`, 1 page, metadata stream | PDF 2.0, 1 page |
| pdf20-utf8-test | `%PDF-2.0`, `/Lang`, `/MarkInfo`, `/StructTreeRoot`, outlines and optional content | PDF 2.0, tagged, 1 page |

All seven examples opened and rendered through both readers. The two intentionally unusual files demonstrate why a single header check is insufficient: the incremental-save example carries PDF 2.0 in the catalog version, and the offset-start example has non-PDF bytes before the PDF data.

## Boundary

The repository describes these as educational examples and explicitly says they are not a comprehensive assessment of UTF-8 support or every PDF 2.0 conforming file. This lab therefore proves reader interoperability observations only. It does not establish ISO 32000-2 conformance, PDF/A, PDF/UA, PDF/X, or production suitability.
