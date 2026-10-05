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
REVIEW
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

### 6.1 Repository accessibility inspection

The instructor repository reports:

```text
visibility    = public
private       = false
allow_forking = true
default branch = main
HTTPS clone URL is published
```

Classification:

```text
INSPECTED
```

### 6.2 Local-only dependency scan

Repository search found no CORE runtime dependency on:

```text
os.environ
getenv
dotenv
absolute workstation path
localhost-only service
```

The starter application reads only versioned sample data.

The repository ignore rules exclude local `.env` files.

Classification:

```text
INSPECTED
```

### 6.3 TD01 shell command dry run

Using the exact versioned starter runtime and sample data, the following commands were executed successfully:

```bash
pwd
ls
ls data/sample
cat data/sample/instruments.json
head data/sample/prices.csv
grep AAPL data/sample/prices.csv
grep SP500 data/sample/prices.csv
python --version
git --version
python src/main.py
```

Observed runtime versions:

```text
Python 3.13.5
Git 2.47.3
```

The MarketPulse output remained identical to the documented TD01 output.

Classification:

```text
EXECUTED
```

### 6.4 Team bootstrap safety

`TEAM_TEMPLATE.md` requires only:

```text
TD group
team number
full name
GitHub username
repository name
```

It explicitly forbids:

```text
personal email address
student identification number
phone number
home address
password
access token
private key
cloud billing information
```

Classification:

```text
INSPECTED
```

### 6.5 Remaining external verification

The automated execution sandbox cannot currently resolve `github.com` through its shell network path.

A direct shell command such as:

```bash
git clone https://github.com/tawounfouet/esilv-marketpulse.git
```

therefore cannot be used here as evidence of student-network clone portability.

The repository itself remains accessible through the authenticated repository connector.

This limitation must not be reported as a repository failure.

Classification:

```text
EXTERNAL VERIFY
```

### 6.6 R6.2 acceptance criteria

```text
[ ] actual git clone from the intended student environment
[x] repository is public and forkable
[x] default branch and HTTPS clone endpoint are exposed
[x] no untracked generated file is required by the starter runtime
[x] no local secret or local-only config is required
[x] required TD01 Linux inspection commands execute
[x] python src/main.py works from reconstructed exact versioned starter files
[x] TEAM_TEMPLATE.md can become TEAM.md without requiring sensitive data
```

R6.2 conclusion:

```text
READY FOR EXTERNAL CLONE VERIFY
```

R6.2 does not block the remaining local pedagogical dry run.

## 7. R6.3 - Wave 1 dry run

Status:

```text
DONE
```

Validated:

```text
TD01 Bootstrap + Linux
TD02 Python + CSV / JSON
```

### 7.1 TD01 execution result

The starter path was executed with the versioned CORE assets.

Validated commands include:

```bash
pwd
ls
ls data/sample
cat data/sample/instruments.json
head data/sample/prices.csv
grep AAPL data/sample/prices.csv
grep SP500 data/sample/prices.csv
python --version
git --version
python src/main.py
```

Results:

```text
Python runtime available
Git runtime available
AAPL rows = 21
SP500 rows = 21
starter output matches the documented TD01 output
```

Classification:

```text
EXECUTED
```

### 7.2 TD02 end-state implementation

A temporary teaching working tree was created from the exact starter code.

The TD02 instructions were then applied without changing repository architecture.

Implemented helpers:

```python
get_first_close(...)
get_last_close(...)
display_market_summary(...)
```

The implementation preserves:

```text
csv.DictReader
json.load
filter_prices(...)
src/main.py entry point
standard-library-only dependency model
```

### 7.3 Numeric conversion evidence

The raw CSV close value was confirmed as:

```text
str
```

The helper return values were confirmed as:

```text
float
```

Observed values:

```text
AAPL
first close = 250.0
last close  = 266.2

SP500
first close = 6600.0
last close  = 6742.0
```

Classification:

```text
EXECUTED
```

### 7.4 TD02 target output

Executed:

```bash
python src/main.py
```

Observed output:

```text
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First close  : 250.00 USD
Last close   : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First close  : 6600.00
Last close   : 6742.00
```

This matches the documented TD02 target behaviour.

### 7.5 TD02 syntax validation

Executed:

```bash
python -m py_compile src/main.py
```

Result:

```text
PASS
```

### 7.6 TD02 -> TD03 working-tree handoff

A local Git baseline was created only for dry-run verification.

After applying the TD02 changes:

```bash
git status --short
```

reported:

```text
 M src/main.py
```

The repository `.gitignore` correctly suppresses generated Python cache files.

Executed:

```bash
git diff --check
```

Result:

```text
PASS
```

The meaningful TD02 change therefore remains available for TD03 exactly as intended:

```text
TD02
working Python change
      |
      v
TD03
git status
git diff
git add
git commit
git log
```

### 7.7 Scope protection

The dry run confirmed that TD02 does not require:

```text
pandas
return calculations
base-100 calculations
relative performance
feature branches
Pull Requests
```

The Wave 1 scope remains focused on Linux inspection and basic Python data handling.

### 7.8 Timing interpretation

The technical path contains no newly discovered hidden setup or refactor.

The documented 80-minute CORE plus 10-minute buffer remains structurally plausible.

Actual classroom completion time remains a teaching observation rather than machine-execution evidence.

Classification:

```text
INSPECTED
```

### 7.9 R6.3 acceptance criteria

```text
[x] TD01 starter executes
[x] TD01 Linux inspection commands are coherent
[x] TD02 starts from the TD01 state
[x] JSON metadata loads correctly
[x] CSV observations load correctly
[x] AAPL and SP500 each contain 21 rows
[x] close values are converted from str to float
[x] reusable first/last close helpers work
[x] reusable market summary works
[x] TD02 target output is reproducible
[x] no return calculation is introduced
[x] no external Python dependency is introduced
[x] TD02 leaves a meaningful src/main.py working-tree change for TD03
[x] generated Python cache files remain ignored
[x] git diff --check passes
```

R6.3 conclusion:

```text
PASS
```

## 8. R6.4 - Wave 2 dry run

Status:

```text
REVIEW
```

Validated scope:

```text
TD03 Git Local Workflow
TD04 Branches + Merge
TD04 -> TD05 Team Baseline Gate
TD05 remote branch mechanics
TD06 review and integration mechanics
```

The GitHub Pull Request and review UI still require one real team-fork verification.

### 8.1 Validation topology

The dry run used:

```text
student-a working repository
student-b working repository
team.git bare shared remote
integrator working repository
```

This provided a real Git remote and independent local histories without creating artificial branches or Pull Requests in the instructor repository.

For the Git-only mechanics, the temporary harness used a reduced sample CSV with the same MarketPulse code shape and the same first and last dates.

The authoritative 21-row AAPL/SP500 starter-data validation remains R6.3.

### 8.2 TD03 - local Git workflow

Starting state:

```text
src/main.py modified
=
real TD02-style Python change
```

Executed:

```bash
git status
git diff
git add src/main.py
git diff --staged
git commit
git log --oneline
git show HEAD
python src/main.py
```

Observed transition:

```text
working tree
      |
      v
staged src/main.py
      |
      v
feat: improve MarketPulse market summary
      |
      v
clean main
```

Validation:

```text
git diff --check = PASS
git diff --staged --check = PASS
runtime after commit = PASS
working tree after commit = clean
```

Classification:

```text
EXECUTED
```

### 8.3 TD04 - branch isolation and merge

Created:

```text
feature/display-observation-dates
```

The branch added only:

```text
get_first_date(...)
get_last_date(...)
date presentation in the reusable summary
```

Executed:

```bash
git switch -c feature/display-observation-dates
git status
git diff
python src/main.py
git add src/main.py
git diff --staged
git commit
git log --oneline --graph --decorate --all
git diff main..feature/display-observation-dates
git switch main
git merge feature/display-observation-dates
git branch -d feature/display-observation-dates
```

The branch diff was limited to:

```text
src/main.py
10 insertions
```

Git selected a valid fast-forward merge.

No artificial merge commit was forced.

After merge:

```text
feature visible from main
feature commit still visible in history
MarketPulse runtime = PASS
working tree = clean
```

Classification:

```text
EXECUTED
```

### 8.4 Team Baseline Gate - divergent local histories

The dry run deliberately created two valid but different TD04 histories.

Before synchronization:

```text
student-a/main != student-b/main
```

Student B then executed the documented safety sequence:

```bash
git switch main
git status
git branch archive/td04-local
git fetch origin
git reset --hard origin/main
```

After synchronization:

```text
student-b HEAD = origin/main
archive/td04-local = previous student-b TD04 history
working tree = clean
MarketPulse runtime = PASS
```

The test proved both required properties:

```text
common shared baseline established
+
local learning history preserved
```

This confirms the controlled hard reset is technically justified by the safety branch and clean-tree preconditions.

Classification:

```text
EXECUTED
```

### 8.5 TD05 - remote branch mechanics

From the synchronized shared baseline, two distinct student contributions were created.

Student A:

```text
branch
=
feature/display-provider-label

commit
=
feat: display provider label

changed file
=
src/main.py
```

Student B:

```text
branch
=
docs/improve-execution-docs

commit
=
docs: clarify MarketPulse execution

changed file
=
docs/EXECUTION.md
```

Executed for both students:

```bash
git switch main
git pull --ff-only
git switch -c <feature-branch>
git add <intended-file>
git diff --staged --check
git commit
git push -u origin <feature-branch>
```

The shared remote then contained:

```text
main
feature/display-provider-label
docs/improve-execution-docs
```

Both local feature branches tracked their corresponding remote branches.

The candidate changes were inspectable as:

```text
origin/main
      |
      +--> origin/feature/display-provider-label

origin/main
      |
      +--> origin/docs/improve-execution-docs
```

Classification:

```text
EXECUTED
```

### 8.6 Pull Request boundary

The following Pull Request properties were validated structurally from the actual branch state and from the TD05 contract:

```text
source = pushed student feature branch
target = team main
diff = intended branch change only
PR remains open until TD06
```

However, the dry-run environment does not contain a disposable student team fork.

No artificial Pull Request was created in:

```text
tawounfouet/esilv-marketpulse
```

because that would pollute the instructor repository with synthetic teaching evidence.

Required remaining check:

```text
open one real PR inside a disposable or actual team fork
verify source branch
verify target branch
verify title and description
verify Files changed
leave PR open
```

Classification:

```text
EXTERNAL VERIFY
```

### 8.7 TD06 - review semantics

The two remote candidate diffs were inspected before integration.

Provider-label candidate:

```text
files changed = src/main.py only
scope = 2 inserted lines
runtime = PASS
blocking issue = none
review outcome = APPROVE
```

Execution-documentation candidate:

```text
files changed = docs/EXECUTION.md only
scope = documentation only
blocking issue = none
review outcome = APPROVE
```

No correction commit was manufactured because no real defect was found.

This validates the TD06 rule:

```text
no real defect
      |
      v
meaningful review
      |
      v
approval
```

rather than:

```text
review exercise
      |
      v
fake defect
      |
      v
fake fix commit
```

Classification:

```text
EXECUTED for diff inspection and integration logic
INSPECTED for GitHub review-outcome semantics
```

### 8.8 Reviewed integration and synchronization

After inspection, both branches were integrated into the shared remote main.

The resulting graph contained:

```text
reviewed provider-label integration
+
reviewed execution-documentation integration
+
previous TD04 baseline
+
previous TD03 commit
```

Both student environments then executed:

```bash
git switch main
git pull --ff-only
git status
python src/main.py
```

Final state:

```text
student-a HEAD = origin/main
student-b HEAD = origin/main
student-a working tree = clean
student-b working tree = clean
student-a runtime = PASS
student-b runtime = PASS
```

Classification:

```text
EXECUTED
```

### 8.9 TD06 -> TD07 handoff

Wave 2 now leaves:

```text
one synchronized main
+
established branch workflow
+
established remote push workflow
+
review-before-merge rule
+
clean working trees
```

TD07 can therefore introduce:

```text
src/analytics.py
```

as the next real feature instead of reteaching the collaboration workflow.

### 8.10 R6.4 acceptance criteria

```text
[x] TD03 starts from a meaningful TD02 working-tree change
[x] git status and git diff expose that change
[x] intended work can be staged deliberately
[x] git diff --staged represents the next commit
[x] meaningful local commit can be created and inspected
[x] TD04 starts from clean main
[x] feature branch isolates observation-date work
[x] feature branch compares cleanly against main
[x] fast-forward merge works and is accepted
[x] branch can be deleted without losing history
[x] two divergent TD04 local mains can be reproduced
[x] archive/td04-local preserves pre-alignment history
[x] controlled reset aligns another student to origin/main
[x] remote feature branches can be pushed with upstream tracking
[x] remote candidate diffs contain only intended work
[ ] actual GitHub Pull Request opened in a team fork
[ ] actual GitHub Files changed view verified in a team fork
[ ] actual review submitted by another student account
[ ] actual PR merged through the GitHub UI after review
[x] no fake correction commit is required when review finds no defect
[x] reviewed branch integration mechanics work
[x] all student mains can synchronize to the integrated remote main
[x] MarketPulse remains executable after synchronization
[x] Wave 2 leaves a clean handoff for TD07
```

R6.4 conclusion:

```text
LOCAL AND REMOTE GIT MECHANICS PASS
GITHUB PR/REVIEW UI VERIFY REMAINS
```

R6.4 does not block the Wave 3 dry run.

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
| R6.2 | Clean-clone and student bootstrap portability | REVIEW |
| R6.3 | Wave 1 dry run | DONE |
| R6.4 | Wave 2 dry run | REVIEW |
| R6.5 | Wave 3 dry run | NEXT |
| R6.6 | Wave 4 dry run | NOT STARTED |
| R6.7 | Checkpoint and evidence dry run | NOT STARTED |
| R6.8 | Instructor contingency and provider fallback validation | NOT STARTED |
| R6.9 | Teaching baseline freeze | NOT STARTED |
