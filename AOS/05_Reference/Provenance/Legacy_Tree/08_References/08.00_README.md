Раздел `08_References` сохраняет происхождение знаний, использованных при реконструкции AOS, и задаёт безопасные правила их применения.

Его задача — перенести в новый проект полезный опыт, проверенные contracts, observable behavior, lessons и failure modes, не превращая старые проекты, чаты или внешние материалы в Source of Truth.

## Основной принцип

Новый AOS является самостоятельным проектом.

`NMF13579/AOS-FARM`, AgentOS, AOS-1 и другие исторические материалы используются только как `READ_ONLY_REFERENCE` с `authority: NONE`.

Допустимая цепочка переноса знания:

```text
Reference
→ Analysis
→ Extracted knowledge
→ Verification
→ Project decision
→ Canonical AOS document
```

Недопустимая цепочка:

```text
Legacy project
→ Copy
→ New project foundation
```

## Состав раздела

- `08.01_Reference_Policy` — общие правила работы с reference materials.
- `08.02_Knowledge_Extraction` — процедура извлечения и проверки знаний.
- `08.03_AOS_FARM` — границы использования AOS-FARM.
- `08.04_AgentOS_AOS1` — границы использования AgentOS и AOS-1.
- `08.05_External_References` — внешние проекты, стандарты и публикации.
- `08.06_Research_Materials` — исследовательские материалы и гипотезы.
- `08.07_Source_Conversations` — исторические чаты и handoff materials.
- `08.08_Reference_Catalog` — правила каталога источников и traceability.
- `08.09_Historical_Archive` — superseded и obsolete reference artifacts.

## Граница authority

Материал в этом разделе может объяснять происхождение идеи, но сам по себе не определяет:

- architecture;
- Source of Truth;
- approval;
- lifecycle;
- Risk Profile;
- execution authorization;
- implementation readiness;
- commit, push, merge или release authority.

Такие решения могут существовать только в соответствующих документах нового AOS после отдельного human decision.
