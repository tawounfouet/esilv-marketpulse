# TD10 - Bloomberg Provider

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"MarketPulse must support Bloomberg without rewriting the whole application."
```

## Context

TD09 introduced Bloomberg as a professional market-data environment.

You identified:

- the Bloomberg access method available in class;
- the Bloomberg identifiers for the MarketPulse instrument and benchmark;
- the fields actually returned by the teaching environment;
- the mapping between Bloomberg data and the MarketPulse canonical row model.

TD10 now turns that discovery work into an application provider.

The target architecture is:

```text
CSV
Yahoo
Bloomberg
   |
   v
canonical market data
   |
   v
same alignment logic
   |
   v
same analytics
   |
   v
same MarketPulse output
```

The key objective is provider independence.

## Learning objectives

At the end of TD10, you should be able to:

- isolate Bloomberg-specific acquisition logic;
- reuse the mapping documented in TD09;
- preserve canonical MarketPulse tickers;
- normalize Bloomberg output to the common row contract;
- feed existing analytics without Bloomberg-specific changes;
- select a provider without duplicating analytical code;
- validate both instrument and benchmark paths;
- handle a simple provider failure;
- explain where Bloomberg-specific code starts and stops;
- complete the established GitHub workflow.

## Expected result

MarketPulse should be able to use a Bloomberg provider path such as:

```text
Provider   : Bloomberg
Instrument : AAPL - Apple Inc.
Bloomberg  : AAPL US Equity

Benchmark  : S&P 500
Bloomberg  : SPX Index

Lookback   : 1 month
Interval   : Daily
```

and then reuse:

```text
alignment
period return
daily return
base 100
relative performance
```

without implementing separate Bloomberg-specific formulas.

## Important environment rule

The Bloomberg connection code depends on the actual ESILV teaching environment.

Use only the access method confirmed during TD09.

Do not:

- invent a Bloomberg Python package;
- install random Bloomberg connectors;
- copy another student's credentials;
- commit credentials;
- bypass access controls.

If the class uses an instructor-provided Bloomberg sample instead of a live connection, clearly preserve that distinction.

## Prerequisites

Before starting:

```text
[ ] TD01-TD09 completed
[ ] docs/BLOOMBERG_FIELD_MAPPING.md exists
[ ] Bloomberg identifiers are confirmed
[ ] available Bloomberg fields are documented
[ ] CSV provider path works
[ ] Yahoo provider path works
[ ] common comparison logic works
[ ] team main is up to date
```

Update local main:

```bash
git switch main
git pull
git status
```

Run MarketPulse before changing anything:

```bash
python src/main.py
```

Start from a clean working tree.

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | Review TD09 mapping |
| 10-25 min | Create Bloomberg provider boundary |
| 25-45 min | Implement or connect acquisition |
| 45-60 min | Normalize Bloomberg output |
| 60-72 min | Integrate instrument and benchmark |
| 72-82 min | Reuse existing analytics |
| 82-90 min | Validate, PR and review |

# Part 1 - Review the TD09 mapping

Open:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

Before writing provider code, verify that the document contains:

```text
[ ] instrument canonical ticker
[ ] instrument Bloomberg identifier
[ ] benchmark canonical ticker
[ ] benchmark Bloomberg identifier
[ ] access method used in class
[ ] observed historical fields
[ ] date representation
[ ] notes about missing or provider-specific values
```

Do not start from assumptions that contradict the actual TD09 observations.

# Part 2 - Create the feature branch

Create:

```bash
git switch main
git pull
git switch -c feature/bloomberg-provider
```

Verify:

```bash
git branch
git status
```

All TD10 work should stay on this branch until review and merge.

# Part 3 - Create the Bloomberg provider module

TD10 extends the same frozen CORE structure:

```text
src/
├── main.py
├── analytics.py
└── providers/
    ├── __init__.py
    ├── yahoo_provider.py
    └── bloomberg_provider.py
```

Create:

```text
src/providers/bloomberg_provider.py
```

The provider should have two conceptual responsibilities:

```text
1. acquire Bloomberg data
2. normalize Bloomberg data
```

It should not calculate:

```text
period return
daily return
base 100
relative performance
```

Those belong to the shared analytical layer.

## 3.1 Provider boundary

Conceptually:

```text
Bloomberg identifier
        |
        v
Bloomberg-specific request
        |
        v
Bloomberg-specific response
        |
        v
normalization
        |
        v
MarketPulse canonical rows
```

# Part 4 - Define the Bloomberg identifier mapping

Keep provider identifiers near provider configuration.

A simple mapping may look like:

```python
BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}
```

This mapping means:

```text
canonical ticker
        |
        v
Bloomberg identifier
```

The rest of MarketPulse should continue to use:

```text
AAPL
SP500
```

not Bloomberg identifiers as universal application identifiers.

# Part 5 - Separate acquisition from normalization

A useful provider design has two steps.

## 5.1 Acquisition step

The exact implementation depends on the teaching environment.

Conceptually:

```python
def fetch_raw_bloomberg_history(
    identifier,
    start_date,
    end_date,
):
    ...
```

Replace the implementation body only with the instructor-approved access mechanism.

The function should return the raw Bloomberg response.

Do not put MarketPulse analytics inside it.

## 5.2 Normalization step

Create a function that transforms the observed Bloomberg response into canonical rows.

Conceptual signature:

```python
def normalize_bloomberg_history(
    raw_data,
    canonical_ticker,
):
    ...
```

The output must use:

```text
date
ticker
open
high
low
close
volume
```

The exact source-field names must come from:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

Do not invent field names that were not observed in TD09.

# Part 6 - Build the provider function

Create a high-level function such as:

```python
def fetch_bloomberg_prices(
    identifier,
    canonical_ticker,
    start_date,
    end_date,
):
    raw_data = fetch_raw_bloomberg_history(
        identifier=identifier,
        start_date=start_date,
        end_date=end_date,
    )

    rows = normalize_bloomberg_history(
        raw_data=raw_data,
        canonical_ticker=canonical_ticker,
    )

    if not rows:
        raise ValueError(
            f"No Bloomberg data returned for {identifier}"
        )

    return rows
```

This function defines the MarketPulse provider contract.

The exact connection mechanism stays inside the raw acquisition step.

# Part 7 - Preserve the common row model

Every normalized Bloomberg row should conceptually look like:

```python
{
    "date": "YYYY-MM-DD",
    "ticker": "AAPL",
    "open": 0.0,
    "high": 0.0,
    "low": 0.0,
    "close": 0.0,
    "volume": 0,
}
```

The example numbers above are structural placeholders only.

Do not hard-code them in the real implementation.

## Important

If the teaching environment does not provide one field for a given instrument type, document the behaviour.

For example, benchmark volume may be unavailable or not meaningful.

Do not fabricate data only to fill the schema.

The instructor may allow:

- a neutral value;
- a nullable representation;
- a documented provider-specific rule.

Use the convention approved during class.

# Part 8 - Handle the date window

The common business contract remains:

```text
Lookback : 1 month
Interval : Daily
```

Bloomberg may require explicit start and end dates rather than the Yahoo-style value:

```text
1mo
```

The provider may therefore translate the business contract into provider-specific request parameters.

Conceptually:

```text
MarketPulse
lookback = 1 month
interval = daily
        |
        v
Bloomberg provider
        |
        v
start date
end date
daily historical request
```

Provider-specific translation belongs inside or near the provider layer.

# Part 9 - Retrieve the instrument

Use the confirmed Bloomberg identifier:

```text
AAPL US Equity
```

Conceptual call:

```python
instrument_prices = fetch_bloomberg_prices(
    identifier="AAPL US Equity",
    canonical_ticker="AAPL",
    start_date=start_date,
    end_date=end_date,
)
```

Verify:

```text
[ ] response is not empty
[ ] canonical ticker is AAPL
[ ] dates are available
[ ] close values are numeric
[ ] rows follow the canonical structure
```

# Part 10 - Retrieve the benchmark

Use:

```text
SPX Index
```

Conceptual call:

```python
benchmark_prices = fetch_bloomberg_prices(
    identifier="SPX Index",
    canonical_ticker="SP500",
    start_date=start_date,
    end_date=end_date,
)
```

Verify:

```text
[ ] response is not empty
[ ] canonical ticker is SP500
[ ] dates are available
[ ] close values are numeric
[ ] rows follow the canonical structure
```

# Part 11 - Align the Bloomberg series

Reuse the existing alignment functions from TD07 and TD08.

Conceptually:

```python
instrument_by_date = index_by_date(
    instrument_prices
)

benchmark_by_date = index_by_date(
    benchmark_prices
)

common_dates = sorted(
    set(instrument_by_date)
    & set(benchmark_by_date)
)
```

Then build aligned lists.

Do not create a Bloomberg-specific alignment algorithm unless the provider genuinely requires a documented exception.

# Part 12 - Reuse the analytics unchanged

The most important TD10 validation is architectural.

These functions should not care whether rows came from:

```text
CSV
Yahoo
Bloomberg
```

Reuse:

```text
calculate_period_return()
calculate_daily_returns()
calculate_base_100()
calculate_relative_performance()
```

If you are tempted to create:

```text
calculate_bloomberg_period_return()
```

stop and inspect the design.

That would duplicate business logic unnecessarily.

# Part 13 - Provider selection

MarketPulse now has multiple provider paths.

A simple educational selector is enough.

Conceptually:

```python
provider = "bloomberg"

if provider == "csv":
    ...
elif provider == "yahoo":
    ...
elif provider == "bloomberg":
    ...
else:
    raise ValueError(
        f"Unsupported provider: {provider}"
    )
```

The objective is not to build a complex plugin framework.

The objective is to make acquisition selectable while keeping analytics shared.

# Part 14 - Configuration

The CORE repository already contains:

```text
config/settings.yml
```

In the 18-hour CORE, this file is a human-readable configuration contract.

You are not required to parse YAML from Python.

Do not add PyYAML only because this file exists.

The provider value may still be updated for documentation purposes:

```yaml
market:
  provider: bloomberg
  lookback: 1mo
  interval: 1d
```

Provider-specific identifiers may also be documented conceptually:

```yaml
providers:
  yahoo:
    AAPL: AAPL
    SP500: ^GSPC

  bloomberg:
    AAPL: AAPL US Equity
    SP500: SPX Index
```

If your team chooses to wire YAML into Python, treat it as an explicit optional extension.

The required TD10 implementation must not depend on YAML parsing.

Configuration should make the application clearer, not more complicated.

# Part 15 - Display provider information

The terminal output should clearly identify the provider.

Example:

```text
=== MarketPulse ===

Provider
Bloomberg

Market configuration
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Period     : 1 month
Interval   : Daily

Instrument return : ...
Benchmark return  : ...
Relative performance : ...
```

Do not expose credentials or connection details in normal output.

# Part 16 - Provider failure handling

Professional providers can also return errors.

Possible cases include:

- Bloomberg environment unavailable;
- access not authorized;
- invalid identifier;
- empty historical response;
- missing expected field.

TD10 requires only simple, understandable failure handling.

Possible approach:

```python
if not rows:
    raise ValueError(
        f"No Bloomberg data returned for {identifier}"
    )
```

At application level:

```python
try:
    ...
except ValueError as error:
    print(f"Market data error: {error}")
```

Do not hide every exception with:

```python
except Exception:
    pass
```

That makes failures harder to understand.

# Part 17 - Fallback mode

If live Bloomberg access is unavailable during TD10, use only an instructor-approved sample or export.

The architecture should remain:

```text
approved Bloomberg sample
          |
          v
Bloomberg normalization
          |
          v
canonical rows
          |
          v
shared analytics
```

Document clearly:

```text
live provider access
or
approved sample fallback
```

Do not label sample-based execution as live Bloomberg retrieval.

# Part 18 - Validation matrix

Before committing, validate:

| Requirement | CSV | Yahoo | Bloomberg |
|---|---:|---:|---:|
| Canonical instrument ticker | yes | yes | yes |
| Canonical benchmark ticker | yes | yes | yes |
| Daily historical data | yes | yes | yes or approved sample |
| Common row structure | yes | yes | yes |
| Alignment logic reused | yes | yes | yes |
| Period return reused | yes | yes | yes |
| Base-100 logic reused | yes | yes | yes |
| Relative performance reused | yes | yes | yes |

The exact data values will differ across providers and retrieval dates.

The architecture should remain consistent.

# Part 19 - Inspect the diff

Run:

```bash
git status
git diff
```

Expected files may include:

```text
src/main.py
src/providers/bloomberg_provider.py
config/settings.yml
docs/BLOOMBERG_FIELD_MAPPING.md
```

Only include files actually required by your implementation.

Do not change unrelated files.

# Part 20 - Commit and push

Stage the intended files.

Example:

```bash
git add src/main.py
git add src/providers/bloomberg_provider.py
```

Add configuration or mapping files only if they changed.

Inspect:

```bash
git diff --staged
```

Commit:

```bash
git commit -m "feat: add Bloomberg provider"
```

Push:

```bash
git push -u origin feature/bloomberg-provider
```

# Part 21 - Open the Pull Request

Suggested title:

```text
feat: add Bloomberg provider
```

Suggested description:

```markdown
## What changed

- add Bloomberg provider boundary;
- map Bloomberg identifiers to canonical tickers;
- normalize Bloomberg data to MarketPulse rows;
- reuse existing comparison analytics.

## Validation

- verified AAPL Bloomberg path;
- verified SP500 Bloomberg path;
- verified canonical row structure;
- verified common-date alignment;
- verified period return and base-100 reuse.

## Environment

- Bloomberg access mode: <live or approved sample>
```

Be accurate about the environment used.

# Part 22 - Review points

The reviewer should verify:

```text
[ ] Bloomberg identifiers match the TD09 mapping
[ ] no credentials are committed
[ ] provider-specific code stays in provider layer
[ ] canonical tickers remain AAPL and SP500
[ ] normalized rows follow the common structure
[ ] analytics are reused
[ ] no Bloomberg-specific return formula exists
[ ] provider mode is documented accurately
[ ] MarketPulse still runs
```

Merge only after review.

# Part 23 - Relationship with Checkpoint C

Checkpoint C is performed after TD12.

One required screenshot will be:

```text
01_final_market_data.png
```

When Bloomberg is available, the final provider evidence should show Bloomberg in operation.

The generic filename is intentional because the teaching team may authorize another final provider if Bloomberg access is unavailable for technical or organizational reasons.

Do not create false evidence.

# Part 24 - Mini exercises

## Exercise 1 - Trace provider-specific code

Identify every location in the project that contains:

```text
AAPL US Equity
SPX Index
```

Question:

> Should those values appear inside analytical functions?

## Exercise 2 - Compare normalized rows

Print one normalized row from:

```text
CSV
Yahoo
Bloomberg
```

Compare the keys.

## Exercise 3 - Switch provider

Change the provider selection from Yahoo to Bloomberg.

Verify that analytical function names do not change.

## Exercise 4 - Invalid Bloomberg identifier

Using a safe instructor-approved test, observe what happens when the provider cannot retrieve an identifier.

Explain where the failure is handled.

# Part 25 - If you finish early

## Challenge 1 - Extract provider selection

Move provider selection into a small dedicated function.

Conceptual example:

```python
def load_market_data(provider, ...):
    ...
```

Keep it simple.

## Challenge 2 - Reduce duplication

Compare Yahoo and Bloomberg acquisition paths.

Identify code that is truly shared and code that is provider-specific.

Do not force two provider APIs into identical internal code if their access mechanisms differ.

## Challenge 3 - Provider metadata

Return or display a small metadata structure such as:

```python
{
    "provider": "bloomberg",
    "instrument_source": "AAPL US Equity",
    "benchmark_source": "SPX Index",
}
```

Do not expose credentials.

## Challenge 4 - Architecture diagram

Update an ASCII diagram:

```text
CSV -----------+
               |
Yahoo ---------+--> canonical rows --> analytics
               |
Bloomberg -----+
```

Explain the provider boundary to another student.

# Part 26 - Troubleshooting

## Bloomberg access fails

Verify the instructor-approved environment first.

Do not change the architecture randomly before confirming whether the issue is:

- access;
- identifier;
- field mapping;
- code.

## Provider returns data but normalization fails

Inspect:

```text
raw response
observed field names
date structure
numeric types
```

Compare them with:

```text
docs/BLOOMBERG_FIELD_MAPPING.md
```

## Canonical ticker is wrong

Remember:

```text
AAPL US Equity -> AAPL
SPX Index      -> SP500
```

The provider identifier is not the canonical application ticker.

## Analytics differ between providers

Different providers may return slightly different data histories or adjustments.

First verify:

```text
date range
interval
common dates
close field
adjustment convention
```

Do not assume that differing values automatically mean the formula is wrong.

## Credentials appear in output

Stop.

Remove the sensitive output from code and screenshots.

Notify the instructor if sensitive data was committed.

# Part 27 - Readiness check

Before finishing TD10, each student should be able to explain:

```text
[ ] Bloomberg provider boundary
[ ] raw acquisition vs normalization
[ ] canonical ticker vs Bloomberg identifier
[ ] why analytics stay provider-independent
[ ] how the 1-month daily contract is translated
[ ] how Bloomberg failures are surfaced
[ ] live access vs approved sample fallback
[ ] why provider selection should not duplicate analytics
```

Each student should also confirm:

```text
[ ] I used a feature branch
[ ] I created identifiable commits
[ ] I pushed the branch
[ ] I used a Pull Request
[ ] another student reviewed the change
[ ] no credentials were committed
[ ] Bloomberg rows use canonical tickers
[ ] existing analytics were reused
[ ] MarketPulse still runs
```

# Part 28 - What comes next?

MarketPulse now has the intended provider progression:

```text
CSV
Yahoo
Bloomberg
   |
   v
canonical market data
   |
   v
shared comparison logic
```

The next business requirement is:

```text
"Traders want a visual interface instead of terminal output."
```

In TD11, the analytical results will be exposed through Dash.

The main visual objective will be:

```text
Instrument vs Benchmark
Base 100
```

with clear summary indicators for period and relative performance.
