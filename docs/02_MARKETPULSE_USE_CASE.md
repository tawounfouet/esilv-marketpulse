# MarketPulse Use Case

## 1. Scenario

You are part of the software/data team of a trading desk.

A trader wants a simple application that can follow a financial instrument and compare it with a relevant market benchmark.

The initial MarketPulse pair is:

```text
AAPL
+
S&P 500
```

The application evolves progressively during the labs.

## 2. Business question

The central question is:

> Is the selected instrument outperforming or underperforming its benchmark over the selected period?

This is more useful than displaying a stock price without market context.

## 3. Core functional model

```text
Instrument
+
Benchmark
+
Provider
+
Historical window
+
Interval
        |
        v
Comparable market data
        |
        v
Performance analysis
        |
        v
Dashboard
```

The common course contract is:

```text
Instrument        1
Benchmark         1
Lookback          1 month
Interval          Daily
Starter provider  CSV / JSON
Next provider     Yahoo Finance
Professional provider  Bloomberg
```

## 4. Why a benchmark?

A price alone does not indicate whether an instrument performed well relative to its market.

Example:

```text
Instrument return : +4.0%
Benchmark return  : +2.0%
```

The instrument outperformed its benchmark by approximately:

```text
+2.0 percentage points
```

If the instrument returned +4.0% while the benchmark returned +6.0%, the same instrument would instead have underperformed its market.

## 5. Why base 100?

An equity price and an index level usually use different scales.

Example:

```text
AAPL       260 USD
S&P 500   6700 points
```

Plotting both raw levels on the same axis is not a meaningful performance comparison.

A base-100 representation makes both series start at the same reference value:

```text
Day 1

AAPL       100
S&P 500    100
```

The subsequent evolution can then be compared visually.

## 6. Analytical progression

MarketPulse CORE progressively introduces:

```text
price
  |
  v
period return
  |
  v
base-100 normalization
  |
  v
relative performance
```

Daily returns remain available as an optional extension.

The course does not require advanced quantitative finance.

## 7. Core visualisations

The final common dashboard may include:

### Instrument price history

Shows the actual evolution of the selected instrument.

### Instrument vs benchmark - Base 100

This is the main comparison chart.

It makes relative performance immediately visible.

### Daily returns

Optional if time allows.

It compares daily changes rather than price levels.

### Trading volume

Used for the primary instrument when available.

## 8. Team-specific market pairs

The common starter uses:

```text
AAPL + S&P 500
```

Later, the instructor may allow teams to choose another coherent pair.

Examples:

```text
AAPL + S&P 500
MSFT + NASDAQ-100
AXA + CAC 40
LVMH + CAC 40
```

The architecture remains the same.

Only the selected market instruments change.

## 9. Provider progression

The same business question is progressively served by different data sources:

```text
CSV / JSON
    |
    v
Yahoo Finance
    |
    v
Bloomberg
```

Provider-specific symbols may differ.

Example:

```text
S&P 500

Starter CSV : SP500
Yahoo       : ^GSPC
Bloomberg   : SPX Index
```

The application should progressively learn to separate the business concept from provider-specific identifiers.

## 10. Why this use case fits the module

MarketPulse creates a common reason to use:

- Linux for navigating, inspecting and executing the project;
- Python for reading, filtering, transforming and comparing data;
- Git for versioning changes;
- GitHub for collaboration, Pull Requests and reviews;
- Yahoo Finance for accessible remote market data;
- Bloomberg for professional market-data access;
- Dash for the final user-facing interface.

The project remains intentionally small enough to fit an 18-hour lab sequence.
