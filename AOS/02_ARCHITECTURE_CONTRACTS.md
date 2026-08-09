# 02 — Architecture & State Contracts

## UPSTREAM_ALIGNMENT
* **Aligned claims:** Интерактивная поверхность (Interaction Surface) и продуктовый Runtime разделены (L1/L2), что соответствует Intake, Discovery и Review из Product Model. Boundaries Product Model (WHAT) не пересекаются с деталями реализации.
* **Product-only claims:** Сценарии J-001..J-007, детали ролей акторов (JTBD) и метрики остаются в Product Model и не дублируются как архитектурные компоненты.
* **UPSTREAM_MISMATCH:** NONE.

## 1. Layers L1–L5
* **Layer 1: Interaction Surface**
  * **Purpose:** Отображать состояние системы (state) и доказательства (Evidence).
  * **Responsibility:** Обеспечение взаимодействия (CLI, chat, local UI).
  * **Forbidden responsibilities:** Не является независимым Source of Truth; не превращает действие (click) в явное разрешение (approval) без создания decision record.
* **Layer 2: Product Runtime**
  * **Responsibility:** Обработка Intent, Discovery, Specification, Feature Passport, Status/Next/Details, Review, Project Memory.
* **Layer 3: Development Factory**
  * **Responsibility:** Task Brief compiler, preflight/preview, scoped executor, validation/evidence, Context Pack builder, CI/release helpers.
* **Layer 4: Safety and Control (Governance)**
  * **Purpose:** Обеспечение безопасности (Minimal Safety Floor).
  * **Responsibility:** Authority checks, permission states, scope/path/Git boundaries, result semantics, stop rules.
* **Layer 5: Knowledge / Reference**
  * **Responsibility:** Хранение Accepted documents, DRAFT Feature Passports, lessons, targeted findings, patterns, derived indexes.

*(Примечание: Layer 6 — Optional Extensions (plugins, RAG, и т.д.) не является обязательным ядром).*

## 2. Components
Архитектурный Baseline содержит карту компонентов-кандидатов (INFERENCE), сгруппированных по слоям:
* **L1:** Intake, Discovery, Specification Builder, Status/Next/Details, Review Surface, First-Start.
* **L2:** Feature/Journey Model, Product Feature Registry, Project Memory, Architecture Decision Support, Installer/Updater.
* **L3:** Task Brief Compiler, Preflight/Preview, Scoped Executor, Validation/Evidence, Context Pack Builder, Handoff Builder, Test/CI/Release Helpers.
* **L4:** Authority Resolver, Permission Classifier, Scope/Path Guard, Git Boundary Guard.
* **L5:** Canonical Documents, Feature Passports, Lessons/Patterns, Reference Findings, Derived Index.

**Semantic inputs, outputs, precise dependencies and precise component responsibilities:** `[NOT_SPECIFIED_AT_THIS_LEVEL]` (Базлайн не устанавливает их жёстко на уровне компонентов, только на уровне контрактов).

## 3. Ownership (Data Ownership)
Владение данными строго разделено по классам фактов (Fact classes). Реестры и индексы не владеют данными.
* **Human-accepted Product artifact** → Владеет Product requirement.
* **Human-accepted Feature Passport** → Владеет Feature behavior.
* **Human-accepted ADR** → Владеет Architecture decision.
* **Exact Task Brief** → Владеет Task scope.
* **Exact Execution Authorization Record** → Владеет Execution permission.
* **Instrumental Git/filesystem observation** → Владеет Repository state.
* **Human-authored/verified record** → Владеет Human decision.
* **Immutable subject-bound record** → Владеет Evidence.
* **Derived view** → Владеет Dashboard/status (Не создаёт authority).
* **Rebuildable derived data** → Владеет Registry/RAG/cache (Не создаёт authority).
* **Reference record** → Владеет Legacy finding (Не имеет authority для target AOS).

## 4. Orthogonal State Model
Оси состояний ортогональны (не изменяют друг друга автоматически). Точные переходы (transitions) между ними `[NOT_SPECIFIED_AT_THIS_LEVEL]`.
* **Document maturity:** DRAFT | HUMAN_REVIEW_REQUIRED | HUMAN_ACCEPTED | SUPERSEDED.
* **Task stage:** PLAN | EXECUTE | VALIDATE | REVIEW.
* **Technical result:** CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS.
* **Human decision:** ACCEPT | NEEDS_CHANGES | REJECT | DEFER.
* **Permission:** ALLOWED | HUMAN_AUTHORIZATION_REQUIRED | BLOCKED_POLICY | BLOCKED_UNKNOWN | NOT_APPLICABLE.

*(Примечание: Порядок статусов в перечислении не является графом переходов. Любые transition rules не выводятся без явного доказательства).*

## 5. Architecture Contracts C-001..C-004 (WHAT)
Определяют абстракции уровня проектирования (WHAT). Не требуют Execution Authorization.
* **C-001: Intent Record**
  * **Purpose:** Фиксация исходного намерения.
  * **Semantic content:** actor, original_request, problem, desired_outcome, context, constraints, non_goals, assumptions, unknowns, sensitive_domain_flags, source.
  * **Producer/Consumer/Relationships:** `[NOT_SPECIFIED_AT_THIS_LEVEL]`.
* **C-002: Feature Passport / Feature Contract**
  * **Purpose:** Формализация ожидаемого поведения функциональности.
  * **Semantic content:** feature_id, purpose, users, trigger, preconditions, inputs, outputs, main_flow, states, transitions, failures, recovery, dependencies, constraints, authority_boundaries, acceptance_criteria, negative_scenarios, maturity, evidence_status, human_disposition.
  * **Producer/Consumer/Relationships:** `[NOT_SPECIFIED_AT_THIS_LEVEL]`.
* **C-003: Product Spec**
  * **Purpose:** Определение продуктовых границ и метрик (problem, users, journeys, scope, non-goals, constraints, etc.). Не разрешает execution.
  * **Producer/Consumer/Relationships:** `[NOT_SPECIFIED_AT_THIS_LEVEL]`.
* **C-004: Architecture Decision Record**
  * **Purpose:** Фиксация принятого архитектурного решения.
  * **Semantic content:** question, context, constraints, options, tradeoffs, evidence, selected_option, human_decision_identity, consequences, reversal_conditions.
  * **Producer/Consumer/Relationships:** `[NOT_SPECIFIED_AT_THIS_LEVEL]`.

## 6. Dependencies & Traceability
* **Layer & Component Dependencies:** `[NOT_SPECIFIED_AT_THIS_LEVEL]` (Baseline явно не фиксирует стрелки зависимостей между слоями, кроме косвенных абстракций).
* **Traceability:** Product semantics (ожидания пользователя) отражаются в Architecture Contracts (C-001, C-003), которые далее используются Engineering Factory (уровень DRAFT_03). Точный маппинг `[NOT_SPECIFIED_AT_THIS_LEVEL]`.

## 7. Architecture UNKNOWN (Preserved)
Следующие архитектурные решения остаются неизвестными (UNKNOWN) и подлежат принятию человеком (ADR):
* Compatibility relationship
* First target slice
* Implementation repository
* Exact Interface
* Project Memory persistence
* Runtime / Development Factory boundary (точные границы)
* Governance packaging
* Language/toolchain/dependencies
* Exact engineering schemas/I-O (остаются HOW-деталями)

## 8. Baseline Gaps
* **NOT_FOUND:** Architecture Implementation Specifics (HOW). Детали реализации принципиально отсутствуют в базовом пакете.
* **CONFLICT:** NONE
* **BLOCKED:** NONE
