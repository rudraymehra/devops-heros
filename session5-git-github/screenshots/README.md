# Session 05 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 3. Native captures: 0 accepted; 0 awaiting review; 1 rejected.

## Fresh execution records

### [rudray-20261023-092609](rudray-20261023-092609/README.md)

- [Session 05 — complete isolated Git lab](rudray-20261023-092609/02-git-lab-complete.png): PASS. The screenshot shows `untracked.txt`, the successful cherry-pick, branch graph, and returned prompt.
- The paired [author pager capture](rudray-20261023-092609/01-author-pager-incomplete.png) is retained as incomplete; the pager remained open in that earlier image.

### [rudray-20261023-092416](rudray-20261023-092416/README.md)

- The isolated Git lab reached the branch graph, but this capture only shows the pager tail. It omits the `commit -a` status and the returned prompt, so it is retained as incomplete evidence. The helper now disables Git's pager; rerun it and capture the full output.
- [Pager-tail capture](rudray-20261023-092416/01-pager-tail-incomplete.png)

### [rudray-20261016-212856-656600](rudray-20261016-212856-656600/README.md)

- [Session 05 — actual isolated Git lab](rudray-20261016-212856-656600/01-commit-and-cherry-pick.txt): PASS.
- Reference-specific pending items: NOT RUN: Capture real commit -a status and cherry-pick graph in the disposable lab, not the dirty coursework repository..

### [rudray-20261016-215104-093414](rudray-20261016-215104-093414/README.md)

- [Session 05 — actual isolated Git lab](rudray-20261016-215104-093414/01-commit-and-cherry-pick.txt): PASS.
- Native capture REJECTED: Wrong window: chat conversation instead of Git lab output. Retake the terminal capture; the actual Git log is retained.
- Reference-specific pending items: NOT RUN: Capture real commit -a status and cherry-pick graph in the disposable lab, not the dirty coursework repository..


## Rendered record images (not native screenshots)

[View generated images of our actual logs/recorded CI metadata](rendered-log-views/README.md).
These are explicitly labelled renderings. They do not change native-capture counts or turn failures into passes.


## Existing historical evidence

- [Earlier GitHub Actions run](https://github.com/rudraymehra/devops-heros/actions/runs/38372002674)

Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.

## Historical capture context

The pending note below predates the successful host capture documented above.

Use the [coursework capture guide](../../COURSEWORK-EVIDENCE.md). The helper displays Rudray Mehra around freshly executed commands.

## Reference image inventory (not copied)

- `screenshots/task1-commit-a-vs-commit-01.png`
- `screenshots/task2-cherry-pick-01.png`
- `screenshots/task2-cherry-pick-02.png`

## Checked source files

- [run-cherry-pick-lab.sh](../run-cherry-pick-lab.sh)
