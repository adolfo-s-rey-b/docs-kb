[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/compare.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda compare`[#](https://docs.conda.io/projects/conda/en/stable/commands/compare.html#conda-compare "Link to this heading")

==============================================================================================================================

Compare packages between conda environments.

usage: conda compare \[\-h\] \[\--json\] \[\--console {classic,json}\] \[\-v\] \[\-q\]
                     \[\-n ENVIRONMENT | \-p PATH\]
                     file

Copy to clipboard

Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/compare.html#conda-compare-positional-arguments "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

file

Path to the environment file that is to be compared against.

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/compare.html#conda-compare-output-prompt-and-flow-control-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\--json

Report all output as json. Suitable for using conda programmatically.

\--console

Possible choices: classic, json

Select the backend to use for normal output rendering.

\-v, --verbose

Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.

\-q, --quiet

Do not display progress bar.

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/compare.html#conda-compare-target-environment-specification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Examples:

Compare packages in the current environment with respect to 'environment.yml' located in the current working directory:

> conda compare environment.yml

Compare packages installed into the environment 'myenv' with respect to 'environment.yml' in a different directory:

> conda compare -n myenv path/to/file/environment.yml

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/compare.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/compare.rst.txt)