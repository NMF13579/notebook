# 04 — AOS Lessons


> **Artifact status:** `DRAFT`  
> **Authority:** `NONE`  
> **Canonical status:** `NOT_ASSIGNED`  
> **Human acceptance:** `NOT_REQUESTED`  
> **Implementation authorization:** `NONE`  
> **Source basis:** доступная история чатов проекта, current Project Instructions и загруженные reference notes; current repository/runtime verification — `NOT_RUN`.


## 1. Назначение

Документ превращает историю AOS-FARM, AOS-02 и reconstruction work в практические preventive rules. Он отделяет observed failure от plausible explanation и от accepted project rule.

```text
observed failure
→ source and temporal scope
→ root-cause candidate
→ impact
→ preventive proposal
→ test/review check
→ human acceptance when rule affects project facts
```

## 2. Аудит предыдущего synthesis package

### 2.1 Структурный finding

Предыдущая версия содержала **49 Markdown-файлов**, **78 idea records** и 10 feature-domain files. Это противоречило текущей пользовательской цели: семь понятных top-level documents без file sprawl.

**Impact:** навигация требовала README/index/manifest/cross-links; одинаковые concepts были распределены между `01_Product`, `02_Architecture`, `03_Development`, `04_Lessons`, `05_Reference` и многочисленными `06_Features/*`.

**Correction in this revision:** ровно семь `.md` files; каждый fact class имеет один primary section owner.

### 2.2 Feature-depth finding

Каждая из 78 карточек имела в основном:

```text
Problem
Idea
Minimal safe version
Key risks
Targeted research
Sources
```

Средняя substantive description была около 47 слов. Систематически отсутствовали:

- actors;
- trigger/preconditions;
- inputs/outputs;
- happy path/decision points;
- states/transitions;
- failure and recovery behavior;
- dependencies/shared contracts;
- authority boundaries;
- acceptance criteria;
- negative tests;
- implementation responsibility and non-goals.

**Impact:** человек видел название и intuition, но не мог оценить реальное поведение; agent не мог без догадок спроектировать contract, state model или tests.

**Correction:** 78 ideas сведены в 30 coherent feature families в `06_Features.md`; у каждой family полный dossier и explicit micro-idea crosswalk.

### 2.3 Classification finding

Предыдущий package смешивал:

- product feature;
- internal Development Factory tool;
- governance control;
- architecture extension;
- future module;
- historical implementation mechanism.

`CANDIDATE`, `IDEA_ONLY`, `LINKED_PRODUCT_CANDIDATE`, `DEFERRED_RESEARCH` и другие dispositions были полезны для inventory, но не отвечали на вопрос, что именно должен увидеть пользователь.

**Correction:** каждая feature family теперь имеет layer, maturity/disposition, target user, outcome, Product Runtime boundary и non-goals. Scope effect остаётся `NONE` до human product decision.

### 2.4 Evidence finding

Source mapping был широким, но большинство repository claims не перепроверялось по current snapshots. Historical names, branches, test counts и capability statuses могли выглядеть актуальнее, чем были.

**Correction:** `05_Reference.md` явно разделяет chat-derived intent, source-note proposals, historical repository observations и `NOT_RUN` current verification.

### 2.5 Duplicate-owner finding

`01_Product/feature-catalog.md` содержал 22 normalized candidates, а `06_Features` — 78 ideas. Boundary существовала, но человеку приходилось сопоставлять два каталога.

**Correction:** `01_Product.md` отвечает за product intent, users, journeys, boundaries and admission rules. `06_Features.md` — единственный detailed feature inventory/idea source. Product acceptance по-прежнему требует отдельного human decision.

## 3. Failure and anti-pattern catalog

### FAIL-001 — Governance before executable product value

- **Observation:** approvals, registries, lifecycle and Control Plane grew before a useful Product Runtime slice.
- **Root cause candidate:** control was treated as the product rather than a risk response.
- **Impact:** product progress delayed; formal readiness replaced user outcome.
- **Preventive rule:** one accepted user/problem/outcome and a visible vertical slice before platform expansion.
- **Check:** every major control feature links to a concrete incident/risk and cannot be admitted solely for completeness.

### FAIL-002 — Unfinished Control Plane controlled its own development

- **Observation:** immature control artifacts were used to establish the trust of the process producing them.
- **Root cause:** missing independent subject and witness boundary.
- **Impact:** self-referential assurance and recovery loops.
- **Preventive rule:** validation subject immutable; reviewer/validator cannot alter or approve its own control basis.
- **Test:** validation against disposable/frozen subject; detect self-reference and write-after-freeze.

### FAIL-003 — Planning acquired execution-grade ceremony

- **Observation:** routine tasks repeatedly entered new plans, manifests, hashes and reauthorization layers.
- **Root cause:** no distinction between incomplete Task Brief and executable routine task.
- **Preventive rule:** do not re-plan complete Task Brief absent material change.
- **Check:** planning gate records exact missing field or protected decision.

### FAIL-004 — Readiness and recovery artifacts became blockers

- **Observation:** effort shifted to preparing readiness packages instead of fixing product behavior.
- **Root cause:** process success measured by artifact completion.
- **Preventive rule:** every artifact must support a user-visible capability, decision or falsifiable check.
- **Check:** orphan artifact review; remove artifacts with no consumer.

### FAIL-005 — Technical result was treated as human acceptance

- **Observation:** PASS, Evidence, CI, readiness and approval semantics converged.
- **Root cause:** same status channel represented different fact classes.
- **Preventive rule:** technical results and human decisions use separate records and vocabularies.
- **Negative test:** generated `ACCEPT` or review package cannot unlock execution/Git action.

### FAIL-006 — Human decision was simulated

- **Observation:** prototype accepted human-decision-like fields without trustworthy human provenance.
- **Root cause:** decision authenticity and identity were not part of contract.
- **Preventive rule:** agent-generated decision invalid; missing authenticity blocks only affected authority-bearing action.
- **Test:** reject decision created by same execution agent or lacking exact subject binding.

### FAIL-007 — Schemas existed but runtime did not enforce them

- **Observation:** documents/tests described schemas while executor/CLI accepted incompatible values.
- **Root cause:** multiple parsing/validation paths.
- **Preventive rule:** one strict contract implementation used by runtime and tests.
- **Test:** schema/runtime drift fixtures; bypass path must fail.

### FAIL-008 — Validators accepted invalid/empty states

- **Observation:** empty mappings, bogus status and free-form Risk Profile could pass.
- **Root cause:** permissive defaults and incomplete negative tests.
- **Preventive rule:** closed vocabularies, required fields, explicit empty-state semantics.
- **Tests:** empty object, unknown enum, null, duplicate key, unexpected field, bool-as-int.

### FAIL-009 — CLI failure looked successful

- **Observation:** invalid input or domain failure could return exit code 0 or omit machine-readable terminal result.
- **Root cause:** happy-path-only CLI design.
- **Preventive rule:** every exit path has stable result and exit semantics.
- **Test:** invalid args, contract failure, environment failure and internal exception.

### FAIL-010 — Scope existed only in prose

- **Observation:** allowed paths did not reliably constrain actual mutation.
- **Root cause:** Task Brief was documentation, not executable boundary.
- **Preventive rule:** normalized path allowlist plus post-execution diff reconciliation.
- **Tests:** traversal, symlink ancestor, nested repository, untracked outside scope, case/separator variants.

### FAIL-011 — Dirty worktree contaminated candidate

- **Observation:** unrelated local artifacts could enter task diff or staging.
- **Root cause:** no isolated subject or classification of existing state.
- **Preventive rule:** clean worktree by default; classify out-of-scope state; never auto-stage all.
- **Test:** pre-existing modified/untracked files remain untouched and excluded.

### FAIL-012 — Environment noise caused false blockers

- **Observation:** `.venv/` or unrelated generated files made every task appear unsafe.
- **Root cause:** binary clean/dirty policy.
- **Preventive rule:** distinguish environmental noise, user state, task state and material unknown.
- **Check:** blocker reason names exact affected claim/operation.

### FAIL-013 — Read-only operation changed repository

- **Observation:** status/validation helper created temporary files inside source tree while reporting no mutation.
- **Root cause:** undefined temporary boundary.
- **Preventive rule:** read-only commands produce zero target writes; disposable outputs outside source or under explicit temp root.
- **Test:** before/after tree/status digest exact.

### FAIL-014 — Raw remote data leaked

- **Observation:** visible `git remote` output could expose credential-bearing URL.
- **Root cause:** collection and redaction were separate steps.
- **Preventive rule:** collect through redacting wrapper; never print raw value.
- **Test:** embedded userinfo/token/query/fragment never appears in transcript/report.

### FAIL-015 — Mutation was non-atomic and unrecoverable

- **Observation:** write-capable operation could leave partial state without journal/reconciliation.
- **Root cause:** failure behavior designed after happy path.
- **Preventive rule:** atomic publication or durable operation journal before first mutation.
- **Tests:** interruption at every write boundary; deterministic resume/rollback.

### FAIL-016 — Candidate identity drifted after freeze

- **Observation:** self-reference, write-after-freeze or stale tree identity invalidated validation subject.
- **Root cause:** Evidence/final artifacts created in wrong order.
- **Preventive rule:** finalize evidence inputs, freeze content, verify immutability, then validate.
- **Tests:** mutate any byte after freeze; detect provisional identity and self-hash cycles.

### FAIL-017 — Stale baseline applied to advanced candidate

- **Observation:** validator compared against pre-commit/pre-mutation identity after HEAD changed.
- **Root cause:** reports not bound to baseline and candidate pair.
- **Preventive rule:** every check records exact baseline/candidate; changed subject invalidates result.
- **Test:** move HEAD or alter worktree between preview and validate.

### FAIL-018 — `NOT_RUN` became PASS

- **Observation:** unavailable dependency/environment check disappeared in aggregate success.
- **Root cause:** weak aggregation/claim ceiling.
- **Preventive rule:** required `NOT_RUN` prevents PASS; optional `NOT_RUN` remains visible.
- **Test:** environment-limited suite and mixed required/optional checks.

### FAIL-019 — Default authorization was open

- **Observation:** neutral template could contain `authorized: true`.
- **Root cause:** convenience over authority integrity.
- **Preventive rule:** all authority-bearing defaults false; authorization exact and single-purpose.
- **Test:** omitted field, stale record, copied template and reused authorization all fail closed.

### FAIL-020 — Unknown either blocked everything or was hidden

- **Observation:** low-risk analysis stopped on any unknown, while other flows silently treated unknown as OK.
- **Root cause:** unknown lacked impact scope.
- **Preventive rule:** record impact level and affected operations; block only where correctness/safety/authority requires.
- **Test:** informational unknown does not block read-only synthesis; safety unknown blocks mutation.

### FAIL-021 — Exhaustive extraction produced low signal

- **Observation:** repository-wide campaigns consumed time while implementation usefulness remained low.
- **Root cause:** research optimized source completeness rather than feature demand.
- **Preventive rule:** feature-scoped research with explicit questions and stop conditions.
- **Check:** each inspected path supports one dossier gap.

### FAIL-022 — Legacy topology became target architecture candidate

- **Observation:** historical folders, control components and recovery chains were treated as foundations.
- **Root cause:** implementation was confused with requirement.
- **Preventive rule:** extract observable contract and reimplement; compatibility is separate cost decision.
- **Review check:** every proposed component states why it is needed independent of legacy existence.

### FAIL-023 — Product Runtime and Development Factory blurred

- **Observation:** internal task conveyor or repository administration could be presented as product progress.
- **Root cause:** no user-visible acceptance boundary.
- **Preventive rule:** Product Runtime must perform an identified user job; Factory supports building it.
- **Check:** result visible to target user without reading internal control artifacts.

### FAIL-024 — Automation preceded manual proof

- **Observation:** registry, routing, autonomous loops and enforcement were designed before stable manual cycles.
- **Root cause:** automation substituted for product discovery.
- **Preventive rule:** automate measured repetition only after at least two successful bounded cycles and stable contracts.
- **Check:** automation admission package cites observed frequency, failure modes, fallback and removal path.

### FAIL-025 — Documentation fragmented and duplicated

- **Observation:** many README/index/manifest/files repeated boundaries and feature descriptions.
- **Root cause:** taxonomy growth without one-owner rule.
- **Preventive rule:** one document per current top-level fact class; headings and links instead of duplicate files.
- **Check:** duplicate claim/term owner audit.

### FAIL-026 — Feature cards were too shallow

- **Observation:** idea names and short descriptions lacked behavior/contracts/tests.
- **Root cause:** inventory was mistaken for implementation knowledge.
- **Preventive rule:** each promoted feature uses full dossier schema.
- **Check:** no feature is planning-ready without actors, trigger, I/O, flow, states, failures, recovery, acceptance and negatives.

### FAIL-027 — Skeleton/documentation looked like implementation

- **Observation:** repository files, schemas and CI could be interpreted as a working product.
- **Root cause:** maturity vocabulary absent or weak.
- **Preventive rule:** distinguish `DOCUMENTATION`, `SKELETON`, `PROTOTYPE`, `PARTIALLY_WORKING`, `PRODUCT_RUNTIME`.
- **Test/review:** runtime claim requires executable Evidence against exact subject.

### FAIL-028 — First-contact UX remained fragmented

- **Observation:** installation, FIRST-START, START_HERE, doctor, commands and status interpretation could live in overlapping docs.
- **Root cause:** documentation organized by producer rather than beginner journey.
- **Preventive rule:** one authoritative first-start path, short pointers elsewhere, first safe command bundle and status explanations.
- **Acceptance:** non-programmer completes first safe journey without internal help.

### FAIL-029 — Consumer control features were not integrated as one journey

- **Observation:** Unified Validate, Safety Fixtures, Intake Wizard, Review/Handoff and Lessons Memory appeared as separate deliverables.
- **Root cause:** feature implementation sequence not tied to end-to-end dogfood.
- **Preventive rule:** validate through one real task from install/intake to human decision and lesson capture.
- **Test:** end-to-end first-contact dogfood with beginner review.

### FAIL-030 — Git closure stopped at local technical state

- **Observation:** validated candidate, remote state, merge authorization and lifecycle closure were handled by separate complex chains.
- **Root cause:** closure semantics were not user-facing and compact.
- **Preventive rule:** status helper reports local/remote/review/decision boundaries and one next action; each Git permission remains separate.
- **Test:** stale remote/branch/candidate invalidates merge recommendation without authorizing action.

### FAIL-031 — Model routing was assumed rather than measured

- **Observation:** roles/providers/models could be assigned by intuition or availability.
- **Root cause:** no benchmark, routing record or privacy boundary.
- **Preventive rule:** advisory routing first; explicit agent selection; runtime routing only after measured value.
- **Test:** fallback/model change is visible and cannot increase permissions.

### FAIL-032 — Installer/update ownership was unclear

- **Observation:** managed template, user configuration, project state and human decisions risked being overwritten together.
- **Root cause:** missing ownership model and reconciliation.
- **Preventive rule:** classify every path; preview exact operation; preserve user/project-owned state; verify after apply.
- **Test:** modified managed file, user file conflict, interrupted update, repeated update, uninstall with durable state.

## 4. Successful patterns to retain

1. **Product-first sequencing.** User value before platform.
2. **Compact Safe Path.** Complete Task Brief → bounded Execute → checks → report → stop.
3. **One run, one stage.** No auto correction or stage cascade.
4. **Independent validation.** Validator does not alter subject.
5. **Exact baseline/candidate binding.** Freshness and identity are explicit.
6. **Clean isolated worktree.** Bounded diff and reduced contamination.
7. **Fail-closed result semantics.** Severe/unknown condition cannot be hidden by PASS.
8. **One next action.** Report informs but does not execute transition.
9. **One-document human review.** Low cognitive load with linked Evidence.
10. **Reference Findings Index.** Research result reused rather than rediscovered.
11. **Beginner-facing status explanation.** What happened, why, what was not done, required decision, next action.
12. **Manual dogfood.** Real task exposes UX/contracts before automation.
13. **Strict loader adapter before replacement.** Stabilize contract, migrate callers, then sunset legacy parser.
14. **Negative fixtures as trust infrastructure.** Invalid/stale/unauthorized cases first-class.
15. **Derived indexes rebuildable.** Registry/RAG/dashboard never become accidental SoT.

## 5. Environment and repository hygiene

- Bind interpreter and dependency environment to reports.
- Do not assume shell `python` equals test/runtime interpreter.
- Record missing dependency as `NOT_RUN`/`BLOCKED`, not silent fallback.
- `--help` must have no side effects.
- Temporary files use approved disposable root and never contain canonical decisions/Evidence.
- Do not auto-delete forensic temp after interrupted write until recovery decision.
- Use normalized POSIX-relative paths; forbid `..`, absolute paths, symlink escapes and nested-repo surprises.
- Recheck repository identity before every Git operation.
- Never print secrets or raw remote URL.
- Validate import provenance when testing installed/disposable subject.

## 6. Regression suite derived from lessons

The future AOS test catalog should include at least:

```text
AUTH-001 generated human decision rejected
AUTH-002 authorization defaults false
AUTH-003 stale/reused authorization rejected
STATUS-001 unknown enum rejected
STATUS-002 required NOT_RUN prevents PASS
STATUS-003 Evidence cannot unlock approval
SCOPE-001 path traversal/symlink escape rejected
SCOPE-002 unrelated dirty state excluded
CLI-001 every failure has terminal machine result
CLI-002 --help/read-only has zero writes
ENV-001 interpreter/import provenance recorded
FREEZE-001 write-after-freeze detected
FREEZE-002 self-reference/provisional identity rejected
INSTALL-001 dry-run exact and side-effect free
INSTALL-002 apply bound to unchanged preview
UPDATE-001 user/project state preserved
RECOVERY-001 interruption at each mutation boundary recoverable
REVIEW-001 one package shows acceptance and NOT_RUN honestly
GIT-001 commit/push/merge/release permissions independent
ROUTING-001 model fallback visible and no privilege escalation
CONTENT-001 external instructions treated as untrusted data
DRIFT-001 schema/runtime/docs divergence detected
DOGFOOD-001 non-programmer completes first-contact journey
LESSON-001 incident creates candidate lesson, not automatic rule
```

## 7. Correction status of this seven-document revision

| Previous issue | Correction in current artifact |
|---|---|
| 49 Markdown files | Exactly 7 Markdown files |
| 78 shallow microcards | 30 detailed feature families + complete 78-idea crosswalk |
| Product catalog duplicated idea bank | `01_Product` owns intent/journeys; `06_Features` owns detailed inventory |
| Missing behavior/test fields | Standard full dossier for every family |
| Historical state looked current | `05_Reference` marks current repository/runtime checks `NOT_RUN` |
| Too many indexes/manifests | Headings and embedded registers within seven documents |
| Potential authority confusion | Every file remains `DRAFT`, `authority: NONE`, no implementation/Git authorization |

Independent semantic validation by a separate reviewer remains `NOT_RUN`.
