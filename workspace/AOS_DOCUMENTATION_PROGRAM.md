AOS Documentation Program Plan / Controller R6

Непрерывный Full Draft → Document Refinement → Package Harmonization

> Candidate content for `workspace/AOS_DOCUMENTATION_PROGRAM.md`.
> R6 is a bounded structural correction of exact R5 limited to findings R5-AUD-F001 and R5-AUD-F002. R6 is not active until exact audit and explicit human selection.

<!-- PROGRAM_CONTRACT_START -->
PROGRAM CONTRACT

1. Назначение и граница authority

Этот документ задаёт только orchestration и continuity программы документации AOS:

```text
scope-wide draft
→ ordered document refinement
→ package harmonization
→ exact candidate binding
→ separate audit
→ human decision
```

Он не является canonical owner для product, architecture, feature, research, validation, status или Git semantics.

```text
Program Contract ≠ canonical knowledge
Program State ≠ product truth
Program adoption ≠ implementation authorization
Program adoption ≠ Git authorization
```

Приоритет всегда определяется docs/00_Core.md. При конфликте Current State уступает current explicit human decision, accepted canonical owner и current repository observation для mutable facts.

────────

2. Exact identity и adoption

Целевой repository path:

```text
workspace/AOS_DOCUMENTATION_PROGRAM.md
```

Файл состоит из двух частей:

1. PROGRAM CONTRACT — revisioned и неизменяемый после human selection;
2. CURRENT STATE — derived mutable section для continuity.

Identity Program Contract вычисляется по следующим exact правилам:

1. Файл encoded как UTF-8 без BOM и использует только LF line endings.
2. Start delimiter — единственная LF-delimited line, полное ASCII-содержимое которой равно `<!-- PROGRAM_CONTRACT_START -->`.
3. End delimiter — единственная LF-delimited line, полное ASCII-содержимое которой равно `<!-- PROGRAM_CONTRACT_END -->`.
4. Digest subject начинается с первого byte сразу после LF, завершающего start delimiter line.
5. Digest subject заканчивается LF byte непосредственно перед первым byte end delimiter line; этот завершающий LF входит в digest subject.
6. Delimiter lines и LF, завершающий start delimiter line, в digest не входят.
7. Никакая Unicode normalization, whitespace trimming или line-ending conversion не выполняется.
8. `program_contract_identity` имеет вид `sha256:<lowercase SHA-256 of exact digest subject bytes>`.

Изменение текста Program Contract требует:

```text
successor revision
→ read-only audit
→ explicit human selection
```

Изменение только CURRENT STATE не меняет contract identity и не создаёт новую method revision.

До запуска программы необходим explicit human adoption exact subject, который связывает:

• program_contract_revision;
• program_contract_identity;
• exact human-selection record identity и reproducible locator;
• repository / branch / HEAD at adoption;
• controller path;
• exact selected writable boundaries;
• exact selected allowed_run_kinds;
• initial selected_start_run_kind, допустимый только как AUTHORING_RUN либо explicit отсутствие automatic start (null);
• documentation_edit_authorization identity;
• отсутствие Git и runtime authorization.

Human selection/adoption применяется только через отдельный exact reproducible raw record формата `AOS_PROGRAM_HUMAN_SELECTION_R1` и внешний binding этого record. Record относится только к adoption Program Contract и не является package-level Human Decision из Section 12.

Raw human-selection record encoded как UTF-8 без BOM, использует LF line endings, является одним YAML document без duplicate keys и не содержит собственного digest. Он обязан связывать:

• `record_format: AOS_PROGRAM_HUMAN_SELECTION_R1`;
• `value: ACCEPT`;
• exact program_contract_revision и computed program_contract_identity;
• repository / branch / observed HEAD at selection;
• controller path;
• exact selected writable boundaries;
• exact selected allowed_run_kinds;
• initial selected_start_run_kind, допустимый только как AUTHORING_RUN либо explicit no-start (null);
• documentation_edit_authorization identity и exact permissions;
• implementation_authorization: NONE;
• git_authorization: NONE;
• decision source/provenance.

External binding хранит `record_format`, `record_identity = sha256:<lowercase SHA-256 of complete raw record bytes>` и reproducible `record_locator`. `record_identity` не входит в hashed raw record и поэтому не создаёт self-reference.

Для initial adoption domain `selected_start_run_kind` ограничен exact значениями `AUTHORING_RUN | null`. `AUDIT_RUN`, `CORRECTION_RUN` и `RE_AUDIT_RUN` могут входить в `selected_allowed_run_kinds` только для subsequent runs и не являются допустимыми initial start kinds.

Human selection получает `COMPLETED` только если record bytes доступны через locator, raw-byte digest совпадает с external `record_identity`, YAML и required fields валидны, contract subject пересчитан и совпадает с record, mutable repository facts re-observed, а все selected values дословно скопированы из record в CURRENT STATE. При любом mismatch selection остаётся `NOT_RUN`, adoption не выполняется и создаётся out-of-run control finding по Section 5.

Proposed writable boundaries, proposed allowed run kinds и proposed start run kind не являются выбранными или разрешёнными значениями. Отсутствие любого selected binding означает:

```text
program_phase = NOT_ACTIVATED
current_run_kind = NONE
no documentation mutation
```

Adoption может открыть run только когда `documentation_edit_authorization.status = AUTHORIZED`, exact allowed paths и run kinds совпадают с human-selected adoption subject, `selected_start_run_kind` равен `AUTHORING_RUN`, а `AUTHORING_RUN` входит в `selected_allowed_run_kinds`. При `selected_start_run_kind = null` adoption не открывает run. Наличие файла в repository не является adoption.

После successful human selection/adoption `contract_status = ADOPTED` и `state_status = CURRENT` независимо от перехода в `AUTHORING` или `ADOPTED_IDLE`.

────────

3. Canonical routing

При старте и resume Codex читает:

1. AGENTS.md;
2. docs/00_Core.md;
3. этот Program Controller;
4. только релевантные canonical owners для текущего action.

Маршрутизация:

• authority, statuses, safety — docs/00_Core.md;
• product facts — docs/01_Product.md;
• architecture facts/contracts — docs/02_Architecture.md;
• feature/package authoring и validation boundaries — docs/03_Development.md;
• lessons/regressions — docs/04_Lessons.md;
• targeted research — docs/05_Reference.md;
• feature identity/disposition — docs/06_Features.md;
• accepted global foundation — current package в AOS/;
• repository mutation rules — AGENTS.md.

Program Contract не повторяет их методику. Codex применяет current canonical content непосредственно.

────────

4. Program scope

Программа работает только по human-selected scope, записанному в CURRENT STATE.

Initial candidate scope:

```text
FTR-001
FTR-003
```

SUPPORTING_CONTROL_ONLY может быть отражён как dependency, но не становится самостоятельным documentation subject автоматически.

UNDECIDED, DEFERRED, REFERENCE_ONLY и REJECTED не добавляются в executable scope без отдельного human decision.

Обнаруженная dependency вне selected scope:

```text
record candidate dependency
→ continue unaffected work
→ create exact human decision request
```

Codex не меняет human_disposition.

────────

5. Run model

Программа использует раздельные logical runs.

`technical_result` существует только внутри valid active run. Read-only guard или binding check, выполненный до открытия run, после закрытия run либо при отсутствии valid run binding, не создаёт и не перезаписывает `technical_result`.

Failure такого out-of-run check записывается в `control_findings` как отдельный diagnostic record:

```yaml
finding_id:
classification: CONTRACT_VIOLATION | BLOCKED | UNKNOWN
subject_identity:
evidence_identity:
affected_boundary:
detected_at_state_revision:
status: OPEN | RESOLVED
```

`control_findings` не является technical-result axis, не участвует в Audit transition matrix и не может создать PASS, approval или authority. OPEN control finding останавливает только affected action. Current `technical_result` остаётся неизменным. Finding записывается в CURRENT STATE только когда такая state mutation уже разрешена; иначе он существует только в exact read-only report output. Если тот же failure обнаружен внутри уже valid active run и exact run subject, он может стать run-bound technical result по обычным правилам.

Каждый новый run до первого action обязан:

• получить новый `active_run_id`;
• bind exact `active_run_subject_identity`;
• подтвердить, что run kind входит в human-selected `allowed_run_kinds`;
• подтвердить writable/read-only boundary для этого run kind;
• reset current `technical_result` в объект, bound к новому run и subject:

```yaml
value: NOT_RUN
run_id: <active_run_id>
run_kind: <current_run_kind>
subject_identity: <active_run_subject_identity>
report_identity: null
```

Результат предыдущего run не переносится в current `technical_result`; он сохраняется только в собственном exact report/record.

AUTHORING_RUN

Одна bounded documentation work, которая непрерывно включает внутренние orchestration phases:

```text
AUTHORING_PHASE_0 — Scope Bind
→ AUTHORING_PHASE_1 — Full Draft
→ AUTHORING_PHASE_2 — Document Refinement
→ AUTHORING_PHASE_3 — Package Harmonization
→ Exact Candidate Binding
```

Внутренняя phase completion — checkpoint, а не terminal report и не Human Gate.

Codex автоматически переходит между phases, пока:

• exact candidate не bound;
• либо material blocker не запрещает affected continuation.

Обычная граница Codex session не является Human Gate. Следующая session rebind’ит sources и продолжает тот же active_run_id, если run identity и authorization остаются действительными.

AUDIT_RUN

Отдельный run. Read-only относительно candidate и canonical inputs. `active_run_subject_identity` обязан равняться exact `candidate_identity`.

Допустимые outputs:

• audit report;
• derived audit fields в CURRENT STATE.

Candidate content не исправляется.

CORRECTION_RUN

Отдельный bounded writable run только по exact findings и allowed paths. Его subject identity связывает old candidate identity и exact finding bundle identity.

После любого candidate content change:

```text
old candidate identity invalid
old audit result invalid
technical_result.value = NOT_RUN for the next run
```

RE_AUDIT_RUN

Отдельный read-only run по новой candidate identity. `active_run_subject_identity` обязан равняться новой `candidate_identity`.

HUMAN_DECISION

Внешнее действие человека. Codex его не генерирует.

────────

6. Continuous authoring orchestration

AUTHORING_PHASE_0 — Scope Bind

Codex:

• re-checks repository / branch / HEAD / worktree;
• binds selected scope and feature dispositions;
• binds relevant canonical/global sources;
• confirms writable boundary;
• creates ordered document_queue;
• confirms the one already opened AUTHORING_RUN binding.

AUTHORING_PHASE_1 — Full Draft

Codex создаёт skeleton-depth artifacts для всего selected scope, применяя current docs/03_Development.md.

Цель phase:

```text
все необходимые working artifacts существуют
и весь package виден до глубокой шлифовки
```

Non-blocking gaps сохраняются с canonical classification:

```text
UNKNOWN | NOT_FOUND | CONFLICT | PROPOSAL
```

Codex не останавливается после отдельного документа.

AUTHORING_PHASE_2 — Document Refinement

Codex проходит document_queue в authority/dependency order.

Каждый document углубляется по relevant canonical owners. После локального refinement Codex обновляет затронутые downstream references и переходит к следующему document без Human Review.

AUTHORING_PHASE_3 — Package Harmonization

Codex снова рассматривает все artifacts как единый package и выполняет bounded corrections, разрешённые docs/03_Development.md.

Результат phase:

```text
package coherent enough for exact candidate binding
```

Методические критерии authoring, research, WHAT/HOW и harmonization берутся только из canonical owners.

────────

7. Candidate binding

До audit создаётся один derived candidate manifest формата `AOS_CANDIDATE_MANIFEST_R1`.

Manifest не входит в собственный `ARTIFACT` inventory. Он byte-bind’ит candidate subject и вычисляется по следующим exact правилам:

1. Manifest encoded как UTF-8 без BOM, использует только LF и заканчивается одним LF.
2. Первая line — exact ASCII `AOS_CANDIDATE_MANIFEST_R1`.
3. Каждая последующая line имеет exact форму:

```text
<TYPE><TAB><lowercase_sha256><TAB><RFC4648_BASE64_PAYLOAD><LF>
```

4. Base64 использует standard RFC 4648 alphabet с required `=` padding и без line wrapping.
5. Допустимые `TYPE`: `CONTEXT`, `ARTIFACT`, `SOURCE`, `GLOBAL_PACKAGE`, `FEATURE_DOSSIER`, `HUMAN_DECISION`, `LIMITATION`, `UNKNOWN`, `NOT_RUN`, `DECISION_REQUEST`.
6. Для `ARTIFACT` payload — exact UTF-8 repository-relative path bytes, а SHA-256 — digest raw file bytes.
7. Для `SOURCE`, `GLOBAL_PACKAGE`, `FEATURE_DOSSIER` и `HUMAN_DECISION` payload — exact UTF-8 locator bytes, а SHA-256 — digest exact referenced source/manifest/record bytes.
8. Для `CONTEXT`, `LIMITATION`, `UNKNOWN`, `NOT_RUN` и `DECISION_REQUEST` payload — exact UTF-8 statement bytes, а SHA-256 — digest этих payload bytes.
9. Все non-header record lines уникальны и sorted ascending по полным raw UTF-8 line bytes. Duplicate lines запрещены.
10. Candidate обязан содержать минимум один `ARTIFACT` record.
11. `candidate_identity = sha256:<lowercase SHA-256 of the complete manifest bytes>`.

Manifest обязан связывать:

• exact artifact inventory;
• SHA-256 каждого candidate file;
• repository / branch / HEAD;
• relevant canonical source identities;
• accepted Global Design Package manifest identity;
• relevant feature dossier/disposition identity;
• latest applicable human decision record identity;
• limitations, UNKNOWN, NOT_RUN и decision requests.

`candidate_manifest_path` указывает на derived manifest, а `candidate_identity` равен exact manifest identity. Каждый included candidate artifact byte-bound. Любое изменение artifact bytes, source binding или manifest metadata создаёт новый candidate subject. Content identities where practical не допускается.

────────

8. Required rebind и invalidation

Rebind выполняется:

• при adoption;
• при AUTHORING_PHASE_0;
• перед candidate binding;
• перед AUDIT_RUN;
• перед Human Review package assembly;
• после каждого CORRECTION_RUN;
• после relevant global/canonical change;
• при resume новой session.

Если relevant upstream source drift обнаружен:

```text
identify affected documents/claims
→ invalidate affected readiness
→ re-refine/re-harmonize affected boundary
→ bind new candidate
→ re-audit
```

Старый PASS не переносится на новую candidate identity.

────────

9. Orthogonal Current State

CURRENT STATE хранит оси отдельно:

```yaml
program_phase:
current_run_kind:
active_run_id:
active_run_subject_identity:
artifact_state:
human_selection:
  status:
  value:
  record_format:
  record_identity:
  record_locator:
  subject_contract_revision:
  subject_contract_identity:
technical_result:
  value:
  run_id:
  run_kind:
  subject_identity:
  report_identity:
human_decision:
  status:
  value:
  record_identity:
  record_locator:
  subject_candidate_identity:
  accepted_fact_classes: []
feature_disposition:
candidate_identity:
correction_cycle:
blocked_boundary:
control_findings: []
next_action:
```

Правила:

• operational values применяются только к program_phase, current_run_kind, artifact_state;
• `technical_result.value` использует canonical technical vocabulary;
• непустой technical result действителен только когда его run_id, run_kind и subject_identity совпадают с current active run и exact run subject;
• открытие любого нового run atomically меняет run binding и reset’ит `technical_result.value = NOT_RUN` и `report_identity = null`;
• out-of-run guard failures записываются только в `control_findings` и не мутируют `technical_result`;
• human_selection.status допускает только NOT_RUN | COMPLETED, а human_selection.value — только null | ACCEPT;
• COMPLETED human selection требует valid `AOS_PROGRAM_HUMAN_SELECTION_R1` record по Section 2;
• initial selected_start_run_kind допускает только `AUTHORING_RUN | null`;
• successful human selection/adoption atomically устанавливает `contract_status = ADOPTED` и `state_status = CURRENT`;
• human_decision.value допускает только ACCEPT | NEEDS_CHANGES | REJECT | DEFER;
• отсутствие human decision записывается как human_decision.status: NOT_RUN;
• feature_disposition копируется из authoritative source и не мутируется агентом;
• BLOCKED всегда содержит exact affected boundary.

────────

10. Audit transition matrix

|`technical_result.value`|Program effect                                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------|
|`PASS`                  |Assemble exact Human Review subject; `program_phase = HUMAN_REVIEW`; no approval inference                                      |
|`FAIL`                  |`CORRECTION_RUN` only when findings are exact, bounded and do not require human-only decision; otherwise `HUMAN_REVIEW_REQUIRED`|
|`CONTRACT_VIOLATION`    |Do not downgrade; stop affected route or perform exact bounded contract correction when already authorized                      |
|`BLOCKED`               |Stop affected action, record exact blocker and resolution requirement; unaffected read-only work may continue                   |
|`UNKNOWN`               |Expose affected claims; no promotion to `PASS`; request human decision when material                                            |
|`NOT_RUN`               |No promotion; obtain required reviewer or present explicit limitation to human                                                  |
|`HUMAN_REVIEW_REQUIRED` |Assemble exact decision request; Codex must not simulate the decision                                                           |

Audit result применяется только когда `technical_result.run_kind` равен `AUDIT_RUN` или `RE_AUDIT_RUN`, `technical_result.subject_identity` равен audited `candidate_identity`, а `report_identity` связывает exact audit report bytes. Иначе audit result недействителен и остаётся `NOT_RUN` для transition purposes.

Audit is independent only when reviewer context is genuinely independent. Otherwise reviewer independence is NOT_CLAIMED.

────────

11. Correction policy

Correction is allowed only when:

• finding is exact;
• writable boundary is already authorized;
• no new product scope or architecture choice is introduced;
• no human-only decision is required.

Operational limit:

```text
max_correction_cycles = 3
```

После исчерпания лимита или повторения root cause:

```text
technical_result.value = HUMAN_REVIEW_REQUIRED
→ stop
```

────────

12. Human decision transition matrix

Human decision применяется только через exact reproducible decision record. Record обязан связывать:

• decision value;
• `record_identity = sha256:<lowercase SHA-256 of exact raw decision record bytes>`;
• reproducible `record_locator`;
• exact `subject_candidate_identity`;
• candidate manifest identity;
• explicit `accepted_fact_classes` для ACCEPT;
• decision source/provenance.

Current State update допустим только если record bytes доступны, их digest совпадает с `record_identity`, а `subject_candidate_identity` совпадает с current `candidate_identity`. При mismatch human decision остаётся `NOT_RUN`, affected transition не выполняется и создаётся out-of-run control finding с `classification: CONTRACT_VIOLATION` в exact decision-binding boundary. Current `technical_result` не изменяется.

|Human decision |Program effect                                                                                                |
|---------------|--------------------------------------------------------------------------------------------------------------|
|`ACCEPT`       |Exact subject gains human-accepted authority only in fact classes explicitly listed in the bound decision record; current scope may close|
|`NEEDS_CHANGES`|New bounded `AUTHORING_RUN` limited to human findings → harmonization → new candidate → required re-audit     |
|`REJECT`       |Close exact candidate as rejected; feature disposition changes only when human decision explicitly includes it|
|`DEFER`        |Pause exact subject and preserve state; continue only unaffected work explicitly inside current scope         |

Перед новым AUTHORING_RUN после NEEDS_CHANGES создаётся новый run binding и current `technical_result` reset’ится по Section 5. ACCEPT без explicit non-empty `accepted_fact_classes` недействителен.

ACCEPT does not require a universal Feature Freeze or activation step.

Optional placement/publication/binding is performed only when downstream use materially requires it and only under a separate bounded instruction.

Implementation planning is a separate downstream route and is not started by this Program Contract automatically.

────────

13. Global impact

Feature work does not mutate Global Design Package automatically.

```text
GLOBAL_IMPACT_FOUND
→ identify exact affected global claim
→ record separate proposal
→ continue unaffected work
→ explicit human decision before global mutation
```

После accepted global change выполняется affected-boundary rebind/invalidation по Section 8.

────────

14. Stop conditions

Stop affected route at:

• human-only product decision;
• material architecture choice;
• scope expansion;
• feature disposition decision;
• authoritative conflict;
• required canonical/global mutation;
• research scope expansion;
• unavailable required audit;
• correction limit exhaustion;
• runtime implementation boundary;
• Git action boundary;
• inability to establish exact subject identity.

Не блокировать безопасную независимую работу без material dependency.

────────

15. Current State mutation rules

После adoption Codex может изменять только CURRENT STATE и human-authorized working/audit paths.

Каждое Current State update:

• увеличивает state_revision;
• сохраняет program_contract_revision и program_contract_identity;
• не меняет Program Contract;
• не расширяет scope или permissions;
• записывает exact next_action;
• rechecks mutable repository facts when required.

Mismatch между stored contract identity и computed contract identity:

```text
append control_finding:
  classification = CONTRACT_VIOLATION
  subject_identity = <stored program_contract_identity>
  affected_boundary = PROGRAM_CONTRACT_IDENTITY
technical_result = UNCHANGED
→ stop affected program action
```

Mismatch между current run binding и technical result binding:

```text
preserve mismatched technical-result record as Evidence
→ append out-of-run control_finding:
     classification = CONTRACT_VIOLATION
     affected_boundary = RUN_RESULT_BINDING
→ treat technical result as NOT_RUN for transition purposes
→ stop affected promotion
```

────────

16. Completion for current scope

Program scope готов к Human Review, когда:

```text
AUTHORING_RUN completed
→ exact candidate bound
→ required AUDIT_RUN completed
→ transition matrix resolved
```

Current scope завершён только после explicit human decision по exact subject.

Это не требует:

• documentation всех inventory features;
• implementation repository;
• runtime code;
• implementation authorization;
• Git delivery.

────────

17. Operating rule

```text
Use CURRENT STATE to know WHAT IS NEXT.
Use canonical owners to know HOW THE WORK MUST BE DONE.
Continue automatically through the internal AUTHORING_RUN phases.
Use separate audit/correction runs.
Bind every result to its exact run and subject.
Use control findings for out-of-run guard failures without mutating run results.
Stop only at exact human-authority, validation, identity, Git, or runtime boundaries.
```
<!-- PROGRAM_CONTRACT_END -->

CURRENT STATE

```yaml
program_contract_revision: R6
program_contract_identity: sha256:4fb2f220b28f2bbbf45a902b64889fd20bf032efc5cb54a62f7110352d90062d
contract_status: ADOPTED
authority: NONE

state_revision: 6
state_status: CURRENT

predecessor_provenance:
  predecessor_revision: R5
  predecessor_path: workspace/AOS_DOCUMENTATION_PROGRAM_R5.md
  predecessor_full_file_bytes: 32305
  predecessor_full_file_sha256: 6d5ba9c084133f9294bf7d827f0cfef32893d6f64cd907300d672e8004c46efa
  predecessor_program_contract_bytes: 27011
  predecessor_program_contract_sha256: e650fa4fe278da89eb31c38d0357a2854b55ca54d70e83d31f512f1c1be7a3b9
  audit_report_path: workspace/audits/AOS_DOCUMENTATION_X1_PROGRAM_R5_AUDIT.md
  audit_report_bytes: 10685
  audit_report_sha256: 4b7e455bd219c2e5c8430932d082d52164d3b76fd820c4c1d613ed66d7f9a06f
  audit_raw_source_locator: RUNTIME_TURN_ID:019fe507-7eef-7c31-ad56-a3a37d1b6993
  audit_raw_response_item_id: msg_019fe507-8290-7d00-9e67-c8a6e74abca1
  audit_raw_message_bytes: 9376
  audit_raw_message_sha256: 1aaa5b4ccd1468e4334ccb9f1f92d710a2470f8d3d121a8f16d7e57cb8e93ae5
  contract_correction_findings:
    - R5-AUD-F001
    - R5-AUD-F002

human_selection:
  status: COMPLETED
  value: ACCEPT
  record_format: AOS_PROGRAM_HUMAN_SELECTION_R1
  record_identity: sha256:8827f35cd336f8fcaeb2bc4f61808e8254c61e186fe0e2b029cb16b325216616
  record_locator: workspace/AOS_DOCUMENTATION_X1/HUMAN_SELECTION_RECORD.yaml
  subject_contract_revision: R6
  subject_contract_identity: sha256:4fb2f220b28f2bbbf45a902b64889fd20bf032efc5cb54a62f7110352d90062d
  confirmation:
    source_locator: RUNTIME_TURN_ID:019fe53a-adae-7e63-9d3d-fa97511b300f
    response_item_id: msg_019fe53a-b124-7001-954d-003a1cdb5439
    raw_message_bytes: 86
    raw_message_sha256: d4135a253ef581d628e8ddaa0704435bb189c8bb3b50fe766539ded180a6ab92

adoption:
  target_repository: NMF13579/notebook
  target_branch: dev
  observed_draft_HEAD: 90186b5c1bd0f66496cd742dc6a581dbd6f8ba7c
  adoption_HEAD: 90186b5c1bd0f66496cd742dc6a581dbd6f8ba7c
  controller_path: workspace/AOS_DOCUMENTATION_PROGRAM.md
  proposed_writable_boundaries:
    - workspace/AOS_DOCUMENTATION_PROGRAM.md
    - workspace/AOS_DOCUMENTATION_X1/**
    - workspace/audits/AOS_DOCUMENTATION_X1_*.md
  selected_writable_boundaries:
    - workspace/AOS_DOCUMENTATION_PROGRAM.md
    - workspace/AOS_DOCUMENTATION_X1/**
    - workspace/audits/AOS_DOCUMENTATION_X1_*.md
  proposed_allowed_run_kinds:
    - AUTHORING_RUN
    - AUDIT_RUN
    - CORRECTION_RUN
    - RE_AUDIT_RUN
  selected_allowed_run_kinds:
    - AUTHORING_RUN
    - AUDIT_RUN
    - CORRECTION_RUN
    - RE_AUDIT_RUN
  proposed_start_run_kind: AUTHORING_RUN
  selected_start_run_kind: AUTHORING_RUN
  documentation_edit_authorization:
    status: AUTHORIZED
    identity: sha256:ee5c4639a7fb3e86a54d9c2bd305fac44919383ca58d2060c3ddd6ace7728cfc
    allowed_paths:
      - workspace/AOS_DOCUMENTATION_PROGRAM.md
      - workspace/AOS_DOCUMENTATION_X1/**
      - workspace/audits/AOS_DOCUMENTATION_X1_*.md
    allowed_run_kinds:
      - AUTHORING_RUN
      - AUDIT_RUN
      - CORRECTION_RUN
      - RE_AUDIT_RUN
    start_run_kind: AUTHORING_RUN
  implementation_authorization: NONE
  git_authorization: NONE

program_scope:
  label: X1_DOCUMENTATION
  status: CLOSED
  selected_subjects:
    - FTR-001
    - FTR-003

program_phase: COMPLETED
current_run_kind: AUDIT_RUN
active_run_id: AOS-DOC-X1-R6-AUDIT-001
active_run_subject_identity: sha256:1f0d12c3328348126a5882f05e52a512157075e852993018ffb023cd979bf42d
active_run_binding_path: null

artifact_state: HUMAN_ACCEPTED
technical_result:
  value: PASS
  run_id: AOS-DOC-X1-R6-AUDIT-001
  run_kind: AUDIT_RUN
  subject_identity: sha256:1f0d12c3328348126a5882f05e52a512157075e852993018ffb023cd979bf42d
  report_identity: sha256:ba38649d3ea22bacba433fd133aba753259c5df389cbd538460cc03707eb14a5
authoring_report_path: workspace/AOS_DOCUMENTATION_X1/AUTHORING_REPORT.md

human_decision:
  status: COMPLETED
  value: ACCEPT
  record_format: AOS_PROGRAM_HUMAN_DECISION_R1
  record_identity: sha256:3e9fbbcde2d07a8716f0dc28eb33e642e1c42766da738e41c7137abf358af197
  record_locator: workspace/AOS_DOCUMENTATION_X1/HUMAN_DECISION_RECORD.yaml
  subject_candidate_identity: sha256:1f0d12c3328348126a5882f05e52a512157075e852993018ffb023cd979bf42d
  accepted_fact_classes:
    - FTR-001_FEATURE_BEHAVIOR
    - FTR-003_FEATURE_BEHAVIOR
    - X1_ARCHITECTURE_RELATIONSHIPS_AND_INVARIANTS
    - X1_DECISION_REQUEST_DEFINITIONS
    - X1_DR_001_PRODUCT_ARTIFACT_OWNERSHIP
    - X1_DR_002_FIRST_PRODUCT_RUNTIME_SLICE

resolved_decisions:
  X1-DR-001:
    selected_option: A
    record_identity: sha256:3e9fbbcde2d07a8716f0dc28eb33e642e1c42766da738e41c7137abf358af197
  X1-DR-002:
    selected_option: A
    record_identity: sha256:3e9fbbcde2d07a8716f0dc28eb33e642e1c42766da738e41c7137abf358af197

candidate_status: HUMAN_ACCEPTED

feature_disposition:
  FTR-001: SELECT_FOR_X1
  FTR-003: SELECT_FOR_X1

source_bindings:
  path: workspace/AOS_DOCUMENTATION_X1/SOURCE_BINDINGS.yaml
  identity: sha256:0de0ed871c897d9d2e05c2eb3a242819005988cbc30d848fd4163dcf9b1e9cfb
  repository: NMF13579/notebook
  branch: dev
  HEAD: 90186b5c1bd0f66496cd742dc6a581dbd6f8ba7c
document_queue:
  - workspace/AOS_DOCUMENTATION_X1/FTR-001_INTENT_CONTRACT.md
  - workspace/AOS_DOCUMENTATION_X1/FTR-003_SPECIFICATION_AND_SLICE_CONTRACT.md
  - workspace/AOS_DOCUMENTATION_X1/X1_ARCHITECTURE_CONTRACT.md
  - workspace/AOS_DOCUMENTATION_X1/X1_DECISION_REQUESTS.md
  - workspace/AOS_DOCUMENTATION_X1/README.md
candidate_identity: sha256:1f0d12c3328348126a5882f05e52a512157075e852993018ffb023cd979bf42d
candidate_manifest_format: AOS_CANDIDATE_MANIFEST_R1
candidate_manifest_path: workspace/AOS_DOCUMENTATION_X1/CANDIDATE_MANIFEST.txt
audit_report_path: workspace/audits/AOS_DOCUMENTATION_X1_CANDIDATE_1F0D12C3_AUDIT.md
correction_cycle: 0
blocked_boundary: []
control_findings: []
global_impact_findings:
  - finding_id: X1-GI-001
    classification: CONFLICT
    status: RESOLVED_BY_EXPLICIT_HUMAN_DECISION
    affected_claim: first_product_runtime_slice_status
    sources:
      - docs/01_Product.md#section-15
      - docs/00_Core.md#section-17
      - AOS/01_PRODUCT_MODEL.md#section-6
    mutation: NOT_RUN
    resolution: X1-DR-002_OPTION_A
    decision_record_identity: sha256:3e9fbbcde2d07a8716f0dc28eb33e642e1c42766da738e41c7137abf358af197
next_action: OPTIONAL_SEPARATE_PUBLICATION_OR_IMPLEMENTATION_PLANNING_DECISION

```

Adoption transition after successful audit and explicit human selection

```text
contract_status: PROPOSAL
state_status: GENERATED_DRAFT
human_selection.status: NOT_RUN
program_phase: NOT_ACTIVATED
↓
read-only audit PASS bound to exact R6 program_contract_identity
↓
explicit human ACCEPT through exact AOS_PROGRAM_HUMAN_SELECTION_R1 record
+ verified raw record identity and reproducible locator
+ exact revision + computed contract identity
+ selected writable boundaries
+ selected allowed_run_kinds
+ selected_start_run_kind = AUTHORING_RUN or explicit no-start (null)
+ documentation_edit_authorization identity and exact permissions
↓
human_selection.status: COMPLETED
human_selection.value: ACCEPT
human_selection.record_format: AOS_PROGRAM_HUMAN_SELECTION_R1
human_selection.record_identity: <verified record identity>
human_selection.record_locator: <reproducible locator>
adoption_HEAD: <observed exact HEAD at adoption>
selected bindings copied exactly from human decision
contract_status: ADOPTED
state_status: CURRENT
↓
if selected_start_run_kind = AUTHORING_RUN and authorization bindings match:
  program_phase: AUTHORING
  current_run_kind: AUTHORING_RUN
  active_run_id: <new exact run id>
  active_run_subject_identity: <exact adoption-and-scope binding identity>
  artifact_state: SCOPE_BIND_IN_PROGRESS
  technical_result.value: NOT_RUN
  technical_result bound to new active run and subject
  next_action: AUTHORING_PHASE_0_SCOPE_BIND
else if selected_start_run_kind = null:
  program_phase: ADOPTED_IDLE
  current_run_kind: NONE
  active_run_id: null
  artifact_state: NOT_STARTED
  next_action: EXACT_HUMAN_SELECTED_START_ACTION_REQUIRED

Any other initial selected_start_run_kind is invalid before human_selection.status can become COMPLETED; adoption remains NOT_RUN.
```

Git operations remain NOT_RUN.
