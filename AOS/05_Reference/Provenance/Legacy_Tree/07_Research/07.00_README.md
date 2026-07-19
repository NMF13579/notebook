# 07 — Research

## Назначение

Раздел `07_Research` хранит исследования, извлечённые уроки, архитектурные alternatives, reconstruction hypotheses и experiment candidates, которые могут помочь воспроизвести AOS в новом проекте с меньшей сложностью и без повторения известных ошибок.

Этот раздел не является Source of Truth для продукта, architecture, roadmap, Governance, implementation или execution.

Главная формула раздела:

```text
legacy artifact
→ observation
→ intent
→ lesson или failure mode
→ candidate
→ independent validation
→ explicit human decision
→ новый contract или decision
```

Запрещённый путь:

```text
legacy artifact
→ копирование
→ объявление новым Source of Truth
```

## Legacy boundary

Старые проекты и материалы, включая `NMF13579/AOS-FARM` и `AgentOS/AOS-1`, имеют только следующую роль:

```yaml
role: READ_ONLY_REFERENCE
authority: NONE
```

Они могут использоваться для извлечения:

- product intent;
- observable behavior;
- lessons;
- failure modes;
- candidate contracts;
- reusable concepts;
- rejected approaches;
- вопросов, требующих повторной проверки.

Они не дают:

- product authority;
- architecture authority;
- roadmap authority;
- approval authority;
- execution authorization;
- lifecycle authority;
- permission на protected/canonical changes;
- оснований автоматически переносить topology, dependencies или internal abstractions.

## Структура

```text
07_Research/
├── 07.00_README.md
├── 07.01_Reconstruction_Research_Method/
├── 07.02_Legacy_Lessons_and_Failure_Modes/
├── 07.03_Product_Behavior_Reconstruction/
├── 07.04_Contract_Reconstruction_Research/
├── 07.05_Architecture_Alternatives/
├── 07.06_Model_Routing_and_Task_Decomposition/
├── 07.07_Agent_and_Harness_Engineering/
├── 07.08_Future_Capability_Candidates/
└── 07.09_Open_Questions_and_Experiments/
```

## Общие инварианты

```text
Reference ≠ Source of Truth.
Observation ≠ requirement.
Legacy behavior ≠ accepted contract.
Existing implementation ≠ target architecture.
Historical decision ≠ current decision.
Reusable idea ≠ authorized dependency.
Successful past test ≠ Evidence для новой реализации.
PASS ≠ approval.
Evidence ≠ approval.
CI PASS ≠ approval.
UNKNOWN ≠ OK.
NOT_RUN ≠ PASS.
Human approval cannot be simulated.
```

## Границы соседних разделов

- `03_Product` хранит активное определение продукта и принятые Product Contracts.
- `04_Development` хранит активные development workflows.
- `05_Control` хранит принятые control rules и Governance mechanisms.
- `06_Advanced` хранит принятые или явно запланированные advanced capabilities.
- `08_References` хранит исходные reference-материалы и provenance.
- `09_Archive` хранит superseded, rejected и obsolete artifacts.

Материал остаётся в `07_Research`, пока он не прошёл независимую проверку и explicit human decision о продвижении в активный раздел.
