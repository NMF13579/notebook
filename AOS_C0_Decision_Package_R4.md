---
package: AOS_C0_Decision_Package
package_id: AOS-C0
revision: C0-R4
created: '2026-07-27'
supersedes: C0-R3
status: DRAFT_FOR_HUMAN_DECISION
document_maturity: HUMAN_REVIEW_REQUIRED
human_decision: null
authority: PROPOSAL
fact_class: PRODUCT_AND_ARCHITECTURE_DECISION_PROPOSAL
status_model: ORTHOGONAL
technical_results:
  artifact_structure_validation: PASS
  detached_checksum_validation: NOT_RUN
  repository_validation: PASS
  runtime_validation: NOT_RUN
independent_semantic_validation: NOT_RUN
package_operation_permission: NOT_APPLICABLE
downstream_permissions:
  implementation: NONE
  execution: NONE
  user_repository_mutation: NONE
  code_execution: NONE
  git: NONE
source_baseline:
  package: AOS_Project_Knowledge_Baseline
  revision: R4-RU
  source_repository: NMF13579/notebook
  source_branch: dev
  source_head_commit: d783f7d8cd0d2af2fb88fafa23ea16f289ef8ea6
  source_document:
    path: docs/00_Core.md
    blob_sha: 24e2f4816946e91713280e881c74f391e7bc3795
    package: AOS_Project_Knowledge_Baseline
    package_revision: R4-RU
  audited_predecessor_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
  repository_revalidation: PASS
correction_basis:
  review_id: AOS-C0-R3-READ-ONLY-REVIEW
  review_result: COMPLETED_WITH_BLOCKING_FINDINGS
  reviewed_r3_attachment_sha256: 7c9639f8a30bb017aba5bce2f412dfdd86aa0fefc076dd4738497873d29be10f
  corrected_findings:
    - P1-01_SOURCE_BASELINE_IDENTITY_MISMATCH
    - P1-02_DETACHED_CHECKSUM_NOT_AVAILABLE_FOR_VERIFICATION
prior_correction_basis:
  audit_id: AOS-C0-R2-INDEPENDENT-AUDIT
  audit_revision: AUDIT-R2
  audited_r2_sha256: 14134a643e6f4d5cfefc23ad744893f0f0ee20827232d83fc38b64f9c6c791d3
  audit_file_sha256: d4fb4057f9b27a20bd713a424b6ea2223bc6588e837d8167e4beb43ce56941ef
human_acceptance: NOT_GRANTED
implementation_authorization: NONE
execution_authorization: NONE
git_authorization: NONE
decision_packaging:
  mode: PACKAGE_LEVEL_ALL_OR_NOTHING
  rationale: OPERATIONAL_CONSISTENCY
  partial_acceptance: REQUIRES_SUCCESSOR_REVISION
decision_ids_if_accepted:
  - C0-D01
  - C0-D02
  - C0-D03
  - C0-D04
decision_labels:
  C0-D01: FIRST_USER_AND_JOB
  C0-D02: FIRST_CORE_VERTICAL_SLICE
  C0-D03: MINIMAL_AOS_ARCHITECTURE
  C0-D04: PRODUCT_ARTIFACT_RELATION_FOR_CORE_SLICE_001
c0_decision_authority_role: AOS_PRODUCT_OWNER
first_user_role: DOMAIN_EXPERT_PRODUCT_OWNER
next_artifact_if_accepted: FIRST_SLICE_PRODUCT_CONTRACT_R1
next_phase_id: UNASSIGNED
subject_binding:
  algorithm: SHA-256
  digest_location: DETACHED_CHECKSUM
  checksum_file: AOS_C0_Decision_Package_R4.md.sha256
---

# AOS C0 — Decision Package

## 1. Вывод

`C0-R4` предлагает принять единый стартовый выбор AOS:

1. **First user:** непрограммист / domain expert в роли владельца продукта, способный оценить desired outcome, но не обязанный понимать implementation и repository mechanics.
2. **First job:** превратить неполную software product idea в bounded и reviewable product package первого пользовательского среза, где видны assumptions, unknowns, non-goals и one next action.
3. **First Core vertical slice:** `Intent → Accepted First Feature Passport` — от original request до human decision по exact frozen review bundle, содержащему minimal-depth `C-003 Product Spec` и первый `C-002 Feature Passport`.
4. **Product artifact relation для этого slice:** `C-001 Intent Record → minimal-depth C-003 Product Spec → one C-002 Feature Passport`. Это depth profile существующих contracts, а не новый contract class.
5. **Minimal AOS architecture:** local-first, single-user, modular monolith с deterministic domain core, replaceable local-first interaction port, optional agent adapter, versioned structured-file store и derived Markdown/text views.

C0 различает две authority-роли:

```text
AOS_PRODUCT_OWNER
— принимает или отклоняет стратегическое решение C0 о самом AOS

DOMAIN_EXPERT_PRODUCT_OWNER
— является first user будущего AOS и принимает product artifacts своего first slice
```

Один человек может совмещать обе роли в first dogfood, но subject и authority scope каждого решения остаются раздельными.

First slice **не требует доступа к user repository**, но является write-capable относительно собственного local AOS state: он создаёт immutable artifact revisions и отдельный `HumanDecisionRecord`. Поэтому он не классифицируется как read-only.

Это решение пока имеет класс `PROPOSAL`. До explicit human decision exact revision `C0-R4` не является принятой product/architecture authority, не разрешает implementation и не разрешает Git actions.

## 2. Decision boundary

### 2.1. C0 выбирает

- first user segment и first JTBD;
- границу первого user-visible Product Runtime slice;
- scoped relation `C-001 ↔ C-003 ↔ C-002` для `CORE-SLICE-001`;
- minimal architecture style, component boundaries, authority model, persistence direction и initial interaction boundary самого AOS;
- property-level boundary human decision authenticity: explicit human-controlled action, exact subject binding и запрет agent-generated acceptance;
- complexity, которая явно не входит в first slice;
- следующий bounded artifact после принятия C0.

### 2.2. C0 не выбирает и не разрешает

- implementation repository;
- language, runtime, framework, dependency manager или exact dependency versions;
- exact filesystem paths или serialization profile;
- concrete human-decision capture implementation: chat, signed file, CLI, desktop UI или иной mechanism;
- final UI, cloud deployment или SaaS;
- architecture пользовательского проекта;
- repository discovery, Task Brief compilation, code execution или validation pipeline;
- Risk Profile;
- Commit, Push, Merge или Release;
- полное item-level admission затронутых `FTR-*` dossiers;
- implementation authorization.

### 2.3. Семантика option labels

Labels в сравнительных таблицах ниже являются только presentation labels этого proposal:

```text
RECOMMENDED_IF_ACCEPTED
RETAIN_AS_LATER_CANDIDATE
NOT_SELECTED_FOR_FIRST_SLICE
```

Они не изменяют canonical human disposition из `06_Features.md` и не являются `Human decision` до отдельного exact record.

Frontmatter label `DRAFT_FOR_HUMAN_DECISION` является presentation label: он отображает `document_maturity: HUMAN_REVIEW_REQUIRED` и отсутствие Human Decision Record. Он не создаёт отдельную lifecycle axis и не означает technical result.

## 3. Подтверждённая основа

| Claim | Fact class | Source |
|---|---|---|
| AOS ориентирован на human-directed AI-assisted development, а не на максимальную автономность | `HUMAN_ACCEPTED_FACT` | `00_Core.md` §§2–3 |
| First segment, first vertical slice и architecture утверждает только человек | `HUMAN_ACCEPTED_FACT` | `00_Core.md` §13 |
| Product Runtime должен предшествовать Development Factory | `HUMAN_ACCEPTED_FACT` | `00_Core.md` §12; `01_Product.md` §8 |
| Первый slice должен давать observable result и работать без full Control Plane | `HUMAN_ACCEPTED_FACT` | `01_Product.md` §11 |
| `Product Spec` и `Feature Passport` имеют разные fact owners | `HUMAN_ACCEPTED_FACT` | `01_Product.md` §6; `02_Architecture.md` §§6, 8 |
| Architecture decision принадлежит human-accepted `C-004 ADR` | `HUMAN_ACCEPTED_FACT` | `02_Architecture.md` §§6, 8 |
| Maturity, workflow/stage, technical result, human decision и permission являются независимыми осями | `HUMAN_ACCEPTED_FACT` | `02_Architecture.md` §7 |
| Writes должны быть atomic или journaled и иметь recovery model | `HUMAN_ACCEPTED_FACT` | `02_Architecture.md` §§13–14; `03_Development.md` §13 |
| Feature inventory не выбирает feature автоматически | `HUMAN_ACCEPTED_FACT` | `00_Core.md` §7; `06_Features.md` §§1–3 |
| Human decision требует exact subject binding; generated decision invalid | `HUMAN_ACCEPTED_FACT` | `02_Architecture.md` `C-011`; `06_Features.md` `FTR-012` |

## 4. Рассмотренные варианты

### 4.1. First user/job

| Option | User/job | Плюсы | Минусы | C0 recommendation |
|---|---|---|---|---|
| `U-A` | Domain expert с неполной идеей → reviewable first product contract | Закрывает `P-003`, не требует repository access, даёт понятный result | Требует качественного clarification UX и facilitated first dogfood | **RECOMMENDED_IF_ACCEPTED** |
| `U-B` | Vibe-coder с existing repo → безопасная реализация одной задачи | Сильный coding dogfood | Сразу требует Discovery, Factory, preflight, execution и Git boundaries | `RETAIN_AS_LATER_CANDIDATE` |
| `U-C` | Developer/reviewer → Evidence и review package | Хорошо проверяемо | Не доказывает основной value для nontechnical owner | `RETAIN_AS_LATER_CANDIDATE` |
| `U-D` | Maintainer → status/resume/recovery | Полезно после появления runtime state | Для первого slice ещё нечего надёжно возобновлять | `RETAIN_AS_LATER_CANDIDATE` |

### 4.2. First vertical slice

| Option | Slice | Плюсы | Минусы | C0 recommendation |
|---|---|---|---|---|
| `S-A` | `Intent → Accepted First Feature Passport`; no user-repo access, AOS-local writes | User-visible, product-first, bounded, создаёт upstream contract | Не демонстрирует coding execution | **RECOMMENDED_IF_ACCEPTED** |
| `S-B` | `Repository → Capability Map` | Полезно для existing project | Требует repository access и broader discovery semantics | `RETAIN_AS_LATER_CANDIDATE` |
| `S-C` | `Feature Contract → Task Brief → One Change` | Демонстрирует end-to-end development | Слишком много architecture, safety и tooling до доказанной product value | `NOT_SELECTED_FOR_FIRST_SLICE` |
| `S-D` | `/status → /next → resume` | Понятный UX | Требует уже существующего reliable project state | `RETAIN_AS_LATER_CANDIDATE` |

### 4.3. Product artifact relation для `CORE-SLICE-001`

| Option | Relation | Плюсы | Минусы | C0 recommendation |
|---|---|---|---|---|
| `P-A` | `C-001 → C-002`, без `C-003` | Самая короткая цепочка | Отклоняется от accepted `J-001`/`FTR-003` и заставляет `C-002` владеть product-level context | `NOT_SELECTED_FOR_FIRST_SLICE` |
| `P-B` | `C-001 → minimal-depth C-003 → one C-002` | Сохраняет fact ownership и остаётся bounded | Добавляет один небольшой product-level artifact | **RECOMMENDED_IF_ACCEPTED** |
| `P-C` | Полный широкий `C-003` до выбора slice | Максимальный product context | Риск planning platform и избыточной документации | `NOT_SELECTED_FOR_FIRST_SLICE` |

### 4.4. Minimal architecture

| Option | Architecture | Оценка | C0 recommendation |
|---|---|---|---|
| `A-A` | Prompt/Markdown-only package | Быстро, но не создаёт deterministic runtime и durable state semantics | `NOT_SELECTED_FOR_FIRST_SLICE` |
| `A-B` | Local modular monolith + deterministic core + versioned structured files + thin adapters | Минимальная реализуемая architecture с replaceable internals | **RECOMMENDED_IF_ACCEPTED** |
| `A-C` | Local web application | Лучше onboarding, но вводит frontend/backend complexity | `RETAIN_AS_LATER_CANDIDATE` |
| `A-D` | Services, Control Plane, RAG, multi-agent runtime | Преждевременная platform complexity | `NOT_SELECTED_FOR_FIRST_SLICE` |

## 5. `C0-D01` — First user and first job

```yaml
decision_id: C0-D01
selection_status: PROPOSED
recommended_option: U-A_DOMAIN_EXPERT_TO_FIRST_PRODUCT_PACKAGE
first_user:
  role: DOMAIN_EXPERT_PRODUCT_OWNER
  programming_skill_required: false
  repository_skill_required: false
  authority_scope: FIRST_SLICE_PRODUCT_CONTENT
  required_capability: CAN_EVALUATE_DESIRED_OUTCOME
secondary_user:
  role: VIBE_CODER
  status: SUPPORTED_BUT_NOT_PRIMARY
first_job:
  trigger: USER_HAS_INCOMPLETE_SOFTWARE_PRODUCT_IDEA
  job_statement: >-
    Помоги превратить мою неполную идею в ограниченный и понятный
    product package первого пользовательского среза, чтобы я мог
    исправить assumptions, увидеть unknowns и принять exact revisions
    без разрешения implementation.
```

### 5.1. Почему выбран этот user/job

- Напрямую закрывает `P-003`: free-form request не должен незаметно становиться implementation assumption.
- First user сохраняет product authority над своим product content, не принимая ненужные технические решения.
- Result можно проверить без repository, network, CI и Git.
- Job создаёт upstream product contracts для последующих stages, но не смешивается с Task Brief или execution.

### 5.2. First-job success condition

После review first user способен своими словами объяснить:

1. для кого предназначен first slice;
2. какую проблему он решает;
3. какое observable behavior ожидается;
4. что сознательно не входит;
5. какие assumptions и material unknowns остались;
6. какой exact frozen review bundle (`C-003 + C-002`) он принимает или почему не принимает;
7. какое one next action допустимо.

### 5.3. Authority-role rule

`AOS_PRODUCT_OWNER` принимает exact C0 package как стратегию разработки самого AOS. `DOMAIN_EXPERT_PRODUCT_OWNER` является persona первого пользовательского journey и принимает будущие first-slice Product artifacts. Совпадение physical person не переносит decision автоматически между subjects и не отменяет exact binding.

## 6. `C0-D02` — First Core vertical slice

```yaml
decision_id: C0-D02
slice_id: CORE-SLICE-001
slice_name: INTENT_TO_ACCEPTED_FIRST_FEATURE_PASSPORT
selection_status: PROPOSED
recommended_option: S-A
layer: PRODUCT_RUNTIME
user_repository_access: NOT_REQUIRED
user_repository_mutation: FORBIDDEN
aos_state_mutation: REQUIRED
aos_state_write_authority: EXPLICIT_LOCAL_OPERATION_ONLY
write_model: ATOMIC_OR_JOURNALED
partial_write_recovery: REQUIRED
code_execution: FORBIDDEN
git_actions: FORBIDDEN
core_network_requirement: NONE
```

### 6.1. Actor and trigger

**First-slice product decision actor:** `DOMAIN_EXPERT_PRODUCT_OWNER`.

Это не actor принятия C0. Exact C0 package принимает `AOS_PRODUCT_OWNER` согласно §13.

**Trigger:** человек вводит free-form описание новой software product idea или capability. Input может быть неполным, solution-biased или internally inconsistent.

### 6.2. Inputs

- immutable original request;
- optional context/background;
- known constraints;
- explicit non-goals, если известны;
- answers только на material clarification questions;
- sensitive/provider flags, если применимо.

### 6.3. Observable outputs

1. immutable original request;
2. exact revision `C-001 Intent Record`;
3. exact revision minimal-depth `C-003 Product Spec`;
4. exact revision одного first-slice `C-002 Feature Passport`;
5. derived review view с differences, assumptions, unknowns и limitations;
6. separate `C-011`-compatible `HumanDecisionRecord`, bound к exact subject;
7. derived `Status / Next / Details` view.

### 6.4. Minimal flow

```text
free-form intent
→ preserve original input
→ separate problem/outcome from proposed solution
→ detect sensitive/provider boundary
→ ask only material questions
→ draft C-001 Intent Record
→ draft minimal-depth C-003 Product Spec
→ draft one C-002 Feature Passport
→ deterministic schema/completeness/consistency checks
→ render exact review subject
→ explicit human-controlled decision:
   ACCEPT | NEEDS_CHANGES | REJECT | DEFER
→ persist separate decision record
→ show one bounded next action
```

### 6.5. Contract ownership

| Fact class | Owner in `CORE-SLICE-001` | Must not own |
|---|---|---|
| Original request, initial problem/outcome, source, assumptions/unknowns | `C-001 Intent Record` | Feature state machine, architecture, execution permission |
| Product-level user/JTBD, goal, boundary, non-goals, candidate metrics, open decisions | minimal-depth `C-003 Product Spec` | Detailed behavior of the selected feature, Task Brief |
| First-slice trigger, I/O, flow, states, failures/recovery, acceptance and negatives | one `C-002 Feature Passport` | Project-wide roadmap, execution authorization |
| Human decision | separate `C-011`-compatible record | Product content, technical result, Git permission |
| Status/next/details | derived view | Independent product truth or approval |

`First Slice Contract` — это роль exact revision `C-002 Feature Passport`, а не новый shared contract class.

### 6.6. Orthogonal state model

Одна composite lifecycle chain не используется. Оси сохраняются независимо.

```yaml
workflow_state:
  enum:
    - INTAKE_EMPTY
    - INTAKE_CAPTURED
    - CLARIFICATION_REQUIRED
    - CONTRACT_ASSEMBLY
    - REVIEW_READY
    - DECISION_RECORDED
  role: PRODUCT_WORKFLOW_PROGRESS_ONLY

document_maturity:
  enum:
    - DRAFT
    - HUMAN_REVIEW_REQUIRED
    - HUMAN_ACCEPTED
    - SUPERSEDED
  role: ARTIFACT_MATURITY_ONLY

technical_result:
  enum:
    - CONTRACT_VIOLATION
    - FAIL
    - BLOCKED
    - UNKNOWN
    - NOT_RUN
    - PASS
  role: DETERMINISTIC_CHECK_RESULT_ONLY

human_decision:
  nullable: true
  enum_when_present:
    - ACCEPT
    - NEEDS_CHANGES
    - REJECT
    - DEFER
  role: EXPLICIT_HUMAN_DECISION_ONLY

permission:
  enum:
    - ALLOWED
    - HUMAN_AUTHORIZATION_REQUIRED
    - BLOCKED_POLICY
    - BLOCKED_UNKNOWN
    - NOT_APPLICABLE
  role: EVALUATED_PER_REQUESTED_OPERATION
```

Rules:

1. `PASS` означает только, что exact revision прошла объявленные deterministic checks.
2. `REVIEW_READY` и `HUMAN_REVIEW_REQUIRED` не означают acceptance.
3. `human_decision` остаётся `null`, пока нет valid explicit human-controlled action.
4. `ACCEPT` не переводит project в `EXECUTE` и не создаёт Task Brief.
5. Любое content change создаёт новую revision; старый decision не переносится.
6. `NEEDS_CHANGES` закрывает decision для old revision и создаёт только основание для successor revision.
7. Workflow progress не изменяет maturity, technical result, decision или permission автоматически.

Derived view разрешён только как вычисление:

```text
ACCEPTED_FIRST_FEATURE_PASSPORT =
  product_spec_maturity == HUMAN_ACCEPTED
  AND feature_passport_maturity == HUMAN_ACCEPTED
  AND product_package_human_decision == ACCEPT
  AND package_manifest_binding == VALID
  AND product_spec_dependency_binding == CURRENT
```

`ACCEPTED_FIRST_FEATURE_PASSPORT` не является самостоятельным authority-bearing state.

### 6.7. Operation permission mapping

| Requested operation | Permission rule |
|---|---|
| Create/update DRAFT AOS-local artifact revision | `ALLOWED` только через explicit local operation и accepted store boundary |
| Record Human Decision | `HUMAN_AUTHORIZATION_REQUIRED`; requires explicit human intent, exact subject binding and a human-controlled capture action |
| Agent-generated acceptance | `BLOCKED_POLICY` |
| Mutate user repository | `BLOCKED_POLICY` |
| Execute code or commands in user project | `BLOCKED_POLICY` |
| Commit / Push / Merge / Release | `BLOCKED_POLICY` |
| No operation requested | `NOT_APPLICABLE` |

### 6.8. Failure and recovery boundary

| Failure | Required behavior | Recovery |
|---|---|---|
| Request materially empty | `CLARIFICATION_REQUIRED`; no fabricated contract | Ask one bounded clarification set |
| Contradictory answers | Show `CONFLICT`; do not choose a side | Human resolves; create new DRAFT revision |
| Agent adds unsupported claim | Mark `ASSUMPTION`; no promotion to fact | Human confirms, rejects or leaves unknown |
| Generated text claims approval | Reject decision record | Require explicit human-controlled action bound to the exact subject |
| Decision subject digest/revision mismatch | Mark decision invalid/stale | Re-render exact subject and request new decision |
| Partial AOS-state write | Do not expose new revision as durable/current | Detect journal/transaction state, reconcile, recover previous durable revision |
| Accepted content is edited | Preserve old decision against old bytes only | Create successor revision and new review cycle |
| External agent/network unavailable | Core remains usable without provider | Use manual structured-input fallback |
| Sensitive data lacks provider policy | Block external-agent route only | Continue through approved local/manual boundary or obtain policy decision |

Automatic retry is forbidden when scope, subject identity, permission or human-decision requirement changes.

### 6.9. Acceptance scenarios for the next contract artifact

1. Empty or materially incomplete idea produces `CLARIFICATION_REQUIRED`, not a fabricated contract.
2. Sufficient input produces exactly one bounded first-slice proposal, not a roadmap/platform.
3. Added assumptions are visible and distinct from human-provided facts.
4. Minimal `C-003` and `C-002` have non-overlapping fact ownership.
5. `C-002` contains observable value, non-goals, failures/recovery, acceptance and negative scenarios.
6. Technical `PASS` does not create a human decision.
7. `ACCEPT` binds to exact immutable subject and creates no execution/Git permission.
8. Partial-write interruption leaves either the previous durable revision or a recoverable journal, never a false completed revision.
9. After terminal decision, the view shows exactly one bounded next action.

### 6.10. Required negative scenarios

- agent chooses architecture of the user's product without a separate decision;
- legacy feature presence becomes a requirement automatically;
- system creates multiple competing first slices instead of one decision-ready proposal;
- `UNKNOWN` or `NOT_RUN` is hidden behind `PASS`/confidence wording;
- old acceptance is reused after revision or digest change;
- unbound, inferred or agent-authored UI/chat text becomes approval without a valid decision record;
- operator or agent is falsely attributed as decision actor;
- workflow continues into Task Brief or implementation automatically;
- partial write exposes corrupted/new state as current;
- provider/network becomes mandatory for core operation.

### 6.11. Scoped feature relations

Acceptance of C0 does **not** change canonical `human_disposition` in `06_Features.md`. It accepts only the following slice-scoped relations:

| Feature | Catalog human disposition | Catalog changed | Slice behavior selection | Selected behaviors |
|---|---|---|---|---|
| `FTR-001` | `UNDECIDED` | false | `REQUIRED` | preserve original intent; material clarification; explicit assumptions/unknowns; one next route |
| `FTR-003` | `UNDECIDED` | false | `REQUIRED` | minimal `C-003`; one full first-slice `C-002`; exact human slice decision |
| `FTR-008` | `UNDECIDED` | false | `REQUIRED` | derived display-only `Status / Next / Details` |
| `FTR-012` | `UNDECIDED` | false | `REQUIRED` | exact review subject; explicit human decision record; generated decision rejection |
| `FTR-016` | `UNDECIDED` | false | `REQUIRED` | local revision continuity and resume for this slice only |

```yaml
relation_scope: CORE-SLICE-001_ONLY
catalog_disposition_authority: UNCHANGED
full_dossier_admission: NOT_PERFORMED
```

## 7. `C0-D03` — Minimal architecture of AOS

`C0-D03` является embedded `C-004 Architecture Decision Record`. До package-level `ACCEPT` он остаётся `HUMAN_REVIEW_REQUIRED` proposal. Frozen ADR bytes не переписываются после решения: accepted ADR view вычисляется только из exact package и valid subject-bound `C-011` Human Decision Record.

### 7.1. Embedded `C-004 ADR`

```yaml
adr_id: ADR-AOS-C0-001
decision_id: C0-D03
contract_class: C-004
document_maturity: HUMAN_REVIEW_REQUIRED
question: >-
  Какая минимальная architecture самого AOS достаточна для
  CORE-SLICE-001 без преждевременного Development Factory,
  Control Plane, distributed services или provider lock-in?
context:
  - first user is a nontechnical domain expert/product owner
  - first slice creates and reviews local product artifacts
  - user repository access and code execution are out of scope
  - agent output is probabilistic and cannot own authority
constraints:
  - local-first operation
  - single-user first version
  - replaceable interaction and agent adapters
  - deterministic validation and authority checks
  - atomic or journaled writes
  - structured canonical state with rebuildable human views
  - no database, RAG, multi-agent orchestration or SaaS dependency
options:
  - id: A-A
    name: PROMPT_AND_MARKDOWN_ONLY
    summary: No deterministic runtime or durable state core
  - id: A-B
    name: LOCAL_FIRST_MODULAR_MONOLITH
    summary: Deterministic core, product application layer, local store and thin adapters
  - id: A-C
    name: LOCAL_WEB_APPLICATION
    summary: Local frontend/backend as first interface
  - id: A-D
    name: DISTRIBUTED_CONTROL_PLATFORM
    summary: Services, registries, RAG and multi-agent runtime
tradeoffs:
  - option: A-A
    value: lowest setup cost
    cost: weak machine-verifiable contracts, state and authority separation
  - option: A-B
    value: smallest real runtime with replaceable internals and offline core
    cost: requires explicit storage/recovery and operator flow contracts
  - option: A-C
    value: stronger onboarding potential
    cost: premature frontend/backend and deployment complexity
  - option: A-D
    value: future scale and orchestration
    cost: unjustified platform complexity and larger failure surface
evidence:
  - 00_Core.md §§10–13
  - 01_Product.md §§8, 11–14
  - 02_Architecture.md §§2–5, 7–17
  - 03_Development.md §§13, 15, 21–22
  - 06_Features.md FTR-001, FTR-003, FTR-008, FTR-012, FTR-016
selected_option: A-B_LOCAL_FIRST_MODULAR_MONOLITH
selection_status: PROPOSED_UNTIL_PACKAGE_ACCEPT
human_decision_identity: PENDING
acceptance_binding:
  satisfied_by: AOS_C0_HUMAN_DECISION
  required_subject_binding:
    package_id: AOS-C0
    package_revision: C0-R4
    sha256: REQUIRED
    selected_decision_id: C0-D03
accepted_adr_view:
  authority_source: VALID_C011_SUBJECT_BINDING_ONLY
  maturity_before_valid_accept: HUMAN_REVIEW_REQUIRED
  maturity_after_valid_accept: HUMAN_ACCEPTED
  required_conditions:
    - package decision is ACCEPT
    - accepted decision ids include C0-D03
    - package revision and sha256 match exact frozen bytes
    - decided_by actor role is AOS_PRODUCT_OWNER
  invalid_or_missing_binding_result: HUMAN_REVIEW_REQUIRED
consequences:
  - deterministic core owns schemas, validation, authority rules and revision binding
  - product application layer owns intake/specification/review orchestration
  - local structured files own canonical durable state
  - Markdown/text views are derived and rebuildable
  - local interaction port and agent adapter are replaceable ports
  - first slice has no Development Factory dependency
reversal_conditions:
  - measured nontechnical-user friction requires another interface
  - concurrency or collaboration requires multi-user state
  - filesystem store fails measured reliability/scale requirements
  - deployment/compliance boundary justifies service split
  - provider/privacy requirements invalidate current adapter boundary
```

The accepted ADR view is derived; `document_maturity` inside frozen `C0-R4` remains an immutable statement about the proposal bytes and is not mutated by the later decision record.

### 7.2. Architecture summary

```yaml
architecture_style: LOCAL_FIRST_MODULAR_MONOLITH
operating_model: SINGLE_USER_SINGLE_PROCESS
initial_interaction_boundary: LOCAL_FIRST_REPLACEABLE_HUMAN_INTERACTION_PORT_WITH_OPTIONAL_AGENT_MEDIATION
canonical_state: VERSIONED_STRUCTURED_FILES
human_view: DERIVED_MARKDOWN_OR_TEXT
llm_role: UNTRUSTED_PROPOSAL_PROVIDER
core_network_requirement: NONE
external_agent_network: OUTSIDE_CORE_BOUNDARY
manual_structured_fallback: REQUIRED
embedded_database: NONE
services: NONE
execution_engine: NONE
git_automation: NONE
full_control_plane: NONE
```

### 7.3. Minimal component map

```text
First-slice human decision actor
   │
   ▼
Interaction Port
(local guided command surface; optional agent mediation)
   │ proposals / explicit local actions
   ▼
Product Application Layer
(Intake + Product Context + First Slice Builder + Review)
   │
   ▼
Deterministic Domain Core
(contracts + validation + orthogonal state + revision binding + authority)
   │
   ├──────────────► Derived Status Renderer
   │                (Status / Next / Details)
   ▼
Local Revision Store
(versioned structured artifacts + immutable decision records)
```

### 7.4. Proposed module boundaries

| Module boundary | Owns | Must not own in first slice |
|---|---|---|
| `aos_core` | contract schemas, orthogonal status semantics, revision identity, authority checks, deterministic validation | prompts, UI, repository execution |
| `aos_product` | intake, minimal Product Spec, first Feature Passport, review application services | Task Brief, executor, Git actions |
| `aos_storage` | atomic/journaled artifact revisions, loading, recovery metadata, decision-record persistence | product inference, approval logic |
| `aos_cli` or equivalent local port | commands, rendering, human-controlled action capture when implemented by this port | canonical state or independent decisions |
| `agent_adapter` | transform conversation into non-authoritative proposals | durable direct writes, authority, acceptance |

Names являются topology candidates; language/package layout остаются `UNDECIDED`. `aos_factory` не входит в first slice.

### 7.5. Actor, operator and decision channel

```yaml
c0_package_decision_actor:
  role: AOS_PRODUCT_OWNER
  authority_scope: C0_PACKAGE_ONLY
first_slice_product_decision_actor:
  role: DOMAIN_EXPERT_PRODUCT_OWNER
  authority_scope: FIRST_SLICE_PRODUCT_ARTIFACTS
same_human_may_hold_both_roles: true
interaction_operator:
  default: SAME_HUMAN
  allowed_assistance: TRUSTED_HUMAN_OPERATOR
proposal_provider: AGENT_ADAPTER_OR_MANUAL_INPUT
decision_capture_requirement:
  class: HUMAN_CONTROLLED_EXPLICIT_ACTION
  implementation: UNDECIDED
  exact_subject_binding: REQUIRED
  explicit_human_intent: REQUIRED
  agent_inference_or_autonomous_submission: INVALID
identity_assurance:
  current_model: HUMAN_CONTROLLED_SELF_ATTESTATION
  cryptographic_identity_assurance: NOT_CLAIMED
first_dogfood_setup: FACILITATED_LOCAL_SESSION
```

Rules:

1. `AOS_PRODUCT_OWNER` is the only actor role that may accept or reject the C0 strategy package.
2. `DOMAIN_EXPERT_PRODUCT_OWNER` remains the decision actor for future first-slice product content.
3. The same physical human may hold both roles, but each record must name the role matching its exact subject.
4. A trusted human operator or deterministic capture component may persist a record but never owns or substitutes the decision.
5. Agent adapter may prepare proposals, templates and exact decision subjects; it cannot infer, submit or validate a human decision autonomously.
6. Valid capture requires explicit human intent and exact revision/digest binding. The concrete mechanism remains `UNDECIDED` at C0.
7. First dogfood may be facilitated because product bootstrap/installer is not part of this slice.
8. Self-attestation does not prove physical identity; multi-user, remote and cryptographic assurance remain out of scope.

### 7.6. Initial interface

The minimal architecture requires a thin, local-first, replaceable human interaction port. A CLI is the preferred engineering candidate for deterministic tests, but C0 does not require CLI as the sole user interface or human-decision capture mechanism. Agent-mediated, facilitator-guided, signed-file, desktop or other human-controlled mechanisms remain possible if they satisfy exact binding and explicit-intent requirements.

Candidate actions for the next contract artifact:

```text
intake
review
accept <subject-revision> <subject-digest>
needs-changes <subject-revision> <subject-digest>
reject <subject-revision> <subject-digest>
defer <subject-revision> <subject-digest>
status
next
details
```

Exact command syntax, UI and decision-capture implementation are not selected by C0.

### 7.7. Persistence and recovery direction

- canonical artifacts are structured, versioned local files;
- human-readable Markdown/text is a derived view;
- each content change creates a new immutable revision;
- Human Decision Record is a separate immutable object;
- decision binding includes exact revision and digest;
- each fact class has one owner;
- writes are atomic or journaled before first durable mutation;
- partial-write detection and reconciliation are mandatory;
- database and network service are not required;
- exact path, serialization and digest profile are selected later.

### 7.8. Network and provider boundary

```yaml
core_network_requirement: NONE
external_agent_network: OUTSIDE_CORE_BOUNDARY
external_agent_output_authority: NONE
manual_or_offline_proposal_fallback: REQUIRED
provider_data_policy_before_sensitive_dogfood: REQUIRED
hidden_network_calls: FORBIDDEN
```

Core must remain usable with manual structured input when no external model/provider is available. Sensitive data may not be routed to an external provider until the applicable data/provider policy is explicitly decided.

### 7.9. Deferred complexity

Not in the minimal architecture:

- user-repository scanner/discovery runtime;
- Task Brief compiler;
- preflight/preview for code execution;
- execution adapters and runner kernels;
- validation/evidence pipeline for implementation candidates;
- Commit/Push/Merge/Release automation;
- central registry or full Control Plane;
- database, vector DB or RAG;
- autonomous loops or multi-agent cascade;
- plugin marketplace;
- web/SaaS backend;
- model/provider routing;
- domain modules, including medical behavior.

## 8. `C0-D04` — Product artifact relation for `CORE-SLICE-001`

```yaml
decision_id: C0-D04
selection_status: PROPOSED
recommended_option: P-B_MINIMAL_C003_PLUS_ONE_C002
scope: CORE-SLICE-001_ONLY
accepted_journey_deviation: NONE
new_contract_class_created: false
```

### 8.1. Selected policy if accepted

1. `C-001 Intent Record` owns original request, initial actor/problem/outcome, source, assumptions and unknowns.
2. Existing `C-003 Product Spec` is created at **minimal first-slice depth**, not as a new `ProductSpecEnvelope` contract class.
3. `C-003` owns product-level first user/JTBD, product goal, boundary, non-goals, candidate success metrics and open decisions required to contextualize the first slice.
4. One `C-002 Feature Passport` owns exact first-slice observable behavior.
5. `C-002` references `C-003` by identity/revision instead of duplicating product-level facts.
6. Full Product Spec expansion, multi-feature roadmap and Product Feature Registry remain outside `CORE-SLICE-001`.

### 8.2. Minimum `C-003` depth for first slice

```yaml
required_product_spec_fields:
  - product_problem
  - first_user_and_jtbd
  - first_product_goal
  - first_user_journey
  - first_slice_boundary
  - product_non_goals
  - material_constraints
  - candidate_success_metrics
  - product_level_dependencies
  - product_acceptance_boundary
  - open_decisions
optional_or_unknown_fields:
  - broader_journeys
  - additional_user_segments
  - multi_feature_roadmap
  - registry_policy
  - expansion_metrics_thresholds
```

Material absence is represented as explicit `UNKNOWN` with a resolution path; it is not silently fabricated.

### 8.3. Remaining open policy

The exact trigger for expanding minimal `C-003` into a broader Product Spec remains `UNDECIDED`. This blocks only broader product-spec expansion, not C0 selection or preparation of the first-slice Product Contract.

## 9. Consequences

### 9.1. Positive consequences

- AOS begins with direct product value rather than Governance or execution infrastructure.
- First slice is dogfoodable without access to a user implementation repository.
- `C-001`, `C-003`, `C-002` and `C-011` retain distinct ownership.
- Deterministic core separates probabilistic proposal generation from authority-bearing state.
- Local structured persistence supports portability and recovery without database dependency.
- Next artifact can remain one feature-specific Product Contract rather than a full-system specification.

### 9.2. Costs and tradeoffs

- Initial local command surface is not final nontechnical UX.
- Facilitated first dogfood is required before product bootstrap exists.
- Minimal `C-003` adds one artifact and requires strict deduplication.
- Clarification quality partly depends on the proposal provider until measured policy is designed.
- Filesystem persistence requires exact transaction/journal and recovery contracts.
- Self-attested local decisions do not provide cryptographic or multi-user identity assurance.
- First slice does not demonstrate repository execution, validation or Git delivery.

## 10. Conflicts, risks and unknowns

### 10.1. Confirmed conflict

| ID | Classification | Description | Affected action | Resolution |
|---|---|---|---|---|
| `C0-C01` | `CONFLICT` | `00_Core.md` places `HUMAN_REVIEW_REQUIRED` in technical results, while `02_Architecture.md` places it in document maturity | Final global status schema implementation | C0 uses the scoped orthogonal mapping from `02_Architecture.md`; accepted baseline owner must be synchronized before implementation |

This conflict does not block selection of user/job, slice or architecture. It blocks only claiming a final global status schema without a later baseline correction.

### 10.2. Material unknowns

| ID | Classification | Unknown | Effect | One resolution step |
|---|---|---|---|---|
| `C0-U01` | `UNKNOWN` | Exact expansion trigger for broader `C-003` | Blocks only broader Product Spec depth | Define in `FIRST_SLICE_PRODUCT_CONTRACT_R1` or first dogfood review |
| `C0-U02` | `UNKNOWN` | Exact persistence path, serialization and digest profile | Blocks implementation contract | Compare minimal deterministic profiles before scaffolding |
| `C0-U03` | `UNKNOWN` | Language/toolchain/dependencies | Blocks code/scaffold selection | Separate human architecture/toolchain decision |
| `C0-U04` | `UNKNOWN` | Minimum clarification policy | May affect UX and false assumptions | Define material-question rules and dogfood measurements |
| `C0-U05` | `UNKNOWN` | Implementation repository | Blocks repository planning/execution | Separate human decision |
| `C0-U06` | `UNKNOWN` | First dogfood product idea and facilitator | Blocks representative dogfood only | Select one low-sensitivity real idea and named setup role |
| `C0-U07` | `UNKNOWN` | Metrics thresholds | Blocks success claims, not data collection | Collect first dogfood baseline, then decide thresholds |
| `C0-U08` | `UNKNOWN` | Provider/privacy policy | Blocks sensitive external-agent use | Define data/provider boundary before sensitive dogfood |

### 10.3. Main risks

| ID | Risk | Consequence | Mitigation |
|---|---|---|---|
| `C0-R01` | Agent-mediated surface hides core limitations | False autonomy claim | Show proposal provenance, deterministic result and manual fallback |
| `C0-R02` | Slice expands into planning platform | Delayed product learning | One product context, one feature, no roadmap/backlog generation |
| `C0-R03` | Human acceptance is mistaken for execution permission | Authority violation | Orthogonal states, explicit non-authorizations and negative tests |
| `C0-R04` | Minimal `C-003` duplicates `C-002` | SoT drift | Exact ownership table and reference-by-identity |
| `C0-R05` | Local file write fails partially | Corrupt or false current state | Atomic/journaled write, previous durable revision, recovery package |
| `C0-R06` | Operator is mistaken for decision actor | Invalid authority | Separate `decided_by` and `recorded_by`; explicit human-controlled confirmation |
| `C0-R07` | Sensitive content reaches external provider without policy | Privacy breach | External route blocked; local/manual fallback |

## 11. First dogfood measurement candidate

Metrics are collected during manual dogfood; thresholds remain `UNDECIDED` until evidence exists.

```yaml
dogfood_metrics:
  time_intent_to_review_ready:
    threshold: UNDECIDED
  material_clarification_loops:
    threshold: UNDECIDED
  hidden_assumptions_detected:
    threshold: UNDECIDED
  unresolved_material_unknowns_at_decision:
    threshold: UNDECIDED
  revision_count_before_terminal_decision:
    threshold: UNDECIDED
  user_comprehension_check:
    method: USER_EXPLAINS_ACTOR_PROBLEM_OUTCOME_NON_GOALS_UNKNOWNS_NEXT_ACTION
    threshold: UNDECIDED
  authority_confusion_incidents:
    threshold: UNDECIDED
  operator_assistance_events:
    threshold: UNDECIDED
  stale_or_invalid_decision_binding_attempts:
    threshold: UNDECIDED
```

One successful case demonstrates the first slice only; it does not establish a stable Product Core.

## 12. Recommended human decision

Accept `C0-R4` as one package-level decision:

```yaml
recommended_human_decision:
  subject:
    package_id: AOS-C0
    package_revision: C0-R4
    sha256: REQUIRED_FROM_FROZEN_FILE
    selected_decision_ids:
      - C0-D01
      - C0-D02
      - C0-D03
      - C0-D04
  decided_by_role: AOS_PRODUCT_OWNER
  decision: ACCEPT
  selections:
    C0-D01: U-A_DOMAIN_EXPERT_TO_FIRST_PRODUCT_PACKAGE
    C0-D02: S-A_INTENT_TO_ACCEPTED_FIRST_FEATURE_PASSPORT
    C0-D03: A-B_LOCAL_FIRST_MODULAR_MONOLITH
    C0-D04: P-B_MINIMAL_C003_PLUS_ONE_C002
  explicit_non_authorizations:
    implementation: NONE
    user_repository_mutation: NONE
    code_execution: NONE
    git_actions: NONE
```

### 12.1. Dependency matrix

| Decision | Constrains or depends on | Why package consistency matters |
|---|---|---|
| `C0-D01` | constrains `C0-D02` | Slice must solve the selected first user's job |
| `C0-D02` | depends on `C0-D04` | Slice output requires exact Product artifact ownership |
| `C0-D02` + `C0-D04` | constrain `C0-D03` | Architecture must support deterministic local artifacts, review and decision binding |
| `C0-D03` | enables `C0-D02` | Persistence, authority and recovery boundaries are required for the selected slice |

Package-level all-or-nothing handling is an **operational consistency rule**, not a claim that partial acceptance is logically impossible. This revision does not encode mixed accepted/rejected combinations. A human request for partial acceptance must use `NEEDS_CHANGES` and produce a successor package that explicitly records the desired combination.

## 13. Human Decision Record contract

### 13.1. Package-level template

```yaml
decision_record_type: AOS_C0_HUMAN_DECISION
decision_record_revision: R1
subject:
  package_id: AOS-C0
  package_revision: C0-R4
  sha256: '<sha256 of exact frozen AOS_C0_Decision_Package_R4.md bytes>'
  selected_decision_ids:
    - C0-D01
    - C0-D02
    - C0-D03
    - C0-D04
decision: ACCEPT | NEEDS_CHANGES | REJECT | DEFER
accepted_decision_ids: []
requested_changes: []
comment: ''
decided_by:
  actor_role: AOS_PRODUCT_OWNER
  actor_identity: '<human-controlled identity>'
recorded_by:
  recorder_class: SAME_HUMAN | TRUSTED_HUMAN_OPERATOR | DETERMINISTIC_CAPTURE_COMPONENT
  recorder_identity: '<actual recorder identity>'
capture_channel:
  class: HUMAN_CONTROLLED_EXPLICIT_ACTION
  implementation: '<actual mechanism identifier; not selected by C0>'
  explicit_human_intent: true
agent_generated_decision: false
recorded_at: '<timestamp>'
implementation_authorization: NONE
execution_authorization: NONE
git_authorization: NONE
```

### 13.2. Validation rules

1. For `ACCEPT`, `accepted_decision_ids` must equal exactly `[C0-D01, C0-D02, C0-D03, C0-D04]` and `requested_changes` must be empty.
2. For `NEEDS_CHANGES`, `REJECT` or `DEFER`, `accepted_decision_ids` must be empty.
3. A material condition is not encoded as conditional `ACCEPT`; it requires `NEEDS_CHANGES` and a new package revision.
4. `decided_by.actor_role` must be `AOS_PRODUCT_OWNER` for the C0 package. The future first-user role does not satisfy this package authority automatically.
5. Missing human actor identity, timestamp, digest or digest match makes the record invalid.
6. `capture_channel.class` must be `HUMAN_CONTROLLED_EXPLICIT_ACTION`; its concrete implementation may vary.
7. The channel must preserve explicit human intent and exact subject binding. Agent inference, autonomous submission or generated approval is invalid.
8. `recorded_by` owns persistence provenance only. It does not become the decision actor.
9. `agent_generated_decision` must be `false`.
10. Any content change creates new bytes; the old decision applies only to the old digest.
11. `ACCEPT` creates product/architecture authority only in the declared C0 scope. It creates no implementation, execution or Git authorization.

### 13.3. Exact short decision form

The short form must include the digest of the frozen file. It may be expressed through any human-controlled explicit channel and then persisted as a valid structured record. Copying or editing the Markdown requires recomputing the detached checksum before decision capture.

```text
AOS C0 ACCEPT C0-R4 SHA256:<exact-digest>
```

Equivalent forms are allowed for `NEEDS_CHANGES`, `REJECT` and `DEFER`, but only a valid structured Human Decision Record owns the decision fact.

## 14. Next bounded action and pre-acceptance boundary

Current next bounded action:

```yaml
action: HUMAN_REVIEW_EXACT_C0_R4
subject_binding:
  package_id: AOS-C0
  package_revision: C0-R4
  sha256: REQUIRED_FROM_DETACHED_CHECKSUM
allowed_outcomes:
  - ACCEPT
  - NEEDS_CHANGES
  - REJECT
  - DEFER
```

Before C0 acceptance, no downstream Product Contract, implementation planning or repository execution may begin. Safe pre-acceptance support actions remain allowed:

- read-only audit and conflict/gap analysis;
- persistence of exact frozen artifacts to an explicitly permitted path;
- exact-content, checksum and repository-presence validation;
- preparation of a decision-record template without supplying the human decision;
- creation of a successor revision when requested.

After valid human `ACCEPT` of exact `C0-R4`, create:

```yaml
artifact_id: FIRST_SLICE_PRODUCT_CONTRACT_R1
phase_id: UNASSIGNED
scope: CORE-SLICE-001_ONLY
authority: PROPOSAL_UNTIL_HUMAN_ACCEPTANCE
implementation_authorization: NONE
execution_authorization: NONE
git_authorization: NONE
```

It must define:

- exact schemas and identities for `C-001`, minimal-depth `C-003`, `C-002` and `C-011` record;
- field ownership and non-duplication rules;
- product workflow transitions and orthogonal status mapping;
- deterministic validation rules;
- atomic/journaled write and recovery semantics;
- human-controlled decision capture requirements and operator flow;
- acceptance cases and executable negative tests;
- manual/offline fallback;
- dogfood protocol and measurement capture.

It must not select implementation repository, language/toolchain, dependencies, Task Brief, Execution Authorization or Git actions.

## 15. Audit corrections applied

### 15.1. Corrections from `AOS-C0-R3-READ-ONLY-REVIEW`

| Review finding | Correction in `C0-R4` |
|---|---|
| `P1-01_SOURCE_BASELINE_IDENTITY_MISMATCH` | Bound `R4-RU` to exact current repository, branch, HEAD, `docs/00_Core.md` blob and exact file package identity; retained `c7b3f166...` only as `audited_predecessor_commit` |
| `P1-02_DETACHED_CHECKSUM_NOT_AVAILABLE_FOR_VERIFICATION` | Frozen package records `detached_checksum_validation: NOT_RUN`; detached checksum comparison is performed only after freeze and reported in separate Evidence |

### 15.2. Corrections preserved from `AOS-C0-R2-INDEPENDENT-AUDIT`

| Audit finding | Correction in `C0-R4` |
|---|---|
| `P1-01` C0 authority confused with future first user | Added distinct `AOS_PRODUCT_OWNER` and `DOMAIN_EXPERT_PRODUCT_OWNER` roles with non-collapsible authority scopes |
| `P1-02` capture mechanism prematurely fixed | Replaced `DIRECT_LOCAL_HUMAN_ACTION` with property-level `HUMAN_CONTROLLED_EXPLICIT_ACTION`; concrete implementation remains `UNDECIDED` |
| `P1-03` safe pre-acceptance actions forbidden | Explicitly allowed bounded audit, persistence, checksum/repository validation, decision-template preparation and successor revision |
| `P2-01` package-level decision rationale weak | Added dependency matrix and classified all-or-nothing handling as an operational consistency rule |
| `P2-02` package permission ambiguous | Replaced scalar `permission` with `package_operation_permission` and explicit downstream permission map |
| `P2-03` technical result insufficiently granular | Added separate artifact/checksum/repository/runtime technical results; independent semantic validation remains `NOT_RUN` |
| `P2-04` embedded ADR acceptance identity incomplete | Added derived accepted-ADR conditions bound to valid `C-011`, exact revision, digest, selected ID and `AOS_PRODUCT_OWNER` role |

### 15.3. Direction intentionally unchanged

```yaml
C0-D01: U-A_DOMAIN_EXPERT_TO_FIRST_PRODUCT_PACKAGE
C0-D02: S-A_INTENT_TO_ACCEPTED_FIRST_FEATURE_PASSPORT
C0-D03: A-B_LOCAL_FIRST_MODULAR_MONOLITH
C0-D04: P-B_MINIMAL_C003_PLUS_ONE_C002
```

Corrections already introduced in `C0-R2`—orthogonal states, explicit `C-003` relation, embedded ADR ownership, SHA-256 binding, split user-repository/AOS-state boundary, scoped feature relations, non-`ACCEPT` semantics, phase-ID correction, metrics and offline/provider boundary—remain preserved.

`C0-R4` remains a `PROPOSAL`. This correction does not create a Human Decision Record and provides no implementation, execution or Git authorization.
