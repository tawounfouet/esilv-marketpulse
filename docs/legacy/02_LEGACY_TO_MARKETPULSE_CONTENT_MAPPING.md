# Legacy to MarketPulse Content Mapping

## 1. Purpose

Ce document transforme l'analyse du repository historique :

```text
tawounfouet/intro_git_linux_bloomberg
```

en décisions concrètes pour le repository actuel :

```text
tawounfouet/esilv-marketpulse
```

L'objectif est de répondre, pour chaque famille de contenus historiques, à quatre questions :

```text
1. Est-ce déjà couvert par MarketPulse ?
2. Si oui, où ?
3. Si non, faut-il le conserver ailleurs ?
4. Faut-il l'abandonner du parcours commun ?
```

La logique de migration retenue est :

```text
Legacy content
      |
      +-> CORE
      |
      +-> OPTIONAL
      |
      +-> TEACHER_REFERENCE
      |
      +-> DROP
```

Ce document complète :

```text
docs/legacy/01_PREVIOUS_COURSE_REPOSITORY_ANALYSIS.md
```

## 2. Decision taxonomy

### CORE

Le contenu est pertinent pour le parcours obligatoire des 18 heures.

Il est soit :

- déjà présent dans un TD MarketPulse ;
- soit suffisamment important pour être intégré au CORE sans élargir le périmètre.

Règle :

```text
CORE
=
must learn
+
must be observable
+
must fit in the current timebox
```

### OPTIONAL

Le contenu est techniquement utile, mais il ne doit pas être exigé de toute la promotion.

Il peut être proposé :

- aux étudiants avancés ;
- aux groupes en avance ;
- dans un atelier bonus ;
- dans un parcours avancé Linux / Git / Bloomberg.

Règle :

```text
OPTIONAL
=
valuable
but
not required for common completion
```

### TEACHER_REFERENCE

Le contenu doit rester disponible pour l'enseignant afin de :

- contextualiser ;
- expliquer plus profondément ;
- répondre aux questions ;
- préparer une démonstration ;
- enrichir les CM ;
- construire un support avancé.

Il n'a pas besoin d'être transformé en activité étudiant.

Règle :

```text
TEACHER_REFERENCE
=
know it
without requiring students to perform it
```

### DROP

Le contenu ne doit pas être migré dans le parcours commun actuel.

Les principales raisons possibles sont :

- surcharge ;
- dépendance environnementale excessive ;
- faible valeur par rapport au temps consommé ;
- incompatibilité avec le syllabus actuel ;
- dette historique ;
- ancien dispositif d'évaluation ;
- dépendance à des assets ou workflows que le nouveau cursus ne veut pas reproduire.

Règle :

```text
DROP
=
do not migrate into the current common teaching path
```

DROP ne veut pas dire :

```text
technically useless
```

mais :

```text
not appropriate for the current common path
```

## 3. Executive mapping

| Legacy domain | Main decision | MarketPulse destination |
|---|---|---|
| Linux navigation | CORE | TD01 |
| Linux file inspection | CORE | TD01 |
| Linux file creation / copy / move | OPTIONAL | Advanced Linux |
| Linux permissions | OPTIONAL | Advanced Linux |
| sudo / root / package management | TEACHER_REFERENCE | Instructor Linux reference |
| shell variables | OPTIONAL | Advanced Linux |
| shell scripts | OPTIONAL | Advanced Linux |
| cron / daemon | OPTIONAL | Advanced deployment |
| hashing / compression | TEACHER_REFERENCE | Git internals deep dive |
| ACL | DROP | Legacy only |
| grep | CORE | TD01 |
| awk / sed / regex | OPTIONAL | Advanced Linux |
| SSH / SCP | OPTIONAL | Advanced remote track |
| mandatory cloud VM | DROP | Replaced by optional remote track |
| Git status / diff / add / commit / log | CORE | TD03 |
| Git branches / merge | CORE | TD04 |
| Git conflict concept | CORE | TD04 |
| full conflict exercise | OPTIONAL | TD04 extension |
| remote branch / push | CORE | TD05 |
| Pull Request | CORE | TD05 |
| code review | CORE | TD06 |
| git fetch / synchronization | CORE support | TD05 / TD06 baseline workflow |
| reset / revert / restore advanced use | OPTIONAL | Advanced Git |
| interactive rebase | OPTIONAL | Advanced Git |
| Git aliases | OPTIONAL | Advanced Git |
| Git object internals | TEACHER_REFERENCE | Git deep dive |
| manual zlib object construction | DROP | Legacy only |
| Gitflow | TEACHER_REFERENCE | Instructor reference |
| Bloomberg Terminal context | TEACHER_REFERENCE | TD09 intro / CM |
| Bloomberg identifiers | CORE | TD09 |
| LIVE vs sample distinction | CORE | TD09 / TD10 |
| historical Bloomberg retrieval | CONDITIONAL CORE path | TD10 LIVE only |
| Bloomberg normalization | CORE | TD10 |
| xbbg vs blpapi | TEACHER_REFERENCE | Bloomberg instructor reference |
| BDP / BDS / BDH | TEACHER_REFERENCE | Bloomberg instructor reference |
| intraday 5-minute bars | OPTIONAL | Advanced Bloomberg |
| multi-asset quant project | TEACHER_REFERENCE | Final-project inspiration |
| Sharpe / max drawdown | DROP from guided CORE | Final-project option only |
| 24/7 hosting | DROP from guided CORE | Advanced deployment only |
| mandatory credit-card cloud setup | DROP | Not permitted as common requirement |
| ML bonus | DROP from guided CORE | Separate optional project |
| LaTeX build system | DROP | Markdown-first repository |
| historical exam artifacts | TEACHER_REFERENCE | Do not reuse as current contract |

## 4. CM0 Context mapping

The historical context course contains material on:

```text
digital infrastructure
open source
Linux ecosystem
data centers
energy
PUE
network traffic
carbon impact
CodeCarbon
cloud regions
Git binary-file impact
```

### Mapping decisions

| Legacy topic | Decision | Current destination | Notes |
|---|---|---|---|
| Why Linux matters | TEACHER_REFERENCE | CM / instructor opening | Strong contextual value |
| Open source ecosystem | TEACHER_REFERENCE | CM | Useful culture |
| Data-center infrastructure | TEACHER_REFERENCE | CM | Not needed in TD CORE |
| Energy and PUE | TEACHER_REFERENCE | CM | Good contextual material |
| Carbon-aware computing | TEACHER_REFERENCE | CM / optional reading | Keep separate from TD objectives |
| CodeCarbon | OPTIONAL | Optional sustainability extension | Not required by syllabus |
| Git and binary-file cost | TEACHER_REFERENCE | Git conceptual support | Useful when explaining repository hygiene |
| Cloud-region sustainability | TEACHER_REFERENCE | Advanced infrastructure track | Not a common TD requirement |

### Recommended action

Do not migrate this CM into the 18-hour TD path.

Instead:

```text
retain concepts
+
rewrite selected ideas
+
use in CM or instructor notes
```

## 5. CM1 Linux mapping

### 5.1 History and ecosystem

Legacy topics:

```text
Unix history
GNU
Linux history
POSIX
open source
operating systems
```

Decision:

```text
TEACHER_REFERENCE
```

Destination:

```text
CM
instructor notes
optional reading
```

Reason:

These concepts improve technical culture but do not need to consume TD time.

### 5.2 Virtualization and containers

Legacy topics:

```text
virtual machines
containers
Docker
Kubernetes
```

Decision:

```text
TEACHER_REFERENCE
+
OPTIONAL for Docker
```

Destination:

```text
advanced track
```

Current MarketPulse rule:

```text
Docker = optional
Kubernetes = outside common path
```

### 5.3 Shell ecosystem

Legacy topics:

```text
Bash
zsh
fish
shell history
```

Decision:

```text
Bash = CORE environment
other shells = TEACHER_REFERENCE
```

Current destination:

```text
TD01
```

### 5.4 Navigation and inspection

Legacy commands:

```text
pwd
ls
cd
cat
head
grep
```

Decision:

```text
CORE
```

Current destination:

```text
TD01_BOOTSTRAP_LINUX.md
```

This is one of the clearest direct migrations.

## 6. TD1.1 Linux fundamentals mapping

The historical TD1.1 includes several categories.

### 6.1 Navigation

Legacy:

```text
cd /
ls
pwd
cd home
cd ..
```

Decision:

```text
CORE
```

MarketPulse destination:

```text
TD01
```

### 6.2 File and directory creation

Legacy:

```text
mkdir
mv
cp
rm
```

Decision:

```text
OPTIONAL
```

Reason:

Useful shell literacy, but MarketPulse does not require students to manufacture arbitrary directory trees during the common path.

Possible destination:

```text
Advanced Linux extension
```

### 6.3 Shell script creation

Legacy:

```text
#!/bin/bash
echo
source script.sh
```

Decision:

```text
OPTIONAL
```

Possible destination:

```text
Advanced Linux
or
optional automation extension
```

### 6.4 Permissions

Legacy:

```text
chmod
read / write / execute
symbolic permissions
numeric permissions
```

Decision:

```text
OPTIONAL
```

Reason:

Important Linux knowledge but not required for the current MarketPulse runtime.

### 6.5 Root and ownership

Legacy:

```text
sudo
root
chown
```

Decision:

```text
TEACHER_REFERENCE
```

Reason:

Potentially useful during troubleshooting, but not a learning objective for the common sequence.

### 6.6 Package management

Legacy:

```text
apt
system package installation
```

Decision:

```text
TEACHER_REFERENCE
```

Reason:

The common path relies primarily on an already-provisioned environment and Python package installation when required.

## 7. TD1.2 Linux tools mapping

### 7.1 System information

Decision:

```text
OPTIONAL
```

Useful for advanced Linux familiarity.

### 7.2 Variables and script scope

Decision:

```text
OPTIONAL
```

Connection with diagnostic:

```text
L12
environment variable + os.environ
```

This remains a diagnostic ceiling topic.

### 7.3 Scheduling and daemon

Legacy:

```text
cron
daemon
scheduled jobs
```

Decision:

```text
OPTIONAL
```

Potential destination:

```text
advanced deployment track
```

Not needed for TD12 reproducibility.

### 7.4 Hashing

Decision:

```text
TEACHER_REFERENCE
```

Possible use:

Explain content addressing and Git object identity.

### 7.5 Compression

Decision:

```text
TEACHER_REFERENCE
```

Possible use:

Support Git internals explanation.

### 7.6 ACL

Decision:

```text
DROP
```

Reason:

Low priority relative to syllabus and time available.

## 8. TD1.3 grep / awk / sed mapping

### grep

Decision:

```text
CORE
```

Destination:

```text
TD01
```

### pipes

Decision:

```text
OPTIONAL
```

### wc

Decision:

```text
OPTIONAL
```

### awk

Decision:

```text
OPTIONAL
```

### sed

Decision:

```text
OPTIONAL
```

### regex

Decision:

```text
OPTIONAL
```

### curl-based HTML extraction

Decision:

```text
DROP from common path
```

Reason:

The objective is no longer to teach ad hoc shell scraping.

If a separate shell-processing workshop exists, the exercise can be reused conceptually.

## 9. TD1.4 SSH / SCP mapping

### SSH concept

Decision:

```text
OPTIONAL
```

Destination:

```text
Advanced remote Linux track
```

### SSH key permissions

Legacy:

```text
chmod 400
private key
```

Decision:

```text
OPTIONAL
```

### SCP

Decision:

```text
OPTIONAL
```

### Mandatory public cloud account

Decision:

```text
DROP
```

### Mandatory credit card

Decision:

```text
DROP
```

### Mandatory VM creation

Decision:

```text
DROP from common path
OPTIONAL in advanced track
```

### Current replacement

```text
common development environment
+
Codespaces or equivalent
+
no billing requirement
```

This is a deliberate migration decision.

## 10. CM2 Git local mapping

### 10.1 Version-control purpose

Decision:

```text
CORE
```

Destination:

```text
TD03
```

### 10.2 status / add / commit / log

Decision:

```text
CORE
```

Destination:

```text
TD03
```

### 10.3 diff

Decision:

```text
CORE
```

Destination:

```text
TD03
```

### 10.4 staging-area mental model

Decision:

```text
CORE
```

Destination:

```text
TD03
```

This is one of the strongest conceptual elements to preserve.

### 10.5 HEAD

Decision:

```text
TEACHER_REFERENCE
```

It may be explained when useful, but it does not need to become a separate student objective.

### 10.6 Git object model

Legacy:

```text
blob
tree
commit
hash
object database
```

Decision:

```text
TEACHER_REFERENCE
```

Potential destination:

```text
Git deep dive
```

### 10.7 Plumbing vs porcelain

Decision:

```text
TEACHER_REFERENCE
```

High conceptual value, low CORE priority.

## 11. TD2 Git local mapping

### Basic workflow

Legacy:

```text
git init
git status
git add
git commit
git log
```

Decision:

```text
CORE
```

Destination:

```text
TD03
```

The main adaptation is that students now perform these operations on real MarketPulse changes rather than on an isolated artificial repository.

### .gitignore

Decision:

```text
TEACHER_REFERENCE
+
OPTIONAL
```

Current repository already contains:

```text
.gitignore
```

Students do not need a dedicated CORE exercise to understand every ignore nuance.

### diff

Decision:

```text
CORE
```

Destination:

```text
TD03
```

### restore / revert / reset

Decision:

```text
OPTIONAL
```

Reason:

Useful professional knowledge, but potentially destructive and unnecessary for the current common path.

### aliases

Decision:

```text
OPTIONAL
```

### hash-object

Decision:

```text
TEACHER_REFERENCE
```

### manual Git object construction

Decision:

```text
DROP
```

Reason:

Excellent specialized Git exercise but disproportionate for this module.

### zlib object construction

Decision:

```text
DROP
```

Same reasoning.

## 12. CM3 Git remote mapping

### clone

Decision:

```text
CORE concept
```

Current usage:

```text
TD01 onboarding
TD12 reproducibility
```

### remote origin

Decision:

```text
CORE
```

Destination:

```text
TD05
```

### push

Decision:

```text
CORE
```

Destination:

```text
TD05
```

### pull

Decision:

```text
CORE support
```

Destination:

```text
TD05 / TD06 synchronization
```

### fetch

Decision:

```text
CORE support
```

Destination:

```text
team baseline synchronization
```

### branches

Decision:

```text
CORE
```

Destination:

```text
TD04
```

### merge

Decision:

```text
CORE
```

Destination:

```text
TD04
TD06
```

### Pull Request

Decision:

```text
CORE
```

Destination:

```text
TD05
```

### Review

Decision:

```text
CORE
```

Destination:

```text
TD06
```

### Rebase

Decision:

```text
OPTIONAL
```

### Interactive rebase

Decision:

```text
OPTIONAL
```

### Gitflow

Decision:

```text
TEACHER_REFERENCE
```

Reason:

Useful workflow culture, but the course already uses a simpler branch / PR model.

### Tags

Decision:

```text
OPTIONAL
```

Potential use in an advanced release extension after TD12.

## 13. TD3 branches and collaboration mapping

### Team of 3-4

Decision:

```text
CORE principle
```

Current destination:

```text
TEAM_TEMPLATE.md
student onboarding
team repository workflow
```

### Shared repository

Decision:

```text
CORE
```

Current implementation:

```text
one team
=
one shared fork
```

### Branch per student

Legacy approach:

```text
branch named after the student
```

Decision:

```text
DROP as naming convention
```

Current rule:

```text
feature/
fix/
docs/
```

Reason:

Branch names describe work rather than people.

Individual attribution is preserved through Git identity and evidence.

### Simple merge

Decision:

```text
CORE
```

Destination:

```text
TD04
```

### Manufactured conflict

Decision:

```text
OPTIONAL
```

Destination:

```text
TD04 optional or instructor demo
```

### Sync main into local work

Decision:

```text
CORE support
```

Destination:

```text
TD04 -> TD05 Team Baseline Gate
TD06 synchronization
```

### Delete branches

Decision:

```text
OPTIONAL
```

### Interactive rebase

Decision:

```text
OPTIONAL
```

### Pull Request creation

Decision:

```text
CORE
```

Destination:

```text
TD05
```

### Approval / review

Decision:

```text
CORE
```

Destination:

```text
TD06
```

## 14. CM4 Bloomberg mapping

### Bloomberg business context

Decision:

```text
TEACHER_REFERENCE
```

Destination:

```text
TD09 introduction
CM
```

### Bloomberg Terminal navigation

Decision:

```text
TEACHER_REFERENCE
```

Reason:

Useful if actual terminals are available.

### Excel Add-In

Decision:

```text
TEACHER_REFERENCE
```

Not part of MarketPulse Python path.

### API request / response

Decision:

```text
TEACHER_REFERENCE
+
CORE conceptual support
```

Destination:

```text
TD09 / TD10
```

### Subscription

Decision:

```text
TEACHER_REFERENCE
```

### Publishing

Decision:

```text
TEACHER_REFERENCE
```

### BDP

Decision:

```text
TEACHER_REFERENCE
```

### BDS

Decision:

```text
TEACHER_REFERENCE
```

### BDH

Decision:

```text
TEACHER_REFERENCE
```

### FLDS

Decision:

```text
TEACHER_REFERENCE
```

### B-PIPE

Decision:

```text
TEACHER_REFERENCE
```

### xbbg

Decision:

```text
TEACHER_REFERENCE
```

### blpapi

Decision:

```text
CONDITIONAL implementation detail
```

Operational rule:

```text
only if validated in the actual ESILV environment
```

Do not freeze it as a generic CORE dependency without validation.

## 15. TD Bloomberg mapping

### Bloomberg access setup

Decision:

```text
CONDITIONAL
```

Current replacement:

```text
LIVE
or
APPROVED_SAMPLE
```

### Security identifier mapping

Decision:

```text
CORE
```

Destination:

```text
TD09
```

Current mapping:

```text
AAPL
-> AAPL US Equity

SP500
-> SPX Index
```

### Historical data

Decision:

```text
CORE in provider-stage concept
```

Destination:

```text
TD10
```

In APPROVED_SAMPLE mode, a committed reference fixture replaces live retrieval.

### OHLCV mapping

Decision:

```text
CORE
```

Destination:

```text
TD09 field mapping
TD10 normalization
```

Canonical schema:

```text
date
ticker
open
high
low
close
volume
```

### Reference-data requests

Decision:

```text
OPTIONAL
```

### Security metadata

Decision:

```text
OPTIONAL
```

### Intraday bars

Decision:

```text
OPTIONAL
```

Reason:

The MarketPulse CORE contract is:

```text
1 month
Daily
```

### 5-minute interval

Decision:

```text
DROP from common CORE
```

### matplotlib plotting in Bloomberg TD

Decision:

```text
DROP as required step
```

Reason:

The presentation layer is now introduced once, in TD11, through Dash + Plotly.

## 16. Historical project mapping

The former project contains many ideas.

They must be separated rather than migrated as one block.

### Dynamic external data

Decision:

```text
CORE
```

Current destination:

```text
TD08 Yahoo
TD09-TD10 Bloomberg
```

### Dashboard

Decision:

```text
CORE
```

Current destination:

```text
TD11
```

### Automatic refresh every 5 minutes

Decision:

```text
DROP from guided CORE
```

### Cron report

Decision:

```text
OPTIONAL
```

### 24/7 deployment

Decision:

```text
DROP from guided CORE
```

Possible future location:

```text
advanced deployment track
```

### Linux server deployment

Decision:

```text
OPTIONAL
```

### Backtesting

Decision:

```text
DROP from guided CORE
```

Potential use:

```text
separate final project option
```

### Max drawdown

Decision:

```text
DROP from guided CORE
```

### Sharpe ratio

Decision:

```text
DROP from guided CORE
```

### Multi-asset portfolio

Decision:

```text
DROP from guided CORE
```

### Correlation matrix

Decision:

```text
DROP from guided CORE
```

### Portfolio volatility

Decision:

```text
DROP from guided CORE
```

### Rebalancing

Decision:

```text
DROP from guided CORE
```

### Machine learning

Decision:

```text
DROP from guided CORE
```

### Streamlit

Decision:

```text
DROP as common framework
```

Current framework:

```text
Dash
```

### Public API / web scraping

Decision:

```text
DROP as common requirement
```

Current provider path is explicit:

```text
CSV / JSON
Yahoo Finance
Bloomberg
```

## 17. Historical assessment mapping

### Project 1/3

Decision:

```text
DROP as current weighting
```

### Exam 1/3

Decision:

```text
DROP as current weighting
```

### Tutorials 1/3

Decision:

```text
DROP as current weighting
```

Current official framing:

```text
Exam                35%
Lab work / Projects 35%
Final project       30%
```

### Historical exam file

Decision:

```text
TEACHER_REFERENCE
```

Reason:

Can inform question style, but it is not a current evaluation contract.

## 18. Historical LaTeX build system mapping

Legacy:

```text
pdflatex
minted
build.sh
build_all.sh
generated PDFs
```

Decision:

```text
DROP from MarketPulse repository architecture
```

Reason:

MarketPulse is intentionally:

```text
Markdown-first
GitHub-readable
diff-friendly
small-file oriented
```

The LaTeX sources may remain in the historical repository.

## 19. Images and diagrams mapping

The historical repository contains many diagrams and logos.

Examples include:

```text
Git staging diagrams
branch graphs
Linux architecture diagrams
Bloomberg keyboard images
Git logo
Python logo
Linux logo
```

Decision:

```text
TEACHER_REFERENCE
```

Important constraint:

The historical repository is private and no explicit license was identified during the analysis.

Therefore:

```text
do not bulk-copy images into the public MarketPulse repository
```

Recommended approach:

```text
rewrite diagrams
or
use independently licensed assets
or
link to official sources
```

## 20. Reverse mapping by MarketPulse TD

This section answers the opposite question:

```text
For each current TD,
which legacy ideas are preserved?
```

### TD01 - Bootstrap + Linux

Legacy inheritance:

```text
CM1 Linux CLI
TD1.1 navigation
TD1.3 grep
```

Preserved as CORE:

```text
pwd
ls
cd
cat
head
grep
terminal usage
```

Deliberately not inherited:

```text
chmod
sudo
chown
apt
SSH
SCP
cron
ACL
awk
sed
regex
```

### TD02 - Python + CSV / JSON

Legacy inheritance:

```text
general Python-in-finance orientation
file-oriented workflows
```

New MarketPulse contribution:

```text
CSV / JSON starter contract
instrument + benchmark model
canonical starter identifiers
```

This TD has no direct one-to-one historical equivalent.

### TD03 - Git Local Workflow

Legacy inheritance:

```text
CM2
TD2 basic workflow
staging mental model
diff
commit history
```

Preserved:

```text
status
diff
add
commit
log
show
```

Not inherited:

```text
hash-object
zlib
manual .git/objects manipulation
advanced reset
```

### TD04 - Branches + Merge

Legacy inheritance:

```text
CM3 branches
TD3 simple merge
TD3 conflict concept
```

Preserved:

```text
branch
switch
merge
conflict understanding
```

Moved to optional:

```text
manufactured multi-user conflict
interactive rebase
branch deletion
```

### TD05 - Remote Branch + Pull Request

Legacy inheritance:

```text
CM3 remote workflow
TD3 push
TD3 PR
```

Preserved:

```text
remote branch
push
Pull Request
```

New MarketPulse contribution:

```text
team baseline gate
team fork naming
individual contribution trace
```

### TD06 - Code Review

Legacy inheritance:

```text
PR approval concept
```

Expanded in MarketPulse:

```text
Files changed inspection
meaningful review
request correction only when real
approval
merge
sync main
```

This is a stronger explicit review stage than the historical path.

### TD07 - Data Normalization + Comparison

Legacy inheritance:

```text
financial-data orientation
```

New MarketPulse contribution:

```text
canonical rows
date alignment
period return
base 100
relative performance
analytics.py
```

This is largely a new pedagogical layer.

### TD08 - Yahoo Finance

Legacy inheritance:

```text
external market-data acquisition concept
```

New MarketPulse contribution:

```text
accessible non-proprietary bridge provider
yfinance
AAPL / ^GSPC mapping
provider-neutral analytics reuse
```

This is a major addition relative to the historical path.

### TD09 - Bloomberg Introduction

Legacy inheritance:

```text
Bloomberg context
professional identifiers
API concepts
```

MarketPulse adaptation:

```text
mapping first
no provider implementation yet
LIVE vs APPROVED_SAMPLE
no invented field names
```

### TD10 - Bloomberg Provider

Legacy inheritance:

```text
Bloomberg data acquisition
historical rows
OHLCV
```

MarketPulse adaptation:

```text
provider boundary
canonical normalization
AAPL / SP500 semantics
reuse analytics
fallback fixture
```

### TD11 - Dash Dashboard

Legacy inheritance:

```text
web-app requirement
interactive visualization concept
```

MarketPulse adaptation:

```text
Dash
Plotly
one Base-100 chart
shared snapshot
no duplicate provider logic
no duplicate analytics
```

### TD12 - Integration + Release

Legacy inheritance:

```text
deployment / reproducibility ambition
```

MarketPulse adaptation:

```text
clean repo
requirements
README
fresh run
final PR
review
merged main validation
Checkpoint C
```

This replaces infrastructure-heavy deployment with a smaller reproducibility contract.

## 21. Legacy content already fully represented in MarketPulse

The following historical concepts already have a clear current home:

```text
Linux navigation
file inspection
grep
Git status
Git diff
Git add
Git commit
Git log
branches
merge
push
Pull Request
review
remote synchronization
Bloomberg identifier mapping
Bloomberg provider boundary
OHLCV normalization
dashboard presentation
reproducibility
```

These should not be duplicated in a separate legacy lab.

## 22. Legacy content suitable for OPTIONAL work

Recommended optional backlog:

```text
Linux
- mkdir / cp / mv / rm drills
- chmod
- shell variables
- shell scripts
- pipes
- awk
- sed
- regex
- SSH
- SCP
- cron

Git
- restore
- revert
- reset
- aliases
- branch deletion
- manufactured conflict
- interactive rebase
- tags

Bloomberg
- reference-data request
- extra metadata
- intraday bars
- xbbg exploration
- blpapi low-level exploration

Infrastructure
- remote Linux deployment
- systemd
- Docker
- GitHub Actions
```

These activities should remain outside checkpoint requirements.

## 23. Legacy content suitable for TEACHER_REFERENCE

Recommended instructor-reference backlog:

```text
Unix history
GNU / POSIX
open-source context
VM vs containers
Docker / Kubernetes context
digital infrastructure sustainability
Git object model
blob / tree / commit
HEAD
plumbing vs porcelain
Gitflow
Bloomberg Terminal context
BDP / BDS / BDH
FLDS
Request / Response / Subscription
B-PIPE
xbbg vs blpapi
historical exam style
```

These topics can enrich explanations without expanding student deliverables.

## 24. Legacy content recommended for DROP from the common path

```text
mandatory cloud account creation
mandatory credit card
mandatory personal VM
ACL exercises
manual Git object construction
zlib object injection into .git/objects
mandatory interactive rebase
mandatory Gitflow
mandatory intraday Bloomberg
5-minute live refresh
24/7 hosting requirement
mandatory cron reporting
multi-asset portfolio analytics
Sharpe ratio
max drawdown
portfolio optimization
ML regression bonus
tree-based ML bonus
LaTeX build chain in the MarketPulse repository
historical evaluation weighting
```

Again:

```text
DROP
!=
bad topic
```

It means:

```text
not part of the current common 18-hour path
```

## 25. Relationship with the diagnostic questionnaire

The mapping also explains several diagnostic questions.

### Linux ceiling

Historical coverage explains the presence of questions on:

```text
mkdir
cp
chmod
pipes
stderr
environment variables
&&
```

Current interpretation:

```text
useful prior knowledge or ceiling
not common prerequisite
```

### Git ceiling

Historical coverage explains:

```text
git fetch
merge conflict
.gitignore
```

Current interpretation:

```text
foundation to intermediate for some items
ceiling for full conflict / ignore nuance
```

### Python / Bloomberg / Dash ceiling

Historical project ambition explains:

```text
virtual environment
missing-data policy
provider architecture
Dash callback
```

Current interpretation:

```text
advanced prior knowledge
not a requirement before TD01
```

## 26. Migration principles

Any future migration from the historical repository should follow these rules.

### Rule 1

Do not copy material only because it already exists.

Ask:

```text
Does it support a current learning objective?
```

### Rule 2

Do not expand a TD beyond its 80-minute CORE to make room for legacy material.

### Rule 3

Prefer:

```text
rewrite
+
simplify
+
contextualize inside MarketPulse
```

over:

```text
copy
+
paste
```

### Rule 4

Keep advanced material clearly labelled:

```text
OPTIONAL
or
TEACHER_REFERENCE
```

### Rule 5

Do not migrate third-party images or historical assets without confirming reuse rights.

### Rule 6

Do not reintroduce infrastructure dependencies that require personal payment information.

### Rule 7

Do not make LIVE Bloomberg connectivity a universal completion condition.

### Rule 8

Do not reintroduce finance complexity that obscures Python, Git and Linux learning goals.

## 27. Recommended next documents

The optional backlog is now documented in:

```text
docs/legacy/03_OPTIONAL_ADVANCED_CONTENT_BACKLOG.md
```

It transforms the items classified OPTIONAL into a structured backlog for:

```text
Linux Advanced
Git Advanced
Bloomberg Advanced
Remote Linux
Dash Advanced
Deployment
```

The instructor deep-dive reference is now documented in:

```text
docs/instructor/01_LEGACY_DEEP_DIVE_REFERENCE.md
```

It covers the items classified:

```text
TEACHER_REFERENCE
```

## 28. Final decision map

```text
LEGACY REPOSITORY
       |
       v
CONTENT INVENTORY
       |
       +-------------------+
       |                   |
       v                   v
CURRENT NEED          NO CURRENT NEED
       |                   |
       v                   v
CORE / OPTIONAL      REFERENCE / DROP
       |                   |
       +---------+---------+
                 |
                 v
           MARKETPULSE
```

The migration objective is therefore not:

```text
preserve everything
```

but:

```text
preserve value
+
remove overload
+
protect current contracts
+
keep advanced depth available
```

That is the intended bridge between the historical teaching material and the current MarketPulse curriculum.
