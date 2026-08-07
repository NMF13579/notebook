# DOCUMENTATION FACTORY

Настоящий документ является операционной инструкцией (Manual) для работы Documentation Agent. Он описывает мета-процесс — конвейер создания самой документации продукта AOS от исходной Knowledge Baseline до опубликованного замороженного архитектурного пакета. 

*Важно: Документ описывает процесс написания документации, а не целевой программный продукт (Runtime AOS).*

---

## 1. Factory Overview

*   **Цель:** Стандартизировать и сделать воспроизводимым процесс проектирования архитектуры системы, исключив хаотичные изменения и смешение абстракций.
*   **Вход (Input):** Первичные требования, уроки и концепты (Knowledge Baseline).
*   **Выход (Output):** Опубликованный пакет архитектуры (`AOS/`), готовый служить входом для downstream-процессов планирования.
*   **Область ответственности:** Определение ЧТО (WHAT) должна делать система. Factory не отвечает за код, структуры данных, API и Engineering Design (HOW).

---

## 2. Полный Documentation Pipeline

Конвейер проектирования состоит из следующих строго последовательных стадий:

### 2.1. Knowledge Baseline
*   **Purpose:** Фиксация исходных знаний, правил и продуктовых границ.
*   **Input:** Продуктовые идеи, требования пользователя, Lessons.
*   **Output:** Каталог `docs/` (`00_Core` – `06_Features`).
*   **Owner:** Product Owner / The Commander.
*   **Entry Criteria:** Старт проектирования.
*   **Exit Criteria:** База знаний полна, непротиворечива и зафиксирована.
*   **Next Stage:** PASS 1.

### 2.2. PASS 1 (Concept Design)
*   **Purpose:** Построение высокоуровневой концептуальной модели системы.
*   **Input:** Knowledge Baseline.
*   **Output:** `workspace/01_SYSTEM_DESIGN.md`.
*   **Owner:** Documentation Agent.
*   **Entry Criteria:** Baseline утвержден.
*   **Exit Criteria:** Документ описывает концепцию продукта (Actor, Module, Capability).
*   **Next Stage:** Structural Review.

### 2.3. Structural Review
*   **Purpose:** Независимая проверка концепции на целостность.
*   **Input:** `workspace/01_SYSTEM_DESIGN.md`.
*   **Output:** Вердикт (PASS / FAIL).
*   **Owner:** Auditor Agent.
*   **Entry Criteria:** Завершен PASS 1.
*   **Exit Criteria:** Документ самодостаточен и не содержит деталей реализации.
*   **Next Stage:** PASS 2.

### 2.4. PASS 2 (Architecture Contracts)
*   **Purpose:** Описание потока данных (Pipeline) и инвариантов/гарантий системы.
*   **Input:** `01_SYSTEM_DESIGN.md`, Knowledge Baseline.
*   **Output:** `workspace/02_PIPELINE.md`, `workspace/03_SYSTEM_CONTRACTS.md`.
*   **Owner:** Documentation Agent.
*   **Entry Criteria:** Structural Review = PASS.
*   **Exit Criteria:** Потоки (Runtime Pipeline) и контракты формализованы.
*   **Next Stage:** Integration Review.

### 2.5. Integration Review
*   **Purpose:** Проверка пакета из трёх документов на отсутствие противоречий (Cross-document Consistency) и разрывов (Domain Mismatch).
*   **Input:** Пакет (01, 02, 03).
*   **Output:** Вердикт (PASS / FAIL).
*   **Owner:** Auditor Agent.
*   **Entry Criteria:** Завершен PASS 2.
*   **Exit Criteria:** Документы описывают единую целевую систему, словарь (Ubiquitous Language) синхронизирован.
*   **Next Stage:** Global Design Freeze.

### 2.6. Global Design Freeze
*   **Purpose:** Архитектурная заморозка дизайна перед реализацией.
*   **Input:** Пакет в `workspace/`, Integration Review = PASS.
*   **Output:** Статус FREEZE.
*   **Owner:** The Commander (Человек).
*   **Entry Criteria:** Integration Review = PASS.
*   **Exit Criteria:** Статус зафиксирован, документы Read-Only.
*   **Next Stage:** Publish to AOS.

### 2.7. Publish to AOS
*   **Purpose:** Передача замороженного пакета в релизную директорию.
*   **Input:** Замороженные документы `workspace/`.
*   **Output:** Директория `AOS/`.
*   **Owner:** Documentation Agent.
*   **Entry Criteria:** Статус FREEZE.
*   **Exit Criteria:** Документы скопированы "байт в байт".
*   **Next Stage:** Implementation Planning.

### 2.8. Implementation Planning Handoff
*   **Purpose:** Передача ответственности из архитектурной фабрики в конвейер планирования реализации.
*   **Input:** Опубликованный пакет `AOS/`.
*   **Output:** Делегирование управления downstream-процессам.
*   **Owner:** Implementation Planner.
*   **Entry Criteria:** Архитектурный пакет опубликован в `AOS/`.
*   **Exit Criteria:** Управление передано по следующей цепочке: Architecture Package (`AOS/`) → определение макро-стратегии и последовательности срезов (`04_IMPLEMENTATION_ROADMAP.md`) → выбор ограниченного среза (selected bounded subject) → планирование реализации среза строго по правилам `IMPLEMENTATION_PLANNING_PIPELINE_R9.md`.
*   **Next Stage:** Вне ответственности Documentation Factory.

---

## 3. Reviews

В Factory существуют два критических барьера качества:
1.  **Structural Review:** Проводится в конце PASS 1. Проверяет **Concept Independence** (понятность без дополнительных документов) и **Concept Completeness**. Считается пройденным (PASS), если документ определяет продукт без погружения в инженерные детали.
2.  **Integration Review:** Проводится в конце PASS 2. Проверяет **Domain Match** (отсутствие смешения продукта и процесса создания продукта) и кросс-документную целостность (единый словарь ролей и состояний). Считается пройденным, если 01, 02 и 03 образуют монолитный дизайн.

---

## 4. Freeze

**Global Design Freeze** означает полный запрет на архитектурные изменения.
*   **Последствия:** Система, агенты реализации и планировщики не имеют права изменять документы `AOS/`. Если в ходе реализации выявляется нехватка данных, реализация блокируется.
*   **Условия Reopen (разморозки):** Проектирование можно возобновить только если:
    1. Обнаружено внутреннее неразрешимое техническое противоречие (Technical Deadlock).
    2. Изменились Product Requirements в `docs/`.
    3. The Commander явно отдал команду на изменение архитектуры (Explicit Human Decision).

---

## 5. Deliverables

По мере прохождения пайплайна формируются следующие ключевые артефакты:
*   `Knowledge Baseline` (Файлы `docs/`).
*   `System Design` (`01_SYSTEM_DESIGN.md`).
*   `Runtime Pipeline` (`02_PIPELINE.md`).
*   `System Contracts` (`03_SYSTEM_CONTRACTS.md`).
*   `Deliverable Package` (Папка `AOS/`).

---

## 6. Working Areas

Ответственность файловой структуры, с которой работает Factory:
*   `docs/`: **Source of Truth**. Авторитетная базовая линия продукта. Редактируется только при явном изменении бизнес-требований.
*   `workspace/`: **Draft Area**. Песочница агента-документалиста. Здесь хранятся черновики PASS 1, PASS 2, Roadmap и текущий рабочий процесс.
*   `AOS/`: **Deliverable Package**. Замороженный эталон. Релизная версия документации. Строго Read-Only для всех процессов реализации.
*   `archive/`: **History**. Исторические копии, отброшенные варианты, логи старых интеграций.

---

## 7. Agent Rules

Любой Documentation Agent обязан неукоснительно следовать правилам:
*   **WHAT / HOW Separation:** Документация описывает ЧТО (WHAT). Агент никогда не пишет в архитектурные документы API, структуры БД, JSON или псевдокод (HOW).
*   **Fail Closed:** При любом конфликте источников, неизвестности или нарушении правил пайплайна агент обязан остановиться, вернуть статус FAIL или BLOCKED и запросить решение человека.
*   **Authoritative Source:** Источником истины для дизайна является `docs/`. Запрещено использовать обрывки диалогов из чата как доказательство архитектурного решения.
*   **No Self-Heal:** Агент не должен придумывать недостающие бизнес-правила самостоятельно, пытаясь спасти проваливающийся Review.
*   **One Next Action:** За один запуск (run) агент выполняет только одну стадию Factory (например, только Review или только написание конкретного документа).
*   **No Scope Creep:** Агент не расширяет свою задачу на смежные документы без явной команды.

---

## 8. Factory Completion

Работа Documentation Factory считается успешно завершенной, когда:
1. Архитектурный пакет прошел Integration Review и заморожен (Global Design Freeze).
2. Замороженные документы опубликованы (скопированы) в `AOS/`.
3. Архитектурная база готова к передаче ответственности (Handoff) по цепочке: Architecture Package (`AOS/`) → макро-стратегия и границы срезов (`04_IMPLEMENTATION_ROADMAP.md`) → выбор ограниченного среза → планирование реализации среза (`IMPLEMENTATION_PLANNING_PIPELINE_R9.md`).
