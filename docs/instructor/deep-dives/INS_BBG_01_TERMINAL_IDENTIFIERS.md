# INS-BBG-01 - Bloomberg Terminal and Identifiers

Status:

```text
INSTRUCTOR_READY
```

Primary teaching moment:

```text
TD09 - Bloomberg Introduction
```

## 1. Purpose

Help the instructor position Bloomberg as a professional market-data environment and explain why provider identifiers differ from MarketPulse canonical tickers.

## 2. Student CORE boundary

Students need to understand:

```text
AAPL
->
AAPL US Equity

SP500
->
SPX Index
```

They do not need a broad Terminal-navigation course.

## 3. Instructor mental model

MarketPulse uses an application identifier:

```text
AAPL
SP500
```

A provider may use a richer security identifier containing provider-specific market or asset-class context.

The provider boundary therefore performs:

```text
canonical application identity
        |
        v
provider identity
        |
        v
provider data
        |
        v
canonical rows
```

This separation is more important than memorizing many Bloomberg identifiers.

## 4. Best teaching moment

Use at the start of TD09 when students first see:

```text
AAPL US Equity
SPX Index
```

Ask:

```text
Why not use the same symbol everywhere?
```

## 5. Short explanation

A concise explanation:

```text
MarketPulse owns its business identifiers.

Bloomberg owns provider-specific identifiers.

The provider module translates between the two.
```

The key software-engineering lesson is:

```text
provider vocabulary
must not leak everywhere in the application
```

## 6. Worked example

Application configuration:

```text
instrument = AAPL
benchmark = SP500
```

Provider mapping:

```python
BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}
```

Normalization returns canonical rows where the application-facing ticker remains:

```text
AAPL
SP500
```

not provider identifiers.

## 7. Common misconception

Misconception:

```text
A ticker is a universal identifier.
```

Correction:

```text
symbols and identifiers are provider- and market-context dependent
```

Misconception:

```text
Bloomberg access means every Bloomberg product or field is available.
```

Correction:

```text
actual access depends on the approved environment and must be verified
```

## 8. Stop point

Do not spend TD09 teaching extensive Terminal navigation.

Do not introduce unverified:

```text
field names
entitlements
pricing
rate limits
connector assumptions
```

as current facts.

## 9. Source discipline

Historical source:

```text
CM4 Bloomberg
TD4 Bloomberg
```

Current operational sources:

```text
docs/labs/TD09_BLOOMBERG_INTRODUCTION.md
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md
```

Current safety rule:

```text
observed or approved
not guessed
```

## 10. Optional extension

Show how another provider might use a different symbol for the same business instrument.

The extension should reinforce the provider-boundary concept, not expand the mandatory mapping table.
