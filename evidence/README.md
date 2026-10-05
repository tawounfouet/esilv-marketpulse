# Evidence

This directory is used for checkpoint evidence.

Do not add screenshots for every lab.

Evidence is requested only for:

- Checkpoint A;
- Checkpoint B;
- Checkpoint C.

The official evidence contract is defined in:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

## Naming rules

All screenshots use:

```text
format          : PNG
naming          : lowercase_snake_case
numbering       : 01_, 02_, 03_...
spaces          : forbidden
accents         : forbidden
free naming     : forbidden
```

Do not rename the official evidence files.

## Official filenames

### Checkpoint A

Required:

```text
01_terminal_python.png
02_git_status_log.png
03_branch_merge.png
```

### Checkpoint B

Required:

```text
01_pull_request.png
02_code_review.png
03_yahoo_market_data.png
04_instrument_benchmark.png
```

### Checkpoint C

Required:

```text
01_final_market_data.png
02_dash_dashboard.png
03_final_pull_request.png
04_reproducible_run.png
```

Optional:

```text
05_advanced_deployment.png
```

## Individual structure

Each student stores evidence under their own GitHub username.

Example:

```text
evidence/
|
+-- checkpoint-a/
|   +-- alice-martin/
|   |   +-- README.md
|   |   +-- 01_terminal_python.png
|   |   +-- 02_git_status_log.png
|   |   +-- 03_branch_merge.png
|   |
|   +-- bob-dupont/
|
+-- checkpoint-b/
|   +-- alice-martin/
|   |   +-- README.md
|   |   +-- 01_pull_request.png
|   |   +-- 02_code_review.png
|   |   +-- 03_yahoo_market_data.png
|   |   +-- 04_instrument_benchmark.png
|   |
|   +-- bob-dupont/
|
+-- checkpoint-c/
    +-- alice-martin/
    |   +-- README.md
    |   +-- 01_final_market_data.png
    |   +-- 02_dash_dashboard.png
    |   +-- 03_final_pull_request.png
    |   +-- 04_reproducible_run.png
    |   +-- 05_advanced_deployment.png
    |
    +-- bob-dupont/
```

## Individual README

Each checkpoint directory must contain a `README.md` identifying:

- student name;
- GitHub username;
- branch;
- main commits;
- Pull Request;
- reviewed Pull Request;
- work completed;
- main difficulty;
- evidence files.

The filenames listed in the README must exactly match the files stored in the directory.

## Important

Screenshots complement Git history and live validation.

They do not replace:

- commits;
- Pull Requests;
- reviews;
- execution;
- explanation.

Each student must provide their own individual contribution evidence.

## Security

Never include:

- passwords;
- API keys;
- access tokens;
- SSH private keys;
- Bloomberg credentials;
- cloud credentials;
- payment information.

Inspect every screenshot before committing it.
