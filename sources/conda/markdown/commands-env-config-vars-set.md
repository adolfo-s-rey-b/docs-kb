[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/set.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda env config vars set`[#](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/set.html#conda-env-config-vars-set "Link to this heading")

==================================================================================================================================================================

Set environment variables for a conda environment.

usage: conda env config vars set \[\-h\] \[\-n ENVIRONMENT | \-p PATH\] \[vars ...\]

Copy to clipboard

Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/set.html#conda-env-config-vars-set-positional-arguments "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

vars

Environment variables to set in the form <KEY>=<VALUE> separated by spaces

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/env/config/vars/set.html#conda-env-config-vars-set-target-environment-specification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Example:

> conda env config vars set MY\_VAR=foo

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/env/config/vars/set.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/env/config/vars/set.rst.txt)