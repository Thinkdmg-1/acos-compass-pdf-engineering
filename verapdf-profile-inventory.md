# veraPDF 1.30.2 profile inventory

**Run date:** 2026-10-05  
**Executable:** `veraPDF 1.30.2`, built 2026-06-03  
**Command:** `JAVA_HOME=<pinned JDK> verapdf --list`

The pinned CLI reports these profiles:

- PDF/A-1a, 1b
- PDF/A-2a, 2b, 2u
- PDF/A-3a, 3b, 3u
- PDF/A-4, 4f, 4e
- PDF/UA-1
- PDF/UA-2 plus Tagged PDF
- WTPDF 1.0 Reuse and WTPDF 1.0 Accessibility

It does **not** list a PDF/X-6 profile. This is a validator-capability boundary, not evidence that PDF/X-6 is optional or that the PDF/X-6 claim has been tested. PFE 613 therefore requires a separate PDF/X-capable preflight path and must keep the PDF/X-6 claim unresolved until that path, the current ISO 15930-9:2020 requirements, and a declared production fixture are available.

The output is preserved to keep the distinction between “the selected validator can test this profile” and “the curriculum requirement has been satisfied.” The profile inventory supplements the raw validation reports; it does not replace normative PDF/X-6 text or a preflight result.
