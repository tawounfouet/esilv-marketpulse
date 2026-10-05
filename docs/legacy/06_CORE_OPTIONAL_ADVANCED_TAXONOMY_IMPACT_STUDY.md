# CORE / OPTIONAL / ADVANCED / INSTRUCTOR Taxonomy Impact Study

## 1. Purpose

This document maps the repository-wide impact of introducing an explicit:

```text
CORE
OPTIONAL
ADVANCED
INSTRUCTOR
```

teaching taxonomy into MarketPulse.

The purpose is to prevent R7.4 from becoming an uncontrolled rewrite of the 12 student labs.

No lab change should be implemented before this impact map is understood.

This document is governed by:

```text
docs/legacy/04_LEGACY_CONTENT_OPERATIONALIZATION_ROADMAP.md
docs/legacy/05_LEGACY_FINAL_MIGRATION_REGISTRY.md
```

Frozen CORE boundary:

```text
docs/16_TEACHING_BASELINE_RELEASE.md
```

## 2. Executive decision

Adopt four distinct teaching layers.

### CORE

```text
mandatory
timeboxed
common to all students
checkpoint-aligned
part of the frozen 18-hour path
```

### OPTIONAL

```text
lightweight extension
normally 5 to 20 minutes
no major new technology
no major new architecture
no checkpoint requirement
kept inside the TD file
```

### ADVANCED

```text
materially deeper practice
new technical capability or deeper engineering concept
typically 20 to 90 minutes
not checkpoint-required
implemented as a dedicated support under docs/advanced/
linked from the relevant TD
```

### INSTRUCTOR

```text
teacher-facing depth
not a student deliverable
not evidence
not graded
stored under docs/instructor/
may later feed short R7.5 enrichment capsules
```

The relationship is:

```text
student path

CORE
 |
 v
OPTIONAL
 |
 v
ADVANCED


teacher path

INSTRUCTOR
 |
 v
better explanations
 |
 v
CORE remains unchanged
```

## 3. Non-negotiable rules

The taxonomy must preserve these invariants:

```text
CORE
=
required

OPTIONAL
=
never required

ADVANCED
=
never required

INSTRUCTOR
=
never student evidence
```

Also:

```text
no ADVANCED activity may be required for a checkpoint

no ADVANCED activity may change the grade ceiling for students who complete only CORE

no ADVANCED activity may silently change the canonical runtime

no ADVANCED activity may silently add a root dependency

no ADVANCED link may appear as READY_TO_TEACH before its support is qualified

no INSTRUCTOR note may become a hidden prerequisite
```

## 4. Current-state inventory

The 12 current student labs contain:

```text
12 CORE sections
12 OPTIONAL sections
56 Optional activities
0 explicit ADVANCED sections
```

Current Optional activity count:

| TD | Current Optional activities |
|---|---:|
| TD01 | 4 |
| TD02 | 5 |
| TD03 | 6 |
| TD04 | 4 |
| TD05 | 5 |
| TD06 | 5 |
| TD07 | 4 |
| TD08 | 5 |
| TD09 | 4 |
| TD10 | 5 |
| TD11 | 6 |
| TD12 | 3 |
| Total | 56 |

R7.3 has already created:

```text
10 INSTRUCTOR_READY deep dives
```

R7.4 currently has:

```text
12 P1 ADVANCED_READY targets
```

which are still awaiting READY_TO_TEACH qualification.

## 5. Reclassification result

Only three existing Optional activities should be reclassified as ADVANCED during the P1 rollout.

### TD04

Current:

```text
Optional 1 - Execute a controlled conflict
```

Target:

```text
ADV-GIT-01 - Conflict resolution
```

Reason:

```text
new operational Git skill
30-45 minute mini-lab
controlled merge-conflict lifecycle
explicit P1 advanced backlog item
```

### TD11

Current:

```text
Optional 3 - Simple selector
```

Target:

```text
ADV-DASH-02 - Instrument selector
```

Reason:

```text
new interaction capability
requires parameterized application boundary
depends on ADV-DASH-01
```

Current:

```text
Optional 4 - Callback
```

Target:

```text
ADV-DASH-01 - Callback
```

Reason:

```text
new Dash interaction model
30-45 minute mini-lab
introduces callback architecture
explicit P1 advanced backlog item
```

Therefore:

```text
56 current Optional activities
-
3 reclassified to ADVANCED
=
53 retained Optional activities
```

## 6. New ADVANCED entry points

The 12 P1 supports must all have a student-facing entry point after their prerequisites are satisfied.

Three replace current Optional items.

Nine are net-new links.

Final P1 placement:

| TD | ADVANCED ID | Topic | Placement reason |
|---|---|---|---|
| TD01 | ADV-LNX-01 | File operations | TD01 complete is prerequisite |
| TD01 | ADV-LNX-02 | Permissions and chmod | basic Linux + file context |
| TD01 | ADV-LNX-03 | Pipes and text processing | TD01 local files available |
| TD02 | ADV-LNX-04 | Environment variables | TD02 complete + Python imports |
| TD03 | ADV-GIT-02 | Restore, revert and reset | meaningful local history exists |
| TD04 | ADV-GIT-01 | Conflict resolution | branch + merge understood |
| TD10 | ADV-BBG-01 | Bloomberg reference data | TD09-TD10 complete + LIVE required |
| TD11 | ADV-DASH-01 | Callback | static dashboard works |
| TD11 | ADV-DASH-02 | Instrument selector | depends on ADV-DASH-01 |
| TD12 | ADV-GIT-04 | Tags and releases | explicitly designed for after TD12 |
| TD12 | ADV-RMT-01 | SSH fundamentals | deployment-oriented advanced path |
| TD12 | ADV-RMT-03 | systemd service | requires TD11 + remote Linux |

Total:

```text
12 P1 ADVANCED entry points
```

## 7. Lab-by-lab impact map

### TD01 - Bootstrap + Linux

Current Optional:

```text
4
```

Keep all four as OPTIONAL.

Add ADVANCED links:

```text
ADV-LNX-01 File operations
ADV-LNX-02 Permissions and chmod
ADV-LNX-03 Pipes and text processing
```

Instructor relation:

```text
INS-LNX-01 Unix philosophy
INS-LNX-02 Permissions troubleshooting
```

CORE impact:

```text
NONE
```

### TD02 - Python + CSV / JSON

Current Optional:

```text
5
```

Keep all five as OPTIONAL.

Add ADVANCED link:

```text
ADV-LNX-04 Environment variables
```

Reason:

```text
its prerequisite explicitly includes TD02 completion
```

CORE impact:

```text
NONE
```

### TD03 - Git Local Workflow

Current Optional:

```text
6
```

Keep all six as OPTIONAL.

Add ADVANCED link:

```text
ADV-GIT-02 Restore, revert and reset
```

Instructor relation:

```text
INS-GIT-01 Staging mental model
INS-GIT-02 HEAD / refs
INS-GIT-03 Git object model
```

CORE impact:

```text
NONE
```

### TD04 - Branches + Merge

Current Optional:

```text
4
```

Reclassify:

```text
Optional 1 controlled conflict
->
ADV-GIT-01 Conflict resolution
```

Keep as OPTIONAL:

```text
Compare another branch
Inspect graph decorations
File history
```

Instructor relation:

```text
INS-GIT-02 HEAD / refs
INS-GIT-04 Merge vs rebase
```

CORE impact:

```text
NONE
```

Checkpoint A impact:

```text
NONE
```

Conflict execution remains unnecessary for Checkpoint A.

### TD05 - Remote Branch + Pull Request

Current Optional:

```text
5
```

Keep all five as OPTIONAL.

No P1 ADVANCED student support is attached directly to TD05.

Instructor relation:

```text
INS-GIT-02 HEAD / refs / remote-tracking refs
INS-GIT-04 Merge vs rebase
```

CORE impact:

```text
NONE
```

### TD06 - Code Review

Current Optional:

```text
5
```

Keep all five as OPTIONAL.

No P1 ADVANCED student support is attached directly to TD06.

Instructor relation:

```text
INS-GIT-04 Merge vs rebase
```

CORE impact:

```text
NONE
```

### TD07 - Data Normalization + Comparison

Current Optional:

```text
4
```

Keep all four as OPTIONAL.

Daily returns remain OPTIONAL rather than ADVANCED because:

```text
they are a small local extension
no new dependency
no new application layer
no P1 advanced target
```

No P1 ADVANCED support is attached directly to TD07.

CORE impact:

```text
NONE
```

### TD08 - Yahoo Finance

Current Optional:

```text
5
```

Keep all five as OPTIONAL.

The current provider selector and additional error handling remain small experiments with explicit scope limits.

Do not turn them into a generic provider-framework advanced lab during R7.4.

No P1 ADVANCED support is attached directly to TD08.

Checkpoint B impact:

```text
NONE
```

### TD09 - Bloomberg Introduction

Current Optional:

```text
4
```

Keep all four as OPTIONAL for R7.4.

Do not link ADV-BBG-01 yet because its prerequisite is:

```text
TD09-TD10 complete
+
LIVE Bloomberg environment validated
```

Instructor relation:

```text
INS-BBG-01 Terminal + identifiers
INS-BBG-02 BDP / BDS / BDH
INS-BBG-03 Request/Response vs Subscription
```

CORE impact:

```text
NONE
```

### TD10 - Bloomberg Provider

Current Optional:

```text
5
```

Keep all five as OPTIONAL.

Add ADVANCED link:

```text
ADV-BBG-01 Bloomberg reference data
```

The advanced support must clearly state:

```text
LIVE required
may be skipped if LIVE unavailable
no fabricated evidence
```

Instructor relation:

```text
INS-BBG-03 Request/Response vs Subscription
INS-BBG-04 xbbg vs blpapi
```

CORE impact:

```text
NONE
```

### TD11 - Dash Dashboard

Current Optional:

```text
6
```

Keep as OPTIONAL:

```text
Daily-return chart
Instrument volume chart
Styling polish
Layout helper
```

Reclassify:

```text
Simple selector
->
ADV-DASH-02

Callback
->
ADV-DASH-01
```

ADVANCED order:

```text
ADV-DASH-01
then
ADV-DASH-02
```

CORE impact:

```text
NONE
```

### TD12 - Integration + Release

Current section:

```text
OPTIONAL / REFERENCE
```

Current items:

```text
Advanced deployment
Docker
GitHub Actions
```

These are semantically advanced but they are not part of the R7.4 P1 production commitment.

For R7.4:

```text
keep current items as OPTIONAL / REFERENCE
```

Add P1 ADVANCED links:

```text
ADV-GIT-04 Tags and releases
ADV-RMT-01 SSH fundamentals
ADV-RMT-03 systemd service
```

R7.6 must revisit:

```text
Docker
GitHub Actions
generic advanced deployment
```

when P2 advanced packaging is considered.

Checkpoint C impact:

```text
NONE
```

## 8. Standard lab structure after integration

Every student lab should use the same top-level vocabulary:

```text
# CORE

# OPTIONAL

# ADVANCED
```

For structural consistency, all 12 TD files should contain an ADVANCED section.

If no READY_TO_TEACH advanced support is attached to a TD:

```text
# ADVANCED

No READY_TO_TEACH advanced activity is attached to this TD.
Complete the CORE and OPTIONAL work only.
```

This applies initially to:

```text
TD05
TD06
TD07
TD08
TD09
```

This avoids ambiguity about whether an ADVANCED section was forgotten.

## 9. ADVANCED section contract

An ADVANCED section inside a TD must remain short.

It should contain:

```text
advanced ID
title
prerequisites
estimated duration
READY_TO_TEACH status
direct link to docs/advanced/<support>.md
explicit non-checkpoint statement
```

It must not duplicate the full advanced exercise.

Example:

```text
# ADVANCED

## ADV-GIT-01 - Conflict Resolution

Status:
READY_TO_TEACH

Prerequisite:
TD04 CORE complete

Duration:
30-45 minutes

Support:
docs/advanced/ADV_GIT_01_CONFLICT_RESOLUTION.md

This activity is not required for Checkpoint A.
```

## 10. New files to add in R7.4

The 12 P1 supports:

```text
docs/advanced/ADV_LNX_01_FILE_OPERATIONS.md
docs/advanced/ADV_LNX_02_PERMISSIONS_CHMOD.md
docs/advanced/ADV_LNX_03_PIPES_TEXT_PROCESSING.md
docs/advanced/ADV_LNX_04_ENVIRONMENT_VARIABLES.md

docs/advanced/ADV_GIT_01_CONFLICT_RESOLUTION.md
docs/advanced/ADV_GIT_02_RESTORE_REVERT_RESET.md
docs/advanced/ADV_GIT_04_TAGS_RELEASES.md

docs/advanced/ADV_RMT_01_SSH_FUNDAMENTALS.md
docs/advanced/ADV_RMT_03_SYSTEMD_SERVICE.md

docs/advanced/ADV_BBG_01_REFERENCE_DATA.md

docs/advanced/ADV_DASH_01_CALLBACK.md
docs/advanced/ADV_DASH_02_INSTRUMENT_SELECTOR.md
```

No additional P1 support should be invented during R7.4 without first updating:

```text
03 backlog
04 roadmap
05 migration registry
this impact study
```

## 11. Files to update during R7.4

### All 12 student labs

Update:

```text
docs/labs/TD01_BOOTSTRAP_LINUX.md
docs/labs/TD02_PYTHON_CSV_JSON.md
docs/labs/TD03_GIT_LOCAL_WORKFLOW.md
docs/labs/TD04_BRANCHES_AND_MERGE.md
docs/labs/TD05_FORK_AND_PULL_REQUEST.md
docs/labs/TD06_CODE_REVIEW.md
docs/labs/TD07_DATA_NORMALIZATION_AND_COMPARISON.md
docs/labs/TD08_YAHOO_FINANCE.md
docs/labs/TD09_BLOOMBERG_INTRODUCTION.md
docs/labs/TD10_BLOOMBERG_PROVIDER.md
docs/labs/TD11_DASH_DASHBOARD.md
docs/labs/TD12_INTEGRATION_AND_RELEASE.md
```

Purpose:

```text
standardize ADVANCED presence
move 3 deep Optional activities to ADVANCED
add 9 new P1 entry points
preserve CORE
preserve lightweight Optional work
```

### Lab index

Update:

```text
docs/labs/README.md
```

Add:

```text
taxonomy definition
ADVANCED availability by TD
links to READY_TO_TEACH supports
explicit checkpoint rule
```

### Advanced backlog

Update:

```text
docs/legacy/03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
```

As supports qualify:

```text
READY_TO_DESIGN
->
READY_TO_TEACH
```

### R7 roadmap

Update:

```text
docs/legacy/04_LEGACY_CONTENT_OPERATIONALIZATION_ROADMAP.md
```

Track R7.4 sub-phases and closure.

### Final migration registry

Update:

```text
docs/legacy/05_LEGACY_FINAL_MIGRATION_REGISTRY.md
```

For each P1 item:

```text
READY_TO_DESIGN_R7.4
->
DONE

TO_VALIDATE
->
REFERENCE_VALIDATED or EXECUTED
```

and record the TD entry point.

## 12. Transverse documentation impact

### Root README

File:

```text
README.md
```

Update section:

```text
CORE vs optional extensions
```

Target vocabulary:

```text
CORE
OPTIONAL
ADVANCED
INSTRUCTOR
```

Add links to:

```text
docs/advanced/
docs/instructor/deep-dives/
```

No runtime or dependency contract changes.

### TD sequence

File:

```text
docs/06_TD_SEQUENCE_AND_LEARNING_PATH.md
```

Update:

```text
Common path vs advanced path
```

Clarify:

```text
OPTIONAL
=
lightweight in-TD extension

ADVANCED
=
separate READY_TO_TEACH activity
```

The 12-TD sequence remains unchanged.

### Transverse review

File:

```text
docs/07_TD_TRANSVERSE_REVIEW_AND_REBALANCING.md
```

Do not rewrite the historical review.

Append a post-freeze taxonomy addendum explaining that the former:

```text
CORE / OPTIONAL / INSTRUCTOR DEMO
```

model has been refined to:

```text
CORE / OPTIONAL / ADVANCED / INSTRUCTOR
```

The old review remains valid as historical decision evidence.

### Checkpoint contract

File:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

No filename or required evidence changes.

Add one explicit taxonomy rule:

```text
ADVANCED work is never required for Checkpoint A, B or C.
```

Keep:

```text
05_advanced_deployment.png
=
optional
```

A student who completes only CORE must not be penalized.

### Dependencies document

File:

```text
docs/13_MARKETPULSE_LIBRARIES_AND_DEPENDENCIES.md
```

No CORE dependency change is expected from the 12 P1 supports.

Rules:

```text
advanced-only dependency
must be documented in its advanced support

advanced-only dependency
must not be added to root requirements.txt
unless CORE itself uses it
```

For current P1:

```text
Dash / Plotly
already CORE dependencies by TD11

SSH / systemd
system/environment capabilities, not root Python dependencies

Bloomberg reference data
environment-dependent, no generic root dependency added

Linux / Git advanced labs
no new Python dependency
```

### Teaching baseline release

File:

```text
docs/16_TEACHING_BASELINE_RELEASE.md
```

No CORE release decision change is required.

Reason:

```text
R7.4 changes only non-mandatory teaching layers
```

A targeted post-change consistency check is sufficient if:

```text
CORE sections remain byte-for-byte or semantically unchanged
checkpoint contract remains unchanged
runtime remains unchanged
```

## 13. R7.5 impact

R7.5 introduces:

```text
docs/instructor/02_TD_ENRICHMENT_CAPSULES.md
```

Recommended design:

```text
central instructor map
rather than copying instructor notes into student labs
```

The capsule file will map:

```text
TD
->
instructor deep dive
->
5 to 10 minute explanation
->
stop point
```

Student labs should not contain the full instructor material.

This avoids student-facing clutter and hidden expectations.

## 14. R7.6 impact

R7.6 introduces advanced-track packaging.

Planned addition:

```text
docs/advanced/README.md
```

It will index READY_TO_TEACH material by:

```text
domain
prerequisites
duration
external environment needs
diagnostic relevance
delivery mode
```

R7.6 must also revisit P2/P3 advanced candidates such as:

```text
Docker
GitHub Actions
VPS deployment
xbbg exploration
blpapi low-level request
intraday bars
interactive rebase
Bash scripting
cron
```

These must not be advertised as READY_TO_TEACH until separately qualified.

## 15. Diagnostic impact

No diagnostic-question rewrite is required for R7.4.

Existing ceiling questions already cover areas such as:

```text
permissions
pipes
environment variables
merge conflicts
provider architecture
Dash callbacks
```

Use diagnostic results only to decide:

```text
which ADVANCED supports are realistic for a cohort
```

Never use strong diagnostic results to increase mandatory CORE workload.

## 16. Assessment impact

Required checkpoint evidence:

```text
UNCHANGED
```

Weights:

```text
UNCHANGED
```

CORE completion expectation:

```text
UNCHANGED
```

Advanced work may demonstrate initiative.

It must not become necessary to receive full credit for the common checkpoint contract.

Assessment invariant:

```text
student A
CORE complete
ADVANCED none

student B
CORE complete
ADVANCED several

both
must remain eligible for full common CORE assessment
```

Advanced work may only be recognized under a separately defined bonus or enrichment policy if the teaching team explicitly introduces one later.

No such bonus policy is created by R7.4.

## 17. Runtime and architecture impact

Canonical commands remain:

```bash
python src/main.py
python src/dashboard.py
```

No change to:

```text
canonical rows
analytics formulas
provider boundary
snapshot keys
checkpoint filenames
12 TD sequence
18-hour CORE
```

Advanced exercises may use disposable files or disposable repositories.

They must not leave the shared CORE repository in an unreproducible state.

## 18. Security impact

Advanced work has higher operational risk than lightweight Optional work.

Mandatory safeguards:

```text
ADV-GIT-02
use disposable Git repository for destructive concepts

ADV-RMT-01
no personal billing
no shared private key
no committed key

ADV-RMT-03
no secret embedded in service file

ADV-BBG-01
LIVE only when approved
no invented field
no fabricated evidence

ADV-DASH-01/02
no direct provider calls from callbacks
no duplicated analytics

ADV-LNX-02
no chmod 777 generic fix

ADV-LNX-03
project-controlled files
no arbitrary web scraping
```

## 19. Documentation impact matrix

| Artifact | Action | Impact level | CORE revalidation? |
|---|---|---|---|
| 12 TD files | Add standardized ADVANCED section | Medium | No, if CORE unchanged |
| 3 current Optional items | Reclassify to ADVANCED | Medium | No |
| 12 P1 advanced supports | Add under docs/advanced | High content volume | No CORE revalidation |
| docs/labs/README.md | Add taxonomy + advanced map | Medium | No |
| docs/legacy/03 backlog | Promote statuses progressively | Low | No |
| docs/legacy/04 roadmap | Add R7.4 sub-phases | Low | No |
| docs/legacy/05 registry | Record READY_TO_TEACH + TD links | Low | No |
| README.md | Expose 4-layer taxonomy | Low | No |
| docs/04 checkpoints | Clarify ADVANCED is never required | Low | No |
| docs/06 sequence | Refine optional vs advanced path | Low | No |
| docs/07 transverse review | Append taxonomy addendum | Low | No |
| docs/13 dependencies | Clarify advanced dependency isolation | Low | No |
| docs/instructor/02_TD_ENRICHMENT_CAPSULES.md | Add in R7.5 | Medium | No |
| docs/advanced/README.md | Add in R7.6 | Medium | No |
| docs/16 release | No content change planned | None | No |

## 20. Change-volume estimate

Planned additions:

```text
1 impact-study document
12 P1 advanced support documents
1 instructor capsule document
1 advanced-track README
```

Planned direct lab modifications:

```text
12 / 12 labs
```

Planned current Optional reclassifications:

```text
3
```

Planned Optional activities retained:

```text
53
```

Planned P1 ADVANCED entry points:

```text
12
```

Net-new ADVANCED student choices:

```text
9
```

because three already exist today as Optional activities.

## 21. Risk analysis

### Risk 1 - ADVANCED becomes hidden CORE

Severity:

```text
HIGH
```

Control:

```text
explicit non-checkpoint statement in every advanced link
```

### Risk 2 - Duplicate exercises

Severity:

```text
MEDIUM
```

Example:

```text
TD04 controlled conflict
+
ADV-GIT-01 controlled conflict
```

Control:

```text
remove the detailed Optional exercise
replace with the ADVANCED link
```

### Risk 3 - Timebox creep

Severity:

```text
HIGH
```

Control:

```text
CORE stop point remains before ADVANCED
advanced work starts only after CORE
```

### Risk 4 - Link to unqualified support

Severity:

```text
HIGH
```

Control:

```text
TD link added only after READY_TO_TEACH gate passes
```

### Risk 5 - Dependency contamination

Severity:

```text
MEDIUM
```

Control:

```text
advanced-only dependencies stay local to advanced support
```

### Risk 6 - Evidence bias

Severity:

```text
HIGH
```

Control:

```text
checkpoints remain CORE-only
optional advanced evidence stays non-required
```

### Risk 7 - Proprietary environment blockage

Severity:

```text
HIGH for ADV-BBG-01
```

Control:

```text
LIVE prerequisite
skip when unavailable
no fallback masquerading as reference-data LIVE
```

### Risk 8 - Student-facing clutter

Severity:

```text
MEDIUM
```

Control:

```text
TD ADVANCED section contains links and metadata only
full exercise lives in docs/advanced
```

## 22. Recommended R7.4 decomposition

R7.4 should be split into four controlled sub-phases.

### R7.4.1 - Taxonomy and impact baseline

Deliverables:

```text
this impact study
taxonomy contract
lab placement map
change inventory
```

Status after this document:

```text
DONE
```

### R7.4.2 - P1 advanced support production

Create and qualify the 12 supports.

A support must satisfy:

```text
objective precise
prerequisites explicit
duration explicit
commands tested
cleanup defined
security reviewed
no personal payment
observable result
MarketPulse relation explicit
CORE unaffected
```

### R7.4.3 - Lab taxonomy integration

Only after the corresponding support becomes READY_TO_TEACH:

```text
add / update # ADVANCED section
remove duplicate Optional implementation if reclassified
add direct support link
preserve CORE
```

### R7.4.4 - Qualification and registry closure

Verify:

```text
12 TDs contain explicit ADVANCED sections
53 Optional activities remain
3 former Optional activities are reclassified
12 P1 ADVANCED links exist
12 support paths resolve
no checkpoint requirement changed
no CORE command changed
no root dependency contamination
```

Then update:

```text
03 backlog
04 roadmap
05 registry
labs index
root README
transverse documentation
```

## 23. Implementation order

Recommended order:

```text
1. freeze taxonomy contract
2. create advanced support file
3. test support independently
4. mark READY_TO_TEACH
5. add TD ADVANCED link
6. update registry status
7. continue with next P1 item
8. after all 12, run global taxonomy audit
```

Do not:

```text
edit all 12 labs first
then hope advanced supports catch up later
```

That would create broken links and a false READY_TO_TEACH surface.

## 24. Files intentionally not changed by this study

This impact study itself does not modify:

```text
TD01-TD12 student labs
checkpoint evidence
requirements.txt
src/
config/
data/
analytics
providers
runtime commands
assessment weights
```

Those changes, where planned, begin only under R7.4.2 and R7.4.3.

## 25. Impact-study acceptance criteria

```text
[x] all 12 labs inventoried
[x] all 56 current Optional activities accounted for
[x] reclassification candidates identified
[x] all 12 P1 advanced items assigned to a TD
[x] all new P1 support files identified
[x] all transverse documents impacted are mapped
[x] checkpoint impact explicitly assessed
[x] dependency impact explicitly assessed
[x] runtime impact explicitly assessed
[x] security impact explicitly assessed
[x] R7.4 implementation sequence defined
[x] frozen CORE remains protected
```

Conclusion:

```text
IMPACT MAPPED

R7.4 MAY PROCEED
WITHOUT REOPENING THE CORE
```
