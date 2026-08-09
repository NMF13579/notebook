---
document_type: AOS_DOCUMENTATION_PROGRAM_AUDIT_PROVENANCE
document_revision: R1
status: REPORTED_READ_ONLY_AUDIT
authority: EVIDENCE_ONLY
subject_path: workspace/AOS_DOCUMENTATION_PROGRAM.md
subject_revision: R4
subject_full_file_bytes: 26439
subject_full_file_sha256: 54298fffaff28971772375c3c5de98015fb94b03614397b59a500709f64dfeb1
subject_program_contract_bytes: 22607
subject_program_contract_sha256: a4c5412deadefb6632ee23f09455de15b994ee4edb0ce219693ae5402b1b38c6
source_kind: RUNTIME_USER_MESSAGE
source_locator: RUNTIME_TURN_ID:019fe4da-dbd0-7e91-9abc-103440d5654a
source_response_item_id: msg_019fe4da-e37c-7b10-b548-8bb2e3ae0445
source_raw_message_bytes: 4625
source_raw_message_sha256: bb256d8492105b67248700e464c896b0b1f3246f2906fe1e4a91d05828ffa313
capture_rule: EXACT_INPUT_TEXT_BYTES_NO_NORMALIZATION
implementation_authorization: NONE
git_authorization: NONE
---

# AOS Documentation Program R4 — Audit Provenance

This artifact preserves the exact reviewer report supplied by the human from the separate read-only audit context. The payload between the exact marker lines is byte-identical to the source message identified above. Marker lines and their separating LF bytes are not part of the raw-message identity.

<!-- EXACT_AUDIT_REPORT_START -->
technical_result: `FAIL`

Exact identities подтверждены, но candidate не проходит semantic audit: два material contract defect и один blocking provenance gap.

Findings:

1. `R4-AUD-F001 — BLOCKED_R3_PROVENANCE_NOT_FOUND`  
   В [candidate](/Users/muhammed/Documents/GitHub/notebook/workspace/AOS_DOCUMENTATION_PROGRAM.md:6) есть только утверждение о закрытии `R3-F001…R3-F005`. Exact R3 bytes/identity и определения findings отсутствуют в worktree и reachable Git history. Поэтому проверка «закрыты только эти пять findings» объективно `NOT_RUN`; результат — `UNKNOWN/BLOCKED`, не `PASS`.

2. `R4-AUD-F002 — FAIL_RUN_RESULT_BINDING_CONTRADICTION`  
   Contract требует, чтобы любой technical result совпадал с active run binding ([line 374](/Users/muhammed/Documents/GitHub/notebook/workspace/AOS_DOCUMENTATION_PROGRAM.md:374)). Но decision-binding mismatch ([line 437](/Users/muhammed/Documents/GitHub/notebook/workspace/AOS_DOCUMENTATION_PROGRAM.md:437)) и contract-identity mismatch ([line 506](/Users/muhammed/Documents/GitHub/notebook/workspace/AOS_DOCUMENTATION_PROGRAM.md:506)) создают `CONTRACT_VIOLATION` без нового valid run binding. По собственному правилу такой result становится недействительным/`NOT_RUN` для transitions.

3. `R4-AUD-F003 — FAIL_ADOPTION_DECISION_BINDING_INCOMPLETE`  
   Package-level human decision имеет raw-byte digest и locator rules, но pre-adoption `human_selection` — только `identity` без формата, reproducible locator и проверки raw record bytes ([state](/Users/muhammed/Documents/GitHub/notebook/workspace/AOS_DOCUMENTATION_PROGRAM.md:570), [transition](/Users/muhammed/Documents/GitHub/notebook/workspace/AOS_DOCUMENTATION_PROGRAM.md:647)). Поздний decision-record contract требует `candidate_identity` и не может валидировать initial program adoption.

Checks run:

- Full file: `26439` bytes; SHA-256 `54298fffaff28971772375c3c5de98015fb94b03614397b59a500709f64dfeb1`.
- Marker subject: `22607` bytes; SHA-256 `a4c5412deadefb6632ee23f09455de15b994ee4edb0ce219693ae5402b1b38c6`.
- UTF-8 valid, BOM absent, CR bytes `0`, final LF present; exact start/end marker lines `1/1`.
- CURRENT STATE YAML parsed; one block, no duplicate keys.
- Markdown fences balanced: `25/25`; malformed/unclosed `0`.
- Current authority state is safe: `PROPOSAL`, `authority: NONE`, `NOT_ACTIVATED`; selection/edit authorization/human decision `NOT_RUN`; implementation/Git authority `NONE`.
- FTR-001 and FTR-003 dispositions match live [docs/06_Features.md](/Users/muhammed/Documents/GitHub/notebook/docs/06_Features.md:78): both `SELECT_FOR_X1`.
- Routing checked against [AGENTS.md](/Users/muhammed/Documents/GitHub/notebook/AGENTS.md:30), [docs/00_Core.md](/Users/muhammed/Documents/GitHub/notebook/docs/00_Core.md:159), and [docs/03_Development.md](/Users/muhammed/Documents/GitHub/notebook/docs/03_Development.md:108).
- Manifest contract statically inspected; current manifest instance is correctly absent.
- Global Design ordered manifest independently recomputed as `b9ef04820f9e71da1866c61c87417c7ac39d1c27c93a74327ab7f40f2e25aebf`.
- Whitespace checks: tracked/staged/candidate outputs all `0` bytes.

checks_NOT_RUN:

- Exact R3→R4 diff and one-to-one `R3-F001…R3-F005` closure mapping: missing exact R3/finding bundle.
- Candidate manifest instance validation: `candidate_identity/path: null`.
- Human selection, adoption and decision-record validation: `NOT_RUN`.
- AUTHORING/AUDIT/CORRECTION/RE_AUDIT program runs: `NOT_RUN`.
- Commit, Push, Merge, Release: `NOT_RUN`.

reviewer_independence:

- `status: CLAIMED_WITHIN_CURRENT_AUDIT_CONTEXT`
- Fresh read-only checks; no authoring/correction and no historical PASS reused.
- Missing R3 evidence remains an explicit independence limitation.

Repository mutation proof:

- Branch/HEAD before and after: `dev` / `90186b5c1bd0f66496cd742dc6a581dbd6f8ba7c`.
- Status before and after: only `?? workspace/AOS_DOCUMENTATION_PROGRAM.md`.
- Candidate inode, mtime, bytes and SHA unchanged.
- `.git/index` SHA unchanged: `890d76d2dcacb94a35fc2c73316a0f167c5275e10158657de1acfc910d88ddbf`.

```yaml
human_selection: NOT_RUN
adoption: NOT_RUN
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
changed_paths: []
next_required_action: SEPARATE_HUMAN_DECISION_ON_FINDINGS
stop: true
```
<!-- EXACT_AUDIT_REPORT_END -->
