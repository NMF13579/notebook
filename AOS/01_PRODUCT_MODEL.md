# 01 — Product Model & Feature Scope

## 1. Product Goals
* **Product Problem:** Непрограммист может описать желаемый результат, но не способен надёжно контролировать каждую repository operation, permission, test и implementation detail. AI-агенты могут потерять product intent, расширить scope, завысить completion или создать maintenance debt.
* **Product Promise:** Пользователь формулирует проблему или идею → AOS делает понимание и uncertainty видимыми → создаёт bounded, reviewable development cycle → показывает Evidence и remaining risk → человек принимает решение → работа безопасно возобновляется.
* **Value:** Снижение стоимости и непредсказуемости AI-разработки через визуализацию неопределенности, проверяемость результатов (Evidence) и строгие точки принятия решений (Human Checkpoints).

## 2. Product Boundaries
* **Product Runtime (In scope):** Intent/Problem Intake, Discovery, Product Spec/Feature Passport, Status/Next/Details, Review Package, Project Memory/Handoff, First-Start/Tutor и optional Architecture Support/Guided Bootstrap.
* **Development Factory (In scope):** Task Brief compiler, preflight/preview, execution adapters, validators/test harness, Context Packs, backlog/decomposition, CI/release helpers, strict loaders/drift checks.
* **Governance (In scope):** Minimal Safety Floor всегда; stronger controls только после observed need.
* **Out of scope (non-goals):** Автономное "решение" проекта без контрольных точек, обязательная мультиагентная оркестрация, скрытое автоматическое исправление (self-heal), автоматическая доставка (Commit, Push, Merge, Release), платформа хостинга (SaaS-сервис).
* **WHAT / HOW boundary:** Документация описывает абстракции и правила (WHAT). Инженерная реализация (HOW) вынесена в код и не смешивается с дизайном.

## 3. Actors
* **Непрограммист / domain expert:**
  * **Role / JTBD:** Описать проблему обычным языком, увидеть понятое/упущенное, утвердить intent и high-risk actions, resume after interruption.
  * **Responsibilities:** Принимать окончательные решения (Accept/Reject), оценивать user-visible result без чтения всего кода.
  * **Boundaries:** Эксклюзивное право принятия решений об изменении состояния системы, утверждении намерений и архитектуры (The Commander).
  * **Interactions:** Интервью с Intake Engine, Review Surface.
* **Vibe-coder / product builder:**
  * **Role / JTBD:** Получить safe default workflow, предотвращать scope drift и false completion, менять coding agents без переписывания правил.
  * **Responsibilities:** Использование агентов без потери scope/state, сохранение maintainable knowledge.
  * **Boundaries:** Действует в рамках The Commander, управляет пайплайном, но полагается на систему для защиты.
* **AI coding agent / implementer:**
  * **Role / JTBD:** Получить bounded context и one task, знать allowed/forbidden changes, сообщить uncertainty/remaining risk.
  * **Responsibilities:** Оставить recoverable handoff, связать acceptance criteria с Evidence.
  * **Boundaries:** Действует в строгих рамках Task Brief (песочница). Не может изменять Scope, утверждать результаты (simulated approval) или менять Knowledge Baseline без отдельной задачи.
* **Reviewer / operator / maintainer:**
  * **Role / JTBD:** Inspect current state/drift, reproduce checks, отличать historical report от current result.
  * **Responsibilities:** Диагностировать drift, понимать ownership/rationale, обеспечивать долгосрочное здоровье проекта.
  * **Boundaries:** The Auditor, не инициирует изменения, а анализирует и формирует новые правила (Lessons).

## 4. User Journeys
* **J-001 — Запуск нового проекта**
  * **Actor:** Непрограммист / Vibe-coder
  * **Trigger:** Пользователь формулирует проблему (Intent).
  * **Intent:** Описать проблему, получить понятый план и запустить первую безопасную итерацию.
  * **Product-level conceptual steps:** Пользователь описывает проблему (intent) → AOS проясняет неизвестные и формирует Product Spec → Пользователь выбирает первый шаг (slice choice) и принимает архитектурные решения при необходимости → Формируется строгая граница задачи (Task Brief), и пользователь даёт явное разрешение (authorization) → Система выполняет работу, собирает доказательства (validation) и предоставляет их на проверку (review) → Пользователь принимает окончательное решение.
  * **Expected product outcome:** Первичное решение человека по результатам первой итерации.
  * **Human checkpoint:** Явное разрешение (authorization) перед началом работы, финальное решение (human decision).
  * **User-visible uncertainty/failure boundary:** Ошибка понимания контекста (Intake) приводит к остановке и уточнению до запуска любой работы.
  * **Related Feature:** FTR-001, FTR-003.
* **J-002 — Исследование существующего проекта**
  * **Actor:** Reviewer / Vibe-coder
  * **Trigger:** Подключение AOS к существующему репозиторию.
  * **Intent:** Безопасно понять текущее состояние, возможности и проблемы проекта без его изменения.
  * **Product-level conceptual steps:** AOS подключается в режиме read-only (identity/preflight) → Строит карту текущих возможностей проекта (capability map) → Обнаруживает пробелы и конфликты с Baseline → Предлагает пользователю безопасные цели для работы (candidate objectives) → Пользователь выбирает цель (human selection).
  * **Expected product outcome:** Понятная картина проекта и выбранная пользователем цель для дальнейшей работы.
  * **Human checkpoint:** Выбор цели (human selection).
  * **User-visible uncertainty/failure boundary:** [NOT_SPECIFIED_AT_THIS_LEVEL]
  * **Related Feature:** FTR-002.
* **J-003 — Реализация одной feature**
  * **Actor:** Agent / implementer / Commander (основной процесс принятия решений)
  * **Trigger:** Наличие Feature Passport.
  * **Intent:** Безопасно реализовать изолированную функциональность на основе согласованного паспорта.
  * **Product-level conceptual steps:** Фича исследуется в контексте проекта (targeted research) → Формируется продуктовый контракт и архитектура → Границы выполнения фиксируются в Task Brief → Происходит защищённое выполнение с отчётом (Stage Report) → Результат и доказательства передаются пользователю (REVIEW) → Пользователь принимает решение (decision).
  * **Expected product outcome:** Решение пользователя на основе предоставленных доказательств (Evidence).
  * **Human checkpoint:** Окончательное решение пользователя (decision).
  * **User-visible uncertainty/failure boundary:** [NOT_SPECIFIED_AT_THIS_LEVEL]
  * **Related Feature:** [UNKNOWN]
* **J-004 — Возобновление работы**
  * **Actor:** Любой человек.
  * **Trigger:** Возвращение пользователя к проекту (команда /status).
  * **Intent:** Понять, где остановилась работа, и безопасно её продолжить.
  * **Product-level conceptual steps:** Запрос статуса → AOS определяет точное состояние проекта на основе репозитория (repository-derived state) → Пользователь видит блокировки и ожидающие решения (blockers/decisions) → Пользователю предлагается следующее безопасное действие (/next).
  * **Expected product outcome:** Понятное следующее действие для продолжения работы.
  * **Human checkpoint:** Разрешение обнаруженных блокировок (blockers/decisions).
  * **User-visible uncertainty/failure boundary:** [NOT_SPECIFIED_AT_THIS_LEVEL]
* **J-005 — Проверка и решение**
  * **Actor:** Непрограммист / The Commander.
  * **Trigger:** Окончание работы (завершенный REVIEW), готовность Evidence.
  * **Intent:** Оценить результат работы и принять решение без необходимости читать весь код.
  * **Product-level conceptual steps:** Пользователь видит состояние "до/после" и изменённый scope → Изучает собранные доказательства (Evidence) и ограничения (limitations/NOT_RUN) → На основе находок принимает одно из решений: ACCEPT, NEEDS_CHANGES, REJECT или DEFER.
  * **Expected product outcome:** Явный вердикт человека.
  * **Human checkpoint:** Само решение (ACCEPT | NEEDS_CHANGES | REJECT | DEFER).
  * **User-visible uncertainty/failure boundary:** Остановка при отсутствии или подделке Evidence.
* **J-006 — Защищённая доставка**
  * **Actor:** The Commander.
  * **Trigger:** Готовность защищённого (protected) scope к публикации.
  * **Intent:** Безопасно опубликовать изменения без случайных слияний или потери контроля.
  * **Product-level conceptual steps:** Определяется защищённый план доставки → Пользователь формирует профиль риска (Risk Profile) → Авторизует выполнение (authorized EXECUTE) → Изменения независимо проверяются и 리뷰ются → Выполняются отдельные, контролируемые человеком шаги доставки (Commit ≠ Push ≠ Merge ≠ Release; каждое критическое действие требует отдельной границы решения/разрешения).
  * **Expected product outcome:** Безопасная доставка кода в целевое окружение.
  * **Human checkpoint:** Отдельное разрешение на каждый этап доставки (Commit, Push, Merge, Release).
  * **User-visible uncertainty/failure boundary:** Откат до безопасного состояния при любой ошибке.
* **J-007 — Reconstruction по reference**
  * **Actor:** Domain expert / Vibe-coder.
  * **Trigger:** Обнаружение архитектурного или функционального пробела (feature gap).
  * **Intent:** Изучить legacy-код (reference) без автоматического копирования его устаревшей сложности.
  * **Product-level conceptual steps:** Формируется узкий запрос (narrow question) → Изучается зафиксированный снимок legacy (pinned snapshot) → Доказательства классифицируются → Устаревшая сложность отклоняется (reject legacy complexity) → Обновляется досье новой фичи → Человек принимает решение об использовании.
  * **Expected product outcome:** Обновлённое досье фичи и решение о применении знаний.
  * **Human checkpoint:** Окончательное решение человека о принятии найденного знания.
  * **User-visible uncertainty/failure boundary:** [NOT_SPECIFIED_AT_THIS_LEVEL]

## 5. Feature Map & Traceability
* **Роль Feature Inventory:** Принятый единый inventory известных фич (30 штук) и каталог design-level dossiers. Принятие inventory не является item-level feature selection. Наличие в каталоге ≠ приоритет roadmap ≠ принятая архитектура ≠ разрешение на реализацию. (Inventory ≠ roadmap).
* **Selected Features (X1):** FTR-001 (Intake), FTR-003 (Spec/Passport).
* **Supporting-control Features:** FTR-005, FTR-006, FTR-011, FTR-012, FTR-013.
* **Undecided Features:** Остальные (FTR-002, FTR-004, FTR-007 и т.д.).
* **Feature Disposition:** Решение человека по фиче принимает одно из значений: SELECT_FOR_X1 | SUPPORTING_CONTROL_ONLY | REQUIRED | OPTIONAL | DEFERRED | REFERENCE_ONLY | REJECTED | UNDECIDED.
* **Traceability (Actor → Journey → Feature):**
  * Domain expert → J-001 → FTR-001 (Intake), FTR-003 (Spec/Passport).
  * Reviewer/Coder → J-002 → FTR-002.
  * [UNKNOWN] Точный и полный маппинг всех J-001..J-007 на FTR-001..FTR-030 не доказан явно в Baseline.

## 6. Product UNKNOWN (Preserved)
Следующие продуктовые решения остаются неизвестными (UNKNOWN) и подлежат явному принятию решения человеком:
* First segment/job/slice
* Точный маппинг Journey ↔ Feature
* Связь Product Spec ↔ Feature Passport
* Реализация Feature Registry
* Scenario/access/UX timing
* Точный Interface
* Acceptance identity
* Install ownership
* Metrics
