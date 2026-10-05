# TD07 - Data Normalization + Comparison

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"All market-data sources must feed a common comparison model."
```

## Context

The collaborative Git workflow is now established.

From TD05 and TD06 onward, new MarketPulse features should follow:

```text
feature branch
      |
      v
commit
      |
      v
push
      |
      v
Pull Request
      |
      v
review
      |
      v
merge
```

The next problem is functional.

MarketPulse currently handles:

```text
AAPL
+
S&P 500
```

but a raw stock price and an index level are not directly comparable.

Example:

```text
AAPL      about 250 USD
S&P 500   about 6600 points
```

The absolute values are on different scales.

To answer the business question:

> Is the selected instrument outperforming or underperforming its benchmark over the selected period?

MarketPulse needs a common comparison model.

## Learning objectives

At the end of TD07, you should be able to:

- distinguish raw provider data from comparison-ready data;
- convert market-data fields to useful Python types;
- preserve a common row structure;
- align instrument and benchmark observations by date;
- calculate a period return;
- calculate simple daily returns;
- calculate a base-100 performance series;
- calculate relative performance;
- explain why price levels cannot always be compared directly;
- implement the feature using the established GitHub workflow.

## Expected result

At the end of TD07, MarketPulse should be able to produce a comparison summary such as:

```text
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Period return : 6.48%

Benchmark
SP500 - S&P 500
Period return : 2.15%

Relative performance
AAPL vs SP500 : +4.33 percentage points

Base 100
AAPL  : 100.00 -> 106.48
SP500 : 100.00 -> 102.15
```

The exact percentages depend on the data used.

## Scope

TD07 introduces only simple analytical concepts.

Required:

```text
period return
daily return
base 100
relative performance
```

Not required:

```text
Sharpe ratio
beta
CAPM
alpha
VaR
RSI
MACD
Bollinger Bands
portfolio optimization
```

Do not add advanced quantitative-finance indicators.

## Prerequisites

Before starting:

```text
[ ] TD01-TD06 completed
[ ] MarketPulse runs
[ ] instrument and benchmark are loaded
[ ] branches understood
[ ] Pull Requests understood
[ ] code review understood
[ ] team main is up to date
```

Update local main:

```bash
git switch main
git pull
git status
```

Run:

```bash
python src/main.py
```

Start from a clean working tree.

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | Why raw prices are not enough |
| 10-25 min | Normalize row types |
| 25-40 min | Align instrument and benchmark |
| 40-55 min | Calculate period returns |
| 55-68 min | Build base-100 series |
| 68-78 min | Calculate relative performance |
| 78-90 min | Validate, push and open PR |

# Part 1 - Understand the comparison problem

The current sample contains two series:

```text
AAPL
SP500
```

Their raw levels are different.

AAPL may be near:

```text
250
```

while the S&P 500 may be near:

```text
6600
```

A direct chart of raw values can be misleading when the business question is about relative performance.

## 1.1 Price level vs performance

Price level answers:

```text
"What is the current value?"
```

Performance answers:

```text
"How much did the value change over the period?"
```

MarketPulse needs both concepts.

## 1.2 Common period and frequency

The comparison is valid only if both series use a common contract:

```text
same lookback
+
same interval
+
compatible observation dates
```

For the common course path:

```text
Lookback : 1 month
Interval : Daily
```

Question:

> Why would comparing one month of AAPL with one week of S&P 500 be incoherent?

# Part 2 - Create the feature branch

Create a branch for the comparison work:

```bash
git switch main
git pull
git switch -c feature/market-comparison
```

Verify:

```bash
git branch
git status
```

The work from this TD should follow the complete collaborative workflow.

# Part 3 - Normalize market-data rows

The CSV reader initially returns text values.

A row may look conceptually like:

```python
{
    "date": "2026-09-01",
    "ticker": "AAPL",
    "open": "249.20",
    "high": "251.50",
    "low": "248.00",
    "close": "250.00",
    "volume": "38000000",
}
```

For calculations, numeric fields should be numeric.

## 3.1 Common row contract

Use the following common fields:

```text
date
ticker
open
high
low
close
volume
```

This is the MarketPulse canonical row structure for the common course path.

## 3.2 Create a normalization function

Suggested function:

```python
def normalize_price_row(row):
    return {
        "date": row["date"],
        "ticker": row["ticker"],
        "open": float(row["open"]),
        "high": float(row["high"]),
        "low": float(row["low"]),
        "close": float(row["close"]),
        "volume": int(row["volume"]),
    }
```

Then apply it when loading or preparing prices.

Possible approach:

```python
normalized_prices = [
    normalize_price_row(row)
    for row in prices
]
```

The exact organization is your responsibility.

## 3.3 Validate the types

Temporarily inspect:

```python
print(type(normalized_prices[0]["close"]))
print(type(normalized_prices[0]["volume"]))
```

Expected:

```text
float
int
```

Remove temporary debug output afterward.

# Part 4 - Align instrument and benchmark observations

Two series must be comparable on common dates.

The current sample is already designed with matching dates.

Still, MarketPulse should make the alignment explicit.

## 4.1 Build a date index

One simple approach is to build dictionaries indexed by date.

Example:

```python
def index_by_date(prices):
    return {
        row["date"]: row
        for row in prices
    }
```

Then:

```python
instrument_by_date = index_by_date(instrument_prices)
benchmark_by_date = index_by_date(benchmark_prices)
```

## 4.2 Find common dates

Use set intersection:

```python
common_dates = sorted(
    set(instrument_by_date)
    & set(benchmark_by_date)
)
```

Questions:

1. What does `set(instrument_by_date)` contain?
2. What does the `&` operator do here?
3. Why is `sorted()` useful?

## 4.3 Verify the alignment

Display:

```python
print(len(common_dates))
print(common_dates[0])
print(common_dates[-1])
```

With the starter dataset, you should currently obtain:

```text
21
2026-09-01
2026-09-30
```

# Part 5 - Calculate period return

The simple period-return formula is:

```text
(last price / first price - 1) * 100
```

## 5.1 Implement the function

Suggested function:

```python
def calculate_period_return(prices):
    first_close = prices[0]["close"]
    last_close = prices[-1]["close"]

    return (last_close / first_close - 1) * 100
```

This assumes:

- prices are not empty;
- prices are ordered chronologically;
- close values are numeric.

## 5.2 Calculate both returns

Example:

```python
instrument_return = calculate_period_return(
    instrument_prices
)

benchmark_return = calculate_period_return(
    benchmark_prices
)
```

Format with two decimal places:

```python
print(f"{instrument_return:.2f}%")
```

## 5.3 Interpret the result

Do not only calculate.

Explain in words:

```text
positive return
=
ending value above starting value

negative return
=
ending value below starting value
```

# Part 6 - Calculate relative performance

Relative performance compares the two period returns.

Formula:

```text
instrument return
-
benchmark return
```

Suggested function:

```python
def calculate_relative_performance(
    instrument_return,
    benchmark_return,
):
    return instrument_return - benchmark_return
```

Example interpretation:

```text
Instrument return : +6.48%
Benchmark return  : +2.15%

Relative performance
=
+4.33 percentage points
```

Important vocabulary:

```text
percentage points
```

not:

```text
percent
```

for the simple difference between two percentage returns.

## Question

> If AAPL returns +4% and the benchmark returns +6%, is relative performance positive or negative?

# Part 7 - Build a base-100 series

Base 100 solves the scale problem.

Both series start at:

```text
100
```

Formula:

```text
base_100
=
current_close / first_close * 100
```

## 7.1 Implement the function

Suggested implementation:

```python
def calculate_base_100(prices):
    first_close = prices[0]["close"]
    result = []

    for row in prices:
        result.append({
            "date": row["date"],
            "ticker": row["ticker"],
            "value": row["close"] / first_close * 100,
        })

    return result
```

This produces a new derived series without changing the original close values.

## 7.2 Verify the first point

For both series, the first value should be:

```text
100.00
```

Question:

> Why must the first value equal 100?

## 7.3 Verify the last point

The last base-100 value should reflect the period performance.

For example:

```text
period return = +6.48%

final base 100
about
106.48
```

This relationship is useful for checking your calculations.

# Part 8 - Calculate daily returns

Daily return compares one close with the previous close.

Formula:

```text
(current close / previous close - 1) * 100
```

Suggested function:

```python
def calculate_daily_returns(prices):
    returns = []

    for index in range(1, len(prices)):
        previous = prices[index - 1]
        current = prices[index]

        value = (
            current["close"] / previous["close"] - 1
        ) * 100

        returns.append({
            "date": current["date"],
            "ticker": current["ticker"],
            "return": value,
        })

    return returns
```

## Important observation

If the price series has:

```text
21 observations
```

the daily-return series has:

```text
20 returns
```

Question:

> Why is one observation lost?

# Part 9 - Keep acquisition and analysis separate

Do not place every calculation directly inside `load_prices()`.

A useful conceptual separation is:

```text
load data
    |
    v
normalize data
    |
    v
filter instrument and benchmark
    |
    v
align observations
    |
    v
calculate analytics
    |
    v
display result
```

This separation becomes important in TD08 when CSV data is no longer the only provider.

# Part 10 - Display the comparison summary

Update MarketPulse so it displays a concise comparison.

Target shape:

```text
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Period return : 6.48%

Benchmark
SP500 - S&P 500
Period return : 2.15%

Relative performance
AAPL vs SP500 : +4.33 percentage points

Base 100
AAPL  : 100.00 -> 106.48
SP500 : 100.00 -> 102.15
```

Use your calculated values.

Do not hard-code the percentages.

# Part 11 - Validation checks

Before committing, verify:

```text
[ ] prices are numeric after normalization
[ ] AAPL observations are ordered
[ ] SP500 observations are ordered
[ ] common dates are identified
[ ] period returns are calculated
[ ] relative performance is calculated
[ ] first base-100 value is 100
[ ] daily-return series has one fewer row
[ ] MarketPulse still runs
```

Run:

```bash
python src/main.py
```

Then inspect Git:

```bash
git status
git diff
```

# Part 12 - Commit the feature

Stage only intended files.

Example:

```bash
git add src/main.py
```

Inspect:

```bash
git diff --staged
```

Commit with a meaningful message.

Example:

```bash
git commit -m "feat: add instrument benchmark comparison"
```

Push:

```bash
git push -u origin feature/market-comparison
```

# Part 13 - Open the Pull Request

Open a Pull Request toward:

```text
team main
```

Suggested title:

```text
feat: add instrument benchmark comparison
```

Suggested description structure:

```markdown
## What changed

- normalize numeric market-data fields;
- align instrument and benchmark observations;
- calculate period returns;
- calculate relative performance;
- calculate base-100 series.

## Validation

- ran `python src/main.py`;
- verified 21 aligned observations;
- verified first base-100 values equal 100;
- verified instrument and benchmark use the same period.
```

A team member should review the Pull Request before merge.

# Part 14 - Review points for TD07

The reviewer should verify at least:

```text
[ ] no hard-coded return percentages
[ ] both series use the same period
[ ] numeric conversion is explicit
[ ] base-100 starts at 100
[ ] relative performance uses instrument minus benchmark
[ ] no unrelated feature is included
[ ] MarketPulse still runs
```

# Part 15 - Relationship with Checkpoint B

Checkpoint B is performed after TD08.

One required screenshot is:

```text
04_instrument_benchmark.png
```

That screenshot should later show that MarketPulse handles:

```text
Instrument
+
Benchmark
+
same lookback
+
same interval
```

The TD07 comparison output prepares that evidence.

Do not submit Checkpoint B yet.

# Part 16 - Mini exercises

## Exercise 1 - Verify the formula manually

Take the first and last AAPL closes.

Calculate manually:

```text
(last / first - 1) * 100
```

Compare your result with Python.

## Exercise 2 - Negative relative performance

Imagine:

```text
Instrument : +2%
Benchmark  : +5%
```

Calculate relative performance.

Explain the result in words.

## Exercise 3 - Missing date thought experiment

Imagine AAPL contains:

```text
2026-09-01
2026-09-02
2026-09-03
```

and the benchmark contains:

```text
2026-09-01
2026-09-03
```

Question:

> Which dates should be used for a direct aligned comparison?

## Exercise 4 - Preserve raw data

Check that your base-100 calculation does not overwrite the original `close` values.

Explain why derived data should not silently destroy source data.

# Part 17 - If you finish early

## Challenge 1 - Display best daily return

For the instrument daily-return series, identify the maximum return.

Do not use pandas.

## Challenge 2 - Display worst daily return

Identify the minimum daily return.

## Challenge 3 - Build aligned comparison rows

Create a structure such as:

```python
{
    "date": "...",
    "instrument_close": ...,
    "benchmark_close": ...,
}
```

for every common date.

## Challenge 4 - Add a simple table

Display the first five base-100 comparison rows:

```text
date        AAPL      SP500
2026-...   100.00    100.00
...
```

Keep the output readable.

# Part 18 - Troubleshooting

## TypeError during calculations

Check the type:

```python
print(type(row["close"]))
```

CSV values may still be strings if normalization was not applied.

## Division problem

Check:

```text
first close
current close
```

The first close must be a valid non-zero numeric value.

## Wrong number of common dates

Inspect:

```python
print(sorted(instrument_by_date))
print(sorted(benchmark_by_date))
```

Compare the date sets.

## Base 100 does not start at 100

Verify the formula:

```text
current close / first close * 100
```

For the first observation:

```text
first close / first close * 100
=
100
```

## Relative performance sign is wrong

Use:

```text
instrument return
-
benchmark return
```

not the reverse.

# Part 19 - Readiness check

Before finishing TD07, each student should be able to explain:

```text
[ ] why raw price levels are not enough
[ ] why instrument and benchmark need common dates
[ ] why CSV numeric fields need conversion
[ ] period return formula
[ ] daily return formula
[ ] base-100 formula
[ ] relative performance formula
[ ] percentage points vocabulary
[ ] why analysis should stay separate from acquisition
```

Each student should also confirm:

```text
[ ] I worked on a feature branch
[ ] I created an identifiable commit
[ ] I pushed the branch
[ ] I opened or contributed to a Pull Request
[ ] another student reviewed the change
[ ] MarketPulse still runs
```

# Part 20 - What comes next?

The local CSV file now feeds a real comparison model.

The next business requirement is:

```text
"Traders need more recent market data than local files."
```

In TD08, MarketPulse will introduce Yahoo Finance.

The key architectural question becomes:

```text
Can a new data provider feed
the same comparison logic
without rewriting the analysis?
```

TD08 will therefore connect remote market data to the model built in TD07.
