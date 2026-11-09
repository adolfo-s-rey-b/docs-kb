[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/env/remove.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda env remove`[#](https://docs.conda.io/projects/conda/en/stable/commands/env/remove.html#conda-env-remove "Link to this heading")

=======================================================================================================================================

Remove an environment.

Removes a provided environment. You must deactivate the existing environment before you can remove it.

usage: conda env remove \[\-h\] \[\--override\-frozen\] \[\-n ENVIRONMENT | \-p PATH\]
                        \[\--solver {libmamba,rattler}\] \[\--json\]
                        \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\-d\] \[\-y\]

Copy to clipboard

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/env/remove.html#conda-env-remove-named-arguments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

\--override-frozen

DANGEROUS. Use at your own risk. Ignore protections if the environment is frozen.

\--solver

Possible choices: libmamba, rattler

Choose which solver backend to use.

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/env/remove.html#conda-env-remove-target-environment-specification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/env/remove.html#conda-env-remove-output-prompt-and-flow-control-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

> conda env remove --name FOO conda env remove -n FOO

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/env/remove.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/env/remove.rst.txt)