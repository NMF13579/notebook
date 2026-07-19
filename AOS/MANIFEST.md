# AOS Document Manifest

## Authority

This file is the active ownership registry. Each topic has exactly one canonical owner.

- Allowed topic statuses are `canonical` and `reference-only`.
- Section README files are navigation-only.
- Provenance records have authority `NONE`.
- Migration history is maintained in `AOS/05_Reference/Provenance/`.
- Provenance records preserve historical identities and Git recovery references; physical legacy source copies are not retained in the current repository tree.

## Ownership

| Topic ID | Topic | Canonical owner | Status | Disposition | Provenance |
|---|---|---|---|---|---|
| `project-identity` | Project identity | `AOS/00_Core/Project_Identity.md` | `canonical` | `active-normative` | [PR-001](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-001) |
| `project-principles` | Project principles | `AOS/00_Core/Project_Principles.md` | `canonical` | `active-normative` | [PR-002](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-002) |
| `minimal-safety-floor` | Minimal safety floor | `AOS/00_Core/Minimal_Safety_Floor.md` | `canonical` | `active-normative` | [PR-003](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-003) |
| `product-vision` | Product vision | `AOS/01_Product/Product_Vision.md` | `canonical` | `active-normative` | [PR-004](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-004) |
| `target-user-and-core-problem` | Target user and core problem | `AOS/01_Product/Target_User_and_Core_Problem.md` | `canonical` | `active-normative` | [PR-005](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-005) |
| `product-outcome` | Product outcome | `AOS/01_Product/Product_Outcome.md` | `canonical` | `active-normative` | [PR-006](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-006) |
| `first-vertical-slice` | First vertical slice | `AOS/01_Product/First_Vertical_Slice.md` | `canonical` | `active-normative` | [PR-007](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-007) |
| `primary-user-journey` | Primary user journey | `AOS/01_Product/Primary_User_Journey.md` | `canonical` | `active-normative` | [PR-008](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-008) |
| `product-contracts-and-observable-behavior` | Product contracts and observable behavior | `AOS/01_Product/Product_Contracts_and_Observable_Behavior.md` | `canonical` | `active-normative` | [PR-009](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-009) |
| `acceptance-criteria` | Acceptance criteria | `AOS/01_Product/Acceptance_Criteria.md` | `canonical` | `active-normative` | [PR-010](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-010) |
| `product-boundaries-and-success-metrics` | Product boundaries and success metrics | `AOS/01_Product/Product_Boundaries_and_Success_Metrics.md` | `canonical` | `active-normative` | [PR-011](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-011) |
| `project-skeleton` | Project skeleton | `AOS/02_Architecture/Project_Skeleton.md` | `canonical` | `active-normative` | [PR-012](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-012) |
| `workspace-foundation` | Workspace foundation | `AOS/02_Architecture/Workspace_Foundation.md` | `canonical` | `active-normative` | [PR-013](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-013) |
| `agent-contract` | Agent contract | `AOS/02_Architecture/Agent_Contract.md` | `canonical` | `active-normative` | [PR-014](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-014) |
| `git-foundation` | Git foundation | `AOS/02_Architecture/Git_Foundation.md` | `canonical` | `active-normative` | [PR-015](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-015) |
| `task-and-report-templates` | Task and report templates | `AOS/03_Development/Task_And_Report_Templates.md` | `canonical` | `active-normative` | [PR-016](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-016) |
| `local-development-environment` | Local development environment | `AOS/03_Development/Local_Development_Environment.md` | `canonical` | `active-normative` | [PR-017](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-017) |
| `minimal-checks-and-ci` | Minimal checks and CI | `AOS/03_Development/Minimal_Checks_And_CI.md` | `canonical` | `active-normative` | [PR-018](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-018) |
| `first-manual-workflow` | First manual workflow | `AOS/03_Development/First_Manual_Workflow.md` | `canonical` | `active-normative` | [PR-019](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-019) |
| `development-model` | Development model | `AOS/03_Development/Development_Model.md` | `canonical` | `active-normative` | [PR-020](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-020) |
| `task-model` | Task model | `AOS/03_Development/Task_Model.md` | `canonical` | `active-normative` | [PR-021](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-021) |
| `execution-model` | Execution model | `AOS/03_Development/Execution_Model.md` | `canonical` | `active-normative` | [PR-022](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-022) |
| `validation-model` | Validation model | `AOS/03_Development/Validation_Model.md` | `canonical` | `active-normative` | [PR-023](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-023) |
| `decision-model` | Decision model | `AOS/03_Development/Decision_Model.md` | `canonical` | `active-normative` | [PR-024](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-024) |
| `project-memory` | Project memory | `AOS/03_Development/Project_Memory.md` | `canonical` | `active-normative` | [PR-025](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-025) |
| `recovery-model` | Recovery model | `AOS/03_Development/Recovery_Model.md` | `canonical` | `active-normative` | [PR-026](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-026) |
| `development-factory` | Development factory | `AOS/03_Development/Development_Factory.md` | `canonical` | `active-normative` | [PR-027](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-027) |
| `agent-collaboration` | Agent collaboration | `AOS/03_Development/Agent_Collaboration.md` | `canonical` | `active-normative` | [PR-028](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-028) |
| `process-evolution` | Process evolution | `AOS/03_Development/Process_Evolution.md` | `canonical` | `active-normative` | [PR-029](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-029) |
| `anti-patterns-and-lessons` | Anti-patterns and lessons | `AOS/04_Lessons/Anti_Patterns_and_Lessons.md` | `canonical` | `active-normative` | [PR-030](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-030) |
| `reconstruction-roadmap` | Reconstruction roadmap | `AOS/05_Reference/Reconstruction_Roadmap.md` | `reference-only` | `deferred-reference` | [PR-031](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-031) |
| `control-overview` | Control overview | `AOS/05_Reference/Control/README.md` | `reference-only` | `deferred-reference` | [PR-032](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-032) |
| `control-purpose-and-boundaries` | Control Purpose and Boundaries | `AOS/05_Reference/Control/Control_Purpose_and_Boundaries.md` | `reference-only` | `deferred-reference` | [PR-033](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-033) |
| `human-authority-and-decision-rights` | Human Authority and Decision Rights | `AOS/05_Reference/Control/Human_Authority_and_Decision_Rights.md` | `reference-only` | `deferred-reference` | [PR-034](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-034) |
| `claims-evidence-review-and-decisions` | Claims, Evidence, Review and Decisions | `AOS/05_Reference/Control/Claims_Evidence_Review_and_Decisions.md` | `reference-only` | `deferred-reference` | [PR-035](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-035) |
| `risk-unknowns-and-stop-rules` | Risk, Unknowns and Stop Rules | `AOS/05_Reference/Control/Risk_Unknowns_and_Stop_Rules.md` | `reference-only` | `deferred-reference` | [PR-036](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-036) |
| `control-points-in-product-and-development-workflows` | Control Points in Product and Development Workflows | `AOS/05_Reference/Control/Control_Points_in_Product_and_Development_Workflows.md` | `reference-only` | `deferred-reference` | [PR-037](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-037) |
| `source-of-truth-and-protected-changes` | Source of Truth and Protected Changes | `AOS/05_Reference/Control/Source_of_Truth_and_Protected_Changes.md` | `reference-only` | `deferred-reference` | [PR-038](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-038) |
| `execution-git-and-destructive-authorization` | Execution, Git and Destructive Authorization | `AOS/05_Reference/Control/Execution_Git_and_Destructive_Authorization.md` | `reference-only` | `deferred-reference` | [PR-039](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-039) |
| `control-failure-modes-and-anti-patterns` | Control Failure Modes and Anti-Patterns | `AOS/05_Reference/Control/Control_Failure_Modes_and_Anti_Patterns.md` | `reference-only` | `deferred-reference` | [PR-040](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-040) |
| `progressive-control-evolution` | Progressive Control Evolution | `AOS/05_Reference/Control/Progressive_Control_Evolution.md` | `reference-only` | `deferred-reference` | [PR-041](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-041) |
| `advanced-overview` | Advanced overview | `AOS/05_Reference/Advanced/README.md` | `reference-only` | `deferred-reference` | [PR-042](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-042) |
| `admission-criteria` | Admission Criteria | `AOS/05_Reference/Advanced/Admission_Criteria.md` | `reference-only` | `deferred-reference` | [PR-043](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-043) |
| `architecture-evolution` | Architecture Evolution | `AOS/05_Reference/Advanced/Architecture_Evolution.md` | `reference-only` | `deferred-reference` | [PR-044](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-044) |
| `automation-principles` | Automation Principles | `AOS/05_Reference/Advanced/Automation_Principles.md` | `reference-only` | `deferred-reference` | [PR-045](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-045) |
| `runtime-enforcement` | Runtime Enforcement | `AOS/05_Reference/Advanced/Runtime_Enforcement.md` | `reference-only` | `deferred-reference` | [PR-046](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-046) |
| `registries-and-indexes` | Registries and Indexes | `AOS/05_Reference/Advanced/Registries_and_Indexes.md` | `reference-only` | `deferred-reference` | [PR-047](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-047) |
| `external-integrations` | External Integrations | `AOS/05_Reference/Advanced/External_Integrations.md` | `reference-only` | `deferred-reference` | [PR-048](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-048) |
| `multi-project-support` | Multi Project Support | `AOS/05_Reference/Advanced/Multi_Project_Support.md` | `reference-only` | `deferred-reference` | [PR-049](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-049) |
| `scaling` | Scaling | `AOS/05_Reference/Advanced/Scaling.md` | `reference-only` | `deferred-reference` | [PR-050](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-050) |
| `operational-lessons` | Operational Lessons | `AOS/05_Reference/Advanced/Operational_Lessons.md` | `reference-only` | `deferred-reference` | [PR-051](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-051) |
| `retirement-and-simplification` | Retirement and Simplification | `AOS/05_Reference/Advanced/Retirement_and_Simplification.md` | `reference-only` | `deferred-reference` | [PR-052](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-052) |
| `research-overview` | Research overview | `AOS/05_Reference/Research/README.md` | `reference-only` | `deferred-reference` | [PR-053](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-053) |
| `reconstruction-research-method` | Reconstruction Research Method | `AOS/05_Reference/Research/Reconstruction_Research_Method.md` | `reference-only` | `deferred-reference` | [PR-054](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-054) |
| `legacy-lessons-and-failure-modes` | Legacy Lessons and Failure Modes | `AOS/05_Reference/Research/Legacy_Lessons_and_Failure_Modes.md` | `reference-only` | `deferred-reference` | [PR-055](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-055) |
| `product-behavior-reconstruction` | Product Behavior Reconstruction | `AOS/05_Reference/Research/Product_Behavior_Reconstruction.md` | `reference-only` | `deferred-reference` | [PR-056](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-056) |
| `contract-reconstruction-research` | Contract Reconstruction Research | `AOS/05_Reference/Research/Contract_Reconstruction_Research.md` | `reference-only` | `deferred-reference` | [PR-057](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-057) |
| `architecture-alternatives` | Architecture Alternatives | `AOS/05_Reference/Research/Architecture_Alternatives.md` | `reference-only` | `deferred-reference` | [PR-058](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-058) |
| `model-routing-and-task-decomposition` | Model Routing and Task Decomposition | `AOS/05_Reference/Research/Model_Routing_and_Task_Decomposition.md` | `reference-only` | `deferred-reference` | [PR-059](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-059) |
| `agent-and-harness-engineering` | Agent and Harness Engineering | `AOS/05_Reference/Research/Agent_and_Harness_Engineering.md` | `reference-only` | `deferred-reference` | [PR-060](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-060) |
| `future-capability-candidates` | Future Capability Candidates | `AOS/05_Reference/Research/Future_Capability_Candidates.md` | `reference-only` | `deferred-reference` | [PR-061](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-061) |
| `open-questions-and-experiments` | Open Questions and Experiments | `AOS/05_Reference/Research/Open_Questions_and_Experiments.md` | `reference-only` | `deferred-reference` | [PR-062](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-062) |
| `references-overview` | References overview | `AOS/05_Reference/References/README.md` | `reference-only` | `deferred-reference` | [PR-063](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-063) |
| `reference-policy` | Reference Policy | `AOS/05_Reference/References/Reference_Policy.md` | `reference-only` | `deferred-reference` | [PR-064](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-064) |
| `knowledge-extraction` | Knowledge Extraction | `AOS/05_Reference/References/Knowledge_Extraction.md` | `reference-only` | `deferred-reference` | [PR-065](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-065) |
| `aos-farm` | AOS-FARM | `AOS/05_Reference/References/AOS_FARM.md` | `reference-only` | `deferred-reference` | [PR-066](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-066) |
| `agentos-and-aos-1` | AgentOS and AOS-1 | `AOS/05_Reference/References/AgentOS_AOS1.md` | `reference-only` | `deferred-reference` | [PR-067](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-067) |
| `external-references` | External References | `AOS/05_Reference/References/External_References.md` | `reference-only` | `deferred-reference` | [PR-068](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-068) |
| `research-materials` | Research Materials | `AOS/05_Reference/References/Research_Materials.md` | `reference-only` | `deferred-reference` | [PR-069](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-069) |
| `source-conversations` | Source Conversations | `AOS/05_Reference/References/Source_Conversations.md` | `reference-only` | `deferred-reference` | [PR-070](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-070) |
| `reference-catalog` | Reference Catalog | `AOS/05_Reference/References/Reference_Catalog.md` | `reference-only` | `deferred-reference` | [PR-071](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-071) |
| `historical-archive` | Historical Archive | `AOS/05_Reference/References/Historical_Archive.md` | `reference-only` | `deferred-reference` | [PR-072](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-072) |
| `archive-overview` | Archive overview | `AOS/05_Reference/Archive/README.md` | `reference-only` | `deferred-reference` | [PR-073](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-073) |
| `archive-policy` | Archive Policy | `AOS/05_Reference/Archive/Archive_Policy.md` | `reference-only` | `deferred-reference` | [PR-074](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-074) |
| `superseded-project-artifacts` | Superseded Project Artifacts | `AOS/05_Reference/Archive/Superseded_Project_Artifacts.md` | `reference-only` | `deferred-reference` | [PR-075](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-075) |
| `rejected-project-proposals` | Rejected Project Proposals | `AOS/05_Reference/Archive/Rejected_Project_Proposals.md` | `reference-only` | `deferred-reference` | [PR-076](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-076) |
| `obsolete-project-plans` | Obsolete Project Plans | `AOS/05_Reference/Archive/Obsolete_Project_Plans.md` | `reference-only` | `deferred-reference` | [PR-077](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-077) |
| `closed-temporary-artifacts` | Closed Temporary Artifacts | `AOS/05_Reference/Archive/Closed_Temporary_Artifacts.md` | `reference-only` | `deferred-reference` | [PR-078](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-078) |
| `archive-register` | Archive Register | `AOS/05_Reference/Archive/Archive_Register.md` | `reference-only` | `deferred-reference` | [PR-079](05_Reference/Provenance/PROVENANCE_REGISTER.md#pr-079) |

## Rules

- One canonical owner exists per topic.
- This registry does not duplicate normative topic content.
- Provenance does not create authority.
- `05_Reference` remains reference-only unless separately promoted.
- Old trees and META remain non-canonical.
- Move and deletion require separate authorization.
