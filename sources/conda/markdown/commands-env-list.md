[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/env/list.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda env list`[#](https://docs.conda.io/projects/conda/en/stable/commands/env/list.html#conda-env-list "Link to this heading")

=================================================================================================================================

An alias for conda info --envs. Lists all conda environments.

usage: conda env list \[\-h\] \[\--json\] \[\--console {classic,json}\] \[\-v\] \[\-q\]
                      \[\--size\]

Copy to clipboard

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/env/list.html#conda-env-list-named-arguments "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

\--size

Show conda-managed disk usage for each environment (excludes untracked files created after installation).

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/env/list.html#conda-env-list-output-prompt-and-flow-control-options "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\--json

Report all output as json. Suitable for using conda programmatically.

\--console

Possible choices: classic, json

Select the backend to use for normal output rendering.

\-v, --verbose

Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.

\-q, --quiet

Do not display progress bar.

Examples:

> conda env list conda env list --json conda env list --size

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/env/list.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/env/list.rst.txt)