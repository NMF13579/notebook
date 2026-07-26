---
document_id: 04_Lessons
title: "Lessons"
status: draft
authority: supporting
human_review_required: true
version: 4.0
updated: 2026-07-26
repository_snapshot: "NMF13579/AgentOS dev@e3a60a92fbd5e78e583cddb519d39527583f3433 (2026-06-05)"
repository_commands_tests_build: NOT_RUN
---

# Lessons

## Catalog audit summary

The previous package was not suitable as a decision or implementation baseline because it mixed assistant proposals, historical notes and repository presence; lacked complete status/provenance separation; and spread the catalog across more files than requested.

This corrected edition keeps exactly seven documents. The source material and substantive findings are retained, while audit/source/conflict material is consolidated into `04_Lessons.md` and `05_Reference.md`.

Key audit rule: **an assistant suggestion is not `DECIDED`; a repository file is not runtime proof; a stored PASS is not current PASS.**

## Errors and extracted lessons

This file records significant project, lifecycle, quality, safety, and maintainability failures. It does not list every coding defect.


## E-01. Exhaustive extraction produced low-value complexity

- **What happened:** The project tried to create a complete reconstruction base with claims, evidence packages, schemas, and exhaustive provenance.
- **Cause:** The extraction goal was broader than the immediate design decisions and user needs.
- **Consequences:** High time cost, opaque output, user fatigue, and weak implementation usefulness.
- **Correction:** Move to a compact catalog of product intent, schemes, features, errors, and references; research details on demand.
- **Lesson:** Documentation must reduce the next design decision, not maximize artifact count.
- **Repeat risk:** Medium if extraction scope is not bounded.
- **Status:** DECIDED lesson.
- **Sources:** CH-05, CH-06, CH-10, CH-11.

## E-02. Assistant proposal was treated as a project decision

- **What happened:** Prior synthesis labelled some suggested mechanisms as `DECIDED` without explicit user acceptance.
- **Cause:** Source authority was not separated from content quality.
- **Consequences:** The package could silently invent target architecture and roadmap.
- **Correction:** Require explicit human source for DECIDED; otherwise use REPORTED/UNKNOWN.
- **Lesson:** A plausible answer is not governance authority.
- **Repeat risk:** High.
- **Status:** OBSERVED in previous package; corrected.
- **Sources:** CH-13.

## E-03. Plan/readiness/report was confused with implementation

- **What happened:** Historical artifacts and chat reports sometimes sounded complete while the mechanism was only planned, documented, or partially implemented.
- **Cause:** Maturity dimensions were collapsed.
- **Consequences:** False confidence and premature downstream work.
- **Correction:** Track decision, code/docs presence, test execution, and human acceptance separately.
- **Lesson:** `PLAN_COMPLETE`, file presence, validator PASS, and product approval are different states.
- **Repeat risk:** High.
- **Status:** DECIDED lesson.
- **Sources:** CH-03, CH-05, RP-14.

## E-04. False PASS and simulated authority

- **What happened:** Validation language could imply approval, task completion, production readiness, or lifecycle mutation.
- **Cause:** Technical signals were allowed to carry semantic authority they did not possess.
- **Consequences:** Unsafe execution and misleading closure.
- **Correction:** Use evidence binding, strict claim boundaries, negative fixtures, and explicit human-review status.
- **Lesson:** PASS proves only the declared check.
- **Repeat risk:** High.
- **Status:** DECIDED + OBSERVED mitigation.
- **Sources:** CH-03, RP-14, NT-15.

## E-05. Current-status documentation drift

- **What happened:** `README.md` states M39 while the audited HEAD/HANDOFF states M90 complete and M91 not authorized.
- **Cause:** Status is copied into multiple documents without freshness binding.
- **Consequences:** Users and agents can start from the wrong milestone.
- **Correction:** One current-state source, generated summaries, and commit-bound freshness checks.
- **Lesson:** Status text must identify its source and snapshot.
- **Repeat risk:** High.
- **Status:** CONFLICT.
- **Sources:** RP-01, RP-04.

## E-06. Stale repository map and context index

- **What happened:** The repo map reports 64 files; a later inventory records 5,183. Context index contains one entry from an older commit.
- **Cause:** Derived artifacts were not kept fresh or were built from incomplete metadata.
- **Consequences:** Context selection can omit relevant rules and create false completeness.
- **Correction:** Fail closed on stale commit/hash; rebuild or remove stale derived artifacts; improve metadata coverage.
- **Lesson:** A generated index is useful only when freshness and coverage are provable.
- **Repeat risk:** High.
- **Status:** CONFLICT.
- **Sources:** RP-13, RP-16, RP-17, NT-11.

## E-07. Broad idle-state bypass can produce false PASS

- **What happened:** `validate-task.py` skips schema validation when scope/contract markers are absent.
- **Cause:** Idle detection uses permissive heuristics rather than a strict explicit idle schema.
- **Consequences:** Malformed or truncated task files may be accepted as idle.
- **Correction:** Define one explicit idle representation and validate it; reject ambiguous files.
- **Lesson:** Fail-open convenience is dangerous in authority-bearing contracts.
- **Repeat risk:** High.
- **Status:** OBSERVED risk.
- **Sources:** RP-10.

## E-08. Governance grew before product value was proven

- **What happened:** Historical work accumulated runtime enforcement, registries, milestone gates, evidence layers, and control artifacts.
- **Cause:** The project optimized control completeness before validating the simplest user workflow.
- **Consequences:** High cognitive load, slow delivery, and uncertain product value.
- **Correction:** Start with one product vertical slice and minimal safety floor; add controls after dogfood evidence.
- **Lesson:** Governance must earn its complexity by reducing real failures.
- **Repeat risk:** High.
- **Status:** DECIDED lesson.
- **Sources:** CH-01, CH-03, CH-09, CH-10.

## E-09. Duplicate rules and authority surfaces

- **What happened:** Rules appear in canonical modules, README, llms, adapters, prompt packs, reports, and notes.
- **Cause:** Manual copying and historical accumulation.
- **Consequences:** Contradictions, stale wording, and unclear source of truth.
- **Correction:** One authority per rule area; adapters remain thin/generated; duplication scanner reports but does not auto-delete.
- **Lesson:** Duplicate text is not redundancy when authority differs—it is drift risk.
- **Repeat risk:** High.
- **Status:** OBSERVED.
- **Sources:** RP-03, RP-16, RP-20.

## E-10. Context overload

- **What happened:** Large startup surfaces and exhaustive reading were proposed or accumulated.
- **Cause:** New knowledge was added to bootstrap instead of routed on demand.
- **Consequences:** Token cost, slower agents, and conflicting instructions.
- **Correction:** Minimal bootstrap, task-scoped Context Pack, and source-on-demand reference research.
- **Lesson:** More context can reduce correctness when authority and relevance are unclear.
- **Repeat risk:** Medium.
- **Status:** DECIDED direction + OBSERVED problem.
- **Sources:** CH-11, RP-13, RP-16, NT-08.

## E-11. Docs, schema, CLI, and implementation drift

- **What happened:** Specifications, scripts, status tokens, command paths, and validator behavior can diverge.
- **Cause:** Each surface evolved independently and reports were copied forward.
- **Consequences:** Checks pass against one representation while user-visible behavior differs.
- **Correction:** Verification must compare docs ↔ schema ↔ CLI ↔ code ↔ tests; reports must be commit-bound.
- **Lesson:** Contract consistency is a first-class verification gate.
- **Repeat risk:** High.
- **Status:** OBSERVED/REPORTED.
- **Sources:** RP-09–RP-11, RP-16, NT-19.

## E-12. Automation without a human checkpoint

- **What happened:** Retry, self-heal, queue movement, commit, or rule mutation can cascade if one signal triggers multiple actions.
- **Cause:** Automation was designed as a chain rather than bounded commands.
- **Consequences:** Unreviewed scope expansion and irreversible operations.
- **Correction:** One signal-one action; bounded retry; no autonomous canonical/product changes.
- **Lesson:** Automation may prepare evidence; authority remains explicit.
- **Repeat risk:** High.
- **Status:** DECIDED principle; candidate mechanisms REPORTED.
- **Sources:** CH-03, RP-15, NT-08.

## E-13. UI can accidentally become authority

- **What happened:** A dashboard or decision card may appear to approve work merely because a control is clicked or a status is rendered.
- **Cause:** Visual state and governed state are conflated.
- **Consequences:** False approval and user misunderstanding.
- **Correction:** UI only renders signed/recorded decisions; state mutation uses explicit contracts and evidence.
- **Lesson:** A control surface is not a control authority.
- **Repeat risk:** High.
- **Status:** REPORTED lesson.
- **Sources:** NT-09, NT-10, NT-24.

## E-14. AI-written code maintainability debt

- **What happened:** Generated code may lack rationale, ownership, consistent documentation, and reliable handoff.
- **Cause:** Delivery optimization ignores long-term maintenance.
- **Consequences:** Repeated rediscovery, fragile refactors, and docs-code drift.
- **Correction:** Add minimal rationale/ownership/decision records and targeted maintainability checks after the core workflow is stable.
- **Lesson:** Maintainability is a user-facing reliability concern, not just style.
- **Repeat risk:** Medium.
- **Status:** REPORTED; dedicated scripts NOT_FOUND.
- **Sources:** NT-13, NT-14, RP-19.

## E-15. Legacy roadmap leaked into present planning

- **What happened:** M44–M71, M88–M91, AOS-FARM, and new AOS reconstruction sequences coexist.
- **Cause:** Historical milestone systems were reused as navigation rather than bounded references.
- **Consequences:** The next project can inherit stale priorities and false dependencies.
- **Correction:** Discard legacy numbering during synthesis; select features by current problem/value/evidence.
- **Lesson:** Chronology is provenance, not architecture.
- **Repeat risk:** High.
- **Status:** CONFLICT.
- **Sources:** CH-09, NT-18, RP-04.

## Gaps and conflicts requiring human resolution

Priority interpretation:

- `CONFLICT` — sources disagree and a decision is required.
- `NOT_FOUND` — the named mechanism/path was not found in the inspected area.
- `UNKNOWN` — evidence is insufficient.
- `NOT_RUN` — no execution result exists from this audit.


## G-01. Project name

- **Evidence:** Recent target chats use `AOS`; historical repository and many notes use `AgentOS`.
- **Status:** CONFLICT.
- **Required resolution:** Human chooses target name and records relationship to historical repositories.
- **Sources:** CH-01, CH-09, RP-00.

## G-02. Target repository

- **Evidence:** No accepted implementation repository for the next system was found.
- **Status:** UNKNOWN.
- **Required resolution:** Assign only after product boundary, architecture, MVP, and dependency policy are accepted.
- **Sources:** CH-09.

## G-03. Legacy authority

- **Evidence:** Historical repository contains canonical labels, but the human decided it is reference-only for reconstruction.
- **Status:** CONFLICT.
- **Required resolution:** Keep `authority: NONE` outside the historical repo; import only selected mechanisms.
- **Sources:** CH-01, RP-03.

## G-04. Current milestone

- **Evidence:** README says M39; HEAD/HANDOFF say M90 complete and M91 not started.
- **Status:** CONFLICT.
- **Required resolution:** Choose one current-state source and regenerate secondary summaries.
- **Sources:** RP-01, RP-04.

## G-05. Repository map freshness

- **Evidence:** `repo-map.md` says 64 files; later M68 inventory says 5,183.
- **Status:** CONFLICT.
- **Required resolution:** Rebuild with SHA binding or remove from current navigation.
- **Sources:** RP-16, RP-17.

## G-06. Context index readiness

- **Evidence:** One stale indexed entry conflicts with the note's full-readiness claim.
- **Status:** CONFLICT.
- **Required resolution:** Treat context engine as partial; rebuild metadata coverage and freshness proof.
- **Sources:** RP-13, NT-11.

## G-07. Task idle validation

- **Evidence:** Broad heuristic idle bypass may accept malformed active-task documents.
- **Status:** OBSERVED.
- **Required resolution:** Replace with an explicit validated idle contract and negative fixtures.
- **Sources:** RP-10.

## G-08. Current verification evidence

- **Evidence:** Inspected verification file is a TODO demo artifact.
- **Status:** NOT_FOUND.
- **Required resolution:** Create task-bound real verification only when a real target task exists.
- **Sources:** RP-11.

## G-09. Lesson commit authority

- **Evidence:** Workflow says to commit lesson separately; human rules require explicit commit authorization.
- **Status:** CONFLICT.
- **Required resolution:** Change wording to prepare/stage a lesson proposal; commit only when separately authorized.
- **Sources:** CH-03, RP-05.

## G-10. Validation entrypoint

- **Evidence:** README calls `agentos-validate.py all` official; llms emphasizes `audit-agentos.py`.
- **Status:** CONFLICT.
- **Required resolution:** Declare one official entrypoint and mark focused checks as subordinate.
- **Sources:** RP-01, RP-02.

## G-11. Portable links

- **Evidence:** `llms.txt` includes absolute local `file:///Users/...` paths.
- **Status:** OBSERVED.
- **Required resolution:** Use repository-relative links and test template portability.
- **Sources:** RP-02.

## G-12. Target MVP

- **Evidence:** No human-approved final MVP feature subset was found.
- **Status:** UNKNOWN.
- **Required resolution:** Use F-42 as design anchor, then accept/reject individual feature cards.
- **Sources:** CH-09, CH-11.

## G-13. Governance topology

- **Evidence:** Governance may be integrated, optional, or a separate repository/module.
- **Status:** UNKNOWN.
- **Required resolution:** Choose after the product vertical slice demonstrates required control points.
- **Sources:** CH-01, CH-09.

## G-14. UI foundation

- **Evidence:** Named semantic UI, token, and replaceability policy files are missing.
- **Status:** NOT_FOUND.
- **Required resolution:** Do not claim UI foundation implemented; design only when product UI is in scope.
- **Sources:** RP-09, RP-18, NT-10.

## G-15. Code Stewardship implementation

- **Evidence:** Dedicated maintainability and doc-drift checker paths were not found.
- **Status:** NOT_FOUND.
- **Required resolution:** Retain problem/requirements; defer tooling or implement a minimal targeted checker later.
- **Sources:** RP-19, NT-13.

## G-16. Multi-agent direction

- **Evidence:** Research sources propose specialized agents/MAD; current minimal direction and README exclude multi-agent orchestration.
- **Status:** CONFLICT.
- **Required resolution:** Defer until single-agent workflow metrics show a specific deficit.
- **Sources:** CH-03, RP-01, NT-04, NT-21.

## G-17. Self-heal direction

- **Evidence:** Biological-development note proposes self-heal; current README says no self-heal platform and human authority must remain.
- **Status:** CONFLICT.
- **Required resolution:** Allow at most logged structural repair after explicit design; no product/canonical auto-repair.
- **Sources:** RP-01, NT-08.

## G-18. Control UI/SaaS direction

- **Evidence:** Historical notes propose admin panel, chat, preview, SaaS, cloud, and marketplace; current README lists several as non-goals.
- **Status:** CONFLICT.
- **Required resolution:** Treat as historical reference, not target roadmap.
- **Sources:** RP-01, NT-18, NT-24.

## G-19. Feature conflict checker

- **Evidence:** Need is clear, but no accepted semantic-review contract or implementation was established.
- **Status:** UNKNOWN.
- **Required resolution:** Specify inputs, conflict classes, evidence, and human decision boundary.
- **Sources:** NT-06, RP-08.

## G-20. Cross-repo product feature

- **Evidence:** Read-only cross-repo extraction is accepted, but reusable installation/sync behavior is not designed.
- **Status:** UNKNOWN.
- **Required resolution:** Separate operational workflow from a future productized module.
- **Sources:** CH-08, NT-12.

## G-21. Independent repository health

- **Evidence:** Repository reports claim many PASS results, but this audit ran nothing.
- **Status:** UNKNOWN / NOT_RUN.
- **Required resolution:** Run separately only under a governed task; do not convert stored reports into current PASS.
- **Sources:** RP-14, RP-16.

## G-22. Complete chat provenance

- **Evidence:** Only available chats and summaries were inspected; raw full history is not guaranteed.
- **Status:** UNKNOWN.
- **Required resolution:** Human review should flag missing decisions; retrieve a specific chat on demand if material.
- **Sources:** CH-01–CH-13.

## G-23. Feature acceptance rule

- **Evidence:** The catalog is accepted, but the exact scoring/filter policy is only a note.
- **Status:** UNKNOWN.
- **Required resolution:** Human approves a concise keep/simplify/defer/reject decision method.
- **Sources:** CH-12, NT-02.

## G-24. Product/runtime boundary

- **Evidence:** Which historical product-spec, task, runtime, and governance components form the new product is not selected.
- **Status:** UNKNOWN.
- **Required resolution:** Complete synthesis before architecture or implementation.
- **Sources:** CH-09.

## Consolidated anti-patterns

- Treating legacy `canonical` labels as target authority.
- Counting documents/validators as product progress.
- Letting a Task Brief or candidate become executable by implication.
- Treating validation/readiness as human acceptance.
- Adding Governance before proving a real product cycle.
- Reading the whole repository instead of bounded context.
- Hiding `UNKNOWN`, `NOT_RUN` or warning states.
- Mixing unrelated cleanup with the active task.
- Adding RAG, multi-agent, replay, UI or cloud without a measured problem.
- Auto-merging cross-repo changes because a superficial contract appears unchanged.
- Letting model consensus authorize execution.
- Allowing self-heal to modify product/canonical decisions.
- Using machine-specific paths in portable templates.
- Writing process rules that silently imply commit/push authority.

## Human review checklist

1. Confirm which lessons are accepted for the next system.
2. Resolve target name, repository, MVP and first vertical slice.
3. Select `KEEP`, `SIMPLIFY`, `DEFER`, `REFERENCE_ONLY` or `REJECT` for each feature in [06_Features.md](06_Features.md).
4. Decide the Product Runtime/Governance boundary.
5. Approve a concise Feature Passport/Registry contract.
6. Approve human acceptance and authority records.
7. Choose a real-task dogfood scenario and success measures.
8. Remove or defer mechanisms whose operational cost exceeds measured value.

No lesson automatically changes a rule, file, roadmap or repository.

**PARTIAL EXTRACTION READY FOR REVIEW**

**HUMAN REVIEW REQUIRED**
