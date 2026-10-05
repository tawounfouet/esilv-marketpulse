# MarketPulse Functional Contract

## Purpose

MarketPulse is the progressive financial market-data use case for the ESILV A4 module MESIFI472326 - Python, Git, Linux.

The project is intentionally designed to evolve during the labs. Students start from local CSV and JSON files, then progressively introduce collaborative Git workflows, remote market data providers and a Dash interface.

## Core business question

MarketPulse answers a simple question:

> How is a financial instrument performing compared with its market benchmark?

The application therefore works with two market series:

- one primary instrument;
- one benchmark.

Starter example:

| Role | Instrument |
|---|---|
| Primary instrument | Apple Inc. - AAPL |
| Benchmark | S&P 500 - SP500 |

## Core functional contract

The common lab scope is fixed as follows:

| Parameter | Core value |
|---|---|
| Primary instruments | 1 |
| Benchmarks | 1 |
| Historical window | 1 month |
| Interval | Daily |
| Starter provider | CSV / JSON |
| Next provider | Yahoo Finance |
| Professional provider | Bloomberg |
| Comparison rule | Same period and same frequency |

In configuration terms:

```text
Instrument
+
Benchmark
+
Provider
+
Lookback
+
Interval
+
Performance comparison
```

## Starter configuration

The starter uses:

```text
Instrument : AAPL
Benchmark  : S&P 500
Provider   : CSV
Lookback   : 1 month
Interval   : Daily
```

The corresponding technical values are:

```text
provider = csv
lookback = 1mo
interval = 1d
```

## Data-source progression

MarketPulse evolves progressively:

```text
CSV / JSON
    |
    v
Yahoo Finance
    |
    v
Bloomberg
    |
    v
Normalized market data
    |
    v
Performance comparison
    |
    v
Dash
```

The business concept stays stable while the provider changes.

## Provider identifiers

The starter deliberately uses simple provider-neutral identifiers.

Example:

```text
S&P 500
  |
  +-- Starter CSV : SP500
  +-- Yahoo       : ^GSPC
  +-- Bloomberg   : SPX Index
```

Provider-specific identifiers will be introduced only when the relevant provider is introduced in the labs.

## Time-series contract

The primary instrument and benchmark must be compared over:

- the same historical window;
- the same interval;
- compatible observation dates.

Core settings:

```text
Historical window : 1 month
Interval          : Daily
```

Intraday data is outside the common core.

Optional advanced work may later explore shorter intervals such as hourly data, but this must not be required for the core grade.

## Core analytical progression

The starter does not implement the final analytics.

The labs progressively introduce:

```text
price
  |
  v
daily return
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

The final comparison should make it possible to answer whether the primary instrument outperforms or underperforms its benchmark over the selected period.

## Core dashboard target

The final common dashboard may contain:

1. instrument price history;
2. instrument vs benchmark performance in base 100;
3. period return for the instrument;
4. period return for the benchmark;
5. relative performance;
6. instrument trading volume.

Daily-return charts may be added if time allows.

Advanced financial indicators such as Sharpe ratio, beta, CAPM, VaR, RSI or portfolio optimization are outside the common core.

## Starter dataset

The starter repository contains a small illustrative dataset representing approximately one month of daily observations.

The values are educational sample data.

They must not be presented as certified historical market observations.

The goal of the starter dataset is to support:

- Linux file manipulation;
- Python file reading;
- filtering by ticker;
- comparison of two aligned time series;
- progressive refactoring during the labs.

## Scope protection

The module remains focused on:

```text
Python
+
Git
+
Linux
+
financial market-data workflow
```

The following topics are not required in the common core:

- automated testing frameworks;
- Docker;
- CI/CD;
- intraday market microstructure;
- machine learning;
- advanced quantitative finance.

Some may be presented later as optional extensions.

## Reference statement

The MarketPulse core contract is therefore:

```text
MarketPulse
=
1 instrument
+
1 benchmark
+
1 provider
+
1 month lookback
+
daily interval
+
performance comparison
```

This contract should remain stable across the common labs unless the teaching team explicitly revises it.
