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

## 2. Checkpoint A - Foundations

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

### Example evidence

Maximum recommended screenshots:

```text
3
```

Possible evidence:

1. terminal with repository navigation and Python execution;
2. `git status` and `git log --oneline`;
3. branch and merge evidence.

### Live micro-validation

The instructor may ask for a small modification such as:

```text
create a branch
change displayed information
show git diff
commit the change
run MarketPulse
```

## 3. Checkpoint B - Collaboration and Data

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
- ability to change the selected market pair.

### Example evidence

Maximum recommended screenshots:

```text
3 to 4
```

Possible evidence:

1. Pull Request;
2. code review;
3. Yahoo Finance execution;
4. optional comparison of local and remote data.

### Example oral questions

The instructor may ask:

- Where is Yahoo Finance called?
- What data is returned?
- Where is the benchmark handled?
- Why should processing not depend directly on one provider?
- Can you change the selected ticker and run the application again?

## 4. Checkpoint C - Integration and Release

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
- Dash interface;
- Git collaborative workflow;
- clear contribution history;
- reproducible project execution;
- ability to explain and modify the submitted work.

### Suggested final validation

A short technical demonstration may include:

```text
5 to 8 minutes per team
+
targeted individual questions
```

### Example evidence

Maximum recommended screenshots:

```text
4 to 5
```

Possible evidence:

1. Bloomberg or final market-data retrieval;
2. Dash dashboard;
3. final Pull Request;
4. fresh clone and run;
5. optional advanced deployment evidence.

## 5. Evidence directory

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

The individual directory name should match the student's GitHub username.

## 6. Individual checkpoint README

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

- 01_pull-request.png
- 02_code-review.png
- 03_yahoo-provider.png
```

## 7. Team vs individual validation

For collaborative tasks, a possible interpretation is:

```text
70% individual evidence and understanding
30% collective project result
```

The teaching team may adjust this weighting if needed.

## 8. Assessment dimensions

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

## 9. AI-assisted work

The objective is not to detect whether a tool helped produce code.

Students remain responsible for submitted work.

They must be able to:

- explain it;
- run it;
- modify it;
- debug it;
- identify where their contribution fits.

A live modification is stronger evidence than authorship speculation.

## 10. Security

Screenshots and evidence must never expose:

- passwords;
- API keys;
- GitHub tokens;
- SSH private keys;
- Bloomberg credentials;
- cloud credentials;
- payment information.

## 11. Important distinction

```text
Presence
!=
work
!=
competence
```

Validation is based on demonstrated work and understanding.
