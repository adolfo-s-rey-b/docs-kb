[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/env/create.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda env create`[#](https://docs.conda.io/projects/conda/en/stable/commands/env/create.html#conda-env-create "Link to this heading")

=======================================================================================================================================

Create an environment based on an environment definition file.

The file format is detected from the filename or contents. Which formats are supported depends on the plugins installed in your environment. See the epilog for the list of formats available here.

If the file declares a name in its contents (for instance as the first line of an environment.yml file), that name is used unless overridden on the CLI with -n/--name.

Unless you are in the directory containing the environment definition file, use -f to specify the file path of the environment definition file you want to use.

usage: conda env create \[\-h\] \[\-f \[FILE ...\]\] \[\-n ENVIRONMENT | \-p PATH\] \[\-C\]
                        \[\-k\] \[\--offline\]
                        \[\--environment\-specifier {cep\-24,environment\-yaml,env.yml,conda\-lock\-v1,conda\-lock,environment.yml,explicit,rattler\-lock\-v6,pixi,pixi\-lock\-v6,requirements.txt,requirements,reqs}\]
                        \[\--format FORMAT\] \[\--no\-default\-packages\] \[\--json\]
                        \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\-d\] \[\-y\]
                        \[\--solver {libmamba,rattler}\] \[\--subdir SUBDIR\]

Copy to clipboard

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/env/create.html#conda-env-create-named-arguments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

\-f, --file

Environment definition file (default: environment.yml). Standard filenames registered by the installed format plugins are auto-detected. Custom filenames require --format.

\--environment-specifier, --env-spec

Possible choices: cep-24, environment-yaml, env.yml, conda-lock-v1, conda-lock, environment.yml, explicit, rattler-lock-v6, pixi, pixi-lock-v6, requirements.txt, requirements, reqs

\--env-spec is deprecated and will be removed in 27.3. Use the \--format flag instead.

\--format

Possible choices: cep-24, environment-yaml, env.yml, conda-lock-v1, conda-lock, environment.yml, explicit, rattler-lock-v6, pixi, pixi-lock-v6, requirements.txt, requirements, reqs

Override auto-detection of the input file's format. See conda export --help for the formats available in your installation. Aliases are interchangeable with canonical names.

\--no-default-packages

Ignore create\_default\_packages in the .condarc file.

\--solver

Possible choices: libmamba, rattler

Choose which solver backend to use.

\--subdir, --platform

Possible choices: emscripten-wasm32, freebsd-64, linux-32, linux-64, linux-aarch64, linux-armv6l, linux-armv7l, linux-ppc64, linux-ppc64le, linux-riscv64, linux-s390x, osx-64, osx-arm64, wasi-wasm32, win-32, win-64, win-arm64, zos-z

Use packages built for this platform. The new environment will be configured to remember this choice. Should be formatted like 'osx-64', 'linux-32', 'win-64', and so on. Defaults to the current (native) platform.

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/env/create.html#conda-env-create-target-environment-specification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Networking Options[#](https://docs.conda.io/projects/conda/en/stable/commands/env/create.html#conda-env-create-networking-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

\-C, --use-index-cache

Use cache of channel index files, even if it has expired. This is useful if you don't want conda to check whether a new version of the repodata file exists, which will save bandwidth.

\-k, --insecure

Allow conda to perform "insecure" SSL connections and transfers. Equivalent to setting 'ssl\_verify' to 'false'.

\--offline

Offline mode. Don't connect to the Internet.

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/env/create.html#conda-env-create-output-prompt-and-flow-control-options "Link to this heading")

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

Examples:

Create from an environment spec (solved at install time):

conda env create -f /path/to/environment.yml

Create from a lockfile (no solve, exact reproduction):

conda env create -f explicit.txt

Use the default file in the current directory:

conda env create conda env create -n envname

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

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/env/create.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/env/create.rst.txt)