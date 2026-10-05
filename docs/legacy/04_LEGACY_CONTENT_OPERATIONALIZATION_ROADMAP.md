# Legacy Content Operationalization Roadmap

## 1. Purpose

This document is the single execution roadmap for the remaining Legacy-to-MarketPulse work.

It exists to prevent divergence after the CORE teaching baseline freeze.

The Legacy stream is no longer allowed to evolve through ad hoc additions.

Every new Legacy migration, instructor note, advanced lab or final decision must map to a lot defined here.

The objective is:

```text
historical material
        |
        v
inventory
        |
        v
decision
        |
        v
operational destination
        |
        v
verified closure
```

The final goal is not to preserve everything.

The final goal is:

```text
preserve useful depth
+
protect the 18-hour CORE
+
make advanced material usable
+
make instructor depth accessible
+
explicitly close dropped content
```

## 2. Canonical status

This document is the source of truth for Legacy operationalization.

It complements:

```text
docs/legacy/01_PREVIOUS_COURSE_REPOSITORY_ANALYSIS.md
docs/legacy/02_LEGACY_TO_MARKETPULSE_CONTENT_MAPPING.md
docs/legacy/03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
docs/instructor/01_LEGACY_DEEP_DIVE_REFERENCE.md
```

Those documents answer:

```text
01
What existed?

02
What should happen to it?

03
What optional content could become advanced teaching material?

Instructor deep dive
What conceptual depth should the teacher retain?
```

This roadmap answers:

```text
What do we execute next?
In what order?
When is a Legacy item considered truly operationalized?
```

## 3. Relationship with the frozen CORE

The MarketPulse CORE is already frozen through R6.

Therefore:

```text
R7
must not redesign R1-R6
```

R7 may:

```text
document
formalize
extract
rewrite
test
package
classify
close
```

R7 must not silently:

```text
add a 13th mandatory TD
change checkpoint requirements
change canonical runtime commands
change provider contracts
change analytics formulas
change the frozen 18-hour workload
```

Any proposed CORE change requires a separate explicit change request and targeted revalidation.

## 4. Anti-divergence rules

From this point onward:

```text
Rule 1
No new Legacy document without a roadmap lot.

Rule 2
No new advanced lab without an ID from the existing backlog or an explicit roadmap amendment.

Rule 3
No instructor deep-dive expansion without mapping it to a priority topic.

Rule 4
No OPTIONAL item may become mandatory by accident.

Rule 5
No DROP item may re-enter the common path without a documented decision reversal.

Rule 6
No historical asset may be copied into the public repository without a reuse-rights check.

Rule 7
No LIVE Bloomberg claim without LIVE evidence.

Rule 8
No personal billing or mandatory personal cloud account may be reintroduced.

Rule 9
Every implemented Legacy item must have one final destination.

Rule 10
Roadmap status must be updated in the same change that closes a lot.
```

## 5. Final destination model

Every significant Legacy item must end in exactly one of these destinations:

```text
CORE_MIGRATED
=
already absorbed into TD01-TD12

INSTRUCTOR_READY
=
teacher-facing note is operational and usable

ADVANCED_READY
=
optional advanced support is READY_TO_TEACH

REFERENCE_ONLY
=
kept for conceptual or historical reference

DROP_CLOSED
=
explicitly excluded from the current curriculum
```

No important Legacy item should remain in an ambiguous state such as:

```text
maybe later
interesting
to review
possibly useful
```

without an explicit backlog status.

## 6. R7 roadmap

```text
R7.1  Legacy freeze reconciliation
R7.2  Final migration registry
R7.3  Instructor deep-dive operationalization
R7.4  Advanced P1 content operationalization
R7.5  TD enrichment capsules
R7.6  Advanced-track packaging
R7.7  Legacy closure audit
```

## 7. R7.1 - Legacy freeze reconciliation

### Goal

Reconcile Legacy documentation with the frozen R6 teaching baseline.

### Scope

Update stale status or phase references in:

```text
docs/legacy/README.md
docs/legacy/01_PREVIOUS_COURSE_REPOSITORY_ANALYSIS.md
docs/legacy/02_LEGACY_TO_MARKETPULSE_CONTENT_MAPPING.md
docs/legacy/03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
docs/instructor/01_LEGACY_DEEP_DIVE_REFERENCE.md
```

Only stale lifecycle references should change.

Historical analysis content should not be rewritten merely because R6 is closed.

### Acceptance criteria

```text
[x] legacy README points to this roadmap
[x] stale R5/R6 "next phase" wording is removed
[x] R6 frozen CORE status is acknowledged
[x] R7 scope is explicit
[x] legacy analysis remains historically intact
[x] no CORE contract is changed
```

### Exit result

```text
LEGACY DOCUMENTATION
ALIGNED WITH FROZEN CORE
```

### Execution result

R7.1 reconciled the Legacy documentation with the frozen R6 baseline without rewriting the historical analysis.

Updated:

```text
docs/legacy/README.md
docs/legacy/01_PREVIOUS_COURSE_REPOSITORY_ANALYSIS.md
docs/legacy/02_LEGACY_TO_MARKETPULSE_CONTENT_MAPPING.md
docs/legacy/03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
docs/instructor/01_LEGACY_DEEP_DIVE_REFERENCE.md
```

The reconciliation establishes:

```text
analysis
=
historical source

mapping
=
classification source

advanced backlog
=
optional design source

instructor deep dive
=
consolidated teacher reference

R7 roadmap
=
execution source

R6 release
=
frozen CORE boundary
```

No TD, checkpoint, runtime, provider or analytics contract was changed.

### R7.1 acceptance result

```text
[x] legacy README points to this roadmap
[x] stale R5/R6 next-phase wording is removed
[x] R6 frozen CORE status is acknowledged
[x] R7 scope is explicit
[x] legacy analysis remains historically intact
[x] no CORE contract is changed
```

R7.1 conclusion:

```text
PASS

LEGACY DOCUMENTATION
ALIGNED WITH FROZEN CORE
```

## 8. R7.2 - Final migration registry

### Goal

Create one authoritative registry showing the final destination of each significant Legacy topic.

### Planned artifact

```text
docs/legacy/05_LEGACY_FINAL_MIGRATION_REGISTRY.md
```

### Required dimensions

At minimum:

```text
legacy source
legacy topic
current decision
current destination
target document
target TD or advanced ID
operational status
validation status
notes
```

### Example

```text
CM2
working tree / index / commit
CORE_MIGRATED
TD03
DONE

CM3
interactive rebase
ADVANCED_READY candidate
ADV-GIT-03
NOT YET READY_TO_TEACH

CM4
BDP / BDS / BDH
INSTRUCTOR_READY target
Instructor deep dive
TO FORMALIZE

Project
Sharpe ratio
DROP_CLOSED
No current target
CLOSED
```

### Acceptance criteria

```text
[x] every high-priority Legacy topic has a row
[x] every P1 optional backlog item has a row
[x] every instructor-priority deep dive has a row
[x] every DROP cluster has a documented closure
[x] no important Legacy concept has an undefined destination
```

### Execution result

Created:

```text
docs/legacy/05_LEGACY_FINAL_MIGRATION_REGISTRY.md
```

The registry contains:

```text
25 CORE_MIGRATED rows
10 INSTRUCTOR_READY targets
12 P1 ADVANCED_READY targets
12 other optional rows
13 REFERENCE_ONLY rows
26 DROP_CLOSED rows

98 registered rows total
```

High-priority coverage:

```text
10 / 10 explicit destinations
```

R7.2 conclusion:

```text
PASS

LEGACY FINAL MIGRATION REGISTRY
ESTABLISHED
```

## 9. R7.3 - Instructor deep-dive operationalization

### Goal

Transform the existing large instructor reference into smaller usable teaching notes.

The current reference already contains the knowledge.

R7.3 turns that knowledge into operational material.

### Priority topics

```text
INS-GIT-01  Staging mental model
INS-GIT-02  HEAD / refs / remote-tracking refs
INS-GIT-03  Git object model
INS-GIT-04  Merge vs rebase
INS-LNX-01  Unix philosophy
INS-LNX-02  Permissions troubleshooting
INS-BBG-01  Bloomberg Terminal + identifiers
INS-BBG-02  BDP / BDS / BDH
INS-BBG-03  Request/Response vs Subscription
INS-BBG-04  xbbg vs blpapi
```

### Recommended target directory

```text
docs/instructor/deep-dives/
```

### Each note must contain

```text
purpose
student CORE boundary
instructor mental model
best teaching moment
short explanation
worked example
common misconception
stop point
source discipline
optional extension
```

### Acceptance criteria per note

```text
[x] useful in a real TD
[x] can be read quickly before or during class
[x] does not create a new mandatory student deliverable
[x] aligns with one or more current TDs
[x] avoids stale historical claims
[x] marks environment-specific claims clearly
```

### R7.3 closure

R7.3 is complete only when all 10 priority notes are:

```text
INSTRUCTOR_READY
```

### Execution result

Created index:

```text
docs/instructor/deep-dives/README.md
```

Created 10 operational notes:

```text
INS_GIT_01_STAGING_MENTAL_MODEL.md
INS_GIT_02_HEAD_REFS_REMOTE_TRACKING.md
INS_GIT_03_OBJECT_MODEL.md
INS_GIT_04_MERGE_VS_REBASE.md

INS_LNX_01_UNIX_PHILOSOPHY.md
INS_LNX_02_PERMISSIONS_TROUBLESHOOTING.md

INS_BBG_01_TERMINAL_IDENTIFIERS.md
INS_BBG_02_BDP_BDS_BDH.md
INS_BBG_03_REQUEST_RESPONSE_SUBSCRIPTION.md
INS_BBG_04_XBBG_VS_BLPAPI.md
```

Structural validation:

```text
notes present              = 10 / 10
INSTRUCTOR_READY status    = 10 / 10
required sections present  = 10 / 10
CORE boundary present      = 10 / 10
stop point present         = 10 / 10
```

No TD, checkpoint, runtime, analytics or provider contract was changed.

Bloomberg notes explicitly preserve the rule:

```text
current operational fact
=
verify in approved environment
```

R7.3 conclusion:

```text
PASS

10 / 10 PRIORITY DEEP DIVES
INSTRUCTOR_READY
```

## 10. R7.4 - Advanced P1 content operationalization

### Goal

Convert the highest-value optional backlog items from:

```text
READY_TO_DESIGN
```

to:

```text
READY_TO_TEACH
```

### P1 candidates

```text
ADV-LNX-01  File operations
ADV-LNX-02  Permissions and chmod
ADV-LNX-03  Pipes and text processing
ADV-LNX-04  Environment variables

ADV-GIT-01  Conflict resolution
ADV-GIT-02  Restore, revert and reset
ADV-GIT-04  Tags and releases

ADV-RMT-01  SSH fundamentals
ADV-RMT-03  systemd service

ADV-BBG-01  Bloomberg reference data

ADV-DASH-01 Callback
ADV-DASH-02 Instrument selector
```

### Important sequencing rule

Do not attempt all 12 at once.

Recommended implementation order:

```text
1. ADV-GIT-01
2. ADV-LNX-03
3. ADV-LNX-04
4. ADV-GIT-04
5. ADV-DASH-01
6. ADV-LNX-01
7. ADV-LNX-02
8. ADV-GIT-02
9. ADV-RMT-01
10. ADV-BBG-01
11. ADV-DASH-02
12. ADV-RMT-03
```

### Promotion gate

An advanced item becomes READY_TO_TEACH only when:

```text
[ ] objective is precise
[ ] prerequisites are explicit
[ ] duration is defined
[ ] commands were tested
[ ] cleanup procedure exists
[ ] security risks were reviewed
[ ] no personal payment is required
[ ] expected result is observable
[ ] MarketPulse relationship is explicit
[ ] CORE remains unaffected
```

### Target directory

```text
docs/advanced/
```

Do not put these supports in:

```text
docs/labs/
```

unless a future explicit curriculum revision promotes them into the official 12-TD sequence.

### R7.4 taxonomy decision

R7.4 now uses the explicit teaching taxonomy:

```text
CORE
OPTIONAL
ADVANCED
INSTRUCTOR
```

Canonical impact study:

```text
docs/legacy/06_CORE_OPTIONAL_ADVANCED_TAXONOMY_IMPACT_STUDY.md
```

### R7.4 sub-phases

| Sub-lot | Scope | Status |
|---|---|---|
| R7.4.1 | Taxonomy and impact baseline | DONE |
| R7.4.2 | P1 advanced support production | DONE |
| R7.4.3 | Lab taxonomy integration | DONE |
| R7.4.4 | Qualification and registry closure | DONE |

R7.4.1 established:

```text
56 current Optional activities
53 retained Optional activities
3 reclassified ADVANCED activities
12 P1 ADVANCED entry points
9 net-new ADVANCED choices
12 labs requiring explicit ADVANCED sections
```

No CORE or checkpoint contract was changed during R7.4.1.

### R7.4.2 execution result

Produced:

```text
12 / 12 P1 advanced support documents
```

Local executable validation:

```text
ADV-LNX-01 PASS
ADV-LNX-02 PASS
ADV-LNX-03 PASS
ADV-LNX-04 PASS
ADV-GIT-01 PASS
ADV-GIT-02 PASS
ADV-GIT-04 PASS
```

Additional structural validation:

```text
ADV-RMT-03
systemd-analyze verify
=
PASS

ADV-DASH-01
Python callback snippet syntax
=
PASS

ADV-DASH-02
Python callback snippet syntax
=
PASS
```

Current qualification result:

```text
READY_TO_TEACH
=
7

PENDING_EXTERNAL
=
5
```

READY_TO_TEACH:

```text
ADV-LNX-01
ADV-LNX-02
ADV-LNX-03
ADV-LNX-04
ADV-GIT-01
ADV-GIT-02
ADV-GIT-04
```

PENDING_EXTERNAL:

```text
ADV-RMT-01
ADV-RMT-03
ADV-BBG-01
ADV-DASH-01
ADV-DASH-02
```

Reason for PENDING_EXTERNAL:

```text
ADV-RMT-01
requires real SSH client + approved host

ADV-RMT-03
unit syntax validated
real systemd lifecycle still requires approved host

ADV-BBG-01
requires validated Bloomberg LIVE environment

ADV-DASH-01
requires real Dash package/runtime

ADV-DASH-02
requires real Dash package/runtime
+
parameterized application state
```

R7.4.2 conclusion:

```text
PASS FOR SUPPORT PRODUCTION

12 / 12 supports produced
7 / 12 READY_TO_TEACH
5 / 12 PENDING_EXTERNAL
```

R7.4.2 does not claim final R7.4 qualification.

R7.4.3 may integrate only READY_TO_TEACH supports as active student links.

### R7.4.3 execution result

Integrated the taxonomy into:

```text
TD01-TD12
docs/labs/README.md
```

Result:

```text
12 / 12 labs contain an explicit ADVANCED section

53 current activities remain OPTIONAL

3 former Optional activities are reclassified:
TD04 controlled conflict
TD11 callback
TD11 simple selector

7 READY_TO_TEACH supports are active student links

5 PENDING_EXTERNAL supports remain inactive
```

Active links:

```text
TD01 -> ADV-LNX-01, ADV-LNX-02, ADV-LNX-03
TD02 -> ADV-LNX-04
TD03 -> ADV-GIT-02
TD04 -> ADV-GIT-01
TD12 -> ADV-GIT-04
```

Pending, not activated:

```text
TD10 -> ADV-BBG-01
TD11 -> ADV-DASH-01, ADV-DASH-02
TD12 -> ADV-RMT-01, ADV-RMT-03
```

No CORE section, checkpoint requirement or canonical runtime was intentionally changed.

R7.4.3 conclusion:

```text
PASS

LAB TAXONOMY INTEGRATED
WITH READY-ONLY ACTIVATION
```

### R7.4.4 execution result

Global qualification:

```text
12 / 12 support paths resolve
12 / 12 labs contain ADVANCED
53 Optional activities remain
3 former Optional activities reclassified
7 active links target READY_TO_TEACH supports
5 PENDING_EXTERNAL supports remain inactive
0 active PENDING_EXTERNAL links
requirements.txt unchanged
checkpoint requirements unchanged
canonical runtime unchanged
```

Transverse documentation aligned:

```text
README.md
docs/04_CHECKPOINTS_AND_EVIDENCE.md
docs/06_TD_SEQUENCE_AND_LEARNING_PATH.md
docs/07_TD_TRANSVERSE_REVIEW_AND_REBALANCING.md
docs/13_MARKETPULSE_LIBRARIES_AND_DEPENDENCIES.md
docs/labs/README.md
```

P1 resolution rule:

```text
READY_TO_TEACH
or
PENDING_EXTERNAL with explicit gate
or
DEFERRED
```

Current result:

```text
READY_TO_TEACH = 7
PENDING_EXTERNAL = 5
DEFERRED = 0
AMBIGUOUS = 0
```

Closure evidence:

```text
docs/legacy/07_R7_4_ADVANCED_QUALIFICATION_AND_CLOSURE.md
```

R7.4 conclusion:

```text
DONE
```

The five external-gated items remain unavailable as student links until real validation promotes them.

## 11. R7.5 - TD enrichment capsules

### Goal

Identify small Legacy concepts that can enrich an existing TD without increasing mandatory workload.

These are not new labs.

They are instructor-side capsules.

### Candidate examples

```text
TD01
Unix philosophy
stdin / stdout / stderr
permissions troubleshooting

TD03
staging snapshot mental model
HEAD

TD04-TD06
remote-tracking refs
fetch vs pull
merge vs rebase context

TD09
Bloomberg Terminal context
BDP / BDS / BDH
request / response vs subscription
```

### Recommended format

Each capsule should be:

```text
5 to 10 minutes
optional to deliver
no new student artifact
no checkpoint requirement
```

### Possible artifact

```text
docs/instructor/02_TD_ENRICHMENT_CAPSULES.md
```

### Acceptance criteria

```text
[x] each capsule maps to one TD
[x] each capsule has a stop point
[x] no capsule changes CORE DoD
[x] no capsule creates hidden prerequisite
```

### Execution result

Created:

```text
docs/instructor/02_TD_ENRICHMENT_CAPSULES.md
```

Result:

```text
11 capsules
mapped to 6 primary TDs
```

Primary TDs:

```text
TD01
TD03
TD04
TD05
TD09
TD10
```

Intentionally no default capsule:

```text
TD02
TD06
TD07
TD08
TD11
TD12
```

The document provides for every capsule:

```text
source deep dive
duration
delivery trigger
teaching objective
micro-sequence
understanding check
stop point
non-impact statement
```

Global rules:

```text
CORE completion
>
capsule

capsule
!=
student exercise

capsule
!=
checkpoint evidence

capsule
!=
ADVANCED lab
```

R7.5 conclusion:

```text
PASS

TD ENRICHMENT CAPSULES
OPERATIONAL
```

## 12. R7.6 - Advanced-track packaging

### Goal

Make the advanced material navigable once several items are READY_TO_TEACH.

### Planned artifacts

```text
docs/advanced/README.md
docs/advanced/ADV_*.md
```

### README should explain

```text
who should use advanced labs
when they should be used
how diagnostic results may influence selection
which labs require external infrastructure
which labs require proprietary access
which labs are self-study
which labs are instructor-demo only
```

### Rule

```text
advanced track
!=
second mandatory curriculum
```

## 13. R7.7 - Legacy closure audit

### Goal

Prove that the Legacy stream has no remaining ambiguous high-value content.

### Final audit sources

```text
historical repository analysis
Legacy mapping
advanced backlog
instructor deep dives
advanced supports
TD enrichment capsules
final migration registry
```

### Final questions

```text
Has every high-priority Legacy topic received a final destination?

Has every P1 advanced item been explicitly resolved as:
READY_TO_TEACH
or
PENDING_EXTERNAL with an explicit delivery gate
or
DEFERRED?

Have instructor-priority concepts been operationalized?

Are DROP items still excluded from the CORE?

Did any advanced item silently become mandatory?

Did any historical proprietary claim become current without verification?

Did any copied asset bypass license review?
```

### Final acceptance criteria

```text
[ ] final migration registry complete
[ ] 10 instructor priority deep dives resolved
[ ] every P1 advanced item resolved
[ ] TD enrichment capsules reviewed
[ ] advanced index exists if advanced supports exist
[ ] no Legacy item changes checkpoint requirements
[ ] no Legacy item changes frozen CORE runtime
[ ] no unverified third-party asset migration
[ ] no mandatory personal payment requirement
[ ] no fake LIVE provider requirement
[ ] all DROP clusters remain closed or have explicit reversal
```

### Final conclusion target

```text
LEGACY CONTENT OPERATIONALIZATION
COMPLETE
```

## 14. Status model

Use only:

```text
NOT STARTED
IN PROGRESS
REVIEW
DONE
DEFERRED
```

For advanced backlog items, keep the existing item-level statuses:

```text
CANDIDATE
READY_TO_DESIGN
PENDING_EXTERNAL
READY_TO_TEACH
DEFERRED
REJECTED
```

Do not mix the two status systems.

## 15. Current status board

| Lot | Scope | Status |
|---|---|---|
| R7.1 | Legacy freeze reconciliation | DONE |
| R7.2 | Final migration registry | DONE |
| R7.3 | Instructor deep-dive operationalization | DONE |
| R7.4 | Advanced P1 content operationalization | DONE |
| R7.5 | TD enrichment capsules | DONE |
| R7.6 | Advanced-track packaging | NEXT |
| R7.7 | Legacy closure audit | NOT STARTED |

## 16. Current baseline facts

At roadmap creation time:

```text
R1-R6 CORE remediation/readiness
=
closed

Legacy historical analysis
=
DONE

Legacy content mapping
=
DONE

Optional advanced backlog
=
DONE as backlog design

Instructor deep-dive reference
=
DONE as consolidated reference

Instructor deep-dive operationalization
=
DONE

Advanced P1 support production
=
DONE

Current P1 qualification
=
7 READY_TO_TEACH
+
5 PENDING_EXTERNAL
```

This distinction is important.

A complete analysis is not the same as complete teaching operationalization.

## 17. Definition of Done

R7 is complete only when:

```text
[x] R7.1 DONE
[x] R7.2 DONE
[x] R7.3 DONE
[x] R7.4 DONE with every P1 item explicitly resolved
[x] R7.5 DONE
[ ] R7.6 DONE when advanced supports exist
[ ] R7.7 DONE
```

Expected final state:

```text
frozen 18-hour CORE
+
final Legacy migration registry
+
operational instructor deep dives
+
usable advanced supports
+
controlled enrichment capsules
+
explicit DROP closure
=
LEGACY VALUE PRESERVED
WITHOUT CORE DIVERGENCE
```

## 18. Immediate next action

The current action is:

```text
R7.6 - Advanced-track packaging
```

R7.5 is closed.

The instructor layer now contains both:
10 operational deep dives
+
11 TD enrichment capsules.
