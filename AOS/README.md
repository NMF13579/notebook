# AOS Global Design Deliverable

`AOS/` contains the current human-selected Global Design Package:

- `01_PRODUCT_MODEL.md` — product goals, boundaries, actors, journeys and feature scope;
- `02_ARCHITECTURE_CONTRACTS.md` — architecture, ownership, state and contract semantics;
- `03_ENGINEERING_PIPELINE.md` — engineering workflow, evidence, recovery and handoff semantics without implementation HOW.

`docs/03_Development.md` is the sole canonical owner of the documentation lifecycle. `workspace/` contains source synthesis, drafts and superseded working artifacts; presence in `workspace/` does not create authority.

Exact review, acceptance provenance and Freeze identity are recorded in:

- `reviews/GLOBAL_DESIGN_PACKAGE_REVIEW.md`;
- `decisions/GLOBAL_DESIGN_PACKAGE_ACCEPTANCE.md`;
- `GLOBAL_DESIGN_FREEZE.md`.

Freeze does not grant implementation authorization or permission for Commit, Push, Merge or Release. A content change to the package requires explicit Reopen, review of a new exact candidate and a new Freeze identity.
