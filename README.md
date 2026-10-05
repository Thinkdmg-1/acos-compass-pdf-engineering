# veraPDF runtime capability receipt — 2026-10-06

**Purpose:** distinguish preserved veraPDF reports from the current host's ability to execute a fresh validator run.

## Method

The pinned launcher at `work/verapdf-1.30.2/install/verapdf` was invoked with `--list-profiles` in a fresh shell. The launcher was present and executable, but it could not locate a Java Runtime Environment and exited before listing profiles or validating a file.

Observed diagnostic:

```text
The operation couldn’t be completed. Unable to locate a Java Runtime.
Please visit http://www.java.com for information about installing Java.
```

## Interpretation

This is a current host-capability boundary, not a PDF result. It does not invalidate the preserved veraPDF 1.30.2 reports already committed under `reports/verapdf-1.30.2/` and `reports/production-pdfa4-2026-10-05/`; those reports remain historical evidence with their recorded commands, profiles, fixtures, and outputs. It does mean that no new validation run or profile inventory can honestly be claimed from this host until a compatible Java runtime is available.

The absence of a Java runtime does not establish PDF/A, PDF/UA, or PDF/X pass/fail. The current release interpretation remains `CHANGES_REQUIRED`.
