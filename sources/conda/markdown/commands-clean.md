[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/clean.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda clean`[#](https://docs.conda.io/projects/conda/en/stable/commands/clean.html#conda-clean "Link to this heading")

========================================================================================================================

Remove unused packages and caches.

usage: conda clean \[\-h\] \[\-a\] \[\-i\] \[\-p\] \[\-t\] \[\-f\] \[\-c \[TEMPFILES ...\]\] \[\-l\]
                   \[\--json\] \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\-d\] \[\-y\]

Copy to clipboard

Removal Targets[#](https://docs.conda.io/projects/conda/en/stable/commands/clean.html#conda-clean-removal-targets "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

\-a, --all

Remove index cache, unused cache packages, tarballs, tempfiles, and logfiles.

\-i, --index-cache

Remove index cache.

\-p, --packages

Remove unused packages from writable package caches. WARNING: Environments not listed by conda info --envs are not checked for symlinks back to the package cache.

\-t, --tarballs

Remove cached package tarballs.

\-f, --force-pkgs-dirs

Remove _all_ writable package caches. This option is not included with the --all flag. WARNING: This will break environments with packages installed using symlinks back to the package cache.

\-c, --tempfiles

Remove temporary files that could not be deleted earlier due to being in-use. The argument for the --tempfiles flag is a path (or list of paths) to the environment(s) where the tempfiles should be found and removed.

\-l, --logfiles

Remove log files.

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/clean.html#conda-clean-output-prompt-and-flow-control-options "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

> conda clean --tarballs

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/clean.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/clean.rst.txt)