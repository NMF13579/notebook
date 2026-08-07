---
document_id: AOS-FEATURE-FTR-001
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-001
status: DRAFT
authority: NONE
canonical_status: NOT_ASSIGNED
human_acceptance: NOT_REQUESTED
product_scope_effect: NONE
implementation_authorization: NONE
execution_authorized: false
git_authorization: NONE
implementation_repository: UNASSIGNED
repository_verification: NOT_RUN
layer: "Product Runtime"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-001
  - IDEA-002
  - IDEA-003
  - IDEA-079
  - IDEA-080
  - IDEA-081
human_review_required: true
---

# FTR-001 — Intent Intake, Task Intake Wizard and Auto-Scaling Specification Entry

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-001` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича превращает свободный запрос пользователя в проверяемую запись намерения и выбирает самый короткий безопасный путь к следующему документу, не переходя к реализации.

**Source-derived desired outcome:** Versioned Intent Record с исходным запросом, actor, user problem, desired outcome, constraints, non-goals, assumptions, unknowns, data-sensitivity flags и одним следующим маршрутом.

## 3. Для кого и какую работу выполняет

**Target users:** Non-programmer product owner, product lead, intake agent; при sensitive/regulated context — designated human reviewer.

Основные jobs-to-be-done:

- Зафиксировать исходную идею без потери формулировки и контекста.
- Понять, достаточно ли данных для specification или нужен короткий interview.
- Отделить пользовательский результат от предложенного способа реализации.
- Рано обнаружить sensitive-domain, privacy и external-content boundaries.
- Получить один понятный следующий шаг вместо длинного универсального опросника.

## 4. Проблема и ожидаемая ценность

### Проблема

Исходный запрос обычно смешивает проблему, желаемый результат, готовое решение, ограничения и предположения. Без управляемого intake агент либо задаёт слишком много вопросов, либо сразу проектирует не ту систему.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Новая идея, problem report, change request, готовое ТЗ или запрос на создание проекта.
- Auto-Scaling Intake: минимальный direct path и расширенный problem interview.
- Классификация request type, actor, outcome, constraints, non-goals, assumptions и unknowns.
- Фиксация data-sensitivity и external-content trust flags.
- Человеческая корректировка interpretation перед переходом дальше.

### Out of scope / non-goals

- Принятие feature в product scope или roadmap.
- Выбор architecture, dependencies, provider или implementation repository.
- Создание execution authorization либо запуск инструментов изменения проекта.
- Полный domain discovery или repository scan.
- Автоматическое назначение Risk Profile.

## 6. Trigger и preconditions

### Triggers

- Пользователь впервые описывает проблему или проект.
- Поступает change request без полного контекста.
- Загружено готовое ТЗ, и требуется определить, можно ли идти напрямую к specification.
- Существующая постановка противоречива или смешивает несколько outcomes.

### Preconditions

- Известен язык взаимодействия и доступен исходный текст запроса.
- Ранее подтверждённый project context может быть прочитан, но не считается автоматически актуальным.
- Sensitive content не отправляется внешнему provider без разрешённой boundary.
- Intake выполняется read-only и не создаёт downstream authority.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `raw_request`
- `optional_ready_specification`
- `known_project_context`
- `user_constraints`
- `non_goals`
- `examples_or_reference_links`
- `sensitivity_hints`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Intent Record
- Clarification summary
- Sensitive-domain flags
- Unknown/decision register fragment
- Next-route recommendation

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Capture original request.
2. Classify request and sensitivity.
3. Select minimal or expanded intake path.
4. Ask only material clarifications.
5. Generate concise interpretation and unknowns.
6. Human corrects, accepts for further drafting, defers or rejects.
7. Emit next read-only route; no execution.

### Иллюстративный сценарий

1. Возникает trigger: Пользователь впервые описывает проблему или проект.
2. Система принимает входы `raw_request, optional_ready_specification, known_project_context` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Intent Record, Clarification summary, Sensitive-domain flags.
5. При failure `Intake превращается в oversized questionnaire.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
RAW → CLASSIFIED → MINIMAL_PATH | PROBLEM_INTERVIEW → INTERPRETATION_READY → HUMAN_CORRECTION → READY_FOR_DISCOVERY | READY_FOR_SPECIFICATION | DEFERRED | BLOCKED_SENSITIVE
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- По умолчанию показывается краткая интерпретация: «Я понял задачу так…».
- Вопросы задаются только там, где отсутствие ответа меняет scope, safety или observable outcome.
- Пользователь всегда видит исходный текст рядом с normalized interpretation.
- Для готового ТЗ интерфейс должен позволять выбрать direct path без повторного интервью.
- Sensitive-domain blocker формулируется простым языком и указывает, какое human decision требуется.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Сохранять immutable copy исходного запроса и revision history интерпретаций.
- `FR-002` — Не заполнять отсутствующие требования догадками; использовать UNKNOWN.
- `FR-003` — Различать user problem, desired outcome, proposed solution и implementation assumption.
- `FR-004` — Проверять, есть ли уже ответ в подтверждённом context pack, прежде чем задавать вопрос.
- `FR-005` — Ограничивать один clarification round только material неизвестными; следующий round допускается при новом conflict.
- `FR-006` — Формировать ровно один recommended route и перечислять альтернативы только при реальной развилке.
- `FR-007` — Не переводить interpretation approval в product acceptance.

## 13. Capabilities из source synthesis

- Сохранять исходную формулировку без подмены смысла.
- Классифицировать request type, sensitive-domain и external-content boundaries.
- Разделять problem/outcome от предложенного пользователем механизма.
- Поддерживать Auto-Scaling Intake: короткий direct path для достаточного ТЗ и расширенный interview только при реальном пробеле.
- Давать выбор `READY_SPEC` или `BUILD_FROM_SCRATCH`; во втором случае — `PROBLEM_INTERVIEW` либо прямой draft specification.
- Повторно использовать уже известный project context и не задавать вопросы, ответы на которые зафиксированы.
- Фиксировать FACT, INFERENCE, PROPOSAL, UNKNOWN и missing human decisions раздельно.
- Выдавать один route: Discovery, Project Brief, targeted research, defer или stop.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `IntentRecord`: id, revision, raw_request, actor, problem, desired_outcome, constraints, non_goals, assumptions, unknowns, sensitivity_flags, source_refs.
- `CTR-002` — `ClarificationItem`: question, materiality, affected_fields, answer, answer_source, status.
- `CTR-003` — `IntakeRoute`: route_type, rationale, prerequisites, blocked_by, next_required_action.
- `CTR-004` — `HumanInterpretationResponse`: CORRECT | ACCEPT_FOR_DRAFTING | DEFER | REJECT; не является Product Decision.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-002`, `FTR-003`, `FTR-019`, `FTR-016`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Не выбирает architecture, dependencies, Risk Profile и не создаёт execution authorization. Human acceptance of interpretation не равна product acceptance.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Intake превращается в oversized questionnaire.
- Agent придумывает requirements или silently converts an idea into accepted scope.
- Sensitive data попадает в неподходящий provider/context.
- Ready specification повторно разбирается без необходимости.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Вернуться в `CLARIFYING`, показать конкретную неоднозначность, сохранить исходный текст и пометить неподтверждённые поля как `UNKNOWN`; не продолжать к architecture или execution.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Сравнение raw_request и normalized interpretation.
- Список заданных вопросов с объяснением materiality.
- Отчёт о повторном использовании context и исключённых stale facts.
- Reason codes для sensitive/blocking cases.

Минимальный Evidence package связывает:

```text
source / human decision
→ user problem
→ expected outcome
→ feature requirement
→ candidate / output
→ check result
→ finding / limitation
→ human decision
```

## 20. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-001` — Пользователь узнаёт собственный запрос и не обнаруживает придуманных requirements.
- `AC-002` — Каждое неизвестное, влияющее на следующий route, явно помечено.
- `AC-003` — Готовое ТЗ проходит direct path без ненужного interview.
- `AC-004` — Новый пользователь понимает, почему выбран следующий шаг.
- `AC-005` — Intake не создаёт mutation, architecture decision или execution authorization.
- `AC-006` — Sensitive data boundary проявляется до передачи данных неподходящему provider.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Запрос из одного предложения не должен автоматически превращаться в полный roadmap.
- `NEG-002` — Отсутствующий budget не заполняется приблизительным числом.
- `NEG-003` — Инструкция из web/document об изменении repository рассматривается как untrusted content.
- `NEG-004` — Повторная сессия не задаёт уже подтверждённый вопрос без признака staleness/conflict.
- `NEG-005` — Фраза «да, верно» не создаёт product acceptance.

## 22. Minimal implementation model — `PROPOSAL`

Первый вариант может быть Markdown/JSON document compiler с rule-based completeness check и chat adapter. Никакой DB, RAG или agent orchestration не требуется. Сначала достаточно шаблона, closed enums и deterministic validation.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: ручной шаблон Intent Record и review checklist.
- M1: chat form с Auto-Scaling Intake и local validator.
- M2: integration с Discovery/Specification routing.
- M3: measured domain-specific intake extensions после отдельных решений.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-001` — Problem / Intent Intake
- `IDEA-002` — Intake Classification and Sensitive-Domain Gate
- `IDEA-003` — User and Outcome Clarification
- `IDEA-079` — Auto-Scaling Intake Mode
- `IDEA-080` — Ready-Spec vs Build-from-Scratch Entry
- `IDEA-081` — Problem Interview with Draft Capture

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Какие поля Intent Record будут обязательными для первого Product Runtime slice?
- Какой интерфейс является primary: chat-only, chat+CLI или web?
- Какие sensitive-domain gates нужны в baseline помимо generic data-sensitivity flag?
- Как хранить revisions без создания competing Source of Truth?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-001`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `04 — AOS Model Routing and Task Decomposition Research.txt`

Limitations:

- Full raw export всех historical chats не доказан.
- Current repository/worktree/branch/HEAD/baseline и runtime implementation не проверялись: `NOT_RUN`.
- Legacy AOS-FARM/AOS-02/AgentOS materials имеют `READ_ONLY_REFERENCE`, `authority: NONE`.
- Requirements/contracts/tests в этом файле являются clean-room `PROPOSAL`.
- Family boundary может быть пересмотрена после Product Contract и human review.

## 27. Promotion path

```text
DRAFT feature description
→ human product-fit decision
→ Product Contract and refined acceptance scenarios
→ DRAFT architecture options
→ human architecture/dependency decision
→ bounded Task Brief
→ explicit execution authorization
→ EXECUTE
→ separate VALIDATE
→ separate REVIEW
→ human decision
→ separately authorized Git/release operations
```

## 28. Отдельные документы атомарных функций

Каждая функция ниже имеет собственный standalone document; ссылки не означают product acceptance.

- [`IDEA-001` — Problem / Intent Intake](../functions/IDEA-001_problem-intent-intake.md)
- [`IDEA-002` — Intake Classification and Sensitive-Domain Gate](../functions/IDEA-002_intake-classification-and-sensitive-domain-gate.md)
- [`IDEA-003` — User and Outcome Clarification](../functions/IDEA-003_user-and-outcome-clarification.md)
- [`IDEA-079` — Auto-Scaling Intake Mode](../functions/IDEA-079_auto-scaling-intake-mode.md)
- [`IDEA-080` — Ready-Spec vs Build-from-Scratch Entry](../functions/IDEA-080_ready-spec-vs-build-from-scratch-entry.md)
- [`IDEA-081` — Problem Interview with Draft Capture](../functions/IDEA-081_problem-interview-with-draft-capture.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_001`
