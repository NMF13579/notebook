---
document_id: 05_Reference
title: "Reference"
status: draft
authority: supporting
human_review_required: true
version: 4.0
updated: 2026-07-26
repository_snapshot: "NMF13579/AgentOS dev@e3a60a92fbd5e78e583cddb519d39527583f3433 (2026-06-05)"
repository_commands_tests_build: NOT_RUN
---

# Reference

## Reference policy

A reference may supply a problem pattern, behavior pattern, failure mode, implementation idea, constraint or test concept. It cannot supply target authority, approval or roadmap priority by itself.

Historical AgentOS, AOS-FARM and AOS-02 are read-only references. Only an explicit human decision may promote a mechanism into the target design.

## Repository snapshot

- URL: `https://github.com/NMF13579/AgentOS/tree/dev`
- Branch: `dev`
- Commit: `e3a60a92fbd5e78e583cddb519d39527583f3433`
- Commit date: `2026-06-05T12:38:19Z`
- Inspection mode: static read-only
- Commands/tests/build: `NOT_RUN`
- At inspection, `main` was reported 13 commits ahead of requested `dev`; no main-branch content is imported into these conclusions.

## Source register

## 1. Source authority rules

1. An explicit human statement in a chat may support `DECIDED`.
2. An assistant response does not become `DECIDED` without explicit human acceptance.
3. A repository path supports `OBSERVED` only for the pinned commit.
4. Repository reports support what they record, but their embedded test claims remain `REPORTED` unless independently run.
5. Uploaded notes are candidate/reference sources unless a matching human decision exists.
6. A document's self-declared `canonical` frontmatter does not establish target authority.
7. Chat summaries are incomplete sources and must be marked accordingly.

## 2. Chat sources

| ID | Chat title | Date | Completeness | Permitted use |
|---|---|---:|---|---|
| CH-01 | Handoff / AOS Documentation Reconstruction | 2026-07-19 | Partial summary | Legacy authority boundary; product-first reconstruction |
| CH-02 | Структура документационного слоя | 2026-07-19 | Partial summary | Documentation structure; target reconstruction intent |
| CH-03 | Внедрение безопасного рабочего процесса | 2026-07-19 | Partial summary | Minimal safety floor; authority separation |
| CH-04 | Этапы пайплайна проекта | 2026-07-20 | Partial summary | End-to-end task pipeline and human acceptance |
| CH-05 | AOS-FARM Extraction Review | 2026-07-20 | Partial summary | Limits of reconstruction packages |
| CH-06 | Статическая экстракция AOS-FARM | 2026-07-22 | Partial summary | Read-only extraction; reconstruction limitations |
| CH-07 | Экстракция данных проекта | 2026-07-23 | Partial summary | Schemes, features, errors, lessons; simple extraction |
| CH-08 | Автономная экстракция данных | 2026-07-23 | Partial summary | Separate output workspace; source repo read-only |
| CH-09 | Проектирование архитектуры AOS | 2026-07-23 | Partial summary | Reconstruction → synthesis → design → implementation |
| CH-10 | Создание документов и синтез | 2026-07-24 | Partial summary | Exhaustive extraction judged too costly and low-value |
| CH-11 | Реализация через фичи | 2026-07-26 | Partial summary | Compact catalog and feature-driven reconstruction |
| CH-12 | Обобщенная информация для каталога | 2026-07-26 | Current project turn | Requested Core/Product/Architecture/Development/Lessons/Reference/Features |
| CH-13 | Current audit request | 2026-07-26 | Complete current turn | Audit, recheck chats/sources, corrected package |

## 3. Repository source

### RP-00 — pinned snapshot

- URL: `https://github.com/NMF13579/AgentOS`
- Branch: `dev`
- Commit: `e3a60a92fbd5e78e583cddb519d39527583f3433`
- Commit date: `2026-06-05T12:38:19Z`
- Mode: static read-only inspection
- Tests/builds/validators: `NOT_RUN`

### Repository path groups

| ID | Paths | What they support |
|---|---|---|
| RP-01 | `README.md`, `INIT.md` | Product identity, onboarding, current capability claims, Spec Wizard boundary |
| RP-02 | `llms.txt`, `ROUTES-REGISTRY.md` | Bootstrap and route ownership |
| RP-03 | `core-rules/MAIN.md` | Authority, governance, agent boundaries |
| RP-04 | `state/MAIN.md`, `HANDOFF.md`, `tasks/active-task.md` | State lifecycle, current handoff, idle task |
| RP-05 | `workflow/MAIN.md` | Plan gate, task contract, scope, one-task rule, lesson capture |
| RP-06 | `quality/MAIN.md`, `security/MAIN.md` | Verification gates, release blockers, risk/security |
| RP-07 | `docs/PROBLEM-INTERVIEW-ARCHITECTURE.md`, `scripts/check-interview-completeness.py` | Problem interview and completeness checker |
| RP-08 | `docs/PRODUCT-SPEC-ARCHITECTURE.md` | Product intent, lifecycle, progressive depth, authority boundary |
| RP-09 | `docs/SPEC-TO-TASK-GENERATOR.md`, `scripts/generate-tasks-from-spec.py` | Candidate Task Contract generation |
| RP-10 | `schemas/task.schema.json`, `scripts/validate-task.py` | Task schema and validation behavior |
| RP-11 | `schemas/verification.schema.json`, `scripts/validate-verification.py`, `reports/verification.md` | Verification contract and demo artifact |
| RP-12 | `lessons/lessons.md`, `lessons/templates/lesson-entry.md` | Incident-to-lesson mechanism |
| RP-13 | `docs/M28-HYBRID-RAG-LIGHT-ARCHITECTURE.md`, `scripts/build-context-index.py`, `data/context-index.json`, `data/index.json` | Context selection and index state |
| RP-14 | `docs/HONEST-PASS-RESULT-CONTRACT.md`, `scripts/check-false-pass-resistance.py`, `reports/m67-completion-review.md` | False-PASS resistance |
| RP-15 | `docs/BOUNDED-RETRY-POLICY.md` | Retry policy and limits |
| RP-16 | `scripts/repo-scan.py`, `reports/m68-inventory-review.md`, `reports/m68-docs-to-code-drift.json` | Repository hygiene and drift evidence |
| RP-17 | `repo-map.md` | Historical generated repository map |
| RP-18 | `docs/UI-SEMANTIC-COMPONENT-CONTRACT.md`, `docs/DESIGN-TOKENS-POLICY.md`, `docs/UI-REPLACEABILITY-POLICY.md` | `NOT_FOUND` at RP-00; listed as known gaps |
| RP-19 | `scripts/check-code-maintainability.py`, `scripts/check-doc-drift.py` | `NOT_FOUND` at RP-00 |
| RP-20 | `prompt-packs/**`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` | Agent adapters and prompt-pack surfaces |

## 4. Uploaded project notes

All note-only claims default to `REPORTED` unless corroborated by a human decision or repository observation.

| ID | File | Date | Main content |
|---|---|---:|---|
| NT-01 | `Главный ориентир проекта.txt` | UNKNOWN | Non-programmer control and real-project proof as project compass |
| NT-02 | `Добавление фич.txt` | UNKNOWN | Feature acceptance filter |
| NT-03 | `Философия агентос.txt` | UNKNOWN | Human authority, uncertainty, resilience, explainability |
| NT-04 | `Направления-развития.txt` | 2026-04-23 | 15 feature proposals and three-sprint roadmap |
| NT-05 | `Методы повышения точности.txt` | 2026-04-24 | Schema validation, few-shot, adaptive compute, routing, fine-tuning |
| NT-06 | `Вариант автоматизации оформления тз.txt` | 2026-04-25 | Natural-language idea → structured spec → contextual conflict check |
| NT-07 | `Что можно внедрить.txt` | 2026-04-29 | Ruler, Git context, Git-backed memory, replay candidates |
| NT-08 | `Правила биологического развития.txt` | 2026-04-30 | Context limits, one signal-one action, structural self-heal |
| NT-09 | `Проблемное интервью. Сценарии. UX.txt` | UNKNOWN | Interview, scenario, access, UX object, and screen-map pipeline |
| NT-10 | `Базовый UI.txt` | UNKNOWN | Neutral UI foundation and UI authority boundary |
| NT-11 | `Контекстный движок.txt` | UNKNOWN | Context engine readiness claims |
| NT-12 | `Кросс репо фича.txt` | UNKNOWN | Cross-repository installation and shared docs |
| NT-13 | `Сопровождение кода написанногоAI.txt` | UNKNOWN | AI-code maintainability and Code Stewardship |
| NT-14 | `Проблемы обслуживания AI-written code.txt` | UNKNOWN | Maintainability failure modes |
| NT-15 | `Проверка агента через изолированный чек лист.txt` | UNKNOWN | Honest PASS and isolated/private verification |
| NT-16 | `Паттерн для контроля изменения файлов.txt` | UNKNOWN | Git-status and changed-file guard |
| NT-17 | `Повысить качество кода.txt` | UNKNOWN | Small quality improvements and final quality gate |
| NT-18 | `Дорожная карта.txt` | UNKNOWN | Historical M44–M71 roadmap |
| NT-19 | `План исправлений 23.05.26.txt` | 2026-05-23 | Command, status, CI, duplication, and repository-hygiene fixes |
| NT-20 | `Этапы контроля принятия выполненных задач.txt` | UNKNOWN | Execution validity, closure readiness, controlled completion |
| NT-21 | `Совет моделей (mad).txt` | UNKNOWN | Multi-agent debate proposal |
| NT-22 | `Стек.txt` | UNKNOWN | Record project stack in technical specification |
| NT-23 | `Система безопасности.txt` | UNKNOWN | External security guidance as a candidate reference |
| NT-24 | `agentos_concept_notes_ru.md` | UNKNOWN | Historical broad AgentOS concept and control-panel roadmap |

## 5. External references inside notes

External papers, repositories, and product claims embedded in notes were not revalidated in this audit. They remain `REPORTED` and may be researched later on demand.

## Historical repository observations

Observed significant mechanisms include:

- safe installation/Simple Mode;
- `/init` discovery and `/spec` Task Brief;
- Product Interview/Product Spec;
- active Task Contract;
- scope/risk/state/quality/security modules;
- proposal-to-task candidate conversion;
- queue/readiness/authorization/session/verification architecture;
- negative fixtures and false-PASS mechanisms;
- context-index/repo-map experiments;
- lessons/retry;
- prompt packs and repository-health reports.

Cautions:

- many artifacts define architecture/policy/contracts rather than working runtime;
- runner is described as dry-run in the inspected safety document;
- current status sources conflict (`README` M39 versus `HANDOFF` M90/M91);
- context index/repo-map are stale or incomplete;
- absolute `file:///Users/...` links reduce portability;
- Product Feature Registry and dedicated AI-code maintainability checker were not found;
- repository test claims were not reproduced.

## Decision timeline

| Date | Decision / direction | Current interpretation |
|---|---|---|
| 2026-04-26 | Agent prompt packs; active-task only executable | Accepted direction; prompt packs observed |
| 2026-05-04 | Nonprogrammer/vibe-coder and Idea-to-Execution thesis | Current product purpose |
| 2026-05-11 | Problem → scenarios → access → UX objects/screens → approval | Historical accepted sequence; timing deferred |
| 2026-05-21 | Product Spec and small SaaS/control surface | Product direction historically desired; implementation deferred |
| 2026-05-31 | Defer UX/ТЗ/RAG/SQLite/SaaS/cross-repo/MAD during stabilization | Historical stabilization boundary |
| 2026-06-03 | Feature Passport and registry-controlled direction | Product Feature Registry still not found |
| 2026-06-04 | Light RAG/SQLite derived-only; cross-repo by default | Later deferred/superseded for current stage |
| 2026-06-03/04 | Small controlled changes, inventory, rollback and script↔spec check | Current development lessons |
| 2026-06-06 | Old source supplies principles, not authority | Current legacy boundary |
| 2026-07-02 | Dashboard/guided flow/chat desired | Deferred product surface |
| 2026-07-09 | Manual real-task dogfood | Current validation direction |
| 2026-07-17/18 | Exact source binding, read-only reference, greenfield target | Current reconstruction boundary |
| 2026-07-19 | Product Runtime first, Minimal Safety Floor, modular monorepo | Current architectural direction at principle level |
| 2026-07-24 | Stop exhaustive extraction | Current process decision |
| 2026-07-26 | Feature-first catalog and reference-on-demand | Current extraction strategy |

## External research themes

Research only when a selected feature requires it:

- GitHub Spec Kit / spec-driven development;
- Aider-style repo maps;
- single-source agent rules/adapters;
- structured outputs/schema validation;
- adaptive model routing;
- Git-backed context/replay;
- specialized agent roles;
- semantic UI/tokens;
- AI-code maintainability and docs-code drift.

Benchmark percentages, cost claims and current product behavior in notes must be freshly verified before material design/procurement decisions.

## Reference selection test

1. Which observed target problem does this pattern solve?
2. Can the principle be used without the full dependency?
3. Does it preserve human authority and Markdown readability?
4. What metric would show improvement?
5. What is the smallest experiment?
6. What is the rollback?
7. Is simplification better?

## Audit limitations

- Available chat history includes summaries, not guaranteed complete raw transcripts.
- Uploaded notes may contain earlier assistant analysis.
- Self-declared canonical labels in notes do not create target authority.
- Repository inspection was static and significant-component focused.
- No command/test/build/CI/release check was run.
- This package has not been accepted by the human owner.

## Navigation

- Core decisions: [00_Core.md](00_Core.md)
- Product: [01_Product.md](01_Product.md)
- Architecture: [02_Architecture.md](02_Architecture.md)
- Development: [03_Development.md](03_Development.md)
- Lessons/conflicts: [04_Lessons.md](04_Lessons.md)
- Feature passports: [06_Features.md](06_Features.md)

**HUMAN REVIEW REQUIRED**
