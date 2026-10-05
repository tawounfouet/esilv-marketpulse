# INS-BBG-04 - xbbg vs blpapi

Status:

```text
INSTRUCTOR_READY
```

Primary teaching moment:

```text
TD10 - Bloomberg Provider
```

## 1. Purpose

Give the instructor a framework for explaining abstraction levels in Bloomberg Python integration without freezing either library as a universal MarketPulse dependency.

## 2. Student CORE boundary

Students need:

```text
src/providers/bloomberg_provider.py
```

with a provider boundary that returns canonical rows.

They do not need to master multiple Bloomberg Python libraries.

## 3. Instructor mental model

Historical course framing:

```text
xbbg
=
higher-level convenience abstraction

blpapi
=
lower-level Bloomberg API access
with more explicit API mechanics
```

The important teaching concept is not:

```text
which library is best
```

It is:

```text
application architecture should isolate provider integration choices
```

## 4. Best teaching moment

Use when students see the provider module and ask:

```text
Why don't we call Bloomberg directly from main.py?
Why use a wrapper library?
Why would anyone use a lower-level API?
```

## 5. Short explanation

A higher-level library can reduce integration code.

A lower-level API can expose more control and more of the provider's native model.

Both choices still belong behind:

```text
bloomberg_provider.py
```

The rest of MarketPulse should receive:

```text
canonical rows
```

regardless of connector choice.

## 6. Worked example

Bad boundary:

```text
main.py
-> Bloomberg-specific session calls
-> field parsing
-> analytics
```

Preferred boundary:

```text
main.py
-> bloomberg_provider.py
-> approved connector or APPROVED_SAMPLE
-> canonical rows
-> analytics.py
```

Changing the connector should not require rewriting:

```text
calculate_period_return(...)
calculate_base_100(...)
calculate_relative_performance(...)
```

## 7. Common misconception

Misconception:

```text
xbbg is the beginner version and blpapi is the professional version.
```

Correction:

```text
they represent different abstraction choices; suitability depends on the actual environment and requirements
```

Misconception:

```text
we should install both to be safe.
```

Correction:

```text
dependencies should reflect the implementation actually used
```

## 8. Stop point

Do not modify:

```text
requirements.txt
```

merely because both technologies are discussed.

Do not claim a connector is available in the current ESILV environment until it has been verified there.

## 9. Source discipline

Historical material compared xbbg and blpapi.

That comparison is retained as conceptual context.

Operational facts that may change include:

```text
package compatibility
installation path
Terminal/Desktop API configuration
access rights
supported environment
```

Verify those before class if they matter to the selected LIVE path.

Current safe fallback remains:

```text
APPROVED_SAMPLE
```

when LIVE integration is unavailable.

## 10. Optional extension

Potential advanced paths:

```text
ADV-BBG-02 - xbbg exploration
ADV-BBG-03 - blpapi low-level request
```

Both remain optional and environment-dependent.
