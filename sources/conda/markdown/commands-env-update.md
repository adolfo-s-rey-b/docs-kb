[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/env/update.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda env update`[#](https://docs.conda.io/projects/conda/en/stable/commands/env/update.html#conda-env-update "Link to this heading")

=======================================================================================================================================

Update the current environment based on environment file.

usage: conda env update \[\-h\]
                        \[\--environment\-specifier {cep\-24,environment\-yaml,env.yml,conda\-lock\-v1,conda\-lock,environment.yml,explicit,rattler\-lock\-v6,pixi,pixi\-lock\-v6,requirements.txt,requirements,reqs}\]
                        \[\--format FORMAT\] \[\--override\-frozen\]
                        \[\-n ENVIRONMENT | \-p PATH\] \[\-f FILE\] \[\--prune\]
                        \[\--json\] \[\--console {classic,json}\] \[\-v\] \[\-q\]
                        \[\--solver {libmamba,rattler}\]

Copy to clipboard

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/env/update.html#conda-env-update-named-arguments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

\--environment-specifier, --env-spec

Possible choices: cep-24, environment-yaml, env.yml, conda-lock-v1, conda-lock, environment.yml, explicit, rattler-lock-v6, pixi, pixi-lock-v6, requirements.txt, requirements, reqs

\--env-spec is deprecated and will be removed in 27.3. Use the \--format flag instead.

\--format

Possible choices: cep-24, environment-yaml, env.yml, conda-lock-v1, conda-lock, environment.yml, explicit, rattler-lock-v6, pixi, pixi-lock-v6, requirements.txt, requirements, reqs

Override auto-detection of the input file's format. See conda export --help for the formats available in your installation. Aliases are interchangeable with canonical names.

\--override-frozen

DANGEROUS. Use at your own risk. Ignore protections if the environment is frozen.

\-f, --file

environment definition (default: environment.yml)

\--prune

remove installed packages not defined in environment.yml

\--solver

Possible choices: libmamba, rattler

Choose which solver backend to use.

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/env/update.html#conda-env-update-target-environment-specification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/env/update.html#conda-env-update-output-prompt-and-flow-control-options "Link to this heading")

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

Examples:

> conda env update conda env update -n=foo conda env update -f=/path/to/environment.yml conda env update --name=foo --file=environment.yml conda env update vader/deathstar

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/env/update.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/env/update.rst.txt)