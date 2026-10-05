# TD06 - Code Review

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"Changes must be reviewed before integration."
```

## Context

In TD05, each student created a feature branch, pushed it to the team repository and opened a Pull Request.

A Pull Request is not only a technical mechanism for merging code.

It is also a place where another developer can:

- read the proposed change;
- ask questions;
- identify a problem;
- request a correction;
- approve the change;
- verify that the feature is ready to merge.

TD06 introduces this collaborative review step.

The target workflow is now:

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
code review
      |
      v
correction if needed
      |
      v
approval
      |
      v
merge
```

## Learning objectives

At the end of TD06, you should be able to:

- explain the purpose of code review;
- read the files changed in a Pull Request;
- distinguish a comment from an approval;
- identify a useful review comment;
- request a correction when necessary;
- update a Pull Request after feedback;
- approve a Pull Request when it is ready;
- merge an approved Pull Request;
- verify the result on `main`;
- explain why review quality matters more than simply clicking a button.

## Expected result

Each student should complete the following cycle:

```text
review another student's PR
        |
        v
leave meaningful feedback
        |
        v
author updates branch if needed
        |
        v
review again
        |
        v
approve
        |
        v
merge
```

By the end of TD06:

```text
[ ] I reviewed another student's Pull Request
[ ] I left at least one meaningful review comment
[ ] I understand request changes vs approve
[ ] I responded to review feedback on my own PR
[ ] my PR was merged only after review
[ ] I updated local main after merge
[ ] MarketPulse still runs
```

## Prerequisites

Before starting:

```text
[ ] TD05 completed
[ ] I have an open Pull Request
[ ] another team member has an open Pull Request
[ ] my branch was pushed to origin
[ ] my PR targets team main
[ ] MarketPulse runs
```

If your team has too few open Pull Requests, create a small coherent feature branch before starting the review exercise.

## Important rule

A review is not:

```text
"looks good"
"ok"
"nice"
👍
```

A meaningful review should demonstrate that you inspected the change.

Examples:

```text
"The benchmark label is clear, but the same metadata is printed twice.
Could this reuse the existing display function?"

"The new output works for AAPL, but does it also work for SP500?"

"Please run python src/main.py and confirm both series still show 21 observations."
```

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | Why code review matters |
| 10-25 min | Inspect another Pull Request |
| 25-40 min | Write meaningful review feedback |
| 40-55 min | Apply requested changes |
| 55-68 min | Review again and approve |
| 68-78 min | Merge and update local main |
| 78-90 min | Review evidence and recap |

# Part 1 - Understand code review

Code review serves several purposes:

```text
quality
+
shared understanding
+
error detection
+
consistency
+
knowledge transfer
```

The reviewer does not need to rewrite the feature.

The reviewer should verify that the proposed change is:

- understandable;
- relevant to the business requirement;
- limited in scope;
- technically coherent;
- safe to integrate.

## Questions

1. Why is code review useful even if the program already runs?
2. Why should the reviewer be someone other than the author?
3. What could a reviewer detect that the author may not notice?

# Part 2 - Choose a Pull Request to review

Each student reviews another team member's Pull Request.

Do not review your own Pull Request.

A good pairing for a team of three may be:

```text
Student A reviews Student B
Student B reviews Student C
Student C reviews Student A
```

For four students:

```text
A reviews B
B reviews C
C reviews D
D reviews A
```

This keeps review responsibility distributed.

# Part 3 - Read the Pull Request before commenting

Open the Pull Request.

Inspect:

```text
title
description
author
source branch
target branch
commits
Files changed
```

Before writing a comment, answer:

1. What business need does the PR address?
2. Which files changed?
3. Are the changes limited to the intended feature?
4. Does the PR description match the actual diff?
5. Is the implementation understandable?

## 3.1 Inspect Files changed

Use the GitHub:

```text
Files changed
```

view.

Look for:

- unexpected file modifications;
- duplicated logic;
- debug prints;
- unclear variable names;
- accidental formatting changes;
- hard-coded values;
- missing validation.

Do not search for sophisticated problems that are outside the current course level.

The review should remain proportional to the feature.

# Part 4 - Write a meaningful review

## 4.1 Good review comments

A useful comment is:

```text
specific
+
technical
+
actionable
+
respectful
```

Example:

```text
The instrument market is displayed correctly.
Could you also verify the same function handles the benchmark so we avoid duplicated output logic?
```

Another example:

```text
This line reads the metadata correctly, but the label says "Exchange".
The JSON field is "market". Could we keep the vocabulary consistent with the data model?
```

## 4.2 Weak review comments

Avoid:

```text
ok
good
fine
works
nice code
```

These do not show what was inspected.

## 4.3 Ask for validation

A reviewer may request evidence such as:

```bash
python src/main.py
```

The author can answer in the Pull Request discussion:

```text
Validated locally with python src/main.py.
AAPL and SP500 both display correctly.
```

# Part 5 - Use review outcomes

Depending on what you find, the review may conclude with:

```text
Comment
Request changes
Approve
```

## Comment

Use a comment when:

- asking a question;
- suggesting an improvement;
- discussing a detail.

## Request changes

Use request changes when the Pull Request should not be merged yet.

Examples:

- feature does not work;
- benchmark case is broken;
- unintended file is included;
- required correction is missing.

## Approve

Approve when the Pull Request is ready to integrate.

Approval should follow actual inspection.

Do not approve before reading the diff.

# Part 6 - Respond to review feedback

Now return to your own Pull Request.

Read the feedback from your reviewer.

If a correction is requested, stay on the same feature branch.

Verify:

```bash
git branch
```

Make the correction.

Then:

```bash
git status
git diff
python src/main.py
```

If the result is correct:

```bash
git add <changed-file>
git commit -m "fix: address review feedback"
git push
```

Refresh the Pull Request.

The new commit should appear automatically.

## Important concept

You do not create a new Pull Request for every correction.

The Pull Request follows the same source branch.

```text
same feature branch
      |
      +-- initial commit
      |
      +-- review fix commit
      |
      v
same Pull Request
```

# Part 7 - Review again

The reviewer should inspect the updated Pull Request.

Check:

- was the requested correction implemented?
- does the feature still match the original scope?
- does MarketPulse still work?
- are there unexpected new changes?

If the PR is now ready:

```text
Approve
```

Do not approve only because the author says the fix is complete.

Inspect the new diff.

# Part 8 - Merge the Pull Request

After approval, merge the Pull Request into:

```text
team main
```

Do not merge into the instructor repository.

The exact merge button available may depend on repository settings.

The important outcome is:

```text
reviewed feature
      |
      v
team main
```

## 8.1 Verify on GitHub

After merge, confirm that the PR status shows:

```text
Merged
```

The feature should now be visible in the team repository `main` branch.

# Part 9 - Update local main

Your local repository does not automatically update when GitHub `main` changes.

Switch to main:

```bash
git switch main
```

Inspect:

```bash
git status
```

Then update from the team repository:

```bash
git pull
```

Run:

```bash
git log --oneline -5
python src/main.py
```

Question:

> Can you find the merged feature in your local history?

# Part 10 - Delete merged feature branches

After a branch is merged, it may be cleaned up.

On GitHub, the team may delete the remote feature branch.

Locally:

```bash
git branch -d feature/<description>
```

Only delete a branch after confirming its work is integrated.

Do not use force deletion without understanding why.

# Part 11 - Complete workflow recap

The collaborative workflow is now:

```text
main
  |
  v
feature branch
  |
  v
implementation
  |
  v
git diff
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
review by another student
  |
  +-- request changes
  |        |
  |        v
  |     correction
  |        |
  |        v
  |      push
  |        |
  +--------+
  |
  v
approval
  |
  v
merge
  |
  v
updated main
```

This workflow will now be reused for later MarketPulse features.

# Part 12 - Review a real MarketPulse concern

During TD06, the reviewer should check at least one functional point.

Possible questions:

```text
Does the feature work for both instrument and benchmark?

Does the implementation duplicate logic?

Does the output preserve the common lookback and interval?

Does the feature change unrelated files?

Does python src/main.py still work?
```

The objective is to connect Git review to application behaviour.

# Part 13 - Review comments should be attributable

Each student review should be performed with their own GitHub account.

The review history should make visible:

```text
reviewer identity
+
review comment
+
review status
```

Do not ask one student to perform all reviews for the team.

# Part 14 - Relationship with Checkpoint B

Checkpoint B is performed after TD08.

One required screenshot is:

```text
02_code_review.png
```

The screenshot should demonstrate a meaningful review performed by the student.

It should make visible, when possible:

- reviewer identity;
- Pull Request context;
- technical comment or review action.

A reaction alone is not sufficient evidence.

Do not submit Checkpoint B yet.

# Part 15 - Mini review exercise

Choose one already merged or open Pull Request.

Without commenting immediately, write a short private checklist:

```text
[ ] business requirement understood
[ ] source branch identified
[ ] target branch identified
[ ] changed files inspected
[ ] feature works
[ ] no unrelated change
[ ] one technical point verified
```

Only then write your GitHub review.

Question:

> Did the checklist change what you noticed in the Pull Request?

# Part 16 - Review vocabulary

You should now understand:

```text
Pull Request
review
reviewer
author
comment
request changes
approve
merge
Files changed
conversation
source branch
target branch
```

# Part 17 - Common mistakes

## Mistake 1 - Reviewing without opening Files changed

A useful review requires inspecting the actual diff.

## Mistake 2 - Approving your own Pull Request

The review should come from another team member.

## Mistake 3 - Treating code review as personal criticism

Review the code and the change, not the person.

Prefer:

```text
"This condition does not appear to handle the benchmark."
```

Avoid:

```text
"You wrote this badly."
```

## Mistake 4 - Requesting unrelated work

Do not expand a small PR into a large redesign unless the current change truly requires it.

## Mistake 5 - Creating a new PR for a review correction

Update the same feature branch and push again.

## Mistake 6 - Merging before approval

The purpose of TD06 is to establish review before integration.

# Part 18 - If you finish early

## Challenge 1 - Compare commits inside a PR

Inspect the Pull Request commit list.

Explain which commit was:

- initial implementation;
- review correction.

## Challenge 2 - Review commit history

Run:

```bash
git log --oneline --graph --decorate --all
```

Identify the feature integration.

## Challenge 3 - Inspect a merged change

Use:

```bash
git show <commit-id>
```

Explain what changed and why.

## Challenge 4 - Write a better review

Take a weak comment such as:

```text
Looks good.
```

Rewrite it into a comment that demonstrates actual inspection.

# Part 19 - Troubleshooting

## No open Pull Request to review

Coordinate within the team.

A student who finished TD05 should leave a coherent Pull Request open for TD06.

If necessary, create a small feature branch and PR before continuing.

## Cannot review or approve

Check that:

- you are signed into your own GitHub account;
- you have collaborator access;
- you are not reviewing your own PR.

## New commit does not appear in the PR

Check:

```bash
git branch
git status
git remote -v
git push
```

Make sure you pushed to the branch used by the Pull Request.

## Local main does not contain the merged feature

Run:

```bash
git switch main
git pull
git log --oneline -5
```

## Merge creates unexpected result

Run:

```bash
python src/main.py
git status
git log --oneline --graph --decorate --all
```

Do not start another feature until the team understands the repository state.

# Part 20 - Readiness check

Before finishing TD06, each student should be able to explain:

```text
[ ] why code review exists
[ ] how to inspect Files changed
[ ] what a useful review comment looks like
[ ] comment vs request changes
[ ] request changes vs approve
[ ] how to update an open Pull Request
[ ] why the same PR follows new commits
[ ] when a Pull Request is ready to merge
[ ] how to update local main after merge
```

Each student should also confirm:

```text
[ ] I reviewed another student's Pull Request
[ ] my review contained meaningful technical feedback
[ ] I responded to review feedback on my own PR
[ ] my feature was reviewed before merge
[ ] I can find the merged feature in Git history
[ ] MarketPulse still runs
```

# Part 21 - What comes next?

Pedagogical Wave 2 is now complete:

```text
Wave 2 - Git and Collaboration - 6 hours

TD03 - Git Local Workflow
TD04 - Branches + Merge
TD05 - Remote Branch + Pull Request
TD06 - Code Review
```

Checkpoint B is not performed yet. It closes Checkpoint Phase B after TD08.

The collaboration workflow is now established.

The next business requirement is:

```text
"All market-data sources must feed a common comparison model."
```

In TD07, the focus returns to Python and market data.

You will start preparing:

```text
instrument
+
benchmark
+
aligned observations
+
returns
+
base-100 comparison
```

The Git workflow introduced in TD05 and TD06 should now be reused for all new MarketPulse features.
