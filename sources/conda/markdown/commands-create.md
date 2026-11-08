[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/create.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda create`[#](https://docs.conda.io/projects/conda/en/stable/commands/create.html#conda-create "Link to this heading")

===========================================================================================================================

Create a new conda environment from a list of specified packages.

Environments can be created from package specs on the command line, from an input file whose format is detected from its name or contents, or as a clone of an existing environment. See the epilog for the input formats available in your installation.

To use the newly-created environment, use 'conda activate envname'. This command requires either the -n NAME or -p PREFIX option unless --dry-run or --download-only is specified.

usage: conda create \[\-h\] \[\--clone ENV\] \[\-n ENVIRONMENT | \-p PATH\] \[\-c CHANNEL\]
                    \[\--use\-local\] \[\-O\] \[\--repodata\-fn REPODATA\_FNS\]
                    \[\--experimental {jlap,lock}\] \[\--no\-lock\]
                    \[\--repodata\-use\-zst | \--no\-repodata\-use\-zst\]
                    \[\--repodata\-use\-shards | \--no\-repodata\-use\-shards\]
                    \[\--strict\-channel\-priority\] \[\--no\-channel\-priority\]
                    \[\--no\-deps | \--only\-deps\] \[\--no\-pin\]
                    \[\--exclude\-newer DURATION\_OR\_DATE\] \[\--copy\]
                    \[\--no\-shortcuts\] \[\--shortcuts\-only SHORTCUTS\_ONLY\]
                    \[\--clobber\] \[\-C\] \[\-k\] \[\--offline\] \[\--json\]
                    \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\-d\] \[\-y\]
                    \[\--download\-only\] \[\--show\-channel\-urls\] \[\-f FILE\]
                    \[\--environment\-specifier {cep\-24,environment\-yaml,env.yml,conda\-lock\-v1,conda\-lock,environment.yml,explicit,rattler\-lock\-v6,pixi,pixi\-lock\-v6,requirements.txt,requirements,reqs}\]
                    \[\--format FORMAT\] \[\--no\-default\-packages\]
                    \[\--subdir SUBDIR\] \[\--solver {libmamba,rattler}\] \[\--dev\]
                    \[package\_spec ...\]

Copy to clipboard

Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/create.html#conda-create-positional-arguments "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

package\_spec

List of packages to install or update in the conda environment.

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/create.html#conda-create-named-arguments "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

\--clone

Create a new environment as a copy of an existing local environment.

\-f, --file

Read environment or package specs from a file. The format is detected from the filename or contents. Which formats are supported depends on the installed plugins (see the epilog for the list available here). Custom filenames require --format. May be repeated (e.g. --file=file1 --file=file2).

\--environment-specifier, --env-spec

Possible choices: cep-24, environment-yaml, env.yml, conda-lock-v1, conda-lock, environment.yml, explicit, rattler-lock-v6, pixi, pixi-lock-v6, requirements.txt, requirements, reqs

\--env-spec is deprecated and will be removed in 27.3. Use the \--format flag instead.

\--format

Possible choices: cep-24, environment-yaml, env.yml, conda-lock-v1, conda-lock, environment.yml, explicit, rattler-lock-v6, pixi, pixi-lock-v6, requirements.txt, requirements, reqs

Override auto-detection of the input file's format. See conda export --help for the formats available in your installation. Aliases are interchangeable with canonical names.

\--dev

\--dev is pending deprecation and will be removed in 27.9. Set PYTHONPATH to the conda source root instead.

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/create.html#conda-create-target-environment-specification "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Channel Customization[#](https://docs.conda.io/projects/conda/en/stable/commands/create.html#conda-create-channel-customization "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

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

\--subdir, --platform

Possible choices: emscripten-wasm32, freebsd-64, linux-32, linux-64, linux-aarch64, linux-armv6l, linux-armv7l, linux-ppc64, linux-ppc64le, linux-riscv64, linux-s390x, osx-64, osx-arm64, wasi-wasm32, win-32, win-64, win-arm64, zos-z

Use packages built for this platform. The new environment will be configured to remember this choice. Should be formatted like 'osx-64', 'linux-32', 'win-64', and so on. Defaults to the current (native) platform.

Solver Mode Modifiers[#](https://docs.conda.io/projects/conda/en/stable/commands/create.html#conda-create-solver-mode-modifiers "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

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

\--no-default-packages

Ignore create\_default\_packages in the .condarc file.

\--solver

Possible choices: libmamba, rattler

Choose which solver backend to use.

Package Linking and Install-time Options[#](https://docs.conda.io/projects/conda/en/stable/commands/create.html#conda-create-package-linking-and-install-time-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\--copy

Install all packages using copies instead of hard- or soft-linking.

\--no-shortcuts

Don't install start menu shortcuts

\--shortcuts-only

Install shortcuts only for this package name. Can be used several times.

\--clobber

Allow clobbering (i.e. overwriting) of overlapping file paths within packages and suppress related warnings.

Networking Options[#](https://docs.conda.io/projects/conda/en/stable/commands/create.html#conda-create-networking-options "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

\-C, --use-index-cache

Use cache of channel index files, even if it has expired. This is useful if you don't want conda to check whether a new version of the repodata file exists, which will save bandwidth.

\-k, --insecure

Allow conda to perform "insecure" SSL connections and transfers. Equivalent to setting 'ssl\_verify' to 'false'.

\--offline

Offline mode. Don't connect to the Internet.

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/create.html#conda-create-output-prompt-and-flow-control-options "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

Create from package specs:

conda create -n myenv python=3.12 numpy

Create from an environment spec (solved at install time):

conda create -n myenv --file environment.yml

Create from a lockfile (no solve, exact reproduction):

conda create -n myenv --file explicit.txt

Clone an existing environment:

conda create -n env2 --clone env1

Available input formats:

Environment specs:

*   cep-24 (aliases: environment-yaml, env.yml): environment.yml, environment.yaml
    
*   environment.yml: environment.yml, environment.yaml
    
*   requirements.txt (aliases: requirements, reqs): requirements.txt, spec.txt
    

Lockfiles:

*   conda-lock-v1 (aliases: conda-lock): conda-lock.yml, conda-lock.yaml
    
*   explicit: explicit.txt
    
*   rattler-lock-v6 (aliases: pixi, pixi-lock-v6): pixi.lock
    

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/create.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/create.rst.txt)