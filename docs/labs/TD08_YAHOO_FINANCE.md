# TD08 - Yahoo Finance

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"Traders need more recent market data than local files."
```

## Context

Until now, MarketPulse has worked with local CSV and JSON files.

TD07 introduced a comparison model based on:

```text
instrument
+
benchmark
+
same lookback
+
same interval
+
aligned observations
+
performance comparison
```

The next objective is to change the data source without rewriting the analytical logic.

MarketPulse will now retrieve daily market data through the Python package:

```text
yfinance
```

Important:

```text
yfinance is a community Python library.
It is not the official Yahoo Finance API.
```

The package is used here as an accessible pedagogical bridge before Bloomberg.

## Learning objectives

At the end of TD08, you should be able to:

- install and record a Python dependency;
- retrieve remote market data with `yfinance`;
- distinguish a business ticker from a provider-specific symbol;
- use a 1-month lookback and daily interval;
- convert provider output to the MarketPulse canonical row structure;
- feed the existing comparison logic with Yahoo Finance data;
- handle a basic remote-data failure;
- explain why provider acquisition should remain separate from analytics;
- complete the established branch, PR and review workflow.

## Expected result

MarketPulse should be able to use:

```text
Provider   : Yahoo Finance
Instrument : AAPL
Benchmark  : S&P 500
Yahoo      : AAPL + ^GSPC
Lookback   : 1 month
Interval   : Daily
```

and produce a comparison summary using remote data.

Example shape:

```text
=== MarketPulse ===

Provider
Yahoo Finance

Market configuration
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Period     : 1 month
Interval   : Daily

Instrument return : ...
Benchmark return  : ...

Relative performance
AAPL vs SP500 : ... percentage points
```

The exact observations and values depend on the retrieval date.

Do not hard-code expected market prices.

## Prerequisites

Before starting:

```text
[ ] TD01-TD07 completed
[ ] team main is up to date
[ ] MarketPulse comparison works with CSV
[ ] period return works
[ ] base-100 calculation works
[ ] branch / PR / review workflow is understood
[ ] internet access is available
```

Update local main:

```bash
git switch main
git pull
git status
```

Run the current application:

```bash
python src/main.py
```

Start from a clean working tree.

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | Provider concept and Yahoo symbols |
| 10-22 min | Install and record yfinance |
| 22-38 min | Retrieve first remote series |
| 38-55 min | Normalize Yahoo data |
| 55-68 min | Retrieve instrument and benchmark |
| 68-78 min | Reuse comparison logic |
| 78-90 min | Validate, PR, review and Checkpoint B |

# Part 1 - Understand the provider problem

The business concept should remain stable even when the provider changes.

For MarketPulse:

```text
Business instrument
AAPL
    |
    +-- CSV symbol    : AAPL
    +-- Yahoo symbol  : AAPL
    +-- Bloomberg     : later
```

For the benchmark:

```text
Business benchmark
S&P 500
    |
    +-- CSV symbol    : SP500
    +-- Yahoo symbol  : ^GSPC
    +-- Bloomberg     : later
```

Provider-specific identifiers are not always identical.

## Question

> Why should MarketPulse avoid treating `^GSPC` as the universal business identifier for the S&P 500?

Because `^GSPC` belongs to one provider convention.

The application should preserve the business concept:

```text
S&P 500
```

while adapters translate it to provider-specific identifiers.

# Part 2 - Create the feature branch

Create a branch:

```bash
git switch main
git pull
git switch -c feature/yahoo-provider
```

Verify:

```bash
git branch
git status
```

All TD08 work should remain on this feature branch until review and merge.

# Part 3 - Install yfinance

Check whether the package is already installed:

```bash
python -m pip show yfinance
```

If it is not installed:

```bash
python -m pip install yfinance
```

Verify:

```bash
python -m pip show yfinance
```

## 3.1 Record the dependency

Update:

```text
requirements.txt
```

Add:

```text
yfinance
```

Do not add every transitive package manually.

The direct dependency for this TD is `yfinance`.

## 3.2 Why record dependencies?

A local installation is not enough.

Another student should be able to prepare the project with:

```bash
python -m pip install -r requirements.txt
```

This becomes increasingly important before the final reproducibility check.

# Part 4 - Retrieve one remote series

Start with the primary instrument only.

Create a small experiment in Python.

Example:

```python
import yfinance as yf

ticker = yf.Ticker("AAPL")

history = ticker.history(
    period="1mo",
    interval="1d",
    auto_adjust=False,
)

print(history.head())
print(history.tail())
```

Run the experiment.

## Questions

1. Is the result empty?
2. Which columns are available?
3. What type of object is returned?
4. Are the column names the same as the MarketPulse CSV schema?
5. Where are the dates stored?

## Important

`yfinance` returns a table-like structure backed by pandas.

TD08 is not a full pandas course.

You only need enough interaction with the returned table to convert it into the existing MarketPulse data contract.

# Part 5 - Understand the schema mismatch

MarketPulse expects rows such as:

```python
{
    "date": "2026-09-01",
    "ticker": "AAPL",
    "open": 249.20,
    "high": 251.50,
    "low": 248.00,
    "close": 250.00,
    "volume": 38000000,
}
```

Yahoo data uses provider-oriented column names such as:

```text
Open
High
Low
Close
Volume
```

The provider adapter must translate from:

```text
Yahoo schema
      |
      v
MarketPulse canonical schema
```

This is normalization at the provider boundary.

# Part 6 - Create the Yahoo provider module

TD08 extends the frozen CORE structure:

```text
src/
├── main.py
├── analytics.py
└── providers/
    ├── __init__.py
    └── yahoo_provider.py
```

Create:

```text
src/providers/__init__.py
src/providers/yahoo_provider.py
```

Keep shared comparison logic in `src/analytics.py`.

A possible starter implementation is:

```python
import yfinance as yf


def fetch_yahoo_prices(
    symbol,
    canonical_ticker,
    period="1mo",
    interval="1d",
):
    history = yf.Ticker(symbol).history(
        period=period,
        interval=interval,
        auto_adjust=False,
    )

    if history.empty:
        raise ValueError(
            f"No Yahoo Finance data returned for {symbol}"
        )

    rows = []

    for timestamp, row in history.iterrows():
        rows.append({
            "date": timestamp.strftime("%Y-%m-%d"),
            "ticker": canonical_ticker,
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        })

    return rows
```

This is a pedagogical implementation.

The important contract is the returned structure, not the exact internal syntax.

## 6.1 Why two identifiers?

The function accepts:

```text
symbol
canonical_ticker
```

Example:

```python
fetch_yahoo_prices(
    symbol="^GSPC",
    canonical_ticker="SP500",
)
```

Yahoo receives:

```text
^GSPC
```

while the rest of MarketPulse continues to know the benchmark as:

```text
SP500
```

# Part 7 - Configure provider symbols

For TD08, a simple mapping is sufficient.

Example:

```python
YAHOO_SYMBOLS = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}
```

The mapping may temporarily live near the acquisition configuration.

Do not scatter provider symbols throughout analytical functions.

The analytical layer should not contain:

```text
^GSPC
```

unless it is explicitly dealing with the Yahoo provider.

# Part 8 - Retrieve both market series

Import the provider function into the application.

Example:

```python
from providers.yahoo_provider import fetch_yahoo_prices
```

Then retrieve:

```python
instrument_prices = fetch_yahoo_prices(
    symbol="AAPL",
    canonical_ticker="AAPL",
    period="1mo",
    interval="1d",
)

benchmark_prices = fetch_yahoo_prices(
    symbol="^GSPC",
    canonical_ticker="SP500",
    period="1mo",
    interval="1d",
)
```

Do not duplicate the Yahoo retrieval implementation for instrument and benchmark.

# Part 9 - Validate the canonical structure

Inspect one row:

```python
print(instrument_prices[0])
print(benchmark_prices[0])
```

Verify that both contain:

```text
date
ticker
open
high
low
close
volume
```

Verify types:

```python
print(type(instrument_prices[0]["close"]))
print(type(instrument_prices[0]["volume"]))
```

Expected:

```text
float
int
```

The exact number of rows may differ from the static CSV sample because the remote one-month window depends on trading days and retrieval date.

# Part 10 - Reuse TD07 analytics

This is the architectural test.

Your TD07 analytical functions should work with the Yahoo rows without being rewritten specifically for Yahoo.

Conceptually:

```text
CSV provider
     |
     +------+
            |
Yahoo provider
     |      |
     +------+
        |
        v
canonical rows
        |
        v
alignment
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

If your analysis functions need to know whether the source is CSV or Yahoo, inspect your design.

Provider details should remain near acquisition.

# Part 11 - Align remote observations

Yahoo may return dates that differ from the static teaching CSV.

Build or reuse the TD07 alignment logic.

Example:

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

Verify:

```python
print(len(common_dates))
print(common_dates[0])
print(common_dates[-1])
```

Do not assume that the two raw series always have exactly the same number of rows.

Use common dates for direct comparison.

# Part 12 - Build aligned lists

Create aligned instrument and benchmark lists from the common dates.

Example:

```python
aligned_instrument = [
    instrument_by_date[date]
    for date in common_dates
]

aligned_benchmark = [
    benchmark_by_date[date]
    for date in common_dates
]
```

Then reuse the TD07 functions.

For example:

```python
instrument_return = calculate_period_return(
    aligned_instrument
)

benchmark_return = calculate_period_return(
    aligned_benchmark
)
```

# Part 13 - Display provider information

The user should be able to understand the data source.

Add a clear provider label.

Example:

```text
Provider
Yahoo Finance
```

Do not present `yfinance` as an official Yahoo API.

A precise description is:

```text
Yahoo Finance data accessed through the yfinance Python package.
```

# Part 14 - Validate the business contract

Before committing, verify:

```text
[ ] provider is Yahoo Finance
[ ] instrument business ticker remains AAPL
[ ] benchmark business ticker remains SP500
[ ] Yahoo benchmark symbol is ^GSPC
[ ] lookback is 1 month
[ ] interval is daily
[ ] instrument data is not empty
[ ] benchmark data is not empty
[ ] common dates exist
[ ] period returns are calculated
[ ] relative performance is calculated
[ ] base-100 comparison can be produced
```

Run:

```bash
python src/main.py
```

# Part 15 - Handle a simple provider failure

Remote services can fail.

Possible causes include:

- no internet connection;
- provider temporarily unavailable;
- invalid symbol;
- empty response.

The application should not fail with a mysterious error if the provider returns no data.

The provider function already includes:

```python
if history.empty:
    raise ValueError(
        f"No Yahoo Finance data returned for {symbol}"
    )
```

At application level, a simple TD08 approach is enough.

Example:

```python
try:
    ...
except ValueError as error:
    print(f"Market data error: {error}")
```

Do not build a complex retry framework in TD08.

# Part 16 - Invalid symbol exercise

Try a clearly invalid symbol in a temporary experiment.

Example:

```text
THIS_SYMBOL_SHOULD_NOT_EXIST_123
```

Observe the result.

Then restore the correct configuration.

Question:

> Why is an empty provider response different from an empty local CSV file?

Discuss where each failure originates.

# Part 17 - Git workflow

Inspect:

```bash
git status
git diff
```

Expected changed files may include:

```text
requirements.txt
src/main.py
src/providers/__init__.py
src/providers/yahoo_provider.py
```

Do not include unrelated files.

Stage the intended files.

Example:

```bash
git add requirements.txt
git add src/main.py
git add src/providers/__init__.py
git add src/providers/yahoo_provider.py
```

Inspect:

```bash
git diff --staged
```

Commit:

```bash
git commit -m "feat: add Yahoo Finance provider"
```

Push:

```bash
git push -u origin feature/yahoo-provider
```

# Part 18 - Open the Pull Request

Suggested title:

```text
feat: add Yahoo Finance provider
```

Suggested description:

```markdown
## What changed

- add yfinance dependency;
- add Yahoo Finance acquisition module;
- map Yahoo symbols to MarketPulse tickers;
- normalize Yahoo data to the canonical row structure;
- reuse existing instrument vs benchmark comparison.

## Validation

- retrieved AAPL data for 1 month at daily interval;
- retrieved ^GSPC data for 1 month at daily interval;
- aligned common dates;
- ran MarketPulse successfully;
- verified period and relative performance output.
```

Another team member reviews the Pull Request before merge.

# Part 19 - Review points

The reviewer should verify:

```text
[ ] yfinance is recorded in requirements.txt
[ ] provider code is separate from analytical calculations
[ ] AAPL uses Yahoo symbol AAPL
[ ] S&P 500 uses Yahoo symbol ^GSPC
[ ] canonical ticker remains SP500
[ ] period is 1 month
[ ] interval is daily
[ ] returned rows use canonical field names
[ ] comparison functions are reused
[ ] no market values are hard-coded
[ ] no unrelated files are included
```

# Part 20 - Checkpoint B

Checkpoint B is performed after TD08.

It closes Checkpoint Phase B:

```text
Checkpoint Phase B - TD05-TD08

TD05 - Fork + Pull Request
TD06 - Code Review
TD07 - Data Normalization + Comparison
TD08 - Yahoo Finance
        |
        v
Checkpoint B
```

TD08 also closes pedagogical Wave 3, which covers TD07-TD08.

## 20.1 Evidence directory

Each student uses:

```text
evidence/checkpoint-b/<github-username>/
```

## 20.2 Required files

Exactly these files are required:

```text
README.md
01_pull_request.png
02_code_review.png
03_yahoo_market_data.png
04_instrument_benchmark.png
```

Do not rename them.

## 20.3 01_pull_request.png

Show:

- PR title;
- author;
- source branch;
- target branch;
- relevant status.

The Pull Request must correspond to identifiable work by the student.

## 20.4 02_code_review.png

Show a meaningful review performed by the student on another team member's Pull Request.

A reaction alone is not sufficient.

## 20.5 03_yahoo_market_data.png

Show MarketPulse retrieving or displaying remote Yahoo Finance market data.

The screenshot should make the provider and market series understandable.

Do not use a screenshot of static CSV output as Yahoo evidence.

## 20.6 04_instrument_benchmark.png

Show that MarketPulse handles both:

```text
Instrument
+
Benchmark
```

under the common contract:

```text
Lookback : 1 month
Interval : Daily
```

The output should make the selected instrument and benchmark identifiable.

# Part 21 - Checkpoint B README

Create:

```text
evidence/checkpoint-b/<github-username>/README.md
```

Suggested structure:

```markdown
# Checkpoint B

## Student

- Name: Alice Martin
- GitHub: @alice-martin

## Contribution

- Branch: feature/yahoo-provider
- Main commits:
  - <commit-id>
- Pull Request: #...
- Reviewed Pull Request: #...

## Work completed

Briefly describe your contribution.

## Main difficulty

Briefly explain one technical or collaborative difficulty.

## Evidence

- 01_pull_request.png
- 02_code_review.png
- 03_yahoo_market_data.png
- 04_instrument_benchmark.png
```

# Part 22 - Checkpoint B live validation

The instructor may ask you to:

```text
change the selected Yahoo symbol
run MarketPulse
explain where Yahoo is called
show the canonical row structure
show the benchmark mapping
explain the common-date alignment
show your Pull Request
show a review you performed
```

You should be able to modify and run the project without relying only on screenshots.

# Part 23 - If Yahoo Finance is temporarily unavailable

Remote services are outside the repository's control.

If Yahoo Finance is unavailable during the lab:

1. verify your internet connection;
2. verify the symbol;
3. retry once after checking the code;
4. keep the provider implementation;
5. use the local CSV path to continue architectural work;
6. report the outage to the instructor.

Do not fabricate Yahoo Finance evidence.

Checkpoint B Yahoo evidence should be captured after a successful remote retrieval.

If an external outage prevents this during the scheduled session, the instructor decides the recovery procedure.

# Part 24 - Mini exercises

## Exercise 1 - Change instrument

Temporarily retrieve another widely traded instrument.

Example:

```text
MSFT
```

Do not change the permanent team market pair unless instructed.

Verify that the provider function remains reusable.

## Exercise 2 - Inspect provider symbols

Explain why:

```text
SP500
```

and:

```text
^GSPC
```

represent related concepts but serve different roles.

## Exercise 3 - Compare row contracts

Print one CSV-normalized row and one Yahoo-normalized row.

Verify that both have the same keys.

## Exercise 4 - Compare observation counts

Display:

```text
raw instrument observations
raw benchmark observations
common aligned observations
```

Explain why these numbers may differ.

# Part 25 - If you finish early

## Challenge 1 - Provider selection

Introduce a simple provider setting:

```text
csv
or
yahoo
```

Then choose the acquisition path without changing analytical functions.

Keep the implementation small.

## Challenge 2 - Extract symbol mapping

Move the Yahoo symbol mapping into a clearer configuration structure.

Do not introduce secrets or unnecessary frameworks.

## Challenge 3 - Print retrieval window

Display the first and last common dates returned by Yahoo.

## Challenge 4 - Compare CSV and Yahoo architecture

Draw:

```text
CSV
 |
 v
canonical rows

Yahoo
 |
 v
canonical rows
```

Then explain why both can feed the same calculations.

# Part 26 - Troubleshooting

## ModuleNotFoundError: yfinance

Run:

```bash
python -m pip install -r requirements.txt
```

or verify:

```bash
python -m pip show yfinance
```

## Empty Yahoo response

Check:

- internet access;
- symbol spelling;
- period;
- interval.

Test the instrument and benchmark independently.

## Import error for providers

Check the structure:

```text
src/
├── main.py
└── providers/
    ├── __init__.py
    └── yahoo_provider.py
```

Run the application from the repository root:

```bash
python src/main.py
```

## KeyError on Yahoo columns

Inspect:

```python
print(history.columns)
```

Verify the actual provider output before assuming a column name.

## Dates do not align

Inspect the date sets and use common dates.

Do not compare rows only by list position if dates differ.

## Benchmark volume looks unusual

Index volume may differ from equity volume and may be zero or provider-dependent.

Volume is not required for the benchmark-performance calculation.

# Part 27 - Readiness check

Before finishing TD08, each student should be able to explain:

```text
[ ] what yfinance is
[ ] why it is not described as the official Yahoo API
[ ] provider-specific symbol vs canonical ticker
[ ] why SP500 maps to ^GSPC for Yahoo
[ ] why Yahoo data must be normalized
[ ] why common dates matter
[ ] why analytics should not depend on the provider
[ ] how requirements.txt improves reproducibility
[ ] what to do when a remote provider returns no data
```

Each student should also confirm:

```text
[ ] I used a feature branch
[ ] I created identifiable commits
[ ] I pushed the branch
[ ] I used a Pull Request
[ ] another student reviewed work
[ ] Yahoo data was retrieved successfully
[ ] instrument and benchmark comparison works
[ ] Checkpoint B evidence uses the official filenames
```

# Part 28 - What comes next?

Pedagogical Wave 3 and Checkpoint Phase B are now complete:

```text
Wave 3 - Comparison + Yahoo Finance - 3 hours

TD07 - Data Normalization + Comparison
TD08 - Yahoo Finance

Checkpoint Phase B - TD05-TD08
        |
        v
Checkpoint B
```

The next business requirement is:

```text
"The trading desk now has access to a professional market-data environment."
```

In TD09, MarketPulse will begin the Bloomberg stage.

The key idea remains unchanged:

```text
new provider
      |
      v
canonical market data
      |
      v
existing comparison logic
```
