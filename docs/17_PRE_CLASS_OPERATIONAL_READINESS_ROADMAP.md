# R8 - Pre-Class Operational Readiness Roadmap

## 1. Purpose

R7 closed the Legacy content operationalization stream.

The repository is now structurally ready, but several external teaching conditions still require real pre-class validation.

R8 converts the remaining operational gates into one controlled execution roadmap.

R8 does not redesign:

```text
CORE
OPTIONAL
ADVANCED
INSTRUCTOR
```

R8 does not reopen:

```text
R6 teaching baseline
R7 Legacy closure
```

R8 exists to answer:

```text
What must be verified
before each teaching stage
so that classroom delivery is operational?
```

## 2. Governing sources

R8 consumes the existing contracts from:

```text
docs/14_TEACHING_READINESS_AND_DRY_RUN_PLAN.md
docs/15_INSTRUCTOR_CONTINGENCY_AND_RECOVERY_PLAYBOOK.md
docs/16_TEACHING_BASELINE_RELEASE.md
docs/advanced/README.md
docs/legacy/08_R7_LEGACY_CLOSURE_AUDIT.md
```

R8 is an execution layer over those documents.

If a conflict appears:

```text
R6 / R7 canonical contract
wins
```

## 3. Readiness model

Every operational gate must use one of:

```text
NOT_STARTED
IN_PROGRESS
PASS
PENDING_EXTERNAL
BLOCKED
DEFERRED
```

Meaning:

### NOT_STARTED

No real pre-class verification has been executed yet.

### IN_PROGRESS

Verification is underway but evidence is incomplete.

### PASS

The exact required environment or workflow has been executed successfully.

### PENDING_EXTERNAL

The repository-side preparation is complete but the required external environment is not yet available for validation.

### BLOCKED

The required environment exists but the validation failed.

A BLOCKED gate requires:

```text
root cause
+
contingency
+
retest
```

### DEFERRED

The feature will not be offered during the current teaching window.

DEFERRED is acceptable only for optional Advanced material.

It is not acceptable for a required CORE pre-class gate.

## 4. Evidence rule

No gate may become PASS from:

```text
documentation inspection only
assumption
mocked provider success
APPROVED_SAMPLE presented as LIVE
static code syntax only
```

PASS requires real execution of the gate-specific workflow.

Evidence should record:

```text
date
environment
command or action
observed result
status
fallback if applicable
```

Secrets, credentials and sensitive environment information must never be committed.

## 5. R8 roadmap

```text
R8.1  Student bootstrap and clone validation
R8.2  GitHub collaboration validation
R8.3  Yahoo Finance network validation
R8.4  Bloomberg teaching-mode validation
R8.5  Dash runtime validation
R8.6  Final clean reproduction validation
R8.7  Advanced external-gate validation
R8.8  Teaching-day recovery runbook
R8.9  Session readiness matrix and final GO / NO-GO
```

Dependency view:

```text
R8.1
  |
  v
R8.2

R8.3
  |
  +------+
  |      |
  v      v
R8.4   R8.5
  |      |
  +---+--+
      |
      v
    R8.6

R8.7
independent optional advanced gates

R8.1-R8.6
      |
      v
    R8.8
      |
      v
    R8.9
```

## 6. R8.1 - Student bootstrap and clone validation

Source:

```text
Pre-class Gate A
docs/16_TEACHING_BASELINE_RELEASE.md
```

Timing:

```text
before the first TD session
```

Status:

```text
PENDING_EXTERNAL
```

Evidence:

```text
docs/readiness/01_R8_1_STUDENT_BOOTSTRAP_AND_CLONE_VALIDATION.md
```

Current result:

```text
repository-side bootstrap
=
PASS

actual clone from validation runner
=
BLOCKED BY RUNNER DNS

actual clone from intended ESILV/student network
=
PENDING_EXTERNAL
```

### Required environment

Use the environment students are expected to use or the closest approved equivalent.

### Validate

```text
repository reachable
clone works
repository root is correct
Python available
Git available
starter files visible
python src/main.py works
```

Canonical flow:

```bash
git clone <canonical-repository-url>
cd esilv-marketpulse
python --version
git --version
python src/main.py
```

Then verify the TD01 inspection path:

```bash
ls
ls data/sample
head data/sample/prices.csv
grep AAPL data/sample/prices.csv
```

### Acceptance criteria

```text
[ ] actual clone from intended teaching/student network
[ ] repository opens from a fresh checkout
[ ] Python works
[ ] Git works
[ ] starter data is readable
[ ] python src/main.py succeeds
[ ] no local-only file is required
```

### Failure policy

If clone fails but repository access exists through another approved mechanism:

```text
record BLOCKED
apply contingency
do not mark PASS
```

## 7. R8.2 - GitHub collaboration validation

Source:

```text
Pre-class Gate B
```

Timing:

```text
before TD05-TD06
```

Status:

```text
NOT_STARTED
```

### Validate with a real disposable or teaching-team repository

```text
fork or approved team repository exists
collaborator access works
feature branch push works
Pull Request targets team main
Files changed is correct
second account can review
review can be submitted
reviewed PR can be merged
main can be resynchronized
```

### Acceptance criteria

```text
[ ] real feature branch pushed
[ ] real Pull Request opened
[ ] source branch verified
[ ] target main verified
[ ] Files changed verified
[ ] review submitted from another account
[ ] merge completed through GitHub
[ ] post-merge pull / sync succeeds
```

### Repository hygiene

Do not create synthetic teaching PRs in the canonical instructor repository merely to generate evidence.

Prefer:

```text
disposable team fork
or
real teaching team repository
```

## 8. R8.3 - Yahoo Finance network validation

Source:

```text
Pre-class Gate C
```

Timing:

```text
before TD08
```

Status:

```text
NOT_STARTED
```

### Validate

In the actual teaching environment:

```bash
python -m pip install yfinance
python -m pip show yfinance
```

Then retrieve non-empty:

```text
AAPL
^GSPC
```

with:

```text
period = 1mo
interval = 1d
auto_adjust = False
```

### Acceptance criteria

```text
[ ] package installation works
[ ] network request works
[ ] AAPL result is non-empty
[ ] ^GSPC result is non-empty
[ ] canonical mapping remains AAPL -> AAPL
[ ] canonical mapping remains ^GSPC -> SP500
[ ] TD08 provider path executes
```

### Failure policy

If Yahoo is unavailable:

```text
continue analytics with approved local data
mark Yahoo evidence PENDING_EXTERNAL
use contingency playbook
```

## 9. R8.4 - Bloomberg teaching-mode validation

Source:

```text
Pre-class Gate D
```

Timing:

```text
before TD09
```

Status:

```text
NOT_STARTED
```

### Required decision

Choose explicitly:

```text
LIVE
or
APPROVED_SAMPLE
```

### LIVE path

Validate the exact approved Bloomberg access mechanism.

Record only observed:

```text
identifiers
fields
connector behaviour
returned rows
```

Do not infer availability from historical course material.

### APPROVED_SAMPLE path

Verify the fallback remains usable:

```text
21 AAPL rows
21 SP500 rows
42 canonical rows
2026-09-01 to 2026-09-30
```

### Acceptance criteria

```text
[ ] teaching mode chosen explicitly
[ ] mode documented honestly
[ ] LIVE access verified if LIVE selected
[ ] APPROVED_SAMPLE files verified if fallback selected
[ ] provider mapping still coherent
[ ] no fallback evidence presented as LIVE
```

## 10. R8.5 - Dash runtime validation

Source:

```text
Pre-class Gate E
```

Timing:

```text
before TD11
```

Status:

```text
NOT_STARTED
```

### Validate

From the teaching environment:

```bash
python -m pip install -r requirements.txt
python -m pip show dash
python -m pip show plotly
python src/dashboard.py
```

Open the local application.

Verify:

```text
provider visible
instrument visible
benchmark visible
lookback visible
interval visible
instrument return visible
benchmark return visible
relative performance visible
two base-100 series visible
```

Architecture check:

```text
dashboard
->
build_market_snapshot(...)

not

dashboard
->
provider-specific acquisition
```

### Acceptance criteria

```text
[ ] dash installed
[ ] plotly installed
[ ] dashboard server starts
[ ] browser page opens
[ ] required values visible
[ ] base-100 chart visible
[ ] no duplicated analytics
[ ] no direct provider logic in dashboard
```

## 11. R8.6 - Final clean reproduction validation

Source:

```text
Pre-class Gate F
```

Timing:

```text
before TD12 / Checkpoint C
```

Status:

```text
NOT_STARTED
```

### Validate from a clean environment

```bash
git clone <validation-repository>
cd <validation-repository>
python -m pip install -r requirements.txt
python src/main.py
python src/dashboard.py
```

### Acceptance criteria

```text
[ ] clean clone succeeds
[ ] requirements install succeeds
[ ] terminal runtime succeeds
[ ] dashboard runtime succeeds
[ ] selected provider/mode is documented
[ ] fallback use is explicit when applicable
[ ] no local workstation dependency is required
```

A failed install is not successful reproducibility evidence.

## 12. R8.7 - Advanced external-gate validation

This lot concerns optional Advanced supports only.

It does not block CORE delivery when the corresponding Advanced activity is not offered.

Current targets:

```text
ADV-RMT-01
ADV-RMT-03
ADV-BBG-01
ADV-DASH-01
ADV-DASH-02
```

### R8.7.1 - ADV-RMT-01 SSH Fundamentals

Initial status:

```text
PENDING_EXTERNAL
```

Required:

```text
real SSH client
approved remote host
approved account model
successful connect / inspect / disconnect
```

If unavailable:

```text
DEFERRED
```

is acceptable for the current course delivery.

### R8.7.2 - ADV-RMT-03 systemd Service

Initial status:

```text
PENDING_EXTERNAL
```

Required:

```text
approved systemd host
approved permissions
unit validation
start
status
journal inspection
stop
cleanup
```

### R8.7.3 - ADV-BBG-01 Reference Data

Initial status:

```text
PENDING_EXTERNAL
```

Required:

```text
Bloomberg LIVE
approved access mechanism
observed reference field
observed value
no fabricated evidence
```

If LIVE is unavailable:

```text
DEFERRED
```

Do not use APPROVED_SAMPLE as fake reference-data LIVE proof.

### R8.7.4 - ADV-DASH-01 Callback

Initial status:

```text
PENDING_EXTERNAL
```

Required:

```text
real Dash runtime
callback executes
visible output changes
no provider-specific logic in callback
no duplicated analytics
```

### R8.7.5 - ADV-DASH-02 Instrument Selector

Initial status:

```text
PENDING_EXTERNAL
```

Required:

```text
ADV-DASH-01 PASS
parameterized application function
at least two coherent instruments
figure updates
provider boundary preserved
```

## 13. Advanced promotion procedure

When an Advanced gate passes:

```text
1. update support status
   PENDING_EXTERNAL -> READY_TO_TEACH

2. update docs/advanced/README.md

3. update docs/labs/README.md

4. activate the TD link

5. update docs/legacy/03 backlog

6. update docs/legacy/05 migration registry

7. retain the R7 closure
```

R7 does not need to be reopened when:

```text
support contract unchanged
external gate genuinely passed
CORE unchanged
checkpoint contract unchanged
```

## 14. R8.8 - Teaching-day recovery runbook

Status:

```text
NOT_STARTED
```

Purpose:

```text
convert the contingency playbook
into a compact classroom execution checklist
```

Target document:

```text
docs/instructor/03_TEACHING_DAY_OPERATIONAL_RUNBOOK.md
```

It should include:

```text
before students arrive
first 10 minutes
clone failure
Python failure
Git failure
GitHub outage
Yahoo outage
Bloomberg LIVE failure
Dash failure
late student recovery
conflict recovery
checkpoint evidence recovery
end-of-session cleanup
```

The runbook must point to:

```text
docs/15_INSTRUCTOR_CONTINGENCY_AND_RECOVERY_PLAYBOOK.md
```

instead of duplicating its full reasoning.

## 15. R8.9 - Session readiness matrix and final GO / NO-GO

Status:

```text
NOT_STARTED
```

Target document:

```text
docs/instructor/04_SESSION_READINESS_MATRIX.md
```

The matrix should track readiness by teaching stage:

| Teaching stage | Required gates |
|---|---|
| TD01-TD04 | R8.1 |
| TD05-TD06 | R8.1 + R8.2 |
| TD07 | R8.1 + R8.2 |
| TD08 | R8.1 + R8.2 + R8.3 |
| TD09-TD10 | R8.1 + R8.2 + R8.3 + R8.4 |
| TD11 | R8.1 + R8.2 + R8.3 + R8.4 + R8.5 |
| TD12 / Checkpoint C | R8.1-R8.6 |

Advanced gates are tracked separately.

### GO rule

A teaching stage is:

```text
GO
```

when every required CORE gate for that stage is:

```text
PASS
or
has an explicitly approved CORE fallback
```

### NO-GO rule

Use:

```text
NO-GO
```

when a required CORE gate is BLOCKED and no approved fallback exists.

### Advanced rule

A blocked optional Advanced gate:

```text
does not create CORE NO-GO
```

It simply leaves that Advanced activity inactive.

## 16. Current status board

| Lot | Scope | Status |
|---|---|---|
| R8.1 | Student bootstrap and clone validation | PENDING_EXTERNAL |
| R8.2 | GitHub collaboration validation | NEXT |
| R8.3 | Yahoo Finance network validation | NOT_STARTED |
| R8.4 | Bloomberg teaching-mode validation | NOT_STARTED |
| R8.5 | Dash runtime validation | NOT_STARTED |
| R8.6 | Final clean reproduction validation | NOT_STARTED |
| R8.7 | Advanced external-gate validation | NOT_STARTED |
| R8.8 | Teaching-day recovery runbook | NOT_STARTED |
| R8.9 | Session readiness matrix and final GO / NO-GO | NOT_STARTED |

## 17. R8 acceptance criteria

R8 is complete only when:

```text
[ ] R8.1 resolved
[ ] R8.2 resolved
[ ] R8.3 resolved
[ ] R8.4 resolved
[ ] R8.5 resolved
[ ] R8.6 resolved
[ ] R8.7 every Advanced external gate is PASS or DEFERRED
[ ] R8.8 operational runbook complete
[ ] R8.9 session readiness matrix complete
[ ] no fake external success is recorded
[ ] CORE remains unchanged unless an explicit new change process is opened
```

## 18. Change-control rule

R8 may update:

```text
readiness evidence
instructor operational docs
external-gate statuses
Advanced activation links
contingency references
```

R8 must not silently change:

```text
CORE scope
12-TD sequence
checkpoint requirements
analytics formulas
provider canonical contract
snapshot contract
assessment weights
```

If such a change becomes necessary:

```text
stop R8
open an explicit remediation change
revalidate the affected R6 baseline contract
```

## 19. Current next action

```text
R8.2
GitHub collaboration validation
```

R8.1 repository-side bootstrap checks are complete.

The real clone from the intended ESILV/student network remains PENDING_EXTERNAL and is still required before final teaching GO.
