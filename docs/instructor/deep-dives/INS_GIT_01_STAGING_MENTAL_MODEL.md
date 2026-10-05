# INS-GIT-01 - Staging Mental Model

Status:

```text
INSTRUCTOR_READY
```

Primary teaching moment:

```text
TD03 - Git Local Workflow
```

## 1. Purpose

Give the instructor a compact mental model for explaining why:

```text
git add
```

does not mean:

```text
remember this file name for later
```

The useful model is:

```text
working tree
      |
      | git add
      v
staging area / index
      |
      | git commit
      v
commit
```

## 2. Student CORE boundary

Students need to be able to use and interpret:

```bash
git status
git diff
git add <file>
git diff --staged
git commit
```

They do not need to inspect the raw Git index file or manipulate internal index entries.

## 3. Instructor mental model

The index represents the snapshot that the next commit will record.

A file can therefore exist in three relevant states at once:

```text
HEAD version
staged version
working-tree version
```

This explains one of the most useful Git demonstrations:

```text
edit
-> stage
-> edit again
```

The second edit is not automatically staged.

## 4. Best teaching moment

Use this explanation when a student asks:

```text
Why does git diff show something after I already ran git add?
```

or:

```text
Why is git diff --staged different from git diff?
```

Keep the explanation to roughly 3 to 5 minutes unless the class explicitly asks for more depth.

## 5. Short explanation

A practical explanation is:

```text
git diff
=
working tree vs staging area

git diff --staged
=
staging area vs current commit
```

Therefore:

```text
git add
=
choose the content snapshot for the next commit
```

## 6. Worked example

Start from a clean repository.

Edit:

```text
src/main.py
```

Then:

```bash
git diff
git add src/main.py
git diff
git diff --staged
```

Now edit the same file again.

Run:

```bash
git status
git diff
git diff --staged
```

Expected mental model:

```text
first edit
=
staged

second edit
=
not staged
```

If the student commits now, the commit contains the staged snapshot, not automatically the latest working-tree content.

## 7. Common misconception

Misconception:

```text
git add
=
mark this file forever for the next commit
```

Correction:

```text
git add
=
stage the current content at that moment
```

Another misconception:

```text
git commit
=
commit everything I edited
```

Correction:

```text
git commit
=
record the staged snapshot
```

## 8. Stop point

Do not move into:

```text
raw index format
git update-index internals
manual cache entries
plumbing commands
```

during TD03 CORE.

The teaching objective is the snapshot model, not Git internals.

## 9. Source discipline

This note is derived from the historical Git-local material and the current MarketPulse TD03 workflow.

Canonical current student workflow:

```text
docs/labs/TD03_GIT_LOCAL_WORKFLOW.md
```

Historical depth source:

```text
docs/instructor/01_LEGACY_DEEP_DIVE_REFERENCE.md
```

## 10. Optional extension

For advanced students, ask:

```text
Can a single file contain both staged and unstaged changes?
```

Then demonstrate exactly that state.

Do not turn the extension into a checkpoint requirement.
