# Instructor Deep-Dive Index

## 1. Purpose

This directory contains the operational instructor notes created from the Legacy teaching material.

They are not student labs.

They are not checkpoint requirements.

They exist to help the instructor answer deeper questions without expanding the frozen MarketPulse CORE.

The governing roadmap is:

```text
docs/legacy/04_LEGACY_CONTENT_OPERATIONALIZATION_ROADMAP.md
```

The migration registry is:

```text
docs/legacy/05_LEGACY_FINAL_MIGRATION_REGISTRY.md
```

## 2. Status

All 10 R7.3 priority notes are:

```text
INSTRUCTOR_READY
```

## 3. Git deep dives

| ID | Topic | Best TD | Typical use |
|---|---|---|---|
| INS-GIT-01 | Staging mental model | TD03 | Explain working tree vs index vs commit |
| INS-GIT-02 | HEAD / refs / remote-tracking refs | TD03-TD05 | Explain HEAD, main, origin/main and fetch |
| INS-GIT-03 | Git object model | TD03 | Answer what a commit/branch really is |
| INS-GIT-04 | Merge vs rebase | TD04-TD06 | Answer advanced workflow questions without changing CORE |

Files:

```text
INS_GIT_01_STAGING_MENTAL_MODEL.md
INS_GIT_02_HEAD_REFS_REMOTE_TRACKING.md
INS_GIT_03_OBJECT_MODEL.md
INS_GIT_04_MERGE_VS_REBASE.md
```

## 4. Linux deep dives

| ID | Topic | Best TD | Typical use |
|---|---|---|---|
| INS-LNX-01 | Unix philosophy | TD01 | Explain terminal composition and small-tool thinking |
| INS-LNX-02 | Permissions troubleshooting | TD01 / advanced remote | Diagnose permission errors safely |

Files:

```text
INS_LNX_01_UNIX_PHILOSOPHY.md
INS_LNX_02_PERMISSIONS_TROUBLESHOOTING.md
```

## 5. Bloomberg deep dives

| ID | Topic | Best TD | Typical use |
|---|---|---|---|
| INS-BBG-01 | Terminal + identifiers | TD09 | Explain provider identifiers and provider boundaries |
| INS-BBG-02 | BDP / BDS / BDH | TD09 | Give Bloomberg retrieval vocabulary |
| INS-BBG-03 | Request/Response vs Subscription | TD09-TD10 | Explain why MarketPulse is historical rather than streaming |
| INS-BBG-04 | xbbg vs blpapi | TD10 | Explain integration abstraction levels |

Files:

```text
INS_BBG_01_TERMINAL_IDENTIFIERS.md
INS_BBG_02_BDP_BDS_BDH.md
INS_BBG_03_REQUEST_RESPONSE_SUBSCRIPTION.md
INS_BBG_04_XBBG_VS_BLPAPI.md
```

## 6. Instructor usage rule

Use a deep dive only when it helps the current teaching objective.

A good trigger is:

```text
student question
+
current TD relevance
+
3 to 5 minute explanation
```

Some topics may justify 5 to 10 minutes when the cohort is strong and CORE execution remains on schedule.

The default rule remains:

```text
CORE execution
>
deep dive
```

## 7. Common note contract

Every note contains:

```text
Purpose
Student CORE boundary
Instructor mental model
Best teaching moment
Short explanation
Worked example
Common misconception
Stop point
Source discipline
Optional extension
```

This contract is intentional.

It prevents a deep dive from silently becoming a new student requirement.

## 8. Environment-sensitive material

Bloomberg notes are conceptual unless the current ESILV environment has been verified.

Do not assume current:

```text
access rights
fields
packages
connector configuration
rate limits
Terminal/Desktop API behavior
```

Use:

```text
observed or approved
not guessed
```

The MarketPulse fallback distinction remains:

```text
LIVE
or
APPROVED_SAMPLE
```

## 9. Relationship with R7.5

R7.3 provides reusable instructor notes.

R7.5 may later compose selected parts of these notes into:

```text
5 to 10 minute TD enrichment capsules
```

R7.5 must reference these notes rather than duplicate their full content.

## 10. Frozen CORE boundary

These notes do not modify:

```text
12 TD sequence
18-hour workload
checkpoint requirements
runtime commands
provider contracts
analytics formulas
snapshot contract
assessment rules
```

The instructor can know more than students are required to reproduce.

That is the purpose of this directory.
