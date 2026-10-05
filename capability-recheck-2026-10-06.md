# PDF production and human-review capability recheck — 2026-10-06

## Purpose

Recheck the host capabilities that are required for the unresolved production PDF/X-6 preflight and human PDF/UA review gates. This is a capability receipt, not a conformance result.

## Method and custody

The executable lookup was run in the repository worktree on 2026-10-05 at 17:23:03 UTC. The raw shell receipt was saved temporarily as /tmp/pdf-capability-recheck-20261006.txt and has SHA-256 efc39a676e3d648ef2ae22826bdd613189e14f4a666f1a7446539a13745e82b1.

## Result

| Capability | State | Evidence |
|---|---|---|
| veraPDF command on PATH | unavailable | Installed disposable launchers exist under /tmp, but no PATH command is present. |
| qpdf, MuPDF, Ghostscript, pdfcpu, cpdf | unavailable | No executable was found. |
| Poppler text/font tools | unavailable | pdftotext and pdffonts were not found. |
| PDF metadata inspection | available | Bundled pdfinfo is available. |
| PDF/X-6 preflight | unavailable | No installed engine with an explicitly verified ISO 15930-9:2020 PDF/X-6 profile was found. |
| Screen-reader command tools | unavailable | VoiceOver, NVDA, Orca, and JAWS command names were not found. |
| Existing disposable validator evidence | available | veraPDF 1.30.2, veraPDF 1.28.2, and the patched PDF Oxide probe remain available under /tmp; their hashes are retained in the raw receipt. |

## Interpretation

This recheck confirms the environment can support bounded machine checks through the preserved disposable runtimes, but it cannot execute an independent production PDF/X-6 preflight or a real screen-reader review. The absence of a command-line screen-reader name is not proof that no graphical accessibility tool exists; it is a bounded shell capability check. The human-review gate therefore remains open, and no PDF/X-6 production claim is made.
