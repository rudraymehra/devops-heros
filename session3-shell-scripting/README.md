# Shell Scripting Homework

## Screenshot evidence audit — 2026-10-16

See [this session's screenshot inventory and actual capture results](screenshots/README.md).
Missing native captures remain marked pending; historical logs are not relabelled as fresh screenshots.

`system-info.sh` completes the assigned system-information script. It prints the
date, hostname, username, disk usage, and process list; uses variables and three
interactive prompts; creates a requested directory and `process.log`; and redirects
the process list into that file with `>`.

```bash
chmod +x system-info.sh
./system-info.sh
cat system-info-output/report.txt
head system-info-output/processes.txt
```

The generated output directory is runtime evidence and should be reviewed for
sensitive information before committing it.

## Evidence checklist

- [x] Script syntax checked; an earlier local attempt is recorded in [evidence](screenshots/README.md).
- [x] Run the corrected interactive script; [native capture](screenshots/rudray-20261023-091725/02-system-info-run.png) and [generated process file](devops/process.log) show the complete run.
- [x] The user confirmed `rudray` / `371` as the correct identity inputs for this assignment.
- [x] Public repository: https://github.com/rudraymehra/devops-heros
