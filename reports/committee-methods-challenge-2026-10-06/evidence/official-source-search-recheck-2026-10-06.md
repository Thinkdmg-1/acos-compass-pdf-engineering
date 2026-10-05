# Official standards access search recheck — 2026-10-06

**Status:** ACCESS PATH CONFIRMED / NORMATIVE BYTES NOT CUSTODIED

This public-source recheck tested whether the missing authorized PDF/UA, PDF/A, and PDF/X-6 normative text could be recovered from current official PDF Association pages without accepting a vendor checkout, account flow, or license terms.

Sources inspected:

- PDF Association, [ISO 14289-2 — PDF/UA-2](https://pdfa.org/iso-14289-2-pdfua-2/)
- PDF Association, [Sponsored ISO standards for PDF technology](https://pdfa.org/sponsored-standards/)
- PDF Association, [PDF/UA bundle product page](https://www.pdfa-inc.org/product/pdf-ua-bundle/)
- PDF Association, [ISO 19005 resource page](https://pdfa.org/resource/iso-19005-pdfa)
- PDF Association, [ISO 15930 resource page](https://pdfa.org/resource/iso-15930-pdfx/)

The official pages state that the PDF/UA bundle is available at no cost and identify ISO 14289-2:2024, ISO 14289-1:2014, and ISO TS 32005 as its contents. The product page exposes a $0.00 item and an Add to cart action, but the public HTML does not expose the normative PDF bytes. Direct shell retrieval of the product page returned HTTP 403 in this environment.

This strengthens source availability evidence but does not satisfy authorized normative-text custody or clause-by-clause mappings. No account was created, no checkout was accepted, no vendor EULA was accepted, and no ISO conformance claim was added.
