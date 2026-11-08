### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/builtins.html "builtins — Built-in objects")
     |
*   [previous](https://docs.python.org/3/library/sys.monitoring.html "sys.monitoring — Execution event monitoring")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)
     »
*   [`sysconfig` — Provide access to Python’s configuration information](https://docs.python.org/3/library/sysconfig.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`sysconfig` — Provide access to Python’s configuration information[¶](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "Link to this heading")

================================================================================================================================================================

Added in version 3.2.

**Source code:** [Lib/sysconfig](https://github.com/python/cpython/tree/3.15/Lib/sysconfig)

* * *

The `sysconfig` module provides access to Python’s configuration information like the list of installation paths and the configuration variables relevant for the current platform.

Configuration variables[¶](https://docs.python.org/3/library/sysconfig.html#configuration-variables "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

A Python distribution contains a `Makefile` and a `pyconfig.h` header file that are necessary to build both the Python binary itself and third-party C extensions compiled using `setuptools`.

`sysconfig` puts all variables found in these files in a dictionary that can be accessed using [`get_config_vars()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_vars "sysconfig.get_config_vars")
 or [`get_config_var()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_var "sysconfig.get_config_var")
.

Notice that on Windows, it’s a much smaller set.

sysconfig.get\_config\_vars(_\*args_)[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_vars "Link to this definition")

With no arguments, return a dictionary of all configuration variables relevant for the current platform.

With arguments, return a list of values that result from looking up each argument in the configuration variable dictionary.

For each argument, if the value is not found, return `None`.

sysconfig.get\_config\_var(_name_)[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_var "Link to this definition")

Return the value of a single variable _name_. Equivalent to `get_config_vars().get(name)`.

If _name_ is not found, return `None`.

Example of usage:

Copy

\>>> import sysconfig
\>>> sysconfig.get\_config\_var('Py\_ENABLE\_SHARED')
0
\>>> sysconfig.get\_config\_var('LIBDIR')
'/usr/local/lib'
\>>> sysconfig.get\_config\_vars('AR', 'CXX')
\['ar', 'g++'\]

Installation paths[¶](https://docs.python.org/3/library/sysconfig.html#installation-paths "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Python uses an installation scheme that differs depending on the platform and on the installation options. These schemes are stored in `sysconfig` under unique identifiers based on the value returned by [`os.name`](https://docs.python.org/3/library/os.html#os.name "os.name")
. The schemes are used by package installers to determine where to copy files to.

Python currently supports nine schemes:

*   _posix\_prefix_: scheme for POSIX platforms like Linux or macOS. This is the default scheme used when Python or a component is installed.
    
*   _posix\_home_: scheme for POSIX platforms, when the _home_ option is used. This scheme defines paths located under a specific home prefix.
    
*   _posix\_user_: scheme for POSIX platforms, when the _user_ option is used. This scheme defines paths located under the user’s home directory ([`site.USER_BASE`](https://docs.python.org/3/library/site.html#site.USER_BASE "site.USER_BASE")
    ).
    
*   _posix\_venv_: scheme for [`Python virtual environments`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.")
     on POSIX platforms; by default it is the same as _posix\_prefix_.
    
*   _nt_: scheme for Windows. This is the default scheme used when Python or a component is installed.
    
*   _nt\_user_: scheme for Windows, when the _user_ option is used.
    
*   _nt\_venv_: scheme for [`Python virtual environments`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.")
     on Windows; by default it is the same as _nt_.
    
*   _venv_: a scheme with values from either _posix\_venv_ or _nt\_venv_ depending on the platform Python runs on.
    
*   _osx\_framework\_user_: scheme for macOS, when the _user_ option is used.
    

Each scheme is itself composed of a series of paths and each path has a unique identifier. Python currently uses eight paths:

*   _stdlib_: directory containing the standard Python library files that are not platform-specific.
    
*   _platstdlib_: directory containing the standard Python library files that are platform-specific.
    
*   _platlib_: directory for site-specific, platform-specific files.
    
*   _purelib_: directory for site-specific, non-platform-specific files (‘pure’ Python).
    
*   _include_: directory for non-platform-specific header files for the Python C-API.
    
*   _platinclude_: directory for platform-specific header files for the Python C-API.
    
*   _scripts_: directory for script files.
    
*   _data_: directory for data files.
    

User scheme[¶](https://docs.python.org/3/library/sysconfig.html#user-scheme "Link to this heading")

----------------------------------------------------------------------------------------------------

This scheme is designed to be the most convenient solution for users that don’t have write permission to the global site-packages directory or don’t want to install into it.

Files will be installed into subdirectories of [`site.USER_BASE`](https://docs.python.org/3/library/site.html#site.USER_BASE "site.USER_BASE")
 (written as `_userbase_` hereafter). This scheme installs pure Python modules and extension modules in the same location (also known as [`site.USER_SITE`](https://docs.python.org/3/library/site.html#site.USER_SITE "site.USER_SITE")
).

### `posix_user`[¶](https://docs.python.org/3/library/sysconfig.html#posix-user "Link to this heading")

| Path | Installation directory |
| --- | --- |
| _stdlib_ | `_userbase_/lib/python_X.Y_` |
| _platstdlib_ | `_userbase_/lib/python_X.Y_` |
| _platlib_ | `_userbase_/lib/python_X.Y_/site-packages` |
| _purelib_ | `_userbase_/lib/python_X.Y_/site-packages` |
| _include_ | `_userbase_/include/python_X.Y_` |
| _scripts_ | `_userbase_/bin` |
| _data_ | `_userbase_` |

### `nt_user`[¶](https://docs.python.org/3/library/sysconfig.html#nt-user "Link to this heading")

| Path | Installation directory |
| --- | --- |
| _stdlib_ | `_userbase_\Python_XY_` |
| _platstdlib_ | `_userbase_\Python_XY_` |
| _platlib_ | `_userbase_\Python_XY_\site-packages` |
| _purelib_ | `_userbase_\Python_XY_\site-packages` |
| _include_ | `_userbase_\Python_XY_\Include` |
| _scripts_ | `_userbase_\Python_XY_\Scripts` |
| _data_ | `_userbase_` |

### `osx_framework_user`[¶](https://docs.python.org/3/library/sysconfig.html#osx-framework-user "Link to this heading")

| Path | Installation directory |
| --- | --- |
| _stdlib_ | `_userbase_/lib/python` |
| _platstdlib_ | `_userbase_/lib/python` |
| _platlib_ | `_userbase_/lib/python/site-packages` |
| _purelib_ | `_userbase_/lib/python/site-packages` |
| _include_ | `_userbase_/include/python_X.Y_` |
| _scripts_ | `_userbase_/bin` |
| _data_ | `_userbase_` |

Home scheme[¶](https://docs.python.org/3/library/sysconfig.html#home-scheme "Link to this heading")

----------------------------------------------------------------------------------------------------

The idea behind the “home scheme” is that you build and maintain a personal stash of Python modules. This scheme’s name is derived from the idea of a “home” directory on Unix, since it’s not unusual for a Unix user to make their home directory have a layout similar to `/usr/` or `/usr/local/`. This scheme can be used by anyone, regardless of the operating system they are installing for.

### `posix_home`[¶](https://docs.python.org/3/library/sysconfig.html#posix-home "Link to this heading")

| Path | Installation directory |
| --- | --- |
| _stdlib_ | `_home_/lib/python` |
| _platstdlib_ | `_home_/lib/python` |
| _platlib_ | `_home_/lib/python` |
| _purelib_ | `_home_/lib/python` |
| _include_ | `_home_/include/python` |
| _platinclude_ | `_home_/include/python` |
| _scripts_ | `_home_/bin` |
| _data_ | `_home_` |

Prefix scheme[¶](https://docs.python.org/3/library/sysconfig.html#prefix-scheme "Link to this heading")

--------------------------------------------------------------------------------------------------------

The “prefix scheme” is useful when you wish to use one Python installation to perform the build/install (i.e., to run the setup script), but install modules into the third-party module directory of a different Python installation (or something that looks like a different Python installation). If this sounds a trifle unusual, it is—that’s why the user and home schemes come before. However, there are at least two known cases where the prefix scheme will be useful.

First, consider that many Linux distributions put Python in `/usr`, rather than the more traditional `/usr/local`. This is entirely appropriate, since in those cases Python is part of “the system” rather than a local add-on. However, if you are installing Python modules from source, you probably want them to go in `/usr/local/lib/python2._X_` rather than `/usr/lib/python2._X_`.

Another possibility is a network filesystem where the name used to write to a remote directory is different from the name used to read it: for example, the Python interpreter accessed as `/usr/local/bin/python` might search for modules in `/usr/local/lib/python2._X_`, but those modules would have to be installed to, say, `/mnt/_@server_/export/lib/python2._X_`.

### `posix_prefix`[¶](https://docs.python.org/3/library/sysconfig.html#posix-prefix "Link to this heading")

| Path | Installation directory |
| --- | --- |
| _stdlib_ | `_prefix_/lib/python_X.Y_` |
| _platstdlib_ | `_prefix_/lib/python_X.Y_` |
| _platlib_ | `_prefix_/lib/python_X.Y_/site-packages` |
| _purelib_ | `_prefix_/lib/python_X.Y_/site-packages` |
| _include_ | `_prefix_/include/python_X.Y_` |
| _platinclude_ | `_prefix_/include/python_X.Y_` |
| _scripts_ | `_prefix_/bin` |
| _data_ | `_prefix_` |

### `nt`[¶](https://docs.python.org/3/library/sysconfig.html#nt "Link to this heading")

| Path | Installation directory |
| --- | --- |
| _stdlib_ | `_prefix_\Lib` |
| _platstdlib_ | `_prefix_\Lib` |
| _platlib_ | `_prefix_\Lib\site-packages` |
| _purelib_ | `_prefix_\Lib\site-packages` |
| _include_ | `_prefix_\Include` |
| _platinclude_ | `_prefix_\Include` |
| _scripts_ | `_prefix_\Scripts` |
| _data_ | `_prefix_` |

Installation path functions[¶](https://docs.python.org/3/library/sysconfig.html#installation-path-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

`sysconfig` provides some functions to determine these installation paths.

sysconfig.get\_scheme\_names()[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_scheme_names "Link to this definition")

Return a tuple containing all schemes currently supported in `sysconfig`.

sysconfig.get\_default\_scheme()[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_default_scheme "Link to this definition")

Return the default scheme name for the current platform.

Added in version 3.10: This function was previously named `_get_default_scheme()` and considered an implementation detail.

Changed in version 3.11: When Python runs from a virtual environment, the _venv_ scheme is returned.

sysconfig.get\_preferred\_scheme(_key_)[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_preferred_scheme "Link to this definition")

Return a preferred scheme name for an installation layout specified by _key_.

_key_ must be either `"prefix"`, `"home"`, or `"user"`.

The return value is a scheme name listed in [`get_scheme_names()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_scheme_names "sysconfig.get_scheme_names")
. It can be passed to `sysconfig` functions that take a _scheme_ argument, such as [`get_paths()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_paths "sysconfig.get_paths")
.

Added in version 3.10.

Changed in version 3.11: When Python runs from a virtual environment and `key="prefix"`, the _venv_ scheme is returned.

sysconfig.\_get\_preferred\_schemes()[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig._get_preferred_schemes "Link to this definition")

Return a dict containing preferred scheme names on the current platform. Python implementers and redistributors may add their preferred schemes to the `_INSTALL_SCHEMES` module-level global value, and modify this function to return those scheme names, to e.g. provide different schemes for system and language package managers to use, so packages installed by either do not mix with those by the other.

End users should not use this function, but [`get_default_scheme()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_default_scheme "sysconfig.get_default_scheme")
 and [`get_preferred_scheme()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_preferred_scheme "sysconfig.get_preferred_scheme")
 instead.

Added in version 3.10.

sysconfig.get\_path\_names()[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_path_names "Link to this definition")

Return a tuple containing all path names currently supported in `sysconfig`.

sysconfig.get\_path(_name_\[, _scheme_\[, _vars_\[, _expand_\]\]\])[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_path "Link to this definition")

Return an installation path corresponding to the path _name_, from the install scheme named _scheme_.

_name_ has to be a value from the list returned by [`get_path_names()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_path_names "sysconfig.get_path_names")
.

`sysconfig` stores installation paths corresponding to each path name, for each platform, with variables to be expanded. For instance the _stdlib_ path for the _nt_ scheme is: `{base}/Lib`.

`get_path()` will use the variables returned by [`get_config_vars()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_vars "sysconfig.get_config_vars")
 to expand the path. All variables have default values for each platform so one may call this function and get the default value.

If _scheme_ is provided, it must be a value from the list returned by [`get_scheme_names()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_scheme_names "sysconfig.get_scheme_names")
. Otherwise, the default scheme for the current platform is used.

If _vars_ is provided, it must be a dictionary of variables that will update the dictionary returned by [`get_config_vars()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_vars "sysconfig.get_config_vars")
.

If _expand_ is set to `False`, the path will not be expanded using the variables.

If _name_ is not found, raise a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
.

sysconfig.get\_paths(\[_scheme_\[, _vars_\[, _expand_\]\]\])[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_paths "Link to this definition")

Return a dictionary containing all installation paths corresponding to an installation scheme. See [`get_path()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_path "sysconfig.get_path")
 for more information.

If _scheme_ is not provided, will use the default scheme for the current platform.

If _vars_ is provided, it must be a dictionary of variables that will update the dictionary used to expand the paths.

If _expand_ is set to false, the paths will not be expanded.

If _scheme_ is not an existing scheme, `get_paths()` will raise a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
.

Other functions[¶](https://docs.python.org/3/library/sysconfig.html#other-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------

sysconfig.get\_python\_version()[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_python_version "Link to this definition")

Return the `MAJOR.MINOR` Python version number as a string. Similar to `'%d.%d' % sys.version_info[:2]`.

sysconfig.get\_platform()[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_platform "Link to this definition")

Return a string that identifies the current platform.

This is used mainly to distinguish platform-specific build directories and platform-specific built distributions. Typically includes the OS name and version and the architecture (as supplied by [`os.uname()`](https://docs.python.org/3/library/os.html#os.uname "os.uname")
), although the exact information included depends on the OS; e.g., on Linux, the kernel version isn’t particularly important.

Examples of returned values:

*   linux-x86\_64
    
*   linux-aarch64
    
*   solaris-2.6-sun4u
    

Windows:

*   win-amd64 (64-bit Windows on AMD64, aka x86\_64, Intel64, and EM64T)
    
*   win-arm64 (64-bit Windows on ARM64, aka AArch64)
    
*   win32 (all others - specifically, sys.platform is returned)
    

POSIX based OS:

*   linux-x86\_64
    
*   macosx-15.5-arm64
    
*   macosx-26.0-universal2 (macOS on Apple Silicon or Intel)
    
*   android-24-arm64\_v8a
    

For other non-POSIX platforms, currently just returns [`sys.platform`](https://docs.python.org/3/library/sys.html#sys.platform "sys.platform")
.

sysconfig.is\_python\_build()[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.is_python_build "Link to this definition")

Return `True` if the running Python interpreter was built from source and is being run from its built location, and not from a location resulting from e.g. running `make install` or installing via a binary installer.

sysconfig.parse\_config\_h(_fp_\[, _vars_\])[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.parse_config_h "Link to this definition")

Parse a `config.h`\-style file.

_fp_ is a file-like object pointing to the `config.h`\-like file.

A dictionary containing name/value pairs is returned. If an optional dictionary is passed in as the second argument, it is used instead of a new dictionary, and updated with the values read in the file.

sysconfig.get\_config\_h\_filename()[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_h_filename "Link to this definition")

Return the path of `pyconfig.h`.

sysconfig.get\_makefile\_filename()[¶](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_makefile_filename "Link to this definition")

Return the path of `Makefile`.

Command-line usage[¶](https://docs.python.org/3/library/sysconfig.html#command-line-usage "Link to this heading")

------------------------------------------------------------------------------------------------------------------

You can use `sysconfig` as a script with Python’s _\-m_ option:

Copy

$ python \-m sysconfig
Platform: "macosx-10.4-i386"
Python version: "3.2"
Current installation scheme: "posix\_prefix"

Paths:
        data = "/usr/local"
        include = "/Users/tarek/Dev/svn.python.org/py3k/Include"
        platinclude = "."
        platlib = "/usr/local/lib/python3.2/site-packages"
        platstdlib = "/usr/local/lib/python3.2"
        purelib = "/usr/local/lib/python3.2/site-packages"
        scripts = "/usr/local/bin"
        stdlib = "/usr/local/lib/python3.2"

Variables:
        AC\_APPLE\_UNIVERSAL\_BUILD = "0"
        AIX\_GENUINE\_CPLUSPLUS = "0"
        AR = "ar"
        ARFLAGS = "rc"
        ...

This call will print in the standard output the information returned by [`get_platform()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_platform "sysconfig.get_platform")
, [`get_python_version()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_python_version "sysconfig.get_python_version")
, [`get_path()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_path "sysconfig.get_path")
 and [`get_config_vars()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_vars "sysconfig.get_config_vars")
.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`sysconfig` — Provide access to Python’s configuration information](https://docs.python.org/3/library/sysconfig.html#)
    *   [Configuration variables](https://docs.python.org/3/library/sysconfig.html#configuration-variables)
        
    *   [Installation paths](https://docs.python.org/3/library/sysconfig.html#installation-paths)
        
    *   [User scheme](https://docs.python.org/3/library/sysconfig.html#user-scheme)
        *   [`posix_user`](https://docs.python.org/3/library/sysconfig.html#posix-user)
            
        *   [`nt_user`](https://docs.python.org/3/library/sysconfig.html#nt-user)
            
        *   [`osx_framework_user`](https://docs.python.org/3/library/sysconfig.html#osx-framework-user)
            
    *   [Home scheme](https://docs.python.org/3/library/sysconfig.html#home-scheme)
        *   [`posix_home`](https://docs.python.org/3/library/sysconfig.html#posix-home)
            
    *   [Prefix scheme](https://docs.python.org/3/library/sysconfig.html#prefix-scheme)
        *   [`posix_prefix`](https://docs.python.org/3/library/sysconfig.html#posix-prefix)
            
        *   [`nt`](https://docs.python.org/3/library/sysconfig.html#nt)
            
    *   [Installation path functions](https://docs.python.org/3/library/sysconfig.html#installation-path-functions)
        
    *   [Other functions](https://docs.python.org/3/library/sysconfig.html#other-functions)
        
    *   [Command-line usage](https://docs.python.org/3/library/sysconfig.html#command-line-usage)
        

#### Previous topic

[`sys.monitoring` — Execution event monitoring](https://docs.python.org/3/library/sys.monitoring.html "previous chapter")

#### Next topic

[`builtins` — Built-in objects](https://docs.python.org/3/library/builtins.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=sysconfig+%E2%80%94+Provide+access+to+Python%E2%80%99s+configuration+information&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsysconfig.html&pagesource=library%2Fsysconfig.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/sysconfig.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/builtins.html "builtins — Built-in objects")
     |
*   [previous](https://docs.python.org/3/library/sys.monitoring.html "sys.monitoring — Execution event monitoring")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)
     »
*   [`sysconfig` — Provide access to Python’s configuration information](https://docs.python.org/3/library/sysconfig.html)
    
*    
    
    |
*   Theme Auto Light Dark |