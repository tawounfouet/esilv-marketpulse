# TD05 - Fork + Pull Request

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"Several developers now contribute to the same MarketPulse repository."
```

## Context

During TD01, your team created one shared fork of the instructor repository.

During TD03 and TD04, you learned how to:

- inspect changes;
- create commits;
- create feature branches;
- merge locally.

The next step is collaborative GitHub work.

A feature should now move through:

```text
local feature branch
        |
        v
push to team repository
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

TD05 focuses on:

```text
push
+
remote branch
+
Pull Request
```

Formal code review is developed further in TD06.

## Important repository model

The course uses:

```text
1 team
=
1 shared fork
```

not:

```text
1 student
=
1 fork
```

The instructor repository is:

```text
tawounfouet/esilv-marketpulse
```

The team repository is:

```text
<team-owner>/esilv-marketpulse-gXX-tYY
```

Example:

```text
alice-martin/esilv-marketpulse-g03-t02
```

All team members collaborate in that same team repository.

Do not create additional individual forks for TD05.

## Learning objectives

At the end of TD05, you should be able to:

- explain the difference between a local branch and a remote branch;
- inspect configured Git remotes;
- identify `origin`;
- create a local feature branch;
- push the branch to the team repository;
- understand upstream tracking;
- open a Pull Request;
- identify source and target branches;
- write a clear Pull Request title and description;
- connect a Pull Request to an individual student contribution;
- explain why feature work is not developed directly on `main`.

## Expected result

Each student should be able to demonstrate:

```text
main
  |
  +-- feature/<description>
          |
          v
       local commit
          |
          v
        git push
          |
          v
GitHub remote branch
          |
          v
Pull Request
          |
          v
team main
```

By the end of TD05:

```text
[ ] one feature branch created
[ ] at least one meaningful commit created
[ ] feature branch pushed to GitHub
[ ] Pull Request opened
[ ] PR title is clear
[ ] PR description explains the change
[ ] source and target branches are understood
[ ] MarketPulse still runs
```

## Prerequisites

Before starting:

```text
[ ] TD01-TD04 completed
[ ] Checkpoint A completed or ready
[ ] team repository accessible
[ ] all team members are collaborators
[ ] git status understood
[ ] commits understood
[ ] branches understood
[ ] local merge understood
[ ] MarketPulse runs
```

Before creating any TD05 feature branch, complete the Team Baseline Gate below.

## Team Baseline Gate

TD03 and TD04 intentionally allowed local learning histories.

Different students may therefore have different local `main` commits.

TD05 must not begin until the team has one shared remote baseline.

### Gate rule

```text
one team
=
one validated origin/main
=
one starting point for all TD05 branches
```

The instructor or designated team integrator controls this handoff.

Do not improvise merges or rebases between divergent student histories.

### Step 1 - Capture Checkpoint A first

If Checkpoint A evidence is still needed, capture it before realigning local `main`.

Your local TD03-TD04 history may be useful for:

```text
02_git_status_log.png
03_branch_merge.png
```

### Step 2 - Make every local working tree safe

Each student runs:

```bash
git switch main
git status
```

Do not continue with uncommitted work.

If meaningful local work still exists, commit it or ask the instructor what to preserve.

### Step 3 - Preserve the local TD04 history

Before alignment, each student creates a local safety branch:

```bash
git branch archive/td04-local
```

This branch is local safety material.

Do not push it unless the instructor explicitly asks you to.

### Step 4 - Select the team baseline

The instructor or designated integrator selects one validated local `main`.

The selected baseline must satisfy:

```text
[ ] TEAM.md is correct
[ ] MarketPulse runs
[ ] required starter files are present
[ ] no temporary conflict-demo file remains
[ ] working tree is clean
```

Verify:

```bash
python src/main.py
git status
```

### Step 5 - Verify origin before publishing

On the selected baseline environment:

```bash
git remote get-url origin
```

It must point to:

```text
<team-owner>/esilv-marketpulse-gXX-tYY
```

If it points elsewhere, stop and ask the instructor.

### Step 6 - Publish the validated baseline

Only the selected integrator publishes the baseline:

```bash
git switch main
git push origin main
```

At this point:

```text
origin/main
=
official TD05 team baseline
```

### Step 7 - Align every other student

Each other student runs, under instructor guidance:

```bash
git switch main
git status
git fetch origin
git reset --hard origin/main
```

The `reset --hard` step is permitted here only because:

```text
working tree was checked clean
+
archive/td04-local preserves the previous local history
+
the instructor controls the synchronization
```

Do not use `git reset --hard` casually outside this controlled handoff.

If the instructor prefers not to use reset, opening a fresh Codespace or fresh clone from the team repository after the baseline is published is an acceptable alternative.

### Step 8 - Verify common HEAD

Each student runs:

```bash
git status
git rev-parse HEAD
git rev-parse origin/main
python src/main.py
```

For each student:

```text
HEAD
=
origin/main
```

and MarketPulse must run.

### Baseline Gate definition of done

TD05 feature work may start only when:

```text
[ ] origin points to the team repository
[ ] one validated origin/main exists
[ ] every student starts from that same origin/main
[ ] every working tree is clean
[ ] MarketPulse runs for every student
[ ] previous local TD04 history was preserved before destructive alignment
```

This gate is not an advanced Git-history lesson.

Its purpose is to remove hidden divergence before collaborative branch and Pull Request work begins.

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | Local vs remote Git |
| 10-20 min | Inspect origin and team repository |
| 20-35 min | Create a feature branch |
| 35-50 min | Implement and commit a MarketPulse change |
| 50-65 min | Push the branch |
| 65-80 min | Open a Pull Request |
| 80-90 min | PR validation and recap |

# Part 1 - Local repository vs remote repository

Until now, most Git work has been local.

You now need to distinguish:

```text
LOCAL
working directory
staging area
commits
branches

REMOTE
GitHub team repository
remote branches
Pull Requests
```

A simplified model is:

```text
Local computer or Codespace
        |
        | git push
        v
GitHub team repository
```

## 1.1 Inspect remotes

Run:

```bash
git remote -v
```

You should see a remote called:

```text
origin
```

Conceptually:

```text
origin
=
your team repository
```

Example:

```text
<team-owner>/esilv-marketpulse-g03-t02
```

Question:

> Why should `origin` point to the team repository rather than directly to the instructor repository?

# Part 2 - Understand origin and upstream

For the course model:

```text
origin
=
team repository

upstream
=
instructor repository
```

The instructor repository is:

```text
tawounfouet/esilv-marketpulse
```

You may not yet have an `upstream` remote configured.

That is acceptable.

TD05 mainly uses:

```text
origin
```

Advanced synchronization with `upstream` is not required today.

## 2.1 Verify origin

Run:

```bash
git remote get-url origin
```

Check that the URL corresponds to your team repository.

If it does not, stop and ask the instructor before pushing.

# Part 3 - Create a feature branch

## 3.1 New business request

The trading desk wants a clearer terminal summary.

Implement a small improvement such as:

```text
Display the market and currency metadata
for the instrument and benchmark.
```

Example target:

```text
Instrument
AAPL - Apple Inc.
Market       : NASDAQ
Currency     : USD
Observations : 21

Benchmark
SP500 - S&P 500
Market       : US
Currency     : USD
Observations : 21
```

Do not calculate returns yet.

## 3.2 Start from main

Run:

```bash
git switch main
git status
```

Make sure the working tree is clean.

## 3.3 Create a branch

Use:

```bash
git switch -c feature/display-market-metadata
```

Verify:

```bash
git branch
```

Expected shape:

```text
* feature/display-market-metadata
  main
```

# Part 4 - Implement the change

Modify:

```text
src/main.py
```

Use the existing metadata already present in:

```text
data/sample/instruments.json
```

The values include:

```text
ticker
name
currency
market
```

Keep the implementation simple.

Do not duplicate large blocks of output code if a reusable function already exists.

## 4.1 Run MarketPulse

Run:

```bash
python src/main.py
```

Verify that the new information appears for both the instrument and benchmark.

## 4.2 Inspect the diff

Run:

```bash
git status
git diff
```

Explain your change to another team member before staging it.

# Part 5 - Commit the feature

Stage the intended file:

```bash
git add src/main.py
```

Inspect:

```bash
git diff --staged
```

Commit:

```bash
git commit -m "feat: display market metadata"
```

Use a message that matches your actual implementation.

Verify:

```bash
git status
git log --oneline -5
```

# Part 6 - Push the branch

The local branch does not automatically exist on GitHub.

Push it:

```bash
git push -u origin feature/display-market-metadata
```

The `-u` option connects the local branch to its remote tracking branch.

After this first push, later pushes may usually use:

```bash
git push
```

## 6.1 Verify tracking

Run:

```bash
git branch -vv
```

You should see information indicating that the local feature branch tracks a remote branch.

## 6.2 Verify on GitHub

Open the team repository on GitHub.

Confirm that the branch exists remotely.

You should be able to distinguish:

```text
local branch
vs
remote branch
```

# Part 7 - Open a Pull Request

A Pull Request proposes integrating one branch into another.

For TD05:

```text
source
=
feature/display-market-metadata

target
=
main
```

## 7.1 Open the Pull Request

On GitHub:

1. open the team repository;
2. select the pushed feature branch if necessary;
3. choose to create a Pull Request;
4. verify the base branch is `main`;
5. verify the compare branch is your feature branch.

Do not create the PR against the instructor repository.

The Pull Request belongs inside the team repository.

## 7.2 Pull Request title

Use a clear title.

Recommended:

```text
feat: display market metadata
```

Avoid:

```text
PR
my work
changes
final
test
```

## 7.3 Pull Request description

A useful description should answer:

```text
What changed?
Why was it needed?
How was it validated?
```

Example:

```markdown
## What changed

- display market metadata for the instrument;
- display market metadata for the benchmark.

## Why

The terminal summary should provide clearer context about each market series.

## Validation

- ran `python src/main.py`;
- verified AAPL and SP500 output;
- verified 21 observations for each series.
```

Do not copy the example blindly if your implementation differs.

# Part 8 - Understand source and target

A Pull Request has two important sides.

```text
source branch
      |
      v
Pull Request
      |
      v
target branch
```

For this TD:

```text
feature/display-market-metadata
      |
      v
Pull Request
      |
      v
main
```

Questions:

1. Which branch contains your proposed change?
2. Which branch receives the change after merge?
3. Why should the source branch not be `main`?
4. Why should you inspect both branch names before opening the PR?

# Part 9 - Individual traceability

A Pull Request is part of your individual Git trace.

It makes visible:

- author;
- branch;
- commits;
- changed files;
- discussion;
- review;
- merge status.

Each student should eventually have identifiable:

```text
commits
+
branches
+
Pull Requests
+
reviews
```

Do not create a Pull Request under another student's account to simulate contribution.

# Part 10 - Add another commit to an open PR

A Pull Request follows the branch.

It is not a frozen copy of the branch.

Make one small justified improvement on the same feature branch.

For example:

- improve a label;
- correct formatting;
- remove an unnecessary blank line.

Then:

```bash
git status
git diff
git add src/main.py
git commit -m "refactor: improve market metadata display"
git push
```

Refresh the Pull Request on GitHub.

Question:

> Did you need to create a second Pull Request?

No.

The new commit appears in the existing Pull Request because the PR follows the source branch.

# Part 11 - Do not merge immediately

TD05 focuses on opening and understanding the Pull Request.

Formal review is the main topic of TD06.

Unless the instructor asks otherwise:

```text
leave the Pull Request open
```

at the end of TD05.

This gives another student something real to review in TD06.

# Part 12 - Pull Request quality checklist

Before finishing, verify:

```text
[ ] title is meaningful
[ ] description explains the change
[ ] source branch is correct
[ ] target branch is main
[ ] commits are understandable
[ ] changed files are expected
[ ] no secret is exposed
[ ] MarketPulse runs
```

## Inspect the Files changed tab

Open:

```text
Files changed
```

Question:

> Does the Pull Request contain only the intended feature?

If unrelated changes appear, investigate before requesting review.

# Part 13 - Relationship with Checkpoint B

Checkpoint B is performed after TD08.

One required screenshot is:

```text
01_pull_request.png
```

The screenshot must make visible:

- Pull Request title;
- author;
- source branch;
- target branch;
- relevant status.

Do not submit Checkpoint B yet.

TD05 teaches the workflow that this evidence will later demonstrate.

# Part 14 - Common mistakes

## Mistake 1 - Developing directly on main

Incorrect:

```text
main
  |
  v
edit
  |
  v
commit
  |
  v
push
```

Expected from TD04 onward:

```text
main
  |
  v
feature branch
  |
  v
edit
  |
  v
commit
  |
  v
push
```

## Mistake 2 - Opening the PR against the instructor repository

Your team PR should normally target:

```text
team repository main
```

not:

```text
tawounfouet/esilv-marketpulse main
```

## Mistake 3 - One Pull Request containing unrelated work

A PR should represent one coherent change.

Avoid mixing:

```text
feature
+
random documentation
+
temporary debug code
+
unrelated data changes
```

## Mistake 4 - Vague title

Avoid:

```text
changes
work
update
```

Prefer:

```text
feat: display market metadata
```

# Part 15 - Git commands recap

You should now understand:

```bash
git remote -v
git remote get-url origin
git switch main
git switch -c feature/<description>
git status
git diff
git add
git commit
git push -u origin <branch>
git push
git branch -vv
git log --oneline
```

You should also understand the GitHub concepts:

```text
remote branch
Pull Request
source branch
target branch
Files changed
PR description
```

# Part 16 - Mini exercises

## Exercise 1 - Identify origin

Run:

```bash
git remote -v
```

Write down:

```text
origin repository
```

Confirm that it is the team repository.

## Exercise 2 - Inspect tracking

Run:

```bash
git branch -vv
```

Identify which remote branch your feature branch tracks.

## Exercise 3 - Explain your PR

To another team member, explain:

```text
business requirement
branch name
main commit
files changed
validation performed
```

## Exercise 4 - Find your branch on GitHub

Without using your local terminal, use GitHub to identify:

- your feature branch;
- its latest commit;
- its open Pull Request.

# Part 17 - If you finish early

## Challenge 1 - Inspect remote branches

Run:

```bash
git branch -r
```

Identify remote branches under:

```text
origin/
```

## Challenge 2 - Inspect all branches

Run:

```bash
git branch -a
```

Compare local and remote branch names.

## Challenge 3 - Compare main with your feature

Run:

```bash
git diff main..feature/display-market-metadata
```

Then compare with the GitHub `Files changed` view.

## Challenge 4 - Inspect commit range

Try:

```bash
git log --oneline main..feature/display-market-metadata
```

Question:

> Which commits exist on the feature branch but not on main?

# Part 18 - Troubleshooting

## Push rejected

Check:

```bash
git status
git branch
git remote -v
```

Make sure:

- you are on the expected branch;
- `origin` is the team repository;
- you have collaborator access.

## Permission denied

Verify that:

- you are authenticated with your own GitHub account;
- the fork owner added you as a collaborator;
- you accepted the invitation.

Do not share another student's credentials.

## Wrong remote repository

Run:

```bash
git remote get-url origin
```

If it points somewhere unexpected, stop before pushing.

Ask the instructor for help.

## Pull Request contains unexpected files

Inspect locally:

```bash
git status
git log --oneline
git diff main..HEAD
```

Then inspect the GitHub `Files changed` tab.

## Pull Request targets the wrong repository or branch

Do not merge it.

Correct the target if GitHub allows it, or ask the instructor before recreating the PR.

# Part 19 - Readiness check

Before finishing TD05, each student should be able to explain:

```text
[ ] local branch
[ ] remote branch
[ ] origin
[ ] git push
[ ] upstream tracking
[ ] Pull Request
[ ] source branch
[ ] target branch
[ ] PR title
[ ] PR description
```

Each student should also confirm:

```text
[ ] I created an identifiable feature branch
[ ] I created at least one commit
[ ] I pushed my branch to the team repository
[ ] I opened a Pull Request
[ ] my Pull Request targets team main
[ ] my Pull Request contains only intended changes
[ ] MarketPulse still runs
```

# Part 20 - What comes next?

In TD06, the business requirement becomes:

```text
"Changes must be reviewed before integration."
```

You will use the Pull Requests created in TD05 to practice:

```text
review
+
comment
+
request changes
+
approval
+
merge
```

From that point, collaborative MarketPulse development will follow the complete workflow:

```text
feature branch
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
```
