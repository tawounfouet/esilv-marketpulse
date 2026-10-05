# MarketPulse

MarketPulse is the progressive use case for the **ESILV A4 - Python, Git, Linux** labs.

## Business context

You are part of the software/data team of a **trading desk**.

The traders currently receive market data from local CSV and JSON files. During the labs, MarketPulse will progressively evolve to use:

1. CSV / JSON
2. Yahoo Finance
3. Bloomberg
4. Dash

The goal is not to build the final architecture on day one. The repository will evolve progressively as new business and technical requirements are introduced.

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
Instrument: AAPL
Name: Apple Inc.
Last price: 260.80 USD
Observations: 5
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
│       └── instrument.json
├── src/
│   └── main.py
└── evidence/
    └── README.md
```

## Starter note

At this initial stage, `src/main.py` reads the sample CSV/JSON files directly. `config/settings.yml` is already present as a preview of the configuration mechanism that will be wired into MarketPulse later in the labs.

## Initial learning objectives

The starter is intentionally small.

You should first be able to:

- navigate the repository from a Linux terminal;
- inspect the sample files;
- execute a Python program;
- understand where the market data comes from;
- progressively version your changes with Git.

## Repository evolution

The following concepts will appear progressively during the labs:

```text
Local CSV / JSON
      ↓
Git workflow
      ↓
Collaborative Git workflow
      ↓
Yahoo Finance
      ↓
Bloomberg
      ↓
Dash
```

More advanced topics such as remote Linux, SSH, deployment, Docker or GitHub Actions are **optional extensions** and are not part of the initial starter.

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
