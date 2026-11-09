[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/init.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda init`[#](https://docs.conda.io/projects/conda/en/stable/commands/init.html#conda-init "Link to this heading")

=====================================================================================================================

Initialize conda for shell interaction.

usage: conda init \[\-h\] \[\--all\] \[\--condabin\] \[\--user\] \[\--no\-user\] \[\--system\]
                  \[\--reverse\] \[\--json\] \[\--console {classic,json}\] \[\-v\] \[\-q\]
                  \[\-d\]
                  \[SHELLS ...\]

Copy to clipboard

Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/init.html#conda-init-positional-arguments "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

SHELLS

Possible choices: bash, fish, tcsh, xonsh, zsh, powershell

One or more shells to be initialized. If not given, the default value is 'bash' on unix and 'cmd.exe' & 'powershell' on Windows. Use the '--all' flag to initialize all shells. Available shells: \['bash', 'fish', 'powershell', 'tcsh', 'xonsh', 'zsh'\]

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/init.html#conda-init-named-arguments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

\--all

Initialize all currently available shells.

\-d, --dry-run

Only display what would have been done.

setup type[#](https://docs.conda.io/projects/conda/en/stable/commands/init.html#conda-init-setup-type "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

\--condabin

Add 'condabin/' directory to PATH only. Does not install the shell function.

\--user

Initialize conda for the current user (default).

\--no-user

Don't initialize conda for the current user.

\--system

Initialize conda for all users on the system.

\--reverse

Undo effects of last conda init.

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/init.html#conda-init-output-prompt-and-flow-control-options "Link to this heading")

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

Key parts of conda's functionality require that it interact directly with the shell within which conda is being invoked. The conda activate and conda deactivate commands specifically are shell-level commands. That is, they affect the state (e.g. environment variables) of the shell context being interacted with. Other core commands, like conda create and conda install, also necessarily interact with the shell environment. They're therefore implemented in ways specific to each shell. Each shell must be configured to make use of them.

The --condabin option adds the "$CONDA\_PREFIX/condabin" directory to the PATH environment variable. This directory only contains the conda executable and does not contain other executables from other packages installed in the base environment. On most shells, a small snippet is added to the shell profile. For CMD, the PATH environment variable is modified directly in the registry.

This command makes changes to your system that are specific and customized for each shell. To see the specific files and locations on your system that will be affected before, use the '--dry-run' flag. To see the exact changes that are being or will be made to each location, use the '--verbose' flag.

IMPORTANT: After running conda init, most shells will need to be closed and restarted for changes to take effect.

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/init.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/init.rst.txt)