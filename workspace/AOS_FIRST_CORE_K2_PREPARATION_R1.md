# K2 — support and first-effect preparation R1

> Historical preparation snapshot. Its pending/NOT_RUN labels describe the
> original subject and do not restart work. For the accepted result and next
> chat, read [current continuation](AOS_CORE_CONTINUATION_PLAN.md).

Subject: AOS-FIRST-CORE-001/K2-PREPARATION-R1.
Status: PREPARED / WAIT_HUMAN_REVIEW. Implementation and runtime checks: NOT_RUN.
This is a derived handoff proposal, not a canonical owner or execution grant.

## 1. Accepted starting point

W: `/Users/muhammed/Documents/GitHub/AOS-3-first-core-20260915`.
Implementation repository: NMF13579/AOS-3; strategy REIMPLEMENT_FROM_CONTRACT.
K1 source digest rechecked during preparation:
`d3be86db62de0af192e03d9acf27c7252d82caea8a83684f99c14b89a18f3249`.
Human accepted this exact supervised result in the current App conversation after
review. K1 acceptance does not prove native admission or authorize another run.
Historical base: `e99cc3ee03128deb4506bc268839ebd1f52a3f3a`, expected branch
`codex/first-core-20260915`; fresh Git/environment binding is required before launch.
Preserve all S0/K1 source provenance, state, findings and Evidence. No dev mutation.

Owners:
- [Core decisions and D1](../docs/00_Core.md#host-integration-d1).
- [Product S0–K4](../docs/01_Product.md#scaffold-core-outcome).
- [Architecture interfaces](../docs/02_Architecture.md#scaffold-core-interfaces).
- [Development initial state](../docs/03_Development.md#initial-product-state).
- [Development native proof](../docs/03_Development.md#native-host-bounded-probes).

## 2. Two distinct results

**Support implementation and fixture evidence:** implement already accepted product
state/admission/validation/connector contracts in the isolated new source tree,
test them with explicitly synthetic decisions and disposable targets. This is a
proposed future supervised development run, not currently authorized. Product
admission code is not a replacement external host controller or a proof of its
own authority to perform this development run.

**Actual K2 result:** current authentic Human authorization, exact action/candidate,
preflight and C-006A admission lead to one observed permitted effect and independent
result validation; denied/stale/mismatched/replayed cases have no new effect.
Direct and queued routes need their respective support before use. Fixture records,
manually checked JSON and an App acceptance message alone cannot establish native
atomic admission. K2 is not COMPLETE merely because product unit tests pass.

The S0 and K1 exceptions were scoped to those runs. No exception for K2 is inferred.
NP-01 remains unresolved for full current authorization/state binding. No probes,
new host adapter, permanent external control layer or new provider are selected here.
Code implementing the accepted product contracts is distinct from a new mechanism
introduced to work around native probe results; the latter still requires D1 evidence
and a separate Human architecture decision.

## 3. Required dependency order

| Work | Existing owner / contracts | Required result before consumer |
|---|---|---|
| Bind source/candidate and scope | FTR-009/013/019; C-007 | Exact root, baseline, allowed/forbidden actions and freshness; no guessed current facts |
| Create initial task state | FTR-016; C-012 | Explicit new-task request; covered service paths; create-if-absent; complete initial tuple and budget |
| Preserve operation history | FTR-016/014; C-008/C-010/C-012 | Durable admission/operation linkage; uncertain effects remain unknown, never inferred absent |
| Admit one product action | FTR-010/019; C-006/C-006A | Read current parent/state/event/candidate; atomic transition and one-time consumption before effect |
| Observe and validate | FTR-013/011; C-009/C-010 | Exact independently observed result, scope and purpose; validator cannot repair |
| Register local connector | FTR-010/016/019; C-015 | Static local identity/version/generation and operation scope; no executing plugin discovery |
| Persist and deliver message | FTR-010/014/016; C-016 | Durable acceptance, bounded queue, operation identity, fresh dispatch admission; ACK is not result |
| First real effect | FTR-009/019 → 010 → 013/011 | All applicable support and actual launch authority available; no missing proof hidden by fixture PASS |

Registration/queue are mandatory before queued effects. The dependency order does
not require a separate Human gate for every internal component once a bounded run
is explicitly covered. It does not add new FTRs, a service, database or agent role.

## 4. Proposed implementation boundary

Python standard library, existing source-run CLI, local modular monolith; no installs.
Proposed new source files under W/first_core:

- `aos_core/state.py`: durable task and operation state, initialization/reconciliation.
- `aos_core/admission.py`: accepted product C-006A checks and atomic consumption.
- `aos_core/validation.py`: exact subject/result/scope checks, separate from writer.
- `aos_core/connectors.py`: static C-015 bindings and narrow local file handler.
- `aos_core/queue.py`: bounded durable C-016 message/delivery semantics.
- `tests/test_k2_support.py`: component and integration positive/negative controls.

Exact affected existing files: `aos_core/__main__.py`, `README.md`, `CONTRACTS.md`,
`tests/test_scaffold.py` and `tests/test_k1.py`. Preserve K1 interfaces and all
30 regression scenarios. Both test modules currently fix their output to K1 scratch;
move their fixture roots to the new support scratch. The scaffold manifest grows
from eleven to seventeen source files. Do not write into consumed S0/K1 runs.

Proposed new development state: W/.first-core-state/K2-SUPPORT-RUN-001.json.
Proposed scratch/service/test target root:
W/.first-core-scratch/k2-support/run-001/.
Fixture C-012/queue/ledger records live only inside that disposable root, separate
from the real development run state and historical parent accounting.
No service-state file, queue or target is created during this preparation.
Exact selected serialization/locking/publication and commands follow below. They
remain reversible HOW within the accepted contracts, not immutable architecture.

## 5. Finite proposed fixture profile

For future local fixture tests only: one parent, one active delivery owner per
ordering key; at most 16 queued messages, 4 KiB payload each, 64 KiB queued payload
total; message lifetime 60 seconds, waiting limit 30 seconds, claim 5 seconds,
at most two bounded delivery attempts, one-second retry delay. Expired claim never
proves the prior owner stopped. Preserve all test observations until review;
no cleanup or production retention policy is authorized.

Proposed development budget: 60 active minutes, 30 effectful dispatches, 4 MiB
total new source/state/Evidence, two-hour run expiry; each check at most 60 seconds.
These numbers are proposals, not allocated resources. Historical parent remainder
is UNKNOWN; a future separate grant must explicitly preserve that uncertainty.
Stop on authority/source drift, unexpected access, unknown effects, budget/expiry,
concurrent writer, material contract change or repeated failure without new evidence.

## 6. Acceptance and failure evidence matrix

All rows currently NOT_RUN. An independent expected result precedes actual outputs.

| Case | Required observation |
|---|---|
| Initial state | Explicit new identity produces BIND_TASK/ACTIVE/RUNNING, original lifecycle, exact candidate/authority refs, NOT_RUN criteria, empty ledger |
| Existing/partial state | Existing identity preserved; inaccessible history stays UNKNOWN; interrupted publication reconciled without treating it as a new task |
| Current matching admission | State/event/candidate/action/parent tuple matches; consumption and lifecycle transition publish together; effect follows only afterward |
| Each mismatched field | Parent revision/digest, state, candidate, action, scope, expiry/revocation or transition mismatch denies before effect; no partial state transition |
| Replay/correction | Consumed envelope rejected; CORRECT without matching gate rejected; unknown effect does not trigger retry |
| Independent result | Writer target and reader target differ: integration fails despite component success; observed byte result and permitted scope both required |
| Local connection | Unknown identity/version/generation and disabled receiver rejected; DIRECT_READ does not perform hidden writes |
| Durable enqueue | Capacity/payload/expiry checked; no accepted ACK before durable save; same ID/different payload rejected |
| Delivery | Fresh admission at dispatch; completed operation not repeated on redelivery; message acceptance and operation result reported separately |
| Ownership/recovery | Old claimant cannot continue after takeover; in-flight ambiguity blocks another effect until reconciliation |
| Read-only event | Independent subscription/read/service scope; no invented task authority or mutation from payload; result stored before ACK |
| Preservation | Source, historical S0/K1 and unrelated state unchanged; fixture paths contained; required NOT_RUN stays explicit |
| Regression | S0/K1 behavior retained after any manifest/scratch migration; altered candidate gets fresh checks and read-only final review |

Fixture current-authority stores test the product contract only. They do not stand
in for trusted native Human capture, external fencing, interruption/wakeup or HD-28.
The actual first-effect packet must name exact target/action/expected bytes and
its independent observer; this document does not authorize a write of «7» anywhere.

## 7. Remaining gaps and launch decision

| Category | Exact remainder |
|---|---|
| Implementation HOW | Selected below; source must be inspected before first execution and actual tests still required |
| Mutable preflight | Current branch/HEAD, accepted K1 hashes, absent new paths, actual sandbox/runtime, owner revisions and budget |
| Development authorization | A separately reviewed support-only implementation/test packet and explicit supervised grant; no inferred reuse of K1 authorization |
| Actual K2 host evidence | Current trusted admission/state binding and required host checks remain unresolved; synthetic support PASS cannot close them |
| Human architecture decision | None requested merely to implement already accepted contracts. Any proposed permanent host workaround remains separately gated under D1 |

Next bounded action: fresh read-only review of this exact support-only package,
then one explicit Human launch decision if review finds no material gap. Keep actual
product K2 launch BLOCKED until its own prerequisites and authorization are satisfied.
No automatic transition into K3, probes, external access or Git delivery.

## 8. Selected local HOW and publication semantics

One UTF-8 JSON snapshot per fixture store, schema `K2_SUPPORT_STORE_V1`. The store
contains distinct task, authority-fixture, admission/envelope, operation ledger,
registration, subscription and delivery records. Delivery records remain logically
separate from C-012 even if stored in the same snapshot; neither ACK nor storage
changes criterion completion. No database, service, broker or background loop.
Fixture authority is explicitly `FIXTURE_ONLY`, never Human trusted capture.

Each store lives in a unique directory below the owned fixture root. Within it:
`store.json`, stable `store.lock`, create-exclusive `publication-<nonce>.json`,
and `target.txt`. IDs are data keys, not interpolated filesystem paths. Only this
new fixture state may be replaced during tests; historical run records are immutable.
The target is absent initially; the narrow test handler creates it once containing
the single UTF-8 byte `7`. It never overwrites an existing file. Reading bytes for
the oracle is separate from the handler result, and paths outside the fixture root
are rejected before action. No arbitrary command or code loader is accepted.

On macOS use standard-library `fcntl.flock` on the stable lock file; acquire
nonblocking with a finite deadline. Reject symlink parents/targets and unsupported
platforms explicitly. Linux/Windows remain unvalidated; importing existing K1 must
not fail merely because a platform lacks this optional implementation primitive.
An alternative portability mechanism is future HOW, not proof of Windows support.

Under lock: load and validate current store/schema and the expected revision;
read the current authority record, candidate observation, action and transition;
validate exact C-006A subset/superset constraints and lifecycle; build the next
snapshot with consumed envelope, before/after tuple and durable operation admission.
Serialize to a new publication file, flush/fsync, atomically replace `store.json`,
then fsync its parent directory. Do not dispatch before durable confirmation.
The lock file is never replaced/deleted. Reject an invalid transition without
publishing a new store, changing lifecycle or consuming the envelope.

Hold the same lock through the fixture effect and durable result publication.
Every cooperative fixture writer/claimant uses this entry point. A waiting contender
must reacquire and reread current revisions; it cannot act on a cached claim. No
takeover based solely on elapsed claim time. An effect that bypasses this protocol,
an external same-user writer or true host fencing is not proven by the fixture.

Create initialization is explicit, not an automatic consequence of a missing file.
An existing lock/history/temporary publication with no complete store is partial or
unknown state requiring reconciliation, not a new empty task. Existing complete
store returns its binding without reset. Unknown schema or unreadable history blocks.

If publication fails before replacement, do not perform the effect. If replacement
or fsync outcome is uncertain, retain observations and return UNKNOWN. Reopen and
reconcile before further effects. A consumed admission with missing result does not
prove no effect. For this specific create-once byte fixture, independent observation
may show absent target, exact expected byte, or mismatch: absent can permit a fresh
attempt only after reconciling prior admission and current authority; exact expected
bytes bind the existing operation/result; mismatched or unattributable data blocks.
Do not generalize that oracle to arbitrary filesystem effects or exactly-once work.
No cleanup is part of this run; retained publication files count against its budget.

## 9. Exact fixture operations and queue profile

The callable support APIs implement the accepted product contracts under test.
Their only invoked effects in this package are disposable fixture operations.
The public CLI exposes only a read-only inspection command, not a task-launch API.
Test initialization uses explicit fixture current-authority records; it must not
feed them back into the real development task's authority or claim native conformance.

One static connector: `fixture.local-file`, interface revision `1`, generation `1`.
Operations: `read` (DIRECT_READ), `create_seven` (QUEUED_COMMAND); a direct action
test calls the same narrow handler through product admission, not via DIRECT_READ.
Register only this known handler by code; unknown code paths/classes/imports fail.
Fixture commands are tied to a single active parent and current generation.

Event `fixture.result_observed` has two explicit read-only subscriber bindings,
`fixture.status` and `fixture.review`. They consume the observation after the source
task is terminal only when their independently current subscription/read/service
scope is valid. Separate per-subscriber delivery/result records precede ACK. Invalid
scope/version or a request to mutate from an event produces refusal, no fake task.

Queue limits from §5 apply to retained messages, not only pending entries. Queue
capacity exhaustion therefore remains explicit until separately authorized cleanup.
Use an injected clock for expiry/retry test boundaries rather than long sleeps;
record that clock evidence is a fixture, not real automatic wake/resume. Real
simultaneous owned processes test lock contention; no process is killed and no
App Server/native approval or interruption probe runs. Failure injection is scoped
to publication steps of the owned test store, never monkeypatching host security.

## 10. Exact commands, inputs and output scope

W is the exact worktree in §1; R is
`/Users/muhammed/Documents/GitHub/AOS-3-first-core-20260915/.first-core-scratch/k2-support/run-001`.
P is
`/Users/muhammed/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3.12`.
Expected P SHA256: `ac60cfe0268614638d0ffa35f3b0284fc7b3a11482723793455e17eeb278509e`.
Use cwd W/first_core. No pip, installations, dependencies, sudo or network.
These entrypoints are proposed implementation targets, not commands claimed to
exist or have passed:

```text
/usr/bin/sandbox-exec -f R/checks.sb P -B -m aos_core --help
/usr/bin/sandbox-exec -f R/checks.sb P -B -m aos_core --version
/usr/bin/sandbox-exec -f R/checks.sb P -B -m unittest discover -s tests -p 'test_*.py' -v
/usr/bin/sandbox-exec -f R/checks.sb P -B -m aos_core k2-support inspect --state R/fixtures/inspection/store.json
```

Expand W/R/P only from this reviewed package. The suite creates the explicit
`fixtures/inspection` store with a known FIXTURE label for the final inspect command;
its existence is checked before inspection. Other cases each reserve a fresh unique
fixture directory. Missing/partial state is diagnostic, never an inspect-triggered
initialization. `inspect` returns bounded JSON to stdout: schema/task/revision,
operation/delivery statuses, limitations and FIXTURE_ONLY. Exit 0 means read success;
2 invalid input/schema/path; 3 missing/unknown/partial state. It never creates files.

Child sandbox profile at R/checks.sb:

```text
(version 1)
(allow default)
(deny network*)
(deny file-write* (require-not (subpath "R")))
```

Substitute exact R above before use. Scoped executor writes may create/edit only
the eleven paths selected in §4, new K2-SUPPORT-RUN-001.json and R descendants.
Runtime child writes are limited to R. Reads are procedural allowlists, not an
OS-enforced read-deny policy. No new source/project scans or credential reads.
Runtime fixtures read their own files, the seventeen new/current source files and
required Python standard library. The App model route is the existing authorized
conversation only, outside local child network prohibition.

Use -B and sanitized PYTHONPATH/PYTHONHOME for children. Capture stdout/stderr/exits
under R/outputs; baseline and candidate manifests under R; no output elsewhere.
Bounded writer checks before exceeding total 4 MiB; each command timeout 60 seconds;
at most two simultaneous owned child processes, counting test runner plus one
contender. The runner participates as the second contender for concurrency tests.
No full-suite subprocess recursion. Atomic replacement affects only new fixture
store/publication files; it does not authorize deletion or replacement outside R.

## 11. Required proof before reporting support ready

The test module must produce explicit results for every row of §6. It must include
at least one actually successful fixture effect; an implementation that always
refuses cannot pass. Expected values are prepared independently of production
helpers. An oracle reads exact `target.txt` and prior/current store observations;
it does not infer success from a handler return, queue acceptance or ACK alone.

Separate each mismatch dimension, ensure other inputs valid, and check both no
target effect and unchanged protected state tuple on denial. Cover duplicate same
identity/same payload versus same identity/different payload, corrupt/missing store,
create conflict, pre/post-publication failures, post-effect/lost-result reconciliation,
disabled/stale connector, expiry/queue limits, stale claimant and two event recipients.
Inject fixture publication failures deterministically; real process interruption,
native fences and autonomous resume remain NOT_RUN.

Preserve all intermediate failures and corrections; affected checks rerun against
the new candidate. Freeze all seventeen source-file hashes and current outputs.
Fresh read-only final validator receives the exact candidate, independent oracle,
scope diff/baseline, results and limitations. No silent validator repair. Success is
SUPPORT_FIXTURE_CHECKS PASS, not K2 READY, autonomous conformance or Human ACCEPT.

## 12. Launch conditions and Human-only boundaries

Before source mutation recheck package SHA256, exact K1 source hashes, owners,
branch/HEAD, new-target absence/symlink containment, P and actual sandbox policy.
Persist the current separate Human grant, Risk Profile, start/expiry, budget and
one next action in the new run state. Current inspected bytes differing from this
package require affected rebind/review; do not silently import unrelated changes.

A future Human launch grant must explicitly accept this temporary supervised
support-only profile, fixture file effects and publication replacement within R,
the procedural limitations, exact paths and separate budget despite UNKNOWN parent
remainder. The required native host gaps are not thereby declared fixed or waived
for actual K2 execution. Material Product/Architecture/authority expansion, new
external access, permanent host workaround and real product target effects remain
Human decisions. Ordinary bounded correction inside the granted run is automatic.

Stop after reviewable support result. No actual K2 task launch, K3, native probes,
Git actions, new provider, schedules or automatic restart. Even unused budget does
not authorize a second run. Acceptance does not trigger a Commit for this package.
