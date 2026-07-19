# 09.02 — Superseded Project Artifacts

## Назначение

Этот объект хранит artifacts нового AOS, которые ранее были active, но позднее были заменены.

Superseded artifact сохраняется для:

- восстановления истории решений;
- понимания evolution проекта;
- сравнения старого и нового contracts;
- сохранения lessons;
- предотвращения повторного внедрения устранённых ошибок;
- объяснения причин replacement.

## Критерий superseded

Artifact относится к этой категории, если:

1. он действительно использовался как active knowledge;
2. существует более новый artifact, который занял его роль;
3. replacement был выбран отдельно;
4. старый artifact больше не должен направлять текущую работу.

Сам факт наличия более новой версии файла не всегда означает superseded. Minor correction может быть обычным изменением того же artifact.

## Обязательная связь с replacement

Для каждого superseded artifact должна быть понятна связь:

```text
superseded artifact
→ replacement artifact
→ reason for replacement
→ preserved lessons
```

Если replacement отсутствует, artifact не следует автоматически классифицировать как superseded. Возможно, он является obsolete или removed without replacement.

## Что может храниться здесь

- прежняя версия project identity;
- заменённый product contract;
- старый acceptance model;
- предыдущая architecture decision;
- заменённая workflow definition;
- прежний governance rule;
- устаревшая структура документации нового проекта;
- старый interface contract, заменённый новым.

## Что не должно храниться здесь

- legacy AOS-FARM documents;
- AgentOS/AOS-1 artifacts;
- предложения, которые никогда не были приняты;
- temporary drafts;
- raw research;
- unresolved alternatives;
- artifacts, удалённые без replacement;
- копии active documents;
- implementation code без отдельной archive rationale.

Legacy artifacts принадлежат `08_References`.

## Минимальное описание archived item

Archived item должен позволять установить:

- исходный путь;
- первоначальное назначение;
- период active use;
- replacement;
- причину replacement;
- основные incompatibilities;
- lessons;
- ограничения повторного использования.

## Правило authority

```text
Superseded ≠ active.
Superseded ≠ invalid in every context.
Superseded approval ≠ current approval.
Superseded PASS ≠ current PASS.
```

Artifact сохраняет историческое значение, но теряет текущую authority.

## Повторное использование

Повторное использование возможно только как source material для нового предложения.

Нельзя:

- восстановить artifact без проверки;
- ссылаться на прежний approval как на текущий;
- копировать старые assumptions;
- считать старое validation действительным для нового baseline;
- использовать старый artifact для обхода active contract.

## Lessons-first подход

Главная ценность superseded artifact — не сам текст, а объяснение:

- что было полезно;
- что оказалось неверным;
- какие assumptions изменились;
- какое failure mode был устранён;
- почему replacement лучше соответствует текущей задаче.

## Взаимодействие с legacy material

Legacy material не становится superseded artifact нового проекта, потому что он никогда не обладал authority внутри нового AOS.

Допустимая формулировка:

```text
This new-project artifact was informed by AOS-FARM reference material.
```

Недопустимая формулировка:

```text
AOS-FARM artifact was the previous Source of Truth of the new project.
```
