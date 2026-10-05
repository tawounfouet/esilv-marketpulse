# TD Transverse Review and Rebalancing

## 1. Purpose

This document reviews the complete 18-hour MarketPulse practical sequence after the creation of TD01 through TD12.

The review focuses on seven questions:

1. Is the sequence globally coherent?
2. Can each TD realistically fit into 1 hour 30 minutes?
3. Are dependencies between TDs explicit and technically viable?
4. Are concepts repeated more than necessary?
5. Does the pedagogical difficulty increase progressively?
6. Do the three checkpoints assess skills that were actually prepared in the labs?
7. Does the repository produced by one TD remain a viable starting point for the next TD?

This document is a teaching-design review.

It does not replace:

- the functional contract;
- the checkpoint contract;
- the learning-path document;
- the student-facing lab instructions.

## 2. Overall conclusion

The global learning path is strong and coherent.

The business progression is easy to understand:

```text
local files
    |
    v
Python manipulation
    |
    v
Git history
    |
    v
branches
    |
    v
GitHub collaboration
    |
    v
comparison model
    |
    v
Yahoo Finance
    |
    v
Bloomberg
    |
    v
Dash
    |
    v
reproducible release
```

The three checkpoint positions are also logically placed:

```text
TD04 -> Checkpoint A
TD08 -> Checkpoint B
TD12 -> Checkpoint C
```

However, the review identifies five major issues that should be corrected before the labs are considered frozen:

```text
1. several TDs contain more work than a realistic 90-minute session;
2. the local Git work from TD02-TD04 does not yet have a fully explicit transition to the shared remote workflow in TD05;
3. the repository architecture described in docs/05 and the paths used by TD08-TD12 are not fully aligned;
4. TD12 uses a three-wave recap while docs/06 correctly defines four official pedagogical waves;
5. Checkpoint C individual Pull Request evidence must not depend on every student being the author of one team-level final integration PR.
```

The recommended strategy is therefore:

```text
keep the 12-TD sequence
+
keep the three checkpoints
+
reduce CORE scope inside overloaded TDs
+
move secondary work to OPTIONAL
+
freeze one executable repository architecture
+
make cross-TD handoffs explicit
```

No additional TD is required.

## 3. Audit basis

The review covers:

- `docs/00_MARKETPULSE_FUNCTIONAL_CONTRACT.md`;
- `docs/04_CHECKPOINTS_AND_EVIDENCE.md`;
- `docs/05_TARGET_REPOSITORY_STRUCTURE.md`;
- `docs/06_TD_SEQUENCE_AND_LEARNING_PATH.md`;
- `docs/labs/README.md`;
- all files from `TD01` to `TD12`;
- the current starter `src/main.py`;
- `requirements.txt`;
- `config/settings.yml`;
- `CONTRIBUTING.md`.

The review assumes the fixed common contract:

```text
1 instrument
+
1 benchmark
+
1 provider
+
1 month lookback
+
daily interval
+
performance comparison
```

## 4. Documentation-density indicator

Document length is not the same thing as teaching time.

However, it is a useful warning signal when a 90-minute lab contains many concepts, code blocks, exercises, Git operations and checkpoint activities.

Current student-facing lab size:

| TD | Approx. lines | Approx. words | Main parts | 90-minute risk |
|---|---:|---:|---:|---|
| TD01 | 683 | 1,698 | 13 | Medium |
| TD02 | 805 | 1,936 | 16 | Medium |
| TD03 | 916 | 2,201 | 18 | Medium |
| TD04 | 1,029 | 2,481 | 19 | High |
| TD05 | 1,059 | 2,444 | 20 | High |
| TD06 | 850 | 2,435 | 21 | Medium |
| TD07 | 1,040 | 2,424 | 20 | High |
| TD08 | 1,203 | 3,022 | 28 | Critical |
| TD09 | 841 | 2,628 | 22 | High |
| TD10 | 1,062 | 2,772 | 28 | Critical |
| TD11 | 1,095 | 2,613 | 29 | Critical |
| TD12 | 1,206 | 3,144 | 33 | Critical |

The main conclusion is not that the files are too long by themselves.

The problem is that several later TDs combine:

```text
new concept
+
new code
+
new architecture
+
dependency installation
+
Git workflow
+
review
+
evidence preparation
```

inside one 90-minute block.

That is where rebalancing is required.

## 5. Global strengths to preserve

### 5.1 One stable business question

The same business question remains visible throughout the sequence:

> How is a financial instrument performing compared with its market benchmark?

This is a major strength.

The technical concepts are therefore introduced because MarketPulse needs them, not as disconnected exercises.

### 5.2 Progressive Git learning

The Git progression is pedagogically sound:

```text
inspect
    |
    v
commit
    |
    v
branch
    |
    v
push
    |
    v
Pull Request
    |
    v
review
    |
    v
merge
```

The sequence should be preserved.

### 5.3 Provider progression

The provider progression is also coherent:

```text
CSV / JSON
    |
    v
Yahoo Finance
    |
    v
Bloomberg
```

Each provider adds a reason to separate acquisition from analytics.

### 5.4 Checkpoint progression

The checkpoints assess increasingly complete evidence:

```text
Checkpoint A
environment + Python + local Git

Checkpoint B
collaboration + remote data + comparison

Checkpoint C
professional provider + dashboard + reproducibility
```

The weighting progression:

```text
25%
30%
45%
```

is coherent with the increasing integration difficulty.

### 5.5 Scope protection

The current documentation correctly keeps the following outside the mandatory CORE:

- automated test frameworks;
- Docker;
- GitHub Actions;
- Kubernetes;
- intraday market data;
- advanced quantitative finance.

This protection should remain.

## 6. Cross-TD dependency review

### TD01 -> TD02

Status:

```text
GOOD
```

TD01 prepares:

- repository access;
- Linux terminal;
- CSV and JSON inspection;
- Python execution.

TD02 immediately reuses these elements.

No major dependency gap exists.

### TD02 -> TD03

Status:

```text
PARTIAL
```

TD02 asks students to modify MarketPulse.

TD03 introduces the first real commit workflow.

This is logically useful because TD03 can version code created during TD02.

However, the handoff is not explicit enough.

Recommended clarification:

```text
TD02 ends with working but potentially uncommitted Python changes.

TD03 begins by inspecting those changes with:
git status
git diff

The first meaningful TD03 commit may capture the student's TD02 work.
```

This creates a stronger project narrative than inventing an unrelated modification only to demonstrate Git.

### TD03 -> TD04

Status:

```text
GOOD LOCALLY
```

Local commits naturally lead to feature branches and merge.

The main risk is time, not conceptual continuity.

### TD04 -> TD05

Status:

```text
CRITICAL HANDOFF GAP
```

TD03 and TD04 are intentionally local.

TD05 suddenly assumes a shared team repository becomes the collaborative source of truth.

If several students have independent local histories after TD03 and TD04, there is no explicit reconciliation step before remote collaboration begins.

This can produce:

- divergent local `main` branches;
- different TD02 implementations;
- uncertainty about which branch represents the team baseline;
- push rejections;
- unnecessary merge problems before Pull Requests are even introduced.

A canonical handoff must be added.

Recommended rule:

```text
At the end of TD04, each student has local evidence.

Before TD05 feature work begins, the team selects one validated team baseline.

TD05 starts by synchronizing every student to that baseline before new branches are created.
```

The exact synchronization procedure must remain simple and instructor-controlled.

Do not make history reconciliation itself a hidden advanced Git exercise.

### TD05 -> TD06

Status:

```text
GOOD
```

TD05 deliberately leaves Pull Requests open.

TD06 then uses those real Pull Requests for review.

This is one of the strongest handoffs in the sequence.

### TD06 -> TD07

Status:

```text
GOOD
```

By TD07, the collaboration workflow is established and can become routine rather than a new lesson.

Later TDs should therefore shorten repeated Git explanations and refer back to `CONTRIBUTING.md`.

### TD07 -> TD08

Status:

```text
CONCEPTUALLY GOOD
TECHNICALLY UNDER-SPECIFIED
```

TD07 creates the analytical contract that TD08 should reuse.

However, the exact location of reusable analytical functions is not frozen.

TD08 introduces `src/providers/yahoo_provider.py`, while TD07 may still leave all analytical functions inside `src/main.py`.

This works for small scripts but becomes fragile before Dash.

Decision required before the labs are frozen:

```text
TD07 must establish the canonical location of reusable analytics.
```

Recommended CORE structure is defined later in this document.

### TD08 -> TD09

Status:

```text
GOOD
```

Yahoo introduces provider-specific identifiers and normalization.

Bloomberg then extends exactly the same idea.

### TD09 -> TD10

Status:

```text
HIGH EXTERNAL DEPENDENCY
```

TD10 depends on information discovered during TD09:

- available Bloomberg access method;
- actual returned fields;
- date representation;
- identifier behaviour.

This dependency is legitimate, but the course must not depend entirely on live Bloomberg availability.

Required instructor preparation:

```text
a known-good approved Bloomberg sample
+
a completed reference field mapping
+
a validated fallback path
```

Students may create their own mapping during TD09, but the instructor must have a recovery artefact ready.

### TD10 -> TD11

Status:

```text
ARCHITECTURE GAP
```

TD11 requires Dash to reuse application results.

The current labs correctly say that provider logic should not be duplicated in the dashboard.

However, no single reusable application-level function is currently frozen as the source of dashboard data.

Before TD11, MarketPulse should expose something conceptually similar to:

```python
build_market_snapshot(...)
```

returning:

```text
provider metadata
instrument metadata
benchmark metadata
aligned series
period returns
relative performance
base-100 series
```

Then both terminal output and Dash can consume the same computed result.

### TD11 -> TD12

Status:

```text
GOOD CONCEPTUALLY
RUNTIME COMMAND MUST BE FROZEN
```

The final reproducibility test depends on one stable execution contract.

The repository must define exactly:

```text
how to run terminal mode
how to run dashboard mode
```

before TD12.

These commands must not still be changing during the release session.

## 7. Repository architecture and runtime contract

This finding has now been remediated by LOT-R1.1 and LOT-R1.2.

The 18-hour CORE uses one deliberately simple executable layout:

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

The two canonical runtime commands are:

```bash
python src/main.py
python src/dashboard.py
```

The terminal entry point is used from the starter onward.

The dashboard entry point is introduced in TD11 and is reused unchanged in TD12.

This decision avoids accidental Python packaging and import-path complexity during a beginner practical sequence.

Suggested responsibility:

```text
main.py
application orchestration + terminal output

analytics.py
alignment + period return + base 100 + relative performance

providers/
provider-specific acquisition + normalization

dashboard.py
Dash presentation using shared application results
```

A more formal Python package remains an optional professional evolution outside the mandatory CORE.

The CORE therefore prioritizes reliable execution and conceptual clarity over packaging sophistication.

## 8. Configuration contract

This finding has now been remediated by LOT-R1.3.

The repository keeps:

```text
config/settings.yml
```

as a human-readable configuration contract.

The 18-hour CORE does not require YAML parsing.

The starter code, README and TD10 now state this explicitly.

Students should not add PyYAML only because `settings.yml` exists.

If YAML parsing is introduced later, it must be presented as an explicit optional extension rather than an implicit CORE requirement.

## 9. Official waves vs checkpoint phases

This finding has now been remediated by LOT-R1.4.

The four pedagogical waves are:

```text
Wave 1 - TD01-TD02 - 3h
Wave 2 - TD03-TD06 - 6h
Wave 3 - TD07-TD08 - 3h
Wave 4 - TD09-TD12 - 6h
```

The assessment checkpoint phases are:

```text
Checkpoint Phase A - TD01-TD04
Checkpoint Phase B - TD05-TD08
Checkpoint Phase C - TD09-TD12
```

The two grouping systems now use distinct terminology throughout the active teaching documents.

A wave describes pedagogical sequencing.

A checkpoint phase describes the group of TDs whose evidence contributes to one assessment checkpoint.

## 10. Detailed workload review

### TD01 - Bootstrap + Linux

Current status:

```text
KEEP WITH TIMEBOX PROTECTION
```

Strengths:

- excellent introduction to MarketPulse;
- Linux commands are concrete;
- no premature Python modification;
- onboarding and project context are integrated.

Risk:

Team creation, fork setup, collaborator invitations and environment problems can consume much more than the planned time.

Rebalancing:

CORE:

- MarketPulse context;
- one team fork;
- TEAM.md;
- working terminal;
- `pwd`, `ls`, `cd`, `cat`, `head`, `grep`;
- Python and Git version;
- run MarketPulse.

OPTIONAL:

- recursive grep;
- file counting;
- extra Git exploration.

Operational rule:

```text
After approximately 10 minutes on an individual environment blocker,
the student temporarily pairs with a teammate and continues the lab.
```

Verdict:

```text
90 minutes feasible if environment escalation is controlled.
```

### TD02 - Python + CSV / JSON

Current status:

```text
KEEP, SLIGHTLY SIMPLIFY
```

Strengths:

- directly reuses starter files;
- good progression from data structures to functions;
- does not introduce pandas too early;
- correctly postpones returns.

Risk:

Too many recap and exercise sections for a first Python manipulation lab.

CORE:

- inspect existing program;
- JSON dictionary access;
- CSV `DictReader`;
- numeric conversion;
- filter by ticker;
- first and last close;
- reusable summary function;
- run final output.

OPTIONAL:

- positive-volume exercise;
- min/max close;
- slicing challenges;
- extended formatting work.

Recommended handoff to TD03:

```text
Do not require a final Git workflow in TD02.

Leave a meaningful working change that TD03 can inspect and commit.
```

Verdict:

```text
90 minutes feasible after reducing exercise pressure.
```

### TD03 - Git Local Workflow

Current status:

```text
KEEP, REDUCE SECONDARY EXERCISES
```

Strengths:

- good mental model;
- strong use of `git status`, `git diff`, staging and history;
- no premature remote complexity.

Main improvement:

Use the TD02 modification as the primary real change whenever possible.

This makes the sequence:

```text
TD02 creates useful Python work
TD03 learns how to version that real work
```

rather than inventing a new cosmetic change only for Git.

CORE:

- status;
- diff;
- add;
- staged diff;
- commit;
- log;
- show;
- clean working tree.

OPTIONAL / REFERENCE:

- tracked/untracked temporary-file exercise;
- two-file staging exercise;
- author filtering;
- `git ls-files`.

Verdict:

```text
90 minutes feasible with a narrower CORE.
```

### TD04 - Branches + Merge

Current status:

```text
TOO HEAVY
```

Current lab combines:

- branch mental model;
- feature implementation;
- commit;
- branch comparison;
- merge;
- branch deletion;
- merge conflict;
- conflict resolution;
- Checkpoint A;
- live validation;
- evidence security.

The merge-conflict exercise is educational but is not required by Checkpoint A.

Rebalancing:

CORE:

- create branch;
- implement one small feature;
- commit;
- compare branch;
- merge;
- inspect graph;
- prepare Checkpoint A.

INSTRUCTOR DEMO or OPTIONAL:

- manufactured conflict;
- manual conflict resolution;
- cleanup of conflict practice file.

Conflict concepts can still be explained in 5 minutes without requiring every team to manufacture one.

Verdict:

```text
Current version is unlikely to fit safely in 90 minutes.
Rebalanced version can fit.
```

### TD05 - Fork + Pull Request

Current status:

```text
KEEP CONCEPT, REFRAME TITLE AND START
```

The fork itself was already created in TD01.

The new concept in TD05 is actually:

```text
remote branch
+
push
+
Pull Request
```

Recommended pedagogical title:

```text
TD05 - Remote Branch + Pull Request
```

The existing filename may be retained if compatibility is preferred, but the student-facing title should reflect the actual new skill.

Critical addition:

```text
Start TD05 with team baseline synchronization.
```

CORE:

- verify `origin`;
- synchronize to validated team baseline;
- create feature branch;
- implement small change;
- commit;
- push;
- open PR;
- inspect source, target and Files changed.

OPTIONAL:

- second commit on the same open PR;
- advanced remote-branch commands.

Verdict:

```text
90 minutes feasible only if repository state is clean at the start.
```

### TD06 - Code Review

Current status:

```text
GOOD WITH ONE IMPORTANT RULE CHANGE
```

The lab currently encourages a full cycle with feedback, correction, review again and approval.

This is useful, but a correction should not be artificially required.

A correct PR may genuinely need no code change.

Recommended rule:

```text
Every student must perform a meaningful review.

A correction is required only when the review identifies a real issue.
```

Meaningful review evidence can be:

- technical question;
- validation request;
- actionable suggestion;
- request changes;
- approval with specific rationale.

CORE:

- inspect another PR;
- review Files changed;
- leave meaningful feedback;
- respond appropriately;
- approve or request changes;
- merge when ready;
- pull updated main.

Verdict:

```text
90 minutes realistic if TD05 leaves usable open PRs.
```

### TD07 - Data Normalization + Comparison

Remediation status:

```text
REMEDIATED BY LOT-R3.1
```

The revised CORE is now limited to:

```text
numeric normalization
+
common-date alignment
+
period return
+
base 100
+
relative performance
```

The stable analytics module is introduced in TD07:

```text
src/analytics.py
```

with the provider-neutral functions:

```python
index_by_date(...)
align_series(...)
calculate_period_return(...)
calculate_base_100(...)
calculate_relative_performance(...)
```

Daily returns, daily extrema and extra comparison tables are now explicitly OPTIONAL.

The TD07 -> TD08 dependency is also explicit: reviewed TD07 analytics must be available from team `main` before Yahoo Finance integration begins.

Verdict:

```text
Rebalanced CORE fits the intended 80-minute working window plus buffer.
Daily returns are no longer a CORE dependency.
```

### TD08 - Yahoo Finance

Remediation status:

```text
REMEDIATED BY LOT-R3.2
```

The revised CORE now focuses on:

- install and record `yfinance`;
- retrieve AAPL;
- inspect only the provider structure needed for normalization;
- create `src/providers/yahoo_provider.py`;
- normalize to canonical rows;
- preserve `AAPL` and `SP500` as canonical tickers;
- map Yahoo benchmark symbol `^GSPC` at the provider boundary;
- retrieve both instrument and benchmark;
- reuse TD07 `align_series()`;
- reuse TD07 analytics unchanged;
- run MarketPulse;
- use the established Git workflow;
- prepare Checkpoint B evidence.

The following are now explicitly OPTIONAL:

- invalid-symbol experiment;
- alternate instrument;
- provider selector;
- configuration refactor;
- advanced provider-error handling.

An instructor reference asset now provides a known-good retrieval shape, canonical row example and temporary-outage procedure:

```text
docs/09_YAHOO_FINANCE_INSTRUCTOR_REFERENCE.md
```

The lab no longer depends on extended pandas exploration or extra provider drills.

Historical finding before remediation:

- dependency installation;
- first yfinance experiment;
- pandas-like response inspection;
- schema normalization;
- provider module creation;
- provider-symbol mapping;
- two-series retrieval;
- canonical validation;
- alignment;
- analytics reuse;
- failure handling;
- invalid-symbol exercise;
- Git workflow;
- PR;
- review;
- full Checkpoint B;
- live validation.

Rebalancing:

CORE:

- install `yfinance`;
- record dependency;
- retrieve AAPL;
- normalize to canonical rows;
- map SP500 to `^GSPC`;
- retrieve both series;
- align common dates;
- reuse TD07 analytics;
- run MarketPulse;
- push and open PR.

REFERENCE / OPTIONAL:

- invalid-symbol exercise;
- extended provider-failure experiment;
- alternate instrument exercise;
- provider selector;
- advanced mapping refactor.

Checkpoint B:

The exact evidence filenames remain mandatory, but the detailed evidence contract should remain centralized in `docs/04_CHECKPOINTS_AND_EVIDENCE.md`.

The lab should contain a short capture checklist and a link to the canonical document rather than repeating the entire contract.

Recommended instructor preparation:

Provide a known-good `yfinance` snippet or provider skeleton so that time is spent understanding normalization rather than debugging library syntax.

Historical verdict before remediation:

```text
The previous version did not safely fit 90 minutes.
```

Current verdict after LOT-R3.2:

```text
The reduced CORE is designed for about 80 minutes plus a 10-minute buffer.
Remote availability remains an external teaching risk, covered by the instructor reference and outage procedure.
```

### TD09 - Bloomberg Introduction

Remediation status:

```text
REMEDIATED BY LOT-R4.2
```

The revised TD09 CORE result is:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

produced from exactly one explicit access mode:

```text
LIVE
or
APPROVED_SAMPLE
```

CORE now focuses on:

- Bloomberg role in the provider progression;
- canonical vs Bloomberg identifier mapping;
- `AAPL US Equity`;
- `SPX Index`;
- inspect one approved instrument input;
- inspect one approved benchmark input;
- document observed LIVE fields or approved teaching wrapper keys;
- preserve canonical `AAPL` and `SP500`;
- create the TD10 handoff mapping;
- standard Git review.

Live connectivity is no longer a completion condition.

Provider implementation is deferred to TD10.

OPTIONAL now contains:

- extended LIVE exploration;
- additional identifiers;
- extra provider comparison diagrams.

Required instructor assets are now prepared by LOT-R4.1:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
```

The fallback fixture is deliberately not presented as raw live Bloomberg output.

It uses documented teaching wrapper keys so the course does not invent unverified Bloomberg field mnemonics.

The reference also defines the required `LIVE` vs `APPROVED_SAMPLE` distinction.

Current verdict after LOT-R4.2:

```text
TD09 is designed for about 80 minutes plus a 10-minute buffer.
The deliverable is a reviewed mapping contract, not a provider implementation.
LIVE and APPROVED_SAMPLE are both valid CORE paths when documented honestly.
```

### TD10 - Bloomberg Provider

Remediation status:

```text
REMEDIATED BY LOT-R4.3
```

The revised CORE is limited to:

- use the reviewed TD09 mapping;
- create `src/providers/bloomberg_provider.py`;
- keep one authorized raw input boundary;
- support the session's `LIVE` or `APPROVED_SAMPLE` mode;
- normalize provider-stage input to canonical rows;
- preserve `AAPL` and `SP500`;
- obtain instrument and benchmark rows;
- reuse `align_series()`;
- reuse period return, base 100 and relative performance;
- show the actual access mode in terminal output;
- use the established Git workflow.

The provider implementation no longer requires:

- daily returns;
- generalized provider selector;
- YAML parsing;
- rich provider metadata;
- extended error architecture;
- dynamic plugin design.

A teaching scaffold is now available:

```text
docs/11_BLOOMBERG_PROVIDER_SCAFFOLD.md
```

It contains an exact APPROVED_SAMPLE normalization path and a clearly marked LIVE acquisition boundary without inventing a connector.

Current verdict:

```text
The scaffolded TD10 CORE is designed for about 80 minutes plus a 10-minute buffer.
Provider independence is demonstrated through canonical rows and unchanged analytics.
```

### TD11 - Dash Dashboard

Remediation status:

```text
REMEDIATED BY LOT-R4.5
```

The revised CORE uses exactly one dashboard entry point:

```text
src/dashboard.py
```

with the frozen command:

```bash
python src/dashboard.py
```

CORE is now limited to:

- install and record `dash` and `plotly`;
- create one minimal Dash application;
- consume `build_market_snapshot(...)`;
- show provider, instrument, benchmark, lookback and interval;
- show instrument return, benchmark return and relative performance;
- show one base-100 comparison chart with both series;
- compare terminal and dashboard results;
- standard PR and review.

The dashboard is explicitly forbidden from:

- calling Yahoo directly;
- calling Bloomberg directly;
- calculating period return;
- calculating base 100;
- calculating relative performance.

OPTIONAL now contains:

- daily-return chart, only if already implemented;
- volume chart;
- selectors;
- callbacks;
- styling polish;
- small layout helpers.

Current verdict:

```text
The TD11 CORE is designed for about 80 minutes plus a 10-minute buffer.
One snapshot, one dashboard file and one required chart keep the lab within scope.
```

### TD12 - Integration + Release

Current status:

```text
CRITICAL OVERLOAD
```

The objective is correct:

```text
no new major feature
+
integration
+
documentation
+
reproducibility
```

The current document is too large because it also repeats much of the checkpoint and architecture material.

CORE:

- final provider confirmation;
- remove temporary artefacts;
- verify direct dependencies;
- update README;
- fresh clone or clean-environment run;
- final integration PR;
- review;
- merge;
- final run.

Checkpoint C evidence:

Keep only a short checklist in TD12 and make `docs/04_CHECKPOINTS_AND_EVIDENCE.md` the canonical contract.

Individual-evidence correction:

This issue has now been remediated by LOT-R1.6.

For:

```text
03_final_pull_request.png
```

the canonical rule is now explicit:

```text
meaningful late-stage PR from TD09-TD12
+
attributable to the student
```

The evidence does not have to be the single team-level final integration PR.

One integration lead may author the team release PR while other students use their own attributable late-stage Pull Requests.

Artificial duplicate release PRs are not required.

Release dependency recommendation:

By the start of TD12:

```text
dashboard command already frozen
provider command already frozen
dependencies already known
```

TD12 should validate these contracts, not invent them.

Verdict:

```text
Current version is too large for 90 minutes.
A release-only version can fit.
```

## 11. Git-content duplication review

From TD07 onward, the Git workflow is already learned.

The later labs repeatedly restate:

```text
git switch main
git pull
git switch -c ...
git status
git diff
git add
git commit
git push
open Pull Request
review
merge
```

This is useful as a reminder but currently consumes substantial document space.

Recommended pattern from TD07 onward:

```text
## Standard Git workflow

Use the workflow defined in CONTRIBUTING.md.

Suggested branch:
feature/...

Suggested commit:
feat: ...

Before opening the PR:
- run the required application command;
- inspect git diff;
- verify no unrelated files are included.
```

Keep full Git teaching only in TD03-TD06.

This reduces duplication without removing the workflow.

## 12. Checkpoint-content duplication review

The authoritative evidence contract is already:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

TD04, TD08 and TD12 currently repeat large portions of that contract.

Risk:

If evidence filenames or rules change later, several files must be updated consistently.

Recommended single-source rule:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
=
canonical evidence specification
```

Checkpoint-ending labs should contain only:

- checkpoint name;
- required filenames;
- short "capture now" checklist;
- link to the canonical evidence document.

Do not duplicate the full rubric and evidence philosophy in every lab.

## 13. Pedagogical difficulty curve

Current conceptual curve:

```text
LOW
TD01 environment
TD02 Python data structures
TD03 Git local
TD04 branches

MEDIUM
TD05 remote Git
TD06 review
TD07 financial comparison

HIGH
TD08 remote provider
TD09 professional provider concepts
TD10 provider integration
TD11 web dashboard
TD12 release
```

The direction is correct.

The issue is that TD08-TD12 currently increase both:

```text
conceptual difficulty
and
task count
```

at the same time.

Rebalancing should keep conceptual difficulty rising while reducing the number of required side tasks.

## 14. Finance-scope review

The CORE financial concepts should be frozen as:

```text
price
period return
base 100
relative performance
```

Daily return should move to:

```text
OPTIONAL / TIME PERMITTING
```

This matches the actual dashboard target, which does not require a daily-return chart.

Do not add:

- Sharpe ratio;
- beta;
- CAPM;
- alpha;
- VaR;
- RSI;
- MACD;
- Bollinger Bands;
- portfolio optimization.

## 15. Checkpoint alignment review

### Checkpoint A

Alignment:

```text
GOOD
```

Evidence:

- terminal and Python from TD01-TD02;
- Git status and log from TD03;
- branch and merge from TD04.

Important consequence:

A mandatory merge-conflict exercise is not necessary for Checkpoint A.

### Checkpoint B

Alignment:

```text
REMEDIATED BY LOT-R3.3
```

Evidence remains:

- Pull Request from TD05;
- code review from TD06;
- comparison from TD07;
- Yahoo data from TD08.

Resolved decision:

```text
Checkpoint B validates the common CORE pair:
AAPL + S&P 500
```

Changing the selected ticker or market pair is no longer a mandatory Checkpoint B skill.

Alternate coherent market pairs remain:

```text
OPTIONAL
or
oral extension
```

This aligns the canonical checkpoint contract with what TD08 actually guarantees.

### Checkpoint C

Alignment:

```text
GOOD WITH INDIVIDUAL TRACEABILITY CLARIFICATION
```

Evidence:

- final market provider from TD09-TD10;
- dashboard from TD11;
- final or late-stage PR from TD09-TD12;
- reproducible run from TD12.

Required clarification:

```text
03_final_pull_request.png
does not have to be the single team release PR.
```

It must be a late-stage PR attributable to the student.

## 16. Proposed canonical CORE repository evolution

### TD01-TD06

Keep:

```text
src/
└── main.py
```

This avoids architecture work before students need it.

### TD07

Introduce:

```text
src/
├── main.py
└── analytics.py
```

Purpose:

Move reusable comparison calculations out of terminal presentation.

### TD08

Introduce:

```text
src/
├── main.py
├── analytics.py
└── providers/
    ├── __init__.py
    └── yahoo_provider.py
```

### TD10

Extend:

```text
src/
├── main.py
├── analytics.py
└── providers/
    ├── __init__.py
    ├── yahoo_provider.py
    └── bloomberg_provider.py
```

### TD11

Add one simple dashboard entry point:

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

Execution contract:

```bash
python src/main.py
python src/dashboard.py
```

This is the recommended 18-hour CORE architecture.

A more formal package structure can be shown after the CORE sequence as an architectural extension.

## 17. Proposed CORE vs OPTIONAL decisions

| TD | Keep in CORE | Move to optional / demo |
|---|---|---|
| TD01 | setup, Linux, run starter | extended shell exploration |
| TD02 | JSON, CSV, types, filtering, reusable summary | min/max, volume and extra formatting exercises |
| TD03 | status, diff, add, commit, log, show | multi-file staging drills, author filtering |
| TD04 | branch, feature, merge, graph, CP-A | manufactured conflict exercise |
| TD05 | remote, push, PR | second PR-update commit exercise |
| TD06 | meaningful review, approve/request changes, merge | forced correction when no real issue exists |
| TD07 | normalization, alignment, period return, base 100, relative performance | daily returns and daily extrema |
| TD08 | yfinance, symbol mapping, normalization, two-series reuse | invalid-symbol experiment, extra provider selector |
| TD09 | Bloomberg concepts, approved sample/live inspection, mapping | extended live exploration |
| TD10 | normalize Bloomberg, canonical rows, reuse analytics | YAML wiring, generic provider framework |
| TD11 | static Dash summary + base-100 chart | callbacks, extra charts, styling, selectors |
| TD12 | clean, document, fresh run, final PR, release | advanced deployment |

## 18. Rebalanced 18-hour target

The official schedule remains unchanged:

```text
Wave 1
TD01 + TD02
3 hours

Wave 2
TD03 + TD04 + TD05 + TD06
6 hours

Wave 3
TD07 + TD08
3 hours

Wave 4
TD09 + TD10 + TD11 + TD12
6 hours
```

Checkpoint phases remain:

```text
Checkpoint Phase A
TD01-TD04

Checkpoint Phase B
TD05-TD08

Checkpoint Phase C
TD09-TD12
```

Do not call the three checkpoint phases "waves".

## 19. Priority corrections

### P0 - Must be corrected before teaching

1. Freeze one CORE repository architecture.
2. Fix the TD04 -> TD05 local-to-remote handoff.
3. Reduce TD08, TD10, TD11 and TD12 CORE scope.
4. Make Bloomberg fallback material available before TD09.
5. Correct the TD12 three-wave terminology.
6. Clarify Checkpoint C individual PR evidence.

### P1 - Strongly recommended

1. Move daily returns out of TD07 CORE.
2. Move merge-conflict execution out of TD04 CORE.
3. Reframe TD05 around remote branch + PR rather than fork creation.
4. Stop requiring an artificial correction in TD06.
5. Centralize checkpoint details in docs/04.
6. Shorten repeated Git instructions after TD06.
7. Clarify that settings.yml is a reference contract, not mandatory parsed YAML.

### P2 - Quality improvements

1. Rename the labs index heading from "TD Index" to "Lab Index" while retaining TD filenames.
2. Add a visible CORE / OPTIONAL / INSTRUCTOR DEMO label convention to every lab.
3. Add a short "Definition of Done" near the top of each lab.
4. Keep optional challenges but move them after the CORE stop point.
5. Freeze tested direct dependency versions at release time rather than relying indefinitely on unbounded package versions.

## 20. Proposed lab template after rebalancing

Each student-facing lab should converge toward:

```text
# TDxx - Title

## Duration
## Business requirement
## Learning objectives
## CORE definition of done
## Prerequisites
## Session plan

# CORE
Part 1
Part 2
Part 3
...

# Validation
Run command
Expected behaviour

# Standard Git workflow
Short reminder only

# Checkpoint relation
Short canonical reference

# OPTIONAL
Exercises / challenges

# Troubleshooting
Only topic-specific issues

# What comes next?
```

This keeps each lab operational while reducing repeated material.

## 21. Recommended implementation sequence

The review should now be followed by a controlled rebalancing pass.

Recommended order:

```text
R1 - Freeze cross-cutting contracts
     repository structure
     runtime commands
     wave terminology
     configuration status
     checkpoint source of truth

R2 - Rebalance Wave 1 and Wave 2
     TD01-TD06
     especially TD04-TD05 handoff

R3 - Rebalance Wave 3
     TD07-TD08
     create analytics contract

R4 - Rebalance Wave 4
     TD09-TD12
     Bloomberg fallback
     dashboard entry point
     reproducibility

R5 - Final consistency scan
     paths
     filenames
     commands
     evidence
     no duplicated contradictions
```

## 22. Final assessment

The current 12-TD design should not be replaced.

Its architecture and business narrative are strong.

The main problem is not the sequence.

The main problem is density.

The correct next move is:

```text
preserve the sequence
+
simplify the CORE
+
make optional material explicit
+
freeze technical handoffs
+
centralize repeated contracts
```

After these corrections, the MarketPulse sequence can realistically function as a coherent 18-hour practical path rather than only as twelve individually complete documents.
