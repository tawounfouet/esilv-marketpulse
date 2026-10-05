# TD01 - Bootstrap + Linux

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"We need a common environment before we can work on MarketPulse."
```

## Context

You are joining the software/data team of a trading desk.

During the module, your team will progressively build MarketPulse, a Python application that compares a financial instrument with its market benchmark.

The common starter uses:

```text
Instrument : AAPL - Apple Inc.
Benchmark  : S&P 500
Lookback   : 1 month
Interval   : Daily
Provider   : CSV
```

Today, the goal is not to modify the financial logic.

The goal is to make sure that every team can access, inspect and run the project from a Linux environment.

## Learning objectives

At the end of TD01, you should be able to:

- identify the MarketPulse project;
- work inside an identified team repository;
- use a Linux terminal;
- understand your current directory;
- list and inspect project files;
- verify Python and Git availability;
- execute the MarketPulse starter;
- identify the CSV and JSON input files.

## Expected result

At the end of the session, your team should have:

```text
[ ] one team repository
[ ] repository name esilv-marketpulse-gXX-tYY
[ ] TEAM.md completed
[ ] all team members added as collaborators
[ ] working development environment
[ ] working Linux terminal
[ ] Python available
[ ] Git available
[ ] MarketPulse running
[ ] CSV and JSON files inspected
```

## Before starting

The instructor repository is:

```text
tawounfouet/esilv-marketpulse
```

Your team repository naming convention is:

```text
esilv-marketpulse-gXX-tYY
```

Example:

```text
esilv-marketpulse-g03-t02
```

Recommended team size:

```text
3 to 4 students
```

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | MarketPulse introduction |
| 10-25 min | Team creation and fork |
| 25-40 min | TEAM.md and collaborators |
| 40-55 min | Development environment and terminal |
| 55-70 min | Linux navigation and file inspection |
| 70-82 min | Run MarketPulse |
| 82-90 min | Readiness check |

The instructor may adjust the timing depending on onboarding issues.

# Part 1 - Understand MarketPulse

## 1.1 Business question

MarketPulse progressively answers:

> How is a financial instrument performing compared with its market benchmark?

The project will later evolve through:

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
Performance comparison
    |
    v
Dash
```

Do not try to implement these later stages today.

## 1.2 Identify the starter

The starter contains:

```text
esilv-marketpulse/
├── README.md
├── TEAM_TEMPLATE.md
├── CONTRIBUTING.md
├── config/
├── data/
├── docs/
├── evidence/
└── src/
```

The important files for TD01 are:

```text
README.md
TEAM_TEMPLATE.md
data/sample/instruments.json
data/sample/prices.csv
src/main.py
```

# Part 2 - Create the team repository

## 2.1 Form the team

Confirm:

```text
TD Group        : GXX
MarketPulse Team: TXX
```

Example:

```text
TD Group        : G03
MarketPulse Team: T02
```

## 2.2 Fork the instructor repository

One team member creates the initial fork from:

```text
tawounfouet/esilv-marketpulse
```

Only one team fork is required.

Do not create one fork per student.

## 2.3 Rename the fork

Rename the team repository using:

```text
esilv-marketpulse-gXX-tYY
```

Example:

```text
esilv-marketpulse-g03-t02
```

Do not add student initials to the repository name.

## 2.4 Add collaborators

The owner of the fork adds the other team members as collaborators.

Every student should confirm that they can access the repository using their own GitHub account.

# Part 3 - Create TEAM.md

## 3.1 Copy the template

Create:

```text
TEAM.md
```

from:

```text
TEAM_TEMPLATE.md
```

## 3.2 Complete team information

At minimum, complete:

- TD group;
- MarketPulse team number;
- full name of each member;
- GitHub username of each member;
- team repository name.

Do not add:

- student identification numbers;
- personal email addresses;
- phone numbers;
- passwords;
- tokens.

## 3.3 Verify the team file

Every team member should be able to answer:

```text
What is our TD group?
What is our MarketPulse team?
What is our repository name?
Who are the repository collaborators?
```

# Part 4 - Open the development environment

## 4.1 Start the common environment

Use the development environment indicated by the instructor.

For the common course path, GitHub Codespaces may be used to provide a Linux terminal and Python environment.

The objective is not to learn Codespaces as a separate technology.

Codespaces is only a means to obtain a common working environment.

## 4.2 Open a terminal

You should see a command prompt.

Do not worry if your prompt looks different from another student's prompt.

The important point is that you can type and execute commands.

# Part 5 - First Linux commands

## 5.1 Where am I?

Run:

```bash
pwd
```

Question:

> What does the displayed path represent?

## 5.2 What files are here?

Run:

```bash
ls
```

Then:

```bash
ls -la
```

Identify:

```text
README.md
config
data
docs
evidence
src
```

Question:

> What additional information does `ls -la` show compared with `ls`?

## 5.3 Navigate into a directory

Run:

```bash
cd data
pwd
ls
```

Then:

```bash
cd sample
pwd
ls
```

You should find:

```text
instruments.json
prices.csv
```

## 5.4 Move back to the repository root

Run:

```bash
cd ../..
pwd
```

Check that you are back at the project root.

# Part 6 - Inspect the MarketPulse data

## 6.1 Inspect the JSON file

Run:

```bash
cat data/sample/instruments.json
```

Identify:

```text
instrument
benchmark
ticker
name
currency
market
```

Questions:

1. What is the primary instrument?
2. What is the benchmark?
3. Which fields describe each one?

## 6.2 Inspect the CSV file

Run:

```bash
head data/sample/prices.csv
```

Identify the columns:

```text
date
ticker
open
high
low
close
volume
```

Question:

> Why does the CSV contain both AAPL and SP500 rows?

## 6.3 Search for a ticker

Run:

```bash
grep AAPL data/sample/prices.csv
```

Then:

```bash
grep SP500 data/sample/prices.csv
```

Question:

> What does `grep` help you find?

## 6.4 Count observations

Try:

```bash
grep -c AAPL data/sample/prices.csv
grep -c SP500 data/sample/prices.csv
```

Expected result:

```text
21
21
```

This confirms that the two series currently contain the same number of daily observations.

# Part 7 - Verify Python and Git

## 7.1 Python

Run:

```bash
python --version
```

If your environment requires it, the instructor may ask you to use:

```bash
python3 --version
```

## 7.2 Git

Run:

```bash
git --version
```

## 7.3 Git identity

Run:

```bash
git config user.name
git config user.email
```

Your commits later in the module must be attributable to your own GitHub identity.

If the values look incorrect, ask the instructor before changing them.

# Part 8 - Run MarketPulse

From the repository root, run:

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

## Questions

1. Which file contains the Python program?
2. Which file contains market metadata?
3. Which file contains daily prices?
4. How many observations are loaded for AAPL?
5. How many observations are loaded for SP500?
6. Why do instrument and benchmark need a common period?

# Part 9 - Read the Python file without modifying it

Run:

```bash
cat src/main.py
```

Do not try to understand every line yet.

Identify only:

```text
imports
DATA_DIR
load_instruments
load_prices
filter_prices
main
```

Question:

> Which function appears responsible for selecting rows for one ticker?

The detailed Python work starts in TD02.

# Part 10 - Readiness check

Before finishing TD01, each student should confirm:

```text
[ ] I can access the team repository
[ ] I know my team repository name
[ ] I can open the development environment
[ ] I can use pwd
[ ] I can use ls
[ ] I can use cd
[ ] I can use cat
[ ] I can use head
[ ] I can use grep
[ ] I can check the Python version
[ ] I can check the Git version
[ ] I can run python src/main.py
[ ] I can identify instrument and benchmark
```

The team should confirm:

```text
[ ] TEAM.md is completed
[ ] all members have repository access
[ ] repository naming is correct
```

# Part 11 - If you finish early

Do not wait passively.

Complete these optional exploration tasks.

## Challenge 1 - Explore Linux output

Try:

```bash
ls -lh
head -n 5 data/sample/prices.csv
tail -n 5 data/sample/prices.csv
```

Explain what each command changes compared with the previous commands.

## Challenge 2 - Count files

Try:

```bash
find . -type f
```

Question:

> Which directories contain most of the project documentation?

## Challenge 3 - Search the repository

Try:

```bash
grep -R "AAPL" .
```

Question:

> In which files does AAPL currently appear?

## Challenge 4 - Inspect Git without changing anything

Try:

```bash
git status
git log --oneline
```

Do not create branches or commits yet unless the instructor asks you to.

Formal Git workflow begins in later TDs.

# Part 12 - Troubleshooting

## Python command not found

Ask the instructor which Python command is expected in the common environment.

Do not spend the whole session installing a different Python distribution.

## Repository not accessible

Check:

- that you are signed into the correct GitHub account;
- that the fork owner added you as a collaborator;
- that you accepted any collaboration invitation.

## Codespace or environment issue

If the problem cannot be solved quickly, pair temporarily with another team member so that you can continue the TD.

The objective is to keep learning while the environment problem is diagnosed.

## MarketPulse does not run

Check:

```bash
pwd
ls
ls src
ls data/sample
```

Make sure you are running the command from the repository root.

# Part 13 - What comes next?

In TD02, MarketPulse becomes a real Python exercise.

You will work more directly with:

```text
CSV
+
JSON
+
Instrument
+
Benchmark
```

and begin to understand how the application reads and manipulates its market data.

No checkpoint evidence is required at the end of TD01.

Checkpoint A will be performed after TD04.
