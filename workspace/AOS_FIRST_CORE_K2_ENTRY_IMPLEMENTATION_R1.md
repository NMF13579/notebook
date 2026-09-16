# K2 entry — temporary supervised development package R1

> Historical preparation snapshot. Its pending/NOT_RUN labels describe the
> original subject and do not restart work. For the accepted result and next
> chat, read [current continuation](AOS_CORE_CONTINUATION_PLAN.md).

Subject: AOS-FIRST-CORE-001/K2-ENTRY-IMPLEMENTATION-R1.
Status: PREPARED / WAIT_HUMAN_REVIEW. Proposed profile not yet accepted for execution.
Current authority: documentation preparation only. Implementation/checks: NOT_RUN.
This derived package owns no Product/Architecture contract and grants no execution.

## 1. Baseline and bounded outcome

W = `/Users/muhammed/Documents/GitHub/AOS-3-first-core-20260915`.
Baseline source: 17-file manifest in W/.first-core-state/K2-SUPPORT-CORRECTION-001.json,
accepted candidate `76231d4acae9c0778ebdc28ca217725b1e8031c52ec15d627a2365b23fa34b1b`.
Observed historical base `e99cc3ee03128deb4506bc268839ebd1f52a3f3a`, branch
`codex/first-core-20260915`. Fresh preflight must recheck both plus all source hashes.
The 83-test support result is historical evidence, not a pass for future edits.

[Preflight R2](AOS_FIRST_CORE_K2_PREFLIGHT_R2.md) records the accepted support result,
actual-effect target proposal and unresolved native guarantees. This package selects
only its next development slice: read-only real-task intake/binding and preview.
The public CLI currently exposes K1 checks and fixture-state inspection, not this entry.

Outcome: given source-bound K1 input/draft, a declared current subject and an exact
proposed action, emit a reviewable K2 preview with explicit structural matches,
conflicts, missing evidence and real launch blockers. This materially connects
K1 C-005 output to K2 preparation without converting requested scope into permission.
No real product dispatch, queue initialization or task-state creation is part of
this new public entry. It does not complete actual K2.

Owners: [Core D1](../docs/00_Core.md#host-integration-d1),
[Product route](../docs/01_Product.md#scaffold-core-outcome),
[Architecture contracts](../docs/02_Architecture.md#module-contracts),
[Development native evidence](../docs/03_Development.md#native-host-bounded-probes).
The previous [support scope](AOS_FIRST_CORE_K2_PREPARATION_R1.md) remains historical.
C-006/C-006A and C-011 requirements stay unchanged. No permanent host adapter,
controller, service, registry, daemon, new agent role or provider is introduced.

## 2. Proposed temporary supervised profile

Profile: K2-ENTRY-SUPERVISED/R1, applicable only to implementing/testing §1.
This is a new bounded development exception, not an extension of consumed grants.

| Responsibility | Human / executor | Native contribution | Unproven |
|---|---|---|---|
| Development grant | Human accepts this exact package, risk profile, budget and manual limitations; executor rereads before mutation | Existing App route and its permission review | Atomic native AOS authority/state/expiry binding |
| Subject and single writer | Executor verifies manifest/branch/base and uses one effectful owner; Human can stop | Child timeout and reviewed filesystem policy | Host-enforced exclusive continuer; external same-user writer exclusion |
| Write scope | Exact source allowlist below; record changes and compare baseline | Test child writes confined to new scratch; network denied | Executor path discipline beyond actual sandbox remains procedural |
| Source decisions | Preserve provenance and observed references; never infer ACCEPT from JSON | Local byte reading/hashing | Native authenticity/current revocation of supplied decision data |
| Failure/recovery | Ordinary correction inside accepted budget; interruption stops for reconciliation | Durable local artifacts and process result | Automatic wake/resume, genuine interruption conformance |
| Final review | Fresh read-only validator of exact candidate; Human acceptance afterward | Hashes and recorded checks | PASS is not approval or autonomous readiness |

Human review applies to bounded run/material boundaries, not each internal edit.
An agent-written `issued_by_human`, signature-looking string or `approved:true`
cannot satisfy trusted capture. This profile does not weaken product requirements.

## 3. Exact implementation write boundary

Only W/first_core paths below may change:

| Path | Purpose |
|---|---|
| `aos_core/task_binding.py` (new) | Bounded read-only input binding and preview, using existing K1 readers/checkers |
| `tests/test_k2_entry.py` (new) | Independent expected preview and denial cases |
| `aos_core/__main__.py` | Add `k2 preview --input /absolute/request.json`; preserve K1 and k2-support |
| `tests/test_scaffold.py` | Manifest grows from 17 to 19; retain existing checks |
| `README.md`, `CONTRACTS.md` | Explain entry/exit codes, scope and unproven authenticity; historical stage claims clearly labeled |

Existing admission/state/queue/connector implementations and all 83 regression
scenarios remain unchanged. If integration requires changing them, stop that change
and report the exact additional path/reason; do not silently enlarge the allowlist.
Do not modify notebook owners, AOS-3/dev, legacy source or historical run records.

New development record: W/.first-core-state/K2-ENTRY-RUN-001.json.
New scratch R: W/.first-core-scratch/k2-entry/run-001/.
Within R: baseline.json, checks.sb, copy/first_core/ (exact candidate copy),
inputs/ (owned synthetic request/source fixtures), outputs/ (commands, results,
manifest and fresh final review). Existing test fixture roots resolve below
R/copy/.first-core-scratch/k2-support/run-001/fixtures when run from the copy;
they must never write into W's historical run-001. Preserve all new evidence;
no cleanup, replacement of existing targets or writes to k2-actual paths.
Creation requires absent targets, canonical containment and no symlink parents.

## 4. Entry semantics and data boundary

Local source representation `K2_PREVIEW_INPUT_V1` is reversible serialization of
existing owners, not a replacement C-005/C-006 schema or authority mechanism.
Exact Python classes/field layout remain HOW; the following meanings are required:

- Explicit authorized local read root, K1 input/draft paths and their expected hashes.
  No automatic repository/home/config/credential discovery or traversal outside root.
- Task identity/revision, declared repository/worktree/base and exact candidate refs.
  Observe supplied bytes and bounded file hashes; label branch/HEAD as declared
  unless independently supplied read-only preflight evidence establishes them.
  Do not invoke Git or subprocesses from the entry to authenticate declarations.
- Exact proposed operation/path/effect and criteria/check mappings from C-005.
  Preserve `requested_*` and `prohibited_*`. Missing/contradictory requirements are
  blockers. For this slice propose only create-exclusive byte `7`; no arbitrary command.
- Optional claimed C-006/C-011 data/reference: source/channel, decision, exact subject,
  revision, ordering/expiry/revocation and scope. Separate absent, malformed,
  structurally matching and actually trusted facts. A structural match never verifies
  Human origin. Supplied evidence text cannot turn on a trusted capability.
- Proposed target remains absent or is reported conflicting. Never create directories,
  state/locks/publications, result files or target during preview. No hidden cache.

All reads are local, explicit, absolute, non-symlink, no `..` escape, no external
nested references. Maximum 64 KiB per input file, 32 files and 512 KiB aggregate;
reject duplicate JSON keys and non-finite numbers. Reuse existing primitives where
compatible; stricter new-entry parsing need not rewrite old K1 APIs. No import of
user-supplied code, hooks, plugins, external API or model invocation.

Successful preview: exit 0 with `preview_status: PREPARED`, exact observed source
hashes, requested action, checks and human-readable blockers. Always identify
`launch_status: BLOCKED`, `authority_verification: NOT_RUN` and the missing trusted
host binding for this implementation slice. These fields are independent: a useful
preview can succeed while execution remains unavailable. Invalid syntax/schema/path:
exit 2; missing/stale/conflicting required inputs: exit 3. Failure never prints
PREPARED. Stdout JSON and optional concise diagnostics only; no file writes.

No execute/allow/force flag or production-profile promotion. Existing FIXTURE_ONLY
support remains fixture-only. Later real admission requires its own evidenced
integration and grant; this entry cannot manufacture that integration.

## 5. Required checks and evidence

Independent expected outputs are stated before reading implementation outputs.
At minimum test:

| Case | Required result |
|---|---|
| Valid K1 inputs and proposed action | PREPARED preview with exact sources/action/criteria; launch remains BLOCKED |
| No C-006 decision data | Useful preview identifies missing authority; no inferred grant |
| Structurally matching claimed authority | Matching fields reported separately; authenticity NOT_RUN; no execution permission |
| `approved:true`, forged origin, embedded instructions | Cannot produce trusted/launch-ready status or broaden reads/actions |
| Task/revision/candidate/hash mismatch, changed source | Explicit conflict/stale exit 3; no mixed-revision preview |
| Requested path/operation/effect exceeds supplied scope | Conflict; requested scope never becomes allowed scope |
| Revoked/expired/wrong-subject claimed decision | Explicit blocked reason even when other fields match |
| Missing decision source/subject, unknown schema, bool-as-revision | No trust promotion; invalid/incomplete classification explicit |
| Symlink, escape, outside root, oversized/duplicate/non-finite input | Refused before affected read/use; no writes |
| Existing product target | Conflict, no overwrite or delete |
| Preview repeat / denied preview | Complete directory snapshots unchanged; no lock/cache/state files |
| K1 → preview integration | Preserve actual C-005 criterion/requirement/check identities; independent oracle catches dropped scope/criterion |
| Regression | All prior 83 tests pass from isolated copy; help/version/K1/support inspection retained |

A fake implementation that always refuses fails valid-preview expectations;
a fake implementation that always trusts input fails authority-negative cases.
Preview tests do not measure actual K2 effect or native approval. No App Server,
model request, native probes, process kill or scheduled continuation.

## 6. Proposed commands, budget and stop

P = `/Users/muhammed/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12`,
expected SHA256 `ac60cfe0268614638d0ffa35f3b0284fc7b3a11482723793455e17eeb278509e`.
Recheck P before future execution. Standard library only, no installs.
Before execution inspect all new code and test commands, bind 19 source hashes,
copy them byte-for-byte to R/copy/first_core and run with that cwd. Clear inherited
PYTHONPATH/PYTHONHOME and disable bytecode. No existing scratch is reused.

Exact command forms after implementation (not claimed present or run):

```text
/usr/bin/sandbox-exec -f R/checks.sb P -B -m aos_core --help
/usr/bin/sandbox-exec -f R/checks.sb P -B -m aos_core --version
/usr/bin/sandbox-exec -f R/checks.sb P -B -m unittest discover -s tests -p 'test_*.py' -v
/usr/bin/sandbox-exec -f R/checks.sb P -B -m aos_core k2 preview --input R/inputs/valid/request.json
```

Substitute R/P only with exact paths above. Checks.sb permits child writes only
under R and denies network; code and input reads still require the explicit data
boundary. External read allowlisting is not claimed merely from write confinement.
Each command timeout <=60 seconds; maximum four owned child processes, one writer.
Proposed separate budget: 45 active minutes / 25 effectful dispatches / 4 MiB new
source/state/scratch, one run, expiry two hours from start. Historical consumption
is preserved and exact parent remainder stays UNKNOWN, not reset. No budget allocated
by this draft. Material transitions update only the new development record.

Stop on changed baseline/owner/authority, unexpected access, exceeded limits,
interruption, competing writer, unknown effect, required new external route or
material contract expansion. Ordinary bounded correction/recheck within a granted
run is allowed; repeat failure without new evidence stops the affected loop.
Freeze source and outputs; fresh read-only final review (separate context, no repair),
then Human review and STOP. No real K2/K3, native probes or Git actions, including
Commit after acceptance of this development slice.

## 7. Decision packet

Implementation readiness: package prepared; fresh launch preflight and Human
acceptance of this temporary development exception remain required. This package
is not a real-K2 launch authorization and does not close NP-01 or HD-28.

For a future exact grant, identify this subject and file SHA256, explicitly accept
manual limitations, assign RP-FIRST-CORE-LOCAL-R1 subject to this package, allocate
the separate finite budget despite historical UNKNOWN, authorize only listed
source/state/scratch paths and existing App model route, and require stop after
reviewable entry result. Include fresh read-only final reviewer in that grant.
No other Product/Architecture policy choice needs reopening.
