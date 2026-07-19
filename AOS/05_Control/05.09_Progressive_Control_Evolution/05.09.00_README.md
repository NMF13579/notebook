# Progressive Control Evolution

## Принцип

Control развивается из наблюдаемых проблем нового проекта.

```text
Minimal Safety
→ Manual Control
→ Repeated Manual Evidence
→ Targeted Governance
→ Controlled Automation
→ Selective Runtime Enforcement
```

Следующий уровень не является автоматическим maturity milestone.

## Minimal Safety

С первого дня действуют human authority, bounded scope, unknown handling, stop conditions, destructive authorization, Git boundaries, validation separation, Source of Truth discipline и legacy-as-reference-only.

Control Plane не требуется.

## Manual Control

Используются Task Brief, preflight, bounded execution, Stage Report, independent validation, human review, отдельные Git decisions, handoff и stop.

Цель — понять реальный процесс, а не доказать зрелость.

## Repeated Manual Evidence

Несколько реальных cycles показывают повторяющиеся шаги, ошибки, human-only decisions, полезные artifacts, реальные bottlenecks и ненужный control overhead.

Один успешный cycle недостаточен для универсального framework.

## Targeted Governance

Governance добавляется точечно для повторяющейся проблемы: protected change rule, dependency decision, required review или handling blocking findings.

Она не должна сразу становиться общей platform.

## Controlled Automation

Automation допустима, когда процесс стабилен, повторяем, имеет понятные inputs/outputs, известные failure modes, измеримую выгоду и rollback.

Automation не симулирует human decisions.

## Selective Runtime Enforcement

Runtime Enforcement оправдано, если нарушение имеет существенный ущерб, process guidance недостаточно, правило детерминировано, а enforcement имеет safe fallback.

Не все Governance rules должны стать runtime rules.

## Добавление механизма

Требуются:

- observed problem;
- frequency или severity;
- affected boundary;
- expected benefit;
- minimal design;
- operational cost;
- false-positive risk;
- rollback или disable path;
- human decision.

Механизм не добавляется, если проблема гипотетическая, существует простой manual check, создаётся новый Source of Truth, нужна преждевременная infrastructure или решение копируется только из legacy.

## Удаление механизма

Control упрощается или удаляется, если underlying risk исчез, механизм не предотвращает problems, создаёт false positives, дублирует другой layer, требует постоянного recovery или блокирует независимую low-risk work.

## Целевое состояние

```text
минимальный достаточный Control
+
понятный Product
+
воспроизводимый Development
+
human authority
```

Зрелость определяется стабильным полезным результатом, а не сложностью Governance.
