# Historical Archive

## Назначение

Historical Archive сохраняет superseded, rejected, obsolete и no-longer-active reference artifacts, которые могут быть полезны для traceability и предотвращения повторения ошибок.

Archive не является active workspace.

## Что переносится в Archive

- прежние планы;
- rejected architecture proposals;
- superseded research;
- obsolete terminology;
- old handoff packages;
- закрытые recovery materials;
- historical reference indexes;
- старые comparisons;
- deprecated process descriptions;
- документы, заменённые новой самостоятельной формулировкой.

## Причины сохранения

Artifact имеет смысл сохранить, если он помогает понять:

- почему решение было изменено;
- какие assumptions оказались неверными;
- какие failure modes наблюдались;
- какие alternatives уже исследовались;
- как сформировался current contract;
- какие ошибки не следует повторять.

## Что Archive не делает

Archive не определяет:

- current project state;
- active scope;
- architecture;
- Source of Truth;
- approval;
- lifecycle;
- Risk Profile;
- execution authorization;
- implementation readiness.

## Запрет silent revival

Archived artifact нельзя возвращать в active use только потому, что он существует или когда-то был accepted.

Возврат требует:

1. нового анализа применимости;
2. проверки current constraints;
3. выявления conflicts;
4. новой формулировки;
5. human decision;
6. обновления соответствующего active document.

## Archive и удаление

Archive не должен становиться бесконечным складом файлов.

Материал может быть удалён отдельным explicit human decision, если:

- он не имеет traceability value;
- содержит чувствительные данные;
- нарушает license или retention requirements;
- является точным duplicate;
- его сохранение создаёт риск ошибочного использования.

Destructive deletion не выполняется агентом без explicit human authorization.

## Читаемость

Archived material должен быть явно отделён от active documents. Название, расположение и surrounding context не должны создавать впечатление, что artifact продолжает действовать.

## Главный принцип

Archive сохраняет память проекта, но не управляет настоящим проекта.
