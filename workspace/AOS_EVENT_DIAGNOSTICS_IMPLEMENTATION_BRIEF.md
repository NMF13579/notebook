# FTR-025 — минимальная диагностика событий: вход и scoped review

Дата: 2026-09-15. Статус: DRAFT / производный handoff. Implementation/Git authorization: NONE. Этот brief не выбирает реализацию FTR-025 и не меняет UNDECIDED. Источник — адаптация FTR-025-A R2; не новая фича и не отдельный normative owner.

## 1. Предмет и маршрут

Один существующий action → безопасная корреляция попытки и фактического результата → доступное пользователю диагностическое сообщение. Отказ диагностики не скрывает primary outcome и не повторяет действие. Сначала использовать подходящий report/ledger; новый writer не является заранее выбранным решением. Полная FTR-025 с incidents/lessons/regressions вне этого уточнения.

| Владелец | Что прочитать |
|---|---|
| [Product](../docs/01_Product.md#event-diagnostics-purpose) | Пользовательский результат, граница пользы и не-цели |
| [FTR-025](../docs/06_Features.md#event-diagnostics-behavior) | Trigger/I/O/flow, read-only/privacy/failures, parent acceptance и unknowns |
| [Architecture](../docs/02_Architecture.md#event-diagnostics-contract) | Корреляция, C-008/C-010/C-012/C-009 owners, C-015/C-016 mode, lifecycle |
| [Development](../docs/03_Development.md#event-diagnostics-verification) | EV-C01–12, реальный стык, проверка usefulness и границы execution |
| [Reference](../docs/05_Reference.md#event-diagnostics-source) | Взятое из R2, исключённый HOW, различия baseline и пределы доказательности |

Исполнитель получает source-bound action context, actual outcome и scope; готовит безопасный result либо limitation. Layout/utility/формат/synchronization выбирает в поддержанном profile; semantic mapping, privacy и authorization не угадывает. Один будущий bounded C-005/C-006 покрывает выбранный путь и его checks; этот документ не запускает его и не создаёт требование новых ручных заданий для каждого шага.

## 2. Авторская проверка по §25.4–25.7

Проверен только внесённый контракт диагностического события и его стыки, не весь parent FTR-025/ядро. Использованы текущие notebook owners; runtime/AOS-3 inspection в этом edit не повторялся, прежний scoped review ограничен в Reference. Статусы ниже — документальная достаточность, не C-009 runtime verdict. Independent review — NOT_RUN.

| Критерий | Итог | Основание и предел |
|---|---|---|
| К1, назначение | PASS | Product + FTR-025: один диагностический результат; полный Incident/Lesson scope не закрыт |
| К2, входы | PASS | FTR-025 input/privacy; Architecture correlation; EV-C04–06: current binding, source IDs, неполные/неподдержанные inputs |
| К3, поведение | PASS | FTR-025 шаги 1–5; EV-C01/02/07: start/terminal/denied и recording outcome различимы, crash не синтезирует результат |
| К4, ownership/интерфейсы | PASS | Architecture producer/consumer table: существующий action profile и C-016 command, без нового сервиса, raw-store access и скрытого EVENT effect |
| К5, recovery | PASS | FTR-025 failures + EV-C07/09/10/12: partial/unknown запись, channel failure, no primary replay, чтение сохранившихся observations |
| К6, критерии | PASS | EV-C01–12 содержат positive и negative oracles; всегда skip/пустой ответ не проходит. Исполнение всех сценариев NOT_RUN |
| К7, смысл | PASS | Action/attempt/outcome и код должны различать выбранный failure; raw payload запрещён, UNCLASSIFIED не доказывает root cause/usefulness |
| К8, самостоятельность | PASS | WHAT и открытый HOW разделены; дальнейший action определяется реальным gap, не форматом JSONL. Порядок работы/завершение — Development и этот brief |
| К9, интеграция | PASS | Новый состав модуля N/A: одна существующая фича. Фактические стыки проверяются EV-C12; disable/update/retained data — EV-C10; реальные E2E NOT_RUN |
| К10, согласованность | PASS | R2 HRR/UUID/path не перенесены автоматически; parent/dispositions сохранены; owners связаны ссылками, current runtime не выведен из текста |

Протокол §25.4: предмет/change и C-002 уточнены; producer/consumer/ownership и C-015/C-016 определены семантически; lifecycle §25.5 описан; scenarios дают criterion→oracle; этот brief собирает один вход. Completion диагностического пути не означает завершение всей FTR-025. Лишняя QUEUED_EVENT subscription N/A: первый путь не вводит фонового subscriber.

## 3. Замечания, репетиции и контрпримеры

Закрытые замечания исходного R2: EV-F01 — смешанный result vocabulary (Architecture + EV-C06); EV-F02 — UUID и component без ясной action correlation (тот же owner/проверка); EV-F03 — заранее выбранные path/writer/lock вместо проверенного gap (Product/Reference); EV-F04 — риск optional log failure заменить primary result либо ослабить required Evidence (FTR-025 + EV-C07/11). Это исправления документа, не наблюдённые runtime дефекты.

| Репетиция | Разрешённый следующий шаг / проверенное основание |
|---|---|
| 1. Достаточный вход | Передать событие выбранного action с exact correlation и исходным outcome; EV-C01. Positive означает полезное доступное сообщение, не просто валидные поля |
| 2. Неполный вход | Нет storage permission или безопасной correlation — scoped failure/limitation без fallback; EV-C04/06. Не запрашивать UUID у человека |
| 3. Противоречие | Несовместимые result/profile bindings не объединяются; сохранить primary outcome, ограничить запись; EV-C06/10 |
| 4. Недоступная зависимость | Diagnostic channel/storage unavailable — EV-C07, core reporting/ledger не отключены. Полная потеря каналов не выдаётся за доставленное сообщение |
| 5. Обычный дефект | Неверная projection/потерянный reason → исправление адаптера в покрытом scope и повтор EV-C05/07/12. Новый product choice нужен только при изменении смысла/границ |
| 6. Прерывание/повтор | Unknown recording outcome → owner reconciliation; не повторять primary, не переписывать history; EV-C09/12 |
| 7. Сломанный стык | Writer positive при потерянном action ref/limitation не закрывает общий путь; EV-C12 требует фактического caller/report |
| 8. Завершение | Документальная правка заканчивается scoped checks/report. Будущая реализация требует actual positive/negative/Evidence и остановки по parent predicate; full FTR-025 не объявляется завершённой |

Репетиции выполнены автором как анализ текста, не исполнение программы. Расхождений с внесённым контрактом не найдено. Попытка «две реализации»: одна меняет primary PASS на FAIL из-за optional storage, другая сохраняет PASS и показывает limitation; первая исключена EV-C07. Разные storage/serialization при одинаковых guarantees остаются свободой HOW. Попытка «плохая реализация проходит»: всегда SKIPPED или запись OPERATION_ERROR без различимого action/attempt не проходит EV-C01/usefulness; подмена реального adapter unit-вызовом writer не проходит EV-C12.

## 4. Предпосылки запуска и итог

| Открытый вход | Кто/как закрывает; влияние |
|---|---|
| Один реальный failure/action и полезное различие | Владелец задаёт цель; агент сопоставляет existing report/ledger и предлагает ограниченный путь. Без этого польза нового writer UNKNOWN |
| Exact target/action/interface/caller result и IDs | Агент наблюдает actual implementation и связывает допустимый profile; notebook не implementation target. До этого нет runtime compatibility claim |
| Diagnostic channel, read/output scope, data/retention и поддержанный storage | Определяются применимые ограничения/решения и средства host; неподтверждённая boundary запрещает соответствующую запись |
| Environment/fixtures/limits, действующая authority и continuation | Агент готовит конкретный запуск по existing workflow; отдельные полномочия и фактическая среда не выводятся из brief |

Новых решений для завершения текущего документационного scope не требуется. Изменение dispositions, обязательная observability, JSONL/path/byte constants или новый сервис не выбраны. Открытые HOW не блокируют описание; отсутствие actual target/binding/authority ограничивает запуск. Pilot, runtime/security/concurrency tests, измерение пользы и independent review — NOT_RUN.

**Итог:** описание достаточно для указанного документального уточнения и подготовки одного проверяемого подключения. Реализация и Git-доставка не выполнялись. Старый parent и остальные модули не были предметом полного повторного аудита.
