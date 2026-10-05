# INS-GIT-04 - Merge vs Rebase

Status:

```text
INSTRUCTOR_READY
```

Primary teaching moments:

```text
TD04
TD05
TD06
```

## 1. Purpose

Equip the instructor to answer rebase questions while keeping the MarketPulse collaboration workflow merge-oriented.

## 2. Student CORE boundary

MarketPulse CORE uses:

```text
feature branch
+
Pull Request
+
review
+
merge
```

Interactive rebase is not mandatory.

Students do not need force-push workflows to complete the guided path.

## 3. Instructor mental model

Merge:

```text
combine histories
without replaying existing commits
```

Rebase:

```text
replay commits onto another base
creating new commit identities
```

Simple model:

```text
before

A---B---C main
     \
      D---E feature

merge

A---B---C------M
     \        /
      D---E---

rebase conceptually

A---B---C---D'---E'
```

## 4. Best teaching moment

Use when an advanced student asks:

```text
Why not rebase instead of merge?
Why is my history different after rebase?
Why can force-push be dangerous?
```

## 5. Short explanation

A useful teaching rule:

```text
merge
=
combine existing histories

rebase
=
rewrite the base of local commits
```

Rebase can make a linear history easier to read, but history rewriting matters when commits are already shared.

## 6. Worked example

Do not modify the shared team repository for the demonstration.

Use a disposable repository or a drawing.

Show:

```bash
git log --oneline --graph --decorate --all
```

before and after a simple merge.

Then explain that a rebase would create new commit IDs for replayed commits.

The objective is conceptual contrast, not workflow migration.

## 7. Common misconception

Misconception:

```text
rebase is a cleaner merge
```

Correction:

```text
rebase changes commit ancestry and identities
```

Misconception:

```text
merge commits are always bad
```

Correction:

```text
history strategy is a team convention, not a universal moral rule
```

## 8. Stop point

Do not introduce mandatory:

```text
interactive rebase
force push
squash chains
shared-history rewriting
```

into TD04-TD06.

Those belong to optional advanced Git work.

## 9. Source discipline

Historical material discussed merge, rebase, interactive rebase and Gitflow.

Current MarketPulse contract deliberately narrows the student path.

Current sources:

```text
docs/03_GITHUB_TEAM_WORKFLOW.md
docs/labs/TD04_BRANCHES_AND_MERGE.md
docs/labs/TD05_FORK_AND_PULL_REQUEST.md
docs/labs/TD06_CODE_REVIEW.md
```

## 10. Optional extension

After the CORE is complete, point interested students to:

```text
ADV-GIT-03 - Interactive rebase
```

which remains optional and is not part of R7.4 P1 closure.
