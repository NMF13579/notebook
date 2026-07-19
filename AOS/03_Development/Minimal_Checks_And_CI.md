# Minimal Checks and CI

Назначение

Этот документ определяет минимальные технические проверки и начальную модель Continuous Integration для проекта AOS.

Minimal Checks and CI нужны для того, чтобы:

* обнаруживать очевидные ошибки до принятия изменения;
* проверять, что задача не вышла за разрешённый scope;
* запускать одинаковые базовые проверки локально и в CI;
* предотвращать ложный положительный результат;
* отличать выполненную проверку от невыполненной;
* сохранять воспроизводимый технический baseline;
* не допускать случайного повреждения документации или кода;
* подготовить основу для первого manual development workflow;
* не превращать bootstrap в сложный delivery pipeline.

Проверки подтверждают только те условия, которые они фактически проверяют.

Они не принимают решения за человека.

⸻

Основная граница

Check PASS
не означает
Task approval

Обязательные различия:

PASS не означает approval.
CI PASS не означает approval.
Evidence не означает approval.
Все обязательные checks PASS не означают merge authorization.
Merge не означает release.
UNKNOWN не означает OK.
NOT_RUN не означает PASS.
BLOCKED не означает PASS.

CI является техническим механизмом проверки.

CI не является:

* human reviewer;
* approval authority;
* architecture authority;
* Product Owner;
* Risk Profile authority;
* merge authority по умолчанию;
* release authority;
* доказательством полной готовности продукта.

⸻

Главная цель минимальных проверок

Минимальный набор checks должен отвечать на несколько конкретных вопросов:

1. Изменены ли только ожидаемые файлы?
2. Не повреждена ли базовая структура artifacts?
3. Проходит ли заявленная техническая validation?
4. Не скрыты ли failed, unknown или невыполненные проверки?
5. Можно ли воспроизвести проверку локально?
6. Соответствует ли результат Task Brief?
7. Не появился ли очевидный regression?
8. Не попал ли в repository запрещённый или временный material?

Checks не должны пытаться доказать всё сразу.

⸻

Local-first

Основные проверки сначала должны работать локально.

Правильная последовательность:

локальная проверка
→ локальное исправление в рамках execution
→ независимая validation при необходимости
→ push
→ повтор тех же checks в CI

CI не должен быть единственным местом, где можно узнать, работает ли изменение.

Пользователь или агент должны иметь возможность запустить основные checks до push.

Это сокращает:

* медленные feedback loops;
* ненужные remote runs;
* расход CI resources;
* зависимость от network;
* количество исправляющих commits;
* расхождение между local и remote environments.

⸻

Минимальность

Каждый check должен иметь ясное назначение.

Не следует добавлять tool или pipeline stage только потому, что он обычно встречается в других проектах.

Новый check оправдан, если:

* он проверяет значимый contract;
* ошибка уже наблюдалась или имеет существенную цену;
* результат однозначен;
* check воспроизводим;
* false positives управляемы;
* check можно запустить локально или объяснить, почему это невозможно;
* его failure приводит к понятному действию.

⸻

Классы проверок

В AOS могут использоваться следующие классы checks:

repository checks
documentation checks
structure checks
syntax checks
unit tests
integration tests
acceptance checks
type checks
lint checks
security checks
dependency checks
build checks
package checks
manual checks

Не все классы обязательны с первого дня.

Набор checks расширяется вместе с реальным Product Runtime.

⸻

Состояния проверки

Каждая существенная проверка должна иметь одно из понятных состояний:

PASS
FAIL
UNKNOWN
NOT_RUN
BLOCKED

PASS

Проверка была фактически выполнена, завершилась ожидаемым образом и подтвердила проверяемое условие.

FAIL

Проверка была выполнена и показала несоответствие ожидаемому условию.

UNKNOWN

Данных недостаточно, чтобы сделать вывод.

NOT_RUN

Проверка не запускалась.

BLOCKED

Проверка не могла быть выполнена из-за конкретного blocker.

Нельзя объединять эти состояния в общий оптимистичный status.

⸻

Правило против false PASS

Check не может считаться PASS, если:

* команда не запускалась;
* executable отсутствовал;
* test discovery нашёл ноль tests, хотя tests ожидались;
* часть обязательного набора была пропущена;
* process завершился раньше проверки;
* output не удалось интерпретировать;
* проверка выполнялась не на ожидаемом baseline;
* использовался другой target;
* command завершилась с ignored failure;
* shell pipeline скрыл exit code;
* required files отсутствовали;
* result был взят из старого run.

В таких случаях используется:

FAIL
UNKNOWN
NOT_RUN
или
BLOCKED

в зависимости от фактической причины.

⸻

Zero tests не означает PASS

Если test suite должен существовать, но runner сообщает:

0 tests collected

это не должно автоматически считаться успешной validation.

Возможные причины:

* неправильная directory;
* сломанный discovery;
* tests отсутствуют;
* неверная configuration;
* tests исключены filter;
* package установлен неправильно.

Такой результат должен быть классифицирован как FAIL, UNKNOWN или BLOCKED, а не как обычный PASS.

⸻

Required и advisory checks

Checks могут быть:

Required

Без успешного результата нельзя продолжать затронутое техническое действие.

Advisory

Результат предоставляет дополнительную информацию, но не блокирует обычную работу автоматически.

Пример:

syntax check
→ required
experimental compatibility check
→ advisory
coverage report без принятого threshold
→ advisory

Статус advisory не позволяет скрывать failure.

Он означает только, что соответствующее решение пока не использует этот check как blocking gate.

⸻

Определение blocking checks

Check становится blocking, если:

* он защищает принятый contract;
* failure означает нарушение expected behavior;
* failure создаёт существенный safety risk;
* без него невозможно проверить результат Task Brief;
* он предотвращает повреждение repository;
* он требуется для конкретного protected действия;
* он принят как branch protection requirement.

Агент не должен самостоятельно превращать advisory check в обязательный policy gate или, наоборот, ослаблять required check.

⸻

Проверки текущего документационного этапа

На текущем этапе AOS в первую очередь собирает документационный слой.

Минимальный набор для изменения одного Markdown-документа:

git status --short
git diff --check
git diff -- <target-file>

Дополнительно проверяется вручную:

* сохранены Markdown headings;
* code fences закрыты;
* inline code не повреждён;
* изменён только target file;
* отсутствуют случайные YAML metadata и служебные статусы, если они не предусмотрены;
* документ не выдаёт skeleton за implementation;
* документ не создаёт approval или authorization claim;
* соседние artifacts не изменены.

⸻

git diff --check

Команда:

git diff --check

выявляет некоторые whitespace errors.

Она может обнаружить:

* trailing whitespace;
* конфликтные whitespace markers;
* некоторые malformed diff conditions.

Она не проверяет:

* правильность смысла;
* корректность Markdown hierarchy;
* актуальность links;
* consistency с другими документами;
* отсутствие ложных claims;
* соответствие Product Vision;
* human acceptance.

Поэтому git diff --check: PASS является узким техническим результатом.

⸻

Target-only diff

Для bounded task необходимо проверять конкретный target:

git diff -- <target-path>

Цель:

* увидеть точное изменение;
* обнаружить accidental deletion;
* проверить Markdown;
* убедиться, что содержание не сократилось неожиданно;
* сравнить результат с Task Brief.

Если одновременно существуют unrelated changes, они должны быть видимыми, но не включаться в текущий result claim.

⸻

Проверка Markdown

На раннем этапе проверка Markdown может быть ручной.

Необходимо убедиться, что:

* существует один основной title;
* heading hierarchy последовательна;
* code fences сбалансированы;
* списки отображаются корректно;
* inline code сохранён;
* paths и commands визуально различимы;
* нет случайного plain-text flattening;
* документ читается без знания истории чата.

Markdown linter можно добавить позже, если он решает реальную повторяющуюся проблему и не создаёт массовый formatting diff.

⸻

Проверка ссылок

Link checker становится полезным после появления значимого количества внутренних links.

Он должен проверять:

* существование relative target;
* корректность anchors;
* отсутствие ссылок на удалённые files;
* отсутствие path drift после rename.

External links могут требовать network и должны проверяться отдельно.

External link failure не всегда означает дефект проекта:

* сайт может быть временно недоступен;
* access может быть ограничен;
* URL может требовать authentication.

Поэтому local и external link checks следует разделять.

⸻

Проверка структуры документации

После стабилизации skeleton можно добавить thin structure check.

Он может проверять:

* разрешённые top-level sections;
* уникальность номеров;
* наличие обязательных entry files;
* naming convention;
* отсутствие files в запрещённых temporary paths;
* существование targets из `AOS/MANIFEST.md`;
* отсутствие duplicate numbering;
* отсутствие случайных backup files.

Structure check не должен определять содержание документа или принимать architectural decisions.

⸻

Проверка canonical manifest

CI может проверять:

`AOS/MANIFEST.md` соответствует canonical files

Предпочтительный подход:

read manifest
→ resolve targets and provenance
→ fail on missing or duplicate ownership

CI не должен скрыто переписывать manifest или commit его обратно.

Manifest остаётся canonical ownership map, а не generated normative content.

⸻

Проверка temporary files

Checks могут выявлять попадание в tracked content файлов вроде:

.aos-tmp/
*.log
*.tmp
*.bak
draft_latest.md
final_v2.md
.DS_Store
.pytest_cache/
.venv/

Но check не должен автоматически удалять их.

При обнаружении:

report
→ одно действие
→ stop

Destructive cleanup без разрешения запрещён.

⸻

Проверка secrets

До появления внешних integrations достаточно базового контроля:

* .env не отслеживается;
* реальные API keys не находятся в examples;
* tokens не попадают в reports;
* credentials не входят в fixtures;
* logs не содержат secrets.

Автоматический secret scanner может быть добавлен позже.

Результат scanner не гарантирует отсутствие всех secrets.

Он только проверяет известные patterns и heuristics.

⸻

Первый набор checks после появления кода

После реализации первого Product Runtime vertical slice минимальный набор может включать:

package installation
import or startup check
unit tests
first acceptance scenario
git diff --check

Возможная Python-команда:

python -m pytest -q

Точный набор определяется Task Brief и Architecture Contract первого vertical slice.

До появления code package нельзя объявлять конкретную test command canonical.

⸻

Unit tests

Unit tests проверяют локальное поведение ограниченных components.

Они полезны для:

* deterministic functions;
* validation logic;
* parsing;
* path handling;
* state transitions;
* error handling.

Unit tests не доказывают:

* полный пользовательский workflow;
* корректность integration;
* production readiness;
* human acceptance;
* отсутствие всех defects.

⸻

Integration tests

Integration tests проверяют взаимодействие нескольких components или внешней системы.

Они добавляются, когда появляется реальная integration boundary.

Не следует создавать фиктивную integration architecture только ради наличия integration tests.

Integration check должен ясно указывать:

* какие components участвуют;
* требуется ли network;
* какие credentials нужны;
* какие external writes выполняются;
* как очищается test state;
* что происходит при недоступности service.

⸻

Acceptance checks

Acceptance check подтверждает observable user behavior.

Он должен быть связан с Product Contract.

Пример:

пользователь передаёт ограниченную задачу
→ AOS формирует понятный Task Brief
→ результат содержит scope, validation и одно следующее действие

Acceptance checks важнее формальной проверки наличия внутренних classes или directories.

⸻

Negative tests

AOS особенно нуждается в negative tests для safety boundaries.

Они должны проверять, что система отклоняет:

* fake approval;
* неизвестный status;
* invalid scope;
* allowed/forbidden overlap;
* path traversal;
* malformed artifact;
* empty required document;
* неправильный baseline;
* NOT_RUN, выданный за PASS;
* unauthorized action;
* invalid human decision type;
* unsupported file type.

Negative test должен подтверждать fail-closed behavior конкретной boundary.

⸻

Regression tests

Каждый исправленный значимый defect желательно закреплять regression test.

Regression test должен:

* воспроизводить исходную проблему;
* падать до исправления;
* проходить после исправления;
* проверять contract, а не случайную implementation detail.

Не каждая текстовая ошибка требует отдельного automated test.

⸻

Coverage

Coverage может помогать находить непроверенные участки кода.

Но:

высокий coverage
не означает
высокое качество tests

На первом vertical slice coverage report может быть advisory.

Coverage threshold следует вводить только после понимания:

* какой code считается product-critical;
* какие paths исключаются;
* как threshold влияет на workflow;
* не стимулирует ли он бессмысленные tests.

Coverage PASS не означает product acceptance.

⸻

Lint

Lint проверяет определённые классы style и static errors.

Он может быть полезен для:

* unused imports;
* очевидных syntax patterns;
* consistency;
* потенциальных defects.

Lint не должен:

* массово переписывать unrelated files;
* заменять tests;
* считаться behavioral validation;
* автоматически менять code в validation stage.

Auto-fix является write operation и выполняется только в execution scope.

⸻

Type checking

Type checker может стать required check для стабилизированных typed interfaces.

До этого момента он может быть advisory или отсутствовать.

Если используется partial typing, CI должен проверять только заявленный scope и не создавать ложный claim о полной типовой безопасности проекта.

⸻

Build check

После появления distributable package CI может проверять:

source distribution
wheel
clean installation
startup

Editable local install недостаточен для доказательства корректности package artifact.

Build check добавляется ближе к распространению продукта, а не в documentation bootstrap.

⸻

Dependency check

Dependency checks могут включать:

* корректность manifest;
* отсутствие conflicting declarations;
* installation;
* known vulnerability scan;
* license check;
* lock consistency.

Security advisory scanner не гарантирует отсутствие vulnerabilities.

Результат зависит от:

* базы advisories;
* версии scanner;
* dependency resolution;
* transitive graph;
* даты проверки.

Поэтому scan result должен сохранять дату и границы.

⸻

Manual checks

Некоторые проверки остаются ручными:

* понятность UX;
* корректность Product Vision;
* соответствие architecture intent;
* качество human-facing report;
* удобство session resume;
* понятность одного следующего действия.

Manual check должен быть явно указан.

Если он не выполнялся:

NOT_RUN

Нельзя считать его покрытым unit tests автоматически.

⸻

CI назначение

Initial CI должен:

* получить точный repository state;
* установить минимальный toolchain;
* установить declared dependencies;
* запустить основной technical validation path;
* вернуть понятный exit status;
* сохранить короткий log;
* не изменять repository;
* не использовать secrets без необходимости;
* не выполнять commit, push, merge или release.

⸻

Минимальный CI pipeline

После появления code package базовый pipeline может выглядеть так:

checkout
→ setup runtime
→ install dependencies
→ run technical checks
→ report result

Пример для будущего Python baseline:

checkout repository
→ setup accepted Python version
→ install test dependencies
→ run pytest

Это пример класса pipeline, а не готовая конфигурация до выбора toolchain.

⸻

CI для текущего документационного этапа

До появления implementation CI может ограничиваться:

* проверкой Git whitespace;
* structure check;
* internal link check;
* naming check;
* lightweight document contract check.

Но даже эти checks не следует добавлять до стабилизации структуры.

На раннем ручном этапе локальный diff review может быть достаточным.

CI не нужен только ради наличия badge.

⸻

CI permissions

CI должен использовать минимальные permissions.

Для обычной validation достаточно read-only доступа к repository content.

Базовый принцип:

contents: read

CI не должен получать write permissions, если pipeline только проверяет изменения.

Дополнительные permissions добавляются отдельно и только для конкретной необходимости.

⸻

Pinned CI actions

Third-party CI actions являются исполняемыми dependencies.

Для устойчивого pipeline предпочтительно фиксировать actions на точный commit SHA.

Это уменьшает риск неожиданного изменения action по mutable tag.

При pinning необходимо сохранять понятную информацию о версии, чтобы updates оставались управляемыми.

Pinned action не становится автоматически доверенной навсегда.

Её всё равно следует обновлять и проверять.

⸻

CI и network

CI обычно требует network для:

* checkout;
* runtime setup;
* dependency installation;
* загрузки actions.

Но application tests не должны использовать произвольный network без явной необходимости.

External integration tests следует отделять от basic pipeline.

Basic CI не должен:

* обращаться к production API;
* отправлять пользовательские данные;
* выполнять внешние mutations;
* использовать production credentials.

⸻

CI и secrets

Initial validation pipeline должен по возможности работать без secrets.

Если secrets необходимы для отдельной integration:

* используется отдельный job;
* secret доступен только этому job;
* forked contributions не получают secret автоматически;
* secret не выводится в log;
* failure не раскрывает значение;
* внешние writes ограничены или отсутствуют.

Добавление CI secret является отдельным controlled change.

⸻

Local и CI parity

Основная CI command должна совпадать с локальной.

Плохо:

локально запускается один набор tests,
в CI — скрытый другой workflow.

Хорошо:

local:
python -m pytest -q
CI:
python -m pytest -q

Дополнительные CI-only checks допустимы, если причина ясна.

⸻

Runtime version parity

Local development и CI должны использовать совместимую принятую runtime version.

Если CI использует Python 3.11, а локальная документация допускает только неопределённый Python 3, возникает drift.

Version matrix добавляется только после появления обязательства поддерживать несколько runtime versions.

До этого лучше:

одна основная версия
→ локально
→ в CI

⸻

CI output

CI output должен быть:

* достаточно подробным для диагностики;
* не перегруженным;
* без secrets;
* с понятным failed command;
* с сохранённым exit code;
* с различием между failed и skipped checks.

Не следует скрывать failure за общим report generator, который всегда возвращает exit code 0.

⸻

Exit codes

Blocking technical failure должен приводить к ненулевому process exit code.

Команда не должна возвращать 0, если:

* обязательная validation провалилась;
* input invalid;
* required file отсутствует;
* internal exception не обработан;
* expected tests не были обнаружены;
* result нельзя проверить.

Human review requirement сам по себе не всегда означает технический process failure.

Технический exit status и human decision status должны быть разделены.

⸻

Skipped checks

Пропущенная проверка должна быть видима.

Допустимые причины:

* platform не поддерживается;
* optional integration не настроена;
* test требует отсутствующий external service;
* job не относится к изменённому scope.

Недопустимо использовать skip, чтобы скрыть устойчиво failing test.

Для required check skip обычно означает NOT_RUN, UNKNOWN или BLOCKED, а не PASS.

⸻

Conditional checks

Path-based conditional CI может сократить время.

Например:

изменена только документация
→ не запускать тяжёлый integration suite

Но conditional logic должна быть простой и проверяемой.

Нельзя пропустить required check из-за ошибочного path filter.

До появления большого test suite условная сложность обычно не нужна.

⸻

Documentation-only changes

После появления code pipeline документационные изменения всё равно могут запускать:

* structure check;
* link check;
* Markdown check;
* forbidden-claim check;
* lightweight repository tests.

Полный runtime suite может запускаться, если documentation влияет на generated artifacts, examples или user commands.

Policy должна определяться фактической dependency, а не только extension .md.

⸻

CI artifacts

CI может сохранять:

* test reports;
* coverage reports;
* build packages;
* logs;
* screenshots.

CI artifact является Evidence или derived output.

Он не является:

* approval;
* Source of Truth;
* human decision;
* release authorization.

Artifact retention должна соответствовать реальной необходимости.

⸻

CI cache

Cache ускоряет installation и build.

Cache является disposable.

Cache не должен влиять на correctness.

Периодически pipeline должен быть способен пройти без cache.

Cache key должен учитывать:

* runtime version;
* dependency manifest;
* lock file;
* relevant configuration.

Stale cache failure не должен приводить к созданию recovery lifecycle.

⸻

Flaky tests

Flaky test не должен автоматически перезапускаться до зелёного результата без фиксации проблемы.

Автоматический retry может скрыть nondeterminism.

Если retry используется, CI должен показывать:

* первоначальный failure;
* количество attempts;
* итоговый результат;
* что test является потенциально flaky.

Repeated intermittent failure должен стать отдельным finding.

⸻

Retry policy

На минимальном этапе предпочтительно:

один deterministic run

Retry допустим только для явно нестабильной external integration, где transient failure является известной характеристикой.

Retry не должен применяться к:

* unit tests;
* schema validation;
* repository structure;
* deterministic safety checks;
* invalid input handling.

⸻

Failure behavior

При failed required check:

1. CI отмечает job как failed;
2. failed command видима;
3. следующий write-stage не начинается автоматически;
4. merge не выполняется автоматически;
5. формируется технический result;
6. исправление выполняется отдельной execution task.

CI не должен изменять code, создавать correction commit или перезапускать development agent автоматически.

⸻

CI и automatic correction

Initial CI не должно:

* запускать coding agent;
* исправлять formatting;
* переписывать generated files;
* обновлять dependencies;
* создавать commits;
* открывать pull request с исправлением;
* менять status artifacts.

Такая automation возможна только позднее после принятого contract и manual cycles.

⸻

CI и merge

CI PASS может быть необходимым условием merge.

Но этого недостаточно.

Merge может дополнительно требовать:

* human review;
* отсутствие blocking findings;
* соответствие exact head;
* разрешённый merge method;
* protected branch policy;
* отдельное merge authorization.

Обязательное правило:

CI PASS не означает merge approval.

⸻

CI и release

Release pipeline появляется позже.

Даже если build и tests проходят:

CI PASS
не означает
release authorization

Release требует отдельного решения, version scope и release validation.

⸻

Branch protection

Branch protection можно добавить после стабилизации collaboration workflow.

Для main могут потребоваться:

* запрет force push;
* required checks;
* human review;
* запрет unresolved conversations;
* запрет merge при conflicts.

На раннем личном documentation repository branch protection может быть отложена.

Отсутствие branch protection должно быть известно, но не требует немедленного создания полного Governance.

⸻

Pull requests

Pull request полезен для:

* review;
* обсуждения;
* запуска CI;
* отображения diff;
* отделения feature branch.

PR не является approval сам по себе.

Open PR, green checks или отсутствие комментариев не означают human acceptance.

⸻

Check naming

Названия checks должны объяснять назначение.

Хорошо:

documentation-structure
unit-tests
first-vertical-slice
package-build
dependency-audit

Плохо:

gate-1
validation-final
everything-pass
quality

Название не должно преувеличивать проверяемый scope.

⸻

Один основной validation command

На каждом этапе должен существовать один основной entry point для базовой validation.

На документационном этапе это может быть documented sequence:

git diff --check
git diff -- <target-path>

После появления package:

python -m pytest -q

Позже может появиться unified command:

python -m aos validate

Но unified validator добавляется только после стабилизации нескольких реальных checks.

⸻

Unified validator

Future unified validator должен:

* запускать известные deterministic checks;
* сохранять exit codes;
* показывать NOT_RUN;
* различать required и advisory;
* не создавать approval;
* не исправлять artifacts;
* не включать network скрыто;
* не начинать следующий этап.

Validator не должен превращаться в полный Control Plane.

⸻

Check registry

На раннем этапе отдельный registry checks не нужен.

Набор commands может храниться:

* в documentation;
* в pyproject.toml;
* в CI workflow;
* в простом script.

Registry оправдан позднее, если:

* checks становятся многочисленными;
* selection зависит от task type;
* появляется несколько projects;
* возникает реальный drift.

До этого registry создаёт больше complexity, чем пользы.

⸻

Не дублировать commands

Не следует независимо хранить разные версии validation commands в:

* README;
* AGENTS.md;
* CI;
* scripts;
* Task Brief templates;
* onboarding guide.

Нужно определить один canonical technical entry point и ссылаться на него.

Пока такого entry point нет, documentation должна явно помечать commands как candidate или current local sequence.

⸻

Изменение CI

Изменение CI может повлиять на:

* required checks;
* merge behavior;
* permissions;
* secrets;
* runtime;
* dependencies;
* supply-chain risk.

Поэтому CI change не должно скрываться внутри unrelated feature.

Task Brief должен указать:

* что меняется;
* почему;
* какие permissions нужны;
* какие checks добавляются или удаляются;
* как проверяется workflow;
* влияет ли изменение на branch protection.

⸻

Ослабление check

Удаление или ослабление required check требует отдельного объяснения.

Недопустимо:

* удалить failing test ради green CI;
* превратить failure в warning без решения;
* исключить directory, потому что tests нестабильны;
* добавить || true;
* игнорировать exit code;
* расширить skip condition;
* снизить threshold без анализа.

Если check ошибочен, сначала нужно доказать ошибку check.

⸻

continue-on-error

continue-on-error допустим только для явно advisory job.

Он не должен применяться к required safety или acceptance check.

CI UI должна ясно показывать, что advisory check failed, даже если общий workflow продолжился.

⸻

Supply-chain boundary

CI выполняет external actions и устанавливает packages.

Минимальные меры:

* least-privilege permissions;
* pinned action SHAs;
* ограниченное количество actions;
* known package registries;
* отсутствие curl | sh;
* review dependency updates;
* отсутствие production secrets в basic pipeline.

Полный supply-chain security framework не требуется для первого vertical slice.

⸻

Matrix testing

Test matrix оправдана, если AOS официально поддерживает:

* несколько Python versions;
* несколько operating systems;
* несколько databases;
* несколько providers.

До этого момента одна reference environment лучше, чем формальная непроверенная matrix.

Каждый элемент matrix увеличивает:

* время;
* стоимость;
* количество transient failures;
* maintenance.

⸻

Performance checks

Performance benchmark не нужен в bootstrap, если Product Contract не содержит performance requirement.

Benchmark добавляется, когда:

* существует measurable target;
* environment контролируется;
* result воспроизводим;
* regression имеет пользовательское значение.

Случайные timing values из shared CI machines не должны становиться строгим gate без анализа вариативности.

⸻

Security checks

Минимальные security checks появляются вместе с соответствующей attack surface.

Возможные этапы:

secret check
→ dependency audit
→ static analysis
→ unsafe deserialization checks
→ permission checks
→ integration security tests

Не следует добавлять весь security toolchain до появления executable Product Runtime.

Но secrets и dangerous Git operations запрещены с первого дня независимо от наличия scanner.

⸻

Проверка licenses

License check становится необходимым до:

* внешнего распространения;
* коммерческого использования;
* включения значимых third-party components;
* публикации package.

Отсутствие автоматического license check не означает, что licensing не важно.

Это отдельный legal/productization concern.

⸻

Reports

Результат validation должен включать:

check name
scope
command
result
important output
unknowns
not-run checks
blocking finding

Для простых tasks достаточно короткого report.

Не нужен большой Evidence package для каждого Markdown diff.

⸻

Минимальный report checks

Пример:

## Выполненные проверки
- `git diff --check` — PASS
- Target-only diff — PASS
- Markdown preview — PASS
- Internal links — NOT_RUN
- Content review — NOT_RUN

Это честнее, чем:

Все проверки пройдены.

если фактически проверялись только whitespace и diff.

⸻

CI result в Stage Report

Stage Report должен отдельно указывать:

Local checks
CI checks
Human review

Пример:

Local checks: PASS
CI checks: NOT_RUN — branch не публиковалась
Human review: NOT_PROVIDED

Нельзя объединять эти состояния.

⸻

First manual workflow

До появления mandatory CI первый manual workflow может использовать только local checks.

Это допустимо, если:

* задача low-risk и reversible;
* scope ограничен;
* protected content не затрагивается;
* commands понятны;
* diff проверен;
* результат проходит отдельный human review;
* CI: NOT_RUN раскрыт.

CI не должно становиться prerequisite первого manual cycle только ради формальной зрелости.

⸻

Когда минимальный CI становится необходим

Minimal CI целесообразно добавить, когда:

* появляется code package;
* существует repeatable test command;
* changes начинают публиковаться в remote;
* требуется защищать main;
* несколько contributors работают с repository;
* local drift становится реальной проблемой;
* первый vertical slice должен проверяться автоматически.

⸻

Suggested initial CI characteristics

После появления implementation initial CI должен быть:

* single-purpose;
* read-only;
* least-privilege;
* коротким;
* reproducible;
* основанным на одной runtime version;
* использующим dependency manifest;
* запускающим основной local test command;
* без secrets;
* без deployment;
* без auto-merge;
* без auto-correction.

⸻

Anti-patterns

CI before executable behavior

Workflow создаётся раньше, чем существует meaningful test command.

CI badge как product progress

Зелёный badge не заменяет работающий vertical slice.

Green at any cost

Tests, exit codes или filters ослабляются ради PASS.

Hidden skipped checks

Общий status выглядит успешным, хотя обязательные проверки не выполнялись.

CI-only development

Пользователь вынужден делать push после каждого небольшого изменения, чтобы узнать результат.

Too many tools

Bootstrap использует множество linters, scanners и runners без принятого contract.

Auto-fix in validation

CI изменяет artifact, который должно было только проверять.

Auto-merge

Technical PASS автоматически приводит к merge без human boundary.

Mutable actions

CI исполняет mutable third-party tags без контроля обновлений.

Broad permissions

Validation workflow получает write, issues или deployment permissions без необходимости.

Secret-heavy basic pipeline

Обычные unit tests зависят от production credentials.

Retry until green

Flaky test скрывается многократным автоматическим retry.

Zero tests as success

Broken discovery создаёт ложный положительный результат.

Coverage theater

Высокий percentage используется как замена meaningful acceptance tests.

⸻

Критерий готовности Minimal Checks

Minimal Checks считаются достаточно определёнными, если:

1. для текущего типа задачи существует понятный local check;
2. check имеет ограниченный claim;
3. PASS, FAIL, UNKNOWN, NOT_RUN и BLOCKED различаются;
4. zero tests не считается успехом;
5. target-only diff проверяется;
6. unrelated changes не скрываются;
7. validation не исправляет artifact;
8. failed check приводит к report и stop;
9. human approval остаётся отдельным;
10. checks пропорциональны риску задачи.

⸻

Критерий готовности Initial CI

Initial CI считается достаточно определённым, если:

1. существует реальный executable project;
2. определена основная local validation command;
3. CI повторяет эту command;
4. runtime version зафиксирована;
5. dependencies устанавливаются из manifest;
6. permissions минимальны;
7. actions контролируются;
8. secrets не требуются для basic checks;
9. failure возвращает ненулевой exit code;
10. skipped checks видимы;
11. CI ничего не исправляет;
12. CI не выполняет commit, push, merge или release;
13. CI PASS не интерпретируется как approval.

⸻

Что не входит в этот документ

Этот документ не определяет:

* production deployment;
* release pipeline;
* full branch protection policy;
* merge queue;
* enterprise compliance;
* full security scanning suite;
* test coverage threshold;
* multi-platform matrix;
* performance benchmark policy;
* automated dependency updates;
* automatic correction;
* agent execution из CI;
* merge authorization package;
* Runtime Enforcement;
* полный Governance / Control Module.

Эти механизмы добавляются позднее при подтверждённой необходимости.

⸻

Следующее развитие

После Minimal Checks and CI необходимо определить:

[`First Manual Workflow`](First_Manual_Workflow.md)

First Manual Workflow должен собрать уже определённые элементы в один реальный bounded cycle:

Task Brief
→ preflight
→ controlled change
→ local checks
→ Stage Report
→ human review
→ одно следующее действие

Он должен работать до создания full Development Factory, registry и автоматического conveyor.

⸻

Источники

Документ сформирован на основе:

* Project Principles;
* Agent Contract;
* Git Foundation;
* Task and Report Templates;
* Minimal Safety Floor;
* Local Development Environment;
* historical AOS-FARM validation practices;
* AOS-02 bootstrap и CI audits;
* правила CI PASS ≠ approval;
* lessons о false-green, zero tests, exit codes и local/CI parity.

Legacy CI и validators использованы только как reference patterns. Они не становятся обязательной implementation нового AOS автоматически.
