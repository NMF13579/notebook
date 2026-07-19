# Execution, Git and Destructive Authorization

## Planning и execution

Planning создаёт предложение scope, approach, validation и stop conditions.

```text
Plan output ≠ Task Brief.
Plan output ≠ execution authorization.
```

Execution разрешается только внутри явно понятной bounded task. Read-only planning не должен блокироваться execution-grade условиями.

## Git boundaries

```text
Edit ≠ commit.
Commit ≠ push.
Push ≠ merge.
Merge ≠ release.
```

Разрешение на edit не включает Git mutation.

Commit требует отдельной authority, target-only diff, отсутствия unrelated changes, требуемой validation и проверки secrets.

Push изменяет remote state и требует отдельного разрешения, проверки remote, branch и candidate HEAD.

Merge меняет shared baseline. CI PASS или local acceptance не создают merge authorization.

Release создаёт пользовательское или операционное состояние и не выводится из merge.

## Destructive operations

К destructive относятся удаление данных, `git reset --hard`, `git clean`, force push, history rewrite, bulk replacement, destructive migration и irreversible external API action.

Destructive operation требует explicit human authorization с конкретным scope. Формулировка «исправь» не считается таким разрешением.

## Protected changes

Protected change может быть обратимым, но менять критический contract. Destructive action может не менять contract, но уничтожать state. Эти boundaries различаются и обе требуют отдельного контроля.

## Network

Network определяется отдельной boundary: цель, разрешённые services, допустимые данные, read/write mode, expected artifact и stop conditions.

Network не включается автоматически, если задачу можно выполнить локально.

## Dependencies

Установка dependency является side effect. Проверяются необходимость, source, version pinning, runtime impact, reproducibility и simpler alternatives.

Dependency не переносится только из-за legacy usage.

## Secrets

Secrets нельзя печатать, записывать в repository или reports. Возможный secret в diff является blocking finding для commit и push.

## External systems

Локальное разрешение не включает изменения GitHub, cloud, package registry, production, external database или messaging system.

Stage Report явно сообщает, какие edit, commit, push, merge, release, network и destructive actions выполнялись или не выполнялись.
