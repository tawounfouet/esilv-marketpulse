# TD Remediation Plan

## 1. Purpose

This document defines the remediation plan for the 12 MarketPulse practical labs after the transverse review documented in:

```text
docs/07_TD_TRANSVERSE_REVIEW_AND_REBALANCING.md
```

The objective is not to redesign the teaching sequence.

The objective is to make the existing 18-hour path:

```text
coherent
+
realistic in 90-minute units
+
technically continuous
+
easy to execute
+
easy to assess
+
maintainable
```

The remediation plan preserves:

- the 12 TD sequence;
- the MarketPulse fil rouge;
- the three checkpoints;
- the official 18-hour volume;
- the instrument / benchmark comparison model;
- the CSV -> Yahoo -> Bloomberg -> Dash progression;
- the Git progression from local work to collaborative review.

## 2. Remediation principles

All remediation work follows these principles.

### 2.1 Preserve the teaching sequence

The sequence remains:

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

### 2.2 Reduce CORE scope before removing concepts

When a TD is overloaded, the preferred action is:

```text
KEEP IN CORE
or
MOVE TO OPTIONAL
or
MOVE TO INSTRUCTOR DEMO
```

before considering full removal.

### 2.3 One source of truth per cross-cutting contract

The following documents remain authoritative:

```text
docs/00_MARKETPULSE_FUNCTIONAL_CONTRACT.md
docs/04_CHECKPOINTS_AND_EVIDENCE.md
docs/05_TARGET_REPOSITORY_STRUCTURE.md
docs/06_TD_SEQUENCE_AND_LEARNING_PATH.md
docs/07_TD_TRANSVERSE_REVIEW_AND_REBALANCING.md
```

The lab files should reference these documents rather than duplicate large sections.

### 2.4 CORE first

Each TD must clearly distinguish:

```text
CORE
OPTIONAL
INSTRUCTOR DEMO
REFERENCE
```

The CORE must be achievable in approximately 90 minutes under normal classroom conditions.

### 2.5 Stable technical handoffs

A TD must not assume a file, function, branch state or architecture that the previous TD did not create or explicitly prepare.

### 2.6 No hidden complexity

The CORE should not introduce advanced packaging, CI/CD, Docker, Kubernetes, automated testing frameworks or advanced quantitative finance.

## 3. Global remediation roadmap

The remediation is divided into five lots.

```text
R1 - Cross-cutting contracts
R2 - TD01 to TD06
R3 - TD07 to TD08
R4 - TD09 to TD12
R5 - Final consistency and teaching readiness
```

Dependency flow:

```text
R1
 |
 +--> R2
 |
 +--> R3
 |
 +--> R4
        |
        v
       R5
```

R1 must be completed first.

R2, R3 and R4 can then be executed in sequence.

R5 closes the remediation line.

## 4. Priority model

### P0 - Blocking

Must be corrected before the sequence is frozen for teaching.

### P1 - Important

Strongly recommended for teaching quality and maintainability.

### P2 - Quality improvement

Can be completed after P0 and P1 without blocking the teaching path.

## 5. R1 - Cross-cutting contracts

### Objective

Freeze the technical and pedagogical contracts used by all labs.

### Priority

```text
P0
```

### R1.1 Freeze the CORE repository architecture

Status:

```text
DONE
```

Implemented in commit associated with LOT-R1.1.

Current problem:

Different documents described different final Python structures.

Decision:

Use the following CORE architecture:

```text
src/
├── main.py
├── analytics.py
├── dashboard.py
└── providers/
    ├── __init__.py
    ├── yahoo_provider.py
    └── bloomberg_provider.py
```

Evolution:

```text
TD01-TD06
src/main.py

TD07
src/main.py
src/analytics.py

TD08
src/main.py
src/analytics.py
src/providers/yahoo_provider.py

TD10
src/providers/bloomberg_provider.py

TD11
src/dashboard.py
```

Required actions:

- update `docs/05_TARGET_REPOSITORY_STRUCTURE.md`;
- update TD07-TD12 paths;
- remove conflicting `src/marketpulse/` CORE expectations;
- keep formal package architecture as optional future evolution only.

Acceptance criteria:

```text
[x] one CORE structure is documented
[x] every affected TD uses the same structure
[x] no TD requires src/marketpulse/ for CORE
[x] no TD uses src/dashboard/app.py for CORE
```

### R1.2 Freeze runtime commands

Status:

```text
DONE
```

CORE commands:

```bash
python src/main.py
python src/dashboard.py
```

The terminal command is valid from the starter onward.

The dashboard command is introduced in TD11 and reused unchanged in TD12.

Completed actions:

- canonical commands documented in the root README;
- canonical commands documented in the learning path;
- TD11 uses the single-file dashboard entry point;
- TD12 fresh-run and final validation use the same commands;
- the transverse review now reflects the resolved runtime contract.

Acceptance criteria:

```text
[x] terminal command is unique and stable
[x] dashboard command is unique and stable
[x] TD12 fresh-run instructions use the same commands
```

### R1.3 Freeze configuration status

Status:

```text
DONE
```

Decision:

```text
config/settings.yml
=
human-readable configuration contract
```

YAML parsing is not mandatory in the CORE.

Completed actions:

- starter comments in `src/main.py` now describe `settings.yml` as a reference contract;
- the root README no longer promises future YAML wiring;
- `config/settings.yml` documents its CORE role directly;
- TD10 states that provider configuration may be documented without being parsed;
- PyYAML remains outside the CORE unless introduced as an explicit optional extension;
- the transverse review reflects the resolved configuration contract.

Acceptance criteria:

```text
[x] no unfulfilled promise that YAML will definitely be parsed
[x] no mandatory PyYAML dependency
[x] settings.yml remains useful documentation
```

### R1.4 Freeze pedagogical wave terminology

Status:

```text
DONE
```

Official waves:

```text
Wave 1 - TD01-TD02
Wave 2 - TD03-TD06
Wave 3 - TD07-TD08
Wave 4 - TD09-TD12
```

Checkpoint phases:

```text
Checkpoint Phase A - TD01-TD04
Checkpoint Phase B - TD05-TD08
Checkpoint Phase C - TD09-TD12
```

Completed actions:

- TD02 now closes Wave 1 explicitly;
- TD04 now closes Checkpoint Phase A rather than incorrectly closing a wave;
- TD06 now closes Wave 2 explicitly;
- TD08 now distinguishes Wave 3 from Checkpoint Phase B;
- TD12 now recaps four pedagogical waves and three checkpoint phases separately;
- the lab index and learning-path documents use the same terminology;
- the transverse review reflects the resolved terminology contract.

Acceptance criteria:

```text
[x] four waves everywhere
[x] checkpoint groupings are called phases, not waves
```

### R1.5 Freeze checkpoint source of truth

Status:

```text
DONE
```

Canonical file:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

Completed actions:

- docs/04 now explicitly declares itself the single source of truth;
- exact screenshot meaning, README rules, live validation and assessment guidance remain centralized there;
- TD04, TD08 and TD12 now keep only a short checkpoint summary, capture checklist and canonical reference;
- evidence/README.md no longer maintains a parallel filename specification;
- duplicated checkpoint README templates and detailed screenshot definitions were removed from the labs;
- checkpoint security reminders remain visible at the point of capture.

Acceptance criteria:

```text
[x] evidence requirements are defined canonically in docs/04
[x] labs reference docs/04
[x] no parallel evidence contract remains in evidence/README.md
[x] no contradictory checkpoint rules are intentionally maintained
```

### R1.6 Clarify Checkpoint C Pull Request evidence

Decision:

```text
03_final_pull_request.png
=
a final or late-stage PR attributable to the student
```

It does not have to be the single team-level final release PR.

Required actions:

- clarify `docs/04_CHECKPOINTS_AND_EVIDENCE.md`;
- update TD12;
- preserve individual traceability.

Acceptance criteria:

```text
[ ] no requirement that every student authors one team final PR
[ ] every student can show attributable late-stage PR evidence
```

## 6. R2 - Rebalance TD01 to TD06

### Objective

Make the foundations and Git collaboration sequence realistic in six hours of official Wave 2 plus the three-hour Wave 1 foundation.

### Priority

```text
P0 + P1
```

### R2.1 TD01 - Bootstrap + Linux

Status:

```text
KEEP WITH TIMEBOX
```

CORE:

- MarketPulse context;
- team fork;
- TEAM.md;
- collaborators;
- common environment;
- `pwd`;
- `ls`;
- `cd`;
- `cat`;
- `head`;
- `grep`;
- Python version;
- Git version;
- run starter.

Move to OPTIONAL:

- recursive grep;
- extended `find`;
- extra Git exploration;
- extended shell challenges.

Add operational rule:

```text
Individual environment blocker > approximately 10 minutes
-> pair temporarily with a teammate
-> continue the TD
```

Acceptance criteria:

```text
[ ] CORE fits 90 minutes
[ ] environment fallback rule is visible
[ ] optional shell work is clearly labelled
```

### R2.2 TD02 - Python + CSV / JSON

Status:

```text
SLIGHTLY SIMPLIFY
```

CORE:

- inspect starter;
- JSON dictionaries;
- CSV DictReader;
- numeric conversion;
- filter by ticker;
- first close;
- last close;
- reusable summary;
- final run.

Move to OPTIONAL:

- positive-volume count;
- min/max close;
- slicing exercises;
- additional formatting exercises.

Important handoff:

TD02 should finish with meaningful Python changes that may still be uncommitted.

TD03 should use those changes as real Git material.

Acceptance criteria:

```text
[ ] no return calculation in TD02
[ ] meaningful code change exists for TD03
[ ] optional exercises do not block completion
```

### R2.3 TD03 - Git Local Workflow

Status:

```text
KEEP, REDUCE DRILLS
```

CORE:

```text
git status
git diff
git add
git diff --staged
git commit
git log
git show
```

Primary exercise:

Version the useful TD02 change.

Move to OPTIONAL:

- temporary tracked/untracked file exercise;
- multi-file staging drill;
- author filtering;
- `git ls-files`.

Acceptance criteria:

```text
[ ] first meaningful commit can represent TD02 work
[ ] each student can explain working tree vs staging vs commit
[ ] no remote Git required yet
```

### R2.4 TD04 - Branches + Merge

Status:

```text
MAJOR REBALANCING
```

CORE:

- create branch;
- implement one small feature;
- commit;
- compare branch;
- merge;
- inspect graph;
- prepare Checkpoint A.

Move to INSTRUCTOR DEMO or OPTIONAL:

- manufactured merge conflict;
- manual conflict resolution;
- conflict-demo file lifecycle.

Checkpoint A remains after TD04.

Acceptance criteria:

```text
[ ] branch + merge is completed by every student
[ ] conflict understanding is introduced
[ ] conflict execution is not mandatory
[ ] Checkpoint A still fully supported
```

### R2.5 Add TD04 -> TD05 team baseline handoff

Status:

```text
NEW P0 CONTROL
```

Problem:

Students may have different local histories after TD03-TD04.

Required handoff:

```text
local learning histories
        |
        v
validated team baseline
        |
        v
all students synchronize
        |
        v
TD05 collaborative branches
```

Required actions:

- define an instructor-controlled synchronization procedure;
- add it at the end of TD04 or start of TD05;
- make clear that the exercise is not an advanced Git-history lesson.

Acceptance criteria:

```text
[ ] all students start TD05 from the same team main
[ ] no hidden divergent-main assumption remains
[ ] origin points to team repository
```

### R2.6 TD05 - Remote Branch + Pull Request

Status:

```text
REFRAME
```

Recommended displayed title:

```text
TD05 - Remote Branch + Pull Request
```

The filename can remain unchanged if desired.

CORE:

- verify `origin`;
- synchronize team baseline;
- create feature branch;
- implement one small change;
- commit;
- push;
- inspect remote branch;
- open PR;
- inspect source / target / Files changed.

Move to OPTIONAL:

- second commit on the same PR;
- extra remote-branch commands.

End state:

```text
PR remains open for TD06
```

Acceptance criteria:

```text
[ ] each student can push a branch
[ ] each student can open a PR
[ ] PR targets team main
[ ] usable PRs remain open for TD06
```

### R2.7 TD06 - Code Review

Status:

```text
KEEP WITH RULE CHANGE
```

CORE:

- inspect another student's PR;
- inspect Files changed;
- leave meaningful feedback;
- use Comment / Request changes / Approve appropriately;
- merge when ready;
- pull updated `main`.

Rule change:

```text
A correction is required only if a real issue exists.
```

Do not force artificial review fixes.

Acceptance criteria:

```text
[ ] each student reviews another student's PR
[ ] review contains meaningful technical content
[ ] corrections are evidence-based, not manufactured
[ ] team main is synchronized after merge
```

## 7. R3 - Rebalance TD07 to TD08

### Objective

Create a stable analytics layer and integrate the first remote provider in three hours.

### Priority

```text
P0
```

### R3.1 TD07 - Create analytics contract

Status:

```text
MAJOR REBALANCING
```

Introduce:

```text
src/analytics.py
```

CORE functions:

```python
index_by_date(...)
align_series(...)
calculate_period_return(...)
calculate_base_100(...)
calculate_relative_performance(...)
```

CORE concepts:

- numeric normalization;
- common dates;
- period return;
- base 100;
- relative performance.

Move to OPTIONAL:

- daily returns;
- best daily return;
- worst daily return;
- extra comparison tables.

Update functional wording if needed so daily return is no longer a mandatory final CORE feature.

Acceptance criteria:

```text
[ ] analytics are reusable outside main.py
[ ] no provider-specific identifier exists inside analytics.py
[ ] base 100 starts at 100
[ ] relative performance uses instrument minus benchmark
[ ] daily returns are optional
```

### R3.2 TD08 - Yahoo Finance

Status:

```text
CRITICAL REMEDIATION
```

CORE:

- install `yfinance`;
- record dependency;
- retrieve AAPL;
- understand returned structure;
- create `src/providers/yahoo_provider.py`;
- normalize to canonical rows;
- map `SP500 -> ^GSPC`;
- retrieve instrument and benchmark;
- align common dates;
- reuse TD07 analytics;
- run MarketPulse;
- standard Git workflow;
- prepare Checkpoint B evidence.

Move to OPTIONAL:

- invalid-symbol experiment;
- extra provider-error drills;
- alternate instrument;
- provider selector;
- configuration refactor.

Instructor preparation:

- known-good yfinance example;
- known-good expected canonical row;
- fallback explanation for temporary remote outage.

Acceptance criteria:

```text
[ ] Yahoo provider returns canonical rows
[ ] SP500 remains canonical ticker
[ ] ^GSPC remains provider-specific
[ ] TD07 analytics run unchanged
[ ] Checkpoint B can be completed
```

### R3.3 Resolve Checkpoint B market-pair requirement

Current gap:

Checkpoint B currently mentions ability to change the selected market pair.

Recommended decision:

Remove this from mandatory CORE validation.

Keep alternate market pairs as:

```text
OPTIONAL
or
oral extension
```

Acceptance criteria:

```text
[ ] Checkpoint B mandatory scope matches what TD08 actually teaches
```

## 8. R4 - Rebalance TD09 to TD12

### Objective

Keep professional data integration, dashboard construction and release achievable in six hours.

### Priority

```text
P0
```

### R4.1 Prepare instructor Bloomberg fallback assets

Status:

```text
P0 PRE-CLASS REQUIREMENT
```

Prepare:

```text
1. known-good Bloomberg sample
2. reference field mapping
3. expected canonical normalized result
4. documented live vs sample distinction
```

The sample must be usable without exposing credentials.

Acceptance criteria:

```text
[ ] TD09 can succeed without live Bloomberg
[ ] TD10 can succeed without fabricating provider evidence
[ ] students can distinguish live from approved sample mode
```

### R4.2 TD09 - Bloomberg Introduction

Status:

```text
SIMPLIFY
```

CORE:

- Bloomberg role;
- canonical vs provider identifier;
- `AAPL US Equity`;
- `SPX Index`;
- inspect live or approved sample;
- identify returned fields;
- create `docs/BLOOMBERG_FIELD_MAPPING.md`;
- preserve canonical tickers.

Move to OPTIONAL:

- extended live exploration;
- extra identifiers;
- additional provider investigations.

Acceptance criteria:

```text
[ ] mapping document reflects observed or approved fields
[ ] access mode is documented honestly
[ ] no credentials are committed
```

### R4.3 TD10 - Bloomberg Provider

Status:

```text
CRITICAL REMEDIATION
```

CORE:

- use TD09 mapping;
- create `src/providers/bloomberg_provider.py`;
- isolate raw acquisition boundary;
- normalize Bloomberg data;
- preserve canonical tickers;
- obtain instrument and benchmark rows;
- reuse alignment;
- reuse analytics;
- validate terminal output;
- standard Git workflow.

Move to OPTIONAL:

- YAML provider configuration;
- generic provider framework;
- advanced provider metadata;
- extended error architecture;
- dynamic provider selector.

Acceptance criteria:

```text
[ ] Bloomberg-specific logic remains inside provider boundary
[ ] analytics are unchanged
[ ] canonical output matches Yahoo/CSV structure
[ ] live vs sample mode is visible and honest
```

### R4.4 Add reusable application snapshot contract

Status:

```text
NEW P0 CONTROL
```

Before TD11, define one application-level result contract.

Conceptual function:

```python
build_market_snapshot(...)
```

Conceptual output:

```python
{
    "provider": ...,
    "lookback": ...,
    "interval": ...,
    "instrument": ...,
    "benchmark": ...,
    "instrument_return": ...,
    "benchmark_return": ...,
    "relative_performance": ...,
    "instrument_base_100": ...,
    "benchmark_base_100": ...,
}
```

Purpose:

```text
terminal
   |
   +------+
          |
dashboard +--> same application result
```

Acceptance criteria:

```text
[ ] terminal and Dash do not recompute separate business logic
[ ] dashboard does not call Bloomberg/Yahoo directly
```

### R4.5 TD11 - Dash Dashboard

Status:

```text
CRITICAL REMEDIATION
```

Use:

```text
src/dashboard.py
```

CORE:

- install `dash` and `plotly`;
- record direct dependencies;
- create minimal app;
- consume shared MarketPulse snapshot;
- show provider;
- show instrument;
- show benchmark;
- show lookback;
- show interval;
- show instrument return;
- show benchmark return;
- show relative performance;
- show one base-100 comparison chart.

Move to OPTIONAL:

- daily-return chart;
- volume chart;
- callbacks;
- selectors;
- advanced layout;
- styling polish.

Acceptance criteria:

```text
[ ] python src/dashboard.py works
[ ] no provider logic exists in dashboard.py
[ ] no hard-coded return values
[ ] both base-100 series are visible
```

### R4.6 TD12 - Integration + Release

Status:

```text
CRITICAL REMEDIATION
```

CORE only:

- confirm final provider;
- remove temporary artefacts;
- verify requirements;
- verify README;
- fresh clone or clean setup;
- run terminal path;
- run dashboard path;
- final integration PR;
- review;
- merge;
- final Checkpoint C capture.

Move to REFERENCE / OPTIONAL:

- long architecture recap;
- repeated Git theory;
- full evidence philosophy;
- advanced deployment.

Use `docs/04_CHECKPOINTS_AND_EVIDENCE.md` for full evidence rules.

Acceptance criteria:

```text
[ ] fresh run succeeds using documented commands
[ ] final provider is documented honestly
[ ] final dashboard runs
[ ] final or late-stage PR evidence is attributable
[ ] Checkpoint C can be completed without invented work
```

## 9. R5 - Final consistency and teaching readiness

### Objective

Validate the entire sequence after all remediation changes.

### Priority

```text
P0 closure
```

### R5.1 Path scan

Verify that all file paths are coherent.

Search for stale CORE paths such as:

```text
docs/td/
src/marketpulse/
src/dashboard/app.py
```

Acceptance criteria:

```text
[ ] docs/labs/ is used
[ ] no stale CORE Python structure remains
```

### R5.2 Runtime-command scan

Verify every occurrence of:

```text
python src/main.py
python src/dashboard.py
```

Acceptance criteria:

```text
[ ] no contradictory dashboard command
[ ] TD12 uses final commands
```

### R5.3 Checkpoint scan

Verify:

```text
Checkpoint A
01_terminal_python.png
02_git_status_log.png
03_branch_merge.png

Checkpoint B
01_pull_request.png
02_code_review.png
03_yahoo_market_data.png
04_instrument_benchmark.png

Checkpoint C
01_final_market_data.png
02_dash_dashboard.png
03_final_pull_request.png
04_reproducible_run.png
05_advanced_deployment.png optional
```

Acceptance criteria:

```text
[ ] exact filenames match everywhere
[ ] optional file remains optional
[ ] docs/04 is canonical
```

### R5.4 Terminology scan

Verify consistency for:

```text
instrument
benchmark
provider
lookback
interval
canonical ticker
provider identifier
base 100
relative performance
percentage points
```

Acceptance criteria:

```text
[ ] no contradictory vocabulary
[ ] same-period and same-frequency rule is preserved
```

### R5.5 Timing scan

Every TD must have:

```text
CORE <= approximately 80 minutes planned work
+
approximately 10 minutes buffer / validation
```

The buffer is necessary for:

- student questions;
- environment variance;
- Git mistakes;
- instructor explanations.

Acceptance criteria:

```text
[ ] no CORE requires optional challenges to finish
[ ] checkpoint capture time is included where relevant
```

### R5.6 Dependency continuity scan

Validate the chain:

```text
TD01 environment
    |
TD02 Python change
    |
TD03 first commit
    |
TD04 branch + merge
    |
team baseline
    |
TD05 remote PR
    |
TD06 review
    |
TD07 analytics.py
    |
TD08 yahoo_provider.py
    |
TD09 Bloomberg mapping
    |
TD10 bloomberg_provider.py
    |
shared market snapshot
    |
TD11 dashboard.py
    |
TD12 release
```

Acceptance criteria:

```text
[ ] every file exists before the next TD needs it
[ ] every function dependency is introduced earlier
[ ] no unexplained refactor is required between labs
```

### R5.7 Security scan

Verify that no lab asks students to expose:

- passwords;
- tokens;
- SSH private keys;
- Bloomberg credentials;
- cloud credentials;
- billing information.

Acceptance criteria:

```text
[ ] security reminders remain at relevant provider/evidence steps
[ ] no credentials are needed in versioned config
```

### R5.8 Character convention scan

Repository convention:

```text
Do not use the em dash character.
Use the simple hyphen instead.
```

Acceptance criteria:

```text
[ ] zero em dash occurrences
```

## 10. Documentation updates by file

### docs/00_MARKETPULSE_FUNCTIONAL_CONTRACT.md

Actions:

- make daily returns optional;
- keep period return, base 100 and relative performance as CORE;
- preserve common 1mo / 1d contract.

### docs/04_CHECKPOINTS_AND_EVIDENCE.md

Actions:

- remain canonical source;
- remove mandatory alternate-pair requirement if retained there;
- clarify late-stage PR rule for Checkpoint C.

### docs/05_TARGET_REPOSITORY_STRUCTURE.md

Actions:

- replace formal package structure as CORE;
- document simplified CORE structure;
- move `src/marketpulse/` to optional professional evolution.

### docs/06_TD_SEQUENCE_AND_LEARNING_PATH.md

Actions:

- keep four official waves;
- reflect reduced TD07 daily-return scope;
- reflect simplified TD11 entry point;
- clarify checkpoint phases separately.

### docs/07_TD_TRANSVERSE_REVIEW_AND_REBALANCING.md

Status:

```text
REFERENCE
```

No large rewrite required unless remediation decisions change.

### docs/labs/README.md

Actions:

- rename heading to `MarketPulse Lab Index`;
- keep TD filenames;
- optionally add CORE / OPTIONAL convention.

### README.md

Actions:

- update final structure references;
- clarify `settings.yml` role;
- keep starter command stable;
- later add dashboard run command when appropriate.

### src/main.py

Actions:

- remove promise that YAML will necessarily be wired later;
- preserve starter simplicity.

### requirements.txt

Actions:

- TD01-TD07 remain minimal;
- yfinance introduced at TD08;
- dash and plotly introduced at TD11;
- Bloomberg-specific dependency only if validated by teaching environment.

## 11. Remediation execution order

Recommended implementation order:

```text
LOT-R1.1  Freeze CORE repository structure
LOT-R1.2  Freeze runtime commands
LOT-R1.3  Freeze config/settings.yml status
LOT-R1.4  Correct wave / checkpoint-phase terminology
LOT-R1.5  Centralize checkpoint contract
LOT-R1.6  Clarify Checkpoint C PR evidence

LOT-R2.1  Rebalance TD01
LOT-R2.2  Rebalance TD02
LOT-R2.3  Rebalance TD03
LOT-R2.4  Rebalance TD04
LOT-R2.5  Add team-baseline handoff
LOT-R2.6  Rebalance TD05
LOT-R2.7  Rebalance TD06

LOT-R3.1  Rebalance TD07 and introduce analytics.py
LOT-R3.2  Rebalance TD08
LOT-R3.3  Align Checkpoint B scope

LOT-R4.1  Prepare Bloomberg fallback contract
LOT-R4.2  Rebalance TD09
LOT-R4.3  Rebalance TD10
LOT-R4.4  Define shared market snapshot
LOT-R4.5  Rebalance TD11
LOT-R4.6  Rebalance TD12

LOT-R5.1  Paths
LOT-R5.2  Commands
LOT-R5.3  Checkpoints
LOT-R5.4  Terminology
LOT-R5.5  Timing
LOT-R5.6  Dependency continuity
LOT-R5.7  Security
LOT-R5.8  Character convention
```

## 12. Remediation status board

Initial status:

| Lot | Scope | Priority | Status |
|---|---|---|---|
| R1 | Cross-cutting contracts | P0 | IN PROGRESS |
| R2 | TD01-TD06 | P0/P1 | NOT STARTED |
| R3 | TD07-TD08 | P0 | NOT STARTED |
| R4 | TD09-TD12 | P0 | NOT STARTED |
| R5 | Final validation | P0 closure | NOT STARTED |

Each lot should move through:

```text
NOT STARTED
    |
    v
IN PROGRESS
    |
    v
REVIEW
    |
    v
DONE
```

## 13. Global Definition of Done

The remediation is complete only when all of the following are true.

### Pedagogy

```text
[ ] all 12 TDs remain
[ ] each TD has explicit CORE scope
[ ] optional work is clearly separated
[ ] every CORE is realistic in 90 minutes
[ ] difficulty rises progressively
```

### Technical continuity

```text
[ ] one CORE Python structure exists
[ ] one terminal command exists
[ ] one dashboard command exists
[ ] TD04 -> TD05 team handoff is explicit
[ ] TD07 analytics are reusable
[ ] TD08 Yahoo feeds canonical rows
[ ] TD10 Bloomberg feeds canonical rows
[ ] TD11 reuses shared results
[ ] TD12 validates rather than redesigns
```

### Checkpoints

```text
[ ] Checkpoint A derives from TD01-TD04
[ ] Checkpoint B derives from TD05-TD08
[ ] Checkpoint C derives from TD09-TD12
[ ] docs/04 is the single evidence source of truth
[ ] every screenshot filename is consistent
[ ] individual contribution rules are realistic
```

### Maintainability

```text
[ ] repeated Git theory is reduced after TD06
[ ] checkpoint duplication is reduced
[ ] no stale file paths remain
[ ] no contradictory architecture remains
[ ] no unfulfilled YAML promise remains
```

### Safety

```text
[ ] no credentials are required in the repository
[ ] Bloomberg fallback is safe
[ ] screenshots do not require secret exposure
```

### Repository convention

```text
[ ] zero em dash occurrences
```

## 14. Expected final state

After remediation, the teaching path should be:

```text
TD01
environment works
   |
   v
TD02
Python manipulates local data
   |
   v
TD03
real changes become commits
   |
   v
TD04
features become branches
   |
   v
TEAM BASELINE
   |
   v
TD05
branches become Pull Requests
   |
   v
TD06
Pull Requests become reviewed integrations
   |
   v
TD07
comparison logic becomes reusable analytics
   |
   v
TD08
Yahoo feeds the same analytics
   |
   v
TD09
Bloomberg concepts and fields are understood
   |
   v
TD10
Bloomberg feeds the same analytics
   |
   v
TD11
shared results become a Dash interface
   |
   v
TD12
the integrated application becomes reproducible
```

The final objective remains unchanged:

```text
18 hours
+
12 coherent labs
+
3 evidence checkpoints
+
1 progressive MarketPulse application
```
