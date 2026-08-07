# 04 — Implementation Roadmap

## 1. Purpose
Цель данного Roadmap — перевести замороженный архитектурный концепт AOS (пакет `AOS/`) в строгую, последовательную стратегию реализации. Документ определяет порядок постройки системы изолированными, проверяемыми вертикальными срезами (vertical slices) без нарушения контрактов и архитектурных инвариантов.

## 2. Scope
Roadmap охватывает первичную реализацию ядра AOS (Core Runtime Pipeline) от приема команды пользователя до слияния кода. 
Вне scope: автономная оркестрация, сложные UI/Dashboards, Control Plane для множества параллельных агентов, самовосстанавливающиеся (self-heal) циклы.

## 3. Authoritative Inputs
*   `docs/00_Core.md` (Правила безопасности, Minimal Safety Floor).
*   `AOS/01_SYSTEM_DESIGN.md` (Концепт и модули).
*   `AOS/02_PIPELINE.md` (Потоки исполнения).
*   `AOS/03_SYSTEM_CONTRACTS.md` (Инварианты и гарантии).

## 4. Implementation Principles
1.  **Product Runtime First:** В первую очередь создается основной пользовательский путь (от запроса до интеграции), а не внутренние инструменты автоматизации (Development Factory).
2.  **Manual Before Automation:** Передача управления и состояний (Handoff) реализуется через простые механизмы и ручной запуск. `PROPOSAL`: CLI-скрипты и файловая система.
3.  **Contract-First:** Реализация каждого среза начинается с обеспечения валидации контрактов входа и выхода (Invariants validation).
4.  **No Platform-Building:** Исключается создание тяжелых платформ (full Control Plane, RAG, Vector DB, autonomous loops) без доказанной необходимости на конкретном срезе.

## 5. Dependency Model
Граф зависимостей строится линейно, отражая Runtime Pipeline:
`Foundation → Slice 1 (Intake) → Slice 2 (Execution) → Slice 3 (Verification) → Slice 4 (Decision)`.
Каждый последующий срез не может функционировать без результатов предыдущего, при этом каждый срез несет самостоятельную тестируемую и верифицируемую ценность.

## 6. Foundation
Минимальная постоянная инфраструктура (Stage 0), без которой невозможно начать работу над первым вертикальным срезом (Slice 1).

*   **Структура хранения кода и данных:**
    *   *Зачем нужно 1 slice:* Место для сохранения кода Intake Engine и генерации выходных артефактов (Bounded Intent Artifact).
    *   *Классификация:* `PROPOSAL` (Modular monorepo; хранение состояния локально на диске / filesystem storage).
    *   *Отложено:* Базы данных, message brokers, cloud infrastructure.
*   **Точка входа (Entrypoint):**
    *   *Зачем нужно 1 slice:* Способ передать первый пользовательский Intent в систему.
    *   *Классификация:* `PROPOSAL` (Примитивный CLI-интерфейс).
    *   *Отложено:* Сложные UI, веб-дашборды, API сервера, чат-интерфейсы.
*   **Связь с LLM (LLM API Integration):**
    *   *Зачем нужно 1 slice:* Для трансляции Intent в формальный контракт (суть Intake Engine).
    *   *Классификация:* `HUMAN_ACCEPTED_FACT` (Использование AI-агентов / Executor'ов закреплено в 01_SYSTEM_DESIGN.md).
    *   *Отложено:* RAG, Vector DB, autonomous orchestration, сложный prompt management.

*(Элементы изоляции исполнения, такие как git worktree или контейнеры, намеренно не включены в Foundation, так как они не требуются для запуска Slice 1, а отложены до Slice 2).*

## 7. Implementation Stages / Vertical Slices

### Slice 1: Minimal Intake & Specification
*   **Purpose:** Преобразование статичного неструктурированного запроса (Intent) в формализованное, ограниченное представление (bounded representation) с учетом Baseline.
*   **Value:** Исключение эффекта "Garbage-in / Garbage-out"; реализация минимальной проверяемой стадии Runtime Pipeline без скрытого Engineering Design.
*   **Входные зависимости:** Foundation, `docs/00_Core.md`, явно сформулированный статичный Intent пользователя.
*   **Архитектура:** Модуль *The Intake Engine* (`01_SYSTEM_DESIGN.md`); этапы *2.1 Intake & Definition* и *2.2 Specification & Briefing* (`02_PIPELINE.md`).
*   **Executable Contracts:** *Intent Contract* (Bounded, Traceable, Unambiguous).
*   **Observable Result:** Формирование проверяемого артефакта (Bounded Intent Artifact), выполняющего семантическую роль `Task Brief`, или явный отказ (validation failure).
*   **Acceptance Boundary:** При двусмысленном или нарушающем Baseline намерении система отказывается формировать артефакт (Fail Closed).
*   **Negative Scenarios:** LLM получает запрос, выходящий за Product Scope, и система возвращает проверяемую ошибку валидации.
*   **Вне scope:** Интерактивное уточнение задачи у пользователя (multi-turn dialog); фактическое написание кода по задаче. Roadmap определяет только семантическую роль `Task Brief`. Точная техническая схема (schema), required fields, validation rules, state semantics и I/O определяются отдельным Engineering Design до реализации. Coding Agent этот контракт не проектирует.
*   **Зависимость следующего slice:** Bounded Execution (Slice 2) требует утвержденный формализованный `Task Brief` (в строгом соответствии с заранее спроектированным Engineering-контрактом).

### Slice 2: Bounded Execution
*   **Purpose:** Безопасное внесение изменений в изолированной среде.
*   **Value:** Защита основной кодовой базы от неконтролируемых мутаций.
*   **Входные зависимости:** Утвержденный Task Brief (как артефакт, соответствующий фиксированной схеме), Foundation.
*   **Архитектура:** Модули *The Control Matrix*, *The Executor* (`01_SYSTEM_DESIGN.md`); этап *2.3 Bounded Execution* (`02_PIPELINE.md`).
*   **Executable Contracts:** *Authority Contract* (нет системных привилегий по умолчанию; наличие Execution Authorization).
*   **Observable Result:** Изолированная среда (`PROPOSAL`: git worktree или иная технология изоляции ветвления), в которой изменены целевые файлы в строгом соответствии с Task Brief.
*   **Acceptance Boundary:** `HUMAN_ACCEPTED_FACT`: Bounded isolation. Код изменен только в рамках изолированной песочницы; основное состояние остается неизменным.
*   **Negative Scenarios:** Агент пытается изменить файлы вне Task Brief или выполнить деструктивные команды. Ожидаемое поведение: отказ доступа / прерывание.
*   **Вне scope:** Self-heal при ошибках; запуск валидации внутри потока исполнения.
*   **Зависимость следующего slice:** Verification & Evidence требует изолированную мутировавшую среду на входе.

### Slice 3: Verification & Evidence
*   **Purpose:** Механическая сборка доказательств работоспособности измененного кода.
*   **Value:** Переход от "доверия к LLM" к "объективным механистическим доказательствам" качества.
*   **Входные зависимости:** Изолированная измененная среда (Mutating State).
*   **Архитектура:** Модуль *The Verification Protocol* (`01_SYSTEM_DESIGN.md`); этап *2.4 Verification & Evidence* (`02_PIPELINE.md`).
*   **Executable Contracts:** *Evidence Contract* (Immutable, Independent, Precedent).
*   **Observable Result:** Формирование файла `Evidence Record` (содержащего exit codes, diff, логи).
*   **Acceptance Boundary:** Среда замораживается (Frozen State) во время проверки; Evidence не зависит от мнения LLM.
*   **Negative Scenarios:** Тесты/чеки падают. Ожидаемое поведение: Evidence Record фиксирует `FAIL`, процесс останавливается.
*   **Вне scope:** Динамическая генерация тестов агентом; попытки самопочинки (Self-heal).
*   **Зависимость следующего slice:** Human Decision требует сформированный Evidence Record.

### Slice 4: Decision & Integration
*   **Purpose:** Передача принятия решения человеку и применение подтвержденных изменений.
*   **Value:** Гарантия финального вердикта от лица человека (The Commander) перед изменением состояния.
*   **Входные зависимости:** Immutable Evidence Record, Diff изменений.
*   **Архитектура:** Модуль *The Decision Surface* (`01_SYSTEM_DESIGN.md`); этапы *2.5 Human Decision* и *2.6 Integration & Evolution* (`02_PIPELINE.md`).
*   **Executable Contracts:** *Human Decision Contract* (Integration Verdict; Evidence before Decision).
*   **Observable Result:** CLI/UI prompt пользователя (Accept/Reject). При Accept — применение изменений в глобальное состояние.
*   **Acceptance Boundary:** Изменение глобального состояния происходит только при явном Accept.
*   **Negative Scenarios:** Дрейф состояния (State Drift) основного репозитория во время проверки. Ожидаемое поведение: блокировка интеграции.
*   **Вне scope:** Автоматическое разрешение конфликтов слияния (Merge conflict resolution).

## 8. Runtime Pipeline Mapping
Вертикальные срезы прямо имплементируют абстрактный Runtime Pipeline (`AOS/02_PIPELINE.md`):
*   **Slice 1** покрывает `2.1 Intake & Definition` и `2.2 Specification & Briefing`.
*   **Slice 2** покрывает `2.3 Bounded Execution`.
*   **Slice 3** покрывает `2.4 Verification & Evidence`.
*   **Slice 4** покрывает `2.5 Human Decision` и `2.6 Integration & Evolution`.

## 9. Contract Coverage
*   **Slice 1:** Реализует `Intent Contract` (формализация намерений).
*   **Slice 2:** Реализует `Authority Contract` (работа только в рамках песочницы).
*   **Slice 3:** Реализует `Evidence Contract` (неизменяемое доказательство работоспособности).
*   **Slice 4:** Реализует `Human Decision Contract` (Explicit Human Decision для фиксации изменений).

## 10. Validation Strategy
Стратегия верификации Roadmap в ходе реализации заключается в изолированном тестировании каждого среза:
*   **Slice 1:** Mock Intent → генерация формализованного Bounded Intent Artifact (согласно спроектированной схеме) → валидация формата и compliance.
*   **Slice 2:** Mock Task Brief → проверка корректной мутации в изолированной среде без затрагивания глобального состояния.
*   **Slice 3:** Mock изолированная среда (с ошибками и без) → проверка формата Evidence Record, отсутствие галлюцинаций LLM.
*   **Slice 4:** Mock Evidence Record → подтверждение интеграции (или отказа от неё) через ручной Accept/Reject.

## 11. Risks / Unknowns / Conflicts
*   **UNKNOWN:** Точные схемы (schema), required fields, I/O formats, validation rules, state semantics, failure/recovery semantics, API/CLI contracts и форматы хранения (`Task Brief`, `Evidence Record`, `Lessons`). Эти неизвестные должны быть определены на этапе Engineering Design **до** передачи задачи Coding Agent'у. Coding Agent не проектирует эти контракты.
*   **PROPOSAL / RISK:** Использование `git worktree` для изоляции сред в Slice 2. Управление изолированными средами может привести к State Drift при длительном ожидании Human Decision. *Митигация:* Изначальная реализация поддерживает строго последовательное исполнение (одна задача за раз, блокировка новых Execution до Decision).
*   **CONFLICT:** Отсутствуют (архитектурных противоречий с замороженным пакетом AOS не выявлено).

## 12. Roadmap Exit Criteria
Данный Roadmap считается полностью завершенным как planning artifact (документ планирования), когда выполнены следующие условия:
*   Scope реализации ядра AOS определен.
*   Foundation строго ограничен необходимой инфраструктурой для запуска первого среза.
*   Vertical slices (1–4) явно выделены, их границы (Boundaries) и зависимости определены.
*   Этапы Runtime Pipeline полностью покрыты предложенными срезами.
*   Архитектурные Contracts (`03_SYSTEM_CONTRACTS.md`) корректно распределены по срезам.
*   Все принятые факты, `PROPOSAL`, `UNKNOWN` и `CONFLICT` корректно классифицированы и не содержат скрытых архитектурных решений.
*   Строгая последовательность передачи работы (Handoff sequence) определена.
*   Документ прошел необходимые проверки (Reviews) и готов к Human Review.

## 13. Implementation Completion Target
В будущем, реализация продукта на базе этого Roadmap будет считаться успешной (достижение informational target) при следующем условии:
*   `Foundation + Slice 1–4 implemented and validated end-to-end.`
*Ожидаемый результат реализации является будущей целью и не означает текущий статус готовности (PASS/READY/implemented) на этапе планирования.*

## 14. Handoff & Next Actions
Roadmap определяет макро-стратегию и не занимается детальным проектированием или передачей задач агентам реализации.

Строгая последовательность следующих действий:
1.  **Macro Selection:** Выбор следующего приоритетного макро-среза из Roadmap (например, Foundation + Slice 1).
2.  **R9 Handoff:** Передача выбранного среза (bounded subject) в конвейер `IMPLEMENTATION_PLANNING_PIPELINE_R9.md`.
3.  **Pipeline Execution:** Дальнейшее детальное планирование (Feature Selection, Product Contract, Engineering Design и формирование Implementation Package) осуществляется строго по правилам R9. Roadmap не владеет этим внутренним процессом.
