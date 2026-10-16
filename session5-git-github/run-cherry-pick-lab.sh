#!/usr/bin/env bash
set -euo pipefail

lab_directory=$(mktemp -d /tmp/git-homework.XXXXXX)
cd "$lab_directory"

git init --initial-branch=main --quiet
git config user.name "Rudray Mehra"
git config user.email "rudray.24bcs10425@sst.scaler.com"
git config commit.gpgsign false

printf 'first line\n' > notes.txt
git add notes.txt
git commit --quiet -m "Add initial notes"

printf 'second line\n' >> notes.txt
git commit --quiet -a -m "Update tracked notes with commit -a"

printf 'untracked content\n' > untracked.txt
printf '%s\n' 'Status after commit -a (new file remains untracked):'
git status --short
rm untracked.txt

git switch --quiet -c feature/cherry-pick-demo
printf 'selected change\n' > selected.txt
git add selected.txt
git commit --quiet -m "Add selected demonstration change"
selected_commit=$(git rev-parse HEAD)

printf 'feature-only change\n' > feature-only.txt
git add feature-only.txt
git commit --quiet -m "Add feature-only change"

git switch --quiet main
git cherry-pick "$selected_commit" >/dev/null

test -f selected.txt
test ! -f feature-only.txt
printf '\nCherry-pick verification passed. Branch graph:\n'
git log --oneline --graph --decorate --all
git log -1 --format='Lab commit author: %an <%ae>'
printf '\nDisposable lab retained for inspection: %s\n' "$lab_directory"
