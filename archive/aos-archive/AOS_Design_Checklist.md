---
artifact_id: AOS-DESIGN-CHECKLIST-001
artifact_type: HUMAN_READABLE_DESIGN_CHECKLIST
status: PROPOSAL
fact_class: SYNTHESIZED
authority: NONE
source_of_truth: false
human_acceptance: NOT_GRANTED
implementation_authorization: NONE
git_authorization: NONE
---

# AOS Design Checklist

## Назначение

Этот документ определяет, на какие концептуальные вопросы должна отвечать документация проекта, чтобы по ней можно было последовательно спроектировать и создать сам инструмент AOS.

Документ предназначен для:

- проверки полноты проектной документации;
- обнаружения пробелов, конфликтов и неподтверждённых предположений;
- определения решений, которые ещё должен принять человек;
- построения roadmap на основе реально недостающих знаний;
- предотвращения преждевременного перехода к реализации;
- сохранения различия между target AOS, Core v1, first Product Runtime slice и поздними extensions.

Этот документ не является Source of Truth, Product Contract, roadmap, Task Brief, approval или authorization.

Ответы должны храниться в профильных документах-владельцах. Сам checklist только помогает определить, какие вопросы уже закрыты, где находятся ответы и какие gaps ещё требуют решения.

## Как использовать checklist

Для каждого material question нужно определить:

- есть ли обоснованный ответ;
- где находится Source of Truth;
- к какому горизонту относится вопрос;
- является ли ответ принятым фактом, направлением, proposal, observation или inference;
- есть ли conflict;
- какой ближайший artifact, decision или action зависит от ответа;
- должен ли gap закрываться сейчас или может быть отложен.

Допустимые результаты semantic review:

```text
COVERED
PARTIAL
CONFLICT
NOT_FOUND
NOT_APPLICABLE
```

Эти результаты показывают только полноту документального ответа.

```text
COVERED ≠ accepted feature
COVERED ≠ implementation-ready
COVERED ≠ validated
COVERED ≠ authorized
```

---

Сначала нужно определить, что такое AOS и какой горизонт мы создаём.

- Что представляет собой AOS как продукт?
- Какую фундаментальную проблему он решает?
- Для кого AOS создаётся в первую очередь?
- Какую работу пользователь передаёт AOS?
- Какую ценность AOS должен давать без полной Development Factory и automation?
- Чем AOS отличается от IDE, coding agent, orchestration framework и набора prompts?
- Какие свойства AOS являются неизменными независимо от версии?
- Что является target AOS?
- Что является independently useful AOS Core?
- Что должно войти в Core v1?
- Что должно войти только в first Product Runtime slice?
- Что относится к более поздним extensions?
- Какие возможности должны оставаться возможными архитектурно, но не реализовываться сейчас?
- Где заканчивается AOS и начинается внешний инструмент?
- Что AOS принципиально не должен делать?
- Во что AOS не должен превратиться?
- Как не принять target architecture за MVP?
- Какое изменение контекста потребует пересмотреть границу Core?

Затем нужно определить, для кого существует AOS и какую работу он выполняет.

- Кто является первым пользователем AOS?
- Каков его реальный job-to-be-done?
- В какой ситуации он обращается к AOS?
- Как пользователь решает эту задачу сегодня?
- Какие проблемы возникают в текущем процессе?
- Какие из этих проблем AOS должен решить первым?
- Какой результат пользователь считает полезным?
- Что пользователь должен увидеть, понять или суметь сделать?
- Как выглядит минимально полезный результат?
- Какие пользователи и use cases не входят в первую версию?
- Кто ещё будет затронут работой AOS?
- Какие решения пользователь хочет сохранить за собой?
- Как пользователь понимает, что AOS помогает, а не усложняет процесс?
- Какие признаки покажут, что AOS создаёт новую ценность?
- Что произойдёт, если AOS не будет создан?
- Почему AOS нужен как отдельный инструмент, а не как набор инструкций?

После этого нужно описать bounded operating loop и observable behavior AOS.

- Как начинается работа с AOS?
- Как выглядит First-Start?
- Как пользователь сообщает намерение?
- Как AOS отделяет problem, desired outcome и proposed solution?
- Как AOS обнаруживает assumptions, unknowns и contradictions?
- Какие вопросы AOS задаёт человеку?
- Какие ответы AOS должен получать самостоятельно из доступных источников?
- Какой первый user-visible artifact создаёт AOS?
- Как определяется current subject?
- Как определяется exact revision?
- Как выглядит основной end-to-end operating loop?
- Какие состояния проходит работа?
- Какие переходы между состояниями допустимы?
- Какие переходы запрещены?
- Как пользователь видит current status?
- Как пользователь видит blocker?
- Как пользователь видит one next action?
- Как AOS показывает `UNKNOWN`, `NOT_FOUND`, `NOT_RUN`, `BLOCKED`, `PASS` и `FAIL`?
- Когда AOS должен продолжать самостоятельно?
- Когда AOS обязан остановиться?
- Как AOS объясняет причину остановки?
- Как пользователь исправляет понимание AOS?
- Как продолжается работа после interruption?
- Как один agent environment передаёт работу другому?
- Как AOS завершает bounded stage?
- Что считается завершением всего user journey?
- Как operating loop работает без Development Factory и optional modules?

Теперь нужно определить state, artifacts, identity и persistence.

- Какие основные сущности существуют в AOS?
- Какие artifacts создаёт AOS?
- Какую роль имеет каждый artifact?
- Кто владеет каждым fact class?
- Какие artifacts являются canonical?
- Какие representations являются derived и rebuildable?
- Какие данные должны храниться постоянно?
- Какие данные можно пересоздать?
- Какие данные являются временными?
- Где хранится durable state?
- Как определяется identity artifact?
- Как определяется identity revision?
- Как определяется identity subject?
- Как определяется identity candidate?
- Как связываются intent, Product Contract, Task Brief, Authorization, Result, Evidence и Human Decision?
- Как определяется stale state?
- Как определяется superseded artifact?
- Как сохраняется история human decisions?
- Как обнаруживается partial write?
- Как выполняется atomic update?
- Как выполняется idempotent retry?
- Как выполняется recovery после сбоя?
- Как пользователь восстанавливает работу после повреждения state?
- Как изменяются schemas?
- Как выполняются migrations?
- Как обновление AOS сохраняет пользовательские данные?
- Какие данные не должны храниться?
- Как определяется срок жизни временных artifacts?
- Как предотвращается расхождение между canonical и derived data?

Затем нужно установить human authority, trust и safety boundaries.

- Какие решения AOS может принимать самостоятельно?
- Какие решения AOS может только рекомендовать?
- Какие решения принимает только человек?
- Какие действия требуют explicit human authorization?
- Как представляется authorization?
- К какому exact subject, revision и scope относится authorization?
- Когда authorization становится недействительной?
- Как различаются Plan, Execute, Validate и Review?
- Как различаются technical result, recommendation и Human Decision?
- Как разделяются Edit, Commit, Push, Merge и Release?
- Какие действия запрещены по умолчанию?
- Как AOS предотвращает hidden scope expansion?
- Как AOS обнаруживает изменение assumptions во время работы?
- Как AOS действует при `CONFLICT`?
- Как AOS действует при `UNKNOWN`?
- Как AOS блокирует только затронутый action?
- Какие operations являются reversible?
- Какие operations являются protected?
- Как выполняется rollback?
- Что происходит при утрате connection с внешним agent environment?
- Как AOS защищается от инструкций внутри repository content?
- Как внешние данные отделяются от trusted instructions?
- Как permissions сохраняются при смене adapter или provider?
- Какие audit/evidence данные обязательны?
- Как optional module доказывает, что не ослабляет Core safety?

После этого можно определить architecture responsibilities, ports и dependencies.

- Какие responsibility boundaries существуют в target AOS?
- Какие из них обязательны для Core v1?
- Какие из них физически нужны в first slice?
- Какие границы достаточно сохранить архитектурно?
- Какие компоненты относятся к Interaction Surface?
- Какие компоненты относятся к Product Runtime?
- Какие компоненты относятся к Development Factory?
- Какие компоненты относятся к Safety and Authority?
- Какие компоненты относятся к Knowledge and State?
- Какие компоненты являются optional modules?
- Какой компонент владеет каждым fact class?
- Какие contracts связывают компоненты?
- Какие ports нужны между Core и внешними systems?
- Какие adapters нужны?
- Какие dependencies являются обязательными?
- Какие dependencies можно заменить?
- Какие dependencies не должны проникать в Core?
- Где заканчивается deterministic logic?
- Где начинается LLM-generated proposal?
- Какие решения должны быть deterministic?
- Какие данные могут быть переданы LLM?
- Какие данные не должны покидать local boundary?
- Как component failure влияет на остальные части?
- Как Core работает при отключённых modules?
- Как module подключается?
- Как module удаляется?
- Какие criteria оправдывают выделение нового module?
- Как избежать преждевременного Control Plane?
- Как избежать преждевременной multi-agent architecture?
- Как избежать переноса legacy topology без contract justification?

Отдельно нужно определить integration с agent environments и repositories.

- Является ли AOS executor или управляет внешним executor?
- Какие действия выполняет сам AOS?
- Какие действия выполняет coding agent?
- Какие действия остаются за человеком?
- Как AOS передаёт bounded instruction внешнему agent?
- Как agent возвращает Result и Evidence?
- Как проверяется соответствие Result разрешённому scope?
- Как AOS работает с разными coding-agent environments?
- Как thin adapter получает правила, не копируя Source of Truth?
- Как adapter объявляет свои capabilities?
- Как adapter объявляет ограничения?
- Что происходит при adapter failure?
- Что происходит при частично выполненной external operation?
- Как AOS работает без конкретного provider или model?
- Как определяется current repository?
- Как определяется current branch и baseline?
- Как AOS работает с несколькими repositories?
- Что принадлежит AOS repository?
- Что принадлежит пользовательскому repository?
- Где AOS может создавать artifacts?
- Как repository observation отличается от accepted fact?
- Как AOS предотвращает mutation без authorization?
- Как AOS подтверждает фактическое состояние repository перед действием?
- Как выполняется handoff между ChatGPT, Codex, AntiGravity и другими environments?

Затем нужно определить installation, operation, recovery и update.

- Где устанавливается AOS?
- Может ли AOS работать отдельно от пользовательского repository?
- Как выглядит установка?
- Какие prerequisites необходимы?
- Как создаётся local state?
- Как проверяется исправность installation?
- Как выглядит First-Start для непрограммиста?
- Как пользователь выбирает или подключает repository?
- Как AOS диагностирует missing dependencies?
- Может ли AOS работать offline?
- Какие network dependencies допустимы?
- Какие provider dependencies допустимы?
- Как выполняется update?
- Как выполняется rollback update?
- Как выполняется uninstall?
- Что происходит с пользовательскими данными при uninstall?
- Как AOS переносится между компьютерами?
- Как обеспечивается portability между macOS и Linux?
- Как обеспечивается portability между agent environments?
- Как пользователь восстанавливается после повреждения installation?
- Какие diagnostics доступны пользователю?
- Как AOS сообщает degraded mode?
- Какие operations остаются доступными в degraded mode?
- Как AOS защищает собственное state от случайного изменения пользовательским проектом?

После этого нужно выбрать first slice и отложенную complexity.

- Какой first user выбран?
- Какой exact job-to-be-done выбран?
- Какой observable outcome должен дать first slice?
- Какой smallest useful vertical slice проверяет ценность AOS?
- Какие exact behaviors входят в slice?
- Какие behaviors не входят?
- Какие feature dossiers содержат нужные capabilities?
- Какие item-level human dispositions требуются?
- Какие capabilities можно выполнить вручную?
- Что не следует автоматизировать до dogfood?
- Какой interface достаточен для first slice?
- Какие artifacts обязательны?
- Какие states обязательны?
- Какие failure/recovery paths обязательны?
- Какие dependencies обязательны?
- Какие dependencies можно исключить?
- Какие architecture decisions нужны до slice?
- Какие architecture decisions можно отложить?
- Какой Product Contract нужен до implementation planning?
- Какие executable negative scenarios обязательны?
- Какие признаки покажут, что slice полезен?
- Какие результаты покажут, что выбран неправильный slice?
- Какие reversal conditions остановят развитие направления?
- Как не допустить расширения slice до полной платформы?

Теперь можно определить Development Scaffold и technical choices.

- Какой repository является implementation repository?
- Какой baseline используется?
- Какая repository topology минимально необходима?
- Какой language выбран?
- Какой runtime выбран?
- Почему этот language/runtime подходит first slice?
- Какие alternatives рассматривались?
- Какие technical choices трудно будет изменить?
- Какой dependency model допустим?
- Какие dependencies запрещены без measured need?
- Как воспроизводится development environment?
- Какие platform targets обязательны?
- Как выглядит минимальная package structure?
- Как выглядит минимальная test structure?
- Как выглядит official validation entrypoint?
- Как scaffold доказывает build/test reproducibility?
- Как scaffold не выдаёт себя за реализованный AOS?
- Какие checks обязательны до first behavior?
- Какие checks можно отложить?
- Как фиксируется toolchain?
- Как выполняется dependency update?
- Как предотвращается schema/runtime drift?
- Как предотвращается docs/runtime drift?
- Как development workflow сохраняет Edit ≠ Commit ≠ Push ≠ Merge ≠ Release?
- Какие artifacts создаются до implementation?
- Какие artifacts создаются после implementation?
- Какие действия требуют отдельной Git authorization?

Затем нужно определить validation, non-functional requirements и dogfood.

- Какие user journeys должны работать end-to-end?
- Что доказывает достаточность Product Definition?
- Что доказывает достаточность Core architecture?
- Что доказывает достаточность selected Product Contract?
- Что доказывает воспроизводимость Development Scaffold?
- Что доказывает работоспособность first slice?
- Что доказывает пригодность для manual dogfood?
- Какие positive scenarios обязательны?
- Какие negative scenarios обязательны?
- Какие recovery scenarios обязательны?
- Какие authority scenarios обязательны?
- Как проверяется отсутствие hidden scope expansion?
- Как проверяется persistence?
- Как проверяется recovery после partial failure?
- Как проверяется смена agent environment?
- Как проверяется portability?
- Какие reliability guarantees обязательны?
- Какой failure mode допустим?
- Какие операции должны быть deterministic?
- Какова допустимая latency?
- Какова допустимая стоимость одной операции?
- Каков допустимый startup context?
- Каков допустимый task-scoped context?
- Какие privacy boundaries обязательны?
- Какие security boundaries обязательны?
- Какие accessibility требования обязательны?
- Как проверяется понятность для непрограммиста?
- Какие observability данные обязательны?
- Какие Evidence нужны для human review?
- Что остаётся `NOT_RUN` после каждого milestone?
- Какое Human Decision завершает каждый milestone?
- Сколько manual real-task cycles нужно до обсуждения automation?
- Какие measured failures оправдывают automation?
- Какие данные dogfood должны привести к пересмотру Product Contract?

В завершение нужно определить evolution, compatibility, maintenance и acceptance.

- Как эволюционируют contracts?
- Как определяется breaking change?
- Как определяется compatibility target?
- Как выполняются migrations?
- Как выполняется deprecation?
- Как выполняется sunset устаревшего behavior?
- Как feature становится частью Core?
- Как feature остаётся optional?
- Как module принимается?
- Как module отклоняется?
- Как module удаляется?
- Какие dependencies должны оставаться replaceable?
- Как проверяется drift между docs, schemas, runtime и adapters?
- Какие reversal conditions имеет крупное решение?
- Какие решения требуют нового Architecture Decision?
- Как lessons превращаются в regression cases?
- Как не превращать единичную ошибку в постоянную ceremony?
- Как AOS сохраняет minimal task-scoped context?
- Когда Development Factory действительно нужна?
- Какие measured needs оправдывают Control Plane?
- Какие measured needs оправдывают multi-agent routing?
- Как определяется поддерживаемая версия?
- Кто отвечает за maintenance?
- Как определяется end-of-life?
- Какие Evidence нужны для acceptance Core v1?
- Какие Evidence нужны для acceptance first slice?
- Какие Evidence нужны для acceptance automation?
- Кто принимает окончательное решение?
- Что acceptance разрешает?
- Что acceptance не разрешает?
- Как следующий разработчик или agent понимает current state и one next action?

## Проверка полноты документации

После material изменения документации агент должен уметь ответить:

- Какие вопросы из checklist затронуты?
- Какие ответы изменились?
- В каком документе находится каждый ответ?
- Является ли документ владельцем этого fact class?
- Каков fact class ответа?
- Какие ответы являются partial?
- Где существуют conflicts?
- Какие вопросы не применимы к текущему horizon?
- Какие вопросы относятся к более позднему horizon?
- Какие gaps блокируют ближайшее решение?
- Какие gaps можно отложить?
- Какой один owner document должен быть обновлён?
- Какое Human Decision требуется?
- Какой один следующий bounded action?

## Граница использования

Checklist применяется для:

- design audit самого AOS;
- построения и пересмотра roadmap;
- выбора first user и first slice;
- Product/Core architecture review;
- подготовки feature-specific Product Contract;
- проверки крупных изменений baseline.

Checklist обычно не применяется для:

- routine implementation task с полным Product Contract и Task Brief;
- VALIDATE frozen subject;
- повторного planning уже принятого bounded task;
- Git delivery;
- задач без material product/architecture uncertainty.
