# Pre-Lab Diagnostic Interpretation Guide

## 1. Purpose

This guide explains how the teaching team can use the pre-lab diagnostic to adapt delivery of the 12 MarketPulse labs.

It does not define a student grade and does not replace the module assessment model.

The canonical assessment evidence remains:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

## 2. Core principle

Do not reduce the diagnostic to one undifferentiated 39-question readiness score.

Use:

```text
domain
+
question layer
+
cohort pattern
+
completion time
+
"I don't know yet" pattern
```

The objective is instructional adaptation.

## 3. Recommended reporting dimensions

Report at least:

```text
A. Python fundamentals
B. Linux prior exposure
C. Git prior exposure
D. Intermediate collaborative Git
E. Advanced / ceiling knowledge
F. Completion time
G. "I don't know yet" frequency
```

# 4. Python fundamentals

Primary group:

```text
P01-P05
```

If the cohort is weak:

```text
TD02
-> slower code walkthrough
-> explicit type-conversion explanation
-> more live list and dictionary examples
-> smaller function-building steps
-> preserve full buffer
```

If the cohort is strong:

```text
TD02
-> shorten syntax recap
-> move faster to CSV / JSON
-> spend more time on reusable functions
-> preserve the same CORE definition of done
```

# 5. Linux prior exposure

Primary group:

```text
L01
L03
L05
L07
```

Additional exposure:

```text
L02
L04
L06
```

If early exposure is weak:

```text
TD01
-> keep full navigation pacing
-> demonstrate before independent execution
-> reinforce current directory and relative paths
-> keep environment support time
```

This is not a readiness failure because no previous Linux experience is required.

If early exposure is strong:

```text
TD01
-> accelerate command explanation
-> spend more time on repository orientation
-> spend more time on CSV / JSON inspection
-> use advanced shell work only after CORE completion
```

Do not automatically promote L08-L13 into CORE.

# 6. Git prior exposure

Foundation group:

```text
G01-G07
```

Intermediate collaborative group:

```text
G08-G11
```

If G01-G05 are weak:

```text
TD03
-> slow down working tree / staging / commit model
-> use visual diagrams
-> inspect real TD02 changes
-> emphasize git status and git diff
```

If G01-G07 are strong:

```text
TD03
-> shorter command explanation
-> more practice on meaningful diffs and commits

TD04
-> move quickly to branch isolation
```

If G08-G11 are strong:

```text
TD05-TD06
-> less time defining remote concepts
-> more time on PR quality
-> more time on code-review quality
```

# 7. Advanced / ceiling signal

Recommended ceiling group:

```text
L08-L13
G12-G13
P07-P08
P10-P13
```

High ceiling results may justify:

```text
OPTIONAL challenges
peer explanation where appropriate
faster explanations in later labs
```

Keep the common CORE unchanged.

Low ceiling results require no remediation.

# 8. P12 and P13

## P12 - Provider architecture

High success may indicate prior understanding of:

```text
data-access layer
provider boundary
separation of responsibilities
```

Possible consequence:

```text
TD09-TD10
-> shorter architecture explanation
-> more time on mapping and normalization
```

## P13 - Dash callback

Callbacks are OPTIONAL in the current CORE.

High success may justify optional interactive work for advanced teams.

Low success requires no change to TD11.

# 9. "I don't know yet"

Do not treat:

```text
wrong answer
```

and:

```text
I don't know yet
```

as pedagogically identical.

A provisional interpretation is:

```text
I don't know yet
=
recognized knowledge gap

incorrect answer
=
possible misconception or guess
```

Use this distinction for teaching, not grading.

# 10. Cohort-level adaptation

The diagnostic should primarily guide:

```text
class pacing
demonstration depth
scaffolding
optional extensions
instructor emphasis
```

Avoid permanent labels such as:

```text
weak student
strong student
not ready
```

based on one short diagnostic.

# 11. Provisional cohort heuristics

These thresholds are only teaching heuristics and must be calibrated after the pilot.

### Around 80% or more correct on a basic group

Possible signal:

```text
most of the cohort already knows this material
```

Action:

```text
consider accelerating explanation
but keep CORE validation
```

### Around 50-80% correct

Possible signal:

```text
mixed cohort
```

Action:

```text
keep planned pacing
use peer comparison and instructor checks
preserve buffer
```

### Below around 50% correct

Possible signal:

```text
limited prior exposure
```

Action:

```text
use full planned scaffolding
avoid promoting optional material
protect the buffer
```

These are not grades.

# 12. Pilot review

After teacher testing and the first student pilot, record:

```text
median completion time
range of completion times
questions frequently left as "I don't know yet"
questions with unexpected error rates
ambiguous questions
disputed answers
code readability issues
access issues
```

For each question, decide:

```text
keep
rewrite
replace
remove
```

# 13. Timing

Current estimate:

```text
25-35 minutes
```

Do not treat it as final before pilot evidence exists.

Intermediate students may take longest because they attempt more reasoning than students who answer confidently or select "I don't know yet".

# 14. Suggested teaching-team summary

```text
COHORT DIAGNOSTIC SUMMARY

Python fundamentals
- P01-P05: ...

Linux early-course exposure
- L01/L03/L05/L07: ...

Git foundation
- G01-G07: ...

Collaborative Git
- G08-G11: ...

Advanced ceiling
- L08-L13 / G12-G13 / selected Python ceiling: ...

Median completion time
- ...

Main misconceptions
- ...

Teaching adjustments
- TD01: ...
- TD02: ...
- TD03-TD06: ...
- TD08-TD11 optional scope: ...
```

# 15. Mapping to MarketPulse

```text
Linux results
        |
        v
TD01 pacing

Python fundamentals
        |
        v
TD02 scaffolding

Git foundation
        |
        v
TD03-TD04 pacing

Collaborative Git
        |
        v
TD05-TD06 pacing

Provider architecture ceiling
        |
        v
TD09-TD10 explanation depth

Dash callback ceiling
        |
        v
TD11 OPTIONAL interaction track
```

# 16. What must not change automatically

Diagnostic results should not silently redefine:

```text
MarketPulse CORE
checkpoint contracts
runtime commands
evidence filenames
provider honesty rules
security requirements
```

Any curriculum change should be explicit and documented.

# 17. Recommended use before the first TD

```text
1. Run the diagnostic.
2. Review cohort results by domain.
3. Review pilot timing.
4. Identify two or three teaching adjustments only.
5. Keep the published CORE stable.
6. Use OPTIONAL material for advanced groups.
7. Reassess after TD02 and TD06 using actual classroom evidence.
```

The diagnostic informs teaching.

It does not replace observation during the labs.