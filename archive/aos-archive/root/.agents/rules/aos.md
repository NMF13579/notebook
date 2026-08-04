# AOS workspace rule

@../../AOS-3/AGENTS.md
@../../AOS-3/development-package-state/CURRENT.md

Всегда используй указанные package files как обязательную точку входа для работы в этом workspace.

- Не дублируй и не переопределяй их authority.
- Начинай с `PLAN` и read-only observation, если explicit human authorization не разрешает mutation.
- Не выводи implementation или Git permission из package presence, readiness, Evidence или `PASS`.
- `Task Brief ≠ Execution Authorization`.
- Commit, Push, Merge и Release являются отдельными human permissions.
- При material conflict или unknown останови только затронутый action и используй conflict route из `AOS-3/AGENTS.md`.
