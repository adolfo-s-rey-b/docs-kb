[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/run.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda run`[#](https://docs.conda.io/projects/conda/en/stable/commands/run.html#conda-run "Link to this heading")

==================================================================================================================

Run an executable in a conda environment.

usage: conda run \[\-h\] \[\-n ENVIRONMENT | \-p PATH\] \[\-v\] \[\--dev\]
                 \[\--debug\-wrapper\-scripts\] \[\--cwd CWD\] \[\-s\]
                 ...

Copy to clipboard

Positional Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/run.html#conda-run-positional-arguments "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

executable\_call

Executable name, with additional arguments to be passed to the executable on invocation. Use '--' to separate conda options from executable options.

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/run.html#conda-run-named-arguments "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

\-v, --verbose

Can be used multiple times. Once for detailed output, twice for INFO logging, thrice for DEBUG logging, four times for TRACE logging.

\--dev

\--dev is deprecated and will be removed in 27.3. Set PYTHONPATH to the conda source root instead.

\--debug-wrapper-scripts

When this is set, where implemented, the shell wrapper scriptswill use the echo command to print debugging information to stderr (standard error).

\--cwd

Current working directory for command to run in. Defaults to the user's current working directory if no directory is specified.

\-s, --no-capture-output, --live-stream

Don't capture stdout/stderr (standard out/standard error).

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/run.html#conda-run-target-environment-specification "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Example:

$ conda create -y -n my-python-env python=3 $ conda run -n my-python-env python --version

Use '--' to separate conda run's options from the executable's options:

$ conda run -n my-python-env -- python -v $ conda run -v -n my-python-env -- tar -tvf file.tar

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/run.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/run.rst.txt)