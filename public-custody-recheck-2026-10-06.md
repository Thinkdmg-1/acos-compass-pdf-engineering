# Public evidence custody recheck — 2026-10-06

The public GitHub repository was checked through the GitHub Contents API and raw-file endpoint.

- Boundary report commit: b9c0289
- Font-inspection receipt commit: 7f19b74
- Boundary report raw endpoint: HTTP 200; 2,273 bytes; SHA-256 484254890d3f8c36b0eeff482829c21ec8a25fc60aa5bfb0f3909ce67768c71d
- Font receipt raw endpoint: HTTP 200

The font receipt records descendant FontFile2 streams for F4 and F5. The Rust PDF/X-6 implementation probe reports those fonts as unembedded. This remains an implementation-resolution conflict, not proof that the font programs are absent and not an ISO PDF/X-6 conformance claim.
