### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/unix.html "2. Using Python on Unix platforms")
     |
*   [previous](https://docs.python.org/3/using/index.html "Python Setup and Usage")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python Setup and Usage](https://docs.python.org/3/using/index.html)
     »
*   [1\. Command line and environment](https://docs.python.org/3/using/cmdline.html)
    
*    
    
    |
*   Theme Auto Light Dark |

1\. Command line and environment[¶](https://docs.python.org/3/using/cmdline.html#command-line-and-environment "Link to this heading")

======================================================================================================================================

The CPython interpreter scans the command line and the environment for various settings.

**CPython implementation detail:** Other implementations’ command line schemes may differ. See [Alternate Implementations](https://docs.python.org/3/reference/introduction.html#implementations)
 for further resources.

1.1. Command line[¶](https://docs.python.org/3/using/cmdline.html#command-line "Link to this heading")

-------------------------------------------------------------------------------------------------------

When invoking Python, you may specify any of these options:

Copy

python \[\-bBdEhiIOPqRsSuvVWx?\] \[\-c command | \-m module-name | script | \- \] \[args\]

The most common use case is, of course, a simple invocation of a script:

Copy

python myscript.py

### 1.1.1. Interface options[¶](https://docs.python.org/3/using/cmdline.html#interface-options "Link to this heading")

The interpreter interface resembles that of the UNIX shell, but provides some additional methods of invocation:

*   When called with standard input connected to a tty device, it prompts for commands and executes them until an EOF (an end-of-file character, you can produce that with Ctrl\-D on UNIX or Ctrl\-Z, Enter on Windows) is read. For more on interactive mode, see [Interactive Mode](https://docs.python.org/3/tutorial/appendix.html#tut-interac)
    .
    
*   When called with a file name argument or with a file as standard input, it reads and executes a script from that file.
    
*   When called with a directory name argument, it reads and executes an appropriately named script from that directory.
    
*   When called with `-c command`, it executes the Python statement(s) given as _command_. Here _command_ may contain multiple statements separated by newlines.
    
*   When called with `-m module-name`, the given module is located using the standard import mechanism and executed as a script.
    

In non-interactive mode, the entire input is parsed before it is executed.

An interface option terminates the list of options consumed by the interpreter, all consecutive arguments will end up in [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
 – note that the first element, subscript zero (`sys.argv[0]`), is a string reflecting the program’s source.

\-c <command>[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-c "Link to this definition")

Execute the Python code in _command_. _command_ can be one or more statements separated by newlines, with significant leading whitespace as in normal module code.

If this option is given, the first element of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
 will be `"-c"` and the current directory will be added to the start of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 (allowing modules in that directory to be imported as top level modules).

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `cpython.run_command` with argument `command`.

Changed in version 3.14: _command_ is automatically dedented before execution.

\-m <module-name>[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-m "Link to this definition")

Locate the module using the standard import mechanism and execute its contents as the [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.")
 module.

Since the argument is a _module_ name, you must not give a file extension (`.py`). The module name should be a valid absolute Python module name, but the implementation may not always enforce this (e.g. it may allow you to use a name that includes a hyphen).

Package names (including namespace packages) are also permitted. When a package name is supplied instead of a normal module, the interpreter will execute `<pkg>.__main__` as the main module. This behaviour is deliberately similar to the handling of directories and zipfiles that are passed to the interpreter as the script argument.

Note

This option cannot be used with built-in modules and extension modules written in C, since they do not have Python module files. However, it can still be used for precompiled modules, even if the original source file is not available.

If this option is given, the first element of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
 will be the full path to the module file (while the module file is being located, the first element will be set to `"-m"`). As with the [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c)
 option, the current directory will be added to the start of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
.

[`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I)
 option can be used to run the script in isolated mode where [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 contains neither the current directory nor the user’s site-packages directory. All `PYTHON*` environment variables are ignored, too.

Many standard library modules contain code that is invoked on their execution as a script. An example is the [`timeit`](https://docs.python.org/3/library/timeit.html#module-timeit "timeit: Measure the execution time of small code snippets.")
 module:

Copy

python \-m timeit \-s "setup here" "benchmarked code here"
python \-m timeit \-h \# for details

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `cpython.run_module` with argument `module-name`.

See also

[`runpy.run_module()`](https://docs.python.org/3/library/runpy.html#runpy.run_module "runpy.run_module")

Equivalent functionality directly available to Python code

[**PEP 338**](https://peps.python.org/pep-0338/)
 – Executing modules as scripts

Changed in version 3.1: Supply the package name to run a `__main__` submodule.

Changed in version 3.4: namespace packages are also supported

\-

Read commands from standard input ([`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
). If standard input is a terminal, [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i)
 is implied.

If this option is given, the first element of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
 will be `"-"` and the current directory will be added to the start of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `cpython.run_stdin` with no arguments.

<script>

Execute the Python code contained in _script_, which must be a filesystem path (absolute or relative) referring to either a Python file, a directory containing a `__main__.py` file, or a zipfile containing a `__main__.py` file.

If this option is given, the first element of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")
 will be the script name as given on the command line.

If the script name refers directly to a Python file, the directory containing that file is added to the start of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
, and the file is executed as the [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.")
 module.

If the script name refers to a directory or zipfile, the script name is added to the start of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 and the `__main__.py` file in that location is executed as the [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.")
 module.

[`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I)
 option can be used to run the script in isolated mode where [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 contains neither the script’s directory nor the user’s site-packages directory. All `PYTHON*` environment variables are ignored, too.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `cpython.run_file` with argument `filename`.

See also

[`runpy.run_path()`](https://docs.python.org/3/library/runpy.html#runpy.run_path "runpy.run_path")

Equivalent functionality directly available to Python code

If no interface option is given, [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i)
 is implied, `sys.argv[0]` is an empty string (`""`) and the current directory will be added to the start of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
. Also, tab-completion and history editing is automatically enabled, if available on your platform (see [Readline configuration](https://docs.python.org/3/library/site.html#rlcompleter-config)
).

See also

[Invoking the Interpreter](https://docs.python.org/3/tutorial/interpreter.html#tut-invoking)

Changed in version 3.4: Automatic enabling of tab-completion and history editing.

### 1.1.2. Generic options[¶](https://docs.python.org/3/using/cmdline.html#generic-options "Link to this heading")

\-?[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-0 "Link to this definition")

\-h[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-h "Link to this definition")

\--help[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-help "Link to this definition")

Print a short description of all command line options and corresponding environment variables and exit.

\--help-env[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-help-env "Link to this definition")

Print a short description of Python-specific environment variables and exit.

Added in version 3.11.

\--help-xoptions[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-help-xoptions "Link to this definition")

Print a description of implementation-specific [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 options and exit.

Added in version 3.11.

\--help-all[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-help-all "Link to this definition")

Print complete usage information and exit.

Added in version 3.11.

\-V[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-V "Link to this definition")

\--version[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-version "Link to this definition")

Print the Python version number and exit. Example output could be:

Python 3.8.0b2+

When given twice, print more information about the build, like:

Python 3.8.0b2+ (3.8:0c076caaa8, Apr 20 2019, 21:55:00)
\[GCC 6.2.0 20161005\]

Added in version 3.6: The `-VV` option.

### 1.1.3. Miscellaneous options[¶](https://docs.python.org/3/using/cmdline.html#miscellaneous-options "Link to this heading")

\-b[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-b "Link to this definition")

Issue a warning when converting [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 or [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 to [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 without specifying encoding or comparing `bytes` or `bytearray` with `str` or `bytes` with [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
. Issue an error when the option is given twice (`-bb`).

Changed in version 3.5: Affects also comparisons of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 with [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
.

Deprecated since version 3.15: Deprecate [`-b`](https://docs.python.org/3/using/cmdline.html#cmdoption-b)
 and `-bb` command line options and schedule them to become no-op in Python 3.17. These were primarily helpers for the Python 2 -> 3 transition. Starting with Python 3.17, no [`BytesWarning`](https://docs.python.org/3/builtins/exceptions.html#BytesWarning "BytesWarning")
 will be raised for these cases; use a type checker instead.

\-B[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-B "Link to this definition")

If given, Python won’t try to write `.pyc` files on the import of source modules. See also [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE)
.

\--check-hash-based-pycs default|always|never[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-check-hash-based-pycs "Link to this definition")

Control the validation behavior of hash-based `.pyc` files. See [Cached bytecode invalidation](https://docs.python.org/3/reference/import.html#pyc-invalidation)
. When set to `default`, checked and unchecked hash-based bytecode cache files are validated according to their default semantics. When set to `always`, all hash-based `.pyc` files, whether checked or unchecked, are validated against their corresponding source file. When set to `never`, hash-based `.pyc` files are not validated against their corresponding source files.

The semantics of timestamp-based `.pyc` files are unaffected by this option.

\-d[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-d "Link to this definition")

Turn on parser debugging output (for expert only). See also the [`PYTHONDEBUG`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDEBUG)
 environment variable.

This option requires a [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build)
, otherwise it’s ignored.

\-E[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-E "Link to this definition")

Ignore all `PYTHON*` environment variables, e.g. [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
 and [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
, that might be set.

See also the [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P)
 and [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I)
 (isolated) options.

\-i[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-i "Link to this definition")

Enter interactive mode after execution.

Using the [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i)
 option will enter interactive mode in any of the following circumstances:

*   When a script is passed as first argument
    
*   When the [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c)
     option is used
    
*   When the [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)
     option is used
    

Interactive mode will start even when [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
 does not appear to be a terminal. The [`PYTHONSTARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP)
 file is not read.

This can be useful to inspect global variables or a stack trace when a script raises an exception. See also [`PYTHONINSPECT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINSPECT)
.

\-I[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-I "Link to this definition")

Run Python in isolated mode. This also implies [`-E`](https://docs.python.org/3/using/cmdline.html#cmdoption-E)
, [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P)
 and [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s)
 options.

In isolated mode [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 contains neither the script’s directory nor the user’s site-packages directory. All `PYTHON*` environment variables are ignored, too. Further restrictions may be imposed to prevent the user from injecting malicious code.

Added in version 3.4.

\-O[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-O "Link to this definition")

Remove assert statements and any code conditional on the value of [`__debug__`](https://docs.python.org/3/builtins/constants.html#debug__ "__debug__")
. Augment the filename for compiled ([bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
) files by adding `.opt-1` before the `.pyc` extension (see [**PEP 488**](https://peps.python.org/pep-0488/)
). See also [`PYTHONOPTIMIZE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONOPTIMIZE)
.

Changed in version 3.5: Modify `.pyc` filenames according to [**PEP 488**](https://peps.python.org/pep-0488/)
.

\-OO[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-OO "Link to this definition")

Do [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O)
 and also discard docstrings. Augment the filename for compiled ([bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
) files by adding `.opt-2` before the `.pyc` extension (see [**PEP 488**](https://peps.python.org/pep-0488/)
).

Changed in version 3.5: Modify `.pyc` filenames according to [**PEP 488**](https://peps.python.org/pep-0488/)
.

\-P[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-P "Link to this definition")

Don’t prepend a potentially unsafe path to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
:

*   `python -m module` command line: Don’t prepend the current working directory.
    
*   `python script.py` command line: Don’t prepend the script’s directory. If it’s a symbolic link, resolve symbolic links.
    
*   `python -c code` and `python` (REPL) command lines: Don’t prepend an empty string, which means the current working directory.
    

See also the [`PYTHONSAFEPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSAFEPATH)
 environment variable, and [`-E`](https://docs.python.org/3/using/cmdline.html#cmdoption-E)
 and [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I)
 (isolated) options.

Added in version 3.11.

\-q[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-q "Link to this definition")

Don’t display the copyright and version messages even in interactive mode.

Added in version 3.2.

\-R[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-R "Link to this definition")

Turn on hash randomization. This option only has an effect if the [`PYTHONHASHSEED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED)
 environment variable is set to anything other than `random`, since hash randomization is enabled by default.

On previous versions of Python, this option turns on hash randomization, so that the [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
 values of str and bytes objects are “salted” with an unpredictable random value. Although they remain constant within an individual Python process, they are not predictable between repeated invocations of Python.

Hash randomization is intended to provide protection against a denial-of-service caused by carefully chosen inputs that exploit the worst case performance of a dict construction, _O_(_n_2) complexity. See [https://ocert.org/advisories/ocert-2011-003.html](https://ocert.org/advisories/ocert-2011-003.html)
 for details.

[`PYTHONHASHSEED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED)
 allows you to set a fixed value for the hash seed secret.

Added in version 3.2.3.

Changed in version 3.7: The option is no longer ignored.

\-s[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-s "Link to this definition")

Don’t add the [`user site-packages directory`](https://docs.python.org/3/library/site.html#site.USER_SITE "site.USER_SITE")
 to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
.

See also [`PYTHONNOUSERSITE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNOUSERSITE)
.

See also

[**PEP 370**](https://peps.python.org/pep-0370/)
 – Per user site-packages directory

\-S[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-S "Link to this definition")

Disable the import of the module [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 and the site-dependent manipulations of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 that it entails. Also disable these manipulations if `site` is explicitly imported later (call [`site.main()`](https://docs.python.org/3/library/site.html#site.main "site.main")
 if you want them to be triggered).

\-u[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-u "Link to this definition")

Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream.

See also [`PYTHONUNBUFFERED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED)
.

Changed in version 3.7: The text layer of the stdout and stderr streams now is unbuffered.

\-v[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-v "Link to this definition")

Print a message each time a module is initialized, showing the place (filename or built-in module) from which it is loaded. When given twice (`-vv`), print a message for each file that is checked for when searching for a module. Also provides information on module cleanup at exit.

Changed in version 3.10: The [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module reports the site-specific paths and `.pth` files being processed.

See also [`PYTHONVERBOSE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONVERBOSE)
.

\-W arg[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-W "Link to this definition")

Warning control. Python’s warning machinery by default prints warning messages to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
.

The simplest settings apply a particular action unconditionally to all warnings emitted by a process (even those that are otherwise ignored by default):

Copy

\-Wdefault  \# Warn once per call location
-Werror    \# Convert to exceptions
-Walways   \# Warn every time
-Wall      \# Same as -Walways
-Wmodule   \# Warn once per calling module
-Wonce     \# Warn once per Python process
-Wignore   \# Never warn

The action names can be abbreviated as desired and the interpreter will resolve them to the appropriate action name. For example, `-Wi` is the same as `-Wignore`.

The full form of argument is:

Copy

action:message:category:module:lineno

Empty fields match all values; trailing empty fields may be omitted. For example `-W ignore::DeprecationWarning` ignores all DeprecationWarning warnings.

The _action_ field is as explained above but only applies to warnings that match the remaining fields.

The _message_ field must match the start of the warning message; this match is case-insensitive. If it starts and ends with a forward slash (`/`), it specifies a regular expression, otherwise it specifies a literal string.

The _category_ field matches the warning category (ex: `DeprecationWarning`). This must be a class name; the match test whether the actual warning category of the message is a subclass of the specified warning category.

The _module_ field matches the (fully qualified) module name; this match is case-sensitive. If it starts and ends with a forward slash (`/`), it specifies a regular expression that the start of the fully qualified module name must match, otherwise it specifies a literal string that the fully qualified module name must be equal to.

The _lineno_ field matches the line number, where zero matches all line numbers and is thus equivalent to an omitted line number.

Multiple [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W)
 options can be given; when a warning matches more than one option, the action for the last matching option is performed. Invalid `-W` options are ignored (though, a warning message is printed about invalid options when the first warning is issued).

Warnings can also be controlled using the [`PYTHONWARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS)
 environment variable and from within a Python program using the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
 module. For example, the [`warnings.filterwarnings()`](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings")
 function can be used to use a regular expression on the warning message.

See [The Warnings Filter](https://docs.python.org/3/library/warnings.html#warning-filter)
 and [Describing Warning Filters](https://docs.python.org/3/library/warnings.html#describing-warning-filters)
 for more details.

Changed in version 3.15: Added regular expression support for _message_ and _module_.

\-x[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-x "Link to this definition")

Skip the first line of the source, allowing use of non-Unix forms of `#!cmd`.

This can be used to turn a Python script into a Windows batch file. Similarly to adding a shebang line and setting the executable bit on Unix, the extension of the Python script can be changed to `.bat` and the following line can be added at the start of the script:

@py -x "%~f0" %\* & exit /b

Or, to specify the path to the Python interpreter explicitly:

@"C:\\Path\\to\\python.exe" -x "%~f0" %\* & exit /b

Unlike a shebang line which is a Python comment, this line is not valid Python syntax, and the [`-x`](https://docs.python.org/3/using/cmdline.html#cmdoption-x)
 option is needed to skip it.

\-X[¶](https://docs.python.org/3/using/cmdline.html#cmdoption-X "Link to this definition")

Reserved for various implementation-specific options. CPython currently defines the following possible values:

*   `-X faulthandler` to enable [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.")
    . See also [`PYTHONFAULTHANDLER`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER)
    .
    
    Added in version 3.3.
    
*   `-X showrefcount` to output the total reference count and number of used memory blocks when the program finishes or after each statement in the interactive interpreter. This only works on [debug builds](https://docs.python.org/3/using/configure.html#debug-build)
    .
    
    Added in version 3.4.
    
*   `-X tracemalloc` to start tracing Python memory allocations using the [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")
     module. By default, only the most recent frame is stored in a traceback of a trace. Use `-X tracemalloc=NFRAME` to start tracing with a traceback limit of _NFRAME_ frames. See [`tracemalloc.start()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "tracemalloc.start")
     and [`PYTHONTRACEMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONTRACEMALLOC)
     for more information.
    
    Added in version 3.4.
    
*   `-X int_max_str_digits` configures the [integer string conversion length limitation](https://docs.python.org/3/builtins/stdtypes.html#int-max-str-digits)
    . See also [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS)
    .
    
    Added in version 3.11.
    
*   `-X importtime` to show how long each import takes. It shows module name, cumulative time (including nested imports) and self time (excluding nested imports). Note that its output may be broken in multi-threaded application. Typical usage is `python -X importtime -c 'import asyncio'`.
    
    `-X importtime=2` enables additional output that indicates when an imported module has already been loaded. In such cases, the string `cached` will be printed in both time columns.
    
    See also [`PYTHONPROFILEIMPORTTIME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPROFILEIMPORTTIME)
    .
    
    Added in version 3.7.
    
    Changed in version 3.14: Added `-X importtime=2` to also trace imports of loaded modules, and reserved values other than `1` and `2` for future use.
    
*   `-X dev`: enable [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
    , introducing additional runtime checks that are too expensive to be enabled by default. See also [`PYTHONDEVMODE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDEVMODE)
    .
    
    Added in version 3.7.
    
*   `-X utf8` enables the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
    . `-X utf8=0` explicitly disables [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
     (even when it would otherwise activate automatically). See also [`PYTHONUTF8`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8)
    .
    
    Added in version 3.7.
    
*   `-X pycache_prefix=PATH` enables writing `.pyc` files to a parallel tree rooted at the given directory instead of to the code tree. See also [`PYTHONPYCACHEPREFIX`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX)
    .
    
    Added in version 3.8.
    
*   `-X warn_default_encoding` issues a [`EncodingWarning`](https://docs.python.org/3/builtins/exceptions.html#EncodingWarning "EncodingWarning")
     when the locale-specific default encoding is used for opening files. See also [`PYTHONWARNDEFAULTENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING)
    .
    
    Added in version 3.10.
    
*   `-X no_debug_ranges` disables the inclusion of the tables mapping extra location information (end line, start column offset and end column offset) to every instruction in code objects. This is useful when smaller code objects and pyc files are desired as well as suppressing the extra visual location indicators when the interpreter displays tracebacks. See also [`PYTHONNODEBUGRANGES`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNODEBUGRANGES)
    .
    
    Added in version 3.11.
    
*   `-X frozen_modules` determines whether or not frozen modules are ignored by the import machinery. A value of `on` means they get imported and `off` means they are ignored. The default is `on` if this is an installed Python (the normal case). If it’s under development (running from the source tree) then the default is `off`. Note that the `importlib_bootstrap` and `importlib_bootstrap_external` frozen modules are always used, even if this flag is set to `off`. See also [`PYTHON_FROZEN_MODULES`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_FROZEN_MODULES)
    .
    
    Added in version 3.11.
    
*   `-X perf` enables support for the Linux `perf` profiler. When this option is provided, the `perf` profiler will be able to report Python calls. This option is only available on some platforms and will do nothing if is not supported on the current system. The default value is “off”. See also [`PYTHONPERFSUPPORT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPERFSUPPORT)
     and [Python support for the perf map compatible profilers](https://docs.python.org/3/howto/perf_profiling.html#perf-profiling)
    .
    
    Added in version 3.12.
    
*   `-X perf_jit` enables support for the Linux `perf` profiler with DWARF support. When this option is provided, the `perf` profiler will be able to report Python calls using DWARF information. This option is only available on some platforms and will do nothing if is not supported on the current system. The default value is “off”. See also [`PYTHON_PERF_JIT_SUPPORT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PERF_JIT_SUPPORT)
     and [Python support for the perf map compatible profilers](https://docs.python.org/3/howto/perf_profiling.html#perf-profiling)
    .
    
    Added in version 3.13.
    
*   `-X disable-remote-debug` disables the remote debugging support as described in [**PEP 768**](https://peps.python.org/pep-0768/)
    . This includes both the functionality to schedule code for execution in another process and the functionality to receive code for execution in the current process.
    
    This option is only available on some platforms and will do nothing if is not supported on the current system. See also [`PYTHON_DISABLE_REMOTE_DEBUG`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_DISABLE_REMOTE_DEBUG)
     and [**PEP 768**](https://peps.python.org/pep-0768/)
    .
    
    Added in version 3.14.
    
*   `-X cpu_count=_n_` overrides [`os.cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count")
    , [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
    , and [`multiprocessing.cpu_count()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.cpu_count "multiprocessing.cpu_count")
    . _n_ must be greater than or equal to 1. This option may be useful for users who need to limit CPU resources of a container system. See also [`PYTHON_CPU_COUNT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT)
    . If _n_ is `default`, nothing is overridden.
    
    Added in version 3.13.
    
*   `-X presite=_module_` or `-X presite=_module:func_` specifies an entry point that should be executed before the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
     module is executed and before the [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.")
     module exists. Therefore, the imported module isn’t `__main__`. This can be used to execute code early during Python initialization. Python needs to be [built in debug mode](https://docs.python.org/3/using/configure.html#debug-build)
     for this option to exist. See also [`PYTHON_PRESITE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PRESITE)
    .
    
    Changed in version 3.15: Accept also `module:func` entry point format.
    
    Added in version 3.13.
    
*   `-X gil=_0,1_` forces the GIL to be disabled or enabled, respectively. Setting to `0` is only available in builds configured with [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
    . See also [`PYTHON_GIL`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_GIL)
     and [Free-threaded CPython](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-free-threaded-cpython)
    .
    
    Added in version 3.13.
    
*   `-X thread_inherit_context=_0,1_` causes [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread")
     to, by default, use a copy of context of the caller of `Thread.start()` when starting. Otherwise, threads will start with an empty context. If unset, the value of this option defaults to `1` on free-threaded builds and to `0` otherwise. See also [`PYTHON_THREAD_INHERIT_CONTEXT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_THREAD_INHERIT_CONTEXT)
    .
    
    Added in version 3.14.
    
*   `-X context_aware_warnings=_0,1_` causes the [`warnings.catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
     context manager to use a [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar")
     to store warnings filter state. If unset, the value of this option defaults to `1` on free-threaded builds and to `0` otherwise. See also [`PYTHON_CONTEXT_AWARE_WARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CONTEXT_AWARE_WARNINGS)
    .
    
    Added in version 3.14.
    
*   `-X pathconfig_warnings=_0,1_` if true (`1`) then [The initialization of the sys.path module search path](https://docs.python.org/3/library/sys_path_init.html#sys-path-init)
     is allowed to log warnings into stderr. If false (`0`) suppress these warnings. Set to true by default. See also [`PYTHON_PATHCONFIG_WARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PATHCONFIG_WARNINGS)
    .
    
    Added in version 3.15.
    
*   `-X tlbc=_0,1_` enables (1, the default) or disables (0) thread-local bytecode in builds configured with [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
    . When disabled, this also disables the specializing interpreter. See also [`PYTHON_TLBC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_TLBC)
    .
    
    Added in version 3.14.
    
*   `-X lazy_imports=_all,normal_` controls lazy import behavior. `all` makes all imports lazy by default, and `normal` (the default) respects the `lazy` keyword in source code. See also [`PYTHON_LAZY_IMPORTS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_LAZY_IMPORTS)
    .
    
    Added in version 3.15.
    

It also allows passing arbitrary values and retrieving them through the [`sys._xoptions`](https://docs.python.org/3/library/sys.html#sys._xoptions "sys._xoptions")
 dictionary.

Added in version 3.2.

Changed in version 3.9: Removed the `-X showalloccount` option.

Changed in version 3.10: Removed the `-X oldparser` option.

Removed in version 3.14: `-J` is no longer reserved for use by [Jython](https://www.jython.org/)
, and now has no special meaning.

### 1.1.4. Controlling color[¶](https://docs.python.org/3/using/cmdline.html#controlling-color "Link to this heading")

The Python interpreter is configured by default to use colors to highlight output in certain situations such as when displaying tracebacks. This behavior can be controlled by setting different environment variables.

Setting the environment variable `TERM` to `dumb` will disable color.

If the [`FORCE_COLOR`](https://force-color.org/)
 environment variable is set, then color will be enabled regardless of the value of TERM. This is useful on CI systems which aren’t terminals but can still display ANSI escape sequences.

If the [`NO_COLOR`](https://no-color.org/)
 environment variable is set, Python will disable all color in the output. This takes precedence over `FORCE_COLOR`.

All these environment variables are used also by other tools to control color output. To control the color output only in the Python interpreter, the [`PYTHON_COLORS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_COLORS)
 environment variable can be used. This variable takes precedence over `NO_COLOR`, which in turn takes precedence over `FORCE_COLOR`.

1.2. Environment variables[¶](https://docs.python.org/3/using/cmdline.html#environment-variables "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

These environment variables influence Python’s behavior, they are processed before the command-line switches other than -E or -I. It is customary that command-line switches override environmental variables where there is a conflict.

PYTHONHOME[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME "Link to this definition")

Change the location of the standard Python libraries. By default, the libraries are searched in `_prefix_/lib/python_version_` and `_exec_prefix_/lib/python_version_`, where `_prefix_` and `_exec_prefix_` are installation-dependent directories, both defaulting to `/usr/local`.

When [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
 is set to a single directory, its value replaces both `_prefix_` and `_exec_prefix_`. To specify different values for these, set `PYTHONHOME` to `_prefix_:_exec_prefix_`.

PYTHONPATH[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH "Link to this definition")

Augment the default search path for module files. The format is the same as the shell’s `PATH`: one or more directory pathnames separated by [`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep")
 (e.g. colons on Unix or semicolons on Windows). Non-existent directories are silently ignored.

In addition to normal directories, individual [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
 entries may refer to zipfiles containing pure Python modules (in either source or compiled form). Extension modules cannot be imported from zipfiles.

The default search path is installation dependent, but generally begins with `_prefix_/lib/python_version_` (see [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
 above). It is _always_ appended to [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
.

An additional directory will be inserted in the search path in front of [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
 as described above under [Interface options](https://docs.python.org/3/using/cmdline.html#using-on-interface-options)
. The search path can be manipulated from within a Python program as the variable [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
.

PYTHONSAFEPATH[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSAFEPATH "Link to this definition")

If this is set to a non-empty string, don’t prepend a potentially unsafe path to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
: see the [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P)
 option for details.

Added in version 3.11.

PYTHONPLATLIBDIR[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPLATLIBDIR "Link to this definition")

If this is set to a non-empty string, it overrides the [`sys.platlibdir`](https://docs.python.org/3/library/sys.html#sys.platlibdir "sys.platlibdir")
 value.

Added in version 3.9.

PYTHONSTARTUP[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP "Link to this definition")

If this is the name of a readable file, the Python commands in that file are executed before the first prompt is displayed in interactive mode. The file is executed in the same namespace where interactive commands are executed so that objects defined or imported in it can be used without qualification in the interactive session. You can also change the prompts [`sys.ps1`](https://docs.python.org/3/library/sys.html#sys.ps1 "sys.ps1")
 and [`sys.ps2`](https://docs.python.org/3/library/sys.html#sys.ps2 "sys.ps2")
 and the hook [`sys.__interactivehook__`](https://docs.python.org/3/library/sys.html#sys.__interactivehook__ "sys.__interactivehook__")
 in this file.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `cpython.run_startup` with the filename as the argument when called on startup.

PYTHONOPTIMIZE[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONOPTIMIZE "Link to this definition")

If this is set to a non-empty string it is equivalent to specifying the [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O)
 option. If set to an integer, it is equivalent to specifying `-O` multiple times.

PYTHONBREAKPOINT[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONBREAKPOINT "Link to this definition")

If this is set, it names a callable using dotted-path notation. The module containing the callable will be imported and then the callable will be run by the default implementation of [`sys.breakpointhook()`](https://docs.python.org/3/library/sys.html#sys.breakpointhook "sys.breakpointhook")
 which itself is called by built-in [`breakpoint()`](https://docs.python.org/3/builtins/functions.html#breakpoint "breakpoint")
. If not set, or set to the empty string, it is equivalent to the value “pdb.set\_trace”. Setting this to the string “0” causes the default implementation of `sys.breakpointhook()` to do nothing but return immediately.

Added in version 3.7.

PYTHONDEBUG[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDEBUG "Link to this definition")

If this is set to a non-empty string it is equivalent to specifying the [`-d`](https://docs.python.org/3/using/cmdline.html#cmdoption-d)
 option. If set to an integer, it is equivalent to specifying `-d` multiple times.

This environment variable requires a [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build)
, otherwise it’s ignored.

PYTHONINSPECT[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINSPECT "Link to this definition")

If this is set to a non-empty string it is equivalent to specifying the [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i)
 option.

This variable can also be modified by Python code using [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
 to force inspect mode on program termination.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `cpython.run_stdin` with no arguments.

Changed in version 3.12.5: (also 3.11.10, 3.10.15, 3.9.20, and 3.8.20) Emits audit events.

Changed in version 3.13: Uses PyREPL if possible, in which case [`PYTHONSTARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP)
 is also executed. Emits audit events.

PYTHONUNBUFFERED[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED "Link to this definition")

If this is set to a non-empty string it is equivalent to specifying the [`-u`](https://docs.python.org/3/using/cmdline.html#cmdoption-u)
 option.

PYTHONVERBOSE[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONVERBOSE "Link to this definition")

If this is set to a non-empty string it is equivalent to specifying the [`-v`](https://docs.python.org/3/using/cmdline.html#cmdoption-v)
 option. If set to an integer, it is equivalent to specifying `-v` multiple times.

PYTHONCASEOK[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONCASEOK "Link to this definition")

If this is set, Python ignores case in [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
 statements. This only works on Windows and macOS.

PYTHONDONTWRITEBYTECODE[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE "Link to this definition")

If this is set to a non-empty string, Python won’t try to write `.pyc` files on the import of source modules. This is equivalent to specifying the [`-B`](https://docs.python.org/3/using/cmdline.html#cmdoption-B)
 option.

PYTHONPYCACHEPREFIX[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX "Link to this definition")

If this is set, Python will write `.pyc` files in a mirror directory tree at this path, instead of in `__pycache__` directories within the source tree. This is equivalent to specifying the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `pycache_prefix=PATH` option.

Added in version 3.8.

PYTHONHASHSEED[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED "Link to this definition")

If this variable is not set or set to `random`, a random value is used to seed the hashes of str and bytes objects.

If [`PYTHONHASHSEED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED)
 is set to an integer value, it is used as a fixed seed for generating the hash() of the types covered by the hash randomization.

Its purpose is to allow repeatable hashing, such as for selftests for the interpreter itself, or to allow a cluster of python processes to share hash values.

The integer must be a decimal number in the range \[0,4294967295\]. Specifying the value 0 will disable hash randomization.

Added in version 3.2.3.

PYTHONINTMAXSTRDIGITS[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS "Link to this definition")

If this variable is set to an integer, it is used to configure the interpreter’s global [integer string conversion length limitation](https://docs.python.org/3/builtins/stdtypes.html#int-max-str-digits)
.

Added in version 3.11.

PYTHONIOENCODING[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONIOENCODING "Link to this definition")

If this is set before running the interpreter, it overrides the encoding used for stdin/stdout/stderr, in the syntax `encodingname:errorhandler`. Both the `encodingname` and the `:errorhandler` parts are optional and have the same meaning as in [`str.encode()`](https://docs.python.org/3/builtins/stdtypes.html#str.encode "str.encode")
.

For stderr, the `:errorhandler` part is ignored; the handler will always be `'backslashreplace'`.

Changed in version 3.4: The `encodingname` part is now optional.

Changed in version 3.6: On Windows, the encoding specified by this variable is ignored for interactive console buffers unless [`PYTHONLEGACYWINDOWSSTDIO`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO)
 is also specified. Files and pipes redirected through the standard streams are not affected.

PYTHONNOUSERSITE[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNOUSERSITE "Link to this definition")

This is equivalent to the [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s)
 option. If this is set, Python won’t add the [`user site-packages directory`](https://docs.python.org/3/library/site.html#site.USER_SITE "site.USER_SITE")
 to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
.

See also

[**PEP 370**](https://peps.python.org/pep-0370/)
 – Per user site-packages directory

PYTHONUSERBASE[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUSERBASE "Link to this definition")

Defines the [`user base directory`](https://docs.python.org/3/library/site.html#site.USER_BASE "site.USER_BASE")
, which is used to compute the path of the [`user site-packages directory`](https://docs.python.org/3/library/site.html#site.USER_SITE "site.USER_SITE")
 and [installation paths](https://docs.python.org/3/library/sysconfig.html#sysconfig-user-scheme)
 for `python -m pip install --user`.

To disable the user site-packages, see [`PYTHONNOUSERSITE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNOUSERSITE)
 or the [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s)
 option.

See also

[**PEP 370**](https://peps.python.org/pep-0370/)
 – Per user site-packages directory

PYTHONEXECUTABLE[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONEXECUTABLE "Link to this definition")

If this environment variable is set, `sys.argv[0]` will be set to its value instead of the value got through the C runtime. Only works on macOS.

PYTHONWARNINGS[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS "Link to this definition")

This is equivalent to the [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W)
 option. If set to a comma separated string, it is equivalent to specifying `-W` multiple times, with filters later in the list taking precedence over those earlier in the list.

The simplest settings apply a particular action unconditionally to all warnings emitted by a process (even those that are otherwise ignored by default):

Copy

PYTHONWARNINGS\=default  \# Warn once per call location
PYTHONWARNINGS\=error    \# Convert to exceptions
PYTHONWARNINGS\=always   \# Warn every time
PYTHONWARNINGS\=all      \# Same as PYTHONWARNINGS=always
PYTHONWARNINGS\=module   \# Warn once per calling module
PYTHONWARNINGS\=once     \# Warn once per Python process
PYTHONWARNINGS\=ignore   \# Never warn

See [The Warnings Filter](https://docs.python.org/3/library/warnings.html#warning-filter)
 and [Describing Warning Filters](https://docs.python.org/3/library/warnings.html#describing-warning-filters)
 for more details.

Changed in version 3.15: Added regular expression support for _message_ and _module_.

PYTHONFAULTHANDLER[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER "Link to this definition")

If this environment variable is set to a non-empty string, [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable")
 is called at startup: install a handler for [`SIGSEGV`](https://docs.python.org/3/library/signal.html#signal.SIGSEGV "signal.SIGSEGV")
, [`SIGFPE`](https://docs.python.org/3/library/signal.html#signal.SIGFPE "signal.SIGFPE")
, [`SIGABRT`](https://docs.python.org/3/library/signal.html#signal.SIGABRT "signal.SIGABRT")
, [`SIGBUS`](https://docs.python.org/3/library/signal.html#signal.SIGBUS "signal.SIGBUS")
 and [`SIGILL`](https://docs.python.org/3/library/signal.html#signal.SIGILL "signal.SIGILL")
 signals to dump the Python traceback. This is equivalent to [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `faulthandler` option.

Added in version 3.3.

PYTHONTRACEMALLOC[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONTRACEMALLOC "Link to this definition")

If this environment variable is set to a non-empty string, start tracing Python memory allocations using the [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")
 module. The value of the variable is the maximum number of frames stored in a traceback of a trace. For example, `PYTHONTRACEMALLOC=1` stores only the most recent frame. See the [`tracemalloc.start()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.start "tracemalloc.start")
 function for more information. This is equivalent to setting the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `tracemalloc` option.

Added in version 3.4.

PYTHONPROFILEIMPORTTIME[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPROFILEIMPORTTIME "Link to this definition")

If this environment variable is set to `1`, Python will show how long each import takes. If set to `2`, Python will include output for imported modules that have already been loaded. This is equivalent to setting the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `importtime` option.

Added in version 3.7.

Changed in version 3.14: Added `PYTHONPROFILEIMPORTTIME=2` to also trace imports of loaded modules.

PYTHONASYNCIODEBUG[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONASYNCIODEBUG "Link to this definition")

If this environment variable is set to a non-empty string, enable the [debug mode](https://docs.python.org/3/library/asyncio-dev.html#asyncio-debug-mode)
 of the [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
 module.

Added in version 3.4.

PYTHONMALLOC[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC "Link to this definition")

Set the Python memory allocators and/or install debug hooks.

Set the family of memory allocators used by Python:

*   `default`: use the [default memory allocators](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
    .
    
*   `malloc`: use the `malloc()` function of the C library for all domains ([`PYMEM_DOMAIN_RAW`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_RAW "PYMEM_DOMAIN_RAW")
    , [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_MEM "PYMEM_DOMAIN_MEM")
    , [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "PYMEM_DOMAIN_OBJ")
    ).
    
*   `pymalloc`: use the [pymalloc allocator](https://docs.python.org/3/c-api/memory.html#pymalloc)
     for [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_MEM "PYMEM_DOMAIN_MEM")
     and [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "PYMEM_DOMAIN_OBJ")
     domains and use the `malloc()` function for the [`PYMEM_DOMAIN_RAW`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_RAW "PYMEM_DOMAIN_RAW")
     domain.
    
*   `mimalloc`: use the [mimalloc allocator](https://docs.python.org/3/c-api/memory.html#mimalloc)
     for [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_MEM "PYMEM_DOMAIN_MEM")
     and [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "PYMEM_DOMAIN_OBJ")
     domains and use the `malloc()` function for the [`PYMEM_DOMAIN_RAW`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_RAW "PYMEM_DOMAIN_RAW")
     domain.
    

Install [debug hooks](https://docs.python.org/3/c-api/memory.html#pymem-debug-hooks)
:

*   `debug`: install debug hooks on top of the [default memory allocators](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
    .
    
*   `malloc_debug`: same as `malloc` but also install debug hooks.
    
*   `pymalloc_debug`: same as `pymalloc` but also install debug hooks.
    
*   `mimalloc_debug`: same as `mimalloc` but also install debug hooks.
    

Note

In the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build, the `malloc`, `malloc_debug`, `pymalloc`, and `pymalloc_debug` values are not supported. Only `default`, `debug`, `mimalloc`, and `mimalloc_debug` are accepted.

Added in version 3.6.

Changed in version 3.7: Added the `"default"` allocator.

PYTHONMALLOCSTATS[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOCSTATS "Link to this definition")

If set to a non-empty string, Python will print statistics of the [pymalloc memory allocator](https://docs.python.org/3/c-api/memory.html#pymalloc)
 or the [mimalloc memory allocator](https://docs.python.org/3/c-api/memory.html#mimalloc)
 (whichever is in use) every time a new object arena is created, and on shutdown.

This variable is ignored if the [`PYTHONMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC)
 environment variable is used to force the `malloc()` allocator of the C library, or if Python is configured without both `pymalloc` and `mimalloc` support.

Changed in version 3.6: This variable can now also be used on Python compiled in release mode. It now has no effect if set to an empty string.

PYTHON\_PYMALLOC\_HUGEPAGES[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PYMALLOC_HUGEPAGES "Link to this definition")

If set to a non-zero integer, enable huge page support for [pymalloc](https://docs.python.org/3/c-api/memory.html#pymalloc)
 arenas. Set to `0` or unset to disable. Python must be compiled with [`--with-pymalloc-hugepages`](https://docs.python.org/3/using/configure.html#cmdoption-with-pymalloc-hugepages)
 for this variable to have any effect.

When enabled, arena allocation uses `MAP_HUGETLB` (Linux) or `MEM_LARGE_PAGES` (Windows) with automatic fallback to regular pages if huge pages are not available.

Warning

On Linux, if the huge-page pool is exhausted, page faults — including copy-on-write faults triggered by [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
 — deliver `SIGBUS` and kill the process. Only enable this in environments where the huge-page pool is properly sized and fork-safety is not a concern.

On Windows you need a special privilege. See the [Windows documentation for large pages](https://learn.microsoft.com/windows/win32/memory/large-page-support)
 for details. Python will fail on startup if the required privilege [SeLockMemoryPrivilege](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/lock-pages-in-memory)
 is not held by the user.

Added in version 3.15.

PYTHONLEGACYWINDOWSFSENCODING[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING "Link to this definition")

If set to a non-empty string, the default [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 mode will revert to their pre-3.6 values of ‘mbcs’ and ‘replace’, respectively. Otherwise, the new defaults ‘utf-8’ and ‘surrogatepass’ are used.

This may also be enabled at runtime with [`sys._enablelegacywindowsfsencoding()`](https://docs.python.org/3/library/sys.html#sys._enablelegacywindowsfsencoding "sys._enablelegacywindowsfsencoding")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Added in version 3.6: See [**PEP 529**](https://peps.python.org/pep-0529/)
 for more details.

PYTHONLEGACYWINDOWSSTDIO[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO "Link to this definition")

If set to a non-empty string, does not use the new console reader and writer. This means that Unicode characters will be encoded according to the active console code page, rather than using utf-8.

This variable is ignored if the standard streams are redirected (to files or pipes) rather than referring to console buffers.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Added in version 3.6.

PYTHONCOERCECLOCALE[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONCOERCECLOCALE "Link to this definition")

If set to the value `0`, causes the main Python command line application to skip coercing the legacy ASCII-based C and POSIX locales to a more capable UTF-8 based alternative.

If this variable is _not_ set (or is set to a value other than `0`), the `LC_ALL` locale override environment variable is also not set, and the current locale reported for the `LC_CTYPE` category is either the default `C` locale, or else the explicitly ASCII-based `POSIX` locale, then the Python CLI will attempt to configure the following locales for the `LC_CTYPE` category in the order listed before loading the interpreter runtime:

*   `C.UTF-8`
    
*   `C.utf8`
    
*   `UTF-8`
    

If setting one of these locale categories succeeds, then the `LC_CTYPE` environment variable will also be set accordingly in the current process environment before the Python runtime is initialized. This ensures that in addition to being seen by both the interpreter itself and other locale-aware components running in the same process (such as the GNU `readline` library), the updated setting is also seen in subprocesses (regardless of whether or not those processes are running a Python interpreter), as well as in operations that query the environment rather than the current C locale (such as Python’s own [`locale.getdefaultlocale()`](https://docs.python.org/3/library/locale.html#locale.getdefaultlocale "locale.getdefaultlocale")
).

Configuring one of these locales (either explicitly or via the above implicit locale coercion) automatically enables the `surrogateescape` [error handler](https://docs.python.org/3/library/codecs.html#error-handlers)
 for [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
 and [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 ([`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 continues to use `backslashreplace` as it does in any other locale). This stream handling behavior can be overridden using [`PYTHONIOENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONIOENCODING)
 as usual.

For debugging purposes, setting `PYTHONCOERCECLOCALE=warn` will cause Python to emit warning messages on `stderr` if either the locale coercion activates, or else if a locale that _would_ have triggered coercion is still active when the Python runtime is initialized.

Also note that even when locale coercion is disabled, or when it fails to find a suitable target locale, [`PYTHONUTF8`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8)
 will still activate by default in legacy ASCII-based locales. Both features must be disabled in order to force the interpreter to use `ASCII` instead of `UTF-8` for system interfaces.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.7: See [**PEP 538**](https://peps.python.org/pep-0538/)
 for more details.

PYTHONDEVMODE[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDEVMODE "Link to this definition")

If this environment variable is set to a non-empty string, enable [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
, introducing additional runtime checks that are too expensive to be enabled by default. This is equivalent to setting the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `dev` option.

Added in version 3.7.

PYTHONUTF8[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8 "Link to this definition")

If set to `1`, enable the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
.

If set to `0`, disable the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
.

Setting any other non-empty string causes an error during interpreter initialisation.

Added in version 3.7.

PYTHONWARNDEFAULTENCODING[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING "Link to this definition")

If this environment variable is set to a non-empty string, issue a [`EncodingWarning`](https://docs.python.org/3/builtins/exceptions.html#EncodingWarning "EncodingWarning")
 when the locale-specific default encoding is used.

See [Opt-in EncodingWarning](https://docs.python.org/3/library/io.html#io-encoding-warning)
 for details.

Added in version 3.10.

PYTHONNODEBUGRANGES[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNODEBUGRANGES "Link to this definition")

If this variable is set, it disables the inclusion of the tables mapping extra location information (end line, start column offset and end column offset) to every instruction in code objects. This is useful when smaller code objects and pyc files are desired as well as suppressing the extra visual location indicators when the interpreter displays tracebacks.

Added in version 3.11.

PYTHONPERFSUPPORT[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPERFSUPPORT "Link to this definition")

If this variable is set to a nonzero value, it enables support for the Linux `perf` profiler so Python calls can be detected by it.

If set to `0`, disable Linux `perf` profiler support.

See also the [`-X perf`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option and [Python support for the perf map compatible profilers](https://docs.python.org/3/howto/perf_profiling.html#perf-profiling)
.

Added in version 3.12.

PYTHON\_PERF\_JIT\_SUPPORT[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PERF_JIT_SUPPORT "Link to this definition")

If this variable is set to a nonzero value, it enables support for the Linux `perf` profiler so Python calls can be detected by it using DWARF information.

If set to `0`, disable Linux `perf` profiler support.

See also the [`-X perf_jit`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option and [Python support for the perf map compatible profilers](https://docs.python.org/3/howto/perf_profiling.html#perf-profiling)
.

Added in version 3.13.

PYTHON\_DISABLE\_REMOTE\_DEBUG[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_DISABLE_REMOTE_DEBUG "Link to this definition")

If this variable is set to a non-empty string, it disables the remote debugging feature described in [**PEP 768**](https://peps.python.org/pep-0768/)
. This includes both the functionality to schedule code for execution in another process and the functionality to receive code for execution in the current process.

See also the [`-X disable-remote-debug`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option.

Added in version 3.14.

PYTHON\_CPU\_COUNT[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT "Link to this definition")

If this variable is set to a positive integer, it overrides the return values of [`os.cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count")
 and [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
.

See also the [`-X cpu_count`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option.

Added in version 3.13.

PYTHON\_FROZEN\_MODULES[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_FROZEN_MODULES "Link to this definition")

If this variable is set to `on` or `off`, it determines whether or not frozen modules are ignored by the import machinery. A value of `on` means they get imported and `off` means they are ignored. The default is `on` for non-debug builds (the normal case) and `off` for debug builds. Note that the `importlib_bootstrap` and `importlib_bootstrap_external` frozen modules are always used, even if this flag is set to `off`.

See also the [`-X frozen_modules`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option.

Added in version 3.13.

PYTHON\_COLORS[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_COLORS "Link to this definition")

If this variable is set to `1`, the interpreter will colorize various kinds of output. Setting it to `0` deactivates this behavior. See also [Controlling color](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
.

Added in version 3.13.

PYTHON\_BASIC\_REPL[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_BASIC_REPL "Link to this definition")

If this variable is set to any value, the interpreter will not attempt to load the Python-based [REPL](https://docs.python.org/3/glossary.html#term-REPL)
 that requires [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
, and will instead use the traditional parser-based REPL.

Added in version 3.13.

PYTHON\_BASIC\_COMPLETER[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_BASIC_COMPLETER "Link to this definition")

If this variable is set to any value, PyREPL will use [`rlcompleter`](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.")
 to implement tab completion, instead of the default one which uses colors.

Added in version 3.15.

PYTHON\_HISTORY[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_HISTORY "Link to this definition")

This environment variable can be used to set the location of a `.python_history` file (by default, it is `.python_history` in the user’s home directory).

Added in version 3.13.

PYTHON\_GIL[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_GIL "Link to this definition")

If this variable is set to `1`, the global interpreter lock (GIL) will be forced on. Setting it to `0` forces the GIL off (needs Python configured with the [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
 build option).

See also the [`-X gil`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option, which takes precedence over this variable, and [Free-threaded CPython](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-free-threaded-cpython)
.

Added in version 3.13.

PYTHON\_THREAD\_INHERIT\_CONTEXT[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_THREAD_INHERIT_CONTEXT "Link to this definition")

If this variable is set to `1` then [`Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread")
 will, by default, use a copy of context of the caller of `Thread.start()` when starting. Otherwise, new threads will start with an empty context. If unset, this variable defaults to `1` on free-threaded builds and to `0` otherwise. See also [`-X thread_inherit_context`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
.

Added in version 3.14.

PYTHON\_CONTEXT\_AWARE\_WARNINGS[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CONTEXT_AWARE_WARNINGS "Link to this definition")

If set to `1` then the [`warnings.catch_warnings`](https://docs.python.org/3/library/warnings.html#warnings.catch_warnings "warnings.catch_warnings")
 context manager will use a [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar")
 to store warnings filter state. If unset, this variable defaults to `1` on free-threaded builds and to `0` otherwise. See [`-X context_aware_warnings`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
.

Added in version 3.14.

PYTHON\_PATHCONFIG\_WARNINGS[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PATHCONFIG_WARNINGS "Link to this definition")

If true (`1`) then [The initialization of the sys.path module search path](https://docs.python.org/3/library/sys_path_init.html#sys-path-init)
 is allowed to log warnings into stderr. If false (`0`) suppress these warnings. Set to true by default. See also [`-X pathconfig_warnings`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
.

Added in version 3.15.

PYTHON\_JIT[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_JIT "Link to this definition")

On builds where experimental just-in-time compilation is available, this variable can force the JIT to be disabled (`0`) or enabled (`1`) at interpreter startup.

Added in version 3.13.

PYTHON\_TLBC[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_TLBC "Link to this definition")

If set to `1` enables thread-local bytecode. If set to `0` thread-local bytecode and the specializing interpreter are disabled. Only applies to builds configured with [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
.

See also the [`-X tlbc`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option.

Added in version 3.14.

PYTHON\_LAZY\_IMPORTS[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_LAZY_IMPORTS "Link to this definition")

Controls lazy import behavior. Accepts two values: `all` makes all imports lazy by default, and `normal` (the default) respects the `lazy` keyword in source code.

See also the [`-X lazy_imports`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option.

Added in version 3.15.

### 1.2.1. Debug-mode variables[¶](https://docs.python.org/3/using/cmdline.html#debug-mode-variables "Link to this heading")

PYTHONDUMPREFS[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDUMPREFS "Link to this definition")

If set, Python will dump objects and reference counts still alive after shutting down the interpreter.

Needs Python configured with the [`--with-trace-refs`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs)
 build option.

PYTHONDUMPREFSFILE[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDUMPREFSFILE "Link to this definition")

If set, Python will dump objects and reference counts still alive after shutting down the interpreter into a file under the path given as the value to this environment variable.

Needs Python configured with the [`--with-trace-refs`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs)
 build option.

Added in version 3.11.

PYTHON\_PRESITE[¶](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PRESITE "Link to this definition")

If this variable is set to a module, that module will be imported early in the interpreter lifecycle, before the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module is executed, and before the [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.")
 module is created. Therefore, the imported module is not treated as `__main__`.

This can be used to execute code early during Python initialization.

To import a submodule, use `package.module` as the value, like in an import statement.

See also the [`-X presite`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option, which takes precedence over this variable.

Needs Python configured with the [`--with-pydebug`](https://docs.python.org/3/using/configure.html#cmdoption-with-pydebug)
 build option.

Changed in version 3.15: Accept also `module:func` entry point format.

Added in version 3.13.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [1\. Command line and environment](https://docs.python.org/3/using/cmdline.html#)
    *   [1.1. Command line](https://docs.python.org/3/using/cmdline.html#command-line)
        *   [1.1.1. Interface options](https://docs.python.org/3/using/cmdline.html#interface-options)
            
        *   [1.1.2. Generic options](https://docs.python.org/3/using/cmdline.html#generic-options)
            
        *   [1.1.3. Miscellaneous options](https://docs.python.org/3/using/cmdline.html#miscellaneous-options)
            
        *   [1.1.4. Controlling color](https://docs.python.org/3/using/cmdline.html#controlling-color)
            
    *   [1.2. Environment variables](https://docs.python.org/3/using/cmdline.html#environment-variables)
        *   [1.2.1. Debug-mode variables](https://docs.python.org/3/using/cmdline.html#debug-mode-variables)
            

#### Previous topic

[Python Setup and Usage](https://docs.python.org/3/using/index.html "previous chapter")

#### Next topic

[2\. Using Python on Unix platforms](https://docs.python.org/3/using/unix.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=1.+Command+line+and+environment&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fusing%2Fcmdline.html&pagesource=using%2Fcmdline.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/using/cmdline.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/unix.html "2. Using Python on Unix platforms")
     |
*   [previous](https://docs.python.org/3/using/index.html "Python Setup and Usage")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python Setup and Usage](https://docs.python.org/3/using/index.html)
     »
*   [1\. Command line and environment](https://docs.python.org/3/using/cmdline.html)
    
*    
    
    |
*   Theme Auto Light Dark |