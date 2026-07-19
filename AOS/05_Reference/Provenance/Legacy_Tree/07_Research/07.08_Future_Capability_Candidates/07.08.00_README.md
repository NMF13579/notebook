# 07.08 — Future Capability Candidates

## Назначение

Документ хранит capabilities, которые могут понадобиться после подтверждения Product Runtime value и успешных manual cycles.

Наличие capability в этом списке не делает её requirement, roadmap commitment или implementation authorization.

## Admission sequence

```text
observed recurring problem
→ manual workaround
→ repeated Evidence
→ bounded capability hypothesis
→ alternatives analysis
→ experiment
→ human decision
→ roadmap admission
```

## Development Factory

Возможные candidates:

- structured Task Brief generation;
- execution package assembly;
- deterministic reports;
- reusable validation recipes;
- project memory;
- session handoff tooling.

Development Factory не должна становиться prerequisite базового product usage.

## Progressive Governance

Candidates:

- Risk Profile workflow;
- protected/canonical gates;
- Evidence completeness checks;
- human review packages;
- lifecycle mutation controls;
- policy validation.

Полный Governance вводится пропорционально реальным рискам.

## Registry

Registry рассматривается только при подтверждённой проблеме discovery, ownership или drift.

Условия:

- один canonical owner per fact class;
- registry не дублирует Source of Truth;
- derived data можно полностью перестроить;
- silent data loss исключена;
- migration и recovery определены.

## Runtime Enforcement

Possible candidates:

- command guards;
- workspace guards;
- authorization package verification;
- protected file enforcement;
- Git mutation gates;
- claim ceiling verification.

Runtime Enforcement не может симулировать human approval.

## Integrations

Potential integrations:

- GitHub;
- IDEs;
- model providers;
- issue trackers;
- document systems;
- notifications;
- CI systems.

Каждая integration требует отдельного trust, credential, data ownership и external mutation analysis.

## Multi-project operation

Рассматривается после устойчивой работы одного проекта.

Необходимо определить:

- project isolation;
- shared knowledge boundaries;
- credential isolation;
- per-project Source of Truth;
- concurrency model;
- failure containment.

## Advanced user interfaces

Chat-first остаётся исходной hypothesis. Dashboard, graphical workflow и admin interfaces добавляются только при подтверждённой пользовательской потребности.

Dashboard по умолчанию read-only, пока mutation contracts не определены отдельно.

## Explicit non-prerequisites

Для первого полезного Product Runtime не обязательны:

- Control Plane;
- registry;
- database;
- RAG;
- autonomous agents;
- multi-agent runtime;
- external orchestration framework;
- Runtime Enforcement;
- SaaS platform;
- multi-project scaling.

## Disposition

Для каждого candidate используется одно состояние:

```text
OBSERVE
RESEARCH
EXPERIMENT_CANDIDATE
PROPOSAL_READY_FOR_HUMAN_REVIEW
DEFER
REJECT
```

Ни одно из этих состояний не является approval.
