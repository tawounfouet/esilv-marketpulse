# TD03 - Git Local Workflow

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"We need to keep a reliable history of changes."
```

## Context

In TD01, your team created a common working environment.

In TD02, you started modifying the Python code used by MarketPulse.

You now need to answer a new question:

> How can we know what changed, who changed it and when?

Git provides that history.

In this TD, the focus is local Git usage.

You will learn how to inspect modifications, prepare a commit and read repository history.

Remote collaboration, Pull Requests and code review come later.

## Learning objectives

At the end of TD03, you should be able to:

- explain the difference between a working directory and a commit;
- inspect repository state with `git status`;
- inspect code changes with `git diff`;
- stage selected changes with `git add`;
- create a commit with `git commit`;
- read history with `git log`;
- recognize a commit identifier;
- understand why commit messages matter;
- distinguish tracked, modified and staged files;
- explain why Git history is useful for MarketPulse.

## Expected result

At the end of the session, you should be able to demonstrate:

```text
working directory
      |
      v
git status
      |
      v
git diff
      |
      v
git add
      |
      v
staging area
      |
      v
git commit
      |
      v
local history
      |
      v
git log
```

Each student should create at least one identifiable local commit.

## Prerequisites

Before starting:

```text
[ ] TD01 completed
[ ] TD02 completed
[ ] team repository accessible
[ ] MarketPulse runs
[ ] Git is available
[ ] Git identity is correct
```

Verify:

```bash
git --version
git config user.name
git config user.email
```

If your Git identity is incorrect, ask the instructor before continuing.

## Important rule for TD03

Branches are introduced in TD04.

Pull Requests are introduced in TD05.

During TD03, the instructor may temporarily allow direct local commits on `main` only for learning purposes.

This is a temporary pedagogical exception.

Later in the module:

```text
feature work
    |
    v
branch
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
| 00-10 min | Git mental model |
| 10-25 min | Inspect repository state |
| 25-40 min | Create a small MarketPulse change |
| 40-55 min | Stage changes |
| 55-70 min | Commit changes |
| 70-82 min | Read and interpret history |
| 82-90 min | Readiness check |

# Part 1 - Understand the Git model

Git tracks versions of files.

A useful simplified model is:

```text
Working directory
       |
       | git add
       v
Staging area
       |
       | git commit
       v
Local repository history
```

## 1.1 Working directory

The working directory contains the files you are currently editing.

Examples:

```text
src/main.py
README.md
data/sample/prices.csv
```

If you modify a tracked file, Git can detect that the file changed.

## 1.2 Staging area

The staging area contains the changes selected for the next commit.

A file may be:

```text
modified
but not staged
```

or:

```text
modified
and staged
```

These are different states.

## 1.3 Commit

A commit records a selected version of the project.

A commit contains information such as:

- changed files;
- author;
- date;
- commit message;
- commit identifier.

A commit is not the same thing as saving a file in the editor.

# Part 2 - Inspect the repository

From the repository root, run:

```bash
pwd
git status
```

Read the output carefully.

Questions:

1. Which branch are you currently on?
2. Are there modified files?
3. Are there untracked files?
4. Are any changes already staged?

## 2.1 Short status

Try:

```bash
git status --short
```

Possible markers include:

```text
M
??
```

Discuss with your team what these markers mean.

## 2.2 Inspect recent history

Run:

```bash
git log --oneline
```

Each line represents one commit.

Example shape:

```text
abc1234 docs: add TD03 Git local workflow lab
def5678 docs: add TD02 Python CSV JSON lab
```

The short value at the beginning is part of the commit identifier.

# Part 3 - Create a small MarketPulse change

You need a real change to version.

Use a small modification that does not introduce a new business feature.

Choose one of the following tasks.

## Option A - Improve one output label

For example, in `src/main.py`, improve a label so the terminal output is clearer.

Do not calculate returns yet.

## Option B - Improve one explanatory comment

Add or improve one short comment in `src/main.py`.

The comment should explain why a piece of code exists.

Avoid comments that only repeat the code.

## Option C - Improve README wording

Improve one small part of the team README related to how MarketPulse is executed.

Do not rewrite the whole document.

## Individual contribution rule

Each student should be able to point to a change they personally understand.

A good TD03 change is:

```text
small
+
clear
+
easy to explain
```

Do not create a large feature just to have more Git activity.

# Part 4 - Inspect the modification

After editing a file, run:

```bash
git status
```

Then:

```bash
git diff
```

## Questions

1. Which file is modified?
2. Which lines were removed?
3. Which lines were added?
4. Does the diff match the change you intended?

The important habit is:

```text
edit
  |
  v
inspect
  |
  v
stage
  |
  v
commit
```

Do not commit blindly.

# Part 5 - Stage the change

Suppose you modified:

```text
src/main.py
```

Stage only that file:

```bash
git add src/main.py
```

Then run:

```bash
git status
```

Question:

> What changed in the status output after `git add`?

## 5.1 Inspect the staged diff

Run:

```bash
git diff --staged
```

This displays the changes that will be part of the next commit.

Compare:

```bash
git diff
```

with:

```bash
git diff --staged
```

Questions:

1. Which command shows unstaged changes?
2. Which command shows staged changes?
3. Why is this distinction useful?

# Part 6 - Commit the change

## 6.1 Write a meaningful message

A good commit message describes the change.

Examples:

```text
feat: improve MarketPulse market summary
docs: clarify starter execution instructions
refactor: simplify market summary display
```

Avoid:

```text
update
changes
work
test
final
final2
```

## 6.2 Create the commit

Example:

```bash
git commit -m "docs: clarify MarketPulse execution"
```

Use a message that matches your actual change.

## 6.3 Verify repository state

Run:

```bash
git status
```

If every intended change was committed, Git may report a clean working tree.

Question:

> What does a clean working tree mean?

# Part 7 - Read repository history

Run:

```bash
git log --oneline
```

Your new commit should appear near the top.

Identify:

```text
commit identifier
commit message
```

## 7.1 Detailed commit information

Run:

```bash
git log -1
```

Identify:

- commit identifier;
- author;
- date;
- message.

## 7.2 Inspect one commit

Copy the short identifier from your latest commit.

Then run:

```bash
git show <commit-id>
```

Example:

```bash
git show abc1234
```

Do not copy the example identifier literally.

Use one from your repository.

Question:

> How is `git show` different from `git log --oneline`?

# Part 8 - Understand tracked and untracked files

Create a temporary text file:

```bash
touch td03_notes.txt
```

Run:

```bash
git status
```

The file should appear as untracked.

Question:

> Why can Git see the file even though it has never been committed?

Now remove the temporary file:

```bash
rm td03_notes.txt
```

Run:

```bash
git status
```

The temporary file should disappear from the status output.

Do not commit this file.

# Part 9 - Practice with two modifications

Modify two files with very small harmless changes.

For example:

```text
README.md
src/main.py
```

Run:

```bash
git status
git diff
```

Stage only one file:

```bash
git add README.md
```

Then inspect:

```bash
git status
git diff
git diff --staged
```

Question:

> Can one file be staged while another modified file remains unstaged?

Yes.

This is one of the reasons the staging area exists.

## Clean up the exercise

Decide which change you want to keep.

If both changes are meaningful, you may create separate commits.

If one change was only experimental, ask the instructor how to discard it safely.

Do not use destructive Git commands you do not understand.

# Part 10 - Commit quality

A useful commit should be:

```text
small
coherent
understandable
explainable
```

A commit should not mix unrelated work such as:

```text
Python refactor
+
large documentation rewrite
+
random data changes
+
temporary debug code
```

when these changes could have been separated.

## Example

Better:

```text
feat: display first and last market observations
docs: clarify MarketPulse execution
```

Less useful:

```text
update everything
```

# Part 11 - Individual traceability

MarketPulse is a team project.

Git history helps preserve individual contribution.

Each student should eventually be able to answer:

```text
Which commits are mine?
What did I change?
Why did I change it?
Can I explain the diff?
Can I reproduce the change?
```

Being listed in `TEAM.md` is not evidence of technical contribution.

# Part 12 - Local vs remote Git

TD03 focuses on local Git.

For now:

```text
Working directory
      |
      v
Staging area
      |
      v
Local commits
```

Later:

```text
Local commits
      |
      v
push
      |
      v
GitHub
      |
      v
Pull Request
```

Do not worry if `git push` is not yet part of today's required workflow.

Push and Pull Requests are introduced later.

# Part 13 - Checkpoint A connection

Checkpoint A is performed after TD04.

One of the required screenshots is:

```text
02_git_status_log.png
```

It must later show evidence including:

```bash
git status
git log --oneline
```

Do not submit the checkpoint yet.

Today, make sure you understand what those commands show.

# Part 14 - Mini exercises

## Exercise 1 - Identify the latest commit

Run:

```bash
git log --oneline -5
```

Write down:

```text
latest commit id
latest commit message
```

## Exercise 2 - Inspect one file history

Try:

```bash
git log --oneline -- src/main.py
```

Question:

> What does this command filter?

## Exercise 3 - Inspect one commit

Use:

```bash
git show <commit-id>
```

Explain the change to another team member.

## Exercise 4 - Compare working state with history

Make one small temporary edit but do not stage it.

Then run:

```bash
git status
git diff
git log --oneline -3
```

Explain why the temporary modification appears in `git diff` but not in the commit history.

Undo the temporary edit using your editor.

# Part 15 - If you finish early

## Challenge 1 - Graph view

Try:

```bash
git log --oneline --graph --decorate
```

You may not see branches yet.

That becomes more interesting in TD04.

## Challenge 2 - File statistics

Try:

```bash
git show --stat
```

Question:

> What does the statistics view summarize?

## Challenge 3 - Author filtering

Try:

```bash
git log --author="<your name>" --oneline
```

Use the author name configured in your Git environment.

Question:

> How can this help demonstrate individual contribution?

## Challenge 4 - Inspect tracked files

Try:

```bash
git ls-files
```

Question:

> Which project files are already tracked by Git?

# Part 16 - Troubleshooting

## Nothing to commit

If Git reports:

```text
nothing to commit
```

check:

```bash
git status
git diff
```

You may not have modified a tracked file.

## Commit identity error

If Git asks you to configure your identity, stop and verify:

```bash
git config user.name
git config user.email
```

Ask the instructor if you are unsure which values should be used.

## Wrong file staged

Do not use random destructive commands.

Ask the instructor how to unstage the file while preserving your work.

The objective is to understand the staging area, not to memorize recovery commands without context.

## Unexpected large diff

Run:

```bash
git status
git diff
```

Check that you did not accidentally reformat or replace a large file.

## MarketPulse no longer runs

Before committing a Python change, run:

```bash
python src/main.py
```

A commit should preferably preserve a working project state.

# Part 17 - Readiness check

Before finishing TD03, each student should be able to explain:

```text
[ ] working directory
[ ] staging area
[ ] commit
[ ] commit identifier
[ ] git status
[ ] git diff
[ ] git diff --staged
[ ] git add
[ ] git commit
[ ] git log
[ ] git show
```

Each student should also confirm:

```text
[ ] my Git identity is correct
[ ] I created at least one understandable commit
[ ] I can find my commit in git log
[ ] I can explain the diff in my commit
[ ] MarketPulse still runs
```

# Part 18 - What comes next?

In TD04, the business requirement changes:

```text
"Features should no longer be developed directly on main."
```

You will introduce:

```text
branches
+
feature isolation
+
merge
+
simple conflict resolution
```

The Git history you created today becomes the foundation for that workflow.
