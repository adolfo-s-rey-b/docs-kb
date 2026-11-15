[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/rename.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda rename`[#](https://docs.conda.io/projects/conda/en/stable/commands/rename.html#conda-rename "Link to this heading")

===========================================================================================================================

Rename an existing environment.

This command renames a conda environment via its name (-n/--name) or its prefix (-p/--prefix).

The base environment and the currently-active environment cannot be renamed.

usage: conda rename \[\-h\] \[\-n ENVIRONMENT | \-p PATH\] \[\--json\]
                    \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\-d\] \[\-y\]
                    destination

Copy to clipboard

Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/rename.html#conda-rename-positional-arguments "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

destination

New name for the conda environment.

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/rename.html#conda-rename-target-environment-specification "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/rename.html#conda-rename-output-prompt-and-flow-control-options "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

Examples:

> conda rename -n test123 test321
> 
> conda rename --name test123 test321
> 
> conda rename -p path/to/test123 test321
> 
> conda rename --prefix path/to/test123 test321

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/rename.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/rename.rst.txt)