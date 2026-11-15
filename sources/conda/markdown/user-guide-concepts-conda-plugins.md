[Skip to main content](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-plugins.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

Plugins[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-plugins.html#plugins "Link to this heading")

=================================================================================================================================

In order to enable customization and extra features that are compatible with and discoverable by conda (but do not necessarily ship as a default part of the conda codebase), an official conda plugin mechanism has been implemented as of version `22.11.0`.

Implementation[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-plugins.html#implementation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

Plugins in conda integrate the "hook + entry point" structure by utilizing the [Pluggy](https://pluggy.readthedocs.io/en/stable/)
 Python framework. This implementation can be broken down via the following two steps:

*   Define the hook(s) to be registered
    
*   Register the plugin under the conda entrypoint namespace
    

### Hook[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-plugins.html#hook "Link to this heading")

Below is an example of a very basic plugin "hook":

my\_plugin.py[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-plugins.html#id1 "Link to this code")

import conda.plugins

@conda.plugins.hookimpl
def conda\_subcommands(): ...

Copy to clipboard

### Packaging using a pyproject.toml file[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-plugins.html#packaging-using-a-pyproject-toml-file "Link to this heading")

Below is an example that configures `setuptools` using a `pyproject.toml` file (note that the `setup.py` file is optional if a `pyproject.toml` file is defined, and thus will not be discussed here):

pyproject.toml[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-plugins.html#id2 "Link to this code")

\[build-system\]
requires \= \["setuptools", "setuptools-scm"\]
build-backend \= "setuptools.build\_meta"

\[project\]
name \= "my-conda-plugin"
version \= "1.0.0"
description \= "My conda plugin"
requires-python \= ">=3.11"
dependencies \= \["conda"\]

\[project.entry-points."conda"\]
my-conda-plugin \= "my\_plugin"

Copy to clipboard

Conda plugins use cases[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-plugins.html#conda-plugins-use-cases "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The new conda plugin API ecosystem brings about many possibilities, including but not limited to:

*   [Custom subcommands](https://docs.conda.io/projects/conda/en/stable/dev-guide/plugins/subcommands.html)
    
*   Support for packaging-related topics (_e.g._, [virtual packages](https://docs.conda.io/projects/conda/en/stable/dev-guide/plugins/virtual_packages.html)
    )
    
*   Development environment integrations (_e.g._, shells)
    
*   Alternative dependency solver backends
    
*   Network adapters
    
*   Build system integrations
    
*   Non-Python language support (_e.g._, C, Rust)
    
*   [Environment export formats](https://docs.conda.io/projects/conda/en/stable/dev-guide/plugins/environment_exporters.html)
    
*   Experimental features that are not currently covered by conda
    

Benefits of conda plugins[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/conda-plugins.html#benefits-of-conda-plugins "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

A conda plugin ecosystem enables contributors across the conda community to develop and share new features, thus bringing about more functionality and focus on the user experience. Though the list below is by no means exhaustive, some of the benefits of conda plugins include:

*   Support for a better distribution of maintenance in the conda community
    
*   Enabling third party contributors to use official APIs instead of having to divert to workarounds and wrappers
    
*   The ability to extend conda internals via official APIs
    
*   Lowering the barrier for contributions from other stakeholders in the conda ecosystem
    
*   ... and much more!
    

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/user-guide/concepts/conda-plugins.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/user-guide/concepts/conda-plugins.rst.txt)