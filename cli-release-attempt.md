# PDF Oxide CLI release attempt — 2026-10-06

**Status:** EXECUTED / CLI SCOPE LIMIT

A disposable macOS x86_64 PDF Oxide 0.3.78 release archive was downloaded to `/tmp` from the project's GitHub release and verified before execution:

- Archive: `pdf_oxide-macos-x86_64-0.3.78.tar.gz`
- Archive SHA-256: `8fde97f0bc02c205ae02af04b8e4639e26bebfd3739ea0ac6da8a87756643303`
- Executable: `pdf-oxide`, Mach-O x86_64
- Executable SHA-256: `c5517bf6f11db0c20de698498e50da242e36bcf0437b0dac4f7952cd2236f144`
- Version output: `pdf-oxide 0.3.78`

The executable was run with `--help`. Its command surface includes text, classify, metadata, render, and other document operations, but it exposes no `validate` or PDF/X compliance command. The binary therefore cannot execute the documented library-level `PdfXLevel::X6` request as a CLI operation. The archive was used only from `/tmp`; no system installation or repository dependency was changed.

This is additional capability evidence, not a PDF/X-6 conformance result. The release has a runnable executable, but the available CLI surface does not expose the required validation path. The Python binding rejection, Rust-source declaration, absent host Rust toolchain, and this CLI scope limit remain distinct records.
