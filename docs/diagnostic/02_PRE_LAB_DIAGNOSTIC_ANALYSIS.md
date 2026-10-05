# Pre-Lab Diagnostic Analysis

## 1. Purpose

This document analyses the initial 39-question pre-lab diagnostic against the current ESILV MarketPulse 18-hour learning path.

The questionnaire and the curriculum answer different questions:

```text
Diagnostic
=
What do students already know?
How far can the strongest students already go?
Where are the cohort's weak points?

MarketPulse curriculum
=
What do we actually teach?
In what order?
What is CORE?
What remains OPTIONAL?
What can realistically fit in 18 hours?
```

The two are complementary.

## 2. Executive conclusion

The diagnostic is strong as an exploratory instrument because each domain moves from basic questions toward intermediate and advanced questions.

However:

```text
39 diagnostic questions
!=
39 course prerequisites
```

The module explicitly assumes:

```text
No previous Linux experience required
No previous Git experience required
Some Python fundamentals expected
```

Advanced Linux, Git, provider-architecture or Dash questions must therefore not be interpreted as readiness failures.

## 3. Recommended interpretation layers

Use three layers:

```text
A. Entry / early-course signal
B. Useful prior experience
C. Ceiling / advanced prior knowledge
```

For Linux and Git, Layer A measures prior exposure rather than mandatory prerequisites.

For Python, the first fundamentals are the closest thing to a true entry baseline.

# 4. Linux analysis

Current TD01 CORE:

```text
pwd
ls
cd
cat
head
grep
Python version
Git version
run MarketPulse
```

| Question | Topic | Current curriculum relationship | Interpretation |
|---|---|---|---|
| L01 | `pwd` | Direct TD01 CORE | Entry / early-course |
| L02 | `ls -a` | `ls` is CORE; hidden-file option is extra detail | Useful prior experience |
| L03 | `cd ..` | Direct TD01 navigation | Entry / early-course |
| L04 | `mkdir` | Not required by current TD01 CORE | Useful prior experience |
| L05 | `cat` | Direct TD01 CORE | Entry / early-course |
| L06 | `cp` | Not required by current TD01 CORE | Useful prior experience |
| L07 | `grep` | Direct TD01 CORE | Entry / early-course |
| L08 | pipe + `wc -l` | Outside required TD01 scope | Ceiling |
| L09 | output redirection | Outside required TD01 scope | Ceiling |
| L10 | `chmod` | Outside required TD01 scope | Ceiling |
| L11 | stdout + stderr redirection | Outside required TD01 scope | Ceiling |
| L12 | environment variable + `os.environ` | Outside required CORE | Ceiling |
| L13 | `&&` chaining | Outside required CORE | Ceiling |

Linux conclusion:

```text
strong advanced results
=
possible acceleration

weak advanced results
!=
curriculum problem
```

# 5. Git analysis

Current Git progression:

```text
TD03
working tree -> staging -> commit history

TD04
branches -> merge -> conflict concept

TD05
remote branch -> push -> Pull Request

TD06
review -> merge -> synchronization
```

| Question | Topic | Current curriculum relationship | Interpretation |
|---|---|---|---|
| G01 | purpose of Git | Core mental model | Foundation |
| G02 | clone | Repository acquisition concept | Foundation |
| G03 | `git status` | TD03 CORE | Foundation |
| G04 | `git add` | TD03 CORE | Foundation |
| G05 | `git commit` | TD03 CORE | Foundation |
| G06 | `git switch -c` | TD04 CORE | Foundation |
| G07 | `git push -u` | TD05 CORE | Foundation |
| G08 | `git fetch origin` | Used in team-baseline synchronization | Intermediate |
| G09 | Pull Request | TD05 CORE | Intermediate |
| G10 | fork vs branch | Directly relevant to team-repository model | Intermediate |
| G11 | staged B vs working-tree C | Excellent staging-area mental-model check | Intermediate |
| G12 | full conflict resolution | Conflict understanding is CORE; full manual resolution is not mandatory | Ceiling |
| G13 | tracked file + `.gitignore` | Useful professional detail, not explicit CORE objective | Ceiling |

G11 is especially valuable because it tests:

```text
working tree
!=
staging area
!=
commit
```

# 6. Python analysis

The module expects some Python fundamentals.

| Question | Topic | Current curriculum relationship | Interpretation |
|---|---|---|---|
| P01 | type conversion | Directly useful in TD02 | Expected Python baseline |
| P02 | list indexing | Directly useful in TD02 | Expected Python baseline |
| P03 | dictionary access | Directly useful in TD02 | Expected Python baseline |
| P04 | loop + accumulation | Directly useful in TD02 | Expected Python baseline |
| P05 | function + return | Directly useful in TD02 | Expected Python baseline |
| P06 | list comprehension | Encountered in TD02 material | Useful prior experience |
| P07 | aliasing / mutability | General Python understanding, not a CORE dependency | Ceiling |
| P08 | exception handling | Useful professional Python, not required early | Ceiling |
| P09 | `with open(...)` | Directly present in starter and TD02 | Useful prior experience |
| P10 | virtual environment | Useful tooling knowledge, not current CORE objective | Ceiling |
| P11 | missing-data policy | Data-engineering maturity above basic prerequisite | Ceiling |
| P12 | provider data-access responsibility | Directly anticipates TD09-TD10 architecture | Ceiling |
| P13 | Dash callback | Callbacks are OPTIONAL in TD11 | Ceiling |

The most important readiness group is:

```text
P01-P05
```

It covers:

```text
conversion
lists
dictionaries
loops
functions
```

# 7. Key alignment observations

## P12

P12 anticipates the later architecture:

```text
provider-specific acquisition
        |
        v
canonical rows
        |
        v
provider-neutral analytics
```

It is a strong architecture ceiling question, not a prerequisite.

## P13

Current TD11 contract:

```text
static Dash dashboard = CORE
callbacks = OPTIONAL
selectors = OPTIONAL
```

Therefore:

```text
wrong P13 answer
!=
TD11 readiness problem
```

## G12

Current TD04 contract:

```text
understand merge conflict = CORE
manufactured full conflict exercise = OPTIONAL / instructor demo
```

## L11-L13

These measure shell maturity:

```text
stderr redirection
environment variables
conditional command chaining
```

They are useful diagnostic ceiling questions but not common CORE requirements.

# 8. Strengths of the questionnaire

## Progressive difficulty

Each domain moves from accessible questions toward discriminating questions.

## "I don't know yet"

This helps distinguish:

```text
recognized knowledge gap
from
confident misconception or guess
```

## Concrete situations

The questionnaire uses real commands and small code fragments rather than only terminology.

# 9. Main interpretation risk

Avoid:

```text
readiness = correct answers / 39
```

That would mix:

```text
expected Python fundamentals
skills taught later
skills outside CORE
optional material
```

A student can be fully ready while missing many ceiling questions.

# 10. Recommended result model

Analyse separately:

```text
Python fundamentals
Linux prior exposure
Git prior exposure
Intermediate collaborative Git
Advanced / ceiling knowledge
```

Suggested groups:

```text
Python fundamentals
P01-P05

Linux early-course exposure
L01, L03, L05, L07

Additional Linux exposure
L02, L04, L06

Git foundation
G01-G07

Intermediate collaborative Git
G08-G11

Advanced / ceiling
L08-L13
G12-G13
P07-P08
P10-P13

Useful Python prior experience
P06, P09
```

# 11. Time estimate

The form announces:

```text
25-35 minutes
estimate to be checked with a pilot
```

The pilot matters because intermediate students may take longer than beginners who select "I don't know yet" quickly or advanced students who answer confidently.

Do not freeze the duration until pilot evidence exists.

# 12. Overall assessment

The diagnostic is strongest for:

```text
finding the cohort floor
+
finding the cohort ceiling
+
identifying where pacing can change
```

The MarketPulse curriculum is strongest for:

```text
mandatory progression
+
CORE / OPTIONAL boundaries
+
realistic 90-minute lab scope
```

Recommended model:

```text
DIAGNOSTIC
What do they already know?

        +

CURRICULUM
What do we teach and in what order?

        |
        v

ADAPTIVE DELIVERY
Where should the instructor slow down,
maintain pace,
or accelerate?
```

See:

```text
docs/diagnostic/03_PRE_LAB_DIAGNOSTIC_INTERPRETATION_GUIDE.md
```