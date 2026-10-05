# INS-LNX-01 - Unix Philosophy

Status:

```text
INSTRUCTOR_READY
```

Primary teaching moment:

```text
TD01 - Bootstrap + Linux
```

## 1. Purpose

Give the instructor a short conceptual explanation for why command-line tools remain valuable even when graphical tools exist.

## 2. Student CORE boundary

Students need only the commands required to inspect and run MarketPulse:

```text
pwd
ls
cd
cat
head
grep
```

Pipes, awk, sed and shell scripting are not mandatory TD01 outcomes.

## 3. Instructor mental model

A useful Unix-inspired frame is:

```text
small tools
+
text streams
+
composition
+
clear interfaces
```

Commands become more powerful when their input and output can be connected.

This is cultural context, not a requirement to teach the full Unix tradition.

## 4. Best teaching moment

Use when students ask:

```text
Why use a terminal?
Why use grep instead of opening the file?
Why are so many tools text-based?
```

A 2 to 4 minute explanation is enough for CORE.

## 5. Short explanation

Example:

```text
cat
reads text

grep
filters text

head
limits text

pipes
can connect tools
```

The key idea is not the specific command.

It is:

```text
each tool has a small responsibility
```

## 6. Worked example

CORE-safe:

```bash
head data/sample/prices.csv
grep AAPL data/sample/prices.csv
```

Optional instructor demonstration:

```bash
grep AAPL data/sample/prices.csv | head
```

Explain the pipe as:

```text
stdout of the first command
becomes input to the second command
```

Do not make the pipe required if it has not yet been taught.

## 7. Common misconception

Misconception:

```text
The terminal is an old-fashioned user interface.
```

Correction:

```text
It is also a composable automation interface used heavily in engineering workflows.
```

Misconception:

```text
Linux means Bash.
```

Correction:

```text
Linux, shell and command-line tools are related but distinct concepts.
```

## 8. Stop point

Do not expand TD01 into mandatory:

```text
awk
sed
regex
shell scripting
process management
system administration
```

Those belong to optional advanced material.

## 9. Source discipline

Historical context:

```text
CM0
CM1
TD1.3
```

Current student source:

```text
docs/labs/TD01_BOOTSTRAP_LINUX.md
```

The note preserves conceptual depth while respecting the frozen CORE.

## 10. Optional extension

After CORE completion, direct interested students toward:

```text
ADV-LNX-03 - Pipes and text processing
```

Do not convert the extension into a hidden prerequisite.
