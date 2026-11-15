[Skip to main content](https://docs.conda.io/projects/conda/en/stable/index.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

Conda Documentation[#](https://docs.conda.io/projects/conda/en/stable/index.html#conda-documentation "Link to this heading")

=============================================================================================================================

Welcome to conda's documentation! Conda provides package, dependency, and environment management for any language. Here, you will find everything you need to get started using conda in your own projects.

Install [#](https://docs.conda.io/projects/conda/en/stable/index.html#install-svg-version-1-1-width-1-0em-height-1-0em-class-sd-octicon-sd-octicon-download-sd-text-primary-viewbox-0-0-16-16-aria-hidden-true-path-d-m2-75-14a1-75-1-75-0-0-1-1-12-25v-2-5a-75-75-0-0-1-1-5-0v2-5c0-138-112-25-25-25h10-5a-25-25-0-0-0-25-25v-2-5a-75-75-0-0-1-1-5-0v2-5a1-75-1-75-0-0-1-13-25-14z-path-path-d-m7-25-7-689v2a-75-75-0-0-1-1-5-0v5-689l1-97-1-969a-749-749-0-1-1-1-06-1-06l-3-25-3-25a-749-749-0-0-1-1-06-0l4-22-6-78a-749-749-0-1-1-1-06-1-06l1-97-1-969z-path-svg "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We recommend the following conda distribtions to install conda:

Miniconda

[Miniconda](https://anaconda.com/docs/getting-started/concepts/anaconda-or-miniconda)
 is an installer by [Anaconda](https://anaconda.com/)
 that comes preconfigured for use with the Anaconda Repository. See the notes about Anaconda's [Terms of Service](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html#anaconda-tos-notes)
.

[Windows x86\_64](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)

[macOS arm64 (Apple Silicon)](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg)

[macOS x86\_64 (Intel)](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg)

[Linux x86\_64 (amd64)](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)

[Linux aarch64 (arm64)](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh)

Or with [Homebrew](https://brew.sh/)
:

brew install miniconda

Copy to clipboard

Miniforge

Miniforge is an installer maintained by the [conda-forge community](https://conda-forge.org/)
 that comes preconfigured for use with the conda-forge channel.

[Windows x86\_64](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe)

[macOS arm64 (Apple Silicon)](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh)

[macOS x86\_64 (Intel)](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-x86_64.sh)

[Linux x86\_64 (amd64)](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh)

[Linux aarch64 (arm64)](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh)

Or with [Homebrew](https://brew.sh/)
:

brew install miniforge

Copy to clipboard

For more detailed instructions, see [Miniconda's installation guide](https://anaconda.com/docs/getting-started/installation)
 and [conda-forge's download site](https://conda-forge.org/download/)

.

New to conda? [#](https://docs.conda.io/projects/conda/en/stable/index.html#new-to-conda-svg-version-1-1-width-1-0em-height-1-0em-class-sd-octicon-sd-octicon-rocket-sd-text-primary-viewbox-0-0-16-16-aria-hidden-true-path-d-m14-064-0h-186c15-216-0-16-784-16-1-75v-186a8-752-8-752-0-0-1-2-564-6-186l-458-459c-314-314-641-616-979-904v3-207c0-608-315-1-172-833-1-49l-2-774-1-707a-749-749-0-0-1-1-11-418l-954-3-102a1-214-1-214-0-0-1-145-125l3-754-9-816a1-218-1-218-0-0-1-124-145l-528-8-717a-749-749-0-0-1-418-1-11l1-71-2-774a1-748-1-748-0-0-1-3-31-4h3-204c-288-338-59-665-904-979l-459-458a8-749-8-749-0-0-1-14-064-0zm8-938-3-623h-002l-458-458c-76-76-1-437-1-598-2-02-2-5l-1-5-2-317-2-143-2-143-2-317-1-5c-902-583-1-74-1-26-2-499-2-02l-459-458a7-25-7-25-0-0-0-2-123-5-127v1-75a-25-25-0-0-0-25-25h-186a7-249-7-249-0-0-0-5-125-2-123zm3-56-14-56c-732-732-2-334-1-045-3-005-1-148a-234-234-0-0-1-201-064-234-234-0-0-1-064-201c-103-671-416-2-273-1-15-3-003a1-502-1-502-0-1-1-2-12-2-12zm6-94-3-935c-088-06-177-118-266-175l-2-35-1-521-548-1-783-1-949-1-2a-25-25-0-0-0-119-213zm3-678-8-116-5-2-5-766c-058-09-117-178-176-266h3-309a-25-25-0-0-0-213-119l-1-2-1-95zm12-5a1-1-0-1-1-2-0-1-1-0-0-1-2-0z-path-svg "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are new to conda, we first recommend the following articles:

Getting started guide

Learn the basics of using conda such as creating and adding packages to environments

[Getting started with conda](https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html)

Managing environments

Learn more about environments and best practices for using them in your projects

[Managing environments](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)

See also

Want to get even more in-depth training on how to use conda for free? Check out Anaconda's [free course on conda basics](https://learning.anaconda.cloud/conda-basics)
.

Other useful resources [#](https://docs.conda.io/projects/conda/en/stable/index.html#other-useful-resources-svg-version-1-1-width-1-0em-height-1-0em-class-sd-octicon-sd-octicon-light-bulb-sd-text-primary-viewbox-0-0-16-16-aria-hidden-true-path-d-m8-1-5c-2-363-0-4-1-69-4-3-75-0-984-424-1-625-984-2-304l-214-253c-223-264-47-556-673-848-284-411-537-896-621-1-49a-75-75-0-0-1-1-484-211c-04-282-163-547-37-847a8-456-8-456-0-0-0-542-68c-084-1-173-205-268-32c3-201-7-75-2-5-6-766-2-5-5-25-2-5-2-31-4-863-0-8-0s5-5-2-31-5-5-5-25c0-1-516-701-2-5-1-328-3-259-095-115-184-22-268-319-207-245-383-453-541-681-208-3-33-565-37-847a-751-751-0-0-1-1-485-212c-084-593-337-1-078-621-1-489-203-292-45-584-673-848-075-088-147-173-213-253-561-679-985-1-32-985-2-304-0-2-06-1-637-3-75-4-3-75zm5-75-12h4-5a-75-75-0-0-1-0-1-5h-4-5a-75-75-0-0-1-0-1-5zm6-15-25a-75-75-0-0-1-75-75h2-5a-75-75-0-0-1-0-1-5h-2-5a-75-75-0-0-1-75-75z-path-svg "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Command reference

Full reference for all standard commands and options

[Commands](https://docs.conda.io/projects/conda/en/stable/commands/index.html)

Cheatsheets

Get the latest cheatsheet for commonly used commands

[Cheatsheet](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html)

Configuring conda

Learn about the various ways conda's behavior can be configured

[Using the .condarc conda configuration file](https://docs.conda.io/projects/conda/en/stable/user-guide/configuration/use-condarc.html)

Glossary

Important vocabulary to know when working with conda

[Glossary](https://docs.conda.io/projects/conda/en/stable/glossary.html)

Contributors welcome [#](https://docs.conda.io/projects/conda/en/stable/index.html#contributors-welcome-svg-version-1-1-width-1-0em-height-1-0em-class-sd-octicon-sd-octicon-git-pull-request-sd-text-primary-viewbox-0-0-16-16-aria-hidden-true-path-d-m1-5-3-25a2-25-2-25-0-1-1-3-2-122v5-256a2-251-2-251-0-1-1-1-5-0v5-372a2-25-2-25-0-0-1-1-5-3-25zm5-677-177l9-573-677a-25-25-0-0-1-10-854v2-5h1a2-5-2-5-0-0-1-13-5-5v5-628a2-251-2-251-0-1-1-1-5-0v5a1-1-0-0-0-1-1h-1v1-646a-25-25-0-0-1-427-177l7-177-3-427a-25-25-0-0-1-0-354zm3-75-2-5a-75-75-0-1-0-0-1-5-75-75-0-0-0-0-1-5zm0-9-5a-75-75-0-1-0-0-1-5-75-75-0-0-0-0-1-5zm8-25-75a-75-75-0-1-0-1-5-0-75-75-0-0-0-1-5-0z-path-svg "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Conda is an open source project and always welcomes new contributions. Please read the following guides to get started developing conda and making your own contributions.

Contributing 101

Learn more about how the conda project is managed and how to contribute

[Contributing to conda](https://docs.conda.io/projects/conda/en/stable/dev-guide/contributing.html)

Development environment

Follow this guide to get your own development environment set up

[Development Environment](https://docs.conda.io/projects/conda/en/stable/dev-guide/development-environment.html)

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/index.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/index.rst.txt)