# Control Purpose and Boundaries

## Назначение

Control удерживает Product и Development в понятных человеку границах. Он предотвращает несанкционированное расширение scope, false claims, смешение технических результатов с human decisions и внешние действия без authority.

```text
понять boundary
→ проверить условие
→ разрешить или заблокировать конкретный переход
→ сохранить human authority
→ остановиться
```

## Исходная позиция

Новый AOS строится product-first. До расширения Control должны быть определены пользователь, core problem, product outcome, Product contracts, первый vertical slice и Development workflow.

Control проектируется поверх этих объектов. Он не определяет их задним числом и не переносится из AOS-FARM как готовая architecture.

## Внутри Control

- authority boundaries;
- claims, Evidence, review и decision semantics;
- unknown handling;
- stop conditions;
- protected и destructive changes;
- authorization boundaries;
- control points в реальных workflows;
- progressive evolution.

## Вне Control

- Product intent и feature design;
- implementation;
- полный Development workflow;
- автоматическое принятие решений;
- universal state machine;
- обязательный registry;
- автономный Control Plane;
- Runtime Enforcement без доказанной необходимости.

## Граница с Product

Product определяет user outcome, observable behavior, contracts и acceptance criteria. Control проверяет соблюдение согласованных границ, но не становится владельцем Product intent.

## Граница с Development

Development определяет planning, execution, validation, review, correction и handoff. Control задаёт только условия безопасных переходов и не дублирует весь workflow.

## Граница с Automation

Automation допустима после успешных manual cycles, когда процесс стабилен, входы и выходы понятны, а failure modes наблюдались.

## Граница с Runtime Enforcement

```text
documented rule ≠ enforced rule
validation ≠ prevention
process control ≠ runtime authority service
```

Runtime Enforcement вводится выборочно для повторяющихся или высокоопасных нарушений, которые можно детерминированно предотвратить.

## Критерий полезности

Control mechanism оправдан, если он уменьшает реальный риск больше, чем создаёт операционную нагрузку. Иначе он упрощается, ограничивается или удаляется.

При нескольких вариантах выбирается кратчайший безопасный путь: меньше новых сущностей, меньше постоянных artifacts, проще manual verification и легче rollback.
