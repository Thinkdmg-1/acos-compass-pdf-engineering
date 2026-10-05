# Independent user-facing checks for the PDF/UA machine-pass copy

A separate pypdf and Poppler path compared the original tagged fixture with the final machine-pass copy. It checked page count, MediaBox, extracted-text digest and length, catalog keys, and a 144 DPI first-page raster digest. The complete receipt is in results.json.

These checks establish whether the bounded repair changed tested geometry, extracted text, or tested raster output. They do not establish screen-reader behavior, keyboard focus, visual acceptability, or standards conformance beyond the recorded validator result.
