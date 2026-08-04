# Repository agent entrypoint

Этот repository использует переносимый development package AOS, расположенный в `AOS-3/`.

## Обязательная точка входа

Перед planning, созданием Task Brief или изменением repository прочитай:

1. `AOS-3/AGENTS.md`
2. `AOS-3/development-package-state/CURRENT.md`

`AOS-3/AGENTS.md` является canonical instruction owner переносимого package. Этот root-файл — только repository-wide router.

## Рабочие границы

- Начинай с `PLAN` и read-only observation, если current explicit human authorization не разрешает mutation.
- Перед repository-bound planning или mutation выполни full target repository preflight.
- Не выбирай feature, Product Contract, architecture, dependency, Risk Profile или implementation scope от имени человека.
- Не считай package presence, readiness, Evidence или technical `PASS` разрешением на execution.
- `Task Brief ≠ Execution Authorization`.
- `PASS ≠ approval`.
- `Edit ≠ Commit ≠ Push ≠ Merge ≠ Release`.
- Commit, Push, Merge и Release требуют отдельных explicit human permissions.
- При `CONFLICT`, material `UNKNOWN` или subject drift следуй route из `AOS-3/AGENTS.md`; не угадывай.

## Tool-specific adapters

- Codex и совместимые coding agents используют этот `AGENTS.md`.
- Antigravity workspace rule находится в `.agents/rules/aos.md`.
- Все adapters направляют к одним и тем же owners внутри `AOS-3/`.
