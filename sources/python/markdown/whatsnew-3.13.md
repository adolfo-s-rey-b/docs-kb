### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/3.12.html "What’s New In Python 3.12")
     |
*   [previous](https://docs.python.org/3/whatsnew/3.14.html "What’s new in Python 3.14")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [What’s New in Python](https://docs.python.org/3/whatsnew/index.html)
     »
*   [What’s New In Python 3.13](https://docs.python.org/3/whatsnew/3.13.html)
    
*    
    
    |
*   Theme Auto Light Dark |

What’s New In Python 3.13[¶](https://docs.python.org/3/whatsnew/3.13.html#what-s-new-in-python-3-13 "Link to this heading")

============================================================================================================================

Editors:

Adam Turner and Thomas Wouters

This article explains the new features in Python 3.13, compared to 3.12. Python 3.13 was released on October 7, 2024. For full details, see the [changelog](https://docs.python.org/3/whatsnew/changelog.html#changelog)
.

See also

[**PEP 719**](https://peps.python.org/pep-0719/)
 – Python 3.13 Release Schedule

Summary – Release Highlights[¶](https://docs.python.org/3/whatsnew/3.13.html#summary-release-highlights "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Python 3.13 is a stable release of the Python programming language, with a mix of changes to the language, the implementation and the standard library. The biggest changes include a new [interactive interpreter](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-better-interactive-interpreter)
, experimental support for running in a [free-threaded mode](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-free-threaded-cpython)
 ([**PEP 703**](https://peps.python.org/pep-0703/)
), and a [Just-In-Time compiler](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-jit-compiler)
 ([**PEP 744**](https://peps.python.org/pep-0744/)
).

Error messages continue to improve, with tracebacks now highlighted in color by default. The [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
 builtin now has [defined semantics](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-locals-semantics)
 for changing the returned mapping, and type parameters now support default values.

The library changes contain removal of deprecated APIs and modules, as well as the usual improvements in user-friendliness and correctness. Several legacy standard library modules have now [been removed](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-pep594)
 following their deprecation in Python 3.11 ([**PEP 594**](https://peps.python.org/pep-0594/)
).

This article doesn’t attempt to provide a complete specification of all new features, but instead gives a convenient overview. For full details refer to the documentation, such as the [Library Reference](https://docs.python.org/3/library/index.html#library-index)
 and [Language Reference](https://docs.python.org/3/reference/index.html#reference-index)
. To understand the complete implementation and design rationale for a change, refer to the PEP for a particular new feature; but note that PEPs usually are not kept up-to-date once a feature has been fully implemented. See [Porting to Python 3.13](https://docs.python.org/3/whatsnew/3.13.html#porting-to-python-3-13)
 for guidance on upgrading from earlier versions of Python.

* * *

Interpreter improvements:

*   A greatly improved [interactive interpreter](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-better-interactive-interpreter)
     and [improved error messages](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-improved-error-messages)
    .
    
*   [**PEP 667**](https://peps.python.org/pep-0667/)
    : The [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
     builtin now has [defined semantics](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-locals-semantics)
     when mutating the returned mapping. Python debuggers and similar tools may now more reliably update local variables in optimized scopes even during concurrent code execution.
    
*   [**PEP 703**](https://peps.python.org/pep-0703/)
    : CPython 3.13 has experimental support for running with the [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
     disabled. See [Free-threaded CPython](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-free-threaded-cpython)
     for more details.
    
*   [**PEP 744**](https://peps.python.org/pep-0744/)
    : A basic [JIT compiler](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-jit-compiler)
     was added. It is currently disabled by default (though we may turn it on later). Performance improvements are modest – we expect to improve this over the next few releases.
    
*   Color support in the new [interactive interpreter](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-better-interactive-interpreter)
    , as well as in [tracebacks](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-improved-error-messages)
     and [doctest](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-doctest)
     output. This can be disabled through the [`PYTHON_COLORS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_COLORS)
     and [`NO_COLOR`](https://no-color.org/)
     environment variables.
    

Python data model improvements:

*   [`__static_attributes__`](https://docs.python.org/3/reference/datamodel.html#type.__static_attributes__ "type.__static_attributes__")
     stores the names of attributes accessed through `self.X` in any function in a class body.
    
*   [`__firstlineno__`](https://docs.python.org/3/reference/datamodel.html#type.__firstlineno__ "type.__firstlineno__")
     records the first line number of a class definition.
    

Significant improvements in the standard library:

*   Add a new [`PythonFinalizationError`](https://docs.python.org/3/builtins/exceptions.html#PythonFinalizationError "PythonFinalizationError")
     exception, raised when an operation is blocked during [finalization](https://docs.python.org/3/glossary.html#term-interpreter-shutdown)
    .
    
*   The [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
     module now supports deprecating command-line options, positional arguments, and subcommands.
    
*   The new functions [`base64.z85encode()`](https://docs.python.org/3/library/base64.html#base64.z85encode "base64.z85encode")
     and [`base64.z85decode()`](https://docs.python.org/3/library/base64.html#base64.z85decode "base64.z85decode")
     support encoding and decoding [Z85 data](https://rfc.zeromq.org/spec/32/)
    .
    
*   The [`copy`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.")
     module now has a [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace")
     function, with support for many builtin types and any class defining the [`__replace__()`](https://docs.python.org/3/library/copy.html#object.__replace__ "object.__replace__")
     method.
    
*   The new [`dbm.sqlite3`](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm")
     module is now the default [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Interfaces to various Unix "database" formats.")
     backend.
    
*   The [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
     module has a [suite of new functions](https://docs.python.org/3/library/os.html#os-timerfd)
     for working with Linux’s timer notification file descriptors.
    
*   The [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.")
     module now has a [command-line interface](https://docs.python.org/3/library/random.html#random-cli)
    .
    

Security improvements:

*   [`ssl.create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context")
     sets [`ssl.VERIFY_X509_PARTIAL_CHAIN`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN "ssl.VERIFY_X509_PARTIAL_CHAIN")
     and [`ssl.VERIFY_X509_STRICT`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_STRICT "ssl.VERIFY_X509_STRICT")
     as default flags.
    

C API improvements:

*   The [`Py_mod_gil`](https://docs.python.org/3/c-api/module.html#c.Py_mod_gil "Py_mod_gil")
     slot is now used to indicate that an extension module supports running with the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
     disabled.
    
*   The [PyTime C API](https://docs.python.org/3/c-api/time.html)
     has been added, providing access to system clocks.
    
*   [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
     is a new lightweight mutex that occupies a single byte.
    
*   There is a new [suite of functions](https://docs.python.org/3/c-api/monitoring.html#c-api-monitoring)
     for generating [**PEP 669**](https://peps.python.org/pep-0669/)
     monitoring events in the C API.
    

New typing features:

*   [**PEP 696**](https://peps.python.org/pep-0696/)
    : Type parameters ([`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar")
    , [`typing.ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec")
    , and [`typing.TypeVarTuple`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple")
    ) now support defaults.
    
*   [**PEP 702**](https://peps.python.org/pep-0702/)
    : The new [`warnings.deprecated()`](https://docs.python.org/3/library/warnings.html#warnings.deprecated "warnings.deprecated")
     decorator adds support for marking deprecations in the type system and at runtime.
    
*   [**PEP 705**](https://peps.python.org/pep-0705/)
    : [`typing.ReadOnly`](https://docs.python.org/3/library/typing.html#typing.ReadOnly "typing.ReadOnly")
     can be used to mark an item of a [`typing.TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict")
     as read-only for type checkers.
    
*   [**PEP 742**](https://peps.python.org/pep-0742/)
    : [`typing.TypeIs`](https://docs.python.org/3/library/typing.html#typing.TypeIs "typing.TypeIs")
     provides more intuitive type narrowing behavior, as an alternative to [`typing.TypeGuard`](https://docs.python.org/3/library/typing.html#typing.TypeGuard "typing.TypeGuard")
    .
    

Platform support:

*   [**PEP 730**](https://peps.python.org/pep-0730/)
    : Apple’s iOS is now an [officially supported platform](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-platform-support)
    , at [**tier 3**](https://peps.python.org/pep-0011/#tier-3)
    .
    
*   [**PEP 738**](https://peps.python.org/pep-0738/)
    : Android is now an [officially supported platform](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-platform-support)
    , at [**tier 3**](https://peps.python.org/pep-0011/#tier-3)
    .
    
*   `wasm32-wasi` is now supported as a [**tier 2**](https://peps.python.org/pep-0011/#tier-2)
     platform.
    
*   `wasm32-emscripten` is no longer an officially supported platform.
    

Important removals:

*   [PEP 594](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-pep594)
    : The remaining 19 “dead batteries” (legacy stdlib modules) have been removed from the standard library: `aifc`, `audioop`, `cgi`, `cgitb`, `chunk`, `crypt`, `imghdr`, `mailcap`, `msilib`, `nis`, `nntplib`, `ossaudiodev`, `pipes`, `sndhdr`, `spwd`, `sunau`, `telnetlib`, `uu` and `xdrlib`.
    
*   Remove the **2to3** tool and `lib2to3` module (deprecated in Python 3.11).
    
*   Remove the `tkinter.tix` module (deprecated in Python 3.6).
    
*   Remove the `locale.resetlocale()` function.
    
*   Remove the `typing.io` and `typing.re` namespaces.
    
*   Remove chained [`classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
     descriptors.
    

Release schedule changes:

[**PEP 602**](https://peps.python.org/pep-0602/)
 (“Annual Release Cycle for Python”) has been updated to extend the full support (‘bugfix’) period for new releases to two years. This updated policy means that:

*   Python 3.9–3.12 have one and a half years of full support, followed by three and a half years of security fixes.
    
*   Python 3.13 and later have two years of full support, followed by three years of security fixes.
    

New Features[¶](https://docs.python.org/3/whatsnew/3.13.html#new-features "Link to this heading")

--------------------------------------------------------------------------------------------------

### A better interactive interpreter[¶](https://docs.python.org/3/whatsnew/3.13.html#a-better-interactive-interpreter "Link to this heading")

Python now uses a new [interactive](https://docs.python.org/3/glossary.html#term-interactive)
 shell by default, based on code from the [PyPy project](https://pypy.org/)
. When the user starts the [REPL](https://docs.python.org/3/glossary.html#term-REPL)
 from an interactive terminal, the following new features are now supported:

*   Multiline editing with history preservation.
    
*   Direct support for REPL-specific commands like help, exit, and quit, without the need to call them as functions.
    
*   Prompts and tracebacks with [color enabled by default](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    .
    
*   Interactive help browsing using F1 with a separate command history.
    
*   History browsing using F2 that skips output as well as the [\>>>](https://docs.python.org/3/glossary.html#term-0)
     and […](https://docs.python.org/3/glossary.html#term-...)
     prompts.
    
*   “Paste mode” with F3 that makes pasting larger blocks of code easier (press F3 again to return to the regular prompt).
    

To disable the new interactive shell, set the [`PYTHON_BASIC_REPL`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_BASIC_REPL)
 environment variable. For more on interactive mode, see [Interactive Mode](https://docs.python.org/3/tutorial/appendix.html#tut-interac)
.

(Contributed by Pablo Galindo Salgado, Łukasz Langa, and Lysandros Nikolaou in [gh-111201](https://github.com/python/cpython/issues/111201)
 based on code from the PyPy project. Windows support contributed by Dino Viehland and Anthony Shaw.)

### Improved error messages[¶](https://docs.python.org/3/whatsnew/3.13.html#improved-error-messages "Link to this heading")

*   The interpreter now uses color by default when displaying tracebacks in the terminal. This feature [can be controlled](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
     via the new [`PYTHON_COLORS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_COLORS)
     environment variable as well as the canonical [`NO_COLOR`](https://no-color.org/)
     and [`FORCE_COLOR`](https://force-color.org/)
     environment variables. (Contributed by Pablo Galindo Salgado in [gh-112730](https://github.com/python/cpython/issues/112730)
    .)
    
*   A common mistake is to write a script with the same name as a standard library module. When this results in errors, we now display a more helpful error message:
    
    $ python random.py
    Traceback (most recent call last):
      File "/home/me/random.py", line 1, in <module>
        import random
      File "/home/me/random.py", line 3, in <module>
        print(random.randint(5))
              ^^^^^^^^^^^^^^
    AttributeError: module 'random' has no attribute 'randint' (consider renaming '/home/me/random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
    
    Similarly, if a script has the same name as a third-party module that it attempts to import and this results in errors, we also display a more helpful error message:
    
    $ python numpy.py
    Traceback (most recent call last):
      File "/home/me/numpy.py", line 1, in <module>
        import numpy as np
      File "/home/me/numpy.py", line 3, in <module>
        np.array(\[1, 2, 3\])
        ^^^^^^^^
    AttributeError: module 'numpy' has no attribute 'array' (consider renaming '/home/me/numpy.py' if it has the same name as a library you intended to import)
    
    (Contributed by Shantanu Jain in [gh-95754](https://github.com/python/cpython/issues/95754)
    .)
    
*   The error message now tries to suggest the correct keyword argument when an incorrect keyword argument is passed to a function.
    
    Copy
    
    \>>> "Better error messages!".split(max\_split\=1)
    Traceback (most recent call last):
      File "<python-input-0>", line 1, in <module>
        "Better error messages!".split(max\_split\=1)
        \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
    TypeError: split() got an unexpected keyword argument 'max\_split'. Did you mean 'maxsplit'?
    
    (Contributed by Pablo Galindo Salgado and Shantanu Jain in [gh-107944](https://github.com/python/cpython/issues/107944)
    .)
    

### Free-threaded CPython[¶](https://docs.python.org/3/whatsnew/3.13.html#free-threaded-cpython "Link to this heading")

CPython now has experimental support for running in a free-threaded mode, with the [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
 (GIL) disabled. This is an experimental feature and therefore is not enabled by default. The free-threaded mode requires a different executable, usually called `python3.13t` or `python3.13t.exe`. Pre-built binaries marked as _free-threaded_ can be installed as part of the official [Windows](https://docs.python.org/3/using/windows.html#install-freethreaded-windows)
 and [macOS](https://docs.python.org/3/using/mac.html#install-freethreaded-macos)
 installers, or CPython can be built from source with the [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
 option.

Free-threaded execution allows for full utilization of the available processing power by running threads in parallel on available CPU cores. While not all software will benefit from this automatically, programs designed with threading in mind will run faster on multi-core hardware. **The free-threaded mode is experimental** and work is ongoing to improve it: expect some bugs and a substantial single-threaded performance hit. Free-threaded builds of CPython support optionally running with the GIL enabled at runtime using the environment variable [`PYTHON_GIL`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_GIL)
 or the command-line option [`-X gil=1`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
.

To check if the current interpreter supports free-threading, [`python -VV`](https://docs.python.org/3/using/cmdline.html#cmdoption-V)
 and [`sys.version`](https://docs.python.org/3/library/sys.html#sys.version "sys.version")
 contain “experimental free-threading build”. The new `sys._is_gil_enabled()` function can be used to check whether the GIL is actually disabled in the running process.

C-API extension modules need to be built specifically for the free-threaded build. Extensions that support running with the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
 disabled should use the [`Py_mod_gil`](https://docs.python.org/3/c-api/module.html#c.Py_mod_gil "Py_mod_gil")
 slot. Extensions using single-phase init should use [`PyUnstable_Module_SetGIL()`](https://docs.python.org/3/c-api/module.html#c.PyUnstable_Module_SetGIL "PyUnstable_Module_SetGIL")
 to indicate whether they support running with the GIL disabled. Importing C extensions that don’t use these mechanisms will cause the GIL to be enabled, unless the GIL was explicitly disabled with the [`PYTHON_GIL`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_GIL)
 environment variable or the [`-X gil=0`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 option. pip 24.1 or newer is required to install packages with C extensions in the free-threaded build.

This work was made possible thanks to many individuals and organizations, including the large community of contributors to Python and third-party projects to test and enable free-threading support. Notable contributors include: Sam Gross, Ken Jin, Donghee Na, Itamar Oren, Matt Page, Brett Simmers, Dino Viehland, Carl Meyer, Nathan Goldbaum, Ralf Gommers, Lysandros Nikolaou, and many others. Many of these contributors are employed by Meta, which has provided significant engineering resources to support this project.

See also

[**PEP 703**](https://peps.python.org/pep-0703/)
 “Making the Global Interpreter Lock Optional in CPython” contains rationale and information surrounding this work.

[Porting Extension Modules to Support Free-Threading](https://py-free-threading.github.io/porting/)
: A community-maintained porting guide for extension authors.

### An experimental just-in-time (JIT) compiler[¶](https://docs.python.org/3/whatsnew/3.13.html#an-experimental-just-in-time-jit-compiler "Link to this heading")

When CPython is configured and built using the `--enable-experimental-jit` option, a just-in-time (JIT) compiler is added which may speed up some Python programs. On Windows, use `PCbuild/build.bat --experimental-jit` to enable the JIT or `--experimental-jit-interpreter` to enable the Tier 2 interpreter. Build requirements and further supporting information [are contained at](https://github.com/python/cpython/blob/main/Tools/jit/README.md)
 `Tools/jit/README.md`.

The `--enable-experimental-jit` option takes these (optional) values, defaulting to `yes` if `--enable-experimental-jit` is present without the optional value.

*   `no`: Disable the entire Tier 2 and JIT pipeline.
    
*   `yes`: Enable the JIT. To disable the JIT at runtime, pass the environment variable `PYTHON_JIT=0`.
    
*   `yes-off`: Build the JIT but disable it by default. To enable the JIT at runtime, pass the environment variable `PYTHON_JIT=1`.
    
*   `interpreter`: Enable the Tier 2 interpreter but disable the JIT. The interpreter can be disabled by running with `PYTHON_JIT=0`.
    

The internal architecture is roughly as follows:

*   We start with specialized _Tier 1 bytecode_. See [What’s new in 3.11](https://docs.python.org/3/whatsnew/3.11.html#whatsnew311-pep659)
     for details.
    
*   When the Tier 1 bytecode gets hot enough, it gets translated to a new purely internal intermediate representation (IR), called the _Tier 2 IR_, and sometimes referred to as micro-ops (“uops”).
    
*   The Tier 2 IR uses the same stack-based virtual machine as Tier 1, but the instruction format is better suited to translation to machine code.
    
*   We have several optimization passes for Tier 2 IR, which are applied before it is interpreted or translated to machine code.
    
*   There is a Tier 2 interpreter, but it is mostly intended for debugging the earlier stages of the optimization pipeline. The Tier 2 interpreter can be enabled by configuring Python with `--enable-experimental-jit=interpreter`.
    
*   When the JIT is enabled, the optimized Tier 2 IR is translated to machine code, which is then executed.
    
*   The machine code translation process uses a technique called _copy-and-patch_. It has no runtime dependencies, but there is a new build-time dependency on LLVM.
    

See also

[**PEP 744**](https://peps.python.org/pep-0744/)

(JIT by Brandt Bucher, inspired by a paper by Haoran Xu and Fredrik Kjolstad. Tier 2 IR by Mark Shannon and Guido van Rossum. Tier 2 optimizer by Ken Jin.)

### Defined mutation semantics for [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
[¶](https://docs.python.org/3/whatsnew/3.13.html#defined-mutation-semantics-for-locals "Link to this heading")

Historically, the expected result of mutating the return value of [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
 has been left to individual Python implementations to define. Starting from Python 3.13, [**PEP 667**](https://peps.python.org/pep-0667/)
 standardises the historical behavior of CPython for most code execution scopes, but changes [optimized scopes](https://docs.python.org/3/glossary.html#term-optimized-scope)
 (functions, generators, coroutines, comprehensions, and generator expressions) to explicitly return independent snapshots of the currently assigned local variables, including locally referenced nonlocal variables captured in closures.

This change to the semantics of [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
 in optimized scopes also affects the default behavior of code execution functions that implicitly target `locals()` if no explicit namespace is provided (such as [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 and [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
). In previous versions, whether or not changes could be accessed by calling `locals()` after calling the code execution function was implementation-dependent. In CPython specifically, such code would typically appear to work as desired, but could sometimes fail in optimized scopes based on other code (including debuggers and code execution tracing tools) potentially resetting the shared snapshot in that scope. Now, the code will always run against an independent snapshot of the local variables in optimized scopes, and hence the changes will never be visible in subsequent calls to `locals()`. To access the changes made in these cases, an explicit namespace reference must now be passed to the relevant function. Alternatively, it may make sense to update affected code to use a higher level code execution API that returns the resulting code execution namespace (e.g. [`runpy.run_path()`](https://docs.python.org/3/library/runpy.html#runpy.run_path "runpy.run_path")
 when executing Python files from disk).

To ensure debuggers and similar tools can reliably update local variables in scopes affected by this change, [`FrameType.f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 now returns a write-through proxy to the frame’s local and locally referenced nonlocal variables in these scopes, rather than returning an inconsistently updated shared `dict` instance with undefined runtime semantics.

See [**PEP 667**](https://peps.python.org/pep-0667/)
 for more details, including related C API changes and deprecations. Porting notes are also provided below for the affected [Python APIs](https://docs.python.org/3/whatsnew/3.13.html#pep667-porting-notes-py)
 and [C APIs](https://docs.python.org/3/whatsnew/3.13.html#pep667-porting-notes-c)
.

(PEP and implementation contributed by Mark Shannon and Tian Gao in [gh-74929](https://github.com/python/cpython/issues/74929)
. Documentation updates provided by Guido van Rossum and Alyssa Coghlan.)

### Support for mobile platforms[¶](https://docs.python.org/3/whatsnew/3.13.html#support-for-mobile-platforms "Link to this heading")

[**PEP 730**](https://peps.python.org/pep-0730/)
: iOS is now a [**PEP 11**](https://peps.python.org/pep-0011/)
 supported platform, with the `arm64-apple-ios` and `arm64-apple-ios-simulator` targets at tier 3 (iPhone and iPad devices released after 2013 and the Xcode iOS simulator running on Apple silicon hardware, respectively). `x86_64-apple-ios-simulator` (the Xcode iOS simulator running on older `x86_64` hardware) is not a tier 3 supported platform, but will have best-effort support. (PEP written and implementation contributed by Russell Keith-Magee in [gh-114099](https://github.com/python/cpython/issues/114099)
.)

[**PEP 738**](https://peps.python.org/pep-0738/)
: Android is now a [**PEP 11**](https://peps.python.org/pep-0011/)
 supported platform, with the `aarch64-linux-android` and `x86_64-linux-android` targets at tier 3. The 32-bit targets `arm-linux-androideabi` and `i686-linux-android` are not tier 3 supported platforms, but will have best-effort support. (PEP written and implementation contributed by Malcolm Smith in [gh-116622](https://github.com/python/cpython/issues/116622)
.)

See also

[**PEP 730**](https://peps.python.org/pep-0730/)
, [**PEP 738**](https://peps.python.org/pep-0738/)

Other Language Changes[¶](https://docs.python.org/3/whatsnew/3.13.html#other-language-changes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

*   The compiler now strips common leading whitespace from every line in a docstring. This reduces the size of the [bytecode cache](https://docs.python.org/3/glossary.html#term-bytecode)
     (such as `.pyc` files), with reductions in file size of around 5%, for example in `sqlalchemy.orm.session` from SQLAlchemy 2.0. This change affects tools that use docstrings, such as [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.")
    .
    
    Copy
    
    \>>> def spam():
    ... """
    ...         This is a docstring with
    ...           leading whitespace.
    ...
    ...         It even has multiple paragraphs!
    ...     """
    ...
    \>>> spam.\_\_doc\_\_
    '\\nThis is a docstring with\\n  leading whitespace.\\n\\nIt even has multiple paragraphs!\\n'
    
    (Contributed by Inada Naoki in [gh-81283](https://github.com/python/cpython/issues/81283)
    .)
    
*   [Annotation scopes](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
     within class scopes can now contain lambdas and comprehensions. Comprehensions that are located within class scopes are not inlined into their parent scope.
    
    Copy
    
    class C\[T\]:
        type Alias \= lambda: T
    
    (Contributed by Jelle Zijlstra in [gh-109118](https://github.com/python/cpython/issues/109118)
     and [gh-118160](https://github.com/python/cpython/issues/118160)
    .)
    
*   [Future statements](https://docs.python.org/3/reference/simple_stmts.html#future)
     are no longer triggered by relative imports of the [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions")
     module, meaning that statements of the form `from .__future__ import ...` are now simply standard relative imports, with no special features activated. (Contributed by Jeremiah Gabriel Pascual in [gh-118216](https://github.com/python/cpython/issues/118216)
    .)
    
*   [`global`](https://docs.python.org/3/reference/simple_stmts.html#global)
     declarations are now permitted in [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
     blocks when that global is used in the [`else`](https://docs.python.org/3/reference/compound_stmts.html#else)
     block. Previously this raised an erroneous [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
    . (Contributed by Irit Katriel in [gh-111123](https://github.com/python/cpython/issues/111123)
    .)
    
*   Add [`PYTHON_FROZEN_MODULES`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_FROZEN_MODULES)
    , a new environment variable that determines whether frozen modules are ignored by the import machinery, equivalent to the [`-X frozen_modules`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
     command-line option. (Contributed by Yilei Yang in [gh-111374](https://github.com/python/cpython/issues/111374)
    .)
    
*   Add [support for the perf profiler](https://docs.python.org/3/howto/perf_profiling.html#perf-profiling)
     working without [frame pointers](https://en.wikipedia.org/wiki/Call_stack)
     through the new environment variable [`PYTHON_PERF_JIT_SUPPORT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PERF_JIT_SUPPORT)
     and command-line option [`-X perf_jit`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
    . (Contributed by Pablo Galindo in [gh-118518](https://github.com/python/cpython/issues/118518)
    .)
    
*   The location of a `.python_history` file can be changed via the new [`PYTHON_HISTORY`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_HISTORY)
     environment variable. (Contributed by Levi Sabah, Zackery Spytz and Hugo van Kemenade in [gh-73965](https://github.com/python/cpython/issues/73965)
    .)
    
*   Classes have a new [`__static_attributes__`](https://docs.python.org/3/reference/datamodel.html#type.__static_attributes__ "type.__static_attributes__")
     attribute. This is populated by the compiler with a tuple of the class’s attribute names which are assigned through `self.<name>` from any function in its body. (Contributed by Irit Katriel in [gh-115775](https://github.com/python/cpython/issues/115775)
    .)
    
*   The compiler now creates a `__firstlineno__` attribute on classes with the line number of the first line of the class definition. (Contributed by Serhiy Storchaka in [gh-118465](https://github.com/python/cpython/issues/118465)
    .)
    
*   The [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
     and [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
     builtins now accept the _globals_ and _locals_ arguments as keywords. (Contributed by Raphael Gaschignard in [gh-105879](https://github.com/python/cpython/issues/105879)
    )
    
*   The [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
     builtin now accepts a new flag, `ast.PyCF_OPTIMIZED_AST`, which is similar to `ast.PyCF_ONLY_AST` except that the returned AST is optimized according to the value of the _optimize_ argument. (Contributed by Irit Katriel in [gh-108113](https://github.com/python/cpython/issues/108113)
    ).
    
*   Add a [`__name__`](https://docs.python.org/3/builtins/functions.html#property.__name__ "property.__name__")
     attribute on [`property`](https://docs.python.org/3/builtins/functions.html#property "property")
     objects. (Contributed by Eugene Toder in [gh-101860](https://github.com/python/cpython/issues/101860)
    .)
    
*   Add [`PythonFinalizationError`](https://docs.python.org/3/builtins/exceptions.html#PythonFinalizationError "PythonFinalizationError")
    , a new exception derived from [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
     and used to signal when operations are blocked during [finalization](https://docs.python.org/3/glossary.html#term-interpreter-shutdown)
    . The following callables now raise `PythonFinalizationError`, instead of `RuntimeError`:
    
    *   [`_thread.start_new_thread()`](https://docs.python.org/3/library/_thread.html#thread.start_new_thread "_thread.start_new_thread")
        
    *   [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
        
    *   [`os.forkpty()`](https://docs.python.org/3/library/os.html#os.forkpty "os.forkpty")
        
    *   [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
        
    
    (Contributed by Victor Stinner in [gh-114570](https://github.com/python/cpython/issues/114570)
    .)
    
*   Allow the _count_ argument of [`str.replace()`](https://docs.python.org/3/builtins/stdtypes.html#str.replace "str.replace")
     to be a keyword. (Contributed by Hugo van Kemenade in [gh-106487](https://github.com/python/cpython/issues/106487)
    .)
    
*   Many functions now emit a warning if a boolean value is passed as a file descriptor argument. This can help catch some errors earlier. (Contributed by Serhiy Storchaka in [gh-82626](https://github.com/python/cpython/issues/82626)
    .)
    
*   Added `name` and `mode` attributes for compressed and archived file-like objects in the [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
    , [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
    , [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
    , and [`zipfile`](https://docs.python.org/3/library/zipfile.html#module-zipfile "zipfile: Read and write ZIP-format archive files.")
     modules. (Contributed by Serhiy Storchaka in [gh-115961](https://github.com/python/cpython/issues/115961)
    .)
    

New Modules[¶](https://docs.python.org/3/whatsnew/3.13.html#new-modules "Link to this heading")

------------------------------------------------------------------------------------------------

*   [`dbm.sqlite3`](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm")
    : An SQLite backend for [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Interfaces to various Unix "database" formats.")
    . (Contributed by Raymond Hettinger and Erlend E. Aasland in [gh-100414](https://github.com/python/cpython/issues/100414)
    .)
    

Improved Modules[¶](https://docs.python.org/3/whatsnew/3.13.html#improved-modules "Link to this heading")

----------------------------------------------------------------------------------------------------------

### argparse[¶](https://docs.python.org/3/whatsnew/3.13.html#argparse "Link to this heading")

*   Add the _deprecated_ parameter to the [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
     and `add_parser()` methods, to enable deprecating command-line options, positional arguments, and subcommands. (Contributed by Serhiy Storchaka in [gh-83648](https://github.com/python/cpython/issues/83648)
    .)
    

### array[¶](https://docs.python.org/3/whatsnew/3.13.html#array "Link to this heading")

*   Add the `'w'` type code (`Py_UCS4`) for Unicode characters. It should be used instead of the deprecated `'u'` type code. (Contributed by Inada Naoki in [gh-80480](https://github.com/python/cpython/issues/80480)
    .)
    
*   Register [`array.array`](https://docs.python.org/3/library/array.html#array.array "array.array")
     as a [`MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence")
     by implementing the [`clear()`](https://docs.python.org/3/library/array.html#array.array.clear "array.array.clear")
     method. (Contributed by Mike Zimin in [gh-114894](https://github.com/python/cpython/issues/114894)
    .)
    

### ast[¶](https://docs.python.org/3/whatsnew/3.13.html#ast "Link to this heading")

*   The constructors of node types in the [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.")
     module are now stricter in the arguments they accept, with more intuitive behavior when arguments are omitted.
    
    If an optional field on an AST node is not included as an argument when constructing an instance, the field will now be set to `None`. Similarly, if a list field is omitted, that field will now be set to an empty list, and if an `expr_context` field is omitted, it defaults to [`Load()`](https://docs.python.org/3/library/ast.html#ast.Load "ast.Load")
    . (Previously, in all cases, the attribute would be missing on the newly constructed AST node instance.)
    
    In all other cases, where a required argument is omitted, the node constructor will emit a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
    . This will raise an exception in Python 3.15. Similarly, passing a keyword argument to the constructor that does not map to a field on the AST node is now deprecated, and will raise an exception in Python 3.15.
    
    These changes do not apply to user-defined subclasses of [`ast.AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST")
     unless the class opts in to the new behavior by defining the [`AST._field_types`](https://docs.python.org/3/library/ast.html#ast.AST._field_types "ast.AST._field_types")
     mapping.
    
    (Contributed by Jelle Zijlstra in [gh-105858](https://github.com/python/cpython/issues/105858)
    , [gh-117486](https://github.com/python/cpython/issues/117486)
    , and [gh-118851](https://github.com/python/cpython/issues/118851)
    .)
    
*   [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse")
     now accepts an optional argument _optimize_ which is passed on to [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
    . This makes it possible to obtain an optimized AST. (Contributed by Irit Katriel in [gh-108113](https://github.com/python/cpython/issues/108113)
    .)
    

### asyncio[¶](https://docs.python.org/3/whatsnew/3.13.html#asyncio "Link to this heading")

*   [`asyncio.as_completed()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.as_completed "asyncio.as_completed")
     now returns an object that is both an [asynchronous iterator](https://docs.python.org/3/glossary.html#term-asynchronous-iterator)
     and a plain [iterator](https://docs.python.org/3/glossary.html#term-iterator)
     of [awaitables](https://docs.python.org/3/glossary.html#term-awaitable)
    . The awaitables yielded by asynchronous iteration include original task or future objects that were passed in, making it easier to associate results with the tasks being completed. (Contributed by Justin Arthur in [gh-77714](https://github.com/python/cpython/issues/77714)
    .)
    
*   [`asyncio.loop.create_unix_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server")
     will now automatically remove the Unix socket when the server is closed. (Contributed by Pierre Ossman in [gh-111246](https://github.com/python/cpython/issues/111246)
    .)
    
*   [`DatagramTransport.sendto()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.DatagramTransport.sendto "asyncio.DatagramTransport.sendto")
     will now send zero-length datagrams if called with an empty bytes object. The transport flow control also now accounts for the datagram header when calculating the buffer size. (Contributed by Jamie Phan in [gh-115199](https://github.com/python/cpython/issues/115199)
    .)
    
*   Add [`Queue.shutdown`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.shutdown "asyncio.Queue.shutdown")
     and [`QueueShutDown`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueShutDown "asyncio.QueueShutDown")
     to manage queue termination. (Contributed by Laurie Opperman and Yves Duprat in [gh-104228](https://github.com/python/cpython/issues/104228)
    .)
    
*   Add the [`Server.close_clients()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.close_clients "asyncio.Server.close_clients")
     and [`Server.abort_clients()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.abort_clients "asyncio.Server.abort_clients")
     methods, which more forcefully close an asyncio server. (Contributed by Pierre Ossman in [gh-113538](https://github.com/python/cpython/issues/113538)
    .)
    
*   Accept a tuple of separators in [`StreamReader.readuntil()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader.readuntil "asyncio.StreamReader.readuntil")
    , stopping when any one of them is encountered. (Contributed by Bruce Merry in [gh-81322](https://github.com/python/cpython/issues/81322)
    .)
    
*   Improve the behavior of [`TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup")
     when an external cancellation collides with an internal cancellation. For example, when two task groups are nested and both experience an exception in a child task simultaneously, it was possible that the outer task group would hang, because its internal cancellation was swallowed by the inner task group.
    
    In the case where a task group is cancelled externally and also must raise an [`ExceptionGroup`](https://docs.python.org/3/builtins/exceptions.html#ExceptionGroup "ExceptionGroup")
    , it will now call the parent task’s [`cancel()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.cancel "asyncio.Task.cancel")
     method. This ensures that a [`CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError")
     will be raised at the next [`await`](https://docs.python.org/3/reference/expressions.html#await)
    , so the cancellation is not lost.
    
    An added benefit of these changes is that task groups now preserve the cancellation count ([`cancelling()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.cancelling "asyncio.Task.cancelling")
    ).
    
    In order to handle some corner cases, [`uncancel()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.uncancel "asyncio.Task.uncancel")
     may now reset the undocumented `_must_cancel` flag when the cancellation count reaches zero.
    
    (Inspired by an issue reported by Arthur Tacca in [gh-116720](https://github.com/python/cpython/issues/116720)
    .)
    
*   When [`TaskGroup.create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup.create_task "asyncio.TaskGroup.create_task")
     is called on an inactive [`TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup")
    , the given coroutine will be closed (which prevents a [`RuntimeWarning`](https://docs.python.org/3/builtins/exceptions.html#RuntimeWarning "RuntimeWarning")
     about the given coroutine being never awaited). (Contributed by Arthur Tacca and Jason Zhang in [gh-115957](https://github.com/python/cpython/issues/115957)
    .)
    
*   The function and methods named `create_task` have received a new `**kwargs` argument that is passed through to the task constructor. This change was accidentally added in 3.13.3, and broke the API contract for custom task factories. Several third-party task factories implemented workarounds for this. In 3.13.4 and later releases the old factory contract is honored once again (until 3.14). To keep the workarounds working, the extra `**kwargs` argument still allows passing additional keyword arguments to [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
     and to custom task factories.
    
    This affects the following function and methods: [`asyncio.create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task")
    , [`asyncio.loop.create_task()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task")
    , [`asyncio.TaskGroup.create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup.create_task "asyncio.TaskGroup.create_task")
    . (Contributed by Thomas Grainger in [gh-128307](https://github.com/python/cpython/issues/128307)
    .)
    

### base64[¶](https://docs.python.org/3/whatsnew/3.13.html#base64 "Link to this heading")

*   Add [`z85encode()`](https://docs.python.org/3/library/base64.html#base64.z85encode "base64.z85encode")
     and [`z85decode()`](https://docs.python.org/3/library/base64.html#base64.z85decode "base64.z85decode")
     functions for encoding [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     as [Z85 data](https://rfc.zeromq.org/spec/32/)
     and decoding Z85-encoded data to `bytes`. (Contributed by Matan Perelman in [gh-75299](https://github.com/python/cpython/issues/75299)
    .)
    

### compileall[¶](https://docs.python.org/3/whatsnew/3.13.html#compileall "Link to this heading")

*   The default number of worker threads and processes is now selected using [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
     instead of [`os.cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count")
    . (Contributed by Victor Stinner in [gh-109649](https://github.com/python/cpython/issues/109649)
    .)
    

### concurrent.futures[¶](https://docs.python.org/3/whatsnew/3.13.html#concurrent-futures "Link to this heading")

*   The default number of worker threads and processes is now selected using [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
     instead of [`os.cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count")
    . (Contributed by Victor Stinner in [gh-109649](https://github.com/python/cpython/issues/109649)
    .)
    

### configparser[¶](https://docs.python.org/3/whatsnew/3.13.html#configparser "Link to this heading")

*   [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
     now has support for unnamed sections, which allows for top-level key-value pairs. This can be enabled with the new _allow\_unnamed\_section_ parameter. (Contributed by Pedro Sousa Lacerda in [gh-66449](https://github.com/python/cpython/issues/66449)
    .)
    

### copy[¶](https://docs.python.org/3/whatsnew/3.13.html#copy "Link to this heading")

*   The new [`replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace")
     function and the [`replace protocol`](https://docs.python.org/3/library/copy.html#object.__replace__ "object.__replace__")
     make creating modified copies of objects much simpler. This is especially useful when working with immutable objects. The following types support the `replace()` function and implement the replace protocol:
    
    *   [`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
        
    *   [`dataclasses.dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass")
        
    *   [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
        , [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
        , [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time")
        
    *   [`inspect.Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature")
        , [`inspect.Parameter`](https://docs.python.org/3/library/inspect.html#inspect.Parameter "inspect.Parameter")
        
    *   [`types.SimpleNamespace`](https://docs.python.org/3/library/types.html#types.SimpleNamespace "types.SimpleNamespace")
        
    *   [code objects](https://docs.python.org/3/reference/datamodel.html#code-objects)
        
    
    Any user-defined class can also support [`copy.replace()`](https://docs.python.org/3/library/copy.html#copy.replace "copy.replace")
     by defining the [`__replace__()`](https://docs.python.org/3/library/copy.html#object.__replace__ "object.__replace__")
     method. (Contributed by Serhiy Storchaka in [gh-108751](https://github.com/python/cpython/issues/108751)
    .)
    

### ctypes[¶](https://docs.python.org/3/whatsnew/3.13.html#ctypes "Link to this heading")

*   As a consequence of necessary internal refactoring, initialization of internal metaclasses now happens in `__init__` rather than in `__new__`. This affects projects that subclass these internal metaclasses to provide custom initialization. Generally:
    
    *   Custom logic that was done in `__new__` after calling `super().__new__` should be moved to `__init__`.
        
    *   To create a class, call the metaclass, not only the metaclass’s `__new__` method.
        
    
    See [gh-124520](https://github.com/python/cpython/issues/124520)
     for discussion and links to changes in some affected projects.
    
*   [`ctypes.Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure")
     objects have a new [`_align_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._align_ "ctypes.Structure._align_")
     attribute which allows the alignment of the structure being packed to/from memory to be specified explicitly. (Contributed by Matt Sanderson in [gh-112433](https://github.com/python/cpython/issues/112433)
    )
    

### dbm[¶](https://docs.python.org/3/whatsnew/3.13.html#dbm "Link to this heading")

*   Add [`dbm.sqlite3`](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm")
    , a new module which implements an SQLite backend, and make it the default `dbm` backend. (Contributed by Raymond Hettinger and Erlend E. Aasland in [gh-100414](https://github.com/python/cpython/issues/100414)
    .)
    
*   Allow removing all items from the database through the new `clear()` methods of the GDBM and NDBM database objects. (Contributed by Donghee Na in [gh-107122](https://github.com/python/cpython/issues/107122)
    .)
    

### dis[¶](https://docs.python.org/3/whatsnew/3.13.html#dis "Link to this heading")

*   Change the output of [`dis`](https://docs.python.org/3/library/dis.html#module-dis "dis: Disassembler for Python bytecode.")
     module functions to show logical labels for jump targets and exception handlers, rather than offsets. The offsets can be added with the new [`-O`](https://docs.python.org/3/library/dis.html#cmdoption-dis-O)
     command-line option or the _show\_offsets_ argument. (Contributed by Irit Katriel in [gh-112137](https://github.com/python/cpython/issues/112137)
    .)
    
*   [`get_instructions()`](https://docs.python.org/3/library/dis.html#dis.get_instructions "dis.get_instructions")
     no longer represents cache entries as separate instructions. Instead, it returns them as part of the [`Instruction`](https://docs.python.org/3/library/dis.html#dis.Instruction "dis.Instruction")
    , in the new _cache\_info_ field. The _show\_caches_ argument to `get_instructions()` is deprecated and no longer has any effect. (Contributed by Irit Katriel in [gh-112962](https://github.com/python/cpython/issues/112962)
    .)
    

### doctest[¶](https://docs.python.org/3/whatsnew/3.13.html#doctest "Link to this heading")

*   [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.")
     output is now colored by default. This can be controlled via the new [`PYTHON_COLORS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_COLORS)
     environment variable as well as the canonical [`NO_COLOR`](https://no-color.org/)
     and [`FORCE_COLOR`](https://force-color.org/)
     environment variables. See also [Controlling color](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Hugo van Kemenade in [gh-117225](https://github.com/python/cpython/issues/117225)
    .)
    
*   The [`DocTestRunner.run()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.run "doctest.DocTestRunner.run")
     method now counts the number of skipped tests. Add the [`DocTestRunner.skips`](https://docs.python.org/3/library/doctest.html#doctest.DocTestRunner.skips "doctest.DocTestRunner.skips")
     and [`TestResults.skipped`](https://docs.python.org/3/library/doctest.html#doctest.TestResults.skipped "doctest.TestResults.skipped")
     attributes. (Contributed by Victor Stinner in [gh-108794](https://github.com/python/cpython/issues/108794)
    .)
    

### email[¶](https://docs.python.org/3/whatsnew/3.13.html#email "Link to this heading")

*   Headers with embedded newlines are now quoted on output. The [`generator`](https://docs.python.org/3/library/email.generator.html#module-email.generator "email.generator: Generate flat text email messages from a message structure.")
     will now refuse to serialize (write) headers that are improperly folded or delimited, such that they would be parsed as multiple headers or joined with adjacent data. If you need to turn this safety feature off, set [`verify_generated_headers`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.verify_generated_headers "email.policy.Policy.verify_generated_headers")
    . (Contributed by Bas Bloemsaat and Petr Viktorin in [gh-121650](https://github.com/python/cpython/issues/121650)
    .)
    
*   [`getaddresses()`](https://docs.python.org/3/library/email.utils.html#email.utils.getaddresses "email.utils.getaddresses")
     and [`parseaddr()`](https://docs.python.org/3/library/email.utils.html#email.utils.parseaddr "email.utils.parseaddr")
     now return `('', '')` pairs in more situations where invalid email addresses are encountered instead of potentially inaccurate values. The two functions have a new optional _strict_ parameter (default `True`). To get the old behavior (accepting malformed input), use `strict=False`. `getattr(email.utils, 'supports_strict_parsing', False)` can be used to check if the _strict_ parameter is available. (Contributed by Thomas Dwyer and Victor Stinner for [gh-102988](https://github.com/python/cpython/issues/102988)
     to improve the [**CVE 2023-27043**](https://www.cve.org/CVERecord?id=CVE-2023-27043)
     fix.)
    

### enum[¶](https://docs.python.org/3/whatsnew/3.13.html#enum "Link to this heading")

*   [`EnumDict`](https://docs.python.org/3/library/enum.html#enum.EnumDict "enum.EnumDict")
     has been made public to better support subclassing [`EnumType`](https://docs.python.org/3/library/enum.html#enum.EnumType "enum.EnumType")
    .
    

### fractions[¶](https://docs.python.org/3/whatsnew/3.13.html#fractions "Link to this heading")

*   [`Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction")
     objects now support the standard [format specification mini-language](https://docs.python.org/3/library/string.html#formatspec)
     rules for fill, alignment, sign handling, minimum width, and grouping. (Contributed by Mark Dickinson in [gh-111320](https://github.com/python/cpython/issues/111320)
    .)
    

### glob[¶](https://docs.python.org/3/whatsnew/3.13.html#glob "Link to this heading")

*   Add [`translate()`](https://docs.python.org/3/library/glob.html#glob.translate "glob.translate")
    , a function to convert a path specification with shell-style wildcards to a regular expression. (Contributed by Barney Gale in [gh-72904](https://github.com/python/cpython/issues/72904)
    .)
    

### importlib[¶](https://docs.python.org/3/whatsnew/3.13.html#importlib "Link to this heading")

*   The following functions in [`importlib.resources`](https://docs.python.org/3/library/importlib.resources.html#module-importlib.resources "importlib.resources: Package resource reading, opening, and access")
     now allow accessing a directory (or tree) of resources, using multiple positional arguments (the _encoding_ and _errors_ arguments in the text-reading functions are now keyword-only):
    
    *   [`is_resource()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.is_resource "importlib.resources.is_resource")
        
    *   [`open_binary()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.open_binary "importlib.resources.open_binary")
        
    *   [`open_text()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.open_text "importlib.resources.open_text")
        
    *   [`path()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.path "importlib.resources.path")
        
    *   [`read_binary()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.read_binary "importlib.resources.read_binary")
        
    *   [`read_text()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.read_text "importlib.resources.read_text")
        
    
    These functions are no longer deprecated and are not scheduled for removal. (Contributed by Petr Viktorin in [gh-116608](https://github.com/python/cpython/issues/116608)
    .)
    
*   [`contents()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.contents "importlib.resources.contents")
     remains deprecated in favor of the fully-featured [`Traversable`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable")
     API. However, there is now no plan to remove it. (Contributed by Petr Viktorin in [gh-116608](https://github.com/python/cpython/issues/116608)
    .)
    

### io[¶](https://docs.python.org/3/whatsnew/3.13.html#io "Link to this heading")

*   The [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase")
     finalizer now logs any errors raised by the [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close")
     method with [`sys.unraisablehook`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook")
    . Previously, errors were ignored silently by default, and only logged in [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
     or when using a [Python debug build](https://docs.python.org/3/using/configure.html#debug-build)
    . (Contributed by Victor Stinner in [gh-62948](https://github.com/python/cpython/issues/62948)
    .)
    

### ipaddress[¶](https://docs.python.org/3/whatsnew/3.13.html#ipaddress "Link to this heading")

*   Add the [`IPv4Address.ipv6_mapped`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.ipv6_mapped "ipaddress.IPv4Address.ipv6_mapped")
     property, which returns the IPv4-mapped IPv6 address. (Contributed by Charles Machalow in [gh-109466](https://github.com/python/cpython/issues/109466)
    .)
    
*   Fix `is_global` and `is_private` behavior in [`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address")
    , [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address")
    , [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network")
    , and [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network")
    . (Contributed by Jakub Stasiak in [gh-113171](https://github.com/python/cpython/issues/113171)
    .)
    

### itertools[¶](https://docs.python.org/3/whatsnew/3.13.html#itertools "Link to this heading")

*   [`batched()`](https://docs.python.org/3/library/itertools.html#itertools.batched "itertools.batched")
     has a new _strict_ parameter, which raises a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     if the final batch is shorter than the specified batch size. (Contributed by Raymond Hettinger in [gh-113202](https://github.com/python/cpython/issues/113202)
    .)
    

### marshal[¶](https://docs.python.org/3/whatsnew/3.13.html#marshal "Link to this heading")

*   Add the _allow\_code_ parameter in module functions. Passing `allow_code=False` prevents serialization and de-serialization of code objects which are incompatible between Python versions. (Contributed by Serhiy Storchaka in [gh-113626](https://github.com/python/cpython/issues/113626)
    .)
    

### math[¶](https://docs.python.org/3/whatsnew/3.13.html#math "Link to this heading")

*   The new function [`fma()`](https://docs.python.org/3/library/math.html#math.fma "math.fma")
     performs fused multiply-add operations. This computes `x * y + z` with only a single round, and so avoids any intermediate loss of precision. It wraps the `fma()` function provided by C99, and follows the specification of the IEEE 754 “fusedMultiplyAdd” operation for special cases. (Contributed by Mark Dickinson and Victor Stinner in [gh-73468](https://github.com/python/cpython/issues/73468)
    .)
    

### mimetypes[¶](https://docs.python.org/3/whatsnew/3.13.html#mimetypes "Link to this heading")

*   Add the [`guess_file_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_file_type "mimetypes.guess_file_type")
     function to guess a MIME type from a filesystem path. Using paths with [`guess_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type")
     is now [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
    . (Contributed by Serhiy Storchaka in [gh-66543](https://github.com/python/cpython/issues/66543)
    .)
    

### mmap[¶](https://docs.python.org/3/whatsnew/3.13.html#mmap "Link to this heading")

*   [`mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap")
     is now protected from crashing on Windows when the mapped memory is inaccessible due to file system errors or access violations. (Contributed by Jannis Weigend in [gh-118209](https://github.com/python/cpython/issues/118209)
    .)
    
*   [`mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap")
     has a new [`seekable()`](https://docs.python.org/3/library/mmap.html#mmap.mmap.seekable "mmap.mmap.seekable")
     method that can be used when a seekable file-like object is required. The [`seek()`](https://docs.python.org/3/library/mmap.html#mmap.mmap.seek "mmap.mmap.seek")
     method now returns the new absolute position. (Contributed by Donghee Na and Sylvie Liberman in [gh-111835](https://github.com/python/cpython/issues/111835)
    .)
    
*   The new UNIX-only _trackfd_ parameter for [`mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap")
     controls file descriptor duplication; if false, the file descriptor specified by _fileno_ will not be duplicated. (Contributed by Zackery Spytz and Petr Viktorin in [gh-78502](https://github.com/python/cpython/issues/78502)
    .)
    

### multiprocessing[¶](https://docs.python.org/3/whatsnew/3.13.html#multiprocessing "Link to this heading")

*   The default number of worker threads and processes is now selected using [`os.process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
     instead of [`os.cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count")
    . (Contributed by Victor Stinner in [gh-109649](https://github.com/python/cpython/issues/109649)
    .)
    

### os[¶](https://docs.python.org/3/whatsnew/3.13.html#os "Link to this heading")

*   Add [`process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
     function to get the number of logical CPU cores usable by the calling thread of the current process. (Contributed by Victor Stinner in [gh-109649](https://github.com/python/cpython/issues/109649)
    .)
    
*   [`cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count")
     and [`process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
     can be overridden through the new environment variable [`PYTHON_CPU_COUNT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT)
     or the new command-line option [`-X cpu_count`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
    . This option is useful for users who need to limit CPU resources of a container system without having to modify application code or the container itself. (Contributed by Donghee Na in [gh-109595](https://github.com/python/cpython/issues/109595)
    .)
    
*   Add a [low level interface](https://docs.python.org/3/library/os.html#os-timerfd)
     to Linux’s _[timer file descriptors](https://manpages.debian.org/timerfd_create(2))
    _ via [`timerfd_create()`](https://docs.python.org/3/library/os.html#os.timerfd_create "os.timerfd_create")
    , [`timerfd_settime()`](https://docs.python.org/3/library/os.html#os.timerfd_settime "os.timerfd_settime")
    , [`timerfd_settime_ns()`](https://docs.python.org/3/library/os.html#os.timerfd_settime_ns "os.timerfd_settime_ns")
    , [`timerfd_gettime()`](https://docs.python.org/3/library/os.html#os.timerfd_gettime "os.timerfd_gettime")
    , [`timerfd_gettime_ns()`](https://docs.python.org/3/library/os.html#os.timerfd_gettime_ns "os.timerfd_gettime_ns")
    , [`TFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "os.TFD_NONBLOCK")
    , [`TFD_CLOEXEC`](https://docs.python.org/3/library/os.html#os.TFD_CLOEXEC "os.TFD_CLOEXEC")
    , [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME")
    , and [`TFD_TIMER_CANCEL_ON_SET`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_CANCEL_ON_SET "os.TFD_TIMER_CANCEL_ON_SET")
     (Contributed by Masaru Tsuchiyama in [gh-108277](https://github.com/python/cpython/issues/108277)
    .)
    
*   [`lchmod()`](https://docs.python.org/3/library/os.html#os.lchmod "os.lchmod")
     and the _follow\_symlinks_ argument of [`chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")
     are both now available on Windows. Note that the default value of _follow\_symlinks_ in `lchmod()` is `False` on Windows. (Contributed by Serhiy Storchaka in [gh-59616](https://github.com/python/cpython/issues/59616)
    .)
    
*   [`fchmod()`](https://docs.python.org/3/library/os.html#os.fchmod "os.fchmod")
     and support for file descriptors in [`chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")
     are both now available on Windows. (Contributed by Serhiy Storchaka in [gh-113191](https://github.com/python/cpython/issues/113191)
    .)
    
*   On Windows, [`mkdir()`](https://docs.python.org/3/library/os.html#os.mkdir "os.mkdir")
     and [`makedirs()`](https://docs.python.org/3/library/os.html#os.makedirs "os.makedirs")
     now support passing a _mode_ value of `0o700` to apply access control to the new directory. This implicitly affects [`tempfile.mkdtemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp")
     and is a mitigation for [**CVE 2024-4030**](https://www.cve.org/CVERecord?id=CVE-2024-4030)
    . Other values for _mode_ continue to be ignored. (Contributed by Steve Dower in [gh-118486](https://github.com/python/cpython/issues/118486)
    .)
    
*   [`posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn")
     now accepts `None` for the _env_ argument, which makes the newly spawned process use the current process environment. (Contributed by Jakub Kulik in [gh-113119](https://github.com/python/cpython/issues/113119)
    .)
    
*   [`posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn")
     can now use the [`POSIX_SPAWN_CLOSEFROM`](https://docs.python.org/3/library/os.html#os.POSIX_SPAWN_CLOSEFROM "os.POSIX_SPAWN_CLOSEFROM")
     attribute in the _file\_actions_ parameter on platforms that support `posix_spawn_file_actions_addclosefrom_np()`. (Contributed by Jakub Kulik in [gh-113117](https://github.com/python/cpython/issues/113117)
    .)
    

### os.path[¶](https://docs.python.org/3/whatsnew/3.13.html#os-path "Link to this heading")

*   Add [`isreserved()`](https://docs.python.org/3/library/os.path.html#os.path.isreserved "os.path.isreserved")
     to check if a path is reserved on the current system. This function is only available on Windows. (Contributed by Barney Gale in [gh-88569](https://github.com/python/cpython/issues/88569)
    .)
    
*   On Windows, [`isabs()`](https://docs.python.org/3/library/os.path.html#os.path.isabs "os.path.isabs")
     no longer considers paths starting with exactly one slash (`\` or `/`) to be absolute. (Contributed by Barney Gale and Jon Foster in [gh-44626](https://github.com/python/cpython/issues/44626)
    .)
    
*   [`realpath()`](https://docs.python.org/3/library/os.path.html#os.path.realpath "os.path.realpath")
     now resolves MS-DOS style file names even if the file is not accessible. (Contributed by Moonsik Park in [gh-82367](https://github.com/python/cpython/issues/82367)
    .)
    

### pathlib[¶](https://docs.python.org/3/whatsnew/3.13.html#pathlib "Link to this heading")

*   Add [`UnsupportedOperation`](https://docs.python.org/3/library/pathlib.html#pathlib.UnsupportedOperation "pathlib.UnsupportedOperation")
    , which is raised instead of [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
     when a path operation isn’t supported. (Contributed by Barney Gale in [gh-89812](https://github.com/python/cpython/issues/89812)
    .)
    
*   Add a new constructor for creating [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
     objects from ‘file’ URIs (`file:///`), [`Path.from_uri()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.from_uri "pathlib.Path.from_uri")
    . (Contributed by Barney Gale in [gh-107465](https://github.com/python/cpython/issues/107465)
    .)
    
*   Add [`PurePath.full_match()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.full_match "pathlib.PurePath.full_match")
     for matching paths with shell-style wildcards, including the recursive wildcard “`**`”. (Contributed by Barney Gale in [gh-73435](https://github.com/python/cpython/issues/73435)
    .)
    
*   Add the [`PurePath.parser`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parser "pathlib.PurePath.parser")
     class attribute to store the implementation of [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
     used for low-level path parsing and joining. This will be either `posixpath` or `ntpath`.
    
*   Add _recurse\_symlinks_ keyword-only argument to [`Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob")
     and [`rglob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob "pathlib.Path.rglob")
    . (Contributed by Barney Gale in [gh-77609](https://github.com/python/cpython/issues/77609)
    .)
    
*   [`Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob")
     and [`rglob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob "pathlib.Path.rglob")
     now return files and directories when given a pattern that ends with “`**`”. Previously, only directories were returned. (Contributed by Barney Gale in [gh-70303](https://github.com/python/cpython/issues/70303)
    .)
    
*   Add the _follow\_symlinks_ keyword-only argument to [`Path.is_file`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_file "pathlib.Path.is_file")
    , [`Path.is_dir`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir "pathlib.Path.is_dir")
    , [`Path.owner()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.owner "pathlib.Path.owner")
    , and [`Path.group()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.group "pathlib.Path.group")
    . (Contributed by Barney Gale in [gh-105793](https://github.com/python/cpython/issues/105793)
     and Kamil Turek in [gh-107962](https://github.com/python/cpython/issues/107962)
    .)
    

### pdb[¶](https://docs.python.org/3/whatsnew/3.13.html#pdb "Link to this heading")

*   [`breakpoint()`](https://docs.python.org/3/builtins/functions.html#breakpoint "breakpoint")
     and [`set_trace()`](https://docs.python.org/3/library/pdb.html#pdb.set_trace "pdb.set_trace")
     now enter the debugger immediately rather than on the next line of code to be executed. This change prevents the debugger from breaking outside of the context when `breakpoint()` is positioned at the end of the context. (Contributed by Tian Gao in [gh-118579](https://github.com/python/cpython/issues/118579)
    .)
    
*   `sys.path[0]` is no longer replaced by the directory of the script being debugged when [`sys.flags.safe_path`](https://docs.python.org/3/library/sys.html#sys.flags.safe_path "sys.flags.safe_path")
     is set. (Contributed by Tian Gao and Christian Walther in [gh-111762](https://github.com/python/cpython/issues/111762)
    .)
    
*   [`zipapp`](https://docs.python.org/3/library/zipapp.html#module-zipapp "zipapp: Manage executable Python zip archives")
     is now supported as a debugging target. (Contributed by Tian Gao in [gh-118501](https://github.com/python/cpython/issues/118501)
    .)
    
*   Add ability to move between chained exceptions during post-mortem debugging in [`pm()`](https://docs.python.org/3/library/pdb.html#pdb.pm "pdb.pm")
     using the new [`exceptions [exc_number]`](https://docs.python.org/3/library/pdb.html#pdbcommand-exceptions)
     command for Pdb. (Contributed by Matthias Bussonnier in [gh-106676](https://github.com/python/cpython/issues/106676)
    .)
    
*   Expressions and statements whose prefix is a pdb command are now correctly identified and executed. (Contributed by Tian Gao in [gh-108464](https://github.com/python/cpython/issues/108464)
    .)
    

### queue[¶](https://docs.python.org/3/whatsnew/3.13.html#queue "Link to this heading")

*   Add [`Queue.shutdown`](https://docs.python.org/3/library/queue.html#queue.Queue.shutdown "queue.Queue.shutdown")
     and [`ShutDown`](https://docs.python.org/3/library/queue.html#queue.ShutDown "queue.ShutDown")
     to manage queue termination. (Contributed by Laurie Opperman and Yves Duprat in [gh-104750](https://github.com/python/cpython/issues/104750)
    .)
    

### random[¶](https://docs.python.org/3/whatsnew/3.13.html#random "Link to this heading")

*   Add a [command-line interface](https://docs.python.org/3/library/random.html#random-cli)
    . (Contributed by Hugo van Kemenade in [gh-118131](https://github.com/python/cpython/issues/118131)
    .)
    

### re[¶](https://docs.python.org/3/whatsnew/3.13.html#re "Link to this heading")

*   Rename `re.error` to [`PatternError`](https://docs.python.org/3/library/re.html#re.PatternError "re.PatternError")
     for improved clarity. `re.error` is kept for backward compatibility.
    

### shutil[¶](https://docs.python.org/3/whatsnew/3.13.html#shutil "Link to this heading")

*   Support the _dir\_fd_ and _follow\_symlinks_ keyword arguments in [`chown()`](https://docs.python.org/3/library/shutil.html#shutil.chown "shutil.chown")
    . (Contributed by Berker Peksag and Tahia K in [gh-62308](https://github.com/python/cpython/issues/62308)
    )
    

### site[¶](https://docs.python.org/3/whatsnew/3.13.html#site "Link to this heading")

*   `.pth` files are now decoded using UTF-8 first, and then with the [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding)
     if UTF-8 decoding fails. (Contributed by Inada Naoki in [gh-117802](https://github.com/python/cpython/issues/117802)
    .)
    

### sqlite3[¶](https://docs.python.org/3/whatsnew/3.13.html#sqlite3 "Link to this heading")

*   A [`ResourceWarning`](https://docs.python.org/3/builtins/exceptions.html#ResourceWarning "ResourceWarning")
     is now emitted if a [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection")
     object is not [`closed`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.close "sqlite3.Connection.close")
     explicitly. (Contributed by Erlend E. Aasland in [gh-105539](https://github.com/python/cpython/issues/105539)
    .)
    
*   Add the _filter_ keyword-only parameter to [`Connection.iterdump()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.iterdump "sqlite3.Connection.iterdump")
     for filtering database objects to dump. (Contributed by Mariusz Felisiak in [gh-91602](https://github.com/python/cpython/issues/91602)
    .)
    

### ssl[¶](https://docs.python.org/3/whatsnew/3.13.html#ssl "Link to this heading")

*   The [`create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context")
     API now includes [`VERIFY_X509_PARTIAL_CHAIN`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN "ssl.VERIFY_X509_PARTIAL_CHAIN")
     and [`VERIFY_X509_STRICT`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_STRICT "ssl.VERIFY_X509_STRICT")
     in its default flags.
    
    Note
    
    [`VERIFY_X509_STRICT`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_STRICT "ssl.VERIFY_X509_STRICT")
     may reject pre-[**RFC 5280**](https://datatracker.ietf.org/doc/html/rfc5280.html)
     or malformed certificates that the underlying OpenSSL implementation might otherwise accept. Whilst disabling this is not recommended, you can do so using:
    
    Copy
    
    import ssl
    
    ctx \= ssl.create\_default\_context()
    ctx.verify\_flags &= ~ssl.VERIFY\_X509\_STRICT
    
    (Contributed by William Woodruff in [gh-112389](https://github.com/python/cpython/issues/112389)
    .)
    

### statistics[¶](https://docs.python.org/3/whatsnew/3.13.html#statistics "Link to this heading")

*   Add [`kde()`](https://docs.python.org/3/library/statistics.html#statistics.kde "statistics.kde")
     for kernel density estimation. This makes it possible to estimate a continuous probability density function from a fixed number of discrete samples. (Contributed by Raymond Hettinger in [gh-115863](https://github.com/python/cpython/issues/115863)
    .)
    
*   Add [`kde_random()`](https://docs.python.org/3/library/statistics.html#statistics.kde_random "statistics.kde_random")
     for sampling from an estimated probability density function created by [`kde()`](https://docs.python.org/3/library/statistics.html#statistics.kde "statistics.kde")
    . (Contributed by Raymond Hettinger in [gh-115863](https://github.com/python/cpython/issues/115863)
    .)
    

### subprocess[¶](https://docs.python.org/3/whatsnew/3.13.html#subprocess "Link to this heading")

*   The [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
     module now uses the [`posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn")
     function in more situations.
    
    Notably, when _close\_fds_ is `True` (the default), [`posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn")
     will be used when the C library provides `posix_spawn_file_actions_addclosefrom_np()`, which includes recent versions of Linux, FreeBSD, and Solaris. On Linux, this should perform similarly to the existing Linux `vfork()` based code.
    
    A private control knob `subprocess._USE_POSIX_SPAWN` can be set to `False` if you need to force [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
     to never use [`posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn")
    . Please report your reason and platform details in the [issue tracker](https://docs.python.org/3/bugs.html#using-the-tracker)
     if you set this so that we can improve our API selection logic for everyone. (Contributed by Jakub Kulik in [gh-113117](https://github.com/python/cpython/issues/113117)
    .)
    

### sys[¶](https://docs.python.org/3/whatsnew/3.13.html#sys "Link to this heading")

*   Add the [`_is_interned()`](https://docs.python.org/3/library/sys.html#sys._is_interned "sys._is_interned")
     function to test if a string was interned. This function is not guaranteed to exist in all implementations of Python. (Contributed by Serhiy Storchaka in [gh-78573](https://github.com/python/cpython/issues/78573)
    .)
    

### tempfile[¶](https://docs.python.org/3/whatsnew/3.13.html#tempfile "Link to this heading")

*   On Windows, the default mode `0o700` used by [`tempfile.mkdtemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp")
     now limits access to the new directory due to changes to [`os.mkdir()`](https://docs.python.org/3/library/os.html#os.mkdir "os.mkdir")
    . This is a mitigation for [**CVE 2024-4030**](https://www.cve.org/CVERecord?id=CVE-2024-4030)
    . (Contributed by Steve Dower in [gh-118486](https://github.com/python/cpython/issues/118486)
    .)
    

### time[¶](https://docs.python.org/3/whatsnew/3.13.html#time "Link to this heading")

*   On Windows, [`monotonic()`](https://docs.python.org/3/library/time.html#time.monotonic "time.monotonic")
     now uses the `QueryPerformanceCounter()` clock for a resolution of 1 microsecond, instead of the `GetTickCount64()` clock which has a resolution of 15.6 milliseconds. (Contributed by Victor Stinner in [gh-88494](https://github.com/python/cpython/issues/88494)
    .)
    
*   On Windows, [`time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
     now uses the `GetSystemTimePreciseAsFileTime()` clock for a resolution of 1 microsecond, instead of the `GetSystemTimeAsFileTime()` clock which has a resolution of 15.6 milliseconds. (Contributed by Victor Stinner in [gh-63207](https://github.com/python/cpython/issues/63207)
    .)
    

### tkinter[¶](https://docs.python.org/3/whatsnew/3.13.html#tkinter "Link to this heading")

*   Add [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
     widget methods: `tk_busy_hold()`, `tk_busy_configure()`, `tk_busy_cget()`, `tk_busy_forget()`, `tk_busy_current()`, and `tk_busy_status()`. (Contributed by Miguel, klappnase and Serhiy Storchaka in [gh-72684](https://github.com/python/cpython/issues/72684)
    .)
    
*   The [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
     widget method `wm_attributes()` now accepts the attribute name without the minus prefix to get window attributes, for example `w.wm_attributes('alpha')` and allows specifying attributes and values to set as keyword arguments, for example `w.wm_attributes(alpha=0.5)`. (Contributed by Serhiy Storchaka in [gh-43457](https://github.com/python/cpython/issues/43457)
    .)
    
*   `wm_attributes()` can now return attributes as a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
    , by using the new optional keyword-only parameter _return\_python\_dict_. (Contributed by Serhiy Storchaka in [gh-43457](https://github.com/python/cpython/issues/43457)
    .)
    
*   `Text.count()` can now return a simple [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
     when the new optional keyword-only parameter _return\_ints_ is used. Otherwise, the single count is returned as a 1-tuple or `None`. (Contributed by Serhiy Storchaka in [gh-97928](https://github.com/python/cpython/issues/97928)
    .)
    
*   Support the “vsapi” element type in the [`element_create()`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style.element_create "tkinter.ttk.Style.element_create")
     method of [`tkinter.ttk.Style`](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style "tkinter.ttk.Style")
    . (Contributed by Serhiy Storchaka in [gh-68166](https://github.com/python/cpython/issues/68166)
    .)
    
*   Add the `after_info()` method for Tkinter widgets. (Contributed by Cheryl Sabella in [gh-77020](https://github.com/python/cpython/issues/77020)
    .)
    
*   Add a new `copy_replace()` method to `PhotoImage` to copy a region from one image to another, possibly with pixel zooming, subsampling, or both. (Contributed by Serhiy Storchaka in [gh-118225](https://github.com/python/cpython/issues/118225)
    .)
    
*   Add _from\_coords_ parameter to the `PhotoImage` methods `copy()`, `zoom()` and `subsample()`. Add _zoom_ and _subsample_ parameters to the `PhotoImage` method `copy()`. (Contributed by Serhiy Storchaka in [gh-118225](https://github.com/python/cpython/issues/118225)
    .)
    
*   Add the `PhotoImage` methods `read()` to read an image from a file and `data()` to get the image data. Add _background_ and _grayscale_ parameters to the `write()` method. (Contributed by Serhiy Storchaka in [gh-118271](https://github.com/python/cpython/issues/118271)
    .)
    

### traceback[¶](https://docs.python.org/3/whatsnew/3.13.html#traceback "Link to this heading")

*   Add the [`exc_type_str`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.exc_type_str "traceback.TracebackException.exc_type_str")
     attribute to [`TracebackException`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException "traceback.TracebackException")
    , which holds a string display of the _exc\_type_. Deprecate the [`exc_type`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.exc_type "traceback.TracebackException.exc_type")
     attribute, which holds the type object itself. Add parameter _save\_exc\_type_ (default `True`) to indicate whether `exc_type` should be saved. (Contributed by Irit Katriel in [gh-112332](https://github.com/python/cpython/issues/112332)
    .)
    
*   Add a new _show\_group_ keyword-only parameter to [`TracebackException.format_exception_only()`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.format_exception_only "traceback.TracebackException.format_exception_only")
     to (recursively) format the nested exceptions of a [`BaseExceptionGroup`](https://docs.python.org/3/builtins/exceptions.html#BaseExceptionGroup "BaseExceptionGroup")
     instance. (Contributed by Irit Katriel in [gh-105292](https://github.com/python/cpython/issues/105292)
    .)
    

### types[¶](https://docs.python.org/3/whatsnew/3.13.html#types "Link to this heading")

*   [`SimpleNamespace`](https://docs.python.org/3/library/types.html#types.SimpleNamespace "types.SimpleNamespace")
     can now take a single positional argument to initialise the namespace’s arguments. This argument must either be a mapping or an iterable of key-value pairs. (Contributed by Serhiy Storchaka in [gh-108191](https://github.com/python/cpython/issues/108191)
    .)
    

### typing[¶](https://docs.python.org/3/whatsnew/3.13.html#typing "Link to this heading")

*   [**PEP 705**](https://peps.python.org/pep-0705/)
    : Add [`ReadOnly`](https://docs.python.org/3/library/typing.html#typing.ReadOnly "typing.ReadOnly")
    , a special typing construct to mark a [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict")
     item as read-only for type checkers.
    
*   [**PEP 742**](https://peps.python.org/pep-0742/)
    : Add [`TypeIs`](https://docs.python.org/3/library/typing.html#typing.TypeIs "typing.TypeIs")
    , a typing construct that can be used to instruct a type checker how to narrow a type.
    
*   Add [`NoDefault`](https://docs.python.org/3/library/typing.html#typing.NoDefault "typing.NoDefault")
    , a sentinel object used to represent the defaults of some parameters in the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
     module. (Contributed by Jelle Zijlstra in [gh-116126](https://github.com/python/cpython/issues/116126)
    .)
    
*   Add [`get_protocol_members()`](https://docs.python.org/3/library/typing.html#typing.get_protocol_members "typing.get_protocol_members")
     to return the set of members defining a [`typing.Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "typing.Protocol")
    . (Contributed by Jelle Zijlstra in [gh-104873](https://github.com/python/cpython/issues/104873)
    .)
    
*   Add [`is_protocol()`](https://docs.python.org/3/library/typing.html#typing.is_protocol "typing.is_protocol")
     to check whether a class is a [`Protocol`](https://docs.python.org/3/library/typing.html#typing.Protocol "typing.Protocol")
    . (Contributed by Jelle Zijlstra in [gh-104873](https://github.com/python/cpython/issues/104873)
    .)
    
*   [`ClassVar`](https://docs.python.org/3/library/typing.html#typing.ClassVar "typing.ClassVar")
     can now be nested in [`Final`](https://docs.python.org/3/library/typing.html#typing.Final "typing.Final")
    , and vice versa. (Contributed by Mehdi Drissi in [gh-89547](https://github.com/python/cpython/issues/89547)
    .)
    

### unicodedata[¶](https://docs.python.org/3/whatsnew/3.13.html#unicodedata "Link to this heading")

*   Update the Unicode database to [version 15.1.0](https://www.unicode.org/versions/Unicode15.1.0/)
    . (Contributed by James Gerity in [gh-109559](https://github.com/python/cpython/issues/109559)
    .)
    

### venv[¶](https://docs.python.org/3/whatsnew/3.13.html#venv "Link to this heading")

*   Add support for creating source control management (SCM) ignore files in a virtual environment’s directory. By default, Git is supported. This is implemented as opt-in via the API, which can be extended to support other SCMs ([`EnvBuilder`](https://docs.python.org/3/library/venv.html#venv.EnvBuilder "venv.EnvBuilder")
     and [`create()`](https://docs.python.org/3/library/venv.html#venv.create "venv.create")
    ), and opt-out via the CLI, using `--without-scm-ignore-files`. (Contributed by Brett Cannon in [gh-108125](https://github.com/python/cpython/issues/108125)
    .)
    

### warnings[¶](https://docs.python.org/3/whatsnew/3.13.html#warnings "Link to this heading")

*   [**PEP 702**](https://peps.python.org/pep-0702/)
    : The new [`warnings.deprecated()`](https://docs.python.org/3/library/warnings.html#warnings.deprecated "warnings.deprecated")
     decorator provides a way to communicate deprecations to a [static type checker](https://docs.python.org/3/glossary.html#term-static-type-checker)
     and to warn on usage of deprecated classes and functions. A [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
     may also be emitted when a decorated function or class is used at runtime. (Contributed by Jelle Zijlstra in [gh-104003](https://github.com/python/cpython/issues/104003)
    .)
    

### xml[¶](https://docs.python.org/3/whatsnew/3.13.html#xml "Link to this heading")

*   Allow controlling Expat >=2.6.0 reparse deferral ([**CVE 2023-52425**](https://www.cve.org/CVERecord?id=CVE-2023-52425)
    ) by adding five new methods:
    
    *   [`xml.etree.ElementTree.XMLParser.flush()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLParser.flush "xml.etree.ElementTree.XMLParser.flush")
        
    *   [`xml.etree.ElementTree.XMLPullParser.flush()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.XMLPullParser.flush "xml.etree.ElementTree.XMLPullParser.flush")
        
    *   [`xml.parsers.expat.xmlparser.GetReparseDeferralEnabled()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.GetReparseDeferralEnabled "xml.parsers.expat.xmlparser.GetReparseDeferralEnabled")
        
    *   [`xml.parsers.expat.xmlparser.SetReparseDeferralEnabled()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetReparseDeferralEnabled "xml.parsers.expat.xmlparser.SetReparseDeferralEnabled")
        
    *   `xml.sax.expatreader.ExpatParser.flush()`
        
    
    (Contributed by Sebastian Pipping in [gh-115623](https://github.com/python/cpython/issues/115623)
    .)
    
*   Add the `close()` method for the iterator returned by [`iterparse()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse "xml.etree.ElementTree.iterparse")
     for explicit cleanup. (Contributed by Serhiy Storchaka in [gh-69893](https://github.com/python/cpython/issues/69893)
    .)
    

### zipimport[¶](https://docs.python.org/3/whatsnew/3.13.html#zipimport "Link to this heading")

*   Add support for [ZIP64](https://en.wikipedia.org/wiki/Zip_(file_format)#ZIP64)
     format files. Everybody loves huge data, right? (Contributed by Tim Hatch in [gh-94146](https://github.com/python/cpython/issues/94146)
    .)
    

Optimizations[¶](https://docs.python.org/3/whatsnew/3.13.html#optimizations "Link to this heading")

----------------------------------------------------------------------------------------------------

*   Several standard library modules have had their import times significantly improved. For example, the import time of the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
     module has been reduced by around a third by removing dependencies on [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
     and [`contextlib`](https://docs.python.org/3/library/contextlib.html#module-contextlib "contextlib: Utilities for with-statement contexts.")
    . Other modules to enjoy import-time speedups include [`email.utils`](https://docs.python.org/3/library/email.utils.html#module-email.utils "email.utils: Miscellaneous email package utilities.")
    , [`enum`](https://docs.python.org/3/library/enum.html#module-enum "enum: Implementation of an enumeration class.")
    , [`functools`](https://docs.python.org/3/library/functools.html#module-functools "functools: Higher-order functions and operations on callable objects.")
    , [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html#module-importlib.metadata "importlib.metadata: Accessing package metadata")
    , and [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
    . (Contributed by Alex Waygood, Shantanu Jain, Adam Turner, Daniel Hollas, and others in [gh-109653](https://github.com/python/cpython/issues/109653)
    .)
    
*   [`textwrap.indent()`](https://docs.python.org/3/library/textwrap.html#textwrap.indent "textwrap.indent")
     is now around 30% faster than before for large input. (Contributed by Inada Naoki in [gh-107369](https://github.com/python/cpython/issues/107369)
    .)
    
*   The [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
     module now uses the [`posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn")
     function in more situations, including when _close\_fds_ is `True` (the default) on many modern platforms. This should provide a notable performance increase when launching processes on FreeBSD and Solaris. See the [subprocess](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-subprocess)
     section above for details. (Contributed by Jakub Kulik in [gh-113117](https://github.com/python/cpython/issues/113117)
    .)
    

Removed Modules And APIs[¶](https://docs.python.org/3/whatsnew/3.13.html#removed-modules-and-apis "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

### PEP 594: Remove “dead batteries” from the standard library[¶](https://docs.python.org/3/whatsnew/3.13.html#pep-594-remove-dead-batteries-from-the-standard-library "Link to this heading")

[**PEP 594**](https://peps.python.org/pep-0594/)
 proposed removing 19 modules from the standard library, colloquially referred to as ‘dead batteries’ due to their historic, obsolete, or insecure status. All of the following modules were deprecated in Python 3.11, and are now removed:

*   `aifc`
    
    *   [standard-aifc](https://pypi.org/project/standard-aifc/)
        : Use the redistribution of `aifc` library from PyPI.
        
*   `audioop`
    
    *   [audioop-lts](https://pypi.org/project/audioop-lts/)
        : Use `audioop-lts` library from PyPI.
        
*   `chunk`
    
    *   [standard-chunk](https://pypi.org/project/standard-chunk/)
        : Use the redistribution of `chunk` library from PyPI.
        
*   `cgi` and `cgitb`
    
    *   `cgi.FieldStorage` can typically be replaced with [`urllib.parse.parse_qsl()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qsl "urllib.parse.parse_qsl")
         for `GET` and `HEAD` requests, and the [`email.message`](https://docs.python.org/3/library/email.message.html#module-email.message "email.message: The base class representing email messages.")
         module or the [multipart](https://pypi.org/project/multipart/)
         library for `POST` and `PUT` requests.
        
    *   `cgi.parse()` can be replaced by calling [`urllib.parse.parse_qs()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qs "urllib.parse.parse_qs")
         directly on the desired query string, unless the input is `multipart/form-data`, which should be replaced as described below for `cgi.parse_multipart()`.
        
    *   `cgi.parse_header()` can be replaced with the functionality in the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
         package, which implements the same MIME RFCs. For example, with [`email.message.EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
        :
        
        Copy
        
        from email.message import EmailMessage
        
        msg \= EmailMessage()
        msg\['content-type'\] \= 'application/json; charset="utf8"'
        main, params \= msg.get\_content\_type(), msg\['content-type'\].params
        
    *   `cgi.parse_multipart()` can be replaced with the functionality in the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
         package, which implements the same MIME RFCs, or with the [multipart](https://pypi.org/project/multipart/)
         library. For example, the [`email.message.EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
         and [`email.message.Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
         classes.
        
    *   [standard-cgi](https://pypi.org/project/standard-cgi/)
        : and [standard-cgitb](https://pypi.org/project/standard-cgitb/)
        : Use the redistribution of `cgi` and `cgitb` library from PyPI.
        
*   `crypt` and the private `_crypt` extension. The [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
     module may be an appropriate replacement when simply hashing a value is required. Otherwise, various third-party libraries on PyPI are available:
    
    *   [bcrypt](https://pypi.org/project/bcrypt/)
        : Modern password hashing for your software and your servers.
        
    *   [argon2-cffi](https://pypi.org/project/argon2-cffi/)
        : The secure Argon2 password hashing algorithm.
        
    *   [legacycrypt](https://pypi.org/project/legacycrypt/)
        : [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
         wrapper to the POSIX crypt library call and associated functionality.
        
    *   [crypt\_r](https://pypi.org/project/crypt_r/)
        : Fork of the `crypt` module, wrapper to the _[crypt\_r(3)](https://manpages.debian.org/crypt_r(3))
        _ library call and associated functionality.
        
    *   [standard-crypt](https://pypi.org/project/standard-crypt/)
         and [deprecated-crypt-alternative](https://pypi.org/project/deprecated-crypt-alternative/)
        : Use the redistribution of `crypt` and reimplementation of `_crypt` libraries from PyPI.
        
*   `imghdr`: The [filetype](https://pypi.org/project/filetype/)
    , [puremagic](https://pypi.org/project/puremagic/)
    , or [python-magic](https://pypi.org/project/python-magic/)
     libraries should be used as replacements. For example, the `puremagic.what()` function can be used to replace the `imghdr.what()` function for all file formats that were supported by `imghdr`.
    
    *   [standard-imghdr](https://pypi.org/project/standard-imghdr/)
        : Use the redistribution of `imghdr` library from PyPI.
        
*   `mailcap`: Use the [`mimetypes`](https://docs.python.org/3/library/mimetypes.html#module-mimetypes "mimetypes: Mapping of filename extensions to MIME types.")
     module instead.
    
    *   [standard-mailcap](https://pypi.org/project/standard-mailcap/)
        : Use the redistribution of `mailcap` library from PyPI.
        
*   `msilib`
    
*   `nis`
    
*   `nntplib`: Use the [pynntp](https://pypi.org/project/pynntp/)
     library from PyPI instead.
    
    *   [standard-nntplib](https://pypi.org/project/standard-nntplib/)
        : Use the redistribution of `nntplib` library from PyPI.
        
*   `ossaudiodev`: For audio playback, use the [pygame](https://pypi.org/project/pygame/)
     library from PyPI instead.
    
*   `pipes`: Use the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
     module instead. Use [`shlex.quote()`](https://docs.python.org/3/library/shlex.html#shlex.quote "shlex.quote")
     to replace the undocumented `pipes.quote` function.
    
    *   [standard-pipes](https://pypi.org/project/standard-pipes/)
        : Use the redistribution of `pipes` library from PyPI.
        
*   `sndhdr`: The [filetype](https://pypi.org/project/filetype/)
    , [puremagic](https://pypi.org/project/puremagic/)
    , or [python-magic](https://pypi.org/project/python-magic/)
     libraries should be used as replacements.
    
    *   [standard-sndhdr](https://pypi.org/project/standard-sndhdr/)
        : Use the redistribution of `sndhdr` library from PyPI.
        
*   `spwd`: Use the [python-pam](https://pypi.org/project/python-pam/)
     library from PyPI instead.
    
*   `sunau`
    
    *   [standard-sunau](https://pypi.org/project/standard-sunau/)
        : Use the redistribution of `sunau` library from PyPI.
        
*   `telnetlib`, Use the [telnetlib3](https://pypi.org/project/telnetlib3/)
     or [Exscript](https://pypi.org/project/Exscript/)
     libraries from PyPI instead.
    
    *   [standard-telnetlib](https://pypi.org/project/standard-telnetlib/)
        : Use the redistribution of `telnetlib` library from PyPI.
        
*   `uu`: Use the [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")
     module instead, as a modern alternative.
    
    *   [standard-uu](https://pypi.org/project/standard-uu/)
        : Use the redistribution of `uu` library from PyPI.
        
*   `xdrlib`
    
    *   [standard-xdrlib](https://pypi.org/project/standard-xdrlib/)
        : Use the redistribution of `xdrlib` library from PyPI.
        

(Contributed by Victor Stinner and Zachary Ware in [gh-104773](https://github.com/python/cpython/issues/104773)
 and [gh-104780](https://github.com/python/cpython/issues/104780)
.)

### 2to3[¶](https://docs.python.org/3/whatsnew/3.13.html#to3 "Link to this heading")

*   Remove the **2to3** program and the `lib2to3` module, previously deprecated in Python 3.11. (Contributed by Victor Stinner in [gh-104780](https://github.com/python/cpython/issues/104780)
    .)
    

### builtins[¶](https://docs.python.org/3/whatsnew/3.13.html#builtins "Link to this heading")

*   Remove support for chained [`classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
     descriptors (introduced in [gh-63272](https://github.com/python/cpython/issues/63272)
    ). These can no longer be used to wrap other descriptors, such as [`property`](https://docs.python.org/3/builtins/functions.html#property "property")
    . The core design of this feature was flawed and led to several problems. To “pass-through” a `classmethod`, consider using the `__wrapped__` attribute that was added in Python 3.10. (Contributed by Raymond Hettinger in [gh-89519](https://github.com/python/cpython/issues/89519)
    .)
    
*   Raise a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
     when calling [`frame.clear()`](https://docs.python.org/3/reference/datamodel.html#frame.clear "frame.clear")
     on a suspended frame (as has always been the case for an executing frame). (Contributed by Irit Katriel in [gh-79932](https://github.com/python/cpython/issues/79932)
    .)
    

### configparser[¶](https://docs.python.org/3/whatsnew/3.13.html#id3 "Link to this heading")

*   Remove the undocumented `LegacyInterpolation` class, deprecated in the docstring since Python 3.2, and at runtime since Python 3.11. (Contributed by Hugo van Kemenade in [gh-104886](https://github.com/python/cpython/issues/104886)
    .)
    

### importlib.metadata[¶](https://docs.python.org/3/whatsnew/3.13.html#importlib-metadata "Link to this heading")

*   Remove deprecated subscript ([`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
    ) access for [EntryPoint](https://docs.python.org/3/library/importlib.metadata.html#entry-points)
     objects. (Contributed by Jason R. Coombs in [gh-113175](https://github.com/python/cpython/issues/113175)
    .)
    

### locale[¶](https://docs.python.org/3/whatsnew/3.13.html#locale "Link to this heading")

*   Remove the `locale.resetlocale()` function, deprecated in Python 3.11. Use `locale.setlocale(locale.LC_ALL, "")` instead. (Contributed by Victor Stinner in [gh-104783](https://github.com/python/cpython/issues/104783)
    .)
    

### opcode[¶](https://docs.python.org/3/whatsnew/3.13.html#opcode "Link to this heading")

*   Move `opcode.ENABLE_SPECIALIZATION` to `_opcode.ENABLE_SPECIALIZATION`. This field was added in 3.12, it was never documented, and is not intended for external use. (Contributed by Irit Katriel in [gh-105481](https://github.com/python/cpython/issues/105481)
    .)
    
*   Remove `opcode.is_pseudo()`, `opcode.MIN_PSEUDO_OPCODE`, and `opcode.MAX_PSEUDO_OPCODE`, which were added in Python 3.12, but were neither documented nor exposed through [`dis`](https://docs.python.org/3/library/dis.html#module-dis "dis: Disassembler for Python bytecode.")
    , and were not intended to be used externally. (Contributed by Irit Katriel in [gh-105481](https://github.com/python/cpython/issues/105481)
    .)
    

### optparse[¶](https://docs.python.org/3/whatsnew/3.13.html#optparse "Link to this heading")

*   This module is no longer considered [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
    . While [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
     remains preferred for new projects that aren’t using a third party command line argument processing library, there are aspects of the way `argparse` works that mean the lower level `optparse` module may provide a better foundation for _writing_ argument processing libraries, and for implementing command line applications which adhere more strictly than `argparse` does to various Unix command line processing conventions that originate in the behaviour of the C `getopt()` function . (Contributed by Alyssa Coghlan and Serhiy Storchaka in [gh-126180](https://github.com/python/cpython/issues/126180)
    .)
    

### pathlib[¶](https://docs.python.org/3/whatsnew/3.13.html#id4 "Link to this heading")

*   Remove the ability to use [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
     objects as context managers. This functionality was deprecated and has had no effect since Python 3.9. (Contributed by Barney Gale in [gh-83863](https://github.com/python/cpython/issues/83863)
    .)
    

### re[¶](https://docs.python.org/3/whatsnew/3.13.html#id5 "Link to this heading")

*   Remove the undocumented, deprecated, and broken `re.template()` function and `re.TEMPLATE` / `re.T` flag. (Contributed by Serhiy Storchaka and Nikita Sobolev in [gh-105687](https://github.com/python/cpython/issues/105687)
    .)
    

### tkinter.tix[¶](https://docs.python.org/3/whatsnew/3.13.html#tkinter-tix "Link to this heading")

*   Remove the `tkinter.tix` module, deprecated in Python 3.6. The third-party Tix library which the module wrapped is unmaintained. (Contributed by Zachary Ware in [gh-75552](https://github.com/python/cpython/issues/75552)
    .)
    

### turtle[¶](https://docs.python.org/3/whatsnew/3.13.html#turtle "Link to this heading")

*   Remove the `RawTurtle.settiltangle()` method, deprecated in the documentation since Python 3.1 and at runtime since Python 3.11. (Contributed by Hugo van Kemenade in [gh-104876](https://github.com/python/cpython/issues/104876)
    .)
    

### typing[¶](https://docs.python.org/3/whatsnew/3.13.html#id6 "Link to this heading")

*   Remove the `typing.io` and `typing.re` namespaces, deprecated since Python 3.8. The items in those namespaces can be imported directly from the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
     module. (Contributed by Sebastian Rittau in [gh-92871](https://github.com/python/cpython/issues/92871)
    .)
    
*   Remove the keyword-argument method of creating [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict")
     types, deprecated in Python 3.11. (Contributed by Tomas Roun in [gh-104786](https://github.com/python/cpython/issues/104786)
    .)
    

### unittest[¶](https://docs.python.org/3/whatsnew/3.13.html#unittest "Link to this heading")

*   Remove the following [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.")
     functions, deprecated in Python 3.11:
    
    *   `unittest.findTestCases()`
        
    *   `unittest.makeSuite()`
        
    *   `unittest.getTestCaseNames()`
        
    
    Use [`TestLoader`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader")
     methods instead:
    
    *   [`loadTestsFromModule()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromModule "unittest.TestLoader.loadTestsFromModule")
        
    *   [`loadTestsFromTestCase()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromTestCase "unittest.TestLoader.loadTestsFromTestCase")
        
    *   [`getTestCaseNames()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.getTestCaseNames "unittest.TestLoader.getTestCaseNames")
        
    
    (Contributed by Hugo van Kemenade in [gh-104835](https://github.com/python/cpython/issues/104835)
    .)
    
*   Remove the untested and undocumented `TestProgram.usageExit()` method, deprecated in Python 3.11. (Contributed by Hugo van Kemenade in [gh-104992](https://github.com/python/cpython/issues/104992)
    .)
    

### urllib[¶](https://docs.python.org/3/whatsnew/3.13.html#urllib "Link to this heading")

*   Remove the _cafile_, _capath_, and _cadefault_ parameters of the [`urllib.request.urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen")
     function, deprecated in Python 3.6. Use the _context_ parameter instead with an [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
     instance. The [`ssl.SSLContext.load_verify_locations()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations "ssl.SSLContext.load_verify_locations")
     method can be used to load specific CA certificates, or let [`ssl.create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context")
     select the operating system’s trusted certificate authority (CA) certificates. (Contributed by Victor Stinner in [gh-105382](https://github.com/python/cpython/issues/105382)
    .)
    

### webbrowser[¶](https://docs.python.org/3/whatsnew/3.13.html#webbrowser "Link to this heading")

*   Remove the untested and undocumented `MacOSX` class, deprecated in Python 3.11. Use the `MacOSXOSAScript` class (introduced in Python 3.2) instead. (Contributed by Hugo van Kemenade in [gh-104804](https://github.com/python/cpython/issues/104804)
    .)
    
*   Remove the deprecated `MacOSXOSAScript._name` attribute. Use the [`MacOSXOSAScript.name`](https://docs.python.org/3/library/webbrowser.html#webbrowser.controller.name "webbrowser.controller.name")
     attribute instead. (Contributed by Nikita Sobolev in [gh-105546](https://github.com/python/cpython/issues/105546)
    .)
    

New Deprecations[¶](https://docs.python.org/3/whatsnew/3.13.html#new-deprecations "Link to this heading")

----------------------------------------------------------------------------------------------------------

*   [User-defined functions](https://docs.python.org/3/reference/datamodel.html#user-defined-funcs)
    :
    
    *   Deprecate assignment to a function’s [`__code__`](https://docs.python.org/3/reference/datamodel.html#function.__code__ "function.__code__")
         attribute, where the new code object’s type does not match the function’s type. The different types are: plain function, generator, async generator, and coroutine. (Contributed by Irit Katriel in [gh-81137](https://github.com/python/cpython/issues/81137)
        .)
        
*   [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.")
    :
    
    *   Deprecate the `'u'` format code (`wchar_t`) at runtime. This format code has been deprecated in documentation since Python 3.3, and will be removed in Python 3.16. Use the `'w'` format code ([`Py_UCS4`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
        ) for Unicode characters instead. (Contributed by Hugo van Kemenade in [gh-80480](https://github.com/python/cpython/issues/80480)
        .)
        
*   [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
    :
    
    *   Deprecate the undocumented `SetPointerType()` function, to be removed in Python 3.15. (Contributed by Victor Stinner in [gh-105733](https://github.com/python/cpython/issues/105733)
        .)
        
    *   [Soft-deprecate](https://docs.python.org/3/glossary.html#term-soft-deprecated)
         the [`ARRAY()`](https://docs.python.org/3/library/ctypes.html#ctypes.ARRAY "ctypes.ARRAY")
         function in favour of `type * length` multiplication. (Contributed by Victor Stinner in [gh-105733](https://github.com/python/cpython/issues/105733)
        .)
        
*   [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
    :
    
    *   Deprecate the non-standard and undocumented [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
         format specifier `'N'`, which is only supported in the `decimal` module’s C implementation. Scheduled to be removed in Python 3.18. (Contributed by Serhiy Storchaka in [gh-89902](https://github.com/python/cpython/issues/89902)
        .)
        
*   [`dis`](https://docs.python.org/3/library/dis.html#module-dis "dis: Disassembler for Python bytecode.")
    :
    
    *   Deprecate the `HAVE_ARGUMENT` separator. Check membership in [`hasarg`](https://docs.python.org/3/library/dis.html#dis.hasarg "dis.hasarg")
         instead. (Contributed by Irit Katriel in [gh-109319](https://github.com/python/cpython/issues/109319)
        .)
        
*   [`gettext`](https://docs.python.org/3/library/gettext.html#module-gettext "gettext: Multilingual internationalization services.")
    :
    
    *   Deprecate non-integer numbers as arguments to functions and methods that consider plural forms in the `gettext` module, even if no translation was found. (Contributed by Serhiy Storchaka in [gh-88434](https://github.com/python/cpython/issues/88434)
        .)
        
*   [`glob`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.")
    :
    
    *   Deprecate the undocumented `glob0()` and `glob1()` functions. Use [`glob()`](https://docs.python.org/3/library/glob.html#glob.glob "glob.glob")
         and pass a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
         specifying the root directory to the _root\_dir_ parameter instead. (Contributed by Barney Gale in [gh-117337](https://github.com/python/cpython/issues/117337)
        .)
        
*   [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
    :
    
    *   Deprecate `CGIHTTPRequestHandler`, to be removed in Python 3.15. Process-based CGI HTTP servers have been out of favor for a very long time. This code was outdated, unmaintained, and rarely used. It has a high potential for both security and functionality bugs. (Contributed by Gregory P. Smith in [gh-109096](https://github.com/python/cpython/issues/109096)
        .)
        
    *   Deprecate the `--cgi` flag to the **python -m http.server** command-line interface, to be removed in Python 3.15. (Contributed by Gregory P. Smith in [gh-109096](https://github.com/python/cpython/issues/109096)
        .)
        
*   [`mimetypes`](https://docs.python.org/3/library/mimetypes.html#module-mimetypes "mimetypes: Mapping of filename extensions to MIME types.")
    :
    
    *   [Soft-deprecate](https://docs.python.org/3/glossary.html#term-soft-deprecated)
         file path arguments to [`guess_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type "mimetypes.guess_type")
        , use [`guess_file_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_file_type "mimetypes.guess_file_type")
         instead. (Contributed by Serhiy Storchaka in [gh-66543](https://github.com/python/cpython/issues/66543)
        .)
        
*   [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
    :
    
    *   Deprecate passing the optional _maxsplit_, _count_, or _flags_ arguments as positional arguments to the module-level [`split()`](https://docs.python.org/3/library/re.html#re.split "re.split")
        , [`sub()`](https://docs.python.org/3/library/re.html#re.sub "re.sub")
        , and [`subn()`](https://docs.python.org/3/library/re.html#re.subn "re.subn")
         functions. These parameters will become [keyword-only](https://docs.python.org/3/glossary.html#keyword-only-parameter)
         in a future version of Python. (Contributed by Serhiy Storchaka in [gh-56166](https://github.com/python/cpython/issues/56166)
        .)
        
*   [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths")
    :
    
    *   Deprecate `.PurePath.is_reserved()`, to be removed in Python 3.15. Use [`os.path.isreserved()`](https://docs.python.org/3/library/os.path.html#os.path.isreserved "os.path.isreserved")
         to detect reserved paths on Windows. (Contributed by Barney Gale in [gh-88569](https://github.com/python/cpython/issues/88569)
        .)
        
*   [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")
    :
    
    *   Deprecate `platform.java_ver()`, to be removed in Python 3.15. This function is only useful for Jython support, has a confusing API, and is largely untested. (Contributed by Nikita Sobolev in [gh-116349](https://github.com/python/cpython/issues/116349)
        .)
        
*   [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
    :
    
    *   Deprecate the undocumented `ispackage()` function. (Contributed by Zackery Spytz in [gh-64020](https://github.com/python/cpython/issues/64020)
        .)
        
*   [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.")
    :
    
    *   Deprecate passing more than one positional argument to the [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect")
         function and the [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection")
         constructor. The remaining parameters will become keyword-only in Python 3.15. (Contributed by Erlend E. Aasland in [gh-107948](https://github.com/python/cpython/issues/107948)
        .)
        
    *   Deprecate passing name, number of arguments, and the callable as keyword arguments for [`Connection.create_function()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function "sqlite3.Connection.create_function")
         and [`Connection.create_aggregate()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_aggregate "sqlite3.Connection.create_aggregate")
         These parameters will become positional-only in Python 3.15. (Contributed by Erlend E. Aasland in [gh-108278](https://github.com/python/cpython/issues/108278)
        .)
        
    *   Deprecate passing the callback callable by keyword for the [`set_authorizer()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_authorizer "sqlite3.Connection.set_authorizer")
        , [`set_progress_handler()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_progress_handler "sqlite3.Connection.set_progress_handler")
        , and [`set_trace_callback()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_trace_callback "sqlite3.Connection.set_trace_callback")
         [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection")
         methods. The callback callables will become positional-only in Python 3.15. (Contributed by Erlend E. Aasland in [gh-108278](https://github.com/python/cpython/issues/108278)
        .)
        
*   [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
    :
    
    *   Deprecate the [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3/library/sys.html#sys._enablelegacywindowsfsencoding "sys._enablelegacywindowsfsencoding")
         function, to be removed in Python 3.16. Use the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING)
         environment variable instead. (Contributed by Inada Naoki in [gh-73427](https://github.com/python/cpython/issues/73427)
        .)
        
*   [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
    :
    
    *   Deprecate the undocumented and unused `TarFile.tarfile` attribute, to be removed in Python 3.16. (Contributed in [gh-115256](https://github.com/python/cpython/issues/115256)
        .)
        
*   [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.")
    :
    
    *   Deprecate the [`TracebackException.exc_type`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.exc_type "traceback.TracebackException.exc_type")
         attribute. Use [`TracebackException.exc_type_str`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException.exc_type_str "traceback.TracebackException.exc_type_str")
         instead. (Contributed by Irit Katriel in [gh-112332](https://github.com/python/cpython/issues/112332)
        .)
        
*   [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
    :
    
    *   Deprecate the undocumented keyword argument syntax for creating [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")
         classes (e.g. `Point = NamedTuple("Point", x=int, y=int)`), to be removed in Python 3.15. Use the class-based syntax or the functional syntax instead. (Contributed by Alex Waygood in [gh-105566](https://github.com/python/cpython/issues/105566)
        .)
        
    *   Deprecate omitting the _fields_ parameter when creating a [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")
         or [`typing.TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict")
         class, and deprecate passing `None` to the _fields_ parameter of both types. Python 3.15 will require a valid sequence for the _fields_ parameter. To create a NamedTuple class with zero fields, use `class NT(NamedTuple): pass` or `NT = NamedTuple("NT", ())`. To create a TypedDict class with zero fields, use `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})`. (Contributed by Alex Waygood in [gh-105566](https://github.com/python/cpython/issues/105566)
         and [gh-105570](https://github.com/python/cpython/issues/105570)
        .)
        
    *   Deprecate the `typing.no_type_check_decorator` decorator function, to be removed in Python 3.15. After eight years in the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
         module, it has yet to be supported by any major type checker. (Contributed by Alex Waygood in [gh-106309](https://github.com/python/cpython/issues/106309)
        .)
        
    *   Deprecate [`typing.AnyStr`](https://docs.python.org/3/library/typing.html#typing.AnyStr "typing.AnyStr")
        . In Python 3.16, it will be removed from `typing.__all__`, and a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
         will be emitted at runtime when it is imported or accessed. It will be removed entirely in Python 3.18. Use the new [type parameter syntax](https://docs.python.org/3/reference/compound_stmts.html#type-params)
         instead. (Contributed by Michael The in [gh-107116](https://github.com/python/cpython/issues/107116)
        .)
        
*   [`wave`](https://docs.python.org/3/library/wave.html#module-wave "wave: Provide an interface to the WAV sound format.")
    :
    
    *   Deprecate the `getmark()`, `setmark()` and `getmarkers()` methods of the [`Wave_read`](https://docs.python.org/3/library/wave.html#wave.Wave_read "wave.Wave_read")
         and [`Wave_write`](https://docs.python.org/3/library/wave.html#wave.Wave_write "wave.Wave_write")
         classes, to be removed in Python 3.15. (Contributed by Victor Stinner in [gh-105096](https://github.com/python/cpython/issues/105096)
        .)
        

### Pending removal in Python 3.14[¶](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-14 "Link to this heading")

*   [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
    : The _type_, _choices_, and _metavar_ parameters of `argparse.BooleanOptionalAction` are deprecated and will be removed in 3.14. (Contributed by Nikita Sobolev in [gh-92248](https://github.com/python/cpython/issues/92248)
    .)
    
*   [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.")
    : The following features have been deprecated in documentation since Python 3.8, now cause a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
     to be emitted at runtime when they are accessed or used, and will be removed in Python 3.14:
    
    *   `ast.Num`
        
    *   `ast.Str`
        
    *   `ast.Bytes`
        
    *   `ast.NameConstant`
        
    *   `ast.Ellipsis`
        
    
    Use [`ast.Constant`](https://docs.python.org/3/library/ast.html#ast.Constant "ast.Constant")
     instead. (Contributed by Serhiy Storchaka in [gh-90953](https://github.com/python/cpython/issues/90953)
    .)
    
*   [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
    :
    
    *   The child watcher classes `asyncio.MultiLoopChildWatcher`, `asyncio.FastChildWatcher`, `asyncio.AbstractChildWatcher` and `asyncio.SafeChildWatcher` are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597)
        .)
        
    *   `asyncio.set_child_watcher()`, `asyncio.get_child_watcher()`, `asyncio.AbstractEventLoopPolicy.set_child_watcher()` and `asyncio.AbstractEventLoopPolicy.get_child_watcher()` are deprecated and will be removed in Python 3.14. (Contributed by Kumar Aditya in [gh-94597](https://github.com/python/cpython/issues/94597)
        .)
        
    *   The [`get_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop "asyncio.get_event_loop")
         method of the default event loop policy now emits a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
         if there is no current event loop set and it decides to create one. (Contributed by Serhiy Storchaka and Guido van Rossum in [gh-100160](https://github.com/python/cpython/issues/100160)
        .)
        
*   [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.")
    : Deprecated the _isdst_ parameter in [`email.utils.localtime()`](https://docs.python.org/3/library/email.utils.html#email.utils.localtime "email.utils.localtime")
    . (Contributed by Alan Williams in [gh-72346](https://github.com/python/cpython/issues/72346)
    .)
    
*   [`importlib.abc`](https://docs.python.org/3/library/importlib.html#module-importlib.abc "importlib.abc: Abstract base classes related to import")
     deprecated classes:
    
    *   `importlib.abc.ResourceReader`
        
    *   `importlib.abc.Traversable`
        
    *   `importlib.abc.TraversableResources`
        
    
    Use [`importlib.resources.abc`](https://docs.python.org/3/library/importlib.resources.abc.html#module-importlib.resources.abc "importlib.resources.abc: Abstract base classes for resources")
     classes instead:
    
    *   [`importlib.resources.abc.Traversable`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable")
        
    *   [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources "importlib.resources.abc.TraversableResources")
        
    
    (Contributed by Jason R. Coombs and Hugo van Kemenade in [gh-93963](https://github.com/python/cpython/issues/93963)
    .)
    
*   [`itertools`](https://docs.python.org/3/library/itertools.html#module-itertools "itertools: Functions creating iterators for efficient looping.")
     had undocumented, inefficient, historically buggy, and inconsistent support for copy, deepcopy, and pickle operations. This will be removed in 3.14 for a significant reduction in code volume and maintenance burden. (Contributed by Raymond Hettinger in [gh-101588](https://github.com/python/cpython/issues/101588)
    .)
    
*   [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
    : The default start method will change to a safer one on Linux, BSDs, and other non-macOS POSIX platforms where `'fork'` is currently the default ([gh-84559](https://github.com/python/cpython/issues/84559)
    ). Adding a runtime warning about this was deemed too disruptive as the majority of code is not expected to care. Use the [`get_context()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.get_context "multiprocessing.get_context")
     or [`set_start_method()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.set_start_method "multiprocessing.set_start_method")
     APIs to explicitly specify when your code _requires_ `'fork'`. See [Contexts and start methods](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-start-methods)
    .
    
*   [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths")
    : [`is_relative_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.is_relative_to "pathlib.PurePath.is_relative_to")
     and [`relative_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.relative_to "pathlib.PurePath.relative_to")
    : passing additional arguments is deprecated.
    
*   [`pkgutil`](https://docs.python.org/3/library/pkgutil.html#module-pkgutil "pkgutil: Utilities for the import system.")
    : `pkgutil.find_loader()` and `pkgutil.get_loader()` now raise [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
    ; use [`importlib.util.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.find_spec "importlib.util.find_spec")
     instead. (Contributed by Nikita Sobolev in [gh-97850](https://github.com/python/cpython/issues/97850)
    .)
    
*   [`pty`](https://docs.python.org/3/library/pty.html#module-pty "pty: Pseudo-Terminal Handling for Unix.")
    :
    
    *   `master_open()`: use [`pty.openpty()`](https://docs.python.org/3/library/pty.html#pty.openpty "pty.openpty")
        .
        
    *   `slave_open()`: use [`pty.openpty()`](https://docs.python.org/3/library/pty.html#pty.openpty "pty.openpty")
        .
        
*   [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.")
    :
    
    *   `version` and `version_info`.
        
    *   [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute")
         and [`executemany()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany "sqlite3.Cursor.executemany")
         if [named placeholders](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders)
         are used and _parameters_ is a sequence instead of a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
        .
        
*   [`urllib`](https://docs.python.org/3/library/urllib.html#module-urllib "urllib")
    : `urllib.parse.Quoter` is deprecated: it was not intended to be a public API. (Contributed by Gregory P. Smith in [gh-88168](https://github.com/python/cpython/issues/88168)
    .)
    

### Pending removal in Python 3.15[¶](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-15 "Link to this heading")

*   The import system:
    
    *   Setting `__cached__` on a module while failing to set [`__spec__.cached`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.cached "importlib.machinery.ModuleSpec.cached")
         is deprecated. In Python 3.15, `__cached__` will cease to be set or take into consideration by the import system or standard library. ([gh-97879](https://github.com/python/cpython/issues/97879)
        )
        
    *   Setting [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
         on a module while failing to set [`__spec__.parent`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.parent "importlib.machinery.ModuleSpec.parent")
         is deprecated. In Python 3.15, `__package__` will cease to be set or take into consideration by the import system or standard library. ([gh-97879](https://github.com/python/cpython/issues/97879)
        )
        
*   [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
    :
    
    *   The undocumented `ctypes.SetPointerType()` function has been deprecated since Python 3.13.
        
*   [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
    :
    
    *   The obsolete and rarely used `CGIHTTPRequestHandler` has been deprecated since Python 3.13. No direct replacement exists. _Anything_ is better than CGI to interface a web server with a request handler.
        
    *   The `--cgi` flag to the **python -m http.server** command-line interface has been deprecated since Python 3.13.
        
*   [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
    :
    
    *   `load_module()` method: use `exec_module()` instead.
        
*   [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths")
    :
    
    *   `.PurePath.is_reserved()` has been deprecated since Python 3.13. Use [`os.path.isreserved()`](https://docs.python.org/3/library/os.path.html#os.path.isreserved "os.path.isreserved")
         to detect reserved paths on Windows.
        
*   [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")
    :
    
    *   `platform.java_ver()` has been deprecated since Python 3.13. This function is only useful for Jython support, has a confusing API, and is largely untested.
        
*   [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")
    :
    
    *   The _check\_home_ argument of [`sysconfig.is_python_build()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.is_python_build "sysconfig.is_python_build")
         has been deprecated since Python 3.12.
        
*   [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
    :
    
    *   [`RLock()`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock")
         will take no arguments in Python 3.15. Passing any arguments has been deprecated since Python 3.14, as the Python version does not permit any arguments, but the C version allows any number of positional or keyword arguments, ignoring every argument.
        
*   [`types`](https://docs.python.org/3/library/types.html#module-types "types: Names for built-in types.")
    :
    
    *   [`types.CodeType`](https://docs.python.org/3/library/types.html#types.CodeType "types.CodeType")
        : Accessing `codeobject.co_lnotab` was deprecated in [**PEP 626**](https://peps.python.org/pep-0626/)
         since 3.10 and was planned to be removed in 3.12, but it only got a proper [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
         in 3.12. May be removed in 3.15. (Contributed by Nikita Sobolev in [gh-101866](https://github.com/python/cpython/issues/101866)
        .)
        
*   [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
    :
    
    *   The undocumented keyword argument syntax for creating [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")
         classes (for example, `Point = NamedTuple("Point", x=int, y=int)`) has been deprecated since Python 3.13. Use the class-based syntax or the functional syntax instead.
        
    *   When using the functional syntax of [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict")
        s, failing to pass a value to the _fields_ parameter (`TD = TypedDict("TD")`) or passing `None` (`TD = TypedDict("TD", None)`) has been deprecated since Python 3.13. Use `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})` to create a TypedDict with zero field.
        
    *   The `typing.no_type_check_decorator` decorator function has been deprecated since Python 3.13. After eight years in the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
         module, it has yet to be supported by any major type checker.
        
*   `sre_compile`, `sre_constants` and `sre_parse` modules.
    
*   [`wave`](https://docs.python.org/3/library/wave.html#module-wave "wave: Provide an interface to the WAV sound format.")
    :
    
    *   The `getmark()`, `setmark()` and `getmarkers()` methods of the [`Wave_read`](https://docs.python.org/3/library/wave.html#wave.Wave_read "wave.Wave_read")
         and [`Wave_write`](https://docs.python.org/3/library/wave.html#wave.Wave_write "wave.Wave_write")
         classes have been deprecated since Python 3.13.
        
*   [`zipimport`](https://docs.python.org/3/library/zipimport.html#module-zipimport "zipimport: Support for importing Python modules from ZIP archives.")
    :
    
    *   `zipimport.zipimporter.load_module()` has been deprecated since Python 3.10. Use [`exec_module()`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.exec_module "zipimport.zipimporter.exec_module")
         instead. ([gh-125746](https://github.com/python/cpython/issues/125746)
        .)
        

### Pending removal in Python 3.16[¶](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-16 "Link to this heading")

*   The import system:
    
    *   Setting [`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")
         on a module while failing to set [`__spec__.loader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.loader "importlib.machinery.ModuleSpec.loader")
         is deprecated. In Python 3.16, `__loader__` will cease to be set or taken into consideration by the import system or the standard library.
        
*   [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.")
    :
    
    *   The `'u'` format code (`wchar_t`) has been deprecated in documentation since Python 3.3 and at runtime since Python 3.13. Use the `'w'` format code ([`Py_UCS4`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
        ) for Unicode characters instead.
        
*   [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
    :
    
    *   `asyncio.iscoroutinefunction()` is deprecated and will be removed in Python 3.16; use [`inspect.iscoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction "inspect.iscoroutinefunction")
         instead. (Contributed by Jiahao Li and Kumar Aditya in [gh-122875](https://github.com/python/cpython/issues/122875)
        .)
        
    *   [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
         policy system is deprecated and will be removed in Python 3.16. In particular, the following classes and functions are deprecated:
        
        *   [`asyncio.AbstractEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy "asyncio.AbstractEventLoopPolicy")
            
        *   [`asyncio.DefaultEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.DefaultEventLoopPolicy "asyncio.DefaultEventLoopPolicy")
            
        *   [`asyncio.WindowsSelectorEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.WindowsSelectorEventLoopPolicy "asyncio.WindowsSelectorEventLoopPolicy")
            
        *   [`asyncio.WindowsProactorEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.WindowsProactorEventLoopPolicy "asyncio.WindowsProactorEventLoopPolicy")
            
        *   [`asyncio.get_event_loop_policy()`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.get_event_loop_policy "asyncio.get_event_loop_policy")
            
        *   [`asyncio.set_event_loop_policy()`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.set_event_loop_policy "asyncio.set_event_loop_policy")
            
        
        Users should use [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
         or [`asyncio.Runner`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.Runner "asyncio.Runner")
         with _loop\_factory_ to use the desired event loop implementation.
        
        For example, to use [`asyncio.SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
         on Windows:
        
        Copy
        
        import asyncio
        
        async def main():
            ...
        
        asyncio.run(main(), loop\_factory\=asyncio.SelectorEventLoop)
        
        (Contributed by Kumar Aditya in [gh-127949](https://github.com/python/cpython/issues/127949)
        .)
        
*   [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")
    :
    
    *   Bitwise inversion on boolean types, `~True` or `~False` has been deprecated since Python 3.12, as it produces surprising and unintuitive results (`-2` and `-1`). Use `not x` instead for the logical negation of a Boolean. In the rare case that you need the bitwise inversion of the underlying integer, convert to `int` explicitly (`~int(x)`).
        
*   [`functools`](https://docs.python.org/3/library/functools.html#module-functools "functools: Higher-order functions and operations on callable objects.")
    :
    
    *   Calling the Python implementation of [`functools.reduce()`](https://docs.python.org/3/library/functools.html#functools.reduce "functools.reduce")
         with _function_ or _sequence_ as keyword arguments has been deprecated since Python 3.14.
        
*   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
    :
    
    *   Support for custom logging handlers with the _strm_ argument is deprecated and scheduled for removal in Python 3.16. Define handlers with the _stream_ argument instead. (Contributed by Mariusz Felisiak in [gh-115032](https://github.com/python/cpython/issues/115032)
        .)
        
*   [`mimetypes`](https://docs.python.org/3/library/mimetypes.html#module-mimetypes "mimetypes: Mapping of filename extensions to MIME types.")
    :
    
    *   Valid extensions start with a ‘.’ or are empty for [`mimetypes.MimeTypes.add_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.add_type "mimetypes.MimeTypes.add_type")
        . Undotted extensions are deprecated and will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
         in Python 3.16. (Contributed by Hugo van Kemenade in [gh-75223](https://github.com/python/cpython/issues/75223)
        .)
        
*   [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")
    :
    
    *   The `ExecError` exception has been deprecated since Python 3.14. It has not been used by any function in `shutil` since Python 3.4, and is now an alias of [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
        .
        
*   [`symtable`](https://docs.python.org/3/library/symtable.html#module-symtable "symtable: Interface to the compiler's internal symbol tables.")
    :
    
    *   The [`Class.get_methods`](https://docs.python.org/3/library/symtable.html#symtable.Class.get_methods "symtable.Class.get_methods")
         method has been deprecated since Python 3.14.
        
*   [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
    :
    
    *   The [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3/library/sys.html#sys._enablelegacywindowsfsencoding "sys._enablelegacywindowsfsencoding")
         function has been deprecated since Python 3.13. Use the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING)
         environment variable instead.
        
*   [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")
    :
    
    *   The `sysconfig.expand_makefile_vars()` function has been deprecated since Python 3.14. Use the `vars` argument of [`sysconfig.get_paths()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_paths "sysconfig.get_paths")
         instead.
        
*   [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
    :
    
    *   The undocumented and unused `TarFile.tarfile` attribute has been deprecated since Python 3.13.
        

### Pending removal in Python 3.17[¶](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-17 "Link to this heading")

*   [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
    :
    
    *   [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime")
         calls using a format string containing `%e` (day of month) without a year. This has been deprecated since Python 3.15. (Contributed by Stan Ulbrych in [gh-70647](https://github.com/python/cpython/issues/70647)
        .)
        
*   [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")
    :
    
    *   [`collections.abc.ByteString`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ByteString "collections.abc.ByteString")
         is scheduled for removal in Python 3.17.
        
        Use `isinstance(obj, collections.abc.Buffer)` to test if `obj` implements the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
         at runtime. For use in type annotations, either use [`Buffer`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")
         or a union that explicitly specifies the types your code supports (e.g., `bytes | bytearray | memoryview`).
        
        `ByteString` was originally intended to be an abstract class that would serve as a supertype of both [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
         and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
        . However, since the ABC never had any methods, knowing that an object was an instance of `ByteString` never actually told you anything useful about the object. Other common buffer types such as [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
         were also never understood as subtypes of `ByteString` (either at runtime or by static type checkers).
        
        See [**PEP 688**](https://peps.python.org/pep-0688/#current-options)
         for more details. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896)
        .)
        
*   [`encodings`](https://docs.python.org/3/library/codecs.html#module-encodings "encodings: Encodings package")
    :
    
    *   Passing non-ascii _encoding_ names to [`encodings.normalize_encoding()`](https://docs.python.org/3/library/codecs.html#encodings.normalize_encoding "encodings.normalize_encoding")
         is deprecated and scheduled for removal in Python 3.17. (Contributed by Stan Ulbrych in [gh-136702](https://github.com/python/cpython/issues/136702)
        .)
        
*   [`profile`](https://docs.python.org/3/library/profile.html#module-profile "profile: Pure Python profiler (deprecated). (deprecated)")
    :
    
    *   The `profile` module is deprecated and will be removed in Python 3.17. Use [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
         instead, which provides a compatible API. See [**PEP 799**](https://peps.python.org/pep-0799/)
         for details. (Contributed by Pablo Galindo and László Kiss Kollár in [gh-138122](https://github.com/python/cpython/issues/138122)
        .)
        
*   [`webbrowser`](https://docs.python.org/3/library/webbrowser.html#module-webbrowser "webbrowser: Easy-to-use controller for web browsers.")
    :
    
    *   `webbrowser.MacOSXOSAScript` is deprecated in favour of `webbrowser.MacOS`. ([gh-137586](https://github.com/python/cpython/issues/137586)
        )
        
*   [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
    :
    
    *   Before Python 3.14, old-style unions were implemented using the private class `typing._UnionGenericAlias`. This class is no longer needed for the implementation, but it has been retained for backward compatibility, with removal scheduled for Python 3.17. Users should use documented introspection helpers like [`typing.get_origin()`](https://docs.python.org/3/library/typing.html#typing.get_origin "typing.get_origin")
         and [`typing.get_args()`](https://docs.python.org/3/library/typing.html#typing.get_args "typing.get_args")
         instead of relying on private implementation details.
        
    *   [`typing.ByteString`](https://docs.python.org/3/library/typing.html#typing.ByteString "typing.ByteString")
        , deprecated since Python 3.9, is scheduled for removal in Python 3.17.
        
        Use `isinstance(obj, collections.abc.Buffer)` to test if `obj` implements the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
         at runtime. For use in type annotations, either use [`Buffer`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")
         or a union that explicitly specifies the types your code supports (e.g., `bytes | bytearray | memoryview`).
        
        `ByteString` was originally intended to be an abstract class that would serve as a supertype of both [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
         and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
        . However, since the ABC never had any methods, knowing that an object was an instance of `ByteString` never actually told you anything useful about the object. Other common buffer types such as [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
         were also never understood as subtypes of `ByteString` (either at runtime or by static type checkers).
        
        See [**PEP 688**](https://peps.python.org/pep-0688/#current-options)
         for more details. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896)
        .)
        
*   [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
    :
    
    *   The `tkinter.Variable` methods `trace_variable()`, `trace()` (an alias of `trace_variable()`), `trace_vdelete()` and `trace_vinfo()`, deprecated since Python 3.14, are scheduled for removal in Python 3.17. Use `trace_add()`, `trace_remove()` and `trace_info()` instead. (Contributed by Serhiy Storchaka in [gh-120220](https://github.com/python/cpython/issues/120220)
        .)
        

### Pending removal in Python 3.18[¶](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-18 "Link to this heading")

*   No longer accept a boolean value when a file descriptor is expected. (Contributed by Serhiy Storchaka in [gh-82626](https://github.com/python/cpython/issues/82626)
    .)
    
*   [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
    :
    
    *   The non-standard and undocumented [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
         format specifier `'N'`, which is only supported in the `decimal` module’s C implementation, has been deprecated since Python 3.13. (Contributed by Serhiy Storchaka in [gh-89902](https://github.com/python/cpython/issues/89902)
        .)
        
*   Deprecations defined by [**PEP 829**](https://peps.python.org/pep-0829/)
    :
    
    *   `import` lines in `_name_.pth` files are silently ignored.
        
    
    (Contributed by Barry Warsaw in [gh-148641](https://github.com/python/cpython/issues/148641)
    .)
    

### Pending removal in Python 3.19[¶](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-19 "Link to this heading")

*   [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
    :
    
    *   Implicitly switching to the MSVC-compatible struct layout by setting [`_pack_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "ctypes.Structure._pack_")
         but not [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_")
         on non-Windows platforms.
        
*   [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
    :
    
    *   In hash function constructors such as [`new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new")
         or the direct hash-named constructors such as [`md5()`](https://docs.python.org/3/library/hashlib.html#hashlib.md5 "hashlib.md5")
         and [`sha256()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha256 "hashlib.sha256")
        , their optional initial data parameter could also be passed a keyword argument named `data=` or `string=` in various `hashlib` implementations.
        
        Support for the `string` keyword argument name is now deprecated and slated for removal in Python 3.19.
        
        Before Python 3.13, the `string` keyword parameter was not correctly supported depending on the backend implementation of hash functions. Prefer passing the initial data as a positional argument for maximum backwards compatibility.
        
*   [`http.cookies`](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "http.cookies: Support for HTTP state management (cookies).")
    :
    
    *   [`http.cookies.Morsel.js_output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.js_output "http.cookies.Morsel.js_output")
         is deprecated and will be removed in Python 3.19.
        
    *   [`http.cookies.BaseCookie.js_output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.js_output "http.cookies.BaseCookie.js_output")
         is deprecated and will be removed in Python 3.19.
        
*   [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).")
    :
    
    *   Altering [`IMAP4.file`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.file "imaplib.IMAP4.file")
         is now deprecated and slated for removal in Python 3.19. This property is now unused and changing its value does not automatically close the current file.
        
        Before Python 3.14, this property was used to implement the corresponding `read()` and `readline()` methods for [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4")
         but this is no longer the case since then.
        

### Pending removal in Python 3.20[¶](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-20 "Link to this heading")

*   Calling the `__new__()` method of [`struct.Struct`](https://docs.python.org/3/library/struct.html#struct.Struct "struct.Struct")
     without the _format_ argument is deprecated and will be removed in Python 3.20. Calling [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
     method on initialized `Struct` objects is deprecated and will be removed in Python 3.20.
    
    (Contributed by Sergey B Kirpichev and Serhiy Storchaka in [gh-143715](https://github.com/python/cpython/issues/143715)
    .)
    
*   The `__version__`, `version` and `VERSION` attributes have been deprecated in these standard library modules and will be removed in Python 3.20. Use [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")
     instead.
    
    *   [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
        
    *   [`csv`](https://docs.python.org/3/library/csv.html#module-csv "csv: Write and read tabular data to and from delimited files.")
        
    *   [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
        
    *   `ctypes.macholib`
        
    *   [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
         (use [`decimal.SPEC_VERSION`](https://docs.python.org/3/library/decimal.html#decimal.SPEC_VERSION "decimal.SPEC_VERSION")
         instead)
        
    *   [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
        
    *   [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).")
        
    *   [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.")
        
    *   [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")
        
    *   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
         (`__date__` also deprecated)
        
    *   [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")
        
    *   [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
        
    *   [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")
        
    *   [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
        
    *   [`socketserver`](https://docs.python.org/3/library/socketserver.html#module-socketserver "socketserver: A framework for network servers.")
        
    *   [`tabnanny`](https://docs.python.org/3/library/tabnanny.html#module-tabnanny "tabnanny: Tool for detecting white space related problems in Python source files in a directory tree.")
        
    *   [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
        
    *   [`tkinter.font`](https://docs.python.org/3/library/tkinter.font.html#module-tkinter.font "tkinter.font: Tkinter font-wrapping class")
        
    *   [`tkinter.ttk`](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk "tkinter.ttk: Tk themed widget set")
        
    *   [`wsgiref.simple_server`](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.simple_server "wsgiref.simple_server: A simple WSGI HTTP server.")
        
    *   [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")
        
    *   `xml.sax.expatreader`
        
    *   [`xml.sax.handler`](https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.")
        
    *   [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")
        
    
    (Contributed by Hugo van Kemenade and Stan Ulbrych in [gh-76007](https://github.com/python/cpython/issues/76007)
    .)
    
*   Deprecations defined by [**PEP 829**](https://peps.python.org/pep-0829/)
    :
    
    *   Warnings are produced for `import` lines found in `_name_.pth` files.
        
    *   `_name_.pth` files are no longer decoded in the locale encoding by default. They **MUST** be encoded in `utf-8-sig`.
        
    
    (Contributed by Barry Warsaw in [gh-148641](https://github.com/python/cpython/issues/148641)
    .)
    
*   [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.")
    :
    
    *   Creating instances of abstract AST nodes (such as [`ast.AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST")
         or `ast.expr`) is deprecated and will raise an error in Python 3.20.
        
*   [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")
    :
    
    *   It is deprecated to call [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")
         and [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
         checks on protocol classes that were not explicitly decorated with `runtime_checkable()` but that inherit from a runtime-checkable protocol class. This will raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
         in Python 3.20.
        
        (Contributed by Bartosz Sławecki in [gh-132604](https://github.com/python/cpython/issues/132604)
        .)
        

### Pending removal in future versions[¶](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-future-versions "Link to this heading")

The following APIs will be removed in the future, although there is currently no date scheduled for their removal.

*   [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
    :
    
    *   Nesting argument groups and nesting mutually exclusive groups are deprecated.
        
    *   Passing the undocumented keyword argument _prefix\_chars_ to [`add_argument_group()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "argparse.ArgumentParser.add_argument_group")
         is now deprecated.
        
    *   The [`argparse.FileType`](https://docs.python.org/3/library/argparse.html#argparse.FileType "argparse.FileType")
         type converter is deprecated.
        
*   [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")
    :
    
    *   Generators: `throw(type, exc, tb)` and `athrow(type, exc, tb)` signature is deprecated: use `throw(exc)` and `athrow(exc)` instead, the single argument signature.
        
    *   Currently Python accepts numeric literals immediately followed by keywords, for example `0in x`, `1or x`, `0if 1else 2`. It allows confusing and ambiguous expressions like `[0x1for x in y]` (which can be interpreted as `[0x1 for x in y]` or `[0x1f or x in y]`). A syntax warning is raised if the numeric literal is immediately followed by one of keywords [`and`](https://docs.python.org/3/reference/expressions.html#and)
        , [`else`](https://docs.python.org/3/reference/compound_stmts.html#else)
        , [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)
        , [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)
        , [`in`](https://docs.python.org/3/reference/expressions.html#in)
        , [`is`](https://docs.python.org/3/reference/expressions.html#is)
         and [`or`](https://docs.python.org/3/reference/expressions.html#or)
        . In a future release it will be changed to a syntax error. ([gh-87999](https://github.com/python/cpython/issues/87999)
        )
        
    *   Support for `__index__()` and `__int__()` method returning non-int type: these methods will be required to return an instance of a strict subclass of [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
        .
        
    *   Support for `__float__()` method returning a strict subclass of [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
        : these methods will be required to return an instance of `float`.
        
    *   Support for `__complex__()` method returning a strict subclass of [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
        : these methods will be required to return an instance of `complex`.
        
    *   Passing a complex number as the _real_ or _imag_ argument in the [`complex()`](https://docs.python.org/3/builtins/functions.html#complex "complex")
         constructor is now deprecated; it should only be passed as a single positional argument. (Contributed by Serhiy Storchaka in [gh-109218](https://github.com/python/cpython/issues/109218)
        .)
        
*   [`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.")
    : `calendar.January` and `calendar.February` constants are deprecated and replaced by [`calendar.JANUARY`](https://docs.python.org/3/library/calendar.html#calendar.JANUARY "calendar.JANUARY")
     and [`calendar.FEBRUARY`](https://docs.python.org/3/library/calendar.html#calendar.FEBRUARY "calendar.FEBRUARY")
    . (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636)
    .)
    
*   [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")
    : use [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
     instead of [`codecs.open()`](https://docs.python.org/3/library/codecs.html#codecs.open "codecs.open")
    . ([gh-133038](https://github.com/python/cpython/issues/133038)
    )
    
*   `codeobject.co_lnotab`: use the [`codeobject.co_lines()`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lines "codeobject.co_lines")
     method instead.
    
*   [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
    :
    
    *   [`utcnow()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow "datetime.datetime.utcnow")
        : use `datetime.datetime.now(tz=datetime.UTC)`.
        
    *   [`utcfromtimestamp()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp "datetime.datetime.utcfromtimestamp")
        : use `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`.
        
*   [`gettext`](https://docs.python.org/3/library/gettext.html#module-gettext "gettext: Multilingual internationalization services.")
    : Plural value must be an integer.
    
*   [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
    :
    
    *   [`cache_from_source()`](https://docs.python.org/3/library/importlib.html#importlib.util.cache_from_source "importlib.util.cache_from_source")
         _debug\_override_ parameter is deprecated: use the _optimization_ parameter instead.
        
*   [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html#module-importlib.metadata "importlib.metadata: Accessing package metadata")
    :
    
    *   `EntryPoints` tuple interface.
        
    *   Implicit `None` on return values.
        
*   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
    : the `warn()` method has been deprecated since Python 3.3, use [`warning()`](https://docs.python.org/3/library/logging.html#logging.warning "logging.warning")
     instead.
    
*   [`mailbox`](https://docs.python.org/3/library/mailbox.html#module-mailbox "mailbox: Manipulate mailboxes in various formats")
    : Use of StringIO input and text mode is deprecated, use BytesIO and binary mode instead.
    
*   [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
    : Calling [`os.register_at_fork()`](https://docs.python.org/3/library/os.html#os.register_at_fork "os.register_at_fork")
     in a multi-threaded process.
    
*   [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
    : [`os.path.commonprefix()`](https://docs.python.org/3/library/os.path.html#os.path.commonprefix "os.path.commonprefix")
     is deprecated, use [`os.path.commonpath()`](https://docs.python.org/3/library/os.path.html#os.path.commonpath "os.path.commonpath")
     for path prefixes. The `os.path.commonprefix()` function is being deprecated due to having a misleading name and module. The function is not safe to use for path prefixes despite being included in a module about path manipulation, meaning it is easy to accidentally introduce path traversal vulnerabilities into Python programs by using this function.
    
*   `pydoc.ErrorDuringImport`: A tuple value for _exc\_info_ parameter is deprecated, use an exception instance.
    
*   [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")
    : More strict rules are now applied for numerical group references and group names in regular expressions. Only sequence of ASCII digits is now accepted as a numerical reference. The group name in bytes patterns and replacement strings can now only contain ASCII letters and digits and underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760)
    .)
    
*   [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")
    : [`rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree")
    ’s _onerror_ parameter is deprecated in Python 3.12; use the _onexc_ parameter instead.
    
*   [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
     options and protocols:
    
    *   [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
         without protocol argument is deprecated.
        
    *   [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
        : [`set_npn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_npn_protocols "ssl.SSLContext.set_npn_protocols")
         and `selected_npn_protocol()` are deprecated: use ALPN instead.
        
    *   `ssl.OP_NO_SSL*` options
        
    *   `ssl.OP_NO_TLS*` options
        
    *   `ssl.PROTOCOL_SSLv3`
        
    *   `ssl.PROTOCOL_TLS`
        
    *   `ssl.PROTOCOL_TLSv1`
        
    *   `ssl.PROTOCOL_TLSv1_1`
        
    *   `ssl.PROTOCOL_TLSv1_2`
        
    *   `ssl.TLSVersion.SSLv3`
        
    *   `ssl.TLSVersion.TLSv1`
        
    *   `ssl.TLSVersion.TLSv1_1`
        
*   [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
     methods:
    
    *   `threading.Condition.notifyAll()`: use [`notify_all()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all")
        .
        
    *   `threading.Event.isSet()`: use [`is_set()`](https://docs.python.org/3/library/threading.html#threading.Event.is_set "threading.Event.is_set")
        .
        
    *   `threading.Thread.isDaemon()`, [`threading.Thread.setDaemon()`](https://docs.python.org/3/library/threading.html#threading.Thread.setDaemon "threading.Thread.setDaemon")
        : use [`threading.Thread.daemon`](https://docs.python.org/3/library/threading.html#threading.Thread.daemon "threading.Thread.daemon")
         attribute.
        
    *   `threading.Thread.getName()`, [`threading.Thread.setName()`](https://docs.python.org/3/library/threading.html#threading.Thread.setName "threading.Thread.setName")
        : use [`threading.Thread.name`](https://docs.python.org/3/library/threading.html#threading.Thread.name "threading.Thread.name")
         attribute.
        
    *   `threading.currentThread()`: use [`threading.current_thread()`](https://docs.python.org/3/library/threading.html#threading.current_thread "threading.current_thread")
        .
        
    *   `threading.activeCount()`: use [`threading.active_count()`](https://docs.python.org/3/library/threading.html#threading.active_count "threading.active_count")
        .
        
*   [`typing.Text`](https://docs.python.org/3/library/typing.html#typing.Text "typing.Text")
     ([gh-92332](https://github.com/python/cpython/issues/92332)
    ).
    
*   The internal class `typing._UnionGenericAlias` is no longer used to implement [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")
    . To preserve compatibility with users using this private class, a compatibility shim will be provided until at least Python 3.17. (Contributed by Jelle Zijlstra in [gh-105499](https://github.com/python/cpython/issues/105499)
    .)
    
*   [`unittest.IsolatedAsyncioTestCase`](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase "unittest.IsolatedAsyncioTestCase")
    : it is deprecated to return a value that is not `None` from a test case.
    
*   [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse "urllib.parse: Parse URLs into or assemble them from components.")
     deprecated functions: [`urlparse()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse "urllib.parse.urlparse")
     instead
    
    *   `splitattr()`
        
    *   `splithost()`
        
    *   `splitnport()`
        
    *   `splitpasswd()`
        
    *   `splitport()`
        
    *   `splitquery()`
        
    *   `splittag()`
        
    *   `splittype()`
        
    *   `splituser()`
        
    *   `splitvalue()`
        
    *   `to_bytes()`
        
*   [`wsgiref`](https://docs.python.org/3/library/wsgiref.html#module-wsgiref "wsgiref: WSGI Utilities and Reference Implementation.")
    : `SimpleHandler.stdout.write()` should not do partial writes.
    
*   [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")
    : Testing the truth value of an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
     is deprecated. In a future release it will always return `True`. Prefer explicit `len(elem)` or `elem is not None` tests instead.
    
*   [`sys._clear_type_cache()`](https://docs.python.org/3/library/sys.html#sys._clear_type_cache "sys._clear_type_cache")
     is deprecated: use [`sys._clear_internal_caches()`](https://docs.python.org/3/library/sys.html#sys._clear_internal_caches "sys._clear_internal_caches")
     instead.
    

CPython Bytecode Changes[¶](https://docs.python.org/3/whatsnew/3.13.html#cpython-bytecode-changes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

*   The oparg of [`YIELD_VALUE`](https://docs.python.org/3/library/dis.html#opcode-YIELD_VALUE)
     is now `1` if the yield is part of a yield-from or await, and `0` otherwise. The oparg of [`RESUME`](https://docs.python.org/3/library/dis.html#opcode-RESUME)
     was changed to add a bit indicating if the except-depth is 1, which is needed to optimize closing of generators. (Contributed by Irit Katriel in [gh-111354](https://github.com/python/cpython/issues/111354)
    .)
    

C API Changes[¶](https://docs.python.org/3/whatsnew/3.13.html#c-api-changes "Link to this heading")

----------------------------------------------------------------------------------------------------

### New Features[¶](https://docs.python.org/3/whatsnew/3.13.html#id7 "Link to this heading")

*   Add the [PyMonitoring C API](https://docs.python.org/3/c-api/monitoring.html#c-api-monitoring)
     for generating [**PEP 669**](https://peps.python.org/pep-0669/)
     monitoring events:
    
    *   [`PyMonitoringState`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
        
    *   [`PyMonitoring_FirePyStartEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyStartEvent "PyMonitoring_FirePyStartEvent")
        
    *   [`PyMonitoring_FirePyResumeEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyResumeEvent "PyMonitoring_FirePyResumeEvent")
        
    *   [`PyMonitoring_FirePyReturnEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyReturnEvent "PyMonitoring_FirePyReturnEvent")
        
    *   [`PyMonitoring_FirePyYieldEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyYieldEvent "PyMonitoring_FirePyYieldEvent")
        
    *   [`PyMonitoring_FireCallEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireCallEvent "PyMonitoring_FireCallEvent")
        
    *   [`PyMonitoring_FireLineEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireLineEvent "PyMonitoring_FireLineEvent")
        
    *   [`PyMonitoring_FireJumpEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireJumpEvent "PyMonitoring_FireJumpEvent")
        
    *   `PyMonitoring_FireBranchEvent`
        
    *   [`PyMonitoring_FireCReturnEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireCReturnEvent "PyMonitoring_FireCReturnEvent")
        
    *   [`PyMonitoring_FirePyThrowEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyThrowEvent "PyMonitoring_FirePyThrowEvent")
        
    *   [`PyMonitoring_FireRaiseEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireRaiseEvent "PyMonitoring_FireRaiseEvent")
        
    *   [`PyMonitoring_FireCRaiseEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireCRaiseEvent "PyMonitoring_FireCRaiseEvent")
        
    *   [`PyMonitoring_FireReraiseEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireReraiseEvent "PyMonitoring_FireReraiseEvent")
        
    *   [`PyMonitoring_FireExceptionHandledEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireExceptionHandledEvent "PyMonitoring_FireExceptionHandledEvent")
        
    *   [`PyMonitoring_FirePyUnwindEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyUnwindEvent "PyMonitoring_FirePyUnwindEvent")
        
    *   [`PyMonitoring_FireStopIterationEvent()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireStopIterationEvent "PyMonitoring_FireStopIterationEvent")
        
    *   [`PyMonitoring_EnterScope()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_EnterScope "PyMonitoring_EnterScope")
        
    *   [`PyMonitoring_ExitScope()`](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_ExitScope "PyMonitoring_ExitScope")
        
    
    (Contributed by Irit Katriel in [gh-111997](https://github.com/python/cpython/issues/111997)
    ).
    
*   Add [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
    , a lightweight mutex that occupies a single byte, and the new [`PyMutex_Lock()`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex_Lock "PyMutex_Lock")
     and [`PyMutex_Unlock()`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex_Unlock "PyMutex_Unlock")
     functions. `PyMutex_Lock()` will release the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
     (if currently held) if the operation needs to block. (Contributed by Sam Gross in [gh-108724](https://github.com/python/cpython/issues/108724)
    .)
    
*   Add the [PyTime C API](https://docs.python.org/3/c-api/time.html#c-api-time)
     to provide access to system clocks:
    
    *   [`PyTime_t`](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
        .
        
    *   [`PyTime_MIN`](https://docs.python.org/3/c-api/time.html#c.PyTime_MIN "PyTime_MIN")
         and [`PyTime_MAX`](https://docs.python.org/3/c-api/time.html#c.PyTime_MAX "PyTime_MAX")
        .
        
    *   [`PyTime_AsSecondsDouble()`](https://docs.python.org/3/c-api/time.html#c.PyTime_AsSecondsDouble "PyTime_AsSecondsDouble")
        .
        
    *   [`PyTime_Monotonic()`](https://docs.python.org/3/c-api/time.html#c.PyTime_Monotonic "PyTime_Monotonic")
        .
        
    *   [`PyTime_MonotonicRaw()`](https://docs.python.org/3/c-api/time.html#c.PyTime_MonotonicRaw "PyTime_MonotonicRaw")
        .
        
    *   [`PyTime_PerfCounter()`](https://docs.python.org/3/c-api/time.html#c.PyTime_PerfCounter "PyTime_PerfCounter")
        .
        
    *   [`PyTime_PerfCounterRaw()`](https://docs.python.org/3/c-api/time.html#c.PyTime_PerfCounterRaw "PyTime_PerfCounterRaw")
        .
        
    *   [`PyTime_Time()`](https://docs.python.org/3/c-api/time.html#c.PyTime_Time "PyTime_Time")
        .
        
    *   [`PyTime_TimeRaw()`](https://docs.python.org/3/c-api/time.html#c.PyTime_TimeRaw "PyTime_TimeRaw")
        .
        
    
    (Contributed by Victor Stinner and Petr Viktorin in [gh-110850](https://github.com/python/cpython/issues/110850)
    .)
    
*   Add the [`PyDict_ContainsString()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_ContainsString "PyDict_ContainsString")
     function with the same behavior as [`PyDict_Contains()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Contains "PyDict_Contains")
    , but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
    \*. (Contributed by Victor Stinner in [gh-108314](https://github.com/python/cpython/issues/108314)
    .)
    
*   Add the [`PyDict_GetItemRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemRef "PyDict_GetItemRef")
     and [`PyDict_GetItemStringRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemStringRef "PyDict_GetItemStringRef")
     functions, which behave similarly to [`PyDict_GetItemWithError()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemWithError "PyDict_GetItemWithError")
    , but return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     instead of a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
    . Moreover, these functions return `-1` on error, removing the need to check `PyErr_Occurred()`. (Contributed by Victor Stinner in [gh-106004](https://github.com/python/cpython/issues/106004)
    .)
    
*   Add the [`PyDict_SetDefaultRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetDefaultRef "PyDict_SetDefaultRef")
     function, which behaves similarly to [`PyDict_SetDefault()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetDefault "PyDict_SetDefault")
    , but returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     instead of a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
    . This function returns `-1` on error, `0` on insertion, and `1` if the key was already present in the dictionary. (Contributed by Sam Gross in [gh-112066](https://github.com/python/cpython/issues/112066)
    .)
    
*   Add the [`PyDict_Pop()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Pop "PyDict_Pop")
     and [`PyDict_PopString()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_PopString "PyDict_PopString")
     functions to remove a key from a dictionary and optionally return the removed value. This is similar to [`dict.pop()`](https://docs.python.org/3/builtins/stdtypes.html#dict.pop "dict.pop")
    , though there is no default value, and [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
     is not raised for missing keys. (Contributed by Stefan Behnel and Victor Stinner in [gh-111262](https://github.com/python/cpython/issues/111262)
    .)
    
*   Add the [`PyMapping_GetOptionalItem()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetOptionalItem "PyMapping_GetOptionalItem")
     and [`PyMapping_GetOptionalItemString()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetOptionalItemString "PyMapping_GetOptionalItemString")
     functions as alternatives to [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
     and [`PyMapping_GetItemString()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetItemString "PyMapping_GetItemString")
     respectively. The new functions do not raise [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
     if the requested key is missing from the mapping. These variants are more convenient and faster if a missing key should not be treated as a failure. (Contributed by Serhiy Storchaka in [gh-106307](https://github.com/python/cpython/issues/106307)
    .)
    
*   Add the [`PyObject_GetOptionalAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttr "PyObject_GetOptionalAttr")
     and [`PyObject_GetOptionalAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttrString "PyObject_GetOptionalAttrString")
     functions as alternatives to [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
     and [`PyObject_GetAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttrString "PyObject_GetAttrString")
     respectively. The new functions do not raise [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
     if the requested attribute is not found on the object. These variants are more convenient and faster if the missing attribute should not be treated as a failure. (Contributed by Serhiy Storchaka in [gh-106521](https://github.com/python/cpython/issues/106521)
    .)
    
*   Add the [`PyErr_FormatUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_FormatUnraisable "PyErr_FormatUnraisable")
     function as an extension to [`PyErr_WriteUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WriteUnraisable "PyErr_WriteUnraisable")
     that allows customizing the warning message. (Contributed by Serhiy Storchaka in [gh-108082](https://github.com/python/cpython/issues/108082)
    .)
    
*   Add new functions that return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     instead of a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
     for frame locals, globals, and builtins, as part of [PEP 667](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-locals-semantics)
    :
    
    *   [`PyEval_GetFrameBuiltins()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameBuiltins "PyEval_GetFrameBuiltins")
         replaces [`PyEval_GetBuiltins()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetBuiltins "PyEval_GetBuiltins")
        
    *   [`PyEval_GetFrameGlobals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameGlobals "PyEval_GetFrameGlobals")
         replaces [`PyEval_GetGlobals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetGlobals "PyEval_GetGlobals")
        
    *   [`PyEval_GetFrameLocals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameLocals "PyEval_GetFrameLocals")
         replaces [`PyEval_GetLocals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetLocals "PyEval_GetLocals")
        
    
    (Contributed by Mark Shannon and Tian Gao in [gh-74929](https://github.com/python/cpython/issues/74929)
    .)
    
*   Add the [`Py_GetConstant()`](https://docs.python.org/3/c-api/object.html#c.Py_GetConstant "Py_GetConstant")
     and [`Py_GetConstantBorrowed()`](https://docs.python.org/3/c-api/object.html#c.Py_GetConstantBorrowed "Py_GetConstantBorrowed")
     functions to get [strong](https://docs.python.org/3/glossary.html#term-strong-reference)
     or [borrowed](https://docs.python.org/3/glossary.html#term-borrowed-reference)
     references to constants. For example, `Py_GetConstant(Py_CONSTANT_ZERO)` returns a strong reference to the constant zero. (Contributed by Victor Stinner in [gh-115754](https://github.com/python/cpython/issues/115754)
    .)
    
*   Add the [`PyImport_AddModuleRef()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModuleRef "PyImport_AddModuleRef")
     function as a replacement for [`PyImport_AddModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModule "PyImport_AddModule")
     that returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     instead of a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
    . (Contributed by Victor Stinner in [gh-105922](https://github.com/python/cpython/issues/105922)
    .)
    
*   Add the [`Py_IsFinalizing()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IsFinalizing "Py_IsFinalizing")
     function to check whether the main Python interpreter is [shutting down](https://docs.python.org/3/glossary.html#term-interpreter-shutdown)
    . (Contributed by Victor Stinner in [gh-108014](https://github.com/python/cpython/issues/108014)
    .)
    
*   Add the [`PyList_GetItemRef()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItemRef "PyList_GetItemRef")
     function as a replacement for [`PyList_GetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem "PyList_GetItem")
     that returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     instead of a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
    . (Contributed by Sam Gross in [gh-114329](https://github.com/python/cpython/issues/114329)
    .)
    
*   Add the [`PyList_Extend()`](https://docs.python.org/3/c-api/list.html#c.PyList_Extend "PyList_Extend")
     and [`PyList_Clear()`](https://docs.python.org/3/c-api/list.html#c.PyList_Clear "PyList_Clear")
     functions, mirroring the Python [`list.extend()`](https://docs.python.org/3/builtins/stdtypes.html#list.extend "list.extend")
     and [`list.clear()`](https://docs.python.org/3/builtins/stdtypes.html#list.clear "list.clear")
     methods. (Contributed by Victor Stinner in [gh-111138](https://github.com/python/cpython/issues/111138)
    .)
    
*   Add the [`PyLong_AsInt()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsInt "PyLong_AsInt")
     function. It behaves similarly to [`PyLong_AsLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLong "PyLong_AsLong")
    , but stores the result in a C int instead of a C long. (Contributed by Victor Stinner in [gh-108014](https://github.com/python/cpython/issues/108014)
    .)
    
*   Add the [`PyLong_AsNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsNativeBytes "PyLong_AsNativeBytes")
    , [`PyLong_FromNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromNativeBytes "PyLong_FromNativeBytes")
    , and [`PyLong_FromUnsignedNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUnsignedNativeBytes "PyLong_FromUnsignedNativeBytes")
     functions to simplify converting between native integer types and Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
     objects. (Contributed by Steve Dower in [gh-111140](https://github.com/python/cpython/issues/111140)
    .)
    
*   Add [`PyModule_Add()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Add "PyModule_Add")
     function, which is similar to [`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef")
     and [`PyModule_AddObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObject "PyModule_AddObject")
    , but always steals a reference to the value. (Contributed by Serhiy Storchaka in [gh-86493](https://github.com/python/cpython/issues/86493)
    .)
    
*   Add the [`PyObject_GenericHash()`](https://docs.python.org/3/c-api/hash.html#c.PyObject_GenericHash "PyObject_GenericHash")
     function that implements the default hashing function of a Python object. (Contributed by Serhiy Storchaka in [gh-113024](https://github.com/python/cpython/issues/113024)
    .)
    
*   Add the [`Py_HashPointer()`](https://docs.python.org/3/c-api/hash.html#c.Py_HashPointer "Py_HashPointer")
     function to hash a raw pointer. (Contributed by Victor Stinner in [gh-111545](https://github.com/python/cpython/issues/111545)
    .)
    
*   Add the [`PyObject_VisitManagedDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_VisitManagedDict "PyObject_VisitManagedDict")
     and [`PyObject_ClearManagedDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_ClearManagedDict "PyObject_ClearManagedDict")
     functions. which must be called by the traverse and clear functions of a type using the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
     flag. The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to use these functions with Python 3.11 and 3.12. (Contributed by Victor Stinner in [gh-107073](https://github.com/python/cpython/issues/107073)
    .)
    
*   Add the [`PyRefTracer_SetTracer()`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_SetTracer "PyRefTracer_SetTracer")
     and [`PyRefTracer_GetTracer()`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_GetTracer "PyRefTracer_GetTracer")
     functions, which enable tracking object creation and destruction in the same way that the [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")
     module does. (Contributed by Pablo Galindo in [gh-93502](https://github.com/python/cpython/issues/93502)
    .)
    
*   Add the [`PySys_AuditTuple()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AuditTuple "PySys_AuditTuple")
     function as an alternative to [`PySys_Audit()`](https://docs.python.org/3/c-api/sys.html#c.PySys_Audit "PySys_Audit")
     that takes event arguments as a Python [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
     object. (Contributed by Victor Stinner in [gh-85283](https://github.com/python/cpython/issues/85283)
    .)
    
*   Add the [`PyThreadState_GetUnchecked()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetUnchecked "PyThreadState_GetUnchecked")
     function as an alternative to [`PyThreadState_Get()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_Get "PyThreadState_Get")
     that doesn’t kill the process with a fatal error if it is `NULL`. The caller is responsible for checking if the result is `NULL`. (Contributed by Victor Stinner in [gh-108867](https://github.com/python/cpython/issues/108867)
    .)
    
*   Add the [`PyType_GetFullyQualifiedName()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetFullyQualifiedName "PyType_GetFullyQualifiedName")
     function to get the type’s fully qualified name. The module name is prepended if [`type.__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__")
     is a string and is not equal to either `'builtins'` or `'__main__'`. (Contributed by Victor Stinner in [gh-111696](https://github.com/python/cpython/issues/111696)
    .)
    
*   Add the [`PyType_GetModuleName()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleName "PyType_GetModuleName")
     function to get the type’s module name. This is equivalent to getting the [`type.__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__")
     attribute. (Contributed by Eric Snow and Victor Stinner in [gh-111696](https://github.com/python/cpython/issues/111696)
    .)
    
*   Add the [`PyUnicode_EqualToUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EqualToUTF8AndSize "PyUnicode_EqualToUTF8AndSize")
     and [`PyUnicode_EqualToUTF8()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EqualToUTF8 "PyUnicode_EqualToUTF8")
     functions to compare a Unicode object with a const char\* UTF-8 encoded string and `1` if they are equal or `0` otherwise. These functions do not raise exceptions. (Contributed by Serhiy Storchaka in [gh-110289](https://github.com/python/cpython/issues/110289)
    .)
    
*   Add the [`PyWeakref_GetRef()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef")
     function as an alternative to `PyWeakref_GetObject()` that returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     or `NULL` if the referent is no longer live. (Contributed by Victor Stinner in [gh-105927](https://github.com/python/cpython/issues/105927)
    .)
    
*   Add fixed variants of functions which silently ignore errors:
    
    *   [`PyObject_HasAttrWithError()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrWithError "PyObject_HasAttrWithError")
         replaces [`PyObject_HasAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttr "PyObject_HasAttr")
        .
        
    *   [`PyObject_HasAttrStringWithError()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrStringWithError "PyObject_HasAttrStringWithError")
         replaces [`PyObject_HasAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrString "PyObject_HasAttrString")
        .
        
    *   [`PyMapping_HasKeyWithError()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyWithError "PyMapping_HasKeyWithError")
         replaces [`PyMapping_HasKey()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKey "PyMapping_HasKey")
        .
        
    *   [`PyMapping_HasKeyStringWithError()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyStringWithError "PyMapping_HasKeyStringWithError")
         replaces [`PyMapping_HasKeyString()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyString "PyMapping_HasKeyString")
        .
        
    
    The new functions return `-1` for errors and the standard `1` for true and `0` for false.
    
    (Contributed by Serhiy Storchaka in [gh-108511](https://github.com/python/cpython/issues/108511)
    .)
    

### Changed C APIs[¶](https://docs.python.org/3/whatsnew/3.13.html#changed-c-apis "Link to this heading")

*   The _keywords_ parameter of [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords")
     and [`PyArg_VaParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_VaParseTupleAndKeywords "PyArg_VaParseTupleAndKeywords")
     now has type char \*const\* in C and const char \*const\* in C++, instead of char\*\*. In C++, this makes these functions compatible with arguments of type const char \*const\*, const char\*\*, or char \*const\* without an explicit type cast. In C, the functions only support arguments of type char \*const\*. This can be overridden with the [`PY_CXX_CONST`](https://docs.python.org/3/c-api/arg.html#c.PY_CXX_CONST "PY_CXX_CONST")
     macro. (Contributed by Serhiy Storchaka in [gh-65210](https://github.com/python/cpython/issues/65210)
    .)
    
*   [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords")
     now supports non-ASCII keyword parameter names. (Contributed by Serhiy Storchaka in [gh-110815](https://github.com/python/cpython/issues/110815)
    .)
    
*   The `PyCode_GetFirstFree()` function is now unstable API and is now named [`PyUnstable_Code_GetFirstFree()`](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_GetFirstFree "PyUnstable_Code_GetFirstFree")
    . (Contributed by Bogdan Romanyuk in [gh-115781](https://github.com/python/cpython/issues/115781)
    .)
    
*   The [`PyDict_GetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem "PyDict_GetItem")
    , [`PyDict_GetItemString()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemString "PyDict_GetItemString")
    , [`PyMapping_HasKey()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKey "PyMapping_HasKey")
    , [`PyMapping_HasKeyString()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyString "PyMapping_HasKeyString")
    , [`PyObject_HasAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttr "PyObject_HasAttr")
    , [`PyObject_HasAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrString "PyObject_HasAttrString")
    , and [`PySys_GetObject()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetObject "PySys_GetObject")
     functions, each of which clears all errors which occurred when calling them now reports these errors using [`sys.unraisablehook()`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook")
    . You may replace them with other functions as recommended in the documentation. (Contributed by Serhiy Storchaka in [gh-106672](https://github.com/python/cpython/issues/106672)
    .)
    
*   Add support for the `%T`, `%#T`, `%N` and `%#N` formats to [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
    :
    
    *   `%T`: Get the fully qualified name of an object type
        
    *   `%#T`: As above, but use a colon as the separator
        
    *   `%N`: Get the fully qualified name of a type
        
    *   `%#N`: As above, but use a colon as the separator
        
    
    See [**PEP 737**](https://peps.python.org/pep-0737/)
     for more information. (Contributed by Victor Stinner in [gh-111696](https://github.com/python/cpython/issues/111696)
    .)
    
*   You no longer have to define the `PY_SSIZE_T_CLEAN` macro before including `Python.h` when using `#` formats in [format codes](https://docs.python.org/3/c-api/arg.html#arg-parsing-string-and-buffers)
    . APIs accepting the format codes always use `Py_ssize_t` for `#` formats. (Contributed by Inada Naoki in [gh-104922](https://github.com/python/cpython/issues/104922)
    .)
    
*   If Python is built in [debug mode](https://docs.python.org/3/using/configure.html#debug-build)
     or [`with assertions`](https://docs.python.org/3/using/configure.html#cmdoption-with-assertions)
    , [`PyTuple_SET_ITEM()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SET_ITEM "PyTuple_SET_ITEM")
     and [`PyList_SET_ITEM()`](https://docs.python.org/3/c-api/list.html#c.PyList_SET_ITEM "PyList_SET_ITEM")
     now check the index argument with an assertion. (Contributed by Victor Stinner in [gh-106168](https://github.com/python/cpython/issues/106168)
    .)
    

### Limited C API Changes[¶](https://docs.python.org/3/whatsnew/3.13.html#limited-c-api-changes "Link to this heading")

*   The following functions are now included in the Limited C API:
    
    *   [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
        
    *   [`PyMem_RawCalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawCalloc "PyMem_RawCalloc")
        
    *   [`PyMem_RawRealloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
        
    *   [`PyMem_RawFree()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawFree "PyMem_RawFree")
        
    *   [`PySys_Audit()`](https://docs.python.org/3/c-api/sys.html#c.PySys_Audit "PySys_Audit")
        
    *   [`PySys_AuditTuple()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AuditTuple "PySys_AuditTuple")
        
    *   [`PyType_GetModuleByDef()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByDef "PyType_GetModuleByDef")
        
    
    (Contributed by Victor Stinner in [gh-85283](https://github.com/python/cpython/issues/85283)
     and [gh-116936](https://github.com/python/cpython/issues/116936)
    .)
    
*   Python built with [`--with-trace-refs`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs)
     (tracing references) now supports the [Limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
    . (Contributed by Victor Stinner in [gh-108634](https://github.com/python/cpython/issues/108634)
    .)
    

### Removed C APIs[¶](https://docs.python.org/3/whatsnew/3.13.html#removed-c-apis "Link to this heading")

*   Remove several functions, macros, variables, etc with names prefixed by `_Py` or `_PY` (which are considered private). If your project is affected by one of these removals and you believe that the removed API should remain available, please [open a new issue](https://docs.python.org/3/bugs.html#using-the-tracker)
     to request a public C API and add `cc: @vstinner` to the issue to notify Victor Stinner. (Contributed by Victor Stinner in [gh-106320](https://github.com/python/cpython/issues/106320)
    .)
    
*   Remove old buffer protocols deprecated in Python 3.0. Use [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
     instead.
    
    *   `PyObject_CheckReadBuffer()`: Use [`PyObject_CheckBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_CheckBuffer "PyObject_CheckBuffer")
         to test whether the object supports the buffer protocol. Note that `PyObject_CheckBuffer()` doesn’t guarantee that [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
         will succeed. To test if the object is actually readable, see the next example of `PyObject_GetBuffer()`.
        
    *   `PyObject_AsCharBuffer()`, `PyObject_AsReadBuffer()`: Use [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
         and [`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
         instead:
        
        Py\_buffer view;
        if (PyObject\_GetBuffer(obj, &view, PyBUF\_SIMPLE) < 0) {
            return NULL;
        }
        // Use \`view.buf\` and \`view.len\` to read from the buffer.
        // You may need to cast buf as \`(const char\*)view.buf\`.
        PyBuffer\_Release(&view);
        
    *   `PyObject_AsWriteBuffer()`: Use [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
         and [`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
         instead:
        
        Py\_buffer view;
        if (PyObject\_GetBuffer(obj, &view, PyBUF\_WRITABLE) < 0) {
            return NULL;
        }
        // Use \`view.buf\` and \`view.len\` to write to the buffer.
        PyBuffer\_Release(&view);
        
    
    (Contributed by Inada Naoki in [gh-85275](https://github.com/python/cpython/issues/85275)
    .)
    
*   Remove various functions deprecated in Python 3.9:
    
    *   `PyEval_CallObject()`, `PyEval_CallObjectWithKeywords()`: Use [`PyObject_CallNoArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallNoArgs "PyObject_CallNoArgs")
         or [`PyObject_Call()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Call "PyObject_Call")
         instead.
        
        Warning
        
        In [`PyObject_Call()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Call "PyObject_Call")
        , positional arguments must be a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
         and must not be `NULL`, and keyword arguments must be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
         or `NULL`, whereas the removed functions checked argument types and accepted `NULL` positional and keyword arguments. To replace `PyEval_CallObjectWithKeywords(func, NULL, kwargs)` with `PyObject_Call()`, pass an empty tuple as positional arguments using [`PyTuple_New(0)`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_New "PyTuple_New")
        .
        
    *   `PyEval_CallFunction()`: Use [`PyObject_CallFunction()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallFunction "PyObject_CallFunction")
         instead.
        
    *   `PyEval_CallMethod()`: Use [`PyObject_CallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethod "PyObject_CallMethod")
         instead.
        
    *   `PyCFunction_Call()`: Use [`PyObject_Call()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Call "PyObject_Call")
         instead.
        
    
    (Contributed by Victor Stinner in [gh-105107](https://github.com/python/cpython/issues/105107)
    .)
    
*   Remove the following old functions to configure the Python initialization, deprecated in Python 3.11:
    
    *   `PySys_AddWarnOptionUnicode()`: Use [`PyConfig.warnoptions`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.warnoptions "PyConfig.warnoptions")
         instead.
        
    *   `PySys_AddWarnOption()`: Use [`PyConfig.warnoptions`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.warnoptions "PyConfig.warnoptions")
         instead.
        
    *   `PySys_AddXOption()`: Use [`PyConfig.xoptions`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.xoptions "PyConfig.xoptions")
         instead.
        
    *   `PySys_HasWarnOptions()`: Use [`PyConfig.warnoptions`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.warnoptions "PyConfig.warnoptions")
         instead.
        
    *   `PySys_SetPath()`: Set [`PyConfig.module_search_paths`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths "PyConfig.module_search_paths")
         instead.
        
    *   `Py_SetPath()`: Set [`PyConfig.module_search_paths`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.module_search_paths "PyConfig.module_search_paths")
         instead.
        
    *   `Py_SetStandardStreamEncoding()`: Set [`PyConfig.stdio_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdio_encoding "PyConfig.stdio_encoding")
         instead, and set also maybe [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.legacy_windows_stdio "PyConfig.legacy_windows_stdio")
         (on Windows).
        
    *   `_Py_SetProgramFullPath()`: Set [`PyConfig.executable`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.executable "PyConfig.executable")
         instead.
        
    
    Use the new [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
     API of the [Python Initialization Configuration](https://docs.python.org/3/c-api/init_config.html#init-config)
     instead ([**PEP 587**](https://peps.python.org/pep-0587/)
    ), added to Python 3.8. (Contributed by Victor Stinner in [gh-105145](https://github.com/python/cpython/issues/105145)
    .)
    
*   Remove `PyEval_AcquireLock()` and `PyEval_ReleaseLock()` functions, deprecated in Python 3.2. They didn’t update the current thread state. They can be replaced with:
    
    *   [`PyEval_SaveThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_SaveThread "PyEval_SaveThread")
         and [`PyEval_RestoreThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_RestoreThread "PyEval_RestoreThread")
        ;
        
    *   low-level [`PyEval_AcquireThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_AcquireThread "PyEval_AcquireThread")
         and [`PyEval_ReleaseThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_ReleaseThread "PyEval_ReleaseThread")
        ;
        
    *   or [`PyGILState_Ensure()`](https://docs.python.org/3/c-api/threads.html#c.PyGILState_Ensure "PyGILState_Ensure")
         and [`PyGILState_Release()`](https://docs.python.org/3/c-api/threads.html#c.PyGILState_Release "PyGILState_Release")
        .
        
    
    (Contributed by Victor Stinner in [gh-105182](https://github.com/python/cpython/issues/105182)
    .)
    
*   Remove the `PyEval_ThreadsInitialized()` function, deprecated in Python 3.9. Since Python 3.7, `Py_Initialize()` always creates the GIL: calling `PyEval_InitThreads()` does nothing and `PyEval_ThreadsInitialized()` always returns non-zero. (Contributed by Victor Stinner in [gh-105182](https://github.com/python/cpython/issues/105182)
    .)
    
*   Remove the `_PyInterpreterState_Get()` alias to [`PyInterpreterState_Get()`](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState_Get "PyInterpreterState_Get")
     which was kept for backward compatibility with Python 3.8. The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get `PyInterpreterState_Get()` on Python 3.8 and older. (Contributed by Victor Stinner in [gh-106320](https://github.com/python/cpython/issues/106320)
    .)
    
*   Remove the private `_PyObject_FastCall()` function: use `PyObject_Vectorcall()` which is available since Python 3.8 ([**PEP 590**](https://peps.python.org/pep-0590/)
    ). (Contributed by Victor Stinner in [gh-106023](https://github.com/python/cpython/issues/106023)
    .)
    
*   Remove the `cpython/pytime.h` header file, which only contained private functions. (Contributed by Victor Stinner in [gh-106316](https://github.com/python/cpython/issues/106316)
    .)
    
*   Remove the undocumented `PY_TIMEOUT_MAX` constant from the limited C API. (Contributed by Victor Stinner in [gh-110014](https://github.com/python/cpython/issues/110014)
    .)
    
*   Remove the old trashcan macros `Py_TRASHCAN_SAFE_BEGIN` and `Py_TRASHCAN_SAFE_END`. Replace both with the new macros `Py_TRASHCAN_BEGIN` and `Py_TRASHCAN_END`. (Contributed by Irit Katriel in [gh-105111](https://github.com/python/cpython/issues/105111)
    .)
    

### Deprecated C APIs[¶](https://docs.python.org/3/whatsnew/3.13.html#deprecated-c-apis "Link to this heading")

*   Deprecate old Python initialization functions:
    
    *   `PySys_ResetWarnOptions()`: Clear [`sys.warnoptions`](https://docs.python.org/3/library/sys.html#sys.warnoptions "sys.warnoptions")
         and `warnings.filters` instead.
        
    *   `Py_GetExecPrefix()`: Get [`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix")
         instead.
        
    *   `Py_GetPath()`: Get [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
         instead.
        
    *   `Py_GetPrefix()`: Get [`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix")
         instead.
        
    *   `Py_GetProgramFullPath()`: Get [`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")
         instead.
        
    *   `Py_GetProgramName()`: Get [`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")
         instead.
        
    *   `Py_GetPythonHome()`: Get [`PyConfig.home`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.home "PyConfig.home")
         or the [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
         environment variable instead.
        
    
    (Contributed by Victor Stinner in [gh-105145](https://github.com/python/cpython/issues/105145)
    .)
    
*   [Soft deprecate](https://docs.python.org/3/glossary.html#term-soft-deprecated)
     the [`PyEval_GetBuiltins()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetBuiltins "PyEval_GetBuiltins")
    , [`PyEval_GetGlobals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetGlobals "PyEval_GetGlobals")
    , and [`PyEval_GetLocals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetLocals "PyEval_GetLocals")
     functions, which return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
    . (Soft deprecated as part of [**PEP 667**](https://peps.python.org/pep-0667/)
    .)
    
*   Deprecate the `PyImport_ImportModuleNoBlock()` function, which is just an alias to [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
     since Python 3.3. (Contributed by Victor Stinner in [gh-105396](https://github.com/python/cpython/issues/105396)
    .)
    
*   [Soft deprecate](https://docs.python.org/3/glossary.html#term-soft-deprecated)
     the [`PyModule_AddObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObject "PyModule_AddObject")
     function. It should be replaced with [`PyModule_Add()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Add "PyModule_Add")
     or [`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef")
    . (Contributed by Serhiy Storchaka in [gh-86493](https://github.com/python/cpython/issues/86493)
    .)
    
*   Deprecate the old `Py_UNICODE` and `PY_UNICODE_TYPE` types and the `Py_UNICODE_WIDE` define. Use the `wchar_t` type directly instead. Since Python 3.3, `Py_UNICODE` and `PY_UNICODE_TYPE` are just aliases to `wchar_t`. (Contributed by Victor Stinner in [gh-105156](https://github.com/python/cpython/issues/105156)
    .)
    
*   Deprecate the `PyWeakref_GetObject()` and `PyWeakref_GET_OBJECT()` functions, which return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
    . Replace them with the new [`PyWeakref_GetRef()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef")
     function, which returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
    . The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get `PyWeakref_GetRef()` on Python 3.12 and older. (Contributed by Victor Stinner in [gh-105927](https://github.com/python/cpython/issues/105927)
    .)
    

#### Pending removal in Python 3.14[¶](https://docs.python.org/3/whatsnew/3.13.html#id8 "Link to this heading")

*   The `ma_version_tag` field in [`PyDictObject`](https://docs.python.org/3/c-api/dict.html#c.PyDictObject "PyDictObject")
     for extension modules ([**PEP 699**](https://peps.python.org/pep-0699/)
    ; [gh-101193](https://github.com/python/cpython/issues/101193)
    ).
    
*   Creating [`immutable types`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Py_TPFLAGS_IMMUTABLETYPE")
     with mutable bases ([gh-95388](https://github.com/python/cpython/issues/95388)
    ).
    

#### Pending removal in Python 3.15[¶](https://docs.python.org/3/whatsnew/3.13.html#id9 "Link to this heading")

*   The `PyImport_ImportModuleNoBlock()`: Use [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
     instead.
    
*   `PyWeakref_GetObject()` and `PyWeakref_GET_OBJECT()`: Use [`PyWeakref_GetRef()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef")
     instead. The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get `PyWeakref_GetRef()` on Python 3.12 and older.
    
*   `PyUnicode_AsDecodedObject()`: Use [`PyCodec_Decode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")
     instead.
    
*   `PyUnicode_AsDecodedUnicode()`: Use [`PyCodec_Decode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")
     instead; Note that some codecs (for example, “base64”) may return a type other than [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    , such as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    .
    
*   `PyUnicode_AsEncodedObject()`: Use [`PyCodec_Encode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")
     instead.
    
*   `PyUnicode_AsEncodedUnicode()`: Use [`PyCodec_Encode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")
     instead; Note that some codecs (for example, “base64”) may return a type other than [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    , such as [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    .
    
*   Python initialization functions, deprecated in Python 3.13:
    
    *   `Py_GetPath()`: Use [`PyConfig_Get("module_search_paths")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
        ) instead.
        
    *   `Py_GetPrefix()`: Use [`PyConfig_Get("base_prefix")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix")
        ) instead. Use `PyConfig_Get("prefix")` ([`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix")
        ) if [virtual environments](https://docs.python.org/3/library/venv.html#venv-def)
         need to be handled.
        
    *   `Py_GetExecPrefix()`: Use [`PyConfig_Get("base_exec_prefix")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.base_exec_prefix`](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix")
        ) instead. Use `PyConfig_Get("exec_prefix")` ([`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix")
        ) if [virtual environments](https://docs.python.org/3/library/venv.html#venv-def)
         need to be handled.
        
    *   `Py_GetProgramFullPath()`: Use [`PyConfig_Get("executable")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")
        ) instead.
        
    *   `Py_GetProgramName()`: Use [`PyConfig_Get("executable")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         ([`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")
        ) instead.
        
    *   `Py_GetPythonHome()`: Use [`PyConfig_Get("home")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         or the [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
         environment variable instead.
        
    
    The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
     on Python 3.13 and older.
    
*   Functions to configure Python’s initialization, deprecated in Python 3.11:
    
    *   `PySys_SetArgvEx()`: Set [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
         instead.
        
    *   `PySys_SetArgv()`: Set [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
         instead.
        
    *   `Py_SetProgramName()`: Set [`PyConfig.program_name`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.program_name "PyConfig.program_name")
         instead.
        
    *   `Py_SetPythonHome()`: Set [`PyConfig.home`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.home "PyConfig.home")
         instead.
        
    *   `PySys_ResetWarnOptions()`: Clear [`sys.warnoptions`](https://docs.python.org/3/library/sys.html#sys.warnoptions "sys.warnoptions")
         and `warnings.filters` instead.
        
    
    The [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
     API should be used with [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
     instead.
    
*   Global configuration variables:
    
    *   [`Py_DebugFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_DebugFlag "Py_DebugFlag")
        : Use [`PyConfig.parser_debug`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parser_debug "PyConfig.parser_debug")
         or [`PyConfig_Get("parser_debug")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_VerboseFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_VerboseFlag "Py_VerboseFlag")
        : Use [`PyConfig.verbose`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.verbose "PyConfig.verbose")
         or [`PyConfig_Get("verbose")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_QuietFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_QuietFlag "Py_QuietFlag")
        : Use [`PyConfig.quiet`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.quiet "PyConfig.quiet")
         or [`PyConfig_Get("quiet")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_InteractiveFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InteractiveFlag "Py_InteractiveFlag")
        : Use [`PyConfig.interactive`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.interactive "PyConfig.interactive")
         or [`PyConfig_Get("interactive")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_InspectFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InspectFlag "Py_InspectFlag")
        : Use [`PyConfig.inspect`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.inspect "PyConfig.inspect")
         or [`PyConfig_Get("inspect")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_OptimizeFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_OptimizeFlag "Py_OptimizeFlag")
        : Use [`PyConfig.optimization_level`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.optimization_level "PyConfig.optimization_level")
         or [`PyConfig_Get("optimization_level")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_NoSiteFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_NoSiteFlag "Py_NoSiteFlag")
        : Use [`PyConfig.site_import`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.site_import "PyConfig.site_import")
         or [`PyConfig_Get("site_import")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_BytesWarningFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_BytesWarningFlag "Py_BytesWarningFlag")
        : Use [`PyConfig.bytes_warning`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.bytes_warning "PyConfig.bytes_warning")
         or [`PyConfig_Get("bytes_warning")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_FrozenFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_FrozenFlag "Py_FrozenFlag")
        : Use [`PyConfig.pathconfig_warnings`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.pathconfig_warnings "PyConfig.pathconfig_warnings")
         or [`PyConfig_Get("pathconfig_warnings")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_IgnoreEnvironmentFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IgnoreEnvironmentFlag "Py_IgnoreEnvironmentFlag")
        : Use [`PyConfig.use_environment`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment")
         or [`PyConfig_Get("use_environment")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_DontWriteBytecodeFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_DontWriteBytecodeFlag "Py_DontWriteBytecodeFlag")
        : Use [`PyConfig.write_bytecode`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.write_bytecode "PyConfig.write_bytecode")
         or [`PyConfig_Get("write_bytecode")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_NoUserSiteDirectory`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_NoUserSiteDirectory "Py_NoUserSiteDirectory")
        : Use [`PyConfig.user_site_directory`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.user_site_directory "PyConfig.user_site_directory")
         or [`PyConfig_Get("user_site_directory")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_UnbufferedStdioFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_UnbufferedStdioFlag "Py_UnbufferedStdioFlag")
        : Use [`PyConfig.buffered_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.buffered_stdio "PyConfig.buffered_stdio")
         or [`PyConfig_Get("buffered_stdio")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_HashRandomizationFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_HashRandomizationFlag "Py_HashRandomizationFlag")
        : Use [`PyConfig.use_hash_seed`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_hash_seed "PyConfig.use_hash_seed")
         and [`PyConfig.hash_seed`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.hash_seed "PyConfig.hash_seed")
         or [`PyConfig_Get("hash_seed")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_IsolatedFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IsolatedFlag "Py_IsolatedFlag")
        : Use [`PyConfig.isolated`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.isolated "PyConfig.isolated")
         or [`PyConfig_Get("isolated")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_LegacyWindowsFSEncodingFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_LegacyWindowsFSEncodingFlag "Py_LegacyWindowsFSEncodingFlag")
        : Use [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding "PyPreConfig.legacy_windows_fs_encoding")
         or [`PyConfig_Get("legacy_windows_fs_encoding")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   [`Py_LegacyWindowsStdioFlag`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_LegacyWindowsStdioFlag "Py_LegacyWindowsStdioFlag")
        : Use [`PyConfig.legacy_windows_stdio`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.legacy_windows_stdio "PyConfig.legacy_windows_stdio")
         or [`PyConfig_Get("legacy_windows_stdio")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   `Py_FileSystemDefaultEncoding`, `Py_HasFileSystemDefaultEncoding`: Use [`PyConfig.filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")
         or [`PyConfig_Get("filesystem_encoding")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   `Py_FileSystemDefaultEncodeErrors`: Use [`PyConfig.filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")
         or [`PyConfig_Get("filesystem_errors")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead.
        
    *   `Py_UTF8Mode`: Use [`PyPreConfig.utf8_mode`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.utf8_mode "PyPreConfig.utf8_mode")
         or [`PyConfig_Get("utf8_mode")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
         instead. (see [`Py_PreInitialize()`](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitialize "Py_PreInitialize")
        )
        
    
    The [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
     API should be used with [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
     to set these options. Or [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")
     can be used to get these options at runtime.
    

#### Pending removal in Python 3.16[¶](https://docs.python.org/3/whatsnew/3.13.html#id10 "Link to this heading")

*   The bundled copy of `libmpdec`.
    

#### Pending removal in Python 3.18[¶](https://docs.python.org/3/whatsnew/3.13.html#id11 "Link to this heading")

*   The following private functions are deprecated and planned for removal in Python 3.18:
    
    *   `_PyBytes_Join()`: use [`PyBytes_Join()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Join "PyBytes_Join")
        .
        
    *   `_PyDict_GetItemStringWithError()`: use [`PyDict_GetItemStringRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemStringRef "PyDict_GetItemStringRef")
        .
        
    *   `_PyDict_Pop()`: use [`PyDict_Pop()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Pop "PyDict_Pop")
        .
        
    *   `_PyLong_Sign()`: use [`PyLong_GetSign()`](https://docs.python.org/3/c-api/long.html#c.PyLong_GetSign "PyLong_GetSign")
        .
        
    *   `_PyLong_FromDigits()` and `_PyLong_New()`: use [`PyLongWriter_Create()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Create "PyLongWriter_Create")
        .
        
    *   `_PyThreadState_UncheckedGet()`: use [`PyThreadState_GetUnchecked()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetUnchecked "PyThreadState_GetUnchecked")
        .
        
    *   `_PyUnicode_AsString()`: use [`PyUnicode_AsUTF8()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8 "PyUnicode_AsUTF8")
        .
        
    *   `_PyUnicodeWriter_Init()`: replace `_PyUnicodeWriter_Init(&writer)` with [`writer = PyUnicodeWriter_Create(0)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Create "PyUnicodeWriter_Create")
        .
        
    *   `_PyUnicodeWriter_Finish()`: replace `_PyUnicodeWriter_Finish(&writer)` with [`PyUnicodeWriter_Finish(writer)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Finish "PyUnicodeWriter_Finish")
        .
        
    *   `_PyUnicodeWriter_Dealloc()`: replace `_PyUnicodeWriter_Dealloc(&writer)` with [`PyUnicodeWriter_Discard(writer)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Discard "PyUnicodeWriter_Discard")
        .
        
    *   `_PyUnicodeWriter_WriteChar()`: replace `_PyUnicodeWriter_WriteChar(&writer, ch)` with [`PyUnicodeWriter_WriteChar(writer, ch)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteChar "PyUnicodeWriter_WriteChar")
        .
        
    *   `_PyUnicodeWriter_WriteStr()`: replace `_PyUnicodeWriter_WriteStr(&writer, str)` with [`PyUnicodeWriter_WriteStr(writer, str)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteStr "PyUnicodeWriter_WriteStr")
        .
        
    *   `_PyUnicodeWriter_WriteSubstring()`: replace `_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)` with [`PyUnicodeWriter_WriteSubstring(writer, str, start, end)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteSubstring "PyUnicodeWriter_WriteSubstring")
        .
        
    *   `_PyUnicodeWriter_WriteASCIIString()`: replace `_PyUnicodeWriter_WriteASCIIString(&writer, str, size)` with [`PyUnicodeWriter_WriteASCII(writer, str, size)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteASCII "PyUnicodeWriter_WriteASCII")
        .
        
    *   `_PyUnicodeWriter_WriteLatin1String()`: replace `_PyUnicodeWriter_WriteLatin1String(&writer, str, size)` by decoding the string with [`PyUnicode_DecodeLatin1()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLatin1 "PyUnicode_DecodeLatin1")
        , writing the result with [`PyUnicodeWriter_WriteStr()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteStr "PyUnicodeWriter_WriteStr")
        , and releasing the result with [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
        .
        
    *   `_PyUnicodeWriter_Prepare()`: (no replacement).
        
    *   `_PyUnicodeWriter_PrepareKind()`: (no replacement).
        
    *   `_Py_HashPointer()`: use [`Py_HashPointer()`](https://docs.python.org/3/c-api/hash.html#c.Py_HashPointer "Py_HashPointer")
        .
        
    *   `_Py_fopen_obj()`: use [`Py_fopen()`](https://docs.python.org/3/c-api/sys.html#c.Py_fopen "Py_fopen")
        .
        
    
    The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get these new public functions on Python 3.13 and older. (Contributed by Victor Stinner in [gh-128863](https://github.com/python/cpython/issues/128863)
    .)
    

#### Pending removal in future versions[¶](https://docs.python.org/3/whatsnew/3.13.html#id12 "Link to this heading")

The following APIs are deprecated and will be removed, although there is currently no date scheduled for their removal.

*   [`Py_TPFLAGS_HAVE_FINALIZE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_FINALIZE "Py_TPFLAGS_HAVE_FINALIZE")
    : Unneeded since Python 3.8.
    
*   [`PyErr_Fetch()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Fetch "PyErr_Fetch")
    : Use [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
     instead.
    
*   [`PyErr_NormalizeException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NormalizeException "PyErr_NormalizeException")
    : Use [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
     instead.
    
*   [`PyErr_Restore()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Restore "PyErr_Restore")
    : Use [`PyErr_SetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetRaisedException "PyErr_SetRaisedException")
     instead.
    
*   [`PyModule_GetFilename()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilename "PyModule_GetFilename")
    : Use [`PyModule_GetFilenameObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilenameObject "PyModule_GetFilenameObject")
     instead.
    
*   [`PyOS_AfterFork()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork "PyOS_AfterFork")
    : Use [`PyOS_AfterFork_Child()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Child "PyOS_AfterFork_Child")
     instead.
    
*   [`PySlice_GetIndicesEx()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_GetIndicesEx "PySlice_GetIndicesEx")
    : Use [`PySlice_Unpack()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_Unpack "PySlice_Unpack")
     and [`PySlice_AdjustIndices()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_AdjustIndices "PySlice_AdjustIndices")
     instead.
    
*   [`PyUnicode_READY()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READY "PyUnicode_READY")
    : Unneeded since Python 3.12
    
*   `PyErr_Display()`: Use [`PyErr_DisplayException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_DisplayException "PyErr_DisplayException")
     instead.
    
*   `_PyErr_ChainExceptions()`: Use `_PyErr_ChainExceptions1()` instead.
    
*   `PyBytesObject.ob_shash` member: call [`PyObject_Hash()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Hash "PyObject_Hash")
     instead.
    
*   Thread Local Storage (TLS) API:
    
    *   [`PyThread_create_key()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_create_key "PyThread_create_key")
        : Use [`PyThread_tss_alloc()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_alloc "PyThread_tss_alloc")
         instead.
        
    *   [`PyThread_delete_key()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_delete_key "PyThread_delete_key")
        : Use [`PyThread_tss_free()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_free "PyThread_tss_free")
         instead.
        
    *   [`PyThread_set_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_set_key_value "PyThread_set_key_value")
        : Use [`PyThread_tss_set()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_set "PyThread_tss_set")
         instead.
        
    *   [`PyThread_get_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_get_key_value "PyThread_get_key_value")
        : Use [`PyThread_tss_get()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_get "PyThread_tss_get")
         instead.
        
    *   [`PyThread_delete_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_delete_key_value "PyThread_delete_key_value")
        : Use [`PyThread_tss_delete()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_delete "PyThread_tss_delete")
         instead.
        
    *   [`PyThread_ReInitTLS()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_ReInitTLS "PyThread_ReInitTLS")
        : Unneeded since Python 3.7.
        

Build Changes[¶](https://docs.python.org/3/whatsnew/3.13.html#build-changes "Link to this heading")

----------------------------------------------------------------------------------------------------

*   `arm64-apple-ios` and `arm64-apple-ios-simulator` are both now [**PEP 11**](https://peps.python.org/pep-0011/)
     tier 3 platforms. ([PEP 730](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-platform-support)
     written and implementation contributed by Russell Keith-Magee in [gh-114099](https://github.com/python/cpython/issues/114099)
    .)
    
*   `aarch64-linux-android` and `x86_64-linux-android` are both now [**PEP 11**](https://peps.python.org/pep-0011/)
     tier 3 platforms. ([PEP 738](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-platform-support)
     written and implementation contributed by Malcolm Smith in [gh-116622](https://github.com/python/cpython/issues/116622)
    .)
    
*   `wasm32-wasi` is now a [**PEP 11**](https://peps.python.org/pep-0011/)
     tier 2 platform. (Contributed by Brett Cannon in [gh-115192](https://github.com/python/cpython/issues/115192)
    .)
    
*   `wasm32-emscripten` is no longer a [**PEP 11**](https://peps.python.org/pep-0011/)
     supported platform. (Contributed by Brett Cannon in [gh-115192](https://github.com/python/cpython/issues/115192)
    .)
    
*   Building CPython now requires a compiler with support for the C11 atomic library, GCC built-in atomic functions, or MSVC interlocked intrinsics.
    
*   Autoconf 2.71 and aclocal 1.16.5 are now required to regenerate the `configure` script. (Contributed by Christian Heimes in [gh-89886](https://github.com/python/cpython/issues/89886)
     and by Victor Stinner in [gh-112090](https://github.com/python/cpython/issues/112090)
    .)
    
*   SQLite 3.15.2 or newer is required to build the [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.")
     extension module. (Contributed by Erlend Aasland in [gh-105875](https://github.com/python/cpython/issues/105875)
    .)
    
*   CPython now bundles the [mimalloc library](https://github.com/microsoft/mimalloc/)
     by default. It is licensed under the MIT license; see [mimalloc license](https://docs.python.org/3/license.html#mimalloc-license)
    . The bundled mimalloc has custom changes, see [gh-113141](https://github.com/python/cpython/issues/113141)
     for details. (Contributed by Dino Viehland in [gh-109914](https://github.com/python/cpython/issues/109914)
    .)
    
*   The `configure` option [`--with-system-libmpdec`](https://docs.python.org/3/using/configure.html#cmdoption-with-system-libmpdec)
     now defaults to `yes`. The bundled copy of `libmpdec` will be removed in Python 3.16.
    
*   Python built with `configure` [`--with-trace-refs`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs)
     (tracing references) is now ABI compatible with the Python release build and [debug build](https://docs.python.org/3/using/configure.html#debug-build)
    . (Contributed by Victor Stinner in [gh-108634](https://github.com/python/cpython/issues/108634)
    .)
    
*   On POSIX systems, the pkg-config (`.pc`) filenames now include the ABI flags. For example, the free-threaded build generates `python-3.13t.pc` and the debug build generates `python-3.13d.pc`.
    
*   The `errno`, `fcntl`, `grp`, `md5`, `pwd`, `resource`, `termios`, `winsound`, `_ctypes_test`, `_multiprocessing.posixshmem`, `_scproxy`, `_stat`, `_statistics`, `_testconsole`, `_testimportmultiple` and `_uuid` C extensions are now built with the [limited C API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
    . (Contributed by Victor Stinner in [gh-85283](https://github.com/python/cpython/issues/85283)
    .)
    

Porting to Python 3.13[¶](https://docs.python.org/3/whatsnew/3.13.html#porting-to-python-3-13 "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

This section lists previously described changes and other bugfixes that may require changes to your code.

### Changes in the Python API[¶](https://docs.python.org/3/whatsnew/3.13.html#changes-in-the-python-api "Link to this heading")

*   [PEP 667](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-locals-semantics)
     introduces several changes to the semantics of [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
     and [`f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
    :
    
    *   Calling [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
         in an [optimized scope](https://docs.python.org/3/glossary.html#term-optimized-scope)
         now produces an independent snapshot on each call, and hence no longer implicitly updates previously returned references. Obtaining the legacy CPython behavior now requires explicit calls to update the initially returned dictionary with the results of subsequent calls to `locals()`. Code execution functions that implicitly target `locals()` (such as `exec` and `eval`) must be passed an explicit namespace to access their results in an optimized scope. (Changed as part of [**PEP 667**](https://peps.python.org/pep-0667/)
        .)
        
    *   Calling [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
         from a comprehension at module or class scope (including via `exec` or `eval`) once more behaves as if the comprehension were running as an independent nested function (i.e. the local variables from the containing scope are not included). In Python 3.12, this had changed to include the local variables from the containing scope when implementing [**PEP 709**](https://peps.python.org/pep-0709/)
        . (Changed as part of [**PEP 667**](https://peps.python.org/pep-0667/)
        .)
        
    *   Accessing [`FrameType.f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
         in an [optimized scope](https://docs.python.org/3/glossary.html#term-optimized-scope)
         now returns a write-through proxy rather than a snapshot that gets updated at ill-specified times. If a snapshot is desired, it must be created explicitly with `dict` or the proxy’s `.copy()` method. (Changed as part of [**PEP 667**](https://peps.python.org/pep-0667/)
        .)
        
*   [`functools.partial`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
     now emits a [`FutureWarning`](https://docs.python.org/3/builtins/exceptions.html#FutureWarning "FutureWarning")
     when used as a method. The behavior will change in future Python versions. Wrap it in [`staticmethod()`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
     if you want to preserve the old behavior. (Contributed by Serhiy Storchaka in [gh-121027](https://github.com/python/cpython/issues/121027)
    .)
    
*   An [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
     is now raised by [`getpass.getuser()`](https://docs.python.org/3/library/getpass.html#getpass.getuser "getpass.getuser")
     for any failure to retrieve a username, instead of [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
     on non-Unix platforms or [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
     on Unix platforms where the password database is empty.
    
*   The value of the `mode` attribute of [`gzip.GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile")
     is now a string (`'rb'` or `'wb'`) instead of an integer (`1` or `2`). The value of the `mode` attribute of the readable file-like object returned by [`zipfile.ZipFile.open()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open "zipfile.ZipFile.open")
     is now `'rb'` instead of `'r'`. (Contributed by Serhiy Storchaka in [gh-115961](https://github.com/python/cpython/issues/115961)
    .)
    
*   [`mailbox.Maildir`](https://docs.python.org/3/library/mailbox.html#mailbox.Maildir "mailbox.Maildir")
     now ignores files with a leading dot (`.`). (Contributed by Zackery Spytz in [gh-65559](https://github.com/python/cpython/issues/65559)
    .)
    
*   [`pathlib.Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob")
     and [`rglob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob "pathlib.Path.rglob")
     now return both files and directories if a pattern that ends with “`**`” is given, rather than directories only. Add a trailing slash to keep the previous behavior and only match directories.
    
*   The [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
     module now expects the `_thread` module to have an `_is_main_interpreter()` function. This function takes no arguments and returns `True` if the current interpreter is the main interpreter.
    
    Any library or application that provides a custom `_thread` module must provide `_is_main_interpreter()`, just like the module’s other “private” attributes. ([gh-112826](https://github.com/python/cpython/issues/112826)
    .)
    

### Changes in the C API[¶](https://docs.python.org/3/whatsnew/3.13.html#changes-in-the-c-api "Link to this heading")

*   `Python.h` no longer includes the `<ieeefp.h>` standard header. It was included for the `finite()` function which is now provided by the `<math.h>` header. It should now be included explicitly if needed. Remove also the `HAVE_IEEEFP_H` macro. (Contributed by Victor Stinner in [gh-108765](https://github.com/python/cpython/issues/108765)
    .)
    
*   `Python.h` no longer includes these standard header files: `<time.h>`, `<sys/select.h>` and `<sys/time.h>`. If needed, they should now be included explicitly. For example, `<time.h>` provides the `clock()` and `gmtime()` functions, `<sys/select.h>` provides the `select()` function, and `<sys/time.h>` provides the `futimes()`, `gettimeofday()` and `setitimer()` functions. (Contributed by Victor Stinner in [gh-108765](https://github.com/python/cpython/issues/108765)
    .)
    
*   On Windows, `Python.h` no longer includes the `<stddef.h>` standard header file. If needed, it should now be included explicitly. For example, it provides `offsetof()` function, and `size_t` and `ptrdiff_t` types. Including `<stddef.h>` explicitly was already needed by all other platforms, the `HAVE_STDDEF_H` macro is only defined on Windows. (Contributed by Victor Stinner in [gh-108765](https://github.com/python/cpython/issues/108765)
    .)
    
*   If the [`Py_LIMITED_API`](https://docs.python.org/3/c-api/stable.html#c.Py_LIMITED_API "Py_LIMITED_API")
     macro is defined, `Py_BUILD_CORE`, `Py_BUILD_CORE_BUILTIN` and `Py_BUILD_CORE_MODULE` macros are now undefined by `<Python.h>`. (Contributed by Victor Stinner in [gh-85283](https://github.com/python/cpython/issues/85283)
    .)
    
*   The old trashcan macros `Py_TRASHCAN_SAFE_BEGIN` and `Py_TRASHCAN_SAFE_END` were removed. They should be replaced by the new macros `Py_TRASHCAN_BEGIN` and `Py_TRASHCAN_END`.
    
    A `tp_dealloc` function that has the old macros, such as:
    
    Copy
    
    static void
    mytype\_dealloc(mytype \*p)
    {
        PyObject\_GC\_UnTrack(p);
        Py\_TRASHCAN\_SAFE\_BEGIN(p);
        ...
        Py\_TRASHCAN\_SAFE\_END(p)
    }
    
    should migrate to the new macros as follows:
    
    Copy
    
    static void
    mytype\_dealloc(mytype \*p)
    {
        PyObject\_GC\_UnTrack(p);
        Py\_TRASHCAN\_BEGIN(p, mytype\_dealloc)
        ...
        Py\_TRASHCAN\_END
    }
    
    Note that `Py_TRASHCAN_BEGIN` has a second argument which should be the deallocation function it is in. The new macros were added in Python 3.8 and the old macros were deprecated in Python 3.11. (Contributed by Irit Katriel in [gh-105111](https://github.com/python/cpython/issues/105111)
    .)
    

*   [PEP 667](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-locals-semantics)
     introduces several changes to frame-related functions:
    
    *   The effects of mutating the dictionary returned from [`PyEval_GetLocals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetLocals "PyEval_GetLocals")
         in an [optimized scope](https://docs.python.org/3/glossary.html#term-optimized-scope)
         have changed. New dict entries added this way will now _only_ be visible to subsequent `PyEval_GetLocals()` calls in that frame, as [`PyFrame_GetLocals()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals")
        , [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
        , and [`FrameType.f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
         no longer access the same underlying cached dictionary. Changes made to entries for actual variable names and names added via the write-through proxy interfaces will be overwritten on subsequent calls to `PyEval_GetLocals()` in that frame. The recommended code update depends on how the function was being used, so refer to the deprecation notice on the function for details.
        
    *   Calling [`PyFrame_GetLocals()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals")
         in an [optimized scope](https://docs.python.org/3/glossary.html#term-optimized-scope)
         now returns a write-through proxy rather than a snapshot that gets updated at ill-specified times. If a snapshot is desired, it must be created explicitly, or by calling the new [`PyEval_GetFrameLocals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameLocals "PyEval_GetFrameLocals")
         API.
        
    *   `PyFrame_FastToLocals()` and `PyFrame_FastToLocalsWithError()` no longer have any effect. Calling these functions has been redundant since Python 3.11, when [`PyFrame_GetLocals()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals")
         was first introduced.
        
    *   `PyFrame_LocalsToFast()` no longer has any effect. Calling this function is redundant now that [`PyFrame_GetLocals()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals")
         returns a write-through proxy for [optimized scopes](https://docs.python.org/3/glossary.html#term-optimized-scope)
        .
        
*   Python 3.13 removed many private functions. Some of them can be replaced using these alternatives:
    
    *   `_PyDict_Pop()`: [`PyDict_Pop()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Pop "PyDict_Pop")
         or [`PyDict_PopString()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_PopString "PyDict_PopString")
        ;
        
    *   `_PyDict_GetItemWithError()`: [`PyDict_GetItemRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemRef "PyDict_GetItemRef")
        ;
        
    *   `_PyErr_WriteUnraisableMsg()`: [`PyErr_FormatUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_FormatUnraisable "PyErr_FormatUnraisable")
        ;
        
    *   `_PyEval_SetTrace()`: [`PyEval_SetTrace()`](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetTrace "PyEval_SetTrace")
         or [`PyEval_SetTraceAllThreads()`](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetTraceAllThreads "PyEval_SetTraceAllThreads")
        ;
        
    *   `_PyList_Extend()`: [`PyList_Extend()`](https://docs.python.org/3/c-api/list.html#c.PyList_Extend "PyList_Extend")
        ;
        
    *   `_PyLong_AsInt()`: [`PyLong_AsInt()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsInt "PyLong_AsInt")
        ;
        
    *   `_PyMem_RawStrdup()`: `strdup()`;
        
    *   `_PyMem_Strdup()`: `strdup()`;
        
    *   `_PyObject_ClearManagedDict()`: [`PyObject_ClearManagedDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_ClearManagedDict "PyObject_ClearManagedDict")
        ;
        
    *   `_PyObject_VisitManagedDict()`: [`PyObject_VisitManagedDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_VisitManagedDict "PyObject_VisitManagedDict")
        ;
        
    *   `_PyThreadState_UncheckedGet()`: [`PyThreadState_GetUnchecked()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetUnchecked "PyThreadState_GetUnchecked")
        ;
        
    *   `_PyTime_AsSecondsDouble()`: [`PyTime_AsSecondsDouble()`](https://docs.python.org/3/c-api/time.html#c.PyTime_AsSecondsDouble "PyTime_AsSecondsDouble")
        ;
        
    *   `_PyTime_GetMonotonicClock()`: [`PyTime_Monotonic()`](https://docs.python.org/3/c-api/time.html#c.PyTime_Monotonic "PyTime_Monotonic")
         or [`PyTime_MonotonicRaw()`](https://docs.python.org/3/c-api/time.html#c.PyTime_MonotonicRaw "PyTime_MonotonicRaw")
        ;
        
    *   `_PyTime_GetPerfCounter()`: [`PyTime_PerfCounter()`](https://docs.python.org/3/c-api/time.html#c.PyTime_PerfCounter "PyTime_PerfCounter")
         or [`PyTime_PerfCounterRaw()`](https://docs.python.org/3/c-api/time.html#c.PyTime_PerfCounterRaw "PyTime_PerfCounterRaw")
        ;
        
    *   `_PyTime_GetSystemClock()`: [`PyTime_Time()`](https://docs.python.org/3/c-api/time.html#c.PyTime_Time "PyTime_Time")
         or [`PyTime_TimeRaw()`](https://docs.python.org/3/c-api/time.html#c.PyTime_TimeRaw "PyTime_TimeRaw")
        ;
        
    *   `_PyTime_MAX`: [`PyTime_MAX`](https://docs.python.org/3/c-api/time.html#c.PyTime_MAX "PyTime_MAX")
        ;
        
    *   `_PyTime_MIN`: [`PyTime_MIN`](https://docs.python.org/3/c-api/time.html#c.PyTime_MIN "PyTime_MIN")
        ;
        
    *   `_PyTime_t`: [`PyTime_t`](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
        ;
        
    *   `_Py_HashPointer()`: [`Py_HashPointer()`](https://docs.python.org/3/c-api/hash.html#c.Py_HashPointer "Py_HashPointer")
        ;
        
    *   `_Py_IsFinalizing()`: [`Py_IsFinalizing()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IsFinalizing "Py_IsFinalizing")
        .
        
    
    The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get most of these new functions on Python 3.12 and older.
    

Regression Test Changes[¶](https://docs.python.org/3/whatsnew/3.13.html#regression-test-changes "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

*   Python built with `configure` [`--with-pydebug`](https://docs.python.org/3/using/configure.html#cmdoption-with-pydebug)
     now supports a [`-X presite=package.module`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
     command-line option. If used, it specifies a module that should be imported early in the lifecycle of the interpreter, before `site.py` is executed. (Contributed by Łukasz Langa in [gh-110769](https://github.com/python/cpython/issues/110769)
    .)
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [What’s New In Python 3.13](https://docs.python.org/3/whatsnew/3.13.html#)
    *   [Summary – Release Highlights](https://docs.python.org/3/whatsnew/3.13.html#summary-release-highlights)
        
    *   [New Features](https://docs.python.org/3/whatsnew/3.13.html#new-features)
        *   [A better interactive interpreter](https://docs.python.org/3/whatsnew/3.13.html#a-better-interactive-interpreter)
            
        *   [Improved error messages](https://docs.python.org/3/whatsnew/3.13.html#improved-error-messages)
            
        *   [Free-threaded CPython](https://docs.python.org/3/whatsnew/3.13.html#free-threaded-cpython)
            
        *   [An experimental just-in-time (JIT) compiler](https://docs.python.org/3/whatsnew/3.13.html#an-experimental-just-in-time-jit-compiler)
            
        *   [Defined mutation semantics for `locals()`](https://docs.python.org/3/whatsnew/3.13.html#defined-mutation-semantics-for-locals)
            
        *   [Support for mobile platforms](https://docs.python.org/3/whatsnew/3.13.html#support-for-mobile-platforms)
            
    *   [Other Language Changes](https://docs.python.org/3/whatsnew/3.13.html#other-language-changes)
        
    *   [New Modules](https://docs.python.org/3/whatsnew/3.13.html#new-modules)
        
    *   [Improved Modules](https://docs.python.org/3/whatsnew/3.13.html#improved-modules)
        *   [argparse](https://docs.python.org/3/whatsnew/3.13.html#argparse)
            
        *   [array](https://docs.python.org/3/whatsnew/3.13.html#array)
            
        *   [ast](https://docs.python.org/3/whatsnew/3.13.html#ast)
            
        *   [asyncio](https://docs.python.org/3/whatsnew/3.13.html#asyncio)
            
        *   [base64](https://docs.python.org/3/whatsnew/3.13.html#base64)
            
        *   [compileall](https://docs.python.org/3/whatsnew/3.13.html#compileall)
            
        *   [concurrent.futures](https://docs.python.org/3/whatsnew/3.13.html#concurrent-futures)
            
        *   [configparser](https://docs.python.org/3/whatsnew/3.13.html#configparser)
            
        *   [copy](https://docs.python.org/3/whatsnew/3.13.html#copy)
            
        *   [ctypes](https://docs.python.org/3/whatsnew/3.13.html#ctypes)
            
        *   [dbm](https://docs.python.org/3/whatsnew/3.13.html#dbm)
            
        *   [dis](https://docs.python.org/3/whatsnew/3.13.html#dis)
            
        *   [doctest](https://docs.python.org/3/whatsnew/3.13.html#doctest)
            
        *   [email](https://docs.python.org/3/whatsnew/3.13.html#email)
            
        *   [enum](https://docs.python.org/3/whatsnew/3.13.html#enum)
            
        *   [fractions](https://docs.python.org/3/whatsnew/3.13.html#fractions)
            
        *   [glob](https://docs.python.org/3/whatsnew/3.13.html#glob)
            
        *   [importlib](https://docs.python.org/3/whatsnew/3.13.html#importlib)
            
        *   [io](https://docs.python.org/3/whatsnew/3.13.html#io)
            
        *   [ipaddress](https://docs.python.org/3/whatsnew/3.13.html#ipaddress)
            
        *   [itertools](https://docs.python.org/3/whatsnew/3.13.html#itertools)
            
        *   [marshal](https://docs.python.org/3/whatsnew/3.13.html#marshal)
            
        *   [math](https://docs.python.org/3/whatsnew/3.13.html#math)
            
        *   [mimetypes](https://docs.python.org/3/whatsnew/3.13.html#mimetypes)
            
        *   [mmap](https://docs.python.org/3/whatsnew/3.13.html#mmap)
            
        *   [multiprocessing](https://docs.python.org/3/whatsnew/3.13.html#multiprocessing)
            
        *   [os](https://docs.python.org/3/whatsnew/3.13.html#os)
            
        *   [os.path](https://docs.python.org/3/whatsnew/3.13.html#os-path)
            
        *   [pathlib](https://docs.python.org/3/whatsnew/3.13.html#pathlib)
            
        *   [pdb](https://docs.python.org/3/whatsnew/3.13.html#pdb)
            
        *   [queue](https://docs.python.org/3/whatsnew/3.13.html#queue)
            
        *   [random](https://docs.python.org/3/whatsnew/3.13.html#random)
            
        *   [re](https://docs.python.org/3/whatsnew/3.13.html#re)
            
        *   [shutil](https://docs.python.org/3/whatsnew/3.13.html#shutil)
            
        *   [site](https://docs.python.org/3/whatsnew/3.13.html#site)
            
        *   [sqlite3](https://docs.python.org/3/whatsnew/3.13.html#sqlite3)
            
        *   [ssl](https://docs.python.org/3/whatsnew/3.13.html#ssl)
            
        *   [statistics](https://docs.python.org/3/whatsnew/3.13.html#statistics)
            
        *   [subprocess](https://docs.python.org/3/whatsnew/3.13.html#subprocess)
            
        *   [sys](https://docs.python.org/3/whatsnew/3.13.html#sys)
            
        *   [tempfile](https://docs.python.org/3/whatsnew/3.13.html#tempfile)
            
        *   [time](https://docs.python.org/3/whatsnew/3.13.html#time)
            
        *   [tkinter](https://docs.python.org/3/whatsnew/3.13.html#tkinter)
            
        *   [traceback](https://docs.python.org/3/whatsnew/3.13.html#traceback)
            
        *   [types](https://docs.python.org/3/whatsnew/3.13.html#types)
            
        *   [typing](https://docs.python.org/3/whatsnew/3.13.html#typing)
            
        *   [unicodedata](https://docs.python.org/3/whatsnew/3.13.html#unicodedata)
            
        *   [venv](https://docs.python.org/3/whatsnew/3.13.html#venv)
            
        *   [warnings](https://docs.python.org/3/whatsnew/3.13.html#warnings)
            
        *   [xml](https://docs.python.org/3/whatsnew/3.13.html#xml)
            
        *   [zipimport](https://docs.python.org/3/whatsnew/3.13.html#zipimport)
            
    *   [Optimizations](https://docs.python.org/3/whatsnew/3.13.html#optimizations)
        
    *   [Removed Modules And APIs](https://docs.python.org/3/whatsnew/3.13.html#removed-modules-and-apis)
        *   [PEP 594: Remove “dead batteries” from the standard library](https://docs.python.org/3/whatsnew/3.13.html#pep-594-remove-dead-batteries-from-the-standard-library)
            
        *   [2to3](https://docs.python.org/3/whatsnew/3.13.html#to3)
            
        *   [builtins](https://docs.python.org/3/whatsnew/3.13.html#builtins)
            
        *   [configparser](https://docs.python.org/3/whatsnew/3.13.html#id3)
            
        *   [importlib.metadata](https://docs.python.org/3/whatsnew/3.13.html#importlib-metadata)
            
        *   [locale](https://docs.python.org/3/whatsnew/3.13.html#locale)
            
        *   [opcode](https://docs.python.org/3/whatsnew/3.13.html#opcode)
            
        *   [optparse](https://docs.python.org/3/whatsnew/3.13.html#optparse)
            
        *   [pathlib](https://docs.python.org/3/whatsnew/3.13.html#id4)
            
        *   [re](https://docs.python.org/3/whatsnew/3.13.html#id5)
            
        *   [tkinter.tix](https://docs.python.org/3/whatsnew/3.13.html#tkinter-tix)
            
        *   [turtle](https://docs.python.org/3/whatsnew/3.13.html#turtle)
            
        *   [typing](https://docs.python.org/3/whatsnew/3.13.html#id6)
            
        *   [unittest](https://docs.python.org/3/whatsnew/3.13.html#unittest)
            
        *   [urllib](https://docs.python.org/3/whatsnew/3.13.html#urllib)
            
        *   [webbrowser](https://docs.python.org/3/whatsnew/3.13.html#webbrowser)
            
    *   [New Deprecations](https://docs.python.org/3/whatsnew/3.13.html#new-deprecations)
        *   [Pending removal in Python 3.14](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-14)
            
        *   [Pending removal in Python 3.15](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-15)
            
        *   [Pending removal in Python 3.16](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-16)
            
        *   [Pending removal in Python 3.17](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-17)
            
        *   [Pending removal in Python 3.18](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-18)
            
        *   [Pending removal in Python 3.19](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-19)
            
        *   [Pending removal in Python 3.20](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-python-3-20)
            
        *   [Pending removal in future versions](https://docs.python.org/3/whatsnew/3.13.html#pending-removal-in-future-versions)
            
    *   [CPython Bytecode Changes](https://docs.python.org/3/whatsnew/3.13.html#cpython-bytecode-changes)
        
    *   [C API Changes](https://docs.python.org/3/whatsnew/3.13.html#c-api-changes)
        *   [New Features](https://docs.python.org/3/whatsnew/3.13.html#id7)
            
        *   [Changed C APIs](https://docs.python.org/3/whatsnew/3.13.html#changed-c-apis)
            
        *   [Limited C API Changes](https://docs.python.org/3/whatsnew/3.13.html#limited-c-api-changes)
            
        *   [Removed C APIs](https://docs.python.org/3/whatsnew/3.13.html#removed-c-apis)
            
        *   [Deprecated C APIs](https://docs.python.org/3/whatsnew/3.13.html#deprecated-c-apis)
            *   [Pending removal in Python 3.14](https://docs.python.org/3/whatsnew/3.13.html#id8)
                
            *   [Pending removal in Python 3.15](https://docs.python.org/3/whatsnew/3.13.html#id9)
                
            *   [Pending removal in Python 3.16](https://docs.python.org/3/whatsnew/3.13.html#id10)
                
            *   [Pending removal in Python 3.18](https://docs.python.org/3/whatsnew/3.13.html#id11)
                
            *   [Pending removal in future versions](https://docs.python.org/3/whatsnew/3.13.html#id12)
                
    *   [Build Changes](https://docs.python.org/3/whatsnew/3.13.html#build-changes)
        
    *   [Porting to Python 3.13](https://docs.python.org/3/whatsnew/3.13.html#porting-to-python-3-13)
        *   [Changes in the Python API](https://docs.python.org/3/whatsnew/3.13.html#changes-in-the-python-api)
            
        *   [Changes in the C API](https://docs.python.org/3/whatsnew/3.13.html#changes-in-the-c-api)
            
    *   [Regression Test Changes](https://docs.python.org/3/whatsnew/3.13.html#regression-test-changes)
        

#### Previous topic

[What’s new in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html "previous chapter")

#### Next topic

[What’s New In Python 3.12](https://docs.python.org/3/whatsnew/3.12.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=What%E2%80%99s+New+In+Python+3.13&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fwhatsnew%2F3.13.html&pagesource=whatsnew%2F3.13.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/whatsnew/3.13.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/3.12.html "What’s New In Python 3.12")
     |
*   [previous](https://docs.python.org/3/whatsnew/3.14.html "What’s new in Python 3.14")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [What’s New in Python](https://docs.python.org/3/whatsnew/index.html)
     »
*   [What’s New In Python 3.13](https://docs.python.org/3/whatsnew/3.13.html)
    
*    
    
    |
*   Theme Auto Light Dark |