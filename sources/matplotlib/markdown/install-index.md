[Skip to main content](https://matplotlib.org/stable/install/index.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Installation[#](https://matplotlib.org/stable/install/index.html#installation "Link to this heading")

======================================================================================================

 pip

pip install matplotlib

 conda

conda install \-c conda-forge matplotlib

 pixi

pixi add matplotlib

 uv

uv add matplotlib

Warning

uv usually installs its own versions of Python from the python-build-standalone project, and only recent versions of those Python builds (August 2025) work properly with the `tkagg` backend for displaying plots in a window. Please make sure you are using uv 0.8.7 or newer (update with e.g. `uv self update`) and that your bundled Python installs are up to date (with `uv python upgrade --reinstall`). Alternatively, you can use one of the other [supported GUI frameworks](https://matplotlib.org/stable/install/dependencies.html#optional-dependencies)
, e.g.

uv add matplotlib pyside6

 other

[Install an official release](https://matplotlib.org/stable/install/index.html#install-official)

[Third-party distributions](https://matplotlib.org/stable/install/index.html#install-third-party)

[Install a nightly build](https://matplotlib.org/stable/install/index.html#install-nightly-build)

[Install from source](https://matplotlib.org/stable/install/index.html#install-source)

Install an official release[#](https://matplotlib.org/stable/install/index.html#install-an-official-release "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Matplotlib releases are available as wheel packages for macOS, Windows and Linux on [PyPI](https://pypi.org/project/matplotlib/)
. Install it using `pip`:

python \-m pip install \-U pip
python \-m pip install \-U matplotlib

If this command results in Matplotlib being compiled from source and there's trouble with the compilation, you can add `--prefer-binary` to select the newest version of Matplotlib for which there is a precompiled wheel for your OS and Python.

Note

The following non-interactive backends work out of the box: Agg, ps, pdf, svg

The TkAgg interactive backend also typically works out of the box. It requires Tk bindings, which are usually provided via the Python standard library's `tkinter` module. On some OSes, you may need to install a separate package like `python3-tk` to add this component of the standard library.

Some tools like `uv` make use of Python builds from the python-build-standalone project, which only gained usable Tk bindings recently (August 2025). If you are having trouble with the TkAgg backend, ensure you have an up-to-date build, e.g. `uv self update && uv python upgrade --reinstall`.

For support of other GUI frameworks, LaTeX rendering, saving animations and a larger selection of file formats, you can install [optional dependencies](https://matplotlib.org/stable/install/dependencies.html#optional-dependencies)
.

Third-party distributions[#](https://matplotlib.org/stable/install/index.html#third-party-distributions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Various third-parties provide Matplotlib for their environments.

### Conda packages[#](https://matplotlib.org/stable/install/index.html#conda-packages "Link to this heading")

Matplotlib is available both via the _anaconda main channel_

conda install matplotlib

as well as via the _conda-forge community channel_

conda install \-c conda-forge matplotlib

### Python distributions[#](https://matplotlib.org/stable/install/index.html#python-distributions "Link to this heading")

Matplotlib is part of major Python distributions:

*   [Anaconda](https://www.anaconda.com/)
    
*   [ActiveState ActivePython](https://www.activestate.com/products/python/downloads/)
    
*   [WinPython](https://winpython.github.io/)
    

### Linux package manager[#](https://matplotlib.org/stable/install/index.html#linux-package-manager "Link to this heading")

If you are using the Python version that comes with your Linux distribution, you can install Matplotlib via your package manager, e.g.:

*   Debian / Ubuntu: `sudo apt-get install python3-matplotlib`
    
*   Fedora: `sudo dnf install python3-matplotlib`
    
*   Red Hat: `sudo yum install python3-matplotlib`
    
*   Arch: `sudo pacman -S python-matplotlib`
    

Install a nightly build[#](https://matplotlib.org/stable/install/index.html#install-a-nightly-build "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Matplotlib makes nightly development build wheels available on the [scientific-python-nightly-wheels Anaconda Cloud organization](https://anaconda.org/scientific-python-nightly-wheels)
. These wheels can be installed with `pip` by specifying scientific-python-nightly-wheels as the package index to query:

python \-m pip install \--upgrade \--pre \--index-url https://pypi.anaconda.org/scientific-python-nightly-wheels/simple \--extra-index-url https://pypi.org/simple matplotlib

Install from source[#](https://matplotlib.org/stable/install/index.html#install-from-source "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

Installing for Development

If you would like to contribute to Matplotlib or otherwise need to install the latest development code, please follow the instructions in [Development setup](https://matplotlib.org/stable/devel/development_setup.html#installing-for-devs)
.

The following instructions are for installing from source for production use. This is generally _not_ recommended; please use prebuilt packages when possible. Proceed with caution because these instructions may result in your build producing unexpected behavior and/or causing local testing to fail.

Before trying to install Matplotlib, please install the [Dependencies](https://matplotlib.org/stable/install/dependencies.html#dependencies)
.

To build from a tarball, download the latest _tar.gz_ release file from [the PyPI files page](https://pypi.org/project/matplotlib/)
.

If you are building your own Matplotlib wheels (or sdists) on Windows, note that any DLLs that you copy into the source tree will be packaged too.

Configure build and behavior defaults[#](https://matplotlib.org/stable/install/index.html#configure-build-and-behavior-defaults "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

We provide a [meson.options](https://github.com/matplotlib/matplotlib/blob/main/meson.options)
 file containing options with which you can use to customize the build process. For example, which default backend to use, whether some of the optional libraries that Matplotlib ships with are installed, and so on. These options will be particularly useful to those packaging Matplotlib.

Aspects of some behavioral defaults of the library can be configured via:

*   [Environment variables](https://matplotlib.org/stable/install/environment_variables_faq.html)
    *   [Setting environment variables in Linux and macOS](https://matplotlib.org/stable/install/environment_variables_faq.html#setting-environment-variables-in-linux-and-macos)
        
    *   [Setting environment variables in Windows](https://matplotlib.org/stable/install/environment_variables_faq.html#setting-environment-variables-in-windows)
        

Default plotting appearance and behavior can be configured via the [rcParams file](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)
.

Dependencies[#](https://matplotlib.org/stable/install/index.html#dependencies "Link to this heading")

------------------------------------------------------------------------------------------------------

Mandatory dependencies should be installed automatically if you install Matplotlib using a package manager such as `pip` or `conda`; therefore this list is primarily for reference and troubleshooting.

*   [Dependencies](https://matplotlib.org/stable/install/dependencies.html)
    *   [Runtime dependencies](https://matplotlib.org/stable/install/dependencies.html#runtime-dependencies)
        
    *   [Build dependencies](https://matplotlib.org/stable/install/dependencies.html#build-dependencies)
        
    *   [Test dependencies](https://matplotlib.org/stable/install/dependencies.html#test-dependencies)
        
    *   [Documentation dependencies](https://matplotlib.org/stable/install/dependencies.html#documentation-dependencies)
        

Frequently asked questions[#](https://matplotlib.org/stable/install/index.html#frequently-asked-questions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

### Report a compilation problem[#](https://matplotlib.org/stable/install/index.html#report-a-compilation-problem "Link to this heading")

See [Get help](https://matplotlib.org/stable/users/faq.html#reporting-problems)
.

### Matplotlib compiled fine, but nothing shows up when I use it[#](https://matplotlib.org/stable/install/index.html#matplotlib-compiled-fine-but-nothing-shows-up-when-i-use-it "Link to this heading")

The first thing to try is a [clean install](https://matplotlib.org/stable/install/index.html#clean-install)
 and see if that helps. If not, the best way to test your install is by running a script, rather than working interactively from a python shell or an integrated development environment such as **IDLE** which add additional complexities. Open up a UNIX shell or a DOS command prompt and run, for example:

python \-c "from pylab import \*; set\_loglevel('DEBUG'); plot(); show()"

This will give you additional information about which backends Matplotlib is loading, version information, and more. At this point you might want to make sure you understand Matplotlib's [configuration](https://matplotlib.org/stable/users/explain/customizing.html#customizing)
 process, governed by the `matplotlibrc` configuration file which contains instructions within and the concept of the Matplotlib backend.

If you are still having trouble, see [Get help](https://matplotlib.org/stable/users/faq.html#reporting-problems)
.

### How to completely remove Matplotlib[#](https://matplotlib.org/stable/install/index.html#how-to-completely-remove-matplotlib "Link to this heading")

Occasionally, problems with Matplotlib can be solved with a clean installation of the package. In order to fully remove an installed Matplotlib:

1.  Delete the caches from your [Matplotlib configuration directory](https://matplotlib.org/stable/install/index.html#locating-matplotlib-config-dir)
    .
    
2.  Delete any Matplotlib directories or eggs from your [installation directory](https://matplotlib.org/stable/install/index.html#locating-matplotlib-install)
    .
    

### macOS Notes[#](https://matplotlib.org/stable/install/index.html#macos-notes "Link to this heading")

#### Which python for macOS?[#](https://matplotlib.org/stable/install/index.html#which-python-for-macos "Link to this heading")

Apple ships macOS with its own Python, in `/usr/bin/python`, and its own copy of Matplotlib. Unfortunately, the way Apple currently installs its own copies of NumPy, Scipy and Matplotlib means that these packages are difficult to upgrade (see [system python packages](https://github.com/MacPython/wiki/wiki/Which-Python#system-python-and-extra-python-packages)
). For that reason we strongly suggest that you install a fresh version of Python and use that as the basis for installing libraries such as NumPy and Matplotlib. One convenient way to install Matplotlib with other useful Python software is to use the [Anaconda](https://www.anaconda.com/)
 Python scientific software collection, which includes Python itself and a wide range of libraries; if you need a library that is not available from the collection, you can install it yourself using standard methods such as _pip_. See the Anaconda web page for installation support.

Other options for a fresh Python install are the standard installer from [python.org](https://www.python.org/downloads/macos/)
, or installing Python using a general macOS package management system such as [homebrew](https://brew.sh/)
 or [macports](https://www.macports.org/)
. Power users on macOS will likely want one of homebrew or macports on their system to install open source software packages, but it is perfectly possible to use these systems with another source for your Python binary, such as Anaconda or Python.org Python.

#### Installing macOS binary wheels[#](https://matplotlib.org/stable/install/index.html#installing-macos-binary-wheels "Link to this heading")

If you are using Python from [https://www.python.org](https://www.python.org/)
, Homebrew, or Macports, then you can use the standard pip installer to install Matplotlib binaries in the form of wheels.

pip is installed by default with python.org and Homebrew Python, but needs to be manually installed on Macports with

sudo port install py38-pip

Once pip is installed, you can install Matplotlib and all its dependencies with from the Terminal.app command line:

python3 \-m pip install matplotlib

You might also want to install IPython or the Jupyter notebook (`python3 -m pip install ipython notebook`).

#### Checking your installation[#](https://matplotlib.org/stable/install/index.html#checking-your-installation "Link to this heading")

The new version of Matplotlib should now be on your Python "path". Check this at the Terminal.app command line:

python3 \-c 'import matplotlib; print(matplotlib.\_\_version\_\_, matplotlib.\_\_file\_\_)'

You should see something like

3.10.0 /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/matplotlib/\_\_init\_\_.py

where `3.10.0` is the Matplotlib version you just installed, and the path following depends on whether you are using Python.org Python, Homebrew or Macports. If you see another version, or you get an error like

Traceback (most recent call last):
  File "<string>", line 1, in <module>
ImportError: No module named matplotlib

then check that the Python binary is the one you expected by running

which python3

If you get a result like `/usr/bin/python...`, then you are getting the Python installed with macOS, which is probably not what you want. Try closing and restarting Terminal.app before running the check again. If that doesn't fix the problem, depending on which Python you wanted to use, consider reinstalling Python.org Python, or check your homebrew or macports setup. Remember that the disk image installer only works for Python.org Python, and will not get picked up by other Pythons. If all these fail, please [let us know](https://matplotlib.org/stable/users/faq.html#reporting-problems)
.

Troubleshooting[#](https://matplotlib.org/stable/install/index.html#troubleshooting "Link to this heading")

------------------------------------------------------------------------------------------------------------

### Obtaining Matplotlib version[#](https://matplotlib.org/stable/install/index.html#obtaining-matplotlib-version "Link to this heading")

To find out your Matplotlib version number, import it and print the `__version__` attribute:

\>>> import matplotlib
\>>> matplotlib.\_\_version\_\_
'0.98.0'

### `matplotlib` install location[#](https://matplotlib.org/stable/install/index.html#matplotlib-install-location "Link to this heading")

You can find what directory Matplotlib is installed in by importing it and printing the `__file__` attribute:

\>>> import matplotlib
\>>> matplotlib.\_\_file\_\_
'/home/jdhunter/dev/lib64/python2.5/site-packages/matplotlib/\_\_init\_\_.pyc'

### `matplotlib` configuration and cache directory locations[#](https://matplotlib.org/stable/install/index.html#matplotlib-configuration-and-cache-directory-locations "Link to this heading")

Each user has a Matplotlib configuration directory which may contain a [matplotlibrc](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-matplotlibrc-files)
 file. To locate your `matplotlib/` configuration directory, use [`matplotlib.get_configdir()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_configdir "matplotlib.get_configdir")
:

\>>> import matplotlib as mpl
\>>> mpl.get\_configdir()
'/home/darren/.config/matplotlib'

On Unix-like systems, this directory is generally located in your [`HOME`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-HOME)
 directory under the `.config/` directory.

In addition, users have a cache directory. On Unix-like systems, this is separate from the configuration directory by default. To locate your `.cache/` directory, use [`matplotlib.get_cachedir()`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_cachedir "matplotlib.get_cachedir")
:

\>>> import matplotlib as mpl
\>>> mpl.get\_cachedir()
'/home/darren/.cache/matplotlib'

On Windows, both the config directory and the cache directory are the same and are in your `Documents and Settings` or `Users` directory by default:

\>>> import matplotlib as mpl
\>>> mpl.get\_configdir()
'C:\\\\Documents and Settings\\\\jdhunter\\\\.matplotlib'
\>>> mpl.get\_cachedir()
'C:\\\\Documents and Settings\\\\jdhunter\\\\.matplotlib'

If you would like to use a different configuration directory, you can do so by specifying the location in your [`MPLCONFIGDIR`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLCONFIGDIR)
 environment variable -- see [Setting environment variables in Linux and macOS](https://matplotlib.org/stable/install/environment_variables_faq.html#setting-linux-macos-environment-variables)
. Note that [`MPLCONFIGDIR`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLCONFIGDIR)
 sets the location of both the configuration directory and the cache directory.

On this page