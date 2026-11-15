[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/remove.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda remove`[#](https://docs.conda.io/projects/conda/en/stable/commands/remove.html#conda-remove "Link to this heading")

===========================================================================================================================

Remove a list of packages from a specified conda environment.

Use \--all flag to remove all packages and the environment itself.

This command will also remove any package that depends on any of the specified packages as well---unless a replacement can be found without that dependency. If you wish to skip this dependency checking and remove just the requested packages, add the '--force' option. Note however that this may result in a broken environment, so use this with caution.

usage: conda remove \[\-h\] \[\--override\-frozen\] \[\-n ENVIRONMENT | \-p PATH\]
                    \[\-c CHANNEL\] \[\--use\-local\] \[\-O\]
                    \[\--repodata\-fn REPODATA\_FNS\] \[\--experimental {jlap,lock}\]
                    \[\--no\-lock\] \[\--repodata\-use\-zst | \--no\-repodata\-use\-zst\]
                    \[\--repodata\-use\-shards | \--no\-repodata\-use\-shards\]
                    \[\--features\] \[\--force\-remove\] \[\--no\-pin\]
                    \[\--solver {libmamba,rattler}\] \[\-C\] \[\-k\] \[\--offline\]
                    \[\--json\] \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\-d\] \[\-y\]
                    \[\--all\] \[\--keep\-env\] \[\--dev\]
                    \[package\_name ...\]

Copy to clipboard

Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/remove.html#conda-remove-uninstall-positional-arguments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

package\_name

Package names to remove from the environment.

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/remove.html#conda-remove-uninstall-named-arguments "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

\--override-frozen

DANGEROUS. Use at your own risk. Ignore protections if the environment is frozen.

\--all

Remove all packages, i.e., the entire environment.

\--keep-env

Used with \--all, delete all packages but keep the environment.

\--dev

\--dev is pending deprecation and will be removed in 27.9. Set PYTHONPATH to the conda source root instead.

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/remove.html#conda-remove-uninstall-target-environment-specification "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Channel Customization[#](https://docs.conda.io/projects/conda/en/stable/commands/remove.html#conda-remove-uninstall-channel-customization "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

Solver Mode Modifiers[#](https://docs.conda.io/projects/conda/en/stable/commands/remove.html#conda-remove-uninstall-solver-mode-modifiers "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

\--features

Remove features (instead of packages).

\--force-remove, --force

Forces removal of a package without removing packages that depend on it. Using this option will usually leave your environment in a broken and inconsistent state.

\--no-pin

Ignore pinned package(s) that apply to the current operation. These pinned packages might come from a .condarc file or a file in <TARGET\_ENVIRONMENT>/conda-meta/pinned.

\--solver

Possible choices: libmamba, rattler

Choose which solver backend to use.

Networking Options[#](https://docs.conda.io/projects/conda/en/stable/commands/remove.html#conda-remove-uninstall-networking-options "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

\-C, --use-index-cache

Use cache of channel index files, even if it has expired. This is useful if you don't want conda to check whether a new version of the repodata file exists, which will save bandwidth.

\-k, --insecure

Allow conda to perform "insecure" SSL connections and transfers. Equivalent to setting 'ssl\_verify' to 'false'.

\--offline

Offline mode. Don't connect to the Internet.

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/remove.html#conda-remove-uninstall-output-prompt-and-flow-control-options "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\--json

Report all output as json. Suitable for using conda programmatically.

\--console

Possible choices: classic, json

Select the backend to use for normal output rendering.

\-v, --verbose

Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.

\-q, --quiet

Do not display progress bar.

\-d, --dry-run

Only display what would have been done.

\-y, --yes

Sets any confirmation values to 'yes' automatically. Users will not be asked to confirm any adding, deleting, backups, etc.

Examples:

Remove the package 'scipy' from the currently-active environment:

> conda remove scipy

Remove a list of packages from an environment 'myenv':

> conda remove -n myenv scipy curl wheel

Remove all packages from environment myenv and the environment itself:

> conda remove -n myenv --all

Remove all packages from the environment myenv but retain the environment:

> conda remove -n myenv --all --keep-env

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/remove.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/remove.rst.txt)