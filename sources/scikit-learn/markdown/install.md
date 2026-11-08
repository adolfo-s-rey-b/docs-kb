[Skip to main content](https://scikit-learn.org/stable/install.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

Choose version

Installing scikit-learn[#](https://scikit-learn.org/stable/install.html#installing-scikit-learn "Link to this heading")

========================================================================================================================

There are different ways to install scikit-learn:

*   [Install the latest official release](https://scikit-learn.org/stable/install.html#install-official-release)
    . This is the best approach for most users. It will provide a stable version and pre-built packages are available for most platforms.
    
*   Install the version of scikit-learn provided by your [operating system or Python distribution](https://scikit-learn.org/stable/install.html#install-by-distribution)
    . This is a quick option for those who have operating systems or Python distributions that distribute scikit-learn. It might not provide the latest release version.
    
*   [Install a nightly build](https://scikit-learn.org/stable/install.html#install-nightly-builds)
    . This is the quickest way to try a new feature that will be shipped in the next release (that is, a feature from a pull-request that was recently merged to the main branch); or to check whether a bug you encountered has been fixed since the last release.
    
*   [Building the package from source](https://scikit-learn.org/stable/developers/development_setup.html#setup-development-environment)
    . This is mainly needed by users who wish to contribute to the project, as this allows to install an editable version of the project.
    

Installing the latest release[#](https://scikit-learn.org/stable/install.html#installing-the-latest-release "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

 Windows

 pip

Install the 64-bit version of Python 3, for instance from the [official website](https://www.python.org/downloads/windows/)
.

Now create a [virtual environment (venv)](https://docs.python.org/3/tutorial/venv.html)
 and install scikit-learn. Note that the virtual environment is optional but strongly recommended, in order to avoid potential conflicts with other packages.

python \-m venv sklearn-env
sklearn-env\\Scripts\\activate  \# activate
pip install \-U scikit-learn

Copy to clipboard

In order to check your installation, you can use:

python \-m pip show scikit-learn  \# show scikit-learn version and location
python \-m pip freeze             \# show all installed packages in the environment
python \-c "import sklearn; sklearn.show\_versions()"

Copy to clipboard

 conda

Install conda using the [conda-forge installers](https://conda-forge.org/download/)
 (no administrator permission required). Then run:

conda create \-n sklearn-env \-c conda-forge scikit-learn
conda activate sklearn-env

Copy to clipboard

In order to check your installation, you can use:

conda list scikit-learn  \# show scikit-learn version and location
conda list               \# show all installed packages in the environment
python \-c "import sklearn; sklearn.show\_versions()"

Copy to clipboard

 MacOS

 pip

Install Python 3 using [homebrew](https://brew.sh/)
 (`brew install python`) or by manually installing the package from the [official website](https://www.python.org/downloads/macos/)
.

Now create a [virtual environment (venv)](https://docs.python.org/3/tutorial/venv.html)
 and install scikit-learn. Note that the virtual environment is optional but strongly recommended, in order to avoid potential conflicts with other packages.

python \-m venv sklearn-env
source sklearn-env/bin/activate  \# activate
pip install \-U scikit-learn

Copy to clipboard

In order to check your installation, you can use:

python \-m pip show scikit-learn  \# show scikit-learn version and location
python \-m pip freeze             \# show all installed packages in the environment
python \-c "import sklearn; sklearn.show\_versions()"

Copy to clipboard

 conda

Install conda using the [conda-forge installers](https://conda-forge.org/download/)
 (no administrator permission required). Then run:

conda create \-n sklearn-env \-c conda-forge scikit-learn
conda activate sklearn-env

Copy to clipboard

In order to check your installation, you can use:

conda list scikit-learn  \# show scikit-learn version and location
conda list               \# show all installed packages in the environment
python \-c "import sklearn; sklearn.show\_versions()"

Copy to clipboard

 Linux

 pip

Python 3 is usually installed by default on most Linux distributions. To check if you have it installed, try:

python3 \--version
pip3 \--version

Copy to clipboard

If you don’t have Python 3 installed, please install `python3` and `python3-pip` from your distribution’s package manager.

Now create a [virtual environment (venv)](https://docs.python.org/3/tutorial/venv.html)
 and install scikit-learn. Note that the virtual environment is optional but strongly recommended, in order to avoid potential conflicts with other packages.

python3 \-m venv sklearn-env
source sklearn-env/bin/activate  \# activate
pip3 install \-U scikit-learn

Copy to clipboard

In order to check your installation, you can use:

python3 \-m pip show scikit-learn  \# show scikit-learn version and location
python3 \-m pip freeze             \# show all installed packages in the environment
python3 \-c "import sklearn; sklearn.show\_versions()"

Copy to clipboard

 conda

Install conda using the [conda-forge installers](https://conda-forge.org/download/)
 (no administrator permission required). Then run:

conda create \-n sklearn-env \-c conda-forge scikit-learn
conda activate sklearn-env

Copy to clipboard

In order to check your installation, you can use:

conda list scikit-learn  \# show scikit-learn version and location
conda list               \# show all installed packages in the environment
python \-c "import sklearn; sklearn.show\_versions()"

Copy to clipboard

Using an isolated environment such as pip venv or conda makes it possible to install a specific version of scikit-learn with pip or conda and its dependencies independently of any previously installed Python packages. In particular under Linux it is discouraged to install pip packages alongside the packages managed by the package manager of the distribution (apt, dnf, pacman…).

Note that you should always remember to activate the environment of your choice prior to running any Python command whenever you start a new terminal session.

If you have not installed NumPy or SciPy yet, you can also install these using conda or pip. When using pip, please ensure that _binary wheels_ are used, and NumPy and SciPy are not recompiled from source, which can happen when using particular configurations of operating system and hardware (such as Linux on a Raspberry Pi).

Scikit-learn plotting capabilities (i.e., functions starting with `plot_` and classes ending with `Display`) require Matplotlib. The examples require Matplotlib and some examples require scikit-image, pandas, or seaborn. The minimum version of scikit-learn dependencies are listed below along with its purpose.

| Dependency | Minimum Version | Purpose |
| --- | --- | --- |
| numpy | 1.24.1 | build, install |
| scipy | 1.10.0 | build, install |
| joblib | 1.4.0 | install |
| narwhals | 2.0.1 | install |
| threadpoolctl | 3.5.0 | install |
| cython | 3.1.2 | build |
| meson-python | 0.17.1 | build |
| matplotlib | 3.6.1 | benchmark, docs, examples, tests |
| scikit-image | 0.22.0 | docs, examples |
| pandas | 1.5.0 | benchmark, docs, examples, tests |
| rich | 14.1.0 | docs, examples, tests |
| seaborn | 0.13.0 | docs, examples |
| memory\_profiler | 0.57.0 | benchmark, docs |
| pytest | 7.1.2 | tests |
| pytest-cov | 2.9.0 | tests |
| ruff | 0.12.2 | tests |
| pyrefly | 1.2.0 | tests |
| cython-lint | 0.21 | tests |
| sphinx-lint | 1.0.2 | tests |
| codespell | 2.4.1 | tests |
| pyamg | 5.0.0 | tests |
| polars | 0.20.30 | docs, tests |
| pyarrow | 13.0.0 | tests |
| sphinx | 7.3.7 | docs |
| sphinx-copybutton | 0.5.2 | docs |
| sphinx-gallery | 0.17.1 | docs |
| numpydoc | 1.2.0 | docs, tests |
| Pillow | 12.1.1 | docs |
| pooch | 1.8.0 | docs, examples, tests |
| sphinx-prompt | 1.4.0 | docs |
| sphinxext-opengraph | 0.9.1 | docs |
| plotly | 5.22.0 | docs, examples |
| sphinx-remove-toctrees | 1.0.0.post1 | docs |
| sphinx-design | 0.6.0 | docs |
| pydata-sphinx-theme | 0.15.3 | docs |
| towncrier | 24.8.0 | docs |
| conda-lock | 3.0.1 | maintenance |

Warning

Scikit-learn 0.20 was the last version to support Python 2.7 and Python 3.4.

Scikit-learn 0.21 supported Python 3.5—3.7.

Scikit-learn 0.22 supported Python 3.5—3.8.

Scikit-learn 0.23 required Python 3.6—3.8.

Scikit-learn 0.24 required Python 3.6—3.9.

Scikit-learn 1.0 supported Python 3.7—3.10.

Scikit-learn 1.1, 1.2 and 1.3 supported Python 3.8—3.12.

Scikit-learn 1.4 and 1.5 supported Python 3.9—3.12.

Scikit-learn 1.6 supported Python 3.9—3.13.

Scikit-learn 1.7 requires Python 3.10 or newer.

Third party distributions of scikit-learn[#](https://scikit-learn.org/stable/install.html#third-party-distributions-of-scikit-learn "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

Some third-party distributions provide versions of scikit-learn integrated with their package-management systems.

These can make installation and upgrading much easier for users since the integration includes the ability to automatically install dependencies (numpy, scipy) that scikit-learn requires.

The following is an incomplete list of OS and python distributions that provide their own version of scikit-learn.

### Alpine Linux[#](https://scikit-learn.org/stable/install.html#alpine-linux "Link to this heading")

Alpine Linux’s package is provided through the [official repositories](https://pkgs.alpinelinux.org/packages?name=py3-scikit-learn)
 as `py3-scikit-learn` for Python. It can be installed by typing the following command:

sudo apk add py3-scikit-learn

Copy to clipboard

### Arch Linux[#](https://scikit-learn.org/stable/install.html#arch-linux "Link to this heading")

Arch Linux’s package is provided through the [official repositories](https://www.archlinux.org/packages/?q=scikit-learn)
 as `python-scikit-learn` for Python. It can be installed by typing the following command:

sudo pacman \-S python-scikit-learn

Copy to clipboard

### Debian/Ubuntu[#](https://scikit-learn.org/stable/install.html#debian-ubuntu "Link to this heading")

The Debian/Ubuntu package is split in three different packages called `python3-sklearn` (python modules), `python3-sklearn-lib` (low-level implementations and bindings), `python-sklearn-doc` (documentation). Note that scikit-learn requires Python 3, hence the need to use the `python3-` suffixed package names. Packages can be installed using `apt-get`:

sudo apt-get install python3-sklearn python3-sklearn-lib python-sklearn-doc

Copy to clipboard

### Fedora[#](https://scikit-learn.org/stable/install.html#fedora "Link to this heading")

The Fedora package is called `python3-scikit-learn` for the python 3 version, the only one available in Fedora. It can be installed using `dnf`:

sudo dnf install python3-scikit-learn

Copy to clipboard

### NetBSD[#](https://scikit-learn.org/stable/install.html#netbsd "Link to this heading")

scikit-learn is available via [pkgsrc-wip](https://pkgsrc-wip.sourceforge.net/)
: [https://pkgsrc.se/math/py-scikit-learn](https://pkgsrc.se/math/py-scikit-learn)

### MacPorts for Mac OSX[#](https://scikit-learn.org/stable/install.html#macports-for-mac-osx "Link to this heading")

The MacPorts package is named `py<XY>-scikit-learn`, where `XY` denotes the Python version. It can be installed by typing the following command:

sudo port install py312-scikit-learn

Copy to clipboard

### Anaconda and Enthought Deployment Manager for all supported platforms[#](https://scikit-learn.org/stable/install.html#anaconda-and-enthought-deployment-manager-for-all-supported-platforms "Link to this heading")

[Anaconda](https://www.anaconda.com/download)
 and [Enthought Deployment Manager](https://assets.enthought.com/downloads/)
 both ship with scikit-learn in addition to a large set of scientific python library for Windows, Mac OSX and Linux.

Anaconda offers scikit-learn as part of its free distribution.

### Intel Extension for Scikit-learn[#](https://scikit-learn.org/stable/install.html#intel-extension-for-scikit-learn "Link to this heading")

Intel maintains an optimized x86\_64 package, available in PyPI (via `pip`), and in the `main`, `conda-forge` and `intel` conda channels:

conda install scikit-learn-intelex

Copy to clipboard

This package has an Intel optimized version of many estimators. Whenever an alternative implementation doesn’t exist, scikit-learn implementation is used as a fallback. Those optimized solvers come from the oneDAL C++ library and are optimized for the x86\_64 architecture, and are optimized for multi-core Intel CPUs.

Note that those solvers are not enabled by default, please refer to the [scikit-learn-intelex](https://uxlfoundation.github.io/scikit-learn-intelex/latest/patching.html)
 documentation for more details on usage scenarios. Direct export example:

from sklearnex.neighbors import NearestNeighbors

Copy to clipboard

Compatibility with the standard scikit-learn solvers is checked by running the full scikit-learn test suite via automated continuous integration as reported on [intel/scikit-learn-intelex](https://github.com/intel/scikit-learn-intelex)
. If you observe any issue with `scikit-learn-intelex`, please report the issue on their [issue tracker](https://github.com/intel/scikit-learn-intelex/issues)
.

### WinPython for Windows[#](https://scikit-learn.org/stable/install.html#winpython-for-windows "Link to this heading")

The [WinPython](https://winpython.github.io/)
 project distributes scikit-learn as an additional plugin.

Troubleshooting[#](https://scikit-learn.org/stable/install.html#troubleshooting "Link to this heading")

--------------------------------------------------------------------------------------------------------

If you encounter unexpected failures when installing scikit-learn, you may submit an issue to the [issue tracker](https://github.com/scikit-learn/scikit-learn/issues)
. Before that, please also make sure to check the following common issues.

### Error caused by file path length limit on Windows[#](https://scikit-learn.org/stable/install.html#error-caused-by-file-path-length-limit-on-windows "Link to this heading")

It can happen that pip fails to install packages when reaching the default path size limit of Windows if Python is installed in a nested location such as the `AppData` folder structure under the user home directory, for instance:

C:\\Users\\username\>C:\\Users\\username\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe \-m pip install scikit\-learn
Collecting scikit\-learn
...
Installing collected packages: scikit\-learn
ERROR: Could not install packages due to an OSError: \[Errno 2\] No such file or directory: 'C:\\\\Users\\\\username\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.7\_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python37\\\\site-packages\\\\sklearn\\\\datasets\\\\tests\\\\data\\\\openml\\\\292\\\\api-v1-json-data-list-data\_name-australian-limit-2-data\_version-1-status-deactivated.json.gz'

Copy to clipboard

In this case it is possible to lift that limit in the Windows registry by using the `regedit` tool:

1.  Type “regedit” in the Windows start menu to launch `regedit`.
    
2.  Go to the `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem` key.
    
3.  Edit the value of the `LongPathsEnabled` property of that key and set it to 1.
    
4.  Reinstall scikit-learn (ignoring the previous broken installation):
    
    pip install \-\-exists-action\=i scikit-learn
    
    Copy to clipboard
    

Installing nightly builds[#](https://scikit-learn.org/stable/install.html#installing-nightly-builds "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

The continuous integration servers of the scikit-learn project build, test and upload wheel packages for the most recent Python version on a nightly basis.

You can install the nightly build of scikit-learn using the `scientific-python-nightly-wheels` index from the PyPI registry of `anaconda.org`:

pip install \--pre \--extra-index https://pypi.anaconda.org/scientific-python-nightly-wheels/simple scikit-learn

Copy to clipboard

Note that first uninstalling scikit-learn might be required to be able to install nightly builds of scikit-learn.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)