[Skip to main content](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

Cheatsheet[#](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#cheatsheet "Link to this heading")

===========================================================================================================================

The conda cheatsheet contains the most important information about using conda, such as basic commands for creating and managing environments, installing packages, and importing and exporting environments.

See the [`conda cheatsheet`](https://docs.conda.io/projects/conda/en/stable/_downloads/9bd19ff225f7e368e394d54d887d121a/conda-25.3.1.pdf)
 for a PDF version.

**Versions**

*   [`conda 25.3.1`](https://docs.conda.io/projects/conda/en/stable/_downloads/9bd19ff225f7e368e394d54d887d121a/conda-25.3.1.pdf)
     (latest)
    
*   [`conda 24.4.0`](https://docs.conda.io/projects/conda/en/stable/_downloads/e0795803d81d6d87b74abed339025237/conda-24.4.0.pdf)
    
*   [`conda 4.14.x`](https://docs.conda.io/projects/conda/en/stable/_downloads/a35958a2a7fa1e927e7dfb61ebcd69a9/conda-4.14.pdf)
    
*   [`conda 4.12.x`](https://docs.conda.io/projects/conda/en/stable/_downloads/cb0ffc4c7b1e6c0e716c066d2b077faf/conda-4.12.pdf)
    
*   [`conda 4.6.x`](https://docs.conda.io/projects/conda/en/stable/_downloads/69c8c83c892884d9bc3700172a949a5b/conda-4.6.pdf)
    

Quickstart[#](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#quickstart "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

Tip

It is recommended to create a new environment for any new project or workflow.

|     |     |
| --- | --- | 
| verify conda install and check version | `conda info` |
| update conda in base environment | `conda update --name base conda` |
| install latest anaconda distribution (see release notes) | `conda install anaconda` |
| create a new environment (tip: name environment descriptively) | `conda create --name ENVNAME` |
| activate environment (do this before installing packages) | `conda activate ENVNAME` |

Channels and Packages[#](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#channels-and-packages "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Tip

Package dependencies and platform specifics are automatically resolved when using conda.

|     |     |
| --- | --- | 
| list installed packages | `conda list` |
| list installed packages with source info | `conda list --show-channel-urls` |
| update all packages | `conda update --all` |
| install a package from specific channel | `conda install --channel CHANNELNAME PKGNAME`<br><br>`conda install CHANNELNAME::PKGNAME` |
| install specific version of package | `conda install PKGNAME=3.1.4` |
| install package with AND logic | `conda install "PKGNAME>2.5, <3.2"` |
| install package with OR logic | `conda install "PKGNAME [version='2.5\|3.2']"` |
| uninstall package | `conda uninstall PKGNAME` |
| view channel sources | `conda config --show-sources` |
| add channel | `conda config --add channels CHANNELNAME` |

Working with Conda Environments[#](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#working-with-conda-environments "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tip

List environments at the beginning of your session. Environments with an asterisk are active.

|     |     |
| --- | --- | 
| list all environments and locations | `conda info --envs` |
| list all packages + source channels | `conda list --name ENVNAME --show-channel-urls` |
| install packages in environment | `conda install --name ENVNAME PKGNAME1 PKGNAME2` |
| remove package from environment | `conda uninstall --name ENVNAME PKGNAME` |
| update all packages in environment | `conda update --all --name ENVNAME` |

Environment Management[#](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#environment-management "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Tip

Specifying the environment name confines conda commands to that environment.

|     |     |
| --- | --- | 
| create environment with Python version | `conda create --name ENVNAME python=3.10` |
| clone environment | `conda create --clone ENVNAME --name NEWENV` |
| rename environment | `conda rename --name ENVNAME NEWENVNAME` |
| delete environment by name | `conda remove --name ENVNAME --all` |
| list revisions made to environment | `conda list --name ENVNAME --revisions` |
| restore environment to a revision | `conda install --name ENVNAME --revision NUMBER` |
| uninstall package from specific channel | `conda remove --name ENVNAME --channel CHANNELNAME PKGNAME` |

Exporting Environments[#](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#exporting-environments "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Tip

Name your export file after your environment to preserve your environment name.

|     |     |
| --- | --- | 
| cross-platform compatible (YAML) | `conda export --format=environment-yaml` |
| cross-platform compatible (JSON) | `conda export --format=environment-json` |
| cross-platform from history | `conda export --from-history` |
| platform + package specific (explicit) | `conda export --format=explicit` |
| platform + package specific (requirements) | `conda export --format=requirements` |
| auto-detect format by filename | `conda export --file=environment.yaml` |
| traditional env export | `conda env export > environment.yml` |

Importing Environments[#](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#importing-environments "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Tip

When importing an environment, conda resolves platform and package specifics.

|     |     |
| --- | --- | 
| from a .yml file | `conda create --file ENV.yml` |
| from a .txt file | `conda create --name ENVNAME --file ENV.txt` |

Additional Hints[#](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#additional-hints "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- | 
| get help for any command | `conda COMMAND --help` |
| get info for any package | `conda search PKGNAME --info` |
| run commands w/o user prompt, e.g., installing multiple packages | `conda COMMAND ARG --yes`<br><br>`conda install PKGNAME1 PKGNAME2 --yes` |
| remove all unused files | `conda clean --all` |
| examine conda configuration | `conda config --show` |

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/user-guide/cheatsheet.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/user-guide/cheatsheet.rst.txt)