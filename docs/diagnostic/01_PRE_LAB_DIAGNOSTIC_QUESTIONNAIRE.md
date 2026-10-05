# ESILV Python, Git, Linux - Pre-Lab Diagnostic Questionnaire

## Status

```text
Teacher reference copy
Not a graded exam
39 questions
13 Linux + 13 Git + 13 Python
```

No answer key is included. Personal account and messaging metadata are intentionally excluded.

## Original instructions

**ESILV - Python, Git, Linux: pre-lab diagnostic**

This is not a graded exam. Your answers will help us adapt the labs to the class. No previous Linux or Git experience is required; some Python fundamentals are expected. The final questions in each section explore topics you may not have studied yet.

Allow approximately 25-35 minutes (estimate to be checked with a pilot). Work individually without search, AI assistance, or running the commands/code. Choose one answer per question. Select "I don't know yet" instead of guessing. All code uses Python 3; shell questions use Bash on Linux. No Bloomberg access or finance knowledge is needed. No name or email is requested. Please submit once.

# Linux

13 questions. Choose one answer per question; use "I don't know yet" when needed.

## L01
Which command prints the absolute path of your current directory?

- `ls`
- `pwd`
- `cd`
- `mkdir`
- I don't know yet

## L02
Which command lists entries in the current directory, including hidden files?

- `ls -a`
- `pwd -a`
- `cd -a`
- `mkdir -a`
- I don't know yet

## L03
You are in `/home/student/project`. What is your working directory after running `cd ..`?

- `/home`
- `/home/student/project`
- `/`
- `/home/student`
- I don't know yet

## L04
Which command creates a directory named `data` in the current directory, assuming it does not exist?

- `touch data`
- `cd data`
- `mkdir data`
- `cat data`
- I don't know yet

## L05
Which command displays the entire contents of a small text file named `prices.csv`?

- `cat prices.csv`
- `cd prices.csv`
- `mkdir prices.csv`
- `pwd prices.csv`
- I don't know yet

## L06
The directory `backup` already exists. Which command copies `prices.csv` into it while keeping the original?

- `mv prices.csv backup/`
- `cp prices.csv backup/`
- `rm prices.csv`
- `cd prices.csv backup/`
- I don't know yet

## L07
Which command prints lines containing the case-sensitive text `ERROR` from `app.log`?

- `cat ERROR app.log`
- `find ERROR app.log`
- `grep "ERROR" app.log`
- `cd ERROR app.log`
- I don't know yet

## L08
Assume `app.log` is a text file. What does this command count?

```bash
grep "ERROR" app.log | wc -l
```

- Characters in `app.log`
- All lines in `app.log`
- Files named `ERROR`
- Lines containing `ERROR`
- I don't know yet

## L09
In Bash with default settings, `report.txt` already exists. What does this command do?

```bash
printf "done\n" > report.txt
```

- Appends `done` to the file
- Replaces the file contents with `done` and a newline
- Prints only to the terminal
- Renames the file
- I don't know yet

## L10
You own `run.sh`. Which command adds execute permission for you without removing existing permissions?

- `chmod u+x run.sh`
- `chmod u-x run.sh`
- `chown +x run.sh`
- `mkdir run.sh`
- I don't know yet

## L11
A program writes diagnostics to standard error. Which Bash command saves standard output and standard error in `run.log`?

- `python3 app.py > run.log`
- `python3 app.py 2> run.log`
- `python3 app.py > run.log 2>&1`
- `python3 app.py < run.log`
- I don't know yet

## L12
A Bash script contains:

```bash
export DATA_DIR=/tmp/data
python3 load.py
```

How can `load.py` access `DATA_DIR` using the Python standard library?

- It becomes a Python variable automatically
- By importing `DATA_DIR` as a module
- Only by reading the Bash script file
- Using `os.environ["DATA_DIR"]` after importing `os`
- I don't know yet

## L13
In Bash, what does this command do?

```bash
python3 fetch.py && python3 dashboard.py
```

- Runs both commands simultaneously
- Runs `dashboard.py` only if `fetch.py` exits with status 0
- Runs `dashboard.py` only if `fetch.py` fails
- Always runs `dashboard.py` after `fetch.py`
- I don't know yet

# Git

13 questions. Choose one answer per question; use "I don't know yet" when needed.

## G01
What is the main purpose of Git?

- Run Python code faster
- Host every project on a public website
- Track changes and support collaboration on files
- Replace the operating system
- I don't know yet

## G02
What does `git clone <repository-url>` normally create?

- A local repository containing project history and a working copy
- Only an empty folder
- A new account on the hosting service
- A pull request
- I don't know yet

## G03
Which command shows staged changes, unstaged changes, and untracked files?

- `git log`
- `git push`
- `git branch`
- `git status`
- I don't know yet

## G04
What does `git add analysis.py` do?

- Publishes the file online
- Stages the current contents of `analysis.py` for a commit
- Deletes earlier versions
- Creates a new branch
- I don't know yet

## G05
What does `git commit -m "Add analysis"` normally do?

- Uploads all local files to every remote
- Stages every untracked file
- Records staged changes in local history
- Deletes the staging area permanently
- I don't know yet

## G06
Which command creates a branch named `feature` and switches to it, assuming it does not already exist?

- `git switch -c feature`
- `git switch main`
- `git clone feature`
- `git add feature`
- I don't know yet

## G07
You have committed on `feature`. The remote `origin` exists and you have permission. Which command pushes `feature` and sets its upstream?

- `git fetch origin feature`
- `git add origin feature`
- `git commit origin feature`
- `git push -u origin feature`
- I don't know yet

## G08
What does `git fetch origin` normally do?

- Automatically resolves every conflict
- Downloads remote objects and updates remote-tracking references without merging into your current branch
- Deletes local commits absent from `origin`
- Commits your unstaged changes
- I don't know yet

## G09
On a repository hosting platform, what is a pull request typically used for?

- Requesting permission to install Git
- Automatically copying files into Linux
- Proposing branch changes for review and possible merge
- Replacing local commits with screenshots
- I don't know yet

## G10
On a hosting platform, how does a fork differ from a branch?

- A fork is a separate hosted repository; a branch is a line of development within a repository
- A fork contains no history; a branch contains all repositories
- They are both Linux folders only
- A branch must be public; a fork must be private
- I don't know yet

## G11
A tracked file starts at version A. You edit it to B, run `git add`, then edit it to C. You run `git commit -m "Update"` with no other options. Which version is committed?

- A
- C
- Both B and C
- B
- I don't know yet

## G12
A merge stops with a content conflict in `analysis.py`. What is the appropriate next step?

- Run `git push` to resolve the conflict
- Inspect and reconcile the conflicting content, remove conflict markers, stage the resolved file, then complete the merge commit
- Delete the entire repository
- Run `git add` without inspecting the file and assume Git has fixed it
- I don't know yet

## G13
A file is already tracked and committed. What happens if you add its path to `.gitignore`?

- Its earlier commits are erased
- The remote file is deleted automatically
- It remains tracked; `.gitignore` does not untrack it
- Git encrypts the file
- I don't know yet

# Python

13 questions. Choose one answer per question; use "I don't know yet" when needed.

## P01
What does this Python 3 code print?

```python
x = "3"
print(int(x) + 2)
```

- `5`
- `32`
- `3`
- A `TypeError`
- I don't know yet

## P02
What does this code print?

```python
prices = [100, 105, 98]
print(prices[-1])
```

- `100`
- `105`
- An `IndexError`
- `98`
- I don't know yet

## P03
What does this code print?

```python
quote = {"symbol": "ABC", "price": 102}
print(quote["price"])
```

- `ABC`
- `102`
- `price`
- An empty dictionary
- I don't know yet

## P04
What does this code print?

```python
total = 0
for value in [2, 3, 4]:
    total += value
print(total)
```

- `4`
- `6`
- `9`
- `234`
- I don't know yet

## P05
What does this code print?

```python
def double(x):
    return 2 * x

print(double(3) + 1)
```

- `7`
- `6`
- `8`
- `None`
- I don't know yet

## P06
What is the value of `positive`?

```python
returns = [-2, 0, 3, 5]
positive = [r for r in returns if r > 0]
```

- `[-2, 0]`
- `[0, 3, 5]`
- `[True, True]`
- `[3, 5]`
- I don't know yet

## P07
What does this code print?

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

- `[1, 2]`
- `[1, 2, 3]`
- `[3]`
- `None`
- I don't know yet

## P08
What does this code print?

```python
try:
    value = float("N/A")
except ValueError:
    value = None
print(value)
```

- `0.0`
- `N/A`
- `None`
- An uncaught `ValueError`
- I don't know yet

## P09
Why use `with open("prices.csv") as f:` when reading a file?

- It closes the file when the block exits, including on an exception
- It automatically converts CSV rows into dictionaries
- It guarantees the file exists
- It downloads the latest prices
- I don't know yet

## P10
What is the main benefit of a Python virtual environment?

- It makes every algorithm faster
- It commits dependencies to Git automatically
- It provides free access to financial data
- It isolates a project's installed Python packages from other environments
- I don't know yet

## P11
A market-data API returns `{"price": null}`. After JSON decoding in Python, how should you handle the price before calculating a return?

- Assume the price is zero
- Check for `None` and apply an explicit missing-data policy
- Convert `None` to a float directly
- Treat the response as a valid positive price
- I don't know yet

## P12
In a Python project using Bloomberg data, which responsibility belongs to the data-access layer?

- Drawing every dashboard chart
- Committing the repository
- Managing the provider connection/session, requesting authorized data, and handling responses and errors
- Replacing all missing values with zero without reporting it
- I don't know yet

## P13
In a Dash app, a chart should update when a user selects another symbol in a dropdown. What normally connects the selection to the chart update?

- A callback with the dropdown value as an input and the figure as an output
- A Git commit
- A Linux file permission
- A Python comment above the chart
- I don't know yet

# End of questionnaire

Operational reminder:

```text
This questionnaire is diagnostic.
It is not a graded exam.
Do not interpret all 39 questions as mandatory prerequisites.
```

See:

```text
docs/diagnostic/02_PRE_LAB_DIAGNOSTIC_ANALYSIS.md
docs/diagnostic/03_PRE_LAB_DIAGNOSTIC_INTERPRETATION_GUIDE.md
```