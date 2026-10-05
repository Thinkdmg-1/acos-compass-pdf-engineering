# Committee-style methods challenge rehearsal — 2026-10-06

**Protocol:** PFE-ORAL-2026-10-06-v1  
**Status:** REHEARSAL / NOT AN EXTERNAL COMMITTEE REVIEW

This bounded rehearsal uses eight adversarial lenses. The roles are challenge lenses, not named people or fabricated approvals.

| Lens | Question | Disposition |
|---|---|---|
| Standards chair | Which statements are ISO requirements versus implementation observations? | No ISO conformance claim is released without authorized text and clause maps. PASS WITH LIMIT. |
| Methods chair | Does a PDF/UA-2 machine pass generalize to production PDFs? | No; the result is fixture-scoped and excludes production and human claims. PASS WITH LIMIT. |
| Typography chair | Does HarfBuzz shaping prove PDF semantic correctness? | No; shaping, ToUnicode, structure, and accessibility are separate layers. PASS WITH LIMIT. |
| Pagination chair | Does held-out agreement prove an optimal production paginator? | No; it covers only the bounded contiguous-block objective. PASS WITH LIMIT. |
| Production chair | Does the Rust PDF/X-6 probe prove conformance? | No; it is an implementation diagnostic, not an accepted preflight or normative authority. PASS WITH LIMIT. |
| Accessibility chair | Does veraPDF replace human accessibility testing? | No; screen-reader, keyboard, high-contrast, and second-reviewer checks remain open. PASS WITH LIMIT. |
| Reproducibility chair | Are these copied assertions? | Separate checkers, hashes, held-out fixtures, and pinned runtimes exist; external rerun remains missing. PASS WITH LIMIT. |
| Governance chair | Why is the score below 995? | Hard vetoes cannot be compensated for by local experiments. PASS WITH LIMIT. |

This cannot substitute for an external committee or second human reviewer. Score: 796/1000, CHANGES_REQUIRED. No points are added; do not treat this as a qualifying pass or production release.
