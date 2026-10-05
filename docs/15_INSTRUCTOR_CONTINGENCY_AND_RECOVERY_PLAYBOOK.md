# MarketPulse Instructor Contingency and Recovery Playbook

## 1. Purpose

This document is the operational recovery reference for the MarketPulse 18-hour teaching path.

Use it when a student or team cannot follow the normal TD sequence because of an environment, platform, provider, Git-state or evidence problem.

The objective is:

```text
preserve learning continuity
+
preserve real student work
+
preserve evidence integrity
+
avoid invented success
```

This playbook does not replace the normal lab instructions.

It defines what to do when the normal path is temporarily unavailable.

## 2. Recovery principles

Apply these rules in every incident:

```text
1. classify the failure before changing the architecture
2. preserve local work before destructive Git operations
3. keep provider-specific failures outside analytics.py
4. use only authorized provider fallbacks
5. distinguish teaching continuity from evidence completion
6. never manufacture screenshots, provider output or review activity
7. return to the canonical workflow when the blocker disappears
```

Recovery is not about making every green check appear immediately.

It is about keeping the student progressing on the learning objective without corrupting the project contract.

## 3. Incident classes

Use one of these classes:

```text
LOCAL_ENVIRONMENT
PLATFORM_EXTERNAL
PROVIDER_EXTERNAL
GIT_STATE
EVIDENCE_STATE
```

Examples:

```text
LOCAL_ENVIRONMENT
broken Codespace
Python unavailable
student workstation issue

PLATFORM_EXTERNAL
GitHub unavailable
collaborator access delay
package index unavailable

PROVIDER_EXTERNAL
Yahoo unavailable
Bloomberg LIVE unavailable
provider returns no data

GIT_STATE
late synchronization
divergent local main
merge conflict
dirty working tree

EVIDENCE_STATE
missing screenshot
wrong filename
external proof unavailable
screenshot exposes a secret
```

## 4. Recovery outcomes

### CONTINUE_LOCAL

The student can continue useful work without the unavailable remote service.

Typical case:

```text
GitHub unavailable
but local Git works
```

### PAIR_TEMPORARILY

The student's environment is unusable but another team environment is healthy.

The blocked student participates actively while their environment is repaired.

Pairing is temporary and does not replace individual Git or checkpoint evidence.

### APPROVED_SAMPLE

Bloomberg LIVE is unavailable or unsuitable.

Use only the instructor-approved Bloomberg fallback assets.

### PENDING_EXTERNAL

A required proof cannot currently be completed because an external dependency is unavailable.

This applies to the evidence item, not to unrelated student work.

### ARCHIVE_AND_ALIGN

A student has valid local history but must rejoin a newer shared baseline.

Preserve the old local history before controlled alignment.

### RESOLVE_AND_VALIDATE

A merge conflict requires human interpretation before the workflow can continue.

## 5. Scenario 1 - student environment failure

### Symptoms

```text
Codespace does not start
Python command unavailable
terminal unusable
local dependency state corrupted
student laptop problem
```

### Response

First determine whether the problem is specific to the student's environment.

Do not turn the entire lab into workstation debugging.

If another team environment works, use:

```text
PAIR_TEMPORARILY
```

The student should still:

```text
read the code
explain commands
predict output
participate in debugging
make decisions
```

When their environment is restored, recover individual traceability through their own branch, commits and checkpoint evidence.

A fresh Codespace or fresh clone is preferable to spending the entire session repairing an unknown local state.

### Do not

```text
share GitHub credentials
copy another student's personal evidence
attribute another student's commit to the blocked student
```

This is consistent with the temporary-pairing rule already defined in `docs/01_STUDENT_ONBOARDING.md`.

## 6. Scenario 2 - GitHub unavailable or delayed

### Symptoms

```text
GitHub page unavailable
push cannot reach GitHub
Pull Request UI unavailable
collaborator invitation delayed
```

### Recovery mode

```text
CONTINUE_LOCAL
```

If local Git works, continue:

```bash
git status
git diff
git add <intended-files>
git commit -m "<meaningful message>"
git log --oneline
```

Once branches have been introduced, feature work remains on a feature branch.

When GitHub returns:

```bash
git push -u origin <feature-branch>
```

Then create the real Pull Request and complete review normally.

### R6.8 dry-run proof

The dry run created a local feature commit before any remote existed.

A remote was attached later and the feature branch was pushed.

Validated invariant:

```text
local feature HEAD
=
remote feature HEAD after recovery
```

No local commit rewrite was required.

### Evidence rule

PR or review evidence remains:

```text
PENDING_EXTERNAL
```

until the real GitHub action exists.

A local commit screenshot is not a Pull Request screenshot.

## 7. Scenario 3 - Yahoo provider failure

### Symptoms

```text
yfinance cannot be installed
AAPL history empty
^GSPC history empty
network unavailable
Yahoo temporarily fails
```

### Recovery sequence

```text
1. verify network access
2. verify symbol spelling
3. compare provider code with the instructor reference
4. retry once after correcting local mistakes
5. continue analytics validation with local CSV data
6. mark Yahoo evidence PENDING_EXTERNAL if the external service remains unavailable
```

Critical boundary:

```text
Yahoo outage
!=
analytics defect
```

Do not rewrite:

```text
align_series()
calculate_period_return()
calculate_base_100()
calculate_relative_performance()
```

because Yahoo is unavailable.

### Evidence rule

`03_yahoo_market_data.png` requires a real successful Yahoo retrieval.

Do not use:

```text
CSV output
controlled provider-double output
old unrelated Yahoo output
fabricated prices
```

as Yahoo remote evidence.

### R6 proof

R6.5 validated:

```text
empty provider response
-> explicit ValueError

local CSV
-> analytics remain executable
```

The validation runner also confirms that `yfinance` is currently unavailable in its environment, so this external dependency boundary is real rather than assumed.

## 8. Scenario 4 - Bloomberg LIVE unavailable

### Recovery mode

With instructor approval, switch to:

```text
APPROVED_SAMPLE
```

Use only:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
docs/11_BLOOMBERG_PROVIDER_SCAFFOLD.md
data/sample/bloomberg_reference_sample.json
data/sample/bloomberg_reference_expected.json
```

The application and evidence must make the mode visible as:

```text
Bloomberg stage - APPROVED_SAMPLE
```

Never relabel fallback output as:

```text
Bloomberg - LIVE
```

### R6.6 dry-run proof

The full fallback path was executed:

```text
21 AAPL observations
+
21 SP500 observations
-> 42 / 42 exact normalized-row match
-> same analytics.py
-> build_market_snapshot(...)
-> terminal and dashboard presentation contract
```

The fallback preserves the one-month CORE learning path without claiming LIVE connectivity.

## 9. Scenario 5 - Dash dependency or startup issue

### Symptoms

```text
ModuleNotFoundError: dash
plotly unavailable
package index unavailable
dashboard cannot start
```

First inspect:

```bash
python -m pip show dash
python -m pip show plotly
```

Then verify:

```text
requirements.txt
src/dashboard.py
src/main.py
```

If the package index is unavailable, do not move presentation logic into `main.py` and do not duplicate analytics inside `dashboard.py`.

Continue validating the upstream contract with:

```bash
python src/main.py
```

and inspect `build_market_snapshot(...)`.

When package installation is available again:

```bash
python -m pip install -r requirements.txt
python src/dashboard.py
```

### Evidence rule

A dashboard screenshot requires a real working dashboard.

If Dash cannot be installed because of an external package-index problem:

```text
02_dash_dashboard.png
=
PENDING_EXTERNAL
```

until the real dashboard runs.

### R6.8 environment evidence

The validation runner reports:

```text
dash = unavailable
yfinance = unavailable
plotly = available
```

R6.6 validated the presentation boundary with real Plotly and a controlled Dash dependency double, but that run was not classified as real Dash evidence.

## 10. Scenario 6 - late student synchronization

### Symptoms

```text
student missed the team baseline update
student local main diverged
origin/main advanced while student was away
```

### Recovery mode

```text
ARCHIVE_AND_ALIGN
```

Use this only when the working tree is clean and the authoritative team baseline is known.

Preserve the current history:

```bash
git switch main
git status
git branch archive/pre-sync
```

Then:

```bash
git fetch origin
git reset --hard origin/main
```

Verify:

```bash
git rev-parse HEAD
git rev-parse origin/main
python src/main.py
```

### R6.8 dry-run proof

The scenario was executed with an independent shared remote.

Validated:

```text
archive/pre-sync
=
old local HEAD

new local HEAD
=
origin/main

working tree
=
clean
```

The old student history remained recoverable through the archive branch.

### Do not

Use `reset --hard` when:

```text
working tree is dirty
local work has not been preserved
authoritative baseline is unclear
```

## 11. Scenario 7 - merge conflict

A conflict is not a Git failure.

It means Git cannot safely decide the final content.

Typical status:

```text
UU <file>
```

### Recovery mode

```text
RESOLVE_AND_VALIDATE
```

Use:

```bash
git status
```

Read both versions and choose the intended final content.

Then:

```bash
git add <resolved-file>
git commit
python src/main.py
```

when MarketPulse business code is involved.

### R6.8 dry-run proof

The dry run created incompatible changes to the same line.

Observed:

```text
merge exit code != 0
UU config.txt
```

After human resolution and commit:

```text
working tree = clean
resolved value = chosen final content
```

### Do not

```text
blindly keep ours
blindly keep theirs
force-delete branches
rewrite history only to avoid understanding the conflict
```

## 12. Scenario 8 - missing checkpoint evidence

First classify why the evidence is missing.

### Case A - external dependency prevented capture

Examples:

```text
Yahoo unavailable
GitHub unavailable
Dash package index unavailable
```

Use:

```text
PENDING_EXTERNAL
```

and complete the real proof during an instructor-approved recovery window.

### Case B - locally controllable screenshot forgotten

Examples:

```text
terminal screenshot forgotten
Git status screenshot forgotten
filename incorrect
```

Do not use `PENDING_EXTERNAL`.

Recover from real current state when possible:

```bash
python src/main.py
git status
git log --oneline --graph --decorate --all
```

If the exact historical state no longer exists, the instructor may use a live micro-validation to assess the skill.

Do not manufacture an old screenshot or rewrite Git history solely to recreate a prettier image.

The canonical submission may still need an instructor-approved late capture or replacement decision.

### Case C - screenshot contains a secret

Do not commit it.

Retake or sanitize evidence from a safe real state.

If a secret has already been committed, stop normal evidence work and follow the institution's credential-rotation or incident procedure.

## 13. Quick decision matrix

| Incident | Continue learning? | Authorized recovery | Evidence state |
|---|---|---|---|
| Student environment broken | Yes | Pair temporarily or fresh environment | Normal once restored |
| GitHub unavailable | Yes | Continue local Git, push later | Remote proof pending |
| Yahoo unavailable | Yes | Validate analytics with local CSV | Yahoo proof `PENDING_EXTERNAL` |
| Bloomberg LIVE unavailable | Yes | `APPROVED_SAMPLE` | Valid fallback evidence, not LIVE |
| Dash cannot install | Partly | Validate terminal + snapshot, install later | Dashboard proof `PENDING_EXTERNAL` |
| Student main late/divergent | Yes | Archive and align | Normal after sync |
| Merge conflict | Yes | Resolve and validate | Normal after resolution |
| Local screenshot forgotten | Usually | Recapture real state / live validation | Not `PENDING_EXTERNAL` |

## 14. Instructor stop conditions

Stop the current workflow before proceeding when:

```text
a secret appears in Git or evidence
origin points to the wrong repository before destructive sync
working tree is dirty before reset --hard
provider mode is being mislabelled
student is about to fabricate remote evidence
analytics are being rewritten only to hide provider failure
student is about to overwrite unpreserved local work
```

## 15. Recovery does not change assessment meaning

The same distinction remains true during incidents:

```text
Presence
!=
work
!=
competence
```

Recovery paths preserve an opportunity to demonstrate competence.

They do not award evidence that was never produced.

Students remain responsible for being able to:

```text
explain
run
modify
debug
identify personal contribution
```

## 16. Instructor pre-session checklist

Before a session, verify the items relevant to that TD:

```text
[ ] instructor repository accessible
[ ] starter runtime known-good
[ ] team-fork model understood
[ ] Yahoo reference available before TD08
[ ] Bloomberg session mode selected before TD09
[ ] Bloomberg fallback assets parse and match expected output
[ ] Dash dependencies expected before TD11
[ ] evidence recovery rule understood before checkpoint capture
[ ] no recovery path requires fabricated evidence
```

## 17. Cross-reference map

Use this playbook together with:

```text
docs/01_STUDENT_ONBOARDING.md
=
student environment and temporary pairing

docs/03_GITHUB_TEAM_WORKFLOW.md
=
team repository, branches and synchronization

docs/04_CHECKPOINTS_AND_EVIDENCE.md
=
PENDING_EXTERNAL, filenames and security

docs/09_YAHOO_FINANCE_INSTRUCTOR_REFERENCE.md
=
Yahoo diagnostics

docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
=
LIVE vs APPROVED_SAMPLE

docs/11_BLOOMBERG_PROVIDER_SCAFFOLD.md
=
Bloomberg fallback implementation

docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md
=
terminal/dashboard shared boundary
```

## 18. Final principle

```text
External failure
!=
learning failure
```

The instructor should preserve the learning objective whenever possible while keeping all claims honest.

```text
continue what is controllable
preserve work
label what is external
recover later
never fabricate success
```
