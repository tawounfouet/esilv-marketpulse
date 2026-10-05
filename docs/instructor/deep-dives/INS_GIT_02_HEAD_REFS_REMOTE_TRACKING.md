# INS-GIT-02 - HEAD, Refs and Remote-Tracking Refs

Status:

```text
INSTRUCTOR_READY
```

Primary teaching moments:

```text
TD03
TD04
TD05
```

## 1. Purpose

Give the instructor a precise but lightweight model for explaining:

```text
HEAD
main
origin/main
origin
```

without turning the course into a Git-internals module.

## 2. Student CORE boundary

Students need to distinguish:

```text
current local branch
remote repository
remote-tracking reference
```

They do not need to manipulate refs directly.

## 3. Instructor mental model

Use this model:

```text
HEAD
 |
 v
main
 |
 v
commit A
```

Conceptually:

```text
HEAD
=
where the current checkout is anchored

main
=
a local branch reference

origin
=
a configured remote

origin/main
=
the local repository's last fetched knowledge of remote main
```

Important:

```text
origin/main
!=
a live network connection
```

It is a local remote-tracking reference updated by network operations such as fetch.

## 4. Best teaching moment

TD03:

```text
What does HEAD mean in git log?
```

TD04:

```text
Why does switching branch move what I see?
```

TD05:

```text
Why can main and origin/main differ?
```

## 5. Short explanation

A useful three-line explanation:

```text
main
=
my local branch

origin/main
=
my local record of remote main

git fetch
=
refresh that record without merging it into main
```

## 6. Worked example

Run:

```bash
git branch
git log --oneline --decorate -5
git remote -v
git fetch origin
git log --oneline --decorate --all -8
```

Ask students to identify:

```text
HEAD
main
origin/main
feature branch
```

If local `main` is behind:

```text
main
      |
      v
commit A

origin/main
      |
      v
commit B
```

the local branch does not move merely because `origin/main` moved after fetch.

## 7. Common misconception

Misconception:

```text
origin/main
=
the branch currently running on GitHub
```

Correction:

```text
origin/main
=
a local tracking reference representing the last fetched state
```

Misconception:

```text
HEAD
=
the latest commit in the repository
```

Correction:

```text
HEAD
=
the current checkout context
```

## 8. Stop point

Do not teach direct editing of:

```text
.git/HEAD
.git/refs/
packed-refs
```

during the common TD sequence.

Detached HEAD may be explained only if a real student situation requires it.

## 9. Source discipline

Current workflow sources:

```text
docs/labs/TD03_GIT_LOCAL_WORKFLOW.md
docs/labs/TD04_BRANCHES_AND_MERGE.md
docs/labs/TD05_FORK_AND_PULL_REQUEST.md
docs/03_GITHUB_TEAM_WORKFLOW.md
```

Historical conceptual source:

```text
docs/instructor/01_LEGACY_DEEP_DIVE_REFERENCE.md
```

## 10. Optional extension

Compare:

```bash
git fetch
git pull --ff-only
```

Ask:

```text
Which command only updates remote knowledge?
Which command also integrates into the local branch?
```

Keep rebase out of this extension unless INS-GIT-04 is intentionally used.
