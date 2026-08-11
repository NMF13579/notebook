---
title: AOS Lean Portable Documentation Package Design
date: 2026-08-09
status: DESIGN_APPROVED_PENDING_WRITTEN_REVIEW
authority: DOCUMENTATION_DESIGN_ONLY
source_candidate: sha256:57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65
source_audit: sha256:b6cd639302fb719ab7ef47e894075c791d683c3e46b35291c11a2c591f989cfe
source_acceptance: sha256:0353347d106d1985e7b296f721ade4b9e51a1a26a304468b97dc39b00c7598df
frozen_foundation: sha256:b9ef04820f9e71da1866c61c87417c7ac39d1c27c93a74327ab7f40f2e25aebf
source_commit: 73716e65d6bb4512c58fefbced53d407cec57bca
target_root: AOS/portable
implementation_authorization: NONE
git_authorization: NONE
---

# AOS Lean Portable Documentation Package Design

## 1. Outcome

Create one self-contained documentation handoff for future AOS implementation work. The package must be convenient for a human or coding agent to read without access to this knowledge repository, while preserving accepted facts, visible proposals and unresolved decisions.

The package is documentation, not runtime implementation, an implementation repository binding or Git authorization.

## 2. Target layout

```text
AOS/portable/
├── AGENTS.md
├── README.md
├── 00_PROJECT_CORE.md
├── 01_PRODUCT_MODEL.md
├── 02_ARCHITECTURE_CONTRACTS.md
├── 03_ENGINEERING_WORKFLOW.md
├── 04_FEATURE_SPECIFICATIONS.md
├── 05_USER_JOURNEYS_AND_UX.md
├── 06_PROJECT_ROADMAP.md
├── 07_DECISION_REGISTER.md
├── 08_TRACEABILITY.md
├── MANIFEST.txt
└── PACKAGE_ACCEPTANCE.yaml
```

The manifest-bound candidate contains exactly eleven Markdown content files: `AGENTS.md`, `README.md` and `00…08`. `MANIFEST.txt` binds those files and excludes itself. `PACKAGE_ACCEPTANCE.yaml` is created only after audit and human acceptance; it binds the manifest identity and is excluded from the manifest to avoid recursion.

## 3. File responsibilities

- `AGENTS.md` is a thin package-local router: reading order, authority boundaries, open-decision handling and prohibition on inferring implementation or Git permission.
- `README.md` explains purpose, status, inventory, reading paths, portability and the package identity model.
- `00_PROJECT_CORE.md` owns package-level identity, vocabulary, source precedence and safety semantics.
- `01_PRODUCT_MODEL.md` describes product problems, users, requirements, capabilities and success model.
- `02_ARCHITECTURE_CONTRACTS.md` describes WHAT-level layers, contracts, ownership, trust and recovery boundaries.
- `03_ENGINEERING_WORKFLOW.md` describes future planning, execution, validation, review, recovery and delivery semantics.
- `04_FEATURE_SPECIFICATIONS.md` contains design-level specifications for `FTR-001…FTR-030` and preserves item dispositions.
- `05_USER_JOURNEYS_AND_UX.md` contains interface-neutral journeys and UX requirements.
- `06_PROJECT_ROADMAP.md` contains proposed phase order, gates and dependency timing without activating phases.
- `07_DECISION_REGISTER.md` separates accepted decisions, current safe states and open human-only choices.
- `08_TRACEABILITY.md` contains the live problem-to-decision graph and package coverage, without construction-history ceremony.
- `MANIFEST.txt` provides deterministic raw-byte identity.
- `PACKAGE_ACCEPTANCE.yaml` records the later exact human package decision.

## 4. Source and harmonization rules

The accepted DRAFT-R2 package is the primary content source. The current frozen three-file Global Design Package remains an upstream accepted foundation and must not be modified by this work.

Portable authoring is a harmonization, not a byte-for-byte copy:

1. Preserve accepted fact classes and explicit classifications from DRAFT-R2.
2. Reconcile overlapping Product, Architecture and Workflow content with the frozen foundation without changing its files.
3. Replace links to `../../docs`, `../../AOS`, X1 workspace records and audit paths with package-internal navigation or concise embedded provenance metadata.
4. Remove R1/R2 construction narrative, correction history and reviewer workflow from operational content.
5. Preserve open decisions, `UNKNOWN`, `NOT_RUN`, feature dispositions and authority exclusions.
6. Do not introduce implementation HOW, repository choice, toolchain selection, runtime claims or new feature scope.

## 5. Portability and ownership

The package must remain understandable after copying `AOS/portable/` alone. No required relative link may escape the package root. Historical sources may be named by repository identity and SHA-256, but they are provenance rather than runtime dependencies.

Within the portable package, each fact class has one clear owner. `README.md`, `AGENTS.md`, `08_TRACEABILITY.md` and `MANIFEST.txt` are navigation or identity artifacts and do not duplicate Product, Architecture, Feature or Workflow ownership.

## 6. Identity and acceptance

Candidate identity is SHA-256 of exact `MANIFEST.txt` bytes. Manifest records use UTF-8 bytewise path order, lowercase SHA-256, exact byte count and one LF per record.

Any byte change to a manifest-bound file creates a new candidate identity and invalidates prior audit evidence for the old candidate.

`PACKAGE_ACCEPTANCE.yaml` is created after a separate audit and explicit human decision. It records the candidate manifest identity, audit evidence identity, accepted fact classes and exclusions. It does not grant implementation, Git, deployment or release authority.

## 7. Minimal workflow

```text
one bounded harmonization pass
→ focused construction checks
→ one independent read-only package audit
→ one package-level human decision
→ optional separately authorized commit
```

Do not repeat per-document human review unless audit findings or authoring changes introduce a material product or architecture choice. Non-material packaging defects may use one bounded correction followed by a full re-audit of the new candidate.

## 8. Validation

Construction checks must verify:

- exact expected inventory and no unexpected file types or symlinks;
- UTF-8, final LF, balanced Markdown fences and parseable YAML where applicable;
- all package-relative links resolve and no required link escapes `AOS/portable/`;
- exactly 30 feature identities and preserved dispositions;
- complete `C-001…C-014`, journey, roadmap and decision-route coverage;
- no duplicated fact ownership or unclassified material claim;
- no implementation/Git authority grant and no prescribed reversible HOW;
- deterministic manifest records and reproducible candidate identity;
- current frozen `AOS/` foundation, canonical `docs/` and accepted workspace evidence remain unchanged.

The independent audit is read-only relative to the candidate and does not correct it or create human acceptance.

## 9. Failure handling

- Relevant source drift before candidate binding requires re-harmonizing only the affected boundary.
- A material source conflict, new product scope or architecture choice stops the affected route for human decision.
- A broken external dependency is corrected by making the package self-contained, not by copying the entire knowledge repository.
- An audit finding produces a separate bounded correction and a new manifest identity.
- The existing frozen three-file package is never silently reopened, overwritten or reclassified.

## 10. Exclusions

The portable package does not include:

- DRAFT-R1 or DRAFT-R2 workspace directories;
- completeness audit reports or construction logs;
- Program Controllers, lifecycle state files or correction history;
- canonical `docs/` copies;
- X1 working-package files;
- runtime code, tests, dependencies, CI/CD or deployment configuration.

These remain available in the knowledge repository as provenance when needed.

## 11. Completion criteria

The design is implemented when one exact portable candidate exists at `AOS/portable/`, all construction checks pass, a separate audit has no material finding, and the human issues one exact package-level decision. The frozen Global Design foundation remains byte-identical, and implementation and Git authority remain absent unless separately granted.

The next task after written-design approval is a bounded documentation implementation plan for creating this package. It must not begin runtime implementation or mutate the current frozen three-file subject.
