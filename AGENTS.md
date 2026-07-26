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

## Обязательная точка входа

Перед существенной задачей прочитай `AOS-3/00_Core.md`. Затем открывай только релевантные документы:

- Product: `AOS-3/01_Product.md` + relevant feature в `AOS-3/06_Features.md`.
- Architecture: Product context → feature → `AOS-3/02_Architecture.md` → related lessons.
- Development workflow: `AOS-3/03_Development.md` + relevant contracts/lessons.
- Reference research: selected feature → `AOS-3/05_Reference.md` → exact paths.

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

`AOS-3/06_Features.md` — accepted inventory, но item-level `human_disposition` остаётся отдельным решением. Shared defaults в dossiers необходимо заменить feature-specific contract перед implementation planning.

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

Изменять accepted documentation можно только по bounded task с goal, target paths, allowed/forbidden changes, expected result, validation и stop conditions.

## Git boundaries

```text
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Не выполняй Commit, Push, Merge, branch deletion, force push или Release без отдельного явного решения пользователя для exact action и subject.

## Инварианты

```text
Documentation ≠ implementation
Repository presence ≠ authority
Historical PASS ≠ current PASS
PASS ≠ approval
CI PASS ≠ approval
Evidence ≠ approval
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
```

Не симулируй human approval и не повышай статус утверждения самостоятельно.

## Проверка после изменения документации

Минимально проверь:

1. В `AOS-3/` осталось ровно семь canonical `.md` files.
2. YAML frontmatter читается.
3. Markdown fences и relative links корректны.
4. `FTR-001..030` и `LES-001..042` остаются уникальными.
5. В документах нет `implementation_authorization: AUTHORIZED` или `git_authorization: AUTHORIZED`.
6. `git diff --check` не сообщает ошибок.
7. Отчёт явно перечисляет checks run и `NOT_RUN`.

## Формат существенного отчёта

1. Вывод.
2. Подтверждённые facts.
3. Proposals/inferences.
4. Conflicts и unknowns.
5. Изменённые paths.
6. Checks run / NOT_RUN.
7. Один следующий bounded action.
