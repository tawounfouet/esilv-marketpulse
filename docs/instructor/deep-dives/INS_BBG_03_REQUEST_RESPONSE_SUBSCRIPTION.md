# INS-BBG-03 - Request/Response vs Subscription

Status:

```text
INSTRUCTOR_READY
```

Primary teaching moments:

```text
TD09
TD10
```

## 1. Purpose

Help the instructor explain why MarketPulse uses a historical acquisition model rather than a live streaming architecture.

## 2. Student CORE boundary

Students need a provider function that retrieves the data required by the MarketPulse snapshot.

They do not need to build:

```text
streaming consumers
long-lived subscriptions
event-driven market-data infrastructure
```

## 3. Instructor mental model

Two useful paradigms:

```text
Request / Response
=
ask for a bounded result
receive messages/results
finish the operation

Subscription
=
register interest
receive updates over time
continue until stopped
```

Historical Bloomberg material also discusses publishing, but publishing remains reference-only for this course.

## 4. Best teaching moment

Use when a student asks:

```text
Why don't we update prices continuously?
Is Bloomberg real-time?
Why does MarketPulse retrieve a historical window instead?
```

## 5. Short explanation

MarketPulse business need:

```text
compare AAPL with SP500
over 1 month
at Daily frequency
```

That requirement is naturally satisfied by a bounded historical-data workflow.

A live subscription would introduce unrelated concerns:

```text
continuous connection
event handling
timestamps
market hours
reconnect logic
state updates
rate/entitlement constraints
```

## 6. Worked example

Current CORE:

```text
request historical observations
        |
        v
normalize rows
        |
        v
align dates
        |
        v
calculate
        |
        v
snapshot
```

Streaming alternative:

```text
subscribe
   |
   v
continuous events
   |
   v
stateful aggregation
   |
   v
live UI updates
```

Explain that the second architecture is a different learning problem.

## 7. Common misconception

Misconception:

```text
professional market data should always be streamed.
```

Correction:

```text
the acquisition model should match the business requirement
```

Misconception:

```text
request/response means synchronous blocking code only.
```

Correction:

```text
the conceptual request model is separate from implementation-level concurrency choices
```

## 8. Stop point

Do not move CORE toward:

```text
websockets
stream processors
subscription callbacks
continuous dashboard refresh
```

because of this explanation.

Intraday or streaming work belongs to advanced material.

## 9. Source discipline

Historical conceptual source:

```text
CM4 Bloomberg
```

Current business contract:

```text
1 month
Daily
instrument vs benchmark
```

Any operational Bloomberg subscription capability must be verified in the current environment before being demonstrated as available.

## 10. Optional extension

Compare the CORE with:

```text
ADV-BBG-04 - Intraday bars
```

or a future streaming demonstration.

Keep it clearly separate from the required TD10 provider path.
