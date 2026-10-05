# MarketPulse Teaching Readiness and Dry Run Plan

## 1. Purpose

R1 to R5 closed the documentation remediation cycle.

R6 validates that the teaching repository can actually be used as a progressive classroom system.

The objective is not to redesign MarketPulse.

The objective is to prove that the documented path can be executed, taught and recovered under realistic student conditions.

```text
R1-R5
documentation consistency
        |
        v
R6
teaching execution readiness
        |
        v
Teaching Baseline
```

## 2. Scope

R6 covers:

```text
starter runtime
student bootstrap
TD01-TD12 execution path
cross-TD state transitions
checkpoint evidence
provider fallbacks
instructor recovery paths
final teaching baseline
```

R6 does not add new business scope.

R6 does not turn optional professional extensions into CORE requirements.

## 3. Validation principles

Every readiness claim must be classified as one of:

```text
EXECUTED
=
command or program was actually run

INSPECTED
=
repository artifact was reviewed directly

EXTERNAL VERIFY
=
requires an environment or service unavailable to the current validation runner

NOT TESTED
=
no evidence yet
```

No simulated success is allowed for an unavailable external dependency.

## 4. R6 roadmap

```text
R6.1  Starter runtime baseline
R6.2  Clean-clone and student bootstrap portability
R6.3  Wave 1 dry run - TD01 to TD02
R6.4  Wave 2 dry run - TD03 to TD06
R6.5  Wave 3 dry run - TD07 to TD08
R6.6  Wave 4 dry run - TD09 to TD12
R6.7  Checkpoint and evidence dry run
R6.8  Instructor contingency and provider fallback validation
R6.9  Teaching baseline freeze
```

## 5. R6.1 - Starter runtime baseline

Status:

```text
DONE
```

### 5.1 Source baseline

Validated against the current `main` repository state after R5 closure.

Relevant starter artifacts:

```text
requirements.txt
src/main.py
data/sample/instruments.json
data/sample/prices.csv
config/settings.yml
docs/labs/TD01_BOOTSTRAP_LINUX.md
```

### 5.2 Environment evidence

Executed in an isolated runtime:

```text
Python 3.13.5
Git 2.47.3
```

The repository starter does not require an external Python package for TD01 or TD02.

The command:

```bash
python -m pip install -r requirements.txt
```

completed without requiring a package installation.

### 5.3 Starter data evidence

Executed checks:

```bash
head data/sample/prices.csv
grep -c AAPL data/sample/prices.csv
grep -c SP500 data/sample/prices.csv
```

Observed counts:

```text
AAPL  = 21
SP500 = 21
```

This matches the TD01 expected observations.

### 5.4 Runtime evidence

Executed:

```bash
python src/main.py
```

Observed output:

```text
=== MarketPulse ===

Instrument
AAPL - Apple Inc.
Last price: 266.20 USD

Benchmark
SP500 - S&P 500
Last level: 6742.00

Period: 1 month
Interval: Daily

Observations
AAPL: 21
SP500: 21
```

The result matches the TD01 documented expected output.

### 5.5 Syntax evidence

Executed:

```bash
python -m py_compile src/main.py
```

Result:

```text
PASS
```

### 5.6 R6.1 acceptance criteria

```text
[x] Python runtime available
[x] Git executable available
[x] TD01 requirements install path is valid
[x] starter CSV is readable
[x] starter JSON is readable by the application
[x] AAPL observation count is 21
[x] SP500 observation count is 21
[x] python src/main.py executes successfully
[x] output matches the TD01 contract
[x] src/main.py compiles successfully
```

R6.1 conclusion:

```text
PASS
```

## 6. R6.2 - Clean-clone and student bootstrap portability

Status:

```text
NEXT
```

Validate from a genuinely fresh checkout:

```text
new environment
      |
      v
clone or fork
      |
      v
repository root
      |
      v
Python + Git checks
      |
      v
starter data inspection
      |
      v
python src/main.py
```

Required checks:

```text
[ ] public instructor repository can be cloned from the intended student environment
[ ] repository opens at the expected root
[ ] no untracked generated file is required
[ ] no local secret or local-only config is required
[ ] TD01 Linux commands work from a fresh checkout
[ ] python src/main.py works without manual repair
[ ] TEAM_TEMPLATE.md can become TEAM.md without exposing sensitive data
```

Current validation note:

```text
The automated execution sandbox used for R6.1 cannot resolve github.com through its shell network path.

The GitHub repository itself remains accessible through the authenticated repository connector.

Therefore:
- repository content validation = EXECUTED / INSPECTED
- shell git clone validation = EXTERNAL VERIFY
```

This limitation must not be reported as a repository failure.

## 7. R6.3 - Wave 1 dry run

Validate:

```text
TD01 Bootstrap + Linux
TD02 Python + CSV / JSON
```

Focus:

```text
student starting point
command accuracy
expected output
file mutations
handoff into TD03
90-minute realism
```

## 8. R6.4 - Wave 2 dry run

Validate:

```text
TD03 Git Local Workflow
TD04 Branches + Merge
TD05 Remote Branch + Pull Request
TD06 Code Review
```

Focus:

```text
real changes
commit history
branch state
Team Baseline Gate
remote workflow
Pull Request lifecycle
review and merge
handoff into analytics work
```

## 9. R6.5 - Wave 3 dry run

Validate:

```text
TD07 Data Normalization + Comparison
TD08 Yahoo Finance
```

Focus:

```text
analytics.py creation
alignment
period return
base 100
relative performance
Yahoo provider boundary
canonical rows
Checkpoint B readiness
```

## 10. R6.6 - Wave 4 dry run

Validate:

```text
TD09 Bloomberg Introduction
TD10 Bloomberg Provider
TD11 Dash Dashboard
TD12 Integration + Release
```

Focus:

```text
Bloomberg mapping
LIVE vs APPROVED_SAMPLE honesty
provider normalization
shared build_market_snapshot(...)
import-safe main.py
Dash consumption
dependency installation
release reproducibility
```

## 11. R6.7 - Checkpoint and evidence dry run

Validate the canonical evidence contract for:

```text
Checkpoint A
TD01-TD04

Checkpoint B
TD05-TD08

Checkpoint C
TD09-TD12
```

The dry run must prove that required evidence can actually be produced without exposing credentials or requiring artificial screenshots.

## 12. R6.8 - Instructor contingency and provider fallback validation

Validate recovery paths for:

```text
student environment failure
GitHub access delay
Yahoo provider failure
Bloomberg LIVE unavailable
Dash dependency issue
late student synchronization
merge conflict
missing checkpoint evidence
```

The objective is to preserve learning continuity without fabricating provider results.

## 13. R6.9 - Teaching baseline freeze

The final baseline can be frozen only when:

```text
[ ] R6.1 PASS
[ ] R6.2 PASS or explicitly instructor-verified
[ ] R6.3 PASS
[ ] R6.4 PASS
[ ] R6.5 PASS
[ ] R6.6 PASS
[ ] R6.7 PASS
[ ] R6.8 PASS
```

Expected final state:

```text
12 coherent labs
+
3 executable checkpoints
+
1 tested starter
+
1 tested progressive application path
+
documented provider fallbacks
+
documented instructor recovery paths
=
TEACHING BASELINE READY
```

## 14. Status board

| Lot | Scope | Status |
|---|---|---|
| R6.1 | Starter runtime baseline | DONE |
| R6.2 | Clean-clone and student bootstrap portability | NEXT |
| R6.3 | Wave 1 dry run | NOT STARTED |
| R6.4 | Wave 2 dry run | NOT STARTED |
| R6.5 | Wave 3 dry run | NOT STARTED |
| R6.6 | Wave 4 dry run | NOT STARTED |
| R6.7 | Checkpoint and evidence dry run | NOT STARTED |
| R6.8 | Instructor contingency and provider fallback validation | NOT STARTED |
| R6.9 | Teaching baseline freeze | NOT STARTED |
