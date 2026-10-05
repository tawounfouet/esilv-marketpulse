# TD11 - Dash Dashboard

## Duration

```text
1 hour 30 minutes
```

## Business requirement

```text
"Traders want a visual interface instead of terminal output."
```

## Context

MarketPulse can now retrieve and normalize market data from several provider stages:

```text
CSV
Yahoo
Bloomberg
   |
   v
canonical market data
   |
   v
shared comparison logic
```

The application can already calculate:

```text
period return
daily return
base 100
relative performance
```

Until now, most results have been displayed in the terminal.

TD11 introduces a web interface with Dash.

The objective is not to build a complex trading platform.

The objective is to expose the existing MarketPulse comparison clearly and visually.

The central chart is:

```text
Instrument vs Benchmark
Base 100
```

## Learning objectives

At the end of TD11, you should be able to:

- install and record Dash dependencies;
- explain the role of Dash in MarketPulse;
- create a minimal Dash application;
- display MarketPulse configuration;
- display instrument and benchmark period returns;
- display relative performance;
- create a base-100 comparison chart;
- understand the difference between application data and presentation;
- keep provider logic outside the dashboard;
- run the dashboard locally;
- complete the established GitHub workflow.

## Expected result

The dashboard should make the following information visible:

```text
MarketPulse

Provider
Instrument
Benchmark
Lookback
Interval

Instrument return
Benchmark return
Relative performance

Instrument vs Benchmark
Base 100 chart
```

A simplified visual target is:

```text
+----------------------------------------------------+
| MarketPulse                                        |
+----------------------------------------------------+
| Provider   | Instrument | Benchmark | Period       |
| Bloomberg  | AAPL       | SP500     | 1 month      |
+----------------------------------------------------+
| AAPL Return | SP500 Return | Relative Performance  |
|   +x.xx%    |    +x.xx%    |       +x.xx pts       |
+----------------------------------------------------+
|                                                    |
|        Instrument vs Benchmark - Base 100          |
|                                                    |
|  110 |                        AAPL                 |
|  105 |                  _____/                     |
|  100 |____SP500_________/________________          |
|      +------------------------------------         |
|                                                    |
+----------------------------------------------------+
```

The exact values depend on the selected provider and retrieval date.

## Core scope

Required:

```text
configuration summary
period-return cards
relative-performance card
base-100 comparison chart
```

Optional if time allows:

```text
daily-return chart
instrument volume chart
simple provider selector
simple instrument selector
```

Do not make optional features block the required dashboard.

## Prerequisites

Before starting:

```text
[ ] TD01-TD10 completed
[ ] team main is up to date
[ ] provider path works
[ ] normalized rows are available
[ ] period return works
[ ] base-100 series works
[ ] relative performance works
[ ] build_market_snapshot(...) follows docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md
[ ] terminal presentation can consume the shared snapshot
[ ] no credentials are exposed
```

Update local main:

```bash
git switch main
git pull
git status
```

Run the current terminal version:

```bash
python src/main.py
```

Start from a clean working tree.

## Session plan

| Time | Activity |
|---|---|
| 00-10 min | Dashboard objective and architecture |
| 10-20 min | Install and record Dash dependencies |
| 20-35 min | Create minimal Dash application |
| 35-50 min | Add summary cards |
| 50-68 min | Build base-100 comparison chart |
| 68-78 min | Integrate MarketPulse data |
| 78-90 min | Validate, PR and review |

# Part 1 - Understand the dashboard boundary

Dash belongs to the presentation layer.

The dashboard should consume results from MarketPulse.

It should not become the place where provider-specific acquisition logic is implemented.

Target separation:

```text
Provider
   |
   v
canonical rows
   |
   v
analytics
   |
   v
dashboard data
   |
   v
Dash presentation
```

Avoid:

```text
Dash callback
   |
   v
Bloomberg-specific request
   |
   v
return calculation
   |
   v
HTML
```

The dashboard should remain as thin as possible.

# Part 2 - Create the feature branch

Create:

```bash
git switch main
git pull
git switch -c feature/dash-dashboard
```

Verify:

```bash
git branch
git status
```

All TD11 work should stay on this branch until review and merge.

# Part 3 - Install Dash

Check whether Dash is installed:

```bash
python -m pip show dash
```

If needed:

```bash
python -m pip install dash plotly
```

Update:

```text
requirements.txt
```

Add the direct dependencies used by your code:

```text
dash
plotly
```

Keep the existing dependencies such as:

```text
yfinance
```

if they are already part of your project.

## Why record both?

If your code imports both:

```python
from dash import Dash
import plotly.graph_objects as go
```

then both are direct project dependencies.

# Part 4 - Create the dashboard entry point

TD11 adds one simple dashboard entry point:

```text
src/
├── main.py
├── analytics.py
├── dashboard.py
└── providers/
    ├── __init__.py
    ├── yahoo_provider.py
    └── bloomberg_provider.py
```

Create:

```text
src/dashboard.py
```

Do not create a nested dashboard package for the CORE.

The single-file entry point keeps imports and execution understandable within the 18-hour scope.

# Part 5 - Create a minimal Dash application

Start with a minimal application.

Example:

```python
from dash import Dash, html


app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1("MarketPulse"),
        html.P(
            "Instrument vs Benchmark market comparison"
        ),
    ]
)


if __name__ == "__main__":
    app.run(debug=True)
```

Run:

```bash
python src/dashboard.py
```

Open the local URL displayed by Dash.

You should see:

```text
MarketPulse
Instrument vs Benchmark market comparison
```

## Question

> What is the difference between the Dash Python process and the page displayed in your browser?

# Part 6 - Consume the MarketPulse snapshot

Do not hard-code market returns inside the layout.

The application-level contract is frozen in:

```text
docs/12_MARKETPULSE_APPLICATION_SNAPSHOT_CONTRACT.md
```

The shared function is:

```python
build_market_snapshot(...)
```

For the flat CORE structure, it lives in:

```text
src/main.py
```

The dashboard should consume it:

```python
from main import build_market_snapshot


snapshot = build_market_snapshot()
```

Required snapshot keys:

```text
provider
lookback
interval
instrument
benchmark
instrument_return
benchmark_return
relative_performance
instrument_base_100
benchmark_base_100
```

The important principle is:

```text
providers acquire
+
analytics calculate
+
snapshot assembles
+
dashboard displays
```

Do not call Yahoo or Bloomberg directly from `dashboard.py`.

Do not recalculate returns or base 100 inside `dashboard.py`.

# Part 7 - Display configuration information

Add a simple configuration section.

Example with Dash components:

```python
html.Div(
    [
        html.P(f"Provider: {provider_name}"),
        html.P(
            f"Instrument: {instrument['ticker']}"
        ),
        html.P(
            f"Benchmark: {benchmark['ticker']}"
        ),
        html.P("Period: 1 month"),
        html.P("Interval: Daily"),
    ]
)
```

The output must make the comparison context understandable.

Required visible information:

```text
Provider
Instrument
Benchmark
Lookback
Interval
```

# Part 8 - Add performance cards

The dashboard should display three key indicators.

```text
Instrument return
Benchmark return
Relative performance
```

Example content:

```python
html.Div(
    [
        html.Div(
            [
                html.H3("Instrument Return"),
                html.P(
                    f"{instrument_return:+.2f}%"
                ),
            ]
        ),
        html.Div(
            [
                html.H3("Benchmark Return"),
                html.P(
                    f"{benchmark_return:+.2f}%"
                ),
            ]
        ),
        html.Div(
            [
                html.H3("Relative Performance"),
                html.P(
                    f"{relative_performance:+.2f} pts"
                ),
            ]
        ),
    ]
)
```

The exact visual styling is secondary in TD11.

Correct data is more important than sophisticated CSS.

# Part 9 - Build the base-100 figure

The central chart compares performance on a common scale.

Use the base-100 series from TD07.

Import Plotly:

```python
import plotly.graph_objects as go
```

Create a figure:

```python
figure = go.Figure()
```

Add the instrument:

```python
figure.add_trace(
    go.Scatter(
        x=[
            row["date"]
            for row in instrument_base_100
        ],
        y=[
            row["value"]
            for row in instrument_base_100
        ],
        mode="lines",
        name=instrument_ticker,
    )
)
```

Add the benchmark:

```python
figure.add_trace(
    go.Scatter(
        x=[
            row["date"]
            for row in benchmark_base_100
        ],
        y=[
            row["value"]
            for row in benchmark_base_100
        ],
        mode="lines",
        name=benchmark_ticker,
    )
)
```

Add a title:

```python
figure.update_layout(
    title="Instrument vs Benchmark - Base 100",
    xaxis_title="Date",
    yaxis_title="Base 100",
)
```

# Part 10 - Add the graph to Dash

Import:

```python
from dash import dcc
```

Then add:

```python
dcc.Graph(
    figure=figure
)
```

to the layout.

The central visual should show two series:

```text
AAPL
SP500
```

or the selected team pair.

## Validation question

> Do both lines start near 100?

If not, inspect the base-100 calculation before changing the chart.

# Part 11 - Align chart dates

The chart should compare the same common dates.

Do not plot:

```text
unaligned instrument dates
+
unaligned benchmark dates
```

if the objective is direct comparison.

Reuse the common-date logic from TD07 and TD08.

Target:

```text
same dates
+
same lookback
+
same interval
```

# Part 12 - Run the complete dashboard

Run:

```bash
python src/dashboard.py
```

Verify:

```text
[ ] page loads
[ ] provider is visible
[ ] instrument is visible
[ ] benchmark is visible
[ ] period is visible
[ ] interval is visible
[ ] instrument return is visible
[ ] benchmark return is visible
[ ] relative performance is visible
[ ] base-100 chart displays both series
```

# Part 13 - Keep the terminal path useful

TD11 introduces Dash, but the application should not become impossible to debug from the terminal.

Where practical, keep:

```bash
python src/main.py
```

working as a simpler validation path.

The dashboard should reuse application logic rather than replace it with hidden duplicate calculations.

# Part 14 - Optional daily-return chart

Only after the required dashboard works.

You may add:

```text
Daily Returns
```

using the TD07 daily-return series.

Do not replace the base-100 chart.

The base-100 comparison remains the central required chart.

# Part 15 - Optional instrument volume chart

If time allows, add:

```text
Instrument Volume
```

This chart should normally focus on the primary instrument.

Benchmark volume may be unavailable or not directly meaningful depending on the provider.

Do not make benchmark volume a required feature.

# Part 16 - Avoid unnecessary callbacks

A static dashboard is sufficient for the TD11 core.

You do not need callbacks simply because Dash supports them.

Only introduce a callback if you implement an actual interaction such as:

```text
provider selector
instrument selector
```

The required dashboard can be rendered from prepared data without interactive callbacks.

# Part 17 - Optional provider selector

If the team finishes early, a simple dropdown may allow:

```text
CSV
Yahoo
Bloomberg
```

This is optional.

If implemented, provider selection should call the existing provider boundary.

Do not duplicate:

```text
analytics
layout
return formulas
```

for each provider.

# Part 18 - Styling scope

TD11 does not require professional visual design.

Priorities are:

```text
1. correct data
2. readable labels
3. understandable comparison
4. stable execution
5. visual polish
```

Avoid spending the whole session on colors, fonts or spacing.

# Part 19 - Git validation

Before committing:

```bash
git status
git diff
```

Expected changes may include:

```text
requirements.txt
src/dashboard.py
src/dashboard.py
src/main.py
```

Only include files actually required by your implementation.

Run:

```bash
python src/main.py
python src/dashboard.py
```

Verify both paths if your architecture supports them.

# Part 20 - Commit and push

Stage intended files.

Example:

```bash
git add requirements.txt
git add src/dashboard.py
git add src/dashboard.py
```

Add other files only if they changed intentionally.

Inspect:

```bash
git diff --staged
```

Commit:

```bash
git commit -m "feat: add MarketPulse Dash dashboard"
```

Push:

```bash
git push -u origin feature/dash-dashboard
```

# Part 21 - Open the Pull Request

Suggested title:

```text
feat: add MarketPulse Dash dashboard
```

Suggested description:

```markdown
## What changed

- add Dash application;
- display provider and market configuration;
- display instrument return;
- display benchmark return;
- display relative performance;
- add instrument vs benchmark base-100 chart.

## Validation

- ran MarketPulse terminal path;
- ran Dash application;
- verified both series use common dates;
- verified both base-100 series start at 100;
- verified dashboard values match analytical output.
```

Another team member reviews before merge.

# Part 22 - Review points

The reviewer should verify:

```text
[ ] dashboard does not hard-code market results
[ ] provider logic is not duplicated in the layout
[ ] instrument is visible
[ ] benchmark is visible
[ ] lookback is visible
[ ] interval is visible
[ ] period returns are visible
[ ] relative performance is visible
[ ] base-100 chart contains two aligned series
[ ] no credentials are exposed
[ ] dependencies are recorded
```

# Part 23 - Relationship with Checkpoint C

Checkpoint C is performed after TD12.

One required screenshot is:

```text
02_dash_dashboard.png
```

This screenshot should show at minimum:

```text
Instrument
Benchmark
Lookback
Interval
Instrument return
Benchmark return
Relative performance
Base-100 comparison chart
```

The screenshot must demonstrate a functional comparative dashboard.

A screenshot showing only:

```text
Dash is running
```

is not sufficient.

# Part 24 - Dashboard evidence preparation

Before taking the future Checkpoint C screenshot:

1. use a valid provider;
2. confirm the selected instrument;
3. confirm the benchmark;
4. confirm the period;
5. confirm the interval;
6. verify returns;
7. verify relative performance;
8. verify both base-100 series;
9. ensure no credentials are visible.

Do not capture browser tabs, terminals or interface areas that expose sensitive information.

# Part 25 - Mini exercises

## Exercise 1 - Check dashboard consistency

Compare:

```text
terminal instrument return
dashboard instrument return
```

They should match for the same data.

Repeat for the benchmark.

## Exercise 2 - Check base 100

Read the first visible values of both chart series.

Explain why both begin at 100.

## Exercise 3 - Change provider

If your project supports provider selection, switch from one provider to another.

Question:

> Which dashboard code changed?

Ideally, little or none.

## Exercise 4 - Explain the architecture

To another student, explain:

```text
provider
-> canonical rows
-> analytics
-> dashboard data
-> Dash
```

# Part 26 - If you finish early

## Challenge 1 - Add daily returns

Add a second chart for daily returns.

Keep it secondary to the base-100 chart.

## Challenge 2 - Add volume

Add an instrument-volume chart.

Do not assume benchmark volume is meaningful.

## Challenge 3 - Add a dropdown

Add a simple provider or instrument selector.

Keep callbacks small.

## Challenge 4 - Separate layout

If `app.py` becomes difficult to read, move layout construction into:

```text
src/dashboard.py
```

Do this only if the refactoring improves clarity.

# Part 27 - Troubleshooting

## ModuleNotFoundError: dash

Run:

```bash
python -m pip install -r requirements.txt
```

Verify:

```bash
python -m pip show dash
```

## ModuleNotFoundError: plotly

Verify that:

```text
plotly
```

is recorded in `requirements.txt` if your code imports it directly.

## Dashboard starts but chart is empty

Inspect the data before blaming Dash.

Check:

```text
instrument_base_100
benchmark_base_100
common dates
```

## One chart series starts above or below 100

Inspect the base-100 formula.

The first aligned observation should map to:

```text
100
```

## Dashboard values differ from terminal values

Verify that both paths use:

```text
same provider
same instrument
same benchmark
same dates
same interval
```

## Import path error

Check the repository structure and run from the project root.

Do not solve import problems by copying analytical code into the dashboard.

# Part 28 - Readiness check

Before finishing TD11, each student should be able to explain:

```text
[ ] Dash's role in MarketPulse
[ ] presentation layer vs analytics
[ ] why dashboard values should not be hard-coded
[ ] why base 100 is the main comparison chart
[ ] why instrument and benchmark dates must align
[ ] how Dash receives MarketPulse results
[ ] why provider logic should stay outside the dashboard
[ ] why requirements.txt must include direct dependencies
```

Each student should also confirm:

```text
[ ] I used a feature branch
[ ] I created identifiable commits
[ ] I pushed the branch
[ ] I opened or contributed to a Pull Request
[ ] another student reviewed the change
[ ] dashboard starts successfully
[ ] required summary information is visible
[ ] base-100 chart contains both series
[ ] no credentials are visible
```

# Part 29 - What comes next?

MarketPulse now has:

```text
market data
+
provider abstraction
+
comparison analytics
+
visual dashboard
```

The final business requirement is:

```text
"We need a reproducible version of MarketPulse that another person can run."
```

TD12 will therefore focus on:

```text
integration
documentation
fresh setup
reproducible run
final Pull Request
Checkpoint C
```

TD12 closes the 18-hour practical sequence.
