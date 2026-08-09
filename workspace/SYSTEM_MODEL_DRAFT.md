# SYSTEM_MODEL_DRAFT

## 1. Product goals и boundaries
* **Product Promise** [FOUND: `docs/01_Product.md` - 3. Обещание продукта]: Пользователь формулирует проблему → AOS делает uncertainty видимым → создаёт bounded reviewable cycle → показывает Evidence → человек принимает решение → работа безопасно возобновляется.
* **Product Boundaries** [FOUND: `docs/01_Product.md` - 8. Границы продукта, `docs/00_Core.md` - 11. Product boundary]:
  * **In scope**: Product Runtime, Development Factory, Governance (Minimal Safety Floor), Knowledge/Reference.
  * **Out of scope (non-goals)**: autonomous coding without checkpoints, mandatory multi-agent orchestration, full RAG, autonomous self-heal, automatic Git delivery.

## 2. Actors
* **Непрограммист / domain expert** [FOUND: `docs/01_Product.md` - 4. Пользователи и JTBD]: Описывает проблему, утверждает intent, оценивает результат.
* **Vibe-coder / product builder** [FOUND: `docs/01_Product.md` - 4. Пользователи и JTBD]: Использует агентов без потери scope/state, сохраняет maintainable knowledge.
* **AI coding agent / implementer** [FOUND: `docs/01_Product.md` - 4. Пользователи и JTBD]: Получает bounded context и task, связывает criteria с Evidence.
* **Reviewer / operator / maintainer** [FOUND: `docs/01_Product.md` - 4. Пользователи и JTBD]: Диагностирует drift, понимает actual change и rationale.

## 3. User journeys
* **J-001 — Запуск нового проекта** [FOUND: `docs/01_Product.md` - 9. Основные пользовательские journeys].
* **J-002 — Исследование существующего проекта** [FOUND: `docs/01_Product.md` - 9. Основные пользовательские journeys].
* **J-003 — Реализация одной feature** [FOUND: `docs/01_Product.md` - 9. Основные пользовательские journeys].
* **J-004 — Возобновление работы** [FOUND: `docs/01_Product.md` - 9. Основные пользовательские journeys].
* **J-005 — Проверка и решение** [FOUND: `docs/01_Product.md` - 9. Основные пользовательские journeys].
* **J-006 — Защищённая доставка** [FOUND: `docs/01_Product.md` - 9. Основные пользовательские journeys].
* **J-007 — Reconstruction по reference** [FOUND: `docs/01_Product.md` - 9. Основные пользовательские journeys].

## 4. Runtime flows
* **Documentation Lifecycle** [FOUND: `docs/03_Development.md` - 11. Жизненный цикл документации]: Workspace (Drafts) → Pass 1 (System Design) → Structural Review → Pass 2 (Pipeline + Contracts) → Integration Review → Global Design Freeze → Publish to AOS (Deliverable).
* **Runtime Implementation Stages** [FOUND: `docs/03_Development.md` - 10. Модель стадий Runtime-реализации]: PLAN → EXECUTE → VALIDATE → REVIEW → DELIVER.
* **Reconstruction via feature** [FOUND: `docs/03_Development.md` - 6. Reconstruction через feature]: Feature selection → gap identification → bind read-only legacy → inspect → classify → update dossier.

## 5. Components и ownership
* **Layer 1: Interaction Surface** [FOUND: `docs/02_Architecture.md` - 3. Модель слоёв, 4. Карта компонентов]: Intake, Discovery, Specification Builder, Status/Next/Details, Review Surface, First-Start.
* **Layer 2: Product Runtime** [FOUND: `docs/02_Architecture.md` - 3. Модель слоёв, 4. Карта компонентов]: Feature/Journey Model, Product Feature Registry, Project Memory, Architecture Decision Support, Installer/Updater.
* **Layer 3: Development Factory** [FOUND: `docs/02_Architecture.md` - 3. Модель слоёв, 4. Карта компонентов]: Task Brief Compiler, Preflight/Preview, Scoped Executor, Validation/Evidence, Context Pack Builder, Handoff Builder, Test/CI/Release Helpers.
* **Layer 4: Safety and Control (Governance)** [FOUND: `docs/02_Architecture.md` - 3. Модель слоёв, 4. Карта компонентов]: Authority Resolver, Permission Classifier, Scope/Path Guard, Git Boundary Guard.
* **Layer 5: Knowledge / Reference** [FOUND: `docs/02_Architecture.md` - 3. Модель слоёв, 4. Карта компонентов]: Canonical Documents, Feature Passports, Lessons/Patterns, Reference Findings, Derived Index.
* **Data Ownership** [FOUND: `docs/02_Architecture.md` - 8. Владение данными]:
  * Product requirement → Human-accepted Product artifact
  * Feature behavior → Human-accepted Feature Passport
  * Architecture decision → Human-accepted ADR
  * Task scope → Exact Task Brief
  * Execution permission → Exact Execution Authorization Record
  * Repository state → Instrumental Git/filesystem observation
  * Human decision → Human-authored record
  * Evidence → Immutable subject-bound record

## 6. States и transitions
* **Document maturity** [FOUND: `docs/02_Architecture.md` - 7. Ортогональная модель состояний]: DRAFT | HUMAN_REVIEW_REQUIRED | HUMAN_ACCEPTED | SUPERSEDED.
* **Task stage** [FOUND: `docs/02_Architecture.md` - 7. Ортогональная модель состояний]: PLAN | EXECUTE | VALIDATE | REVIEW.
* **Technical result** [FOUND: `docs/02_Architecture.md` - 7. Ортогональная модель состояний]: CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS.
* **Human decision** [FOUND: `docs/02_Architecture.md` - 7. Ортогональная модель состояний]: ACCEPT | NEEDS_CHANGES | REJECT | DEFER.
* **Permission** [FOUND: `docs/02_Architecture.md` - 7. Ортогональная модель состояний]: ALLOWED | HUMAN_AUTHORIZATION_REQUIRED | BLOCKED_POLICY | BLOCKED_UNKNOWN | NOT_APPLICABLE.
* **Feature disposition** [FOUND: `docs/00_Core.md` - 7. Решение по фиче]: REQUIRED | OPTIONAL | DEFERRED | REFERENCE_ONLY | REJECTED | UNDECIDED.

## 7. Contracts / interfaces
* **Architecture Contracts (WHAT)** [FOUND: `docs/02_Architecture.md` - 6. Общие классы contracts]: C-001 (Intent Record), C-002 (Feature Passport), C-003 (Product Spec), C-004 (Architecture Decision Record).
* **Engineering Contracts (HOW)** [FOUND: `docs/02_Architecture.md` - 6. Общие классы contracts]: C-005 (Task Brief), C-006 (Execution Authorization Record), C-007 (Preflight / Preview), C-008 (Execution Record), C-009 (ValidationEnvelope), C-010 (Evidence Record), C-011 (Human Review / Decision), C-012 (Project Memory / Handoff), C-013 (Install / Update Manifest), C-014 (Git Delivery Record).

## 8. Feature map
* **Feature Inventory (FTR-001..FTR-030)** [FOUND: `docs/06_Features.md` - 4. Индекс каталога]: Каталог из 30 фич. Выделены ключевые для Product Runtime (FTR-001..FTR-006, FTR-008, FTR-012, FTR-014, FTR-016), Development Factory (FTR-007, FTR-009, FTR-010, FTR-011, FTR-013, FTR-015, FTR-023) и Safety/Governance (FTR-019..FTR-021).
* **Selected for X1** [FOUND: `docs/06_Features.md` - 4. Индекс каталога]: FTR-001 (Intake), FTR-003 (Spec/Passport). FTR-005, FTR-006, FTR-011, FTR-012, FTR-013 — SUPPORTING_CONTROL_ONLY. Остальные — UNDECIDED.

## 9. Dependencies
* **Layer Dependencies** [DERIVED: `docs/02_Architecture.md` - 3. Модель слоёв, `docs/01_Product.md` - 15. Жизненный цикл внедрения]: Interaction Surface (L1) зависит от Product Runtime (L2). Product Runtime (L2) запускает Development Factory (L3). Development Factory использует Safety/Control (L4). Вся система опирается на Knowledge Baseline (L5).
* **External Dependencies** [UNKNOWN: `docs/02_Architecture.md` - 16. Необходимые architecture decisions]: language/toolchain/dependencies не выбраны.

## 10. Validation flows
* **Verification Gates** [FOUND: `docs/03_Development.md` - 15. Пять verification gates (для Runtime)]: 1. Structure, 2. Scope, 3. Acceptance, 4. Regression/smoke, 5. Security/release blockers.
* **Validation Protocol** [FOUND: `docs/03_Development.md` - 18. Протокол validation]: Freeze subject → verify provenance → run targeted checks → wider suite if relevant → record commands/results → preserve required/optional → classify limitations → inspect diff → verify no mutation → stop with one next action.

## 11. Failure / recovery flows
* **Failure Model** [FOUND: `docs/02_Architecture.md` - 14. Модель failures и recovery]: Каждый write-capable component определяет failure before write, partial-write detection, transaction/journal, reconciliation, idempotent retry, cancellation, recovery package, rollback.
* **Execution Failure** [FOUND: `docs/03_Development.md` - 20. Recovery и handoff]: Остановка, сохранение state/logs, no auto-retry если failure меняет scope/identity/permissions. Correction выносится в отдельную задачу.

## 12. Cross-document relationships
* **Canonical Structure** [FOUND: `docs/00_Core.md` - 1. Назначение, 5. Иерархия источников]: Иерархия строгая. 00_Core определяет safety и authority, 01_Product задает boundaries, 02_Architecture — layers и contracts.
* **Fact Class Ownership** [DERIVED: `docs/04_Lessons.md` - LES-002, `docs/00_Core.md` - 5. Иерархия источников]: Каждый факт имеет единственного владельца (One fact class — one owner). Ссылки между документами осуществляются на owner'а, предотвращая drift.
* **Reference to Legacy** [FOUND: `docs/05_Reference.md` - 2. Классы источников, 10. Feature-to-reference routing]: Legacy является read-only reference, связанным через exact snapshots. Наличие в reference не дает authority для target AOS.

## 13. UNKNOWN
* **Product Decisions** [UNKNOWN: `docs/01_Product.md` - 14. Необходимые product decisions]: First segment/job/slice, Product Spec↔Feature Passport, Feature Registry, scenario/access/UX timing, interface, acceptance identity, install ownership, metrics.
* **Architecture Decisions** [UNKNOWN: `docs/02_Architecture.md` - 16. Необходимые architecture decisions]: Compatibility relationship, first slice, implementation repo, interface, Project Memory persistence, Runtime/Factory boundary, Governance packaging, language/toolchain/dependencies.

## 14. CONFLICT
CONFLICT: NONE

## 15. NOT_FOUND
* **Architecture Implementation Specifics (HOW)** [NOT_FOUND: `docs/00_Core.md` - 12. Уровни проектирования документации]: Детали реализации (Engineering Design) принципиально отсутствуют в пакете.

## 16. BLOCKED
BLOCKED: NONE
