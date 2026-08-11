---
package: AOS_LEAN_PORTABLE_DOCUMENTATION
package_revision: PORTABLE-DRAFT-1
artifact_role: PACKAGE_LOCAL_ROUTER
status: DRAFT
authority: NONE
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# AGENTS — Portable AOS Documentation Router

## 1. Purpose

This directory is a self-contained documentation candidate for future AOS implementation planning. It describes product intent, architecture contracts, feature behavior, user journeys, workflow, roadmap proposals, decisions and traceability.

It is not runtime code, an implementation repository, an Execution Authorization or Git permission.

## 2. Reading routes

Start with [README.md](README.md), then read only the owners needed for the current question:

| Question | Owner |
|---|---|
| identity, vocabulary, precedence, safety | [00_PROJECT_CORE.md](00_PROJECT_CORE.md) |
| product problems, users, requirements, capabilities | [01_PRODUCT_MODEL.md](01_PRODUCT_MODEL.md) |
| layers, contracts, ownership, trust, recovery | [02_ARCHITECTURE_CONTRACTS.md](02_ARCHITECTURE_CONTRACTS.md) |
| planning, execution, validation, review, recovery, delivery | [03_ENGINEERING_WORKFLOW.md](03_ENGINEERING_WORKFLOW.md) |
| feature-specific behavior and disposition | [04_FEATURE_SPECIFICATIONS.md](04_FEATURE_SPECIFICATIONS.md) |
| journeys and interface-neutral UX | [05_USER_JOURNEYS_AND_UX.md](05_USER_JOURNEYS_AND_UX.md) |
| proposed order, gates and timing | [06_PROJECT_ROADMAP.md](06_PROJECT_ROADMAP.md) |
| accepted decisions, safe states, open choices | [07_DECISION_REGISTER.md](07_DECISION_REGISTER.md) |
| coverage and cross-document navigation | [08_TRACEABILITY.md](08_TRACEABILITY.md) |

## 3. Ownership

Each fact class has one package-local owner. `README.md`, this file and `08_TRACEABILITY.md` route or derive facts; they do not replace Product, Architecture, Workflow or Feature owners.

When statements appear to conflict:

1. current explicit human decision bound to an exact subject;
2. accepted fact in its declared class;
3. current direct observation for mutable facts;
4. visibly classified proposal;
5. inference.

Do not silently resolve a material conflict. Record the affected claim and request a human decision.

## 4. Status and authority

The manifest-bound portable package remains a `DRAFT` with `authority: NONE` until a separate audit and exact human package decision. Source acceptance does not automatically accept changed portable bytes.

Keep these axes separate:

```text
technical result != human decision
documentation acceptance != implementation authorization
Edit != Commit != Push != Merge != Release
UNKNOWN != OK
NOT_RUN != PASS
```

Recommendations and roadmap placements never mutate a feature disposition or select an open option. Only a human may choose an option in [07_DECISION_REGISTER.md](07_DECISION_REGISTER.md).

## 5. Documentation edit boundary

For an authorized documentation change:

1. bind the exact candidate and writable paths;
2. read the relevant owner;
3. preserve accepted/proposal/unknown classifications;
4. update affected internal links and traceability;
5. run focused checks;
6. bind new bytes in [MANIFEST.txt](MANIFEST.txt);
7. stop before independent validation or Git action unless separately instructed.

Any byte change to a manifest-bound Markdown file creates a new candidate identity and invalidates audit evidence for the previous identity.

## 6. Validation boundary

An independent audit is read-only relative to the candidate. It reproduces manifest records, checks structure and semantic completeness, records limitations and reports `PASS | FAIL | BLOCKED | UNKNOWN`. It does not correct the candidate or create human approval.

## 7. Runtime and Git boundaries

Do not infer or create runtime code, scaffolding, dependencies, tests, CI/CD, deployment, database or implementation repository from this package. Future implementation HOW remains with a separately authorized coding task after material human decisions are resolved.

Commit, Push, Merge and Release each require their own explicit authorization and exact subject.
