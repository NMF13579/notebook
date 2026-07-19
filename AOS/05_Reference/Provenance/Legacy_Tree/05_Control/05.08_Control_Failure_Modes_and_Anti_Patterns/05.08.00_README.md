# Control Failure Modes and Anti-Patterns

## Назначение

Документ сохраняет опыт legacy AOS как предупреждения, а не как architecture нового проекта.

## Governance before Product

**Ошибка:** Governance и control infrastructure создаются раньше полезного Product Runtime.

**Последствие:** readiness заменяет пользовательский progress.

**Правило:** сначала Product definition, first vertical slice и manual validation.

## Self-governing Control Plane

**Ошибка:** незавершённый Control Plane становится prerequisite собственной разработки.

**Последствие:** циклическая блокировка.

**Правило:** до доказанной необходимости используются manual workflow и обычные repository tools.

## Execution-grade gates for planning

**Ошибка:** read-only planning блокируется execution, environment или merge requirements.

**Правило:** такие условия применяются только перед соответствующим side effect.

## Permanent recovery

**Ошибка:** recovery создаёт новые plans и gates, но не уменьшает uncertainty.

**Правило:** recovery имеет bounded object, exit criterion, stop condition и не заменяет Product work.

## Formal readiness replacing delivery

**Ошибка:** PASS, reports и packages трактуются как product value.

**Правило:** progress измеряется observable behavior.

## Distributed Sources of Truth

**Ошибка:** current state одновременно хранится в repository, chats, reports и legacy documents.

**Правило:** один fact class — один canonical owner.

## Excessive approval granularity

**Ошибка:** человек подтверждает каждую обратимую операцию.

**Правило:** human checkpoints концентрируются на scope, authority, protected state и существенном риске.

## Approval bundling

**Ошибка:** acceptance одновременно трактуется как commit, push, merge и release authorization.

**Правило:** независимые side effects разделяются.

## Evidence inflation

**Ошибка:** тяжёлый Evidence package обязателен для низкорисковой работы.

**Правило:** Evidence пропорционально риску и конкретному claim.

## Stage fragmentation

**Ошибка:** работа делится на стадии без самостоятельного output или risk boundary.

**Правило:** отдельная стадия нужна только при отдельной роли, результате и stop point.

## Mixed validation and correction

**Ошибка:** validator исправляет найденные проблемы.

**Правило:** validation read-only; correction — отдельная task.

## Automatic retry loops

**Ошибка:** failure автоматически запускает correction или следующий этап.

**Правило:** report и stop.

## Automation before understanding

**Ошибка:** автоматизируется процесс до нескольких успешных manual cycles.

**Правило:** сначала наблюдение стабильного процесса.

## Legacy topology copying

**Ошибка:** новые folders, registries, schemas и services копируются из AOS-FARM.

**Правило:** переносится independently justified lesson или contract, а implementation проектируется заново.

## Control as product

**Ошибка:** plans, approvals, reports и registries становятся главным output.

**Правило:** Control остаётся минимальным помощником Product и Development.
