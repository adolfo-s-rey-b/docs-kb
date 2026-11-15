[Skip to main content](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-commands.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

Commands[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-commands.html#commands "Link to this heading")

====================================================================================================================================

The `conda` command is the primary command-line interface for managing conda environments and packages. You can use conda commands to create environments, install packages, update packages, remove packages, search for packages, and inspect your current conda configuration.

Common commands[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-commands.html#common-commands "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Some of the most commonly used conda commands include:

`conda create`

Creates a new conda environment.

$ conda create \--name myenv python\=3.12

Copy to clipboard

`conda install`

Installs packages into the active environment or into a specified environment.

$ conda install numpy pandas

Copy to clipboard

`conda update`

Updates packages in an environment.

$ conda update numpy

Copy to clipboard

`conda remove`

Removes packages from an environment.

$ conda remove numpy

Copy to clipboard

Other commands are available for managing channels, listing environments, searching for packages, cleaning package caches, and viewing conda configuration.

Tip

You can abbreviate many frequently used command options that are preceded by two dashes (`--`) to one dash and the first letter of the option. For example, `--name` and `--envs` can be written as `-n` and `-e`.

Getting help for commands[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-commands.html#getting-help-for-commands "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use `--help` or `-h` to see help for conda itself or for an individual command.

To see top-level conda help:

$ conda \--help

Copy to clipboard

To see help for a specific command:

$ conda install \--help

Copy to clipboard

or:

$ conda install \-h

Copy to clipboard

For full usage of each command, including abbreviations, see [commands](https://docs.conda.io/projects/conda/en/stable/commands/index.html)
. You can see the same information at the command line by [viewing the command-line help](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/view-command-line-help.html)
.

Plugin commands[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-commands.html#plugin-commands "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

Conda plugins can add their own commands or subcommands to the conda command-line interface. For example, a plugin may add a command for a custom workflow, package source, or environment management task.

Plugins that add conda commands must be installed in the `base` environment, where conda itself is installed. You can use `conda self install` to install a plugin into the `base` environment. Installing a plugin into another environment does not make its command available to the main `conda` command.

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/user-guide/concepts/conda-commands.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/user-guide/concepts/conda-commands.rst.txt)