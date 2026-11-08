[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/config.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda config`[#](https://docs.conda.io/projects/conda/en/stable/commands/config.html#conda-config "Link to this heading")

===========================================================================================================================

Modify configuration values in .condarc.

This is modeled after the git config command. Writes to the user .condarc file (/home/docs/.condarc) by default. Use the --show-sources flag to display all identified configuration locations on your computer.

usage: conda config \[\-h\] \[\--json\] \[\--console {classic,json}\] \[\-v\] \[\-q\]
                    \[\--system | \--env | \--file FILE | \-n ENVIRONMENT |\
                    \-p PATH\] \[\--show \[SHOW ...\] | \--show\-sources |\
                    \--validate | \--describe \[DESCRIBE ...\] | \--write\-default\]
                    \[\--get \[KEY ...\] | \--append KEY VALUE |\
                    \--prepend KEY VALUE | \--set KEY VALUE |\
                    \--remove KEY VALUE | \--clear KEY | \--remove\-key KEY |\
                    \--stdin\]

Copy to clipboard

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/config.html#conda-config-output-prompt-and-flow-control-options "Link to this heading")

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

Config File Location Selection[#](https://docs.conda.io/projects/conda/en/stable/commands/config.html#conda-config-config-file-location-selection "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Without one of these flags, the user config file at '/home/docs/.condarc' is used.

\--system

Write to the system .condarc file at '/home/docs/checkouts/readthedocs.org/user\_builds/continuumio-conda/conda/stable/.condarc'.

\--env

Write to the active conda environment .condarc file (<no active environment>). If no environment is active, write to the user config file (/home/docs/.condarc).

\--file

Write to the given file.

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Config Subcommands[#](https://docs.conda.io/projects/conda/en/stable/commands/config.html#conda-config-config-subcommands "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

\--show

Display configuration values as calculated and compiled. If no arguments given, show information for all configuration values.

\--show-sources

Display all identified configuration sources.

\--validate

Validate all configuration sources. Iterates over all .condarc files and checks for parsing errors.

\--describe

Describe given configuration parameters. If no arguments given, show information for all configuration parameters.

\--write-default

Write the default configuration to a file. Equivalent to conda config --describe > ~/.condarc.

Config Modifiers[#](https://docs.conda.io/projects/conda/en/stable/commands/config.html#conda-config-config-modifiers "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

\--get

Get a configuration value.

\--append

Add one configuration value to the end of a list key.

\--prepend, --add

Add one configuration value to the beginning of a list key.

\--set

Set a boolean or string key.

\--remove

Remove a configuration value from a list key.

This removes all instances of the value.

\--clear

Clear all values from a list key.

\--remove-key

Remove a configuration key (and all its values).

\--stdin

Apply configuration information given in yaml format piped through stdin.

See conda config --describe or [https://conda.io/docs/config.html](https://conda.io/docs/config.html)
 for details on all the options that can go in .condarc.

Examples:

Display all configuration values as calculated and compiled:

> conda config --show

Display all identified configuration sources:

> conda config --show-sources

Print the descriptions of all available configuration options to your command line:

> conda config --describe

Print the description for the "channel\_priority" configuration option to your command line:

> conda config --describe channel\_priority

Add the conda-canary channel:

> conda config --add channels conda-canary

Set the output verbosity to level 3 (highest) for the current activate environment:

> conda config --set verbosity 3 --env

Add the 'conda-forge' channel as a backup to 'defaults':

> conda config --append channels conda-forge

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/config.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/config.rst.txt)