# FTR-032 — Repository UX Pages: короткий вход

Статус: DRAFT, производный маршрут. FTR-032 остаётся DEFERRED; этот brief не
владеет требованиями и не даёт implementation/Git authority. Notebook — knowledge
repository, implementation target не назначен. Модель источника R2 не является
принятым ТЗ; FTR-027 остаётся неактивной заглушкой.

## Предмет и маршрут

Один модуль FTR-032: owning HTML/embedded YAML → согласованные Human/Engineering
Surface → понятный review/correction → внешнее решение → context exact задачи.
Состав не включает новый Workbench, domain Design, backend или approval service.

1. [Core §§5–12](../docs/00_Core.md#5-иерархия-источников) — authority и WHAT/HOW.
2. [Product: UX-путь](../docs/01_Product.md#ux-pages-product) — результат/границы.
3. [FTR-032](../docs/06_Features.md#ftr-032-contract) — поведение, потребители,
   ограничения симуляции и [DS-T01–22](../docs/06_Features.md#ux-pages-cases).
4. [Architecture](../docs/02_Architecture.md#ux-pages-contract) — owners,
   full-file identity, snapshot, preview, C-011/C-012/C-015/C-016 и recovery.
5. [Development](../docs/03_Development.md#ux-pages-verification) — проверки/пилот;
   общий цикл §10/§25.2, содержательная проверка §25.7 остаются владельцами процесса.
6. [Reference](../docs/05_Reference.md#ux-pages-r2-source) — источник R2, адаптации
   и недоступные исходные приложения; не восстанавливать их схемы по памяти.

## Перед dependent implementation

Сверить [DS-O01–05](../docs/06_Features.md#ux-pages-open-decisions): target/authority,
путь записи решения, supported input/runtime contract, preview environment и
конкретный пилот. Существующие ответы не спрашивать повторно; material UX/данные
не угадывать. Затем один C-005/C-006 для выбранного достаточного scope, consumers,
checks/oracles, outputs и resource/resume limits. Сейчас запуск не поручен.

Не ждать собственного viewer для начала сборки; сначала обязательные contracts и
реальные capabilities внешнего host, затем implementation и declared integrations.
Layout, parser/library, renderer и механизм синхронизации — HOW в пределах owners.
Потерянное подтверждение требует reconciliation; новая сессия не обнуляет ledger.

## Граница результата

Техническое завершение определяется выбранными критериями частей и реальных стыков
по Development, не badge/index или суммой локальных PASS. FRONTEND pack не требует
ещё не созданного backend; INTEGRATION требует достаточных API/error/permission refs.
Отсутствие preview не блокирует безопасный разбор, но не закрывает interactive path.
Usability pilot, human acceptance, runtime и независимый review сейчас NOT_RUN /
NOT_REQUESTED; документационная репетиция не является их доказательством.
