# AOS Document Manifest

## Authority

This file is the single canonical manifest for document location, topic ownership, migration status, and legacy provenance after migration stages M4–M6. It does not replace the normative content of a topic document.

Rules:

1. Each topic has exactly one canonical target path in the tables below.
2. A target topic file is either a byte-identical copy of its declared legacy source at baseline `b4645d6a6fd6f9e7b2be8c9a85e4c9601a4a68f7` or is explicitly classified in the authored transformation registry below.
3. Legacy Markdown sources are retained for later destructive review. Their migration status is `superseded-source`; they are not competing normative sources.
4. Old aggregate documents and placeholder shortcuts are retained but are not canonical. Unique aggregate content is consolidated into the declared canonical target while the source remains preserved for later destructive review.
5. All distributed `*_META.yml` files are `superseded-metadata`. This manifest replaces them for document location and migration status; their historical fields remain evidence only.
6. Section README files are navigation only. They link to canonical topics and must not duplicate normative text.
7. `05_Reference` material is deferred/reference-only unless a separate authorized decision promotes a statement into an active canonical topic.

## Canonical active topics

| Topic | Canonical target | Legacy source | Status |
|---|---|---|---|
| Project identity | [`00_Core/Project_Identity.md`](00_Core/Project_Identity.md) | `01_Project/01.01_Project_Identity/01.01.00_README.md` | canonical |
| Project principles | [`00_Core/Project_Principles.md`](00_Core/Project_Principles.md) | `01_Project/01.03_Project_Principles/01.03.00_README.md` | canonical |
| Minimal safety floor | [`00_Core/Minimal_Safety_Floor.md`](00_Core/Minimal_Safety_Floor.md) | `02_Scaffolding/02.06_Minimal_Safety_Floor/02.06.00_README.md` | canonical |
| Product vision | [`01_Product/Product_Vision.md`](01_Product/Product_Vision.md) | `01_Project/01.02_Product_Vision/01.02.00_README.md` | canonical |
| Target user and core problem | [`01_Product/Target_User_and_Core_Problem.md`](01_Product/Target_User_and_Core_Problem.md) | `03_Product/03.01_Target_User_and_Core_Problem/03.01.00_README.md` | canonical |
| Product outcome | [`01_Product/Product_Outcome.md`](01_Product/Product_Outcome.md) | `03_Product/03.02_Product_Outcome/03.02.00_README.md` | canonical |
| First vertical slice | [`01_Product/First_Vertical_Slice.md`](01_Product/First_Vertical_Slice.md) | `03_Product/03.03_First_Vertical_Slice/03.03.00_README.md` | canonical |
| Primary user journey | [`01_Product/Primary_User_Journey.md`](01_Product/Primary_User_Journey.md) | `03_Product/03.04_Primary_User_Journey/03.04.00_README.md` | canonical |
| Product contracts and observable behavior | [`01_Product/Product_Contracts_and_Observable_Behavior.md`](01_Product/Product_Contracts_and_Observable_Behavior.md) | `03_Product/03.05_Product_Contracts_and_Observable_Behavior/03.05.00_README.md` | canonical |
| Acceptance criteria | [`01_Product/Acceptance_Criteria.md`](01_Product/Acceptance_Criteria.md) | `03_Product/03.06_Acceptance_Criteria/03.06.00_README.md` | canonical |
| Product boundaries and success metrics | [`01_Product/Product_Boundaries_and_Success_Metrics.md`](01_Product/Product_Boundaries_and_Success_Metrics.md) | `03_Product/03.00_README.md` | canonical |
| Project skeleton | [`02_Architecture/Project_Skeleton.md`](02_Architecture/Project_Skeleton.md) | `02_Scaffolding/02.01_Project_Skeleton/02.01.00_README.md` | canonical |
| Workspace foundation | [`02_Architecture/Workspace_Foundation.md`](02_Architecture/Workspace_Foundation.md) | `02_Scaffolding/02.02_Workspace_Foundation/02.02.00_README.md` | canonical |
| Agent contract | [`02_Architecture/Agent_Contract.md`](02_Architecture/Agent_Contract.md) | `02_Scaffolding/02.03_Agent_Contract/02.03.00_README.md` | canonical |
| Git foundation | [`02_Architecture/Git_Foundation.md`](02_Architecture/Git_Foundation.md) | `02_Scaffolding/02.04_Git_Foundation/02.04.00_README.md` | canonical |
| Task and report templates | [`03_Development/Task_And_Report_Templates.md`](03_Development/Task_And_Report_Templates.md) | `02_Scaffolding/02.05_Task_And_Report_Templates/02.05.00_README.md` | canonical |
| Local development environment | [`03_Development/Local_Development_Environment.md`](03_Development/Local_Development_Environment.md) | `02_Scaffolding/02.07_Local_Development_Environment/02.07.00_README.md` | canonical |
| Minimal checks and CI | [`03_Development/Minimal_Checks_And_CI.md`](03_Development/Minimal_Checks_And_CI.md) | `02_Scaffolding/02.08_Minimal_Checks_And_CI/02.08.00_README.md` | canonical |
| First manual workflow | [`03_Development/First_Manual_Workflow.md`](03_Development/First_Manual_Workflow.md) | `02_Scaffolding/02.09_First_Manual_Workflow/02.09.00_README.md` | canonical |
| Development model | [`03_Development/Development_Model.md`](03_Development/Development_Model.md) | `04_Development/04.01_Development_Model/04.01.00_README.md` | canonical |
| Task model | [`03_Development/Task_Model.md`](03_Development/Task_Model.md) | `04_Development/04.02_Task_Model/04.02.00_README.md` | canonical |
| Execution model | [`03_Development/Execution_Model.md`](03_Development/Execution_Model.md) | `04_Development/04.03_Execution_Model/04.03.00_README.md` | canonical |
| Validation model | [`03_Development/Validation_Model.md`](03_Development/Validation_Model.md) | `04_Development/04.04_Validation_Model/04.04.00_README.md` | canonical |
| Decision model | [`03_Development/Decision_Model.md`](03_Development/Decision_Model.md) | `04_Development/04.05_Decision_Model/04.05.00_README.md` | canonical |
| Project memory | [`03_Development/Project_Memory.md`](03_Development/Project_Memory.md) | `04_Development/04.06_Project_Memory/04.06.00_README.md` | canonical |
| Recovery model | [`03_Development/Recovery_Model.md`](03_Development/Recovery_Model.md) | `04_Development/04.07_Recovery_Model/04.07.00_README.md` | canonical |
| Development factory | [`03_Development/Development_Factory.md`](03_Development/Development_Factory.md) | `04_Development/04.08_Development_Factory/04.08.00_README.md` | canonical |
| Agent collaboration | [`03_Development/Agent_Collaboration.md`](03_Development/Agent_Collaboration.md) | `04_Development/04.09_Agent_Collaboration/04.09.00_README.md` | canonical |
| Process evolution | [`03_Development/Process_Evolution.md`](03_Development/Process_Evolution.md) | `04_Development/04.10_Process_Evolution/04.10.00_README.md` | canonical |
| Anti-patterns and lessons | [`04_Lessons/Anti_Patterns_and_Lessons.md`](04_Lessons/Anti_Patterns_and_Lessons.md) | `04_Development/04.11_Anti_Patterns_and_Lessons/04.11.00_README.md` | canonical |

## Deferred reference topics

All rows in this section have status `reference-only`. The target is the sole maintained location for that reference topic; the legacy source is superseded.

| Topic | Canonical target | Legacy source |
|---|---|---|
| Reconstruction roadmap | [`05_Reference/Reconstruction_Roadmap.md`](05_Reference/Reconstruction_Roadmap.md) | `01_Project/01.00_README.md` |
| Control overview | [`05_Reference/Control/README.md`](05_Reference/Control/README.md) | `05_Control/05.00_README.md` |
| Control Purpose and Boundaries | [`05_Reference/Control/Control_Purpose_and_Boundaries.md`](05_Reference/Control/Control_Purpose_and_Boundaries.md) | `05_Control/05.01_Control_Purpose_and_Boundaries/05.01.00_README.md` |
| Human Authority and Decision Rights | [`05_Reference/Control/Human_Authority_and_Decision_Rights.md`](05_Reference/Control/Human_Authority_and_Decision_Rights.md) | `05_Control/05.02_Human_Authority_and_Decision_Rights/05.02.00_README.md` |
| Claims, Evidence, Review and Decisions | [`05_Reference/Control/Claims_Evidence_Review_and_Decisions.md`](05_Reference/Control/Claims_Evidence_Review_and_Decisions.md) | `05_Control/05.03_Claims_Evidence_Review_and_Decisions/05.03.00_README.md` |
| Risk, Unknowns and Stop Rules | [`05_Reference/Control/Risk_Unknowns_and_Stop_Rules.md`](05_Reference/Control/Risk_Unknowns_and_Stop_Rules.md) | `05_Control/05.04_Risk_Unknowns_and_Stop_Rules/05.04.00_README.md` |
| Control Points in Product and Development Workflows | [`05_Reference/Control/Control_Points_in_Product_and_Development_Workflows.md`](05_Reference/Control/Control_Points_in_Product_and_Development_Workflows.md) | `05_Control/05.05_Control_Points_in_Product_and_Development_Workflows/05.05.00_README.md` |
| Source of Truth and Protected Changes | [`05_Reference/Control/Source_of_Truth_and_Protected_Changes.md`](05_Reference/Control/Source_of_Truth_and_Protected_Changes.md) | `05_Control/05.06_Source_of_Truth_and_Protected_Changes/05.06.00_README.md` |
| Execution, Git and Destructive Authorization | [`05_Reference/Control/Execution_Git_and_Destructive_Authorization.md`](05_Reference/Control/Execution_Git_and_Destructive_Authorization.md) | `05_Control/05.07_Execution_Git_and_Destructive_Authorization/05.07.00_README.md` |
| Control Failure Modes and Anti-Patterns | [`05_Reference/Control/Control_Failure_Modes_and_Anti_Patterns.md`](05_Reference/Control/Control_Failure_Modes_and_Anti_Patterns.md) | `05_Control/05.08_Control_Failure_Modes_and_Anti_Patterns/05.08.00_README.md` |
| Progressive Control Evolution | [`05_Reference/Control/Progressive_Control_Evolution.md`](05_Reference/Control/Progressive_Control_Evolution.md) | `05_Control/05.09_Progressive_Control_Evolution/05.09.00_README.md` |
| Advanced overview | [`05_Reference/Advanced/README.md`](05_Reference/Advanced/README.md) | `06_Advanced/06.00_README.md` |
| Admission Criteria | [`05_Reference/Advanced/Admission_Criteria.md`](05_Reference/Advanced/Admission_Criteria.md) | `06_Advanced/06.01_Admission_Criteria/06.01.00_README.md` |
| Architecture Evolution | [`05_Reference/Advanced/Architecture_Evolution.md`](05_Reference/Advanced/Architecture_Evolution.md) | `06_Advanced/06.02_Architecture_Evolution/06.02.00_README.md` |
| Automation Principles | [`05_Reference/Advanced/Automation_Principles.md`](05_Reference/Advanced/Automation_Principles.md) | `06_Advanced/06.03_Automation_Principles/06.03.00_README.md` |
| Runtime Enforcement | [`05_Reference/Advanced/Runtime_Enforcement.md`](05_Reference/Advanced/Runtime_Enforcement.md) | `06_Advanced/06.04_Runtime_Enforcement/06.04.00_README.md` |
| Registries and Indexes | [`05_Reference/Advanced/Registries_and_Indexes.md`](05_Reference/Advanced/Registries_and_Indexes.md) | `06_Advanced/06.05_Registries_and_Indexes/06.05.00_README.md` |
| External Integrations | [`05_Reference/Advanced/External_Integrations.md`](05_Reference/Advanced/External_Integrations.md) | `06_Advanced/06.06_External_Integrations/06.06.00_README.md` |
| Multi Project Support | [`05_Reference/Advanced/Multi_Project_Support.md`](05_Reference/Advanced/Multi_Project_Support.md) | `06_Advanced/06.07_Multi_Project_Support/06.07.00_README.md` |
| Scaling | [`05_Reference/Advanced/Scaling.md`](05_Reference/Advanced/Scaling.md) | `06_Advanced/06.08_Scaling/06.08.00_README.md` |
| Operational Lessons | [`05_Reference/Advanced/Operational_Lessons.md`](05_Reference/Advanced/Operational_Lessons.md) | `06_Advanced/06.09_Operational_Lessons/06.09.00_README.md` |
| Retirement and Simplification | [`05_Reference/Advanced/Retirement_and_Simplification.md`](05_Reference/Advanced/Retirement_and_Simplification.md) | `06_Advanced/06.10_Retirement_and_Simplification/06.10.00_README.md` |
| Research overview | [`05_Reference/Research/README.md`](05_Reference/Research/README.md) | `07_Research/07.00_README.md` |
| Reconstruction Research Method | [`05_Reference/Research/Reconstruction_Research_Method.md`](05_Reference/Research/Reconstruction_Research_Method.md) | `07_Research/07.01_Reconstruction_Research_Method/07.01.00_README.md` |
| Legacy Lessons and Failure Modes | [`05_Reference/Research/Legacy_Lessons_and_Failure_Modes.md`](05_Reference/Research/Legacy_Lessons_and_Failure_Modes.md) | `07_Research/07.02_Legacy_Lessons_and_Failure_Modes/07.02.00_README.md` |
| Product Behavior Reconstruction | [`05_Reference/Research/Product_Behavior_Reconstruction.md`](05_Reference/Research/Product_Behavior_Reconstruction.md) | `07_Research/07.03_Product_Behavior_Reconstruction/07.03.00_README.md` |
| Contract Reconstruction Research | [`05_Reference/Research/Contract_Reconstruction_Research.md`](05_Reference/Research/Contract_Reconstruction_Research.md) | `07_Research/07.04_Contract_Reconstruction_Research/07.04.00_README.md` |
| Architecture Alternatives | [`05_Reference/Research/Architecture_Alternatives.md`](05_Reference/Research/Architecture_Alternatives.md) | `07_Research/07.05_Architecture_Alternatives/07.05.00_README.md` |
| Model Routing and Task Decomposition | [`05_Reference/Research/Model_Routing_and_Task_Decomposition.md`](05_Reference/Research/Model_Routing_and_Task_Decomposition.md) | `07_Research/07.06_Model_Routing_and_Task_Decomposition/07.06.00_README.md` |
| Agent and Harness Engineering | [`05_Reference/Research/Agent_and_Harness_Engineering.md`](05_Reference/Research/Agent_and_Harness_Engineering.md) | `07_Research/07.07_Agent_and_Harness_Engineering/07.07.00_README.md` |
| Future Capability Candidates | [`05_Reference/Research/Future_Capability_Candidates.md`](05_Reference/Research/Future_Capability_Candidates.md) | `07_Research/07.08_Future_Capability_Candidates/07.08.00_README.md` |
| Open Questions and Experiments | [`05_Reference/Research/Open_Questions_and_Experiments.md`](05_Reference/Research/Open_Questions_and_Experiments.md) | `07_Research/07.09_Open_Questions_and_Experiments/07.09.00_README.md` |
| References overview | [`05_Reference/References/README.md`](05_Reference/References/README.md) | `08_References/08.00_README.md` |
| Reference Policy | [`05_Reference/References/Reference_Policy.md`](05_Reference/References/Reference_Policy.md) | `08_References/08.01_Reference_Policy/08.01.00_README.md` |
| Knowledge Extraction | [`05_Reference/References/Knowledge_Extraction.md`](05_Reference/References/Knowledge_Extraction.md) | `08_References/08.02_Knowledge_Extraction/08.02.00_README.md` |
| AOS-FARM | [`05_Reference/References/AOS_FARM.md`](05_Reference/References/AOS_FARM.md) | `08_References/08.03_AOS_FARM/08.03.00_README.md` |
| AgentOS and AOS-1 | [`05_Reference/References/AgentOS_AOS1.md`](05_Reference/References/AgentOS_AOS1.md) | `08_References/08.04_AgentOS_AOS1/08.04.00_README.md` |
| External References | [`05_Reference/References/External_References.md`](05_Reference/References/External_References.md) | `08_References/08.05_External_References/08.05.00_README.md` |
| Research Materials | [`05_Reference/References/Research_Materials.md`](05_Reference/References/Research_Materials.md) | `08_References/08.06_Research_Materials/08.06.00_README.md` |
| Source Conversations | [`05_Reference/References/Source_Conversations.md`](05_Reference/References/Source_Conversations.md) | `08_References/08.07_Source_Conversations/08.07.00_README.md` |
| Reference Catalog | [`05_Reference/References/Reference_Catalog.md`](05_Reference/References/Reference_Catalog.md) | `08_References/08.08_Reference_Catalog/08.08.00_README.md` |
| Historical Archive | [`05_Reference/References/Historical_Archive.md`](05_Reference/References/Historical_Archive.md) | `08_References/08.09_Historical_Archive/08.09.00_README.md` |
| Archive overview | [`05_Reference/Archive/README.md`](05_Reference/Archive/README.md) | `09_Archive/09.00_README.md` |
| Archive Policy | [`05_Reference/Archive/Archive_Policy.md`](05_Reference/Archive/Archive_Policy.md) | `09_Archive/09.01_Archive_Policy/09.01.00_README.md` |
| Superseded Project Artifacts | [`05_Reference/Archive/Superseded_Project_Artifacts.md`](05_Reference/Archive/Superseded_Project_Artifacts.md) | `09_Archive/09.02_Superseded_Project_Artifacts/09.02.00_README.md` |
| Rejected Project Proposals | [`05_Reference/Archive/Rejected_Project_Proposals.md`](05_Reference/Archive/Rejected_Project_Proposals.md) | `09_Archive/09.03_Rejected_Project_Proposals/09.03.00_README.md` |
| Obsolete Project Plans | [`05_Reference/Archive/Obsolete_Project_Plans.md`](05_Reference/Archive/Obsolete_Project_Plans.md) | `09_Archive/09.04_Obsolete_Project_Plans/09.04.00_README.md` |
| Closed Temporary Artifacts | [`05_Reference/Archive/Closed_Temporary_Artifacts.md`](05_Reference/Archive/Closed_Temporary_Artifacts.md) | `09_Archive/09.05_Closed_Temporary_Artifacts/09.05.00_README.md` |
| Archive Register | [`05_Reference/Archive/Archive_Register.md`](05_Reference/Archive/Archive_Register.md) | `09_Archive/09.06_Archive_Register/09.06.00_README.md` |

## Provenance summary

SHA-256 comparison against the declared baseline sources currently yields:

- source-target pairs: **79**;
- byte-identical canonical targets: **49**;
- authored/modified canonical targets: **30**.

Every non-identical target is classified below. A `YES` in the final column means duplicated global normative text was replaced by a link to its canonical owner; it does not indicate loss of unique domain content.

## Authored transformation registry

| Canonical target | Baseline source | Transformation class | Short reason | Unique source content preserved | Global duplicate replaced by canonical link |
|---|---|---|---|---|---|
| `AOS/00_Core/Project_Identity.md` | `AOS/01_Project/01.01_Project_Identity/01.01.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Repeated global safety and Git invariant block replaced by the canonical safety owner; active title normalized. | YES; identity-specific rules retained. | YES — `AOS/00_Core/Minimal_Safety_Floor.md` |
| `AOS/00_Core/Project_Principles.md` | `AOS/01_Project/01.03_Project_Principles/01.03.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Added the canonical Legacy Reference Boundary, removed implied legacy authority, and normalized the active title. | YES; source principles retained and the authority boundary added. | NO — this target is the canonical owner. |
| `AOS/00_Core/Minimal_Safety_Floor.md` | `AOS/02_Scaffolding/02.06_Minimal_Safety_Floor/02.06.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Normalized the complete global invariant set, active title, and next canonical route. | YES; source safety contracts retained and the invariant owner completed. | NO — this target is the canonical owner. |
| `AOS/01_Product/Product_Vision.md` | `AOS/01_Project/01.02_Product_Vision/01.02.00_README.md` | `NAVIGATION_CORRECTION` | Removed the superseded numeric identifier from the active document title. | YES; product vision retained. | NO |
| `AOS/01_Product/Primary_User_Journey.md` | `AOS/03_Product/03.04_Primary_User_Journey/03.04.00_README.md` | `NAVIGATION_CORRECTION` | Replaced stale legacy source-path examples with the canonical target path. | YES; journey contracts and examples retained. | NO |
| `AOS/01_Product/Product_Contracts_and_Observable_Behavior.md` | `AOS/03_Product/03.05_Product_Contracts_and_Observable_Behavior/03.05.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Deduplicated the complete global invariant block and corrected a stale document path. | YES; domain contracts, observable behavior and local boundaries retained. | YES — `AOS/00_Core/Minimal_Safety_Floor.md` |
| `AOS/01_Product/Acceptance_Criteria.md` | `AOS/03_Product/03.06_Acceptance_Criteria/03.06.00_README.md` | `NORMATIVE_DEDUPLICATION` | Replaced repeated global invariants with a domain-specific acceptance statement and canonical link. | YES; acceptance-specific rules retained. | YES — `AOS/00_Core/Minimal_Safety_Floor.md` |
| `AOS/01_Product/Product_Boundaries_and_Success_Metrics.md` | `AOS/03_Product/03.00_README.md` | `SEMANTIC_CONSOLIDATION` | Consolidated the aggregate product-boundary body and linked duplicated global safety material. | YES; all product-specific scope, metrics, anti-metrics, failure signals and formal statements retained. | YES — `AOS/00_Core/Minimal_Safety_Floor.md` |
| `AOS/02_Architecture/Project_Skeleton.md` | `AOS/02_Scaffolding/02.01_Project_Skeleton/02.01.00_README.md` | `TOPOLOGY_CORRECTION` | Replaced the old active tree, stale 02.03/02.04 mappings and legacy navigation with canonical topology and owners. | YES; unique skeleton contracts retained; obsolete topology assertions intentionally replaced. | NO |
| `AOS/02_Architecture/Workspace_Foundation.md` | `AOS/02_Scaffolding/02.02_Workspace_Foundation/02.02.00_README.md` | `TOPOLOGY_CORRECTION` | Replaced the active 02.03 Git mapping with simplified topology and canonical Agent/Git owners. | YES; unique workspace contracts retained; obsolete mapping intentionally replaced. | NO |
| `AOS/02_Architecture/Agent_Contract.md` | `AOS/02_Scaffolding/02.03_Agent_Contract/02.03.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the repeated complete invariant block with a domain-specific canonical link; normalized the active title and next route. | YES; agent-specific authority and behavior rules retained. | YES — `AOS/00_Core/Minimal_Safety_Floor.md` |
| `AOS/02_Architecture/Git_Foundation.md` | `AOS/02_Scaffolding/02.04_Git_Foundation/02.04.00_README.md` | `NAVIGATION_CORRECTION` | Replaced stale legacy paths and numeric navigation with canonical links; normalized the active title and next route. | YES; Git contracts retained. | NO |
| `AOS/03_Development/Task_And_Report_Templates.md` | `AOS/02_Scaffolding/02.05_Task_And_Report_Templates/02.05.00_README.md` | `TOPOLOGY_CORRECTION` | Replaced stale scope/future-tree examples and numeric navigation with canonical topology; normalized the active title and next route. | YES; task and report template contracts retained. | NO |
| `AOS/03_Development/Local_Development_Environment.md` | `AOS/02_Scaffolding/02.07_Local_Development_Environment/02.07.00_README.md` | `NAVIGATION_CORRECTION` | Removed the superseded numeric title and replaced the numeric next route with a canonical link. | YES; local environment contracts retained. | NO |
| `AOS/03_Development/Minimal_Checks_And_CI.md` | `AOS/02_Scaffolding/02.08_Minimal_Checks_And_CI/02.08.00_README.md` | `NAVIGATION_CORRECTION` | Replaced `00_INDEX.md` ownership with MANIFEST checks, normalized the active title, and linked the next canonical route. | YES; check and CI contracts retained. | NO |
| `AOS/03_Development/First_Manual_Workflow.md` | `AOS/02_Scaffolding/02.09_First_Manual_Workflow/02.09.00_README.md` | `TOPOLOGY_CORRECTION` | Replaced active Scaffolding/03_Product readiness and routing with canonical Architecture, Development and Product paths. | YES; workflow requirements, boundaries and completion criteria retained. | NO |
| `AOS/03_Development/Development_Model.md` | `AOS/04_Development/04.01_Development_Model/04.01.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary and old documentation tree with canonical topology while preserving maturity sequencing. | YES; development contracts and product-maturity semantics retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/03_Development/Task_Model.md` | `AOS/04_Development/04.02_Task_Model/04.02.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary with a canonical contextual link and normalized the active title. | YES; task-specific legacy implications retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/03_Development/Execution_Model.md` | `AOS/04_Development/04.03_Execution_Model/04.03.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary with a canonical contextual link and normalized the active title. | YES; execution-specific legacy implications retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/03_Development/Validation_Model.md` | `AOS/04_Development/04.04_Validation_Model/04.04.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary with a canonical contextual link and normalized the active title. | YES; validation-specific legacy implications retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/03_Development/Decision_Model.md` | `AOS/04_Development/04.05_Decision_Model/04.05.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary with a canonical contextual link and normalized the active title. | YES; decision-specific legacy implications retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/03_Development/Project_Memory.md` | `AOS/04_Development/04.06_Project_Memory/04.06.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary with a canonical contextual link and normalized the active title. | YES; memory-specific legacy implications retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/03_Development/Recovery_Model.md` | `AOS/04_Development/04.07_Recovery_Model/04.07.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary with a canonical contextual link and normalized the active title. | YES; recovery-specific legacy implications retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/03_Development/Development_Factory.md` | `AOS/04_Development/04.08_Development_Factory/04.08.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary with a canonical contextual link and normalized the active title. | YES; factory-specific legacy implications retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/03_Development/Agent_Collaboration.md` | `AOS/04_Development/04.09_Agent_Collaboration/04.09.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary with a canonical contextual link and normalized the active title. | YES; collaboration-specific legacy implications retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/03_Development/Process_Evolution.md` | `AOS/04_Development/04.10_Process_Evolution/04.10.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary with a canonical contextual link and normalized the active title. | YES; evolution-specific legacy implications retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/04_Lessons/Anti_Patterns_and_Lessons.md` | `AOS/04_Development/04.11_Anti_Patterns_and_Lessons/04.11.00_README.md` | `MIXED_AUTHORED_CORRECTION` | Replaced the duplicated Legacy Reference Boundary with a canonical contextual link and normalized the active title. | YES; lesson-specific legacy implications retained. | YES — `AOS/00_Core/Project_Principles.md` |
| `AOS/05_Reference/Reconstruction_Roadmap.md` | `AOS/01_Project/01.00_README.md` | `SEMANTIC_CONSOLIDATION` | Consolidated the complete roadmap body and replaced the obsolete active-path claim. | YES; stages 0–14, completion conditions, stop rules and open questions retained. | NO |
| `AOS/05_Reference/References/AgentOS_AOS1.md` | `AOS/08_References/08.04_AgentOS_AOS1/08.04.00_README.md` | `REFERENCE_MODE_NORMALIZATION` | Normalized normative `reference_mode` from `HISTORICAL_REFERENCE` to `READ_ONLY_REFERENCE`. | YES; reference lessons and constraints retained. | NO |
| `AOS/05_Reference/Archive/Archive_Register.md` | `AOS/09_Archive/09.06_Archive_Register/09.06.00_README.md` | `NAVIGATION_CORRECTION` | Replaced old index/reference locations with canonical MANIFEST and `05_Reference` paths. | YES; archive register contracts retained. | NO |

All roadmap open questions remain open. Authored transformations do not import authority from their superseded baseline sources.

## Superseded navigation and metadata

The following retained source classes are explicitly superseded and must not be treated as current canonical locations:

- `00_INDEX.md` — old generated navigation.
- `01_Project/01.00_README.md`, `02_Scaffolding/02.00_README.md`, and `03_Product/03.00_README.md` — aggregate documents that overlap canonical topic files.
- `01_Project/README.md`, `Vision.md`, `Product.md`, `Principles.md`, `Glossary.md`, and `Roadmap.md` — one-line placeholder shortcuts.
- Every `*_META.yml` under the legacy tree — distributed document-location and state metadata.
- Every legacy Markdown source named in the tables above — retained content-preserving migration evidence after its canonical target copy was created.

## Aggregate disposition

- `01_Project/01.00_README.md` — unique roadmap content consolidated into `05_Reference/Reconstruction_Roadmap.md`; retained as superseded evidence.
- `02_Scaffolding/02.00_README.md` — legacy navigation fully covered by the canonical section README files; retained as superseded evidence.
- `03_Product/03.00_README.md` — unique product-boundary and success-metric content consolidated into `01_Product/Product_Boundaries_and_Success_Metrics.md`; retained as superseded evidence.

No aggregate was deleted or moved.
