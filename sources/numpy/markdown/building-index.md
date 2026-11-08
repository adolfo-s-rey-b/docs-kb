[Skip to main content](https://numpy.org/doc/stable/building/index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/building/index.html)
[2.5 (stable)](https://numpy.org/doc/stable/building/index.html)
[2.4](https://numpy.org/doc/2.4/building/index.html)
[2.3](https://numpy.org/doc/2.3/building/index.html)
[2.2](https://numpy.org/doc/2.2/building/index.html)
[2.1](https://numpy.org/doc/2.1/building/index.html)
[2.0](https://numpy.org/doc/2.0/building/index.html)
[1.26](https://numpy.org/doc/1.26/building/index.html)
[1.25](https://numpy.org/doc/1.25/building/index.html)
[1.24](https://numpy.org/doc/1.24/building/index.html)
[1.23](https://numpy.org/doc/1.23/building/index.html)
[1.22](https://numpy.org/doc/1.22/building/index.html)
[1.21](https://numpy.org/doc/1.21/building/index.html)
[1.20](https://numpy.org/doc/1.20/building/index.html)
[1.19](https://numpy.org/doc/1.19/building/index.html)
[1.18](https://numpy.org/doc/1.18/building/index.html)
[1.17](https://numpy.org/doc/1.17/building/index.html)
[1.16](https://numpy.org/doc/1.16/building/index.html)
[1.15](https://numpy.org/doc/1.15/building/index.html)
[1.14](https://numpy.org/doc/1.14/building/index.html)
[1.13](https://numpy.org/doc/1.13/building/index.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Building from source[#](https://numpy.org/doc/stable/building/index.html#building-from-source "Link to this heading")

======================================================================================================================

Note

If you are only trying to install NumPy, we recommend using binaries - see [Installation](https://numpy.org/install)
 for details on that.

Building NumPy from source requires setting up system-level dependencies (compilers, BLAS/LAPACK libraries, etc.) first, and then invoking a build. The build may be done in order to install NumPy for local usage, develop NumPy itself, or build redistributable binary packages. And it may be desired to customize aspects of how the build is done. This guide will cover all these aspects. In addition, it provides background information on how the NumPy build works, and links to up-to-date guides for generic Python build & packaging documentation that is relevant.

System-level dependencies[#](https://numpy.org/doc/stable/building/index.html#system-level-dependencies "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

NumPy uses compiled code for speed, which means you need compilers and some other system-level (i.e, non-Python / non-PyPI) dependencies to build it on your system.

Note

If you are using Conda, you can skip the steps in this section - with the exception of installing compilers for Windows or the Apple Developer Tools for macOS. All other dependencies will be installed automatically by the `mamba env create -f environment.yml` command.

 Linux

If you want to use the system Python and `pip`, you will need:

*   C and C++ compilers (typically GCC).
    
*   Python header files (typically a package named `python3-dev` or `python3-devel`)
    
*   BLAS and LAPACK libraries. [OpenBLAS](https://github.com/OpenMathLib/OpenBLAS/)
     is the NumPy default; other variants include Apple Accelerate, [MKL](https://software.intel.com/en-us/intel-mkl)
    , [ATLAS](https://math-atlas.sourceforge.net/)
     and [Netlib](https://www.netlib.org/lapack/index.html)
     (or “Reference”) BLAS and LAPACK.
    
*   `pkg-config` for dependency detection.
    
*   A Fortran compiler is needed only for running the `f2py` tests. The instructions below include a Fortran compiler, however you can safely leave it out.
    

 Debian/Ubuntu Linux

To install NumPy build requirements, you can do:

sudo apt install \-y gcc g++ gfortran libopenblas\-dev liblapack\-dev pkg\-config python3\-pip python3\-dev

Copy to clipboard

Alternatively, you can do:

sudo apt build\-dep numpy

Copy to clipboard

This command installs whatever is needed to build NumPy, with the advantage that new dependencies or updates to required versions are handled by the package managers.

 Fedora

To install NumPy build requirements, you can do:

sudo dnf install gcc\-gfortran python3\-devel openblas\-devel lapack\-devel pkgconfig

Copy to clipboard

Alternatively, you can do:

sudo dnf builddep numpy

Copy to clipboard

This command installs whatever is needed to build NumPy, with the advantage that new dependencies or updates to required versions are handled by the package managers.

 CentOS/RHEL

To install NumPy build requirements, you can do:

sudo yum install gcc\-gfortran python3\-devel openblas\-devel lapack\-devel pkgconfig

Copy to clipboard

Alternatively, you can do:

sudo yum\-builddep numpy

Copy to clipboard

This command installs whatever is needed to build NumPy, with the advantage that new dependencies or updates to required versions are handled by the package managers.

 Arch

To install NumPy build requirements, you can do:

sudo pacman \-S gcc\-fortran openblas pkgconf

Copy to clipboard

 macOS

Install Apple Developer Tools. An easy way to do this is to [open a terminal window](https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line)
, enter the command:

xcode\-select \--install

Copy to clipboard

and follow the prompts. Apple Developer Tools includes Git, the Clang C/C++ compilers, and other development utilities that may be required.

Do _not_ use the macOS system Python. Instead, install Python with [the python.org installer](https://www.python.org/downloads/)
 or with a package manager like Homebrew, MacPorts or Fink.

On macOS >=13.3, the easiest build option is to use Accelerate, which is already installed and will be automatically used by default.

On older macOS versions you need a different BLAS library, most likely OpenBLAS, plus pkg-config to detect OpenBLAS. These are easiest to install with [Homebrew](https://brew.sh/)
:

brew install openblas pkg\-config gfortran

Copy to clipboard

 Windows

Compared to macOS and Linux, building NumPy on Windows is a little more difficult, due to the need to set up compilers. First, install Microsoft Visual Studio - the 2019 Community Edition or any newer version will work (see the [Visual Studio download site](https://visualstudio.microsoft.com/downloads/)
). This is needed to ensure you have the Windows Universal C Runtime. The recommended version of the UCRT is >= 10.0.22621.0.

The MSVC installer does not put the compilers on the system path, and the install location may change. To query the install location, MSVC comes with a `vswhere.exe` command-line utility. And to make the C/C++ compilers available inside the shell you are using, you need to run a `.bat` file for the correct bitness and architecture (e.g., for 64-bit Intel CPUs, use `vcvars64.bat`).

For detailed guidance, see [Use the Microsoft C++ toolset from the command line](https://learn.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-170)
.

If you don’t need `f2py`, MSVC alone is sufficient. For Fortran compiler setup (needed for `f2py`), see [F2PY and Windows](https://numpy.org/doc/stable/f2py/windows/index.html#f2py-windows)
.

Note

Compilers should be on the system path (i.e., the `PATH` environment variable should contain the directory in which the compiler executables can be found) in order to be found, with the exception of MSVC which will be found automatically if and only if there are no other compilers on the `PATH`. You can use any shell (e.g., Powershell, `cmd` or Git Bash) to invoke a build.

Warning

When using a conda environment it is possible that the environment creation will not work due to an outdated Fortran compiler. If that happens, remove the `compilers` entry from `environment.yml` and try again. The Fortran compiler should be installed as described in the [F2PY Windows documentation](https://numpy.org/doc/stable/f2py/windows/index.html#f2py-windows)
.

 Windows on ARM64

In Windows on ARM64, the compiler options available for building NumPy are limited. GCC and gfortran are not yet supported. Currently, the NumPy build for Windows on ARM64 is supported with MSVC and LLVM toolchains.

First, install Microsoft Visual Studio - the 2022 Community Edition will work (see the [Visual Studio download site](https://visualstudio.microsoft.com/downloads/)
). Ensure that you have installed necessary Visual Studio components for building NumPy on WoA from [here](https://gist.github.com/Mugundanmcw/c3bb93018d5da9311fb2b222f205ba19)
.

The MSVC installer does not put the compilers on the system path, and the install location may change. To query the install location, MSVC comes with a `vswhere.exe` command-line utility. And to make the C/C++ compilers available inside the shell you are using, you need to run a `.bat` file for the correct bitness and architecture (e.g., for ARM64-based CPUs, use `vcvarsarm64.bat`).

For detailed guidance, see [Use the Microsoft C++ toolset from the command line](https://learn.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-170)
.

If you don’t need `f2py`, MSVC alone is sufficient. For Fortran compiler setup (needed for `f2py`), see [F2PY and Windows](https://numpy.org/doc/stable/f2py/windows/index.html#f2py-windows)
.

Note

Compilers should be on the system path (i.e., the `PATH` environment variable should contain the directory in which the compiler executables can be found) in order to be found, with the exception of MSVC which will be found automatically if and only if there are no other compilers on the `PATH`. You can use any shell (e.g., Powershell, `cmd` or Git Bash) to invoke a build.

Warning

Currently, Conda environment is not yet supported officially on [Windows on ARM64](https://github.com/conda-forge/conda-forge.github.io/issues/1940)
. The present approach uses virtualenv for building NumPy from source on Windows on ARM64.

Building NumPy from source[#](https://numpy.org/doc/stable/building/index.html#building-numpy-from-source "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

If you want to only install NumPy from source once and not do any development work, then the recommended way to build and install is to use `pip`. Otherwise, conda is recommended.

Note

If you don’t have a conda installation yet, we recommend using [Miniforge](https://github.com/conda-forge/miniforge)
; any conda flavor will work though.

### Building from source to use NumPy[#](https://numpy.org/doc/stable/building/index.html#building-from-source-to-use-numpy "Link to this heading")

 Conda env

If you are using a conda environment, `pip` is still the tool you use to invoke a from-source build of NumPy. It is important to always use the `--no-build-isolation` flag to the `pip install` command, to avoid building against a `numpy` wheel from PyPI. In order for that to work you must first install the remaining build dependencies into the conda environment:

\# Either install all NumPy dev dependencies into a fresh conda environment
mamba env create \-f environment.yml

\# Or, install only the required build dependencies
mamba install python numpy cython compilers openblas meson\-python pkg\-config

\# To build the latest stable release:
pip install numpy \--no\-build\-isolation \--no\-binary numpy

\# To build a development version, you need a local clone of the NumPy git repository:
git clone https://github.com/numpy/numpy.git
cd numpy
git submodule update \--init
pip install . \--no\-build\-isolation

Copy to clipboard

Warning

On Windows, the AR, LD, and LDFLAGS environment variables may be set, which will cause the pip install command to fail. These variables are only needed for flang and can be safely unset prior to running pip install.

 Virtual env or system Python

\# To build the latest stable release:
pip install numpy \--no\-binary numpy

\# To build a development version, you need a local clone of the NumPy git repository:
git clone https://github.com/numpy/numpy.git
cd numpy
git submodule update \--init
pip install .

Copy to clipboard

### Building from source for NumPy development[#](https://numpy.org/doc/stable/building/index.html#building-from-source-for-numpy-development "Link to this heading")

If you want to build from source in order to work on NumPy itself, first clone the NumPy repository:

git clone https://github.com/numpy/numpy.git
cd numpy
git submodule update \--init

Copy to clipboard

Then you want to do the following:

1.  Create a dedicated development environment (virtual environment or conda environment),
    
2.  Install all needed dependencies (_build_, and also _test_, _doc_ and _optional_ dependencies),
    
3.  Build NumPy with the `spin` developer interface.
    

Step (3) is always the same, steps (1) and (2) are different between conda and virtual environments:

 Conda env

To create a `numpy-dev` development environment with every required and optional dependency installed, run:

mamba env create \-f environment.yml
mamba activate numpy\-dev

Copy to clipboard

 Virtual env or system Python

Note

There are many tools to manage virtual environments, like `venv`, `virtualenv`/`virtualenvwrapper`, `pyenv`/`pyenv-virtualenv`, Poetry, PDM, Hatch, and more. Here we use the basic `venv` tool that is part of the Python stdlib. You can use any other tool; all we need is an activated Python environment.

Create and activate a virtual environment in a new directory named `venv` ( note that the exact activation command may be different based on your OS and shell - see [“How venvs work”](https://docs.python.org/3/library/venv.html#how-venvs-work)
 in the `venv` docs).

 Linux

python \-m venv venv
source venv/bin/activate

Copy to clipboard

 macOS

python \-m venv venv
source venv/bin/activate

Copy to clipboard

 Windows

python \-m venv venv
.\\venv\\Scripts\\activate

Copy to clipboard

 Windows on ARM64

python \-m venv venv
.\\venv\\Scripts\\activate

Copy to clipboard

Note

Building NumPy with BLAS and LAPACK functions requires OpenBLAS library at Runtime. In Windows on ARM64, this can be done by setting up pkg-config for OpenBLAS dependency. The build steps for OpenBLAS for Windows on ARM64 can be found [here](http://www.openmathlib.org/OpenBLAS/docs/install/#windows-on-arm)
.

Then install the Python-level dependencies from PyPI with:

python \-m pip install \-r requirements/build\_requirements.txt

Copy to clipboard

To build NumPy in an activated development environment, run:

spin build

Copy to clipboard

This will install NumPy inside the repository (by default in a `build-install` directory). You can then run tests (`spin test`), drop into IPython (`spin ipython`), or take other development steps like build the html documentation or running benchmarks. The `spin` interface is self-documenting, so please see `spin --help` and `spin <subcommand> --help` for detailed guidance.

Warning

In an activated conda environment on Windows, the AR, LD, and LDFLAGS environment variables may be set, which will cause the build to fail. These variables are only needed for flang and can be safely unset for build.

IDE support & editable installs

While the `spin` interface is our recommended way of working on NumPy, it has one limitation: because of the custom install location, NumPy installed using `spin` will not be recognized automatically within an IDE (e.g., for running a script via a “run” button, or setting breakpoints visually). This will work better with an _in-place build_ (or “editable install”).

Editable installs are supported. It is important to understand that **you may use either an editable install or** `spin` **in a given repository clone, but not both**. If you use editable installs, you have to use `pytest` and other development tools directly instead of using `spin`.

To use an editable install, ensure you start from a clean repository (run `git clean -xdf` if you’ve built with `spin` before) and have all dependencies set up correctly as described higher up on this page. Then do:

\# Note: the --no-build-isolation is important!
pip install \-e . \--no\-build\-isolation

\# To run the tests for, e.g., the \`numpy.linalg\` module:
pytest numpy/linalg

Copy to clipboard

When making changes to NumPy code, including to compiled code, there is no need to manually rebuild or reinstall. NumPy is automatically rebuilt each time NumPy is imported by the Python interpreter; see the [meson-python](https://mesonbuild.com/meson-python/)
 documentation on editable installs for more details on how that works under the hood.

When you run `git clean -xdf`, which removes the built extension modules, remember to also uninstall NumPy with `pip uninstall numpy`.

Warning

Note that editable installs are fundamentally incomplete installs. Their only guarantee is that `import numpy` works - so they are suitable for working on NumPy itself, and for working on pure Python packages that depend on NumPy. Headers, entrypoints, and other such things may not be available from an editable install.

Customizing builds[#](https://numpy.org/doc/stable/building/index.html#customizing-builds "Link to this heading")

------------------------------------------------------------------------------------------------------------------

*   [Compiler selection and customizing a build](https://numpy.org/doc/stable/building/compilers_and_options.html)
    
*   [BLAS and LAPACK](https://numpy.org/doc/stable/building/blas_lapack.html)
    
*   [CPU support & SIMD](https://numpy.org/doc/stable/building/cpu_simd.html)
    
*   [Cross compilation](https://numpy.org/doc/stable/building/cross_compilation.html)
    
*   [Building redistributable binaries](https://numpy.org/doc/stable/building/redistributable_binaries.html)
    

Background information[#](https://numpy.org/doc/stable/building/index.html#background-information "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

*   [Understanding Meson](https://numpy.org/doc/stable/building/understanding_meson.html)
    
*   [Introspecting build steps](https://numpy.org/doc/stable/building/introspecting_a_build.html)
    
*   [Meson and `distutils` ways of doing things](https://numpy.org/doc/stable/building/distutils_equivalents.html)
    

On this page