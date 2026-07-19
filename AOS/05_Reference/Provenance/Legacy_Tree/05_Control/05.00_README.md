# 05_Control

`05_Control` описывает минимальный и постепенно развиваемый control layer нового AOS.

Он создаётся после `03_Product` и `04_Development`, выводится из потребностей нового проекта и не копируется из legacy topology.

## Legacy boundary

Материалы `NMF13579/AOS-FARM`, `AgentOS/AOS-1`, старые планы, reports и Governance artifacts используются только как:

```text
READ_ONLY_REFERENCE
authority: NONE
```

Из них извлекаются lessons, contracts, failure modes, negative scenarios и anti-patterns. Они не определяют автоматически architecture, Source of Truth, lifecycle, Risk Profiles, gates, approval model, implementation order или Runtime Enforcement нового проекта.

## Формула раздела

```text
Product requirements
→ Development workflow
→ observed risks
→ minimal control requirements
→ manual validation
→ targeted control evolution
```

## Структура

```text
05_Control/
├── 05.01_Control_Purpose_and_Boundaries/
├── 05.02_Human_Authority_and_Decision_Rights/
├── 05.03_Claims_Evidence_Review_and_Decisions/
├── 05.04_Risk_Unknowns_and_Stop_Rules/
├── 05.05_Control_Points_in_Product_and_Development_Workflows/
├── 05.06_Source_of_Truth_and_Protected_Changes/
├── 05.07_Execution_Git_and_Destructive_Authorization/
├── 05.08_Control_Failure_Modes_and_Anti_Patterns/
└── 05.09_Progressive_Control_Evolution/
```

## Базовые инварианты

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
Plan output ≠ execution authorization.
Routing decision ≠ execution authorization.

Edit ≠ commit.
Commit ≠ push.
Push ≠ merge.
Merge ≠ release.
```

Раздел не создаёт Control Plane, execution engine, registry, database, universal lifecycle machine, approval service или Runtime Enforcement.
