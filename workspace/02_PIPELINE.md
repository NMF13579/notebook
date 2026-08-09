# 02 — Documentation Pipeline

> **Status: SUPERSEDED_WORKING_ARTIFACT.** Retained for historical provenance only. It is not a second canonical Documentation Pipeline; `docs/03_Development.md` is the sole active lifecycle owner. This file is not the removed legacy Runtime Pipeline and must not be published as `AOS/02_PIPELINE.md`.

## 1. Назначение пайплайна

Настоящий документ описывает **исключительно пайплайн проектирования и создания документации AOS**.
Он не описывает, как работает программный runtime AOS или как агенты пишут код. Документ регламентирует строгую последовательность шагов, через которую проходят знания — от первоначальной базы (Knowledge Baseline) до формирования контрактов на реализацию (Task Brief).

---

## 2. Pipeline Stages

### 2.1. Knowledge Baseline
*   **Purpose:** Установить базовую истину проекта, бизнес-намерения и инвентарь существующих фичей.
*   **Input:** Неструктурированные намерения, исследования, продукт-метрики.
*   **Output:** Пакет базовых знаний (`docs/00_Core.md` – `docs/06_Features.md`).
*   **Owner:** Domain Expert.
*   **Entry Criteria:** Наличие потребности в новой системе или крупном модуле.
*   **Exit Criteria:** База знаний зафиксирована, фичи занесены в Inventory.
*   **Next Stage:** System Design.

### 2.2. System Design
*   **Purpose:** Сформировать абстрактную Concept-модель системы (WHAT), определив её границы и высокоуровневые потоки.
*   **Input:** Knowledge Baseline, правила `PASS_1_SPEC.md`.
*   **Output:** Черновик `workspace/01_SYSTEM_DESIGN.md`.
*   **Owner:** Documentation Agent.
*   **Entry Criteria:** Knowledge Baseline доступна и не содержит внутренних конфликтов.
*   **Exit Criteria:** Документ полностью абстрагирован от кода и технических деталей реализации.
*   **Next Stage:** Pipeline.

### 2.3. Pipeline
*   **Purpose:** Определить этапы обработки, абстрактный поток данных и точки контроля внутри системы (Architecture Pipeline).
*   **Input:** `01_SYSTEM_DESIGN.md`, правила Phase 2A.
*   **Output:** Черновик `workspace/02_PIPELINE.md`.
*   **Owner:** Documentation Agent.
*   **Entry Criteria:** Concept-модель признана успешной и целостной.
*   **Exit Criteria:** Описан поток данных, но строго без архитектурных контрактов и полномочий.
*   **Next Stage:** Architecture Contracts.

### 2.4. Architecture Contracts
*   **Purpose:** Наложить на пайплайн гарантии, полномочия и инварианты сохранения состояния.
*   **Input:** `02_PIPELINE.md`, правила Phase 2B.
*   **Output:** Черновик `workspace/03_SYSTEM_CONTRACTS.md`.
*   **Owner:** Documentation Agent.
*   **Entry Criteria:** Абстрактный поток (Pipeline) полностью сформирован.
*   **Exit Criteria:** Контракты определены без перехода к Engineering Design (API, схемы БД).
*   **Next Stage:** Integration Review.

### 2.5. Integration Review
*   **Purpose:** Проверить весь созданный дизайн на целостность, отсутствие дублирования и строгое соблюдение границы WHAT/HOW.
*   **Input:** `01_SYSTEM_DESIGN.md`, `02_PIPELINE.md`, `03_SYSTEM_CONTRACTS.md`.
*   **Output:** Отчет о проверке (Integration Review Report).
*   **Owner:** Human Reviewer.
*   **Entry Criteria:** Все черновики документации Pass 1 и Pass 2 готовы.
*   **Exit Criteria:** Вынесен финальный вердикт PASS (отсутствие критических замечаний).
*   **Next Stage:** Global Design Freeze.

### 2.6. Global Design Freeze
*   **Purpose:** Заморозить дизайн, сделав его иммунным к изменениям (защита от scope creep) на время цикла реализации.
*   **Input:** Успешный Integration Review Report.
*   **Output:** Замороженный пакет документов в `workspace/`.
*   **Owner:** Domain Expert / Commander.
*   **Entry Criteria:** Получен статус PASS на ревью.
*   **Exit Criteria:** Пакет официально признан окончательным для текущей итерации разработки.
*   **Next Stage:** Publish to AOS.

### 2.7. Publish to AOS
*   **Purpose:** Перенести утвержденный дизайн в официальный релизный пакет поставки (Deliverable).
*   **Input:** Замороженный пакет из `workspace/`.
*   **Output:** Пакет документации, перенесенный в `AOS/`.
*   **Owner:** Documentation Agent.
*   **Entry Criteria:** Решение о Freeze принято человеком.
*   **Exit Criteria:** Файлы скопированы/перемещены без изменений в структуре и содержимом.
*   **Next Stage:** Implementation Roadmap.

### 2.8. Implementation Roadmap
*   **Purpose:** Стратегически разбить замороженный дизайн на этапы внедрения.
*   **Input:** Опубликованный пакет `AOS/`.
*   **Output:** Документ `04_IMPLEMENTATION_ROADMAP.md`.
*   **Owner:** Implementation Planner.
*   **Entry Criteria:** Наличие официального, неизменяемого пакета `AOS/`.
*   **Exit Criteria:** Roadmap логично делит систему на части, поддающиеся независимой реализации.
*   **Next Stage:** Slice.

### 2.9. Slice
*   **Purpose:** Выделить один вертикальный срез системы для ближайшей итерации разработки.
*   **Input:** Implementation Roadmap.
*   **Output:** Выбранный и зафиксированный срез (Slice Scope).
*   **Owner:** Domain Expert.
*   **Entry Criteria:** Roadmap утвержден.
*   **Exit Criteria:** Границы среза четко зафиксированы.
*   **Next Stage:** Task.

### 2.10. Task
*   **Purpose:** Детализировать Slice в точный, ограниченный Task Brief для агента реализации.
*   **Input:** Выбранный Slice, контракты из `AOS/`.
*   **Output:** Утвержденный Task Brief.
*   **Owner:** Implementation Planner.
*   **Entry Criteria:** Срез официально выбран в работу.
*   **Exit Criteria:** Task Brief не содержит неразрешенных противоречий и строго ограничен рамками Slice.
*   **Next Stage:** Implementation Handoff.

### 2.11. Implementation Handoff
*   **Purpose:** Передать завершённый пакет документации в процесс реализации.
*   **Input:** пакет `AOS/`; `04_IMPLEMENTATION_ROADMAP.md`; выбранный Slice; утверждённый Task Brief.
*   **Output:** Implementation Package Ready.
*   **Owner:** Implementation Planner.
*   **Entry Criteria:** Task Brief утверждён.
*   **Exit Criteria:** Полный пакет документации передан процессу реализации.
*   **Next Stage:** Implementation Process (находится вне области ответственности Documentation Pipeline).

---

## 3. Human Checkpoints

Обязательные точки документационного пайплайна, требующие решения человека:
*   **Утверждение Concept (Pass 1):** Убедиться, что System Design верно отражает проблему до начала проектирования пайплайнов.
*   **Integration Review:** Подтвердить, что дизайн не скатился в реализацию.
*   **Global Design Freeze:** Окончательное согласие на заморозку скоупа (предотвращение переписывания на ходу).
*   **Slice Selection:** Выбор приоритетов внедрения.
*   **Task Authorization:** Выдача явного разрешения на начало инженерной работы по спецификации.

---

## 4. Failure Boundaries

Типичные ошибки процесса проектирования документации, приводящие к блокировке пайплайна:
*   **Противоречие в Knowledge Baseline:** Если документы-источники конфликтуют (например, `01_Product` противоречит `02_Architecture`), агент останавливает работу.
*   **Отсутствие Authoritative Source:** Попытка проектировать фичу, не описанную в `06_Features.md`.
*   **Нарушение WHAT/HOW:** Попытка вставить JSON, API или псевдокод в `01_SYSTEM_DESIGN` или `02_PIPELINE`.
*   **Конфликт между документами Pass 2:** Смешивание Pipeline и Contracts в одном документе.
*   **Неуспешный Review:** Обнаружение критических дефектов во время Integration Review.

---

## 5. Recovery

Логика восстановления документационного процесса при сбоях:
*   **При противоречиях в Baseline:** Требуется ручное исправление базовых документов (`docs/`). Процесс проектирования откатывается к началу.
*   **При незначительных нарушениях (Minor Finding):** Применяется точечная правка конкретного текста в документе, после чего ревью возобновляется.
*   **При серьезных нарушениях (Major Finding на ревью):** Локальное переписывание затронутого раздела документа (например, перестроение Module Map) с повторной проверкой без отката всей фазы.
*   **Запрет на самовосстановление (No Self-Heal):** Документационный агент не имеет права сам придумывать недостающие требования. Он обязан остановиться и запросить решение у человека.

---

## 6. Handoff

Что передаётся между этапами проектирования документации:
*   Внутри Pass 1 и Pass 2 передаются **Markdown-черновики** в директории `workspace/`.
*   В момент Publish to AOS передается **замороженный пакет директории**, становящийся иммунным к изменениям.
*   Для этапа Implementation передаются **read-only спецификации**, выступающие строгими контрактами для написания кода. Никакие участки кода между этими документационными этапами не передаются.
*   Documentation Pipeline заканчивается передачей следующего пакета:
    *   пакет `AOS/`;
    *   `04_IMPLEMENTATION_ROADMAP.md`;
    *   выбранный Slice;
    *   утверждённый Task Brief.
    После этого начинается отдельный процесс реализации. Инженерная реализация не является частью данного документа.
