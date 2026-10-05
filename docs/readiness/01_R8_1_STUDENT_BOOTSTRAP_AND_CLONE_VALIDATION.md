# R8.1 - Student Bootstrap and Clone Validation

## 1. Purpose

Record the real execution evidence for:

```text
R8.1
Student bootstrap and clone validation
```

Validation date:

```text
2026-10-05
```

## 2. Target gate

R8.1 requires proof that the repository can be cloned and bootstrapped from the intended teaching/student environment.

The exact acceptance target is:

```text
fresh network checkout
+
Python
+
Git
+
starter data
+
python src/main.py
```

## 3. Repository metadata inspection

Observed repository metadata:

```text
repository
=
tawounfouet/esilv-marketpulse

visibility
=
public

default branch
=
main

clone URL
=
https://github.com/tawounfouet/esilv-marketpulse.git

archived
=
false
```

Classification:

```text
INSPECTED
```

## 4. Real clone attempt from validation runner

Environment:

```text
Git 2.47.3
Python 3.13.5
```

Executed:

```bash
git clone --depth 1 https://github.com/tawounfouet/esilv-marketpulse.git repo
```

Observed result:

```text
fatal: unable to access
https://github.com/tawounfouet/esilv-marketpulse.git/

Could not resolve host: github.com
```

Interpretation:

```text
the validation runner shell
does not have working DNS access to github.com
```

This occurs before GitHub repository authentication or repository transfer.

Therefore the result is not evidence of a MarketPulse repository failure.

Classification:

```text
PENDING_EXTERNAL
```

## 5. Repository API accessibility

The repository tree was successfully retrieved through the connected GitHub repository API.

Observed HEAD at the time of this validation stage:

```text
f3541794c0b5b5dd2a3b8cddf15dc7de23a31871
```

The recursive tree exposed the expected starter artifacts, including:

```text
src/main.py
data/sample/instruments.json
data/sample/prices.csv
requirements.txt
TEAM_TEMPLATE.md
.gitignore
```

Classification:

```text
INSPECTED
```

## 6. Exact starter blob validation

Observed blob SHAs:

```text
src/main.py
884b045eb01903ea9731c55ff99ec65cd78706c9

data/sample/instruments.json
97794c3a4b0946e6baebd0505558b9874ecd9305

data/sample/prices.csv
2fb8b76d13a9be303e95eb2f9d7c9859e14e9f8b

requirements.txt
665b35953c94f8a6ce09c3a326161744ffb3a4c0
```

The files were fetched directly from the current repository state and reconstructed into a clean temporary directory for runtime verification.

Classification:

```text
INSPECTED
+
EXECUTED
```

## 7. Reconstructed clean runtime validation

Executed against the exact current starter blobs:

```bash
python3 src/main.py
```

Observed:

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

Result:

```text
PASS
```

## 8. Python syntax validation

Executed:

```bash
python3 -m py_compile src/main.py
```

Result:

```text
PASS
```

## 9. Starter data validation

Executed:

```bash
grep -c AAPL data/sample/prices.csv
grep -c SP500 data/sample/prices.csv
```

Observed:

```text
AAPL
=
21

SP500
=
21
```

Result:

```text
PASS
```

## 10. Local-only dependency check

Current:

```text
requirements.txt
```

contains no TD01/TD02 external runtime dependency.

The starter uses:

```text
Python standard library
+
versioned local sample files
```

No local secret is required.

The repository ignore file excludes:

```text
.env
virtual environments
Python cache
IDE files
generated raw/processed data
```

Result:

```text
PASS BY INSPECTION
```

## 11. TEAM template safety

The current team template requires only:

```text
TD group
team number
full name
GitHub username
repository name
```

It explicitly forbids:

```text
personal email
student identifier
phone
home address
password
access token
private key
cloud billing information
```

Result:

```text
PASS BY INSPECTION
```

## 12. R8.1 acceptance matrix

```text
[ ] actual git clone from intended ESILV/student network

[x] repository is public
[x] canonical HTTPS clone URL is exposed
[x] default branch is main
[x] validation runner has Git
[x] validation runner has Python
[x] exact current starter blobs are retrievable
[x] starter data is readable
[x] AAPL observation count is 21
[x] SP500 observation count is 21
[x] python src/main.py succeeds from exact starter blobs
[x] src/main.py compiles
[x] no local-only secret/config is required
[x] TEAM template does not require sensitive information
```

## 13. Current R8.1 decision

```text
PENDING_EXTERNAL
```

Reason:

```text
all repository-side bootstrap checks pass

but

the required real clone from the intended
ESILV/student network is not yet proven
```

This gate must not be marked PASS from the current runner because its shell cannot resolve github.com.

## 14. Exact final verification to run at ESILV

From a fresh directory on the intended teaching/student network:

```bash
git clone https://github.com/tawounfouet/esilv-marketpulse.git
cd esilv-marketpulse

python --version
git --version

ls
ls data/sample
head data/sample/prices.csv
grep AAPL data/sample/prices.csv
grep SP500 data/sample/prices.csv

python src/main.py
git status
```

Expected:

```text
clone succeeds

AAPL
=
21 observations

SP500
=
21 observations

python src/main.py
=
PASS

git status
=
clean checkout
```

## 15. Promotion rule

R8.1 may move:

```text
PENDING_EXTERNAL
->
PASS
```

only after the actual clone command succeeds from the intended teaching/student environment.

No documentation change to CORE is required for that promotion.

## 16. Next executable roadmap item

R8.1 remains an external gate for final teaching GO.

Other independent pre-class validations may continue.

The next repository-operational item is:

```text
R8.2
GitHub collaboration validation
```

R8.2 progress does not waive the outstanding R8.1 clone requirement.
