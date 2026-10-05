# MarketPulse

MarketPulse is the progressive financial market-data use case for the **ESILV A4 - Python, Git, Linux** labs.

## Business context

You are part of the software/data team of a **trading desk**.

The desk wants a simple tool to follow a financial instrument and compare its performance with a relevant market benchmark.

The common starter uses:

```text
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Provider   : CSV
Lookback   : 1 month
Interval   : Daily
```

During the labs, MarketPulse will progressively evolve to use:

1. CSV / JSON
2. Yahoo Finance
3. Bloomberg
4. Dash

The goal is not to build the final architecture on day one. The repository evolves as new business and technical requirements are introduced.

## Core idea

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
        |
        v
Performance comparison
```

The primary instrument and benchmark are always compared over the same period and frequency.

See `docs/00_MARKETPULSE_FUNCTIONAL_CONTRACT.md` for the complete common functional contract.

## Getting started

Open a terminal and check your environment:

```bash
pwd
ls
python --version
git --version
```

Run the initial version of MarketPulse:

```bash
python src/main.py
```

Expected output:

```text
=== MarketPulse ===

Instrument
AAPL - Apple Inc.
Last price: 266.20 USD

Benchmark
SP500 - S&P 500
Last level: 6742.00

Period: 1 month
Interval: Daily

Observations
AAPL: 21
SP500: 21
```

## Starter structure

```text
marketpulse/
├── README.md
├── .gitignore
├── requirements.txt
├── config/
│   └── settings.yml
├── data/
│   └── sample/
│       ├── prices.csv
│       └── instruments.json
├── docs/
│   └── 00_MARKETPULSE_FUNCTIONAL_CONTRACT.md
├── src/
│   └── main.py
└── evidence/
    └── README.md
```

## Starter data

The sample CSV contains approximately one month of daily observations for:

- AAPL as the primary instrument;
- SP500 as the benchmark.

The values are **illustrative educational sample data**. They are not certified historical market observations.

The starter dataset is intentionally small enough to inspect directly from the terminal while still supporting two aligned time series.

## Starter note

At this initial stage:

- `src/main.py` reads the sample CSV and JSON files directly;
- `config/settings.yml` already describes the future configuration contract;
- YAML configuration is not yet wired into the Python program;
- returns, base-100 normalization and relative performance are not implemented yet.

Those capabilities will appear progressively during the labs.

## Initial learning objectives

You should first be able to:

- navigate the repository from a Linux terminal;
- inspect CSV and JSON sample files;
- execute a Python program;
- filter observations by ticker;
- understand the distinction between an instrument and its benchmark;
- progressively version your changes with Git.

## Repository evolution

```text
Local CSV / JSON
      |
      v
Git workflow
      |
      v
Collaborative Git workflow
      |
      v
Yahoo Finance
      |
      v
Bloomberg
      |
      v
Performance comparison
      |
      v
Dash
```

Later analytical concepts include:

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

More advanced topics such as remote Linux, SSH, deployment, Docker or GitHub Actions are optional extensions and are not part of the initial starter.

## Security

Never commit:

- passwords;
- API keys;
- access tokens;
- SSH private keys;
- Bloomberg credentials;
- cloud credentials or billing information.

## Evidence

Evidence is requested only at the defined checkpoints. See `evidence/README.md`.

---

**Course:** MESIFI472326 - Python, Git, Linux  
**Use case:** MarketPulse - Multi-Source Financial Market Data Dashboard
