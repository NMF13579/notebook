---
artifact_id: AOS3-R16-README
artifact_type: PORTABLE_PACKAGE_README
package_revision: DRAFT-R16
revision: R2
status: DRAFT
authority: ROUTING_ONLY
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# AOS-3 portable development package

`AOS-3/` переносится только как целая директория. Package является
documentation candidate и не является product runtime, implementation
repository, approval или permission.

Обязательная входная точка: [`AGENTS.md`](AGENTS.md). Current-state owner:
[`development-package-state/CURRENT.md`](development-package-state/CURRENT.md).

Greenfield root payload находится в [`root/`](root/) и governed exact copy
contract [`ROOT_FILES_MANIFEST.yaml`](ROOT_FILES_MANIFEST.yaml). Его
materialization является отдельной human-authorized target bootstrap mutation;
она не поддерживает automatic existing-repository adoption и не заменяет full
target repository preflight.

Все обязательные operational owners находятся внутри `AOS-3/`. Исторические
artifacts и references сохраняются для provenance, но не заменяют `CURRENT.md`
как current-state route.
