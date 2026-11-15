[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/list.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda list`[#](https://docs.conda.io/projects/conda/en/stable/commands/list.html#conda-list "Link to this heading")

=====================================================================================================================

List installed packages in a conda environment.

usage: conda list \[\-h\] \[\-n ENVIRONMENT | \-p PATH\] \[\--json\]
                  \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\--show\-channel\-urls\]
                  \[\--fields LIST\_FIELDS\] \[\--reverse\] \[\-c\] \[\-f\] \[\--explicit\]
                  \[\--md5\] \[\--sha256\] \[\-e\] \[\-r\] \[\--size\] \[\--no\-pip\] \[\--auth\]
                  \[regex\]

Copy to clipboard

Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/list.html#conda-list-positional-arguments "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

regex

List only packages matching this regular expression.

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/list.html#conda-list-named-arguments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

\--show-channel-urls

Show channel urls. Overrides the value given by conda config --show show\_channel\_urls.

\--fields

Comma-separated list of fields to print. Valid values: arch,build,build\_number,channel,channel\_name,constrains,depends,dist\_str,features,fn,license,license\_family,md5,name,noarch,package\_type,requested\_spec,requested\_specs,sha256,size,subdir,timestamp,track\_features,url,version.

\--reverse

List installed packages in reverse order.

\-c, --canonical

Output canonical names of packages only.

\-f, --full-name

Only search for full names, i.e., ^<regex>$. --full-name NAME is identical to regex '^NAME$'.

\--explicit

List explicitly all installed conda packages with URL (output may be used by conda create --file).

\--md5

Add MD5 hashsum when using --explicit.

\--sha256

Add SHA256 hashsum when using --explicit.

\-e, --export

Output explicit, machine-readable requirement strings instead of human-readable lists of packages. This output may be used by conda create --file.

\-r, --revisions

List the revision history.

\--size

Show package and environment sizes.

\--no-pip

Do not include pip-only installed packages.

\--auth

In explicit mode, leave authentication details in package URLs. They are removed by default otherwise.

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/list.html#conda-list-target-environment-specification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/list.html#conda-list-output-prompt-and-flow-control-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\--json

Report all output as json. Suitable for using conda programmatically.

\--console

Possible choices: classic, json

Select the backend to use for normal output rendering.

\-v, --verbose

Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.

\-q, --quiet

Do not display progress bar.

Examples:

List all packages in the current environment:

> conda list

List all packages in reverse order:

> conda list --reverse

List all packages installed into the environment 'myenv':

> conda list -n myenv

List all packages that begin with the letters "py", using regex:

> conda list ^py

List name and version only:

> conda list --fields name,version

Save packages for future use:

> conda list --export > package-list.txt

Reinstall packages from an export file:

> conda create -n myenv --file package-list.txt

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/list.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/list.rst.txt)