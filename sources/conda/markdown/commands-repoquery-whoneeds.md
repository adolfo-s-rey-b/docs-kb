[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/repoquery/whoneeds.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda repoquery whoneeds`[#](https://docs.conda.io/projects/conda/en/stable/commands/repoquery/whoneeds.html#conda-repoquery-whoneeds "Link to this heading")

===============================================================================================================================================================

Note

The `conda repoquery whoneeds` command is provided by the `conda-libmamba-solver`. For more information on the subcommands provided, see [Subcommands](https://conda.github.io/conda-libmamba-solver/user-guide/subcommands/)
.

For more information on the libmamba solver, see [Solvers](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/solvers.html)
.

usage: conda repoquery whoneeds \[\-p PLATFORM\] \[\--no\-installed\] \[\--pretty\] \[\-a\]
                                \[\--use\-cache\-only\] \[\-t\] \[\--recursive\] \[\-h\]
                                \[\-c CHANNEL\] \[\--use\-local\] \[\-O\]
                                \[\--repodata\-fn REPODATA\_FNS\]
                                \[\--experimental {jlap,lock}\] \[\--no\-lock\]
                                \[\--repodata\-use\-zst | \--no\-repodata\-use\-zst\]
                                \[\--repodata\-use\-shards | \--no\-repodata\-use\-shards\]
                                \[\-C\] \[\-k\] \[\--offline\] \[\--json\]
                                \[\--console {classic,json}\] \[\-v\] \[\-q\]
                                specs \[specs ...\]

Copy to clipboard

Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/repoquery/whoneeds.html#conda-repoquery-whoneeds-positional-arguments "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

specs

The target package(s).

Subcommand options[#](https://docs.conda.io/projects/conda/en/stable/commands/repoquery/whoneeds.html#conda-repoquery-whoneeds-subcommand-options "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-p, --platform

Platform/subdir to search packages for. Defaults to current platform.

\--no-installed

Do not search currently installed packages.

\--pretty

Prettier output with more details.

\-a, --all-channels

Look at all channels (for depends / whoneeds).

\--use-cache-only

Search in pkgs\_dirs too

Dependency options[#](https://docs.conda.io/projects/conda/en/stable/commands/repoquery/whoneeds.html#conda-repoquery-whoneeds-dependency-options "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-t, --tree

Show dependencies in a tree-like format.

\--recursive

Show dependencies recursively.

Channel Customization[#](https://docs.conda.io/projects/conda/en/stable/commands/repoquery/whoneeds.html#conda-repoquery-whoneeds-channel-customization "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-c, --channel

Additional channel to search for packages. These are URLs searched in the order they are given (including local directories using the '[file://](file:///)
' syntax or simply a path like '/home/conda/mychan' or '../mychan'). Then, the defaults or channels from .condarc are searched (unless --override-channels is given). You can use 'defaults' to get the default packages for conda. You can also use any name and the .condarc channel\_alias value will be prepended. The default channel\_alias is [https://conda.anaconda.org/](https://conda.anaconda.org/)
.

\--use-local

Use locally built packages. Identical to '-c local'.

\-O, --override-channels

Do not search default or .condarc channels. Requires --channel.

\--repodata-fn

Specify file name of repodata on the remote server where your channels are configured or within local backups. Conda will try whatever you specify, but will ultimately fall back to repodata.json if your specs are not satisfiable with what you specify here. This is used to employ repodata that is smaller and reduced in time scope. You may pass this flag more than once. Leftmost entries are tried first, and the fallback to repodata.json is added for you automatically. For more information, see conda config --describe repodata\_fns.

\--experimental

Possible choices: jlap, lock

\--experimental is deprecated and will be removed in 27.3. Deprecated: jlap and lock no longer supported.

\--no-lock

Disable locking when reading, updating index (repodata.json) cache.

\--repodata-use-zst, --no-repodata-use-zst

Check for/do not check for repodata.json.zst. Enabled by default.

\--repodata-use-shards, --no-repodata-use-shards

Use sharded repodata if available. Enabled by default.

Networking Options[#](https://docs.conda.io/projects/conda/en/stable/commands/repoquery/whoneeds.html#conda-repoquery-whoneeds-networking-options "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-C, --use-index-cache

Use cache of channel index files, even if it has expired. This is useful if you don't want conda to check whether a new version of the repodata file exists, which will save bandwidth.

\-k, --insecure

Allow conda to perform "insecure" SSL connections and transfers. Equivalent to setting 'ssl\_verify' to 'false'.

\--offline

Offline mode. Don't connect to the Internet.

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/repoquery/whoneeds.html#conda-repoquery-whoneeds-output-prompt-and-flow-control-options "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/repoquery/whoneeds.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/repoquery/whoneeds.rst.txt)