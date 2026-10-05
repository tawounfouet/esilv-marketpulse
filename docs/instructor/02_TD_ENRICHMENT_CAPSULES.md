# TD Enrichment Capsules

## 1. Purpose

This document provides short instructor-side enrichment capsules that may be used during the MarketPulse TD sequence.

A capsule is:

```text
5 to 10 minutes
optional to deliver
teacher-led
no new student artifact
no checkpoint evidence
no hidden prerequisite
```

The purpose is to preserve useful Legacy depth without expanding the frozen 18-hour CORE.

Canonical deep-dive sources:

```text
docs/instructor/deep-dives/
```

Canonical student labs:

```text
docs/labs/
```

Canonical advanced student practice:

```text
docs/advanced/
```

## 2. Delivery rule

Use a capsule only when at least one condition is true:

```text
a student question naturally opens the topic
the concept resolves a recurring misconception
the class is ahead of the CORE timebox
the concept improves understanding of the current TD
```

Do not use a capsule merely because it exists.

Priority rule:

```text
CORE completion
>
checkpoint readiness
>
capsule
```

If the class is behind schedule:

```text
SKIP THE CAPSULE
```

## 3. Capsule contract

Every capsule contains:

```text
capsule ID
primary TD
source deep dive
duration
trigger
teaching objective
micro-sequence
observable understanding check
stop point
explicit non-impact statement
```

No capsule may:

```text
change a TD Definition of Done
create checkpoint evidence
become a mandatory exercise
require a new dependency
activate a PENDING_EXTERNAL advanced lab
change the canonical runtime
```

## 4. TD coverage map

| TD | Capsule | Topic | Default delivery |
|---|---|---|---|
| TD01 | CAP-LNX-01 | Unix philosophy | RECOMMENDED if time allows |
| TD01 | CAP-LNX-02 | Permissions troubleshooting | ON_DEMAND |
| TD02 | None | Keep focus on Python + CSV/JSON | SKIP |
| TD03 | CAP-GIT-01 | Staging snapshot mental model | RECOMMENDED |
| TD03 | CAP-GIT-02 | HEAD and refs | RECOMMENDED if questions arise |
| TD03 | CAP-GIT-03 | Git object model | ON_DEMAND |
| TD04 | CAP-GIT-04 | Merge vs rebase | ON_DEMAND |
| TD05 | CAP-GIT-05 | Remote-tracking refs and fetch vs pull | RECOMMENDED |
| TD06 | None | Keep focus on review quality | SKIP unless CAP-GIT-04 is requested |
| TD07 | None | Keep focus on analytics contract | SKIP |
| TD08 | None | Keep focus on Yahoo provider integration | SKIP |
| TD09 | CAP-BBG-01 | Bloomberg Terminal and identifiers | RECOMMENDED |
| TD09 | CAP-BBG-02 | BDP / BDS / BDH | RECOMMENDED if time allows |
| TD09 | CAP-BBG-03 | Request/Response vs Subscription | ON_DEMAND |
| TD10 | CAP-BBG-04 | xbbg vs blpapi | ON_DEMAND |
| TD11 | None | Keep focus on static dashboard CORE | SKIP |
| TD12 | None | Keep focus on reproducibility and release | SKIP |

The absence of a capsule is intentional.

It means:

```text
do not add conceptual depth
unless a real teaching need appears
```

# Linux capsules

## CAP-LNX-01 - Unix Philosophy

Primary TD:

```text
TD01
```

Source:

```text
docs/instructor/deep-dives/INS_LNX_01_UNIX_PHILOSOPHY.md
```

Duration:

```text
5 minutes
```

Delivery:

```text
RECOMMENDED if the CORE is on schedule
```

### Trigger

Use after students have run:

```text
cat
head
grep
```

or when someone asks:

```text
Why use terminal commands instead of opening files manually?
```

### Teaching objective

Students should leave with this mental model:

```text
small tools
+
text streams
+
composition
=
engineering leverage
```

### Micro-sequence

1. Show:

```bash
head data/sample/prices.csv
```

2. Show:

```bash
grep AAPL data/sample/prices.csv
```

3. If appropriate, demonstrate only:

```bash
grep AAPL data/sample/prices.csv | head
```

4. Explain:

```text
the first command produces text
the second consumes text
the pipe connects them
```

### Understanding check

Ask:

```text
What is the advantage of a command that does one small job well?
```

Expected idea:

```text
it can be combined with other tools
```

### Stop point

Stop before:

```text
awk
sed
regex
shell scripting
process management
```

Those belong to ADVANCED material.

### Non-impact statement

```text
No student deliverable.
No checkpoint evidence.
No CORE DoD change.
```

## CAP-LNX-02 - Permissions Troubleshooting

Primary TD:

```text
TD01
```

Source:

```text
docs/instructor/deep-dives/INS_LNX_02_PERMISSIONS_TROUBLESHOOTING.md
```

Duration:

```text
5 minutes
```

Delivery:

```text
ON_DEMAND
```

### Trigger

Use only when a real permission error appears or when students encounter:

```text
Permission denied
```

### Teaching objective

Students should understand the troubleshooting order:

```text
what operation failed?
who owns the file?
which permission is missing?
```

### Micro-sequence

1. Inspect:

```bash
ls -l <path>
```

2. Identify:

```text
owner
group
others
read/write/execute
```

3. Explain why:

```text
chmod 777
```

is not a generic fix.

4. If the failure genuinely concerns execute permission, explain the narrow form:

```bash
chmod u+x <file>
```

without turning it into a required student exercise.

### Understanding check

Ask:

```text
Why should we identify the missing permission before changing permissions?
```

### Stop point

Stop before:

```text
ACL
setuid
setgid
system-wide ownership changes
sudo-based administration
```

### Non-impact statement

The dedicated practice remains:

```text
ADV-LNX-02
```

not this capsule.

# Git capsules

## CAP-GIT-01 - Staging Snapshot Mental Model

Primary TD:

```text
TD03
```

Source:

```text
docs/instructor/deep-dives/INS_GIT_01_STAGING_MENTAL_MODEL.md
```

Duration:

```text
7 minutes
```

Delivery:

```text
RECOMMENDED
```

### Trigger

Use immediately after students first combine:

```text
git diff
git add
git diff --staged
```

### Teaching objective

Students should understand:

```text
working tree
      |
      | git add
      v
staging area
      |
      | git commit
      v
commit
```

and especially:

```text
git add
=
stage the current content snapshot
```

### Micro-sequence

1. Edit one file.

2. Run:

```bash
git diff
git add <file>
git diff --staged
```

3. Edit the same file again.

4. Run:

```bash
git status
git diff
git diff --staged
```

5. Ask students to identify:

```text
staged edit
unstaged edit
```

### Understanding check

Ask:

```text
If I commit now, which version is committed?
```

Expected:

```text
the staged snapshot
```

### Stop point

Stop before:

```text
raw index internals
git update-index internals
manual .git manipulation
```

### Non-impact statement

This clarifies existing TD03 CORE commands.

It does not add a new TD03 requirement.

## CAP-GIT-02 - HEAD and Refs

Primary TD:

```text
TD03
```

Source:

```text
docs/instructor/deep-dives/INS_GIT_02_HEAD_REFS_REMOTE_TRACKING.md
```

Duration:

```text
5 minutes
```

Delivery:

```text
RECOMMENDED if students ask about git log decorations
```

### Trigger

Use when students see:

```text
HEAD -> main
```

in Git output.

### Teaching objective

Students should distinguish:

```text
HEAD
=
current checkout context

main
=
local branch reference
```

### Micro-sequence

Run:

```bash
git log --oneline --decorate -5
```

Draw:

```text
HEAD
 |
 v
main
 |
 v
commit
```

Explain that the branch name moves as commits are created.

### Understanding check

Ask:

```text
Is HEAD the name of the latest commit in the whole repository?
```

Expected:

```text
No.
It identifies the current checkout context.
```

### Stop point

Stop before:

```text
detached HEAD recovery
packed-refs
editing .git/HEAD
```

unless a real student incident requires it.

### Non-impact statement

No new command is required for TD03 completion.

## CAP-GIT-03 - Git Object Model

Primary TD:

```text
TD03
```

Source:

```text
docs/instructor/deep-dives/INS_GIT_03_OBJECT_MODEL.md
```

Duration:

```text
5 minutes
```

Delivery:

```text
ON_DEMAND
```

### Trigger

Use only when a student asks:

```text
What is a commit really?
Why does a commit have a hash?
Why is a branch lightweight?
```

### Teaching objective

Introduce only:

```text
blob
tree
commit
branch reference
```

### Micro-sequence

Draw:

```text
file content
    |
    v
blob

directory snapshot
    |
    v
tree

tree + parent + metadata
    |
    v
commit
```

Optionally show:

```bash
git show --stat HEAD
```

### Understanding check

Ask:

```text
Does creating a branch duplicate the whole repository?
```

Expected:

```text
No.
A branch is mainly a movable reference to a commit.
```

### Stop point

Do not reproduce:

```text
manual git hash-object lab
zlib internals
direct .git/objects manipulation
```

### Non-impact statement

The Git object model remains instructor depth, not CORE.

## CAP-GIT-04 - Merge vs Rebase

Primary TD:

```text
TD04
```

Reusable on demand:

```text
TD05
TD06
```

Source:

```text
docs/instructor/deep-dives/INS_GIT_04_MERGE_VS_REBASE.md
```

Duration:

```text
7 minutes
```

Delivery:

```text
ON_DEMAND
```

### Trigger

Use when someone asks:

```text
Why merge instead of rebase?
Why not squash everything?
```

### Teaching objective

Students should retain:

```text
merge
=
combine existing histories

rebase
=
replay commits on a new base
and create new commit identities
```

### Micro-sequence

Draw:

```text
A---B---C main
     \
      D---E feature
```

Then show conceptually:

```text
merge
=
keep both histories + combine

rebase
=
replay D/E after C
```

Explain:

```text
shared-history rewriting
requires care
```

### Understanding check

Ask:

```text
Why can rebasing already shared commits be risky?
```

Expected:

```text
because commit identities and ancestry are rewritten
```

### Stop point

Stop before:

```text
interactive rebase commands
force-push workflows
squash policy design
Gitflow
```

### Non-impact statement

MarketPulse CORE remains merge-oriented.

## CAP-GIT-05 - Remote-Tracking Refs and fetch vs pull

Primary TD:

```text
TD05
```

Source:

```text
docs/instructor/deep-dives/INS_GIT_02_HEAD_REFS_REMOTE_TRACKING.md
```

Duration:

```text
7 minutes
```

Delivery:

```text
RECOMMENDED
```

### Trigger

Use after students have a real remote and before they confuse:

```text
main
origin/main
origin
```

### Teaching objective

Students should understand:

```text
origin
=
remote configuration

origin/main
=
local record of fetched remote main

main
=
local branch
```

and:

```text
fetch
=
refresh remote knowledge

pull
=
fetch + integration
```

### Micro-sequence

Run:

```bash
git remote -v
git fetch origin
git log --oneline --decorate --all -8
```

Draw:

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

Explain that `origin/main` moving does not automatically move local `main`.

### Understanding check

Ask:

```text
Does origin/main continuously query GitHub?
```

Expected:

```text
No.
It is local remote-tracking state updated by fetch-like operations.
```

### Stop point

Stop before:

```text
refspecs
manual remote-tracking ref manipulation
rebase-based pull policy
```

### Non-impact statement

The current TD05 team workflow remains unchanged.

# Bloomberg capsules

## CAP-BBG-01 - Terminal and Identifiers

Primary TD:

```text
TD09
```

Source:

```text
docs/instructor/deep-dives/INS_BBG_01_TERMINAL_IDENTIFIERS.md
```

Duration:

```text
5 minutes
```

Delivery:

```text
RECOMMENDED
```

### Trigger

Use when students first see:

```text
AAPL
->
AAPL US Equity

SP500
->
SPX Index
```

### Teaching objective

Students should understand:

```text
application identifier
!=
provider identifier
```

and why mapping belongs inside a provider boundary.

### Micro-sequence

Draw:

```text
AAPL
  |
  v
provider mapping
  |
  v
AAPL US Equity
  |
  v
provider data
  |
  v
canonical AAPL rows
```

### Understanding check

Ask:

```text
Should AAPL US Equity appear throughout analytics.py?
```

Expected:

```text
No.
Provider vocabulary should remain isolated.
```

### Stop point

Do not turn the capsule into a Terminal-navigation course.

Do not state unverified:

```text
fields
entitlements
connector availability
rate limits
```

as current facts.

### Non-impact statement

No LIVE Bloomberg access is required to understand the mapping concept.

## CAP-BBG-02 - BDP / BDS / BDH

Primary TD:

```text
TD09
```

Source:

```text
docs/instructor/deep-dives/INS_BBG_02_BDP_BDS_BDH.md
```

Duration:

```text
7 minutes
```

Delivery:

```text
RECOMMENDED if time allows
```

### Trigger

Use after the identifier mapping and before TD10 provider implementation.

### Teaching objective

Students should distinguish three conceptual request shapes:

```text
BDP
=
point/reference style

BDH
=
historical time series

BDS
=
bulk/set-like data
```

### Micro-sequence

Ask:

```text
MarketPulse wants one month of Daily prices.
Which request shape does that resemble?
```

Expected:

```text
historical time-series retrieval
```

Then reconnect to:

```text
date
ticker
open
high
low
close
volume
```

### Understanding check

Ask:

```text
Does MarketPulse need all Bloomberg request families to satisfy the CORE?
```

Expected:

```text
No.
Only the concepts required by the current provider stage.
```

### Stop point

Do not add:

```text
Excel Bloomberg implementation
extra packages
extra provider paths
```

to the CORE.

### Non-impact statement

Reference-data practice remains a separate advanced support and is currently environment-gated when LIVE validation is required.

## CAP-BBG-03 - Request/Response vs Subscription

Primary TD:

```text
TD09
```

Source:

```text
docs/instructor/deep-dives/INS_BBG_03_REQUEST_RESPONSE_SUBSCRIPTION.md
```

Duration:

```text
7 minutes
```

Delivery:

```text
ON_DEMAND
```

### Trigger

Use when a student asks:

```text
Why not update the dashboard continuously?
Why are we not streaming real-time prices?
```

### Teaching objective

Students should understand that acquisition architecture follows the business requirement.

Current CORE:

```text
1 month
Daily
bounded historical comparison
```

### Micro-sequence

Compare:

```text
Request/Response

ask
receive bounded result
finish
```

with:

```text
Subscription

register interest
receive continuing updates
maintain state
stop later
```

Then list the extra streaming concerns:

```text
continuous connection
event handling
timestamps
market hours
reconnect logic
state updates
```

### Understanding check

Ask:

```text
Would a streaming architecture improve the current learning objective enough to justify that complexity?
```

Expected:

```text
No.
It solves a different problem.
```

### Stop point

Stop before:

```text
websockets
stream processors
subscription callbacks
live dashboard refresh
```

### Non-impact statement

The bounded historical provider contract remains unchanged.

## CAP-BBG-04 - xbbg vs blpapi

Primary TD:

```text
TD10
```

Source:

```text
docs/instructor/deep-dives/INS_BBG_04_XBBG_VS_BLPAPI.md
```

Duration:

```text
7 minutes
```

Delivery:

```text
ON_DEMAND
```

### Trigger

Use when students ask:

```text
Why this Bloomberg Python library?
Why not call Bloomberg directly?
```

### Teaching objective

Students should retain the abstraction lesson:

```text
higher-level connector
or
lower-level API

both
belong behind the provider boundary
```

### Micro-sequence

Show:

```text
bad

main.py
-> Bloomberg-specific API
-> parsing
-> analytics
```

versus:

```text
preferred

main.py
-> bloomberg_provider.py
-> approved connector
-> canonical rows
-> analytics
```

### Understanding check

Ask:

```text
If we change Bloomberg connector technology,
which parts of MarketPulse should ideally stay unchanged?
```

Expected:

```text
main application contract
canonical rows
analytics
dashboard business logic
```

### Stop point

Do not:

```text
install both libraries for demonstration
change requirements.txt
claim current ESILV compatibility without verification
```

### Non-impact statement

This is an architecture capsule, not a connector-installation lab.

# TDs intentionally without planned capsules

## TD02

Reason:

```text
Python + CSV/JSON already has enough conceptual density.
Environment variables are available as ADV-LNX-04 after CORE completion.
```

Decision:

```text
NO PLANNED INSTRUCTOR CAPSULE
```

## TD06

Reason:

```text
Code-review quality should remain the focus.
CAP-GIT-04 may be reused only if merge/rebase questions arise.
```

Decision:

```text
NO DEFAULT CAPSULE
```

## TD07

Reason:

```text
The analytics contract is already conceptually dense.
Legacy quantitative depth was intentionally excluded from CORE.
```

Decision:

```text
NO CAPSULE
```

## TD08

Reason:

```text
Provider integration and normalization are the learning priority.
Do not add unrelated architecture depth during Yahoo integration.
```

Decision:

```text
NO CAPSULE
```

## TD11

Reason:

```text
The static Dash CORE already has presentation and runtime concerns.
Callbacks/selectors are ADVANCED and currently PENDING_EXTERNAL.
```

Decision:

```text
NO CAPSULE
```

## TD12

Reason:

```text
Final integration, clean-run proof and release evidence must dominate the session.
Advanced release/deployment work belongs after CORE completion.
```

Decision:

```text
NO CAPSULE
```

# Instructor quick-selection matrix

If only one enrichment capsule is used per wave, prefer:

| Wave | Preferred capsule | Why |
|---|---|---|
| Wave 1 | CAP-LNX-01 | Explains why terminal composition matters |
| Wave 2 | CAP-GIT-01 | Resolves the most common Git mental-model confusion |
| Wave 3 | None | Protect analytics/provider timebox |
| Wave 4 | CAP-BBG-01 | Connects provider identity to application architecture |

If the group is advanced:

```text
Wave 1
CAP-LNX-01

Wave 2
CAP-GIT-01
+
CAP-GIT-05

Wave 3
none

Wave 4
CAP-BBG-01
+
CAP-BBG-02
```

If the group is struggling:

```text
skip all planned enrichment
except an ON_DEMAND capsule
that directly resolves the blocker
```

# Relationship with diagnostic results

Diagnostic results may guide capsule selection.

Examples:

```text
weak Git mental model
->
CAP-GIT-01 strongly useful

strong Git cohort
->
CAP-GIT-03 or CAP-GIT-04 may be appropriate

weak Linux autonomy
->
use CAP-LNX-01 only if it clarifies
do not add command volume

strong finance/data cohort
->
CAP-BBG-02 may be useful
```

Diagnostic results must not:

```text
increase checkpoint requirements
promote ADVANCED to CORE
force a capsule
```

# Capsule vs Advanced distinction

A capsule is:

```text
teacher explanation
5-10 min
no student artifact
```

An advanced lab is:

```text
student practice
20-90 min
separate support
observable DoD
```

Example:

```text
CAP-LNX-02
permissions troubleshooting explanation

!=

ADV-LNX-02
permissions and chmod practice
```

Another example:

```text
CAP-GIT-04
merge vs rebase explanation

!=

ADV-GIT-03
interactive rebase practice
```

Do not merge these layers.

# R7.5 acceptance audit

```text
[x] every capsule maps to one primary TD
[x] every capsule has a deep-dive source
[x] every capsule has a duration
[x] every capsule has a delivery trigger
[x] every capsule has a teaching objective
[x] every capsule has an understanding check
[x] every capsule has a stop point
[x] every capsule has an explicit non-impact statement
[x] TDs without useful capsules are explicitly marked
[x] no capsule changes a CORE DoD
[x] no capsule creates checkpoint evidence
[x] no capsule activates a PENDING_EXTERNAL advanced support
[x] no new dependency is introduced
```

Result:

```text
PASS

11 CAPSULES
MAPPED TO 6 PRIMARY TDs

TD01
TD03
TD04
TD05
TD09
TD10
```

The remaining TDs are intentionally protected from additional conceptual load.
