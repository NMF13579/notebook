---
trigger: always_on
---

# AOS Documentation Repository — Workspace Rule

Activation: Always On

Используй `@/AGENTS.md` как основной repository contract и `@/docs/00_Core.md` как обязательную точку входа.

Этот workspace является принятой project knowledge baseline AOS, а не implementation repository.

Обязательные правила:

- Не создавай runtime-код AOS, CI/CD продукта, deployment или database в этом repository.
- Не создавай параллельные knowledge catalogs и не дублируй fact owners.
- Открывай только релевантные документы из `docs/`; не загружай весь legacy без конкретного gap.
- `docs/06_Features.md` — inventory, не roadmap и не execution contract.
- Перед implementation planning выбранная feature требует feature-specific Product Contract и architecture decision при необходимости.
- AOS-FARM и AgentOS исследуются только read-only, по exact repository/ref/commit/path.
- Не выполняй hidden network calls, terminal mutations или writes вне workspace.
- Не выполняй Commit, Push, Merge или Release без отдельного explicit human decision.
- Не симулируй approval и не превращай PASS/Evidence в authority.

При write-задаче сначала зафиксируй goal, target paths, allowed/forbidden changes, validation и stop conditions. После изменения проверь Markdown, links, YAML, IDs и `git diff --check`, затем остановись с отчётом.

```text
Documentation ≠ implementation
PASS ≠ approval
Evidence ≠ approval
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```
