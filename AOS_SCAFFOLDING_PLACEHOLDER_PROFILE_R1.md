---
document_type: AOS_SCAFFOLDING_CONTRACT_CORRECTION
revision: DRAFT-R1
status: HUMAN_REVIEW_REQUIRED
claim_class: DRAFT_CONTRACT_CANDIDATE
authority: NONE_UNTIL_HUMAN_ACCEPTANCE
authority_scope: PRODUCT_CLI_PLACEHOLDER_RESULT_AND_TEST_PROFILE_ONLY
task_id: DOC-012-CORRECTION-F-001
technical_result: PASS
readiness: READY_FOR_INDEPENDENT_REVALIDATION
human_acceptance: NOT_RUN
accepted_scaffold_contract: AOS_SCAFFOLDING_CONTRACT_R1.md
accepted_scaffold_contract_sha256: 2a76e94dc9ea534a89d045bd428a0f5b2f1be64b6824c0f7462f2529a6e17901
accepted_task: Task-001-Scaffolding.md
accepted_task_sha256: afdbd462be3907d1bd7224e072f05bc11fd06371996bfeb75aeb58ae734b938c
accepted_subjects_modified: false
runtime_implementation: NOT_RUN
execution_authorization: NOT_RUN
git_authorization: NONE
created: 2026-08-05
---

# AOS-3 — Product CLI Placeholder Result Profile R1

## 1. Bounded correction

Accepted scaffold subjects require a product CLI placeholder to remain honestly `NOT_IMPLEMENTED`, but the accepted `aos.dev-result.v1` technical vocabulary is closed and does not contain `NOT_IMPLEMENTED`.

This candidate does not add a technical result and does not modify either accepted subject. It defines the only compatible interpretation for future Task-001 consumers:

```text
NOT_IMPLEMENTED = stable reason code, not technical_result
technical_result = BLOCKED
exit_code = 5
```

The mapping is a narrow validation/compatibility overlay. It neither implements Product Runtime nor changes Task-001 scope, command surface, repository paths, permissions or recovery boundary.

## 2. Exact placeholder terminal profile

When `./aos-dev run -- ARGS` reaches the scaffold placeholder before any Product Runtime slice exists, it MUST:

1. perform zero Product Runtime/state writes;
2. emit exactly one `aos.dev-result.v1` terminal result;
3. set `technical_result: BLOCKED`;
4. return exit code `5` (`blocked identity/scope/permission/network precondition` class, here scope capability absent);
5. place stable reason code `PRODUCT_RUNTIME_NOT_IMPLEMENTED` as the first `limitations` item;
6. include no required check with `PASS` that claims Product Runtime availability;
7. set `next_action` to one bounded human-readable action that requires a separate accepted Product Runtime Task Brief and Execution Authorization;
8. preserve repository bytes, Git status and `.aos/state/`/`.aos/records/` exactly.

Exact semantic example:

```json
{
  "schema_version": "aos.dev-result.v1",
  "command": "run",
  "technical_result": "BLOCKED",
  "required_checks": [],
  "optional_checks": [],
  "writes": [],
  "limitations": ["PRODUCT_RUNTIME_NOT_IMPLEMENTED"],
  "unknowns": [],
  "next_action": "Prepare and human-accept a separate Product Runtime Task Brief before requesting execution authorization"
}
```

The example is semantic: canonical JSON ordering remains owned by the eventual accepted result schema/implementation. No new field is introduced.

## 3. Stable requirement and executable tests

| ID | Requirement | Positive oracle | Negative oracle | Future Evidence |
|---|---|---|---|---|
| `SCF-PRT-001` | unavailable Product Runtime returns honest placeholder result | exact command emits `BLOCKED`, exit `5`, reason code, zero writes | `PASS`, exit `0`, `NOT_IMPLEMENTED` as technical result, missing reason, or any state/product write | command/output/exit record + before/after repository/status/state digest |

Required fixtures:

| Fixture | Input | Expected result |
|---|---|---|
| `SCF-PRT-ACC-001-placeholder` | clean scaffold, Product Runtime absent, `./aos-dev run -- status` | profile section 2 exact semantics |
| `SCF-PRT-NEG-001-false-pass` | placeholder returns `PASS`/exit `0` | test `FAIL`; implementation cannot claim Task-001 PASS |
| `SCF-PRT-NEG-002-new-result-enum` | `technical_result: NOT_IMPLEMENTED` | schema/contract violation |
| `SCF-PRT-NEG-003-missing-reason` | `BLOCKED` without stable reason in `limitations[0]` | test `FAIL` |
| `SCF-PRT-NEG-004-placeholder-writes` | command changes source, Git state or Project Memory paths | test `FAIL`; recovery/scope audit required |
| `SCF-PRT-NEG-005-auto-feature` | placeholder generates or selects Product Runtime work | blocked scope expansion |

`SCF-PRT-001` becomes mandatory only if this exact correction is human-accepted. Until implementation exists, every runtime fixture result is `NOT_RUN`.

## 4. Recovery and stop behavior

| Failure | Preserved facts | Recovery | Revalidation |
|---|---|---|---|
| wrong result/exit/reason | source and accepted contracts | bounded Task-001 implementation correction | full placeholder fixture set + exit table |
| placeholder wrote state | journal/actual diff/user state | stop; use accepted Task-001 recovery boundary; no auto-clean | intended/actual reconciliation + forbidden-path audit |
| Product Runtime unexpectedly present | observed bytes and current task scope | stop as scope conflict; require separate feature/task decision | fresh preflight + exact Product Runtime contract |

No test may repair a subject, create Product Runtime behavior or convert this technical profile into Execution Authorization.

## 5. Traceability and ownership

| Fact | Owner |
|---|---|
| closed technical result and exit table | accepted `AOS_SCAFFOLDING_CONTRACT_R1.md` §9.2 |
| Product Runtime exclusion | accepted `Task-001-Scaffolding.md` §§1, 4, 6 |
| exact placeholder mapping/test profile | this candidate only |
| Task-001 paths/operations/recovery | accepted Task-001 and scaffold contract; unchanged |
| human acceptance/permissions | explicit separate decisions only |

## 6. Candidate status

```yaml
finding: F-001
resolution: DOCUMENTED_AS_PROVISIONAL_COMPATIBILITY_PROFILE
technical_result: PASS
human_acceptance: NOT_RUN
accepted_subjects_modified: false
runtime_implementation: NOT_RUN
runtime_tests: NOT_RUN
execution_authorization: NOT_RUN
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: INDEPENDENT_READ_ONLY_DOC-012_REVALIDATION
stop: false
```
