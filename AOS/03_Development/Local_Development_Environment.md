# Local Development Environment

Назначение

Этот документ определяет минимальную локальную среду разработки проекта AOS.

Local Development Environment должна обеспечить:

* воспроизводимый запуск проекта;
* понятный toolchain;
* отделение runtime dependencies от development dependencies;
* локальную изоляцию dependencies;
* одинаковое базовое поведение на разных машинах;
* возможность запускать проверки без сложной инфраструктуры;
* отсутствие скрытой зависимости от IDE или конкретного AI-agent provider;
* безопасное добавление новых dependencies;
* понятную границу между локальной средой, CI и production environment.

Локальная среда должна быть минимальной.

Она не должна заранее включать:

* database;
* Docker;
* Kubernetes;
* cloud infrastructure;
* RAG;
* vector database;
* orchestration framework;
* multi-agent runtime;
* production deployment;
* full security toolchain;
* собственный package registry;
* сложный environment manager.

Такие компоненты добавляются только после появления подтверждённой необходимости.

⸻

Основной принцип

Первый рабочий AOS должен запускаться в простой локальной среде.

Предпочтительный начальный путь:

Git repository
→ поддерживаемая версия runtime
→ локальное virtual environment
→ минимальные dependencies
→ одна команда установки
→ одна команда проверки

Среда должна быть достаточно простой, чтобы новый пользователь или агент мог:

1. открыть repository;
2. определить требуемую версию runtime;
3. создать изолированное environment;
4. установить dependencies;
5. выполнить базовую проверку;
6. понять результат.

⸻

Environment является частью воспроизводимости

Работающий на одной машине код не является достаточным доказательством воспроизводимости.

Для воспроизводимого результата должны быть понятны:

* operating system или поддерживаемые operating systems;
* runtime;
* версия runtime;
* package manager;
* dependency manifest;
* способ создания environment;
* installation command;
* validation command;
* необходимые environment variables;
* внешние services;
* ограничения среды.

Если существенная часть environment неизвестна, соответствующий compatibility claim должен оставаться UNKNOWN.

⸻

Текущий документационный этап

На текущем этапе AOS является documentation-driven reconstruction project.

Для заполнения документации достаточно:

* Git;
* текстового редактора;
* Markdown support;
* shell;
* возможности просматривать diff.

На этом этапе не требуется:

* Python package;
* Node.js;
* database;
* Docker;
* application server;
* frontend toolchain;
* cloud account.

Implementation toolchain должен быть выбран после определения первого Product Contract и первого vertical slice.

⸻

Предварительный runtime candidate

Исторические материалы AOS-FARM и текущие prototypes в основном используют Python.

Поэтому Python является естественным initial candidate для:

* command-line tools;
* validators;
* task processing;
* local automation;
* tests;
* early Product Runtime prototype.

Это не означает окончательное architecture approval.

Точный выбор language и runtime должен быть подтверждён в Architecture documentation первого vertical slice.

До этого момента следует избегать создания language-specific skeleton без необходимости.

⸻

Минимальная версия Python

Если первый implementation vertical slice использует Python, следует выбрать одну явно поддерживаемую версию.

Не следует оставлять requirement в форме:

Python 3

Потому что разные minor versions могут иметь различия в:

* standard library;
* typing;
* pathlib;
* packaging;
* dependency support;
* security updates;
* CI images.

Рекомендуемая стратегия:

одна основная версия Python
→ одинаковая локально и в CI
→ расширение support matrix позже

Конкретная версия должна быть выбрана по состоянию dependencies и toolchain на момент начала implementation.

До выбора версии документ не должен утверждать, что AOS уже поддерживает определённый Python range.

⸻

Runtime version file

После выбора runtime version её следует зафиксировать в одном понятном месте.

Возможные варианты для Python:

.python-version

или requirement внутри:

pyproject.toml

Не следует одновременно хранить несколько противоречащих друг другу version declarations.

CI, documentation и local setup должны ссылаться на одну и ту же принятую версию или совместимый range.

⸻

Virtual environment

Python dependencies должны устанавливаться в локальное изолированное environment.

Базовый вариант:

python -m venv .venv

Активация на macOS и Linux:

source .venv/bin/activate

Активация на Windows PowerShell:

.venv\Scripts\Activate.ps1

.venv/ должна быть исключена из Git.

Virtual environment не является частью Source of Truth.

Её можно удалить и воспроизвести из dependency manifest.

⸻

Не использовать global installation

Project dependencies не следует устанавливать глобально в system Python.

Global installation создаёт риск:

* version conflicts;
* machine-specific behavior;
* невозможности воспроизвести environment;
* влияния одного проекта на другой;
* случайного использования уже установленных packages;
* различий между local и CI.

Команды проекта должны выполняться внутри активного environment или через tool, который гарантирует изоляцию.

⸻

Package management

На первом Python-этапе предпочтителен стандартный и понятный package workflow.

Возможная основа:

pyproject.toml
pip
venv

Не следует сразу добавлять несколько конкурирующих package managers:

* Poetry;
* Pipenv;
* Hatch;
* PDM;
* Conda;
* uv;
* custom bootstrap scripts.

Один из этих инструментов может быть выбран позднее, если он решает конкретную подтверждённую проблему.

Toolchain не должен усложняться только ради современности или удобства отдельного агента.

⸻

Dependency manifest

После появления Python implementation должен существовать machine-readable dependency manifest.

Предпочтительный современный вариант:

pyproject.toml

В нём могут быть разделены:

* runtime dependencies;
* test dependencies;
* development dependencies;
* optional integrations.

Пример смыслового разделения:

core
test
dev
integration

Не следует устанавливать все возможные tools каждому пользователю продукта.

⸻

Runtime и development dependencies

Runtime dependencies необходимы для работы Product Runtime.

Development dependencies необходимы только для:

* tests;
* lint;
* type checking;
* build;
* local tooling;
* security checks.

Они должны быть разделены.

Пример:

AOS core runtime
→ минимальный dependency set
AOS development environment
→ core + test tools

Product Runtime не должен зависеть от pytest, linters, audit tools или documentation generators.

⸻

Минимум dependencies

По умолчанию следует использовать Python standard library, если она достаточно надёжно решает задачу.

Third-party dependency добавляется, если:

* она решает реальную проблему;
* собственная реализация была бы менее безопасной или значительно сложнее;
* package поддерживается;
* license приемлема;
* version compatibility понятна;
* dependency можно проверить;
* существует понятный fallback или migration path.

Dependency не добавляется только потому, что она популярна или уже использовалась в legacy AOS-FARM.

⸻

Не реализовывать сложные стандарты частично без причины

Минимизация dependencies не означает обязательную самостоятельную реализацию сложных стандартов.

Опасный пример:

отказаться от mature dependency
→ написать partial custom validator
→ считать его эквивалентным полному стандарту

Custom implementation допустима, если:

* поддерживаемый subset явно определён;
* отсутствует claim о полной совместимости;
* edge cases покрыты tests;
* причина отказа от dependency понятна;
* цена сопровождения приемлема.

Для security-sensitive parsing и validation зрелая dependency часто безопаснее собственной неполной реализации.

⸻

Version constraints

Dependencies должны иметь осознанные version constraints.

Слишком широкий range создаёт непредсказуемость:

package>=1

Слишком жёсткая фиксация каждой transitive dependency может создать высокую стоимость обновления.

На раннем этапе допустимо фиксировать:

* совместимый major range;
* известный безопасный minimum;
* upper bound до следующего несовместимого major release.

Пример:

package>=2.4,<3

Конкретные ranges должны определяться по актуальному состоянию packages и security advisories на момент добавления.

⸻

Lock file

Lock file становится полезным, если:

* dependency graph перестаёт быть тривиальным;
* reproducibility между машинами становится проблемой;
* CI и local environment разрешают разные transitive versions;
* проект выпускается внешним пользователям;
* build должен быть детерминированным.

Не следует создавать custom lock mechanism.

Если выбранный package manager поддерживает стандартный lock file, следует использовать его собственный формат.

До появления реальной dependency graph lock file может быть избыточным.

⸻

Installation command

После появления implementation должна существовать одна основная команда установки development environment.

Пример для Python package:

python -m pip install -e ".[test]"

или, если dev dependencies разделены:

python -m pip install -e ".[dev]"

Документация не должна предлагать множество равноправных installation paths без причины.

Один путь является основным.

Альтернативы описываются только для реально поддерживаемых environments.

⸻

Editable installation

Editable install удобен для local development:

python -m pip install -e .

Он позволяет запускать package из текущего source tree.

Но editable install не доказывает:

* корректность distribution package;
* корректность wheel;
* корректность clean installation;
* production readiness.

Перед release позднее потребуется отдельная build и clean-install validation.

⸻

Запуск из project root

Commands должны выполняться из явно определённого project root, если toolchain не гарантирует независимость от current directory.

Нельзя полагаться на случайный PYTHONPATH или локальные import side effects.

Если script требует запуск из root, это должно быть явно документировано.

Предпочтительно строить package так, чтобы commands запускались через module или installed entry point:

python -m aos

или:

aos

а не через хрупкие относительные imports из случайных directories.

⸻

Environment variables

Environment variables используются для configuration, которая зависит от машины или внешней среды.

В repository допустимо хранить:

.env.example

или другой example-файл без secrets.

Он должен содержать:

* имена переменных;
* краткое назначение;
* безопасный пример;
* указание, обязательна ли переменная;
* допустимый формат.

Реальный .env должен быть исключён из Git.

⸻

Secrets

В local environment secrets могут включать:

* API keys;
* tokens;
* passwords;
* private endpoints;
* production credentials.

Secrets нельзя:

* помещать в pyproject.toml;
* помещать в committed .env;
* хранить в Markdown reports;
* записывать в test fixtures;
* выводить полностью в logs;
* передавать агентам без необходимости.

Если первый vertical slice не требует внешнего API, environment не должен вводить secret management заранее.

⸻

Configuration defaults

Безопасные и несекретные defaults могут храниться в repository.

Default configuration должна:

* позволять локальный запуск;
* не подключаться к production;
* не выполнять внешние writes;
* не включать network автоматически;
* не использовать реальные credentials;
* не создавать irreversible resources.

Development environment должна быть безопасной по умолчанию.

⸻

Network boundary

Установка новых dependencies обычно требует network.

Network access должен включаться только для конкретной операции:

получить declared dependencies

Он не даёт разрешение:

* обращаться к произвольным APIs;
* загружать неизвестные scripts;
* выполнять remote installation shell;
* публиковать artifacts;
* отправлять repository content;
* включать telemetry.

После установки большинство local development и validation operations должны работать без network, если внешняя integration не является предметом теста.

⸻

Dependency source

Dependencies должны устанавливаться из известных package registries или проверенных sources.

Не следует использовать:

* случайные archives;
* непроверенные forks;
* install scripts через curl | sh;
* dependencies из неизвестных branches;
* unpinned Git commits без причины.

Git-based dependency требует отдельного объяснения:

* почему registry package недостаточен;
* какой commit используется;
* как проверена integrity;
* кто сопровождает source.

⸻

Dependency changes

Добавление, удаление или существенное обновление dependency является отдельным controlled change.

Task Brief должен объяснять:

* зачем нужна dependency;
* какие alternatives рассмотрены;
* используется ли она в runtime или только development;
* какой version range выбран;
* какие licenses и security implications известны;
* какие tests подтверждают integration;
* как удалить или заменить dependency.

Dependency не должна добавляться скрыто внутри unrelated feature task.

⸻

Security updates

Dependency update не следует выполнять автоматически без проверки.

Перед update нужно определить:

* текущую версию;
* целевую версию;
* причину update;
* breaking changes;
* security advisories;
* изменения transitive dependencies;
* результаты tests.

Автоматический dependency updater может быть добавлен позднее, но его pull requests всё равно требуют validation и review.

⸻

Operating system support

На первом этапе следует выбрать ограниченный support target.

Возможная стратегия:

primary development environment: macOS
CI reference environment: Linux
Windows support: UNKNOWN до отдельной проверки

Но точные утверждения должны основываться на фактическом setup и tests.

Нельзя объявлять cross-platform support только потому, что используется Python.

Paths, shell commands, file permissions, line endings и process behavior могут различаться.

⸻

Platform-independent paths

В code предпочтительно использовать platform-aware path APIs.

Для Python:

from pathlib import Path

Не следует вручную собирать paths через строковые / или \, если это влияет на compatibility.

Tests должны включать хотя бы validation path semantics, если portability является product requirement.

⸻

Shell commands

Документация должна ясно указывать, для какой shell предназначены команды.

Пример:

macOS/Linux — bash/zsh
Windows — PowerShell

Не следует смешивать syntax разных shells в одном неразмеченном block.

Основной local path может сначала поддерживать macOS/Linux, если это соответствует фактической среде разработки.

⸻

Containers

Docker не является обязательной частью initial environment.

Container добавляется, если он решает подтверждённую проблему:

* сложные system dependencies;
* несколько services;
* несовместимость local machines;
* reproducible integration environment;
* production parity;
* external distribution.

Docker не следует добавлять только для запуска одного Python package с несколькими dependencies.

Container не заменяет dependency manifest и local documentation.

⸻

Database

Database не входит в initial development environment по умолчанию.

Она добавляется, если Product Contract требует persistent structured state, который невозможно разумно хранить в простых artifacts.

До этого момента предпочтительны:

* Markdown;
* JSON;
* repository files;
* in-memory state;
* disposable local cache.

Database не должна становиться Source of Truth для human approvals или canonical documentation без отдельного architecture decision.

⸻

RAG и vector storage

RAG, embeddings и vector database не являются обязательной частью bootstrap.

Они могут быть полезны позже для:

* semantic retrieval;
* больших knowledge bases;
* project search;
* historical context.

Но сначала необходимо доказать, что:

* обычного file search недостаточно;
* corpus достаточно велик;
* retrieval quality измеряется;
* source provenance сохраняется;
* stale index не становится authority;
* privacy и cost приемлемы.

⸻

External services

Первый vertical slice по возможности должен работать без обязательных внешних services.

Если внешний service необходим, нужно документировать:

* назначение;
* account requirements;
* credentials;
* network behavior;
* local fallback;
* cost;
* rate limits;
* data sent externally;
* failure behavior.

External service не должен скрыто становиться permanent core dependency.

⸻

AI model providers

Local Development Environment не должна быть привязана к одному AI provider.

Provider-specific configuration может включать:

* API key;
* model name;
* endpoint;
* timeout;
* usage limits.

Но product-level workflow должен по возможности использовать internal interface, позволяющий заменить provider.

На раннем этапе manual agent invocation допустима и может быть предпочтительнее premature provider abstraction.

⸻

IDE

AOS не должен требовать конкретную IDE.

Поддерживаться могут:

* VS Code;
* Cursor;
* Zed;
* terminal editors;
* другие IDE.

Repository может содержать optional editor settings, если они:

* безопасны;
* не обязательны;
* не содержат machine-specific paths;
* не изменяют source files неожиданно.

User-specific editor configuration не должна становиться prerequisite.

⸻

Formatters

Formatter должен быть добавлен только после выбора implementation language и style policy.

Он должен:

* иметь фиксированную configuration;
* менять только разрешённые files;
* запускаться предсказуемо;
* не создавать массовый unrelated diff.

Агент не должен запускать formatter на весь repository внутри ограниченной задачи без разрешения.

Для Markdown массовый formatter также не должен применяться автоматически, если он меняет структуру или authorial formatting.

⸻

Linters

Lint нужен, если он ловит значимые классы ошибок.

Не следует добавлять множество пересекающихся linters без необходимости.

Для каждого tool должно быть понятно:

* что он проверяет;
* является ли check blocking;
* где находится configuration;
* как исправляются false positives;
* одинаково ли он работает локально и в CI.

Lint PASS не означает behavioral correctness.

⸻

Type checking

Static type checking может быть полезен после стабилизации Python interfaces.

Он не обязан входить в самый первый vertical slice.

Type checker добавляется, если:

* interfaces становятся сложнее;
* количество modules растёт;
* typing реально уменьшает defects;
* команда готова поддерживать annotations.

Partial typing допустим, если его scope явно определён.

⸻

Tests

Первый code environment должен поддерживать одну понятную test command.

Для Python возможный вариант:

python -m pytest

Предпочтительно использовать:

python -m pytest -q

для короткого вывода в обычном workflow.

Но test runner и exact command должны быть выбраны вместе с implementation toolchain.

pytest не следует добавлять в runtime dependencies.

⸻

Basic environment check

После setup пользователь должен иметь одну команду, подтверждающую базовую работоспособность environment.

Возможные формы:

python -m pytest -q

или:

python -m aos doctor

Но doctor не следует создавать до появления достаточного количества реальных environment conditions.

На раннем этапе test command может быть достаточен.

⸻

Doctor command

Future doctor command может проверять:

* runtime version;
* installed package;
* required directories;
* configuration presence;
* dependency availability;
* optional integrations;
* write permissions;
* network requirements.

Doctor должен различать:

PASS
FAIL
UNKNOWN
NOT_RUN

Он не должен:

* автоматически изменять environment;
* устанавливать dependencies;
* исправлять configuration;
* считать отсутствие optional tool failure;
* выдавать approval.

⸻

Bootstrap script

Custom bootstrap script не требуется, если environment можно создать несколькими стандартными командами.

Script оправдан, если он:

* убирает реально повторяющуюся ручную работу;
* выполняется детерминированно;
* имеет --help;
* имеет dry-run для опасных действий;
* не устанавливает неизвестные system packages;
* не меняет shell profile;
* не скачивает произвольные scripts;
* не скрывает network operations.

Bootstrap script не должен становиться новым installer framework раньше продукта.

⸻

Makefile и task runners

Makefile, Just, Nox, Tox или другие task runners могут дать короткие команды:

test
lint
validate
build

Но они добавляются после появления нескольких повторяющихся commands.

В начале прямые стандартные commands предпочтительнее дополнительного abstraction layer.

Task runner не должен скрывать существенные действия или permissions.

⸻

Environment documentation

Local setup должен быть описан коротким последовательным guide.

Минимальный guide:

Prerequisites
Clone or open repository
Create environment
Activate environment
Install dependencies
Run baseline check
Troubleshooting

Документация должна соответствовать реально проверенным commands.

Не следует копировать setup instructions из legacy repository без локальной проверки.

⸻

Clean setup validation

Периодически необходимо проверять setup в чистой среде.

Clean setup означает:

* новый clone или clean worktree;
* новое virtual environment;
* отсутствие заранее установленных project packages;
* installation только из manifest;
* запуск documented checks.

Это выявляет:

* скрытые global dependencies;
* missing files;
* неправильные imports;
* неполную documentation;
* случайные local assumptions.

⸻

Local и CI parity

Local и CI environment должны использовать:

* совместимый runtime;
* один dependency manifest;
* те же основные validation commands;
* одинаковую configuration.

Полная идентичность не всегда возможна, но различия должны быть известны.

CI не должен быть единственным местом, где tests могут быть запущены.

Пользователь должен иметь возможность выполнить основные проверки локально.

⸻

Production environment

Production environment не входит в Local Development Environment.

Необходимо различать:

local development
CI validation
test/staging
production

Local credentials, debug mode и disposable storage не должны автоматически переноситься в production.

Production architecture определяется позже отдельным решением.

⸻

Logs

Local logs должны:

* быть краткими;
* не содержать secrets;
* не попадать случайно в Git;
* храниться в temporary directory;
* быть удаляемыми;
* не становиться Source of Truth.

Если log нужен как Evidence, он переносится в durable artifact с sanitization и context.

⸻

Caches

Caches могут ускорять:

* package installation;
* tests;
* generated indexes;
* model responses;
* build.

Cache всегда считается derived и disposable.

Cache не должен хранить единственную копию:

* decision;
* approval;
* canonical content;
* Task Brief;
* Evidence;
* project state.

Проблема stale cache должна решаться удалением или пересозданием cache, а не новым recovery lifecycle.

⸻

Temporary outputs

Все disposable environment outputs должны находиться в:

/.aos-tmp/

или в стандартных ignored directories конкретного tool.

Примеры:

.pytest_cache/
.coverage
htmlcov/
dist/
build/
*.egg-info/

Каждый generated path должен быть классифицирован:

* ignored;
* tracked by reason;
* durable artifact;
* temporary.

⸻

.gitignore

После выбора toolchain .gitignore должен исключать:

* virtual environments;
* caches;
* test outputs;
* build outputs;
* local secrets;
* IDE-specific private files;
* /.aos-tmp/;
* operating-system artifacts.

.gitignore не должен использоваться для сокрытия важных generated artifacts, которые на самом деле должны проверяться или храниться.

⸻

Environment reset

Безопасный reset local environment должен означать удаление только воспроизводимых artifacts:

virtual environment
caches
build outputs
temporary files

Нельзя включать в обычный reset:

* source files;
* documentation;
* Evidence;
* reports;
* uncommitted user work;
* Git history;
* databases с важными данными;
* external resources.

Любой cleanup script должен точно перечислять удаляемые paths.

⸻

Не использовать destructive cleanup по умолчанию

Следующие команды не должны быть частью обычной environment setup или repair:

git reset --hard
git clean -fd
rm -rf .

Environment repair должен по возможности ограничиваться удалением явно воспроизводимых directories:

.venv/
.pytest_cache/
build/
dist/

Даже это выполняется только при понятном scope.

⸻

Troubleshooting

Troubleshooting должен идти от простого к сложному:

проверить current directory
→ проверить runtime version
→ проверить active virtual environment
→ проверить installation
→ проверить dependency manifest
→ выполнить базовую command
→ посмотреть конкретную ошибку

Не следует сразу:

* перестраивать architecture;
* создавать новый environment manager;
* включать Docker;
* переписывать package layout;
* запускать recovery program.

⸻

Environment failure report

Если setup или validation не удалась, report должен указать:

* operating system;
* runtime version;
* command;
* exit code;
* краткую ошибку;
* активное environment;
* installation method;
* какие шаги прошли;
* что осталось UNKNOWN;
* одно следующее действие.

Нельзя писать только:

environment broken

⸻

Development environment и Product Runtime

Среда разработки и среда пользователя могут различаться.

Development environment может включать:

* tests;
* linters;
* type checker;
* build tools;
* fixtures.

Product Runtime должен включать только необходимое для пользовательской функции.

Development Factory dependencies не должны автоматически попадать в Product Runtime.

⸻

Development environment и Control Plane

Local Development Environment не должна зависеть от полноценного Control Plane.

Для запуска первого vertical slice не должны быть обязательны:

* approval database;
* task registry service;
* policy server;
* runtime authorization service;
* merge package system;
* distributed agent orchestrator.

Minimal Safety Floor обеспечивается процессом, Task Brief, diff, validation и human boundaries до появления enforcement.

⸻

Legacy environment

AOS-FARM использовал преимущественно lightweight Python tooling и небольшое количество development dependencies.

Это полезный reference pattern.

Но новый AOS не должен автоматически переносить:

* старую Python version;
* старые package ranges;
* старые scripts;
* старый flat import layout;
* legacy CI;
* outdated dependency constraints;
* recovery-specific tools.

Каждый элемент environment должен быть заново проверен для текущего Product Contract.

⸻

Что следует определить перед первым implementation

До создания code skeleton необходимо принять:

1. implementation language;
2. runtime version;
3. package format;
4. dependency manifest;
5. virtual environment approach;
6. test runner;
7. basic validation command;
8. supported primary OS;
9. network requirements;
10. secret requirements;
11. temporary and ignored paths.

Не требуется заранее определять production infrastructure.

⸻

Минимальный предполагаемый Python setup

После принятия Python в качестве runtime возможен следующий baseline:

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
python -m pytest -q

Этот пример является candidate setup.

Он становится project instruction только после появления и проверки соответствующего pyproject.toml.

⸻

Что не нужно добавлять в bootstrap

Без отдельного требования не добавлять:

* Dockerfile;
* Docker Compose;
* Kubernetes manifests;
* Terraform;
* database server;
* Redis;
* message broker;
* vector database;
* LangGraph;
* CrewAI;
* workflow engine;
* monitoring stack;
* telemetry backend;
* package publishing;
* multi-platform installer;
* plugin system.

Каждый из этих элементов может быть полезен позднее, но не является условием первого рабочего AOS.

⸻

Критерии выбора нового tool

Новый development tool добавляется, если:

1. существует повторяющаяся проблема;
2. проблема наблюдалась в реальной работе;
3. tool явно решает её;
4. tool не дублирует уже существующую функцию;
5. стоимость поддержки приемлема;
6. есть понятная команда;
7. local и CI usage согласованы;
8. tool можно удалить без разрушения Product Runtime;
9. его output не становится скрытым Source of Truth.

⸻

Anti-patterns

Environment before product

Сначала строится сложная infrastructure, хотя пользовательский vertical slice ещё не определён.

Too many tools

Проект использует несколько package managers, linters и task runners без ясной причины.

Global dependencies

Работа зависит от packages, случайно установленных на машине автора.

Undocumented runtime version

Local и CI используют разные Python versions.

Hidden network

Setup обращается к внешним services, хотя documentation этого не сообщает.

Custom installer too early

Несколько стандартных commands заменяются большим installation framework.

Docker by default

Container добавляется до появления system dependencies или services.

Database as project memory

Persistent database создаётся раньше понимания actual project memory requirements.

Partial custom standard implementation

Собственный parser или validator выдаётся за полную реализацию стандарта.

Tool output as authority

Doctor, linter или test result ошибочно считается approval.

Recovery loop

Environment failure приводит к созданию нового управляющего слоя вместо исправления конкретной причины.

⸻

Минимальная проверка документационного environment

На текущем этапе достаточно проверить:

git --version
git rev-parse --show-toplevel
git branch --show-current
git status --short -- AOS
git diff --check

Для Markdown может дополнительно использоваться editor preview или простой link checker после появления достаточного количества links.

Никакой runtime package пока не требуется.

⸻

Минимальная проверка будущего code environment

После появления implementation ожидается следующий класс проверок:

runtime version
package installation
import or startup
unit tests
basic acceptance scenario
clean working tree classification

Конкретные commands определяются вместе с первым implementation Task Brief.

⸻

Критерий готовности

Local Development Environment считается достаточно определённой для начала implementation, если:

1. выбран runtime;
2. зафиксирована его версия;
3. существует один dependency manifest;
4. environment изолируется локально;
5. installation command документирована;
6. test command документирована;
7. clean setup воспроизводим;
8. local и CI используют совместимый toolchain;
9. secrets не попадают в repository;
10. temporary outputs исключены из Git;
11. network requirements явны;
12. runtime и development dependencies разделены;
13. external services не скрыты;
14. unsupported environments не объявлены поддерживаемыми;
15. Product Runtime не зависит от необязательной Development Factory infrastructure.

⸻

Что не входит в этот документ

Этот документ не определяет:

* окончательный production stack;
* deployment architecture;
* cloud provider;
* database architecture;
* frontend framework;
* observability platform;
* release packaging;
* supported enterprise environments;
* multi-repository development;
* full security scanning suite;
* dependency update automation;
* Runtime Enforcement;
* Development Factory implementation.

Эти решения принимаются позднее в соответствующем контексте.

⸻

Следующее развитие

После Local Development Environment необходимо определить:

[`Minimal Checks and CI`](Minimal_Checks_And_CI.md)

Minimal Checks and CI должны установить:

* какие проверки обязательны локально;
* какие проверки выполняются в CI;
* что означает результат каждой проверки;
* как предотвращается false PASS;
* какие checks нужны документации;
* какие checks появятся после начала implementation;
* почему CI PASS не означает approval.
