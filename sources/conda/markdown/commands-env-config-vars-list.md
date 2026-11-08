[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/list.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda env config vars list`[#](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/list.html#conda-env-config-vars-list "Link to this heading")

=====================================================================================================================================================================

List environment variables for a conda environment.

usage: conda env config vars list \[\-h\] \[\-n ENVIRONMENT | \-p PATH\] \[\--json\]
                                  \[\--console {classic,json}\] \[\-v\] \[\-q\]

Copy to clipboard

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/list.html#conda-env-config-vars-list-target-environment-specification "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/list.html#conda-env-config-vars-list-output-prompt-and-flow-control-options "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\--json

Report all output as json. Suitable for using conda programmatically.

\--console

Possible choices: classic, json

Select the backend to use for normal output rendering.

\-v, --verbose

Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.

\-q, --quiet

Do not display progress bar.

Example:

> conda env config vars list -n my\_env

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/env/config/vars/list.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/env/config/vars/list.rst.txt)