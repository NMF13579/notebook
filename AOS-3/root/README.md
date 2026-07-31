# AOS

Этот repository предназначен для разработки AOS с использованием переносимого development package в `AOS-3/`.

## Начало работы

1. Прочитайте [`AOS-3/AGENTS.md`](AOS-3/AGENTS.md).
2. Проверьте [`AOS-3/development-package-state/CURRENT.md`](AOS-3/development-package-state/CURRENT.md).
3. Запустите package validation, указанную в `AOS-3/AGENTS.md`.
4. Выполните full target repository preflight.
5. Зафиксируйте first vertical slice отдельным human decision.
6. Подготовьте feature-specific Product Contract и bounded Task Brief.
7. Не начинайте mutation без отдельной Execution Authorization.

## Инструменты

- Codex и совместимые coding agents используют root [`AGENTS.md`](AGENTS.md).
- Antigravity использует workspace rule [`.agents/rules/aos.md`](.agents/rules/aos.md).
- В Antigravity проверьте, что workspace rule `.agents/rules/aos.md` активирован как `Always On`.

## Границы

```text
Package readiness ≠ implementation readiness
Task Brief ≠ Execution Authorization
PASS ≠ approval
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Текущее состояние и authoritative routing находятся внутри AOS-3/. Этот README не является Product Contract, Task Brief или permission record.
