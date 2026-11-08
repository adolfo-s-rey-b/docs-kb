[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda doctor`[#](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html#conda-doctor "Link to this heading")

===========================================================================================================================

Display a health report for your environment by running registered health checks.

Tip

`conda check` is an alias for `conda doctor`. Use whichever you prefer!

Fixing Issues[#](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html#fixing-issues "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

Use `conda doctor --fix` to automatically fix issues that have available fixes. When a health check detects a problem and has an associated fix, the `--fix` flag will attempt to repair it.

By default, fixes will prompt for confirmation before making changes. Use `--yes` to skip confirmation prompts, or `--dry-run` to see what would be changed without actually making modifications.

Example:

\# Check environment health
conda doctor

\# Fix issues automatically (with confirmation prompts)
conda doctor \--fix

\# Fix issues without prompts
conda doctor \--fix \--yes

\# Preview fixes without applying them
conda doctor \--fix \--dry\-run

Copy to clipboard

Built-in Health Checks[#](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html#built-in-health-checks "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

Use `conda doctor --list` to see all available health checks and their fix capabilities. Conda includes several built-in health checks:

*   `missing-files` - Detects packages with missing files and can reinstall them
    
*   `altered-files` - Detects packages with modified files (checksum mismatch) and can reinstall them
    
*   `consistency` - Checks for missing or inconsistent dependencies
    
*   `environment-txt` - Verifies the environment is registered in `environments.txt`
    
*   `pinned` - Validates the format of the `pinned` file
    
*   `file-locking` - Reports if file locking is supported
    
*   `requests-ca-bundle` - Validates the SSL certificate bundle configuration
    

You can run specific health checks by name:

conda doctor missing\-files altered\-files

Copy to clipboard

Display a health report for your environment.

usage: conda doctor \[\-h\] \[\-n ENVIRONMENT | \-p PATH\] \[\--override\-frozen\]
                    \[\--json\] \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\-d\] \[\-y\]
                    \[\--list\] \[\--fix\]
                    \[NAME ...\]

Copy to clipboard

### Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html#conda-doctor-positional-arguments "Link to this heading")

NAME

Health check names to run (default: all). Use --list to see available checks.

### Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html#conda-doctor-named-arguments "Link to this heading")

\--override-frozen

DANGEROUS. Use at your own risk. Ignore protections if the environment is frozen.

\--list

List all available health checks and their fix capabilities.

\--fix, --heal

Fix issues found by health checks.

### Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html#conda-doctor-target-environment-specification "Link to this heading")

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

### Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html#conda-doctor-output-prompt-and-flow-control-options "Link to this heading")

\--json

Report all output as json. Suitable for using conda programmatically.

\--console

Possible choices: classic, json

Select the backend to use for normal output rendering.

\-v, --verbose

Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.

\-q, --quiet

Do not display progress bar.

\-d, --dry-run

Only display what would have been done.

\-y, --yes

Sets any confirmation values to 'yes' automatically. Users will not be asked to confirm any adding, deleting, backups, etc.

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/doctor.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/doctor.rst.txt)