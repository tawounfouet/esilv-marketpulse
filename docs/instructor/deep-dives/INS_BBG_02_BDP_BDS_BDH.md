# INS-BBG-02 - BDP, BDS and BDH

Status:

```text
INSTRUCTOR_READY
```

Primary teaching moment:

```text
TD09 - Bloomberg Introduction
```

## 1. Purpose

Give the instructor a compact conceptual bridge between common Bloomberg data-retrieval patterns and the MarketPulse historical-data use case.

## 2. Student CORE boundary

Students do not need to implement Excel Bloomberg formulas.

They only need enough context to understand that different request shapes answer different data questions.

## 3. Instructor mental model

Historical Bloomberg teaching material distinguishes:

```text
BDP
=
single-point or field-oriented retrieval

BDH
=
historical time-series retrieval

BDS
=
bulk or set-like data retrieval
```

For MarketPulse, the closest conceptual fit is historical series retrieval:

```text
1 month
Daily
OHLCV-like observations
```

## 4. Best teaching moment

Use after introducing the Bloomberg mapping and before TD10 implementation.

Question:

```text
Are we asking for one value,
a historical series,
or a larger structured collection?
```

## 5. Short explanation

A useful analogy:

```text
BDP
"give me a value"

BDH
"give me values over time"

BDS
"give me a collection associated with the security"
```

This is conceptual vocabulary only.

The actual ESILV environment and approved integration path determine what students can execute.

## 6. Worked example

MarketPulse wants:

```text
AAPL
1 month
Daily
historical observations
```

That is conceptually aligned with:

```text
historical-data retrieval
```

rather than a single-point request.

The provider then normalizes observations into:

```text
date
ticker
open
high
low
close
volume
```

## 7. Common misconception

Misconception:

```text
BDP, BDH and BDS are three Python libraries.
```

Correction:

```text
they are Bloomberg retrieval concepts commonly encountered through Bloomberg workflows
```

Misconception:

```text
MarketPulse needs all three.
```

Correction:

```text
the CORE needs only the concepts necessary for its provider stage
```

## 8. Stop point

Do not add:

```text
Excel implementation
multiple parallel Bloomberg integration paths
extra dependencies
```

to TD09 or TD10 merely to demonstrate the vocabulary.

## 9. Source discipline

This note preserves conceptual organization from historical CM4.

Operational details must be checked in the current approved Bloomberg environment.

Current provider rule:

```text
LIVE
or
APPROVED_SAMPLE
```

APPROVED_SAMPLE is not LIVE evidence.

## 10. Optional extension

If the current environment supports a reference-data exercise, connect this note to:

```text
ADV-BBG-01 - Bloomberg reference data
```

Do not promote that advanced item into the CORE implicitly.
