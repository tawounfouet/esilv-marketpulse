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

Status:

```text
DONE
```

Decision:

```text
03_final_pull_request.png
=
a meaningful late-stage PR from TD09-TD12
+
attributable to the student
```

It does not have to be the single team-level final release PR.

Completed actions:

- `docs/04_CHECKPOINTS_AND_EVIDENCE.md` now states the rule explicitly;
- TD12 tells students not to manufacture duplicate release PRs;
- the team integration PR may be authored by one integration lead;
- other students may use their own meaningful late-stage PR from TD09-TD12;
- individual Git traceability remains mandatory.

Acceptance criteria:

```text
[x] no requirement that every student authors one team final PR
[x] every student can show attributable late-stage PR evidence
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
DONE
```

Implemented remediation:

- added an explicit CORE definition of done;
- planned approximately 80 minutes of required work plus 10 minutes of buffer;
- retained MarketPulse context, team fork, TEAM.md, collaborators and common environment in CORE;
- retained `pwd`, `ls`, `cd`, `cat`, `head` and `grep` in CORE;
- retained Python and Git version checks and starter execution in CORE;
- moved observation counting, recursive search, extended `find` and Git exploration to OPTIONAL;
- removed Git identity setup from the required TD01 path;
- added the explicit approximately 10-minute environment blocker rule;
- added guidance against starting heavyweight local environment installation during the common TD;
- preserved the rule that formal Git workflow starts later.

Acceptance criteria:

```text
[x] CORE is planned within 80 minutes plus a 10-minute buffer
[x] environment fallback rule is visible
[x] optional shell work is clearly labelled
```

### R2.2 TD02 - Python + CSV / JSON

Status:

```text
DONE
```

Implemented remediation:

- added an explicit CORE definition of done;
- planned approximately 80 minutes of required work plus 10 minutes of buffer;
- retained JSON dictionaries, CSV DictReader, filtering and numeric conversion in CORE;
- retained first close, last close and one reusable market-summary function in CORE;
- kept loops and conditions only where they explain the existing filtering logic;
- moved first/last date, positive-volume counting, min/max close, slicing and formatting exercises to OPTIONAL;
- preserved the explicit rule that no return calculation belongs in TD02;
- added a concrete TD02 -> TD03 handoff using the real working Python changes;
- instructed students not to create unnecessary branches, Pull Requests or commits during TD02;
- made the first TD03 commit eligible to represent the useful TD02 work.

Acceptance criteria:

```text
[x] no return calculation in TD02
[x] meaningful code change exists for TD03
[x] optional exercises do not block completion
```

### R2.3 TD03 - Git Local Workflow

Status:

```text
DONE
```

Implemented remediation:

- added an explicit CORE definition of done;
- planned approximately 80 minutes of required work plus 10 minutes of buffer;
- made the real TD02 working changes the primary Git exercise;
- kept `git status`, `git diff`, `git add`, `git diff --staged`, `git commit`, `git log` and `git show` in CORE;
- moved temporary tracked/untracked work, multi-file staging, graph exploration, author filtering and `git ls-files` to OPTIONAL;
- moved Git identity verification into TD03 where commits actually begin;
- kept direct local commits on `main` only as a temporary pedagogical exception;
- kept remote push and Pull Requests outside TD03;
- added a fallback for the case where TD02 work was already committed without encouraging meaningless commits.

Acceptance criteria:

```text
[x] first meaningful commit can represent TD02 work
[x] each student can explain working tree vs staging vs commit
[x] no remote Git is required
```

### R2.4 TD04 - Branches + Merge

Status:

```text
DONE
```

Implemented remediation:

- added an explicit CORE definition of done;
- planned approximately 80 minutes of required work plus 10 minutes of buffer and Checkpoint A capture;
- kept one small feature branch, one meaningful branch commit, branch comparison, merge and Git graph inspection in CORE;
- preserved fast-forward merge as a valid outcome;
- kept merge-conflict understanding in CORE;
- moved the complete manufactured conflict execution and conflict-demo file lifecycle to instructor demo / OPTIONAL;
- removed mandatory manual conflict resolution from CORE;
- kept Checkpoint A fully supported through the canonical evidence contract;
- prepared the TD04 ending for the separate TD04 -> TD05 team-baseline handoff lot.

Acceptance criteria:

```text
[x] branch + merge is completed by every student
[x] conflict understanding is introduced
[x] conflict execution is not mandatory
[x] Checkpoint A remains fully supported
```

### R2.5 Add TD04 -> TD05 team baseline handoff

Status:

```text
DONE
```

Implemented control:

```text
local learning histories
        |
        v
Checkpoint A capture
        |
        v
archive/td04-local safety branch
        |
        v
validated team baseline
        |
        v
origin/main
        |
        v
all students align
        |
        v
TD05 collaborative branches
```

Completed actions:

- added the handoff warning at the end of TD04;
- added a complete Team Baseline Gate at the start of TD05;
- documented the same control in `docs/03_GITHUB_TEAM_WORKFLOW.md`;
- made the instructor or designated integrator responsible for selecting and publishing the baseline;
- require `origin` verification before publication;
- require clean working trees before synchronization;
- preserve each student's previous local history with `archive/td04-local`;
- allow controlled alignment to `origin/main` only after the safety checks;
- document a fresh Codespace / fresh clone alternative;
- explicitly state that divergent-main merge/rebase training is outside this handoff.

Acceptance criteria:

```text
[x] all students start TD05 from the same team main
[x] no hidden divergent-main assumption remains
[x] origin points to team repository
```

### R2.6 TD05 - Remote Branch + Pull Request

Status:

```text
DONE
```

Implemented remediation:

- changed the displayed lab title to `TD05 - Remote Branch + Pull Request`;
- kept the existing filename to avoid unnecessary path churn;
- made the Team Baseline Gate the explicit starting condition;
- planned approximately 80 minutes of required work plus 10 minutes of buffer;
- kept `origin` verification, feature branch, one coherent change, commit, push, remote branch, Pull Request and Files changed inspection in CORE;
- added a team contribution-coordination step to reduce duplicate PRs implementing the same feature;
- moved a second commit on the same PR to OPTIONAL;
- moved `git branch -vv`, remote-branch enumeration and extra range inspection to OPTIONAL;
- removed instructor-repository `upstream` configuration from CORE;
- made the required end state an open, attributable PR targeting team `main`;
- explicitly preserved the PR for TD06 review.

Acceptance criteria:

```text
[x] each student can push a branch
[x] each student can open a PR
[x] PR targets team main
[x] usable PRs remain open for TD06
```

### R2.7 TD06 - Code Review

Status:

```text
DONE
```

Implemented remediation:

- added an explicit CORE definition of done;
- planned approximately 80 minutes of required work plus 10 minutes of buffer;
- kept real review of another student's TD05 Pull Request in CORE;
- kept Files changed inspection and meaningful technical feedback in CORE;
- clarified Comment, Request changes and Approve as different outcomes;
- made correction conditional on a real issue;
- removed any requirement to manufacture a review defect or fix commit;
- kept same-branch PR update only when justified;
- kept approval, merge and local `main` synchronization in CORE;
- moved extended review-history and Git-history exploration to OPTIONAL;
- preserved Checkpoint B code-review evidence through the canonical evidence contract.

Acceptance criteria:

```text
[x] each student reviews another student's PR
[x] review contains meaningful technical content
[x] corrections are evidence-based, not manufactured
[x] team main is synchronized after merge
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
DONE
```

Implemented remediation:

- introduced `src/analytics.py` as the TD07 repository evolution;
- defined `index_by_date(...)`, `align_series(...)`, `calculate_period_return(...)`, `calculate_base_100(...)` and `calculate_relative_performance(...)` as CORE functions;
- made common-date alignment explicit before period comparison;
- kept local CSV numeric normalization outside provider-neutral analytics;
- required `analytics.py` to contain no provider-specific identifier;
- moved daily returns, best/worst daily return and extra comparison tables to OPTIONAL;
- updated the functional contract, use-case document, learning path and root README so daily returns are no longer a mandatory CORE feature;
- reduced repeated Git theory to a standard workflow handoff;
- made reviewed TD07 analytics on team `main` an explicit prerequisite for TD08.

Acceptance criteria:

```text
[x] analytics are reusable outside main.py
[x] no provider-specific identifier exists inside analytics.py
[x] base 100 starts at 100
[x] relative performance uses instrument minus benchmark
[x] daily returns are optional
```

### R3.2 TD08 - Yahoo Finance

Status:

```text
DONE
```

Implemented remediation:

- added an explicit CORE definition of done;
- planned approximately 80 minutes of required work plus 10 minutes of review, remote variation and Checkpoint B buffer;
- retained `yfinance` installation and `requirements.txt` recording in CORE;
- reduced provider exploration to one AAPL retrieval and only the returned structure needed for normalization;
- introduced `src/providers/yahoo_provider.py` as the Yahoo acquisition boundary;
- kept canonical row normalization in the provider;
- froze `AAPL -> AAPL` and `SP500 -> ^GSPC` for TD08 CORE;
- required `SP500` to remain the canonical benchmark ticker;
- required TD07 `align_series()` and analytics functions to run unchanged;
- reduced repeated Git instruction to the established workflow handoff;
- moved invalid-symbol experiment, alternate instrument, provider selector, configuration refactor and advanced error handling to OPTIONAL;
- added `docs/09_YAHOO_FINANCE_INSTRUCTOR_REFERENCE.md` with a known-good teaching shape, canonical row example and outage fallback;
- preserved honest Checkpoint B evidence rules and prohibited fabricated Yahoo output.

Acceptance criteria:

```text
[x] Yahoo provider returns canonical rows
[x] SP500 remains canonical ticker
[x] ^GSPC remains provider-specific
[x] TD07 analytics run unchanged
[x] Checkpoint B can be completed
```

### R3.3 Resolve Checkpoint B market-pair requirement

Status:

```text
DONE
```

Implemented decision:

```text
Checkpoint B mandatory pair
=
AAPL + S&P 500
```

Completed actions:

- removed "ability to change the selected market pair" from mandatory Checkpoint B skills;
- removed mandatory ticker-change validation from Checkpoint B oral questions;
- kept alternate coherent market pairs as OPTIONAL or oral extension;
- updated TD08 to state explicitly that alternate pair selection is not required for Checkpoint B;
- updated the learning path so TD08 mandatory scope is the common CORE pair;
- reconciled the transverse review with the resolved decision.

Acceptance criteria:

```text
[x] Checkpoint B mandatory scope matches what TD08 actually teaches
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
DONE
```

Prepared assets:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
```

Implemented controls:

- added an instructor-approved fallback fixture for the Bloomberg stage;
- reused illustrative MarketPulse starter values rather than claiming certified Bloomberg observations;
- labelled the fixture explicitly as `APPROVED_SAMPLE`;
- made `is_live_bloomberg_output = false` explicit in the sample metadata;
- used teaching wrapper keys rather than inventing Bloomberg field mnemonics;
- documented the wrapper-to-canonical reference mapping;
- added a known expected canonical normalized result;
- froze `AAPL US Equity -> AAPL` and `SPX Index -> SP500` for the teaching path;
- documented `LIVE` vs `APPROVED_SAMPLE` semantics;
- stated explicitly that approved-sample execution does not prove live connectivity;
- linked TD09 and TD10 to the fallback assets;
- kept all fallback assets credential-free.

Acceptance criteria:

```text
[x] TD09 can succeed without live Bloomberg
[x] TD10 can continue provider-boundary work without fabricating live evidence
[x] students can distinguish LIVE from APPROVED_SAMPLE mode
```

### R4.2 TD09 - Bloomberg Introduction

Status:

```text
DONE
```

Implemented remediation:

- added an explicit CORE definition of done;
- planned approximately 80 minutes of required work plus 10 minutes of review and environment buffer;
- made `docs/BLOOMBERG_FIELD_MAPPING.md` the single TD09 deliverable;
- required one explicit session mode: `LIVE` or `APPROVED_SAMPLE`;
- removed live Bloomberg connectivity as a TD09 completion condition;
- kept `AAPL -> AAPL US Equity` and `SP500 -> SPX Index` in CORE;
- required one instrument input and one benchmark input to be inspected;
- required LIVE mappings to use only actually observed fields;
- required APPROVED_SAMPLE mappings to label fallback keys as teaching wrapper keys;
- preserved canonical AAPL and SP500 tickers;
- added an explicit TD09 -> TD10 handoff section to the student mapping document;
- deferred Bloomberg provider implementation to TD10;
- moved extended live exploration and additional identifiers to OPTIONAL;
- preserved the no-credentials rule and canonical evidence separation.

Acceptance criteria:

```text
[x] mapping document reflects observed or approved fields
[x] access mode is documented honestly
[x] no credentials are committed
```

### R4.3 TD10 - Bloomberg Provider

Status:

```text
DONE
```

Implemented remediation:

- added an explicit CORE definition of done;
- planned approximately 80 minutes of required work plus 10 minutes of review and environment buffer;
- made the reviewed TD09 mapping the required source for provider normalization;
- created `docs/11_BLOOMBERG_PROVIDER_SCAFFOLD.md`;
- defined a clear LIVE raw acquisition boundary without inventing a Bloomberg connector;
- provided an exact APPROVED_SAMPLE loader and normalization path;
- required `AAPL US Equity -> AAPL` and `SPX Index -> SP500`;
- required canonical rows before analytics;
- required reuse of `align_series()`, period return, base 100 and relative performance unchanged;
- removed daily returns from TD10 CORE;
- removed generic provider selection from CORE;
- moved YAML settings updates, richer metadata and extended error handling to OPTIONAL;
- required terminal output to expose `LIVE` or `APPROVED_SAMPLE` honestly;
- preserved the standard branch / PR / review workflow.

Acceptance criteria:

```text
[x] Bloomberg-specific logic remains inside provider boundary
[x] analytics are unchanged
[x] canonical output matches Yahoo/CSV structure
[x] LIVE vs APPROVED_SAMPLE mode is visible and honest
```

### R4.4 Add reusable application snapshot contract

Status:

```text
DONE
```

Canonical contract:

```text
docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md
```

Frozen CORE boundary:

```python
build_market_snapshot(...)
```

Frozen result shape:

```python
{
    "provider": ...,
    "lookback": ...,
    "interval": ...,
    "instrument": {
        "ticker": ...,
        "name": ...,
    },
    "benchmark": {
        "ticker": ...,
        "name": ...,
    },
    "instrument_return": ...,
    "benchmark_return": ...,
    "relative_performance": ...,
    "instrument_base_100": ...,
    "benchmark_base_100": ...,
}
```

Implemented controls:

- kept the frozen flat CORE architecture with no new application package;
- placed the CORE snapshot builder contract in `src/main.py`;
- required import-safe `main.py` using the existing `if __name__ == "__main__"` guard;
- defined canonical instrument and benchmark metadata;
- defined numeric return and relative-performance values;
- defined base-100 list contracts;
- required an honest provider label, including LIVE vs APPROVED_SAMPLE distinction;
- required terminal presentation to consume the snapshot;
- required Dash presentation to consume the same snapshot;
- prohibited provider-specific calls from `src/dashboard.py`;
- prohibited duplicate return and base-100 formulas in `src/dashboard.py`;
- updated TD10, TD11, target architecture, learning path and transverse review to reference the shared contract.

Purpose:

```text
providers
   |
   v
analytics
   |
   v
snapshot
   |
   +----------+
   |          |
   v          v
terminal     Dash
```

Acceptance criteria:

```text
[x] terminal and Dash use one frozen application result contract
[x] dashboard does not call Bloomberg/Yahoo directly
[x] dashboard does not own analytical formulas
```

### R4.5 TD11 - Dash Dashboard

Status:

```text
DONE
```

Implemented remediation:

- added an explicit CORE definition of done;
- planned approximately 80 minutes of required work plus 10 minutes of browser, debugging and review buffer;
- froze `src/dashboard.py` as the only CORE dashboard entry point;
- froze `python src/dashboard.py` as the dashboard command;
- kept `dash` and `plotly` as direct recorded dependencies;
- required the dashboard to consume `build_market_snapshot(...)`;
- required provider, instrument, benchmark, lookback and interval to be visible;
- required instrument return, benchmark return and relative performance;
- required one base-100 chart with both series;
- prohibited provider-specific calls from `dashboard.py`;
- prohibited return, base-100 and relative-performance formulas from `dashboard.py`;
- required terminal and dashboard consistency checks;
- moved daily-return chart, volume chart, selectors, callbacks, advanced layout and styling polish to OPTIONAL;
- removed repeated evidence details and kept the canonical Checkpoint C reference.

Acceptance criteria:

```text
[x] python src/dashboard.py is the frozen CORE command
[x] no provider logic belongs in dashboard.py
[x] no analytical formula belongs in dashboard.py
[x] no hard-coded return values are required
[x] both base-100 series are visible
```

### R4.6 TD12 - Integration + Release

Status:

```text
DONE
```

Implemented remediation:

- added an explicit CORE definition of done;
- planned approximately 80 minutes of required release work plus 10 minutes of Checkpoint C and troubleshooting buffer;
- removed the long architecture recap from CORE;
- made final provider or access-mode honesty the first release check;
- kept repository cleanup, direct dependency verification and README validation in CORE;
- froze `python src/main.py` and `python src/dashboard.py` as release commands;
- required a fresh or clean reproducibility test;
- kept one final integration PR, review and merge workflow;
- required the merged `main` version to be run again;
- reduced Checkpoint C content to exact filenames, a short capture checklist and a link to `docs/04_CHECKPOINTS_AND_EVIDENCE.md`;
- preserved the attributable late-stage PR rule from LOT-R1.6;
- moved advanced deployment, Docker and GitHub Actions to OPTIONAL / REFERENCE;
- added explicit guidance not to add CI, security, release or license badges unless those contracts actually exist;
- updated the root README as the instructor repository landing page with course badges, architecture, runtime, learning path, checkpoints and security guidance.

Acceptance criteria:

```text
[x] fresh or clean run uses documented commands
[x] final provider or access mode is documented honestly
[x] final dashboard command is frozen
[x] final or late-stage PR evidence remains attributable
[x] Checkpoint C can be completed without invented work
```

## 9. R5 - Final consistency and teaching readiness

### Objective

Validate the entire sequence after all remediation changes.

### Priority

```text
P0 closure
```

### R5.1 Path scan

Status:

```text
DONE
```

Verify that all file paths are coherent.

Search for stale CORE paths such as:

```text
docs/td/
src/marketpulse/
src/dashboard/app.py
```

Repository-wide scan result:

```text
docs/td/
=
no active path usage
the only occurrence is this stale-path scan specification

src/marketpulse/
=
no CORE requirement
remaining occurrences are intentional:
- remediation history / exclusion language
- optional professional evolution in docs/05

src/dashboard/app.py
=
no CORE requirement
remaining occurrences are intentional:
- remediation scan / historical exclusion language
- explicit "Do not create" example in TD11

legacy instructor repository name without the `esilv-` prefix
=
no active occurrence outside this scan description

canonical instructor repository
=
tawounfouet/esilv-marketpulse

canonical student repository pattern
=
<owner>/esilv-marketpulse-gXX-tYY

canonical lab directory
=
docs/labs/
```

The current repository tree contains:

```text
docs/labs/README.md
docs/labs/TD01_BOOTSTRAP_LINUX.md
...
docs/labs/TD12_INTEGRATION_AND_RELEASE.md
```

The progressive CORE Python structure remains:

```text
TD01-TD06
src/main.py

TD07
+ src/analytics.py

TD08
+ src/providers/yahoo_provider.py

TD10
+ src/providers/bloomberg_provider.py

TD11
+ src/dashboard.py
```

The instructor starter repository currently contains only the Python files that must exist at the current starter stage. Later CORE files are introduced by the corresponding labs.

Acceptance criteria:

```text
[x] docs/labs/ is used
[x] no stale CORE Python structure remains
```

R5.1 conclusion:

```text
PASS
```

### R5.2 Runtime-command scan

Status:

```text
DONE
```

Verify every occurrence of:

```text
python src/main.py
python src/dashboard.py
```

Repository-wide scan result:

```text
canonical terminal command
=
python src/main.py

canonical dashboard command
=
python src/dashboard.py

dashboard availability
=
introduced in TD11
validated again in TD12
```

The scan found the canonical terminal command consistently across:

```text
README.md
student onboarding
TD01-TD12 where execution is relevant
target repository structure
learning path
checkpoint evidence
dependency documentation
legacy / advanced references where the CORE command is restated
```

The dashboard command is consistently documented in:

```text
README.md
TD11
TD12
target repository structure
learning path
transverse review
dependency documentation
advanced backlog
```

Contradictory MarketPulse runtime commands were explicitly searched for and were not found:

```text
python3 src/main.py
python3 src/dashboard.py
python main.py
python dashboard.py
python app.py
python src/dashboard/app.py
streamlit run
flask run
dash run
uvicorn
```

The diagnostic questionnaire contains examples such as:

```text
python3 app.py
```

inside standalone Bash questions.

These are diagnostic examples and are not MarketPulse runtime instructions.

Occurrences of:

```text
python -m pip ...
```

are dependency installation or package-inspection commands, not application entry points.

TD12 uses the final release commands:

```bash
python src/main.py
python src/dashboard.py
```

Acceptance criteria:

```text
[x] no contradictory dashboard command
[x] TD12 uses final commands
```

R5.2 conclusion:

```text
PASS
```

### R5.3 Checkpoint scan

Status:

```text
DONE
```

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

Repository-wide scan result:

```text
Checkpoint A
=
exact filename set preserved in docs/04 and TD04
individual preparation references in TD03 / TD05 are consistent

Checkpoint B
=
exact filename set preserved in docs/04 and TD08
individual preparation references in TD05 / TD06 / TD07 are consistent

Checkpoint C
=
exact required filename set preserved in docs/04 and TD12
TD10 prepares 01_final_market_data.png
TD11 prepares 02_dash_dashboard.png
03_final_pull_request.png keeps the late-stage attributable-PR rule
05_advanced_deployment.png remains optional
```

Canonical evidence authority:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

The canonical document explicitly declares itself the single source of truth for:

```text
checkpoint timing
required filenames
optional filenames
screenshot meaning
individual evidence
live validation
assessment guidance
security
```

The supporting evidence index:

```text
evidence/README.md
```

does not redefine the filename contract and points back to `docs/04_CHECKPOINTS_AND_EVIDENCE.md`.

Checkpoint directories are consistently documented as:

```text
evidence/checkpoint-a/<github-username>/
evidence/checkpoint-b/<github-username>/
evidence/checkpoint-c/<github-username>/
```

A repository-wide `.png` reference scan found no alternate checkpoint filename competing with the canonical names.

The Yahoo logo asset referenced by the root README is unrelated to checkpoint evidence and does not affect this contract.

Acceptance criteria:

```text
[x] exact filenames match everywhere
[x] optional file remains optional
[x] docs/04 is canonical
```

R5.3 conclusion:

```text
PASS
```

### R5.4 Terminology scan

Status:

```text
DONE
```

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

Repository-wide scan result:

```text
instrument
=
primary financial series

benchmark
=
comparison market series

provider
=
data-source boundary

lookback
=
historical comparison window

interval
=
observation frequency

canonical ticker
=
provider-neutral MarketPulse identifier

provider identifier
=
provider-specific identifier or symbol

relative performance
=
instrument return - benchmark return

presentation unit
=
percentage points
```

The terminology scan confirmed these canonical mappings:

```text
AAPL
=
canonical instrument ticker

SP500
=
canonical benchmark ticker

Yahoo
AAPL -> AAPL
SP500 -> ^GSPC

Bloomberg teaching path
AAPL -> AAPL US Equity
SP500 -> SPX Index
```

The repository intentionally uses a few explanatory equivalents:

```text
historical window / period scope
=
lookback

frequency
=
interval

1 month
=
presentation form of 1mo

Daily
=
presentation form of 1d

Yahoo symbol
=
Yahoo-specific provider identifier

Bloomberg identifier
=
Bloomberg-specific provider identifier
```

These equivalences are now explicitly documented in:

```text
docs/00_MARKETPULSE_FUNCTIONAL_CONTRACT.md
```

Orthographic convention:

```text
base 100
=
concept / noun form

base-100
=
adjectival form such as base-100 chart or base-100 normalization
```

Formula scan result:

```text
relative performance
=
instrument_return - benchmark_return

no benchmark-minus-instrument formula found

unit
=
percentage points

no basis-points alternative found
```

The use-case document was aligned from:

```text
Final provider Bloomberg
```

to:

```text
Professional provider Bloomberg
```

because Bloomberg is the professional provider stage, while TD12 and Checkpoint C must still describe the actual authorized final provider or access mode honestly.

Same-period / same-frequency invariant:

```text
same period
+
same frequency
=
same lookback
+
same interval
+
compatible common observation dates
```

Acceptance criteria:

```text
[x] no contradictory vocabulary
[x] same-period and same-frequency rule is preserved
```

R5.4 conclusion:

```text
PASS
```

### R5.5 Timing scan

Status:

```text
DONE
```

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

Repository-wide timing matrix:

| TD | CORE end | 80-90 minute block | Checkpoint capture |
|---|---:|---|---|
| TD01 | 80 min | Buffer, support, optional exploration | N/A |
| TD02 | 80 min | Buffer, optional exercises | N/A |
| TD03 | 80 min | Buffer, optional exercises | N/A |
| TD04 | 80 min | Checkpoint A capture, buffer, optional conflict practice | Included |
| TD05 | 80 min | Buffer, troubleshooting, optional | N/A |
| TD06 | 80 min | Buffer, optional review practice | N/A |
| TD07 | 80 min | Buffer, review, optional analytics | N/A |
| TD08 | 80 min | Review, Checkpoint B capture, troubleshooting | Included |
| TD09 | 80 min | Review, troubleshooting, optional | N/A |
| TD10 | 80 min | Review, troubleshooting, optional | N/A |
| TD11 | 80 min | Review, troubleshooting, optional polish | N/A |
| TD12 | 80 min | Checkpoint C capture, buffer | Included |

Detailed scan result:

```text
TD01
78-80 = CORE definition of done
80-90 = buffer / support / optional exploration

TD02
75-80 = final run + CORE validation
80-90 = buffer / optional exercises

TD03
72-80 = run MarketPulse + CORE validation
80-90 = buffer / optional exercises

TD04
75-80 = CORE validation
80-90 = Checkpoint A capture / buffer / optional practice

TD05
74-80 = inspect Files changed + leave PR open
80-90 = buffer / troubleshooting / optional

TD06
75-80 = CORE validation
80-90 = buffer / optional practice

TD07
72-80 = validation + standard Git handoff
80-90 = buffer / review / optional

TD08
78-80 = CORE definition of done
80-90 = review / Checkpoint B / troubleshooting

TD09
72-80 = validation + standard Git handoff
80-90 = review / troubleshooting / optional

TD10
74-80 = CORE validation + standard Git handoff
80-90 = review / troubleshooting / optional

TD11
78-80 = CORE validation
80-90 = review / troubleshooting / optional

TD12
75-80 = final run from merged main
80-90 = Checkpoint C capture / buffer
```

Optional-section ordering scan:

```text
all 12 labs place their dedicated OPTIONAL sections
after the mandatory CORE material

no optional exercise is required
to satisfy the CORE definition of done
```

Checkpoint timing:

```text
Checkpoint A
=
TD04 final 10-minute block

Checkpoint B
=
TD08 final 10-minute block

Checkpoint C
=
TD12 final 10-minute block
```

The scan also confirms that the 90-minute structure is not being used as:

```text
90 minutes mandatory work
+
extra checkpoint capture
```

Instead, checkpoint-ending labs reserve their final block for capture, support and validation.

Acceptance criteria:

```text
[x] no CORE requires optional challenges to finish
[x] checkpoint capture time is included where relevant
```

R5.5 conclusion:

```text
PASS
```

### R5.6 Dependency continuity scan

Status:

```text
DONE
```

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

Repository-wide dependency scan result:

```text
TD01 -> TD02
TD01 produces:
- accessible team repository
- TEAM.md
- Linux terminal
- working python src/main.py
TD02 explicitly requires those items

TD02 -> TD03
TD02 produces:
- meaningful Python changes
- working local MarketPulse
TD03 explicitly uses those real changes for status / diff / staging / commit

TD03 -> TD04
TD03 produces:
- local Git mental model
- meaningful commits
TD04 explicitly requires status / diff / add / commit / log understanding

TD04 -> TD05
TD04 produces:
- branch + merge understanding
- Checkpoint A evidence
TD05 starts with the explicit Team Baseline Gate before remote feature work

TD05 -> TD06
TD05 produces:
- pushed feature branch
- open Pull Request
TD06 explicitly requires open PRs and performs review / correction / approval / merge

TD06 -> TD07
TD06 leaves:
- reviewed changes merged to team main
- synchronized local main
TD07 starts from synchronized main and reuses the established Git workflow

TD07 -> TD08
TD07 produces:
- src/analytics.py
- align_series()
- calculate_period_return()
- calculate_base_100()
- calculate_relative_performance()
TD08 explicitly requires reviewed TD07 analytics merged to team main

TD08 -> TD09
TD08 produces:
- src/providers/yahoo_provider.py
- provider boundary concept
- canonical remote rows
- Checkpoint B evidence
TD09 explicitly requires the provider boundary and canonical-row model to be understood

TD09 -> TD10
TD09 produces:
- docs/BLOOMBERG_FIELD_MAPPING.md
- documented LIVE or APPROVED_SAMPLE mode
- AAPL / SP500 Bloomberg identifier mapping
TD10 explicitly requires the reviewed mapping and documented mode

TD10 -> TD11
TD10 produces:
- src/providers/bloomberg_provider.py
- shared analytics reuse
- build_market_snapshot(...) in src/main.py
- import-safe main.py
TD11 explicitly requires that snapshot boundary before dashboard work

TD11 -> TD12
TD11 produces:
- src/dashboard.py
- Dash + Plotly direct dependencies
- terminal / dashboard shared-snapshot presentation
TD12 explicitly requires both runtime commands and build_market_snapshot(...) to work
```

One real continuity gap was found during the scan:

```text
previous state
=
TD11 required build_market_snapshot(...)
but TD10 did not explicitly require students to implement it

remediation
=
TD10 now creates build_market_snapshot(...) in src/main.py
and makes main() consume it before TD11 begins
```

The TD10 timing remains inside its previously validated 80-minute CORE by using the existing 65-74 minute integration slot for the snapshot refactor and terminal integration.

The learning-path document now names this explicitly as:

```text
TD10 -> TD11 application snapshot handoff
```

No other unexplained cross-TD refactor was found.

Acceptance criteria:

```text
[x] every file exists before the next TD needs it
[x] every function dependency is introduced earlier
[x] no unexplained refactor is required between labs
```

R5.6 conclusion:

```text
PASS
```

### R5.7 Security scan

Status:

```text
DONE
```

Verify that no lab asks students to expose:

- passwords;
- tokens;
- SSH private keys;
- Bloomberg credentials;
- cloud credentials;
- billing information.

Repository-wide review confirmed:

```text
repository-level security reminders
=
README.md
CONTRIBUTING.md
TEAM_TEMPLATE.md
docs/03_GITHUB_TEAM_WORKFLOW.md

evidence security
=
docs/04_CHECKPOINTS_AND_EVIDENCE.md
evidence/README.md

provider security
=
TD08 requires no committed credential
TD09 forbids sensitive session information in Git or screenshots
TD10 forbids credentials in code and output
APPROVED_SAMPLE requires no Bloomberg credential
```

Versioned configuration review:

```text
config/settings.yml
=
human-readable application configuration only
no credential or billing value is required
```

The repository ignore rules already exclude local environment files.

Optional advanced remote-work documentation also states that:

```text
personal cloud payment is not required
private keys must remain secret
secrets must not be transferred for demonstrations
secrets must not be committed in service configuration
```

A repository code-search review for common credential and private-key signatures found no committed credential candidate.

Acceptance criteria:

```text
[x] security reminders remain at relevant provider/evidence steps
[x] no credentials are needed in versioned config
```

R5.7 conclusion:

```text
PASS
```

### R5.8 Character convention scan

Status:

```text
DONE
```

Repository convention:

```text
Do not use the em dash character.
Use the simple hyphen instead.
```

Repository-wide character scan result:

```text
em dash character (—) = 0 occurrence
en dash character (–) = 0 occurrence
```

No remediation was required because the current default branch already respects the documented character convention.

Acceptance criteria:

```text
[x] zero em dash occurrences
```

R5.8 conclusion:

```text
PASS
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
| R1 | Cross-cutting contracts | P0 | DONE |
| R2 | TD01-TD06 | P0/P1 | DONE |
| R3 | TD07-TD08 | P0 | DONE |
| R4 | TD09-TD12 | P0 | DONE |
| R5 | Final validation | P0 closure | IN PROGRESS |

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
