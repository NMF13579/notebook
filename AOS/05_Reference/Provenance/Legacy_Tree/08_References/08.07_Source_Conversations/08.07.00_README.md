# Source Conversations

## Назначение

Исторические чаты, handoff summaries и рабочие обсуждения могут содержать важные решения, rationale, ошибки и незаписанные product insights.

Они используются как reference и provenance source, но не как canonical project state.

## Полезные классы информации

Из разговоров можно извлекать:

- user intent;
- product expectations;
- rejected directions;
- причины corrections;
- repeated failure patterns;
- terminology decisions;
- scope boundaries;
- unresolved questions;
- human preferences;
- historical sequence решений.

## Ограничения conversational sources

Чат может содержать:

- неполный context;
- промежуточные выводы;
- противоречащие друг другу версии;
- speculative claims;
- ошибки модели;
- решения, позднее отменённые;
- текст, который не был принят человеком;
- tool output без независимой проверки;
- устаревшее состояние repository.

Поэтому сообщение в чате не считается автоматически approval, Task Brief, Evidence, canonical rule или current state.

## Правило explicit human statements

Даже явное решение человека в чате должно быть перенесено в подходящий durable artifact, если оно должно управлять дальнейшей работой.

Conversation остаётся provenance. Durable project document становится рабочим местом правила или решения.

## Handoff summaries

Handoff summary должен:

- отделять facts от interpretations;
- указывать completed и not completed;
- сохранять unknowns;
- не симулировать approval;
- не превращать proposal в accepted direction;
- указывать точную точку продолжения;
- содержать одно следующее действие.

Handoff не должен создавать authority, которой не было в исходной работе.

## Извлечение из разговоров

Перед использованием conversational claim необходимо проверить:

1. Кто его сформулировал.
2. Было ли это предложение, решение или подтверждённый факт.
3. Не было ли оно позднее изменено.
4. Соответствует ли оно repository state.
5. Существует ли durable artifact.
6. Какова текущая применимость.

## Privacy и secrets

Перед сохранением conversation extract необходимо исключить:

- credentials;
- tokens;
- personal data без необходимости;
- private URLs;
- local secrets;
- confidential third-party information.

## Результат

Разговор используется правильно, если он помогает восстановить rationale или lesson, но active project state остаётся определённым самостоятельными документами и repository facts.
