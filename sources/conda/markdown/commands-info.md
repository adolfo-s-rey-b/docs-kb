[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/info.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda info`[#](https://docs.conda.io/projects/conda/en/stable/commands/info.html#conda-info "Link to this heading")

=====================================================================================================================

Display information about current conda install.

usage: conda info \[\-h\] \[\--json\] \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\-a\]
                  \[\--base\] \[\-e\] \[\-s\] \[\--size\] \[\--unsafe\-channels\]

Copy to clipboard

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/info.html#conda-info-named-arguments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

\-a, --all

Show all information.

\--base

Display base environment path.

\-e, --envs

List all known conda environments. Combine with \--json to obtain more details.

\-s, --system

List environment variables.

\--size

Show conda-managed disk usage for each environment (excludes untracked files created after installation).

\--unsafe-channels

Display list of channels with tokens exposed.

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/info.html#conda-info-output-prompt-and-flow-control-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\--json

Report all output as json. Suitable for using conda programmatically.

\--console

Possible choices: classic, json

Select the backend to use for normal output rendering.

\-v, --verbose

Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.

\-q, --quiet

Do not display progress bar.

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/info.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/info.rst.txt)