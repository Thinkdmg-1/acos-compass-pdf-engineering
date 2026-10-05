# XMP-only / shared-profile dual-profile boundary variant

This controlled variant continues the header-20 dual-profile specimen. It removes the PDF/X identification keys from the document information dictionary, retains only ModDate, adds a catalog PieceInfo record, and byte-patches the second output intent so both output intents reference the same ICC profile indirect object. This is an experiment, not a production recipe.

## Results

- veraPDF 1.30.2 PDF/A-4: **pass**, 0 failed rules and 0 failed checks.
- veraPDF 1.30.2 PDF/UA-2: **pass**, 0 failed rules and 0 failed checks.
- veraPDF 1.28.2 PDF/UA-2: **pass**, 0 failed rules and 0 failed checks.
- Independent pypdf check: one page before/after; extracted-text SHA-256 identical (141d3b01923d9daa3b78ff0985fe683048ada2af9e3040d801fe01455593711e); StructTreeRoot retained; two output intents retained; header is PDF-2.0.
- Independent Poppler raster check at 144 DPI: source and variant PNG SHA-256 identical (c64d0955a0d3818fc6ebaaf6a93052dc0dd81cafa2a8a34267e6722c8bb1448b).
- Rust PDF Oxide probe: not compliant. It detects X6 but reports three errors: missing GTS_PDFXVersion in Info and unembedded fonts F4/F5. It also reports missing Trapped and a link annotation appearance warning.

## Interpretation

This is the strongest bounded machine result so far: the same controlled specimen passes the two pinned veraPDF profile checks for PDF/A-4 and PDF/UA-2 while preserving structure, text, and raster output. It does not establish PDF/X-6 conformance. No authorized ISO 15930-9 clause map, independent PDF/X-6 preflight, human accessibility review, or production-export evidence is present. The artifact remains a research boundary experiment and must not be released as a three-profile conforming PDF.

Receipts are retained in the local report directory.

## Font-probe boundary

Independent pypdf object inspection finds FontFile2 streams in both Type 0 fonts' CIDFont descendant FontDescriptor dictionaries. The Rust probe nevertheless reports F4 and F5 as unembedded. This narrows the remaining PDF/X-6 result to an implementation-resolution mismatch rather than evidence that the font programs are absent. It does not override the need for an accepted PDF/X-6 preflight or normative clause review.
