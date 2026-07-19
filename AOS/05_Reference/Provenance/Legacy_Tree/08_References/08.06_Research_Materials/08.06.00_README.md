# Research Materials

## Назначение

Research Materials сохраняют исследования, comparisons, hypotheses и exploratory analysis, которые могут повлиять на будущие решения AOS.

Research помогает принимать решения. Research не является решением.

## Допустимое содержание

- problem exploration;
- architecture alternatives;
- dependency comparisons;
- UX studies;
- threat models;
- performance investigations;
- model routing research;
- automation opportunities;
- future capability ideas;
- benchmark methodology;
- lessons from external systems;
- unresolved questions.

## Граница между Research и active design

Research artifact может:

- описывать варианты;
- рекомендовать направление;
- оценивать trade-offs;
- предлагать experiment;
- выявлять risks;
- предлагать критерии решения.

Research artifact не может сам по себе:

- выбирать active architecture;
- изменять Source of Truth;
- утверждать dependency;
- назначать Risk Profile;
- давать approval;
- разрешать implementation;
- изменять lifecycle;
- объявлять readiness.

## Hypothesis discipline

Каждая существенная hypothesis должна по возможности содержать:

- вопрос;
- rationale;
- assumptions;
- expected evidence;
- falsification condition;
- risks;
- current uncertainty;
- потенциальное место применения.

## Research debt

Research становится долгом, если:

- conclusions используются без проверки;
- старые comparisons считаются актуальными без revision;
- recommendation незаметно превращается в requirement;
- uncertainty удаляется из пересказа;
- source provenance теряется;
- research копируется в canonical document без human decision.

## Promotion path

```text
Research question
→ Sources
→ Analysis
→ Findings
→ Proposed decision
→ Human review
→ Project decision
→ Canonical update
```

Каждый переход должен быть явным. Завершённое исследование не означает принятого решения.

## Historical research

Superseded research сохраняется, если оно объясняет:

- почему был выбран текущий путь;
- какие alternatives уже рассматривались;
- какие assumptions изменились;
- какие ошибки не следует повторять.

После утраты активной ценности material переносится в Historical Archive, а не удаляется без причины.
