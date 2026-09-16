# K3: bounded correction and continuation — preparation R1

> Historical preparation snapshot. Its pending/NOT_RUN labels describe the
> original subject and do not restart work. For the accepted result and next
> chat, read [current continuation](AOS_CORE_CONTINUATION_PLAN.md).

Subject: `AOS-FIRST-CORE-001/K3-CORRECTION-R1`.
Status: PREPARED / WAIT_HUMAN_REVIEW. Implementation and scenario: NOT_RUN.
Current Human «Разрешаю» authorizes the proposed targeted inspection and this
single preparation package; it does not launch K3. The accepted B run is finished.

## 1. Goal and existing evidence

Deliver one working, supervised **controlled-defect** scenario plus its checked
implementation: detect byte `6` where `7` is required, diagnose using observed
fixture provenance, perform one admitted correction, recheck and continue to
the next read-only child check within the same parent. No further preparation-only
deliverable replaces this outcome after a future implementation grant.

Owners remain [Core D1](../docs/00_Core.md#host-integration-d1),
[selected route](../docs/01_Product.md#scaffold-core-outcome),
[C-006A/C-009/C-009A](../docs/02_Architecture.md#module-contracts),
[V3](../docs/02_Architecture.md#core-loop-v3) and
[lifecycle transitions](../docs/03_Development.md#core-lifecycle-transitions).
This is implementation of their existing local correction semantics, not a new
controller platform, architecture owner or host-adapter.

W = `/Users/muhammed/Documents/GitHub/AOS-3-first-core-20260915`.
Repository `NMF13579/AOS-3`; branch `codex/first-core-20260915`; base HEAD
`e99cc3ee03128deb4506bc268839ebd1f52a3f3a` (refresh at execution preflight).
Current accepted 21-file source candidate, rehashed during this preparation:
`a3930f8e43e4be0f24e6f0c20b66d481b1cf49730b0a1a7c32fca07e140bff19`.
Manifest: W/.first-core-scratch/k2-integration/run-001/launch/frozen/code-manifest.json.
Digest uses sorted JSON relative-path/hash mapping with Python default separators,
ensure_ascii=False and allow_nan=False. HEAD alone is insufficient.

User accepted B in chat after its review. Immutable B evidence remains at
W/.first-core-scratch/k2-actual/run-001/:

| Subject | SHA256 |
|---|---|
| outputs/final-review.json | `06daf96906115c3a4bbf7e0c8a7ab6f55e0724224e78bb7b5332c4ec81d72dfb` |
| store.json | `0c7fc4d258e1bf2d0b97f92fdd25786403dd639915f5573cf8260ae391b7fed0` |
| target.txt | `7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451` |

Read-only inspection of current source established:

| Existing part | Coverage and missing seam |
|---|---|
| admission.py correction checks | Checks current diagnostic/gate/authority/state/candidate/action and consumes envelope before effect |
| test_k2_support.py correction positives | Build diagnostic/gate through fixture helpers, then create `7` at ABSENT target; do not demonstrate repair of an existing faulty result |
| admission.py action/candidate restriction | Only create_seven and ABSENT accepted; cannot repair byte `6` |
| supervised.py | One fixed action, rejects existing history, no check→diagnose→correct→continue route |
| queue.py | Issues EXECUTE envelopes; no end-to-end fresh correction gate after queue state changes |
| validation.py | Reads result independently; no complete C-009 check-admission/criterion progression for this scenario |

These are bounded implementation gaps, not native capability FAILs or a reason
to repeat NP probes. Historical 130-test PASS and B PASS remain valid for their
subjects. No tests or product entrypoints were run in this preparation.

## 2. One future run, one outcome

Proposed temporary profile: `K3-SUPERVISED-CORRECTION/R1`.
The future exact grant covers implementation, ordinary source corrections,
isolated fixture checks, the controlled-defect demonstration and fresh read-only
final review together. No Human approval between the demonstration's internal
check/diagnose/correct/recheck steps. No actual effect outside the new K3 scratch.

R = `W/.first-core-scratch/k3-correction/run-001/`.
New development record: `W/.first-core-state/K3-CORRECTION-RUN-001.json`.
Both were absent during preparation; recheck absence and canonical non-symlink
containment. Never reuse or edit B's target/store, old scratch or old records.

Demonstration child `K3-CORRECTION-DEMO-001/R1`, inside AOS-FIRST-CORE-001.
Product/data root D = `R/demo/`; sole corrected artifact `D/target.txt`.
Fixture preparation exclusively seeds that new target with byte `6` and records
its exact provenance and hash:
`e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683`.
Seeding is an explicit authorized fixture effect, not a fabricated production
failure. It occurs before the product loop. No direct fixture mutation may repair
the target after the first product check.

Required observed sequence:

1. Bind exact task, current manual run grant, source manifest, initial target,
   finite budget and accepted correction scope. Record synthetic defect origin
   separately from the genuine Human development-run authorization.
2. BIND_TASK → RECOVER_STATE → SELECT_NEXT_ACTION → CHECK. Admit a read-only
   ACCEPTANCE check under fresh C-009; observe `6`, expected `7`, persist FAIL
   evidence through the controller. The checker never changes the artifact.
3. CHECK → DIAGNOSE. Compare actual bytes, expected criterion, protected input
   hashes and known fixture provenance. Diagnose only this known defect class;
   unexpected bytes, changed inputs or competing explanations block correction.
   Mere mismatch does not prove an arbitrary underlying code defect's cause.
4. Prepare exact correction `replace_known_six_with_seven` for this target only,
   with before hash, after hash and no path/scope expansion. Evaluate C-009A from
   observed evidence: cause, confidence, competing hypotheses, falsifiable
   prediction, affected checks and explicit stop/recovery route. No hard-coded
   ALLOW independent of observations. Persist diagnostic/gate provenance.
5. DIAGNOSE → CORRECT via current C-006A and gate. Use the existing queue/admission
   path. Enqueue/claim revisions invalidate stale gates: evaluate the final gate
   against the tuple actually admitted; do not silently rewrite an old gate to
   match new state. Durable consumption precedes replacement. Recheck exact
   current target hash immediately before mutation under the existing owned lock.
6. CORRECT → CHECK with a new read-only C-009 and updated candidate. Independently
   observe byte `7` and preserved inputs; persist the affected check outcome.
7. CHECK → SELECT_NEXT_ACTION → CHECK: automatically perform the next distinct
   read-only child check (protected input/source preservation) within this parent.
   It must actually execute and produce evidence, not merely set a next-task label.
8. Freeze the resulting code/artifact/ledger. Fresh read-only final reviewer checks
   the exact subject and limitations. Report reviewable scenario result and STOP.
   No claim that the entire parent, K3, K4 or HD-28 is complete.

At most one successful artifact correction in the positive demonstration.
If first check is already correct, no correction; if correction is uncertain,
stop for evidence, no retry or automatic rollback. A before-image may be retained
as evidence; restoring it would require its own covered action. Atomic replacement
and temp-file details remain reversible HOW within D, with exact files/patterns
listed before execution. This does not claim exclusion of a malicious same-user
writer or native exactly-once semantics.

## 3. Exact source allowlist

Only these paths under W/first_core may change under a future grant:

| Paths | Purpose |
|---|---|
| aos_core/correction.py — new | Bounded observed diagnosis and progression for this scenario using existing core mechanisms |
| tests/test_k3_correction.py — new | Independent scenario expectations and negative controls |
| aos_core/__main__.py | Explicit `k3 supervised-run --input /absolute/request.json`; no general execute/force interface |
| aos_core/supervised.py | Explicit profile dispatch/current grant and source inventory binding; preserve K2 behavior |
| aos_core/state.py | Exact initial candidate and durable diagnostic/check/correction progression, existing store/lock only |
| aos_core/admission.py | Narrow conditional replacement admission and correction gate; preserve K2 ABSENT/exclusive-create restriction |
| aos_core/queue.py | Fresh CORRECT binding through existing queue; preserve EXECUTE and result-before-ACK semantics |
| aos_core/connectors.py | Exact owned replacement operation; no arbitrary file editor or dynamic connector discovery |
| aos_core/validation.py | Read-only C-009 worker/check binding; controller owns consumption, transitions and persisted outcomes |
| tests/test_scaffold.py | Source manifest grows from 21 to 23; preserve checks |
| README.md, CONTRACTS.md | Truthful usage and supervised/fixture limits |

Existing K1/K2 test files, task_binding.py and other source stay unchanged. All
130 previous test definitions must remain and pass on final bytes. Existing
K2 profile/source pinning must not be silently rebound to this new implementation:
old B evidence/copy stay frozen. Future new-profile source references use their
own current manifest. No global loosening of profile, candidate or authority checks.

R may hold exact source copies, inputs, finite disposable regression fixture
directories, sandbox policies, stdout/stderr, source manifests, preserved attempted
versions and final review. Run legacy-in-this-core test suites from R/copy/first_core
so their relative fixture writes stay inside R. Do not run the old AOS-3 runtime.
D may contain only listed input/decision/manifest files, target, existing-style
store/lock/publication files, bounded replacement temp files and evidence outputs;
freeze its exact allowlist and argv before starting the demonstration.

No notebook owner edits, dev changes, additional dependencies, services, host
adapter, daemon, scheduler or new permanent control layer. Need for an additional
source path or material contract change stops only that dependent action.

## 4. Responsibility and claim limits

| Boundary | Responsible party / evidence |
|---|---|
| Genuine run grant, semantic task/scope, current Human instruction | Human and supervising App executor; preserve verbatim source/order/subject, never claim native trusted capture |
| C-009/C-009A/C-006A local bindings and transitions | Existing product core; hashes, state/event revisions, evidence and consumption records |
| Fixture origin | Explicit setup manifest; does not count as spontaneously discovered production failure |
| Write scope / network | Reviewed child sandbox restricts demonstration writes to its declared service/target/temp paths; inputs/code read-only; deny network |
| Single executor, finite development budget | Supervising executor manually accounts usage; no host-exclusive continuer claim |
| Validation | Checker and fresh final reviewer do not repair candidate; ordinary correction is separate execution |

C-006A requirements remain intact. Native authority capture, atomic native
chat-to-state binding, host conformance and automatic wake/resume remain
UNKNOWN/NOT_RUN. Deterministic repair of a known seeded defect does not prove
general autonomous diagnosis or arbitrary code repair. No process interruption,
native approval probe, new provider or background continuation is in scope.

## 5. Required checks and completion predicate

| Check | Expected result |
|---|---|
| Main scenario | Observed FAIL on `6`, evidence-bound gate, one correction to `7`, affected check PASS, distinct next child check actually runs |
| Already correct | No corrective artifact write; check evidence is sufficient to choose read-only continuation |
| Unknown byte/source provenance or conflicting diagnosis | No invented PROVEN cause/ALLOW; preserve target and return bounded blocker |
| Missing/DENY/weak/stale/mismatched gate; wrong prediction/check/candidate | Refuse before correction; preserve unconsumed envelope and admission tuple on denial |
| Gate stale after enqueue/claim; changed target after diagnosis | Refuse stale binding; no overwrite of a different candidate |
| Expired/revoked/wrong grant or out-of-scope replacement | No corrective effect; actual clock and current local records checked |
| Replay, duplicate delivery, lost correction result/publication | No second effect; UNKNOWN is retained and no automatic reset/retry occurs |
| C-009 denial or checker mutation attempt | No target mutation; no acceptance PASS from a diagnostic-only check |
| Wrong reader/result and dropped continuation | Independent oracle rejects; ACK/printed labels do not satisfy completion |
| Source/data path escape, symlink, oversized/malformed input | Fail closed before the affected use; no unexpected writes |
| Regression | Full final-candidate suite retains all 130 prior tests and K2 preview/fixture/supervised behavior |

Tests must state their own expected byte, transitions and denial consequences;
do not derive expected results from the writer's output. Controlled faults belong
only in disposable R fixtures. No real B replay or native interruption.

Finish only with the checked implementation, the complete observed demonstration,
negative controls, exact code/result hashes, preserved failures and fresh read-only
final review. Required NOT_RUN remains explicit and prevents claiming its criterion
passed. A partial implementation or another launch-preparation document alone
does not satisfy this run. Do not introduce another A/B approval split inside
this fixture-only development scenario; its full scope is presented here upfront.

## 6. Commands, budget and stop

P = `/Users/muhammed/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12`;
expected SHA256 `ac60cfe0268614638d0ffa35f3b0284fc7b3a11482723793455e17eeb278509e`.
Refresh package/source/base/runtime/path bindings before mutation. Python 3.12+,
standard library only, current App model route; no install or external access.
Clean environment excludes PYTHONPATH/PYTHONHOME/PYTHONOPTIMIZE and user-site
loading; disable bytecode. Cwd: R/copy/first_core. Proposed command forms:

```text
/usr/bin/sandbox-exec -f R/checks.sb P -B -m unittest discover -s tests -p 'test_*.py' -v
/usr/bin/sandbox-exec -f R/demo.sb P -B -m aos_core k3 supervised-run --input R/demo/request.json
```

These are future interfaces, not commands claimed to exist today. Expand exact
paths and record argv/env/policy hashes before dispatch. An independent read-only
observer runs as a separate process under deny-write/deny-network policy.
Test-child writes only R; demonstration child writes only its frozen D allowlist.
No broad filesystem elevation, sudo or config change. Source edits by executor
remain within §3; record material transitions in the one new development record.

Proposed separate budget: **60 active minutes / 30 effectful dispatches / 8 MiB**
new source/state/scratch, one run, expiry two hours from start. Historical spending
is preserved; historical parent remainder remains UNKNOWN. At most four owned
child processes, one writer, timeout <=60 seconds per command. The grant covers
ordinary implementation corrections and affected rechecks within this budget,
not extra Product decisions or a new independent goal.

Stop on missing/expired authority, baseline/input drift, competing writer,
unexpected path/provider, uncertain effect, resource limit, material scope or
architecture expansion, or recurring failure without new discriminating evidence.
No automatic continuation after interruption. No K4, native probes, network,
installation, Commit, Push, Merge, Release or cleanup of historical artifacts.

Next single action: an explicit Human grant for this package's SHA256, temporary
manual limitations, RP-FIRST-CORE-LOCAL-R1, §3 source/state/scratch paths, the finite
budget and fresh read-only final reviewer. After the reviewed K3 scenario result,
STOP. This preparation itself issues none of those execution permissions.
