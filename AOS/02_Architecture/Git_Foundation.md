# Git Foundation

Назначение

Этот документ определяет минимальные правила использования Git в проекте AOS.

Git Foundation должен обеспечить:

* однозначное понимание текущего состояния проекта;
* воспроизводимый baseline;
* отделение активной работы от принятого состояния;
* понятную историю изменений;
* безопасные границы между edit, commit, push, merge и release;
* возможность проверить и отменить отдельное изменение;
* защиту от случайной потери чужой или незавершённой работы;
* простой workflow без преждевременной Git-автоматизации.

Git является источником фактического состояния файлов и истории изменений.

Git не является источником:

* human approval;
* product acceptance;
* architecture approval;
* execution authorization;
* release authorization.

⸻

Основной принцип

Каждое Git-действие имеет самостоятельный смысл.

изменить файл
→ добавить изменение в index
→ создать commit
→ отправить commit в remote
→ объединить branch
→ выпустить release

Эти действия нельзя считать одним разрешением.

Обязательные границы:

Edit не означает commit.
Commit не означает push.
Push не означает merge.
Merge не означает release.

Техническая готовность изменения также не означает разрешение выполнить следующий Git-шаг.

⸻

Роль Git в AOS

Git выполняет несколько функций.

Фактическое состояние

Git показывает, какие файлы существуют в repository и какое их содержимое зафиксировано в конкретном commit.

История

Git сохраняет последовательность принятых изменений.

Baseline

Конкретный commit определяет исходное состояние задачи.

Сравнение

Diff показывает, что изменилось относительно baseline.

Изоляция

Branches и при необходимости worktrees позволяют отделять незавершённую работу от устойчивого состояния.

Восстановление

Git позволяет вернуться к известному commit или восстановить отдельный файл без создания собственного recovery framework.

Git не должен превращаться в сложный lifecycle engine AOS.

⸻

Repository и project subtree

Необходимо различать:

Git repository root

и:

AOS project root

В текущей организации AOS может находиться как subtree внутри более крупного repository.

Пример:

repository root:
notebook/
project root:
notebook/AOS/

Такая модель допустима, если она выбрана явно.

Для Git-команд необходимо понимать, относительно какой границы указываются paths.

Например:

git -C /path/to/repository status --short -- AOS

проверяет только subtree AOS внутри родительского repository.

⸻

Текущая branch model

Для документационной реконструкции используется простая модель:

main
→ устойчивый принятый baseline
dev
→ активная сборка и переработка документации

main

В main должны находиться:

* принятый skeleton;
* проверенные содержательные документы;
* устойчивые версии contracts;
* результаты, которые могут использоваться как baseline следующего этапа.

main не должен использоваться как постоянная черновая область.

dev

В dev выполняются:

* заполнение документации;
* исправление содержания;
* извлечение знаний;
* устранение противоречий;
* подготовка новых объектов;
* review corrections;
* будущая разработка до принятия результата.

Эта модель является минимальной.

Дополнительные branches создаются только при реальной необходимости.

⸻

Feature branches

Отдельная feature branch может использоваться, если:

* изменение затрагивает несколько файлов;
* работа продолжается несколько sessions;
* требуется отдельный review;
* изменение рискованно;
* нужно изолировать эксперимент;
* несколько независимых задач выполняются последовательно разными исполнителями;
* необходимо сохранить dev в рабочем состоянии.

Пример:

docs/02-04-git-foundation
feature/project-intake
fix/session-handoff

Наличие feature branch не означает разрешение на push или merge.

⸻

Не создавать branch без причины

Для изменения одного Markdown-файла внутри активного dev отдельная branch обычно не нужна.

Branch создаётся для изоляции реального риска или объёма, а не как обязательный ритуал.

Не следует создавать:

* branch на каждую мелкую формулировку;
* цепочки вложенных branches;
* branches для planning без файловых изменений;
* branches, назначение которых невозможно объяснить;
* множество долгоживущих незавершённых branches.

⸻

Baseline задачи

Каждая write-задача должна иметь известный baseline.

Минимальный baseline:

repository
branch
commit
target path

Перед изменением полезно выполнить:

git rev-parse --show-toplevel
git branch --show-current
git rev-parse HEAD
git status --short

Для задачи внутри subtree дополнительно:

git status --short -- AOS

Baseline нужен для того, чтобы отличить:

* изменения текущей задачи;
* ранее существовавшие изменения;
* unrelated work;
* изменения других исполнителей.

⸻

Неизвестный baseline

Если для write-задачи невозможно определить исходный commit или branch, execution следует остановить.

Неизвестный baseline не блокирует:

* read-only анализ;
* обсуждение;
* draft;
* исследование источников.

Но он блокирует изменение repository, если невозможно доказать, к какому состоянию применяется работа.

⸻

Working tree

Рабочее дерево может быть:

* clean;
* содержать изменения текущей задачи;
* содержать unrelated changes;
* находиться в конфликтном Git operation.

Не каждый dirty working tree является blocker.

Продолжение допустимо, если:

* unrelated changes понятны;
* они не затрагиваются;
* target paths можно изолировать;
* итоговый diff можно проверить;
* commit не смешает разные задачи.

Работа должна быть остановлена, если:

* target file уже содержит неизвестные изменения;
* unrelated changes будут перезаписаны;
* diff невозможно однозначно связать с задачей;
* существует конфликт;
* выполняется незавершённый merge, rebase, cherry-pick или revert.

⸻

Unrelated changes

Агент или человек не должен:

* исправлять unrelated files;
* форматировать весь repository;
* добавлять unrelated changes в commit;
* сбрасывать чужие изменения;
* выполнять git clean;
* использовать git reset --hard;
* восстанавливать files поверх неизвестной работы.

Unrelated change следует оставить без изменения и указать в отчёте, если оно влияет на проверку.

⸻

Один commit — одна логическая задача

Commit должен представлять одно понятное изменение.

Хороший commit:

* имеет ограниченный scope;
* содержит связанные files;
* имеет понятное назначение;
* может быть проверен отдельно;
* может быть отменён без удаления несвязанной работы.

Не следует объединять в один commit:

* документацию и unrelated code refactoring;
* feature и infrastructure experiment;
* correction нескольких независимых findings;
* generated files неизвестного происхождения;
* formatting всего repository вместе с содержательным изменением.

⸻

Размер commit

Commit должен быть достаточно малым для review, но не искусственно раздробленным.

Не требуется создавать отдельный commit:

* на каждое предложение;
* на каждый placeholder;
* на каждое механическое исправление внутри одной задачи.

Допустимый уровень:

один завершённый документ
одна bounded feature
одно исправление finding
один логический migration step

⸻

Commit message

Commit message должен объяснять, что изменено.

Рекомендуемый простой формат:

docs: define project identity
docs: add agent contract
docs: document Git foundation
feat: implement project intake
fix: preserve approval boundary
test: cover invalid execution status

Commit message не должен заявлять больше, чем доказано.

Не использовать формулировки вроде:

complete AOS
finish governance
fully secure runtime
final fix
production ready

если это не подтверждено соответствующим scope и validation.

⸻

Commit authorization

Commit является отдельным действием.

До commit необходимо проверить:

* target files;
* diff;
* validation result;
* отсутствие unrelated staged files;
* соответствие задаче;
* отсутствие accidental secrets;
* отсутствие временных artifacts.

Даже после успешной проверки commit выполняется только после разрешения человека или заранее установленной политики.

Общая просьба изменить файл не означает автоматическое разрешение на commit.

⸻

Staging area

Git index должен использоваться осознанно.

Перед commit необходимо проверить:

git status --short
git diff
git diff --cached

Для ограниченной задачи предпочтительно добавлять конкретные paths:

git add AOS/00_Core/Project_Identity.md

Не следует автоматически выполнять:

git add .
git add -A

если в working tree присутствуют unrelated changes.

⸻

git add -N

git add -N может использоваться только для отображения diff нового untracked файла.

Он изменяет index state, хотя не добавляет полное содержимое в staged changes.

Поэтому его не следует называть полностью read-only действием.

После использования необходимо понимать состояние index и не оставлять неожиданные staged intents.

⸻

Проверка перед commit

Минимальная проверка документационного изменения:

git diff --check
git diff -- <target-file>

Перед commit:

git diff --cached --check
git diff --cached

Для code change дополнительно выполняются tests и проверки, объявленные задачей.

git diff --check проверяет whitespace errors, но не подтверждает правильность содержания.

⸻

Push boundary

Push публикует commits в remote repository.

Push может:

* сделать изменения видимыми другим участникам;
* запустить remote CI;
* создать remote branch state;
* повлиять на совместную работу.

Поэтому commit authorization не означает push authorization.

Перед push необходимо понимать:

* какой remote используется;
* какая branch будет обновлена;
* не выполняется ли force push;
* соответствует ли remote branch ожидаемому состоянию;
* разрешена ли публикация текущих commits.

⸻

Force push

Force push является потенциально destructive operation.

Без отдельного явного разрешения запрещены:

git push --force
git push -f

Даже --force-with-lease требует понимания последствий и отдельного разрешения, если branch используется другими людьми.

Force push не должен быть обычным способом исправления истории AOS.

⸻

Merge boundary

Merge объединяет одну линию истории с другой.

Merge authorization является отдельным человеческим решением.

До merge необходимо проверить:

* source branch;
* target branch;
* точный head;
* diff;
* validation;
* conflicts;
* unresolved findings;
* соответствие scope;
* допустимый merge method.

CI PASS не означает merge approval.

Push branch не означает разрешение объединить её с main.

⸻

Merge strategy

На раннем этапе AOS не требуется сложная merge policy.

Допустимые варианты могут включать:

* fast-forward;
* merge commit;
* squash merge;
* rebase before merge.

Один preferred method должен быть выбран позднее для конкретного repository.

Выбор метода не должен блокировать заполнение документации.

Главное требование — история должна оставаться понятной, а изменение проверяемым.

⸻

dev → main

Переход из dev в main должен происходить после того, как логический блок:

* завершён;
* проверен;
* не содержит известных blocking findings;
* принят человеком;
* не смешан с unrelated work.

Не требуется merge каждого отдельного документа немедленно.

Можно объединять логически связанный пакет, например:

active canonical package:
* [`Project Identity`](../00_Core/Project_Identity.md)
* [`Product Vision`](../01_Product/Product_Vision.md)
* [`Project Principles`](../00_Core/Project_Principles.md)
* [`Reconstruction Roadmap`](../05_Reference/Reconstruction_Roadmap.md)

Но пакет не должен становиться настолько большим, что review теряет точность.

⸻

Release boundary

Release означает предоставление версии пользователю или объявление устойчивого продукта.

Merge в main не означает release.

Tag не означает автоматически готовность продукта.

Release требует отдельного понимания:

* что входит в версию;
* какие функции доступны;
* какие ограничения известны;
* какая validation выполнена;
* как выполнить installation или upgrade;
* какие риски остаются;
* кто принял release decision.

На документационном этапе release process пока не требуется.

⸻

Tags

Tags могут использоваться для фиксации значимых устойчивых состояний.

Примеры:

docs-skeleton-v1
project-definition-v1
v0.1.0

Tag создаётся только после определения его смысла.

Не следует создавать множество tags для каждого промежуточного документа.

Annotated tags предпочтительнее для будущих releases, если нужен сопровождающий текст.

⸻

Git history не является approval log

Git показывает:

* кто создал commit;
* когда commit появился;
* какие files изменены.

Git сам по себе не доказывает:

* кто принял product decision;
* был ли выполнен human review;
* разрешён ли release;
* соответствует ли commit architecture;
* является ли содержание canonical.

Human decision может быть связан с commit, но commit не заменяет решение.

⸻

Revert

Для отмены уже опубликованного или принятого commit предпочтителен новый revert commit:

git revert <commit>

Это сохраняет историю.

git reset может использоваться для локальной незапушенной работы, но требует осторожности.

Агент не должен самостоятельно выбирать destructive history rewrite вместо безопасного revert.

⸻

Reset

Команды reset имеют разные последствия.

Без отдельного разрешения агент не должен выполнять:

git reset --hard

Потому что команда может удалить незакоммиченные изменения.

Даже git reset --soft и git reset --mixed должны применяться только при понимании состояния index и working tree.

⸻

Clean

Команда:

git clean

может удалить untracked files.

Она является destructive operation.

Без явного human authorization использовать её запрещено.

Temporary files следует контролировать через .gitignore и понятные temporary directories, а не массовым удалением неизвестного содержимого.

⸻

Checkout и restore

Команды восстановления файла могут перезаписать незакоммиченную работу.

Перед использованием:

git restore
git checkout -- <file>

необходимо проверить:

* содержит ли файл важные изменения;
* существует ли сохранённая копия;
* относится ли восстановление к разрешённому scope.

Общая просьба «отменить изменение» не должна интерпретироваться как разрешение удалить все локальные изменения.

⸻

Rebase

Rebase переписывает историю commits.

Он может быть полезен для локальной feature branch до публикации.

Rebase не должен:

* выполняться автоматически;
* использоваться на shared branch без решения;
* скрывать важную историю;
* совмещаться с незавершённой write-задачей.

Незавершённый rebase является stop condition для новой задачи.

⸻

Cherry-pick

Cherry-pick допустим, если необходимо перенести конкретный известный commit.

Перед выполнением нужно понимать:

* source commit;
* target branch;
* возможные conflicts;
* dependency на другие commits;
* соответствие текущему scope.

Cherry-pick не является заменой пониманию содержимого commit.

⸻

Worktree

Git worktree может использоваться для изоляции:

* validation;
* review;
* отдельной feature;
* сравнения baselines;
* parallel read-only analysis.

Worktree не требуется для каждой задачи.

Parallel write agents в разных worktrees допускаются только при независимых scopes и осознанной последующей integration.

По умолчанию предпочтителен один writer.

⸻

Remote configuration

Перед push или remote inspection необходимо понимать:

git remote -v

Агент не должен:

* менять remote URL;
* добавлять новый remote;
* удалять remote;
* менять authentication;
* отправлять данные во внешний repository;

без явного разрешения.

⸻

Secrets и Git

Перед commit необходимо исключить:

* API keys;
* passwords;
* tokens;
* private certificates;
* .env с реальными значениями;
* персональные данные;
* local credentials;
* machine-specific secrets.

Если secret попал в commit, простого удаления файла в следующем commit может быть недостаточно.

Такой случай требует отдельного security response и возможного history cleanup.

⸻

Large files

Большие binary files и repository snapshots не должны добавляться автоматически.

Перед добавлением нужно определить:

* действительно ли файл нужен;
* является ли Git подходящим storage;
* нужна ли Git LFS;
* можно ли хранить external reference;
* содержит ли файл sensitive data;
* можно ли воспроизвести его из source.

⸻

Generated artifacts

Generated artifacts добавляются в Git только если существует ясная причина.

Необходимо определить:

* canonical source;
* generation command;
* reproducibility;
* необходимость review;
* причину отслеживания.

Derived index может храниться в Git для удобства, но не становится самостоятельным Source of Truth.

⸻

Documentation workflow в Git

Для текущего этапа используется простой процесс:

создать или переписать один документ
→ проверить Markdown и содержание
→ посмотреть diff
→ провести review
→ создать commit после разрешения
→ продолжить следующий документ

Не требуется:

* отдельный PR для каждого абзаца;
* сложный approval package;
* automatic document lifecycle;
* generated status registry;
* отдельный recovery workflow.

⸻

Code workflow в Git

После появления implementation минимальный процесс:

определить bounded task
→ зафиксировать baseline
→ изменить ограниченный scope
→ добавить или обновить tests
→ выполнить validation
→ проверить diff
→ human review
→ commit
→ отдельно push
→ отдельно merge

Каждый последующий шаг сохраняет собственную границу.

⸻

Branch protection

Branch protection полезна для main, когда repository начинает использоваться как устойчивый источник.

Возможные требования:

* запрет force push;
* запрет прямого удаления branch;
* обязательный review;
* обязательные checks;
* запрет merge при конфликтах.

Protection не должна добавляться формально до понимания реального collaboration workflow.

Для личного раннего documentation repository простая дисциплина может быть достаточной.

⸻

CI и Git

Remote CI обычно запускается после push или pull request.

CI должен проверять технические условия.

CI не должен:

* выдавать human approval;
* автоматически принимать architecture;
* автоматически merge изменения без установленной политики;
* скрывать NOT_RUN;
* считать все неизвестные разрешёнными.

CI rules будут определены в отдельном документе Minimal Checks and CI.

⸻

Naming branches

Branch name должен быть коротким и понятным.

Рекомендуемые prefixes:

docs/
feature/
fix/
refactor/
test/
chore/
research/

Примеры:

docs/project-definition
feature/project-intake
fix/approval-boundary
research/legacy-inventory

Не использовать branch name как замену Task Brief или полному описанию scope.

⸻

Запрещённые Git-действия без отдельного разрешения

Агент не должен самостоятельно выполнять:

commit
push
merge
release
tag creation
branch deletion
remote modification
force push
hard reset
git clean
history rewrite
destructive restore

Если задача требует одно из этих действий, authorization должен быть явным и относиться именно к этому действию.

⸻

Минимальный Git preflight

Для обычной локальной задачи:

git rev-parse --show-toplevel
git branch --show-current
git rev-parse HEAD
git status --short

При работе в subtree:

git status --short -- AOS

При подозрении на незавершённую operation следует проверить Git state до записи.

⸻

Минимальный Git postflight

После изменения:

git status --short
git diff --check
git diff -- <target-path>

Перед commit:

git diff --cached --check
git diff --cached

После commit:

git show --stat --oneline HEAD
git status --short

Проверки должны быть ограничены текущей задачей.

⸻

Git report

После Git-задачи необходимо сообщить:

* repository root;
* branch;
* baseline commit;
* изменённые files;
* staged files;
* созданный commit, если разрешён;
* push status;
* merge status;
* remaining working tree changes;
* findings;
* одно следующее действие.

Не нужно создавать большой package для обычного документационного commit.

⸻

Ошибки, которых нужно избежать

Смешение всех разрешений

Фраза «сделай и отправь» может быть неоднозначной. Для существенных действий границы следует понимать явно.

git add . в dirty repository

Это может включить unrelated changes.

Commit с неизвестным содержимым

Commit создаётся только после просмотра staged diff.

Push как автоматическое продолжение commit

Remote publication является отдельным действием.

CI PASS как merge approval

Технические проверки не принимают human decision.

Force push как обычное исправление

History rewrite должен быть исключением.

Reset или clean для удобства агента

Нельзя удалять неизвестную пользовательскую работу.

Слишком длинные branches

Долгоживущая branch быстро расходится с baseline и усложняет integration.

Слишком крупные commits

Review становится формальным и теряется возможность локальной отмены.

Git как замена Project Memory

Git хранит изменения файлов, но не всегда объясняет intent, findings и следующее действие.

⸻

Критерий готовности Git Foundation

Git Foundation считается достаточно определённым, если человек или агент понимает:

1. где находится repository root;
2. где находится AOS project root;
3. какая branch используется для работы;
4. какой commit является baseline;
5. какие изменения относятся к задаче;
6. чем edit отличается от commit;
7. чем commit отличается от push;
8. чем push отличается от merge;
9. чем merge отличается от release;
10. какие Git-команды являются destructive;
11. когда требуется human authorization;
12. как проверить diff;
13. как не затронуть unrelated changes;
14. как оставить понятную историю.

⸻

Что не входит в Git Foundation

Этот документ не определяет:

* точную PR policy;
* обязательный merge method;
* release automation;
* semantic versioning;
* changelog format;
* organization-level branch rules;
* multi-repository integration;
* cryptographic commit signing;
* enterprise compliance;
* automatic merge authorization package.

Эти решения принимаются позднее при появлении соответствующей необходимости.

⸻

Следующее развитие

После Git Foundation необходимо определить:

[`Task and Report Templates`](../03_Development/Task_And_Report_Templates.md)

Этот раздел должен установить минимальный формат:

* bounded task;
* expected result;
* allowed scope;
* validation;
* stop conditions;
* итоговый report;
* findings;
* одно следующее действие.

Он не должен создавать сложную task database или lifecycle.
