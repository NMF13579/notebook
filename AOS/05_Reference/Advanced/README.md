# 06_Advanced

## Назначение раздела

Раздел `06_Advanced` описывает поздние capabilities нового AOS, которые могут появиться только после подтверждённой необходимости.

Он не является обязательным implementation roadmap и не означает, что перечисленные здесь подсистемы должны быть созданы.

Основной принцип:

```text
product need
→ repeated manual workflow
→ observed limitation
→ Evidence
→ simpler alternatives
→ bounded capability proposal
→ human decision
→ minimal trial
→ independent validation
→ retain, revise or remove
```

Advanced capability не принимается потому, что она существовала или проектировалась в старом AOS-FARM.

## Legacy Reference Boundary

Материалы:

- `NMF13579/AOS-FARM`;
- `AgentOS/AOS-1`;
- старые планы;
- старые system prompts;
- отчёты;
- recovered artifacts;
- история чатов;

используются только как:

```text
READ_ONLY_REFERENCE
authority: NONE
```

Из них разрешено извлекать:

- product intent;
- observable behavior;
- candidate contracts;
- подтверждённые tests;
- successful patterns;
- failure modes;
- lessons learned;
- trade-offs;
- implementation ideas.

Из них нельзя автоматически переносить:

- active architecture;
- repository topology;
- Source of Truth;
- roadmap;
- lifecycle;
- statuses;
- approvals;
- Risk Profiles;
- execution authorization;
- Commit, Push, Merge или Release authorization;
- незавершённые recovery chains;
- legacy complexity.

Default reuse strategy:

```text
REIMPLEMENT_FROM_CONTRACT
```

Любая идея из legacy становится частью нового AOS только после независимого обоснования потребностями нового продукта, документирования в новом repository и соответствующего human decision.

## Место раздела в развитии AOS

`06_Advanced` рассматривается только после того, как существуют:

- понятный Product Contract;
- работающий Product Runtime;
- минимум один полезный vertical slice;
- повторяемые manual development cycles;
- Minimal Safety Floor;
- подтверждённые operational limitations.

Product Runtime не должен зависеть от Development Factory или advanced control infrastructure.

## Структура

```text
06_Advanced/
├── 06.01_Admission_Criteria/
├── 06.02_Architecture_Evolution/
├── 06.03_Automation_Principles/
├── 06.04_Runtime_Enforcement/
├── 06.05_Registries_and_Indexes/
├── 06.06_External_Integrations/
├── 06.07_Multi_Project_Support/
├── 06.08_Scaling/
├── 06.09_Operational_Lessons/
└── 06.10_Retirement_and_Simplification/
```

## Общие инварианты

```text
PASS ≠ approval.
Evidence ≠ approval.
CI PASS ≠ approval.
UNKNOWN ≠ OK.
NOT_RUN ≠ PASS.
Human approval cannot be simulated.
Skeleton ≠ implementation.
Documentation ≠ technical completion.
Plan output ≠ Task Brief.
Routing decision ≠ execution authorization.
Commit ≠ Push ≠ Merge ≠ Release.
```

Advanced capability не может отменять эти инварианты.

## Что не является основанием для advanced capability

Недостаточными основаниями являются:

- возможность технически её построить;
- наличие аналогичной подсистемы в legacy;
- желание автоматизировать единичную операцию;
- один incident;
- один успешный prototype;
- формальная полнота architecture;
- стремление исключить все unknowns;
- желание централизовать state без доказанной проблемы;
- удобство агента за счёт усложнения продукта;
- предположение, что сложность понадобится позже.

## Минимальный результат раздела

Раздел считается полезным, если позволяет:

- не повторить automation-first ошибку;
- не превратить reference в Source of Truth;
- отличать полезную capability от преждевременной infrastructure;
- вводить сложность постепенно;
- сохранять removal path;
- удалять неподтверждённые механизмы без разрушения Product Runtime.
