# External References

## Назначение

Этот подраздел определяет правила использования внешних repositories, frameworks, standards, specifications, статей, книг и публичных исследований.

## Классы внешних источников

- official standards и RFC;
- official product documentation;
- research papers;
- open-source projects;
- architecture articles;
- security guidance;
- UX research;
- books и long-form publications;
- benchmark и evaluation materials.

## Authority boundary

Внешний источник может обладать authority в собственной области, например specification определяет соответствующий protocol.

Однако он не получает project authority внутри AOS автоматически.

Даже обязательный внешний standard не определяет сам по себе:

- product scope;
- architecture choice;
- dependency choice;
- lifecycle;
- approval;
- Risk Profile;
- implementation authorization.

## Source quality

При оценке источника следует учитывать:

- первичность;
- дату и version;
- authorship;
- reproducibility;
- независимое подтверждение;
- применимость к текущему context;
- conflicts of interest;
- license;
- security implications;
- maintenance state.

Для technical claims предпочтительны primary sources: official documentation, standards и original research.

## Open-source projects

Чужой project может использоваться для изучения:

- UX patterns;
- architecture trade-offs;
- API contracts;
- testing strategies;
- failure handling;
- dependency choices;
- operational practices.

Наличие готового кода не является достаточным основанием для зависимости или копирования.

Перед reuse необходимо отдельно проверить:

- license compatibility;
- maintenance;
- security;
- transitive dependencies;
- portability;
- complexity cost;
- replacement strategy;
- fit с Product Contracts.

## Standards и specifications

При ссылке на standard необходимо фиксировать version или дату, когда это влияет на meaning.

Новый AOS должен явно определять, какие части standard обязательны, а какие используются только как guidance.

## Derived rules

Любое правило, полученное из внешнего source, должно быть переведено в собственный project contract или decision.

Ссылка поддерживает rationale и provenance, но не заменяет полную формулировку обязательного поведения.
