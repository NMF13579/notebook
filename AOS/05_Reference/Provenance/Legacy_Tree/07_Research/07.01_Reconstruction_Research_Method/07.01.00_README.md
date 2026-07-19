# 07.01 — Reconstruction Research Method

## Назначение

Этот документ определяет метод исследования, по которому исторические материалы, старый код, планы, отчёты и чаты преобразуются в пригодные для нового проекта знания без переноса legacy authority.

Цель метода — сохранить полезный опыт и observable behavior, но независимо пересобрать продукт, contracts и architecture.

## Основной принцип

Мы переносим не старый проект, а знания, необходимые для независимого воспроизведения полезного поведения с меньшей сложностью и без повторения известных ошибок.

## Классы утверждений

### Fact

Проверяемое утверждение о конкретном artifact или наблюдаемом результате.

Пример:

```text
В legacy repository существовал validator с таким интерфейсом.
```

Fact не доказывает, что механизм нужен новому проекту.

### Observation

Наблюдение о поведении системы, процесса или пользователя.

```text
Пользователь мог восстановить контекст задачи после перерыва.
```

Observation требует provenance и не является requirement.

### Intent

Предполагаемая проблема или цель, ради которой существовал artifact.

Intent должен быть отделён от конкретной legacy implementation.

### Lesson

Обобщённый вывод, подтверждённый одним или несколькими observations.

Lesson должен объяснять:

- что произошло;
- почему это важно;
- какое правило может предотвратить повторение;
- где вывод остаётся uncertain.

### Failure mode

Повторяемый способ, которым система создаёт неправильный, небезопасный или непропорционально сложный результат.

### Candidate

Идея, contract, capability или правило, которое может быть полезно новому проекту.

Candidate не является roadmap item, accepted requirement или execution authorization.

### Proposal

Оформленное предложение, подготовленное для отдельного human review.

### Decision

Явно принятое человеком решение, перенесённое в соответствующий active Source of Truth.

Research документ не может сам превратить candidate в decision.

## Research record

Каждый существенный вывод должен по возможности содержать:

```text
research_question:
source_material:
source_role:
observed_fact:
observable_behavior:
inferred_intent:
lesson:
failure_mode:
candidate_for_new_project:
alternatives:
unknowns:
validation_needed:
recommended_disposition:
```

`source_role` для старого AOS-FARM и AgentOS/AOS-1 всегда остаётся:

```text
READ_ONLY_REFERENCE
```

## Reconstruction test

Перед продвижением legacy идеи необходимо ответить:

1. Какую пользовательскую или инженерную проблему она решала?
2. Нужна ли эта проблема первой версии нового AOS?
3. Подтверждается ли необходимость observable behavior, а не только старой документацией?
4. Была ли legacy implementation пропорциональна проблеме?
5. Какие failure modes она создала?
6. Можно ли получить тот же outcome проще?
7. Какие dependencies действительно необходимы?
8. Как новое решение будет проверено независимо?
9. Какой active документ должен владеть принятым результатом?
10. Какое explicit human decision требуется?

Если ответы отсутствуют, disposition остаётся `KEEP_AS_RESEARCH` или `REJECT`.

## Evidence и provenance

Research должен сохранять ссылку на источник, но не путать наличие источника с истинностью вывода.

```text
Source exists ≠ claim verified.
Legacy test PASS ≠ new implementation validated.
Multiple repeated claims ≠ independent Evidence.
```

При противоречиях должны фиксироваться все значимые версии, affected decision и необходимая проверка.

## Unknown handling

`UNKNOWN` сохраняется явно.

Unknown не должен:

- превращаться в `OK`;
- скрываться общим положительным выводом;
- блокировать весь проект, если неизвестность локальна;
- использоваться как основание для автоматического переноса legacy решения.

Fail-closed применяется только внутри затронутой boundary.

## Promotion path

```text
research
→ candidate
→ bounded validation or experiment
→ proposal
→ human review
→ explicit decision
→ active document update
```

Продвижение результата не включает автоматически implementation, commit, push, merge или release.

## Rejection и archive

Материал должен быть отклонён или архивирован, если:

- он решает отсутствующую проблему;
- требует непропорциональной сложности;
- дублирует более простой механизм;
- основан только на historical authority;
- противоречит Product First;
- создаёт fake approval или hidden lifecycle mutation;
- расширяет scope без human permission;
- не может быть независимо проверен.

Отклонённый результат сохраняется как lesson, когда он помогает предотвратить повторение ошибки.
