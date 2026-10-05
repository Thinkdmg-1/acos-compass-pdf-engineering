# Source-quality gate: 995/1000

## Purpose

The information used to teach or govern PDF engineering must be strong enough to survive hostile review. “A link exists” is not evidence. A bibliography entry, abstract, search result, vendor summary, or model recollection cannot satisfy the gate by itself.

The repository adopts a 1,000-point internal gate. The score is a release decision for the source set, not a claim that any source is infallible and not a substitute for professional accreditation.

## Frozen rubric

| Factor | Points | Passing evidence |
|---|---:|---|
| Authority and provenance | 180 | Controlling standards body, original research authors, or official university teaching source; author, institution, edition, and origin recorded |
| Directness to the claim | 170 | The source directly supports the specific curriculum statement, rather than a summary or adjacent topic |
| Technical completeness | 150 | Relevant definitions, assumptions, methods, exceptions, and boundary conditions are available for inspection |
| Currency and version control | 120 | Edition, publication date, errata, supersession status, and access date are recorded |
| Reproducibility | 120 | Data, algorithm, assignment, formal requirement, or test procedure can be followed by another learner |
| Independent corroboration | 100 | Important claims are checked against a second authoritative source or independent implementation |
| Scope and transfer limits | 80 | The source states where its conclusion applies and where it does not |
| Accessibility and recoverability | 40 | The material is inspectable, citable, and recoverable by a future learner |
| Evidence integrity | 40 | No unsupported paraphrase, fabricated quotation, hidden failure, or silent source substitution |
| **Total** | **1,000** | **995 target; any hard veto blocks release** |

## Hard vetoes

The source set cannot pass at 995 if any of these remain unresolved:

- a normative requirement is supported only by an informal article;
- a current standard is represented by a superseded edition without a version note;
- a material claim is based only on a search result, abstract, or generated summary;
- a source is inaccessible and no preserved extract or alternate authoritative source exists;
- an apparent conflict between sources is hidden instead of recorded;
- the curriculum claims a validator, university, publisher, or standards body said something it did not say;
- a local experiment is presented as a universal rule;
- the source register has not been independently checked.

## Scoring procedure

1. Freeze the curriculum claim inventory.
2. Assign every claim a source ID and evidence class: `NORMATIVE`, `PRIMARY_RESEARCH`, `UNIVERSITY_TEACHING`, `VALIDATOR_SCOPE`, `LOCAL_EXPERIMENT`, or `PROPOSED_RULE`.
3. Inspect the actual source and record edition, date, scope, and relevant location.
4. Score each factor with a short evidence note. Unknown receives zero for that factor; it is not inferred from reputation.
5. Run an independent source challenge that checks authority, version, directness, and conflict handling.
6. Apply hard vetoes before adding points.
7. Publish the score, missing evidence, dissent, and release state.

## Current disposition

**Target:** 995/1000.  
**Current state:** `CHANGES_REQUIRED`; the conservative provisional scorecard is 788/1000 and is not a release score.  
**Reason:** the curriculum source spine is strong, the public identity/status and validator evidence has been independently challenged, but complete authorized normative text and clause-by-clause mappings are still missing. The repository must not call the source set 995 until those mappings and the remaining human/production checks are complete.

This disposition is deliberate. It preserves the distinction between an ambitious curriculum and a completed source gate.
