# Optional Advanced Content Backlog

## 1. Purpose

Ce document transforme les contenus historiques classés `OPTIONAL` en backlog exploitable pour le parcours avancé MarketPulse.

Il ne modifie pas le CORE des 18 heures.

Il complète :

```text
docs/legacy/01_PREVIOUS_COURSE_REPOSITORY_ANALYSIS.md
docs/legacy/02_LEGACY_TO_MARKETPULSE_CONTENT_MAPPING.md
```

Le principe est :

```text
CORE first
   |
   v
optional depth
   |
   v
advanced practice
```

Aucun item de ce backlog ne doit devenir un prérequis implicite pour :

```text
Checkpoint A
Checkpoint B
Checkpoint C
```

## 2. Backlog status model

Chaque item utilise un statut parmi :

```text
CANDIDATE
READY_TO_DESIGN
READY_TO_TEACH
DEFERRED
REJECTED
```

### CANDIDATE

Le sujet est pertinent mais n'a pas encore de support MarketPulse dédié.

### READY_TO_DESIGN

Le périmètre et les prérequis sont suffisamment clairs pour créer un support.

### READY_TO_TEACH

Le support a été écrit, relu et testé.

### DEFERRED

Le sujet reste pertinent mais n'est pas prioritaire.

### REJECTED

Le sujet a été étudié puis explicitement exclu du parcours avancé actuel.

## 3. Priority model

Les priorités sont :

```text
P1
forte valeur pédagogique
faible à moyen risque
bonne continuité avec MarketPulse

P2
valeur réelle
mais dépendances ou profondeur plus élevées

P3
sujet intéressant
mais faible priorité pour le module actuel
```

Aucune priorité de ce document ne remplace les priorités du CORE.

## 4. Delivery modes

Les contenus optionnels peuvent être proposés sous quatre formes.

### ADVANCED_LAB

Atelier structuré avec objectif, exercices et definition of done.

### MINI_LAB

Extension courte de 20 à 45 minutes.

### INSTRUCTOR_DEMO

Démonstration de 10 à 30 minutes sans exigence de reproduction par toute la classe.

### SELF_STUDY

Support autonome pour étudiants avancés.

## 5. Global guardrails

Tout item avancé doit respecter :

```text
[ ] CORE déjà terminé
[ ] pas de changement des checkpoints
[ ] pas de nouvelle exigence de notation
[ ] pas de donnée sensible
[ ] pas de carte bancaire obligatoire
[ ] pas de dépendance propriétaire non validée
[ ] pas de claim LIVE sans preuve LIVE
[ ] pas de modification du contrat runtime CORE
[ ] pas de dépassement imposé aux étudiants en difficulté
```

Les commandes CORE restent :

```bash
python src/main.py
python src/dashboard.py
```

## 6. Backlog overview

| ID | Domain | Topic | Priority | Mode | Suggested duration | Status |
|---|---|---|---|---|---:|---|
| ADV-LNX-01 | Linux | File operations | P1 | MINI_LAB | 30 min | READY_TO_DESIGN |
| ADV-LNX-02 | Linux | Permissions and chmod | P1 | MINI_LAB | 30-45 min | READY_TO_DESIGN |
| ADV-LNX-03 | Linux | Pipes and text processing | P1 | ADVANCED_LAB | 60-90 min | READY_TO_DESIGN |
| ADV-LNX-04 | Linux | Environment variables | P1 | MINI_LAB | 30 min | READY_TO_DESIGN |
| ADV-LNX-05 | Linux | Bash scripting | P2 | ADVANCED_LAB | 60-90 min | CANDIDATE |
| ADV-LNX-06 | Linux | Cron scheduling | P2 | MINI_LAB | 30-45 min | CANDIDATE |
| ADV-GIT-01 | Git | Conflict resolution | P1 | MINI_LAB | 30-45 min | READY_TO_DESIGN |
| ADV-GIT-02 | Git | Restore, revert and reset | P1 | ADVANCED_LAB | 60 min | READY_TO_DESIGN |
| ADV-GIT-03 | Git | Interactive rebase | P2 | ADVANCED_LAB | 60-90 min | CANDIDATE |
| ADV-GIT-04 | Git | Tags and releases | P1 | MINI_LAB | 30-45 min | READY_TO_DESIGN |
| ADV-GIT-05 | Git | Aliases and productivity | P3 | SELF_STUDY | 20-30 min | CANDIDATE |
| ADV-RMT-01 | Remote Linux | SSH fundamentals | P1 | ADVANCED_LAB | 60 min | READY_TO_DESIGN |
| ADV-RMT-02 | Remote Linux | SCP file transfer | P2 | MINI_LAB | 30 min | CANDIDATE |
| ADV-RMT-03 | Remote Linux | systemd service | P1 | ADVANCED_LAB | 60-90 min | READY_TO_DESIGN |
| ADV-RMT-04 | Remote Linux | VPS deployment | P2 | ADVANCED_LAB | 90 min | CANDIDATE |
| ADV-BBG-01 | Bloomberg | Reference data | P1 | MINI_LAB | 30-45 min | READY_TO_DESIGN |
| ADV-BBG-02 | Bloomberg | xbbg exploration | P2 | INSTRUCTOR_DEMO | 30 min | CANDIDATE |
| ADV-BBG-03 | Bloomberg | blpapi low-level request | P2 | ADVANCED_LAB | 60-90 min | CANDIDATE |
| ADV-BBG-04 | Bloomberg | Intraday bars | P2 | ADVANCED_LAB | 60 min | CANDIDATE |
| ADV-DASH-01 | Dash | Callback | P1 | MINI_LAB | 30-45 min | READY_TO_DESIGN |
| ADV-DASH-02 | Dash | Instrument selector | P1 | MINI_LAB | 30-45 min | READY_TO_DESIGN |
| ADV-DEP-01 | Deployment | Docker | P2 | ADVANCED_LAB | 90 min | CANDIDATE |
| ADV-DEP-02 | Deployment | GitHub Actions | P2 | ADVANCED_LAB | 60-90 min | CANDIDATE |
| ADV-DEP-03 | Deployment | Service + reverse proxy | P3 | SELF_STUDY | 90+ min | DEFERRED |

## 7. Recommended sequencing

The advanced track should not be a second mandatory curriculum.

A sensible order is:

```text
MarketPulse CORE
      |
      v
Linux Advanced
      |
      v
Git Advanced
      |
      v
Dash Interaction
      |
      v
Remote Linux
      |
      v
Bloomberg Advanced
      |
      v
Deployment
```

Not every student needs to follow every branch.

A better model is:

```text
student interest
+
diagnostic level
+
available time
+
environment access
=
selected advanced items
```

# Linux Advanced

## 8. ADV-LNX-01 - File operations

### Goal

Strengthen basic Linux autonomy with:

```text
mkdir
touch
cp
mv
rm
```

### Priority

```text
P1
```

### Suggested mode

```text
MINI_LAB
30 minutes
```

### Prerequisites

```text
TD01 complete
comfortable with pwd / ls / cd
```

### Suggested MarketPulse context

Create a disposable sandbox:

```text
sandbox/
├── raw/
├── archive/
└── notes/
```

Students practice file operations without touching production project files.

### Definition of done

```text
[ ] create a directory
[ ] create a file
[ ] copy a file
[ ] move or rename a file
[ ] remove a disposable file
[ ] explain the difference between copy and move
```

### Guardrail

Never ask students to delete real project directories.

### Legacy source

```text
TD1_1_linux_fundamentals
```

## 9. ADV-LNX-02 - Permissions and chmod

### Goal

Understand:

```text
read
write
execute
owner
group
others
```

and use:

```text
chmod
```

### Priority

```text
P1
```

### Suggested mode

```text
MINI_LAB
30-45 minutes
```

### Prerequisites

```text
TD01 complete
basic file operations
```

### Suggested exercise

Create a harmless script:

```text
scripts/hello.sh
```

Then compare:

```text
readable file
vs
executable file
```

Use:

```bash
ls -l
chmod u+x scripts/hello.sh
```

### Definition of done

```text
[ ] read ls -l permission notation
[ ] add execute permission to owner
[ ] explain u / g / o
[ ] explain why permissions matter for scripts
```

### Explicit exclusions

Do not require:

```text
chmod 777
root modification
system files
production secrets
```

### Diagnostic connection

Related to:

```text
L10
```

### Legacy source

```text
TD1_1_linux_fundamentals
```

## 10. ADV-LNX-03 - Pipes and text processing

### Goal

Introduce Unix composition with:

```text
|
grep
wc
awk
sed
```

### Priority

```text
P1
```

### Suggested mode

```text
ADVANCED_LAB
60-90 minutes
```

### Prerequisites

```text
TD01 complete
local MarketPulse files available
```

### MarketPulse adaptation

Avoid the historical Wikipedia HTML scraping exercise.

Use project-controlled files such as:

```text
data/sample/prices.csv
repository text files
application logs if available
```

### Example questions

```text
How many AAPL rows exist?
How many SP500 rows exist?
Which lines contain a selected ticker?
How can the first field be extracted?
```

### Definition of done

```text
[ ] use one pipe
[ ] combine grep and wc
[ ] use awk on delimited text
[ ] explain why each command performs one step
```

### Optional extension

```text
sed
regex
```

### Diagnostic connection

Related to:

```text
L08
L09
```

### Legacy source

```text
TD1_3_linux_Grep
```

## 11. ADV-LNX-04 - Environment variables

### Goal

Understand how the shell passes configuration to Python.

### Priority

```text
P1
```

### Suggested mode

```text
MINI_LAB
30 minutes
```

### Prerequisites

```text
TD02 complete
basic Python imports
```

### Exercise

Shell:

```bash
export MARKETPULSE_MODE=demo
python src/main.py
```

Python concept:

```python
import os

mode = os.environ.get("MARKETPULSE_MODE")
```

### Learning objective

Understand:

```text
shell variable
vs
environment variable
vs
Python variable
```

### Security connection

Explain that environment variables may carry configuration, but must not be printed or committed when they contain secrets.

### Diagnostic connection

Related to:

```text
L12
```

## 12. ADV-LNX-05 - Bash scripting

### Goal

Turn repeated terminal commands into a small Bash script.

### Priority

```text
P2
```

### Suggested mode

```text
ADVANCED_LAB
60-90 minutes
```

### Candidate script

```text
scripts/run_marketpulse.sh
```

Possible sequence:

```bash
python src/main.py
python src/dashboard.py
```

Do not run the dashboard in a way that blocks an automated script unless the exercise explicitly handles process lifecycle.

### Concepts

```text
shebang
exit code
arguments
quoted variables
&&
```

### Diagnostic connection

Related to:

```text
L13
```

### Guardrail

Do not replace the canonical CORE commands with shell wrappers.

The canonical commands remain documented directly.

## 13. ADV-LNX-06 - Cron scheduling

### Goal

Understand scheduled execution.

### Priority

```text
P2
```

### Suggested mode

```text
MINI_LAB
30-45 minutes
```

### Suggested context

Schedule a harmless report or terminal snapshot in a controlled Linux environment.

### Prerequisites

```text
Linux environment with cron available
MarketPulse terminal command already working
```

### Definition of done

```text
[ ] explain a cron expression
[ ] create a non-sensitive scheduled command
[ ] know where output goes
[ ] remove the scheduled job afterward
```

### Not CORE

Cron must never become a TD12 release requirement.

# Git Advanced

## 14. ADV-GIT-01 - Conflict resolution

### Goal

Go beyond conflict recognition and resolve one real, controlled conflict.

### Priority

```text
P1
```

### Suggested mode

```text
MINI_LAB
30-45 minutes
```

### Prerequisites

```text
TD04 complete
branch and merge understood
```

### Suggested exercise

Create two branches modifying the same small disposable text block.

Then:

```text
merge
inspect conflict markers
choose final content
stage
complete merge
```

### Definition of done

```text
[ ] identify conflict markers
[ ] explain ours / theirs conceptually
[ ] reconcile content intentionally
[ ] stage resolved file
[ ] complete merge
```

### Guardrail

Do not generate conflicts inside a critical MarketPulse file during the first attempt.

### Diagnostic connection

Related to:

```text
G12
```

## 15. ADV-GIT-02 - Restore, revert and reset

### Goal

Understand three distinct undo mechanisms.

### Priority

```text
P1
```

### Suggested mode

```text
ADVANCED_LAB
60 minutes
```

### Core comparison

```text
restore
=
working tree / staging correction

revert
=
new commit that reverses an earlier commit

reset
=
move branch history reference
```

### Safety-first rule

Use a disposable training repository.

Never demonstrate destructive reset first on the team repository.

### Definition of done

```text
[ ] restore an unstaged change
[ ] unstage a file safely
[ ] revert a commit
[ ] explain why reset --hard is dangerous
```

### Legacy source

```text
TD2_Git_local
```

## 16. ADV-GIT-03 - Interactive rebase

### Goal

Understand local history cleanup before publication.

### Priority

```text
P2
```

### Suggested mode

```text
ADVANCED_LAB
60-90 minutes
```

### Prerequisites

```text
TD03-TD06 complete
comfortable with branches and commits
```

### Exercise

Create several disposable commits, then practice:

```text
reword
squash
reorder
```

### Definition of done

```text
[ ] explain what history rewriting means
[ ] squash local commits
[ ] inspect resulting graph
[ ] explain why rewriting shared history is dangerous
```

### Guardrail

Do not require force-pushing shared team history.

## 17. ADV-GIT-04 - Tags and releases

### Goal

Connect Git history to release identity.

### Priority

```text
P1
```

### Suggested mode

```text
MINI_LAB
30-45 minutes
```

### Best placement

After:

```text
TD12
```

### Exercise

On a clean completed repository:

```bash
git tag
git tag -a ...
git show ...
```

### Learning outcome

Understand:

```text
commit
vs
branch
vs
tag
vs
release
```

### Optional extension

Create a GitHub release only if repository permissions and teaching context allow it.

## 18. ADV-GIT-05 - Git aliases and productivity

### Goal

Discover local Git ergonomics without changing project contracts.

### Priority

```text
P3
```

### Suggested mode

```text
SELF_STUDY
20-30 minutes
```

### Examples

```text
status alias
graph alias
last commit alias
```

### Guardrail

Documentation and teaching commands should continue to use full Git commands.

# Remote Linux

## 19. ADV-RMT-01 - SSH fundamentals

### Goal

Connect to a pre-provisioned remote Linux host.

### Priority

```text
P1
```

### Suggested mode

```text
ADVANCED_LAB
60 minutes
```

### Strong recommendation

Use:

```text
instructor-provisioned VM
or
school-provided host
```

Do not require:

```text
personal cloud account
personal credit card
```

### Concepts

```text
host
user
port
private key
known_hosts
remote shell
```

### Definition of done

```text
[ ] connect to remote host
[ ] identify remote working directory
[ ] run Python remotely
[ ] disconnect cleanly
[ ] keep private key secret
```

## 20. ADV-RMT-02 - SCP transfer

### Goal

Transfer a non-sensitive file between local and remote environments.

### Priority

```text
P2
```

### Suggested mode

```text
MINI_LAB
30 minutes
```

### Prerequisites

```text
ADV-RMT-01
```

### Definition of done

```text
[ ] send a file
[ ] retrieve a file
[ ] verify content
[ ] explain source vs destination syntax
```

### Guardrail

Never transfer secrets for demonstration.

## 21. ADV-RMT-03 - systemd service

### Goal

Run the MarketPulse dashboard as a managed Linux service.

### Priority

```text
P1
```

### Suggested mode

```text
ADVANCED_LAB
60-90 minutes
```

### Prerequisites

```text
TD11 complete
remote Linux available
dashboard command works
```

### Concepts

```text
unit file
ExecStart
working directory
restart policy
journalctl
start
stop
status
```

### Definition of done

```text
[ ] service starts
[ ] service status is visible
[ ] logs can be inspected
[ ] service stops cleanly
```

### Security

Do not place secrets directly in a committed service file.

## 22. ADV-RMT-04 - VPS deployment

### Goal

Deploy MarketPulse on a remote Linux host.

### Priority

```text
P2
```

### Suggested mode

```text
ADVANCED_LAB
90 minutes
```

### Prerequisites

```text
ADV-RMT-01
TD12 complete
remote host already provisioned
```

### Important design decision

Provisioning the server itself is outside the exercise unless the school supplies the environment.

The exercise begins with:

```text
reachable Linux host
```

not:

```text
create cloud account
enter payment card
choose billing plan
```

# Bloomberg Advanced

## 23. ADV-BBG-01 - Reference data

### Goal

Explore non-historical Bloomberg reference data when LIVE access is available.

### Priority

```text
P1
```

### Suggested mode

```text
MINI_LAB
30-45 minutes
```

### Prerequisites

```text
TD09-TD10 complete
LIVE Bloomberg environment validated
```

### Candidate concepts

```text
security name
security type
currency
exchange code
```

### Fallback rule

If LIVE access is unavailable:

```text
do not fabricate provider evidence
```

This lab may simply be skipped.

## 24. ADV-BBG-02 - xbbg exploration

### Goal

Show a higher-level Bloomberg Python interface.

### Priority

```text
P2
```

### Suggested mode

```text
INSTRUCTOR_DEMO
30 minutes
```

### Prerequisite

The package and environment must be validated in the actual ESILV setup.

### Comparison objective

```text
xbbg
=
high-level convenience

blpapi
=
lower-level control
```

### Guardrail

Do not add `xbbg` to the common `requirements.txt` unless the course deliberately adopts it.

## 25. ADV-BBG-03 - blpapi low-level request

### Goal

Understand the request / response lifecycle more deeply.

### Priority

```text
P2
```

### Suggested mode

```text
ADVANCED_LAB
60-90 minutes
```

### Concepts

```text
session
service
request
send
event
message
response
error
```

### Prerequisites

```text
validated Bloomberg LIVE environment
TD10 complete
```

### Definition of done

```text
[ ] identify request lifecycle
[ ] obtain authorized data
[ ] inspect response structure
[ ] map result to canonical concepts
```

## 26. ADV-BBG-04 - Intraday bars

### Goal

Explore intraday market data without modifying the CORE contract.

### Priority

```text
P2
```

### Suggested mode

```text
ADVANCED_LAB
60 minutes
```

### Prerequisites

```text
LIVE Bloomberg access
TD10 complete
```

### Important rule

The MarketPulse CORE remains:

```text
1 month
Daily
```

Intraday introduces extra concerns:

```text
timestamps
time zones
market hours
holidays
missing intervals
cross-market alignment
```

The advanced lab should explicitly teach why this is a separate complexity class.

# Dash Advanced

## 27. ADV-DASH-01 - Callback

### Goal

Extend the static CORE dashboard with one meaningful interaction.

### Priority

```text
P1
```

### Suggested mode

```text
MINI_LAB
30-45 minutes
```

### Prerequisites

```text
TD11 complete
static dashboard works
```

### Candidate interaction

```text
dropdown
        |
        v
callback
        |
        v
updated figure
```

### Architectural guardrail

The callback must still use the application boundary.

Avoid:

```text
callback
-> direct provider-specific logic
-> duplicate analytics
```

Prefer:

```text
callback
-> application function
-> snapshot
-> figure
```

### Diagnostic connection

Related to:

```text
P13
```

## 28. ADV-DASH-02 - Instrument selector

### Goal

Allow a user to select another supported instrument without duplicating business logic.

### Priority

```text
P1
```

### Suggested mode

```text
MINI_LAB
30-45 minutes
```

### Prerequisites

```text
ADV-DASH-01
application layer supports parameterized instrument selection
```

### Guardrail

Do not implement the selector by hard-coding multiple unrelated code paths in `dashboard.py`.

# Deployment Advanced

## 29. ADV-DEP-01 - Docker

### Goal

Package the completed MarketPulse application in a reproducible container.

### Priority

```text
P2
```

### Suggested mode

```text
ADVANCED_LAB
90 minutes
```

### Prerequisites

```text
TD12 complete
Docker available
```

### Candidate deliverables

```text
Dockerfile
.dockerignore
documented build command
documented run command
```

### Definition of done

```text
[ ] image builds
[ ] terminal path can execute in container
[ ] dashboard can be started
[ ] no secret is baked into image
```

### Guardrail

Docker remains a stretch objective.

It must not become required evidence for Checkpoint C.

## 30. ADV-DEP-02 - GitHub Actions

### Goal

Introduce simple CI after the Git workflow is already mastered.

### Priority

```text
P2
```

### Suggested mode

```text
ADVANCED_LAB
60-90 minutes
```

### Prerequisites

```text
TD12 complete
repository workflow stable
```

### Candidate workflow

A minimal workflow may verify:

```text
Python environment setup
dependency installation
basic import / smoke execution
```

Do not invent a full CI architecture.

### README badge rule

Only add a CI badge when:

```text
workflow exists
+
workflow path is correct
+
workflow actually runs
```

## 31. ADV-DEP-03 - Service + reverse proxy

### Goal

Explore a more realistic web deployment.

### Priority

```text
P3
```

### Status

```text
DEFERRED
```

### Possible stack

```text
Dash
+
systemd
+
reverse proxy
```

### Reason for deferral

This introduces:

```text
networking
ports
process management
web proxy configuration
TLS considerations
host security
```

which are beyond the current educational objective.

# Backlog by learning objective

## 32. If the goal is stronger Linux autonomy

Recommended sequence:

```text
ADV-LNX-01
      |
      v
ADV-LNX-02
      |
      v
ADV-LNX-03
      |
      v
ADV-LNX-04
      |
      v
ADV-LNX-05
```

## 33. If the goal is stronger Git engineering

Recommended sequence:

```text
ADV-GIT-01
      |
      v
ADV-GIT-02
      |
      v
ADV-GIT-03
      |
      v
ADV-GIT-04
```

## 34. If the goal is remote Linux delivery

Recommended sequence:

```text
ADV-RMT-01
      |
      v
ADV-RMT-02
      |
      v
ADV-RMT-03
      |
      v
ADV-RMT-04
```

## 35. If the goal is deeper Bloomberg knowledge

Recommended sequence:

```text
ADV-BBG-01
      |
      +-> ADV-BBG-02
      |
      +-> ADV-BBG-03
      |
      v
ADV-BBG-04
```

Only when LIVE access is validated.

## 36. If the goal is a more interactive application

Recommended sequence:

```text
TD11
  |
  v
ADV-DASH-01
  |
  v
ADV-DASH-02
```

## 37. If the goal is deployment

Recommended sequence:

```text
TD12
  |
  v
ADV-RMT-01
  |
  v
ADV-RMT-03
  |
  +-> ADV-DEP-01
  |
  +-> ADV-DEP-02
```

Do not require all deployment technologies simultaneously.

# Diagnostic-driven use

## 38. Using the pre-lab diagnostic

The diagnostic can help select optional content.

Examples:

### Strong Linux ceiling

If a substantial part of the cohort already understands:

```text
pipes
chmod
environment variables
&&
```

then:

```text
TD01 CORE stays unchanged
+
ADV-LNX items become realistic extensions
```

### Strong Git ceiling

If students already understand:

```text
fetch
conflicts
.gitignore
```

then:

```text
ADV-GIT-01
ADV-GIT-02
```

may be appropriate after the common Git sequence.

### Strong Dash knowledge

If P13 success is high:

```text
ADV-DASH-01
```

can become a natural extension.

### Important rule

Do not use strong diagnostic results to silently increase mandatory workload for the whole cohort.

# Selection criteria

## 39. When to promote an item to READY_TO_TEACH

An item should move to `READY_TO_TEACH` only when:

```text
[ ] objective is precise
[ ] prerequisites are explicit
[ ] duration was piloted
[ ] commands were tested
[ ] cleanup procedure exists
[ ] security risks were reviewed
[ ] no personal payment is required
[ ] expected result is observable
[ ] relation with MarketPulse is explicit
[ ] CORE remains unaffected
```

## 40. When to reject an optional item

Reject or defer if:

```text
environment setup > learning value
dependency is unstable
requires personal billing
requires secrets students cannot manage safely
duplicates existing CORE
cannot fit its own optional timebox
depends on unverified proprietary access
creates misleading evidence
```

# Suggested future artifacts

## 41. Advanced lab directory

If several items are implemented, create:

```text
docs/advanced/
├── README.md
├── ADV_LINUX_01_...
├── ADV_GIT_01_...
├── ADV_REMOTE_01_...
├── ADV_BLOOMBERG_01_...
├── ADV_DASH_01_...
└── ADV_DEPLOYMENT_01_...
```

Do not place advanced labs in:

```text
docs/labs/
```

unless they become part of the official 12-TD sequence.

## 42. Instructor deep-dive separation

Items classified `TEACHER_REFERENCE` should not be mixed into this backlog.

Recommended future file:

```text
docs/instructor/LEGACY_DEEP_DIVE_REFERENCE.md
```

Examples:

```text
Git object model
plumbing vs porcelain
Gitflow
Unix history
BDP / BDS / BDH
B-PIPE
xbbg vs blpapi comparison
```

# Final backlog principles

## 43. Preserve depth without recreating overload

The advanced backlog exists because the historical course contains valuable material.

The goal is not:

```text
bring everything back
```

The goal is:

```text
make depth available
without making depth mandatory
```

## 44. Preserve MarketPulse architecture

Every advanced item should respect the current architecture:

```text
providers
   |
   v
canonical rows
   |
   v
analytics
   |
   v
snapshot
   |
   +----------+
   |          |
   v          v
terminal     Dash
```

Advanced work may extend this architecture.

It should not bypass it.

## 45. Preserve evaluation boundaries

Optional advanced work can demonstrate initiative.

It must not become necessary to achieve the common checkpoint definition of done.

The rule remains:

```text
CORE competence
before
advanced extension
```

## 46. Final recommended priority order

If only a few advanced items are developed, prioritize:

```text
1. ADV-GIT-01  Conflict resolution
2. ADV-LNX-03  Pipes and text processing
3. ADV-LNX-04  Environment variables
4. ADV-DASH-01 Callback
5. ADV-GIT-04  Tags and releases
6. ADV-RMT-01  SSH fundamentals
7. ADV-RMT-03  systemd service
8. ADV-BBG-01  Bloomberg reference data
```

These items provide the best balance between:

```text
professional value
+
continuity with MarketPulse
+
manageable complexity
```

The remaining items can stay in the backlog until teaching evidence justifies their implementation.
