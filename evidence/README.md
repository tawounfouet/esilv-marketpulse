# Evidence

This directory stores individual MarketPulse checkpoint evidence.

The single source of truth for all evidence requirements is:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```

That document defines the official filenames, required screenshots, optional evidence, individual README content, live validation principles and security rules.

Do not create a parallel evidence specification in this directory.

## Directory convention

Each student stores evidence under their own GitHub username:

```text
evidence/
├── checkpoint-a/
│   └── <github-username>/
├── checkpoint-b/
│   └── <github-username>/
└── checkpoint-c/
    └── <github-username>/
```

Each checkpoint directory must contain the student's checkpoint `README.md` and the evidence files required by the canonical contract.

## Important

Evidence is collected only for:

- Checkpoint A;
- Checkpoint B;
- Checkpoint C.

Do not add screenshots for every TD.

Screenshots complement:

- Git history;
- Pull Requests;
- reviews;
- execution;
- explanation.

They do not replace those elements.

## Security

Before committing any evidence, inspect it carefully.

Never expose:

- passwords;
- API keys;
- access tokens;
- SSH private keys;
- Bloomberg credentials;
- cloud credentials;
- payment information.

For exact filenames and validation criteria, always return to:

```text
docs/04_CHECKPOINTS_AND_EVIDENCE.md
```
