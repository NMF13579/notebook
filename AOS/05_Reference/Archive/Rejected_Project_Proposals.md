# 09.03 — Rejected Project Proposals

## Назначение

Этот объект хранит предложения нового проекта, которые были рассмотрены, но не приняты.

Сохранение rejected proposals помогает:

- не повторять одни и те же обсуждения;
- понимать альтернативы;
- сохранять rationale;
- фиксировать ограничения;
- возвращаться к идее при изменении контекста;
- отличать отклонённое предложение от superseded решения.

## Критерий rejected

Proposal относится сюда, если:

- его scope был достаточно определён;
- он был рассмотрен;
- было принято решение не использовать его;
- он никогда не становился active Source of Truth;
- причина отклонения может быть объяснена.

Draft без рассмотрения не должен автоматически называться rejected.

## Что может храниться здесь

- architecture alternative;
- dependency proposal;
- feature proposal;
- governance mechanism;
- automation proposal;
- workflow variant;
- storage approach;
- interface concept;
- migration strategy;
- scaling model.

## Что не должно храниться здесь

- active proposals, ожидающие review;
- superseded decisions;
- raw ideas без анализа;
- legacy files;
- findings;
- failed validation reports;
- temporary notes;
- решения, отклонённые только агентом без human authority.

## Обязательная информация

Для rejected proposal должна быть понятна следующая информация:

- какую проблему оно пыталось решить;
- какие assumptions использовало;
- какие преимущества ожидались;
- какие риски и costs были выявлены;
- почему предложение не было принято;
- какие части идеи остаются полезными;
- при каких условиях повторное рассмотрение возможно.

## Decision boundary

```text
Proposal quality ≠ approval.
Technical feasibility ≠ product need.
PASS ≠ approval.
Evidence ≠ approval.
Agent recommendation ≠ human decision.
```

Для protected или canonical scope агент не может самостоятельно объявить proposal rejected от имени человека.

## Повторное рассмотрение

Rejected proposal может быть рассмотрено снова, если изменились:

- product requirements;
- user evidence;
- operational constraints;
- technology;
- dependencies;
- cost profile;
- safety requirements;
- scale;
- project maturity.

Повторное рассмотрение создаёт новый decision context. Старое решение не должно автоматически определять новый результат.

## Legacy boundary

AOS-FARM и AgentOS/AOS-1 могут содержать идеи, которые новый проект решает не использовать.

Такие legacy ideas остаются references или research findings. Они не становятся rejected proposals нового AOS, пока не были заново сформулированы и рассмотрены как собственное предложение нового проекта.

## Предотвращение ложной истории

Документ не должен утверждать:

- что proposal было implemented;
- что оно было active;
- что оно прошло approval;
- что оно было validated в новом проекте;

если этого не происходило.

Rejected означает только то, что предложение не было принято.
