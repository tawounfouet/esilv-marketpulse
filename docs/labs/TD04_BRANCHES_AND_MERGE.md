# TD04 - Branches + Merge

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"Features should no longer be developed directly on main."
```

## Context

In TD03, you learned how Git records changes through local commits.

You can now answer:

```text
What changed?
Who changed it?
When was it committed?
```

A new problem now appears.

If every feature is developed directly on `main`, unfinished work can affect the stable version of MarketPulse.

Git branches provide a way to isolate work before integration.

In TD04, you will learn to:

```text
main
  |
  +-- feature branch
          |
          v
       commits
          |
          v
        merge
          |
          v
         main
```

Pull Requests are not introduced yet.

They arrive in TD05.

## Learning objectives

At the end of TD04, you should be able to:

- explain why branches are useful;
- identify the current branch;
- create a feature branch;
- switch between branches;
- make commits on a feature branch;
- compare branch history;
- merge a completed branch into `main`;
- recognize a merge conflict;
- resolve a simple text conflict;
- inspect the resulting history;
- explain why direct feature development on `main` should stop after this TD.

## Expected result

Each student should be able to demonstrate:

```text
main
  |
  +-- feature/<description>
          |
          +-- commit
          |
          v
        merge
          |
          v
         main
```

By the end of TD04:

```text
[ ] one feature branch created
[ ] at least one commit created on the branch
[ ] branch merged into local main
[ ] Git graph inspected
[ ] simple conflict demonstrated or understood
[ ] MarketPulse still runs
[ ] Checkpoint A evidence prepared
```

## Prerequisites

Before starting:

```text
[ ] TD01 completed
[ ] TD02 completed
[ ] TD03 completed
[ ] git status understood
[ ] git diff understood
[ ] git add understood
[ ] git commit understood
[ ] git log understood
[ ] MarketPulse runs
```

Verify:

```bash
git status
git log --oneline -5
python src/main.py
```

Start from a clean working tree.

If your working tree contains unfinished changes, resolve them with the instructor before continuing.

## Important rule from TD04 onward

After branch-based development has been introduced:

```text
No direct feature development on main.
```

The normal local workflow becomes:

```text
main
  |
  v
create feature branch
  |
  v
implement
  |
  v
commit
  |
  v
merge
```

In TD05, this will evolve into:

```text
feature branch
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

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | Branch mental model |
| 10-25 min | Create and inspect a feature branch |
| 25-45 min | Implement a small MarketPulse change |
| 45-60 min | Commit and compare branches |
| 60-72 min | Merge into main |
| 72-82 min | Simple conflict exercise |
| 82-90 min | Checkpoint A preparation |

# Part 1 - Understand branches

A branch is a movable reference to a line of commits.

For this TD, use the following simplified mental model:

```text
main
  |
  o---o---o
          |
          +-- feature/display-dates
                    |
                    o
```

The feature branch lets you work without immediately changing `main`.

## 1.1 Inspect your current branch

Run:

```bash
git branch
```

The current branch is marked with:

```text
*
```

You may also run:

```bash
git status
```

Question:

> Which branch are you currently on?

## 1.2 Inspect branch names

Run:

```bash
git branch --list
```

At this stage, you may only see:

```text
main
```

# Part 2 - Create a feature branch

## 2.1 Choose a small feature

For TD04, use a small MarketPulse improvement.

Recommended task:

```text
Display the first and last observation dates
for both instrument and benchmark.
```

This builds directly on TD02.

The output may evolve toward:

```text
Instrument
AAPL - Apple Inc.
Observations : 21
First date   : 2026-09-01
Last date    : 2026-09-30
First close  : 250.00 USD
Last close   : 266.20 USD
```

Do not calculate returns yet.

## 2.2 Create the branch

Use a descriptive branch name:

```bash
git switch -c feature/display-observation-dates
```

If your Git version does not support `git switch`, the instructor may show the equivalent `git checkout` command.

Verify:

```bash
git branch
```

Expected shape:

```text
* feature/display-observation-dates
  main
```

Question:

> Why is `feature/display-observation-dates` better than a branch called `test` or `student1`?

# Part 3 - Implement the feature

Open:

```text
src/main.py
```

Create or reuse simple functions such as:

```python
def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]
```

Integrate the information into your market summary.

Run:

```bash
python src/main.py
```

Verify that both instrument and benchmark display dates.

## 3.1 Inspect the change before staging

Run:

```bash
git status
git diff
```

Explain the diff to another team member.

## 3.2 Stage the intended file

Example:

```bash
git add src/main.py
```

Inspect:

```bash
git diff --staged
```

# Part 4 - Commit on the feature branch

Create a meaningful commit.

Example:

```bash
git commit -m "feat: display first and last observation dates"
```

Verify:

```bash
git status
git log --oneline -5
```

Question:

> Is the commit now part of `main`?

Not yet.

It currently belongs to the feature branch history.

# Part 5 - Compare branches

## 5.1 Inspect the graph

Run:

```bash
git log --oneline --graph --decorate --all
```

You should be able to identify:

```text
main
feature/display-observation-dates
```

## 5.2 Switch back to main

Run:

```bash
git switch main
```

Then:

```bash
git branch
git log --oneline -5
```

Question:

> Is the feature commit visible as the current commit of main?

## 5.3 Compare the branches

Try:

```bash
git diff main..feature/display-observation-dates
```

Question:

> What difference does Git show between the two branches?

# Part 6 - Merge the feature

Make sure you are on `main`:

```bash
git branch
```

Then merge:

```bash
git merge feature/display-observation-dates
```

Run:

```bash
git log --oneline --graph --decorate --all
```

Then verify MarketPulse:

```bash
python src/main.py
```

## Questions

1. Is the feature now available on `main`?
2. Is the feature commit still visible in history?
3. Did Git create a separate merge commit or perform a fast-forward?
4. What does your Git graph show?

## Important

A fast-forward merge is valid.

Do not force a merge commit only to make the graph look more complex.

The objective is to understand integration, not to manufacture history.

# Part 7 - Branch lifecycle

After successful integration, the local feature branch is no longer needed.

List branches:

```bash
git branch
```

If the instructor asks you to clean the merged branch, use:

```bash
git branch -d feature/display-observation-dates
```

The `-d` option refuses to delete some unmerged branches.

Do not use force deletion unless you understand why it is necessary.

# Part 8 - Understand merge conflicts

A conflict occurs when Git cannot automatically decide how to combine competing changes.

Conceptually:

```text
main changes one line
          +
feature changes the same line
          |
          v
Git cannot choose automatically
          |
          v
merge conflict
```

Conflicts are not errors in Git.

They are situations that require a human decision.

# Part 9 - Simple conflict exercise

This exercise should use a harmless text file so that the MarketPulse code remains safe.

## 9.1 Create a practice file on main

Make sure you are on `main`:

```bash
git switch main
```

Create:

```bash
printf "MarketPulse mode: standard\n" > conflict_demo.txt
git add conflict_demo.txt
git commit -m "chore: add conflict demonstration file"
```

## 9.2 Create a conflict branch

Create:

```bash
git switch -c practice/conflict-demo
```

Change the file:

```bash
printf "MarketPulse mode: feature\n" > conflict_demo.txt
git add conflict_demo.txt
git commit -m "chore: change conflict demo on feature branch"
```

## 9.3 Change the same line on main

Switch back:

```bash
git switch main
```

Change the same line:

```bash
printf "MarketPulse mode: main\n" > conflict_demo.txt
git add conflict_demo.txt
git commit -m "chore: change conflict demo on main"
```

This direct change on `main` exists only to create a controlled conflict exercise.

It is not the normal feature-development workflow.

## 9.4 Attempt the merge

Run:

```bash
git merge practice/conflict-demo
```

Git should report a conflict.

Inspect:

```bash
git status
cat conflict_demo.txt
```

You may see markers similar to:

```text
<<<<<<< HEAD
MarketPulse mode: main
=======
MarketPulse mode: feature
>>>>>>> practice/conflict-demo
```

## 9.5 Resolve the conflict

Choose a final value that your team understands.

For example:

```text
MarketPulse mode: resolved
```

Edit the file so that no conflict markers remain.

Then:

```bash
git add conflict_demo.txt
git status
git commit
```

Use the merge message proposed by Git or a clear equivalent.

Inspect:

```bash
git log --oneline --graph --decorate --all
```

## 9.6 Clean up the demonstration file

The file exists only for the exercise.

After the instructor confirms the conflict exercise, remove it through a normal tracked change:

```bash
rm conflict_demo.txt
git add conflict_demo.txt
git commit -m "chore: remove conflict demonstration file"
```

The exercise remains visible in Git history even though the temporary file is removed.

# Part 10 - What a conflict teaches

You should now understand:

```text
Git detects competing changes
          |
          v
Git stops the merge
          |
          v
human reads the conflict
          |
          v
human chooses final content
          |
          v
git add
          |
          v
commit merge resolution
```

Never resolve a conflict by deleting markers randomly without understanding which content should remain.

# Part 11 - Branch naming convention

Use:

```text
feature/<short-description>
fix/<short-description>
docs/<short-description>
```

Examples:

```text
feature/display-observation-dates
feature/yahoo-provider
fix/invalid-ticker
docs/update-readme
```

Avoid:

```text
test
student1
thomas
mybranch
final
final2
```

A branch describes the work, not the person.

# Part 12 - Git commands recap

By the end of TD04, you should understand:

```bash
git branch
git branch --list
git switch -c <branch>
git switch <branch>
git status
git diff
git add
git commit
git log --oneline
git log --oneline --graph --decorate --all
git diff main..<branch>
git merge <branch>
git branch -d <branch>
```

# Part 13 - Checkpoint A

Checkpoint A is performed after TD04.

It validates the foundations from TD01 to TD04.

## 13.1 Required evidence directory

Each student uses:

```text
evidence/checkpoint-a/<github-username>/
```

Example:

```text
evidence/checkpoint-a/alice-martin/
```

## 13.2 Required files

Exactly these files are required:

```text
README.md
01_terminal_python.png
02_git_status_log.png
03_branch_merge.png
```

Do not rename the screenshots.

## 13.3 01_terminal_python.png

The screenshot should show evidence such as:

```bash
pwd
ls
python src/main.py
```

The image must make it clear that MarketPulse runs from the project environment.

## 13.4 02_git_status_log.png

The screenshot should show:

```bash
git status
git log --oneline
```

The objective is to demonstrate repository state and visible history.

## 13.5 03_branch_merge.png

The screenshot should show branch and merge evidence.

Recommended commands:

```bash
git branch
git log --oneline --graph --decorate --all
```

The graph should make your branch work understandable.

## 13.6 Individual README

Create:

```text
evidence/checkpoint-a/<github-username>/README.md
```

Suggested content:

```markdown
# Checkpoint A

## Student

- Name: Alice Martin
- GitHub: @alice-martin

## Contribution

- Feature branch: feature/display-observation-dates
- Main commit(s):
  - <commit-id>

## Work completed

Briefly explain the change you implemented.

## Main difficulty

Briefly explain one difficulty or concept that required attention.

## Evidence

- 01_terminal_python.png
- 02_git_status_log.png
- 03_branch_merge.png
```

The filenames must exactly match the files stored in the directory.

# Part 14 - Checkpoint A live micro-validation

Screenshots do not replace understanding.

The instructor may ask you to perform a small live task such as:

```text
create a branch
make a small modification
show git diff
stage the change
commit it
show the Git graph
run MarketPulse
```

You should be able to explain what each command changes in the Git state.

# Part 15 - Checkpoint A readiness

Before submitting Checkpoint A, each student should be able to confirm:

```text
[ ] I can navigate the repository from Linux
[ ] I can run MarketPulse
[ ] I understand CSV and JSON input files
[ ] I can explain lists and dictionaries used by MarketPulse
[ ] I can use git status
[ ] I can use git diff
[ ] I can use git add
[ ] I can create a commit
[ ] I can read git log
[ ] I can create a branch
[ ] I can switch branches
[ ] I can merge a branch
[ ] I understand a simple merge conflict
[ ] I can explain my own contribution
```

The team should confirm:

```text
[ ] MarketPulse still runs
[ ] no required evidence filename was changed
[ ] no secrets appear in screenshots
```

# Part 16 - Security before screenshots

Before committing evidence, inspect every screenshot.

Never expose:

- passwords;
- API keys;
- GitHub tokens;
- private SSH keys;
- Bloomberg credentials;
- cloud credentials;
- payment information.

If a terminal displays sensitive information, do not include it in the screenshot.

# Part 17 - If you finish early

## Challenge 1 - Compare two branches

Create a harmless practice branch and use:

```bash
git diff main..<branch>
```

Explain what changes exist only on the branch.

## Challenge 2 - Inspect graph decorations

Run:

```bash
git log --oneline --graph --decorate --all
```

Identify:

- current branch;
- main;
- recent commits.

## Challenge 3 - File history

Run:

```bash
git log --oneline -- src/main.py
```

Then inspect one commit:

```bash
git show <commit-id> -- src/main.py
```

## Challenge 4 - Explain fast-forward

Using your own Git graph, explain in your own words what happened when your feature branch was merged.

You do not need to memorize a formal definition.

# Part 18 - Troubleshooting

## Cannot switch branches

Run:

```bash
git status
```

Uncommitted changes may prevent a safe switch.

Do not discard work blindly.

Ask the instructor if you are unsure.

## Merge says already up to date

Inspect:

```bash
git log --oneline --graph --decorate --all
```

You may already have merged the branch or created no additional commit on it.

## Merge conflict appears unexpectedly

Run:

```bash
git status
```

Identify conflicted files.

Do not continue editing unrelated files.

Resolve one conflict carefully before proceeding.

## Conflict markers remain

Search:

```bash
grep -R "<<<<<<<" .
```

Also check for:

```text
=======
>>>>>>>
```

Do not commit unresolved conflict markers.

## MarketPulse fails after merge

Run:

```bash
python src/main.py
git status
git diff
```

Inspect the merged code before creating more changes.

# Part 19 - What comes next?

The first pedagogical wave is now complete:

```text
TD01 - Bootstrap + Linux
TD02 - Python + CSV / JSON
TD03 - Git Local Workflow
TD04 - Branches + Merge
        |
        v
Checkpoint A
```

In TD05, the workflow becomes collaborative at GitHub level.

The next business requirement is:

```text
"Several developers now contribute to the same MarketPulse repository."
```

You will introduce:

```text
feature branch
+
push
+
Pull Request
```

From that point, a completed feature should no longer be integrated simply by working directly on `main`.
