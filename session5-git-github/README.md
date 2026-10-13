# Git Homework

**Student:** Sudhir Mehra | **Roll number:** 24 BCS 10425 | **Batch:** B

## Task 1: `git commit -a -m` versus `git commit -m`

`git commit -m "message"` commits only changes already staged with `git add`.
`git commit -a -m "message"` automatically stages modifications and deletions of
tracked files, then commits them. It does not include new untracked files.

Safe practice sequence in a disposable repository:

```bash
mkdir git-homework-demo && cd git-homework-demo
git init
git config user.name "Sudhir Mehra"
git config user.email "rudray.24bcs10425@sst.scaler.com"
printf 'first\n' > notes.txt
git add notes.txt
git commit -m "Add initial notes"
printf 'second\n' >> notes.txt
git commit -a -m "Update tracked notes"
printf 'new\n' > untracked.txt
git status --short
```

The last status shows `untracked.txt` because `-a` never stages new files.

## Task 2: cherry-pick

```bash
git switch -c feature/cherry-pick-demo
printf 'selected change\n' > selected.txt
git add selected.txt
git commit -m "Add selected demonstration change"
selected_commit=$(git rev-parse HEAD)

printf 'feature-only change\n' > feature-only.txt
git add feature-only.txt
git commit -m "Add feature-only change"

git switch main
git cherry-pick "$selected_commit"
git log --oneline --graph --decorate --all
test -f selected.txt
test ! -f feature-only.txt
```

Cherry-pick creates a new commit on `main` containing the selected commit's patch;
it does not merge the complete feature branch.

## Evidence checklist

- [x] Replace the example name with your own identity (set your GitHub email before running).
- [ ] Add `git status --short` output demonstrating the `-a` behavior.
- [ ] Add the final `git log --oneline --graph --decorate --all` output.
- [ ] Add the public repository URL or submission screenshot.
