# R7.4 Advanced Qualification and Closure

## 1. Purpose

This document records the final qualification of:

```text
R7.4 - Advanced P1 content operationalization
```

It closes the implementation loop started by:

```text
docs/legacy/06_CORE_OPTIONAL_ADVANCED_TAXONOMY_IMPACT_STUDY.md
```

without reopening the frozen 18-hour CORE.

## 2. Qualification policy

R7.4 distinguishes:

```text
support production
student activation
external delivery validation
```

A P1 item is considered operationally resolved for R7.4 when it is one of:

```text
READY_TO_TEACH
PENDING_EXTERNAL
DEFERRED
```

Interpretation:

```text
READY_TO_TEACH
=
support exists
+
required execution was validated
+
student link may be active

PENDING_EXTERNAL
=
support exists
+
local/static qualification is complete
+
real delivery depends on an external environment
+
student link must remain inactive

DEFERRED
=
explicitly postponed
```

PENDING_EXTERNAL is not success evidence for the external system.

## 3. Support inventory

All 12 P1 support files exist:

```text
ADV_LNX_01_FILE_OPERATIONS.md
ADV_LNX_02_PERMISSIONS_CHMOD.md
ADV_LNX_03_PIPES_TEXT_PROCESSING.md
ADV_LNX_04_ENVIRONMENT_VARIABLES.md

ADV_GIT_01_CONFLICT_RESOLUTION.md
ADV_GIT_02_RESTORE_REVERT_RESET.md
ADV_GIT_04_TAGS_RELEASES.md

ADV_RMT_01_SSH_FUNDAMENTALS.md
ADV_RMT_03_SYSTEMD_SERVICE.md

ADV_BBG_01_REFERENCE_DATA.md

ADV_DASH_01_CALLBACK.md
ADV_DASH_02_INSTRUMENT_SELECTOR.md
```

Result:

```text
12 / 12 support paths resolve
```

## 4. READY_TO_TEACH result

Validated and active:

```text
ADV-LNX-01
ADV-LNX-02
ADV-LNX-03
ADV-LNX-04
ADV-GIT-01
ADV-GIT-02
ADV-GIT-04
```

Count:

```text
7
```

These seven supports are linked from student labs.

## 5. PENDING_EXTERNAL result

Not activated:

```text
ADV-RMT-01
ADV-RMT-03
ADV-BBG-01
ADV-DASH-01
ADV-DASH-02
```

Count:

```text
5
```

Required gates:

```text
ADV-RMT-01
- real SSH client
- approved remote host
- approved identity/credential model

ADV-RMT-03
- approved systemd host
- approved service-management permissions
- real start/status/log/stop lifecycle

ADV-BBG-01
- validated Bloomberg LIVE environment
- observed identifiers/fields
- no fabricated provider evidence

ADV-DASH-01
- real Dash package/runtime
- real callback execution

ADV-DASH-02
- real Dash package/runtime
- ADV-DASH-01 validated
- parameterized application state
```

## 6. Lab taxonomy audit

Observed across TD01-TD12:

```text
ADVANCED sections
=
12 / 12

Optional activities retained
=
53

former Optional activities reclassified
=
3

active READY_TO_TEACH links
=
7

active PENDING_EXTERNAL links
=
0
```

The three reclassifications are:

```text
TD04 controlled conflict
->
ADV-GIT-01

TD11 callback
->
ADV-DASH-01

TD11 simple selector
->
ADV-DASH-02
```

The two Dash items remain inactive because their status is PENDING_EXTERNAL.

## 7. Active entry-point map

| TD | Active ADVANCED support |
|---|---|
| TD01 | ADV-LNX-01 |
| TD01 | ADV-LNX-02 |
| TD01 | ADV-LNX-03 |
| TD02 | ADV-LNX-04 |
| TD03 | ADV-GIT-02 |
| TD04 | ADV-GIT-01 |
| TD12 | ADV-GIT-04 |

Inactive planned destinations:

| TD | P1 support | Status |
|---|---|---|
| TD10 | ADV-BBG-01 | PENDING_EXTERNAL |
| TD11 | ADV-DASH-01 | PENDING_EXTERNAL |
| TD11 | ADV-DASH-02 | PENDING_EXTERNAL |
| TD12 | ADV-RMT-01 | PENDING_EXTERNAL |
| TD12 | ADV-RMT-03 | PENDING_EXTERNAL |

## 8. CORE isolation audit

R7.4.3 integration was performed with an explicit guard that preserved the text before each lab's OPTIONAL boundary while adding or moving non-CORE material.

Result:

```text
CORE teaching contract changed
=
NO
```

Still unchanged:

```text
12-TD sequence
18-hour CORE
canonical runtime commands
provider boundary
analytics formulas
snapshot contract
checkpoint timing
assessment weights
```

## 9. Checkpoint isolation audit

Canonical required evidence remains unchanged.

R7.4 adds the explicit rule:

```text
ADVANCED work is never required
for Checkpoint A, B or C
```

The existing:

```text
05_advanced_deployment.png
```

remains optional.

Result:

```text
checkpoint requirement change
=
NO
```

## 10. Dependency isolation audit

The root dependency file remains at the same Git blob SHA observed before R7.4:

```text
665b35953c94f8a6ce09c3a326161744ffb3a4c0
```

Therefore:

```text
requirements.txt contamination
=
NO
```

Advanced-only environment requirements remain documented inside their advanced supports.

## 11. Transverse-document alignment

Updated:

```text
README.md
docs/04_CHECKPOINTS_AND_EVIDENCE.md
docs/06_TD_SEQUENCE_AND_LEARNING_PATH.md
docs/07_TD_TRANSVERSE_REVIEW_AND_REBALANCING.md
docs/13_MARKETPULSE_LIBRARIES_AND_DEPENDENCIES.md
docs/labs/README.md
docs/legacy/03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
docs/legacy/04_LEGACY_CONTENT_OPERATIONALIZATION_ROADMAP.md
docs/legacy/05_LEGACY_FINAL_MIGRATION_REGISTRY.md
docs/legacy/06_CORE_OPTIONAL_ADVANCED_TAXONOMY_IMPACT_STUDY.md
```

The vocabulary is now consistently:

```text
CORE
OPTIONAL
ADVANCED
INSTRUCTOR
```

## 12. R7.4 acceptance criteria

```text
[x] 12 P1 support files exist
[x] all 12 labs contain an ADVANCED section
[x] 53 Optional activities remain
[x] 3 former Optional activities are reclassified
[x] 7 READY_TO_TEACH student links are active
[x] 5 PENDING_EXTERNAL supports are inactive
[x] every active link targets READY_TO_TEACH content
[x] all 12 support paths resolve
[x] checkpoint requirements remain unchanged
[x] canonical runtime remains unchanged
[x] requirements.txt remains unchanged
[x] transverse documentation is aligned
[x] no fake external validation is claimed
```

Unchecked:

```text
0
```

## 13. Closure decision

R7.4 conclusion:

```text
DONE

7 READY_TO_TEACH
5 PENDING_EXTERNAL
0 ambiguous P1 items
```

This means:

```text
advanced operationalization
=
closed as a repository-design lot

external activation gates
=
still real and still enforced
```

A future external validation may promote a PENDING_EXTERNAL item to READY_TO_TEACH without reopening the frozen CORE.

## 14. Next action

The next roadmap lot is:

```text
R7.5 - TD enrichment capsules
```

R7.5 concerns instructor-side 5 to 10 minute enrichment moments.

It must not duplicate the full deep-dive notes or the student advanced labs.
