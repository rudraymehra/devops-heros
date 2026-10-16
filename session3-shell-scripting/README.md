# Shell Scripting Homework

## Screenshot evidence audit — 2026-10-16

See [this session's screenshot inventory and actual capture results](screenshots/README.md).
Missing native captures remain marked pending; historical logs are not relabelled as fresh screenshots.

`system-info.sh` completes the assigned system-information script. It uses variables,
interactive input, `mkdir`, `touch`, `date`, `hostname`, `whoami`, `df`, `ps`, and
output redirection.

```bash
chmod +x system-info.sh
./system-info.sh
cat system-info-output/report.txt
head system-info-output/processes.txt
```

The generated output directory is runtime evidence and should be reviewed for
sensitive information before committing it.

## Evidence checklist

- [x] Script syntax checked; actual local attempt recorded in [evidence](screenshots/README.md).
- [ ] Successful process/report output and native screenshot: process inspection is blocked in the editing sandbox.
- [x] Public repository: https://github.com/rudraymehra/devops-heros
