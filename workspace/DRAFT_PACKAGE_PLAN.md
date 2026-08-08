# Draft Package Plan (Phase 2A)

## 1. Общая структура пакета
Пакет `Pass 2 (Pipeline + Contracts)` будет состоять из трёх укрупнённых документов, каждый из которых имеет строго одного владельца и описывает независимый класс фактов (Product, Architecture, Engineering). Это исключает искусственное дробление и дублирование, обеспечивая полное покрытие System Model.

## 2. Перечень будущих документов, Owners и Fact Classes

### 2.1. `DRAFT_01_PRODUCT_MODEL.md`
* **Рабочее название**: Product Model & Feature Scope
* **Назначение**: Определение продуктовых границ, целевых пользователей, их путей и карты фич (Product Runtime scope).
* **Owner**: Product Owner
* **Fact class**: `PRODUCT_REQUIREMENTS`
* **Основные разделы**: Product Goals & Boundaries, Actors, User Journeys, Feature Map, Product Open Decisions.
* **Источник информации (System Model)**:
  * 1. Product goals и boundaries
  * 2. Actors
  * 3. User journeys
  * 8. Feature map
  * 13. UNKNOWN (Product Decisions)
* **Зависимости**: Нет.
* **Ссылается на**: Нет.

### 2.2. `DRAFT_02_ARCHITECTURE_CONTRACTS.md`
* **Рабочее название**: Architecture & State Contracts
* **Назначение**: Описание архитектурных слоёв, компонентов, состояний, структурных зависимостей и архитектурных контрактов (WHAT).
* **Owner**: System Architect
* **Fact class**: `ARCHITECTURE_CONTRACTS`
* **Основные разделы**: Components & Ownership, States & Transitions, Architecture Contracts, Dependencies, Cross-Document Relationships, Architecture Open Decisions, Baseline Absences.
* **Источник информации (System Model)**:
  * 5. Components и ownership
  * 6. States и transitions
  * 7. Contracts / interfaces (Architecture Contracts: C-001..C-004)
  * 9. Dependencies
  * 12. Cross-document relationships
  * 13. UNKNOWN (Architecture Decisions)
  * 14. CONFLICT
  * 15. NOT_FOUND
  * 16. BLOCKED
* **Зависимости**: `DRAFT_01_PRODUCT_MODEL.md`.
* **Ссылается на**: `DRAFT_01_PRODUCT_MODEL.md` (реализует заявленные продуктовые фичи).

### 2.3. `DRAFT_03_ENGINEERING_PIPELINE.md`
* **Рабочее название**: Engineering Pipeline & Execution Flows
* **Назначение**: Описание процессов выполнения (Development Factory), инженерных контрактов (HOW), процессов валидации и восстановления после сбоев.
* **Owner**: Engineering Lead
* **Fact class**: `ENGINEERING_WORKFLOW`
* **Основные разделы**: Runtime Flows, Engineering Contracts, Validation Flows, Failure & Recovery Flows.
* **Источник информации (System Model)**:
  * 4. Runtime flows
  * 7. Contracts / interfaces (Engineering Contracts: C-005..C-014)
  * 10. Validation flows
  * 11. Failure / recovery flows
* **Зависимости**: `DRAFT_02_ARCHITECTURE_CONTRACTS.md`.
* **Ссылается на**: `DRAFT_02_ARCHITECTURE_CONTRACTS.md` (использует архитектурные компоненты и состояния).

## 3. Dependency Graph
```text
DRAFT_01_PRODUCT_MODEL.md
└── DRAFT_02_ARCHITECTURE_CONTRACTS.md
    └── DRAFT_03_ENGINEERING_PIPELINE.md
```
Граф зависимостей линеен, циклические зависимости отсутствуют.

## 4. Generation Order
1. **DRAFT_01_PRODUCT_MODEL.md** (Определяет границы и продуктовую ценность).
2. **DRAFT_02_ARCHITECTURE_CONTRACTS.md** (Определяет компоненты, состояния и архитектурные контракты).
3. **DRAFT_03_ENGINEERING_PIPELINE.md** (Определяет конвейер исполнения и инженерные контракты).

## 5. Preserved UNKNOWN
Следующие неизвестные элементы сохраняются в открытом виде для передачи в Phase 2B:
* **Product Decisions**: First segment/job/slice, Product Spec↔Feature Passport, Feature Registry, scenario/access/UX timing, interface, acceptance identity, install ownership, metrics. (Сохраняются в `DRAFT_01_PRODUCT_MODEL.md`).
* **Architecture Decisions**: Compatibility relationship, first slice, implementation repo, interface, Project Memory persistence, Runtime/Factory boundary, Governance packaging, language/toolchain/dependencies. (Сохраняются в `DRAFT_02_ARCHITECTURE_CONTRACTS.md`).

## 6. Phase 2B Readiness
**READY_WITH_KNOWN_UNKNOWNS**
Структура пакета полностью определена, каждый раздел System Model имеет владельца, зависимости ацикличны. Сохранённые UNKNOWN являются ожидаемыми и подлежат уточнению на этапе реализации или более детального проектирования, что делает возможным безопасный старт генерации черновиков.
