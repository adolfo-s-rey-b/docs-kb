### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/windows.html "4. Using Python on Windows")
     |
*   [previous](https://docs.python.org/3/using/unix.html "2. Using Python on Unix platforms")
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
*   [3\. Configure Python](https://docs.python.org/3/using/configure.html)
    
*    
    
    |
*   Theme Auto Light Dark |

3\. Configure Python[¶](https://docs.python.org/3/using/configure.html#configure-python "Link to this heading")

================================================================================================================

3.1. Build requirements[¶](https://docs.python.org/3/using/configure.html#build-requirements "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

To build CPython, you will need:

*   A [C11](https://en.cppreference.com/w/c/11)
     compiler. [Optional C11 features](https://en.wikipedia.org/wiki/C11_(C_standard_revision)#Optional_features)
     are not required.
    
*   On Windows, Microsoft Visual Studio 2017 or later is required.
    
*   Support for [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754)
     floating-point numbers and [floating-point Not-a-Number (NaN)](https://en.wikipedia.org/wiki/NaN#Floating_point)
    .
    
*   Support for threads.
    

Changed in version 3.5: On Windows, Visual Studio 2015 or later is now required.

Changed in version 3.6: Selected C99 features, like `<stdint.h>` and `static inline` functions, are now required.

Changed in version 3.7: Thread support is now required.

Changed in version 3.11: C11 compiler, IEEE 754 and NaN support are now required. On Windows, Visual Studio 2017 or later is required.

See also [**PEP 7**](https://peps.python.org/pep-0007/)
 “Style Guide for C Code” and [**PEP 11**](https://peps.python.org/pep-0011/)
 “CPython platform support”.

### 3.1.1. Requirements for optional modules[¶](https://docs.python.org/3/using/configure.html#requirements-for-optional-modules "Link to this heading")

Some [optional modules](https://docs.python.org/3/glossary.html#term-optional-module)
 of the standard library require third-party libraries installed for development (for example, header files must be available).

Missing requirements are reported in the `configure` output. Modules that are missing due to missing dependencies are listed near the end of the `make` output, sometimes using an internal name, for example, `_ctypes` for [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
 module.

If you distribute a CPython interpreter without optional modules, it’s best practice to advise users, who generally expect that standard library modules are available.

Dependencies to build optional modules are:

| Dependency | Minimum version | Python module |
| --- | --- | --- |
| [libbz2](https://sourceware.org/bzip2/) |     | [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") |
| [libffi](https://sourceware.org/libffi/) | 3.3.0 recommended | [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.") |
| [liblzma](https://tukaani.org/xz/) |     | [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") |
| [libmpdec](https://www.bytereef.org/mpdecimal/doc/libmpdec/) | 2.5.0 | [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")<br> [\[1\]](https://docs.python.org/3/using/configure.html#id8) |
| [libreadline](https://tiswww.case.edu/php/chet/readline/rltop.html)<br> or [libedit](https://www.thrysoee.dk/editline/)<br> [\[2\]](https://docs.python.org/3/using/configure.html#id9) |     | [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") |
| [libuuid](https://linux.die.net/man/3/libuuid) |     | `_uuid` [\[3\]](https://docs.python.org/3/using/configure.html#id10) |
| [ncurses](https://gnu.org/software/ncurses/ncurses.html)<br> [\[4\]](https://docs.python.org/3/using/configure.html#id11) |     | [`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling.") |
| [OpenSSL](https://openssl-library.org/) | [\[6\]](https://docs.python.org/3/using/configure.html#id13) | [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")<br>, [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")<br> [\[5\]](https://docs.python.org/3/using/configure.html#id12) |
| [SQLite](https://sqlite.org/) | 3.15.2 | [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.") |
| [Tcl/Tk](https://www.tcl-lang.org/) | 8.5.12 | [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")<br>, [IDLE](https://docs.python.org/3/library/idle.html#idle)<br>, [`turtle`](https://docs.python.org/3/library/turtle.html#module-turtle "turtle: An educational framework for simple graphics applications") |
| [zlib](https://www.zlib.net/) | 1.2.2.1 | [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")<br>, [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.")<br>, [`ensurepip`](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "ensurepip: Bootstrapping the "pip" installer into an existing Python installation or virtual environment.") |
| [zstd](https://facebook.github.io/zstd/) | 1.4.5 | [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.") |

Note that the table does not include all optional modules; in particular, platform-specific modules like [`winreg`](https://docs.python.org/3/library/winreg.html#module-winreg "winreg: Routines and objects for manipulating the Windows registry.")
 are not listed here.

See also

*   The [devguide](https://devguide.python.org/getting-started/setup-building/#install-dependencies)
     includes a full list of dependencies required to build all modules and instructions on how to install them on common platforms.
    
*   [`--with-system-expat`](https://docs.python.org/3/using/configure.html#cmdoption-with-system-expat)
     allows building with an external [libexpat](https://libexpat.github.io/)
     library.
    
*   [Options for third-party dependencies](https://docs.python.org/3/using/configure.html#configure-options-for-dependencies)
    

Changed in version 3.1: Tcl/Tk version 8.3.1 is now required for [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
.

Changed in version 3.5: Tcl/Tk version 8.4 is now required for [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
.

Changed in version 3.7: OpenSSL 1.0.2 is now required for [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
 and [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
.

Changed in version 3.10: OpenSSL 1.1.1 is now required for [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
 and [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
. SQLite 3.7.15 is now required for [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.")
.

Changed in version 3.11: Tcl/Tk version 8.5.12 is now required for [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
.

Changed in version 3.13: SQLite 3.15.2 is now required for [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.")
.

3.2. Generated files[¶](https://docs.python.org/3/using/configure.html#generated-files "Link to this heading")

---------------------------------------------------------------------------------------------------------------

To reduce build dependencies, Python source code contains multiple generated files. Commands to regenerate all generated files:

Copy

make regen-all
make regen-stdlib-module-names
make regen-limited-abi
make regen-configure
make regen-sbom
make regen-unicodedata

The [Makefile.pre.in](https://github.com/python/cpython/tree/3.15/Makefile.pre.in)
 file documents generated files, their inputs, and tools used to regenerate them. Search for `regen-*` make targets.

### 3.2.1. configure script[¶](https://docs.python.org/3/using/configure.html#configure-script "Link to this heading")

The `make regen-configure` command regenerates the `aclocal.m4` file and the `configure` script using the `Tools/build/regen-configure.sh` shell script which uses an Ubuntu container to get the same tools versions and have a reproducible output.

The container is optional, the following command can be run locally:

Copy

autoreconf \-ivf \-Werror

The generated files can change depending on the exact versions of the tools used. The container that CPython uses has [Autoconf](https://gnu.org/software/autoconf)
 2.72, `aclocal` from [Automake](https://www.gnu.org/software/automake)
 1.16.5, and [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/)
 1.8.1.

Changed in version 3.13: Autoconf 2.71 and aclocal 1.16.5 and are now used to regenerate `configure`.

Changed in version 3.14: Autoconf 2.72 is now used to regenerate `configure`.

3.3. Configure options[¶](https://docs.python.org/3/using/configure.html#configure-options "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

List all `configure` script options using:

Copy

./configure \--help

See also the `Misc/SpecialBuilds.txt` in the Python source distribution.

### 3.3.1. General options[¶](https://docs.python.org/3/using/configure.html#general-options "Link to this heading")

\--enable-loadable-sqlite-extensions[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-loadable-sqlite-extensions "Link to this definition")

Support loadable extensions in the `_sqlite` extension module (default is no) of the [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.")
 module.

See the [`sqlite3.Connection.enable_load_extension()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.enable_load_extension "sqlite3.Connection.enable_load_extension")
 method of the [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.")
 module.

Added in version 3.6.

\--disable-ipv6[¶](https://docs.python.org/3/using/configure.html#cmdoption-disable-ipv6 "Link to this definition")

Disable IPv6 support (enabled by default if supported), see the [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.")
 module.

\--enable-big-digits\=\[15|30\][¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-big-digits "Link to this definition")

Define the size in bits of Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 digits: 15 or 30 bits.

By default, the digit size is 30.

Define [`PYLONG_BITS_IN_DIGIT`](https://docs.python.org/3/c-api/long.html#c.PYLONG_BITS_IN_DIGIT "PYLONG_BITS_IN_DIGIT")
 to `15` or `30`.

See [`sys.int_info.bits_per_digit`](https://docs.python.org/3/library/sys.html#sys.int_info "sys.int_info")
.

\--with-suffix\=SUFFIX[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-suffix "Link to this definition")

Set the Python executable suffix to _SUFFIX_.

The default suffix is `.exe` on Windows and macOS (`python.exe` executable), `.js` on Emscripten node, `.html` on Emscripten browser, `.wasm` on WASI, and an empty string on other platforms (`python` executable).

Changed in version 3.11: The default suffix on WASM platform is one of `.js`, `.html` or `.wasm`.

\--with-tzpath\=<list of absolute paths separated by pathsep>[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-tzpath "Link to this definition")

Select the default time zone search path for [`zoneinfo.TZPATH`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.TZPATH "zoneinfo.TZPATH")
. See the [Compile-time configuration](https://docs.python.org/3/library/zoneinfo.html#zoneinfo-data-compile-time-config)
 of the [`zoneinfo`](https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo "zoneinfo: IANA time zone support")
 module.

Default: `/usr/share/zoneinfo:/usr/lib/zoneinfo:/usr/share/lib/zoneinfo:/etc/zoneinfo`.

See [`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep")
 path separator.

Added in version 3.9.

\--without-decimal-contextvar[¶](https://docs.python.org/3/using/configure.html#cmdoption-without-decimal-contextvar "Link to this definition")

Build the `_decimal` extension module using a thread-local context rather than a coroutine-local context (default), see the [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
 module.

See [`decimal.HAVE_CONTEXTVAR`](https://docs.python.org/3/library/decimal.html#decimal.HAVE_CONTEXTVAR "decimal.HAVE_CONTEXTVAR")
 and the [`contextvars`](https://docs.python.org/3/library/contextvars.html#module-contextvars "contextvars: Context Variables")
 module.

Added in version 3.9.

\--with-dbmliborder\=<list of backend names>[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-dbmliborder "Link to this definition")

Override order to check db backends for the [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Interfaces to various Unix "database" formats.")
 module

A valid value is a colon (`:`) separated string with the backend names:

*   `ndbm`;
    
*   `gdbm`;
    
*   `bdb`.
    

\--without-c-locale-coercion[¶](https://docs.python.org/3/using/configure.html#cmdoption-without-c-locale-coercion "Link to this definition")

Disable C locale coercion to a UTF-8 based locale (enabled by default).

Don’t define the `PY_COERCE_C_LOCALE` macro.

See [`PYTHONCOERCECLOCALE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONCOERCECLOCALE)
 and the [**PEP 538**](https://peps.python.org/pep-0538/)
.

\--with-platlibdir\=DIRNAME[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-platlibdir "Link to this definition")

Python library directory name (default is `lib`).

Fedora and SuSE use `lib64` on 64-bit platforms.

See [`sys.platlibdir`](https://docs.python.org/3/library/sys.html#sys.platlibdir "sys.platlibdir")
.

Added in version 3.9.

\--with-wheel-pkg-dir\=PATH[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-wheel-pkg-dir "Link to this definition")

Directory of wheel packages used by the [`ensurepip`](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "ensurepip: Bootstrapping the "pip" installer into an existing Python installation or virtual environment.")
 module (none by default).

Some Linux distribution packaging policies recommend against bundling dependencies. For example, Fedora installs wheel packages in the `/usr/share/python-wheels/` directory and don’t install the `ensurepip._bundled` package.

Added in version 3.10.

\--with-pkg-config\=\[check|yes|no\][¶](https://docs.python.org/3/using/configure.html#cmdoption-with-pkg-config "Link to this definition")

Whether configure should use **pkg-config** to detect build dependencies.

*   `check` (default): **pkg-config** is optional
    
*   `yes`: **pkg-config** is mandatory
    
*   `no`: configure does not use **pkg-config** even when present
    

Added in version 3.11.

\--with-missing-stdlib-config\=FILE[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-missing-stdlib-config "Link to this definition")

Path to a [JSON](https://www.json.org/json-en.html)
 configuration file containing custom error messages for missing [standard library](https://docs.python.org/3/glossary.html#term-standard-library)
 modules.

This option is intended for Python distributors who wish to provide distribution-specific guidance when users encounter standard library modules that are missing or packaged separately.

The JSON file should map missing module names to custom error message strings. For example, if your distribution packages [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")
 and [`_tkinter`](https://docs.python.org/3/library/tkinter.html#module-_tkinter "_tkinter: A binary module that contains the low-level interface to Tcl/Tk.")
 separately and excludes `_gdbm` for legal reasons, the configuration could contain:

{
    "\_gdbm": "The '\_gdbm' module is not available in this distribution",
    "tkinter": "Install the python-tk package to use tkinter",
    "\_tkinter": "Install the python-tk package to use tkinter",
}

Added in version 3.15.

\--enable-pystats[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-pystats "Link to this definition")

Turn on internal Python performance statistics gathering.

By default, statistics gathering is off. Use `python3 -X pystats` command or set `PYTHONSTATS=1` environment variable to turn on statistics gathering at Python startup.

At Python exit, dump statistics if statistics gathering was on and not cleared.

Effects:

*   Add [`-X pystats`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
     command line option.
    
*   Add `PYTHONSTATS` environment variable.
    
*   Define the `Py_STATS` macro.
    
*   Add functions to the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
     module:
    
    *   `sys._stats_on()`: Turns on statistics gathering.
        
    *   `sys._stats_off()`: Turns off statistics gathering.
        
    *   `sys._stats_clear()`: Clears the statistics.
        
    *   `sys._stats_dump()`: Dump statistics to file, and clears the statistics.
        

The statistics will be dumped to a arbitrary (probably unique) file in `/tmp/py_stats/` (Unix) or `C:\temp\py_stats\` (Windows). If that directory does not exist, results will be printed on stderr.

Use `Tools/scripts/summarize_stats.py` to read the stats.

Statistics:

*   Opcode:
    
    *   Specialization: success, failure, hit, deferred, miss, deopt, failures;
        
    *   Execution count;
        
    *   Pair count.
        
*   Call:
    
    *   Inlined Python calls;
        
    *   PyEval calls;
        
    *   Frames pushed;
        
    *   Frame object created;
        
    *   Eval calls: vector, generator, legacy, function VECTORCALL, build class, slot, function “ex”, API, method.
        
*   Object:
    
    *   incref and decref;
        
    *   interpreter incref and decref;
        
    *   allocations: all, 512 bytes, 4 kiB, big;
        
    *   free;
        
    *   to/from free lists;
        
    *   dictionary materialized/dematerialized;
        
    *   type cache;
        
    *   optimization attempts;
        
    *   optimization traces created/executed;
        
    *   uops executed.
        
*   Garbage collector:
    
    *   Garbage collections;
        
    *   Objects visited;
        
    *   Objects collected.
        

Added in version 3.11.

\--disable-gil[¶](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil "Link to this definition")

Enables support for running Python without the [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
 (GIL): [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
.

Defines the `Py_GIL_DISABLED` macro and adds `"t"` to [`sys.abiflags`](https://docs.python.org/3/library/sys.html#sys.abiflags "sys.abiflags")
.

See [Free-threaded CPython](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-free-threaded-cpython)
 for more detail.

Added in version 3.13.

\--enable-experimental-jit\=\[no|yes|yes-off|interpreter\][¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-experimental-jit "Link to this definition")

Indicate how to integrate the [experimental just-in-time compiler](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-jit-compiler)
.

*   `no`: Don’t build the JIT.
    
*   `yes`: Enable the JIT. To disable it at runtime, set the environment variable [`PYTHON_JIT=0`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_JIT)
    .
    
*   `yes-off`: Build the JIT, but disable it by default. To enable it at runtime, set the environment variable [`PYTHON_JIT=1`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_JIT)
    .
    
*   `interpreter`: Enable the “JIT interpreter” (only useful for those debugging the JIT itself). To disable it at runtime, set the environment variable [`PYTHON_JIT=0`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_JIT)
    .
    

`--enable-experimental-jit=no` is the default behavior if the option is not provided, and `--enable-experimental-jit` is shorthand for `--enable-experimental-jit=yes`. See `Tools/jit/README.md` for more information, including how to install the necessary build-time dependencies.

Note

When building CPython with JIT enabled, ensure that your system has Python 3.11 or later installed.

Added in version 3.13.

PKG\_CONFIG[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-PKG_CONFIG "Link to this definition")

Path to `pkg-config` utility.

PKG\_CONFIG\_LIBDIR[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-PKG_CONFIG_LIBDIR "Link to this definition")

PKG\_CONFIG\_PATH[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-PKG_CONFIG_PATH "Link to this definition")

`pkg-config` options.

\--disable-epoll[¶](https://docs.python.org/3/using/configure.html#cmdoption-disable-epoll "Link to this definition")

Build without `epoll`, meaning that [`select.epoll()`](https://docs.python.org/3/library/select.html#select.epoll "select.epoll")
 will not be present even if the system provides an _[epoll\_create](https://manpages.debian.org/epoll_create(2))
_ function. This may be used on systems where _epoll\_create_ or _[epoll\_create1](https://manpages.debian.org/epoll_create1(2))
_ is available but incompatible with Linux semantics.

Added in version 3.15.

### 3.3.2. C compiler options[¶](https://docs.python.org/3/using/configure.html#c-compiler-options "Link to this heading")

CC[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-CC "Link to this definition")

C compiler command.

CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-CFLAGS "Link to this definition")

C compiler flags.

CPP[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-CPP "Link to this definition")

C preprocessor command.

CPPFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-CPPFLAGS "Link to this definition")

C preprocessor flags, e.g. `-I_include_dir_`.

### 3.3.3. Linker options[¶](https://docs.python.org/3/using/configure.html#linker-options "Link to this heading")

LDFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LDFLAGS "Link to this definition")

Linker flags, e.g. `-L_library_directory_`.

LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBS "Link to this definition")

Libraries to pass to the linker, e.g. `-l_library_`.

MACHDEP[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-MACHDEP "Link to this definition")

Name for machine-dependent library files.

### 3.3.4. Options for third-party dependencies[¶](https://docs.python.org/3/using/configure.html#options-for-third-party-dependencies "Link to this heading")

Added in version 3.11.

BZIP2\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-BZIP2_CFLAGS "Link to this definition")

BZIP2\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-BZIP2_LIBS "Link to this definition")

C compiler and linker flags to link Python to `libbz2`, used by [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
 module, overriding `pkg-config`.

CURSES\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-CURSES_CFLAGS "Link to this definition")

CURSES\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-CURSES_LIBS "Link to this definition")

C compiler and linker flags for `libncurses` or `libncursesw`, used by [`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling.")
 module, overriding `pkg-config`.

GDBM\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-GDBM_CFLAGS "Link to this definition")

GDBM\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-GDBM_LIBS "Link to this definition")

C compiler and linker flags for `gdbm`.

LIBEDIT\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBEDIT_CFLAGS "Link to this definition")

LIBEDIT\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBEDIT_LIBS "Link to this definition")

C compiler and linker flags for `libedit`, used by [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
 module, overriding `pkg-config`.

LIBFFI\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBFFI_CFLAGS "Link to this definition")

LIBFFI\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBFFI_LIBS "Link to this definition")

C compiler and linker flags for `libffi`, used by [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
 module, overriding `pkg-config`.

LIBMPDEC\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBMPDEC_CFLAGS "Link to this definition")

LIBMPDEC\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBMPDEC_LIBS "Link to this definition")

C compiler and linker flags for `libmpdec`, used by [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
 module, overriding `pkg-config`.

Note

These environment variables have no effect unless [`--with-system-libmpdec`](https://docs.python.org/3/using/configure.html#cmdoption-with-system-libmpdec)
 is specified.

LIBLZMA\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBLZMA_CFLAGS "Link to this definition")

LIBLZMA\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBLZMA_LIBS "Link to this definition")

C compiler and linker flags for `liblzma`, used by [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
 module, overriding `pkg-config`.

LIBREADLINE\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBREADLINE_CFLAGS "Link to this definition")

LIBREADLINE\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBREADLINE_LIBS "Link to this definition")

C compiler and linker flags for `libreadline`, used by [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
 module, overriding `pkg-config`.

LIBSQLITE3\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBSQLITE3_CFLAGS "Link to this definition")

LIBSQLITE3\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBSQLITE3_LIBS "Link to this definition")

C compiler and linker flags for `libsqlite3`, used by [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.")
 module, overriding `pkg-config`.

LIBUUID\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBUUID_CFLAGS "Link to this definition")

LIBUUID\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBUUID_LIBS "Link to this definition")

C compiler and linker flags for `libuuid`, used by [`uuid`](https://docs.python.org/3/library/uuid.html#module-uuid "uuid: UUID objects (universally unique identifiers) according to RFC 9562")
 module, overriding `pkg-config`.

LIBZSTD\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBZSTD_CFLAGS "Link to this definition")

LIBZSTD\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBZSTD_LIBS "Link to this definition")

C compiler and linker flags for `libzstd`, used by [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.")
 module, overriding `pkg-config`.

Added in version 3.14.

PANEL\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-PANEL_CFLAGS "Link to this definition")

PANEL\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-PANEL_LIBS "Link to this definition")

C compiler and linker flags for PANEL, overriding `pkg-config`.

C compiler and linker flags for `libpanel` or `libpanelw`, used by [`curses.panel`](https://docs.python.org/3/library/curses.panel.html#module-curses.panel "curses.panel: A panel stack extension that adds depth to  curses windows.")
 module, overriding `pkg-config`.

TCLTK\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-TCLTK_CFLAGS "Link to this definition")

TCLTK\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-TCLTK_LIBS "Link to this definition")

C compiler and linker flags for TCLTK, overriding `pkg-config`.

ZLIB\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-ZLIB_CFLAGS "Link to this definition")

ZLIB\_LIBS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-ZLIB_LIBS "Link to this definition")

C compiler and linker flags for `libzlib`, used by [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.")
 module, overriding `pkg-config`.

### 3.3.5. WebAssembly options[¶](https://docs.python.org/3/using/configure.html#webassembly-options "Link to this heading")

\--enable-wasm-dynamic-linking[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-wasm-dynamic-linking "Link to this definition")

Turn on dynamic linking support for WASM.

Dynamic linking enables `dlopen`. File size of the executable increases due to limited dead code elimination and additional features.

Added in version 3.11.

\--enable-wasm-pthreads[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-wasm-pthreads "Link to this definition")

Turn on pthreads support for WASM.

Added in version 3.11.

### 3.3.6. Install options[¶](https://docs.python.org/3/using/configure.html#install-options "Link to this heading")

\--prefix\=PREFIX[¶](https://docs.python.org/3/using/configure.html#cmdoption-prefix "Link to this definition")

Install architecture-independent files in PREFIX. On Unix, it defaults to `/usr/local`.

This value can be retrieved at runtime using [`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix")
.

As an example, one can use `--prefix="$HOME/.local/"` to install a Python in its home directory.

\--exec-prefix\=EPREFIX[¶](https://docs.python.org/3/using/configure.html#cmdoption-exec-prefix "Link to this definition")

Install architecture-dependent files in EPREFIX, defaults to [`--prefix`](https://docs.python.org/3/using/configure.html#cmdoption-prefix)
.

This value can be retrieved at runtime using [`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix")
.

\--disable-test-modules[¶](https://docs.python.org/3/using/configure.html#cmdoption-disable-test-modules "Link to this definition")

Don’t build nor install test modules, like the [`test`](https://docs.python.org/3/library/test.html#module-test "test: Regression tests package containing the testing suite for Python.")
 package or the `_testcapi` extension module (built and installed by default).

Added in version 3.10.

\--with-ensurepip\=\[upgrade|install|no\][¶](https://docs.python.org/3/using/configure.html#cmdoption-with-ensurepip "Link to this definition")

Select the [`ensurepip`](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "ensurepip: Bootstrapping the "pip" installer into an existing Python installation or virtual environment.")
 command run on Python installation:

*   `upgrade` (default): run `python -m ensurepip --altinstall --upgrade` command.
    
*   `install`: run `python -m ensurepip --altinstall` command;
    
*   `no`: don’t run ensurepip;
    

Added in version 3.6.

### 3.3.7. Performance options[¶](https://docs.python.org/3/using/configure.html#performance-options "Link to this heading")

Configuring Python using `--enable-optimizations --with-lto` (PGO + LTO) is recommended for best performance. The experimental `--enable-bolt` flag can also be used to improve performance.

\--enable-optimizations[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-optimizations "Link to this definition")

Enable Profile Guided Optimization (PGO) using [`PROFILE_TASK`](https://docs.python.org/3/using/configure.html#envvar-PROFILE_TASK)
 (disabled by default).

The C compiler Clang requires `llvm-profdata` program for PGO. On macOS, GCC also requires it: GCC is just an alias to Clang on macOS.

Disable also semantic interposition in libpython if `--enable-shared` and GCC is used: add `-fno-semantic-interposition` to the compiler and linker flags.

Note

During the build, you may encounter compiler warnings about profile data not being available for some source files. These warnings are harmless, as only a subset of the code is exercised during profile data acquisition. To disable these warnings on Clang, manually suppress them by adding `-Wno-profile-instr-unprofiled` to [`CFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CFLAGS)
.

Added in version 3.6.

Changed in version 3.10: Use `-fno-semantic-interposition` on GCC.

PROFILE\_TASK[¶](https://docs.python.org/3/using/configure.html#envvar-PROFILE_TASK "Link to this definition")

Environment variable used in the Makefile: Python command line arguments for the PGO generation task.

Default: `-m test --pgo --timeout=$(TESTTIMEOUT)`.

Added in version 3.8.

Changed in version 3.13: Task failure is no longer ignored silently.

\--with-lto\=\[full|thin|no|yes\][¶](https://docs.python.org/3/using/configure.html#cmdoption-with-lto "Link to this definition")

Enable Link Time Optimization (LTO) in any build (disabled by default).

The C compiler Clang requires `llvm-ar` for LTO (`ar` on macOS), as well as an LTO-aware linker (`ld.gold` or `lld`).

Added in version 3.6.

Added in version 3.11: To use ThinLTO feature, use `--with-lto=thin` on Clang.

Changed in version 3.12: Use ThinLTO as the default optimization policy on Clang if the compiler accepts the flag.

\--enable-bolt[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-bolt "Link to this definition")

Enable usage of the [BOLT post-link binary optimizer](https://github.com/llvm/llvm-project/tree/main/bolt)
 (disabled by default).

BOLT is part of the LLVM project but is not always included in their binary distributions. This flag requires that `llvm-bolt` and `merge-fdata` are available.

BOLT is still a fairly new project so this flag should be considered experimental for now. Because this tool operates on machine code its success is dependent on a combination of the build environment + the other optimization configure args + the CPU architecture, and not all combinations are supported. BOLT versions before LLVM 16 are known to crash BOLT under some scenarios. Use of LLVM 16 or newer for BOLT optimization is strongly encouraged.

The `BOLT_INSTRUMENT_FLAGS` and `BOLT_APPLY_FLAGS` **configure** variables can be defined to override the default set of arguments for **llvm-bolt** to instrument and apply BOLT data to binaries, respectively.

Added in version 3.12.

BOLT\_APPLY\_FLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-BOLT_APPLY_FLAGS "Link to this definition")

Arguments to `llvm-bolt` when creating a [BOLT optimized binary](https://github.com/facebookarchive/BOLT)
.

Added in version 3.12.

BOLT\_INSTRUMENT\_FLAGS[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-BOLT_INSTRUMENT_FLAGS "Link to this definition")

Arguments to `llvm-bolt` when instrumenting binaries.

Added in version 3.12.

\--with-computed-gotos[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-computed-gotos "Link to this definition")

Enable computed gotos in evaluation loop (enabled by default on supported compilers).

\--with-tail-call-interp[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-tail-call-interp "Link to this definition")

Enable interpreters using tail calls in CPython. If enabled, enabling PGO ([`--enable-optimizations`](https://docs.python.org/3/using/configure.html#cmdoption-enable-optimizations)
) is highly recommended. This option specifically requires a C compiler with proper tail call support, and the [preserve\_none](https://clang.llvm.org/docs/AttributeReference.html#preserve-none)
 calling convention. For example, Clang 19 and newer supports this feature.

Added in version 3.14.

\--without-frame-pointers[¶](https://docs.python.org/3/using/configure.html#cmdoption-without-frame-pointers "Link to this definition")

Disable frame pointers, which are enabled by default (see [**PEP 831**](https://peps.python.org/pep-0831/)
).

By default, the build appends flags to generate frame or backchain pointers to `BASECFLAGS`:

*   `-fno-omit-frame-pointer` and/or `-mno-omit-leaf-frame-pointer` are added when the compiler supports them.
    
*   `-marm` and/or `-mno-thumb` is added on 32-bit ARM when supported,
    
*   on s390x platforms, when supported, `-mbackchain` is added _instead_. of the above frame pointer flags.
    
*   on ppc64le platforms, no compiler flags is needed since the power ABI requires that compilers maintain a back chain by default.
    

Frame pointers enable profilers, debuggers, and system tracing tools (`perf`, `eBPF`, `dtrace`, `gdb`) to walk the C call stack without DWARF metadata. The flags propagate to third-party C extensions through [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")
. On compilers that do not understand them, the build silently skips them.

Downstream packagers and authors of native libraries built with custom build systems should set the same flags so the unwind chain stays unbroken across all native frames.

Added in version 3.15.

\--without-mimalloc[¶](https://docs.python.org/3/using/configure.html#cmdoption-without-mimalloc "Link to this definition")

Disable the fast [mimalloc](https://docs.python.org/3/c-api/memory.html#mimalloc)
 allocator (enabled by default).

This option cannot be used together with [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
 because the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build requires mimalloc.

See also [`PYTHONMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC)
 environment variable.

\--without-pymalloc[¶](https://docs.python.org/3/using/configure.html#cmdoption-without-pymalloc "Link to this definition")

Disable the specialized Python memory allocator [pymalloc](https://docs.python.org/3/c-api/memory.html#pymalloc)
 (enabled by default).

See also [`PYTHONMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC)
 environment variable.

\--with-pymalloc-hugepages[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-pymalloc-hugepages "Link to this definition")

Enable huge page support for [pymalloc](https://docs.python.org/3/c-api/memory.html#pymalloc)
 arenas (disabled by default). When enabled, the arena size on 64-bit platforms is increased to 2 MiB and arena allocation uses `MAP_HUGETLB` (Linux) or `MEM_LARGE_PAGES` (Windows) with automatic fallback to regular pages.

Even when compiled with this option, huge pages are **not** used at runtime unless the [`PYTHON_PYMALLOC_HUGEPAGES`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PYMALLOC_HUGEPAGES)
 environment variable is set to `1`. This opt-in is required because huge pages

*   carry risks on Linux: if the huge-page pool is exhausted, page faults (including copy-on-write faults after [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
    ) deliver `SIGBUS` and kill the process.
    
*   need a special privilege on Windows. See the [Windows documentation for large pages](https://learn.microsoft.com/windows/win32/memory/large-page-support)
     for details. Python will fail on startup if the required privilege [SeLockMemoryPrivilege](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/security-policy-settings/lock-pages-in-memory)
     is not held by the user.
    

The configure script checks that the platform supports `MAP_HUGETLB` and emits a warning if it is not available.

On Windows, use the `--pymalloc-hugepages` flag with `build.bat` or set the `UsePymallocHugepages` MSBuild property.

Added in version 3.15.

\--without-doc-strings[¶](https://docs.python.org/3/using/configure.html#cmdoption-without-doc-strings "Link to this definition")

Disable static documentation strings to reduce the memory footprint (enabled by default). Documentation strings defined in Python are not affected.

Don’t define the [`WITH_DOC_STRINGS`](https://docs.python.org/3/using/configure.html#c.WITH_DOC_STRINGS "WITH_DOC_STRINGS")
 macro.

WITH\_DOC\_STRINGS[¶](https://docs.python.org/3/using/configure.html#c.WITH_DOC_STRINGS "Link to this definition")
  

Define this macro to include static documentation strings in the build. It is defined by default, unless [`--without-doc-strings`](https://docs.python.org/3/using/configure.html#cmdoption-without-doc-strings)
 is used.

See the `PyDoc_STRVAR()` macro.

\--enable-profiling[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-profiling "Link to this definition")

Enable C-level code profiling with `gprof` (disabled by default).

\--with-strict-overflow[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-strict-overflow "Link to this definition")

Add `-fstrict-overflow` to the C compiler flags (by default we add `-fno-strict-overflow` instead).

\--without-remote-debug[¶](https://docs.python.org/3/using/configure.html#cmdoption-without-remote-debug "Link to this definition")

Deactivate remote debugging support described in [**PEP 768**](https://peps.python.org/pep-0768/)
 (enabled by default). When this flag is provided the code that allows the interpreter to schedule the execution of a Python file in a separate process as described in [**PEP 768**](https://peps.python.org/pep-0768/)
 is not compiled. This includes both the functionality to schedule code to be executed and the functionality to receive code to be executed.

Py\_REMOTE\_DEBUG[¶](https://docs.python.org/3/using/configure.html#c.Py_REMOTE_DEBUG "Link to this definition")
  

This macro is defined by default, unless Python is configured with [`--without-remote-debug`](https://docs.python.org/3/using/configure.html#cmdoption-without-remote-debug)
.

Note that even if the macro is defined, remote debugging may not be available (for example, on an incompatible platform).

Added in version 3.14.

### 3.3.8. Python debug build[¶](https://docs.python.org/3/using/configure.html#python-debug-build "Link to this heading")

A debug build is Python built with the [`--with-pydebug`](https://docs.python.org/3/using/configure.html#cmdoption-with-pydebug)
 configure option.

Effects of a debug build:

*   Display all warnings by default: the list of default warning filters is empty in the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
     module.
    
*   Add `d` to [`sys.abiflags`](https://docs.python.org/3/library/sys.html#sys.abiflags "sys.abiflags")
    .
    
*   Add `sys.gettotalrefcount()` function.
    
*   Add [`-X showrefcount`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
     command line option.
    
*   Add [`-d`](https://docs.python.org/3/using/cmdline.html#cmdoption-d)
     command line option and [`PYTHONDEBUG`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDEBUG)
     environment variable to debug the parser.
    
*   Add support for the `__lltrace__` variable: enable low-level tracing in the bytecode evaluation loop if the variable is defined.
    
*   Install [debug hooks on memory allocators](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
     to detect buffer overflow and other memory errors.
    
*   Define `Py_DEBUG` and `Py_REF_DEBUG` macros.
    
*   Add runtime checks: code surrounded by `#ifdef Py_DEBUG` and `#endif`. Enable `assert(...)` and `_PyObject_ASSERT(...)` assertions: don’t set the `NDEBUG` macro (see also the [`--with-assertions`](https://docs.python.org/3/using/configure.html#cmdoption-with-assertions)
     configure option). Main runtime checks:
    
    *   Add sanity checks on the function arguments.
        
    *   Unicode and int objects are created with their memory filled with a pattern to detect usage of uninitialized objects.
        
    *   Ensure that functions which can clear or replace the current exception are not called with an exception raised.
        
    *   Check that deallocator functions don’t change the current exception.
        
    *   The garbage collector ([`gc.collect()`](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect")
         function) runs some basic checks on objects consistency.
        
    *   The `Py_SAFE_DOWNCAST()` macro checks for integer underflow and overflow when downcasting from wide types to narrow types.
        

See also the [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
 and the [`--with-trace-refs`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs)
 configure option.

Changed in version 3.8: Release builds are now ABI compatible with debug builds: defining the `Py_DEBUG` macro no longer implies the `Py_TRACE_REFS` macro (see the [`--with-trace-refs`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs)
 option). However, debug builds still expose more symbols than release builds and code built against a debug build is not necessarily compatible with a release build.

### 3.3.9. Debug options[¶](https://docs.python.org/3/using/configure.html#debug-options "Link to this heading")

\--with-pydebug[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-pydebug "Link to this definition")

[Build Python in debug mode](https://docs.python.org/3/using/configure.html#debug-build)
: define the `Py_DEBUG` macro (disabled by default).

\--with-trace-refs[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs "Link to this definition")

Enable tracing references for debugging purpose (disabled by default).

Effects:

*   Define the `Py_TRACE_REFS` macro.
    
*   Add [`sys.getobjects()`](https://docs.python.org/3/library/sys.html#sys.getobjects "sys.getobjects")
     function.
    
*   Add [`PYTHONDUMPREFS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDUMPREFS)
     environment variable.
    

The [`PYTHONDUMPREFS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDUMPREFS)
 environment variable can be used to dump objects and reference counts still alive at Python exit.

[Statically allocated objects](https://docs.python.org/3/c-api/typeobj.html#static-types)
 are not traced.

Added in version 3.8.

Changed in version 3.13: This build is now ABI compatible with release build and [debug build](https://docs.python.org/3/using/configure.html#debug-build)
.

\--with-assertions[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-assertions "Link to this definition")

Build with C assertions enabled (default is no): `assert(...);` and `_PyObject_ASSERT(...);`.

If set, the `NDEBUG` macro is not defined in the [`OPT`](https://docs.python.org/3/using/configure.html#envvar-OPT)
 compiler variable.

See also the [`--with-pydebug`](https://docs.python.org/3/using/configure.html#cmdoption-with-pydebug)
 option ([debug build](https://docs.python.org/3/using/configure.html#debug-build)
) which also enables assertions.

Added in version 3.6.

\--with-valgrind[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-valgrind "Link to this definition")

Enable Valgrind support (default is no).

\--with-dtrace[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-dtrace "Link to this definition")

Enable DTrace support (default is no).

See [Instrumenting CPython with DTrace and SystemTap](https://docs.python.org/3/howto/instrumentation.html#instrumentation)
.

Added in version 3.6.

\--with-address-sanitizer[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-address-sanitizer "Link to this definition")

Enable AddressSanitizer memory error detector, `asan` (default is no). To improve ASan detection capabilities you may also want to combine this with [`--without-pymalloc`](https://docs.python.org/3/using/configure.html#cmdoption-without-pymalloc)
 to disable the specialized small-object allocator whose allocations are not tracked by ASan.

Added in version 3.6.

\--with-memory-sanitizer[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-memory-sanitizer "Link to this definition")

Enable MemorySanitizer allocation error detector, `msan` (default is no).

MSan reports false positives for memory initialized by libraries that are not built with MSan, so either build all dependencies with MSan or disable the extension modules that use them in `Modules/Setup.local`.

Added in version 3.6.

\--with-undefined-behavior-sanitizer[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-undefined-behavior-sanitizer "Link to this definition")

Enable UndefinedBehaviorSanitizer undefined behaviour detector, `ubsan` (default is no).

Added in version 3.6.

\--with-thread-sanitizer[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-thread-sanitizer "Link to this definition")

Enable ThreadSanitizer data race detector, `tsan` (default is no).

Added in version 3.13.

### 3.3.10. Linker options[¶](https://docs.python.org/3/using/configure.html#id16 "Link to this heading")

\--enable-shared[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-shared "Link to this definition")

Enable building a shared Python library: `libpython` (default is no).

\--without-static-libpython[¶](https://docs.python.org/3/using/configure.html#cmdoption-without-static-libpython "Link to this definition")

Do not build `libpythonMAJOR.MINOR.a` and do not install `python.o` (built and enabled by default).

Added in version 3.10.

\--enable-static-libpython-for-interpreter[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-static-libpython-for-interpreter "Link to this definition")

Do not link the Python interpreter binary (`python3`) against the shared Python library; instead, statically link the interpreter against `libpython` as if `--enable-shared` had not been used, but continue to build the shared `libpython` (for use by other programs).

This option does nothing if `--enable-shared` is not used.

The default (when `--enable-shared` is used) is to link the Python interpreter against the built shared library.

Added in version 3.15.

### 3.3.11. Libraries options[¶](https://docs.python.org/3/using/configure.html#libraries-options "Link to this heading")

\--with-libs\='lib1 ...'[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-libs "Link to this definition")

Link against additional libraries (default is no).

\--with-system-expat[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-system-expat "Link to this definition")

Build the `pyexpat` module using an installed `expat` library (default is no).

\--with-system-libmpdec[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-system-libmpdec "Link to this definition")

Build the `_decimal` extension module using an installed `mpdecimal` library, see the [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
 module (default is yes).

Added in version 3.3.

Changed in version 3.13: Default to using the installed `mpdecimal` library.

Changed in version 3.15: A bundled copy of the library will no longer be selected implicitly if an installed `mpdecimal` library is not found. In Python 3.15 only, it can still be selected explicitly using `--with-system-libmpdec=no` or `--without-system-libmpdec`.

Deprecated since version 3.13, will be removed in version 3.16: A copy of the `mpdecimal` library sources will no longer be distributed with Python 3.16.

See also

[`LIBMPDEC_CFLAGS`](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBMPDEC_CFLAGS)
 and [`LIBMPDEC_LIBS`](https://docs.python.org/3/using/configure.html#cmdoption-arg-LIBMPDEC_LIBS)
.

\--with-readline\=readline|editline[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-readline "Link to this definition")

Designate a backend library for the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
 module.

*   readline: Use readline as the backend.
    
*   editline: Use editline as the backend.
    

Added in version 3.10.

\--without-readline[¶](https://docs.python.org/3/using/configure.html#cmdoption-without-readline "Link to this definition")

Don’t build the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
 module (built by default).

Don’t define the `HAVE_LIBREADLINE` macro.

Added in version 3.10.

\--with-libm\=STRING[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-libm "Link to this definition")

Override `libm` math library to _STRING_ (default is system-dependent).

\--with-libc\=STRING[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-libc "Link to this definition")

Override `libc` C library to _STRING_ (default is system-dependent).

\--with-openssl\=DIR[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-openssl "Link to this definition")

Root of the OpenSSL directory.

Added in version 3.7.

\--with-openssl-rpath\=\[no|auto|DIR\][¶](https://docs.python.org/3/using/configure.html#cmdoption-with-openssl-rpath "Link to this definition")

Set runtime library directory (rpath) for OpenSSL libraries:

*   `no` (default): don’t set rpath;
    
*   `auto`: auto-detect rpath from [`--with-openssl`](https://docs.python.org/3/using/configure.html#cmdoption-with-openssl)
     and `pkg-config`;
    
*   _DIR_: set an explicit rpath.
    

Added in version 3.10.

### 3.3.12. Security options[¶](https://docs.python.org/3/using/configure.html#security-options "Link to this heading")

\--with-hash-algorithm\=\[fnv|siphash13|siphash24\][¶](https://docs.python.org/3/using/configure.html#cmdoption-with-hash-algorithm "Link to this definition")

Select hash algorithm for use in `Python/pyhash.c`:

*   `siphash13` (default);
    
*   `siphash24`;
    
*   `fnv`.
    

Added in version 3.4.

Added in version 3.11: `siphash13` is added and it is the new default.

\--with-builtin-hashlib-hashes\=md5,sha1,sha256,sha512,sha3,blake2[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-builtin-hashlib-hashes "Link to this definition")

Built-in hash modules:

*   `md5`;
    
*   `sha1`;
    
*   `sha256`;
    
*   `sha512`;
    
*   `sha3` (with shake);
    
*   `blake2`.
    

Added in version 3.9.

\--with-ssl-default-suites\=\[python|openssl|STRING\][¶](https://docs.python.org/3/using/configure.html#cmdoption-with-ssl-default-suites "Link to this definition")

Override the OpenSSL default cipher suites string:

*   `python` (default): use Python’s preferred selection;
    
*   `openssl`: leave OpenSSL’s defaults untouched;
    
*   _STRING_: use a custom string
    

See the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
 module.

Added in version 3.7.

Changed in version 3.10: The settings `python` and _STRING_ also set TLS 1.2 as minimum protocol version.

\--disable-safety[¶](https://docs.python.org/3/using/configure.html#cmdoption-disable-safety "Link to this definition")

Disable compiler options that are [recommended by OpenSSF](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md)
 for security reasons with no performance overhead. If this option is not enabled, CPython will be built based on safety compiler options with no slow down. When this option is enabled, CPython will not be built with the compiler options listed below.

The following compiler options are disabled with `--disable-safety`:

*   [\-fstack-protector-strong](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md#enable-run-time-checks-for-stack-based-buffer-overflows)
    : Enable run-time checks for stack-based buffer overflows.
    
*   [\-Wtrampolines](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md#enable-warning-about-trampolines-that-require-executable-stacks)
    : Enable warnings about trampolines that require executable stacks.
    

Added in version 3.14.

\--enable-slower-safety[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-slower-safety "Link to this definition")

Enable compiler options that are [recommended by OpenSSF](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md)
 for security reasons which require overhead. If this option is not enabled, CPython will not be built based on safety compiler options which performance impact. When this option is enabled, CPython will be built with the compiler options listed below.

The following compiler options are enabled with `--enable-slower-safety`:

*   [\-D\_FORTIFY\_SOURCE=3](https://github.com/ossf/wg-best-practices-os-developers/blob/main/docs/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.md#fortify-sources-for-unsafe-libc-usage-and-buffer-overflows)
    : Fortify sources with compile- and run-time checks for unsafe libc usage and buffer overflows.
    

Added in version 3.14.

### 3.3.13. macOS options[¶](https://docs.python.org/3/using/configure.html#macos-options "Link to this heading")

See [Mac/README.rst](https://github.com/python/cpython/tree/3.15/Mac/README.rst)
.

\--enable-universalsdk[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-universalsdk "Link to this definition")

\--enable-universalsdk\=SDKDIR[¶](https://docs.python.org/3/using/configure.html#cmdoption-0 "Link to this definition")

Create a universal binary build. _SDKDIR_ specifies which macOS SDK should be used to perform the build (default is no).

\--enable-framework[¶](https://docs.python.org/3/using/configure.html#cmdoption-enable-framework "Link to this definition")

\--enable-framework\=INSTALLDIR[¶](https://docs.python.org/3/using/configure.html#cmdoption-1 "Link to this definition")

Create a Python.framework rather than a traditional Unix install. Optional _INSTALLDIR_ specifies the installation path (default is no).

\--with-universal-archs\=ARCH[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-universal-archs "Link to this definition")

Specify the kind of universal binary that should be created. This option is only valid when [`--enable-universalsdk`](https://docs.python.org/3/using/configure.html#cmdoption-enable-universalsdk)
 is set.

Options:

*   `universal2` (x86-64 and arm64);
    
*   `32-bit` (PPC and i386);
    
*   `64-bit` (PPC64 and x86-64);
    
*   `3-way` (i386, PPC and x86-64);
    
*   `intel` (i386 and x86-64);
    
*   `intel-32` (i386);
    
*   `intel-64` (x86-64);
    
*   `all` (PPC, i386, PPC64 and x86-64).
    

Note that values for this configuration item are _not_ the same as the identifiers used for universal binary wheels on macOS. See the Python Packaging User Guide for details on the [packaging platform compatibility tags used on macOS](https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/#macos)

\--with-framework-name\=FRAMEWORK[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-framework-name "Link to this definition")

Specify the name for the python framework on macOS only valid when [`--enable-framework`](https://docs.python.org/3/using/configure.html#cmdoption-enable-framework)
 is set (default: `Python`).

\--with-app-store-compliance[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-app-store-compliance "Link to this definition")

\--with-app-store-compliance\=PATCH-FILE[¶](https://docs.python.org/3/using/configure.html#cmdoption-2 "Link to this definition")

The Python standard library contains strings that are known to trigger automated inspection tool errors when submitted for distribution by the macOS and iOS App Stores. If enabled, this option will apply the list of patches that are known to correct app store compliance. A custom patch file can also be specified. This option is disabled by default.

Added in version 3.13.

### 3.3.14. iOS options[¶](https://docs.python.org/3/using/configure.html#ios-options "Link to this heading")

See [Platforms/Apple/iOS/README.md](https://github.com/python/cpython/tree/3.15/Platforms/Apple/iOS/README.md)
.

\--enable-framework\=INSTALLDIR[¶](https://docs.python.org/3/using/configure.html#cmdoption-3 "Link to this definition")

Create a Python.framework. Unlike macOS, the _INSTALLDIR_ argument specifying the installation path is mandatory.

\--with-framework-name\=FRAMEWORK[¶](https://docs.python.org/3/using/configure.html#cmdoption-4 "Link to this definition")

Specify the name for the framework (default: `Python`).

### 3.3.15. Cross compiling options[¶](https://docs.python.org/3/using/configure.html#cross-compiling-options "Link to this heading")

Cross compiling, also known as cross building, can be used to build Python for another CPU architecture or platform. Cross compiling requires a Python interpreter for the build platform. The version of the build Python must match the version of the cross compiled host Python.

\--build\=BUILD[¶](https://docs.python.org/3/using/configure.html#cmdoption-build "Link to this definition")

configure for building on BUILD, usually guessed by **config.guess**.

\--host\=HOST[¶](https://docs.python.org/3/using/configure.html#cmdoption-host "Link to this definition")

cross-compile to build programs to run on HOST (target platform)

\--with-build-python\=path/to/python[¶](https://docs.python.org/3/using/configure.html#cmdoption-with-build-python "Link to this definition")

path to build `python` binary for cross compiling

Added in version 3.11.

CONFIG\_SITE\=file[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-CONFIG_SITE "Link to this definition")

An environment variable that points to a file with configure overrides.

Example _config.site_ file:

\# config.site-aarch64
ac\_cv\_buggy\_getaddrinfo\=no
ac\_cv\_file\_\_dev\_ptmx\=yes
ac\_cv\_file\_\_dev\_ptc\=no

HOSTRUNNER[¶](https://docs.python.org/3/using/configure.html#cmdoption-arg-HOSTRUNNER "Link to this definition")

Program to run CPython for the host platform for cross-compilation.

Added in version 3.11.

Cross compiling example:

Copy

CONFIG\_SITE\=config.site-aarch64 ../configure \\
    \--build\=x86\_64-pc-linux-gnu \\
    \--host\=aarch64-unknown-linux-gnu \\
    \--with-build-python\=../x86\_64/python

3.4. Python build system[¶](https://docs.python.org/3/using/configure.html#python-build-system "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

### 3.4.1. Main files of the build system[¶](https://docs.python.org/3/using/configure.html#main-files-of-the-build-system "Link to this heading")

*   `configure.ac` => `configure`;
    
*   `Makefile.pre.in` => `Makefile` (created by `configure`);
    
*   `pyconfig.h` (created by `configure`);
    
*   `Modules/Setup`: C extensions built by the Makefile using `Module/makesetup` shell script;
    

### 3.4.2. Main build steps[¶](https://docs.python.org/3/using/configure.html#main-build-steps "Link to this heading")

*   C files (`.c`) are built as object files (`.o`).
    
*   A static `libpython` library (`.a`) is created from objects files.
    
*   `python.o` and the static `libpython` library are linked into the final `python` program.
    
*   C extensions are built by the Makefile (see `Modules/Setup`).
    

### 3.4.3. Main Makefile targets[¶](https://docs.python.org/3/using/configure.html#main-makefile-targets "Link to this heading")

make[¶](https://docs.python.org/3/using/configure.html#make "Link to this definition")

For the most part, when rebuilding after editing some code or refreshing your checkout from upstream, all you need to do is execute `make`, which (per Make’s semantics) builds the default target, the first one defined in the Makefile. By tradition (including in the CPython project) this is usually the `all` target. The `configure` script expands an `autoconf` variable, `@DEF_MAKE_ALL_RULE@` to describe precisely which targets `make all` will build. The choices are:

*   `profile-opt` (configured with `--enable-optimizations`)
    
*   `bolt-opt` (configured with `--enable-bolt`)
    
*   `build_emscripten` (chosen if the host platform matches `wasm32-emscripten`)
    
*   `build_wasm` (chosen if the host platform matches `wasm32-wasi*`)
    
*   `build_all` (configured without explicitly using any of the others)
    

Depending on the most recent source file changes, Make will rebuild any targets (object files and executables) deemed out-of-date, including running `configure` again if necessary. Source/target dependencies are many and maintained manually however, so Make sometimes doesn’t have all the information necessary to correctly detect all targets which need to be rebuilt. Depending on which targets aren’t rebuilt, you might experience a number of problems. If you have build or test problems which you can’t otherwise explain, `make clean && make` should work around most dependency problems, at the expense of longer build times.

make platform[¶](https://docs.python.org/3/using/configure.html#make-platform "Link to this definition")

Build the `python` program, but don’t build the standard library extension modules. This generates a file named `platform` which contains a single line describing the details of the build platform, for example, `macosx-14.3-arm64-3.12` or `linux-x86_64-3.13`.

make profile-opt[¶](https://docs.python.org/3/using/configure.html#make-profile-opt "Link to this definition")

Build Python using profile-guided optimization (PGO). You can use the configure [`--enable-optimizations`](https://docs.python.org/3/using/configure.html#cmdoption-enable-optimizations)
 option to make this the default target of the `make` command (`make all` or just `make`).

make clean[¶](https://docs.python.org/3/using/configure.html#make-clean "Link to this definition")

Remove built files.

make distclean[¶](https://docs.python.org/3/using/configure.html#make-distclean "Link to this definition")

In addition to the work done by `make clean`, remove files created by the configure script. `configure` will have to be run before building again. [\[7\]](https://docs.python.org/3/using/configure.html#id18)

make install[¶](https://docs.python.org/3/using/configure.html#make-install "Link to this definition")

Build the `all` target and install Python.

make test[¶](https://docs.python.org/3/using/configure.html#make-test "Link to this definition")

Build the `all` target and run the Python test suite with the `--fast-ci` option without GUI tests. Variables:

*   `TESTOPTS`: additional regrtest command-line options.
    
*   `TESTPYTHONOPTS`: additional Python command-line options.
    
*   `TESTTIMEOUT`: timeout in seconds (default: 10 minutes).
    

make ci[¶](https://docs.python.org/3/using/configure.html#make-ci "Link to this definition")

This is similar to `make test`, but uses the `-ugui` to also run GUI tests.

Added in version 3.14.

make buildbottest[¶](https://docs.python.org/3/using/configure.html#make-buildbottest "Link to this definition")

This is similar to `make test`, but uses the `--slow-ci` option and default timeout of 20 minutes, instead of `--fast-ci` option.

make regen-all[¶](https://docs.python.org/3/using/configure.html#make-regen-all "Link to this definition")

Regenerate (almost) all generated files. These include (but are not limited to) bytecode cases, and parser generator files. See [Generated files](https://docs.python.org/3/using/configure.html#generated-files)
 for the targets that must be run separately.

### 3.4.4. C extensions[¶](https://docs.python.org/3/using/configure.html#c-extensions "Link to this heading")

Some C extensions are built as built-in modules, like the `sys` module. They are built with the `Py_BUILD_CORE_BUILTIN` macro defined. Built-in modules have no `__file__` attribute:

Copy

\>>> import sys
\>>> sys
<module 'sys' (built-in)>
\>>> sys.\_\_file\_\_
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'sys' has no attribute '\_\_file\_\_'

Other C extensions are built as dynamic libraries, like the `_zoneinfo` module. They are built with the `Py_BUILD_CORE_MODULE` macro defined. For example on Linux x86-64:

Copy

\>>> import \_zoneinfo
\>>> \_zoneinfo
<module '\_zoneinfo' from '/.../lib.linux-x86\_64-3.16/\_zoneinfo.cpython-316d-x86\_64-linux-gnu.so'>
\>>> \_zoneinfo.\_\_file\_\_
'/.../lib.linux-x86\_64-3.16/\_zoneinfo.cpython-316d-x86\_64-linux-gnu.so'

`Modules/Setup` is used to generate Makefile targets to build C extensions. At the beginning of the files, C extensions are built as built-in modules. Extensions defined after the `*shared*` marker are built as dynamic libraries.

The [`PyAPI_FUNC()`](https://docs.python.org/3/c-api/intro.html#c.PyAPI_FUNC "PyAPI_FUNC")
, [`PyAPI_DATA()`](https://docs.python.org/3/c-api/intro.html#c.PyAPI_DATA "PyAPI_DATA")
 and [`PyMODINIT_FUNC`](https://docs.python.org/3/c-api/extension-modules.html#c.PyMODINIT_FUNC "PyMODINIT_FUNC")
 macros of `Include/exports.h` are defined differently depending if the `Py_BUILD_CORE_MODULE` macro is defined:

*   Use `Py_EXPORTED_SYMBOL` if the `Py_BUILD_CORE_MODULE` is defined
    
*   Use `Py_IMPORTED_SYMBOL` otherwise.
    

If the `Py_BUILD_CORE_BUILTIN` macro is used by mistake on a C extension built as a shared library, its `PyInit__xxx_()` function is not exported, causing an [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
 on import.

3.5. Compiler and linker flags[¶](https://docs.python.org/3/using/configure.html#compiler-and-linker-flags "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

Options set by the `./configure` script and environment variables and used by `Makefile`.

### 3.5.1. Preprocessor flags[¶](https://docs.python.org/3/using/configure.html#preprocessor-flags "Link to this heading")

CONFIGURE\_CPPFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-CONFIGURE_CPPFLAGS "Link to this definition")

Value of [`CPPFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CPPFLAGS)
 variable passed to the `./configure` script.

Added in version 3.6.

CPPFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-CPPFLAGS "Link to this definition")

(Objective) C/C++ preprocessor flags, e.g. `-I_include_dir_` if you have headers in a nonstandard directory _include\_dir_.

Both [`CPPFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CPPFLAGS)
 and [`LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS)
 need to contain the shell’s value to be able to build extension modules using the directories specified in the environment variables.

BASECPPFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-BASECPPFLAGS "Link to this definition")

Added in version 3.4.

PY\_CPPFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-PY_CPPFLAGS "Link to this definition")

Extra preprocessor flags added for building the interpreter object files.

Default: `$(BASECPPFLAGS) -I. -I$(srcdir)/Include $(CONFIGURE_CPPFLAGS) $(CPPFLAGS)`.

Added in version 3.2.

### 3.5.2. Compiler flags[¶](https://docs.python.org/3/using/configure.html#compiler-flags "Link to this heading")

CC[¶](https://docs.python.org/3/using/configure.html#envvar-CC "Link to this definition")

C compiler command.

Example: `gcc -pthread`.

CXX[¶](https://docs.python.org/3/using/configure.html#envvar-CXX "Link to this definition")

C++ compiler command.

Example: `g++ -pthread`.

CFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-CFLAGS "Link to this definition")

C compiler flags.

CFLAGS\_NODIST[¶](https://docs.python.org/3/using/configure.html#envvar-CFLAGS_NODIST "Link to this definition")

[`CFLAGS_NODIST`](https://docs.python.org/3/using/configure.html#envvar-CFLAGS_NODIST)
 is used for building the interpreter and stdlib C extensions. Use it when a compiler flag should _not_ be part of [`CFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CFLAGS)
 once Python is installed ([gh-65320](https://github.com/python/cpython/issues/65320)
).

In particular, [`CFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CFLAGS)
 should not contain:

*   the compiler flag `-I` (for setting the search path for include files). The `-I` flags are processed from left to right, and any flags in [`CFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CFLAGS)
     would take precedence over user- and package-supplied `-I` flags.
    
*   hardening flags such as `-Werror` because distributions cannot control whether packages installed by users conform to such heightened standards.
    

Added in version 3.5.

COMPILEALL\_OPTS[¶](https://docs.python.org/3/using/configure.html#envvar-COMPILEALL_OPTS "Link to this definition")

Options passed to the [`compileall`](https://docs.python.org/3/library/compileall.html#module-compileall "compileall: Tools for byte-compiling all Python source files in a directory tree.")
 command line when building PYC files in `make install`. Default: `-j0`.

Added in version 3.12.

EXTRA\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-EXTRA_CFLAGS "Link to this definition")

Extra C compiler flags.

CONFIGURE\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-CONFIGURE_CFLAGS "Link to this definition")

Value of [`CFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CFLAGS)
 variable passed to the `./configure` script.

Added in version 3.2.

CONFIGURE\_CFLAGS\_NODIST[¶](https://docs.python.org/3/using/configure.html#envvar-CONFIGURE_CFLAGS_NODIST "Link to this definition")

Value of [`CFLAGS_NODIST`](https://docs.python.org/3/using/configure.html#envvar-CFLAGS_NODIST)
 variable passed to the `./configure` script.

Added in version 3.5.

BASECFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-BASECFLAGS "Link to this definition")

Base compiler flags.

OPT[¶](https://docs.python.org/3/using/configure.html#envvar-OPT "Link to this definition")

Optimization flags.

CFLAGS\_ALIASING[¶](https://docs.python.org/3/using/configure.html#envvar-CFLAGS_ALIASING "Link to this definition")

Strict or non-strict aliasing flags used to compile `Python/dtoa.c`.

Added in version 3.7.

CFLAGS\_CEVAL[¶](https://docs.python.org/3/using/configure.html#envvar-CFLAGS_CEVAL "Link to this definition")

Flags used to compile `Python/ceval.c`.

Added in version 3.14.5.

CCSHARED[¶](https://docs.python.org/3/using/configure.html#envvar-CCSHARED "Link to this definition")

Compiler flags used to build a shared library.

For example, `-fPIC` is used on Linux and on BSD.

CFLAGSFORSHARED[¶](https://docs.python.org/3/using/configure.html#envvar-CFLAGSFORSHARED "Link to this definition")

Extra C flags added for building the interpreter object files.

Default: `$(CCSHARED)` when [`--enable-shared`](https://docs.python.org/3/using/configure.html#cmdoption-enable-shared)
 is used, or an empty string otherwise.

PY\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-PY_CFLAGS "Link to this definition")

Default: `$(BASECFLAGS) $(OPT) $(CONFIGURE_CFLAGS) $(CFLAGS) $(EXTRA_CFLAGS)`.

PY\_CFLAGS\_NODIST[¶](https://docs.python.org/3/using/configure.html#envvar-PY_CFLAGS_NODIST "Link to this definition")

Default: `$(CONFIGURE_CFLAGS_NODIST) $(CFLAGS_NODIST) -I$(srcdir)/Include/internal`.

Added in version 3.5.

PY\_STDMODULE\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-PY_STDMODULE_CFLAGS "Link to this definition")

C flags used for building the interpreter object files.

Default: `$(PY_CFLAGS) $(PY_CFLAGS_NODIST) $(PY_CPPFLAGS) $(CFLAGSFORSHARED)`.

Added in version 3.7.

PY\_CORE\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-PY_CORE_CFLAGS "Link to this definition")

Default: `$(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE`.

Added in version 3.2.

PY\_BUILTIN\_MODULE\_CFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-PY_BUILTIN_MODULE_CFLAGS "Link to this definition")

Compiler flags to build a standard library extension module as a built-in module, like the [`posix`](https://docs.python.org/3/library/posix.html#module-posix "posix: The most common POSIX system calls (normally used via module os).")
 module.

Default: `$(PY_STDMODULE_CFLAGS) -DPy_BUILD_CORE_BUILTIN`.

Added in version 3.8.

PURIFY[¶](https://docs.python.org/3/using/configure.html#envvar-PURIFY "Link to this definition")

Purify command. Purify is a memory debugger program.

Default: empty string (not used).

### 3.5.3. Linker flags[¶](https://docs.python.org/3/using/configure.html#linker-flags "Link to this heading")

LINKCC[¶](https://docs.python.org/3/using/configure.html#envvar-LINKCC "Link to this definition")

Linker command used to build programs like `python` and `_testembed`.

Default: `$(PURIFY) $(CC)`.

CONFIGURE\_LDFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-CONFIGURE_LDFLAGS "Link to this definition")

Value of [`LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS)
 variable passed to the `./configure` script.

Avoid assigning [`CFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CFLAGS)
, [`LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS)
, etc. so users can use them on the command line to append to these values without stomping the pre-set values.

Added in version 3.2.

LDFLAGS\_NODIST[¶](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS_NODIST "Link to this definition")

[`LDFLAGS_NODIST`](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS_NODIST)
 is used in the same manner as [`CFLAGS_NODIST`](https://docs.python.org/3/using/configure.html#envvar-CFLAGS_NODIST)
. Use it when a linker flag should _not_ be part of [`LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS)
 once Python is installed ([gh-65320](https://github.com/python/cpython/issues/65320)
).

In particular, [`LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS)
 should not contain:

*   the compiler flag `-L` (for setting the search path for libraries). The `-L` flags are processed from left to right, and any flags in [`LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS)
     would take precedence over user- and package-supplied `-L` flags.
    

CONFIGURE\_LDFLAGS\_NODIST[¶](https://docs.python.org/3/using/configure.html#envvar-CONFIGURE_LDFLAGS_NODIST "Link to this definition")

Value of [`LDFLAGS_NODIST`](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS_NODIST)
 variable passed to the `./configure` script.

Added in version 3.8.

LDFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS "Link to this definition")

Linker flags, e.g. `-L_lib_dir_` if you have libraries in a nonstandard directory _lib\_dir_.

Both [`CPPFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CPPFLAGS)
 and [`LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS)
 need to contain the shell’s value to be able to build extension modules using the directories specified in the environment variables.

Please consider using `EXE_LDFLAGS` if the supplied linker flags are executable specific, e.g. GCC’s `-pie` flag.

LIBS[¶](https://docs.python.org/3/using/configure.html#envvar-LIBS "Link to this definition")

Linker flags to pass libraries to the linker when linking the Python executable.

Example: `-lrt`.

LDSHARED[¶](https://docs.python.org/3/using/configure.html#envvar-LDSHARED "Link to this definition")

Command to build a shared library.

Default: `@LDSHARED@ $(PY_LDFLAGS)`.

BLDSHARED[¶](https://docs.python.org/3/using/configure.html#envvar-BLDSHARED "Link to this definition")

Command to build `libpython` shared library.

Default: `@BLDSHARED@ $(PY_CORE_LDFLAGS)`.

PY\_LDFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-PY_LDFLAGS "Link to this definition")

Default: `$(CONFIGURE_LDFLAGS) $(LDFLAGS)`.

PY\_LDFLAGS\_NODIST[¶](https://docs.python.org/3/using/configure.html#envvar-PY_LDFLAGS_NODIST "Link to this definition")

Default: `$(CONFIGURE_LDFLAGS_NODIST) $(LDFLAGS_NODIST)`.

Added in version 3.8.

PY\_CORE\_LDFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-PY_CORE_LDFLAGS "Link to this definition")

Linker flags used for building the interpreter object files.

Added in version 3.8.

EXE\_LDFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-EXE_LDFLAGS "Link to this definition")

Linker flags used for building executable targets such as the interpreter. If supplied, [`PY_CORE_EXE_LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-PY_CORE_EXE_LDFLAGS)
 will be used in replacement of [`PY_CORE_LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-PY_CORE_LDFLAGS)
.

Added in version 3.15.

CONFIGURE\_EXE\_LDFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-CONFIGURE_EXE_LDFLAGS "Link to this definition")

Value of [`EXE_LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-EXE_LDFLAGS)
 variable passed to the `./configure` script.

Added in version 3.15.

PY\_CORE\_EXE\_LDFLAGS[¶](https://docs.python.org/3/using/configure.html#envvar-PY_CORE_EXE_LDFLAGS "Link to this definition")

Linker flags used for building the interpreter and executable targets.

Default: `$(PY_CORE_LDFLAGS)`

Added in version 3.15.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [3\. Configure Python](https://docs.python.org/3/using/configure.html#)
    *   [3.1. Build requirements](https://docs.python.org/3/using/configure.html#build-requirements)
        *   [3.1.1. Requirements for optional modules](https://docs.python.org/3/using/configure.html#requirements-for-optional-modules)
            
    *   [3.2. Generated files](https://docs.python.org/3/using/configure.html#generated-files)
        *   [3.2.1. configure script](https://docs.python.org/3/using/configure.html#configure-script)
            
    *   [3.3. Configure options](https://docs.python.org/3/using/configure.html#configure-options)
        *   [3.3.1. General options](https://docs.python.org/3/using/configure.html#general-options)
            
        *   [3.3.2. C compiler options](https://docs.python.org/3/using/configure.html#c-compiler-options)
            
        *   [3.3.3. Linker options](https://docs.python.org/3/using/configure.html#linker-options)
            
        *   [3.3.4. Options for third-party dependencies](https://docs.python.org/3/using/configure.html#options-for-third-party-dependencies)
            
        *   [3.3.5. WebAssembly options](https://docs.python.org/3/using/configure.html#webassembly-options)
            
        *   [3.3.6. Install options](https://docs.python.org/3/using/configure.html#install-options)
            
        *   [3.3.7. Performance options](https://docs.python.org/3/using/configure.html#performance-options)
            
        *   [3.3.8. Python debug build](https://docs.python.org/3/using/configure.html#python-debug-build)
            
        *   [3.3.9. Debug options](https://docs.python.org/3/using/configure.html#debug-options)
            
        *   [3.3.10. Linker options](https://docs.python.org/3/using/configure.html#id16)
            
        *   [3.3.11. Libraries options](https://docs.python.org/3/using/configure.html#libraries-options)
            
        *   [3.3.12. Security options](https://docs.python.org/3/using/configure.html#security-options)
            
        *   [3.3.13. macOS options](https://docs.python.org/3/using/configure.html#macos-options)
            
        *   [3.3.14. iOS options](https://docs.python.org/3/using/configure.html#ios-options)
            
        *   [3.3.15. Cross compiling options](https://docs.python.org/3/using/configure.html#cross-compiling-options)
            
    *   [3.4. Python build system](https://docs.python.org/3/using/configure.html#python-build-system)
        *   [3.4.1. Main files of the build system](https://docs.python.org/3/using/configure.html#main-files-of-the-build-system)
            
        *   [3.4.2. Main build steps](https://docs.python.org/3/using/configure.html#main-build-steps)
            
        *   [3.4.3. Main Makefile targets](https://docs.python.org/3/using/configure.html#main-makefile-targets)
            
        *   [3.4.4. C extensions](https://docs.python.org/3/using/configure.html#c-extensions)
            
    *   [3.5. Compiler and linker flags](https://docs.python.org/3/using/configure.html#compiler-and-linker-flags)
        *   [3.5.1. Preprocessor flags](https://docs.python.org/3/using/configure.html#preprocessor-flags)
            
        *   [3.5.2. Compiler flags](https://docs.python.org/3/using/configure.html#compiler-flags)
            
        *   [3.5.3. Linker flags](https://docs.python.org/3/using/configure.html#linker-flags)
            

#### Previous topic

[2\. Using Python on Unix platforms](https://docs.python.org/3/using/unix.html "previous chapter")

#### Next topic

[4\. Using Python on Windows](https://docs.python.org/3/using/windows.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=3.+Configure+Python&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fusing%2Fconfigure.html&pagesource=using%2Fconfigure.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/using/configure.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/windows.html "4. Using Python on Windows")
     |
*   [previous](https://docs.python.org/3/using/unix.html "2. Using Python on Unix platforms")
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
*   [3\. Configure Python](https://docs.python.org/3/using/configure.html)
    
*    
    
    |
*   Theme Auto Light Dark |