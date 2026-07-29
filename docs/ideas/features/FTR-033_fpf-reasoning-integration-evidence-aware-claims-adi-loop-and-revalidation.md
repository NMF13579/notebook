---
document_id: AOS-FEATURE-FTR-033
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-033
status: DRAFT
authority: NONE
canonical_status: NOT_ASSIGNED
human_acceptance: NOT_REQUESTED
product_scope_effect: NONE
implementation_authorization: NONE
execution_authorized: false
git_authorization: NONE
implementation_repository: UNASSIGNED
repository_verification: NOT_RUN
layer: "Documentation Assembly / Reasoning support"
disposition: CANDIDATE_SUPPORT
source_basis: LATE_CHAT_ADDITION_ACCEPT_WITH_MODIFICATION
source_atomic_functions: [IDEA-093, IDEA-094, IDEA-095, IDEA-096]
human_review_required: true
---

# FTR-033 — FPF Reasoning Integration: Evidence-Aware Claims, ADI Loop and Revalidation

> **Статус:** `DRAFT`, `authority: NONE`. Это подробное человекочитаемое описание candidate feature. Оно не делает feature обязательной и не разрешает implementation.

## 1. Что это

Feature family объединяет coherent user outcome и несколько атомарных функций, перечисленных в разделе 24. Она задаёт problem boundary и observable behavior, но не принимает architecture, dependencies или implementation model.

## 2. Проблема

Specification и architecture proposal могут перескакивать от слабого наблюдения к уверенной рекомендации, не сравнивать alternatives или продолжать использовать stale Evidence.

## 3. Пользователи

Analyst, architect, task planner, reviewer и human decision maker.

## 4. Trigger и inputs

Material claim, ambiguity, contradiction или product/architecture decision требуют явного reasoning. Preconditions: уже существуют requirement IDs, decomposition и traceability foundation. Inputs: claims, source references, alternatives, observations, assumptions и decision subject.

## 5. Observable behavior

`FPF Lite` разделяет `FACT`, `HYPOTHESIS`, `ASSUMPTION`, `PROPOSAL` и `UNKNOWN`, связывает claims с provenance и Evidence, применяет компактный ADI cycle — Abduction создаёт hypotheses, Deduction выводит проверяемые consequences, Induction обновляет confidence по observations. Дополнительно выявляются weakest link и revalidation triggers. Full DRR, quantitative decay/`R_eff`, external retrieval и agent cascade остаются optional later modules.

## 6. Outputs и state model

Outputs: Problem Analysis, hypothesis/alternative matrix, Decision Rationale candidate, weakest-link notice, evidence freshness/revalidation notice и review inputs. States: `CLAIMS_COLLECTED → CLASSIFIED → ALTERNATIVES_READY → ADI_CHECK → WEAK_LINK_FOUND | EVIDENCE_SUFFICIENT | REVALIDATION_REQUIRED → HUMAN_DECISION_REQUIRED`.

## 7. Пользовательский flow

1. Пользователь инициирует feature через chat/CLI/UI и видит exact subject.
2. AOS проверяет upstream context, permissions и material unknowns.
3. Выполняются только необходимые atomic functions; каждая сохраняет собственный result/status.
4. Пользователь видит consolidated result, Evidence, limitations и один следующий шаг.
5. Любой human-only decision остаётся pending до реального human input.

## 8. Scope

### In scope

- Problem и observable outcome, описанные в этом dossier.
- Atomic functions из раздела 24.
- Stable IDs, provenance, explicit states, failure/recovery и human-readable outputs.

### Out of scope

- Автоматическое принятие feature в product scope.
- Неразрешённая implementation, Git delivery или release.
- Hidden dependency/provider/runtime choice.
- Scope expansion на соседние feature families без human decision.

## 9. Functional requirements — `PROPOSAL`

- `FR-033-01` — Feature сохраняет один owner для каждого canonical fact/output.
- `FR-033-02` — Atomic function results собираются без потери individual statuses/limitations.
- `FR-033-03` — UI не скрывает `UNKNOWN`, `BLOCKED`, `NOT_RUN` или partial result.
- `FR-033-04` — Human decision/authorization не выводятся из agent result.
- `FR-033-05` — Material scope or subject change invalidates downstream DRAFT artifacts.
- `FR-033-06` — Failure приводит к report + stop; retries/stage transitions не автоматические.

## 10. Contracts — `PROPOSAL`

- `FeatureInvocation`
- `AtomicFunctionResult[]`
- `FeatureAggregateView`
- `EvidenceReference[]`
- `HumanDecisionReference`
- `NextRequiredAction`

Contract invariants: stable IDs, explicit enums, source binding, no duplicate keys/silent coercion, result status separated from human acceptance.

## 11. UX behavior

- Сначала краткий status/outcome, затем details.
- Каждый blocker объясняет cause, affected subject и required human action.
- Cards/views являются derived и не становятся Source of Truth.
- Beginner/Standard/Expert mode может менять presentation, но не safety semantics.

## 12. Failure and recovery

Failure modes: reasoning graph превращается в bureaucracy, confidence score подменяет judgment, stale Evidence silently поддерживает conclusion, FPF имитирует approval authority. Recovery: свернуть analysis до compact claims/unknowns, явно пометить stale Evidence и запросить targeted revalidation или human decision.

Общий recovery contract:

```text
failure/unknown
→ report + freeze observed state
→ human choice where required
→ separately authorized correction/recovery
→ separate targeted validation
```

## 13. Safety and authority

FPF — external methodology/support layer, не governance и не approval authority. Он не заменяет requirements, task dependencies, acceptance criteria, Validation, Evidence или human checkpoints.

Минимальные invariants:

- PASS/Evidence/CI/readiness ≠ approval.
- UNKNOWN/BLOCKED ≠ OK; NOT_RUN ≠ PASS.
- Agent output ≠ human decision.
- Plan/Task Brief/routing/preview ≠ execution authorization.
- Edit ≠ Commit ≠ Push ≠ PR create ≠ Merge ≠ Release.

## 14. Acceptance expectations — `DESIGNED`, tests `NOT_RUN`

Каждый material conclusion показывает basis, alternatives, weakest assumption и revalidation condition; stale Evidence не остаётся silently current; человек может отклонить recommendation без нарушения workflow. Negative case: numeric confidence не превращается в approval.

## 15. Required negative behavior

- Feature не выполняет соседний stage автоматически.
- Missing source/permission не маскируется default value.
- Legacy/reference content не получает authority.
- Derived UI/index не расходится с owner artifacts.
- Failure/partial state не скрываются.

## 16. Observability and Evidence

Feature aggregate должен позволять восстановить:

```text
source / human decision
→ user problem
→ requirement
→ atomic function invocation
→ output/candidate
→ check result
→ finding/limitation
→ human decision
```

## 17. Minimal implementation model — `PROPOSAL`

Markdown sections/checklists и небольшой rationale validator после decomposition/traceability. Full evidence graph не является early-core dependency.

## 18. Rollout

1. Documentation-only contract.
2. Manual checklist flow.
3. Advisory tool.
4. Guarded execution only if needed.
5. Enforced/automated mode only after architecture/risk decisions.

## 19. Dependencies

Dependencies remain design relationships until explicitly accepted. New libraries, services, providers, registries or Control Plane require human decision.

## 20. Test strategy — `NOT_RUN`

- Unit/contract tests per atomic function.
- Integration tests for family aggregate and status preservation.
- Negative fixtures for missing input, stale source, denied permission and partial failure.
- Human-authority tests: no synthetic approval.
- Traceability test from input to Evidence.

## 21. Open human decisions

- Accept, modify, split, merge, defer or reject this family.
- Assign Product Runtime/support/deferred role.
- Approve exact contracts, paths and dependencies.
- Assign Risk Profile.
- Define required independent validation.

## 22. Source basis and limitations

- Reconstructed from accessible project chat history and read-only reference artifacts.
- Full raw chat export completeness: `UNKNOWN`.
- Current repository/runtime implementation: `NOT_RUN`.
- Detailed requirements and implementation model: `PROPOSAL`.

## 23. Promotion path

```text
DRAFT dossier
→ human product review
→ accepted Feature Contract or DEFER/REJECT
→ Task Brief
→ explicit authorization
→ EXECUTE
→ VALIDATE
→ REVIEW
→ human decision
```

## 24. Отдельные документы атомарных функций

- [`IDEA-093` — Evidence-Aware Claim Classifier and Provenance Binder](../functions/IDEA-093_evidence-aware-claim-classifier-and-provenance-binder.md)
- [`IDEA-094` — ADI Reasoning Cycle: Abduction → Deduction → Induction](../functions/IDEA-094_adi-reasoning-cycle-abduction-to-deduction-to-induction.md)
- [`IDEA-095` — Alternative Matrix and Weakest-Link Analysis](../functions/IDEA-095_alternative-matrix-and-weakest-link-analysis.md)
- [`IDEA-096` — Evidence Decay and Revalidation Trigger Manager](../functions/IDEA-096_evidence-decay-and-revalidation-trigger-manager.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_033`
