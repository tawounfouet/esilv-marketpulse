# INS-GIT-03 - Git Object Model

Status:

```text
INSTRUCTOR_READY
```

Primary teaching moment:

```text
TD03
```

## 1. Purpose

Provide enough internal Git understanding for the instructor to explain what a commit represents without asking students to manipulate Git objects manually.

## 2. Student CORE boundary

Students need:

```text
commit identifiers
history
diffs
branches
```

They do not need:

```text
manual object creation
zlib manipulation
direct writes to .git/objects
```

## 3. Instructor mental model

The useful conceptual chain is:

```text
file content
    |
    v
blob

directory snapshot
    |
    v
tree

tree + parent + metadata + message
    |
    v
commit
```

A branch then points to a commit.

This helps explain why Git is fundamentally snapshot-oriented.

## 4. Best teaching moment

Use when students ask:

```text
What is a commit really?
Why does a commit have a hash?
Why are branches lightweight?
```

This is usually most useful after students have already created at least one real commit.

## 5. Short explanation

A concise explanation:

```text
Git stores content as objects.

A commit identifies a project snapshot through a tree,
records parent history and metadata,
and receives an object identifier.

A branch is mainly a movable name pointing to a commit.
```

## 6. Worked example

Use only porcelain inspection:

```bash
git log --oneline --decorate -3
git show --stat HEAD
git show HEAD
```

Optional instructor-only observation:

```bash
git cat-file -t HEAD
git cat-file -p HEAD
```

Explain:

```text
commit
-> tree
-> parent
-> author/committer
-> message
```

Do not require students to memorize the raw format.

## 7. Common misconception

Misconception:

```text
A Git commit is just a patch file.
```

Correction:

```text
The history can be viewed as changes,
but Git's internal model records snapshot relationships.
```

Misconception:

```text
A branch contains a second copy of all files.
```

Correction:

```text
A branch is a reference to a commit history.
```

## 8. Stop point

Do not reproduce historical exercises involving:

```text
git hash-object as a mandatory task
manual zlib compression
manual .git/objects injection
```

These are explicitly outside the frozen CORE.

## 9. Source discipline

Historical source family:

```text
CM2 Git local
TD2 Git local
```

Current classification:

```text
docs/legacy/05_LEGACY_FINAL_MIGRATION_REGISTRY.md
```

The deeper object model is instructor knowledge, not a new checkpoint requirement.

## 10. Optional extension

For a strong group, show:

```bash
git cat-file -t <sha>
git cat-file -p <sha>
```

and ask students to infer relationships.

Stop before manual object construction.
