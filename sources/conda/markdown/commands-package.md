[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/package.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda package`[#](https://docs.conda.io/projects/conda/en/stable/commands/package.html#conda-package "Link to this heading")

==============================================================================================================================

Create low-level conda packages. (EXPERIMENTAL)

usage: conda package \[\-h\] \[\-n ENVIRONMENT | \-p PATH\] \[\-w PATH \[PATH ...\]\] \[\-r\]
                     \[\-u\] \[\--pkg\-name PKG\_NAME\] \[\--pkg\-version PKG\_VERSION\]
                     \[\--pkg\-build PKG\_BUILD\]

Copy to clipboard

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/package.html#conda-package-named-arguments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

\-w, --which

Given some file's PATH, print which conda package the file came from.

\-r, --reset

Remove all untracked files and exit.

\-u, --untracked

Display all untracked files and exit.

\--pkg-name

Designate package name of the package being created.

\--pkg-version

Designate package version of the package being created.

\--pkg-build

Designate package build number of the package being created.

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/package.html#conda-package-target-environment-specification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/package.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/package.rst.txt)