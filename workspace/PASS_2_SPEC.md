# Спецификация Pass 2 (Architecture Contracts & Pipeline)

> **Status: SUPERSEDED.** Retained as a historical working specification for the prior two-document Pass 2. It is not an active process contract or lifecycle owner. The current lifecycle and Pass 2 outputs are owned only by `docs/03_Development.md`.

## 1. Scope Pass 2

Pass 2 разделен на две последовательные фазы:
*   **Phase 2A (Pipeline):** Отвечает исключительно за абстрактный поток исполнения и жизненный цикл задач. Результат — `02_PIPELINE.md`.
*   **Phase 2B (Architecture Contracts):** Отвечает исключительно за определение абстрактных гарантий, полномочий и свойств состояния системы. Результат — `03_SYSTEM_CONTRACTS.md`.

*Что сознательно не входит в Pass 2:*
*   Инженерный дизайн (Engineering Design).
*   Точные схемы данных (I/O схемы, JSON/YAML структуры).
*   Внутреннее представление состояния, API-методы.
*   Алгоритмы, псевдокод, структуры баз данных.

## 2. Phase 2A: Pipeline (`02_PIPELINE.md`)

*Назначение:* Создание абстрактного пайплайна системы без пересечения с архитектурными контрактами.
*Структура Phase 2A:*

1.  **Pipeline Stages:** Абстрактные этапы обработки.
2.  **Actors:** Матрица ответственности для каждой стадии.
3.  **Consumes:** Абстрактные предусловия, которые стадия требует для старта.
4.  **Produces:** Абстрактный результат завершения стадии.
5.  **Failure Boundaries:** Концептуальные границы, за которые не выходит ошибка (fail-closed).
6.  **Recovery:** Стратегия возврата к стабильному состоянию.
7.  **Human Checkpoints:** Обязательные точки остановки для получения решения человека.
8.  **Handoff:** Абстрактная логика передачи управления между стадиями.

*Порядок построения Phase 2A:* Pipeline Stages → Actors → Consumes → Produces → Failure Boundaries → Recovery → Human Checkpoints → Handoff.

## 3. Phase 2B: Architecture Contracts (`03_SYSTEM_CONTRACTS.md`)

*Назначение:* Создание архитектурных контрактов взаимодействия, абстрагированных от конкретных этапов пайплайна.
*Структура Phase 2B:*

1.  **Intent Contract:** Гарантии, что намерение обеспечено четкими целями и границами.
2.  **Authority Contract:** Кто имеет право инициировать действие или изменять скоуп.
3.  **Evidence Contract:** Требования к неизменяемости и полноте предоставляемых доказательств.
4.  **Human Decision Contract:** Требования к явной фиксации решения человека.
5.  **Ownership:** Кто владеет состоянием на концептуальном уровне.
6.  **State:** Абстрактные состояния объектов (без инженерных структур).
7.  **Cross-cutting Invariants:** Сквозные правила (например, Radical Transparency), применяемые поверх пайплайна.

*Правило строгого разграничения:* В `02_PIPELINE.md` нет описания гарантий и контрактов, а в `03_SYSTEM_CONTRACTS.md` нет описания потока исполнения.

## 4. Источники информации

Разделы строятся на основе:
*   `workspace/01_SYSTEM_DESIGN.md`: Основной источник для Stages, Actors, Concept Flows.
*   `docs/00_Core.md`: Minimal Safety Floor (для Human Checkpoints, Authority Contract).
*   `docs/02_Architecture.md`: Концепции контрактов (для Phase 2B).
*   `docs/04_Lessons.md`: Ошибки из прошлого (для Recovery, Failure Boundaries).

## 5. Integration Review

После завершения Phase 2A и Phase 2B проверяется:
*   **Alignment с Pass 1:** Не нарушают ли документы концепции из `01_SYSTEM_DESIGN.md`.
*   **Separation of Concerns:** Не дублируется ли пайплайн в контрактах и наоборот.
*   **WHAT / HOW Boundary:** Отсутствие Engineering Design (API, схемы БД, JSON).
*   **Governance Check:** Наличие Human Checkpoints перед деструктивными действиями.
*   *Цель ревью:* Убедиться, что система готова к Global Design Freeze.

## 6. Exit Criteria

Pass 2 считается полностью завершенным только если:
*   Завершена Phase 2A (сформирован `02_PIPELINE.md`).
*   Завершена Phase 2B (сформирован `03_SYSTEM_CONTRACTS.md`).
*   Integration Review проведено со статусом PASS (без Critical Findings).
*   Пакет полностью готов к стадии Global Design Freeze.

## 7. Deliverables

*   `02_PIPELINE.md` (Фаза 2A)
*   `03_SYSTEM_CONTRACTS.md` (Фаза 2B)
*   `Integration Review Report`
*   `Global Design Freeze Candidate Package`

## 8. Handoff (Порядок передачи ответственности)

*   **После Phase 2A** → сформированный пайплайн передаётся **в Phase 2B** (для наложения абстрактных контрактов поверх готового потока).
*   **После Phase 2B** → объединённый дизайн (Concept + Pipeline + Contracts) передаётся **в Global Design Freeze** (для архитектурной заморозки).
*   **После Global Design Freeze** → пакет передаётся **Implementation-процессу** (кодинг-агентам) для инженерной реализации (HOW).

## 9. Documentation Lifecycle

Этот раздел иллюстрирует полный жизненный цикл проектирования и реализации — от исходной базы знаний до написания кода. Процесс является строго последовательным (отсутствуют циклы). Каждый этап получает понятный вход и завершается формированием конкретного артефакта, который становится входом для единственного следующего этапа.

**1. Knowledge Baseline**
*   **Purpose:** Установить базовую истину проекта.
*   **Input:** Исходные намерения и инфраструктура.
*   **Output:** База знаний (`docs/00..06.md`).
*   **Next Stage:** PASS_1_SPEC

**2. PASS_1_SPEC**
*   **Purpose:** Определить правила концептуального проектирования.
*   **Input:** Knowledge Baseline.
*   **Output:** Спецификация процесса Pass 1.
*   **Next Stage:** 01_SYSTEM_DESIGN

**3. 01_SYSTEM_DESIGN**
*   **Purpose:** Сформировать самостоятельную Concept-модель системы (WHAT).
*   **Input:** Knowledge Baseline + PASS_1_SPEC.
*   **Output:** Черновик `01_SYSTEM_DESIGN.md` (в `workspace/`).
*   **Next Stage:** Structural Review

**4. Structural Review**
*   **Purpose:** Проверить концепцию на отсутствие Engineering Design.
*   **Input:** `01_SYSTEM_DESIGN.md`.
*   **Output:** Structural Review Report (PASS/FAIL).
*   **Next Stage:** PASS_2_SPEC

**5. PASS_2_SPEC**
*   **Purpose:** Определить правила архитектурного проектирования.
*   **Input:** Одобренный `01_SYSTEM_DESIGN.md`.
*   **Output:** Спецификация процесса Pass 2 (Фазы 2A и 2B).
*   **Next Stage:** Phase 2A

**6. Phase 2A (Pipeline Design)**
*   **Purpose:** Спроектировать абстрактный поток данных и точки контроля.
*   **Input:** `01_SYSTEM_DESIGN.md` + PASS_2_SPEC.
*   **Output:** `02_PIPELINE.md`.
*   **Next Stage:** Phase 2B

**7. Phase 2B (Architecture Contracts Design)**
*   **Purpose:** Наложить абстрактные контракты и полномочия поверх пайплайна.
*   **Input:** `02_PIPELINE.md` + PASS_2_SPEC.
*   **Output:** `03_SYSTEM_CONTRACTS.md`.
*   **Next Stage:** Integration Review

**8. Integration Review**
*   **Purpose:** Удостовериться в строгом разделении пайплайна и контрактов.
*   **Input:** `01_SYSTEM_DESIGN.md` + `02_PIPELINE.md` + `03_SYSTEM_CONTRACTS.md`.
*   **Output:** Integration Review Report (PASS/FAIL).
*   **Next Stage:** Global Design Freeze

**9. Global Design Freeze**
*   **Purpose:** Заморозить архитектурный дизайн, предотвращая scope creep.
*   **Input:** Успешный Integration Review Report.
*   **Output:** Global Design Freeze Candidate Package.
*   **Next Stage:** Publish to AOS

**10. Publish to AOS**
*   **Purpose:** Перенести утвержденный дизайн в пакет доставки для агентов реализации.
*   **Input:** Замороженный дизайн из `workspace/`.
*   **Output:** Официальный пакет `AOS/` (Deliverable).
*   **Next Stage:** Implementation Roadmap

**11. Implementation Roadmap**
*   **Purpose:** Спланировать последовательность инженерной реализации.
*   **Input:** Пакет `AOS/`.
*   **Output:** Стратегический план внедрения (Roadmap).
*   **Next Stage:** Slice Selection

**12. Slice Selection**
*   **Purpose:** Выбрать одну вертикальную часть системы для ближайшей реализации.
*   **Input:** Implementation Roadmap.
*   **Output:** Выбранный изолированный Slice.
*   **Next Stage:** Task Preparation

**13. Task Preparation**
*   **Purpose:** Детализировать Slice в точный, ограниченный контракт на разработку.
*   **Input:** Выбранный Slice.
*   **Output:** Утвержденный Task Brief.
*   **Next Stage:** Implementation

**14. Implementation**
*   **Purpose:** Безопасная инженерная реализация, написание кода и сбор доказательств (HOW).
*   **Input:** Утвержденный Task Brief.
*   **Output:** Изолированный, проверенный программный код (Evidence).
*   **Next Stage:** End (переход к следующему Slice).
