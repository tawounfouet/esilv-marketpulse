# TD09 - Bloomberg Introduction

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"The trading desk now has access to a professional market-data environment."
```

## Context

MarketPulse can now work with:

```text
CSV / JSON
+
Yahoo Finance
```

The analytical contract is already stable:

```text
1 instrument
+
1 benchmark
+
same lookback
+
same interval
+
aligned observations
+
performance comparison
```

TD09 introduces Bloomberg as a professional market-data environment.

The goal today is not to redesign the entire application.

The goal is to understand:

- how Bloomberg identifies financial instruments;
- how a professional provider differs from the previous sources;
- how to retrieve or inspect a first Bloomberg market-data sample;
- how Bloomberg data can later feed the same MarketPulse comparison model.

TD10 will focus on integrating Bloomberg as a real MarketPulse provider.

## Learning objectives

At the end of TD09, you should be able to:

- explain Bloomberg's role in the MarketPulse architecture;
- distinguish business identifiers from provider-specific identifiers;
- recognize Bloomberg-style instrument identifiers;
- identify the instrument and benchmark used by MarketPulse;
- retrieve or inspect a first Bloomberg market-data sample when the teaching environment permits;
- identify the main fields required by MarketPulse;
- compare Bloomberg output with the MarketPulse canonical row structure;
- explain why Bloomberg-specific logic must remain outside analytical functions;
- describe what must be normalized before TD10.

## Expected result

At the end of TD09, you should be able to describe the mapping:

```text
Business instrument
AAPL - Apple Inc.
        |
        v
Bloomberg identifier
AAPL US Equity
```

and:

```text
Business benchmark
S&P 500
        |
        v
Bloomberg identifier
SPX Index
```

You should also have inspected or retrieved enough Bloomberg data to identify:

```text
date
open
high
low
close
volume
```

or the closest Bloomberg fields available in the teaching environment.

## Important environment note

Bloomberg access depends on the ESILV teaching environment.

The exact access method may depend on:

- the Bloomberg workstation or Terminal;
- the installed Bloomberg software;
- the Python environment;
- the permissions available during the session.

The instructor will confirm the exact connection method used in class.

Do not attempt to bypass Bloomberg access controls.

Do not use personal credentials from another student.

Do not commit Bloomberg credentials or session information.

## Prerequisites

Before starting:

```text
[ ] TD01-TD08 completed
[ ] Checkpoint B completed or ready
[ ] team main is up to date
[ ] CSV provider understood
[ ] Yahoo provider understood
[ ] canonical row model understood
[ ] comparison logic works
```

Update local main:

```bash
git switch main
git pull
git status
```

Run the current MarketPulse version:

```bash
python src/main.py
```

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | Bloomberg in the MarketPulse architecture |
| 10-25 min | Business identifiers vs Bloomberg identifiers |
| 25-40 min | Discover the Bloomberg teaching environment |
| 40-58 min | Retrieve or inspect a first data sample |
| 58-70 min | Map Bloomberg fields to MarketPulse |
| 70-80 min | Compare Yahoo and Bloomberg responsibilities |
| 80-90 min | Prepare TD10 integration work |

# Part 1 - Position Bloomberg in MarketPulse

The project now has three provider stages:

```text
CSV
 |
 v
local teaching data

Yahoo Finance
 |
 v
accessible remote market data

Bloomberg
 |
 v
professional market-data environment
```

The business logic should remain stable:

```text
provider
   |
   v
canonical market data
   |
   v
instrument + benchmark alignment
   |
   v
period return
   |
   v
base 100
   |
   v
relative performance
```

## Question

> Which part of MarketPulse should change when a new provider is introduced?

Mainly the acquisition and normalization layer.

The performance formulas should not need to know whether data came from CSV, Yahoo Finance or Bloomberg.

# Part 2 - Business identifiers vs provider identifiers

MarketPulse keeps a business-level identity.

For the common starter:

```text
Instrument business ticker
AAPL

Benchmark business ticker
SP500
```

Provider identifiers may differ.

## 2.1 Instrument mapping

```text
Business concept : Apple Inc.
Canonical ticker : AAPL
Yahoo symbol     : AAPL
Bloomberg        : AAPL US Equity
```

## 2.2 Benchmark mapping

```text
Business concept : S&P 500
Canonical ticker : SP500
Yahoo symbol     : ^GSPC
Bloomberg        : SPX Index
```

The exact provider identifiers used in class should be confirmed in the teaching environment.

## Question

> Why should analytical code continue to use the canonical business ticker rather than a Bloomberg-specific identifier?

Because the same analytical code should remain reusable across providers.

# Part 3 - Understand a Bloomberg identifier

A Bloomberg identifier can encode more information than a simple exchange ticker.

Examples used in the course:

```text
AAPL US Equity
SPX Index
```

These identifiers help Bloomberg distinguish:

- the security;
- the market or region context;
- the security type.

You do not need to master the full Bloomberg symbology in TD09.

The objective is to understand that provider identifiers are part of acquisition configuration.

# Part 4 - Discover the teaching environment

Before writing code, identify what is actually available.

With the instructor, verify:

```text
[ ] Bloomberg access is available
[ ] the required Bloomberg software is running
[ ] Python access is available if required
[ ] the teaching environment can query AAPL US Equity
[ ] the teaching environment can query SPX Index
```

The exact commands or Python package used for access are environment-dependent.

Do not install random Bloomberg-related packages from the internet unless the instructor explicitly asks you to.

# Part 5 - Identify the data request

MarketPulse needs historical daily market data.

The common business contract remains:

```text
Instrument : AAPL
Benchmark  : S&P 500
Lookback   : approximately 1 month
Interval   : Daily
```

The minimum useful historical fields are conceptually:

```text
date
open
high
low
close
volume
```

Depending on the Bloomberg query available in class, field names may use Bloomberg-specific naming.

Your task is to identify the fields returned and determine how they map to MarketPulse.

# Part 6 - First Bloomberg sample

Use the instructor-approved Bloomberg access method.

The first goal is deliberately small:

```text
one instrument
+
small historical window
+
one or several price fields
```

Start with:

```text
AAPL US Equity
```

and request a short historical daily sample.

Do not begin with both instrument and benchmark if the connection itself has not yet been validated.

## Record what you observe

Write down:

```text
Bloomberg identifier:
Returned fields:
Date representation:
Data structure:
Number of rows:
Missing values:
```

## Questions

1. How is the Bloomberg instrument identified?
2. How are dates represented?
3. Are numeric values already numeric?
4. Which returned field corresponds to the closing price?
5. Does the response look similar to the Yahoo data structure?

# Part 7 - Retrieve or inspect the benchmark

After the instrument request works, repeat the experiment with:

```text
SPX Index
```

The objective is not yet to build a reusable provider.

The objective is to confirm that both business objects can be represented in Bloomberg.

Record:

```text
Instrument Bloomberg identifier : AAPL US Equity
Benchmark Bloomberg identifier  : SPX Index
```

# Part 8 - Map Bloomberg output to the canonical model

MarketPulse expects the canonical row contract:

```python
{
    "date": "...",
    "ticker": "...",
    "open": ...,
    "high": ...,
    "low": ...,
    "close": ...,
    "volume": ...,
}
```

Your TD09 task is to create a mapping table.

Example structure:

| MarketPulse field | Bloomberg source field | Notes |
|---|---|---|
| date | environment-dependent | daily observation date |
| ticker | application mapping | canonical ticker |
| open | Bloomberg field used in class | numeric |
| high | Bloomberg field used in class | numeric |
| low | Bloomberg field used in class | numeric |
| close | Bloomberg field used in class | numeric |
| volume | Bloomberg field used in class | may depend on instrument type |

Do not invent Bloomberg field names if they have not been confirmed in your environment.

Complete the table using the actual output available during the lab.

# Part 9 - Preserve canonical tickers

Even if Bloomberg uses:

```text
AAPL US Equity
SPX Index
```

MarketPulse should still produce rows with:

```text
AAPL
SP500
```

Example target:

```python
{
    "date": "YYYY-MM-DD",
    "ticker": "SP500",
    "open": ...,
    "high": ...,
    "low": ...,
    "close": ...,
    "volume": ...,
}
```

This keeps the analytical layer independent from Bloomberg symbology.

# Part 10 - Compare Yahoo and Bloomberg

Complete this conceptual comparison.

| Concept | Yahoo stage | Bloomberg stage |
|---|---|---|
| Instrument business ticker | AAPL | AAPL |
| Benchmark business ticker | SP500 | SP500 |
| Provider instrument identifier | AAPL | AAPL US Equity |
| Provider benchmark identifier | ^GSPC | SPX Index |
| Lookback | 1 month | 1 month target |
| Interval | Daily | Daily target |
| Output target | canonical rows | canonical rows |
| Analytics | shared | shared |

The provider changes.

The business contract does not.

# Part 11 - Create the TD09 branch

The discovery work should still follow the Git workflow.

Create:

```bash
git switch main
git pull
git switch -c docs/bloomberg-mapping
```

For TD09, the main deliverable may be documentation rather than a complete provider implementation.

Create:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

Suggested structure:

```markdown
# Bloomberg Field Mapping

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Historical request

- Lookback: 1 month
- Interval: Daily
- Access method used in class: <complete during TD>

## Returned fields

| MarketPulse field | Bloomberg field | Notes |
|---|---|---|
| date | ... | ... |
| open | ... | ... |
| high | ... | ... |
| low | ... | ... |
| close | ... | ... |
| volume | ... | ... |

## Observations

Document any provider-specific behaviour observed during the session.
```

Do not include credentials or screenshots containing secrets in this document.

# Part 12 - Commit the mapping document

Inspect:

```bash
git status
git diff
```

Stage:

```bash
git add docs/BLOOMBERG_FIELD_MAPPING.md
```

Commit:

```bash
git commit -m "docs: map Bloomberg data to MarketPulse"
```

Push:

```bash
git push -u origin docs/bloomberg-mapping
```

Open a Pull Request.

Suggested title:

```text
docs: map Bloomberg data to MarketPulse
```

# Part 13 - Review the mapping

Another student should review the document.

The reviewer checks:

```text
[ ] instrument mapping is documented
[ ] benchmark mapping is documented
[ ] canonical tickers are preserved
[ ] fields reflect actual classroom output
[ ] no unverified Bloomberg field name is invented
[ ] no credentials are present
[ ] no unrelated file is included
```

Merge after review.

# Part 14 - If Bloomberg access works

If the teaching environment supports live retrieval during TD09, capture enough information to prepare TD10.

Record:

```text
access method
import or connection mechanism
request shape
response shape
field names
date format
numeric types
empty-response behaviour
```

Do not attempt to build the final provider if the class has not yet understood the response format.

# Part 15 - If Bloomberg access is unavailable

Bloomberg access may be unavailable because of:

- workstation availability;
- session state;
- network restrictions;
- account permissions;
- teaching-room configuration.

If live access is unavailable:

1. do not fabricate a successful request;
2. do not use another student's credentials;
3. use the instructor-approved fallback assets;
4. complete the field-mapping exercise from that approved sample;
5. document that the session used `APPROVED_SAMPLE` rather than `LIVE`;
6. continue the architectural work.

Instructor reference:

```text
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
```

Fallback input:

```text
data/sample/bloomberg_reference_sample.json
```

Expected canonical result:

```text
data/sample/bloomberg_reference_expected.json
```

The fallback fixture uses teaching wrapper keys, not claimed Bloomberg field mnemonics.

A local approved sample supports mapping and normalization practice.

It does not prove live Bloomberg connectivity.

# Part 16 - Security and access rules

Never commit:

- Bloomberg usernames;
- passwords;
- session tokens;
- API credentials;
- workstation-specific secrets;
- screenshots exposing credentials.

Do not copy credentials between students.

Do not place credentials in:

```text
README.md
settings.yml
Python source
notebooks
screenshots
Git history
```

If credentials appear accidentally in a tracked file, notify the instructor immediately.

# Part 17 - Provider boundary recap

At the end of TD09, the target architecture should be clear:

```text
Bloomberg-specific identifier
          |
          v
Bloomberg request
          |
          v
Bloomberg response
          |
          v
provider normalization
          |
          v
MarketPulse canonical row
          |
          v
existing analytics
```

The provider boundary is where Bloomberg-specific concepts should be translated.

# Part 18 - Mini exercises

## Exercise 1 - Identifier mapping

Explain the difference between:

```text
SP500
^GSPC
SPX Index
```

Use the terms:

```text
canonical business ticker
Yahoo provider symbol
Bloomberg provider identifier
```

## Exercise 2 - Field mapping

Choose one Bloomberg field returned in class.

Explain which canonical MarketPulse field it should feed and why.

## Exercise 3 - Missing volume

Suppose the benchmark response does not provide a useful volume.

Question:

> Does this prevent period-return and base-100 comparison?

Explain your answer.

## Exercise 4 - Provider independence

Identify one TD07 analytical function that should work unchanged after Bloomberg normalization.

# Part 19 - If you finish early

## Challenge 1 - Provider configuration sketch

Draft a simple configuration concept:

```text
canonical ticker
+
Yahoo symbol
+
Bloomberg identifier
```

Do not redesign the whole project.

## Challenge 2 - Compare three providers

Create a small table:

```text
CSV
Yahoo
Bloomberg
```

and identify which elements are provider-specific and which are shared.

## Challenge 3 - Response validation checklist

Draft a small checklist for TD10:

```text
not empty
expected fields present
dates available
numeric values valid
canonical ticker assigned
```

## Challenge 4 - Draw the boundary

Draw an ASCII diagram showing where Bloomberg-specific code should stop and MarketPulse generic logic should begin.

# Part 20 - Troubleshooting

## Bloomberg environment is not available

Use the instructor-approved fallback sample if provided.

Do not replace Bloomberg with an unapproved public source and claim that TD09 live access succeeded.

## Identifier not recognized

Verify the identifier with the instructor and the Bloomberg environment.

Do not guess multiple identifiers until one happens to work.

## Returned fields differ from expectation

Inspect the actual response.

Update your mapping document to reflect observed fields.

Do not force the response into an assumed schema before understanding it.

## Python integration is unavailable but Bloomberg UI works

Use the environment to inspect the identifiers and data fields.

Document the gap.

TD10 integration will depend on the access mechanism available in class.

# Part 21 - Readiness check

Before finishing TD09, each student should be able to explain:

```text
[ ] Bloomberg's role in MarketPulse
[ ] canonical ticker vs provider identifier
[ ] AAPL vs AAPL US Equity
[ ] SP500 vs SPX Index
[ ] why provider-specific identifiers stay outside analytics
[ ] which canonical fields MarketPulse requires
[ ] what Bloomberg access method was available in class
[ ] which Bloomberg fields were actually observed
[ ] how the observed fields map to MarketPulse
```

The team should confirm:

```text
[ ] Bloomberg mapping document exists
[ ] mapping was reviewed
[ ] no credentials were committed
[ ] live access is documented accurately
[ ] fallback sample use is documented if applicable
```

# Part 22 - What comes next?

TD09 establishes the Bloomberg vocabulary and data mapping.

The next business requirement is:

```text
"MarketPulse must support Bloomberg without rewriting the whole application."
```

In TD10, the team will implement the Bloomberg provider boundary.

The target will be:

```text
CSV
Yahoo
Bloomberg
   |
   v
canonical market data
   |
   v
same comparison logic
```

TD10 therefore moves from Bloomberg discovery to Bloomberg integration.
