# FTR-031 — rbac abac: короткий вход

DRAFT / производный маршрут к `2.0-candidate`. Feature остаётся DEFERRED,
requirements IN_DISCOVERY; implementation/Git authority отсутствуют. Этот brief
не владеет требованиями и не разрешает запуск. Notebook — knowledge repository.

## Предмет

Компонент внутри созданного на основе AOS приложения: администратор настраивает
доступ к существующим плоским полям, сервер применяет READ/SET_ON_CREATE/UPDATE.
Первый candidate — grants действующих ролей, ограниченные условия, один экран,
одна active model на scope, версии/откат и один реальный adapter. Он не управляет
агентами AOS, login/назначением ролей или структурой БД; FTR-019 не расширяется.

## Маршрут

1. [Core §§5–12](../docs/00_Core.md#5-иерархия-источников) — authority и WHAT/HOW.
2. [Product](../docs/01_Product.md#rbac-abac-product) — результат и границы.
3. [FTR-031](../docs/06_Features.md#ftr-031-contract) — полный candidate поведения,
   [fixture/RA-T](../docs/06_Features.md#rbac-abac-cases) и [RA-O](../docs/06_Features.md#rbac-abac-open).
4. [Architecture](../docs/02_Architecture.md#rbac-abac-contract) — host inputs,
   применение до effects/serialization, каталог, policy store, версии и recovery.
   Здесь же: direct host exchange, проверка совместимых consumers, lifecycle и
   восстановление неизвестного исхода как apply, так и прикладного write.
5. [Development](../docs/03_Development.md#rbac-abac-verification) — порядок подготовки,
   проверки, шесть UX-задач, correction/resume и общий результат.
6. [Reference](../docs/05_Reference.md#rbac-abac-source) — происхождение, границы
   внешних оснований и недоступные исходные приложения.

## Перед реализацией

Связать выбранное приложение/ТЗ с бизнес-сценариями, ролями/scopes, админ-делегацией,
catalog/defaults/security attributes и inventory всех путей к сущности. Неизвестное
не закрывать evaluator-generated expected answers. Недостающие product choices
собрать одним пакетом после чтения owners; обычный стек/парсер/storage — HOW.
Затем определить target, разрешённые effects, checks/oracles, limits и continuation
в существующей C-005/C-006. Один application binding не обещает поддержку всех ORM.
Сверить применимость §25.4 по Development §25.9 и RA-C01–05 в dossier:
внутренние C-015/C-016 AOS не обязательны, host interfaces и их проверки обязательны.
Без замены required consumer нельзя удалить компонент; закрытый endpoint
обеспечивает отказ доступа, но не заменяет требуемую функцию приложения.

## Завершение

Изменение grant → безопасный пример → apply новой revision → реальное изменение
API/UI → отказной тест. Полнота матрицы не заменяет enforcement всех объявленных
путей; неподключённый путь закрыт. Unknown effect выясняется до повторной активации,
данные/история сохраняются при отключении. Само приложение разрешает настройки
через MANAGE_FIELD_ACCESS; оно не запрашивает C-006 на каждый клик.
Runtime/security/usability и независимая validation NOT_RUN; принятие candidate
не подтверждено. Реальное пользовательское испытание отдельно от технических fixtures.
