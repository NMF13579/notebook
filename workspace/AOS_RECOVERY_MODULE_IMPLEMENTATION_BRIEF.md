# Recovery / FTR-033 — короткий вход

DRAFT, производный маршрут к candidate v0.2 от 2026-09-15. FTR-033 остаётся
DEFERRED / IN_DISCOVERY. Это не owner требований, принятие контракта или
implementation/Git authority. Notebook — knowledge repository.

## Что подготовить

Один existing project + цель → bounded static Assessment с Evidence/UNKNOWN →
human direction/next objective → MMB → один next PLAN → receipt exact revision.
Source/VCS не менять, target code не запускать. Output только в разрешённом
external workspace. Install в source не обязателен. Подготовка handoff не означает
его получение, исправление проекта или разрешение на ремонт.

## Маршрут владельцев

1. [Core §§5–10](../docs/00_Core.md#5-иерархия-источников): source precedence,
   authority и safety. Reference default rewrite не команда переписать target.
2. [Product](../docs/01_Product.md#recovery-product): результат/граница версии.
3. [FTR-033](../docs/06_Features.md#ftr-033-contract): поведение, состояния,
   [REC cases](../docs/06_Features.md#recovery-cases), [открытые решения](../docs/06_Features.md#recovery-open).
4. [Architecture](../docs/02_Architecture.md#recovery-contract): records, origin,
   subject, C-015/C-016, sidecar и lifecycle; [MMB](../docs/02_Architecture.md#recovery-mmb)
   имеет единственное определение здесь.
5. [Development](../docs/03_Development.md#recovery-verification): protocol mapping,
   autonomous build, checks/oracles, pilot/метрики, correction/resume/stop.
6. [Reference](../docs/05_Reference.md#recovery-source): provenance/пределы исходника.

## Перед зависимой реализацией

Нужны exact принятый scope и один implementation profile: compatible core/record
versions, реальные safe reader/storage/C-011/receiver capabilities, OS/filesystem
support, target, data/output boundary, checks, finite limits и continuation.
Подготовить parent task/authority отдельно. Schema и test adapters создаются
внутри разрешённой реализации до их применения; отсутствующая реализация не
требует написать её заранее ради плана. Parser/layout/serialization — HOW.

Pilot project/budget, желаемое/protected business behavior и scope decisions
не угадываются. Уже принятый ответ сначала ищется у owner; новые material choices
собираются одним пакетом. Отсутствие runtime adapters не скрывается manual export.

## Общий результат и продолжение

REC-POS плюс отрицательные/compatibility checks на exact subject и реальных стыках;
пакет доступен receiver, C-012 — единственный ongoing state owner, Recovery records
historical. Lost save/receipt сначала reconciled, затем допустимый retry; старые
decisions/permissions не переносятся на изменённый subject. Required consumer без
замены блокирует remove, данные не удаляются вместе с implementation.
Ремонт, установка, executable observation и Git — отдельные дальнейшие задачи.
Runtime/pilot/usability/independent validation NOT_RUN; новая стадия не запускается
по наличию этого brief.

При compatibility review отдельно проверить REC-C04–07: read-only PLAN не
dispatches effectful save; queued external persistence имеет собственный
допустимый service task/stage/authority, документальный путь не доказывает runtime.
C-011 связывает выбранную стратегию и next objective, receipt — exact пакет и
required inputs принимающей стороны; ни receipt, ни повтор доставки не запускают
и не создают автоматически следующую задачу. Source и output base проверяются отдельно.
