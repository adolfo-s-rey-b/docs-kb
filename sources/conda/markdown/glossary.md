[Skip to main content](https://docs.conda.io/projects/conda/en/stable/glossary.html#main-content)

Back to top  

 Ctrl+K

*   [conda](https://docs.conda.io/projects/conda/)
    
*   [conda-build](https://docs.conda.io/projects/conda-build)
    
*   [conda.org](https://conda.org/)
    

*   [Zulip](https://conda.zulipchat.com/)
    

Glossary[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#glossary "Link to this heading")

==========================================================================================================

.condarc[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#condarc "Link to this heading")

---------------------------------------------------------------------------------------------------------

The Conda Runtime Configuration file, an optional `.yaml` file that allows you to configure many aspects of conda, such as which channels it searches for packages, proxy settings, and environment directories. A `.condarc` file is not included by default, but it is automatically created in your home directory when you use the `conda config` command. The `.condarc` file can also be located in a root environment, in which case it overrides any `.condarc` in the home directory. For more information, see [Using the .condarc conda configuration file](https://docs.conda.io/projects/conda/en/stable/user-guide/configuration/use-condarc.html)
 and [Administering a multi-user conda installation](https://docs.conda.io/projects/conda/en/stable/user-guide/configuration/admin-multi-user-install.html)
. Pronounced "conda r-c".

Activate/Deactivate environment[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#activate-deactivate-environment "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

Conda commands used to switch or move between installed environments. The `conda activate` command prepends the path of your current environment to the PATH environment variable so that you do not need to type it each time. `deactivate` removes it. These commands might also execute activation and deactivation logic specified by some installed packages in your environment. Even when an environment is deactivated, you can still execute programs in that environment by specifying their paths directly, as in `~/anaconda/envs/envname/bin/program_name`. When an environment is activated, you can execute the program in that environment with just `program_name`.

Note

Replace `envname` with the name of the environment and replace `program_name` with the name of the program.

Anaconda[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#anaconda "Link to this heading")

----------------------------------------------------------------------------------------------------------

A downloadable, free, open-source, high-performance, and optimized Python and R distribution. Anaconda includes [conda](https://docs.conda.io/projects/conda/en/stable/glossary.html#conda-glossary)
, conda-build, Python, and 250+ automatically installed, open-source scientific packages and their dependencies that have been tested to work well together, including SciPy, NumPy, and many others. Use the `conda install` command to easily install 7,500+ popular open-source packages for data science--including advanced and scientific analytics--from the Anaconda repository. Use the `conda` command to install thousands more open-source packages.

Because Anaconda is a Python distribution, it can make installing Python quick and easy even for new users.

Available for Windows, macOS, and Linux, all versions of Anaconda are supported by the community.

See also [Miniconda](https://docs.conda.io/projects/conda/en/stable/glossary.html#miniconda-glossary)
 and [conda](https://docs.conda.io/projects/conda/en/stable/glossary.html#conda-glossary)
.

Anaconda.org[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#anaconda-org "Link to this heading")

------------------------------------------------------------------------------------------------------------------

A web-based, repository hosting service in the cloud. Packages created locally can be published to the cloud to be shared with others. [Anaconda.org](https://docs.anaconda.com/anacondaorg/)
 is a public version of Anaconda Repository and was formerly known as Anaconda Cloud.

Anaconda Navigator[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#anaconda-navigator "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

A desktop graphical user interface (GUI) included in all versions of Anaconda that allows you to easily manage conda packages, environments, channels, and notebooks without a command line interface (CLI). See more about [Navigator](https://docs.anaconda.com/navigator/)
.

CEP 23[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#cep-23 "Link to this heading")

------------------------------------------------------------------------------------------------------

Conda Enhancement Proposal 23, which defines the specification for explicit environment files. CEP 23 establishes two distinct environment file formats:

*   **Explicit format** - Files containing package URLs with `@EXPLICIT` header
    
*   **Text spec format** - Files containing MatchSpec strings (requirements format)
    

This proposal standardizes environment export formats and ensures compatibility across conda tools. For more information, see the [CEP 23 specification](https://conda.org/learn/ceps/cep-0023/)
.

Channels[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#channels "Link to this heading")

----------------------------------------------------------------------------------------------------------

The locations of the repositories where conda looks for packages. Channels may point to a Cloud repository or a private location on a remote or local repository that you or your organization created. The `conda channel` command has a default set of channels to search, beginning with [https://repo.anaconda.com/pkgs/](https://repo.anaconda.com/pkgs/)
, which you may override, for example, to maintain a private or internal channel. These default channels are referred to in conda commands and in the `.condarc` file by the channel name "defaults."

conda[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#conda "Link to this heading")

----------------------------------------------------------------------------------------------------

The package and environment manager program bundled with Anaconda that installs and updates conda packages and their dependencies. Conda also lets you easily switch between conda environments on your local computer.

conda environment[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#conda-environment "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

A folder or directory that contains a specific collection of conda packages and their dependencies, so they can be maintained and run separately without interference from each other. For example, you may use a conda environment for only Python 2 and Python 2 packages, maintain another conda environment with only Python 3 and Python 3 packages, and maintain another for R language packages. Environments can be created from:

*   The Navigator GUI
    
*   The command line
    
*   An environment specification file with the name `your-environment-name.yml`
    

conda package[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#conda-package "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

A compressed file that contains everything that a software program needs in order to be installed and run, so that you do not have to manually find and install each dependency separately. A conda package includes system-level libraries, Python or R language modules, executable programs, and other components. You manage conda packages with conda.

conda repository[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#conda-repository "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

A cloud-based repository that contains 7,500+ open-source certified packages that are easily installed locally with the `conda install` command. Anyone can access the repository from:

*   The Navigator GUI
    
*   A terminal using conda commands
    
*   [https://repo.anaconda.com/pkgs/](https://repo.anaconda.com/pkgs/)
    

Environment exporter[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#environment-exporter "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

A plugin that defines how conda environments are exported to specific file formats. Environment exporters are part of conda's plugin architecture and allow extending the `conda export` command with custom formats.

Built-in exporters include:

*   `environment-yaml` - YAML format for cross-platform sharing
    
*   `environment-json` - JSON format for programmatic processing
    
*   `explicit` - CEP 23 compliant explicit URLs format
    
*   `requirements` - MatchSpec-based requirements format
    

Custom exporters can be created through the conda plugin system. See [Environment Exporters](https://docs.conda.io/projects/conda/en/stable/dev-guide/plugins/environment_exporters.html)
 for details.

Explicit format[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#explicit-format "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

A CEP 23 compliant environment file format that contains package URLs with full metadata for exact environment reproduction. Explicit files begin with an `@EXPLICIT` header followed by complete package URLs.

Example:

@EXPLICIT
https://repo.anaconda.com/pkgs/main/osx-64/python-3.9.7-h88f2d9e\_0.tar.bz2
https://repo.anaconda.com/pkgs/main/osx-64/numpy-1.21.0-py39h2e5f516\_0.tar.bz2

Copy to clipboard

This format enables bit-for-bit identical environment reproduction on the same platform and architecture.

Metapackage[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#metapackage "Link to this heading")

----------------------------------------------------------------------------------------------------------------

A metapackage is a very simple package that has at least a name and a version. It need not have any dependencies or build steps. [Metapackages](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/packages.html#meta-package)
 may list dependencies to several core, low-level libraries and may contain links to software files that are automatically downloaded when executed.

Miniconda[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#miniconda "Link to this heading")

------------------------------------------------------------------------------------------------------------

A free minimal installer for conda. [Miniconda](https://docs.anaconda.com/free/miniconda/)
 is a small, bootstrap version of Anaconda that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib, and a few others. Use the `conda install` command to install 7,500+ additional conda packages from the Anaconda repository.

Miniconda is a Python distribution that can make installing Python quick and easy even for new users.

See also [Anaconda](https://docs.conda.io/projects/conda/en/stable/glossary.html#anaconda-glossary)
 and [conda](https://docs.conda.io/projects/conda/en/stable/glossary.html#conda-glossary)
.

Noarch package[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#noarch-package "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

A conda package that contains nothing specific to any system architecture, so it may be installed from any system. When conda searches for packages on any system in a channel, conda checks both the system-specific subdirectory, such as `linux-64`, and the `noarch` directory. Noarch is a contraction of "no architecture".

Package manager[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#package-manager "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

A collection of software tools that automates the process of installing, updating, configuring, and removing computer programs for a computer's operating system. Also known as a package management system. Conda is a package manager.

Packages[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#packages "Link to this heading")

----------------------------------------------------------------------------------------------------------

Software files and information about the software, such as its name, the specific version, and a description, bundled into a file that can be installed and managed by a package manager.

Plugins[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#plugins "Link to this heading")

--------------------------------------------------------------------------------------------------------

Plugins, sometimes referred to as add-ons or extensions, are software or modules that add new functions to a host program (_e.g._, conda) without directly altering the host program itself. Amongst other uses, plugins support is utilized to enable third-party developers to extend an application, support easily adding new features, and to reduce the size of an application by not loading unused features.

Repository[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#repository "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Any storage location from which software assets may be retrieved and installed on a local computer. See also [Anaconda.org](https://docs.conda.io/projects/conda/en/stable/glossary.html#anaconda-org-glossary)
 and [conda repository](https://docs.conda.io/projects/conda/en/stable/glossary.html#conda-repository-glossary)
.

Requirements format[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#requirements-format "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

A CEP 23 compliant environment file format that contains MatchSpec strings for conda-compatible package specifications. This format is similar to pip's `requirements.txt` but uses conda's MatchSpec syntax.

Example:

python=3.9.7
numpy=1.21.0
pandas>=1.3.0,<2.0

Copy to clipboard

This format provides a balance between exactness and flexibility, allowing some version ranges while remaining conda-compatible.

Silent mode installation[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#silent-mode-installation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

When installing Miniconda or Anaconda in silent mode, screen prompts are not shown on screen and default settings are automatically accepted.

Solvers[#](https://docs.conda.io/projects/conda/en/stable/glossary.html#solvers "Link to this heading")

--------------------------------------------------------------------------------------------------------

The component of conda that decides which package versions can be installed together in the same environment. When you install, update, or remove packages, the solver evaluates the package specifications you request, along with their dependencies and any constraints, and determines a compatible set of packages.

Conda supports multiple solvers, so you can choose the one that best fits your needs. For more information on your solver options, see [Solvers](https://docs.conda.io/projects/conda/en/stable/user-guide/concepts/solvers.html)
.

On this page

[Edit on GitHub](https://github.com/conda/conda/edit/main/docs/source/glossary.rst)

[Show Source](https://docs.conda.io/projects/conda/en/stable/_sources/glossary.rst.txt)