---
package: AOS_Project_Knowledge_Baseline
package_revision: R4-RU
updated: '2026-07-26'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
implementation_authorization: NONE
git_authorization: NONE
semantic_audit: COMPLETED_WITH_CORRECTIONS
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
audited_source_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
audited_source_blob_sha: c60c39b4bee652cde2fd2e38f81dc12b498aa817
active_path: docs/03_Development.md
document_language: ru
technical_identifiers_language: en
document_role: CANONICAL_DEVELOPMENT_WORKFLOW
authority_scope:
- task_workflow
- stage_boundaries
- validation_rules
- reporting_rules
- git_action_boundaries
---

# 03 — Разработка

## 1. Граница статуса

Документ задаёт принятый normative workflow для подготовки и проверки работы. Он не является Task Brief, Execution Authorization или разрешением на конкретную mutation либо Git-operation.

## 2. Сквозная модель проектирования и реализации

Процесс строго разделен на проектирование документации и runtime-реализацию.

### Проектирование документации (Workspace → AOS)

```text
Knowledge Baseline
↓
Workspace (Source Synthesis + Drafts)
↓
Pass 1 (Product Model)
↓
Structural Review
↓
Pass 2 (Architecture Contracts + Engineering Workflow Semantics)
↓
Integration Review
↓
Global Design Freeze
↓
Publish to AOS (Deliverable)
```

### Runtime Implementation (Реализация)

После публикации Deliverable в AOS:

```text
Implementation Roadmap
↓
Slice
↓
Task
↓
bounded Task Brief
→ repository preflight
→ explicit Execution Authorization
→ smallest scoped implementation
→ Stage Report and stop
→ separate VALIDATE when required
→ REVIEW
→ human decision
→ separate Commit / Push / Merge / Release
→ handoff and lesson proposal
```

## 3. Семантические различия

Analysis ≠ execution; Plan ≠ implementation; file presence ≠ behavior; readiness ≠ authorization; execution ≠ verification; test PASS ≠ acceptance; CI PASS ≠ approval; verification ≠ commit permission; Commit ≠ Push ≠ Merge ≠ Release; UNKNOWN ≠ OK; NOT_RUN ≠ PASS.

## 4. Условия входа

Feature должна иметь purpose/value, actors, trigger/preconditions, I/O, happy path, states, failures/recovery, dependencies, authority boundaries, acceptance, negative scenarios, unknowns и targeted reference questions.

## 5. Процесс, масштабируемый по риску

### Низкий / trivial

Scope → one reversible change → focused check → concise report. No redundant architecture chain.

### Средний

Explicit acceptance, short plan, relevant regression и handoff.

### Высокий / protected

Pinned baseline, inventory, protected paths, explicit authorization, rollback, Evidence package и human review.

### Критический / destructive / sensitive

Stop-before-action, least privilege, data/provider boundary, recovery plan и explicit human decision.

## 6. Feature-specific documentation package

Для feature, чей exact `feature_id` выбран человеком либо явно привязан к документационной задаче current human instruction или human-accepted artifact, применяется bounded authoring-механика внутри этого canonical workflow:

```text
Selected Feature
↓
Skeleton
↓
Saturation
↓
Harmonization / Review
↓
READY_FOR_HUMAN_REVIEW
```

Это не отдельный lifecycle, не замена Global Design workflow из раздела 11 и не Runtime stage. Механика создаёт reviewable feature-specific documentation package, но не принимает feature или architecture, не разрешает implementation и не предоставляет Git authority.

### Граница package

До authoring агент bind exact `feature_id`, текущий human disposition, цель package, upstream owners/sources, allowed paths и material gaps. Ядро package — feature-specific Feature Contract / Feature Passport. Отдельный Architecture Contract нужен при material boundary/state/ownership или external contract, DRAFT ADR — при decision-ready выборе между значимыми вариантами, engineering handoff/brief — когда принятые product/architecture contracts требуется передать будущей реализации. Product crosswalk или любой из этих элементов выделяется в отдельный artifact только при distinct fact class/owner, independent review boundary или потере однозначности внутри ядра. Один artifact может совмещать несколько логических разделов, но не может смешивать их authority.

Package map, index или review summary остаются derived navigation/Evidence и не становятся владельцами product или architecture facts. DRAFT ADR может подготовить вопрос, варианты, trade-offs и Evidence, но `selected_option` остаётся незаполненным до exact human decision. Engineering artifact может фиксировать принятые contract shapes, examples, constraints, acceptance и negative cases; он не выбирает repository, toolchain, internal structures, storage, adapters, algorithms или иное implementation HOW без accepted upstream decision и не является Execution Authorization.

### Skeleton

Сначала создать целостный каркас всего package: inventory artifacts/sections, role и fact owner каждого элемента, source/provenance, связи, expected outputs, review criteria и видимые `UNKNOWN`/gaps. Каркас должен покрывать обязательные поля feature dossier и требуемые conditional artifacts до глубокой детализации. Пустое место помечается `UNKNOWN`, `NOT_APPLICABLE` или explicit decision request, а не заполняется предположением.

### Saturation

Затем насыщать каркас в порядке authority: current human decisions → accepted canonical sources → current repository observations в разрешённой boundary → targeted research/reference findings → явно помеченные synthesis/inference. Заполнять purpose/users, trigger/preconditions, behavior, I/O, flow/states, failures/recovery, dependencies, constraints, acceptance и negative scenarios только до необходимой feature-specific глубины. Legacy используется read-only для exact gap и не переносит автоматически topology, status, approval или implementation HOW.

### Harmonization / Review

После насыщения снова рассматривать exact artifacts как один package. Проверить vocabulary, provenance, owner boundaries, cross-links, traceability `intent → behavior → contracts → acceptance/negative cases`, согласованность состояний и отсутствие скрытого HOW или authority expansion. Внутри той же authorized documentation task агент может исправлять только bounded defects: терминологию, ссылки, дублирование, formatting и пропуски, однозначно восполнимые из уже authoritative upstream source. Новый scope, material conflict, отсутствующее human-only решение или новая architecture choice требуют explicit finding/decision и не исправляются догадкой.

Harmonization / Review является authoring-фазой, а не независимым `VALIDATE`: bounded corrections здесь допустимы. Если risk требует separate validation, после authoring фиксируется exact candidate, а validator работает read-only и не исправляет subject.

### Readiness gate

Package получает outcome `READY_FOR_HUMAN_REVIEW`, только если:

1. exact subject, inventory, owners, sources и связи определены;
2. обязательные feature-specific fields достаточно насыщены для заявленной human review;
3. необходимость или отсутствие отдельных Architecture/ADR/Engineering artifacts обоснованы;
4. material contradictions отсутствуют, а remaining unknowns видимы и ограничивают только зависимые claims;
5. semantic, cross-document и focused mechanical checks прошли;
6. report перечисляет Evidence, findings, unknowns, `NOT_RUN` и одно следующее human action.

Минимальные checks охватывают exact feature/disposition binding, обязательные dossier fields, owner/source/status markers, rationale conditional artifacts, traceability, explicit unknown/decision requests, Markdown links/fences и отсутствие скрытых authority grants или implementation HOW. Незакрытое human-only decision совместимо с `READY_FOR_HUMAN_REVIEW` только когда package делает exact decision request и не заявляет зависимый от решения вывод; иначе readiness остаётся `BLOCKED` или `UNKNOWN` в затронутой boundary.

`READY_FOR_HUMAN_REVIEW` — package-readiness outcome, а не новый owner document maturity: artifacts сохраняют canonical maturity/status до human decision. Technical `PASS` — Evidence проверки. `PASS ≠ approval`; `READY_FOR_HUMAN_REVIEW ≠ HUMAN_ACCEPTED`; ни один из этих результатов не означает implementation readiness, Execution Authorization или Git permission.

### Targeted reconstruction через feature

1. Bind feature из `06_Features.md`, уже выбранную или явно названную человеком; не изменять её disposition агентом.
2. Подтвердить user/problem/outcome/disposition.
3. Сформулировать exact gaps.
4. Bind legacy repository/ref/SHA/paths read-only.
5. Inspect docs/commands → contracts/schemas → tests/negative fixtures → implementation → reports/plans.
6. Classify findings.
7. Обновить Feature Passport.
8. Не копировать legacy topology.
9. Stop when question answered or scope expands.

## 7. Ленивая декомпозиция

```text
Epic → Stage → Sub-stage only when material → executable Task
```

Child создаётся только по authority boundary, independent validation, material risk, protected operation, distinct acceptance или dependency. Closed children не доказывают parent completion.

## 8. Task Brief и Execution Authorization

Task Brief описывает goal/scope/constraints/validation. Authorization создаётся отдельно человеком, bind к exact task/subject, ограничен stage/operations/paths, имеет expiry/consumption и не разрешает Git actions.

## 9. Preflight репозитория

Проверить root, worktree, branch, HEAD, baseline, staged/unstaged/untracked, diff, nested repos, symlinks, paths, interpreter/dependencies, sandbox/network/remote, temp boundary, stop conditions, candidate identity, source/destination и credentials/data boundary.

```text
IN_SCOPE_EXISTING | OUT_OF_SCOPE_USER_STATE | ENVIRONMENT_NOISE | GENERATED_DISPOSABLE | UNKNOWN_MATERIAL
```

## 10. Модель стадий Runtime-реализации

Эти стадии применяются исключительно к написанию кода и защищенным операциям. Создание и редактирование документации в `workspace/` не требует прохождения через PLAN, EXECUTE, VALIDATE и REVIEW.

### PLAN
Read-only. Decision-ready Task Brief, risks, validation, stop conditions.

### EXECUTE
Exact authorized scope, one stage, no hidden next stage, no unrelated cleanup; terminal result → report and stop.

### VALIDATE
Read-only exact candidate. Does not fix. Independent validation required only when risk/task demands it.

### REVIEW
Read-only assessment/recommendation. No simulated acceptance or correction.

### DELIVER
Handoff package, not stage or Git permission.

## 11. Жизненный цикл документации (Workspace → AOS)

Документационный цикл избавлен от тяжеловесных инженерных проверок.

1. **Workspace**: Source synthesis, research, drafts and superseded working artifacts live in `workspace/`; presence there does not create canonical ownership.
2. **Pass 1 (Product Model)**: Define product goals, boundaries, actors, journeys, feature scope and preserved product decisions at WHAT level. Working output: `workspace/DRAFT_01_PRODUCT_MODEL.md`; published path after all gates: `AOS/01_PRODUCT_MODEL.md`.
3. **Structural Review**: Check product/architecture separation, source traceability and the WHAT / implementation-HOW boundary. Pass 2 starts only after the exact candidate has no material structural conflict.
4. **Pass 2 (Architecture Contracts + Engineering Workflow Semantics)**: Define architecture/state contracts and design-level workflow, authority, validation/evidence, recovery and handoff semantics. Working outputs: `workspace/DRAFT_02_ARCHITECTURE_CONTRACTS.md` and `workspace/DRAFT_03_ENGINEERING_PIPELINE.md`; published paths after all gates: `AOS/02_ARCHITECTURE_CONTRACTS.md` and `AOS/03_ENGINEERING_PIPELINE.md`. Pass 2 does not own schemas, exact I/O, serialization, storage, adapters, toolchain, repository topology or other implementation HOW.
5. **Integration Review**: Check the exact three-file package for consistent vocabulary, traceability, ownership, state/result separation and absence of material cross-document conflicts. A technical PASS is Evidence, not human acceptance.
6. **Global Design Freeze**: Bind exact paths and SHA-256 values after review and explicit human decision. Preserved feature-specific inputs, future implementation decisions and non-blocking global decisions are allowed when explicitly classified; a material unresolved product/architecture conflict blocks Freeze.
7. **Publish to AOS**: Copy the exact reviewed working outputs to `AOS/01_PRODUCT_MODEL.md`, `AOS/02_ARCHITECTURE_CONTRACTS.md` and `AOS/03_ENGINEERING_PIPELINE.md` without content drift. These three published paths are the current deliverable subject. Review, acceptance and Freeze identities are stored separately under `AOS/reviews/`, `AOS/decisions/` and `AOS/GLOBAL_DESIGN_FREEZE.md`.

**Локальные корректировки (Local Corrections)**:
Исправление опечаток, ссылок и форматирования в `workspace/` выполняется без полного ревью-цикла по маршруту: `Short Markdown Task → edit → check → report → stop`.

**Правила публикации deliverable (Handoff)**:
Пакет в `AOS/` передается coding agent'у как read-only Source of Truth в границах exact Freeze identity. Coding agent не имеет права изменять документы в `AOS/` самостоятельно. Any post-Freeze content change requires an explicit Reopen, a new review subject and a new Freeze identity.

## 12. Отчёт стадии

```yaml
task_id:
stage:
result:
starting_identity:
ending_identity:
changed_paths: []
checks_run: []
checks_not_run: []
findings: []
limitations: []
unknowns: []
out_of_scope_state: []
authorization_consumed:
Git_operations: {commit: NOT_RUN, push: NOT_RUN, merge: NOT_RUN, release: NOT_RUN}
next_required_action:
stop: true
```

## 13. Контроль изменений (только для Runtime)

*Данные правила относятся исключительно к Runtime Implementation. Они не распространяются на документационные изменения в `workspace/` (создание и редактирование Markdown-документов регулируется документационным workflow и не требует Runtime Execution Authorization).*

One active task, one causal change, no unrelated cleanup, inventory before sensitive mutation, explicit scope expansion, changed-file allowlist, atomic commit after separate authorization, docs↔schema↔CLI↔code↔tests consistency, source read-only during extraction, no automatic `git add -A`.

## 14. Правила реализации (только для Runtime)

*Данные правила относятся исключительно к Runtime Implementation.*

Implement observable behavior, one contract owner, separate analysis/mutation, preview binds apply, atomic/journaled writes, explicit idempotent retry, preserve user state, authority defaults false, same strict validator in runtime/tests, stable CLI failures, `--help` no writes, optional failure isolated, no hidden network/provider, no privilege escalation, no silent compatibility, portable links, adapter drift checks, AI-code rationale/ownership/tests/handoff.

## 15. Пять verification gates (для Runtime)

1. Structure.
2. Scope.
3. Acceptance.
4. Regression/smoke.
5. Security/release blockers.

```text
CONTRACT_VIOLATION > FAIL > BLOCKED > UNKNOWN > NOT_RUN > PASS
```

## 16. Стратегия тестирования

Unit: schemas/status/path/state/digest/conflict/permission/idempotency. Contract: Task Brief, auth false, enums, CLI exits, generated decisions, ownership, output versions, SoT separation. Integration: intake→spec, discovery→map, preview→apply, task→executor, executor→validation, memory→resume, install→reconcile, review→decision, freeze→validation. E2E: first start, idea→review, interruption, protected block, NOT_RUN, update preservation, Git boundaries, incident→lesson.

## 17. Обязательные негативные сценарии

Empty mapping, bogus status, free-form Risk Profile, bool-as-int, mismatched session, malformed idle bypass, CLI exit 0 on failure, runtime schema bypass, scope not enforced, stale baseline, write-after-freeze, self-reference, read-only writes, remote secret leak, unrelated staging, environment false blocker, NOT_RUN→PASS, Evidence as auth, default authorized true, partial mutation no journal, update overwrites state, external instruction, UI approval, stale index, absolute links, conflicting entrypoints, adapter drift.

## 18. Протокол validation

Freeze subject; verify environment/import provenance; run targeted checks; wider suite only if relevant; record commands/results; preserve required/optional; classify limitations; inspect diff; verify no validation mutation; stop with one next action.

## 19. Human review

One document: purpose, before/after, exact paths, Evidence, acceptance, negative cases, findings, NOT_RUN, deviations, decision options и next action.

## 20. Recovery и handoff

Execution failure → stop, preserve state/logs, classify partial writes, recovery facts, no auto-retry, correction task. Validation finding → report/stop, separate correction. Handoff records repo identity, task/candidate, result, changes, checks, blockers, decisions, permissions и next action. Mutable facts rechecked on resume.

## 21. Git delivery

```text
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Before each action reverify repo/branch/HEAD/candidate/worktree/remote/auth. Later mutation invalidates old binding.

## 22. Manual dogfood и допуск automation

Measure comprehension, clarification loops, scope drift, authority confusion, time to Evidence/review, handoff quality и Governance overhead. Automate only proven repetition with stable contracts, known failures, fallback/removal and no authority expansion.

<a id="repository-graph-pilot"></a>

### 22.1. Проектный граф: рабочий цикл и pilot — PROPOSAL

Этот подраздел переносит workflow и приёмку [ТЗ R2](05_Reference.md#repository-graph-tz). [Назначение](01_Product.md#repository-graph-purpose) и [архитектурный контракт](02_Architecture.md#repository-graph-contract) имеют собственных владельцев. Предлагаемый маршрут применяется только к задаче, в которой выбран graph-assisted context; каждая обычная правка не обязана запускать картографирование. Прямое исследование остаётся допустимым положительным маршрутом работы без графа.

**До задачи:** проверить применимую область карты, запросить context/impact и открыть первичные источники существенных решений. В фиксированном pilot Slice 1 допустим полный rebuild малого scope вместо ещё не реализованного check/refresh; offline query сохраняет `repository_currentness: NOT_RUN`. Найденные ограничения и evidence references включаются в существующий task-local Context Pack по необходимости; выдача карты не заменяет Task Brief, permission или validation criteria.

**После изменения:** выполнить только разрешённый refresh либо rebuild малого scope; проверить semantic diff, новые/удалённые связи, test bindings и pending coverage. Тесты продукта не запускаются неявно. **При handoff:** передать graph digest, observation boundary, compact query и следующий probe как дополнение к сведениям §20; весь payload карты читать не требуется. Bootstrap содержит маршрут к owner/tool instruction, а не копию контракта.

#### Реальный вопрос и oracle до разработки

До Slice 1 задаются exact snapshot/corpus, один реальный вопрос о зависимости, существенные правильные связи, допустимые unknowns и oracle из первичных источников. Reader не определяет собственный правильный ответ. Каждый поддержанный способ обнаружения связи имеет достаточное основание и неоднозначный случай, который должен остаться unresolved.

Кандидат для AOS — «подготовленная задача → preflight → условия допуска исполнения». Вопросы: какие обязательные входы нужны; кто их предоставляет; кто потребляет результат; какие условия окружения существенны; чем проверяется стык. Oracle различает исходный код, утверждение контракта и результат запуска. Условия окружения не объявляются реально выполненными из наличия configuration или test. Это тематический пример из `AOS3-S09`, не выбор FTR/будущей topology и не разрешение защищённого исполнения. При выборе другого сценария он также должен проверять существенный системный стык, а не только известные импорты.

На отдельном примере изменения обязательного входа требуется обнаружить потребителя и необходимую повторную проверку/refresh. Выбранный положительный сценарий при выполненных prerequisites должен давать корректный результат. Корректный отказ проверяется отдельно; инструмент, всегда отвечающий UNKNOWN или отказом, положительную проверку не проходит.

#### Срезы

1. **Полезный ответ:** один язык, одно окружение, небольшой scope и несколько patterns; build, validate, exact query и минимальные context/impact. Coverage, source bindings, безопасная публикация и resource limits присутствуют с первого writer. Full rebuild допустим. Проверяются реальный вопрос/oracle, положительный и отрицательный случаи; общая pagination и optional batch могут быть отложены при честном ограничении pilot и явном отказе на превышении. Выход — ответ, сравнение с обычным поиском и решение о следующем срезе.
2. **Сопровождение доказанного участка:** check, changed/new/deleted sources, selective refresh, partial coverage, NO_CHANGE, worktree binding и recovery/concurrency. Сценарий повторяется после изменения источников. Observation batch включается только при доказанной необходимости.
3. **Повторяемая польза:** полные context/impact/detail с budgets/continuation, нужные feature/contract bindings и сравнение трёх видов задач. Проверяются все применимые критерии выбранной версии; частичный срез не выдаётся за весь контракт.

Это срезы вспомогательного инструмента, а не замена product-first последовательности AOS. Автоматизация допускается после доказанного повторения ручного сценария. Отказ от инструмента должен оставлять возможность продолжить обычную разработку.

#### Приёмка и negative cases

ID в таблице относятся к исходному R2, а не к уже выполненным тестам. Полный перечень fixtures сохранён в [черновике, §§14.1–14.2](../workspace/AOS_REPOSITORY_GRAPH_TZ_R2_DRAFT_2026-09-13.md). Для выбранного среза требуется исполняемая проверка применимых случаев; при данном документационном переносе все запуски остаются `NOT_RUN`.

| Область | Критерии R2 | Обязательная проверка |
|---|---|---|
| Наблюдаемая семантика | AC-01–03, AC-10; N-01–05, N-07 | Пустой repo без выдуманного runtime; правильные typed seeds; направления/parallel edges; test binding без PASS; bounded NOT_FOUND; rename без догадки; rebuild/round-trip сохраняют смысл, types, evidence и uncertainty, а не только counts |
| Выдача и impact | AC-04, AC-13–14; N-09, N-11, N-17–19 | Consumer за artifact найден в поддержанном impact; depth frontier видим; stubs учтены; весь результат доступен по страницам; cursor mismatch и oversized record дают явный отказ |
| Актуальность | AC-05–08; N-06, N-08, N-10, N-12 | Новый consumer при неизменном producer обнаружен либо явно pending; dirty tree при прежнем HEAD обнаружен; partial refresh не повышает непроверенное; source-version mismatch видим; NO_CHANGE не переписывает bytes/mtime; graph-only change не создаёт loop |
| Публикация и worktrees | AC-09, AC-11; N-14–15 | Старый/новый artifact целостен; второй writer или failure не теряет обновление; bindings разных worktrees не смешаны; shared Git metadata не заменяет source delta |
| Полезность и границы | AC-12; N-13, N-16 | Ответ сверяем с primary source; symlink/traversal/instruction не расширяют scope; read/check/query/validate/help без скрытых writes и test execution; graph не выдаёт permission |
| Optional batch | AC-15; N-20 | Stale/conflicting/missing batch не повышает claims; rebuild учитывает exact input либо объявляет ограничение |
| Пределы обработки | AC-16; N-21–22 | Oversized source/graph/batch, сложный input, превышение time/memory дают заявленный failure/partial outcome с сохранностью active graph и явной coverage |

Slice 1 охватывает применимые AC-01–03, AC-09–10, AC-12–13, AC-16 и negatives integrity, untrusted input, source bindings, publication и limits. Неподдержанные продолжение, batch и остальные сценарии остаются явно вне проверенного среза. Graph failure не блокирует прямое исследование; этот fallback также проверяется в pilot.

#### Измерение пользы и стоимости

Сравниваются обычный поиск и graph-assisted поиск на сопоставимых условиях. Oracle не подсказывает ответ измеряемому участнику. Повтор одним агентом уже известной задачи учитывает эффект обучения; допустимы равноценные задачи или честно ограниченный trial, отдельные агенты не обязательны.

Техническая корректность и полезность оцениваются раздельно. Для продолжения нужен начальный сравнительный сигнал: предотвращённый material miss относительно baseline либо снижение суммарных затрат без роста material misses/false positives. Один успешный пример не доказывает универсальной эффективности. Если преимущества не обнаружены или результаты неразличимы, одного technical PASS недостаточно для расширения инструмента.

Для решения о дальнейшем внедрении сравниваются минимум локальная правка, изменение общего контракта и добавление consumer. Измеряются пропущенные/ложные существенные связи, время ориентации и source reads, build/review/refresh/rebuild/исправления карты и сопровождения batch, bytes первой и всех страниц, metadata/evidence overhead, peak memory, cold load и warm query. Указываются revision, corpus, hardware, профиль, selectors/budgets, порядок и число повторений. Initial build cost показывается отдельно и входит в итог на заранее объявленном числе задач; произвольная будущая амортизация не доказывает выгоду.

Начальные цели выдачи принадлежат архитектурному контракту; кандидат latency для warm context — median до 1 секунды на зафиксированной локальной машине и объявленном корпусе масштаба прежней карты. Cold load и полное раскрытие измеряются отдельно. Это гипотеза pilot, не измеренная способность. Превышение требует анализа, а не автоматического перехода к БД или многофайловому storage.

#### Решения перед реализацией и поставка

Для выбранного Slice 1 уточняются repository/worktree и write scope, язык/OS/filesystem, вопрос/corpus/oracle, поддержанные patterns, inputs, schema/interface/error contract и resource profile. Optional batch и миграция прежней карты включаются явно либо остаются вне scope. Это не требование проектировать все срезы заранее. Выбор FTR, архитектуры и execution authority сохраняет существующих владельцев.

Поставка будущей реализации: небольшой tool/module в выбранном repo, машиночитаемый schema contract, fixtures/tests, короткая инструкция в существующем owner, один воспроизводимый example graph и report metrics/limitations. Инженерные способы реализации выбираются внутри разрешённого контракта; отдельные approval для каждого обратимого HOW не добавляются. Нужное Evidence хранится по существующему workflow, а большие временные replay artifacts не входят в active graph.

Если выбрана миграция карты AOS-3, importer доказывает full round-trip, включая допустимые неизвестные поля/статусы и semantic records, либо отказывается от неподдержанного переноса. Наблюдение будущего repo с нуля допустимо; оно не разрешает удаление старой карты. Текущий перенос документации не запускает разработку, pilot, миграцию или Git delivery.

## 23. Цепочка готовности

```text
Detailed Feature Passport ≠ accepted feature
Accepted feature ≠ accepted architecture
Accepted architecture ≠ Task Brief
Task Brief ≠ Execution Authorization
Successful implementation ≠ human acceptance
Human acceptance ≠ Git delivery
```
