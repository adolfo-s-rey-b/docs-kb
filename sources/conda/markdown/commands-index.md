[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/index.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

Commands[#](https://docs.conda.io/projects/conda/en/stable/commands/index.html#commands "Link to this heading")

================================================================================================================

Conda provides many commands for managing packages and environments. The links on this page provide help for each command. You can also access help from the command line with the `--help` flag:

conda install \--help

Copy to clipboard

The following commands are part of conda:

*   [`conda activate`](https://docs.conda.io/projects/conda/en/stable/commands/activate.html)
    
*   [`conda clean`](https://docs.conda.io/projects/conda/en/stable/commands/clean.html)
    
*   [`conda compare`](https://docs.conda.io/projects/conda/en/stable/commands/compare.html)
    
*   [`conda config`](https://docs.conda.io/projects/conda/en/stable/commands/config.html)
    
*   [`conda create`](https://docs.conda.io/projects/conda/en/stable/commands/create.html)
    
*   [`conda deactivate`](https://docs.conda.io/projects/conda/en/stable/commands/deactivate.html)
    
*   [`conda doctor`](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html)
    
*   [`conda env`](https://docs.conda.io/projects/conda/en/stable/commands/env/index.html)
    
*   [`conda export`](https://docs.conda.io/projects/conda/en/stable/commands/export.html)
    
*   [`conda info`](https://docs.conda.io/projects/conda/en/stable/commands/info.html)
    
*   [`conda init`](https://docs.conda.io/projects/conda/en/stable/commands/init.html)
    
*   [`conda install`](https://docs.conda.io/projects/conda/en/stable/commands/install.html)
    
*   [`conda list`](https://docs.conda.io/projects/conda/en/stable/commands/list.html)
    
*   [`conda notices`](https://docs.conda.io/projects/conda/en/stable/commands/notices.html)
    
*   [`conda package`](https://docs.conda.io/projects/conda/en/stable/commands/package.html)
    
*   [`conda repoquery`](https://docs.conda.io/projects/conda/en/stable/commands/repoquery/index.html)
    
*   [`conda remove`](https://docs.conda.io/projects/conda/en/stable/commands/remove.html)
    
*   [`conda rename`](https://docs.conda.io/projects/conda/en/stable/commands/rename.html)
    
*   [`conda run`](https://docs.conda.io/projects/conda/en/stable/commands/run.html)
    
*   [`conda search`](https://docs.conda.io/projects/conda/en/stable/commands/search.html)
    
*   [`conda update`](https://docs.conda.io/projects/conda/en/stable/commands/update.html)
    
*   [`conda commands`](https://docs.conda.io/projects/conda/en/stable/commands/commands.html)
    

Conda vs. pip vs. virtualenv commands[#](https://docs.conda.io/projects/conda/en/stable/commands/index.html#conda-vs-pip-vs-virtualenv-commands "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you have used pip and virtualenv in the past, you can use conda to perform all of the same operations. Pip is a package manager and virtualenv is an environment manager. conda is both.

Scroll to the right to see the entire table.

   
| Task | Conda package and environment manager command | Pip package manager command | Virtualenv environment manager command |
| --- | --- | --- | --- |
| Install a package | `conda install $PACKAGE_NAME` | `pip install $PACKAGE_NAME` | X   |
| Update a package | `conda update --name $ENVIRONMENT_NAME $PACKAGE_NAME` | `pip install --upgrade $PACKAGE_NAME` | X   |
| Update package manager | `conda update conda` | Linux/macOS: `pip install -U pip` Win: `python -m pip install -U pip` | X   |
| Uninstall a package | `conda remove --name $ENVIRONMENT_NAME $PACKAGE_NAME` | `pip uninstall $PACKAGE_NAME` | X   |
| Create an environment | `conda create --name $ENVIRONMENT_NAME python` | X   | `cd $ENV_BASE_DIR; virtualenv $ENVIRONMENT_NAME` |
| Activate an environment | `conda activate $ENVIRONMENT_NAME`\* | X   | `source $ENV_BASE_DIR/$ENVIRONMENT_NAME/bin/activate` |
| Deactivate an environment | `conda deactivate` | X   | `deactivate` |
| Search available packages | `conda search $SEARCH_TERM` | `pip search $SEARCH_TERM` | X   |
| Install package from specific source | `conda install --channel $URL $PACKAGE_NAME` | `pip install --index-url $URL $PACKAGE_NAME` | X   |
| List installed packages | `conda list --name $ENVIRONMENT_NAME` | `pip list` | X   |
| Create requirements file | `conda export --format=requirements` or `conda list --export` | `pip freeze` | X   |
| List all environments | `conda info --envs` | X   | Install virtualenv wrapper, then `lsvirtualenv` |
| Install other package manager | `conda install pip` | `pip install conda` | X   |
| Install Python | `conda install python=x.x` | X   | X   |
| Update Python | `conda update python`\* | X   | X   |

\* `conda activate` only works on conda 4.6 and later versions. For conda versions prior to 4.6, type:

> *   Windows: `activate`
>     
> *   Linux and macOS: `source activate`
>     

\* `conda update python` updates to the most recent in the series, so any Python 2.x would update to the latest 2.x and any Python 3.x to the latest 3.x.

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/index.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/index.rst.txt)