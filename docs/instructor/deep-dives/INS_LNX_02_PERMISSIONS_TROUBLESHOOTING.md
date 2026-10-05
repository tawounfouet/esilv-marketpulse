# INS-LNX-02 - Permissions Troubleshooting

Status:

```text
INSTRUCTOR_READY
```

Primary teaching moments:

```text
TD01 troubleshooting
advanced SSH / remote Linux
```

## 1. Purpose

Provide a safe instructor mental model for diagnosing Linux permission problems without normalizing destructive or overly broad fixes.

## 2. Student CORE boundary

Students do not need a mandatory permissions lab in TD01.

They should only encounter permission concepts when they solve a real execution or access problem.

## 3. Instructor mental model

Classic Unix permission dimensions:

```text
owner
group
others
```

Permission types:

```text
read
write
execute
```

A file can therefore be inspectable but not executable, or executable by one class of user but not another.

For troubleshooting, always ask:

```text
Who owns the file?
Which permission is missing?
Which operation is failing?
```

## 4. Best teaching moment

Use when students see:

```text
Permission denied
```

or when an SSH private key has overly broad permissions.

Do not teach permissions abstractly for 20 minutes if no student problem requires it.

## 5. Short explanation

Useful inspection:

```bash
ls -l <path>
```

Mental model:

```text
permissions
=
policy about which operations identities may perform
```

A safe fix changes only the permission actually required.

## 6. Worked example

Suppose a script exists:

```bash
./run.sh
```

and execution fails.

Inspect:

```bash
ls -l run.sh
```

If execute permission is genuinely missing:

```bash
chmod u+x run.sh
```

Then retry.

The explanation is:

```text
add execute permission for the owner
```

not:

```text
make everything writable and executable
```

## 7. Common misconception

Misconception:

```text
chmod 777 fixes permission problems
```

Correction:

```text
777 is an overly broad permission change and should not be a generic troubleshooting response
```

Misconception:

```text
sudo is the normal fix when a command fails
```

Correction:

```text
first understand ownership, permission and the intended operation
```

## 8. Stop point

Do not turn the common course into Linux administration.

Avoid mandatory treatment of:

```text
ACLs
complex ownership models
setuid/setgid
system security policy
```

unless required by an advanced lab.

## 9. Source discipline

Historical sources include permissions, ownership, root and SSH-key handling.

Current safety rules prohibit:

```text
shared credentials
committed private keys
mandatory personal cloud accounts
```

See:

```text
docs/instructor/01_LEGACY_DEEP_DIVE_REFERENCE.md
docs/15_INSTRUCTOR_CONTINGENCY_AND_RECOVERY_PLAYBOOK.md
```

## 10. Optional extension

Use this note as conceptual preparation for:

```text
ADV-LNX-02 - Permissions and chmod
ADV-RMT-01 - SSH fundamentals
```

Those remain optional advanced activities.
