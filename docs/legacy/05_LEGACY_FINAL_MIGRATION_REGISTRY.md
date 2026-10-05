# Legacy Final Migration Registry

## 1. Purpose

This document is the authoritative migration registry for significant content inherited from:

```text
tawounfouet/intro_git_linux_bloomberg
```

It translates the Legacy analysis and mapping into final operational destinations.

The registry answers, for every significant topic:

```text
Where did it go?
What is its final status?
What still has to be produced?
What is intentionally closed?
```

This document is governed by:

```text
docs/legacy/04_LEGACY_CONTENT_OPERATIONALIZATION_ROADMAP.md
```

It does not modify the frozen R1-R6 MarketPulse CORE.

## 2. Source documents

Primary classification sources:

```text
docs/legacy/01_PREVIOUS_COURSE_REPOSITORY_ANALYSIS.md
docs/legacy/02_LEGACY_TO_MARKETPULSE_CONTENT_MAPPING.md
docs/legacy/03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
docs/instructor/01_LEGACY_DEEP_DIVE_REFERENCE.md
```

Frozen CORE boundary:

```text
docs/16_TEACHING_BASELINE_RELEASE.md
```

## 3. Destination vocabulary

Every registry row uses exactly one final destination family:

```text
CORE_MIGRATED
INSTRUCTOR_READY
ADVANCED_READY
REFERENCE_ONLY
DROP_CLOSED
```

Interpretation:

```text
CORE_MIGRATED
=
already absorbed into TD01-TD12

INSTRUCTOR_READY
=
teacher-facing operational note is the intended final destination

ADVANCED_READY
=
optional advanced support is the intended final destination

REFERENCE_ONLY
=
historical or conceptual reference remains useful without dedicated teaching production

DROP_CLOSED
=
explicitly excluded from the current curriculum
```

A destination may be final while its operational asset is still pending.

Example:

```text
destination = INSTRUCTOR_READY
operational status = TO_BUILD_R7.3
```

## 4. Operational status vocabulary

Use:

```text
DONE
TO_BUILD_R7.3
READY_TO_DESIGN_R7.4
CANDIDATE
DEFERRED
CLOSED
```

Validation status:

```text
VALIDATED_CORE
MAPPED
REFERENCE_VALIDATED
TO_VALIDATE
CLOSED_BY_POLICY
```

## 5. CORE_MIGRATED registry

| ID | Legacy source | Legacy topic | Original decision | Final destination | Current target | Operational status | Validation | Notes |
|---|---|---|---|---|---|---|---|---|
| CORE-LNX-01 | CM1 / TD1.1 | Terminal navigation | CORE | CORE_MIGRATED | TD01 | DONE | VALIDATED_CORE | pwd, ls, cd |
| CORE-LNX-02 | CM1 / TD1.1 | File inspection | CORE | CORE_MIGRATED | TD01 | DONE | VALIDATED_CORE | cat, head |
| CORE-LNX-03 | TD1.3 | grep | CORE | CORE_MIGRATED | TD01 | DONE | VALIDATED_CORE | simple text filtering |
| CORE-LNX-04 | CM1 | Linux CLI culture | CORE | CORE_MIGRATED | TD01 | DONE | VALIDATED_CORE | terminal autonomy only |
| CORE-GIT-01 | CM2 / TD2 | git status | CORE | CORE_MIGRATED | TD03 | DONE | VALIDATED_CORE | local state inspection |
| CORE-GIT-02 | CM2 / TD2 | git diff | CORE | CORE_MIGRATED | TD03 | DONE | VALIDATED_CORE | unstaged/staged comparison |
| CORE-GIT-03 | CM2 / TD2 | git add | CORE | CORE_MIGRATED | TD03 | DONE | VALIDATED_CORE | staging workflow |
| CORE-GIT-04 | CM2 / TD2 | git commit | CORE | CORE_MIGRATED | TD03 | DONE | VALIDATED_CORE | meaningful commit |
| CORE-GIT-05 | CM2 / TD2 | git log / show | CORE | CORE_MIGRATED | TD03 | DONE | VALIDATED_CORE | history inspection |
| CORE-GIT-06 | CM2 | working tree / staging / commit mental model | CORE | CORE_MIGRATED | TD03 | DONE | VALIDATED_CORE | student-visible workflow; deeper internals go to R7.3 |
| CORE-GIT-07 | CM3 / TD3 | branch creation | CORE | CORE_MIGRATED | TD04 | DONE | VALIDATED_CORE | feature branch |
| CORE-GIT-08 | CM3 / TD3 | merge | CORE | CORE_MIGRATED | TD04 | DONE | VALIDATED_CORE | fast-forward accepted |
| CORE-GIT-09 | TD3 | merge-conflict concept | CORE concept | CORE_MIGRATED | TD04 | DONE | VALIDATED_CORE | full manufactured conflict remains advanced |
| CORE-GIT-10 | CM3 | remote origin | CORE | CORE_MIGRATED | TD05 | DONE | VALIDATED_CORE | team remote model |
| CORE-GIT-11 | CM3 / TD3 | push | CORE | CORE_MIGRATED | TD05 | DONE | VALIDATED_CORE | remote feature branch |
| CORE-GIT-12 | CM3 / TD3 | Pull Request | CORE | CORE_MIGRATED | TD05 | DONE | VALIDATED_CORE | team-fork workflow |
| CORE-GIT-13 | CM3 / TD3 | review / approval | CORE | CORE_MIGRATED | TD06 | DONE | VALIDATED_CORE | explicit code-review stage |
| CORE-GIT-14 | CM3 | fetch / synchronization support | CORE support | CORE_MIGRATED | TD04-TD06 | DONE | VALIDATED_CORE | used in team baseline/recovery |
| CORE-BBG-01 | CM4 | Bloomberg professional-provider context | CORE concept | CORE_MIGRATED | TD09 | DONE | VALIDATED_CORE | current operational claims remain environment-verified |
| CORE-BBG-02 | CM4 / TD4 | security identifier mapping | CORE | CORE_MIGRATED | TD09 | DONE | VALIDATED_CORE | AAPL -> AAPL US Equity; SP500 -> SPX Index |
| CORE-BBG-03 | TD4 | historical market-data acquisition | CORE | CORE_MIGRATED | TD10 | DONE | VALIDATED_CORE | LIVE or APPROVED_SAMPLE |
| CORE-BBG-04 | TD4 | OHLCV normalization | CORE | CORE_MIGRATED | TD09-TD10 | DONE | VALIDATED_CORE | canonical row contract |
| CORE-APP-01 | Historical project | external market data | CORE | CORE_MIGRATED | TD08-TD10 | DONE | VALIDATED_CORE | Yahoo + Bloomberg stages |
| CORE-APP-02 | Historical project | dashboard | CORE | CORE_MIGRATED | TD11 | DONE | VALIDATED_CORE | Dash + Plotly |
| CORE-APP-03 | Historical project | reproducibility / deployment ambition | CORE reduced | CORE_MIGRATED | TD12 | DONE | VALIDATED_CORE | clean reproducibility replaces infrastructure-heavy deployment |

CORE migration conclusion:

```text
25 significant Legacy concepts
already absorbed into the frozen CORE
```

These items must not be duplicated into separate mandatory Legacy labs.

## 6. INSTRUCTOR_READY target registry

These topics are already covered in the consolidated instructor reference.

Their final destination is an operational instructor note under R7.3.

| ID | Legacy source | Topic | Original decision | Final destination | R7.3 target | Operational status | Validation | Best current TD |
|---|---|---|---|---|---|---|---|---|
| INS-GIT-01 | CM2 | Staging mental model | TEACHER_REFERENCE + CORE support | INSTRUCTOR_READY | deep-dives/INS_GIT_01_STAGING_MENTAL_MODEL.md | TO_BUILD_R7.3 | MAPPED | TD03 |
| INS-GIT-02 | CM2 / CM3 | HEAD / refs / remote-tracking refs | TEACHER_REFERENCE | INSTRUCTOR_READY | deep-dives/INS_GIT_02_HEAD_REFS_REMOTE_TRACKING.md | TO_BUILD_R7.3 | MAPPED | TD03-TD05 |
| INS-GIT-03 | CM2 | Git object model: blob/tree/commit | TEACHER_REFERENCE | INSTRUCTOR_READY | deep-dives/INS_GIT_03_OBJECT_MODEL.md | TO_BUILD_R7.3 | MAPPED | TD03 |
| INS-GIT-04 | CM3 | Merge vs rebase | TEACHER_REFERENCE | INSTRUCTOR_READY | deep-dives/INS_GIT_04_MERGE_VS_REBASE.md | TO_BUILD_R7.3 | MAPPED | TD04-TD06 |
| INS-LNX-01 | CM0 / CM1 | Unix philosophy | TEACHER_REFERENCE | INSTRUCTOR_READY | deep-dives/INS_LNX_01_UNIX_PHILOSOPHY.md | TO_BUILD_R7.3 | MAPPED | TD01 |
| INS-LNX-02 | CM1 / TD1.1 / TD1.4 | Permissions troubleshooting | TEACHER_REFERENCE | INSTRUCTOR_READY | deep-dives/INS_LNX_02_PERMISSIONS_TROUBLESHOOTING.md | TO_BUILD_R7.3 | MAPPED | TD01 / advanced remote |
| INS-BBG-01 | CM4 | Bloomberg Terminal + identifiers | TEACHER_REFERENCE | INSTRUCTOR_READY | deep-dives/INS_BBG_01_TERMINAL_IDENTIFIERS.md | TO_BUILD_R7.3 | MAPPED | TD09 |
| INS-BBG-02 | CM4 | BDP / BDS / BDH | TEACHER_REFERENCE | INSTRUCTOR_READY | deep-dives/INS_BBG_02_BDP_BDS_BDH.md | TO_BUILD_R7.3 | MAPPED | TD09 |
| INS-BBG-03 | CM4 | Request/Response vs Subscription | TEACHER_REFERENCE | INSTRUCTOR_READY | deep-dives/INS_BBG_03_REQUEST_RESPONSE_SUBSCRIPTION.md | TO_BUILD_R7.3 | MAPPED | TD09-TD10 |
| INS-BBG-04 | CM4 | xbbg vs blpapi | TEACHER_REFERENCE | INSTRUCTOR_READY | deep-dives/INS_BBG_04_XBBG_VS_BLPAPI.md | TO_BUILD_R7.3 | MAPPED | TD10 |

R7.3 closure requirement:

```text
10 / 10
must become INSTRUCTOR_READY
```

## 7. ADVANCED_READY P1 registry

These are the 12 P1 backlog items that R7.4 must resolve.

| ID | Legacy source | Topic | Original decision | Final destination | Target support | Current backlog status | R7.4 status | Validation |
|---|---|---|---|---|---|---|---|---|
| ADV-LNX-01 | TD1.1 | File operations | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_LNX_01_FILE_OPERATIONS.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-LNX-02 | TD1.1 | Permissions and chmod | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_LNX_02_PERMISSIONS_CHMOD.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-LNX-03 | TD1.3 | Pipes and text processing | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_LNX_03_PIPES_TEXT_PROCESSING.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-LNX-04 | CM1 / TD1.2 | Environment variables | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_LNX_04_ENVIRONMENT_VARIABLES.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-GIT-01 | TD3 | Conflict resolution | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_GIT_01_CONFLICT_RESOLUTION.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-GIT-02 | TD2 | Restore / revert / reset | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_GIT_02_RESTORE_REVERT_RESET.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-GIT-04 | CM3 | Tags and releases | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_GIT_04_TAGS_RELEASES.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-RMT-01 | TD1.4 | SSH fundamentals | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_RMT_01_SSH_FUNDAMENTALS.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-RMT-03 | Historical deployment | systemd service | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_RMT_03_SYSTEMD_SERVICE.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-BBG-01 | CM4 / TD4 | Bloomberg reference data | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_BBG_01_REFERENCE_DATA.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-DASH-01 | Historical project | Dash callback | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_DASH_01_CALLBACK.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |
| ADV-DASH-02 | Historical project | Instrument selector | OPTIONAL | ADVANCED_READY | docs/advanced/ADV_DASH_02_INSTRUMENT_SELECTOR.md | READY_TO_DESIGN | READY_TO_DESIGN_R7.4 | TO_VALIDATE |

R7.4 rule:

```text
Each P1 item must become:
READY_TO_TEACH
or
explicitly DEFERRED
```

No P1 item may disappear silently.

## 8. Other optional backlog registry

These items remain valid optional candidates but are not required for R7.4 P1 closure.

| ID | Legacy source | Topic | Final destination | Current status | Validation | Notes |
|---|---|---|---|---|---|---|
| ADV-LNX-05 | CM1 / TD1 | Bash scripting | ADVANCED_READY | CANDIDATE | MAPPED | P2 |
| ADV-LNX-06 | TD1.2 | Cron scheduling | ADVANCED_READY | CANDIDATE | MAPPED | P2 |
| ADV-GIT-03 | TD3 | Interactive rebase | ADVANCED_READY | CANDIDATE | MAPPED | P2, shared-history warning |
| ADV-GIT-05 | CM2 | Git aliases / productivity | ADVANCED_READY | CANDIDATE | MAPPED | P3 |
| ADV-RMT-02 | TD1.4 | SCP file transfer | ADVANCED_READY | CANDIDATE | MAPPED | P2 |
| ADV-RMT-04 | Historical project | VPS deployment | ADVANCED_READY | CANDIDATE | MAPPED | P2, no personal billing |
| ADV-BBG-02 | CM4 | xbbg exploration | ADVANCED_READY | CANDIDATE | MAPPED | P2, instructor-demo candidate |
| ADV-BBG-03 | CM4 | blpapi low-level request | ADVANCED_READY | CANDIDATE | MAPPED | P2, LIVE environment dependent |
| ADV-BBG-04 | TD4 | Intraday bars | ADVANCED_READY | CANDIDATE | MAPPED | P2, separate complexity class |
| ADV-DEP-01 | Historical project | Docker | ADVANCED_READY | CANDIDATE | MAPPED | P2 |
| ADV-DEP-02 | Historical project | GitHub Actions | ADVANCED_READY | CANDIDATE | MAPPED | P2 |
| ADV-DEP-03 | Historical project | Service + reverse proxy | ADVANCED_READY | DEFERRED | MAPPED | P3 |

These may remain candidates at R7 closure if they are not part of the P1 commitment.

## 9. REFERENCE_ONLY registry

These concepts are useful context but do not need dedicated student-facing production in R7.

| ID | Legacy source | Topic | Original decision | Final destination | Current reference | Status | Notes |
|---|---|---|---|---|---|---|---|
| REF-LNX-01 | CM1 | Unix history | TEACHER_REFERENCE | REFERENCE_ONLY | instructor deep dive | CLOSED | cultural context |
| REF-LNX-02 | CM1 | GNU history | TEACHER_REFERENCE | REFERENCE_ONLY | instructor deep dive | CLOSED | cultural context |
| REF-LNX-03 | CM1 | POSIX history | TEACHER_REFERENCE | REFERENCE_ONLY | instructor deep dive | CLOSED | cultural context |
| REF-INFRA-01 | CM1 | VM vs containers | TEACHER_REFERENCE | REFERENCE_ONLY | instructor deep dive | CLOSED | conceptual context |
| REF-INFRA-02 | CM1 | Docker / Kubernetes context | TEACHER_REFERENCE | REFERENCE_ONLY | instructor deep dive | CLOSED | no CORE requirement |
| REF-SUST-01 | CM0 | data-center sustainability / PUE / carbon context | TEACHER_REFERENCE | REFERENCE_ONLY | analysis + instructor reference | CLOSED | optional contextual explanation |
| REF-GIT-01 | CM2 | plumbing vs porcelain | TEACHER_REFERENCE | REFERENCE_ONLY | instructor deep dive | CLOSED | advanced cultural context |
| REF-GIT-02 | CM3 | Gitflow | TEACHER_REFERENCE | REFERENCE_ONLY | instructor deep dive | CLOSED | workflow example only |
| REF-BBG-01 | CM4 | B-PIPE | TEACHER_REFERENCE | REFERENCE_ONLY | instructor deep dive | CLOSED | not CORE |
| REF-BBG-02 | CM4 | Publishing paradigm | TEACHER_REFERENCE | REFERENCE_ONLY | instructor deep dive | CLOSED | not CORE |
| REF-ASSESS-01 | exam / README | Historical exam style | TEACHER_REFERENCE | REFERENCE_ONLY | analysis + instructor reference | CLOSED | not current weighting |
| REF-BUILD-01 | LaTeX source/build scripts | Historical LaTeX build system | REFERENCE_ONLY | REFERENCE_ONLY | legacy repository | CLOSED | no migration required |
| REF-ASSET-01 | historical images/PDFs | diagrams/logos/screenshots | TEACHER_REFERENCE | REFERENCE_ONLY | legacy repository | CLOSED | reuse requires rights check |

## 10. DROP_CLOSED registry

The following clusters are explicitly closed for the current common curriculum.

| ID | Legacy source | Topic / cluster | Original decision | Final destination | Status | Closure reason |
|---|---|---|---|---|---|---|
| DROP-CLOUD-01 | TD1.4 | Mandatory personal cloud account | DROP | DROP_CLOSED | CLOSED | logistical/security risk |
| DROP-CLOUD-02 | TD1.4 | Mandatory personal credit card | DROP | DROP_CLOSED | CLOSED | unacceptable course prerequisite |
| DROP-CLOUD-03 | TD1.4 | Mandatory personal VM creation | DROP | DROP_CLOSED | CLOSED | replaced by optional/instructor-provisioned infrastructure |
| DROP-LNX-01 | TD1.2 | ACL as common requirement | DROP | DROP_CLOSED | CLOSED | outside common autonomy objective |
| DROP-GIT-01 | TD2 | Manual Git object construction | DROP | DROP_CLOSED | CLOSED | too deep for shared 18h CORE |
| DROP-GIT-02 | TD2 | zlib injection / direct .git objects | DROP | DROP_CLOSED | CLOSED | internals exercise only |
| DROP-GIT-03 | TD3 | Mandatory interactive rebase | DROP | DROP_CLOSED | CLOSED | advanced history rewrite |
| DROP-GIT-04 | CM3 | Mandatory Gitflow | DROP | DROP_CLOSED | CLOSED | excessive workflow overhead |
| DROP-BBG-01 | TD4 | Mandatory intraday Bloomberg | DROP | DROP_CLOSED | CLOSED | CORE is 1 month / Daily |
| DROP-BBG-02 | TD4 | Mandatory 5-minute interval | DROP | DROP_CLOSED | CLOSED | time-zone/market-hour complexity |
| DROP-BBG-03 | TD4 | Mandatory matplotlib Bloomberg plotting | DROP | DROP_CLOSED | CLOSED | presentation centralized in TD11 |
| DROP-APP-01 | Historical project | Automatic refresh every 5 minutes | DROP | DROP_CLOSED | CLOSED | outside guided CORE |
| DROP-APP-02 | Historical project | 24/7 hosting requirement | DROP | DROP_CLOSED | CLOSED | infrastructure burden |
| DROP-APP-03 | Historical project | Mandatory cron reporting | DROP | DROP_CLOSED | CLOSED | optional only |
| DROP-QUANT-01 | Historical project | Backtesting | DROP | DROP_CLOSED | CLOSED | obscures Python/Git/Linux goals |
| DROP-QUANT-02 | Historical project | Max drawdown | DROP | DROP_CLOSED | CLOSED | advanced quant scope |
| DROP-QUANT-03 | Historical project | Sharpe ratio | DROP | DROP_CLOSED | CLOSED | advanced quant scope |
| DROP-QUANT-04 | Historical project | Multi-asset portfolio | DROP | DROP_CLOSED | CLOSED | advanced quant scope |
| DROP-QUANT-05 | Historical project | Correlation matrix | DROP | DROP_CLOSED | CLOSED | advanced quant scope |
| DROP-QUANT-06 | Historical project | Portfolio volatility | DROP | DROP_CLOSED | CLOSED | advanced quant scope |
| DROP-QUANT-07 | Historical project | Rebalancing | DROP | DROP_CLOSED | CLOSED | advanced quant scope |
| DROP-ML-01 | Historical project | Machine-learning bonus | DROP | DROP_CLOSED | CLOSED | outside module CORE |
| DROP-UI-01 | Historical project | Streamlit as common framework | DROP | DROP_CLOSED | CLOSED | current presentation framework is Dash |
| DROP-DATA-01 | Historical project | Public API / web scraping as common requirement | DROP | DROP_CLOSED | CLOSED | provider path is explicit |
| DROP-ASSESS-01 | Historical README | historical 1/3 + 1/3 + 1/3 weighting | DROP | DROP_CLOSED | CLOSED | current assessment contract differs |
| DROP-BUILD-01 | Historical repo | LaTeX build chain in MarketPulse | DROP | DROP_CLOSED | CLOSED | Markdown-first repository |

DROP rule:

```text
DROP_CLOSED
!=
topic has no value
```

It means:

```text
not part of the current common curriculum
```

Any future reversal requires an explicit roadmap and CORE change decision.

## 11. High-priority Legacy coverage check

The historical analysis identified these high-priority reuse themes:

```text
Git mental model
working tree / staging / commit
branch graphs
PR concepts
merge conflict explanation
Bloomberg BDP / BDS / BDH overview
Bloomberg xbbg vs blpapi overview
Linux CLI culture
Unix philosophy
SSH concept
```

Registry coverage:

| High-priority theme | Registry destination |
|---|---|
| Git mental model | CORE-GIT-06 + INS-GIT-01/02/03 |
| working tree / staging / commit | CORE-GIT-06 + INS-GIT-01 |
| branch graphs | CORE-GIT-07/08 + INS-GIT-02 |
| PR concepts | CORE-GIT-12/13 |
| merge conflict explanation | CORE-GIT-09 + ADV-GIT-01 |
| BDP / BDS / BDH | INS-BBG-02 |
| xbbg vs blpapi | INS-BBG-04 + optional ADV-BBG-02/03 |
| Linux CLI culture | CORE-LNX-01/02/03/04 |
| Unix philosophy | INS-LNX-01 |
| SSH concept | ADV-RMT-01 |

Result:

```text
10 / 10 high-priority themes
have an explicit destination
```

## 12. R7 dependency map

The registry establishes the execution order:

```text
R7.2 registry
    |
    +--> 10 INSTRUCTOR_READY targets
    |       |
    |       v
    |      R7.3
    |
    +--> 12 P1 ADVANCED_READY targets
    |       |
    |       v
    |      R7.4
    |
    +--> CORE + instructor topics
    |       |
    |       v
    |      R7.5 capsules
    |
    +--> READY_TO_TEACH assets
            |
            v
           R7.6
            |
            v
           R7.7 audit
```

## 13. Registry completeness

Current registry totals:

```text
CORE_MIGRATED rows           = 25
INSTRUCTOR_READY targets     = 10
P1 ADVANCED_READY targets    = 12
other optional rows          = 12
REFERENCE_ONLY rows          = 13
DROP_CLOSED rows             = 26
```

Total registered rows:

```text
98
```

The count is a traceability aid, not a curriculum-size target.

## 14. No undefined destination rule

After R7.2:

```text
high-priority Legacy topics
=
fully routed

P1 optional topics
=
fully routed

priority instructor topics
=
fully routed

major DROP clusters
=
explicitly closed
```

Remaining non-P1 candidates are intentionally kept in the optional backlog with explicit statuses.

They are not undefined work.

## 15. Change control

Any future change to a row must preserve:

```text
one final destination
+
one operational status
+
one validation status
```

If a topic changes destination:

```text
record the reason
+
update this registry
+
update the R7 roadmap
+
revalidate affected teaching contracts
```

A topic must never silently move from:

```text
OPTIONAL
to
CORE
```

or from:

```text
DROP_CLOSED
to
active teaching
```

## 16. R7.2 acceptance result

```text
[x] every high-priority Legacy topic has a row
[x] every P1 optional backlog item has a row
[x] every instructor-priority deep dive has a row
[x] every major DROP cluster has a documented closure
[x] no important Legacy concept has an undefined destination
```

R7.2 conclusion:

```text
PASS

LEGACY FINAL MIGRATION REGISTRY
ESTABLISHED
```

## 17. Next action

The registry now authorizes execution of:

```text
R7.3 - Instructor deep-dive operationalization
```

R7.3 should use the exact IDs:

```text
INS-GIT-01
INS-GIT-02
INS-GIT-03
INS-GIT-04
INS-LNX-01
INS-LNX-02
INS-BBG-01
INS-BBG-02
INS-BBG-03
INS-BBG-04
```

Do not create unrelated instructor notes outside those targets without first updating this registry and the R7 roadmap.
