# Legacy Deep-Dive Reference for Instructors

## 1. Purpose

Ce document rassemble les éléments du cours historique qui ont été classés :

```text
TEACHER_REFERENCE
```

dans :

```text
docs/legacy/02_LEGACY_TO_MARKETPULSE_CONTENT_MAPPING.md
```

Il s'agit d'une ressource pour les enseignants.

Ce document ne crée aucun nouvel objectif étudiant obligatoire.

Il ne modifie pas :

```text
les 12 TD
les checkpoints
les commandes runtime
les exigences d'évaluation
les dépendances CORE
```

Le principe est :

```text
students need
<
instructor should understand
```

L'enseignant peut connaître un concept beaucoup plus profondément que ce qu'il demande aux étudiants de reproduire.

## 2. Source boundary

Ce document est principalement dérivé du repository historique :

```text
tawounfouet/intro_git_linux_bloomberg
```

Les sources historiques principales sont :

```text
src/CM0_Context.tex
src/CM1_Linux.tex
src/CM2_Git_local.tex
src/CM3_Git_remote.tex
src/CM4_bloomberg.tex
src/Project.tex
```

Le but n'est pas de recopier les supports historiques.

Le but est de préserver leur profondeur conceptuelle dans une forme compatible avec le nouveau parcours.

## 3. Instructor-use model

Chaque sujet doit être lu avec quatre questions :

```text
1. What do students need?
2. What should the instructor understand deeper?
3. When is this useful to explain?
4. When should the instructor stop?
```

La dernière question est essentielle.

Un bon approfondissement enseignant ne doit pas devenir automatiquement :

```text
un nouveau TD
+
un nouveau livrable
+
un nouveau prérequis
```

## 4. High-level map

| Domain | Student CORE need | Instructor deeper knowledge |
|---|---|---|
| Linux | Navigate, inspect, run | Unix philosophy, OS context, permissions, package context |
| Git local | status, diff, add, commit, log | HEAD, refs, objects, staging internals, content addressing |
| Git collaboration | branch, push, PR, review, merge | fetch model, merge vs rebase, workflows, Gitflow context |
| Bloomberg | identifiers, mapping, normalization, provider boundary | Terminal, BDP/BDS/BDH, API paradigms, B-PIPE, xbbg vs blpapi |
| Infrastructure | common environment | VM vs container, remote hosts, deployment context |
| Sustainability | not a TD objective | infrastructure cost, energy, PUE, carbon-aware context |
| Assessment history | current rubric only | historical course design and workload lessons |

# Part I - Linux and Unix deep dive

## 5. Unix philosophy

The historical course gives strong importance to the Unix/Linux ecosystem.

For the instructor, the useful conceptual frame is:

```text
small tools
+
text streams
+
composition
+
clear interfaces
```

This helps explain why commands such as:

```text
cat
grep
head
wc
awk
sed
```

can be composed rather than replaced by one monolithic command.

### Students need

In the CORE:

```text
pwd
ls
cd
cat
head
grep
```

### Instructor should additionally understand

```text
standard input
standard output
standard error
pipes
redirection
process exit status
shell composition
```

### Good moment to explain

During TD01 when students ask:

```text
Why use the terminal?
Why not open every file graphically?
Why is grep useful?
```

### Stop point

Do not turn TD01 into:

```text
awk
sed
regex
shell scripting
process management
```

unless the class is explicitly doing optional work.

## 6. GNU, Linux and POSIX context

The historical material includes:

```text
Unix history
GNU
Linux
POSIX
open source
```

This is useful cultural context.

### Students need

Only enough context to understand:

```text
Linux
=
the environment in which commands and Python execution occur
```

### Instructor should additionally understand

The historical distinction between:

```text
Unix
GNU tools
Linux kernel
POSIX conventions
shell
distribution
```

### Good moment to explain

In a short CM or introductory explanation.

### Stop point

Do not make historical terminology a prerequisite for practical lab completion.

## 7. Shell ecosystem

The historical course mentions:

```text
Bash
zsh
fish
```

MarketPulse standardizes teaching examples on:

```text
Bash on Linux
```

### Students need

Recognize that:

```text
shell
!=
Python
!=
Git
```

### Instructor should additionally understand

Why command syntax can vary slightly across shells and why examples should stay stable.

### Good moment to explain

When students compare local macOS, Windows, Codespaces or Linux behavior.

### Stop point

Do not teach multiple shells in parallel.

## 8. Permissions, ownership and privilege

Historical material covers:

```text
chmod
chown
sudo
root
read / write / execute
```

### Students need

No mandatory permission-management exercise in the common path.

### Instructor should additionally understand

```text
owner
group
others
read
write
execute
symbolic modes
basic numeric modes
privilege escalation
```

### Good moment to explain

When troubleshooting:

```text
script not executable
permission denied
SSH private-key permissions
```

### Stop point

Avoid turning troubleshooting into a Linux administration course.

Do not normalize:

```text
chmod 777
```

as a generic fix.

## 9. Package management and system tooling

Historical material uses:

```text
apt
sudo
system packages
```

### Students need

For MarketPulse:

```text
Python package installation
via pip
```

when required.

### Instructor should additionally understand

The difference between:

```text
system package manager
and
Python package manager
```

### Good moment to explain

When students confuse:

```text
apt install
pip install
```

### Stop point

Do not require system package administration in the common path.

## 10. Virtual machines vs containers

Historical material discusses:

```text
VMs
containers
Docker
Kubernetes
```

### Students need

Only the common environment provided by the course.

### Instructor should additionally understand

Conceptually:

```text
VM
=
virtualized operating system environment

container
=
isolated process environment sharing host kernel
```

### Good moment to explain

When positioning:

```text
Codespaces
remote Linux
Docker
deployment
```

### Stop point

Kubernetes remains outside the MarketPulse common path.

# Part II - Digital infrastructure and sustainability

## 11. Why infrastructure context matters

The historical CM0 includes material on:

```text
data centers
energy
PUE
network traffic
embodied emissions
operational emissions
cloud regions
carbon-aware computing
CodeCarbon
```

This material is not required for the 18-hour TD path.

It is nevertheless useful instructor context because MarketPulse uses:

```text
cloud-hosted development
remote data providers
network access
Git hosting
optional deployment
```

### Students need

No specific sustainability deliverable.

### Instructor should additionally understand

That digital systems have costs beyond code:

```text
compute
storage
network
hardware
energy
operations
```

### Good moment to explain

Short CM contextualization around:

```text
why efficient data movement matters
why repository hygiene matters
why unnecessary binary assets matter
```

### Stop point

Do not add a sustainability assignment unless it is explicitly part of the module objectives.

## 12. Git and binary-file cost

One useful historical teaching point is that Git works best with diff-friendly text.

### Students need

Use the Markdown-first MarketPulse repository normally.

### Instructor should additionally understand

Why large binary files create:

```text
repository growth
poor diffs
history cost
review friction
```

### Good moment to explain

When discussing:

```text
screenshots
PDFs
datasets
generated artifacts
```

### Stop point

Do not add Git LFS to the CORE unless a real repository need appears.

# Part III - Git local internals

## 13. Working tree, index and commit

This is one of the most important deep-dive concepts to preserve from the historical course.

The conceptual model is:

```text
working tree
      |
      v
staging area / index
      |
      v
commit
```

### Students need

TD03 should make this observable through:

```text
git status
git diff
git add
git diff --staged
git commit
git log
```

### Instructor should additionally understand

The index is not merely:

```text
a list of files to commit
```

It represents the staged snapshot that the next commit will record.

### Good moment to explain

When a student:

```text
edits
stages
edits again
```

and is surprised that the committed version differs from the final working-tree version.

This is also the conceptual basis of diagnostic question G11.

### Stop point

Do not introduce raw index-file internals in the common TD.

## 14. HEAD

Historical material explicitly teaches `HEAD`.

### Students need

They do not need `HEAD` as a standalone learning objective.

### Instructor should additionally understand

Conceptually:

```text
HEAD
=
reference to the currently checked-out branch or commit context
```

It helps explain:

```text
current branch
parent commit
HEAD~
detached HEAD
```

### Good moment to explain

When students ask about:

```text
git log
checkout history
reset
rebase
```

### Stop point

Avoid detached-HEAD exercises in the common sequence.

## 15. Git object model

Historical CM2 goes deeper into:

```text
blob
tree
commit
object database
hash
```

### Students need

No object-level manipulation.

### Instructor should additionally understand

The useful conceptual chain:

```text
file contents
      |
      v
blob

directory snapshot
      |
      v
tree

metadata + parent + tree
      |
      v
commit
```

This explains why Git is snapshot-oriented rather than simply a sequence of line patches.

### Good moment to explain

If students ask:

```text
What is a commit really?
Why does Git identify objects with hashes?
Why are branches lightweight?
```

### Stop point

Do not ask students to construct Git objects manually.

## 16. Content addressing and hashing

Historical TD material includes hashing and `git hash-object`.

### Students need

Only the idea that commits have identifiers.

### Instructor should additionally understand

That Git uses content-addressed objects.

A change in content produces a different object identity.

### Good moment to explain

When discussing:

```text
commit SHA
object identity
integrity
deduplication
```

### Stop point

Do not require manual SHA calculations.

## 17. Plumbing vs porcelain

Historical CM2 explicitly distinguishes these concepts.

### Instructor model

```text
porcelain
=
user-facing commands

plumbing
=
lower-level commands and object manipulation
```

### Students need

Only the user-facing commands.

### Good moment to explain

As cultural context for advanced Git students.

### Stop point

Do not add plumbing commands to the CORE.

## 18. Restore, revert and reset

These are classified OPTIONAL, but the instructor should understand the distinctions even when not teaching them.

Conceptually:

```text
restore
=
change working tree or staging state

revert
=
record a new commit that reverses an earlier commit

reset
=
move a branch reference and optionally modify index / working tree
```

### Instructor responsibility

Be able to recommend the least destructive recovery method.

### Stop point

Do not casually recommend:

```text
git reset --hard
```

on student team repositories.

# Part IV - Git remote and collaboration deep dive

## 19. Local branch vs remote-tracking branch

Students commonly confuse:

```text
main
origin/main
remote repository
```

### Students need

Enough understanding to:

```text
pull
push
synchronize
open PR
```

### Instructor should additionally understand

```text
main
=
local branch

origin/main
=
local remote-tracking reference

origin
=
configured remote
```

### Good moment to explain

During the TD04 -> TD05 baseline transition.

## 20. Fetch

The historical course gives `git fetch` an important role.

### Students need

MarketPulse uses fetch as part of synchronization support.

### Instructor should additionally understand

```text
fetch
=
update knowledge of remote objects and remote-tracking references
without integrating them into the current branch
```

### Good moment to explain

When contrasting:

```text
fetch
pull
merge
rebase
```

## 21. Merge vs rebase

Historical CM3 explicitly compares these approaches.

### Students need

The common path uses merge-oriented collaboration.

### Instructor should additionally understand

```text
merge
=
preserve branch topology and combine histories

rebase
=
replay commits on another base
and rewrite commit identities
```

### Good moment to explain

When advanced students ask how teams keep history clean.

### Stop point

Do not turn rebase into a mandatory workflow.

## 22. Interactive rebase

Historical material includes:

```text
reword
squash
delete
reorder
```

### Students need

Not required.

### Instructor should additionally understand

Why it is useful for local history cleanup and why it is dangerous on shared history.

### Good moment to explain

Only after students already understand commits, branches and PRs.

### Stop point

Do not require force-pushing shared branch history.

## 23. Gitflow

Historical CM3 presents Gitflow and also notes its mental and organizational overhead.

### Students need

MarketPulse uses a simpler workflow:

```text
feature branch
+
Pull Request
+
review
+
merge
```

### Instructor should additionally understand

Gitflow as an example of a more formal branching model with multiple branch categories.

### Good moment to explain

When discussing:

```text
why teams need a workflow
but not necessarily Gitflow
```

### Stop point

Do not import Gitflow into the student repository.

## 24. Tags and releases

Historical material mentions version tags as good practice.

### Students need

Not required in the current 12 TDs.

### Instructor should additionally understand

The conceptual distinction:

```text
branch
=
moving line of development

tag
=
named reference to a specific object / release point
```

### Good moment to explain

After TD12 or during optional release work.

# Part V - Bloomberg ecosystem deep dive

## 25. Scope warning

The historical Bloomberg CM contains claims and examples tied to the historical support.

This document preserves that conceptual organization.

Exact:

```text
products
features
access rights
field names
API availability
licensing
rate limits
```

must be validated against the actual ESILV Bloomberg environment before teaching them as operational facts.

MarketPulse therefore keeps:

```text
LIVE
or
APPROVED_SAMPLE
```

as the execution distinction.

## 26. Bloomberg Terminal context

Historical CM4 positions Bloomberg as an integrated financial-data and workflow environment.

It covers:

```text
market data
historical data
analytics
news
trading / execution
Excel integration
API integration
```

### Students need

For TD09:

```text
Bloomberg
=
professional market-data provider stage
```

### Instructor should additionally understand

The Terminal as a broader workflow platform rather than just a Python API endpoint.

### Good moment to explain

At the start of TD09.

### Stop point

Do not spend the whole TD teaching Terminal navigation.

## 27. Bloomberg security identifiers

Historical examples use identifiers such as:

```text
AAPL US Equity
TSLA US Equity
IBM US Equity
EURUSD Curncy
META US Equity
```

### Students need

MarketPulse CORE freezes:

```text
AAPL
-> AAPL US Equity

SP500
-> SPX Index
```

### Instructor should additionally understand

That provider identifiers may encode:

```text
security
market
asset class
```

and differ from application canonical tickers.

### Good moment to explain

TD09 mapping.

## 28. Excel Add-In and BDP / BDH / BDS

Historical CM4 introduces:

```text
BDP
BDH
BDS
```

with the conceptual meanings:

```text
BDP
=
single data point / field value

BDH
=
historical time series

BDS
=
bulk dataset
```

### Students need

No Excel-based implementation.

### Instructor should additionally understand

These names are useful for connecting common Bloomberg workflows to API concepts.

### Good moment to explain

Short contextual aside in TD09 or CM.

### Stop point

Do not add Excel as a second implementation path for MarketPulse.

## 29. Bloomberg API paradigms

Historical CM4 distinguishes three paradigms:

```text
Request / Response
Subscription
Publishing
```

### Students need

MarketPulse primarily needs a historical acquisition mental model.

### Instructor should additionally understand

#### Request / Response

```text
request data
receive messages
process result
```

#### Subscription

```text
continuous stream
until unsubscribed
```

#### Publishing

```text
publish / distribute data
```

### Good moment to explain

When students ask why MarketPulse uses daily historical retrieval rather than a live stream.

### Stop point

Do not move MarketPulse CORE into streaming architecture.

## 30. Bloomberg field discovery

Historical CM4 references field discovery through:

```text
FLDS
API field-information services
```

### Students need

Only fields observed or approved in the current environment.

### Instructor should additionally understand

The important methodological principle:

```text
discover or verify
rather than guess
```

This principle directly supports the current TD09 rule:

```text
do not invent Bloomberg field names
```

## 31. Market data services

Historical material references:

```text
//blp/mktdata
//blp/mktbar
//blp/mktvwap
```

### Students need

Not required.

### Instructor should additionally understand

Conceptually:

```text
market data
=
streaming values

market bar
=
aggregated OHLCV intervals

VWAP
=
volume-weighted average price context
```

### Good moment to explain

Only in an advanced Bloomberg discussion.

### Stop point

Do not introduce these services as CORE dependencies.

## 32. B-PIPE context

Historical CM4 positions B-PIPE as Bloomberg market-data infrastructure used for broader professional integration.

### Students need

No B-PIPE knowledge to complete MarketPulse.

### Instructor should additionally understand

That Bloomberg access patterns differ between:

```text
desktop / terminal-linked use
and
enterprise data-feed infrastructure
```

### Good moment to explain

When preventing students from assuming that every Bloomberg integration is equivalent.

## 33. xbbg vs blpapi

Historical CM4 provides a comparison.

The historical framing is:

```text
xbbg
=
higher-level convenience
+
less code

blpapi
=
lower-level
+
more verbose
+
greater API control
```

### Students need

No fixed choice unless the actual environment validates one.

### Instructor should additionally understand

Why a teaching abstraction can differ from a production API integration.

### Good moment to explain

When discussing the purpose of:

```text
src/providers/bloomberg_provider.py
```

### Stop point

Do not add both libraries to `requirements.txt` simply for completeness.

## 34. Historical Bloomberg best-practice claims

Historical CM4 mentions ideas such as:

```text
batch requests
avoid excessive API calls
asynchronous processing
logging requests and responses
```

These are useful architectural directions.

However, exact operational limits or recommended patterns should be validated before being presented as current Bloomberg rules.

### Students need

For CORE:

```text
simple provider boundary
honest mode
canonical normalization
```

### Instructor should additionally understand

Why production data integrations eventually need:

```text
efficiency
observability
error handling
access control
```

# Part VI - Historical project and assessment lessons

## 35. Historical project ambition

The previous project combined:

```text
external data
real-time refresh
Linux deployment
web application
cron
24/7 operation
backtesting
Sharpe
drawdown
portfolio analytics
optional ML
```

### Instructor lesson

The project is a useful source of professional scenarios.

It is also a warning about scope.

### Students need

In MarketPulse guided work:

```text
simple comparative analytics
provider boundaries
Git collaboration
Dash
reproducibility
```

### Instructor should additionally understand

Which advanced ideas may be reused later as:

```text
final-project options
optional challenges
inspiration
```

### Stop point

Do not reintroduce the whole historical project into the guided 18 hours.

## 36. Historical assessment model

The historical README used:

```text
1/3 project
1/3 exam
1/3 tutorials
```

The current official framing is different.

### Instructor rule

Historical weighting is reference only.

It must not be reused as a current assessment contract.

## 37. Historical exam material

Historical exam files may help reveal:

```text
question style
expected technical vocabulary
historical depth
```

### Instructor rule

Use them only as design references.

Do not assume:

```text
old exam
=
current exam specification
```

# Part VII - Instructor decision framework

## 38. Before explaining a deep concept

Ask:

```text
Does this help the current objective?
Will it unblock a student?
Will it improve a mental model?
Can I explain it in under 5 minutes?
Will it create a new expectation?
```

If the explanation creates a new expectation, move it to:

```text
OPTIONAL
```

or:

```text
advanced lab
```

## 39. Depth budget

For a 90-minute TD, a useful instructor rule is:

```text
CORE execution
=
priority

deep dive
=
short explanation only when useful

optional practice
=
only after CORE
```

The historical material should improve explanation quality without consuming the session.

## 40. Suggested deep dives by TD

| TD | Useful instructor deep dive | Keep short |
|---|---|---|
| TD01 | Unix philosophy, shell vs OS, permissions context | Yes |
| TD02 | stdlib vs external packages | Yes |
| TD03 | staging area, HEAD, object model | Yes |
| TD04 | branch refs, merge model | Yes |
| TD05 | local vs remote-tracking refs, fetch | Yes |
| TD06 | workflow conventions, Gitflow as contrast | Yes |
| TD07 | provider-neutral architecture | Already CORE concept |
| TD08 | provider-specific identifiers, library boundary | Yes |
| TD09 | Terminal context, BDP/BDH/BDS, field discovery | Yes |
| TD10 | request/response, xbbg vs blpapi context | Yes |
| TD11 | presentation boundary vs application logic | Already CORE concept |
| TD12 | tag/release concepts, deployment context | Yes |

## 41. Diagnostic connection

The diagnostic contains advanced questions on:

```text
permissions
stderr
environment variables
command chaining
Git fetch
merge conflicts
.gitignore
virtual environments
provider architecture
Dash callbacks
```

The historical repository helps explain why these topics appear.

### Instructor rule

Treat high success as:

```text
evidence that some students may be ready for deeper explanation
```

Treat low success as:

```text
normal for topics outside the entry baseline
```

Do not expand mandatory scope based only on ceiling questions.

# Part VIII - Safety and source discipline

## 42. Do not silently update historical claims

Historical slides may contain:

```text
old product figures
old pricing
old URLs
old package recommendations
old API examples
old academic-year assumptions
```

If a current factual claim matters operationally, verify it separately before teaching it as current.

This document preserves conceptual lessons, not current commercial facts.

## 43. Bloomberg claims

Especially verify before class:

```text
available identifiers
available fields
connector package
access rights
Terminal availability
Desktop API behavior
rate limits
B-PIPE availability
```

The current MarketPulse safety rule remains:

```text
observed or approved
not guessed
```

## 44. Third-party assets

The historical repository contains many images and generated PDFs.

No bulk migration is recommended.

Before reusing an image publicly:

```text
confirm source
confirm rights
prefer official or independently licensed asset
```

## 45. Credentials and cloud access

Historical exercises include cloud and SSH scenarios.

Current instructor rule:

```text
no personal payment requirement
no shared credentials
no committed private keys
no mandatory personal cloud account
```

Advanced remote labs should use instructor- or school-provisioned infrastructure where possible.

# Part IX - Recommended instructor reference backlog

## 46. High-priority deep dives to operationalize

R7.3 now governs the transformation of these topics into separate instructor notes.

Prioritize:

```text
1. Git staging mental model
2. HEAD / refs / remote-tracking refs
3. Git object model
4. merge vs rebase
5. Unix philosophy
6. permissions troubleshooting
7. Bloomberg Terminal and identifier context
8. BDP / BDS / BDH
9. Request / Response vs Subscription
10. xbbg vs blpapi
```

## 47. Topics that should remain contextual only

```text
Unix history
GNU history
POSIX history
Docker / Kubernetes context
data-center sustainability
Gitflow
B-PIPE
Publishing
historical exam structure
```

These can enrich teaching without becoming student tasks.

# Final reference model

## 48. The intended relationship

```text
LEGACY COURSE
      |
      v
CONCEPTUAL DEPTH
      |
      +----------------------+
      |                      |
      v                      v
TEACHER REFERENCE        OPTIONAL PRACTICE
      |                      |
      v                      v
better explanation       advanced students
      |                      |
      +----------+-----------+
                 |
                 v
          MARKETPULSE CORE
          remains unchanged
```

## 49. Final principle

The instructor should be able to answer deeper questions than the course requires.

The students should not be forced to learn every answer the instructor knows.

The design principle is therefore:

```text
deep instructor knowledge
+
small explicit student contract
=
better teaching
```

This document preserves the historical depth while protecting the current MarketPulse learning path.


## 50. Current operationalization status

This document is complete as a consolidated instructor reference.

It is not yet the final operational form for the 10 priority deep dives.

Current state:

```text
consolidated reference
=
DONE

separate instructor-ready notes
=
DONE

index
=
docs/instructor/deep-dives/README.md
```

R7.3 has now operationalized all 10 priority topics as separate instructor notes.

Canonical index:

```text
docs/instructor/deep-dives/README.md
```

The frozen 18-hour CORE remains unchanged.

The notes improve instructor usability without creating new mandatory student deliverables.
