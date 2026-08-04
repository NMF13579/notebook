# AGENTS.md — NMF13579/notebook

## Назначение

Этот repository является принятой проектной базой знаний AOS. Он предназначен для документации, product/architecture design, feature selection и targeted research.

```yaml
repository_role: ACTIVE_PROJECT_KNOWLEDGE_REPOSITORY
implementation_repository: UNASSIGNED
runtime_code_allowed_here: false
implementation_authorization: NONE
git_authorization: NONE
```

Не создавай здесь runtime-код AOS, product package, CI/CD продукта, deployment configuration или database без отдельного explicit human decision о смене repository role.

Документационная задача не является задачей реализации. При создании или корректировке документации не создавай implementation code, scaffolding, executable prototype, product tests или runtime infrastructure. Подготовка implementation brief описывает будущую реализацию, но не выполняет её.

## Обязательная точка входа

Перед существенной задачей прочитай `docs/00_Core.md`. Затем открывай только релевантные документы:

- Product: `docs/01_Product.md` + relevant feature в `docs/06_Features.md`.
- Architecture: Product context → feature → `docs/02_Architecture.md` → related lessons.
- Development workflow: `docs/03_Development.md` + relevant contracts/lessons.
- Reference research: selected feature → `docs/05_Reference.md` → exact paths.

Не загружай все семь документов и весь legacy repository без доказанной необходимости.

## Владение фактами

- `00_Core.md` — identity, authority, source precedence, safety.
- `01_Product.md` — product facts и boundaries.
- `02_Architecture.md` — architecture baseline и contract classes.
- `03_Development.md` — development workflow.
- `04_Lessons.md` — failures, lessons и regressions.
- `05_Reference.md` — provenance и research routing.
- `06_Features.md` — feature inventory и dossiers.

Не создавай параллельные owners или новые top-level knowledge catalogs. Ссылайся на owner вместо копирования утверждения.

## Статус пакета

Пакет принят как knowledge baseline с `FACT_CLASS_SCOPED` authority.

Это не означает:

- принятие каждой feature;
- implementation readiness;
- runtime verification;
- permission на edit/commit/push/merge/release.

`docs/06_Features.md` — accepted inventory, но item-level `human_disposition` остаётся отдельным решением. Shared defaults в dossier необходимо заменить feature-specific contract перед implementation planning.

Для выбранного vertical slice такой contract может быть компактным Markdown implementation brief без YAML и отдельного lifecycle package. Он должен содержать достаточно сведений для будущей реализации: actor, trigger, I/O, main flow, failures/recovery, constraints, acceptance, negative cases и material unknowns.

## Упрощённая документационная работа

Документация служит последующей реализации продукта и не является самостоятельной целью.

Для low/trivial documentation work используй минимально достаточный маршрут:

```text
Short Markdown Task
→ bounded documentation edit
→ focused checks
→ concise report
→ stop
```

Short Markdown Task достаточно описать через:

1. Цель.
2. Контекст.
3. Что сделать.
4. Что не делать.
5. Готово, когда.

Для обычной обратимой документационной задачи не создавай без доказанной необходимости:

- YAML task blocks;
- отдельные lifecycle artifacts для `PLAN`, `EXECUTE`, `VALIDATE`, `REVIEW`, `DELIVER`;
- stage reports;
- acceptance records;
- activation records;
- lifecycle diagrams;
- hashes каждого документа;
- отдельное human approval каждого обычного редакционного шага;
- новые документы, дублирующие `docs/00_Core.md`–`docs/06_Features.md`.

Упрощённая модель отменяет лишний ceremony, но не safety semantics:

- scope известен до edit;
- существенный unknown не скрывается;
- один run выполняет только одну bounded работу;
- scope expansion требует отдельного human decision;
- completion, finding или failure завершается report и stop;
- validation не исправляет subject;
- Task Brief не является Execution Authorization;
- protected actions и Git actions требуют отдельных полномочий.

`docs/03_Development.md` остаётся canonical owner workflow, stage boundaries, validation и reporting rules. Этот раздел задаёт default routing для простой документационной работы, а не создаёт параллельный workflow.

Используй formal или расширенный процесс только когда его требует material risk, independent validation, protected operation, explicit human decision или правило из `docs/00_Core.md` / `docs/03_Development.md`.

Остановись и запроси решение, если:

- отсутствует существенное product decision;
- authoritative sources конфликтуют;
- требуется расширить scope;
- требуется runtime implementation;
- требуется изменить repository role или security boundary;
- требуется Commit, Push, Merge, Release или другое protected action.

## Reference repositories

- https://github.com/NMF13579/AOS-FARM/tree/dev
- https://github.com/NMF13579/AgentOS/tree/dev

Используй их только как `READ_ONLY_REFERENCE`, `authority: NONE`.

Правильный маршрут:

```text
selected feature
→ explicit knowledge gap
→ narrow research question
→ exact repository/ref/commit/path
→ docs/contracts/tests/code
→ classified finding with provenance
```

Не переносить автоматически topology, milestones, Control Plane, dependencies, lifecycle, approval semantics или stored readiness claims. Если reference недоступен, сообщи `BLOCKED_REFERENCE_ACCESS` или `NOT_RUN`; не восстанавливай его по памяти.

## Разрешённые действия по умолчанию

Без отдельной write-задачи разрешены read-only inspection, audit, conflict/gap analysis, DRAFT proposals, Markdown/link checks и targeted research.

Direct current human instruction, которая явно просит изменить конкретную документацию в bounded scope, является разрешением только на этот documentation edit. В ней должны быть понятны goal, subject или target paths, allowed/forbidden changes и expected result либо критерии готовности.

Созданный или принятый Task Brief сам по себе не разрешает edit, runtime implementation или Git action.

Не расширяй documentation edit за пределы explicit task. Если target paths нельзя определить безопасно, сначала верни decision-ready proposal или запроси одно необходимое решение.

## Git boundaries

```text
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Не выполняй Commit, Push, Merge, branch deletion, force push или Release без отдельного явного решения пользователя для exact action и subject.

## Инварианты

```text
Documentation ≠ implementation
Documentation task ≠ runtime implementation
Repository presence ≠ authority
Historical PASS ≠ current PASS
PASS ≠ approval
CI PASS ≠ approval
Evidence ≠ approval
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
Task Brief ≠ Execution Authorization
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Не симулируй human approval и не повышай статус утверждения самостоятельно.

## Проверка после изменения документации

Выполняй проверки пропорционально изменённому предмету.

Для обычной локальной Markdown-правки минимально проверь:

1. Изменение соответствует goal, scope и target paths.
2. Markdown fences и затронутые relative links корректны.
3. `git diff --check` не сообщает ошибок, если доступен repository checkout.
4. Отчёт перечисляет фактически выполненные checks и существенные `NOT_RUN`.

Дополнительно проверяй package-wide invariants только если изменение действительно их затрагивает:

1. В `docs/` осталось ровно семь canonical `.md` files.
2. YAML frontmatter читается.
3. `FTR-001..030` и `LES-001..042` остаются уникальными.
4. В документах нет `implementation_authorization: AUTHORIZED` или `git_authorization: AUTHORIZED`.
5. Cross-document contracts и owner boundaries не нарушены.

Не запускай полный аудит пакета после каждой локальной редакции без risk-based или explicit причины.

## Формат отчёта

Для обычной документационной задачи достаточно краткого Markdown-отчёта:

1. Что сделано.
2. Какие paths изменены.
3. Какие checks выполнены.
4. Что осталось `NOT_RUN`, `UNKNOWN` или вне scope.

При material conflict, существенном unknown, high-risk work, independent validation или explicit human request используй расширенный формат:

1. Вывод.
2. Подтверждённые facts.
3. Proposals/inferences.
4. Conflicts и unknowns.
5. Изменённые paths.
6. Checks run / `NOT_RUN`.
7. Один следующий bounded action.
