[Skip to main content](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/channels.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

Channels[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/channels.html#channels "Link to this heading")

==============================================================================================================================

What is a "channel"?[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/channels.html#what-is-a-channel "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

Channels are locations where conda packages are stored. A channel can be a public package repository, a private or internal package repository, or a local directory on your computer.

Conda [packages](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/packages.html)
 are downloaded from channels, which are URLs or channel names that point to directories containing conda packages. The `conda` command searches a configured set of channels when you install, update, or search for packages.

By default, packages are automatically downloaded and updated from the [default channel](https://repo.anaconda.com/pkgs/)
, which may require a paid license, as described in the [repository terms of service](https://www.anaconda.com/terms-of-service)
. You can modify which channels conda searches. For details, see how to [modify your channel lists](https://docs.conda.io/projects/conda/en/stable/user-guide/configuration/settings.html#config-channels)
.

Common public channels[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/channels.html#common-public-channels "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

Some commonly used public channels and multichannels include:

`defaults`

A built-in multichannel that includes Anaconda-hosted channels such as `main`, `r`, and `msys2` under `repo.anaconda.com`.

`main`

The primary Anaconda-hosted channel under `repo.anaconda.com`. It contains many commonly used packages distributed by Anaconda.

`conda-forge`

A community-led channel with packages maintained by thousands of contributors. The [conda-forge project](https://conda-forge.org/)
 provides a large collection of packages across many ecosystems.

`bioconda`

A community channel focused on bioinformatics packages. The [Bioconda project](https://bioconda.github.io/)
 is commonly used together with `conda-forge`.

You can browse public channels and search for packages on [Anaconda.org](https://anaconda.org/)
.

Specifying channels when installing packages[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/channels.html#specifying-channels-when-installing-packages "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

From the command line, use `--channel` to search a specific channel:

$ conda install scipy \--channel conda-forge

Copy to clipboard

You may specify multiple channels by passing the argument multiple times:

$ conda install scipy \--channel conda-forge \--channel bioconda

Copy to clipboard

Priority decreases from left to right: the first argument has higher priority than the second.

Use `--override-channels` to search only the specified channel or channels instead of any channels configured in `.condarc`. This also ignores conda's default channels.

$ conda search scipy \--channel conda-forge \--override-channels

Copy to clipboard

In `.condarc`, use the `channels` key to configure the list of channels conda searches for packages.

Learn more about [managing channels](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-channels.html)
.

Local channels[#](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/channels.html#local-channels "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

A local channel is a channel stored on your own computer or on a shared filesystem. Local channels are useful when you are building your own packages, testing packages before publishing them, or maintaining packages for an internal workflow.

Local channels use the same channel layout as remote channels. They contain platform subdirectories such as `linux-64`, `osx-64`, `win-64`, and `noarch`. Each subdirectory contains package files and repository metadata.

To use a local channel, provide a `file://` URL or path to the channel root. For example:

$ conda search \--channel file:///opt/conda-channel \--override-channels

Copy to clipboard

For a step-by-step example of creating and indexing a local channel, see [creating custom channels](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/create-custom-channels.html)
.

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/user-guide/concepts/channels.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/user-guide/concepts/channels.rst.txt)