# Legacy Course Documentation

## Purpose

This directory documents the relationship between the previous ESILV teaching repository:

```text
tawounfouet/intro_git_linux_bloomberg
```

and the current MarketPulse teaching repository:

```text
tawounfouet/esilv-marketpulse
```

The objective is not to reproduce the historical course.

The objective is to:

```text
understand what existed
+
identify what still has value
+
map useful content to the current curriculum
+
protect the 18-hour CORE from overload
```

## Historical source

The historical repository contains extensive material on:

```text
Linux
Unix
Git local
Git remote
Git internals
SSH / SCP
cloud
Bloomberg
financial data
deployment
quantitative finance
```

It is treated as:

```text
legacy teaching reference
```

not as the current course contract.

## Current course contract

The current guided path remains the 12-TD MarketPulse sequence:

```text
TD01  Bootstrap + Linux
TD02  Python + CSV / JSON
TD03  Git Local Workflow
TD04  Branches + Merge
TD05  Remote Branch + Pull Request
TD06  Code Review
TD07  Data Normalization + Comparison
TD08  Yahoo Finance
TD09  Bloomberg Introduction
TD10  Bloomberg Provider
TD11  Dash Dashboard
TD12  Integration + Release
```

Reference:

```text
docs/06_TD_SEQUENCE_AND_LEARNING_PATH.md
```

## Documentation set

### 01 - Previous course repository analysis

```text
01_PREVIOUS_COURSE_REPOSITORY_ANALYSIS.md
```

Purpose:

```text
What was in the historical course?
How deep was it?
What were its strengths?
Where did overload or environmental risk appear?
How does it compare with MarketPulse?
```

This document provides the complete historical analysis.

### 02 - Legacy to MarketPulse content mapping

```text
02_LEGACY_TO_MARKETPULSE_CONTENT_MAPPING.md
```

Purpose:

```text
For each historical topic,
what should happen to it now?
```

The decision taxonomy is:

```text
CORE
OPTIONAL
TEACHER_REFERENCE
DROP
```

### 03 - Optional advanced content backlog

```text
03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
```

Purpose:

```text
Transform OPTIONAL legacy content
into a structured advanced-learning backlog.
```

Domains include:

```text
Linux Advanced
Git Advanced
Remote Linux
Bloomberg Advanced
Dash Advanced
Deployment Advanced
```

This backlog does not change checkpoint requirements.

### 04 - Legacy content operationalization roadmap

```text
04_LEGACY_CONTENT_OPERATIONALIZATION_ROADMAP.md
```

Purpose:

```text
Prevent post-freeze divergence.
Define the R7 execution order.
Turn analysis and backlog decisions into operational teaching assets.
```

This is now the canonical execution roadmap for the remaining Legacy stream.

### 05 - Final migration registry

```text
05_LEGACY_FINAL_MIGRATION_REGISTRY.md
```

Purpose:

```text
Assign one final operational destination
to every significant Legacy topic.
```

The registry is the traceability bridge between classification and execution.

### 06 - CORE / OPTIONAL / ADVANCED taxonomy impact study

```text
06_CORE_OPTIONAL_ADVANCED_TAXONOMY_IMPACT_STUDY.md
```

Purpose:

```text
Map every lab and repository change required
before introducing student-facing ADVANCED sections.
```

It freezes the impact scope before R7.4 implementation.

### 07 - R7.4 advanced qualification and closure

```text
07_R7_4_ADVANCED_QUALIFICATION_AND_CLOSURE.md
```

Purpose:

```text
Record the final R7.4 qualification,
active READY_TO_TEACH links,
PENDING_EXTERNAL gates,
and CORE/checkpoint isolation proof.
```

### Instructor deep-dive reference

```text
../instructor/01_LEGACY_DEEP_DIVE_REFERENCE.md
```

Operational deep-dive index:

```text
../instructor/deep-dives/README.md
```

TD enrichment capsules:

```text
../instructor/02_TD_ENRICHMENT_CAPSULES.md
```

Purpose:

```text
Preserve conceptual depth for instructors
without turning every deep concept into a student requirement.
```

It covers areas such as:

```text
Unix philosophy
Linux context
Git object model
HEAD and refs
merge vs rebase
Gitflow
Bloomberg Terminal
BDP / BDS / BDH
Request / Response
Subscription
B-PIPE
xbbg vs blpapi
```

## Relationship between the documents

```text
Historical repository
        |
        v
01 - ANALYSIS
What existed?
        |
        v
02 - MAPPING
What do we do with it?
        |
        +--------------------------+
        |                          |
        v                          v
CORE / DROP                   OPTIONAL / TEACHER_REFERENCE
                                   |
                     +-------------+-------------+
                     |                           |
                     v                           v
03 - OPTIONAL BACKLOG       INSTRUCTOR DEEP DIVE
advanced student work       deeper teacher knowledge
          \                       /
           \                     /
            +---------+----------+
                      |
                      v
              04 - R7 ROADMAP
              operationalization
```

## Decision taxonomy

### CORE

```text
mandatory
+
observable
+
timeboxed
+
part of the common 18-hour path
```

### OPTIONAL

```text
valuable advanced practice
+
not required for common completion
```

### TEACHER_REFERENCE

```text
knowledge useful to instructors
+
not a student deliverable
```

### DROP

```text
do not migrate into the common path
```

Important:

```text
DROP
!=
technically useless
```

It means only:

```text
not appropriate for the current common curriculum
```

## Main migration principle

The current design should preserve:

```text
historical depth
without
historical overload
```

The guiding relationship is:

```text
legacy course
=
bank of depth

MarketPulse
=
common guided path

diagnostic
=
cohort calibration

advanced backlog
=
optional practice

instructor reference
=
teacher depth
```

## What must not happen

Do not:

```text
copy the entire old course into MarketPulse
expand a 90-minute TD to fit legacy material
make optional content necessary for checkpoints
require a personal cloud payment method
make LIVE Bloomberg access mandatory for completion
reintroduce advanced quant finance into the guided CORE
copy historical third-party assets without checking reuse rights
use historical assessment weighting as the current contract
```

## What may be reused

Useful concepts may be:

```text
rewritten
simplified
recontextualized
adapted to MarketPulse
moved to optional material
moved to instructor references
```

Examples:

```text
Git staging mental model
Git branch graphs
conflict-resolution concepts
Unix composition
permissions context
SSH concepts
Bloomberg BDP / BDS / BDH context
request / response vs subscription
xbbg vs blpapi comparison
```

## Public repository note

The historical repository is private.

MarketPulse is public.

Therefore, historical assets must not be bulk-copied into MarketPulse.

Before reusing:

```text
images
PDFs
logos
diagrams
external screenshots
```

verify:

```text
source
license
reuse rights
```

Prefer:

```text
rewritten explanations
new diagrams
official sources
independently licensed assets
```

## Current status

```text
01 Previous course analysis          DONE
02 Legacy to MarketPulse mapping     DONE
03 Optional advanced backlog         DONE as backlog design
Instructor deep-dive reference       DONE as consolidated reference
04 Legacy operationalization roadmap ACTIVE
05 Final migration registry          ACTIVE
06 Taxonomy impact study             DONE
07 R7.4 qualification closure        DONE
```

The analysis and classification stream is complete.

The teaching operationalization stream is not yet complete.

The distinction is:

```text
analysis complete
!=
all useful Legacy content ready to teach
```

## Frozen CORE reference

The common MarketPulse CORE is frozen through R6.

Release decision:

```text
TEACHING BASELINE READY
WITH EXTERNAL PRE-CLASS CHECKS
```

Canonical release reference:

```text
docs/16_TEACHING_BASELINE_RELEASE.md
```

Legacy operationalization must preserve that baseline.

## Next Legacy phase

R1-R6 have frozen the common MarketPulse CORE.

The remaining Legacy work is now governed exclusively by:

```text
docs/legacy/04_LEGACY_CONTENT_OPERATIONALIZATION_ROADMAP.md
```

The current roadmap state is maintained in:

```text
docs/legacy/04_LEGACY_CONTENT_OPERATIONALIZATION_ROADMAP.md
```

R7.1 and R7.2 are now complete.

R7.3 is now complete.

R7.4 is now complete.

R7.5 is now complete.

Instructor enrichment state:

```text
10 deep dives
11 TD enrichment capsules
```

Current P1 state:

```text
7 READY_TO_TEACH
5 PENDING_EXTERNAL
0 ambiguous
```

The current execution target is:

```text
R7.6 - Advanced-track packaging
```

The routing source for R7.3 and R7.4 is:

```text
docs/legacy/05_LEGACY_FINAL_MIGRATION_REGISTRY.md
```

Do not create new Legacy-derived teaching material outside that roadmap.
