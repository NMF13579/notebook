# Project Skeleton

Назначение

Этот документ определяет минимальный skeleton проекта AOS.

Skeleton нужен для того, чтобы:

* человек сразу понимал, где находится каждый тип материала;
* агент мог безопасно ориентироваться в repository;
* структура не смешивала Product Runtime, Development Factory и Control;
* документация могла развиваться без постоянной перестройки;
* будущая implementation получала понятные места для code, tests, configuration и artifacts;
* проект можно было воспроизвести с нуля по документации;
* временные и производные материалы не становились Source of Truth.

Project Skeleton — это только целевая структура.

Он не означает:

* готовность продукта;
* наличие implementation;
* завершённую архитектуру;
* работающий workflow;
* наличие CI;
* наличие Control Plane;
* approval следующих этапов.

⸻

Главная цель skeleton

Skeleton должен обеспечить простую и устойчивую основу, в которой можно последовательно:

документировать проект
→ определить product contracts
→ реализовать первый vertical slice
→ добавить tests
→ проверить manual workflow
→ расширять продукт
→ только затем добавлять automation и control

Структура должна помогать этому пути, а не задавать преждевременно полную архитектуру будущей системы.

⸻

Основной принцип структуры

Repository должен быть организован вокруг canonical слоёв и предметных объектов.

Пользователь и агент должны иметь возможность двигаться сверху вниз:

Core
→ Product
→ Architecture
→ Development
→ Lessons
→ Reference

Deferred Control и Advanced materials, а также Research, References и Archive должны быть отделены от active canonical содержания внутри `05_Reference`.

Такое разделение предотвращает смешение:

* текущих требований;
* будущих идей;
* legacy artifacts;
* исторических plans;
* rejected approaches;
* active product documentation.

⸻

Текущая верхнеуровневая структура

Документационный слой AOS использует следующую canonical основу:

AOS/
├── README.md
├── MANIFEST.md
├── 00_Core/
├── 01_Product/
├── 02_Architecture/
├── 03_Development/
├── 04_Lessons/
└── 05_Reference/

Каждый раздел имеет одного понятного владельца содержания.

⸻

00_Core

Раздел определяет:

* Project Identity;
* Project Principles;
* Minimal Safety Floor;
* глобальные Source of Truth и legacy-reference boundaries.

Core не является implementation plan или runtime implementation.

⸻

01_Product

Раздел определяет Product Runtime с точки зрения пользователя:

* Product Vision и Product Outcome;
* target user и core problem;
* user journey и first vertical slice;
* Product Contracts и observable behavior;
* Acceptance Criteria;
* product boundaries и success metrics.

Он отвечает на вопрос: какую проверяемую ценность получает пользователь?

⸻

02_Architecture

Раздел определяет минимальные structural foundations:

* Project Skeleton;
* Workspace Foundation;
* Agent Contract;
* Git Foundation.

Architecture не получает authority из legacy topology или historical naming.

⸻

03_Development

Раздел определяет active development workflows:

* task preparation;
* execution;
* validation;
* decision model;
* project memory и recovery;
* Development Factory;
* agent collaboration;
* process evolution.

Development workflows не заменяют Product Runtime и не создают human approval.

⸻

04_Lessons

Раздел хранит active lessons и anti-patterns, уже сформулированные для нового AOS.

Historical lessons остаются reference-only до отдельного принятия в canonical topic.

⸻

05_Reference

Раздел хранит deferred или non-active материалы:

* Control;
* Advanced;
* Research;
* References;
* Archive;
* Reconstruction Roadmap.

Presence в `05_Reference` не превращает материал в active architecture, product contract, lifecycle, approval source или implementation foundation.

⸻

Навигация и ownership

`AOS/README.md` является active navigation entry.

`AOS/MANIFEST.md` является canonical ownership, provenance и supersession map.

`AOS/00_INDEX.md` и старые numbered trees `01_Project`–`09_Archive` являются superseded preservation sources. Они не определяют current structure и не являются active navigation.

⸻

Historical numbering convention (superseded)

Legacy trees использовали иерархические identifiers `NN`, `NN.MM` и `NN.MM.KK`. Эти identifiers сохраняются только в legacy paths и provenance records, чтобы не терять историю.

Новая canonical структура не требует продолжения old numbering и не использует номер как status, readiness или authority.

⸻

Структура canonical topic

Каждый canonical topic начинается с одного основного Markdown-файла.

Дополнительные документы создаются только при появлении самостоятельного содержания, например отдельных requirements, validation, lessons или sources.

Не следует создавать пустые placeholders заранее.

Knowledge хранится рядом с canonical owner либо связывается с ним относительной ссылкой. Manifest фиксирует provenance, но не дублирует normative text.

⸻

Когда нужно разделять README

README предметного объекта следует разделить на несколько файлов, если:

* он стал слишком большим;
* разные части имеют самостоятельный lifecycle;
* разные части обновляются независимо;
* отдельный файл нужен для implementation;
* отдельный файл нужен для validation;
* sources стали слишком объёмными;
* разные агенты должны работать с разными аспектами без конфликта.

До этого момента предпочтителен один понятный документ.

⸻

Root README

Корневой README.md должен кратко объяснять:

* что представляет собой repository;
* что проект называется AOS;
* что repository является documentation-driven reconstruction layer;
* что он не является Product Runtime;
* что он не является active Control Plane;
* с какого файла начать чтение;
* как устроена canonical структура;
* какова роль legacy materials.

Root README не должен дублировать всю Project Identity, Product Vision или Roadmap.

⸻

Что не должно лежать в root

В root не следует складывать:

* временные command outputs;
* случайные reports;
* копии чатов;
* extracted fragments;
* generated indexes;
* agent scratch files;
* duplicate documents;
* backup copies;
* файлы вида final_v2_revised_latest.md.

Root должен оставаться коротким и предсказуемым.

⸻

Temporary workspace

Для временных материалов должен использоваться отдельный disposable workspace:

/.aos-tmp/

Он предназначен для:

* scratch files;
* temporary command outputs;
* intermediate generated content;
* disposable logs;
* transient comparison results.

Он не предназначен для:

* canonical documentation;
* Evidence;
* approvals;
* human decisions;
* checkpoints;
* accepted reports;
* durable sources;
* implementation contracts.

Temporary workspace должен быть исключён из Git.

⸻

Documentation и future implementation

Документационный skeleton не обязан заранее создавать code directories.

Будущая implementation structure должна появляться только после определения:

* Product Contract;
* Architecture Contract;
* first vertical slice;
* language and toolchain;
* package boundaries;
* testing strategy.

Не следует заранее создавать:

src/
schemas/
runtime/
database/
services/
api/
frontend/
backend/

только потому, что они могут понадобиться в будущем.

⸻

Минимальная future implementation structure

Когда первый vertical slice будет определён, минимальный implementation skeleton может включать:

src/
tests/
examples/
docs/

Возможны дополнительные элементы:

pyproject.toml
requirements-dev.txt
.github/workflows/

Но только после принятия toolchain и concrete implementation scope.

Skeleton не должен автоматически копировать старую структуру AOS-FARM.

⸻

Разделение documentation и implementation

Необходимо различать:

документ описывает component

и

component существует в коде

Наличие папки или README не означает, что feature реализована.

Наличие implementation не означает, что документация актуальна.

Связь между ними должна подтверждаться позже через:

* acceptance criteria;
* tests;
* repository inspection;
* validation;
* review.

⸻

Не копировать старый skeleton целиком

Старый AOS-FARM имел развитую структуру:

* /aos/;
* scripts;
* schemas;
* templates;
* prompts;
* configs;
* tests;
* reports;
* tasks;
* validators;
* Governance sources.

Эта структура полезна как reference.

Она не должна переноситься автоматически.

Причины:

* часть paths обслуживала recovery;
* часть artifacts была связана с устаревшим lifecycle;
* часть структуры появилась до подтверждения product value;
* часть components была design-only или partial;
* старый skeleton смешивал product, factory и governance concerns.

Каждый элемент старой структуры должен возвращаться только при доказанной необходимости.

⸻

Требования к skeleton

Project Skeleton должен быть:

Понятным

Человек без знания истории должен понимать назначение каждого верхнеуровневого раздела.

Предсказуемым

Одинаковые типы объектов должны иметь одинаковую внутреннюю логику.

Минимальным

Не создавать directories и files до появления содержательной необходимости.

Расширяемым

Новые разделы и документы можно добавлять без массовой перестройки.

Проверяемым

Можно определить, какие файлы существуют и какие placeholders ещё не заполнены.

Независимым от tool

Структура не должна требовать конкретного agent provider, model, IDE или SaaS.

Совместимым с Git

Изменения должны быть понятны в diff и не создавать массовых rename операций.

⸻

Что не входит в Project Skeleton

Project Skeleton не определяет:

* окончательную architecture;
* programming language;
* package manager;
* database;
* API;
* UI framework;
* deployment;
* CI provider;
* runtime storage;
* agent orchestration framework;
* authority service;
* Risk Profile implementation;
* release process.

Эти решения появляются в соответствующих следующих документах.

⸻

Ошибки, которых нужно избежать

Полный skeleton заранее

Создание десятков пустых directories и files создаёт ложную полноту и усложняет навигацию.

Skeleton как architecture approval

Наличие папки не означает, что layer или component архитектурно принят.

Skeleton как implementation claim

Структура не доказывает работоспособность.

Копирование legacy topology

Старые paths не должны автоматически определять новый проект.

Смешение active и reference materials

Legacy, research и active requirements должны быть физически разделены.

Generated index как Source of Truth

Навигация не должна принимать решения вместо содержательных документов.

Временные outputs в durable paths

Scratch files не должны попадать в корень или предметные папки.

Массовая ренумерация

Номера не должны постоянно меняться при развитии структуры.

⸻

Минимальная проверка skeleton

Skeleton можно считать достаточным, если:

1. существует понятный root README;
2. существует навигационный index;
3. разделы имеют ясные назначения;
4. Project и Scaffolding содержательно отделены;
5. Product, Development и Control не смешаны;
6. Research, References и Archive отделены от active content;
7. нет заранее созданной runtime architecture;
8. нет случайных temporary files;
9. нумерация однозначна;
10. новый человек может найти нужный раздел без объяснения автора.

⸻

Критерий готовности

Project Skeleton считается готовым для дальнейшего заполнения, когда:

* вся верхнеуровневая структура существует;
* роль каждого раздела объяснена;
* текущая навигация понятна;
* нет конфликтующих путей;
* нет преждевременной implementation structure;
* не требуется копировать старый repository;
* следующий объект можно заполнять без изменения skeleton.

Готовность skeleton не означает готовность Scaffolding Stage в целом.

⸻

Следующее развитие

После определения Project Skeleton active foundation раскрывается через canonical owners:

* [`Workspace Foundation`](Workspace_Foundation.md);
* [`Agent Contract`](Agent_Contract.md);
* [`Git Foundation`](Git_Foundation.md);
* [`Minimal Safety Floor`](../00_Core/Minimal_Safety_Floor.md);
* [`Task and Report Templates`](../03_Development/Task_And_Report_Templates.md);
* [`Local Development Environment`](../03_Development/Local_Development_Environment.md);
* [`Minimal Checks and CI`](../03_Development/Minimal_Checks_And_CI.md);
* [`First Manual Workflow`](../03_Development/First_Manual_Workflow.md).

Historical numbering `02.02`–`02.09` относится только к superseded source tree и не определяет active ownership или порядок навигации.

Каждый объект должен уточнять только свою область и не расширять scope соседних объектов.

⸻

Источники

Документ сформирован на основе:

* Project Identity;
* Product Vision;
* Project Principles;
* Reconstruction Roadmap;
* canonical skeleton boundaries старого AOS-FARM;
* анализа repository AOS-FARM;
* lessons из refoundation;
* опыта создания текущего documentation skeleton;
* принципа Skeleton ≠ implementation;
* разделения Product Runtime, Development Factory и Governance;
* правила использовать legacy topology только как reference.

Старый AOS-FARM прямо разделял Documentation Assembly Pipeline, Code Assembly Pipeline, Minimal Safety Floor, progressive Governance и более поздний Runtime Enforcement, а также фиксировал, что skeleton не является implementation readiness.

Аудит ветки dev показывает полезную, но уже сильно развитую структуру с /aos/, scripts, schemas, templates, tests, reports и validators; для нового AOS её следует использовать как inventory/reference, а не как обязательную начальную topology.

Refoundation model ограничивает bootstrap минимальными docs, package/test skeleton и basic checks, откладывая registry, selector, dashboard, status machine и automatic corrections до working vertical slice и ручных циклов.
