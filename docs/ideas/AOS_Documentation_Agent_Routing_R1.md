---
document_id: AOS-DOCUMENTATION-AGENT-ROUTING
revision: R2
supersedes_revision: R1
document_type: AGENT_ROUTING_DESIGN
status: DRAFT
authority: NONE
canonical_status: NOT_ASSIGNED
human_acceptance: NOT_REQUESTED_FOR_EXACT_ARTIFACT
human_review_required: true
product_scope_effect: NONE
architecture_effect: NONE_UNTIL_SEPARATE_HUMAN_DECISION
implementation_authorization: NONE
configuration_authorization: CONSUMED_FOR_R2_CORRECTION_EXECUTE
execution_authorized: false
git_authorization: NONE
implementation_repository: UNASSIGNED
source_repository: NMF13579/notebook
source_branch_expected: dev
source_head_observed_before_authoring: 2805eeafa0c96bf7ac432928882db7690b4f7dcc
source_head_observed_before_r2_correction: 2805eeafa0c96bf7ac432928882db7690b4f7dcc
active_path: docs/ideas/AOS_Documentation_Agent_Routing_R1.md
filename_revision_policy: PATH_PRESERVED_REVISION_IN_FRONTMATTER
created: '2026-07-30'
updated: '2026-07-30'
language: ru
technical_identifiers_language: en
---

# AOS — Documentation Agent Routing

## 0. Статус и назначение

Документ определяет DRAFT-дизайн детерминированного routing процесса для создания полного пакета документации AOS с помощью главного агента и специализированных read-only субагентов.

Документ отвечает на вопрос:

> Как организовать создание документации AOS так, чтобы модели выбирались рационально, контекст не дублировался, изменения выполнял один writer, а полномочия человека сохранялись?

Этот документ не является:

- canonical workflow;
- принятой product или target architecture;
- human acceptance уже созданной `.codex` candidate configuration;
- разрешением на изменение canonical документов;
- implementation authorization;
- execution authorization;
- разрешением на Commit, Push, Merge или Release;
- доказательством экономии ресурсов;
- доказательством качества будущего documentation package.

## 1. Основание дизайна

Дизайн опирается на:

- `docs/00_Core.md` — authority, status semantics и Minimal Safety Floor;
- `docs/02_Architecture.md` — layers, contract classes и data ownership;
- `docs/03_Development.md` — stage boundaries, validation и reporting;
- `docs/04_Lessons.md` — failures вокруг premature orchestration и unmeasured routing;
- `docs/06_Features.md`, `FTR-018` — advisory routing candidate;
- `AGENTS.md` — documentation-only repository boundary;
- официальные возможности Codex custom agents и subagent workflows;
- подтверждённые человеком design choices из текущего planning dialogue.

Reference repositories могут использоваться только как `READ_ONLY_REFERENCE`, `authority: NONE`, с exact repository/ref/commit/path.

## 2. Подтверждённые design choices

```yaml
routing_strategy: DETERMINISTIC
routing_scope: DOCUMENTATION_CREATION
writer_policy: SINGLE_WRITER
primary_agent_role: documentation_architect
subagents_write_authorized: false
automatic_routing_authorized_for: READ_ONLY_TASKS
configuration_status: DRAFT_CANDIDATE
mass_documentation_authoring_authorized: false
max_concurrent_subagents: 2
nested_subagents: FORBIDDEN
authority_from_agent_consensus: NONE
fallback_must_be_visible: true
resource_savings_status: NOT_MEASURED
```

Эти choices фиксируют направление дизайна, но exact artifact остаётся `DRAFT` до отдельного review человеком.

## 3. Цели

Routing процесс должен:

1. сохранять главного агента владельцем goal, scope, decisions и final artifact;
2. делегировать только независимые bounded read-only задачи;
3. использовать достаточную, а не максимальную модель;
4. ограничивать параллельность;
5. предотвращать параллельную запись документации;
6. возвращать Evidence вместо сырых длинных промежуточных выводов;
7. делать model choice, fallback и limitations проверяемыми;
8. сохранять `UNKNOWN`, `CONFLICT` и `NOT_RUN`;
9. запрашивать человека только в material decision или mutation boundary;
10. создавать данные для последующей оценки качества и расхода.

## 4. Не-цели

Routing процесс не должен:

- становиться runtime feature AOS без отдельного product decision;
- создавать autonomous multi-agent cascade;
- разрешать субагентам менять repository;
- выдавать model consensus за human decision;
- выбирать product scope, architecture, dependencies или Risk Profile от имени человека;
- автоматически повышать DRAFT до canonical или accepted status;
- автоматически выполнять Git operations;
- скрывать fallback, retry или incomplete Evidence;
- создавать отдельного агента для каждой feature или atomic function;
- объявлять экономию без сравнительного измерения.

## 5. Архитектура ролей

### 5.1 `documentation_architect`

```yaml
role: documentation_architect
recommended_model: gpt-5.6-sol
recommended_reasoning: high
write_access: SCOPED_AFTER_HUMAN_CONFIRMATION
responsibilities:
  - preserve exact objective and authority boundaries
  - classify tasks
  - choose routes
  - create subagent requests
  - verify returned Evidence
  - resolve non-authority-bearing synthesis
  - perform all documentation writes
  - run or initiate validation
  - produce final reports
```

Главный агент является единственным writer. Он не может использовать вывод субагента как готовый authoritative fact без проверки provenance и relevance.

### 5.2 `mechanical_checker`

```yaml
role: mechanical_checker
preferred_model: gpt-5.3-codex-spark
configured_model: gpt-5.6-luna
model_binding: STATIC_CONFIGURATION_BINDING
binding_reason: SPARK_NOT_IN_CONFIGURATION_TIME_MODEL_CATALOG
recommended_reasoning: medium
sandbox: read-only
```

Назначение:

- file inventory;
- IDs и duplicate checks;
- links;
- Markdown fences;
- manifests и checksums;
- schema-shape и deterministic structure;
- mechanical comparison;
- structured extraction.

Роль не выполняет semantic acceptance, architecture synthesis или authoring.

### 5.3 `reference_explorer`

```yaml
role: reference_explorer
recommended_model: gpt-5.6-terra
recommended_reasoning: medium
sandbox: read-only
```

Назначение:

- targeted research;
- exact repository/ref/commit/path inspection;
- поиск contracts, schemas, tests и negative fixtures;
- separation of observed behavior from historical claims;
- provenance-bound Evidence.

### 5.4 `contract_analyst`

```yaml
role: contract_analyst
recommended_model: gpt-5.6-terra
recommended_reasoning: high
sandbox: read-only
```

Назначение:

- анализ contract gaps;
- comparison docs↔schemas↔tests↔runtime;
- failure и recovery analysis;
- negative scenarios;
- contradiction detection;
- proposal of invariants without authority upgrade.

### 5.5 `semantic_reviewer`

```yaml
role: semantic_reviewer
recommended_model: gpt-5.6-sol
recommended_reasoning: high
sandbox: read-only
```

Назначение:

- cross-document consistency;
- traceability review;
- authority/status boundary review;
- detection of hidden assumptions and false readiness;
- review recommendation.

Reviewer не исправляет artifact и не создаёт human acceptance.

## 6. Routing matrix

| Task class | Default route | Fallback | Parallelism |
|---|---|---|---|
| Один короткий file check | Primary agent | None | `0` subagents |
| Counts, IDs, links, manifest, checksum | `mechanical_checker` | No automatic runtime fallback; current static binding is Luna | До `2`, если subjects независимы |
| Targeted reference research | `reference_explorer` | `BLOCKED` при недоступности или material insufficiency | До `2` независимых sources |
| Contract/failure/negative-case analysis | `contract_analyst` | `BLOCKED` при недоступности или material insufficiency | Обычно `1` |
| Cross-package semantic review | `semantic_reviewer` | `BLOCKED_REQUIRED_REVIEW_CAPABILITY` | `1` |
| Documentation synthesis | Primary agent | None | Subagents provide Evidence only |
| Documentation mutation | Primary agent after confirmation | None | `0` writing subagents |
| Git operation | No automatic route | Human decision required | `0` |

## 7. Routing decision algorithm

```text
receive exact objective
→ identify requested stage
→ verify repository and authority boundary
→ classify task
→ determine whether delegation has material value
→ verify task independence
→ select lowest sufficient route
→ bind subject, sources, output contract and stop conditions
→ spawn no more than two read-only subagents
→ collect structured results
→ verify provenance and contradictions
→ record routing decision and fallback
→ continue only within the current stage
```

Субагент не создаётся, если:

- задача решается одним коротким read-only inspection;
- новый agent потребует повторной загрузки большого одинакового context;
- tasks имеют shared mutable state;
- coordination overhead выше ожидаемой пользы;
- exact subject или output contract неизвестен;
- требуется human decision;
- требуется mutation.

## 8. Stage model

```text
PLAN / RESEARCH
→ read-only routing
→ Evidence and proposed package boundary
→ report + stop

EXECUTE
→ task subtype: DOCUMENTATION_AUTHORING или DOCUMENTATION_CORRECTION
→ exact human-confirmed target
→ SINGLE_WRITER change
→ execute report + stop

VALIDATE
→ fresh read-only subject binding
→ mechanical and semantic checks
→ validation report + stop

REVIEW
→ read-only assessment
→ recommendation
→ HUMAN_REVIEW_REQUIRED
```

`AUTHORING` является task subtype внутри `EXECUTE`, а не отдельным stage. Read-only stages не требуют повторного route confirmation, если subject и scope не изменились и ранее подтверждена automatic read-only routing policy. Каждый stage при этом остаётся отдельным и видимым.

## 9. Subagent request contract

```yaml
task_id:
request_id:
parent_task_id:
role:
task_class:
exact_subject:
goal:
source_boundary:
  repositories: []
  commits: []
  paths: []
allowed_operations:
  - READ
forbidden_operations:
  - WRITE
  - COMMIT
  - PUSH
  - MERGE
  - RELEASE
required_methods: []
required_output_fields:
  - task_id
  - request_id
  - parent_task_id
  - task_class
  - role
  - model
  - reasoning
  - exact_subject
  - source_boundary
  - sources
  - methods
  - claims
  - conflicts
  - unknowns
  - recommendations
  - checks_run
  - checks_not_run
  - limitations
  - model_binding
  - repository_mutations
  - git_operations
  - result
  - next_required_action
  - stop
stop_conditions: []
retry_limit: 0
```

Каждый request должен быть понятен без чтения всего main-thread history.

## 10. Subagent result contract

```yaml
task_id:
request_id:
parent_task_id:
task_class:
role:
model:
reasoning:
exact_subject:
source_boundary:
  repositories: []
  commits: []
  paths: []
sources:
  - repository:
    commit:
    paths: []
methods: []
claims:
  - claim_class:
    statement:
    evidence:
conflicts: []
unknowns: []
recommendations: []
checks_run: []
checks_not_run: []
limitations: []
model_binding:
  type:
  preferred_model:
  configured_model:
  reason:
repository_mutations: 0
git_operations:
  status_or_identity_inspection: NOT_RUN
  add: NOT_RUN
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
result:
next_required_action:
stop: true
```

Каждый request обязан передавать `task_id`, `request_id`, `parent_task_id` и `task_class`; субагент не должен угадывать отсутствующие identifiers. Raw output, уверенность модели или количество согласившихся агентов не являются authority.

## 11. Evidence и provenance

Каждый material finding должен содержать:

- exact subject;
- source repository;
- branch/ref и observed commit;
- inspected paths;
- method или command;
- temporal scope;
- claim class;
- limitations.

Допустимые claim classes:

```text
OBSERVED_AT_SNAPSHOT
REPORTED
SYNTHESIZED
CONFLICT
NOT_FOUND
UNKNOWN
NOT_RUN
BLOCKED
```

Отсутствие finding в текущем source boundary не доказывает глобального отсутствия.

## 12. Fallback и error handling

### 12.1 Model binding и fallback

```text
configuration-time catalog:
Spark unavailable
→ static mechanical_checker binding: Luna
→ visible model_binding record

runtime model unavailable или material insufficiency
→ BLOCKED
→ report + stop

Sol unavailable for semantic review
→ BLOCKED_REQUIRED_REVIEW_CAPABILITY
```

Current operational candidate не выполняет автоматический runtime fallback или retry внутри того же request. Замена route/model возможна только как новый explicit request после terminal report.

- static binding и любой новый replacement request записываются в routing record;
- не меняет task scope;
- не увеличивает permissions;
- не скрывает terminal result первого route;
- не называется runtime fallback, если фактически был применён configuration-time binding.

### 12.2 Conflicting results

Если субагенты расходятся:

1. сохранить оба результата;
2. классифицировать `CONFLICT`;
3. проверить различие subject/source/snapshot/method;
4. выполнить один bounded review, если это может разрешить конфликт;
5. при material unresolved conflict запросить человека;
6. не выбирать результат по model prestige или majority vote.

### 12.3 Contract violations

Следующие события завершают затронутый route:

- repository mutation by subagent;
- nested subagent spawn;
- unapproved network/provider expansion;
- subject identity change;
- scope expansion;
- missing required provenance;
- retry beyond limit;
- hidden fallback;
- generated human decision.

Результат:

```text
CONTRACT_VIOLATION
→ preserve Evidence
→ report
→ stop
```

## 13. Human checkpoints

Human confirmation требуется для:

- documentation mutation;
- canonical status change;
- product scope change;
- architecture/dependency decision;
- Risk Profile assignment;
- expansion to a new repository/provider/data boundary;
- Commit;
- Push;
- Merge;
- Release.

Human confirmation не требуется для:

- bounded read-only inventory;
- targeted source inspection в принятой boundary;
- deterministic checks;
- structured comparison;
- creation of findings and recommendations.

Material `UNKNOWN` или `CONFLICT` может потребовать человека даже внутри read-only work.

## 14. Resource controls

```yaml
max_concurrent_subagents: 2
max_delegation_depth: 1
default_retry_limit: 0
runtime_fallback_limit_per_request: 0
duplicate_research: FORBIDDEN
full_repository_scan_default: FORBIDDEN
full_docs_context_default: FORBIDDEN
raw_log_return: FORBIDDEN_UNLESS_REQUIRED
```

В pilot на Codex CLI `0.144.5` наблюдались два одновременно активных spawned agents при работающем primary thread. Это `OBSERVED_AT_SNAPSHOT`, а не переносимая гарантия semantics `max_threads` для других версий.

Context передаётся по принципу:

```text
minimum authority bootstrap
→ exact task contract
→ selected source paths
→ required output schema
```

Один agent на каждый `FTR-*` или `IDEA-*` не создаётся. Работа группируется по независимым contract questions или feature families.

## 15. Current candidate operational artifacts

После отдельного explicit human authorization были созданы следующие candidate files:

```text
.codex/config.toml
.codex/agents/mechanical-checker.toml
.codex/agents/reference-explorer.toml
.codex/agents/contract-analyst.toml
.codex/agents/semantic-reviewer.toml
```

```yaml
configuration_status: DRAFT_CANDIDATE
configuration_creation_authorization: REPORTED_IN_CONTROLLING_SESSION
configuration_correction_authorization: CONSUMED_FOR_R2_CORRECTION_EXECUTE
durable_authorization_record: NOT_CREATED
human_acceptance: NOT_GRANTED
mass_documentation_authoring_authorized: false
git_authorization: NONE
```

Их наличие не является acceptance или разрешением на массовый authoring. Пока exact hash-bound candidate не принят человеком, configuration используется только для bounded read-only pilot/validation и отдельно разрешённых correction stages.

`AGENTS.md` может получить короткое operational правило и ссылку на accepted routing contract только в отдельном authorized stage. Он не должен дублировать всю routing matrix.

## 16. Read-only pilot

До использования routing для массового authoring выполняется pilot:

1. mechanical documentation inventory;
2. targeted reference research;
3. error-to-negative-fixture extraction;
4. contract comparison;
5. semantic consistency review.

Первый routing-correctness pilot выполняет пять routed tasks и safe negative-case matrix. Sol-only comparison является отдельным measurement stage и остаётся `NOT_RUN`, пока человек его отдельно не разрешит. До comparison экономия всегда `NOT_MEASURED`.

## 17. Pilot checks

```yaml
routing_record_created: REQUIRED
correct_role_selected: REQUIRED
concurrency_at_most_two: REQUIRED
subagent_mutations: 0
nested_subagents: 0
unrecorded_fallbacks: 0
scope_expansions: 0
authority_changes: 0
output_schema_valid: REQUIRED
required_not_run_preserved: REQUIRED
```

Negative cases:

- Spark unavailable;
- Terra returns insufficient provenance;
- two results conflict;
- subagent attempts write;
- route requests nested delegation;
- request expands paths;
- retry requested after terminal failure;
- recommendation is presented as human decision.

Negative cases проверяются безопасными prompts без разрешения реальной записи, nested delegation, retry или authority change. Expected behavior — `BLOCKED` или `CONTRACT_VIOLATION`, ноль mutations и terminal stop.

## 18. Metrics

Для каждого route записываются:

- task class;
- selected role/model/reasoning;
- context boundary;
- duration;
- available usage information;
- number of useful facts;
- number of unsupported claims rejected by primary;
- corrections required;
- fallback count;
- duplicate work;
- human interruptions;
- validation result;
- reviewer findings.

Экономия считается `NOT_MEASURED`, пока отдельный measurement stage не сравнит routed tasks с Sol-only baseline на одинаковых representative tasks.

Низкий расход не является улучшением, если result не проходит required checks.

## 19. Acceptance criteria дизайна

Design может быть предложен для human review, если:

1. определён единственный writer;
2. все субагенты read-only;
3. concurrency ограничена двумя;
4. nested delegation запрещена;
5. route classes имеют deterministic model binding и terminal failure behavior;
6. static binding или новый replacement request видимы и не расширяют authority;
7. subagent request/result contracts определены;
8. Evidence имеет provenance;
9. conflicts и unknowns не скрываются;
10. human checkpoints отделены от read-only routing;
11. routing не разрешает Git;
12. pilot предшествует массовому authoring;
13. экономия требует measurements;
14. operational configuration имеет `DRAFT_CANDIDATE` guard и остаётся отдельным authorized `EXECUTE`;
15. документ не объявляет FTR-018 accepted или implemented.

## 20. Rollout sequence

```text
human review of exact design artifact
→ separate implementation plan
→ separate authorization for .codex configuration
→ create custom agents
→ separate configuration validation
→ read-only pilot
→ routing evaluation
→ human decision
→ bounded documentation authoring
→ separate validation
→ semantic review
→ human acceptance
→ separate Git decisions
```

## 21. Limitations

- Actual subscription usage savings: `NOT_MEASURED`.
- R1 custom-agent configuration validation: `PASS_FOR_SUPERSEDED_HASH_SET`.
- R1 read-only pilot: `FAIL_WITH_FINDINGS`.
- R2 correction validation: `NOT_RUN`.
- R2 routing pilot: `NOT_RUN`.
- Reference repository research under this routing: `NOT_RUN`.
- Independent semantic review of exact R2 artifact: `NOT_RUN`.
- FTR-018 item-level human disposition: `UNDECIDED`.
- Runtime implementation of routing inside AOS: `NOT_AUTHORIZED`.
- Implementation repository: `UNASSIGNED`.

## 22. Current result

```yaml
task_class: DOCUMENTATION_AGENT_ROUTING_DESIGN
stage: EXECUTE
result: DRAFT_CORRECTED
artifact: docs/ideas/AOS_Documentation_Agent_Routing_R1.md
authority: NONE
canonical_status: NOT_ASSIGNED
implementation_authorization: NONE
configuration_authorization: CONSUMED_FOR_R2_CORRECTION_EXECUTE
human_acceptance: NOT_GRANTED
mass_documentation_authoring_authorized: false
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: RUN_SEPARATE_CORRECTION_VALIDATION
stop: true
```
