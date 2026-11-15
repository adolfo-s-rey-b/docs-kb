[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/update.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda update`[#](https://docs.conda.io/projects/conda/en/stable/commands/update.html#conda-update "Link to this heading")

===========================================================================================================================

Update conda packages to the latest compatible version.

This command accepts a list of package names and updates them to the latest versions that are compatible with all other packages in the environment.

Conda attempts to install the newest versions of the requested packages. To accomplish this, it may update some packages that are already installed, or install additional packages. To prevent existing packages from updating, use the --no-update-deps option. This may force conda to install older versions of the requested packages, and it does not prevent additional dependency packages from being installed.

When using --file, only the package list from the file is used. Any name or prefix in the file is ignored; packages are updated in the target environment (-n/-p or the current environment).

usage: conda update \[\-h\] \[\--override\-frozen\] \[\-n ENVIRONMENT | \-p PATH\]
                    \[\-c CHANNEL\] \[\--use\-local\] \[\-O\]
                    \[\--repodata\-fn REPODATA\_FNS\] \[\--experimental {jlap,lock}\]
                    \[\--no\-lock\] \[\--repodata\-use\-zst | \--no\-repodata\-use\-zst\]
                    \[\--repodata\-use\-shards | \--no\-repodata\-use\-shards\]
                    \[\--strict\-channel\-priority\] \[\--no\-channel\-priority\]
                    \[\--no\-deps | \--only\-deps\] \[\--no\-pin\]
                    \[\--exclude\-newer DURATION\_OR\_DATE\] \[\--copy\]
                    \[\--no\-shortcuts\] \[\--shortcuts\-only SHORTCUTS\_ONLY\]
                    \[\--clobber\] \[\-C\] \[\-k\] \[\--offline\] \[\--json\]
                    \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\-d\] \[\-y\]
                    \[\--download\-only\] \[\--show\-channel\-urls\] \[\-f FILE\]
                    \[\--environment\-specifier {cep\-24,environment\-yaml,env.yml,conda\-lock\-v1,conda\-lock,environment.yml,explicit,rattler\-lock\-v6,pixi,pixi\-lock\-v6,requirements.txt,requirements,reqs}\]
                    \[\--format FORMAT\] \[\--solver {libmamba,rattler}\]
                    \[\--force\-reinstall\] \[\--freeze\-installed | \--update\-deps |\
                    \-S | \--update\-all | \--update\-specs\]
                    \[package\_spec ...\]

Copy to clipboard

Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/update.html#conda-update-upgrade-positional-arguments "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

package\_spec

List of packages to install or update in the conda environment.

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/update.html#conda-update-upgrade-named-arguments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

\--override-frozen

DANGEROUS. Use at your own risk. Ignore protections if the environment is frozen.

\-f, --file

Read environment or package specs from a file. The format is detected from the filename or contents. Which formats are supported depends on the installed plugins (see the epilog for the list available here). Custom filenames require --format. May be repeated (e.g. --file=file1 --file=file2).

\--environment-specifier, --env-spec

Possible choices: cep-24, environment-yaml, env.yml, conda-lock-v1, conda-lock, environment.yml, explicit, rattler-lock-v6, pixi, pixi-lock-v6, requirements.txt, requirements, reqs

\--env-spec is deprecated and will be removed in 27.3. Use the \--format flag instead.

\--format

Possible choices: cep-24, environment-yaml, env.yml, conda-lock-v1, conda-lock, environment.yml, explicit, rattler-lock-v6, pixi, pixi-lock-v6, requirements.txt, requirements, reqs

Override auto-detection of the input file's format. See conda export --help for the formats available in your installation. Aliases are interchangeable with canonical names.

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/update.html#conda-update-upgrade-target-environment-specification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Channel Customization[#](https://docs.conda.io/projects/conda/en/stable/commands/update.html#conda-update-upgrade-channel-customization "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

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

Solver Mode Modifiers[#](https://docs.conda.io/projects/conda/en/stable/commands/update.html#conda-update-upgrade-solver-mode-modifiers "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

\--strict-channel-priority

Packages in lower priority channels are not considered if a package with the same name appears in a higher priority channel.

\--no-channel-priority

Package version takes precedence over channel priority. Overrides the value given by conda config --show channel\_priority.

\--no-deps

Do not install, update, remove, or change dependencies. This WILL lead to broken environments and inconsistent behavior. Use at your own risk.

\--only-deps

Only install dependencies.

\--no-pin

Ignore pinned file.

\--exclude-newer

Exclude packages published more recently than the given duration (e.g. 7d, 3d12h, 1w) or date (e.g. 2026-04-01, 2026-04-01T12:00:00Z). Date-only values use the start of the next UTC day. Supply 0 for no delay, using the current time as the cutoff. Channel and per-package overrides can be set via channel\_settings and exclude\_newer\_package in .condarc.

\--solver

Possible choices: libmamba, rattler

Choose which solver backend to use.

\--force-reinstall

Ensure that any user-requested package for the current operation is uninstalled and reinstalled, even if that package already exists in the environment.

\--freeze-installed, --no-update-deps

Do not update or change already-installed dependencies.

\--update-deps

Update dependencies that have available updates.

\-S, --satisfied-skip-solve

Exit early and do not run the solver if the requested specs are satisfied. Also skips aggressive updates as configured by the 'aggressive\_update\_packages' config setting. Use 'conda config --describe aggressive\_update\_packages' to view your setting. --satisfied-skip-solve is similar to the default behavior of 'pip install'.

\--update-all, --all

Update all installed packages in the environment.

\--update-specs

Update based on provided specifications.

Package Linking and Install-time Options[#](https://docs.conda.io/projects/conda/en/stable/commands/update.html#conda-update-upgrade-package-linking-and-install-time-options "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\--copy

Install all packages using copies instead of hard- or soft-linking.

\--no-shortcuts

Don't install start menu shortcuts

\--shortcuts-only

Install shortcuts only for this package name. Can be used several times.

\--clobber

Allow clobbering (i.e. overwriting) of overlapping file paths within packages and suppress related warnings.

Networking Options[#](https://docs.conda.io/projects/conda/en/stable/commands/update.html#conda-update-upgrade-networking-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

\-C, --use-index-cache

Use cache of channel index files, even if it has expired. This is useful if you don't want conda to check whether a new version of the repodata file exists, which will save bandwidth.

\-k, --insecure

Allow conda to perform "insecure" SSL connections and transfers. Equivalent to setting 'ssl\_verify' to 'false'.

\--offline

Offline mode. Don't connect to the Internet.

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/update.html#conda-update-upgrade-output-prompt-and-flow-control-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

\--download-only

Solve an environment and ensure package caches are populated, but exit prior to unlinking and linking packages into the prefix.

\--show-channel-urls

Show channel urls. Overrides the value given by conda config --show show\_channel\_urls.

Examples:

> conda update -n myenv scipy

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/update.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/update.rst.txt)