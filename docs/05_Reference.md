---
package: AOS_Project_Knowledge_Baseline
package_revision: R4-RU
updated: '2026-09-13'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
current_change_subject: AOS_SCAFFOLD_CORE_DOCUMENTATION_R1
current_change_authority: CURRENT_EXPLICIT_HUMAN_INSTRUCTION
current_change_status: SCAFFOLD_CORE_DRAFT
current_change_agent_review: PASS
current_change_agent_review_scope: DOCUMENTATION_AUTHOR_SELF_CHECK
current_change_human_review: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
semantic_audit: COMPLETED_WITH_CORRECTIONS
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
audited_source_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
audited_source_blob_sha: b978777097f08d544b9e02f08cf5716ea199998c
active_path: docs/05_Reference.md
document_language: ru
technical_identifiers_language: en
document_role: REFERENCE_AND_PROVENANCE_REGISTRY
authority_scope:
- source_provenance
- snapshot_identity
- targeted_research_routes
reference_authority_for_target_aos: NONE
---

# 05 — Источники и provenance

## 1. Назначение

Документ является единым provenance и research-routing layer. Он не является Product Contract, Architecture Contract, implementation authorization или источником полномочий legacy.

```text
reference occurrence ≠ current implementation
historical acceptance ≠ current acceptance
source mapping ≠ target requirement
stored PASS ≠ current PASS
GitHub URL ≠ загруженный source ChatGPT Project
```

## 2. Классы источников и authority

| Класс источника | Использование | Authority |
|---|---|---|
| Current explicit human decision | Exact decision boundary | Human-scoped |
| Accepted project artifact | Declared fact class | Fact-class scoped |
| Current repository observation | Mutable snapshot facts | Observation only |
| Historical repository snapshot | Behavior, failure, prior art | `NONE` for target |
| Chat summary, note или report | Intent, lessons, candidates | `NONE` |
| Generated synthesis | Navigation и inference | `NONE` |

## 3. Текущая принятая база знаний

```yaml
repository: NMF13579/notebook
branch: dev
audited_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
active_path: docs/
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
implementation_authorization: NONE
git_authorization: NONE
```

Текущие семь документов являются активными owners своих fact classes. Состояние ветки после указанного commit должно проверяться непосредственно перед mutable repository claim.

## 4. Provenance объединённого пакета

До консолидации исходные synthesis-наборы находились в `AOS-FARM/` и `AgentOS/` внутри `notebook`. Они доступны через Git history, а не как live paths:

```yaml
historical_notebook_commit: a27a47ed0a1610115ff88f4da6a898a1aaff778b
former_source_paths:
  - AOS-FARM/00_Core.md ... AOS-FARM/06_Features.md
  - AgentOS/00_Core.md ... AgentOS/06_Features.md
live_status: REMOVED_AFTER_SYNTHESIS
```

Отсутствие этих paths в текущем tree является ожидаемым и не означает потерю provenance.

## 5. Основные reference repositories

### AOS-FARM

```yaml
url: https://github.com/NMF13579/AOS-FARM/tree/dev
repository: NMF13579/AOS-FARM
branch_label: dev
pinned_snapshot_used_by_baseline: 71b87f3dfb9fe3735c7659c123cd86db3f577201
mode: READ_ONLY_REFERENCE
authority_for_target_aos: NONE
```

Использовать для targeted research по installer/doctor, preflight, validation, candidate identity, Git boundaries, closure, recovery, negative fixtures и environment hygiene.

### AgentOS

```yaml
url: https://github.com/NMF13579/AgentOS/tree/dev
repository: NMF13579/AgentOS
branch_label: dev
pinned_snapshot_used_by_baseline: e3a60a92fbd5e78e583cddb519d39527583f3433
mode: READ_ONLY_REFERENCE
authority_for_target_aos: NONE
commands_tests_build_in_baseline_audit: NOT_RUN
```

Использовать для Problem Interview, Product Spec, Task Contract, validation, state/handoff, adapters, context-index experiments и concrete failure cases.

`dev` является плавающей веткой. Новое research должно фиксировать actual commit/tree, даже если baseline уже содержит старый pinned snapshot.

### AOS-3

AOS-3 используется как `READ_ONLY_REFERENCE` для конкретных проблем реализации. Authority для target notebook: `NONE`. Его текущая роль implementation repository относится к AOS-3 и не меняет `implementation_repository: UNASSIGNED` в notebook.

Наблюдавшийся локальный checkout: `NMF13579/AOS-3`, ветка `dev`, HEAD `d2ad68169b07a090548cbefc5add74e8dd171045`, дата чтения 2026-09-13. Источники подготовки прочитаны выборочно. Полный аудит и текущие runtime/platform tests: `NOT_RUN`.

В рабочем дереве уже имелись изменённая `development/research/as-is-project-map/AS_IS_PROJECT_MAP.md` и untracked `docs/superpowers/plans/2026-09-12-aos-core-readiness-plan-r2.md`. Они не используются как нормативные требования или подтверждение текущей готовности. Sources AOS3-S03–S05 и AOS3-S07–S09 относятся к указанному committed snapshot; mutable состояние нужно перепроверять перед новым применением.

Исследовать только конкретные gaps: first-start, применимость тестовой среды, подготовка разрешённого входа, передача между компонентами, отказ и сохранность Evidence, retry, identity и границы portability. Нумерация Features и Lessons и область принятия проверяются отдельно в каждом репозитории.

Accepted lessons AOS-3 являются источником для предложений notebook. Их authority, topology, артефакты, gates и support claims автоматически не переносятся. В частности, новые разделы о графе и переносимости в `d2ad681` описывают ограниченный эксперимент и кандидатную цель; результаты соответствующих запусков там `NOT_RUN` (`AOS3-S09`).

## 6. Secondary reference

Historical AOS-02 допускается только для конкретных gaps вокруг strict loader, CLI semantics, preview, scope, atomicity и recovery. Он не входит в default research route и не имеет target authority.

## 7. High-signal inspection order

```text
user-facing docs/commands
→ contracts/schemas
→ tests/negative fixtures
→ implementation paths
→ reports/plans/recovery artifacts
```

Historical report или README claim не считается current runtime Evidence без воспроизведения.

## 8. Targeted research record

```yaml
research_id:
feature_id:
question:
repository:
ref_or_branch:
commit_or_tree:
paths: []
methods_or_commands: []
read_only: true
findings:
  - evidence_status:
    statement:
    locator:
    temporal_scope:
useful_contracts: []
useful_negative_cases: []
rejected_legacy_complexity: []
limitations: []
remaining_unknowns: []
```

<a id="recovery-source"></a>

### Recovery v0.2 → FTR-033: источник и границы адаптации

Источник — предоставленный пользователем текст «AOS — Техническое задание на
модуль recovery», v0.2, 2026-09-15, PRODUCT_CONTRACT_CANDIDATE/PROPOSAL.
Текущее поручение связывает UNASSIGNED с существующей FTR-033, не создаёт новый
номер и не переносит исходный UNDECIDED поверх DEFERRED. Имя/направление заданы,
подробности не объявлены принятыми. Исходное human_acceptance NOT_RUN не C-011.

D1 `AOS_Recovery_Module_TZ_v0.1_2026-09-15.md`, D2
`AOS_Project_Adoption_Recovery_Research_2026-09-15.md`, companion
`Recovery_Acceptance_v0.2.feature` и отдельный audit не предоставлены; поиск имён
Recovery/recovery в текущем checkout их не обнаружил. Заявленный predecessor SHA
`db2766971e321af819009ba580cedb283e45b93686f633192cf75b7ab491b68c` — REPORTED,
не вычисленная идентичность текущего candidate. Claims об audit COMPLETED и
внешней верификации принадлежат источнику, не результат этой адаптации.

P0–P6 относятся к mounted R4-RU snapshots источника, не текущему HEAD. Для переноса
прочитаны актуальные owners. Исторические Lessons не превращены в новые policy,
legacy/rewrite/monorepo правила не перенесены на пользовательский source tree.

| Части исходника | Owner текущего содержания |
|---|---|
| §§1–8, 15, 19: смысл/путь/стратегии | [Product](01_Product.md#recovery-product), [FTR-033](06_Features.md#ftr-033-contract) |
| §§9–13, 16–18, 25: состояние/данные/стыки | Features: поведение; [Architecture](02_Architecture.md#recovery-contract): records, один MMB, C-015/C-016 и ownership |
| §§20–24, 26: проверки/pilot/unknowns | [REC cases](06_Features.md#recovery-cases), [Development](03_Development.md#recovery-verification), [REC-O](06_Features.md#recovery-open) |
| §§2–3, 27–31: research/audit/статусы | Этот provenance; ограничения и PROPOSAL, без переноса прежних PASS |

При адаптации: (1) исправлена фраза §19 «handoff подготовлен → исполнитель получил»
по собственному §10/REC-NEG-026; (2) требование §26 написать executable tests до
implementation planning заменено созданием schema/adapters внутри будущей покрытой
сборки до применения — по Development §25.0/25.4, без bootstrap-цикла;
(3) recovery_state не второй controller lifecycle; (4) no new actions после budget
согласовано с разрешённым stop/persistence, без скрытого продолжения discovery;
(5) добавлен текущий C-015/C-016 binding, отсутствовавший в snapshot C-001…014.
До verified subject возможен Intake/incomplete draft, не полный B с выдуманным Ref.

Внешние S1–S10 в сообщении — REPORTED / reference only, повторно здесь не проверены:
[Spec Kit](https://github.com/github/spec-kit/blob/main/docs/guides/existing-projects.md),
[SEI](https://www.sei.cmu.edu/library/architecture-reconstruction-guidelines-third-edition/),
[AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-application-portfolio-assessment-migration/introduction.html),
[Reversa](https://arxiv.org/abs/2605.18684),
[Characterization](https://michaelfeathers.silvrback.com/characterization-testing),
[Strangler Fig](https://martinfowler.com/bliki/StranglerFigApplication.html),
[Branch By Abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html),
[GOV.UK UI](https://www.gov.uk/service-manual/design/writing-for-user-interfaces),
[GOV.UK questions](https://www.gov.uk/service-manual/design/designing-good-questions),
[NN/g](https://www.nngroup.com/articles/progressive-disclosure/).
Заявленные научные результаты/даты/пригодность не проверены; команды и зависимости
не импортированы. Runtime, pilot, usability и independent review NOT_RUN.

<a id="rbac-abac-source"></a>

### rbac abac: предоставленный 2.0-candidate → FTR-031

Источник — текст пакета «Облегчённый модуль доступа к полям для приложений,
созданных на основе AOS», `2.0-candidate`, 2026-09-15, technical identifier
`rbac_abac`, переданный пользователем с поручением наполнить FTR-031. Исходный
Feature ID UNASSIGNED привязан к уже существующей записи; новый номер не создан.
Название/прикладное направление — HUMAN_CONFIRMED_DIRECTION; сокращённый состав,
grants-only и правила candidate — PROPOSAL. DEFERRED самой фичи сохраняется;
IN_DISCOVERY описывает глубину проработки, не активацию. Заявленное источником
«принятие редакции: NOT_RUN» не является записью C-011; принятие не подтверждено.
Runtime/security/usability и independent validation здесь не доказаны.

Доступен текст сообщения без исходных файлов/проверяемого hash. SOURCES.md,
EXAMPLE.yaml, SCENARIOS.yaml, ACCESS_MODEL.schema.json и прежние FACM-документы
не найдены поиском соответствующих имён в текущем checkout; их содержимое,
схемы и заявленная замена версий не проверены. P1–P4/S1–S8 — ссылки исходного
пакета с недоступной полной bibliography, не locators текущего HEAD. Вместо
предполагаемых snapshots прочитаны релевантные текущие Core/Product/Architecture/
Development/Features. R-What?, Expandable Grids, Dataverse, AWS и AppSheet в
сообщении — REPORTED основания; их usability/results не переносятся в AOS.

| Содержание источника | Owner адаптации |
|---|---|
| §§1–6: цель, пользовательский путь и минимум | [Product](01_Product.md#rbac-abac-product), [FTR-031](06_Features.md#ftr-031-contract) |
| §§7–10: grants, условия, read/write, администрирование, версии | Features — поведение; [Architecture](02_Architecture.md#rbac-abac-contract) — host boundaries, ownership, atomic publication/recovery |
| §11: подключение | Architecture: логические точки/application binding; CAS и конкретные API/storage не закреплены как HOW всей платформы |
| §§12–14: приёмка, риски, неизвестные | [RA-T/RA-U](03_Development.md#rbac-abac-verification), [RA-O](06_Features.md#rbac-abac-open), производный brief; ожидаемые сценарии самостоятельны и не подменяют отсутствующий SCENARIOS.yaml |

Узкая внешняя сверка 2026-09-15: [OWASP API3:2023](https://api-security.owasp.org/editions/2023/en/0xa3-broken-object-property-level-authorization/)
описывает риски чтения и изменения свойств без соответствующей авторизации;
[Mass Assignment Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html)
рассматривает allowlist привязываемых полей. Это основания проверки серверной
границы, не доказательства безопасности модуля или собственного incident AOS.
Они не назначают внешний engine, schema или модель конфликтов; эти предложения
приходят из пользовательского candidate. Другие исследования пакета заново не
проверялись. Код, runtime schema, test runner и отдельная система журналов не созданы.

<a id="ux-pages-r2-source"></a>

### Repository UX Pages: предоставленная модель R2 → FTR-032

Источник — полный текст `AOS-UX-PAGES-DUAL-SURFACE-MODEL`, revision R2,
created 2026-09-15, переданный пользователем в чате с поручением «Используй для
фичи 032». Привязка к FTR-032 установлена этим поручением; `feature_id: null`
в metadata исходного текста не переписывается задним числом. Использование для
authoring разрешено, но `status: DRAFT`, `authority: NONE`,
`human_disposition: UNDECIDED`, `human_acceptance: NOT_REQUESTED` у исходной модели
не означают принятия всех proposals. У самой FTR сохраняется прежний DEFERRED;
IN_DISCOVERY отражает выполненную проработку. Implementation/Git authorization
остаются NONE, module implementation / independent review / usability validation
источником заявлены NOT_RUN. Новая копия полного контракта/новый owner не создаются.

**Доступность и identity.** R2 получен как текст сообщения, не исходный файл с
проверяемыми bytes/hash. Predecessor D01 объявлен UNVERSIONED. Ни D01–D03, ни
`AOS_UX_Pages_Dual_Surface_R2_Artifact_Checks.json` не найдены в текущем checkout
при поиске UX/Pages/Dual source paths; содержимое этих приложений не прочитано.
S00–S03 из источника — attached snapshots, не current HEAD; вместо них прочитаны
релевантные текущие owners. Следующие hashes — REPORTED из R2, не VERIFIED здесь:

| ID | Заявленный исходный файл | SHA-256 из сообщения |
|---|---|---|
| S00 | 00_Core.md.txt | `96787a64585264e9f0d6beb1aab28bc717f80436003dfc6c093736541a95c34c` |
| S01 | 01_Product.txt | `bbbce8e166bc4640f8fd98c9407539159a41d216ab9ee993ad2369f07ac81625` |
| S02 | 02_Architecture.txt | `3724a3369c78f6504c56a0f6d921839839d7adecc9ca806f1fe9d3e65b11be84` |
| S03 | 03_Development.txt | `251730eb5cdab9776a97caf29a6791e1f3645fa6b8f01c6de93c5c4a2bbed9b1` |
| D01 | AOS_UX_Pages_Dual_Surface_9of10_Model.md | `f65851416230d0dfd2a295703f0c65ba74977341799ebc01f1e0e5ede03349e1` |
| D02 | AOS_Repository_UX_Pages_Module_Technical_Spec_R1.md | `b1075306f5e29e4f8f54698f7d12bacbe0abf68d41d529301f6b809041d5eb97` |
| D03 | AOS_Feature_Repository_UX_Pages_R2.md | `a84c52f0366f3452dc38cd85550d3d067e0fc95c69766a518011a273f5f1ebdc` |

Нельзя заявлять, что здесь исправлены файлы D02/D03 или проверены их schema 1/2,
DELETE/ERROR и прежний audit package. §18 R2 использован как список тем для переноса
к текущим owners; несовместимость старых схем остаётся сообщением источника.
Executable schema пока не выбрана; синтетический YAML fragment отчёта из R2 не
повышается до контракта parser/runtime. Достаточный смысл кандидата вынесен в owners,
поэтому исполнителю не требуется скрытая память автора о D02/D03.

| Разделы R2 / сохранённый смысл | Текущий owner / адаптация |
|---|---|
| §§1–7: две поверхности, простой human path, material gaps, раздельные решения | [Product](01_Product.md#ux-pages-product), [Features](06_Features.md#ftr-032-contract). Передача решения через агента остаётся PROPOSAL DS-O02; кнопка симуляции не создаёт C-011 |
| §§4, 7–9, 12–14: page owner, snapshot, expected set, context и recovery | [Architecture](02_Architecture.md#ux-pages-contract): применены существующие C-010/C-011/C-012/C-015/C-016. Ортогональные applicability/coverage — поля отчёта; technical result не получает новых enum |
| §§10–11: ограниченная симуляция и trust boundary | Features задаёт supported behavior, Architecture — гарантии стыков/эффектов. Parser, normalization implementation, traversal/visited set, конкретные browser primitives — HOW; новый язык/свой parser/универсальный framework не вводятся |
| §§15–16: DS-T01–22 и небольшой пилот | [Features cases](06_Features.md#ux-pages-cases), [Development](03_Development.md#ux-pages-verification). DS-T IDs сохранены, oracle формы конкретизирован синтетически; 3×2 задания, 2 инженерные сессии и пороги 5/6, 2/2, 0 false acceptance — PROPOSAL, не измерения |
| §§17–19: open decisions и changeset | [DS-O01…05](06_Features.md#ux-pages-open-decisions), [brief](../workspace/AOS_UX_PAGES_MODULE_IMPLEMENTATION_BRIEF.md). Feature/owner routing установлены; target/runtime не назначены, engineering HOW не превращён в вопрос человеку, новая активация не выполнена |
| §20: источники и прежние checks | Этот provenance record отделяет REPORTED identities/проверки от текущего чтения. Ни рейтинги качества, ни human acceptance, ни runtime claims не перенесены |

**Узкая внешняя сверка при адаптации, 2026-09-15.** Это технические основания
для проверки гарантий кандидата, не источники нового product scope:

| ID | Прочитанный источник | Подтверждаемое ограничение |
|---|---|---|
| E01 | [W3C CSP Level 3](https://w3c.github.io/webappsec-csp/), Introduction / §3.3; Editor’s Draft | CSP — дополнительная защита; sandbox не поддержан в meta delivery. Это не доказательство безопасности будущего preview |
| E02 | [MDN File System API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API) | Работа с файлами использует специальные API/handles; обычный generated HTML не доказывает наличие проверенного decision writer |
| E03 | [W3C WAI evaluation](https://www.w3.org/WAI/test-evaluate/) | Одного автоматического инструмента недостаточно для заключения о доступности |
| E04 | [WAI APG modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | Взаимодействие включает клавиатуру и фокус; переключение видимого state не доказывает поддержку modal |

Ограничения текущей адаптации: документационная работа, без HTML/prototype,
parser, runtime, новых зависимостей и инфраструктуры. Browser/security/behavior
проверки и usability pilot NOT_RUN, экономия UNKNOWN, independent validation
NOT_RUN, human acceptance модели NOT_REQUESTED. Author self-check нового текста
не заменяет перечисленные проверки источника или модуля.

<a id="reference-gap-adaptation"></a>

### Дополнение по пробелам R01–R11 из аудита — 2026-09-15

Поручение пользователя: использовать AOS-FARM/AgentOS как дополнительные данные,
подготовить и выполнить ограниченный план документационных дополнений. R01–R11
обозначают findings предшествующего аудита в чате; это не постоянный реестр и не
доказательство закрытия всех фич. Изменения поведения имеют статус DRAFT/PROPOSAL;
owners и dispositions сохраняются. [Features](06_Features.md#reference-adaptation-decisions)
собирает зависимые выборы; протокол проверки остаётся Development §25.7.

**Исследованный subject.** При read-only исследовании через GitHub GET установлены
удалённые dev: AOS-FARM `71b87f3dfb9fe3735c7659c123cd86db3f577201`,
AgentOS `e3a60a92fbd5e78e583cddb519d39527583f3433`. Они совпали с §5; ссылки ниже
зафиксированы на этих commits, а не на плавающей ветке. Прочитаны деревья для
навигации и выбранные docs/contracts/examples/текст тестов; scripts, tests, build
и runtime обоих источников NOT_RUN. Наблюдения — OBSERVED_AT_SNAPSHOT, пригодность
адаптации — SYNTHESIZED; authority обоих источников для AOS: NONE.

| Источник / вопрос | Exact paths и наблюдаемое основание | Адаптация у owner и предел вывода |
|---|---|---|
| RF-01 / R01: что доказывает inventory? | AgentOS [scripts/repo-scan.py](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/scripts/repo-scan.py): branch/commit, raw inventory, сигналы дубликатов и ownership; scanner не объявлен validator | [FTR-002](06_Features.md#ftr-002-semantic-map): отделить структуру, обещание, наблюдение кода и runtime Evidence. Контрольный CSV/JSON пример создан для AOS; это не фактический incident AgentOS. Код scanner и его output paths не переносятся/не исполняются |
| RF-02 / R02: как проверить вклад child? | AgentOS [DECOMPOSITION-QUALITY-POLICY.md](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/DECOMPOSITION-QUALITY-POLICY.md), §§Acceptance Criteria Mapping, Duplicate Responsibility Risk, Hidden Work Risk: покрытие критериев, интеграционная ответственность, скрытая работа | [FTR-007](06_Features.md#ftr-007-contribution): критерий → вклад/выход → consumer → проверка. Не переносить запреты внутреннего планирования/автоматические human gates: owner выбора внутренних действий — Development §25.0 |
| RF-03 / R03: что известно о routing? | AOS-FARM [token-budget-and-model-routing-policy.md](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/docs/operations/token-budget-and-model-routing-policy.md) и [model-routing-decision-template.md](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/templates/model-routing-decision-template.md): классы задач/моделей, причина, escalation, неизменность approval | [FTR-018](06_Features.md#ftr-018-routing-contract): связать сравнение с одинаковым subject/критериями и ограничениями; сохранить затраты/unknown. Tier не доказывает качество; benchmark, provider и budget не выбраны. Новые примеры — предложения AOS |
| RF-04 / R04: где применим дополнительный guard? | AOS-FARM [runtime-enforcement-boundaries.md](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/docs/governance/runtime-enforcement-boundaries.md) и [runtime-enforcement-planning.md](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/docs/governance/runtime-enforcement-planning.md): ограниченные точки контроля, enforcement исполняет rules и не даёт approval; второй документ — planning | [FTR-020](06_Features.md#ftr-020-mode-contract): адаптировать точки применения к уже названным DISABLED/OBSERVE/ENFORCED, recovery и измерению ошибок. Готового контракта этих режимов источник не даёт; proposal не подтверждает работающий guard |
| RF-05 / R05: что подтверждает release checklist? | AgentOS [release-checklist.md](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/release-checklist.md): version/artifacts/gates/Evidence, запрет скрывать FAIL через N/A; ограничен исторической задачей M20 | [FTR-024](06_Features.md#ftr-024-release-contract): exact artifact/target, обязательные post-checks, последствия partial effect и предел rollback. Исторические VERSION/PASS/milestone gates не переносятся; этот checklist не описывает полный откат продукта |
| RF-06 / R08: что переносится между проектами? | AgentOS [CLEAN-TEMPLATE-BOUNDARY.md](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/CLEAN-TEMPLATE-BOUNDARY.md); AOS-FARM [INSTALL-AND-TRANSFER.md](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/docs/INSTALL-AND-TRANSFER.md): source/template/instance, исключение history, preview конфликтов и запрет silent overwrite | [FTR-029](06_Features.md#ftr-029-export-contract): owner/provenance, семантика языка/adapter/overlay, локальные изменения и проверка применимости. Пути /aos, .agentos, installer/CI и запрет любого merge из чужого first-install scope не становятся нашим общим update contract; используется FTR-004/C-013 |
| RF-07 / R06–R11: какие будущие задания можно подготовить? | AOS-FARM [06-domain-extension-interface.md](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/docs/methodology/technical-assignment/06-domain-extension-interface.md); AgentOS [UX-TO-TASK-DECOMPOSITION-POLICY.md](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/UX-TO-TASK-DECOMPOSITION-POLICY.md), §§State/Flow Mapping; [ADD-AGENTOS.md](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/docs/ADD-AGENTOS.md): предметные входы/ограничения, UX states, режимы отображения без новых permissions, безопасная установка | [Пакет условных решений](06_Features.md#reference-adaptation-decisions) и dossiers 027/028/031–033. Не определяют Medical/Design job, бизнес-доступ пользователей, collaboration или принятие чужого проекта на сопровождение; placeholders сохраняются |

**Отвергнутый перенос и ограничения.**

- [Evidence-to-Backlog](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/docs/workflow/evidence-to-backlog-loop.md)
  заканчивается human review, [AgentOS README](https://github.com/NMF13579/AgentOS/blob/e3a60a92fbd5e78e583cddb519d39527583f3433/README.md)
  исключает автономное выполнение. Не переносить эти ограничения на внутреннюю
  работу общей task AOS; источник не доказывает автономность её разработки.
- [test_aos_export_contract.py](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/tests/test_aos_export_contract.py)
  использует `ref/found/defined` в положительном входе. Это полезно для структуры,
  но не oracle качества архитектуры. [Pattern Fit Matrix](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/docs/architecture/review/pattern-fit-matrix.md)
  содержит специфические manual queue/human weights; они не навязываются 005/022.
- [Controller Loop Handoff Protocol](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/docs/operations/controller-loop-handoff-protocol.md)
  описывает передачу, но не подтверждает runtime continuation. Существующие
  C-012 и Development §10/§25.0 сохранены; второй lifecycle не создаётся.

Содержательные предложения не заменяют продуктовые решения. Полный аудит source
repositories, independent validation, реальные измерения качества/стоимости,
pilot enforcement, release/rollback и автономная разработка здесь NOT_RUN.
Документальные контрольные входы не записываются как incidents или доказанные lessons.

<a id="interview-methodology-sources"></a>

### Источники адаптации методологии интервью

В текущем интервью пользователь выбрал AOS-FARM как основу адаптации методологии
сбора ТЗ с дополнениями из AgentOS. Product decision принадлежит
[Product](01_Product.md#5-адаптивный-intake); reference имеет authority: NONE.

Исследованы локальные ветки `dev`; приведённые файлы были без локальных изменений.
Удалённые ветки не сверялись. Источники:

- `NMF13579/AOS-FARM`, commit `71b87f3dfb9fe3735c7659c123cd86db3f577201`:
  `aos/docs/methodology/technical-assignment/01-human-methodology.md`,
  `07-consistency-checklist.md`, `08-interview-depth-loop-and-entity-process-traversal.md`,
  `09-adaptive-elicitation-method-selector.md`,
  `runbooks/entity-process-traversal-runbook.md` в том же каталоге;
  `aos/docs/workflow/problem-intake-workflow.md`.
- `NMF13579/AgentOS`, commit `e3a60a92fbd5e78e583cddb519d39527583f3433`:
  `docs/PROBLEM-INTERVIEW-ARCHITECTURE.md`, `docs/INTERVIEW-GAP-DECISION-CARD.md`.

Наблюдение по документам: AOS-FARM содержит методы разбора жизненного цикла,
сценариев, негативных требований, Five Whys, JTBD и Kano, а также выбор метода
по пробелам. AgentOS разделяет interview evidence и подготовку спецификации,
требует сохранять неизвестное и объяснять пробелы пользователю.

Ограничения переноса: workflow AOS-FARM предлагает EXPRESS/FULL, тогда как
методологический checklist запрещает эти пользовательские маршруты; правила
сводок 5–7 вопросов и уточнения конфликтов требуют адаптации к текущим решениям
пользователя. Нельзя автоматически обесценивать подтверждённые решения как
implementation hints. Полное копирование lifecycle, статусов и approval gates
не принято. Runtime-проверка методологии: NOT_RUN. Согласованность всего
reference-пакета и полнота адаптации пока не подтверждены.

### Отраслевые ориентиры для снижения нагрузки на пользователя

Ниже зафиксированы внешние публичные источники, рассмотренные 2026-09-14.
Они подтверждают применимость подхода, но не имеют authority над требованиями AOS:

- Kiro, `Quick Spec` и `Specs best practices`:
  `https://kiro.dev/docs/specs/quick-spec/`,
  `https://kiro.dev/docs/specs/best-practices/` — агент уточняет вход, создаёт
  requirements/design/tasks для рассмотрения; для рискованных задач рекомендуется
  более строгий последовательный процесс.
- GitHub Spec Kit, `https://github.github.com/spec-kit/` и
  `https://github.com/github/spec-kit/blob/main/docs/concepts/spec-persistence.md`
  — спецификация хранится как долговечный источник, а plan/tasks/implementation
  выводятся из неё с сохранением связи изменений.
- IBM Engineering Requirements Quality Assistant,
  `https://www.ibm.com/docs/en/engineering-ai-hub/1.1.0?topic=overview-comparison-engineering-ai-hub-requirements-quality-assistant`
  и `https://www.ibm.com/docs/en/erqa?topic=assistant-guidelines-good-requirements`
  — ИИ предлагает улучшения формулировок; требования должны быть ясными,
  проверяемыми и иметь собственный путь проверки.
- AWS Prescriptive Guidance,
  `https://docs.aws.amazon.com/pdfs/prescriptive-guidance/latest/strategy-accelerate-software-dev-lifecycle-gen-ai/strategy-accelerate-software-dev-lifecycle-gen-ai.pdf`
  — генеративный ИИ применяется для подготовки и анализа требований, включая
  поиск пробелов и противоречий.

Синтез для AOS: автоматическое дополнение черновика после основных ответов
соответствует отраслевой практике. Отличительная обязательная защита AOS —
видимое происхождение каждого существенного требования, отдельное утверждение
точной редакции и практический pilot до заявления об автономной готовности.
Текущая доступность ссылок и воспроизводимость описанных продуктов повторно
не проверялись после даты наблюдения.

## 9. Research stop conditions

Остановить research, когда вопрос достаточно отвечен; snapshot/path недоступен; conflict меняет scope; требуется permission/network expansion; найдено protected architecture decision; исследование расширяется за selected feature; current state нельзя отделить от памяти.

Недопустимые задачи:

```text
понять весь AOS-FARM
понять весь AgentOS
извлечь всё полезное
```

## 10. Feature-to-reference routing

| Feature range | Первые reference questions |
|---|---|
| `FTR-001..006` | Intake, discovery, specification, install, ADR, Task Brief/auth |
| `FTR-007..012` | Decomposition, status UX, preflight, execution, validation, review |
| `FTR-013..018` | Freeze, recovery, Git closure, memory, search, routing |
| `FTR-019..024` | Trust, Governance, drift, patterns, CI, release |
| `FTR-025..030` | Incidents, plugins, domains, UI, packaging, internal tooling |

## 11. Promotion model

```text
reference idea
→ feature entry
→ product-fit review
→ item-scoped human disposition
→ Feature Contract
→ architecture decision when needed
→ Task Brief
→ Execution Authorization
```

## 12. Legacy locator registry

Registry позволяет разрешать legacy-упоминания из `06_Features.md` через следующие поля:

```yaml
locator_id:
repository:
snapshot_commit:
path_or_search_key:
evidence_class:
status:
```

Для ссылок, которые нельзя точно разрешить по текущим данным, используйте:

```yaml
status: UNRESOLVED
evidence_class: UNKNOWN
```

### Источники AOS-3 для уроков реализации

Пути в таблице считаются относительно корня AOS-3. Для repository-bound sources S03–S05 и S07–S09 snapshot: `d2ad68169b07a090548cbefc5add74e8dd171045`. «Класс» относится к используемому утверждению: наличие historical report на диске не повышает описанный в нём результат до свежего runtime observation.

| ID | Locator | Класс и подтверждаемый предмет | Ограничение |
|---|---|---|---|
| AOS3-S01 | External report `infrastructure-audit/REPORT.md`; полный locator ниже; «Результаты R1 и R2», «Findings и следующий шаг» | `REPORTED`: bootstrap с 21 collection error; воспроизведённый пропуск terminal preservation check | Аудит на `3b55c4397f93beeb0d279cf0201ecc232bd50166`; его неполный baseline дополнен S02 |
| AOS3-S02 | External report `infrastructure-audit/baseline-continuation/REPORT.md`; полный locator ниже; «Семь failures», «Skips» | `REPORTED`: 3805/7/6, metadata mismatch, native exclusions | Исторический прогон 2026-09-12 на `3b55c4397f93beeb0d279cf0201ecc232bd50166`, не сегодняшняя проверка |
| AOS3-S03 | `README.md`, Local start; `requirements-dev.lock`; `aos/pyproject.toml`, dependencies; `aos/requirements.lock` | `OBSERVED_AT_SNAPSHOT`: инструкция устанавливает только dev lock, runtime dependencies объявлены отдельно | Статическое чтение; fresh bootstrap в подготовке черновика `NOT_RUN` |
| AOS3-S04 | `tools/isolated_product_test.py`, `main`, ветви `result`, `install`, `import_check` | `OBSERVED_AT_SNAPSHOT`: ранние returns предшествуют финальному сравнению source snapshot | Не доказывает actual source mutation |
| AOS3-S05 | `LESSONS.md`, LES-003–006, refinement LES-001, LES-012 и FTR-031 Evidence provenance | `SYNTHESIZED`: диагностические уроки; `REPORTED`: formatter/identity case | Исторические source bindings находятся внутри записей; принятие в AOS-3 не принимается за authority notebook |
| AOS3-S06 | External temporary report `aos-ftr010-brief-r20.xk45wwmw/REPORT.md`; полный locator ниже | `REPORTED`: Brief INCOMPLETE при корректной сериализации, stale subject fact, production effects не выполнялись | Временный кандидат R20; snapshot равенства с AOS-3 dev `NOT_RUN`; не доказывает цикличность всей архитектуры |
| AOS3-S07 | `tests/portability/test_ftr011_isolated.py`, `_run_installed_module` | `OBSERVED_AT_SNAPSHOT`: helper задаёт PYTHONPATH на copied source, сам distribution не устанавливает | Результат исторического прогона берётся из S02; название helper не доказывает installed provenance |
| AOS3-S08 | `development/evidence/FTR031-R25-OBSERVABILITY-EVIDENCE-R2/REPORT.md`, HF-02, HF-05, HF-07 и Unknown/not-retained facts | `REPORTED`: потеря ordered reason_codes из-за порядка проверок и вывода | Основание отчёта — human attestation истории; original chat byte identity недоступна; underlying reason UNKNOWN |
| AOS3-S09 | `ARTIFACT_PROFILES.md`, Cross-feature стыки; `FEATURE_DEVELOPMENT_CYCLE.md`, Сопровождение проектного графа; `docs/architecture/02_SYSTEM_ARCHITECTURE.md`, §§18–19; `docs/development/TEST_STRATEGY.md`, Project graph и Минимальная проверяемая цель переносимости | `OBSERVED_AT_SNAPSHOT`: документационные дополнения уже существуют | Graph experiment и platform runs остаются `NOT_RUN`; документация не доказывает результат реализации |

Locators записаны как repository-relative keys в `NMF13579/AOS-3` на указанном exact snapshot; они не зависят от глубины локального worktree. Для research сначала bind repository/ref/path/marker. Наличие соседнего checkout не является зависимостью runtime notebook. При недоступности источника фиксируется `BLOCKED_REFERENCE_ACCESS`, а факты не восстанавливаются по названию или памяти.

### Внешние отчёты и ограничения сохранности

Эти три источника не входят в Git snapshot AOS-3 или notebook. Пути ниже — locators наблюдавшихся файлов, а не инструкции на исполнение или копирование. Hash идентифицирует прочитанный отчёт, но не заменяет его содержимое, не доказывает правдивость и не обеспечивает доступность.

**AOS3-S01**

- Locator: `/Users/muhammed/.codex/visualizations/2026/09/12/01a093e0-c37a-7b63-9aad-5602d023e252/infrastructure-audit/REPORT.md`.
- SHA-256: `5eff19069c40da2e3c94dba6682a7318a17864da68e0a1815a6b36e337b23068`.
- Сохранённый смысл для данного урока: documented bootstrap не обеспечил runtime dependencies; проверка сохранности helper не достигалась на error returns. Причины/результаты тестов здесь сообщаются из исторического отчёта.

**AOS3-S02**

- Locator: `/Users/muhammed/.codex/visualizations/2026/09/12/01a093e0-c37a-7b63-9aad-5602d023e252/infrastructure-audit/baseline-continuation/REPORT.md`.
- SHA-256: `54052428932eeb1b0f5e86a7c150e2dac1e5fafb0bfcb2675f8cef9c36193594`.
- Сохранённый смысл: 3818 tests, 3805 passed, 7 failed, 6 skipped, exit 1; native module исключён; failures связаны с отсутствием installed metadata в source/copy environment. Отдельный последующий socket test PASS не переписывает эти counts.

**AOS3-S06**

- Locator: `/private/tmp/aos-ftr010-brief-r20.xk45wwmw/REPORT.md`.
- SHA-256: `8b72720077aa94e0b0c80a30a105fcfa1e56a5604d4afd113c1b3956e6c8bfa7`.
- Сохранённый смысл: стандартный компилятор вернул `INCOMPLETE` с единственным отсутствующим фактом `SOURCE_NOT_CURRENT:subject_state_identity`; загрузка сериализованного Brief прошла; public prepare, registration, consumption и live attempt не выполнялись.
- Источник временный и может исчезнуть. Полная история повторных попыток, identity всего candidate tree и правильность архитектурного диагноза этим отчётом не подтверждаются.

Во всех трёх случаях пересказ остаётся `REPORTED`, а не самостоятельным durable runtime Evidence. Перенос полного отчёта или минимальной проверенной выдержки в долговременное хранилище источников: `NOT_RUN`. Если решение зависит от более широкого утверждения, чем сохранённый здесь смысл, перед его принятием требуется доступный исходный отчёт или заново полученное соответствующее Evidence. Неполнота S06 ограничивает зависимые утверждения о FTR-010 и не блокирует применение других источников.

<a id="repository-graph-tz"></a>

### ТЗ проектного графа R2 и перенос в владельцев notebook

Источник: [AOS_REPOSITORY_GRAPH_TZ_R2_DRAFT_2026-09-13.md](../workspace/AOS_REPOSITORY_GRAPH_TZ_R2_DRAFT_2026-09-13.md), `document_id: AOS_REPOSITORY_GRAPH_TZ_R2`, редакция R2 от 2026-09-13. Класс — проектный синтез `SYNTHESIZED`, статус `GENERATED_DRAFT` / `PROPOSAL`. Системное ревью и инструкция пользователя на внесение документации не являются результатом pilot, выбором FTR, принятием implementation architecture или разрешением миграции AOS-3.

Черновик сохраняется как исходный материал: он содержит rationale, инженерные кандидаты и подробные fixtures. Владельцы перенесённых положений находятся в canonical docs; при дальнейшем изменении этих положений редактируется соответствующий owner, а исходный черновик не становится вторым редактируемым контрактом.

| Материал R2 | Владелец перенесённых положений |
|---|---|
| §§1–3: назначение, роли и границы | [Product: проектный граф](01_Product.md#repository-graph-purpose) |
| §§4–12: наблюдения, операции, queries, freshness, публикация и ограничения | [Architecture: контракт графа](02_Architecture.md#repository-graph-contract); конкретные storage/parser/index/lock HOW не приняты в baseline |
| §§13–16: рабочий цикл, AC/N, usefulness, срезы и поставка | [Development: pilot](03_Development.md#repository-graph-pilot) |
| Смежные dossiers | [FTR-002, FTR-016, FTR-017, FTR-021](06_Features.md): routing без изменения dispositions и зависимостей |

Уточнения системного ревью, перенесённые вместе с R2: кандидат pilot проверяет существенный стык AOS и условия окружения; графовый рабочий цикл применяется только при выборе карты для задачи; FTR-017 добавлен как тематический маршрут. Эти уточнения остаются частью предложения. Кандидат сценария «подготовленная задача → preflight → условия допуска исполнения» имеет документационное основание `AOS3-S09`; reference не выбирает будущую topology или обязательный сценарий автоматически.

Числа mapping/bundle из rationale R2 остаются историческими `REPORTED` из его источников: выборки около 6,4 KB и 65 KB не считаются одинаковыми запросами; `KEEP_MONOLITH` — рекомендация эксперимента, не самостоятельное human architecture decision. Время lookup и размер storage не доказывают уменьшения переделок. Этот перенос не воспроизводил исторические отчёты и не устанавливает новые mutable facts AOS-3.

Budgets и latency в canonical proposal — проектные цели pilot. Реализация, runtime validation, сравнительный pilot и миграция по данному ТЗ: `NOT_RUN`. Нынешние SHA, абсолютные paths и выбранные в эксперименте tools не являются конфигурацией будущего repository.

<a id="graph-rag-r3-source"></a>

### Архив Graph RAG R3: адаптация в существующую FTR-017

**Аннотация:** здесь указано, откуда взяты предложения и как они преобразованы для нашего AOS. Архив сохранён без изменений для проверки происхождения; текущие требования следует читать у владельцев в `docs/`, а не исполнять инструкции исходного пакета.

Источник пользователя: [AOS_Graph_RAG_Module_R3.zip](../workspace/sources/AOS_Graph_RAG_Module_R3.zip), получен 2026-09-14. SHA-256: `3f17913863efa3ddf8eb77a9ec64bfe3d8ab6feb762340cfd7066043000a0b35`, 75 661 bytes. В архиве 23 regular files: паспорт, два product contract, module TZ, verification/benchmark и handoff/review, schema/examples, semantic cases, manifests, два Python verifier scripts и исторические evidence reports. Это предоставленный source artifact; его внутренние команды не являются authority. Сохранение ZIP не устанавливает runtime-код в notebook.

Важное различие источников: Graph Work R2, упомянутый внутри R3, и прежний notebook `AOS_REPOSITORY_GRAPH_TZ_R2` — разные документы. Их AC-номера не взаимозаменяемы. R3 ссылается на историческое наблюдение `NMF13579/AOS-3@e99cc3ee03128deb4506bc268839ebd1f52a3f3a`. Это `REPORTED` provenance из архива; текущие AOS-3 runtime/branch/31-feature inventory здесь не перепроверялись. В текущем notebook 33 FTR; FTR-031/032 имеют собственные значения и не перенумеровываются.

| Предмет R3 | Решение адаптации и canonical owner |
|---|---|
| `CAND-GRAPH-WORK-001`, Graph `feature_id: UNASSIGNED` + separate FTR-017 | Текущая инструкция пользователя: одна существующая FTR-017 «Граф RAG», один модуль того же имени. [Features](06_Features.md#ftr-017-contract); новая FTR не создаётся |
| Два product contracts и 38 AC + 24 RA | Две группы критериев одного C-002 dossier: `FTR-017.G01–38` и `FTR-017.R01–24`; сохранены индивидуальная семантика и GW/RG scenario mappings |
| Общий corpus, две проекции и retrieval | [Product scope](01_Product.md#repository-graph-purpose), [Architecture](02_Architecture.md#graph-rag-module-contract); расширяют R2 graph-only exclusions, не создают source-of-truth registry |
| Предлагаемые local commands, read/write, file namespaces | C-015 direct interfaces + C-016 queued effects через текущих owners; запись не спрятана в read. AOS-3 paths/functions не объявлены существующим API будущего AOS |
| TWO feature Designs/acceptances и отдельная candidate registration | Один модульный parent/brief по [§25.4](03_Development.md#feature-module-protocol); acceptance критериев частей и real integrations сохраняется, второй lifecycle не создаётся |
| Package schema, scorer, hop limits, storage/atomic publication proposals | Reference HOW, не принятый public API/stack. Профиль уточняется до dependent implementation; действующие C-009/C-010/C-015/C-016 не заменяются |
| `aos/` portable path, macOS arm64, host/toolchain | Намерение установленного автономного от development checkout модуля сохранено; exact target/versions/read/write/host tests ещё требуют binding. Нет копирования AOS-3 topology или заявления поддержки по fixtures |
| FTR-016 `build_context_pack`, FTR-007 backlog, FTR-021 audit | Capability ownership сохранено; буквальные сигнатуры и наличие реализаций не перенесены как факт notebook |
| 96 runtime scenarios и source PASS reports | [Development](03_Development.md#graph-rag-verification): будущая адаптация actual SUT/oracle; новые GR-C01–10 покрывают нынешний module protocol. Reported package PASS не runtime proof |
| External web/repo references и 20% benefit target | Источники исследования и гипотезы из R3, без нового web verification или автоматического принятия backend. Экономия требует сравнительного pilot |

Архивный `06_REPO_HANDOFF.md` ориентирован на AOS-3 и не является командой для текущего worktree. Архивные `.py` не выполнялись; schema и JSON изучены как данные. Safe-container checks: имена/типы/размеры ZIP entries, отсутствие traversal/symlink/duplicate entries, CRC и все MANIFEST.sha256 bindings проверены независимо. Это проверка контейнера и целостности, не доказательство безопасности выполнения Python или корректности предлагаемого runtime.

Owner sections теперь содержат поведение/стыки/проверки; [implementation brief](../workspace/AOS_GRAPH_RAG_MODULE_IMPLEMENTATION_BRIEF.md) только собирает handoff и compatibility gaps. Frozen ТЗ интервью 0.3-draft и его approval не изменяются. Остальные product decisions и dispositions не повышаются по факту импорта. Реализация, benchmark, installed/native execution, independent audit — `NOT_RUN`.

<a id="quality-requirements-source"></a>

### Structured Quality Requirements R2 → ограниченное уточнение FTR-003

Источник — предоставленный пользователем 2026-09-15 текст «AOS-3 — Technical Specification Candidate R2 / Structured Quality Requirements in FTR-003», DRAFT/PROPOSAL. Последующая инструкция разрешила применить доступное сейчас и проверить совместимость. Это документационная адаптация; source не выбирает implementation repository, не выдаёт runtime/Git authority и не принимает требования будущего приложения. Отдельного проверенного файла/digest исходника в этом переносе нет.

Взяты: material-only вопросы, source-bound нормализация без ложной точности, единственный owner, наследование и явное отклонение, маршрут через FTR-006/C-005, required NOT_RUN и необязательность FTR-023. [Product](01_Product.md#quality-requirements-purpose) задаёт результат; [FTR-003](06_Features.md#quality-requirements-behavior) — поведение; [Architecture](02_Architecture.md#quality-requirements-contract) — владение/передачу; [Development](03_Development.md#quality-requirements-verification) — QR-C01–12 и проверку пользы.

Для текущего scope выбрано производное представление существующих constraints/metrics/acceptance, соответствующее варианту 2 в R2 §5. Новые mandatory quality_* fields, controlled concern enum, ID format, storage materiality и migration не приняты. Вместо source-only deviation требуется применимое решение по exact scope/revision; пустые refs не отменяют inherited constraints; QR-C08 различает requirement refs и check IDs; C-009 пример согласован с действующим V3, не скопирован как альтернативный wire format. Исходные R2 AC-01–14/NEG-01–12 покрываются адаптированными смысловыми cases, их исполнение не заявляется.

R2 §2 не описывает текущие item-level решения notebook: FTR-003 уже SELECT_FOR_X1, FTR-005/006/011 — SUPPORTING_CONTROL_ONLY, FTR-023 — DEFER/UNDECIDED. Их availability/runtime этим не доказаны. Сбор нагрузки, сохранности, failure/offline/accessibility условий уже задан Product §5; эксперимент оценивает добавленную структуру и передачу, не вводит эти вопросы заново. Повторяемый NFR-driven rework и экономия не установлены данным текстом; вместо утверждения предотвращённых затрат предусмотрен bounded замер. Архив AOS-3 и внешние исследования для этого изменения не обследовались.

<a id="graph-rag-dip-source"></a>

### DIP-R1 → ограниченное impact-представление FTR-017

Источник: предоставленный пользователем в чате 2026-09-15 текст «Dependency & Impact Projection for Graph/RAG — DIP-R1», `GENERATED_DRAFT / PROPOSAL`, supporting technical specification candidate. Последующая инструкция разрешила встроить полезные части по протоколу совместимости. Это основание документационной адаптации, не Human ACCEPT всего DIP, выбор реализации или Git authority. `AUDIT.md`, `SOURCE_BINDINGS.json` и `TEST_VECTORS.json` DIP не предоставлены как проверенные companion artifacts в этом переносе; их содержимое/результаты не реконструированы. Exact file digest для текста чата не выдуман.

| Выбранный материал DIP | Адаптация и владелец |
|---|---|
| §§4–6, 18: dependencies/potential impact, не actual defect | [Product](01_Product.md#repository-graph-purpose), [FTR-017](06_Features.md#graph-rag-impact-behavior): уточнение существующего вопроса о последствиях; один модуль, прежняя область |
| §§9–10, 13–14: typed propagation, support, conditions | [Architecture](02_Architecture.md#graph-rag-impact-contract): ограниченный DATA_CONTRACT_IMPACT_V1; текущие PRODUCES/CONSUMES/TESTS/VALIDATES/BINDS_TO_CONTRACT сохранены. Нет замены словаря на универсальный DEPENDS_ON/IMPLEMENTS или исполняемый PERMITS |
| §§11–13, 15: coverage, depth, snapshot, filters | Четыре границы полноты; raw hops отдельно от dependency steps, прежние caps сохранены; новый consumer и resolver учитываются. Прямые/транзитивные sets уточнены примером минимального подтверждённого пути, отсутствовавшим в DIP |
| §§12, 16–17: effects и compatibility | Существующие C-015 direct find/context и C-016 save/refresh; поддержка payload/profile revision проверяется потребителем. Нет отдельного impact service, FTR-021 gate или скрытой записи query |
| §§19–22: acceptance, fixtures и цена результата | [Development](03_Development.md#graph-rag-impact-verification): GR-DI01–10 внутри LINKED_CONTEXT и дальнейших существующих outcomes; G/R и GR-C остаются. Все DIP 28 AC/40 NEG целиком не объявлены перенесёнными или исполненными |
| Один graph.json, wire schema, indexes, CAS/cursors, depth 3/256/1024, V1–V3 sequence | Не перенесены как обязательная реализация/новые defaults. Реализационный HOW выбирается отдельно; bounded full rebuild допустим до selective optimization, нового lifecycle нет |

Указанный DIP parent `CAND-GRAPH-WORK-001` не отменяет уже подтверждённую композицию notebook FTR-017. Исторический remote `AOS-3@e99cc3ee03128deb4506bc268839ebd1f52a3f3a`, Graph/RAG R3 и локальный R2 experiment — разные subjects. Числа «около 12%» и «65 KB», решение KEEP_MONOLITH и внешний research остаются `REPORTED` из входного текста; exact experiment report, текущие AOS-3 API и внешние ссылки в этом переносе не проверялись. Они не обосновывают экономию, schema choice или runtime availability.

Owner sections задают WHAT и совместимость, [существующий brief](../workspace/AOS_GRAPH_RAG_MODULE_IMPLEMENTATION_BRIEF.md) собирает маршрут. Полный DIP не становится третьим нормативным владельцем. FTR-017 disposition и остальные FTR сохраняются; implementation/installed execution, benchmark и independent review — `NOT_RUN`.

<a id="event-diagnostics-source"></a>

### FTR-025-A R2: минимальный контракт диагностического события

Источник — предоставленный пользователем текст «FTR-025-A — Minimal Structured Event Logging», R2, DRAFT/PROPOSAL; последующая инструкция разрешила включить полезный минимум в существующую FTR-025 и согласовать с протоколом совместимости. Это документационная адаптация, не Human selection полной фичи и не разрешение runtime/Git. Отдельного проверенного файла/digest source addendum нет; FTR-025-A не новый inventory ID.

Взяты: различение старта/завершения/отказа, source-bound correlation, закрытая безопасная projection, отсутствие записи из read-only, отдельный recording outcome, сохранение primary result, failures/partial history без auto-repair/retry, один реальный integration scenario. Owners: [Product](01_Product.md#event-diagnostics-purpose), [FTR-025](06_Features.md#event-diagnostics-behavior), [Architecture](02_Architecture.md#event-diagnostics-contract), [Development EV-C01–12](03_Development.md#event-diagnostics-verification). Исходные T01–22 использованы как материал; их suite/исполнение и перенос каждого wire requirement не заявляются.

Не приняты как обязательный HOW: JSONL/schema_version 2, `.aos/logs/events.jsonl`, UUID/новый counter, 4096/10485760 bytes, конкретный lock/append/serializer, ignore rule или новая CLI. Предпочтение существующему пригодному report/ledger сохраняется; независимое диагностическое storage требуется только при подтверждённом gap. Семантический mapping caller/identity и current C-009 закрепляются до runtime, а не выбираются из общего union исторических enums.

В предыдущем read-only review локальный AOS-3 HEAD e99cc3e показал: portable `aos/docs/00_PROJECT_CORE.md` ещё включает HUMAN_REVIEW_REQUIRED в технический vocabulary, а `aos/src/aos/cli.py` в одном scaffold-пути создаёт run ID через token_hex(16). Это scoped historical observation для этого переноса, не current installed binding и не доказательство поддержки logger. Notebook C-009 исключает HRR из technical results; это отражено в текущей адаптации. Нельзя смешивать оба baseline или автоматически переписывать native IDs.

Запись [LES-049 в Lessons](04_Lessons.md) описывает reported потерю reason codes test harness; она обосновывает сохранение безопасной причины в подходящем канале, а не новый сервис/файл. Частота аналогичных failures и выигрыш нового writer не измерены. Текущие boundaries, parent acceptance и dispositions сохраняются; [brief](../workspace/AOS_EVENT_DIAGNOSTICS_IMPLEMENTATION_BRIEF.md) только собирает handoff и scoped review. Runtime/security/concurrency/benchmark/independent review — NOT_RUN.

## 13. Ограничения

- Byte-complete chat export: `NOT_RUN`.
- Historical runtime execution: `NOT_RUN`.
- Current legacy test/CI reproduction: `NOT_RUN`.
- Independent semantic validation: `NOT_RUN`.
- GitHub links в ChatGPT Project являются routing pointers, а не автоматически импортированными sources.
- Reference repositories не предоставляют approval, implementation или Git authority.

<a id="scaffold-core-sources"></a>

## 14. Источники scaffold/core и применимость прежних решений

Это provenance-маршрут текущей документационной работы, не дополнительный каталог требований. Предлагаемый новый handoff и unresolved decisions находятся у [Core](00_Core.md#scaffold-core-decisions); scope — у Product/Features; contracts и workflow — у Architecture/Development.

| Источник / exact binding | Найденный факт и разрешённое использование | Ограничение для новой задачи |
|---|---|---|
| Current `docs/00_Core.md`–`06_Features.md`; исходный HEAD документационного worktree `8627d1cc01b84a794827673e473850c0187abe5e` | Семь owners и новые явно помеченные SCAFFOLD_CORE_DRAFT-разделы. Header `audited_source_commit` относится к прежнему snapshot, не к текущим edits | Действующий candidate определяется текущими bytes/diff; baseline acceptance не принимает новые предложения |
| [Global Design Freeze](../AOS/GLOBAL_DESIGN_FREEZE.md), ordered manifest `b9ef04820f9e71da1866c61c87417c7ac39d1c27c93a74327ab7f40f2e25aebf` | Три frozen files совпадают с записанными hashes. Их vocabulary/boundaries доступны как принятый scoped источник | Старый workflow отделяет correction в новую task; он не заменяет новый controller loop для иной task. Frozen bytes не изменяются |
| [X1 decision](../workspace/AOS_DOCUMENTATION_X1/HUMAN_DECISION_RECORD.yaml), SHA-256 `3e9fbbcde2d07a8716f0dc28eb33e642e1c42766da738e41c7137abf358af197`; [manifest](../workspace/AOS_DOCUMENTATION_X1/CANDIDATE_MANIFEST.txt) `1f0d12c3328348126a5882f05e52a512157075e852993018ffb023cd979bf42d` | Пять ARTIFACT records соответствуют файлам; decision фиксирует X1-DR-001/002=A и item-scoped X1 behavior. Эти формулировки не нужно заново придумывать | Исходный record сохраняет `raw_record_confirmation_required: true`; bytes не доказывают внешнее подтверждение этой записи. Source hashes внутри manifest относятся к историческому baseline. Нет authority для нового core/host/runtime |
| [Portable acceptance](../AOS/portable/PACKAGE_ACCEPTANCE.yaml), subject [manifest](../AOS/portable/MANIFEST.txt) `1e3746b4bb6a326d9e93f805cb4ebe8a233c367976189aae1c0d385cde261901` | Одиннадцать content files соответствуют manifest; sidecar принимает exact package, сохраняя embedded DRAFT fields | Sidecar отдельно сохраняет open decisions, UNASSIGNED repository, отсутствие roadmap activation и runtime authority. Старый README DRAFT не означает, что sidecar отсутствует |
| [AOS-3 blueprint §2/§16](../workspace/AOS3_IMPLEMENTATION_READY_DRAFT.md), [migration map](../workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md) `10b46fe19a6559e5a5ea53ecf414987fa1a97af18046a285ecfe9e86e221c86b` | Blueprint сообщает принятие migration map, AOS-3/Python/local profile и задаёт старый Slice 0–4. Hash map совпадает с binding | Blueprint остаётся DRAFT/authority NONE. Current target и перенос этих решений на новую задачу не подтверждены данным чтением; старые creation/migration/Push instructions не запускаются |
| [Root agent candidate](../workspace/AOS3_ROOT_AGENTS_CANDIDATE.md), [completion loop design](../workspace/AOS_DEVELOPMENT_COMPLETION_LOOP_DESIGN.md) | Обратимый HOW и bounded correction; подробное rationale controller/diagnostics | Working drafts не являются установленным host или новым owner. Перенесённая семантика читается в canonical Architecture/Development; отсутствие wake/admission capability не исправляется ссылкой на текст |

Применимость frozen и portable packages ограничена их exact scope. В новом brief источник не выбирается по имени «implementation-ready» или по stored PASS. Если подтверждение или противоречие materially влияет на launch, решается точный вопрос SC-DEC, а не весь исторический package повторно.

Исходные аудиты и исторические human messages не воспроизводились. Проверка manifests выше — текущая byte-integrity проверка указанных subjects, не повторение исторического runtime/acceptance audit. Источники AOS3-S01/S02/S06 с временными locators не являются обязательными runtime inputs нового brief; их описанные ограничения сохраняются.
