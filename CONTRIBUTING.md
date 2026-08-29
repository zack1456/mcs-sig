# Contributing literature

You do not need to understand JSON or Git hooks to suggest a source.

## Easiest path: submit an identifier

From the repository folder, run one of these commands with a DOI, PMID, URL, or citation:

```powershell
.\scripts\literature.ps1 add "10.1000/example-doi" --notes "Relevant to PBPK qualification"
```

```text
python scripts/literature.py add "10.1000/example-doi" --notes "Relevant to PBPK qualification"
```

This creates a small intake note. It does **not** publish a source record or claim that an LLM extraction has been scientifically reviewed.

## Check your work

```powershell
.\scripts\literature.ps1 check
```

The final message has one of three meanings:

- **Safe to submit:** automated checks passed.
- **Safe to commit, with review items:** your work is preserved, but a maintainer should review the listed items.
- **Cannot submit yet:** a clear structural error must be corrected. The checker does not delete or revert files.

If the checker says an item is automatically repairable, run:

```powershell
.\scripts\literature.ps1 fix
```

Then run `check` again.

## Review status

Automated checks confirm repository consistency, not scientific truth. New LLM-assisted source records start with `review_status: "draft"`. A person should change this to `"reviewed"` only after comparing the claims and numerical findings with the material actually accessed. Reviewed records must also include `reviewed_by` and `reviewed_date`; `review_notes` can document the scope or caveats of that review.

## Git and GitHub

The repository may run the same check before a commit and again on GitHub. If a check fails, your work has not been erased. Read the first `ERROR` message, use the suggested command, or ask a maintainer for help.

Maintainers who want the automatic check before each local commit can install it once. If this repository already has a working local `.venv`, activate it first:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pre_commit --version
```

If the version command succeeds, `pre-commit` is already installed in the environment and you do **not** need to install from `requirements-dev.txt` again. Install or update the development requirements only when `pre-commit` is missing, the `.venv` has been recreated, or `requirements-dev.txt` has changed:

```text
python -m pip install -r requirements-dev.txt
```

Installing the Git hook is a separate, one-time step for each clone of the repository, even when the `.venv` already exists:

```text
python -m pre_commit install
```

This setup is optional for contributors using GitHub's web interface; GitHub will run the offline check for them.

The installed local hook creates its own small Python environment and works on Windows, macOS, and Linux. The PowerShell launcher is only a Windows convenience; `python scripts/literature.py check` is the portable source-of-truth command used by the hook and GitHub.

Maintainers can manually run online DOI/PMID verification when appropriate:

```text
python -m pre_commit run verify-source-identifiers-online --hook-stage manual --all-files
```

Temporary network failures are reported for review without being mistaken for false identifiers. Confirmed identifier or metadata mismatches fail this manual check.

For the full maintenance contract, see `aiml_wg/sources/MAINTENANCE.md`.
