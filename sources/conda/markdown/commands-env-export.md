[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda env export`[#](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html#conda-env-export "Link to this heading")

=======================================================================================================================================

Note

A newer `conda export` command is now available with enhanced functionality, including multiple export formats and a plugin-based architecture. See [conda export](https://docs.conda.io/projects/conda/en/stable/commands/export.html)
 for the modern approach to environment export.

Export a conda environment to a file. The set of supported formats depends on the plugins installed in your environment. Both portable environment specs and reproducible lockfiles may be available. See the epilog for the list of formats available here.

usage: conda env export \[\-h\] \[\-c CHANNEL\] \[\-O\] \[\--platform EXPORT\_PLATFORMS\]
                        \[\--override\-platforms\] \[\-n ENVIRONMENT | \-p PATH\]
                        \[\-f FILE\] \[\--format FORMAT\] \[\--no\-builds\]
                        \[\--ignore\-channels\] \[\--json\]
                        \[\--console {classic,json}\] \[\-v\] \[\-q\] \[\--from\-history\]

Copy to clipboard

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html#conda-env-export-named-arguments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

\-c, --channel

Additional channel to include in the export

\-O, --override-channels

Do not include .condarc channels

\--platform, --subdir

Target platform(s)/subdir(s) for export (e.g. linux-64, osx-arm64, win-64). For formats that support multi-platform output, repeat the flag to produce a single file covering every platform.

\--override-platforms

Override the platforms specified in the condarc

\-f, --file

File name or path for the exported environment. Standard filenames registered by the installed format plugins are auto-detected. Custom filenames require --format. Existing files are overwritten silently.

\--format

Possible choices: conda-lock, conda-lock-v1, env.yml, environment-json, environment-yaml, explicit, json, pixi, pixi-lock-v6, rattler-lock-v6, reqs, requirements, txt, yaml, yml

Override the output format. When omitted, the format is detected from --file. See the epilog for the formats available in your installation.

\--no-builds

Remove build specification from dependencies

\--ignore-channels

Do not include channel names with package names.

\--from-history

Build environment spec from explicit specs in history

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html#conda-env-export-target-environment-specification "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html#conda-env-export-output-prompt-and-flow-control-options "Link to this heading")

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

Examples:

Export an environment spec:

conda export --from-history > environment.yml

Export a lockfile for the same platform:

conda export --file explicit.txt

Export a lockfile for multiple platforms:

conda export --file conda-lock.yml --platform linux-64 --platform osx-arm64

Available output formats:

Lockfiles:

*   conda-lock-v1 (aliases: conda-lock): conda-lock.yml, conda-lock.yaml
    
*   explicit: explicit.txt
    
*   rattler-lock-v6 (aliases: pixi, pixi-lock-v6): pixi.lock
    

Environment specs:

*   environment-json (aliases: json): environment.json
    
*   environment-yaml (aliases: yaml, yml, env.yml): environment.yaml, environment.yml
    
*   requirements (aliases: reqs, txt): requirements.txt, spec.txt
    

Overview[#](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html#overview "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

The `conda env export` command exports conda environments to YAML format. This command continues to be fully supported.

For new projects, consider [conda export](https://docs.conda.io/projects/conda/en/stable/commands/export.html)
, which provides additional features:

*   Multiple export formats (YAML, JSON, explicit, requirements)
    
*   Automatic format detection based on filename
    
*   Plugin-based architecture for custom formats
    
*   Enhanced cross-platform compatibility options
    

Alternative: Enhanced Export Command[#](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html#alternative-enhanced-export-command "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you're interested in additional export formats and functionality, the `conda export` command offers enhanced capabilities:

**Traditional (conda env export):**

conda env export \> environment.yml
conda env export \--from-history \> environment.yml

Copy to clipboard

**Enhanced (conda export):**

conda export \--format\=environment-yaml \> environment.yaml
conda export \--from-history \--format\=environment-yaml \> environment.yaml

Copy to clipboard

The enhanced command provides additional features:

\# Auto-detect format from filename
conda export \--file\=environment.yaml

\# Export to different formats
conda export \--format\=environment-json \--file\=environment.json
conda export \--format\=explicit \--file\=explicit.txt

Copy to clipboard

See Also[#](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html#see-also "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

*   [conda export](https://docs.conda.io/projects/conda/en/stable/commands/export.html)
     - Enhanced environment export command with multiple formats
    
*   [Managing environments](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)
     - Environment management guide
    

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/env/export.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/env/export.rst.txt)