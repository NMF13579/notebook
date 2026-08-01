---
artifact_id: AOS3-R17-ENTRYPOINT
artifact_type: PORTABLE_PACKAGE_ENTRYPOINT
package_revision: DRAFT-R17
revision: R3
status: DRAFT
authority: ROUTING_ONLY
portable_package_root: AOS-3/
mandatory_first_read: development-package-state/CURRENT.md
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# AOS-3 portable package entrypoint

`AOS-3/` — единая переносимая package boundary. Копируй всю директорию; не
выбирай отдельные файлы. Наличие package не назначает implementation
repository и не создаёт implementation, Git или release permissions.

## Mandatory first read

Прочитай ровно один current-state owner:
[`development-package-state/CURRENT.md`](development-package-state/CURRENT.md).
Не определяй current state по timestamp, имени старого candidate или
frontmatter frozen artifact.

## Package-local route

После `CURRENT.md` используй только нужного owner:

- authority и source precedence:
  [`development-package/00_Control_and_Source_Precedence.md`](development-package/00_Control_and_Source_Precedence.md);
- portability direction:
  [`development-package-state/PORTABILITY_DIRECTION_2026-07-31.md`](development-package-state/PORTABILITY_DIRECTION_2026-07-31.md);
- active subject roles:
  [`development-package-state/SUBJECT_STATE_REGISTRY_R17.md`](development-package-state/SUBJECT_STATE_REGISTRY_R17.md);
- root payload copy contract:
  [`ROOT_FILES_MANIFEST.yaml`](ROOT_FILES_MANIFEST.yaml);
- target root payload source: [`root/`](root/);
- bootstrap и task derivation:
  [`development-package/07_Implementation_Handoff.md`](development-package/07_Implementation_Handoff.md);
- templates: [`templates/`](templates/);
- author self-check:
  `python3 AOS-3/validation/validate_portable_package.py`.

Все обязательные operational routes находятся внутри `AOS-3/`. Материалы
вне package, source repository name и chat history не являются operational
dependencies.

## Separate target bootstrap

Root payload materialization — отдельный target bootstrap stage, а не
автоматически разрешённая mutation или prerequisite для product selection:

1. Скопируй весь `AOS-3/` в observed greenfield target repository.
2. Запусти package author self-check.
3. Получи отдельную human authorization на root materialization exact target.
4. Выполни `PREFLIGHT_ALL_TARGET_PATHS` из `ROOT_FILES_MANIFEST.yaml`; до полного
   `PASS` не записывай ни один target path.
5. Копируй только missing paths raw bytes; identical paths являются `NOOP`.
   Любой differing path блокирует весь payload до записи. Post-copy failure
   откатывает только paths, созданные текущим run, и сохраняет source payload.
6. После materialization отдельно проверь созданные paths. Full target
   repository preflight остаётся отдельным read-only stage и требуется только
   перед target binding, Target-Bound Task Brief или physical implementation
   planning.

Поддерживается только `GREENFIELD_OR_EMPTY_ROOT`. Existing repository adoption
требует отдельного human decision и task. Root materialization preflight не
является full target repository preflight.

## Product-to-target order

Не выбирай feature или vertical slice. Запроси exact human decision через
`FIRST_VERTICAL_SLICE_SELECTION.template.md`. Отсутствие выбора не является
package failure: оно блокирует только dependent Feature Contract, Task
derivation и implementation planning.

```text
human first vertical slice selection
→ feature-specific Product/Feature Contract draft
→ human acceptance of exact Feature Contract
→ minimum Portable Task Candidate
→ exact target repository assignment
→ read-only target preflight and Target Repository Binding
→ Target-Bound Task Brief
→ human Task decision
→ human-assigned Risk Profile
→ separate Execution Authorization
→ one bounded implementation stage
```

Target repository не требуется для slice selection, portable Feature Contract
или Portable Task Candidate. После exact human repository assignment выполни
full read-only target preflight и создай Target Repository Binding только из
direct observations. Не угадывай repository, branch, HEAD, paths, toolchain,
dependencies или commands.

## Conflict and unknown route

При `CONFLICT` или material `UNKNOWN`:

1. укажи confirmed owners;
2. процитируй exact conflict/unknown;
3. назови affected claim/action;
4. заблокируй только affected action;
5. запроси один human resolution step;
6. не заменяй отсутствующий факт inference.

Всегда сохраняй:

```text
Documentation ≠ implementation
PASS ≠ approval
Readiness ≠ permission
Task Brief ≠ Execution Authorization
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```
