# MarketPulse Teaching Baseline Release

## 1. Release decision

Date:

```text
2026-10-05
```

Decision:

```text
TEACHING BASELINE READY
WITH EXTERNAL PRE-CLASS CHECKS
```

This is the frozen teaching baseline for the guided MarketPulse sequence:

```text
18 hours
12 TDs
4 pedagogical waves
3 checkpoint phases
1 progressive application
```

No unresolved repository or pedagogical blocker remains in the validated CORE path.

The remaining checks depend on real external environments, accounts, networks or services and must not be represented as already executed.

## 2. What is frozen

The baseline freezes:

```text
functional contract
TD01-TD12 sequence
CORE scope per TD
repository evolution
Git collaboration model
canonical row contract
shared analytics contract
provider boundaries
application snapshot contract
terminal and dashboard commands
checkpoint evidence contract
provider fallback rules
instructor recovery playbook
```

The canonical CORE runtime remains:

```bash
python src/main.py
python src/dashboard.py
```

The starter intentionally does not contain every final-stage student file on day one.

## 3. Internal validation result

The repository-side and locally executable validation is complete.

Validated areas include:

```text
starter runtime
starter data
TD01-TD02 progression
local Git workflow
branch and merge workflow
remote Git mechanics through a local shared remote
team-baseline alignment
provider-neutral analytics
Yahoo provider contract with controlled external boundary
Bloomberg APPROVED_SAMPLE normalization
full one-month Bloomberg fallback
shared build_market_snapshot(...) contract
import-safe main.py
real Plotly figure construction
clean local clone reproducibility
checkpoint package structure
evidence naming and security
fast-forward evidence capture
outage evidence semantics
instructor contingency recovery
```

R1 through R5 are closed.

R6.1, R6.3 and R6.8 are fully executed and closed.

R6.2, R6.4, R6.5, R6.6 and R6.7 are accepted with the external pre-class gates defined below.

## 4. Why external checks remain

Some course behaviours cannot be proven honestly without the real teaching environment.

Examples:

```text
student-network git clone
team-fork GitHub Pull Request
review by another student account
PyPI package installation
Yahoo LIVE retrieval
real Dash browser serving
clean network-enabled final reproduction
```

These are environment checks, not hidden repository defects.

The release policy is therefore:

```text
validated CORE contract
+
registered external gates
+
documented recovery paths
=
ready teaching baseline
```

not:

```text
pretend every external dependency already succeeded
```

## 5. Pre-class Gate A - bootstrap

Timing:

```text
before TD01
```

Verify from the intended student environment:

```bash
git clone https://github.com/tawounfouet/esilv-marketpulse.git
cd esilv-marketpulse
python --version
git --version
python src/main.py
```

Also verify that the normal fork flow is available.

Expected result:

```text
repository reachable
starter runnable
Python available
Git available
```

This closes the external item carried by R6.2.

## 6. Pre-class Gate B - GitHub collaboration

Timing:

```text
before TD05-TD06
```

Use a real disposable or actual team fork.

Verify:

```text
team collaborators can access the fork
student feature branch can be pushed
Pull Request can target team main
Files changed shows the intended diff
another account can submit meaningful review
reviewed PR can be merged
students can resynchronize main
```

Do not use the instructor repository for synthetic student evidence.

This closes the GitHub UI items carried by R6.4 and R6.7.

## 7. Pre-class Gate C - Yahoo

Timing:

```text
before TD08
```

In a network-enabled teaching environment:

```bash
python -m pip install yfinance
python -m pip show yfinance
```

Then verify non-empty data for:

```text
AAPL
^GSPC
```

using:

```text
period = 1mo
interval = 1d
auto_adjust = False
```

Confirm the canonical mapping remains:

```text
AAPL  -> AAPL
^GSPC -> SP500
```

If Yahoo is unavailable, follow:

```text
docs/15_INSTRUCTOR_CONTINGENCY_AND_RECOVERY_PLAYBOOK.md
```

and keep remote evidence as `PENDING_EXTERNAL`.

This closes the external provider items carried by R6.5 and R6.7.

## 8. Pre-class Gate D - Bloomberg session mode

Timing:

```text
before TD09
```

Choose explicitly:

```text
LIVE
or
APPROVED_SAMPLE
```

If LIVE is selected, validate the actual instructor-approved access mechanism and record only observed fields.

If LIVE is unavailable, the already validated fallback path is:

```text
Bloomberg stage - APPROVED_SAMPLE
```

with:

```text
21 AAPL rows
21 SP500 rows
42 canonical expected rows
2026-09-01 to 2026-09-30
```

APPROVED_SAMPLE remains valid teaching evidence for the provider-stage fallback.

It is never LIVE Bloomberg evidence.

## 9. Pre-class Gate E - Dash

Timing:

```text
before TD11
```

Verify:

```bash
python -m pip install -r requirements.txt
python -m pip show dash
python -m pip show plotly
python src/dashboard.py
```

Open the local application and confirm:

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

The dashboard must consume `build_market_snapshot(...)`.

It must not acquire provider data or recompute analytics.

This closes the real-Dash item carried by R6.6 and R6.7.

## 10. Pre-class Gate F - final clean reproduction

Timing:

```text
before TD12 / Checkpoint C
```

From a clean network-enabled environment:

```bash
git clone <team-or-validation-repository> marketpulse-repro
cd marketpulse-repro
python -m pip install -r requirements.txt
python src/main.py
python src/dashboard.py
```

The final provider or mode must be documented honestly.

A failed installation is not successful reproducibility evidence.

This closes the clean-install item carried by R6.6 and R6.7.

## 11. Gate failure policy

A failed external gate does not authorize fabricated success.

Use the contingency playbook.

Typical outcomes:

```text
GitHub unavailable
-> CONTINUE_LOCAL

Yahoo unavailable
-> continue analytics with local CSV
-> Yahoo evidence PENDING_EXTERNAL

Bloomberg LIVE unavailable
-> APPROVED_SAMPLE

Dash package unavailable
-> validate terminal + snapshot
-> dashboard evidence PENDING_EXTERNAL

late local history
-> ARCHIVE_AND_ALIGN

merge conflict
-> RESOLVE_AND_VALIDATE
```

A locally forgotten screenshot is not `PENDING_EXTERNAL`.

## 12. Release acceptance map

| R6 lot | Release disposition |
|---|---|
| R6.1 Starter runtime | DONE |
| R6.2 Clean-clone/bootstrap | ACCEPTED - Pre-class Gate A |
| R6.3 Wave 1 | DONE |
| R6.4 Wave 2 | ACCEPTED - Pre-class Gate B |
| R6.5 Wave 3 | ACCEPTED - Pre-class Gate C |
| R6.6 Wave 4 | ACCEPTED - Gates B, C, D, E, F as applicable |
| R6.7 Checkpoints/evidence | ACCEPTED - Gates B, C, E, F for real captures |
| R6.8 Contingencies | DONE |
| R6.9 Baseline freeze | DONE |

There is no remaining `NOT TESTED` R6 lot.

## 13. Canonical readiness documents

Use:

```text
docs/14_TEACHING_READINESS_AND_DRY_RUN_PLAN.md
=
detailed execution evidence

docs/15_INSTRUCTOR_CONTINGENCY_AND_RECOVERY_PLAYBOOK.md
=
incident and fallback operations

docs/16_TEACHING_BASELINE_RELEASE.md
=
release decision and pre-class gates
```

The evidence source of truth remains:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

## 14. Change policy after freeze

Changes that alter any of these require renewed targeted validation:

```text
TD sequencing
CORE commands
canonical row fields
analytics formulas
provider identifier mappings
snapshot keys
checkpoint filenames
security rules
fallback meaning
```

External-service refreshes may be documented without redesigning the CORE when the contract remains unchanged.

Examples:

```text
new yfinance release
classroom Bloomberg connector change
GitHub UI wording change
Dash startup variation
```

Update the relevant instructor reference and rerun the affected pre-class gate.

## 15. Final release statement

```text
12 coherent labs
+
3 coherent checkpoint packages
+
tested starter
+
tested progressive application contracts
+
safe provider fallbacks
+
tested Git recovery mechanics
+
documented instructor contingency paths
+
explicit real-environment gates
=
TEACHING BASELINE READY
WITH EXTERNAL PRE-CLASS CHECKS
```

The baseline is ready to teach.

External dependencies must still be checked at the appropriate pre-class gates because their availability is not controlled by the repository.
