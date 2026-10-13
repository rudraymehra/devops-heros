# Session 5 - Git / GitHub Homework

**Name:** Rudray Mehra
**GitHub:** [rudraymehra](https://github.com/rudraymehra)

All commands below were executed on my machine (macOS, `git version 2.39.5 (Apple Git-154)`) inside throwaway repositories created under `/tmp`. The outputs are pasted exactly as the terminal printed them. Short commit hashes will of course differ if someone re-runs the steps.

Setup used for both tasks:

```bash
mkdir /tmp/hwgit-demo && cd /tmp/hwgit-demo
git init -b main
git config user.name  "Rudray Mehra"
git config user.email "rudraymehra@gmail.com"
```

```text
Initialized empty Git repository in /private/tmp/hwgit-demo/.git/
```

---

## Task 1: `git commit -a -m` vs `git commit -m`

### Quick comparison

| | `git commit -m "msg"` | `git commit -a -m "msg"` |
| :--- | :--- | :--- |
| What gets committed | Only what is already in the staging area (index) | Everything in the index **plus** every *tracked* file that is modified or deleted |
| Needs `git add` first? | Yes, for every change you want in the commit | No, for tracked files. `-a` runs the equivalent of `git add -u` for you |
| New (untracked) files | Not included unless you `git add` them | **Still not included**. Git has never seen the file, so `-a` cannot pick it up |
| Behaviour when nothing is staged | Prints the status and exits with code 1, no commit is made | Creates the commit as long as at least one tracked file changed |
| Typical use | Careful, selective commits (partial staging, `git add -p`) | Fast "save my edits" commits when you touched only existing files |

### Step 1: Create the first tracked file and make the initial commit

```bash
echo "line 1: original content" > notes.txt
git add notes.txt
git commit -m "Initial commit: add notes.txt"
```

```text
[main (root-commit) 40ad0a0] Initial commit: add notes.txt
 1 file changed, 1 insertion(+)
 create mode 100644 notes.txt
```

Now `notes.txt` is a *tracked* file: Git knows about it and will notice future edits.

### Step 2: Modify the tracked file and create a brand new (untracked) file

```bash
echo "line 2: edited after first commit" >> notes.txt
echo "this file is brand new" > todo.txt
git status
```

```text
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   notes.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	todo.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Two different situations are visible here: `notes.txt` is *modified but not staged*, and `todo.txt` is *untracked*. Git itself hints at the two ways forward: `git add` or `git commit -a`.

### Step 3: Try `git commit -m` **without** running `git add`

```bash
git commit -m "Trying to commit without staging"
echo "exit code: $?"
```

```text
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   notes.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	todo.txt

no changes added to commit (use "git add" and/or "git commit -a")
exit code: 1
```

No commit was created. `git log` confirms that we still have only the initial commit:

```bash
git log --oneline
```

```text
40ad0a0 Initial commit: add notes.txt
```

### Step 4: Now run `git commit -a -m`

```bash
git commit -a -m "Update notes.txt using commit -a"
```

```text
[main 35a630e] Update notes.txt using commit -a
 1 file changed, 1 insertion(+)
```

This time the commit succeeded and it contains exactly **1 file**: the modified tracked file `notes.txt`.

### Step 5: Check what is left in the working tree

```bash
git status
```

```text
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	todo.txt

nothing added to commit but untracked files present (use "git add" to track)
```

```bash
git log --oneline
git show --stat HEAD
```

```text
35a630e Update notes.txt using commit -a
40ad0a0 Initial commit: add notes.txt
```

```text
commit 35a630e68a46d7acc9b2afe29cb63d45319e2237
Author: Rudray Mehra <rudraymehra@gmail.com>
Date:   Thu Sep 3 19:52:12 2026 +0530

    Update notes.txt using commit -a

 notes.txt | 1 +
 1 file changed, 1 insertion(+)
```

`todo.txt` is still sitting there as untracked. The `-a` flag did **not** add it. To get it into history I would still need `git add todo.txt && git commit -m "..."`.

### What I understood (Task 1)

- A commit is built from the **staging area**, never directly from the working directory. `git commit -m` only packages what I have already staged, which is why it refused to do anything in Step 3.
- `-a` is just a shortcut that stages every *already tracked* file that changed (modified or deleted) right before committing. It saves the `git add` step for edits to existing files.
- `-a` has no effect on **untracked** files. Git only auto-stages files it already knows about, so a new file always needs an explicit `git add` the first time. This is the single most important difference and the reason people accidentally leave new files out of a commit.
- The trade-off: `-a` is convenient but commits everything tracked in one go, so it is easy to sweep in an unrelated edit. When I want a focused commit I stage selectively with `git add <file>` (or `git add -p`) and use plain `-m`.

---

## Task 2: Git Cherry-Pick

`git cherry-pick <commit>` takes the *change* introduced by one specific commit and re-applies it as a brand new commit on the branch I am currently on. It is useful when only one commit from a feature branch is needed on `main` (for example a config fix) without merging the whole branch.

For this task I used a second throwaway repo, `/tmp/hwgit-cherry`, initialised the same way as above (`git init -b main` plus the local `user.name` / `user.email`).

### Step 1: Create 3 commits on `main`

```bash
echo "# Inventory Service" > README.md
git add README.md
git commit -m "main-1: add project README"

echo "APP_PORT=8080" > config.env
git add config.env
git commit -m "main-2: add default config"

echo "Run: ./start.sh" >> README.md
git commit -a -m "main-3: document how to start the service"
```

```text
[main (root-commit) ca46830] main-1: add project README
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

[main 7a14694] main-2: add default config
 1 file changed, 1 insertion(+)
 create mode 100644 config.env

[main da2d46e] main-3: document how to start the service
 1 file changed, 1 insertion(+)
```

(The third commit reuses `-a` from Task 1, since `README.md` was already tracked.)

### Step 2: View the commits on `main`

```bash
git log --oneline
```

```text
da2d46e main-3: document how to start the service
7a14694 main-2: add default config
ca46830 main-1: add project README
```

### Step 3: Create a new branch `feature` and make 3 commits there

```bash
git checkout -b feature

echo "def login(user, pwd): return True" > auth.py
git add auth.py
git commit -m "feature-1: add login stub"

echo "LOG_LEVEL=debug" >> config.env
git commit -a -m "feature-2: enable debug logging in config"

echo "def report(): print('weekly report')" > report.py
git add report.py
git commit -m "feature-3: add reporting script"
```

```text
Switched to a new branch 'feature'

[feature 9a45f41] feature-1: add login stub
 1 file changed, 1 insertion(+)
 create mode 100644 auth.py

[feature f6eef1e] feature-2: enable debug logging in config
 1 file changed, 1 insertion(+)

[feature 8281657] feature-3: add reporting script
 1 file changed, 1 insertion(+)
 create mode 100644 report.py
```

### Step 4: Use `git log` to identify the commit I want

```bash
git log --oneline
```

```text
8281657 feature-3: add reporting script
f6eef1e feature-2: enable debug logging in config
9a45f41 feature-1: add login stub
da2d46e main-3: document how to start the service
7a14694 main-2: add default config
ca46830 main-1: add project README
```

```bash
git log --oneline --graph --all
```

```text
* 8281657 feature-3: add reporting script
* f6eef1e feature-2: enable debug logging in config
* 9a45f41 feature-1: add login stub
* da2d46e main-3: document how to start the service
* 7a14694 main-2: add default config
* ca46830 main-1: add project README
```

At this point the graph is a straight line because `feature` simply continues from `main`; `main` still points at `da2d46e`.

**Target commit:** `f6eef1e` - `feature-2: enable debug logging in config`. The scenario is that the config change is needed on `main` right away, but the login stub (`feature-1`) and reporting script (`feature-3`) are not ready yet, so I do *not* want to merge the whole branch.

### Step 5: Switch back to `main` and cherry-pick that one commit

Before picking, I confirmed the state of `main`:

```bash
git checkout main
cat config.env
ls
```

```text
Switched to branch 'main'
```

```text
APP_PORT=8080
```

```text
config.env
README.md
```

Now the cherry-pick:

```bash
git cherry-pick f6eef1e
```

```text
[main 25204c5] feature-2: enable debug logging in config
 Date: Thu Sep 3 19:52:31 2026 +0530
 1 file changed, 1 insertion(+)
```

Notice the **new hash** `25204c5`. The message, author and original date were kept, but it is a different commit object because its parent is `da2d46e` on `main`, not `9a45f41` on `feature`.

### Step 6: Verify the change is now on `main`

```bash
git log --oneline
```

```text
25204c5 feature-2: enable debug logging in config
da2d46e main-3: document how to start the service
7a14694 main-2: add default config
ca46830 main-1: add project README
```

```bash
git log --oneline --graph --all
```

```text
* 25204c5 feature-2: enable debug logging in config
| * 8281657 feature-3: add reporting script
| * f6eef1e feature-2: enable debug logging in config
| * 9a45f41 feature-1: add login stub
|/
* da2d46e main-3: document how to start the service
* 7a14694 main-2: add default config
* ca46830 main-1: add project README
```

The graph now shows two branches diverging from `da2d46e`: `main` has the single cherry-picked commit `25204c5`, while `feature` still has its original three commits, including the original `f6eef1e`.

```bash
cat config.env
ls
```

```text
APP_PORT=8080
LOG_LEVEL=debug
```

```text
config.env
README.md
```

`LOG_LEVEL=debug` is present on `main`, and `auth.py` / `report.py` are **not** there, which proves only the selected commit came across.

```bash
git show --stat HEAD
```

```text
commit 25204c5e62a5feb6c806c21e06f3c47f8d01de25
Author: Rudray Mehra <rudraymehra@gmail.com>
Date:   Thu Sep 3 19:52:31 2026 +0530

    feature-2: enable debug logging in config

 config.env | 1 +
 1 file changed, 1 insertion(+)
```

One last sanity check comparing the snapshot of the original commit against the cherry-picked one:

```bash
git diff f6eef1e HEAD --stat
```

```text
 auth.py | 1 -
 1 file changed, 1 deletion(-)
```

The only difference between the two snapshots is `auth.py`, which exists in the `feature` history (from `feature-1`) but was never brought to `main`. The `config.env` content is identical, exactly as expected.

### What I understood (Task 2)

- Cherry-pick copies a **change** (the diff of one commit), not the branch. The result is a new commit with a new hash on the current branch; the original commit stays untouched on its own branch.
- Because only the diff is applied, the commits before it on the source branch (`feature-1` here) do not come along. That is the whole point when I need one fix from a branch that is otherwise unfinished.
- The same logical change now exists twice in history (`f6eef1e` on `feature`, `25204c5` on `main`). Git usually handles this fine when `feature` is later merged, but it is one reason to use cherry-pick deliberately for hotfixes/backports rather than as a replacement for merging.
- If the picked commit touches lines that were changed differently on the target branch, cherry-pick stops with a conflict; then I resolve the files, `git add` them and run `git cherry-pick --continue` (or `--abort` to back out).

---

## Cleanup

Both throwaway repositories were removed after the exercise:

```bash
rm -rf /tmp/hwgit-demo /tmp/hwgit-cherry
```
