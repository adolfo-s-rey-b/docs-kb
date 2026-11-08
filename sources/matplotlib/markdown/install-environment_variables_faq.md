[Skip to main content](https://matplotlib.org/stable/install/environment_variables_faq.html#main-content)

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
    

Environment variables[#](https://matplotlib.org/stable/install/environment_variables_faq.html#environment-variables "Link to this heading")

============================================================================================================================================

HOME[#](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-HOME "Link to this definition")

The user's home directory. On Linux, [`~`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-HOME)
 is shorthand for [`HOME`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-HOME)
.

MPLBACKEND[#](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLBACKEND "Link to this definition")

This optional variable can be set to choose the Matplotlib backend. See [What is a backend?](https://matplotlib.org/stable/users/explain/figure/backends.html#what-is-a-backend)
.

MPLCONFIGDIR[#](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLCONFIGDIR "Link to this definition")

This is the directory used to store user customizations to Matplotlib, as well as some caches to improve performance. If [`MPLCONFIGDIR`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPLCONFIGDIR)
 is not defined, `_HOME_/.config/matplotlib` and `_HOME_/.cache/matplotlib` are used on Linux, and `_HOME_/.matplotlib` on other platforms, if they are writable. Otherwise, the Python standard library's [`tempfile.gettempdir`](https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir "(in Python v3.14)")
 is used to find a base directory in which the `matplotlib` subdirectory is created.

MPL\_IGNORE\_SYSTEM\_FONTS[#](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-MPL_IGNORE_SYSTEM_FONTS "Link to this definition")

When this variable is set, Matplotlib will update its font cache only with its own directories. This can be used to limit subprocess usage for querying system fonts.

PATH[#](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-PATH "Link to this definition")

The list of directories searched to find executable programs.

PYTHONPATH[#](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-PYTHONPATH "Link to this definition")

The list of directories that are added to Python's standard search list when importing packages and modules.

QT\_API[#](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-QT_API "Link to this definition")

The Python Qt wrapper to prefer when using Qt-based backends. See [the entry in the usage guide](https://matplotlib.org/stable/api/backend_qt_api.html#qt-bindings)
 for more information.

Setting environment variables in Linux and macOS[#](https://matplotlib.org/stable/install/environment_variables_faq.html#setting-environment-variables-in-linux-and-macos "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To list the current value of [`PYTHONPATH`](https://matplotlib.org/stable/install/environment_variables_faq.html#envvar-PYTHONPATH)
, which may be empty, try:

echo $PYTHONPATH

The procedure for setting environment variables in depends on what your default shell is. Common shells include **bash** and **csh**. You should be able to determine which by running at the command prompt:

echo $SHELL

To create a new environment variable:

export PYTHONPATH\=~/Python  \# bash/ksh
setenv PYTHONPATH ~/Python  \# csh/tcsh

To prepend to an existing environment variable:

export PATH=~/bin:${PATH}  # bash/ksh
setenv PATH ~/bin:${PATH}  # csh/tcsh

The search order may be important to you, do you want `~/bin` to be searched first or last? To append to an existing environment variable:

export PATH=${PATH}:~/bin  # bash/ksh
setenv PATH ${PATH}:~/bin  # csh/tcsh

To make your changes available in the future, add the commands to your `~/.bashrc` or `~/.cshrc` file.

Setting environment variables in Windows[#](https://matplotlib.org/stable/install/environment_variables_faq.html#setting-environment-variables-in-windows "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Open the **Control Panel** (Start ‣ Control Panel), start the **System** program. Click the Advanced tab and select the Environment Variables button. You can edit or add to the User Variables.

On this page