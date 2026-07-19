# Reference Catalog

## Назначение

Reference Catalog обеспечивает discoverability и traceability источников без превращения каталога в Source of Truth.

Каталог отвечает на вопросы:

- какие источники использовались;
- где они находятся;
- к какому классу относятся;
- какую потенциальную ценность имеют;
- какие ограничения известны;
- какие knowledge items из них извлечены.

## Минимальная запись

```text
Reference ID:
Title:
Source type:
Location:
Version or date:
Owner or publisher:
Access mode:
Authority in AOS: NONE
Purpose:
Known limitations:
Related knowledge items:
Related AOS documents:
Archive state:
```

## Reference ID

Reference ID является идентификатором для traceability.

Он не обозначает:

- приоритет;
- approval;
- trust level;
- readiness;
- lifecycle state;
- обязательность использования.

## Source types

Рекомендуемые классы:

- `LEGACY_REPOSITORY`;
- `HISTORICAL_DOCUMENT`;
- `CONVERSATION`;
- `EXTERNAL_PROJECT`;
- `STANDARD`;
- `OFFICIAL_DOCUMENTATION`;
- `RESEARCH_PAPER`;
- `PUBLICATION`;
- `EXPERIMENT_OUTPUT`;
- `ARCHIVED_DECISION`.

## Location handling

Каталог может содержать:

- repository и path;
- commit SHA;
- durable URL;
- local archive path;
- document identifier;
- date range разговора.

Secrets и credentials в location не допускаются.

## Versioning

Если source меняется со временем, запись должна различать:

- version, использованную при анализе;
- текущую доступную version;
- дату последней проверки.

Новый upload старого документа не делает его содержание новым.

## Traceability

Связь с новым AOS должна показывать направление происхождения:

```text
Reference
→ Knowledge Item
→ Project document
```

Обратная ссылка не даёт source authority над project document.

## Duplicate handling

Копии одного source не должны создавать иллюзию независимого подтверждения.

Каталог должен по возможности отмечать:

- original source;
- mirrors;
- derived summaries;
- excerpts;
- translations;
- superseded versions.

## Catalog maintenance

Каталог обновляется при значимых изменениях набора reference materials. Он не обязан меняться после каждого чтения source.

Отсутствие записи в каталоге не доказывает отсутствие source. Наличие записи не доказывает качество или принятие содержащихся в source идей.
