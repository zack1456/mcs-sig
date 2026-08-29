# MCS SIG working repository

This repository contains planning documents, method workstreams, benchmark materials, and a structured literature library for the ISoP Mathematical and Computational Sciences Special Interest Group.

## Start here

- Working-group status and priorities: [`aiml_wg/STATUS.md`](aiml_wg/STATUS.md)
- Current work plan: [`aiml_wg/WORKPLAN.md`](aiml_wg/WORKPLAN.md)
- Literature contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Source-library maintenance contract: [`aiml_wg/sources/MAINTENANCE.md`](aiml_wg/sources/MAINTENANCE.md)

You do not need to know JSON or Git hooks to suggest a paper. Follow the identifier-intake instructions in `CONTRIBUTING.md`, or ask a maintainer for help.

## Quick offline check

```text
python scripts/literature.py check
```

On Windows, `scripts\literature.ps1 check` is an equivalent convenience command. Automated checks verify repository consistency, not scientific correctness; draft source records still require human review.
