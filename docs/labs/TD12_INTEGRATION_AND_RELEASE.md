# TD12 - Integration + Release

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"We need a reproducible version of MarketPulse that another person can run."
```

## Context

MarketPulse has progressively evolved through the complete practical sequence.

You now have experience with:

```text
Linux
Python
CSV / JSON
Git
branches
Pull Requests
code review
data normalization
instrument / benchmark comparison
Yahoo Finance
Bloomberg
Dash
```

TD12 closes the practical sequence.

The objective is not to add another major feature.

The objective is to make the existing application:

```text
integrated
+
documented
+
reviewed
+
reproducible
+
demonstrable
```

A project is not complete only because it works on one student's environment.

Another person should be able to understand the repository, install its dependencies, run MarketPulse and verify the main result.

## Learning objectives

At the end of TD12, you should be able to:

- verify the complete MarketPulse architecture;
- confirm the final provider path;
- identify and remove temporary development artefacts;
- review direct dependencies;
- improve execution documentation;
- perform a fresh reproducibility test;
- create a final integration Pull Request;
- review and merge final changes;
- prepare Checkpoint C evidence;
- explain the full MarketPulse workflow from provider to dashboard;
- distinguish the guided MarketPulse project from the separate final project.

## Expected result

At the end of TD12, the team repository should provide a coherent path from:

```text
clone repository
      |
      v
install dependencies
      |
      v
select / confirm provider
      |
      v
run MarketPulse
      |
      v
open dashboard
      |
      v
verify instrument vs benchmark comparison
```

The final CORE application should demonstrate:

```text
1 Instrument
+
1 Benchmark
+
1 Provider
+
1 month lookback
+
Daily interval
+
Period returns
+
Relative performance
+
Base-100 comparison
+
Dash dashboard
```

## Core completion rule

TD12 is primarily an integration and release session.

Do not start a large new feature.

Priority order:

```text
1. working application
2. reproducible setup
3. clear documentation
4. clean Git history
5. complete evidence
6. optional polish
```

## Prerequisites

Before starting:

```text
[ ] TD01-TD11 completed
[ ] team main is up to date
[ ] MarketPulse terminal path works
[ ] Dash dashboard works
[ ] selected provider path works
[ ] instrument and benchmark comparison works
[ ] Pull Request workflow is understood
[ ] code review workflow is understood
```

Update local main:

```bash
git switch main
git pull
git status
```

Start from a clean working tree.

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | Final architecture review |
| 10-25 min | Repository cleanup and dependency check |
| 25-42 min | README and execution documentation |
| 42-60 min | Fresh reproducibility test |
| 60-72 min | Final integration Pull Request |
| 72-82 min | Review, merge and final run |
| 82-90 min | Checkpoint C preparation |

# Part 1 - Review the final architecture

Before changing anything, explain the current architecture as a team.

Target:

```text
CSV -----------+
               |
Yahoo ---------+--> canonical market data
               |
Bloomberg -----+
                       |
                       v
                 date alignment
                       |
                       v
                 period return
                 daily return
                 base 100
                 relative performance
                       |
                       v
                 dashboard data
                       |
                       v
                     Dash
                       |
                       v
                     User
```

Each student should be able to explain where:

```text
provider-specific code
canonical data
analytics
presentation
```

belong.

# Part 2 - Confirm the final provider

The final provider used for the release must be explicit.

Preferred path when available:

```text
Bloomberg
```

If Bloomberg is not available for technical or organizational reasons, use only the provider authorized by the instructor.

Do not silently change provider and claim Bloomberg execution.

Record the final provider in the README.

Example:

```text
Final provider: Bloomberg
```

or, if authorized:

```text
Final provider: Yahoo Finance
Reason: Bloomberg classroom access unavailable during final validation
```

Accuracy is more important than pretending that every environment behaved identically.

# Part 3 - Create the final integration branch

Create:

```bash
git switch main
git pull
git switch -c feature/final-integration
```

Verify:

```bash
git branch
git status
```

The branch should contain only final integration, documentation and release-readiness changes.

# Part 4 - Inspect the repository

Review the project tree.

Useful commands:

```bash
find . -maxdepth 3 -type f | sort
```

or:

```bash
find . -type f | sort
```

Inspect for:

- temporary files;
- debug output;
- obsolete practice files;
- duplicated scripts;
- accidental screenshots outside evidence folders;
- credentials;
- files that should be ignored.

## 4.1 Git status

Run:

```bash
git status
```

The integration branch should begin clean.

## 4.2 Search for temporary debug code

Review the Python files.

Look for examples such as:

```python
print(type(...))
print(history.head())
print("DEBUG")
```

Keep useful application output.

Remove temporary inspection output that no longer belongs in the final flow.

# Part 5 - Review the target repository structure

The frozen CORE application structure is:

```text
esilv-marketpulse/
├── README.md
├── TEAM.md
├── CONTRIBUTING.md
├── requirements.txt
├── .gitignore
├── config/
│   └── settings.yml
├── data/
│   └── sample/
├── src/
│   ├── main.py
│   ├── analytics.py
│   ├── dashboard.py
│   └── providers/
│       ├── __init__.py
│       ├── yahoo_provider.py
│       └── bloomberg_provider.py
├── evidence/
│   ├── checkpoint-a/
│   ├── checkpoint-b/
│   └── checkpoint-c/
└── docs/
```

This is the common CORE reference defined in `docs/05_TARGET_REPOSITORY_STRUCTURE.md`.

Do not reorganize the project into a more complex package during TD12.

A more formal `src/marketpulse/` package is an optional professional evolution, not a release requirement.

# Part 6 - Review requirements.txt

Open:

```text
requirements.txt
```

Verify that the direct dependencies actually used by the project are present.

Depending on the implemented path, examples may include:

```text
yfinance
dash
plotly
```

Bloomberg-specific dependencies must match the instructor-approved environment.

Do not add packages that are not imported or required.

## 6.1 Test installation command

The documented installation command should be:

```bash
python -m pip install -r requirements.txt
```

Do not rely on packages that happen to be installed globally on one student's machine.

# Part 7 - Review .gitignore

Confirm that the project does not track local or sensitive artefacts.

Typical ignored elements include:

```text
__pycache__/
*.pyc
.venv/
venv/
.env
data/raw/
data/processed/
```

Do not blindly ignore files that are required by the starter or evidence contract.

Check before changing `.gitignore`.

# Part 8 - Improve the README

The root `README.md` should allow another student or evaluator to understand and run the project.

At minimum, include sections equivalent to:

```text
Project purpose
Architecture
Market pair
Provider
Requirements
Installation
Run terminal version
Run dashboard
Expected result
Team
Evidence
Known environment constraints
```

## 8.1 Suggested README structure

```markdown
# MarketPulse

## Purpose

MarketPulse compares one financial instrument with one benchmark over a common historical window.

## Market pair

- Instrument: AAPL - Apple Inc.
- Benchmark: S&P 500

## Core contract

- Lookback: 1 month
- Interval: Daily
- Provider: <final provider>

## Architecture

<short diagram>

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

Terminal:

```bash
python src/main.py
```

Dashboard:

```bash
python src/dashboard.py
```

## Expected result

- instrument return;
- benchmark return;
- relative performance;
- base-100 comparison chart.

## Team

See `TEAM.md`.

## Evidence

See `evidence/`.
```

Adapt this to your actual implementation.

Do not document commands that do not work.

# Part 9 - Document environment constraints

If Bloomberg requires a specific environment, document it clearly.

Example concept:

```text
Bloomberg execution requires the ESILV Bloomberg-enabled environment.

Without that environment, the application can still demonstrate the shared architecture using the instructor-authorized fallback provider.
```

Do not publish credentials or internal access secrets.

# Part 10 - Run the terminal path

Before the reproducibility test, run:

```bash
python src/main.py
```

Verify:

```text
[ ] provider is correct
[ ] instrument is correct
[ ] benchmark is correct
[ ] lookback is 1 month
[ ] interval is Daily
[ ] instrument return is displayed
[ ] benchmark return is displayed
[ ] relative performance is displayed
[ ] no debug output remains
```

# Part 11 - Run the dashboard path

Run:

```bash
python src/dashboard.py
```

Verify:

```text
[ ] dashboard loads
[ ] provider is visible
[ ] instrument is visible
[ ] benchmark is visible
[ ] lookback is visible
[ ] interval is visible
[ ] instrument return is visible
[ ] benchmark return is visible
[ ] relative performance is visible
[ ] base-100 chart contains both series
```

# Part 12 - Perform a fresh reproducibility test

A reproducibility test should simulate a person who does not have your working directory history.

Use a new directory or fresh environment.

Do not destroy your current repository.

A typical sequence is:

```bash
cd ..
git clone <team-repository-url> marketpulse-repro
cd marketpulse-repro
python -m pip install -r requirements.txt
python src/main.py
```

Then, if supported in the environment:

```bash
python src/dashboard.py
```

## Important

If your final unmerged integration work is not yet on `main`, test the relevant remote branch or perform the final clean test after merge.

The final Checkpoint C reproducibility evidence should reflect the final integrated version.

# Part 13 - What reproducibility means

Reproducibility does not mean:

```text
"It works on my machine."
```

It means another person can follow documented steps and obtain a functioning project under the documented environment assumptions.

The reproducibility contract includes:

```text
repository
+
dependencies
+
configuration
+
commands
+
provider prerequisites
+
expected result
```

# Part 14 - Fix reproducibility problems

Typical problems include:

```text
missing dependency
wrong import path
undocumented configuration
hard-coded local path
missing file
provider-specific assumption
README command mismatch
```

Fix the cause.

Do not solve the test by manually editing the fresh clone without documenting the required change.

# Part 15 - Final integration diff

Return to your integration branch.

Run:

```bash
git status
git diff
```

Review every changed file.

Ask:

1. Is this change required for final integration?
2. Is it understandable?
3. Is it safe?
4. Is it documented?
5. Does it preserve the MarketPulse business contract?

# Part 16 - Final commit

Stage only intended files.

Example:

```bash
git add README.md
git add requirements.txt
git add src/
```

Use more precise paths when possible.

Inspect:

```bash
git diff --staged
```

Create a meaningful commit.

Example:

```bash
git commit -m "chore: prepare MarketPulse final release"
```

Push:

```bash
git push -u origin feature/final-integration
```

# Part 17 - Open the final Pull Request

Suggested title:

```text
chore: prepare MarketPulse final release
```

Suggested description:

```markdown
## What changed

- finalize MarketPulse integration;
- clean temporary development artefacts;
- verify direct dependencies;
- update execution documentation;
- prepare reproducible run instructions.

## Validation

- ran terminal application;
- ran Dash dashboard;
- verified instrument and benchmark comparison;
- performed fresh setup test;
- verified evidence structure.

## Final provider

<provider used>

## Known environment constraints

<document only real constraints>
```

# Part 18 - Final code review

Another student reviews the final Pull Request.

The reviewer should verify:

```text
[ ] README commands match the repository
[ ] requirements.txt is sufficient
[ ] no secrets are committed
[ ] no temporary debug files remain
[ ] provider is documented accurately
[ ] terminal path works
[ ] dashboard path works
[ ] instrument and benchmark are both present
[ ] base-100 comparison remains available
[ ] evidence structure is preserved
```

Do not merge merely because this is the last TD.

The final Pull Request should receive a real review.

# Part 19 - Merge and synchronize

After approval, merge the Pull Request.

Then locally:

```bash
git switch main
git pull
git status
git log --oneline -5
```

Run again:

```bash
python src/main.py
```

and:

```bash
python src/dashboard.py
```

The final validation must be performed from the merged version.

# Part 20 - Checkpoint C

Checkpoint C closes the practical sequence.

It validates integration and release readiness.

## 20.1 Evidence directory

Each student uses:

```text
evidence/checkpoint-c/<github-username>/
```

## 20.2 Required files

Exactly these files are required:

```text
README.md
01_final_market_data.png
02_dash_dashboard.png
03_final_pull_request.png
04_reproducible_run.png
```

Optional:

```text
05_advanced_deployment.png
```

Do not rename the files.

# Part 21 - 01_final_market_data.png

This screenshot demonstrates the final market-data provider path.

When Bloomberg is available and authorized, it should show Bloomberg-based MarketPulse execution.

The screenshot should make understandable:

```text
provider
instrument
benchmark
lookback
interval
```

If the instructor authorizes a fallback provider, use the same generic filename:

```text
01_final_market_data.png
```

Document the actual provider honestly in the individual README.

Do not fabricate Bloomberg evidence.

# Part 22 - 02_dash_dashboard.png

This screenshot must show the functional comparative dashboard.

At minimum:

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

The screenshot should make the comparison understandable without requiring hidden context.

# Part 23 - 03_final_pull_request.png

Show a final or late-stage Pull Request demonstrating the collaborative workflow.

The screenshot should make visible:

```text
PR title
author
source branch
target branch
status
```

The PR should correspond to identifiable contribution by the student.

# Part 24 - 04_reproducible_run.png

This screenshot demonstrates that the final project can be executed from a fresh or clean setup.

Useful visible commands may include:

```bash
git clone <team-repository-url>
cd esilv-marketpulse-gXX-tYY
python -m pip install -r requirements.txt
python src/main.py
```

The exact command set may depend on the environment.

The screenshot should clearly demonstrate a clean execution path, not merely an already-running development session.

# Part 25 - Optional 05_advanced_deployment.png

This file is optional.

It may demonstrate an advanced extension such as:

```text
SSH
VPS
systemd
Docker
GitHub Actions
```

These advanced topics are not required for full CORE completion.

Do not use Kubernetes for the CORE project.

Do not require paid cloud infrastructure for the mandatory grade.

# Part 26 - Checkpoint C README

Create:

```text
evidence/checkpoint-c/<github-username>/README.md
```

Suggested structure:

```markdown
# Checkpoint C

## Student

- Name: Alice Martin
- GitHub: @alice-martin

## Contribution

- Branch: feature/final-integration
- Main commits:
  - <commit-id>
- Final Pull Request: #...
- Reviewed Pull Request: #...

## Final provider

<provider actually used>

## Work completed

Briefly explain your contribution to the final integration.

## Main difficulty

Briefly explain one technical or collaborative difficulty.

## Reproducibility

Describe the fresh-run procedure you validated.

## Evidence

- 01_final_market_data.png
- 02_dash_dashboard.png
- 03_final_pull_request.png
- 04_reproducible_run.png
- 05_advanced_deployment.png if used
```

# Part 27 - Checkpoint C live validation

Screenshots do not replace execution and explanation.

The instructor may ask you to:

```text
run MarketPulse
run the dashboard
change or identify the provider
explain instrument / benchmark mapping
explain base 100
show your final Pull Request
show a code review
explain one commit
explain the fresh-run process
modify a small part of the application
```

You should be able to explain the code you submit.

# Part 28 - AI-assisted work

AI tools may have been used during development.

The assessment does not require guessing whether code was produced with AI.

Students remain responsible for the submitted work.

You should be able to:

```text
explain it
run it
modify it
debug it
justify it
```

A repository that works but cannot be explained does not demonstrate the same level of mastery as understood and reproducible work.

# Part 29 - Final CORE checklist

Before finishing TD12, verify:

## Environment

```text
[ ] repository can be cloned
[ ] dependencies can be installed
[ ] no secret is required from Git history
```

## Data

```text
[ ] one instrument is configured
[ ] one benchmark is configured
[ ] provider is explicit
[ ] lookback is 1 month
[ ] interval is Daily
[ ] common dates are handled
```

## Analytics

```text
[ ] instrument period return works
[ ] benchmark period return works
[ ] relative performance works
[ ] base-100 series works
```

## Dashboard

```text
[ ] instrument visible
[ ] benchmark visible
[ ] lookback visible
[ ] interval visible
[ ] returns visible
[ ] relative performance visible
[ ] base-100 chart visible
```

## Git

```text
[ ] feature branches used
[ ] commits are attributable
[ ] Pull Requests used
[ ] reviews performed
[ ] final integration reviewed
```

## Evidence

```text
[ ] checkpoint-c README exists
[ ] 01_final_market_data.png exists
[ ] 02_dash_dashboard.png exists
[ ] 03_final_pull_request.png exists
[ ] 04_reproducible_run.png exists
[ ] filenames are exact
```

# Part 30 - Full learning path recap

You have now completed:

```text
WAVE 1 - Foundations

TD01 - Bootstrap + Linux
TD02 - Python + CSV / JSON
TD03 - Git Local Workflow
TD04 - Branches + Merge
        |
        v
Checkpoint A


WAVE 2 - Collaboration + Data

TD05 - Fork + Pull Request
TD06 - Code Review
TD07 - Data Normalization + Comparison
TD08 - Yahoo Finance
        |
        v
Checkpoint B


WAVE 3 - Professional Integration

TD09 - Bloomberg Introduction
TD10 - Bloomberg Provider
TD11 - Dash Dashboard
TD12 - Integration + Release
        |
        v
Checkpoint C
```

Total practical time:

```text
12 TD x 1h30
=
18 hours
```

# Part 31 - MarketPulse final mental model

The final project should be understandable through this model:

```text
Provider
   |
   v
Market data acquisition
   |
   v
Canonical rows
   |
   v
Instrument / benchmark alignment
   |
   v
Analytics
   |
   +-- Period return
   +-- Daily return
   +-- Base 100
   +-- Relative performance
   |
   v
Dashboard data
   |
   v
Dash
   |
   v
User
```

Git surrounds the complete lifecycle:

```text
branch
  |
  v
commit
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
  |
  v
release-ready main
```

# Part 32 - MarketPulse vs Final Project

MarketPulse is the guided practical thread used throughout the 18 hours of TD.

It supports the lab-work component of the module.

The separate final project remains an autonomous assessment.

The final project should reuse and extend the principles learned through MarketPulse, but it should not be reduced to simply submitting the guided classroom repository unchanged.

Students should be able to transfer:

```text
Python
Git
Linux
market-data access
provider separation
data normalization
comparison logic
Dash
reproducibility
collaboration
```

to the final project context.

# Part 33 - Final readiness questions

Before leaving the practical sequence, each student should be able to answer:

1. What problem does MarketPulse solve?
2. Why does the application compare an instrument with a benchmark?
3. Why is base 100 useful?
4. What is relative performance?
5. What is the difference between a canonical ticker and a provider identifier?
6. Why should provider-specific code remain outside analytics?
7. What is the difference between a local branch and a remote branch?
8. Why do we use Pull Requests?
9. What makes a code review meaningful?
10. What makes a project reproducible?
11. How do you run MarketPulse from a fresh repository?
12. Which part of the project did you personally contribute to?

If you can answer and demonstrate these points, you have completed the CORE MarketPulse practical path.
