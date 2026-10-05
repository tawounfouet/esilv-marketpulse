# GitHub Team Workflow

## 1. Principle

MarketPulse uses:

```text
1 team
=
1 fork
```

not:

```text
1 student
=
1 fork
```

The repository is collective, but contributions must remain individually identifiable.

## 2. Repository model

```text
INSTRUCTOR REPOSITORY
tawounfouet/esilv-marketpulse
        |
        | fork
        v
TEAM REPOSITORY
esilv-marketpulse-gXX-tYY
        |
        +-- Student A
        +-- Student B
        +-- Student C
```

The instructor repository is the common reference.

Students do not develop directly in it.

## 3. Team repository name

Use:

```text
esilv-marketpulse-gXX-tYY
```

Example:

```text
esilv-marketpulse-g03-t02
```

Where:

```text
G03 = TD group
T02 = MarketPulse team
```

## 4. TEAM.md

Each team repository must contain:

```text
TEAM.md
```

Create it from:

```text
TEAM_TEMPLATE.md
```

The file identifies:

- TD group;
- MarketPulse team;
- student full names;
- GitHub usernames.

## 5. Individual Git identity

Every student works with their own GitHub account.

Run:

```bash
git config user.name
git config user.email
```

The objective is to keep commits attributable to the correct contributor.

## 6. Branch model

Use short descriptive branches:

```text
feature/display-benchmark
feature/yahoo-provider
feature/base-100-comparison
fix/invalid-ticker
docs/update-readme
```

Do not encode student initials in branch names.

## 7. Progressive workflow

The complete workflow is:

```text
Requirement
    |
    v
Feature branch
    |
    v
Implementation
    |
    v
Commit
    |
    v
Push
    |
    v
Pull Request
    |
    v
Review
    |
    v
Merge
```

Students are not expected to master all of these steps on the first day.

## 8. Progression by lab stage

### TD01-TD02

Focus:

```text
GitHub
Fork
TEAM.md
Codespaces
Linux
Python
```

### TD03-TD04

Add:

```text
Git local workflow
Commits
Branches
Merge
```

### TD04 -> TD05 Team Baseline Gate

TD03 and TD04 may leave different local `main` histories on different student environments.

Before TD05 collaborative work begins, the team establishes one shared baseline:

```text
local TD04 histories
        |
        v
preserve local archive branches
        |
        v
select one validated main
        |
        v
publish to origin/main
        |
        v
align every student to origin/main
        |
        v
start TD05 feature branches
```

Rules:

- capture Checkpoint A evidence before destructive alignment if needed;
- verify every working tree is clean;
- preserve previous local history with `archive/td04-local`;
- only the instructor or designated integrator publishes the baseline;
- verify `origin` points to the team repository;
- other students align only after the baseline is published;
- a controlled `git reset --hard origin/main` may be used only after the safety branch and clean-tree checks;
- a fresh Codespace or fresh clone is an acceptable alternative;
- do not teach merge or rebase of divergent student mains as part of this handoff.

The objective is operational consistency, not advanced Git-history manipulation.

### TD05-TD06

Add:

```text
Push
Pull Request
Review
Collaborative integration
```

### TD07-TD12

Use the same workflow for MarketPulse feature development.

## 9. main branch

Once branch-based development has been introduced:

```text
No direct feature development on main.
```

Once Pull Requests have been introduced:

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

## 10. Pull Requests

Each student should produce identifiable Pull Requests during the module.

A Pull Request should include:

- a clear title;
- a short description;
- the functionality implemented;
- useful validation information when relevant.

## 11. Reviews

Each student should also review work from another team member once code review is introduced.

A useful review may:

- identify a problem;
- ask for a correction;
- request clarification;
- verify expected behaviour;
- approve a correct change.

## 12. Individual contribution

The team repository does not remove individual accountability.

Each student should have identifiable:

```text
commits
+
branches
+
Pull Requests
+
reviews
+
functional contribution
+
checkpoint evidence
```

## 13. origin and upstream

Conceptually:

```text
origin
=
team repository

upstream
=
tawounfouet/esilv-marketpulse
```

The instructor may introduce these Git remote concepts later.

Advanced upstream synchronisation is not required during initial onboarding.

## 14. Security

Never commit:

- passwords;
- tokens;
- private SSH keys;
- Bloomberg credentials;
- cloud credentials;
- payment information.

## 15. Final principle

```text
Shared repository
+
individual Git trace
+
individual evidence
=
verifiable collaborative work
```
