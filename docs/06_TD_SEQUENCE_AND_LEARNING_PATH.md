# TD Sequence and Learning Path

## 1. Purpose

This document defines the common learning path for the 18 hours of practical work in the ESILV A4 module MESIFI472326 - Python, Git, Linux.

The labs use MarketPulse as a progressive use case. Python, Git and Linux are not treated as isolated topics. Students use them together while building a small financial market-data application.

## 2. Overall progression

The common sequence contains 12 TD units of 1 hour 30 minutes.

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

The 12 units are grouped into four pedagogical waves:

```text
Wave 1 - TD01-TD02 - 3 hours
Wave 2 - TD03-TD06 - 6 hours
Wave 3 - TD07-TD08 - 3 hours
Wave 4 - TD09-TD12 - 6 hours
```

## 3. MarketPulse progression

```text
Local CSV / JSON
        |
        v
Python processing
        |
        v
Git versioning
        |
        v
Collaborative Git workflow
        |
        v
Common market-data model
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
Integrated MarketPulse release
```

The core business contract remains:

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

### CORE runtime contract

The execution contract is intentionally stable:

```bash
python src/main.py
```

is the terminal entry point from the starter onward.

From TD11 onward:

```bash
python src/dashboard.py
```

is the dashboard entry point.

TD12 must validate these same commands from a fresh or clean setup.

## 4. TD01 - Bootstrap + Linux

### Business requirement

```text
"We need a common environment before we can work on MarketPulse."
```

### Learning objectives

Students should be able to:

- identify the MarketPulse business context;
- form a team and identify the team repository;
- fork the instructor repository;
- open the common development environment;
- navigate a Linux terminal;
- inspect repository files;
- verify Python and Git availability;
- run the MarketPulse starter.

### MarketPulse evolution

No business feature is added. The objective is to make the starter operational for every team.

### Git level expected

Introductory only:

- repository;
- fork;
- GitHub account;
- basic Git identity awareness.

No branch workflow is required yet.

### Expected result

```text
esilv-marketpulse-gXX-tYY
+
TEAM.md
+
working environment
+
working terminal
+
python src/main.py
```

### Checkpoint relation

No checkpoint is graded at this stage. TD01 contributes to the foundations later validated by Checkpoint A.

## 5. TD02 - Python + CSV / JSON

### Business requirement

```text
"The trading desk still sends local CSV and JSON market files."
```

### Learning objectives

Students should be able to:

- read CSV data with Python;
- read JSON metadata with Python;
- distinguish instrument and benchmark;
- filter observations by ticker;
- inspect daily observations;
- create simple reusable functions;
- modify MarketPulse output.

### MarketPulse evolution

```text
CSV / JSON
    |
    v
Python
    |
    v
Instrument + Benchmark
```

### Expected result

MarketPulse can load and display local daily data for the primary instrument and benchmark.

### Checkpoint relation

Contributes to Checkpoint A.

## 6. TD03 - Git Local Workflow

### Business requirement

```text
"We need to keep a reliable history of changes."
```

### Learning objectives

Students should be able to use:

```text
git status
git diff
git add
git commit
git log
```

### MarketPulse evolution

Students version small MarketPulse changes locally.

### Expected result

Each student has identifiable commits.

### Checkpoint relation

Contributes directly to Checkpoint A.

## 7. TD04 - Branches + Merge

### Business requirement

```text
"Features should no longer be developed directly on main."
```

### Learning objectives

Students should be able to:

- create and switch branches;
- implement a small feature;
- compare changes;
- merge a branch;
- understand a simple merge conflict.

### MarketPulse evolution

Small features begin to be isolated by branch.

### Checkpoint relation

Checkpoint A is performed after TD04.

## 8. TD05 - Remote Branch + Pull Request

### Business requirement

```text
"Several developers now contribute to the same MarketPulse repository."
```

### Learning objectives

Students should be able to:

- push a feature branch;
- open a Pull Request;
- write a useful Pull Request description;
- identify source and target branches;
- connect a Git contribution to a student identity.

### Checkpoint relation

Contributes to Checkpoint B.

## 9. TD06 - Code Review

### Business requirement

```text
"Changes must be reviewed before integration."
```

### Learning objectives

Students should be able to:

- read another student's changes;
- inspect Files changed;
- comment meaningfully on a Pull Request;
- request a correction only when a real issue exists;
- approve a correct change after inspection;
- merge after review;
- synchronize local main after integration.

### Checkpoint relation

Contributes to Checkpoint B.

## 10. TD07 - Data Normalization + Comparison

### Business requirement

```text
"All market-data sources must feed a common comparison model."
```

### Learning objectives

Students should be able to:

- distinguish local acquisition from provider-neutral analytics;
- create and reuse `src/analytics.py`;
- align instrument and benchmark observations on common dates;
- maintain the common 1-month daily contract;
- calculate period return;
- calculate base-100 series;
- calculate relative performance;
- keep provider identifiers outside analytics.

### Finance concepts introduced

CORE:

```text
period return
base-100 normalization
relative performance
```

OPTIONAL:

```text
daily return
```

Only simple formulas are required.

### Checkpoint relation

Contributes to Checkpoint B.

## 11. TD08 - Yahoo Finance

### Business requirement

```text
"Traders need more recent market data than local files."
```

### Learning objectives

Students should be able to:

- retrieve remote market data for the common CORE pair;
- handle AAPL as the instrument and S&P 500 as the benchmark;
- use the common lookback and interval;
- understand provider-specific symbols;
- handle simple acquisition errors;
- connect remote data to the existing MarketPulse flow.

Changing to another market pair is optional and is not required for Checkpoint B.

### Git level expected

The full branch, Pull Request and review workflow should now be used.

### Checkpoint relation

Checkpoint B is performed after TD08.

## 12. TD09 - Bloomberg Introduction

### Business requirement

```text
"The trading desk now has access to a professional market-data environment."
```

### Learning objectives

Students should be able to:

- understand Bloomberg's role in the provider progression;
- distinguish canonical tickers from Bloomberg identifiers;
- distinguish LIVE from APPROVED_SAMPLE mode;
- inspect an instructor-approved LIVE response or fallback sample;
- document only observed or approved input fields;
- create `docs/BLOOMBERG_FIELD_MAPPING.md`;
- preserve AAPL and SP500 as canonical tickers;
- prepare a mapping contract for TD10 without inventing Bloomberg fields.

Live connectivity is not required for TD09 completion.

### Checkpoint relation

Contributes to Checkpoint C.

## 13. TD10 - Bloomberg Provider

### Business requirement

```text
"MarketPulse must support Bloomberg without rewriting the whole application."
```

### Learning objectives

Students should be able to:

- use the reviewed TD09 mapping as the provider contract;
- create `src/providers/bloomberg_provider.py`;
- isolate the authorized raw input boundary;
- normalize LIVE or APPROVED_SAMPLE input to canonical rows;
- preserve AAPL and SP500 semantics;
- reuse `align_series()` unchanged;
- reuse period return, base 100 and relative performance unchanged;
- display the actual access mode honestly.

Daily returns, generic provider selection and YAML parsing are not required.

### MarketPulse evolution

```text
CSV
Yahoo
Bloomberg
   |
   v
common market-data model
```

### Checkpoint relation

Contributes to Checkpoint C.

## 14. TD11 - Dash Dashboard

### Business requirement

```text
"Traders want a visual interface instead of terminal output."
```

### Minimum dashboard target

```text
Instrument
Benchmark
Lookback
Interval
Instrument return
Benchmark return
Relative performance
Base-100 comparison chart
```

Optional if time allows:

- daily-return chart;
- volume chart.

### Checkpoint relation

Contributes to Checkpoint C.

## 15. TD12 - Integration + Release

### Business requirement

```text
"We need a reproducible version of MarketPulse that another person can run."
```

### Learning objectives

Students should be able to:

- run the complete MarketPulse flow;
- verify the final provider;
- verify instrument and benchmark comparison;
- complete the collaborative Git workflow;
- update project documentation;
- demonstrate a reproducible run;
- explain their individual contribution.

### Expected result

```text
Market data
    |
    v
Instrument + Benchmark
    |
    v
Normalization
    |
    v
Performance comparison
    |
    v
Dash
    |
    v
Trader
```

### Checkpoint relation

Checkpoint C is performed after TD12.

## 16. Checkpoint phases

The checkpoint phases are assessment groupings and are different from the four pedagogical waves.

```text
CHECKPOINT PHASE A - TD01-TD04
    |
    v
CHECKPOINT A - Foundations - 25%

CHECKPOINT PHASE B - TD05-TD08
    |
    v
CHECKPOINT B - Collaboration and Data - 30%

CHECKPOINT PHASE C - TD09-TD12
    |
    v
CHECKPOINT C - Integration and Release - 45%
```

## 17. Common path vs advanced path

The following topics are outside the required 18-hour core:

- remote VPS setup;
- SSH deployment;
- systemd;
- Docker;
- GitHub Actions;
- intraday market data;
- advanced quantitative finance.

These may be offered as optional extensions.

## 18. Pedagogical rule

Each TD should answer a real project need.

```text
new business need
      |
      v
new technical concept
      |
      v
MarketPulse evolution
      |
      v
Git trace
```

The objective is to avoid isolated exercises with no connection to the fil rouge.
