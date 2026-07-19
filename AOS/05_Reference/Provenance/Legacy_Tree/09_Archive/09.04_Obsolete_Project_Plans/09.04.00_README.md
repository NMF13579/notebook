# 09.04 — Obsolete Project Plans

## Назначение

Этот объект хранит планы нового AOS, которые утратили применимость.

План может стать obsolete, даже если:

- он был качественно подготовлен;
- его assumptions были разумны;
- он не был выполнен;
- он был частично выполнен;
- его цель остаётся важной, но путь изменился.

## Причины obsolete state

План может утратить применимость из-за:

- изменения product direction;
- изменения scope;
- появления нового baseline;
- изменения architecture;
- отмены dependency;
- устранения исходной проблемы;
- обнаружения более короткого безопасного пути;
- выявленного failure mode;
- изменения sequencing;
- отсутствия прежних entry conditions;
- перехода от recovery к greenfield reconstruction.

## Что может храниться здесь

- старый implementation plan;
- прежний reconstruction plan;
- migration plan;
- rollout plan;
- validation plan;
- dependency adoption plan;
- recovery plan, если он перестал быть временно активным и не относится к закрытым временным artifacts;
- план автоматизации, отложенный из-за отсутствия product evidence.

## Что не должно храниться здесь

- active roadmap;
- approved executable Task Brief;
- current next action;
- незавершённый план без решения о прекращении;
- legacy plans из AOS-FARM;
- raw research;
- reports о фактическом выполнении.

## Plan boundary

```text
Plan output ≠ Task Brief.
Plan output ≠ approval.
Plan output ≠ execution authorization.
Obsolete plan ≠ failed implementation.
```

План нельзя считать выполненным или неудачным только на основании его архивирования.

## Минимальная запись

Для obsolete plan должна быть понятна следующая информация:

- первоначальная цель;
- assumptions;
- planned scope;
- execution status на момент прекращения;
- причина утраты применимости;
- заменивший план, если он существует;
- элементы, которые можно сохранить;
- элементы, которые нельзя переносить;
- последствия для незавершённых задач.

## Baseline sensitivity

Plan обычно привязан к:

- repository;
- branch;
- baseline;
- scope;
- dependencies;
- validation model;
- stop conditions.

Если эти bindings изменились, старый plan нельзя выполнять без повторного planning.

## Legacy boundary

Старые планы AOS-FARM являются reference material.

Их можно использовать для извлечения:

- sequencing mistakes;
- hidden dependencies;
- scope explosion patterns;
- premature automation;
- governance overload;
- recovery traps;
- missing validation boundaries.

Но они не являются готовыми plans нового проекта.

## Уроки проекта

При архивировании плана следует отдельно зафиксировать:

- что было запланировано слишком рано;
- где scope оказался слишком широким;
- какие dependencies были недооценены;
- какие этапы смешивались;
- где plan создавал видимость progress без product value;
- какой более простой путь следует использовать теперь.
