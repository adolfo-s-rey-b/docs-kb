[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/notices.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda notices`[#](https://docs.conda.io/projects/conda/en/stable/commands/notices.html#conda-notices "Link to this heading")

==============================================================================================================================

Retrieve latest channel notifications.

Conda channel maintainers have the option of setting messages that users will see intermittently. Some of these notices are informational while others are messages concerning the stability of the channel.

usage: conda notices \[\-h\] \[\-c CHANNEL\] \[\--use\-local\] \[\-O\]
                     \[\--repodata\-fn REPODATA\_FNS\] \[\--experimental {jlap,lock}\]
                     \[\--no\-lock\] \[\--repodata\-use\-zst | \--no\-repodata\-use\-zst\]
                     \[\--repodata\-use\-shards | \--no\-repodata\-use\-shards\]
                     \[\--json\] \[\--console {classic,json}\] \[\-v\] \[\-q\]

Copy to clipboard

Channel Customization[#](https://docs.conda.io/projects/conda/en/stable/commands/notices.html#conda-notices-channel-customization "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

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

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/notices.html#conda-notices-output-prompt-and-flow-control-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

> conda notices
> 
> conda notices -c defaults

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/notices.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/notices.rst.txt)