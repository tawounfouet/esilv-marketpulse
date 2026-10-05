# Target Repository Structure

## 1. Principle

Students do not receive the final architecture on day one.

MarketPulse starts small and evolves as new requirements appear.

The objective is to understand why project structure changes.

## 2. Starter repository

Initial structure:

```text
esilv-marketpulse/
├── README.md
├── TEAM_TEMPLATE.md
├── CONTRIBUTING.md
├── .gitignore
├── requirements.txt
│
├── config/
│   └── settings.yml
│
├── data/
│   └── sample/
│       ├── instruments.json
│       └── prices.csv
│
├── docs/
│   ├── 00_MARKETPULSE_FUNCTIONAL_CONTRACT.md
│   ├── 01_STUDENT_ONBOARDING.md
│   ├── 02_MARKETPULSE_USE_CASE.md
│   ├── 03_GITHUB_TEAM_WORKFLOW.md
│   ├── 04_CHECKPOINTS_AND_EVIDENCE.md
│   └── 05_TARGET_REPOSITORY_STRUCTURE.md
│
├── evidence/
│   └── README.md
│
└── src/
    └── main.py
```

This structure is intentionally small.

## 3. Why not start with the final structure?

Students should first understand:

- where the data lives;
- how the Python program reads it;
- how the program is executed;
- how Git records changes.

Later, new requirements create a reason to refactor.

The target architecture should emerge from the project.

## 4. Progressive evolution

### Initial stage

```text
src/
└── main.py
```

### Multiple data sources appear

```text
src/
└── marketpulse/
    ├── main.py
    └── providers/
        ├── csv_provider.py
        └── yahoo_provider.py
```

### Common processing appears

```text
src/
└── marketpulse/
    ├── main.py
    ├── providers/
    └── processing/
        ├── normalization.py
        └── indicators.py
```

### Bloomberg appears

```text
providers/
├── csv_provider.py
├── yahoo_provider.py
└── bloomberg_provider.py
```

### Dash appears

```text
dashboard/
├── layout.py
└── callbacks.py
```

## 5. Target common repository

A possible final common structure is:

```text
esilv-marketpulse/
│
├── README.md
├── TEAM.md
├── CONTRIBUTING.md
├── requirements.txt
├── .gitignore
│
├── config/
│   └── settings.yml
│
├── data/
│   ├── sample/
│   │   ├── instruments.json
│   │   └── prices.csv
│   ├── raw/
│   └── processed/
│
├── src/
│   └── marketpulse/
│       ├── __init__.py
│       ├── app.py
│       ├── cli.py
│       ├── config.py
│       │
│       ├── providers/
│       │   ├── __init__.py
│       │   ├── csv_provider.py
│       │   ├── yahoo_provider.py
│       │   └── bloomberg_provider.py
│       │
│       ├── processing/
│       │   ├── __init__.py
│       │   ├── normalization.py
│       │   └── indicators.py
│       │
│       └── dashboard/
│           ├── __init__.py
│           ├── layout.py
│           └── callbacks.py
│
├── docs/
│   └── ...
│
└── evidence/
    ├── checkpoint-a/
    ├── checkpoint-b/
    └── checkpoint-c/
```

The exact final structure may be simplified depending on the actual pace of the class.

## 6. Important exclusions

The common target does not require:

```text
tests/
Dockerfile
.github/workflows/
Kubernetes
complex packaging
advanced CI/CD
```

These are outside the common 18-hour scope unless explicitly introduced as optional material.

## 7. Core architectural flow

The important structure is conceptual:

```text
CSV
Yahoo
Bloomberg
   |
   v
normalized market data
   |
   v
processing
   |
   v
Dash
   |
   v
Trader
```

The application should progressively make provider changes less disruptive to the rest of the code.

## 8. Market comparison flow

MarketPulse ultimately handles:

```text
Instrument
+
Benchmark
   |
   v
same period
+
same interval
   |
   v
performance comparison
```

The common contract remains:

```text
lookback = 1mo
interval = 1d
```

unless the instructor asks for a different configuration.

## 9. Final criterion

The goal is not to reproduce this tree mechanically.

A successful team should be able to explain:

- why the project was refactored;
- why providers are separated;
- why instrument and benchmark use a common comparison model;
- how Git history reflects the evolution;
- how another student can clone and run the project.
