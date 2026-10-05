# Checkpoints and Evidence

## 1. Purpose

The goal is not to grade every lab independently.

Student progress is validated through three structured checkpoints.

The evidence model combines:

```text
ARTEFACT
+
GIT TRACE
+
SCREENSHOTS
+
EXECUTION
+
EXPLANATION
```

Screenshots alone are never sufficient proof of understanding.

## 2. Global evidence rules

All students must use the same evidence naming convention.

Rules:

```text
format          : PNG
naming          : lowercase_snake_case
numbering       : 01_, 02_, 03_...
spaces          : forbidden
accents         : forbidden
free naming     : forbidden
```

Each student stores evidence under their own GitHub username.

Example:

```text
evidence/
└── checkpoint-b/
    └── alice-martin/
        ├── README.md
        ├── 01_pull_request.png
        ├── 02_code_review.png
        ├── 03_yahoo_market_data.png
        └── 04_instrument_benchmark.png
```

The exact screenshot filenames defined in this document are part of the submission contract.

## 3. Checkpoint A - Foundations

Recommended timing:

```text
after TD04
```

Suggested weight inside the TD grade:

```text
25%
```

### Skills validated

- access to the team repository;
- Linux navigation;
- Python starter execution;
- CSV / JSON inspection;
- basic Git workflow;
- commits;
- branches;
- simple merge.

### Required screenshots

Exactly these three screenshots are required:

```text
01_terminal_python.png
02_git_status_log.png
03_branch_merge.png
```

#### 01_terminal_python.png

The screenshot should show the student working from the project repository and include evidence such as:

```bash
pwd
ls
python src/main.py
```

It should demonstrate that the student can navigate the Linux environment and execute MarketPulse.

#### 02_git_status_log.png

The screenshot should show:

```bash
git status
git log --oneline
```

The objective is to verify repository state and visible Git history.

#### 03_branch_merge.png

The screenshot should show branch usage and visible merge evidence.

Typical commands may include:

```bash
git branch
git log --oneline --graph
```

The exact command sequence may vary, but the evidence must make the branch and merge understandable.

### Live micro-validation

The instructor may ask for a small modification such as:

```text
create a branch
change displayed information
show git diff
commit the change
run MarketPulse
```

## 4. Checkpoint B - Collaboration and Data

Recommended timing:

```text
after TD08
```

Suggested weight inside the TD grade:

```text
30%
```

### Skills validated

- feature branch;
- push;
- Pull Request;
- useful review;
- identifiable individual contribution;
- CSV / JSON data handling;
- instrument and benchmark handling;
- common data model;
- Yahoo Finance integration;
- ability to change the selected market pair;
- same lookback and interval for instrument and benchmark.

### Required screenshots

Exactly these four screenshots are required:

```text
01_pull_request.png
02_code_review.png
03_yahoo_market_data.png
04_instrument_benchmark.png
```

#### 01_pull_request.png

The screenshot should make visible:

- Pull Request title;
- author;
- source branch;
- target branch;
- relevant status.

The Pull Request must correspond to identifiable work by the student.

#### 02_code_review.png

The screenshot should show a meaningful review performed by the student on another team member's Pull Request.

A reaction alone is not sufficient.

#### 03_yahoo_market_data.png

The screenshot should show MarketPulse retrieving or displaying remote market data through the Yahoo Finance stage of the project.

The evidence should make the selected instrument or market pair understandable.

#### 04_instrument_benchmark.png

The screenshot should show that MarketPulse handles both:

```text
Instrument
+
Benchmark
```

over the same common contract:

```text
Lookback : 1 month
Interval : Daily
```

Example:

```text
AAPL
+
S&P 500
```

If the teaching instructions allow another pair, the screenshot should show the team's selected instrument and its coherent benchmark.

### Example oral questions

The instructor may ask:

- Where is Yahoo Finance called?
- What data is returned?
- Where is the benchmark handled?
- Why must instrument and benchmark use the same period and interval?
- Why should processing not depend directly on one provider?
- Can you change the selected ticker and run the application again?

## 5. Checkpoint C - Integration and Release

Recommended timing:

```text
after TD12
```

Suggested weight inside the TD grade:

```text
45%
```

### Skills validated

- multi-source MarketPulse integration;
- Bloomberg data access when the teaching environment permits;
- instrument and benchmark comparison;
- period returns;
- relative performance;
- base-100 comparison;
- Dash interface;
- Git collaborative workflow;
- clear contribution history;
- reproducible project execution;
- ability to explain and modify the submitted work.

### Required screenshots

Exactly these four screenshots are required:

```text
01_final_market_data.png
02_dash_dashboard.png
03_final_pull_request.png
04_reproducible_run.png
```

One optional advanced screenshot may also be submitted:

```text
05_advanced_deployment.png
```

#### 01_final_market_data.png

The screenshot should show the final authorised market-data provider in operation.

When Bloomberg access is available, Bloomberg should be shown.

The generic filename is intentional so that the teaching team can accept another authorised final provider if Bloomberg access is unavailable for technical or organisational reasons.

#### 02_dash_dashboard.png

The screenshot should show the final MarketPulse dashboard.

At minimum, the visible dashboard should make it possible to identify:

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

The objective is to show a real comparative market view, not only that Dash starts successfully.

#### 03_final_pull_request.png

The screenshot should show a final or late-stage Pull Request that demonstrates the collaborative workflow:

```text
feature branch
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

The contribution must be attributable to the student.

#### 04_reproducible_run.png

The screenshot should demonstrate that MarketPulse can be started from a clean or freshly prepared environment by following the repository documentation.

Typical evidence may include:

```bash
git clone ...
cd esilv-marketpulse-gXX-tYY
...
python ...
```

The exact final command may evolve with the project architecture.

#### 05_advanced_deployment.png

Status:

```text
OPTIONAL
```

This screenshot may demonstrate an optional advanced extension such as:

- SSH;
- remote Linux execution;
- VPS deployment;
- systemd;
- Docker;
- GitHub Actions.

It is not required for the common core and must not penalise students who do not complete the advanced track.

### Suggested final validation

A short technical demonstration may include:

```text
5 to 8 minutes per team
+
targeted individual questions
```

## 6. Official evidence matrix

| Checkpoint | Filename | Status |
|---|---|---|
| A | `01_terminal_python.png` | Required |
| A | `02_git_status_log.png` | Required |
| A | `03_branch_merge.png` | Required |
| B | `01_pull_request.png` | Required |
| B | `02_code_review.png` | Required |
| B | `03_yahoo_market_data.png` | Required |
| B | `04_instrument_benchmark.png` | Required |
| C | `01_final_market_data.png` | Required |
| C | `02_dash_dashboard.png` | Required |
| C | `03_final_pull_request.png` | Required |
| C | `04_reproducible_run.png` | Required |
| C | `05_advanced_deployment.png` | Optional |

Do not rename these files.

## 7. Evidence directory

Use:

```text
evidence/
|
+-- checkpoint-a/
|   +-- github-user-a/
|   +-- github-user-b/
|   +-- github-user-c/
|
+-- checkpoint-b/
|   +-- github-user-a/
|   +-- github-user-b/
|   +-- github-user-c/
|
+-- checkpoint-c/
    +-- github-user-a/
    +-- github-user-b/
    +-- github-user-c/
```

The individual directory name must match the student's GitHub username.

## 8. Individual checkpoint README

Each student checkpoint directory must also contain:

```text
README.md
```

Example:

```markdown
# Checkpoint B

## Student

- Name: Alice Martin
- GitHub: @alice-martin

## Contribution

- Branch: feature/yahoo-provider
- Main commits:
  - abc123
  - def456
- Pull Request: #18
- Reviewed Pull Request: #19

## Work completed

Implemented the Yahoo Finance provider and connected
the instrument and benchmark market data.

## Main difficulty

Handling missing observations between two market series.

## Evidence

- 01_pull_request.png
- 02_code_review.png
- 03_yahoo_market_data.png
- 04_instrument_benchmark.png
```

The filenames listed in the README must exactly match the files in the directory.

## 9. Individual evidence rule

Each student provides their own evidence.

A team should not copy the same personal-contribution screenshot into every student's directory when the screenshot is intended to prove individual work.

Shared application behaviour may naturally look similar across team members, but Git contribution evidence must remain attributable to the individual student.

## 10. Team vs individual validation

For collaborative tasks, a possible interpretation is:

```text
70% individual evidence and understanding
30% collective project result
```

The teaching team may adjust this weighting if needed.

## 11. Assessment dimensions

An indicative rubric may consider:

| Dimension | Indicative share |
|---|---:|
| Technical functionality | 30% |
| Git workflow and contribution | 25% |
| Understanding and explanation | 20% |
| Autonomy | 10% |
| Code organisation and clarity | 10% |
| Collaboration and review | 5% |

These percentages are guidance for checkpoint evaluation and may be adapted by the teaching team.

## 12. AI-assisted work

The objective is not to detect whether a tool helped produce code.

Students remain responsible for submitted work.

They must be able to:

- explain it;
- run it;
- modify it;
- debug it;
- identify where their contribution fits.

A live modification is stronger evidence than authorship speculation.

## 13. Security

Screenshots and evidence must never expose:

- passwords;
- API keys;
- GitHub tokens;
- SSH private keys;
- Bloomberg credentials;
- cloud credentials;
- payment information.

Before committing a screenshot, inspect it carefully.

## 14. Important distinction

```text
Presence
!=
work
!=
competence
```

Validation is based on demonstrated work and understanding.
