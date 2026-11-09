[Skip to main content](https://docs.conda.io/projects/conda/en/stable/commands/export.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

`conda export`[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#conda-export "Link to this heading")

===========================================================================================================================

The `conda export` command allows you to export conda environments to various file formats. This command supports an enhanced plugin-based architecture that supports multiple export formats for different use cases.

Export a conda environment to a file. The set of supported formats depends on the plugins installed in your environment. Both portable environment specs and reproducible lockfiles may be available. See the epilog for the list of formats available here.

usage: conda export \[\-h\] \[\-c CHANNEL\] \[\-O\] \[\--platform EXPORT\_PLATFORMS\]
                    \[\--override\-platforms\] \[\-n ENVIRONMENT | \-p PATH\]
                    \[\-f FILE\] \[\--format FORMAT\] \[\--no\-builds\]
                    \[\--ignore\-channels\] \[\--json\] \[\--console {classic,json}\]
                    \[\-v\] \[\-q\] \[\--from\-history\]

Copy to clipboard

Named Arguments[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#conda-export-named-arguments "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

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

Target Environment Specification[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#conda-export-target-environment-specification "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\-n, --name

Name of environment.

\-p, --prefix

Full path to environment location (i.e. prefix).

Output, Prompt, and Flow Control Options[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#conda-export-output-prompt-and-flow-control-options "Link to this heading")

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
    

Overview[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#overview "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

The export command creates portable representations of conda environments that can be shared with others or used to recreate environments on different machines. The command supports multiple output formats through a plugin architecture:

**Structured Formats** (cross-platform friendly):

*   `environment-yaml` - YAML format (default) \[aliases: `yaml`, `yml`\]
    
*   `environment-json` - JSON format \[aliases: `json`\]
    

**Text Formats** (platform/architecture specific):

*   `explicit` - Explicit URLs with `@EXPLICIT` header (CEP 23 compliant)
    
*   `requirements` - Requirements format with MatchSpec strings \[aliases: `reqs`, `txt`\]
    

Format Selection[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#format-selection "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

You can specify the export format in three ways:

1.  **Explicit format specification** (recommended):
    
    conda export \--format\=environment-yaml
    
    Copy to clipboard
    
2.  **File extension detection**:
    
    conda export \--file\=environment.yaml
    
    Copy to clipboard
    
3.  **Default behavior** (outputs YAML to stdout):
    
    conda export
    
    Copy to clipboard
    

Supported Output Formats[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#supported-output-formats "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

### Environment YAML Format[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#environment-yaml-format "Link to this heading")

The default format that creates cross-platform compatible environment files.

|     |     |
| --- | --- |
| Format name | `environment-yaml` |
| Aliases | `yaml`, `yml` |
| Auto-detected filenames | `environment.yaml`, `environment.yml` |

\# Export to stdout
conda export \--format\=environment-yaml

\# Export to file
conda export \--file\=environment.yaml

\# Alternative using aliases
conda export \--format\=yaml
conda export \--format\=yml

Copy to clipboard

Example output:

name: myenv
channels:
  \- conda-forge
  \- defaults
dependencies:
  \- numpy=2.3.1
  \- pandas=2.3.1
  \- python=3.13.5

Copy to clipboard

### Environment JSON Format[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#environment-json-format "Link to this heading")

JSON representation of the environment for programmatic processing.

|     |     |
| --- | --- |
| Format name | `environment-json` |
| Aliases | `json` |
| Auto-detected filenames | `environment.json` |

\# Export to stdout
conda export \--format\=environment-json

\# Export to file
conda export \--file\=environment.json

\# Alternative using alias
conda export \--format\=json

Copy to clipboard

Example output:

{
  "name": "myenv",
  "channels": \[\
    "conda-forge",\
    "defaults"\
  \],
  "dependencies": \[\
    "numpy=2.3.1",\
    "pandas=2.3.1",\
    "python=3.13.5"\
  \]
}

Copy to clipboard

### Explicit Format (CEP 23)[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#explicit-format-cep-23 "Link to this heading")

Creates explicit package URLs for exact environment reproduction.

|     |     |
| --- | --- |
| Format name | `explicit` |
| Aliases | None |
| Auto-detected filenames | `explicit.txt` |

\# Export to stdout
conda export \--format\=explicit

\# Export to file
conda export \--file\=explicit.txt

Copy to clipboard

Example output:

\# This file may be used to create an environment using:
# $ conda create --name <env> --file <this file>
# platform: osx-arm64
@EXPLICIT

https://repo.anaconda.com/pkgs/main/noarch/tzdata-2025b-h04d1e81\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/libffi-3.4.4-hca03da5\_1.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/libcxx-17.0.6-he5c5206\_4.conda
https://repo.anaconda.com/pkgs/main/noarch/pip-25.1-pyhc872135\_2.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/pytz-2025.2-py313hca03da5\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/python-3.13.5-h2eb94d5\_100\_cp313.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/ca-certificates-2025.2.25-hca03da5\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/numexpr-2.11.0-py313hf08b1b5\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/python\_abi-3.13-0\_cp313.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/bzip2-1.0.8-h80987f9\_6.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/xz-5.6.4-h80987f9\_1.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/libgfortran5-11.3.0-h009349e\_28.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/six-1.17.0-py313hca03da5\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/blas-1.0-openblas.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/libgfortran-5.0.0-11\_3\_0\_hca03da5\_28.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/openssl-3.0.17-h4ee41c1\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/wheel-0.45.1-py313hca03da5\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/setuptools-72.1.0-py313hca03da5\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/numpy-base-2.3.1-py313h2506b34\_0.conda
https://repo.anaconda.com/pkgs/main/noarch/python-tzdata-2025.2-pyhd3eb1b0\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/llvm-openmp-17.0.6-h2f17746\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/numpy-2.3.1-py313h50dd0cd\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/bottleneck-1.4.2-py313ha35b7ea\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/ncurses-6.4-h313beb8\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/tk-8.6.14-h6ba3021\_1.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/sqlite-3.50.2-h79febb2\_1.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/libmpdec-4.0.0-h80987f9\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/expat-2.7.1-h313beb8\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/readline-8.2-h1a28f6b\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/zlib-1.2.13-h18a0788\_1.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/pandas-2.3.1-py313h17050e6\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/libopenblas-0.3.29-hea593b9\_0.conda
https://repo.anaconda.com/pkgs/main/osx-arm64/python-dateutil-2.9.0post0-py313hca03da5\_2.conda

Copy to clipboard

### Requirements Format[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#requirements-format "Link to this heading")

Creates a requirements file with MatchSpec strings.

Warning

This format produces conda MatchSpec strings, which differ from `conda list --export` output. The requirements format includes full package specifications with channels and build strings, while `conda list --export` produces simpler package=version format suitable for basic reproduction.

|     |     |
| --- | --- |
| Format name | `requirements` |
| Aliases | `reqs`, `txt` |
| Auto-detected filenames | `requirements.txt`, `spec.txt` |

\# Export to stdout
conda export \--format\=requirements

\# Export to file
conda export \--file\=requirements.txt

\# Alternative using aliases
conda export \--format\=reqs
conda export \--format\=txt

Copy to clipboard

Example output:

\# This file may be used to create an environment using:
# $ conda create --name <env> --file <this file>
# platform: osx-arm64
# Note: This is a conda requirements file (MatchSpec format)
# Contains conda package specifications, not pip requirements
pkgs/main::blas==1.0=openblas
pkgs/main::bottleneck==1.4.2=py313ha35b7ea\_0
pkgs/main::bzip2==1.0.8=h80987f9\_6
pkgs/main::ca-certificates==2025.2.25=hca03da5\_0
pkgs/main::expat==2.7.1=h313beb8\_0
pkgs/main::libcxx==17.0.6=he5c5206\_4
pkgs/main::libffi==3.4.4=hca03da5\_1
pkgs/main::libgfortran==5.0.0=11\_3\_0\_hca03da5\_28
pkgs/main::libgfortran5==11.3.0=h009349e\_28
pkgs/main::libmpdec==4.0.0=h80987f9\_0
pkgs/main::libopenblas==0.3.29=hea593b9\_0
pkgs/main::llvm-openmp==17.0.6=h2f17746\_0
pkgs/main::ncurses==6.4=h313beb8\_0
pkgs/main::numexpr==2.11.0=py313hf08b1b5\_0
pkgs/main::numpy==2.3.1=py313h50dd0cd\_0
pkgs/main::numpy-base==2.3.1=py313h2506b34\_0
pkgs/main::openssl==3.0.17=h4ee41c1\_0
pkgs/main::pandas==2.3.1=py313h17050e6\_0
pkgs/main::pip==25.1=pyhc872135\_2
pkgs/main::python==3.13.5=h2eb94d5\_100\_cp313
pkgs/main::python-dateutil==2.9.0post0=py313hca03da5\_2
pkgs/main::python-tzdata==2025.2=pyhd3eb1b0\_0
pkgs/main::python\_abi==3.13=0\_cp313
pkgs/main::pytz==2025.2=py313hca03da5\_0
pkgs/main::readline==8.2=h1a28f6b\_0
pkgs/main::setuptools==72.1.0=py313hca03da5\_0
pkgs/main::six==1.17.0=py313hca03da5\_0
pkgs/main::sqlite==3.50.2=h79febb2\_1
pkgs/main::tk==8.6.14=h6ba3021\_1
pkgs/main::tzdata==2025b=h04d1e81\_0
pkgs/main::wheel==0.45.1=py313hca03da5\_0
pkgs/main::xz==5.6.4=h80987f9\_1
pkgs/main::zlib==1.2.13=h18a0788\_1

Copy to clipboard

Common Options[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#common-options "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

### Export Current Environment[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#export-current-environment "Link to this heading")

Export the currently active environment:

conda export

Copy to clipboard

### Export Specific Environment[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#export-specific-environment "Link to this heading")

Export a named environment:

conda export \--name myenv

Copy to clipboard

### Export Environment by Path[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#export-environment-by-path "Link to this heading")

Export an environment by its path:

conda export \--prefix /path/to/env

Copy to clipboard

Cross-Platform Compatibility[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#cross-platform-compatibility "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

For cross-platform sharing, use the `--from-history` flag with structured formats:

\# Export only explicitly installed packages (cross-platform friendly)
conda export \--from-history \--format\=environment-yaml

\# This excludes dependency packages that might be platform-specific

Copy to clipboard

When **not** to use `--from-history`:

*   With `explicit` format (always uses all packages)
    
*   With `requirements` format (always uses all packages)
    
*   When you need exact dependency reproduction
    

Platform-Specific Exports[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#platform-specific-exports "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

You can specify target platforms for export using the `--platform` option or by configuring `export_platforms` in your condarc file:

\# Export for specific platforms
conda export \--platform linux-64 \--platform osx-64 \--format\=environment-yaml
\# or
conda export \--subdir linux-64 \--subdir osx-64 \--format\=environment-yaml

\# Export using condarc configuration
conda export \--format\=environment-yaml

Copy to clipboard

With condarc configuration:

export\_platforms:
  \- linux-64
  \- osx-64
  \- win-64

Copy to clipboard

File Format Detection[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#file-format-detection "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

The command automatically detects the export format based on filename patterns:

|     |     |     |     |
| --- | --- | --- | --- |File Detection Patterns and Aliases[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#id1 "Link to this table")
    
| Filename | Detected Format | Format Aliases | Description |
| --- | --- | --- | --- |
| `environment.yaml` | `environment-yaml` | `yaml`, `yml` | YAML environment file |
| `environment.yml` | `environment-yaml` | `yaml`, `yml` | YAML environment file (alternative extension) |
| `environment.json` | `environment-json` | `json` | JSON environment file |
| `explicit.txt` | `explicit` | None | Explicit URL format |
| `requirements.txt` | `requirements` | `reqs`, `txt` | Requirements format |
| `spec.txt` | `requirements` | `reqs`, `txt` | Requirements format |

You can use either the full format name or any of its aliases:

\# These are all equivalent
conda export \--format\=environment-yaml
conda export \--format\=yaml
conda export \--format\=yml

\# These are all equivalent
conda export \--format\=requirements
conda export \--format\=reqs
conda export \--format\=txt

Copy to clipboard

Examples[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

### Basic Usage[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#basic-usage "Link to this heading")

\# Export current environment to YAML (default)
conda export \> environment.yaml

\# Export specific environment
conda export \--name myenv \--format\=environment-yaml

\# Export with cross-platform compatibility
conda export \--from-history \--file\=environment.yaml

Copy to clipboard

### Advanced Usage[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#advanced-usage "Link to this heading")

\# Export to explicit format for exact reproduction
conda export \--format\=explicit \--file\=explicit.txt

\# Export to requirements format using aliases
conda export \--format\=reqs \> requirements.txt
conda export \--format\=txt \--file\=spec.txt

\# Export YAML using short alias
conda export \--format\=yml \--file\=environment.yml

\# Export JSON for programmatic processing
conda export \--format\=json \--file\=environment.json

\# Export with custom channels
conda export \--channel conda-forge \--format\=environment-yaml

\# Export for multiple platforms
conda export \--platform linux-64 \--platform osx-64 \--format\=environment-yaml
conda export \--subdir linux-64 \--subdir osx-64 \--format\=environment-yaml

\# Export for specific platform only
conda export \--platform win-64 \--format\=explicit \--file\=explicit-win-64.txt
conda export \--subdir win-64 \--format\=explicit \--file\=explicit-win-64.txt

Copy to clipboard

Error Handling[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#error-handling "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

The export command will fail in these cases:

*   **Empty environments with text formats**: The `explicit` and `requirements` formats require installed packages
    
*   **Unrecognized filenames**: Files that don't match supported patterns
    
*   **Invalid format names**: Format names that don't exist
    

For unrecognized filenames, specify the format explicitly:

\# This will fail
conda export \--file\=my-custom-file.xyz

\# This will work
conda export \--file\=my-custom-file.xyz \--format\=environment-yaml

Copy to clipboard

Plugin Architecture[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#plugin-architecture "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

The export functionality is built on a plugin architecture that allows extending conda with custom export formats. For information on creating custom exporters, see [Environment Exporters](https://docs.conda.io/projects/conda/en/stable/dev-guide/plugins/environment_exporters.html)
.

See Also[#](https://docs.conda.io/projects/conda/en/stable/commands/export.html#see-also "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

*   [conda env export](https://docs.conda.io/projects/conda/en/stable/commands/env/export.html)
     - Traditional environment export command
    
*   [Managing environments](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html)
     - Environment management guide
    
*   [Environment Exporters](https://docs.conda.io/projects/conda/en/stable/dev-guide/plugins/environment_exporters.html)
     - Plugin development guide
    

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/commands/export.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/commands/export.rst.txt)