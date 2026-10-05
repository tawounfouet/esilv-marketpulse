# TD02 - Python + CSV / JSON

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"The trading desk still sends local CSV and JSON market files."
```

## Context

In TD01, your team learned how to access, inspect and run MarketPulse from a Linux environment.

In TD02, you begin to work directly with the Python code.

The trading desk currently provides:

- instrument metadata in JSON;
- daily market prices in CSV.

MarketPulse must load these files, distinguish the primary instrument from its benchmark, filter the correct observations and display a clear summary.

The common starter still uses:

```text
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Lookback   : 1 month
Interval   : Daily
Provider   : CSV
```

## Learning objectives

At the end of TD02, you should be able to:

- recognize Python lists and dictionaries;
- read JSON data;
- read CSV data;
- understand the structure returned by `csv.DictReader`;
- filter observations by ticker;
- use loops and conditions;
- create simple reusable functions;
- convert numeric text to Python numbers;
- display a simple market summary;
- explain how MarketPulse separates instrument and benchmark data.

## Expected result

At the end of the session, MarketPulse should be able to display a summary similar to:

```text
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First close  : 250.00 USD
Last close   : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First close  : 6600.00
Last close   : 6742.00
```

Do not calculate returns yet.

Return calculations and relative performance will be introduced later.

## Prerequisites

Before starting:

```text
[ ] TD01 completed
[ ] team repository accessible
[ ] TEAM.md completed
[ ] Linux terminal available
[ ] python src/main.py works
```

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | Review the existing Python program |
| 10-25 min | Understand JSON and Python dictionaries |
| 25-40 min | Understand CSV and lists of dictionaries |
| 40-55 min | Filter observations by ticker |
| 55-70 min | Create reusable summary functions |
| 70-82 min | Improve MarketPulse output |
| 82-90 min | Readiness check and recap |

# Part 1 - Review the existing program

Open:

```text
src/main.py
```

You should recognize the following elements:

```text
import csv
import json
Path
DATA_DIR
load_instruments()
load_prices()
filter_prices()
main()
```

Run the current version:

```bash
python src/main.py
```

Before modifying anything, answer:

1. Which function reads the JSON file?
2. Which function reads the CSV file?
3. Which function selects rows for one ticker?
4. Which function coordinates the program execution?
5. Where are the input files stored?

# Part 2 - Understand JSON and dictionaries

## 2.1 Inspect the JSON file

Run:

```bash
cat data/sample/instruments.json
```

The file contains two business objects:

```text
instrument
benchmark
```

In Python, `json.load()` converts this JSON structure into dictionaries.

## 2.2 Explore the loaded structure

Temporarily add simple inspection statements after loading the instruments:

```python
instruments = load_instruments()

print(type(instruments))
print(instruments.keys())
```

Run:

```bash
python src/main.py
```

Question:

> What Python type is returned by `load_instruments()`?

Remove temporary debugging statements when you no longer need them.

## 2.3 Access nested values

Given:

```python
instrument = instruments["instrument"]
benchmark = instruments["benchmark"]
```

Try accessing:

```python
instrument["ticker"]
instrument["name"]
instrument["currency"]

benchmark["ticker"]
benchmark["name"]
```

Questions:

1. What is the type of `instrument`?
2. What is the difference between `instruments` and `instrument`?
3. Why is a dictionary appropriate for instrument metadata?

# Part 3 - Understand CSV and lists of dictionaries

## 3.1 Inspect the CSV

Run:

```bash
head data/sample/prices.csv
```

The columns are:

```text
date
ticker
open
high
low
close
volume
```

## 3.2 Inspect the Python structure

The current function is:

```python
def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))
```

Temporarily inspect the result:

```python
prices = load_prices()

print(type(prices))
print(type(prices[0]))
print(prices[0])
```

Questions:

1. What is the type of `prices`?
2. What is the type of one row?
3. Which dictionary key contains the instrument identifier?

## 3.3 Important observation about CSV types

Try:

```python
print(prices[0]["close"])
print(type(prices[0]["close"]))
```

You should notice that CSV values are initially read as text.

For numerical operations, conversion is required.

Example:

```python
close = float(prices[0]["close"])
print(close)
print(type(close))
```

Question:

> Why would comparing or calculating prices as strings be dangerous?

# Part 4 - Filter observations by ticker

MarketPulse stores both AAPL and SP500 in the same CSV file.

The current helper is:

```python
def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]
```

## 4.1 Use the function

In `main()`:

```python
instrument_prices = filter_prices(
    prices,
    instrument["ticker"],
)

benchmark_prices = filter_prices(
    prices,
    benchmark["ticker"],
)
```

Inspect the number of rows:

```python
print(len(instrument_prices))
print(len(benchmark_prices))
```

Expected result:

```text
21
21
```

## 4.2 Rewrite the logic with a loop

Before moving on, make sure you understand what the list comprehension does.

Equivalent logic:

```python
def filter_prices_with_loop(prices, ticker):
    result = []

    for row in prices:
        if row["ticker"] == ticker:
            result.append(row)

    return result
```

Compare:

```text
loop + condition
vs
list comprehension
```

You do not need to keep both functions.

The objective is to understand that both implementations perform the same filtering operation.

# Part 5 - Create reusable helper functions

The application needs to display information for both the primary instrument and the benchmark.

Avoid duplicating the same logic twice.

## 5.1 Get the first close

Create:

```python
def get_first_close(prices):
    ...
```

The function should:

1. access the first observation;
2. read its `close` value;
3. convert it to `float`;
4. return the result.

Expected examples:

```text
AAPL  -> 250.00
SP500 -> 6600.00
```

## 5.2 Get the last close

Create:

```python
def get_last_close(prices):
    ...
```

Expected examples:

```text
AAPL  -> 266.20
SP500 -> 6742.00
```

## 5.3 Optional safety check

What should happen if a ticker has no observations?

A simple first approach could be:

```python
if not prices:
    ...
```

Discuss with your team what the program should do.

You do not need to build a complex error-management system in TD02.

# Part 6 - Build a reusable market summary

Instead of writing separate display logic for AAPL and SP500, create a reusable function.

Suggested signature:

```python
def display_market_summary(asset, prices, show_currency=True):
    ...
```

The function should display:

```text
ticker
name
number of observations
first close
last close
```

Example for the instrument:

```text
AAPL - Apple Inc.
Observations : 21
First close  : 250.00 USD
Last close   : 266.20 USD
```

Example for the benchmark:

```text
SP500 - S&P 500
Observations : 21
First close  : 6600.00
Last close   : 6742.00
```

The exact internal implementation is your responsibility.

The important idea is:

```text
same operation
+
different data
=
reusable function
```

# Part 7 - Improve main()

Your final `main()` should remain easy to read.

A possible logical sequence is:

```text
load metadata
      |
      v
load prices
      |
      v
select instrument
      |
      v
select benchmark
      |
      v
filter instrument prices
      |
      v
filter benchmark prices
      |
      v
display configuration
      |
      v
display instrument summary
      |
      v
display benchmark summary
```

Do not move everything into `main()`.

Use functions to keep responsibilities understandable.

# Part 8 - Expected final output

Your TD02 version should produce output close to:

```text
=== MarketPulse ===

Market configuration
Period   : 1 month
Interval : Daily

Instrument
AAPL - Apple Inc.
Observations : 21
First close  : 250.00 USD
Last close   : 266.20 USD

Benchmark
SP500 - S&P 500
Observations : 21
First close  : 6600.00
Last close   : 6742.00
```

Small formatting differences are acceptable.

The important requirements are:

```text
[ ] instrument identified
[ ] benchmark identified
[ ] both series filtered correctly
[ ] 21 observations for each
[ ] first close displayed
[ ] last close displayed
[ ] numeric values converted correctly
[ ] reusable functions used
```

# Part 9 - Python concepts recap

By the end of this TD, you should recognize:

## Variables

```python
prices = load_prices()
```

## Dictionaries

```python
instrument["ticker"]
```

## Lists

```python
prices[0]
```

## Functions

```python
def get_last_close(prices):
    ...
```

## Conditions

```python
if row["ticker"] == ticker:
    ...
```

## Loops

```python
for row in prices:
    ...
```

## Type conversion

```python
float(row["close"])
```

# Part 10 - Mini exercises

## Exercise 1 - Display the first date

Create a function:

```python
def get_first_date(prices):
    ...
```

Expected AAPL result:

```text
2026-09-01
```

## Exercise 2 - Display the last date

Create:

```python
def get_last_date(prices):
    ...
```

Expected result:

```text
2026-09-30
```

## Exercise 3 - Count positive-volume observations

For the primary instrument, count rows where:

```python
int(row["volume"]) > 0
```

Question:

> Why is the benchmark volume currently different from the instrument volume in the sample dataset?

The sample data is educational and simplified.

## Exercise 4 - Change the selected ticker manually

Without changing the project architecture, identify which files would need to change if the starter used another instrument and benchmark.

Do not implement provider logic yet.

# Part 11 - If you finish early

## Challenge 1 - Display min and max close

Create simple functions to return:

```text
minimum close
maximum close
```

Do not use pandas.

## Challenge 2 - Display the first three rows

Use slicing:

```python
prices[:3]
```

Then iterate through them with a loop.

## Challenge 3 - Count rows without grep

Use Python to count how many observations exist for one ticker.

Compare your result with:

```bash
grep -c AAPL data/sample/prices.csv
```

## Challenge 4 - Improve formatting

Use Python formatting to display two decimal places.

Example:

```python
f"{value:.2f}"
```

# Part 12 - Troubleshooting

## IndexError

If you access:

```python
prices[0]
```

or:

```python
prices[-1]
```

on an empty list, Python cannot return an observation.

Check that filtering returned rows.

## KeyError

If Python reports a missing dictionary key, inspect:

```python
print(row.keys())
```

or:

```python
print(instrument.keys())
```

Check spelling and capitalization.

## ValueError during float conversion

Inspect the value before converting:

```python
print(row["close"])
```

Make sure the field contains numeric text.

## FileNotFoundError

Check:

```bash
pwd
ls
ls data/sample
```

Run MarketPulse from the repository root.

# Part 13 - Readiness check

Before finishing TD02, each student should be able to explain:

```text
[ ] what a Python list is
[ ] what a Python dictionary is
[ ] what csv.DictReader returns
[ ] why CSV prices need numeric conversion
[ ] how MarketPulse filters by ticker
[ ] why reusable functions reduce duplication
[ ] where instrument metadata is stored
[ ] where price observations are stored
```

The team should confirm:

```text
[ ] MarketPulse still runs
[ ] AAPL has 21 observations
[ ] SP500 has 21 observations
[ ] first and last closes are displayed
[ ] no external Python library was required
```

# Part 14 - Git expectations

Formal Git workflow is introduced in TD03.

Do not create unnecessary branches or Pull Requests in TD02 unless the instructor asks you to.

The objective today is Python and data manipulation.

# Part 15 - Checkpoint relation

No screenshot package is submitted after TD02.

The skills from TD01 and TD02 will later contribute to:

```text
Checkpoint A - Foundations
```

which is validated after TD04.

# Part 16 - What comes next?

In TD03, the business requirement changes:

```text
"We need to keep a reliable history of changes."
```

You will start using the local Git workflow:

```text
git status
git diff
git add
git commit
git log
```

MarketPulse will then become a versioned software project rather than only a collection of local file changes.
