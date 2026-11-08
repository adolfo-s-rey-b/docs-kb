### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/io.html "io — Core tools for working with streams")
     |
*   [previous](https://docs.python.org/3/library/allos.html "Generic Operating System Services")
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
*   [Generic Operating System Services](https://docs.python.org/3/library/allos.html)
     »
*   [`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`os` — Miscellaneous operating system interfaces[¶](https://docs.python.org/3/library/os.html#module-os "Link to this heading")

================================================================================================================================

**Source code:** [Lib/os.py](https://github.com/python/cpython/tree/3.15/Lib/os.py)

* * *

This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
, if you want to manipulate paths, see the [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
 module, and if you want to read all the lines in all the files on the command line see the [`fileinput`](https://docs.python.org/3/library/fileinput.html#module-fileinput "fileinput: Loop over standard input or a list of files.")
 module. For creating temporary files and directories see the [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile "tempfile: Generate temporary files and directories.")
 module, and for high-level file and directory handling see the [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")
 module.

Notes on the availability of these functions:

*   The design of all built-in operating system dependent modules of Python is such that as long as the same functionality is available, it uses the same interface; for example, the function `os.stat(path)` returns stat information about _path_ in the same format (which happens to have originated with the POSIX interface).
    
*   Extensions peculiar to a particular operating system are also available through the `os` module, but using them is of course a threat to portability.
    
*   All functions accepting path or file names accept both bytes and string objects, and result in an object of the same type, if a path or file name is returned.
    
*   On VxWorks, os.popen, os.fork, os.execv and os.spawn\*p\* are not supported.
    
*   On WebAssembly platforms, Android and iOS, large parts of the `os` module are not available or behave differently. APIs related to processes (e.g. [`fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
    , [`execve()`](https://docs.python.org/3/library/os.html#os.execve "os.execve")
    ) and resources (e.g. [`nice()`](https://docs.python.org/3/library/os.html#os.nice "os.nice")
    ) are not available. Others like [`getuid()`](https://docs.python.org/3/library/os.html#os.getuid "os.getuid")
     and [`getpid()`](https://docs.python.org/3/library/os.html#os.getpid "os.getpid")
     are emulated or stubs. WebAssembly platforms also lack support for signals (e.g. [`kill()`](https://docs.python.org/3/library/os.html#os.kill "os.kill")
    , [`wait()`](https://docs.python.org/3/library/os.html#os.wait "os.wait")
    ).
    

Note

All functions in this module raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 (or subclasses thereof) in the case of invalid or inaccessible file names and paths, or other arguments that have the correct type, but are not accepted by the operating system.

exception os.error[¶](https://docs.python.org/3/library/os.html#os.error "Link to this definition")

An alias for the built-in [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exception.

os.name[¶](https://docs.python.org/3/library/os.html#os.name "Link to this definition")

The name of the operating system dependent module imported. The following names have currently been registered: `'posix'`, `'nt'`, `'java'`.

See also

[`sys.platform`](https://docs.python.org/3/library/sys.html#sys.platform "sys.platform")
 has a finer granularity. [`os.uname()`](https://docs.python.org/3/library/os.html#os.uname "os.uname")
 gives system-dependent version information.

The [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")
 module provides detailed checks for the system’s identity.

File Names, Command Line Arguments, and Environment Variables[¶](https://docs.python.org/3/library/os.html#file-names-command-line-arguments-and-environment-variables "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In Python, file names, command line arguments, and environment variables are represented using the string type. On some systems, decoding these strings to and from bytes is necessary before passing them to the operating system. Python uses the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 to perform this conversion (see [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding")
).

The [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 are configured at Python startup by the [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read")
 function: see [`filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")
 and [`filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")
 members of [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
.

Changed in version 3.1: On some systems, conversion using the file system encoding may fail. In this case, Python uses the [surrogateescape encoding error handler](https://docs.python.org/3/library/codecs.html#surrogateescape)
, which means that undecodable bytes are replaced by a Unicode character U+DC_xx_ on decoding, and these are again translated to the original byte on encoding.

The [file system encoding](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 must guarantee to successfully decode all bytes below 128. If the file system encoding fails to provide this guarantee, API functions can raise [`UnicodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeError "UnicodeError")
.

See also the [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding)
.

Python UTF-8 Mode[¶](https://docs.python.org/3/library/os.html#python-utf-8-mode "Link to this heading")

---------------------------------------------------------------------------------------------------------

Added in version 3.7: See [**PEP 540**](https://peps.python.org/pep-0540/)
 for more details.

Changed in version 3.15: Python UTF-8 mode is now enabled by default ([**PEP 686**](https://peps.python.org/pep-0686/)
). It may be disabled by setting [`PYTHONUTF8=0`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8)
 as an environment variable or by using the [`-X utf8=0`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line option.

The Python UTF-8 Mode ignores the [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding)
 and forces the usage of the UTF-8 encoding:

*   Use UTF-8 as the [filesystem encoding](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
    .
    
*   [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding")
     returns `'utf-8'`.
    
*   [`locale.getpreferredencoding()`](https://docs.python.org/3/library/locale.html#locale.getpreferredencoding "locale.getpreferredencoding")
     returns `'utf-8'` (the _do\_setlocale_ argument has no effect).
    
*   [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
    , [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
    , and [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
     all use UTF-8 as their text encoding, with the `surrogateescape` [error handler](https://docs.python.org/3/library/codecs.html#error-handlers)
     being enabled for `sys.stdin` and `sys.stdout` (`sys.stderr` continues to use `backslashreplace` as it does in the default locale-aware mode)
    
*   On Unix, [`os.device_encoding()`](https://docs.python.org/3/library/os.html#os.device_encoding "os.device_encoding")
     returns `'utf-8'` rather than the device encoding.
    

Note that the standard stream settings in UTF-8 mode can be overridden by [`PYTHONIOENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONIOENCODING)
 (just as they can be in the default locale-aware mode).

As a consequence of the changes in those lower level APIs, other higher level APIs also exhibit different default behaviours:

*   Command line arguments, environment variables and filenames are decoded to text using the UTF-8 encoding.
    
*   [`os.fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode")
     and [`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode")
     use the UTF-8 encoding.
    
*   [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
    , [`io.open()`](https://docs.python.org/3/library/io.html#io.open "io.open")
    , and [`codecs.open()`](https://docs.python.org/3/library/codecs.html#codecs.open "codecs.open")
     use the UTF-8 encoding by default. However, they still use the strict error handler by default so that attempting to open a binary file in text mode is likely to raise an exception rather than producing nonsense data.
    

The [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
 is enabled by default. It can be disabled using the [`-X utf8=0`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command line option or the [`PYTHONUTF8=0`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8)
 environment variable. The Python UTF-8 Mode can only be disabled at Python startup. Its value can be read from [`sys.flags.utf8_mode`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags")
.

If the UTF-8 mode is disabled, the interpreter defaults to using the current locale settings, _unless_ the current locale is identified as a legacy ASCII-based locale (as described for [`PYTHONCOERCECLOCALE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONCOERCECLOCALE)
), and locale coercion is either disabled or fails. In such legacy locales, the interpreter will default to enabling UTF-8 mode unless explicitly instructed not to do so.

See also the [UTF-8 mode on Windows](https://docs.python.org/3/using/windows.html#win-utf8-mode)
 and the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

Process Parameters[¶](https://docs.python.org/3/library/os.html#process-parameters "Link to this heading")

-----------------------------------------------------------------------------------------------------------

These functions and data items provide information and operate on the current process and user.

os.ctermid()[¶](https://docs.python.org/3/library/os.html#os.ctermid "Link to this definition")

Return the filename corresponding to the controlling terminal of the process.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.environ[¶](https://docs.python.org/3/library/os.html#os.environ "Link to this definition")

A [mapping](https://docs.python.org/3/glossary.html#term-mapping)
 object where keys and values are strings that represent the process environment. For example, `environ['HOME']` is the pathname of your home directory (on some platforms), and is equivalent to `getenv("HOME")` in C.

This mapping is captured the first time the `os` module is imported, typically during Python startup as part of processing `site.py`. Changes to the environment made after this time are not reflected in `os.environ`, except for changes made by modifying `os.environ` directly.

This mapping may be used to modify the environment as well as query the environment. [`putenv()`](https://docs.python.org/3/library/os.html#os.putenv "os.putenv")
 will be called automatically when the mapping is modified.

On Unix, keys and values use [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding")
 and `'surrogateescape'` error handler. Use [`environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb")
 if you would like to use a different encoding.

On Windows, the keys are converted to uppercase. This also applies when getting, setting, or deleting an item. For example, `environ['monty'] = 'python'` maps the key `'MONTY'` to the value `'python'`.

Note

Calling [`putenv()`](https://docs.python.org/3/library/os.html#os.putenv "os.putenv")
 directly does not change `os.environ`, so it’s better to modify `os.environ`.

Note

On some platforms, including FreeBSD and macOS, setting `environ` may cause memory leaks. Refer to the system documentation for `putenv()`.

You can delete items in this mapping to unset environment variables. [`unsetenv()`](https://docs.python.org/3/library/os.html#os.unsetenv "os.unsetenv")
 will be called automatically when an item is deleted from `os.environ`, and when one of the [`pop()`](https://docs.python.org/3/builtins/stdtypes.html#dict.pop "dict.pop")
 or [`clear()`](https://docs.python.org/3/builtins/stdtypes.html#dict.clear "dict.clear")
 methods is called.

If the _[clearenv(3)](https://manpages.debian.org/clearenv(3))
_ function is available, the [`clear()`](https://docs.python.org/3/builtins/stdtypes.html#dict.clear "dict.clear")
 method uses it and emits a single `os._clearenv` audit event. Otherwise, it emits an `os.unsetenv` event on each deleted variable.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.unsetenv` with argument `key`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os._clearenv` with no arguments.

See also

The [`os.reload_environ()`](https://docs.python.org/3/library/os.html#os.reload_environ "os.reload_environ")
 function.

Changed in version 3.9: Updated to support [**PEP 584**](https://peps.python.org/pep-0584/)
’s merge (`|`) and update (`|=`) operators.

Changed in version 3.15: The [`clear()`](https://docs.python.org/3/builtins/stdtypes.html#dict.clear "dict.clear")
 method can now emit an `os._clearenv` audit event.

os.environb[¶](https://docs.python.org/3/library/os.html#os.environb "Link to this definition")

Bytes version of [`environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
: a [mapping](https://docs.python.org/3/glossary.html#term-mapping)
 object where both keys and values are [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 objects representing the process environment. `environ` and `environb` are synchronized (modifying `environb` updates `environ`, and vice versa).

`environb` is only available if [`supports_bytes_environ`](https://docs.python.org/3/library/os.html#os.supports_bytes_environ "os.supports_bytes_environ")
 is `True`.

Added in version 3.2.

Changed in version 3.9: Updated to support [**PEP 584**](https://peps.python.org/pep-0584/)
’s merge (`|`) and update (`|=`) operators.

os.reload\_environ()[¶](https://docs.python.org/3/library/os.html#os.reload_environ "Link to this definition")

The [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
 and [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb")
 mappings are a cache of environment variables at the time that Python started. As such, changes to the current process environment are not reflected if made outside Python, or by [`os.putenv()`](https://docs.python.org/3/library/os.html#os.putenv "os.putenv")
 or [`os.unsetenv()`](https://docs.python.org/3/library/os.html#os.unsetenv "os.unsetenv")
. Use `os.reload_environ()` to update `os.environ` and `os.environb` with any such changes to the current process environment.

Warning

This function is not thread-safe. Calling it while the environment is being modified in another thread is an undefined behavior. Reading from [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
 or [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb")
, or calling [`os.getenv()`](https://docs.python.org/3/library/os.html#os.getenv "os.getenv")
 while reloading, may return an empty result.

Added in version 3.14.

os.chdir(_path_)

os.fchdir(_fd_)

os.getcwd()

These functions are described in [Files and Directories](https://docs.python.org/3/library/os.html#os-file-dir)
.

os.fsencode(_filename_)[¶](https://docs.python.org/3/library/os.html#os.fsencode "Link to this definition")

Encode [path-like](https://docs.python.org/3/glossary.html#term-path-like-object)
 _filename_ to the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
; return [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 unchanged.

[`fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode")
 is the reverse function.

Added in version 3.2.

Changed in version 3.6: Support added to accept objects implementing the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface.

os.fsdecode(_filename_)[¶](https://docs.python.org/3/library/os.html#os.fsdecode "Link to this definition")

Decode the [path-like](https://docs.python.org/3/glossary.html#term-path-like-object)
 _filename_ from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
; return [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 unchanged.

[`fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode")
 is the reverse function.

Added in version 3.2.

Changed in version 3.6: Support added to accept objects implementing the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface.

os.fspath(_path_)[¶](https://docs.python.org/3/library/os.html#os.fspath "Link to this definition")

Return the file system representation of the path.

If [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 is passed in, it is returned unchanged. Otherwise [`__fspath__()`](https://docs.python.org/3/library/os.html#os.PathLike.__fspath__ "os.PathLike.__fspath__")
 is called and its value is returned as long as it is a `str` or `bytes` object. In all other cases, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised.

Added in version 3.6.

class os.PathLike[¶](https://docs.python.org/3/library/os.html#os.PathLike "Link to this definition")

An [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 for objects representing a file system path, e.g. [`pathlib.PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath")
.

Added in version 3.6.

abstractmethod \_\_fspath\_\_()[¶](https://docs.python.org/3/library/os.html#os.PathLike.__fspath__ "Link to this definition")

Return the file system path representation of the object.

The method should only return a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object, with the preference being for `str`.

os.getenv(_key_, _default\=None_)[¶](https://docs.python.org/3/library/os.html#os.getenv "Link to this definition")

Return the value of the environment variable _key_ as a string if it exists, or _default_ if it doesn’t. _key_ is a string. Note that since `getenv()` uses [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
, the mapping of `getenv()` is similarly also captured on import, and the function may not reflect future environment changes.

On Unix, keys and values are decoded with [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding")
 and `'surrogateescape'` error handler. Use [`os.getenvb()`](https://docs.python.org/3/library/os.html#os.getenvb "os.getenvb")
 if you would like to use a different encoding.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

os.getenvb(_key_, _default\=None_)[¶](https://docs.python.org/3/library/os.html#os.getenvb "Link to this definition")

Return the value of the environment variable _key_ as bytes if it exists, or _default_ if it doesn’t. _key_ must be bytes. Note that since `getenvb()` uses [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb")
, the mapping of `getenvb()` is similarly also captured on import, and the function may not reflect future environment changes.

`getenvb()` is only available if [`supports_bytes_environ`](https://docs.python.org/3/library/os.html#os.supports_bytes_environ "os.supports_bytes_environ")
 is `True`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.2.

os.get\_exec\_path(_env\=None_)[¶](https://docs.python.org/3/library/os.html#os.get_exec_path "Link to this definition")

Returns the list of directories that will be searched for a named executable, similar to a shell, when launching a process. _env_, when specified, should be an environment variable dictionary to lookup the PATH in. By default, when _env_ is `None`, [`environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
 is used.

Added in version 3.2.

os.getegid()[¶](https://docs.python.org/3/library/os.html#os.getegid "Link to this definition")

Return the effective group id of the current process. This corresponds to the “set id” bit on the file being executed in the current process.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.geteuid()[¶](https://docs.python.org/3/library/os.html#os.geteuid "Link to this definition")

Return the current process’s effective user id.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.getgid()[¶](https://docs.python.org/3/library/os.html#os.getgid "Link to this definition")

Return the real group id of the current process.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

os.getgrouplist(_user_, _group_, _/_)[¶](https://docs.python.org/3/library/os.html#os.getgrouplist "Link to this definition")

Return list of group ids that _user_ belongs to. If _group_ is not in the list, it is included; typically, _group_ is specified as the group ID field from the password record for _user_, because that group ID will otherwise be potentially omitted.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.3.

os.getgroups()[¶](https://docs.python.org/3/library/os.html#os.getgroups "Link to this definition")

Return list of supplemental group ids associated with the current process.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Note

On macOS, `getgroups()` behavior differs somewhat from other Unix platforms. If the Python interpreter was built with a deployment target of `10.5` or earlier, `getgroups()` returns the list of effective group ids associated with the current user process; this list is limited to a system-defined number of entries, typically 16, and may be modified by calls to [`setgroups()`](https://docs.python.org/3/library/os.html#os.setgroups "os.setgroups")
 if suitably privileged. If built with a deployment target greater than `10.5`, `getgroups()` returns the current group access list for the user associated with the effective user id of the process; the group access list may change over the lifetime of the process, it is not affected by calls to `setgroups()`, and its length is not limited to 16. The deployment target value can be obtained with [`sysconfig.get_config_var('MACOSX_DEPLOYMENT_TARGET')`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_var "sysconfig.get_config_var")
.

os.getlogin()[¶](https://docs.python.org/3/library/os.html#os.getlogin "Link to this definition")

Return the name of the user logged in on the controlling terminal of the process. For most purposes, it is more useful to use [`getpass.getuser()`](https://docs.python.org/3/library/getpass.html#getpass.getuser "getpass.getuser")
 since the latter checks the environment variables `LOGNAME` or `USERNAME` to find out who the user is, and falls back to `pwd.getpwuid(os.getuid())[0]` to get the login name of the current real user id.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI.

os.getpgid(_pid_)[¶](https://docs.python.org/3/library/os.html#os.getpgid "Link to this definition")

Return the process group id of the process with process id _pid_. If _pid_ is 0, the process group id of the current process is returned.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.getpgrp()[¶](https://docs.python.org/3/library/os.html#os.getpgrp "Link to this definition")

Return the id of the current process group.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.getpid()[¶](https://docs.python.org/3/library/os.html#os.getpid "Link to this definition")

Return the current process id.

The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

os.getppid()[¶](https://docs.python.org/3/library/os.html#os.getppid "Link to this definition")

Return the parent’s process id. When the parent process has exited, on Unix the id returned is the one of the init process (1), on Windows it is still the same id, which may be already reused by another process.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI.

Changed in version 3.2: Added support for Windows.

os.getpriority(_which_, _who_)[¶](https://docs.python.org/3/library/os.html#os.getpriority "Link to this definition")

Get program scheduling priority. The value _which_ is one of [`PRIO_PROCESS`](https://docs.python.org/3/library/os.html#os.PRIO_PROCESS "os.PRIO_PROCESS")
, [`PRIO_PGRP`](https://docs.python.org/3/library/os.html#os.PRIO_PGRP "os.PRIO_PGRP")
, or [`PRIO_USER`](https://docs.python.org/3/library/os.html#os.PRIO_USER "os.PRIO_USER")
, and _who_ is interpreted relative to _which_ (a process identifier for `PRIO_PROCESS`, process group identifier for `PRIO_PGRP`, and a user ID for `PRIO_USER`). A zero value for _who_ denotes (respectively) the calling process, the process group of the calling process, or the real user ID of the calling process.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.3.

os.PRIO\_PROCESS[¶](https://docs.python.org/3/library/os.html#os.PRIO_PROCESS "Link to this definition")

os.PRIO\_PGRP[¶](https://docs.python.org/3/library/os.html#os.PRIO_PGRP "Link to this definition")

os.PRIO\_USER[¶](https://docs.python.org/3/library/os.html#os.PRIO_USER "Link to this definition")

Parameters for the [`getpriority()`](https://docs.python.org/3/library/os.html#os.getpriority "os.getpriority")
 and [`setpriority()`](https://docs.python.org/3/library/os.html#os.setpriority "os.setpriority")
 functions.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.3.

os.PRIO\_DARWIN\_THREAD[¶](https://docs.python.org/3/library/os.html#os.PRIO_DARWIN_THREAD "Link to this definition")

os.PRIO\_DARWIN\_PROCESS[¶](https://docs.python.org/3/library/os.html#os.PRIO_DARWIN_PROCESS "Link to this definition")

os.PRIO\_DARWIN\_BG[¶](https://docs.python.org/3/library/os.html#os.PRIO_DARWIN_BG "Link to this definition")

os.PRIO\_DARWIN\_NONUI[¶](https://docs.python.org/3/library/os.html#os.PRIO_DARWIN_NONUI "Link to this definition")

Parameters for the [`getpriority()`](https://docs.python.org/3/library/os.html#os.getpriority "os.getpriority")
 and [`setpriority()`](https://docs.python.org/3/library/os.html#os.setpriority "os.setpriority")
 functions.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: macOS

Added in version 3.12.

os.getresuid()[¶](https://docs.python.org/3/library/os.html#os.getresuid "Link to this definition")

Return a tuple (ruid, euid, suid) denoting the current process’s real, effective, and saved user ids.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not macOS, not iOS.

Added in version 3.2.

os.getresgid()[¶](https://docs.python.org/3/library/os.html#os.getresgid "Link to this definition")

Return a tuple (rgid, egid, sgid) denoting the current process’s real, effective, and saved group ids.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not macOS, not iOS.

Added in version 3.2.

os.getuid()[¶](https://docs.python.org/3/library/os.html#os.getuid "Link to this definition")

Return the current process’s real user id.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

os.initgroups(_username_, _gid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.initgroups "Link to this definition")

Call the system `initgroups()` to initialize the group access list with all of the groups of which the specified username is a member, plus the specified group id.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android.

Added in version 3.2.

os.putenv(_key_, _value_, _/_)[¶](https://docs.python.org/3/library/os.html#os.putenv "Link to this definition")

Set the environment variable named _key_ to the string _value_. Such changes to the environment affect subprocesses started with [`os.system()`](https://docs.python.org/3/library/os.html#os.system "os.system")
, [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")
 or [`fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
 and [`execv()`](https://docs.python.org/3/library/os.html#os.execv "os.execv")
.

Assignments to items in [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
 are automatically translated into corresponding calls to `putenv()`; however, calls to `putenv()` don’t update `os.environ`, so it is actually preferable to assign to items of `os.environ`. This also applies to [`getenv()`](https://docs.python.org/3/library/os.html#os.getenv "os.getenv")
 and [`getenvb()`](https://docs.python.org/3/library/os.html#os.getenvb "os.getenvb")
, which respectively use `os.environ` and [`os.environb`](https://docs.python.org/3/library/os.html#os.environb "os.environb")
 in their implementations.

See also the [`os.reload_environ()`](https://docs.python.org/3/library/os.html#os.reload_environ "os.reload_environ")
 function.

Note

On some platforms, including FreeBSD and macOS, setting `environ` may cause memory leaks. Refer to the system documentation for `putenv()`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.putenv` with arguments `key`, `value`.

Changed in version 3.9: The function is now always available.

os.setegid(_egid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.setegid "Link to this definition")

Set the current process’s effective group id.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android.

os.seteuid(_euid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.seteuid "Link to this definition")

Set the current process’s effective user id.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android.

os.setgid(_gid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.setgid "Link to this definition")

Set the current process’ group id.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android.

os.setgroups(_groups_, _/_)[¶](https://docs.python.org/3/library/os.html#os.setgroups "Link to this definition")

Set the list of supplemental group ids associated with the current process to _groups_. _groups_ must be a sequence, and each element must be an integer identifying a group. This operation is typically available only to the superuser.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Note

On macOS, the length of _groups_ may not exceed the system-defined maximum number of effective group ids, typically 16. See the documentation for [`getgroups()`](https://docs.python.org/3/library/os.html#os.getgroups "os.getgroups")
 for cases where it may not return the same group list set by calling setgroups().

os.setns(_fd_, _nstype\=0_)[¶](https://docs.python.org/3/library/os.html#os.setns "Link to this definition")

Reassociate the current thread with a Linux namespace. See the _[setns(2)](https://manpages.debian.org/setns(2))
_ and _[namespaces(7)](https://manpages.debian.org/namespaces(7))
_ man pages for more details.

If _fd_ refers to a `/proc/_pid_/ns/` link, `setns()` reassociates the calling thread with the namespace associated with that link, and _nstype_ may be set to one of the [CLONE\_NEW\* constants](https://docs.python.org/3/library/os.html#os-unshare-clone-flags)
 to impose constraints on the operation (`0` means no constraints).

Since Linux 5.8, _fd_ may refer to a PID file descriptor obtained from [`pidfd_open()`](https://docs.python.org/3/library/os.html#os.pidfd_open "os.pidfd_open")
. In this case, `setns()` reassociates the calling thread into one or more of the same namespaces as the thread referred to by _fd_. This is subject to any constraints imposed by _nstype_, which is a bit mask combining one or more of the [CLONE\_NEW\* constants](https://docs.python.org/3/library/os.html#os-unshare-clone-flags)
, e.g. `setns(fd, os.CLONE_NEWUTS | os.CLONE_NEWPID)`. The caller’s memberships in unspecified namespaces are left unchanged.

_fd_ can be any object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method, or a raw file descriptor.

This example reassociates the thread with the `init` process’s network namespace:

Copy

fd \= os.open("/proc/1/ns/net", os.O\_RDONLY)
os.setns(fd, os.CLONE\_NEWNET)
os.close(fd)

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 3.0 with glibc >= 2.14.

Added in version 3.12.

See also

The [`unshare()`](https://docs.python.org/3/library/os.html#os.unshare "os.unshare")
 function.

os.setpgrp()[¶](https://docs.python.org/3/library/os.html#os.setpgrp "Link to this definition")

Call the system call `setpgrp()` or `setpgrp(0, 0)` depending on which version is implemented (if any). See the Unix manual for the semantics.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.setpgid(_pid_, _pgrp_, _/_)[¶](https://docs.python.org/3/library/os.html#os.setpgid "Link to this definition")

Call the system call `setpgid()` to set the process group id of the process with id _pid_ to the process group with id _pgrp_. See the Unix manual for the semantics.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.setpriority(_which_, _who_, _priority_)[¶](https://docs.python.org/3/library/os.html#os.setpriority "Link to this definition")

Set program scheduling priority. The value _which_ is one of [`PRIO_PROCESS`](https://docs.python.org/3/library/os.html#os.PRIO_PROCESS "os.PRIO_PROCESS")
, [`PRIO_PGRP`](https://docs.python.org/3/library/os.html#os.PRIO_PGRP "os.PRIO_PGRP")
, or [`PRIO_USER`](https://docs.python.org/3/library/os.html#os.PRIO_USER "os.PRIO_USER")
, and _who_ is interpreted relative to _which_ (a process identifier for `PRIO_PROCESS`, process group identifier for `PRIO_PGRP`, and a user ID for `PRIO_USER`). A zero value for _who_ denotes (respectively) the calling process, the process group of the calling process, or the real user ID of the calling process. _priority_ is a value in the range -20 to 19. The default priority is 0; lower priorities cause more favorable scheduling.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.3.

os.setregid(_rgid_, _egid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.setregid "Link to this definition")

Set the current process’s real and effective group ids.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android.

os.setresgid(_rgid_, _egid_, _sgid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.setresgid "Link to this definition")

Set the current process’s real, effective, and saved group ids.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not macOS, not iOS.

Added in version 3.2.

os.setresuid(_ruid_, _euid_, _suid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.setresuid "Link to this definition")

Set the current process’s real, effective, and saved user ids.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not macOS, not iOS.

Added in version 3.2.

os.setreuid(_ruid_, _euid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.setreuid "Link to this definition")

Set the current process’s real and effective user ids.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android.

os.getsid(_pid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.getsid "Link to this definition")

Call the system call `getsid()`. See the Unix manual for the semantics.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.setsid()[¶](https://docs.python.org/3/library/os.html#os.setsid "Link to this definition")

Call the system call `setsid()`. See the Unix manual for the semantics.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.setuid(_uid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.setuid "Link to this definition")

Set the current process’s user id.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android.

os.strerror(_code_, _/_)[¶](https://docs.python.org/3/library/os.html#os.strerror "Link to this definition")

Return the error message corresponding to the error code in _code_. On platforms where `strerror()` returns `NULL` when given an unknown error number, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised.

os.supports\_bytes\_environ[¶](https://docs.python.org/3/library/os.html#os.supports_bytes_environ "Link to this definition")

`True` if the native OS type of the environment is bytes (eg. `False` on Windows).

Added in version 3.2.

os.umask(_mask_, _/_)[¶](https://docs.python.org/3/library/os.html#os.umask "Link to this definition")

Set the current numeric umask and return the previous umask.

The function is a stub on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

os.uname()[¶](https://docs.python.org/3/library/os.html#os.uname "Link to this definition")

Returns information identifying the current operating system. The return value is a [`uname_result`](https://docs.python.org/3/library/os.html#os.uname_result "os.uname_result")
.

On macOS, iOS and Android, this returns the _kernel_ name and release (i.e., `'Darwin'` on macOS and iOS; `'Linux'` on Android). [`platform.uname()`](https://docs.python.org/3/library/platform.html#platform.uname "platform.uname")
 can be used to get the user-facing operating system name and release on iOS and Android.

See also

[`sys.platform`](https://docs.python.org/3/library/sys.html#sys.platform "sys.platform")
 which has finer granularity.

The [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")
 module provides detailed checks for the system’s identity.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Changed in version 3.3: Return type changed from a tuple to a tuple-like object with named attributes.

class os.uname\_result[¶](https://docs.python.org/3/library/os.html#os.uname_result "Link to this definition")

Name and information about the system returned by [`os.uname()`](https://docs.python.org/3/library/os.html#os.uname "os.uname")
. These attributes correspond to the members described in _[uname(2)](https://manpages.debian.org/uname(2))
_.

For backwards compatibility, this object is also iterable, behaving like a five-tuple containing [`sysname`](https://docs.python.org/3/library/os.html#os.uname_result.sysname "os.uname_result.sysname")
, [`nodename`](https://docs.python.org/3/library/os.html#os.uname_result.nodename "os.uname_result.nodename")
, [`release`](https://docs.python.org/3/library/os.html#os.uname_result.release "os.uname_result.release")
, [`version`](https://docs.python.org/3/library/os.html#os.uname_result.version "os.uname_result.version")
, and [`machine`](https://docs.python.org/3/library/os.html#os.uname_result.machine "os.uname_result.machine")
 in that order.

sysname[¶](https://docs.python.org/3/library/os.html#os.uname_result.sysname "Link to this definition")

Operating system name.

nodename[¶](https://docs.python.org/3/library/os.html#os.uname_result.nodename "Link to this definition")

Name of machine on network. Some systems truncate `nodename` to 8 characters or to the leading component; a better way to get the hostname is [`socket.gethostname()`](https://docs.python.org/3/library/socket.html#socket.gethostname "socket.gethostname")
 or even `socket.gethostbyaddr(socket.gethostname())`.

release[¶](https://docs.python.org/3/library/os.html#os.uname_result.release "Link to this definition")

Operating system release.

version[¶](https://docs.python.org/3/library/os.html#os.uname_result.version "Link to this definition")

Operating system version.

machine[¶](https://docs.python.org/3/library/os.html#os.uname_result.machine "Link to this definition")

Hardware identifier.

os.unsetenv(_key_, _/_)[¶](https://docs.python.org/3/library/os.html#os.unsetenv "Link to this definition")

Unset (delete) the environment variable named _key_. Such changes to the environment affect subprocesses started with [`os.system()`](https://docs.python.org/3/library/os.html#os.system "os.system")
, [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")
 or [`fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
 and [`execv()`](https://docs.python.org/3/library/os.html#os.execv "os.execv")
.

Deletion of items in [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
 is automatically translated into a corresponding call to `unsetenv()`; however, calls to `unsetenv()` don’t update `os.environ`, so it is actually preferable to delete items of `os.environ`.

See also the [`os.reload_environ()`](https://docs.python.org/3/library/os.html#os.reload_environ "os.reload_environ")
 function.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.unsetenv` with argument `key`.

Changed in version 3.9: The function is now always available and is also available on Windows.

os.unshare(_flags_)[¶](https://docs.python.org/3/library/os.html#os.unshare "Link to this definition")

Disassociate parts of the process execution context, and move them into a newly created namespace. See the _[unshare(2)](https://manpages.debian.org/unshare(2))
_ man page for more details. The _flags_ argument is a bit mask, combining zero or more of the [CLONE\_\* constants](https://docs.python.org/3/library/os.html#os-unshare-clone-flags)
, that specifies which parts of the execution context should be unshared from their existing associations and moved to a new namespace. If the _flags_ argument is `0`, no changes are made to the calling process’s execution context.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.16.

Added in version 3.12.

See also

The [`setns()`](https://docs.python.org/3/library/os.html#os.setns "os.setns")
 function.

Flags to the [`unshare()`](https://docs.python.org/3/library/os.html#os.unshare "os.unshare")
 function, if the implementation supports them. See _[unshare(2)](https://manpages.debian.org/unshare(2))
_ in the Linux manual for their exact effect and availability.

os.CLONE\_FILES[¶](https://docs.python.org/3/library/os.html#os.CLONE_FILES "Link to this definition")

os.CLONE\_FS[¶](https://docs.python.org/3/library/os.html#os.CLONE_FS "Link to this definition")

os.CLONE\_NEWCGROUP[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWCGROUP "Link to this definition")

os.CLONE\_NEWIPC[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWIPC "Link to this definition")

os.CLONE\_NEWNET[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWNET "Link to this definition")

os.CLONE\_NEWNS[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWNS "Link to this definition")

os.CLONE\_NEWPID[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWPID "Link to this definition")

os.CLONE\_NEWTIME[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWTIME "Link to this definition")

os.CLONE\_NEWUSER[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWUSER "Link to this definition")

os.CLONE\_NEWUTS[¶](https://docs.python.org/3/library/os.html#os.CLONE_NEWUTS "Link to this definition")

os.CLONE\_SIGHAND[¶](https://docs.python.org/3/library/os.html#os.CLONE_SIGHAND "Link to this definition")

os.CLONE\_SYSVSEM[¶](https://docs.python.org/3/library/os.html#os.CLONE_SYSVSEM "Link to this definition")

os.CLONE\_THREAD[¶](https://docs.python.org/3/library/os.html#os.CLONE_THREAD "Link to this definition")

os.CLONE\_VM[¶](https://docs.python.org/3/library/os.html#os.CLONE_VM "Link to this definition")

File Object Creation[¶](https://docs.python.org/3/library/os.html#file-object-creation "Link to this heading")

---------------------------------------------------------------------------------------------------------------

These functions create new [file objects](https://docs.python.org/3/glossary.html#term-file-object)
. (See also [`open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 for opening file descriptors.)

os.fdopen(_fd_, _\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/os.html#os.fdopen "Link to this definition")

Return an open file object connected to the file descriptor _fd_. This is an alias of the [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 built-in function and accepts the same arguments. The only difference is that the first argument of `fdopen()` must always be an integer.

File Descriptor Operations[¶](https://docs.python.org/3/library/os.html#file-descriptor-operations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

These functions operate on I/O streams referenced using file descriptors.

File descriptors are small integers corresponding to a file that has been opened by the current process. For example, standard input is usually file descriptor 0, standard output is 1, and standard error is 2. Further files opened by a process will then be assigned 3, 4, 5, and so forth. The name “file descriptor” is slightly deceptive; on Unix platforms, sockets and pipes are also referenced by file descriptors.

The [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method can be used to obtain the file descriptor associated with a [file object](https://docs.python.org/3/glossary.html#term-file-object)
 when required. Note that using the file descriptor directly will bypass the file object methods, ignoring aspects such as internal buffering of data.

os.close(_fd_)[¶](https://docs.python.org/3/library/os.html#os.close "Link to this definition")

Close file descriptor _fd_.

Note

This function is intended for low-level I/O and must be applied to a file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 or [`pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe")
. To close a “file object” returned by the built-in function [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 or by [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")
 or [`fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen")
, use its [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close")
 method.

os.closerange(_fd\_low_, _fd\_high_, _/_)[¶](https://docs.python.org/3/library/os.html#os.closerange "Link to this definition")

Close all file descriptors from _fd\_low_ (inclusive) to _fd\_high_ (exclusive), ignoring errors. Equivalent to (but much faster than):

Copy

for fd in range(fd\_low, fd\_high):
    try:
        os.close(fd)
    except OSError:
        pass

os.copy\_file\_range(_src_, _dst_, _count_, _offset\_src\=None_, _offset\_dst\=None_)[¶](https://docs.python.org/3/library/os.html#os.copy_file_range "Link to this definition")

Copy _count_ bytes from file descriptor _src_, starting from offset _offset\_src_, to file descriptor _dst_, starting from offset _offset\_dst_. If _offset\_src_ is `None`, then _src_ is read from the current position; respectively for _offset\_dst_.

In Linux kernel older than 5.3, the files pointed to by _src_ and _dst_ must reside in the same filesystem, otherwise an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised with [`errno`](https://docs.python.org/3/builtins/exceptions.html#OSError.errno "OSError.errno")
 set to [`errno.EXDEV`](https://docs.python.org/3/library/errno.html#errno.EXDEV "errno.EXDEV")
.

This copy is done without the additional cost of transferring data from the kernel to user space and then back into the kernel. Additionally, some filesystems could implement extra optimizations, such as the use of reflinks (i.e., two or more inodes that share pointers to the same copy-on-write disk blocks; supported file systems include btrfs and XFS) and server-side copy (in the case of NFS).

The function copies bytes between two file descriptors. Text options, like the encoding and the line ending, are ignored.

The return value is the amount of bytes copied. This could be less than the amount requested.

Note

On Linux, `os.copy_file_range()` should not be used for copying a range of a pseudo file from a special filesystem like procfs and sysfs. It will always copy no bytes and return 0 as if the file was empty because of a known Linux kernel issue.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.5 with glibc >= 2.27.

Added in version 3.8.

os.device\_encoding(_fd_)[¶](https://docs.python.org/3/library/os.html#os.device_encoding "Link to this definition")

Return a string describing the encoding of the device associated with _fd_ if it is connected to a terminal; else return [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
.

On Unix, if the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
 is enabled, return `'UTF-8'` rather than the device encoding.

Changed in version 3.10: On Unix, the function now implements the Python UTF-8 Mode.

os.dup(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.dup "Link to this definition")

Return a duplicate of file descriptor _fd_. The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

On Windows, when duplicating a standard stream (0: stdin, 1: stdout, 2: stderr), the new file descriptor is [inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

Changed in version 3.4: The new file descriptor is now non-inheritable.

os.dup2(_fd_, _fd2_, _inheritable\=True_)[¶](https://docs.python.org/3/library/os.html#os.dup2 "Link to this definition")

Duplicate file descriptor _fd_ to _fd2_, closing the latter first if necessary. Return _fd2_. The new file descriptor is [inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
 by default or non-inheritable if _inheritable_ is `False`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

Changed in version 3.4: Add the optional _inheritable_ parameter.

Changed in version 3.7: Return _fd2_ on success. Previously, `None` was always returned.

os.fchmod(_fd_, _mode_)[¶](https://docs.python.org/3/library/os.html#os.fchmod "Link to this definition")

Change the mode of the file given by _fd_ to the numeric _mode_. See the docs for [`chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")
 for possible values of _mode_. As of Python 3.3, this is equivalent to `os.chmod(fd, mode)`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.chmod` with arguments `path`, `mode`, `dir_fd`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

Changed in version 3.13: Added support on Windows.

os.fchown(_fd_, _uid_, _gid_)[¶](https://docs.python.org/3/library/os.html#os.fchown "Link to this definition")

Change the owner and group id of the file given by _fd_ to the numeric _uid_ and _gid_. To leave one of the ids unchanged, set it to -1. See [`chown()`](https://docs.python.org/3/library/os.html#os.chown "os.chown")
. As of Python 3.3, this is equivalent to `os.chown(fd, uid, gid)`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.chown` with arguments `path`, `uid`, `gid`, `dir_fd`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

os.fdatasync(_fd_)[¶](https://docs.python.org/3/library/os.html#os.fdatasync "Link to this definition")

Force write of file with filedescriptor _fd_ to disk. Does not force update of metadata.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not macOS, not iOS.

os.fpathconf(_fd_, _name_, _/_)[¶](https://docs.python.org/3/library/os.html#os.fpathconf "Link to this definition")

Return system configuration information relevant to an open file. _name_ specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (POSIX.1, Unix 95, Unix 98, and others). Some platforms define additional names as well. The names known to the host operating system are given in the `pathconf_names` dictionary. For configuration variables not included in that mapping, passing an integer for _name_ is also accepted.

If _name_ is a string and is not known, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. If a specific value for _name_ is not supported by the host system, even if it is included in `pathconf_names`, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised with [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL")
 for the error number.

As of Python 3.3, this is equivalent to `os.pathconf(fd, name)`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

os.fstat(_fd_)[¶](https://docs.python.org/3/library/os.html#os.fstat "Link to this definition")

Get the status of the file descriptor _fd_. Return a [`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result")
 object.

As of Python 3.3, this is equivalent to `os.stat(fd)`.

See also

The [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 function.

os.fstatvfs(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.fstatvfs "Link to this definition")

Return information about the filesystem containing the file associated with file descriptor _fd_ in a [`statvfs_result`](https://docs.python.org/3/library/os.html#os.statvfs_result "os.statvfs_result")
, like [`statvfs()`](https://docs.python.org/3/library/os.html#os.statvfs "os.statvfs")
. As of Python 3.3, this is equivalent to `os.statvfs(fd)`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

os.fsync(_fd_)[¶](https://docs.python.org/3/library/os.html#os.fsync "Link to this definition")

Force write of file with filedescriptor _fd_ to disk. On Unix, this calls the native `fsync()` function; on Windows, the MS `_commit()` function.

If you’re starting with a buffered Python [file object](https://docs.python.org/3/glossary.html#term-file-object)
 _f_, first do `f.flush()`, and then do `os.fsync(f.fileno())`, to ensure that all internal buffers associated with _f_ are written to disk.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

os.ftruncate(_fd_, _length_, _/_)[¶](https://docs.python.org/3/library/os.html#os.ftruncate "Link to this definition")

Truncate the file corresponding to file descriptor _fd_, so that it is at most _length_ bytes in size. As of Python 3.3, this is equivalent to `os.truncate(fd, length)`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.truncate` with arguments `fd`, `length`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

Changed in version 3.5: Added support for Windows

os.get\_blocking(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.get_blocking "Link to this definition")

Get the blocking mode of the file descriptor: `False` if the [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK")
 flag is set, `True` if the flag is cleared.

See also [`set_blocking()`](https://docs.python.org/3/library/os.html#os.set_blocking "os.set_blocking")
 and [`socket.socket.setblocking()`](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "socket.socket.setblocking")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

On Windows, this function is limited to pipes.

Added in version 3.5.

Changed in version 3.12: Added support for pipes on Windows.

os.grantpt(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.grantpt "Link to this definition")

Grant access to the slave pseudo-terminal device associated with the master pseudo-terminal device to which the file descriptor _fd_ refers. The file descriptor _fd_ is not closed upon failure.

Calls the C standard library function `grantpt()`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.13.

os.isatty(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.isatty "Link to this definition")

Return `True` if the file descriptor _fd_ is open and connected to a tty(-like) device, else `False`.

os.lockf(_fd_, _cmd_, _len_, _/_)[¶](https://docs.python.org/3/library/os.html#os.lockf "Link to this definition")

Apply, test or remove a POSIX lock on an open file descriptor. _fd_ is an open file descriptor. _cmd_ specifies the command to use - one of [`F_LOCK`](https://docs.python.org/3/library/os.html#os.F_LOCK "os.F_LOCK")
, [`F_TLOCK`](https://docs.python.org/3/library/os.html#os.F_TLOCK "os.F_TLOCK")
, [`F_ULOCK`](https://docs.python.org/3/library/os.html#os.F_ULOCK "os.F_ULOCK")
 or [`F_TEST`](https://docs.python.org/3/library/os.html#os.F_TEST "os.F_TEST")
. _len_ specifies the section of the file to lock.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.lockf` with arguments `fd`, `cmd`, `len`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

os.F\_LOCK[¶](https://docs.python.org/3/library/os.html#os.F_LOCK "Link to this definition")

os.F\_TLOCK[¶](https://docs.python.org/3/library/os.html#os.F_TLOCK "Link to this definition")

os.F\_ULOCK[¶](https://docs.python.org/3/library/os.html#os.F_ULOCK "Link to this definition")

os.F\_TEST[¶](https://docs.python.org/3/library/os.html#os.F_TEST "Link to this definition")

Flags that specify what action [`lockf()`](https://docs.python.org/3/library/os.html#os.lockf "os.lockf")
 will take.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

os.login\_tty(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.login_tty "Link to this definition")

Prepare the tty of which fd is a file descriptor for a new login session. Make the calling process a session leader; make the tty the controlling tty, the stdin, the stdout, and the stderr of the calling process; close fd.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.11.

os.lseek(_fd_, _pos_, _whence_, _/_)[¶](https://docs.python.org/3/library/os.html#os.lseek "Link to this definition")

Set the current position of file descriptor _fd_ to position _pos_, modified by _whence_, and return the new position in bytes relative to the start of the file. Valid values for _whence_ are:

*   [`SEEK_SET`](https://docs.python.org/3/library/os.html#os.SEEK_SET "os.SEEK_SET")
     or `0` – set _pos_ relative to the beginning of the file
    
*   [`SEEK_CUR`](https://docs.python.org/3/library/os.html#os.SEEK_CUR "os.SEEK_CUR")
     or `1` – set _pos_ relative to the current file position
    
*   [`SEEK_END`](https://docs.python.org/3/library/os.html#os.SEEK_END "os.SEEK_END")
     or `2` – set _pos_ relative to the end of the file
    
*   [`SEEK_DATA`](https://docs.python.org/3/library/os.html#os.SEEK_DATA "os.SEEK_DATA")
     – set _pos_ to the next data location, relative to _pos_
    
*   [`SEEK_HOLE`](https://docs.python.org/3/library/os.html#os.SEEK_HOLE "os.SEEK_HOLE")
     – set _pos_ to the next data hole, relative to _pos_
    

Changed in version 3.3: Add support for `SEEK_HOLE` and `SEEK_DATA`.

os.SEEK\_SET[¶](https://docs.python.org/3/library/os.html#os.SEEK_SET "Link to this definition")

os.SEEK\_CUR[¶](https://docs.python.org/3/library/os.html#os.SEEK_CUR "Link to this definition")

os.SEEK\_END[¶](https://docs.python.org/3/library/os.html#os.SEEK_END "Link to this definition")

Parameters to the [`lseek()`](https://docs.python.org/3/library/os.html#os.lseek "os.lseek")
 function and the [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek")
 method on [file-like objects](https://docs.python.org/3/glossary.html#term-file-object)
, for whence to adjust the file position indicator.

[`SEEK_SET`](https://docs.python.org/3/library/os.html#os.SEEK_SET "os.SEEK_SET")

Adjust the file position relative to the beginning of the file.

[`SEEK_CUR`](https://docs.python.org/3/library/os.html#os.SEEK_CUR "os.SEEK_CUR")

Adjust the file position relative to the current file position.

[`SEEK_END`](https://docs.python.org/3/library/os.html#os.SEEK_END "os.SEEK_END")

Adjust the file position relative to the end of the file.

Their values are 0, 1, and 2, respectively.

os.SEEK\_HOLE[¶](https://docs.python.org/3/library/os.html#os.SEEK_HOLE "Link to this definition")

os.SEEK\_DATA[¶](https://docs.python.org/3/library/os.html#os.SEEK_DATA "Link to this definition")

Parameters to the [`lseek()`](https://docs.python.org/3/library/os.html#os.lseek "os.lseek")
 function and the [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek")
 method on [file-like objects](https://docs.python.org/3/glossary.html#term-file-object)
, for seeking file data and holes on sparsely allocated files.

`SEEK_DATA`

Adjust the file offset to the next location containing data, relative to the seek position.

`SEEK_HOLE`

Adjust the file offset to the next location containing a hole, relative to the seek position. A hole is defined as a sequence of zeros.

Note

These operations only make sense for filesystems that support them.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 3.1, macOS, Unix

Added in version 3.3.

os.open(_path_, _flags_, _mode\=0o777_, _\*_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.open "Link to this definition")

Open the file _path_ and set various flags according to _flags_ and possibly its mode according to _mode_. When computing _mode_, the current umask value is first masked out. Return the file descriptor for the newly opened file. The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

For a description of the flag and mode values, see the C run-time documentation; flag constants (like [`O_RDONLY`](https://docs.python.org/3/library/os.html#os.O_RDONLY "os.O_RDONLY")
 and [`O_WRONLY`](https://docs.python.org/3/library/os.html#os.O_WRONLY "os.O_WRONLY")
) are defined in the `os` module. In particular, on Windows adding [`O_BINARY`](https://docs.python.org/3/library/os.html#os.O_BINARY "os.O_BINARY")
 is needed to open files in binary mode.

This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
 with the _dir\_fd_ parameter.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `open` with arguments `path`, `mode`, `flags`.

Changed in version 3.4: The new file descriptor is now non-inheritable.

Note

This function is intended for low-level I/O. For normal usage, use the built-in function `open()`, which returns a [file object](https://docs.python.org/3/glossary.html#term-file-object)
 with [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read")
 and [`write()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "io.BufferedIOBase.write")
 methods. To wrap a file descriptor in a file object, use [`fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen")
.

Changed in version 3.3: Added the _dir\_fd_ parameter.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

The following constants are options for the _flags_ parameter to the [`open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 function. They can be combined using the bitwise OR operator `|`. Some of them are not available on all platforms. For descriptions of their availability and use, consult the _[open(2)](https://manpages.debian.org/open(2))
_ manual page on Unix or [the MSDN](https://msdn.microsoft.com/en-us/library/z0kc8e3z.aspx)
 on Windows.

os.O\_RDONLY[¶](https://docs.python.org/3/library/os.html#os.O_RDONLY "Link to this definition")

os.O\_WRONLY[¶](https://docs.python.org/3/library/os.html#os.O_WRONLY "Link to this definition")

os.O\_RDWR[¶](https://docs.python.org/3/library/os.html#os.O_RDWR "Link to this definition")

os.O\_APPEND[¶](https://docs.python.org/3/library/os.html#os.O_APPEND "Link to this definition")

os.O\_CREAT[¶](https://docs.python.org/3/library/os.html#os.O_CREAT "Link to this definition")

os.O\_EXCL[¶](https://docs.python.org/3/library/os.html#os.O_EXCL "Link to this definition")

os.O\_TRUNC[¶](https://docs.python.org/3/library/os.html#os.O_TRUNC "Link to this definition")

The above constants are available on Unix and Windows.

os.O\_DSYNC[¶](https://docs.python.org/3/library/os.html#os.O_DSYNC "Link to this definition")

os.O\_RSYNC[¶](https://docs.python.org/3/library/os.html#os.O_RSYNC "Link to this definition")

os.O\_SYNC[¶](https://docs.python.org/3/library/os.html#os.O_SYNC "Link to this definition")

os.O\_NDELAY[¶](https://docs.python.org/3/library/os.html#os.O_NDELAY "Link to this definition")

os.O\_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "Link to this definition")

os.O\_NOCTTY[¶](https://docs.python.org/3/library/os.html#os.O_NOCTTY "Link to this definition")

os.O\_CLOEXEC[¶](https://docs.python.org/3/library/os.html#os.O_CLOEXEC "Link to this definition")

The above constants are only available on Unix.

Changed in version 3.3: Add `O_CLOEXEC` constant.

os.O\_BINARY[¶](https://docs.python.org/3/library/os.html#os.O_BINARY "Link to this definition")

os.O\_NOINHERIT[¶](https://docs.python.org/3/library/os.html#os.O_NOINHERIT "Link to this definition")

os.O\_SHORT\_LIVED[¶](https://docs.python.org/3/library/os.html#os.O_SHORT_LIVED "Link to this definition")

os.O\_TEMPORARY[¶](https://docs.python.org/3/library/os.html#os.O_TEMPORARY "Link to this definition")

os.O\_RANDOM[¶](https://docs.python.org/3/library/os.html#os.O_RANDOM "Link to this definition")

os.O\_SEQUENTIAL[¶](https://docs.python.org/3/library/os.html#os.O_SEQUENTIAL "Link to this definition")

os.O\_TEXT[¶](https://docs.python.org/3/library/os.html#os.O_TEXT "Link to this definition")

The above constants are only available on Windows.

os.O\_EVTONLY[¶](https://docs.python.org/3/library/os.html#os.O_EVTONLY "Link to this definition")

os.O\_FSYNC[¶](https://docs.python.org/3/library/os.html#os.O_FSYNC "Link to this definition")

os.O\_SYMLINK[¶](https://docs.python.org/3/library/os.html#os.O_SYMLINK "Link to this definition")

os.O\_NOFOLLOW\_ANY[¶](https://docs.python.org/3/library/os.html#os.O_NOFOLLOW_ANY "Link to this definition")

The above constants are only available on macOS.

Changed in version 3.10: Add `O_EVTONLY`, `O_FSYNC`, `O_SYMLINK` and `O_NOFOLLOW_ANY` constants.

os.O\_ASYNC[¶](https://docs.python.org/3/library/os.html#os.O_ASYNC "Link to this definition")

os.O\_DIRECT[¶](https://docs.python.org/3/library/os.html#os.O_DIRECT "Link to this definition")

os.O\_DIRECTORY[¶](https://docs.python.org/3/library/os.html#os.O_DIRECTORY "Link to this definition")

os.O\_NOFOLLOW[¶](https://docs.python.org/3/library/os.html#os.O_NOFOLLOW "Link to this definition")

os.O\_NOATIME[¶](https://docs.python.org/3/library/os.html#os.O_NOATIME "Link to this definition")

os.O\_PATH[¶](https://docs.python.org/3/library/os.html#os.O_PATH "Link to this definition")

os.O\_TMPFILE[¶](https://docs.python.org/3/library/os.html#os.O_TMPFILE "Link to this definition")

os.O\_SHLOCK[¶](https://docs.python.org/3/library/os.html#os.O_SHLOCK "Link to this definition")

os.O\_EXLOCK[¶](https://docs.python.org/3/library/os.html#os.O_EXLOCK "Link to this definition")

The above constants are extensions and not present if they are not defined by the C library.

Changed in version 3.4: Add `O_PATH` on systems that support it. Add `O_TMPFILE`, only available on Linux Kernel 3.11 or newer.

os.openpty()[¶](https://docs.python.org/3/library/os.html#os.openpty "Link to this definition")

Open a new pseudo-terminal pair. Return a pair of file descriptors `(master, slave)` for the pty and the tty, respectively. The new file descriptors are [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
. For a (slightly) more portable approach, use the [`pty`](https://docs.python.org/3/library/pty.html#module-pty "pty: Pseudo-Terminal Handling for Unix.")
 module.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Changed in version 3.4: The new file descriptors are now non-inheritable.

os.pipe()[¶](https://docs.python.org/3/library/os.html#os.pipe "Link to this definition")

Create a pipe. Return a pair of file descriptors `(r, w)` usable for reading and writing, respectively. The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

Changed in version 3.4: The new file descriptors are now non-inheritable.

os.pipe2(_flags_, _/_)[¶](https://docs.python.org/3/library/os.html#os.pipe2 "Link to this definition")

Create a pipe with _flags_ set atomically. _flags_ can be constructed by ORing together one or more of these values: [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK")
, [`O_CLOEXEC`](https://docs.python.org/3/library/os.html#os.O_CLOEXEC "os.O_CLOEXEC")
. Return a pair of file descriptors `(r, w)` usable for reading and writing, respectively.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, macOS >= 27.0, not WASI, not iOS.

Added in version 3.3.

os.posix\_fallocate(_fd_, _offset_, _len_, _/_)[¶](https://docs.python.org/3/library/os.html#os.posix_fallocate "Link to this definition")

Ensures that enough disk space is allocated for the file specified by _fd_ starting from _offset_ and continuing for _len_ bytes.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not macOS, not iOS.

Added in version 3.3.

os.posix\_fadvise(_fd_, _offset_, _len_, _advice_, _/_)[¶](https://docs.python.org/3/library/os.html#os.posix_fadvise "Link to this definition")

Announces an intention to access data in a specific pattern thus allowing the kernel to make optimizations. The advice applies to the region of the file specified by _fd_ starting at _offset_ and continuing for _len_ bytes. _advice_ is one of [`POSIX_FADV_NORMAL`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_NORMAL "os.POSIX_FADV_NORMAL")
, [`POSIX_FADV_SEQUENTIAL`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_SEQUENTIAL "os.POSIX_FADV_SEQUENTIAL")
, [`POSIX_FADV_RANDOM`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_RANDOM "os.POSIX_FADV_RANDOM")
, [`POSIX_FADV_NOREUSE`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_NOREUSE "os.POSIX_FADV_NOREUSE")
, [`POSIX_FADV_WILLNEED`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_WILLNEED "os.POSIX_FADV_WILLNEED")
 or [`POSIX_FADV_DONTNEED`](https://docs.python.org/3/library/os.html#os.POSIX_FADV_DONTNEED "os.POSIX_FADV_DONTNEED")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not macOS, not iOS.

Added in version 3.3.

os.POSIX\_FADV\_NORMAL[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_NORMAL "Link to this definition")

os.POSIX\_FADV\_SEQUENTIAL[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_SEQUENTIAL "Link to this definition")

os.POSIX\_FADV\_RANDOM[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_RANDOM "Link to this definition")

os.POSIX\_FADV\_NOREUSE[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_NOREUSE "Link to this definition")

os.POSIX\_FADV\_WILLNEED[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_WILLNEED "Link to this definition")

os.POSIX\_FADV\_DONTNEED[¶](https://docs.python.org/3/library/os.html#os.POSIX_FADV_DONTNEED "Link to this definition")

Flags that can be used in _advice_ in [`posix_fadvise()`](https://docs.python.org/3/library/os.html#os.posix_fadvise "os.posix_fadvise")
 that specify the access pattern that is likely to be used.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

os.pread(_fd_, _n_, _offset_, _/_)[¶](https://docs.python.org/3/library/os.html#os.pread "Link to this definition")

Read at most _n_ bytes from file descriptor _fd_ at a position of _offset_, leaving the file offset unchanged.

Return a bytestring containing the bytes read. If the end of the file referred to by _fd_ has been reached, an empty bytes object is returned.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

os.posix\_openpt(_oflag_, _/_)[¶](https://docs.python.org/3/library/os.html#os.posix_openpt "Link to this definition")

Open and return a file descriptor for a master pseudo-terminal device.

Calls the C standard library function `posix_openpt()`. The _oflag_ argument is used to set file status flags and file access modes as specified in the manual page of `posix_openpt()` of your system.

The returned file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
. If the value [`O_CLOEXEC`](https://docs.python.org/3/library/os.html#os.O_CLOEXEC "os.O_CLOEXEC")
 is available on the system, it is added to _oflag_.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.13.

os.preadv(_fd_, _buffers_, _offset_, _flags\=0_, _/_)[¶](https://docs.python.org/3/library/os.html#os.preadv "Link to this definition")

Read from a file descriptor _fd_ at a position of _offset_ into mutable [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _buffers_, leaving the file offset unchanged. Transfer data into each buffer until it is full and then move on to the next buffer in the sequence to hold the rest of the data.

The flags argument contains a bitwise OR of zero or more of the following flags:

*   [`RWF_HIPRI`](https://docs.python.org/3/library/os.html#os.RWF_HIPRI "os.RWF_HIPRI")
    
*   [`RWF_NOWAIT`](https://docs.python.org/3/library/os.html#os.RWF_NOWAIT "os.RWF_NOWAIT")
    
*   [`RWF_DONTCACHE`](https://docs.python.org/3/library/os.html#os.RWF_DONTCACHE "os.RWF_DONTCACHE")
    

Return the total number of bytes actually read which can be less than the total capacity of all the objects.

The operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf")
 value `'SC_IOV_MAX'`) on the number of buffers that can be used.

Combine the functionality of [`os.readv()`](https://docs.python.org/3/library/os.html#os.readv "os.readv")
 and [`os.pread()`](https://docs.python.org/3/library/os.html#os.pread "os.pread")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.30, FreeBSD >= 6.0, OpenBSD >= 2.7, AIX >= 7.1.

Using flags requires Linux >= 4.6.

Added in version 3.7.

os.RWF\_NOWAIT[¶](https://docs.python.org/3/library/os.html#os.RWF_NOWAIT "Link to this definition")

Do not wait for data which is not immediately available. If this flag is specified, the system call will return instantly if it would have to read data from the backing storage or wait for a lock.

If some data was successfully read, it will return the number of bytes read. If no bytes were read, it will return `-1` and set errno to [`errno.EAGAIN`](https://docs.python.org/3/library/errno.html#errno.EAGAIN "errno.EAGAIN")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.14.

Added in version 3.7.

os.RWF\_HIPRI[¶](https://docs.python.org/3/library/os.html#os.RWF_HIPRI "Link to this definition")

High priority read/write. Allows block-based filesystems to use polling of the device, which provides lower latency, but may use additional resources.

Currently, on Linux, this feature is usable only on a file descriptor opened using the [`O_DIRECT`](https://docs.python.org/3/library/os.html#os.O_DIRECT "os.O_DIRECT")
 flag.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.6.

Added in version 3.7.

os.RWF\_DONTCACHE[¶](https://docs.python.org/3/library/os.html#os.RWF_DONTCACHE "Link to this definition")

Use uncached buffered IO.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 6.14

Added in version 3.15.

os.RWF\_ATOMIC[¶](https://docs.python.org/3/library/os.html#os.RWF_ATOMIC "Link to this definition")

Write data atomically. Requires alignment to the device’s atomic write unit.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 6.11

Added in version 3.15.

os.ptsname(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.ptsname "Link to this definition")

Return the name of the slave pseudo-terminal device associated with the master pseudo-terminal device to which the file descriptor _fd_ refers. The file descriptor _fd_ is not closed upon failure.

Calls the reentrant C standard library function `ptsname_r()` if it is available; otherwise, the C standard library function `ptsname()`, which is not guaranteed to be thread-safe, is called.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.13.

os.pwrite(_fd_, _str_, _offset_, _/_)[¶](https://docs.python.org/3/library/os.html#os.pwrite "Link to this definition")

Write the bytestring in _str_ to file descriptor _fd_ at position of _offset_, leaving the file offset unchanged.

Return the number of bytes actually written.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

os.pwritev(_fd_, _buffers_, _offset_, _flags\=0_, _/_)[¶](https://docs.python.org/3/library/os.html#os.pwritev "Link to this definition")

Write the _buffers_ contents to file descriptor _fd_ at an offset _offset_, leaving the file offset unchanged. _buffers_ must be a sequence of [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
. Buffers are processed in array order. Entire contents of the first buffer is written before proceeding to the second, and so on.

The flags argument contains a bitwise OR of zero or more of the following flags:

*   [`RWF_DSYNC`](https://docs.python.org/3/library/os.html#os.RWF_DSYNC "os.RWF_DSYNC")
    
*   [`RWF_SYNC`](https://docs.python.org/3/library/os.html#os.RWF_SYNC "os.RWF_SYNC")
    
*   [`RWF_APPEND`](https://docs.python.org/3/library/os.html#os.RWF_APPEND "os.RWF_APPEND")
    
*   [`RWF_DONTCACHE`](https://docs.python.org/3/library/os.html#os.RWF_DONTCACHE "os.RWF_DONTCACHE")
    
*   [`RWF_ATOMIC`](https://docs.python.org/3/library/os.html#os.RWF_ATOMIC "os.RWF_ATOMIC")
    

Return the total number of bytes actually written.

The operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf")
 value `'SC_IOV_MAX'`) on the number of buffers that can be used.

Combine the functionality of [`os.writev()`](https://docs.python.org/3/library/os.html#os.writev "os.writev")
 and [`os.pwrite()`](https://docs.python.org/3/library/os.html#os.pwrite "os.pwrite")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.30, FreeBSD >= 6.0, OpenBSD >= 2.7, AIX >= 7.1.

Using flags requires Linux >= 4.6.

Added in version 3.7.

os.RWF\_DSYNC[¶](https://docs.python.org/3/library/os.html#os.RWF_DSYNC "Link to this definition")

Provide a per-write equivalent of the [`O_DSYNC`](https://docs.python.org/3/library/os.html#os.O_DSYNC "os.O_DSYNC")
 [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 flag. This flag effect applies only to the data range written by the system call.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.7.

Added in version 3.7.

os.RWF\_SYNC[¶](https://docs.python.org/3/library/os.html#os.RWF_SYNC "Link to this definition")

Provide a per-write equivalent of the [`O_SYNC`](https://docs.python.org/3/library/os.html#os.O_SYNC "os.O_SYNC")
 [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 flag. This flag effect applies only to the data range written by the system call.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.7.

Added in version 3.7.

os.RWF\_APPEND[¶](https://docs.python.org/3/library/os.html#os.RWF_APPEND "Link to this definition")

Provide a per-write equivalent of the [`O_APPEND`](https://docs.python.org/3/library/os.html#os.O_APPEND "os.O_APPEND")
 [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 flag. This flag is meaningful only for [`os.pwritev()`](https://docs.python.org/3/library/os.html#os.pwritev "os.pwritev")
, and its effect applies only to the data range written by the system call. The _offset_ argument does not affect the write operation; the data is always appended to the end of the file. However, if the _offset_ argument is `-1`, the current file _offset_ is updated.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.16.

Added in version 3.10.

os.read(_fd_, _n_, _/_)[¶](https://docs.python.org/3/library/os.html#os.read "Link to this definition")

Read at most _n_ bytes from file descriptor _fd_.

Return a bytestring containing the bytes read. If the end of the file referred to by _fd_ has been reached, an empty bytes object is returned.

Note

This function is intended for low-level I/O and must be applied to a file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 or [`pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe")
. To read a “file object” returned by the built-in function [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 or by [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")
 or [`fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen")
, or [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
, use its [`read()`](https://docs.python.org/3/library/io.html#io.TextIOBase.read "io.TextIOBase.read")
 or [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline")
 methods.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

os.readinto(_fd_, _buffer_, _/_)[¶](https://docs.python.org/3/library/os.html#os.readinto "Link to this definition")

Read from a file descriptor _fd_ into a mutable [buffer object](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
 _buffer_.

The _buffer_ should be mutable and [bytes-like](https://docs.python.org/3/glossary.html#term-bytes-like-object)
. On success, returns the number of bytes read. Less bytes may be read than the size of the buffer. The underlying system call will be retried when interrupted by a signal, unless the signal handler raises an exception. Other errors will not be retried and an error will be raised.

Returns 0 if _fd_ is at end of file or if the provided _buffer_ has length 0 (which can be used to check for errors without reading data). Never returns negative.

Note

This function is intended for low-level I/O and must be applied to a file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 or [`os.pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe")
. To read a “file object” returned by the built-in function [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
, or [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
, use its member functions, for example [`io.BufferedIOBase.readinto()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto")
, [`io.BufferedIOBase.read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read")
, or [`io.TextIOBase.read()`](https://docs.python.org/3/library/io.html#io.TextIOBase.read "io.TextIOBase.read")

Added in version 3.14.

os.sendfile(_out\_fd_, _in\_fd_, _offset_, _count_)[¶](https://docs.python.org/3/library/os.html#os.sendfile "Link to this definition")

os.sendfile(_out\_fd_, _in\_fd_, _offset_, _count_, _headers\=()_, _trailers\=()_, _flags\=0_)

Copy _count_ bytes from file descriptor _in\_fd_ to file descriptor _out\_fd_ starting at _offset_. Return the number of bytes sent. When EOF is reached return `0`.

The first function notation is supported by all platforms that define `sendfile()`.

On Linux, if _offset_ is given as `None`, the bytes are read from the current position of _in\_fd_ and the position of _in\_fd_ is updated.

The second case may be used on macOS and FreeBSD where _headers_ and _trailers_ are arbitrary sequences of buffers that are written before and after the data from _in\_fd_ is written. It returns the same as the first case.

On macOS and FreeBSD, a value of `0` for _count_ specifies to send until the end of _in\_fd_ is reached.

All platforms support sockets as _out\_fd_ file descriptor, and some platforms allow other types (e.g. regular file, pipe) as well.

Cross-platform applications should not use _headers_, _trailers_ and _flags_ arguments.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Note

For a higher-level wrapper of `sendfile()`, see [`socket.socket.sendfile()`](https://docs.python.org/3/library/socket.html#socket.socket.sendfile "socket.socket.sendfile")
.

Added in version 3.3.

Changed in version 3.9: Parameters _out_ and _in_ was renamed to _out\_fd_ and _in\_fd_.

os.SF\_NODISKIO[¶](https://docs.python.org/3/library/os.html#os.SF_NODISKIO "Link to this definition")

os.SF\_MNOWAIT[¶](https://docs.python.org/3/library/os.html#os.SF_MNOWAIT "Link to this definition")

os.SF\_SYNC[¶](https://docs.python.org/3/library/os.html#os.SF_SYNC "Link to this definition")

Parameters to the [`sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile")
 function, if the implementation supports them.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.3.

os.SF\_NOCACHE[¶](https://docs.python.org/3/library/os.html#os.SF_NOCACHE "Link to this definition")

Parameter to the [`sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile")
 function, if the implementation supports it. The data won’t be cached in the virtual memory and will be freed afterwards.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.11.

os.set\_blocking(_fd_, _blocking_, _/_)[¶](https://docs.python.org/3/library/os.html#os.set_blocking "Link to this definition")

Set the blocking mode of the specified file descriptor. Set the [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK")
 flag if blocking is `False`, clear the flag otherwise.

See also [`get_blocking()`](https://docs.python.org/3/library/os.html#os.get_blocking "os.get_blocking")
 and [`socket.socket.setblocking()`](https://docs.python.org/3/library/socket.html#socket.socket.setblocking "socket.socket.setblocking")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

On Windows, this function is limited to pipes.

Added in version 3.5.

Changed in version 3.12: Added support for pipes on Windows.

os.splice(_src_, _dst_, _count_, _offset\_src\=None_, _offset\_dst\=None_, _flags\=0_)[¶](https://docs.python.org/3/library/os.html#os.splice "Link to this definition")

Transfer _count_ bytes from file descriptor _src_, starting from offset _offset\_src_, to file descriptor _dst_, starting from offset _offset\_dst_.

The splicing behaviour can be modified by specifying a _flags_ value. Any of the following variables may used, combined using bitwise OR (the `|` operator):

*   If [`SPLICE_F_MOVE`](https://docs.python.org/3/library/os.html#os.SPLICE_F_MOVE "os.SPLICE_F_MOVE")
     is specified, the kernel is asked to move pages instead of copying, but pages may still be copied if the kernel cannot move the pages from the pipe.
    
*   If [`SPLICE_F_NONBLOCK`](https://docs.python.org/3/library/os.html#os.SPLICE_F_NONBLOCK "os.SPLICE_F_NONBLOCK")
     is specified, the kernel is asked to not block on I/O. This makes the splice pipe operations nonblocking, but splice may nevertheless block because the spliced file descriptors may block.
    
*   If [`SPLICE_F_MORE`](https://docs.python.org/3/library/os.html#os.SPLICE_F_MORE "os.SPLICE_F_MORE")
     is specified, it hints to the kernel that more data will be coming in a subsequent splice.
    

At least one of the file descriptors must refer to a pipe. If _offset\_src_ is `None`, then _src_ is read from the current position; respectively for _offset\_dst_. The offset associated to the file descriptor that refers to a pipe must be `None`. The files pointed to by _src_ and _dst_ must reside in the same filesystem, otherwise an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised with [`errno`](https://docs.python.org/3/builtins/exceptions.html#OSError.errno "OSError.errno")
 set to [`errno.EXDEV`](https://docs.python.org/3/library/errno.html#errno.EXDEV "errno.EXDEV")
.

This copy is done without the additional cost of transferring data from the kernel to user space and then back into the kernel. Additionally, some filesystems could implement extra optimizations. The copy is done as if both files are opened as binary.

Upon successful completion, returns the number of bytes spliced to or from the pipe. A return value of 0 means end of input. If _src_ refers to a pipe, then this means that there was no data to transfer, and it would not make sense to block because there are no writers connected to the write end of the pipe.

See also

The _[splice(2)](https://manpages.debian.org/splice(2))
_ man page.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.17 with glibc >= 2.5

Added in version 3.10.

os.SPLICE\_F\_MOVE[¶](https://docs.python.org/3/library/os.html#os.SPLICE_F_MOVE "Link to this definition")

os.SPLICE\_F\_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.SPLICE_F_NONBLOCK "Link to this definition")

os.SPLICE\_F\_MORE[¶](https://docs.python.org/3/library/os.html#os.SPLICE_F_MORE "Link to this definition")

Added in version 3.10.

os.readv(_fd_, _buffers_, _/_)[¶](https://docs.python.org/3/library/os.html#os.readv "Link to this definition")

Read from a file descriptor _fd_ into a number of mutable [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
 _buffers_. Transfer data into each buffer until it is full and then move on to the next buffer in the sequence to hold the rest of the data.

Return the total number of bytes actually read which can be less than the total capacity of all the objects.

The operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf")
 value `'SC_IOV_MAX'`) on the number of buffers that can be used.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

os.tcgetpgrp(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.tcgetpgrp "Link to this definition")

Return the process group associated with the terminal given by _fd_ (an open file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.tcsetpgrp(_fd_, _pg_, _/_)[¶](https://docs.python.org/3/library/os.html#os.tcsetpgrp "Link to this definition")

Set the process group associated with the terminal given by _fd_ (an open file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
) to _pg_.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.ttyname(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.ttyname "Link to this definition")

Return a string which specifies the terminal device associated with file descriptor _fd_. If _fd_ is not associated with a terminal device, an exception is raised.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

os.unlockpt(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.unlockpt "Link to this definition")

Unlock the slave pseudo-terminal device associated with the master pseudo-terminal device to which the file descriptor _fd_ refers. The file descriptor _fd_ is not closed upon failure.

Calls the C standard library function `unlockpt()`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Added in version 3.13.

os.write(_fd_, _str_, _/_)[¶](https://docs.python.org/3/library/os.html#os.write "Link to this definition")

Write the bytestring in _str_ to file descriptor _fd_.

Return the number of bytes actually written.

Note

This function is intended for low-level I/O and must be applied to a file descriptor as returned by [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 or [`pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe")
. To write a “file object” returned by the built-in function [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 or by [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")
 or [`fdopen()`](https://docs.python.org/3/library/os.html#os.fdopen "os.fdopen")
, or [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 or [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
, use its [`write()`](https://docs.python.org/3/library/io.html#io.TextIOBase.write "io.TextIOBase.write")
 method.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

os.writev(_fd_, _buffers_, _/_)[¶](https://docs.python.org/3/library/os.html#os.writev "Link to this definition")

Write the contents of _buffers_ to file descriptor _fd_. _buffers_ must be a sequence of [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
. Buffers are processed in array order. Entire contents of the first buffer is written before proceeding to the second, and so on.

Returns the total number of bytes actually written.

The operating system may set a limit ([`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf")
 value `'SC_IOV_MAX'`) on the number of buffers that can be used.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

### Querying the size of a terminal[¶](https://docs.python.org/3/library/os.html#querying-the-size-of-a-terminal "Link to this heading")

Added in version 3.3.

os.get\_terminal\_size(_fd\=STDOUT\_FILENO_, _/_)[¶](https://docs.python.org/3/library/os.html#os.get_terminal_size "Link to this definition")

Return the size of the terminal window as `(columns, lines)`, tuple of type [`terminal_size`](https://docs.python.org/3/library/os.html#os.terminal_size "os.terminal_size")
.

The optional argument `fd` (default `STDOUT_FILENO`, or standard output) specifies which file descriptor should be queried.

If the file descriptor is not connected to a terminal, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised.

[`shutil.get_terminal_size()`](https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size "shutil.get_terminal_size")
 is the high-level function which should normally be used, `os.get_terminal_size` is the low-level implementation.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

class os.terminal\_size[¶](https://docs.python.org/3/library/os.html#os.terminal_size "Link to this definition")

A subclass of tuple, holding `(columns, lines)` of the terminal window size.

columns[¶](https://docs.python.org/3/library/os.html#os.terminal_size.columns "Link to this definition")

Width of the terminal window in characters.

lines[¶](https://docs.python.org/3/library/os.html#os.terminal_size.lines "Link to this definition")

Height of the terminal window in characters.

### Inheritance of File Descriptors[¶](https://docs.python.org/3/library/os.html#inheritance-of-file-descriptors "Link to this heading")

Added in version 3.4.

A file descriptor has an “inheritable” flag which indicates if the file descriptor can be inherited by child processes. Since Python 3.4, file descriptors created by Python are non-inheritable by default.

On UNIX, non-inheritable file descriptors are closed in child processes at the execution of a new program, other file descriptors are inherited. Note that non-inheritable file descriptors are still _inherited_ by child processes on [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
.

On Windows, non-inheritable handles and file descriptors are closed in child processes, except for standard streams (file descriptors 0, 1 and 2: stdin, stdout and stderr), which are always inherited. Using [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl")
 functions, all inheritable handles and all inheritable file descriptors are inherited. Using the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
 module, all file descriptors except standard streams are closed, and inheritable handles are only inherited if the _close\_fds_ parameter is `False`.

On WebAssembly platforms, the file descriptor cannot be modified.

os.get\_inheritable(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.get_inheritable "Link to this definition")

Get the “inheritable” flag of the specified file descriptor (a boolean).

os.set\_inheritable(_fd_, _inheritable_, _/_)[¶](https://docs.python.org/3/library/os.html#os.set_inheritable "Link to this definition")

Set the “inheritable” flag of the specified file descriptor.

os.get\_handle\_inheritable(_handle_, _/_)[¶](https://docs.python.org/3/library/os.html#os.get_handle_inheritable "Link to this definition")

Get the “inheritable” flag of the specified handle (a boolean).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

os.set\_handle\_inheritable(_handle_, _inheritable_, _/_)[¶](https://docs.python.org/3/library/os.html#os.set_handle_inheritable "Link to this definition")

Set the “inheritable” flag of the specified handle.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Files and Directories[¶](https://docs.python.org/3/library/os.html#files-and-directories "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

On some Unix platforms, many of these functions support one or more of these features:

*   **specifying a file descriptor:** Normally the _path_ argument provided to functions in the `os` module must be a string specifying a file path. However, some functions now alternatively accept an open file descriptor for their _path_ argument. The function will then operate on the file referred to by the descriptor. For POSIX systems, Python will call the variant of the function prefixed with `f` (e.g. call `fchdir` instead of `chdir`).
    
    You can check whether or not _path_ can be specified as a file descriptor for a particular function on your platform using [`os.supports_fd`](https://docs.python.org/3/library/os.html#os.supports_fd "os.supports_fd")
    . If this functionality is unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
    .
    
    If the function also supports _dir\_fd_ or _follow\_symlinks_ arguments, it’s an error to specify one of those when supplying _path_ as a file descriptor.
    

*   **paths relative to directory descriptors:** If _dir\_fd_ is not `None`, it should be a file descriptor referring to a directory, and the path to operate on should be relative; path will then be relative to that directory. If the path is absolute, _dir\_fd_ is ignored. For POSIX systems, Python will call the variant of the function with an `at` suffix and possibly prefixed with `f` (e.g. call `faccessat` instead of `access`).
    
    You can check whether or not _dir\_fd_ is supported for a particular function on your platform using [`os.supports_dir_fd`](https://docs.python.org/3/library/os.html#os.supports_dir_fd "os.supports_dir_fd")
    . If it’s unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
    .
    

*   **not following symlinks:** If _follow\_symlinks_ is `False`, and the last element of the path to operate on is a symbolic link, the function will operate on the symbolic link itself rather than the file pointed to by the link. For POSIX systems, Python will call the `l...` variant of the function.
    
    You can check whether or not _follow\_symlinks_ is supported for a particular function on your platform using [`os.supports_follow_symlinks`](https://docs.python.org/3/library/os.html#os.supports_follow_symlinks "os.supports_follow_symlinks")
    . If it’s unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
    .
    

os.access(_path_, _mode_, _\*_, _dir\_fd\=None_, _effective\_ids\=False_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.access "Link to this definition")

Use the real uid/gid to test for access to _path_. Note that most operations will use the effective uid/gid, therefore this routine can be used in a suid/sgid environment to test if the invoking user has the specified access to _path_. _mode_ should be [`F_OK`](https://docs.python.org/3/library/os.html#os.F_OK "os.F_OK")
 to test the existence of _path_, or it can be the inclusive OR of one or more of [`R_OK`](https://docs.python.org/3/library/os.html#os.R_OK "os.R_OK")
, [`W_OK`](https://docs.python.org/3/library/os.html#os.W_OK "os.W_OK")
, and [`X_OK`](https://docs.python.org/3/library/os.html#os.X_OK "os.X_OK")
 to test permissions. Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 if access is allowed, [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
 if not. See the Unix man page _[access(2)](https://manpages.debian.org/access(2))
_ for more information.

This function can support specifying [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
 and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

If _effective\_ids_ is `True`, `access()` will perform its access checks using the effective uid/gid instead of the real uid/gid. _effective\_ids_ may not be supported on your platform; you can check whether or not it is available using [`os.supports_effective_ids`](https://docs.python.org/3/library/os.html#os.supports_effective_ids "os.supports_effective_ids")
. If it is unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
.

Note

Using `access()` to check if a user is authorized to e.g. open a file before actually doing so using [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 creates a security hole, because the user might exploit the short time interval between checking and opening the file to manipulate it. It’s preferable to use [EAFP](https://docs.python.org/3/glossary.html#term-EAFP)
 techniques. For example:

Copy

if os.access("myfile", os.R\_OK):
    with open("myfile") as fp:
        return fp.read()
return "some default data"

is better written as:

Copy

try:
    fp \= open("myfile")
except PermissionError:
    return "some default data"
else:
    with fp:
        return fp.read()

Note

I/O operations may fail even when `access()` indicates that they would succeed, particularly for operations on network filesystems which may have permissions semantics beyond the usual POSIX permission-bit model.

Changed in version 3.3: Added the _dir\_fd_, _effective\_ids_, and _follow\_symlinks_ parameters.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.F\_OK[¶](https://docs.python.org/3/library/os.html#os.F_OK "Link to this definition")

os.R\_OK[¶](https://docs.python.org/3/library/os.html#os.R_OK "Link to this definition")

os.W\_OK[¶](https://docs.python.org/3/library/os.html#os.W_OK "Link to this definition")

os.X\_OK[¶](https://docs.python.org/3/library/os.html#os.X_OK "Link to this definition")

Values to pass as the _mode_ parameter of [`access()`](https://docs.python.org/3/library/os.html#os.access "os.access")
 to test the existence, readability, writability and executability of _path_, respectively.

os.chdir(_path_)[¶](https://docs.python.org/3/library/os.html#os.chdir "Link to this definition")

Change the current working directory to _path_.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
. The descriptor must refer to an opened directory, not an open file.

This function can raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 and subclasses such as [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
, [`PermissionError`](https://docs.python.org/3/builtins/exceptions.html#PermissionError "PermissionError")
, and [`NotADirectoryError`](https://docs.python.org/3/builtins/exceptions.html#NotADirectoryError "NotADirectoryError")
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.chdir` with argument `path`.

See also

The [`contextlib.chdir()`](https://docs.python.org/3/library/contextlib.html#contextlib.chdir "contextlib.chdir")
 context manager, which changes the current working directory on entering and restores the previous one on exit.

Changed in version 3.3: Added support for specifying _path_ as a file descriptor on some platforms.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.chflags(_path_, _flags_, _\*_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.chflags "Link to this definition")

Set the flags of _path_ to the numeric _flags_. _flags_ may take a combination (bitwise OR) of the following values (as defined in the [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().")
 module):

*   [`stat.UF_NODUMP`](https://docs.python.org/3/library/stat.html#stat.UF_NODUMP "stat.UF_NODUMP")
    
*   [`stat.UF_IMMUTABLE`](https://docs.python.org/3/library/stat.html#stat.UF_IMMUTABLE "stat.UF_IMMUTABLE")
    
*   [`stat.UF_APPEND`](https://docs.python.org/3/library/stat.html#stat.UF_APPEND "stat.UF_APPEND")
    
*   [`stat.UF_OPAQUE`](https://docs.python.org/3/library/stat.html#stat.UF_OPAQUE "stat.UF_OPAQUE")
    
*   [`stat.UF_NOUNLINK`](https://docs.python.org/3/library/stat.html#stat.UF_NOUNLINK "stat.UF_NOUNLINK")
    
*   [`stat.UF_COMPRESSED`](https://docs.python.org/3/library/stat.html#stat.UF_COMPRESSED "stat.UF_COMPRESSED")
    
*   [`stat.UF_HIDDEN`](https://docs.python.org/3/library/stat.html#stat.UF_HIDDEN "stat.UF_HIDDEN")
    
*   [`stat.SF_ARCHIVED`](https://docs.python.org/3/library/stat.html#stat.SF_ARCHIVED "stat.SF_ARCHIVED")
    
*   [`stat.SF_IMMUTABLE`](https://docs.python.org/3/library/stat.html#stat.SF_IMMUTABLE "stat.SF_IMMUTABLE")
    
*   [`stat.SF_APPEND`](https://docs.python.org/3/library/stat.html#stat.SF_APPEND "stat.SF_APPEND")
    
*   [`stat.SF_NOUNLINK`](https://docs.python.org/3/library/stat.html#stat.SF_NOUNLINK "stat.SF_NOUNLINK")
    
*   [`stat.SF_SNAPSHOT`](https://docs.python.org/3/library/stat.html#stat.SF_SNAPSHOT "stat.SF_SNAPSHOT")
    

This function can support [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.chflags` with arguments `path`, `flags`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Changed in version 3.3: Added the _follow\_symlinks_ parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.chmod(_path_, _mode_, _\*_, _dir\_fd\=None_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.chmod "Link to this definition")

Change the mode of _path_ to the numeric _mode_. _mode_ may take one of the following values (as defined in the [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().")
 module) or bitwise ORed combinations of them:

*   [`stat.S_ISUID`](https://docs.python.org/3/library/stat.html#stat.S_ISUID "stat.S_ISUID")
    
*   [`stat.S_ISGID`](https://docs.python.org/3/library/stat.html#stat.S_ISGID "stat.S_ISGID")
    
*   [`stat.S_ENFMT`](https://docs.python.org/3/library/stat.html#stat.S_ENFMT "stat.S_ENFMT")
    
*   [`stat.S_ISVTX`](https://docs.python.org/3/library/stat.html#stat.S_ISVTX "stat.S_ISVTX")
    
*   [`stat.S_IREAD`](https://docs.python.org/3/library/stat.html#stat.S_IREAD "stat.S_IREAD")
    
*   [`stat.S_IWRITE`](https://docs.python.org/3/library/stat.html#stat.S_IWRITE "stat.S_IWRITE")
    
*   [`stat.S_IEXEC`](https://docs.python.org/3/library/stat.html#stat.S_IEXEC "stat.S_IEXEC")
    
*   [`stat.S_IRWXU`](https://docs.python.org/3/library/stat.html#stat.S_IRWXU "stat.S_IRWXU")
    
*   [`stat.S_IRUSR`](https://docs.python.org/3/library/stat.html#stat.S_IRUSR "stat.S_IRUSR")
    
*   [`stat.S_IWUSR`](https://docs.python.org/3/library/stat.html#stat.S_IWUSR "stat.S_IWUSR")
    
*   [`stat.S_IXUSR`](https://docs.python.org/3/library/stat.html#stat.S_IXUSR "stat.S_IXUSR")
    
*   [`stat.S_IRWXG`](https://docs.python.org/3/library/stat.html#stat.S_IRWXG "stat.S_IRWXG")
    
*   [`stat.S_IRGRP`](https://docs.python.org/3/library/stat.html#stat.S_IRGRP "stat.S_IRGRP")
    
*   [`stat.S_IWGRP`](https://docs.python.org/3/library/stat.html#stat.S_IWGRP "stat.S_IWGRP")
    
*   [`stat.S_IXGRP`](https://docs.python.org/3/library/stat.html#stat.S_IXGRP "stat.S_IXGRP")
    
*   [`stat.S_IRWXO`](https://docs.python.org/3/library/stat.html#stat.S_IRWXO "stat.S_IRWXO")
    
*   [`stat.S_IROTH`](https://docs.python.org/3/library/stat.html#stat.S_IROTH "stat.S_IROTH")
    
*   [`stat.S_IWOTH`](https://docs.python.org/3/library/stat.html#stat.S_IWOTH "stat.S_IWOTH")
    
*   [`stat.S_IXOTH`](https://docs.python.org/3/library/stat.html#stat.S_IXOTH "stat.S_IXOTH")
    

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
, [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
 and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

Note

Although Windows supports `chmod()`, you can only set the file’s read-only flag with it (via the `stat.S_IWRITE` and `stat.S_IREAD` constants or a corresponding integer value). All other bits are ignored. The default value of _follow\_symlinks_ is `False` on Windows.

The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.chmod` with arguments `path`, `mode`, `dir_fd`.

Changed in version 3.3: Added support for specifying _path_ as an open file descriptor, and the _dir\_fd_ and _follow\_symlinks_ arguments.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.13: Added support for a file descriptor and the _follow\_symlinks_ argument on Windows.

os.chown(_path_, _uid_, _gid_, _\*_, _dir\_fd\=None_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.chown "Link to this definition")

Change the owner and group id of _path_ to the numeric _uid_ and _gid_. To leave one of the ids unchanged, set it to -1.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
, [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
 and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

See [`shutil.chown()`](https://docs.python.org/3/library/shutil.html#shutil.chown "shutil.chown")
 for a higher-level function that accepts names in addition to numeric ids.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.chown` with arguments `path`, `uid`, `gid`, `dir_fd`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

Changed in version 3.3: Added support for specifying _path_ as an open file descriptor, and the _dir\_fd_ and _follow\_symlinks_ arguments.

Changed in version 3.6: Supports a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.chroot(_path_)[¶](https://docs.python.org/3/library/os.html#os.chroot "Link to this definition")

Change the root directory of the current process to _path_.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.fchdir(_fd_)[¶](https://docs.python.org/3/library/os.html#os.fchdir "Link to this definition")

Change the current working directory to the directory represented by the file descriptor _fd_. The descriptor must refer to an opened directory, not an open file. As of Python 3.3, this is equivalent to `os.chdir(fd)`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.chdir` with argument `path`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

os.getcwd()[¶](https://docs.python.org/3/library/os.html#os.getcwd "Link to this definition")

Return a string representing the current working directory.

os.getcwdb()[¶](https://docs.python.org/3/library/os.html#os.getcwdb "Link to this definition")

Return a bytestring representing the current working directory.

Changed in version 3.8: The function now uses the UTF-8 encoding on Windows, rather than the ANSI code page: see [**PEP 529**](https://peps.python.org/pep-0529/)
 for the rationale. The function is no longer deprecated on Windows.

os.lchflags(_path_, _flags_)[¶](https://docs.python.org/3/library/os.html#os.lchflags "Link to this definition")

Set the flags of _path_ to the numeric _flags_, like [`chflags()`](https://docs.python.org/3/library/os.html#os.chflags "os.chflags")
, but do not follow symbolic links. As of Python 3.3, this is equivalent to `os.chflags(path, flags, follow_symlinks=False)`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.chflags` with arguments `path`, `flags`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.lchmod(_path_, _mode_)[¶](https://docs.python.org/3/library/os.html#os.lchmod "Link to this definition")

Change the mode of _path_ to the numeric _mode_. If path is a symlink, this affects the symlink rather than the target. See the docs for [`chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")
 for possible values of _mode_. As of Python 3.3, this is equivalent to `os.chmod(path, mode, follow_symlinks=False)`.

`lchmod()` is not part of POSIX, but Unix implementations may have it if changing the mode of symbolic links is supported.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.chmod` with arguments `path`, `mode`, `dir_fd`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not Linux, FreeBSD >= 1.3, NetBSD >= 1.3, not OpenBSD

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.13: Added support on Windows.

os.lchown(_path_, _uid_, _gid_)[¶](https://docs.python.org/3/library/os.html#os.lchown "Link to this definition")

Change the owner and group id of _path_ to the numeric _uid_ and _gid_. This function will not follow symbolic links. As of Python 3.3, this is equivalent to `os.chown(path, uid, gid, follow_symlinks=False)`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.chown` with arguments `path`, `uid`, `gid`, `dir_fd`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.link(_src_, _dst_, _\*_, _src\_dir\_fd\=None_, _dst\_dir\_fd\=None_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.link "Link to this definition")

Create a hard link pointing to _src_ named _dst_.

This function can support specifying _src\_dir\_fd_ and/or _dst\_dir\_fd_ to supply [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
, and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
. The default value of _follow\_symlinks_ is `False` on Windows.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.link` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

Changed in version 3.2: Added Windows support.

Changed in version 3.3: Added the _src\_dir\_fd_, _dst\_dir\_fd_, and _follow\_symlinks_ parameters.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 for _src_ and _dst_.

os.listdir(_path\='.'_)[¶](https://docs.python.org/3/library/os.html#os.listdir "Link to this definition")

Return a list containing the names of the entries in the directory given by _path_. The list is in arbitrary order, and does not include the special entries `'.'` and `'..'` even if they are present in the directory. If a file is removed from or added to the directory during the call of this function, whether a name for that file be included is unspecified.

_path_ may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
. If _path_ is of type `bytes` (directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface), the filenames returned will also be of type `bytes`; in all other circumstances, they will be of type `str`.

This function can also support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
; the file descriptor must refer to a directory.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.listdir` with argument `path`.

Note

To encode `str` filenames to `bytes`, use [`fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode")
.

See also

The [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
 function returns directory entries along with file attribute information, giving better performance for many common use cases.

Changed in version 3.2: The _path_ parameter became optional.

Changed in version 3.3: Added support for specifying _path_ as an open file descriptor.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.15: `os.listdir(-1)` now fails with `OSError(errno.EBADF)` rather than listing the current directory.

os.listdrives()[¶](https://docs.python.org/3/library/os.html#os.listdrives "Link to this definition")

Return a list containing the names of drives on a Windows system.

A drive name typically looks like `'C:\\'`. Not every drive name will be associated with a volume, and some may be inaccessible for a variety of reasons, including permissions, network connectivity or missing media. This function does not test for access.

May raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 if an error occurs collecting the drive names.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.listdrives` with no arguments.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

Added in version 3.12.

os.listmounts(_volume_)[¶](https://docs.python.org/3/library/os.html#os.listmounts "Link to this definition")

Return a list containing the mount points for a volume on a Windows system.

_volume_ must be represented as a GUID path, like those returned by [`os.listvolumes()`](https://docs.python.org/3/library/os.html#os.listvolumes "os.listvolumes")
. Volumes may be mounted in multiple locations or not at all. In the latter case, the list will be empty. Mount points that are not associated with a volume will not be returned by this function.

The mount points return by this function will be absolute paths, and may be longer than the drive name.

Raises [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 if the volume is not recognized or if an error occurs collecting the paths.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.listmounts` with argument `volume`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

Added in version 3.12.

os.listvolumes()[¶](https://docs.python.org/3/library/os.html#os.listvolumes "Link to this definition")

Return a list containing the volumes in the system.

Volumes are typically represented as a GUID path that looks like `\\?\Volume{xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}\`. Files can usually be accessed through a GUID path, permissions allowing. However, users are generally not familiar with them, and so the recommended use of this function is to retrieve mount points using [`os.listmounts()`](https://docs.python.org/3/library/os.html#os.listmounts "os.listmounts")
.

May raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 if an error occurs collecting the volumes.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.listvolumes` with no arguments.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

Added in version 3.12.

os.lstat(_path_, _\*_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.lstat "Link to this definition")

Perform the equivalent of an `lstat()` system call on the given path. Similar to [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
, but does not follow symbolic links. Return a [`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result")
 object.

On platforms that do not support symbolic links, this is an alias for [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
.

As of Python 3.3, this is equivalent to `os.stat(path, dir_fd=dir_fd, follow_symlinks=False)`.

This function can also support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
.

See also

The [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 function.

Changed in version 3.2: Added support for Windows 6.0 (Vista) symbolic links.

Changed in version 3.3: Added the _dir\_fd_ parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.8: On Windows, now opens reparse points that represent another path (name surrogates), including symbolic links and directory junctions. Other kinds of reparse points are resolved by the operating system as for [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
.

os.mkdir(_path_, _mode\=0o777_, _\*_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.mkdir "Link to this definition")

Create a directory named _path_ with numeric mode _mode_.

If the directory already exists, [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")
 is raised. If a parent directory in the path does not exist, [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
 is raised.

On some systems, _mode_ is ignored. Where it is used, the current umask value is first masked out. If bits other than the last 9 (i.e. the last 3 digits of the octal representation of the _mode_) are set, their meaning is platform-dependent. On some platforms, they are ignored and you should call [`chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")
 explicitly to set them.

On Windows, a _mode_ of `0o700` is specifically handled to apply access control to the new directory such that only the current user and administrators have access. Other values of _mode_ are ignored.

This function can also support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
.

It is also possible to create temporary directories; see the [`tempfile`](https://docs.python.org/3/library/tempfile.html#module-tempfile "tempfile: Generate temporary files and directories.")
 module’s [`tempfile.mkdtemp()`](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp "tempfile.mkdtemp")
 function.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.mkdir` with arguments `path`, `mode`, `dir_fd`.

Changed in version 3.3: Added the _dir\_fd_ parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.13: Windows now handles a _mode_ of `0o700`.

os.makedirs(_name_, _mode\=0o777_, _exist\_ok\=False_, _\*_, _parent\_mode\=None_)[¶](https://docs.python.org/3/library/os.html#os.makedirs "Link to this definition")

Recursive directory creation function. Like [`mkdir()`](https://docs.python.org/3/library/os.html#os.mkdir "os.mkdir")
, but makes all intermediate-level directories needed to contain the leaf directory.

The _mode_ parameter is passed to [`mkdir()`](https://docs.python.org/3/library/os.html#os.mkdir "os.mkdir")
 for creating the leaf directory; see [the mkdir() description](https://docs.python.org/3/library/os.html#mkdir-modebits)
 for how it is interpreted. To set the file permission bits of any newly created parent directories you can set the umask before invoking `makedirs()`. The file permission bits of existing parent directories are not changed.

If _exist\_ok_ is `False` (the default), a [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")
 is raised if the target directory already exists.

If _parent\_mode_ is not `None`, it is used as the mode for any newly-created, intermediate-level directories. Like _mode_, it is combined with the process’s umask value; see [the mkdir() description](https://docs.python.org/3/library/os.html#mkdir-modebits)
. Otherwise, intermediate directories are created with the default mode, which is also subject to the umask.

Note

`makedirs()` will become confused if the path elements to create include [`pardir`](https://docs.python.org/3/library/os.html#os.pardir "os.pardir")
 (eg. “..” on UNIX systems).

This function handles UNC paths correctly.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.mkdir` with arguments `path`, `mode`, `dir_fd`.

Changed in version 3.2: Added the _exist\_ok_ parameter.

Changed in version 3.4.1: Before Python 3.4.1, if _exist\_ok_ was `True` and the directory existed, `makedirs()` would still raise an error if _mode_ did not match the mode of the existing directory. Since this behavior was impossible to implement safely, it was removed in Python 3.4.1. See [bpo-21082](https://bugs.python.org/issue?@action=redirect&bpo=21082)
.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.7: The _mode_ argument no longer affects the file permission bits of newly created intermediate-level directories.

Added in version 3.15: The _parent\_mode_ parameter. To match the behavior from Python 3.6 and earlier (where _mode_ was applied to all created directories), pass `parent_mode=mode`.

os.mkfifo(_path_, _mode\=0o666_, _\*_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.mkfifo "Link to this definition")

Create a FIFO (a named pipe) named _path_ with numeric mode _mode_. The current umask value is first masked out from the mode.

This function can also support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
.

FIFOs are pipes that can be accessed like regular files. FIFOs exist until they are deleted (for example with [`os.unlink()`](https://docs.python.org/3/library/os.html#os.unlink "os.unlink")
). Generally, FIFOs are used as rendezvous between “client” and “server” type processes: the server opens the FIFO for reading, and the client opens it for writing. Note that `mkfifo()` doesn’t open the FIFO — it just creates the rendezvous point.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Changed in version 3.3: Added the _dir\_fd_ parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.mknod(_path_, _mode\=0o600_, _device\=0_, _\*_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.mknod "Link to this definition")

Create a filesystem node (file, device special file or named pipe) named _path_. _mode_ specifies both the permissions to use and the type of node to be created, being combined (bitwise OR) with one of [`stat.S_IFREG`](https://docs.python.org/3/library/stat.html#stat.S_IFREG "stat.S_IFREG")
, [`stat.S_IFCHR`](https://docs.python.org/3/library/stat.html#stat.S_IFCHR "stat.S_IFCHR")
, [`stat.S_IFBLK`](https://docs.python.org/3/library/stat.html#stat.S_IFBLK "stat.S_IFBLK")
, and [`stat.S_IFIFO`](https://docs.python.org/3/library/stat.html#stat.S_IFIFO "stat.S_IFIFO")
. For `stat.S_IFCHR` and `stat.S_IFBLK`, _device_ defines the newly created device special file (probably using [`os.makedev()`](https://docs.python.org/3/library/os.html#os.makedev "os.makedev")
), otherwise it is ignored.

This function can also support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Changed in version 3.3: Added the _dir\_fd_ parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.major(_device_, _/_)[¶](https://docs.python.org/3/library/os.html#os.major "Link to this definition")

Extract the device major number from a raw device number (usually the [`st_dev`](https://docs.python.org/3/library/os.html#os.stat_result.st_dev "os.stat_result.st_dev")
 or [`st_rdev`](https://docs.python.org/3/library/os.html#os.stat_result.st_rdev "os.stat_result.st_rdev")
 field from `stat`).

os.minor(_device_, _/_)[¶](https://docs.python.org/3/library/os.html#os.minor "Link to this definition")

Extract the device minor number from a raw device number (usually the [`st_dev`](https://docs.python.org/3/library/os.html#os.stat_result.st_dev "os.stat_result.st_dev")
 or [`st_rdev`](https://docs.python.org/3/library/os.html#os.stat_result.st_rdev "os.stat_result.st_rdev")
 field from `stat`).

os.makedev(_major_, _minor_, _/_)[¶](https://docs.python.org/3/library/os.html#os.makedev "Link to this definition")

Compose a raw device number from the major and minor device numbers.

os.NODEV[¶](https://docs.python.org/3/library/os.html#os.NODEV "Link to this definition")

Non-existent device.

Added in version 3.15.

os.pathconf(_path_, _name_)[¶](https://docs.python.org/3/library/os.html#os.pathconf "Link to this definition")

Return system configuration information relevant to a named file. _name_ specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (POSIX.1, Unix 95, Unix 98, and others). Some platforms define additional names as well. The names known to the host operating system are given in the `pathconf_names` dictionary. For configuration variables not included in that mapping, passing an integer for _name_ is also accepted.

If _name_ is a string and is not known, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. If a specific value for _name_ is not supported by the host system, even if it is included in `pathconf_names`, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised with [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL")
 for the error number.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.pathconf\_names[¶](https://docs.python.org/3/library/os.html#os.pathconf_names "Link to this definition")

Dictionary mapping names accepted by [`pathconf()`](https://docs.python.org/3/library/os.html#os.pathconf "os.pathconf")
 and [`fpathconf()`](https://docs.python.org/3/library/os.html#os.fpathconf "os.fpathconf")
 to the integer values defined for those names by the host operating system. This can be used to determine the set of names known to the system.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

os.readlink(_path_, _\*_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.readlink "Link to this definition")

Return a string representing the path to which the symbolic link points. The result may be either an absolute or relative pathname; if it is relative, it may be converted to an absolute pathname using `os.path.join(os.path.dirname(path), result)`.

If the _path_ is a string object (directly or indirectly through a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface), the result will also be a string object, and the call may raise a UnicodeDecodeError. If the _path_ is a bytes object (direct or indirectly), the result will be a bytes object.

This function can also support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
.

When trying to resolve a path that may contain links, use [`realpath()`](https://docs.python.org/3/library/os.path.html#os.path.realpath "os.path.realpath")
 to properly handle recursion and platform differences.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

Changed in version 3.2: Added support for Windows 6.0 (Vista) symbolic links.

Changed in version 3.3: Added the _dir\_fd_ parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 on Unix.

Changed in version 3.8: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 and a bytes object on Windows.

Added support for directory junctions, and changed to return the substitution path (which typically includes `\\?\` prefix) rather than the optional “print name” field that was previously returned.

os.remove(_path_, _\*_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.remove "Link to this definition")

Remove (delete) the file _path_. If _path_ is a directory, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised. Use [`rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir")
 to remove directories. If the file does not exist, a [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
 is raised.

This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
.

On Windows, attempting to remove a file that is in use causes an exception to be raised; on Unix, the directory entry is removed but the storage allocated to the file is not made available until the original file is no longer in use.

This function is semantically identical to [`unlink()`](https://docs.python.org/3/library/os.html#os.unlink "os.unlink")
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.remove` with arguments `path`, `dir_fd`.

Changed in version 3.3: Added the _dir\_fd_ parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.removedirs(_name_)[¶](https://docs.python.org/3/library/os.html#os.removedirs "Link to this definition")

Remove directories recursively. Works like [`rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir")
 except that, if the leaf directory is successfully removed, `removedirs()` tries to successively remove every parent directory mentioned in _path_ until an error is raised (which is ignored, because it generally means that a parent directory is not empty). For example, `os.removedirs('foo/bar/baz')` will first remove the directory `'foo/bar/baz'`, and then remove `'foo/bar'` and `'foo'` if they are empty. Raises [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 if the leaf directory could not be successfully removed.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.remove` with arguments `path`, `dir_fd`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.rename(_src_, _dst_, _\*_, _src\_dir\_fd\=None_, _dst\_dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.rename "Link to this definition")

Rename the file or directory _src_ to _dst_. If _dst_ exists, the operation will fail with an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 subclass in a number of cases:

On Windows, if _dst_ exists a [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")
 is always raised. The operation may fail if _src_ and _dst_ are on different filesystems. Use [`shutil.move()`](https://docs.python.org/3/library/shutil.html#shutil.move "shutil.move")
 to support moves to a different filesystem.

On Unix, if _src_ is a file and _dst_ is a directory or vice-versa, an [`IsADirectoryError`](https://docs.python.org/3/builtins/exceptions.html#IsADirectoryError "IsADirectoryError")
 or a [`NotADirectoryError`](https://docs.python.org/3/builtins/exceptions.html#NotADirectoryError "NotADirectoryError")
 will be raised respectively. If both are directories and _dst_ is empty, _dst_ will be silently replaced. If _dst_ is a non-empty directory, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised. If both are files, _dst_ will be replaced silently if the user has permission. The operation may fail on some Unix flavors if _src_ and _dst_ are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement).

This function can support specifying _src\_dir\_fd_ and/or _dst\_dir\_fd_ to supply [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
.

If you want cross-platform overwriting of the destination, use [`replace()`](https://docs.python.org/3/library/os.html#os.replace "os.replace")
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.rename` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

Changed in version 3.3: Added the _src\_dir\_fd_ and _dst\_dir\_fd_ parameters.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 for _src_ and _dst_.

os.renames(_old_, _new_)[¶](https://docs.python.org/3/library/os.html#os.renames "Link to this definition")

Recursive directory or file renaming function. Works like [`rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename")
, except creation of any intermediate directories needed to make the new pathname good is attempted first. After the rename, directories corresponding to rightmost path segments of the old name will be pruned away using [`removedirs()`](https://docs.python.org/3/library/os.html#os.removedirs "os.removedirs")
.

Note

This function can fail with the new directory structure made if you lack permissions needed to remove the leaf directory or file.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.rename` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 for _old_ and _new_.

os.replace(_src_, _dst_, _\*_, _src\_dir\_fd\=None_, _dst\_dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.replace "Link to this definition")

Rename the file or directory _src_ to _dst_. If _dst_ is a non-empty directory, [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 will be raised. If _dst_ exists and is a file, it will be replaced silently if the user has permission. The operation may fail if _src_ and _dst_ are on different filesystems. If successful, the renaming will be an atomic operation (this is a POSIX requirement).

This function can support specifying _src\_dir\_fd_ and/or _dst\_dir\_fd_ to supply [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.rename` with arguments `src`, `dst`, `src_dir_fd`, `dst_dir_fd`.

Added in version 3.3.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 for _src_ and _dst_.

os.rmdir(_path_, _\*_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.rmdir "Link to this definition")

Remove (delete) the directory _path_. If the directory does not exist or is not empty, a [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
 or an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised respectively. In order to remove whole directory trees, [`shutil.rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree")
 can be used.

This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.rmdir` with arguments `path`, `dir_fd`.

Changed in version 3.3: Added the _dir\_fd_ parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.scandir(_path\='.'_)[¶](https://docs.python.org/3/library/os.html#os.scandir "Link to this definition")

Return an iterator of [`os.DirEntry`](https://docs.python.org/3/library/os.html#os.DirEntry "os.DirEntry")
 objects corresponding to the entries in the directory given by _path_. The entries are yielded in arbitrary order, and the special entries `'.'` and `'..'` are not included. If a file is removed from or added to the directory after creating the iterator, whether an entry for that file be included is unspecified.

Using `scandir()` instead of [`listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir")
 can significantly increase the performance of code that also needs file type or file attribute information, because [`os.DirEntry`](https://docs.python.org/3/library/os.html#os.DirEntry "os.DirEntry")
 objects expose this information if the operating system provides it when scanning a directory. All `os.DirEntry` methods may perform a system call, but [`is_dir()`](https://docs.python.org/3/library/os.html#os.DirEntry.is_dir "os.DirEntry.is_dir")
 and [`is_file()`](https://docs.python.org/3/library/os.html#os.DirEntry.is_file "os.DirEntry.is_file")
 usually only require a system call for symbolic links; [`os.DirEntry.stat()`](https://docs.python.org/3/library/os.html#os.DirEntry.stat "os.DirEntry.stat")
 always requires a system call on Unix but only requires one for symbolic links on Windows.

_path_ may be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
. If _path_ is of type `bytes` (directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface), the type of the [`name`](https://docs.python.org/3/library/os.html#os.DirEntry.name "os.DirEntry.name")
 and [`path`](https://docs.python.org/3/library/os.html#os.DirEntry.path "os.DirEntry.path")
 attributes of each [`os.DirEntry`](https://docs.python.org/3/library/os.html#os.DirEntry "os.DirEntry")
 will be `bytes`; in all other circumstances, they will be of type `str`.

This function can also support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
; the file descriptor must refer to a directory.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.scandir` with argument `path`.

Sharing a `scandir()` iterator between threads will not corrupt the iterator, but it is subject to [race conditions](https://docs.python.org/3/glossary.html#term-race-condition)
: which entries each thread receives is unspecified, and closing the iterator while another thread is iterating ends that iteration early.

The `scandir()` iterator supports the [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
 protocol and has the following method:

scandir.close()[¶](https://docs.python.org/3/library/os.html#os.scandir.close "Link to this definition")

Close the iterator and free acquired resources.

This is called automatically when the iterator is [exhausted](https://docs.python.org/3/glossary.html#term-exhausted)
 or garbage collected, or when an error happens during iterating. However it is advisable to call it explicitly or use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement.

Added in version 3.6.

The following example shows a simple use of `scandir()` to display all the files (excluding directories) in the given _path_ that don’t start with `'.'`. The `entry.is_file()` call will generally not make an additional system call:

Copy

with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is\_file():
            print(entry.name)

Note

On Unix-based systems, `scandir()` uses the system’s [opendir()](https://pubs.opengroup.org/onlinepubs/009695399/functions/opendir.html)
 and [readdir()](https://pubs.opengroup.org/onlinepubs/009695399/functions/readdir_r.html)
 functions. On Windows, it uses the Win32 [FindFirstFileW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364418(v=vs.85).aspx)
 and [FindNextFileW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364428(v=vs.85).aspx)
 functions.

Added in version 3.5.

Changed in version 3.6: Added support for the [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
 protocol and the [`close()`](https://docs.python.org/3/library/os.html#os.scandir.close "os.scandir.close")
 method. If a `scandir()` iterator is neither exhausted nor explicitly closed a [`ResourceWarning`](https://docs.python.org/3/builtins/exceptions.html#ResourceWarning "ResourceWarning")
 will be emitted in its destructor.

The function accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.7: Added support for [file descriptors](https://docs.python.org/3/library/os.html#path-fd)
 on Unix.

Changed in version 3.15: `os.scandir(-1)` now fails with `OSError(errno.EBADF)` rather than listing the current directory.

class os.DirEntry[¶](https://docs.python.org/3/library/os.html#os.DirEntry "Link to this definition")

Object yielded by [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
 to expose the file path and other file attributes of a directory entry.

[`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
 will provide as much of this information as possible without making additional system calls. When a `stat()` or `lstat()` system call is made, the `os.DirEntry` object will cache the result.

`os.DirEntry` instances are not intended to be stored in long-lived data structures; if you know the file metadata has changed or if a long time has elapsed since calling [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
, call `os.stat(entry.path)` to fetch up-to-date information.

Because the `os.DirEntry` methods can make operating system calls, they may also raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
. If you need very fine-grained control over errors, you can catch `OSError` when calling one of the `os.DirEntry` methods and handle as appropriate.

To be directly usable as a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
, `os.DirEntry` implements the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface.

`DirEntry` objects are [generic](https://docs.python.org/3/library/typing.html#generics)
 over the type of the path ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
).

Attributes and methods on a `os.DirEntry` instance are as follows:

name[¶](https://docs.python.org/3/library/os.html#os.DirEntry.name "Link to this definition")

The entry’s base filename, relative to the [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
 _path_ argument.

The [`name`](https://docs.python.org/3/library/os.html#os.name "os.name")
 attribute will be `bytes` if the [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
 _path_ argument is of type `bytes` and `str` otherwise. Use [`fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode")
 to decode byte filenames.

path[¶](https://docs.python.org/3/library/os.html#os.DirEntry.path "Link to this definition")

The entry’s path name: equivalent to `os.path.join(scandir_path, entry.name)` where _scandir\_path_ is the original [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
 _path_ argument. Apart from the filename, the path preserves the original `scandir()` argument. If the `scandir()` _path_ argument was relative, the [`path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
 attribute is also relative. Changing the current working directory after creating the `scandir()` iterator may cause later uses of `path` to resolve differently. On some platforms, the constructed path may not be valid if the original `scandir()` argument was usable for enumeration but not for joining with the entry name. If the `scandir()` _path_ argument was a [file descriptor](https://docs.python.org/3/library/os.html#path-fd)
, the `path` attribute is the same as the [`name`](https://docs.python.org/3/library/os.html#os.name "os.name")
 attribute.

The [`path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
 attribute will be `bytes` if the [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
 _path_ argument is of type `bytes` and `str` otherwise. Use [`fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode")
 to decode byte filenames.

inode()[¶](https://docs.python.org/3/library/os.html#os.DirEntry.inode "Link to this definition")

Return the inode number of the entry.

The result is cached on the `os.DirEntry` object. Use `os.stat(entry.path, follow_symlinks=False).st_ino` to fetch up-to-date information.

On the first, uncached call, a system call is required on Windows but not on Unix.

is\_dir(_\*_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.DirEntry.is_dir "Link to this definition")

Return `True` if this entry is a directory or a symbolic link pointing to a directory; return `False` if the entry is or points to any other kind of file, or if it doesn’t exist anymore.

If _follow\_symlinks_ is `False`, return `True` only if this entry is a directory (without following symlinks); return `False` if the entry is any other kind of file or if it doesn’t exist anymore.

The result is cached on the `os.DirEntry` object, with a separate cache for _follow\_symlinks_ `True` and `False`. Call [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 along with [`stat.S_ISDIR()`](https://docs.python.org/3/library/stat.html#stat.S_ISDIR "stat.S_ISDIR")
 to fetch up-to-date information.

On the first, uncached call, no system call is required in most cases. Specifically, for non-symlinks, neither Windows or Unix require a system call, except on certain Unix file systems, such as network file systems, that return `dirent.d_type == DT_UNKNOWN`. If the entry is a symlink, a system call will be required to follow the symlink unless _follow\_symlinks_ is `False`.

This method can raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
, such as [`PermissionError`](https://docs.python.org/3/builtins/exceptions.html#PermissionError "PermissionError")
, but [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
 is caught and not raised.

is\_file(_\*_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.DirEntry.is_file "Link to this definition")

Return `True` if this entry is a file or a symbolic link pointing to a file; return `False` if the entry is or points to a directory or other non-file entry, or if it doesn’t exist anymore.

If _follow\_symlinks_ is `False`, return `True` only if this entry is a file (without following symlinks); return `False` if the entry is a directory or other non-file entry, or if it doesn’t exist anymore.

The result is cached on the `os.DirEntry` object. Caching, system calls made, and exceptions raised are as per [`is_dir()`](https://docs.python.org/3/library/os.html#os.DirEntry.is_dir "os.DirEntry.is_dir")
.

is\_symlink()[¶](https://docs.python.org/3/library/os.html#os.DirEntry.is_symlink "Link to this definition")

Return `True` if this entry is a symbolic link (even if broken); return `False` if the entry points to a directory or any kind of file, or if it doesn’t exist anymore.

The result is cached on the `os.DirEntry` object. Call [`os.path.islink()`](https://docs.python.org/3/library/os.path.html#os.path.islink "os.path.islink")
 to fetch up-to-date information.

On the first, uncached call, no system call is required in most cases. Specifically, neither Windows or Unix require a system call, except on certain Unix file systems, such as network file systems, that return `dirent.d_type == DT_UNKNOWN`.

This method can raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
, such as [`PermissionError`](https://docs.python.org/3/builtins/exceptions.html#PermissionError "PermissionError")
, but [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
 is caught and not raised.

is\_junction()[¶](https://docs.python.org/3/library/os.html#os.DirEntry.is_junction "Link to this definition")

Return `True` if this entry is a junction (even if broken); return `False` if the entry points to a regular directory, any kind of file, a symlink, or if it doesn’t exist anymore.

The result is cached on the `os.DirEntry` object. Call [`os.path.isjunction()`](https://docs.python.org/3/library/os.path.html#os.path.isjunction "os.path.isjunction")
 to fetch up-to-date information.

Added in version 3.12.

stat(_\*_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.DirEntry.stat "Link to this definition")

Return a [`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result")
 object for this entry. This method follows symbolic links by default; to stat a symbolic link add the `follow_symlinks=False` argument.

On Unix, this method always requires a system call. On Windows, it only requires a system call if _follow\_symlinks_ is `True` and the entry is a reparse point (for example, a symbolic link or directory junction).

On Windows, the `st_ino`, `st_dev` and `st_nlink` attributes of the [`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result")
 are always set to zero. Call [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 to get these attributes.

The result is cached on the `os.DirEntry` object, with a separate cache for _follow\_symlinks_ `True` and `False`. Call [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 to fetch up-to-date information.

Note that there is a nice correspondence between several attributes and methods of `os.DirEntry` and of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
. In particular, the `name` attribute has the same meaning, as do the `is_dir()`, `is_file()`, `is_symlink()`, `is_junction()`, and `stat()` methods.

Added in version 3.5.

Changed in version 3.6: Added support for the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface. Added support for [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 paths on Windows.

Changed in version 3.12: The `st_ctime` attribute of a stat result is deprecated on Windows. The file creation time is properly available as `st_birthtime`, and in the future `st_ctime` may be changed to return zero or the metadata change time, if available.

os.stat(_path_, _\*_, _dir\_fd\=None_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.stat "Link to this definition")

Get the status of a file or a file descriptor. Perform the equivalent of a `stat()` system call on the given path. _path_ may be specified as either a string or bytes – directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface – or as an open file descriptor. Return a [`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result")
 object.

This function normally follows symlinks; to stat a symlink add the argument `follow_symlinks=False`, or use [`lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat")
.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
 and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

On Windows, passing `follow_symlinks=False` will disable following all name-surrogate reparse points, which includes symlinks and directory junctions. Other types of reparse points that do not resemble links or that the operating system is unable to follow will be opened directly. When following a chain of multiple links, this may result in the original link being returned instead of the non-link that prevented full traversal. To obtain stat results for the final path in this case, use the [`os.path.realpath()`](https://docs.python.org/3/library/os.path.html#os.path.realpath "os.path.realpath")
 function to resolve the path name as far as possible and call [`lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat")
 on the result. This does not apply to dangling symlinks or junction points, which will raise the usual exceptions.

Example:

Copy

\>>> import os
\>>> statinfo \= os.stat('somefile.txt')
\>>> statinfo
os.stat\_result(st\_mode=33188, st\_ino=7876932, st\_dev=234881026,
st\_nlink=1, st\_uid=501, st\_gid=501, st\_size=264, st\_atime=1297230295,
st\_mtime=1297230027, st\_ctime=1297230027)
\>>> statinfo.st\_size
264

See also

[`fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat")
 and [`lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat")
 functions.

Changed in version 3.3: Added the _dir\_fd_ and _follow\_symlinks_ parameters, specifying a file descriptor instead of a path.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.8: On Windows, all reparse points that can be resolved by the operating system are now followed, and passing `follow_symlinks=False` disables following all name surrogate reparse points. If the operating system reaches a reparse point that it is not able to follow, _stat_ now returns the information for the original path as if `follow_symlinks=False` had been specified instead of raising an error.

class os.stat\_result[¶](https://docs.python.org/3/library/os.html#os.stat_result "Link to this definition")

Object whose attributes correspond roughly to the members of the `stat` structure. It is used for the result of [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
, [`os.fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat")
 and [`os.lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat")
.

Attributes:

st\_mode[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_mode "Link to this definition")

File mode: file type and file mode bits (permissions).

st\_ino[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_ino "Link to this definition")

Platform dependent, but if non-zero, uniquely identifies the file for a given value of `st_dev`. Typically:

*   the inode number on Unix,
    
*   the [file index](https://msdn.microsoft.com/en-us/library/aa363788)
     on Windows
    

st\_dev[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_dev "Link to this definition")

Identifier of the device on which this file resides.

st\_nlink[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_nlink "Link to this definition")

Number of hard links.

st\_uid[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_uid "Link to this definition")

User identifier of the file owner.

st\_gid[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_gid "Link to this definition")

Group identifier of the file owner.

st\_size[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_size "Link to this definition")

Size of the file in bytes, if it is a regular file or a symbolic link. The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.

Timestamps:

st\_atime[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_atime "Link to this definition")

Time of most recent access expressed in seconds.

st\_mtime[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime "Link to this definition")

Time of most recent content modification expressed in seconds.

st\_ctime[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime "Link to this definition")

Time of most recent metadata change expressed in seconds.

Changed in version 3.12: `st_ctime` is deprecated on Windows. Use `st_birthtime` for the file creation time. In the future, `st_ctime` will contain the time of the most recent metadata change, as for other platforms.

st\_atime\_ns[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_atime_ns "Link to this definition")

Time of most recent access expressed in nanoseconds as an integer.

Added in version 3.3.

st\_mtime\_ns[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime_ns "Link to this definition")

Time of most recent content modification expressed in nanoseconds as an integer.

Added in version 3.3.

st\_ctime\_ns[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime_ns "Link to this definition")

Time of most recent metadata change expressed in nanoseconds as an integer.

Added in version 3.3.

Changed in version 3.12: `st_ctime_ns` is deprecated on Windows. Use `st_birthtime_ns` for the file creation time. In the future, `st_ctime_ns` will contain the time of the most recent metadata change, as for other platforms.

st\_birthtime[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime "Link to this definition")

Time of file creation expressed in seconds. This attribute is not always available, and may raise [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
.

Changed in version 3.12: `st_birthtime` is now available on Windows.

st\_birthtime\_ns[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime_ns "Link to this definition")

Time of file creation expressed in nanoseconds as an integer. This attribute is not always available, and may raise [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
.

Added in version 3.12.

Note

The exact meaning and resolution of the [`st_atime`](https://docs.python.org/3/library/os.html#os.stat_result.st_atime "os.stat_result.st_atime")
, [`st_mtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime "os.stat_result.st_mtime")
, [`st_ctime`](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime "os.stat_result.st_ctime")
 and [`st_birthtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime "os.stat_result.st_birthtime")
 attributes depend on the operating system and the file system. For example, on Windows systems using the FAT32 file systems, `st_mtime` has 2-second resolution, and `st_atime` has only 1-day resolution. See your operating system documentation for details.

Similarly, although [`st_atime_ns`](https://docs.python.org/3/library/os.html#os.stat_result.st_atime_ns "os.stat_result.st_atime_ns")
, [`st_mtime_ns`](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime_ns "os.stat_result.st_mtime_ns")
, [`st_ctime_ns`](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime_ns "os.stat_result.st_ctime_ns")
 and [`st_birthtime_ns`](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime_ns "os.stat_result.st_birthtime_ns")
 are always expressed in nanoseconds, many systems do not provide nanosecond precision. On systems that do provide nanosecond precision, the floating-point object used to store [`st_atime`](https://docs.python.org/3/library/os.html#os.stat_result.st_atime "os.stat_result.st_atime")
, [`st_mtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime "os.stat_result.st_mtime")
, [`st_ctime`](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime "os.stat_result.st_ctime")
 and [`st_birthtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime "os.stat_result.st_birthtime")
 cannot preserve all of it, and as such will be slightly inexact. If you need the exact timestamps you should always use `st_atime_ns`, `st_mtime_ns`, `st_ctime_ns` and `st_birthtime_ns`.

On some Unix systems (such as Linux), the following attributes may also be available:

st\_blocks[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_blocks "Link to this definition")

Number of 512-byte blocks allocated for file. This may be smaller than [`st_size`](https://docs.python.org/3/library/os.html#os.stat_result.st_size "os.stat_result.st_size")
/512 when the file has holes.

st\_blksize[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_blksize "Link to this definition")

“Preferred” blocksize for efficient file system I/O. Writing to a file in smaller chunks may cause an inefficient read-modify-rewrite.

st\_rdev[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_rdev "Link to this definition")

Type of device if an inode device.

st\_flags[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_flags "Link to this definition")

User defined flags for file.

On other Unix systems (such as FreeBSD), the following attributes may be available (but may be only filled out if root tries to use them):

st\_gen[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_gen "Link to this definition")

File generation number.

On Solaris and derivatives, the following attributes may also be available:

st\_fstype[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_fstype "Link to this definition")

String that uniquely identifies the type of the filesystem that contains the file.

On macOS systems, the following attributes may also be available:

st\_rsize[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_rsize "Link to this definition")

Real size of the file.

st\_creator[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_creator "Link to this definition")

Creator of the file.

st\_type[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_type "Link to this definition")

File type.

On Windows systems, the following attributes are also available:

st\_file\_attributes[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_file_attributes "Link to this definition")

Windows file attributes: `dwFileAttributes` member of the `BY_HANDLE_FILE_INFORMATION` structure returned by `GetFileInformationByHandle()`. See the `FILE_ATTRIBUTE_* <stat.FILE_ATTRIBUTE_ARCHIVE>` constants in the [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().")
 module.

Added in version 3.5.

st\_reparse\_tag[¶](https://docs.python.org/3/library/os.html#os.stat_result.st_reparse_tag "Link to this definition")

When [`st_file_attributes`](https://docs.python.org/3/library/os.html#os.stat_result.st_file_attributes "os.stat_result.st_file_attributes")
 has the [`FILE_ATTRIBUTE_REPARSE_POINT`](https://docs.python.org/3/library/stat.html#stat.FILE_ATTRIBUTE_REPARSE_POINT "stat.FILE_ATTRIBUTE_REPARSE_POINT")
 set, this field contains the tag identifying the type of reparse point. See the [`IO_REPARSE_TAG_*`](https://docs.python.org/3/library/stat.html#stat.IO_REPARSE_TAG_SYMLINK "stat.IO_REPARSE_TAG_SYMLINK")
 constants in the [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().")
 module.

The standard module [`stat`](https://docs.python.org/3/library/stat.html#module-stat "stat: Utilities for interpreting the results of os.stat(), os.lstat() and os.fstat().")
 defines functions and constants that are useful for extracting information from a `stat` structure. (On Windows, some items are filled with dummy values.)

For backward compatibility, a `stat_result` instance is also accessible as a tuple of at least 10 integers giving the most important (and portable) members of the `stat` structure, in the order [`st_mode`](https://docs.python.org/3/library/os.html#os.stat_result.st_mode "os.stat_result.st_mode")
, [`st_ino`](https://docs.python.org/3/library/os.html#os.stat_result.st_ino "os.stat_result.st_ino")
, [`st_dev`](https://docs.python.org/3/library/os.html#os.stat_result.st_dev "os.stat_result.st_dev")
, [`st_nlink`](https://docs.python.org/3/library/os.html#os.stat_result.st_nlink "os.stat_result.st_nlink")
, [`st_uid`](https://docs.python.org/3/library/os.html#os.stat_result.st_uid "os.stat_result.st_uid")
, [`st_gid`](https://docs.python.org/3/library/os.html#os.stat_result.st_gid "os.stat_result.st_gid")
, [`st_size`](https://docs.python.org/3/library/os.html#os.stat_result.st_size "os.stat_result.st_size")
, [`st_atime`](https://docs.python.org/3/library/os.html#os.stat_result.st_atime "os.stat_result.st_atime")
, [`st_mtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_mtime "os.stat_result.st_mtime")
, [`st_ctime`](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime "os.stat_result.st_ctime")
. More items may be added at the end by some implementations. For compatibility with older Python versions, accessing `stat_result` as a tuple always returns integers.

Changed in version 3.5: Windows now returns the file index as [`st_ino`](https://docs.python.org/3/library/os.html#os.stat_result.st_ino "os.stat_result.st_ino")
 when available.

Changed in version 3.7: Added the [`st_fstype`](https://docs.python.org/3/library/os.html#os.stat_result.st_fstype "os.stat_result.st_fstype")
 member to Solaris/derivatives.

Changed in version 3.8: Added the [`st_reparse_tag`](https://docs.python.org/3/library/os.html#os.stat_result.st_reparse_tag "os.stat_result.st_reparse_tag")
 member on Windows.

Changed in version 3.8: On Windows, the [`st_mode`](https://docs.python.org/3/library/os.html#os.stat_result.st_mode "os.stat_result.st_mode")
 member now identifies special files as [`S_IFCHR`](https://docs.python.org/3/library/stat.html#stat.S_IFCHR "stat.S_IFCHR")
, [`S_IFIFO`](https://docs.python.org/3/library/stat.html#stat.S_IFIFO "stat.S_IFIFO")
 or [`S_IFBLK`](https://docs.python.org/3/library/stat.html#stat.S_IFBLK "stat.S_IFBLK")
 as appropriate.

Changed in version 3.12: On Windows, [`st_ctime`](https://docs.python.org/3/library/os.html#os.stat_result.st_ctime "os.stat_result.st_ctime")
 is deprecated. Eventually, it will contain the last metadata change time, for consistency with other platforms, but for now still contains creation time. Use [`st_birthtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime "os.stat_result.st_birthtime")
 for the creation time.

On Windows, [`st_ino`](https://docs.python.org/3/library/os.html#os.stat_result.st_ino "os.stat_result.st_ino")
 may now be up to 128 bits, depending on the file system. Previously it would not be above 64 bits, and larger file identifiers would be arbitrarily packed.

On Windows, [`st_rdev`](https://docs.python.org/3/library/os.html#os.stat_result.st_rdev "os.stat_result.st_rdev")
 no longer returns a value. Previously it would contain the same as [`st_dev`](https://docs.python.org/3/library/os.html#os.stat_result.st_dev "os.stat_result.st_dev")
, which was incorrect.

Added the [`st_birthtime`](https://docs.python.org/3/library/os.html#os.stat_result.st_birthtime "os.stat_result.st_birthtime")
 member on Windows.

os.statx(_path_, _mask_, _\*_, _flags\=0_, _dir\_fd\=None_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.statx "Link to this definition")

Get the status of a file or file descriptor by performing a `statx()` system call on the given path.

_path_ is a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 or an open file descriptor. _mask_ is a combination of the module-level [`STATX_*`](https://docs.python.org/3/library/os.html#os.STATX_TYPE "os.STATX_TYPE")
 constants specifying the information to retrieve. _flags_ is a combination of the module-level [`AT_STATX_*`](https://docs.python.org/3/library/os.html#os.AT_STATX_FORCE_SYNC "os.AT_STATX_FORCE_SYNC")
 constants and/or [`AT_NO_AUTOMOUNT`](https://docs.python.org/3/library/os.html#os.AT_NO_AUTOMOUNT "os.AT_NO_AUTOMOUNT")
. Returns a [`statx_result`](https://docs.python.org/3/library/os.html#os.statx_result "os.statx_result")
 object whose [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
 attribute specifies the information actually retrieved (which may differ from _mask_).

This function supports [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
, [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
, and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

See also

The _[statx(2)](https://manpages.debian.org/statx(2))
_ man page.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28.

Added in version 3.15.

class os.statx\_result[¶](https://docs.python.org/3/library/os.html#os.statx_result "Link to this definition")

Information about a file returned by [`os.statx()`](https://docs.python.org/3/library/os.html#os.statx "os.statx")
.

`statx_result` has the following attributes:

stx\_atime[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_atime "Link to this definition")

Time of most recent access expressed in seconds.

Equal to `None` if [`STATX_ATIME`](https://docs.python.org/3/library/os.html#os.STATX_ATIME "os.STATX_ATIME")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_atime\_ns[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_atime_ns "Link to this definition")

Time of most recent access expressed in nanoseconds as an integer.

Equal to `None` if [`STATX_ATIME`](https://docs.python.org/3/library/os.html#os.STATX_ATIME "os.STATX_ATIME")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_atomic\_write\_segments\_max[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_atomic_write_segments_max "Link to this definition")

Maximum iovecs for direct I/O with torn-write protection.

Equal to `None` if [`STATX_WRITE_ATOMIC`](https://docs.python.org/3/library/os.html#os.STATX_WRITE_ATOMIC "os.STATX_WRITE_ATOMIC")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28 and build-time kernel userspace API headers >= 6.11.

stx\_atomic\_write\_unit\_max[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_atomic_write_unit_max "Link to this definition")

Maximum size for direct I/O with torn-write protection.

Equal to `None` if [`STATX_WRITE_ATOMIC`](https://docs.python.org/3/library/os.html#os.STATX_WRITE_ATOMIC "os.STATX_WRITE_ATOMIC")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28 and build-time kernel userspace API headers >= 6.11.

stx\_atomic\_write\_unit\_max\_opt[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_atomic_write_unit_max_opt "Link to this definition")

Maximum optimized size for direct I/O with torn-write protection.

Equal to `None` if [`STATX_WRITE_ATOMIC`](https://docs.python.org/3/library/os.html#os.STATX_WRITE_ATOMIC "os.STATX_WRITE_ATOMIC")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28 and build-time kernel userspace API headers >= 6.16.

stx\_atomic\_write\_unit\_min[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_atomic_write_unit_min "Link to this definition")

Minimum size for direct I/O with torn-write protection.

Equal to `None` if [`STATX_WRITE_ATOMIC`](https://docs.python.org/3/library/os.html#os.STATX_WRITE_ATOMIC "os.STATX_WRITE_ATOMIC")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28 and build-time kernel userspace API headers >= 6.11.

stx\_attributes[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_attributes "Link to this definition")

Bitmask of [`STATX_ATTR_*`](https://docs.python.org/3/library/stat.html#stat.STATX_ATTR_COMPRESSED "stat.STATX_ATTR_COMPRESSED")
 constants specifying the attributes of this file.

stx\_attributes\_mask[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_attributes_mask "Link to this definition")

A mask indicating which bits in [`stx_attributes`](https://docs.python.org/3/library/os.html#os.statx_result.stx_attributes "os.statx_result.stx_attributes")
 are supported by the VFS and the filesystem.

stx\_blksize[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_blksize "Link to this definition")

“Preferred” blocksize for efficient file system I/O. Writing to a file in smaller chunks may cause an inefficient read-modify-rewrite.

stx\_blocks[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_blocks "Link to this definition")

Number of 512-byte blocks allocated for file. This may be smaller than [`stx_size`](https://docs.python.org/3/library/os.html#os.statx_result.stx_size "os.statx_result.stx_size")
/512 when the file has holes.

Equal to `None` if [`STATX_BLOCKS`](https://docs.python.org/3/library/os.html#os.STATX_BLOCKS "os.STATX_BLOCKS")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_btime[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_btime "Link to this definition")

Time of file creation expressed in seconds.

Equal to `None` if [`STATX_BTIME`](https://docs.python.org/3/library/os.html#os.STATX_BTIME "os.STATX_BTIME")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_btime\_ns[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_btime_ns "Link to this definition")

Time of file creation expressed in nanoseconds as an integer.

Equal to `None` if [`STATX_BTIME`](https://docs.python.org/3/library/os.html#os.STATX_BTIME "os.STATX_BTIME")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_ctime[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_ctime "Link to this definition")

Time of most recent metadata change expressed in seconds.

Equal to `None` if [`STATX_CTIME`](https://docs.python.org/3/library/os.html#os.STATX_CTIME "os.STATX_CTIME")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_ctime\_ns[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_ctime_ns "Link to this definition")

Time of most recent metadata change expressed in nanoseconds as an integer.

Equal to `None` if [`STATX_CTIME`](https://docs.python.org/3/library/os.html#os.STATX_CTIME "os.STATX_CTIME")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_dev[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_dev "Link to this definition")

Identifier of the device on which this file resides.

stx\_dev\_major[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_dev_major "Link to this definition")

Major number of the device on which this file resides.

stx\_dev\_minor[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_dev_minor "Link to this definition")

Minor number of the device on which this file resides.

stx\_dio\_mem\_align[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_dio_mem_align "Link to this definition")

Direct I/O memory buffer alignment requirement.

Equal to `None` if [`STATX_DIOALIGN`](https://docs.python.org/3/library/os.html#os.STATX_DIOALIGN "os.STATX_DIOALIGN")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28 and build-time kernel userspace API headers >= 6.1.

stx\_dio\_offset\_align[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_dio_offset_align "Link to this definition")

Direct I/O file offset alignment requirement.

Equal to `None` if [`STATX_DIOALIGN`](https://docs.python.org/3/library/os.html#os.STATX_DIOALIGN "os.STATX_DIOALIGN")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28 and build-time kernel userspace API headers >= 6.1.

stx\_dio\_read\_offset\_align[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_dio_read_offset_align "Link to this definition")

Direct I/O file offset alignment requirement for reads.

Equal to `None` if [`STATX_DIO_READ_ALIGN`](https://docs.python.org/3/library/os.html#os.STATX_DIO_READ_ALIGN "os.STATX_DIO_READ_ALIGN")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28 and build-time kernel userspace API headers >= 6.14.

stx\_gid[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_gid "Link to this definition")

Group identifier of the file owner.

Equal to `None` if [`STATX_GID`](https://docs.python.org/3/library/os.html#os.STATX_GID "os.STATX_GID")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_ino[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_ino "Link to this definition")

Inode number.

Equal to `None` if [`STATX_INO`](https://docs.python.org/3/library/os.html#os.STATX_INO "os.STATX_INO")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_mask[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "Link to this definition")

Bitmask of [`STATX_*`](https://docs.python.org/3/library/os.html#os.STATX_TYPE "os.STATX_TYPE")
 constants specifying the information retrieved, which may differ from what was requested.

stx\_mnt\_id[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_mnt_id "Link to this definition")

Mount identifier.

Equal to `None` if [`STATX_MNT_ID`](https://docs.python.org/3/library/os.html#os.STATX_MNT_ID "os.STATX_MNT_ID")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28 and build-time kernel userspace API headers >= 5.8.

stx\_mode[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_mode "Link to this definition")

File mode: file type and file mode bits (permissions).

Equal to `None` if [`STATX_TYPE | STATX_MODE`](https://docs.python.org/3/library/os.html#os.STATX_TYPE "os.STATX_TYPE")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_mtime[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_mtime "Link to this definition")

Time of most recent content modification expressed in seconds.

Equal to `None` if [`STATX_MTIME`](https://docs.python.org/3/library/os.html#os.STATX_MTIME "os.STATX_MTIME")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_mtime\_ns[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_mtime_ns "Link to this definition")

Time of most recent content modification expressed in nanoseconds as an integer.

Equal to `None` if [`STATX_MTIME`](https://docs.python.org/3/library/os.html#os.STATX_MTIME "os.STATX_MTIME")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_nlink[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_nlink "Link to this definition")

Number of hard links.

Equal to `None` if [`STATX_NLINK`](https://docs.python.org/3/library/os.html#os.STATX_NLINK "os.STATX_NLINK")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_rdev[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_rdev "Link to this definition")

Type of device if an inode device.

stx\_rdev\_major[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_rdev_major "Link to this definition")

Major number of the device this file represents.

stx\_rdev\_minor[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_rdev_minor "Link to this definition")

Minor number of the device this file represents.

stx\_size[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_size "Link to this definition")

Size of the file in bytes, if it is a regular file or a symbolic link. The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.

Equal to `None` if [`STATX_SIZE`](https://docs.python.org/3/library/os.html#os.STATX_SIZE "os.STATX_SIZE")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

stx\_subvol[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_subvol "Link to this definition")

Subvolume identifier.

Equal to `None` if [`STATX_SUBVOL`](https://docs.python.org/3/library/os.html#os.STATX_SUBVOL "os.STATX_SUBVOL")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28 and build-time kernel userspace API headers >= 6.10.

stx\_uid[¶](https://docs.python.org/3/library/os.html#os.statx_result.stx_uid "Link to this definition")

User identifier of the file owner.

Equal to `None` if [`STATX_UID`](https://docs.python.org/3/library/os.html#os.STATX_UID "os.STATX_UID")
 is missing from [`stx_mask`](https://docs.python.org/3/library/os.html#os.statx_result.stx_mask "os.statx_result.stx_mask")
.

See also

The _[statx(2)](https://manpages.debian.org/statx(2))
_ man page.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28.

Added in version 3.15.

os.STATX\_TYPE[¶](https://docs.python.org/3/library/os.html#os.STATX_TYPE "Link to this definition")

os.STATX\_MODE[¶](https://docs.python.org/3/library/os.html#os.STATX_MODE "Link to this definition")

os.STATX\_NLINK[¶](https://docs.python.org/3/library/os.html#os.STATX_NLINK "Link to this definition")

os.STATX\_UID[¶](https://docs.python.org/3/library/os.html#os.STATX_UID "Link to this definition")

os.STATX\_GID[¶](https://docs.python.org/3/library/os.html#os.STATX_GID "Link to this definition")

os.STATX\_ATIME[¶](https://docs.python.org/3/library/os.html#os.STATX_ATIME "Link to this definition")

os.STATX\_MTIME[¶](https://docs.python.org/3/library/os.html#os.STATX_MTIME "Link to this definition")

os.STATX\_CTIME[¶](https://docs.python.org/3/library/os.html#os.STATX_CTIME "Link to this definition")

os.STATX\_INO[¶](https://docs.python.org/3/library/os.html#os.STATX_INO "Link to this definition")

os.STATX\_SIZE[¶](https://docs.python.org/3/library/os.html#os.STATX_SIZE "Link to this definition")

os.STATX\_BLOCKS[¶](https://docs.python.org/3/library/os.html#os.STATX_BLOCKS "Link to this definition")

os.STATX\_BASIC\_STATS[¶](https://docs.python.org/3/library/os.html#os.STATX_BASIC_STATS "Link to this definition")

os.STATX\_BTIME[¶](https://docs.python.org/3/library/os.html#os.STATX_BTIME "Link to this definition")

os.STATX\_MNT\_ID[¶](https://docs.python.org/3/library/os.html#os.STATX_MNT_ID "Link to this definition")

os.STATX\_DIOALIGN[¶](https://docs.python.org/3/library/os.html#os.STATX_DIOALIGN "Link to this definition")

os.STATX\_MNT\_ID\_UNIQUE[¶](https://docs.python.org/3/library/os.html#os.STATX_MNT_ID_UNIQUE "Link to this definition")

os.STATX\_SUBVOL[¶](https://docs.python.org/3/library/os.html#os.STATX_SUBVOL "Link to this definition")

os.STATX\_WRITE\_ATOMIC[¶](https://docs.python.org/3/library/os.html#os.STATX_WRITE_ATOMIC "Link to this definition")

os.STATX\_DIO\_READ\_ALIGN[¶](https://docs.python.org/3/library/os.html#os.STATX_DIO_READ_ALIGN "Link to this definition")

Bitflags for use in the _mask_ parameter to [`os.statx()`](https://docs.python.org/3/library/os.html#os.statx "os.statx")
. Some of these flags may be available even when their corresponding members in [`statx_result`](https://docs.python.org/3/library/os.html#os.statx_result "os.statx_result")
 are not available.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28.

Added in version 3.15.

os.AT\_STATX\_FORCE\_SYNC[¶](https://docs.python.org/3/library/os.html#os.AT_STATX_FORCE_SYNC "Link to this definition")

A flag for the [`os.statx()`](https://docs.python.org/3/library/os.html#os.statx "os.statx")
 function. Requests that the kernel return up-to-date information even when doing so is expensive (for example, requiring a round trip to the server for a file on a network filesystem).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28.

Added in version 3.15.

os.AT\_STATX\_DONT\_SYNC[¶](https://docs.python.org/3/library/os.html#os.AT_STATX_DONT_SYNC "Link to this definition")

A flag for the [`os.statx()`](https://docs.python.org/3/library/os.html#os.statx "os.statx")
 function. Requests that the kernel return cached information if possible.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28.

Added in version 3.15.

os.AT\_STATX\_SYNC\_AS\_STAT[¶](https://docs.python.org/3/library/os.html#os.AT_STATX_SYNC_AS_STAT "Link to this definition")

A flag for the [`os.statx()`](https://docs.python.org/3/library/os.html#os.statx "os.statx")
 function. This flag is defined as `0`, so it has no effect, but it can be used to explicitly indicate neither [`AT_STATX_FORCE_SYNC`](https://docs.python.org/3/library/os.html#os.AT_STATX_FORCE_SYNC "os.AT_STATX_FORCE_SYNC")
 nor [`AT_STATX_DONT_SYNC`](https://docs.python.org/3/library/os.html#os.AT_STATX_DONT_SYNC "os.AT_STATX_DONT_SYNC")
 is being passed. In the absence of the other two flags, the kernel will generally return information as fresh as [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 would return.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 4.11 with glibc >= 2.28.

Added in version 3.15.

os.AT\_NO\_AUTOMOUNT[¶](https://docs.python.org/3/library/os.html#os.AT_NO_AUTOMOUNT "Link to this definition")

If the final component of a path is an automount point, operate on the automount point instead of performing the automount. On Linux, [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
, [`os.fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat")
 and [`os.lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat")
 always behave this way.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.15.

os.statvfs(_path_)[¶](https://docs.python.org/3/library/os.html#os.statvfs "Link to this definition")

Perform a _[statvfs(3)](https://manpages.debian.org/statvfs(3))
_ system call on the given path. The return value is a [`statvfs_result`](https://docs.python.org/3/library/os.html#os.statvfs_result "os.statvfs_result")
 whose attributes describe the filesystem on the given path and correspond to the members of the `statvfs` structure.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Changed in version 3.3: Added support for specifying _path_ as an open file descriptor.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

class os.statvfs\_result[¶](https://docs.python.org/3/library/os.html#os.statvfs_result "Link to this definition")

Filesystem statistics returned by [`os.statvfs()`](https://docs.python.org/3/library/os.html#os.statvfs "os.statvfs")
 and [`os.fstatvfs()`](https://docs.python.org/3/library/os.html#os.fstatvfs "os.fstatvfs")
. See _[statvfs(3)](https://manpages.debian.org/statvfs(3))
_ for more details.

f\_bsize[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_bsize "Link to this definition")

Block size.

f\_frsize[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_frsize "Link to this definition")

Fragment size.

f\_blocks[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_blocks "Link to this definition")

Number of [`f_frsize`](https://docs.python.org/3/library/os.html#os.statvfs_result.f_frsize "os.statvfs_result.f_frsize")
 sized blocks the filesystem can contain.

f\_bfree[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_bfree "Link to this definition")

Number of free blocks.

f\_bavail[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_bavail "Link to this definition")

Number of free blocks for unprivileged users.

f\_files[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_files "Link to this definition")

Number of file entries, inodes, the filesystem can contain.

f\_ffree[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_ffree "Link to this definition")

Number of free files entries.

f\_favail[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_favail "Link to this definition")

Number of free file entries for unprivileged users.

f\_flag[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_flag "Link to this definition")

Bit-mask of mount flags. The following flags are defined: [`ST_RDONLY`](https://docs.python.org/3/library/os.html#os.ST_RDONLY "os.ST_RDONLY")
, [`ST_NOSUID`](https://docs.python.org/3/library/os.html#os.ST_NOSUID "os.ST_NOSUID")
, [`ST_NODEV`](https://docs.python.org/3/library/os.html#os.ST_NODEV "os.ST_NODEV")
, [`ST_NOEXEC`](https://docs.python.org/3/library/os.html#os.ST_NOEXEC "os.ST_NOEXEC")
, [`ST_SYNCHRONOUS`](https://docs.python.org/3/library/os.html#os.ST_SYNCHRONOUS "os.ST_SYNCHRONOUS")
, [`ST_MANDLOCK`](https://docs.python.org/3/library/os.html#os.ST_MANDLOCK "os.ST_MANDLOCK")
, [`ST_WRITE`](https://docs.python.org/3/library/os.html#os.ST_WRITE "os.ST_WRITE")
, [`ST_APPEND`](https://docs.python.org/3/library/os.html#os.ST_APPEND "os.ST_APPEND")
, [`ST_IMMUTABLE`](https://docs.python.org/3/library/os.html#os.ST_IMMUTABLE "os.ST_IMMUTABLE")
, [`ST_NOATIME`](https://docs.python.org/3/library/os.html#os.ST_NOATIME "os.ST_NOATIME")
, [`ST_NODIRATIME`](https://docs.python.org/3/library/os.html#os.ST_NODIRATIME "os.ST_NODIRATIME")
, and [`ST_RELATIME`](https://docs.python.org/3/library/os.html#os.ST_RELATIME "os.ST_RELATIME")
.

f\_namemax[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_namemax "Link to this definition")

Filesystem max filename length. OS specific limitations such as [Windows MAX\_PATH](https://docs.python.org/3/using/windows.html#max-path)
 and those described in Linux _[pathname(7)](https://manpages.debian.org/pathname(7))
_ may exist.

f\_fsid[¶](https://docs.python.org/3/library/os.html#os.statvfs_result.f_fsid "Link to this definition")

Filesystem ID.

Added in version 3.7.

The following flags are used in [`statvfs_result.f_flag`](https://docs.python.org/3/library/os.html#os.statvfs_result.f_flag "os.statvfs_result.f_flag")
.

os.ST\_RDONLY[¶](https://docs.python.org/3/library/os.html#os.ST_RDONLY "Link to this definition")

Read-only filesystem.

Added in version 3.2.

os.ST\_NOSUID[¶](https://docs.python.org/3/library/os.html#os.ST_NOSUID "Link to this definition")

Setuid/setgid bits are disabled or not supported.

Added in version 3.2.

os.ST\_NODEV[¶](https://docs.python.org/3/library/os.html#os.ST_NODEV "Link to this definition")

Disallow access to device special files.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.4.

os.ST\_NOEXEC[¶](https://docs.python.org/3/library/os.html#os.ST_NOEXEC "Link to this definition")

Disallow program execution.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.4.

os.ST\_SYNCHRONOUS[¶](https://docs.python.org/3/library/os.html#os.ST_SYNCHRONOUS "Link to this definition")

Writes are synced at once.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.4.

os.ST\_MANDLOCK[¶](https://docs.python.org/3/library/os.html#os.ST_MANDLOCK "Link to this definition")

Allow mandatory locks on an FS.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.4.

os.ST\_WRITE[¶](https://docs.python.org/3/library/os.html#os.ST_WRITE "Link to this definition")

Write on file/directory/symlink.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.4.

os.ST\_APPEND[¶](https://docs.python.org/3/library/os.html#os.ST_APPEND "Link to this definition")

Append-only file.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.4.

os.ST\_IMMUTABLE[¶](https://docs.python.org/3/library/os.html#os.ST_IMMUTABLE "Link to this definition")

Immutable file.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.4.

os.ST\_NOATIME[¶](https://docs.python.org/3/library/os.html#os.ST_NOATIME "Link to this definition")

Do not update access times.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.4.

os.ST\_NODIRATIME[¶](https://docs.python.org/3/library/os.html#os.ST_NODIRATIME "Link to this definition")

Do not update directory access times.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.4.

os.ST\_RELATIME[¶](https://docs.python.org/3/library/os.html#os.ST_RELATIME "Link to this definition")

Update atime relative to mtime/ctime.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.4.

os.supports\_dir\_fd[¶](https://docs.python.org/3/library/os.html#os.supports_dir_fd "Link to this definition")

A [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 object indicating which functions in the `os` module accept an open file descriptor for their _dir\_fd_ parameter. Different platforms provide different features, and the underlying functionality Python uses to implement the _dir\_fd_ parameter is not available on all platforms Python supports. For consistency’s sake, functions that may support _dir\_fd_ always allow specifying the parameter, but will throw an exception if the functionality is used when it’s not locally available. (Specifying `None` for _dir\_fd_ is always supported on all platforms.)

To check whether a particular function accepts an open file descriptor for its _dir\_fd_ parameter, use the `in` operator on `supports_dir_fd`. As an example, this expression evaluates to `True` if [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 accepts open file descriptors for _dir\_fd_ on the local platform:

Copy

os.stat in os.supports\_dir\_fd

Currently _dir\_fd_ parameters only work on Unix platforms; none of them work on Windows.

Added in version 3.3.

os.supports\_effective\_ids[¶](https://docs.python.org/3/library/os.html#os.supports_effective_ids "Link to this definition")

A [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 object indicating whether [`os.access()`](https://docs.python.org/3/library/os.html#os.access "os.access")
 permits specifying `True` for its _effective\_ids_ parameter on the local platform. (Specifying `False` for _effective\_ids_ is always supported on all platforms.) If the local platform supports it, the collection will contain `os.access()`; otherwise it will be empty.

This expression evaluates to `True` if [`os.access()`](https://docs.python.org/3/library/os.html#os.access "os.access")
 supports `effective_ids=True` on the local platform:

Copy

os.access in os.supports\_effective\_ids

Currently _effective\_ids_ is only supported on Unix platforms; it does not work on Windows.

Added in version 3.3.

os.supports\_fd[¶](https://docs.python.org/3/library/os.html#os.supports_fd "Link to this definition")

A [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 object indicating which functions in the `os` module permit specifying their _path_ parameter as an open file descriptor on the local platform. Different platforms provide different features, and the underlying functionality Python uses to accept open file descriptors as _path_ arguments is not available on all platforms Python supports.

To determine whether a particular function permits specifying an open file descriptor for its _path_ parameter, use the `in` operator on `supports_fd`. As an example, this expression evaluates to `True` if [`os.chdir()`](https://docs.python.org/3/library/os.html#os.chdir "os.chdir")
 accepts open file descriptors for _path_ on your local platform:

Copy

os.chdir in os.supports\_fd

Added in version 3.3.

os.supports\_follow\_symlinks[¶](https://docs.python.org/3/library/os.html#os.supports_follow_symlinks "Link to this definition")

A [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 object indicating which functions in the `os` module accept `False` for their _follow\_symlinks_ parameter on the local platform. Different platforms provide different features, and the underlying functionality Python uses to implement _follow\_symlinks_ is not available on all platforms Python supports. For consistency’s sake, functions that may support _follow\_symlinks_ always allow specifying the parameter, but will throw an exception if the functionality is used when it’s not locally available. (Specifying `True` for _follow\_symlinks_ is always supported on all platforms.)

To check whether a particular function accepts `False` for its _follow\_symlinks_ parameter, use the `in` operator on `supports_follow_symlinks`. As an example, this expression evaluates to `True` if you may specify `follow_symlinks=False` when calling [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 on the local platform:

Copy

os.stat in os.supports\_follow\_symlinks

Added in version 3.3.

os.symlink(_src_, _dst_, _target\_is\_directory\=False_, _\*_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.symlink "Link to this definition")

Create a symbolic link pointing to _src_ named _dst_.

The _src_ parameter refers to the target of the link (the file or directory being linked to), and _dst_ is the name of the link being created.

On Windows, a symlink represents either a file or a directory, and does not morph to the target dynamically. If the target is present, the type of the symlink will be created to match. Otherwise, the symlink will be created as a directory if _target\_is\_directory_ is `True` or a file symlink (the default) otherwise. On non-Windows platforms, _target\_is\_directory_ is ignored.

This function can support [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
.

Note

On newer versions of Windows 10, unprivileged accounts can create symlinks if Developer Mode is enabled. When Developer Mode is not available/enabled, the _SeCreateSymbolicLinkPrivilege_ privilege is required, or the process must be run as an administrator.

[`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised when the function is called by an unprivileged user.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.symlink` with arguments `src`, `dst`, `dir_fd`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

The function is limited on WASI, see [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

Changed in version 3.2: Added support for Windows 6.0 (Vista) symbolic links.

Changed in version 3.3: Added the _dir\_fd_ parameter, and now allow _target\_is\_directory_ on non-Windows platforms.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 for _src_ and _dst_.

Changed in version 3.8: Added support for unelevated symlinks on Windows with Developer Mode.

os.sync()[¶](https://docs.python.org/3/library/os.html#os.sync "Link to this definition")

Force write of everything to disk.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

os.truncate(_path_, _length_)[¶](https://docs.python.org/3/library/os.html#os.truncate "Link to this definition")

Truncate the file corresponding to _path_, so that it is at most _length_ bytes in size.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.truncate` with arguments `path`, `length`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

Added in version 3.3.

Changed in version 3.5: Added support for Windows

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.unlink(_path_, _\*_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.unlink "Link to this definition")

Remove (delete) the file _path_. This function is semantically identical to [`remove()`](https://docs.python.org/3/library/os.html#os.remove "os.remove")
; the `unlink` name is its traditional Unix name. Please see the documentation for `remove()` for further information.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.remove` with arguments `path`, `dir_fd`.

Changed in version 3.3: Added the _dir\_fd_ parameter.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.utime(_path_, _times\=None_, _\*_, \[_ns_, \]_dir\_fd\=None_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.utime "Link to this definition")

Set the access and modified times of the file specified by _path_.

`utime()` takes two optional parameters, _times_ and _ns_. These specify the times set on _path_ and are used as follows:

*   If _ns_ is specified, it must be a 2-tuple of the form `(atime_ns, mtime_ns)` where each member is an int expressing nanoseconds.
    
*   If _times_ is not `None`, it must be a 2-tuple of the form `(atime, mtime)` where each member is a real number expressing seconds, rounded down to nanoseconds.
    
*   If _times_ is `None` and _ns_ is unspecified, this is equivalent to specifying `ns=(atime_ns, mtime_ns)` where both times are the current time.
    

It is an error to specify tuples for both _times_ and _ns_.

Note that the exact times you set here may not be returned by a subsequent [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
 call, depending on the resolution with which your operating system records access and modification times; see `stat()`. The best way to preserve exact times is to use the _st\_atime\_ns_ and _st\_mtime\_ns_ fields from the `os.stat()` result object with the _ns_ parameter to `utime()`.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
, [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
 and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.utime` with arguments `path`, `times`, `ns`, `dir_fd`.

Changed in version 3.3: Added support for specifying _path_ as an open file descriptor, and the _dir\_fd_, _follow\_symlinks_, and _ns_ parameters.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.15: Accepts any real numbers as _times_, not only integers or floats.

os.walk(_top_, _topdown\=True_, _onerror\=None_, _followlinks\=False_)[¶](https://docs.python.org/3/library/os.html#os.walk "Link to this definition")

Generate the file names in a directory tree by walking the tree either top-down or bottom-up. For each directory in the tree rooted at directory _top_ (including _top_ itself), it yields a 3-tuple `(dirpath, dirnames, filenames)`.

_dirpath_ is a string, the path to the directory. _dirnames_ is a list of the names of the subdirectories in _dirpath_ (including symlinks to directories, and excluding `'.'` and `'..'`). _filenames_ is a list of the names of the non-directory files in _dirpath_. Note that the names in the lists contain no path components. To get a full path (which begins with _top_) to a file or directory in _dirpath_, do `os.path.join(dirpath, name)`. Whether or not the lists are sorted depends on the file system. If a file is removed from or added to the _dirpath_ directory during generating the lists, whether a name for that file be included is unspecified.

If optional argument _topdown_ is `True` or not specified, the triple for a directory is generated before the triples for any of its subdirectories (directories are generated top-down). If _topdown_ is `False`, the triple for a directory is generated after the triples for all of its subdirectories (directories are generated bottom-up). No matter the value of _topdown_, the list of subdirectories is retrieved before the tuples for the directory and its subdirectories are generated.

When _topdown_ is `True`, the caller can modify the _dirnames_ list in-place (perhaps using [`del`](https://docs.python.org/3/reference/simple_stmts.html#del)
 or slice assignment), and `walk()` will only recurse into the subdirectories whose names remain in _dirnames_; this can be used to prune the search, impose a specific order of visiting, or even to inform `walk()` about directories the caller creates or renames before it resumes `walk()` again. Modifying _dirnames_ when _topdown_ is `False` has no effect on the behavior of the walk, because in bottom-up mode the directories in _dirnames_ are generated before _dirpath_ itself is generated.

By default, errors from the [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
 call are ignored. If optional argument _onerror_ is specified, it should be a function; it will be called with one argument, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 instance. It can report the error to continue with the walk, or raise the exception to abort the walk. Note that the filename is available as the `filename` attribute of the exception object.

By default, `walk()` will not walk down into symbolic links that resolve to directories. Set _followlinks_ to `True` to visit directories pointed to by symlinks, on systems that support them.

Note

Be aware that setting _followlinks_ to `True` can lead to infinite recursion if a link points to a parent directory of itself. `walk()` does not keep track of the directories it visited already.

Note

If you pass a relative pathname, don’t change the current working directory between resumptions of `walk()`. `walk()` never changes the current directory, and assumes that its caller doesn’t either.

This example displays the number of bytes taken by non-directory files in each directory under the starting directory, except that it doesn’t look under any `__pycache__` subdirectory:

Copy

import os
from os.path import join, getsize
for root, dirs, files in os.walk('python/Lib/xml'):
    print(root, "consumes", end\=" ")
    print(sum(getsize(join(root, name)) for name in files), end\=" ")
    print("bytes in", len(files), "non-directory files")
    if '\_\_pycache\_\_' in dirs:
        dirs.remove('\_\_pycache\_\_')  \# don't visit \_\_pycache\_\_ directories

In the next example (simple implementation of [`shutil.rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree")
), walking the tree bottom-up is essential, [`rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir")
 doesn’t allow deleting a directory before the directory is empty:

Copy

\# Delete everything reachable from the directory named in "top",
\# assuming there are no symbolic links.
\# CAUTION:  This is dangerous!  For example, if top == '/', it
\# could delete all your disk files.
import os
for root, dirs, files in os.walk(top, topdown\=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
os.rmdir(top)

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.walk` with arguments `top`, `topdown`, `onerror`, `followlinks`.

Changed in version 3.5: This function now calls [`os.scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
 instead of [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir")
, making it faster by reducing the number of calls to [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.fwalk(_top\='.'_, _topdown\=True_, _onerror\=None_, _\*_, _follow\_symlinks\=False_, _dir\_fd\=None_)[¶](https://docs.python.org/3/library/os.html#os.fwalk "Link to this definition")

This behaves exactly like [`walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk")
, except that it yields a 4-tuple `(dirpath, dirnames, filenames, dirfd)`, and it supports `dir_fd`.

_dirpath_, _dirnames_ and _filenames_ are identical to [`walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk")
 output, and _dirfd_ is a file descriptor referring to the directory _dirpath_.

This function always supports [paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
 and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
. Note however that, unlike other functions, the `fwalk()` default value for _follow\_symlinks_ is `False`.

Note

Since `fwalk()` yields file descriptors, those are only valid until the next iteration step, so you should duplicate them (e.g. with [`dup()`](https://docs.python.org/3/library/os.html#os.dup "os.dup")
) if you want to keep them longer.

This example displays the number of bytes taken by non-directory files in each directory under the starting directory, except that it doesn’t look under any `__pycache__` subdirectory:

Copy

import os
for root, dirs, files, rootfd in os.fwalk('python/Lib/xml'):
    print(root, "consumes", end\=" ")
    print(sum(\[os.stat(name, dir\_fd\=rootfd).st\_size for name in files\]),
          end\=" ")
    print("bytes in", len(files), "non-directory files")
    if '\_\_pycache\_\_' in dirs:
        dirs.remove('\_\_pycache\_\_')  \# don't visit \_\_pycache\_\_ directories

In the next example, walking the tree bottom-up is essential: [`rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir")
 doesn’t allow deleting a directory before the directory is empty:

Copy

\# Delete everything reachable from the directory named in "top",
\# assuming there are no symbolic links.
\# CAUTION:  This is dangerous!  For example, if top == '/', it
\# could delete all your disk files.
import os
for root, dirs, files, rootfd in os.fwalk(top, topdown\=False):
    for name in files:
        os.unlink(name, dir\_fd\=rootfd)
    for name in dirs:
        os.rmdir(name, dir\_fd\=rootfd)

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.fwalk` with arguments `top`, `topdown`, `onerror`, `follow_symlinks`, `dir_fd`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.7: Added support for [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 paths.

os.memfd\_create(_name_\[, _flags\=os.MFD\_CLOEXEC_\])[¶](https://docs.python.org/3/library/os.html#os.memfd_create "Link to this definition")

Create an anonymous file and return a file descriptor that refers to it. _flags_ must be one of the `os.MFD_*` constants available on the system (or a bitwise ORed combination of them). By default, the new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

The name supplied in _name_ is used as a filename and will be displayed as the target of the corresponding symbolic link in the directory `/proc/self/fd/`. The displayed name is always prefixed with `memfd:` and serves only for debugging purposes. Names do not affect the behavior of the file descriptor, and as such multiple files can have the same name without any side effects.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 3.17 with glibc >= 2.27.

Added in version 3.8.

os.MFD\_CLOEXEC[¶](https://docs.python.org/3/library/os.html#os.MFD_CLOEXEC "Link to this definition")

os.MFD\_ALLOW\_SEALING[¶](https://docs.python.org/3/library/os.html#os.MFD_ALLOW_SEALING "Link to this definition")

os.MFD\_HUGETLB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGETLB "Link to this definition")

os.MFD\_HUGE\_SHIFT[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_SHIFT "Link to this definition")

os.MFD\_HUGE\_MASK[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_MASK "Link to this definition")

os.MFD\_HUGE\_64KB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_64KB "Link to this definition")

os.MFD\_HUGE\_512KB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_512KB "Link to this definition")

os.MFD\_HUGE\_1MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_1MB "Link to this definition")

os.MFD\_HUGE\_2MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_2MB "Link to this definition")

os.MFD\_HUGE\_8MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_8MB "Link to this definition")

os.MFD\_HUGE\_16MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_16MB "Link to this definition")

os.MFD\_HUGE\_32MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_32MB "Link to this definition")

os.MFD\_HUGE\_256MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_256MB "Link to this definition")

os.MFD\_HUGE\_512MB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_512MB "Link to this definition")

os.MFD\_HUGE\_1GB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_1GB "Link to this definition")

os.MFD\_HUGE\_2GB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_2GB "Link to this definition")

os.MFD\_HUGE\_16GB[¶](https://docs.python.org/3/library/os.html#os.MFD_HUGE_16GB "Link to this definition")

These flags can be passed to [`memfd_create()`](https://docs.python.org/3/library/os.html#os.memfd_create "os.memfd_create")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 3.17 with glibc >= 2.27

The `MFD_HUGE*` flags are only available since Linux 4.14.

Added in version 3.8.

os.eventfd(_initval_\[, _flags\=os.EFD\_CLOEXEC_\])[¶](https://docs.python.org/3/library/os.html#os.eventfd "Link to this definition")

Create and return an event file descriptor. The file descriptors supports raw [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read")
 and [`write()`](https://docs.python.org/3/library/os.html#os.write "os.write")
 with a buffer size of 8, [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select")
, [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll")
 and similar. See man page _[eventfd(2)](https://manpages.debian.org/eventfd(2))
_ for more information. By default, the new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

_initval_ is the initial value of the event counter. The initial value must be a 32 bit unsigned integer. Please note that the initial value is limited to a 32 bit unsigned int although the event counter is an unsigned 64 bit integer with a maximum value of 264\-2.

_flags_ can be constructed from [`EFD_CLOEXEC`](https://docs.python.org/3/library/os.html#os.EFD_CLOEXEC "os.EFD_CLOEXEC")
, [`EFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.EFD_NONBLOCK "os.EFD_NONBLOCK")
, and [`EFD_SEMAPHORE`](https://docs.python.org/3/library/os.html#os.EFD_SEMAPHORE "os.EFD_SEMAPHORE")
.

If [`EFD_SEMAPHORE`](https://docs.python.org/3/library/os.html#os.EFD_SEMAPHORE "os.EFD_SEMAPHORE")
 is specified and the event counter is non-zero, [`eventfd_read()`](https://docs.python.org/3/library/os.html#os.eventfd_read "os.eventfd_read")
 returns 1 and decrements the counter by one.

If [`EFD_SEMAPHORE`](https://docs.python.org/3/library/os.html#os.EFD_SEMAPHORE "os.EFD_SEMAPHORE")
 is not specified and the event counter is non-zero, [`eventfd_read()`](https://docs.python.org/3/library/os.html#os.eventfd_read "os.eventfd_read")
 returns the current event counter value and resets the counter to zero.

If the event counter is zero and [`EFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.EFD_NONBLOCK "os.EFD_NONBLOCK")
 is not specified, [`eventfd_read()`](https://docs.python.org/3/library/os.html#os.eventfd_read "os.eventfd_read")
 blocks.

[`eventfd_write()`](https://docs.python.org/3/library/os.html#os.eventfd_write "os.eventfd_write")
 increments the event counter. Write blocks if the write operation would increment the counter to a value larger than 264\-2.

Example:

Copy

import os

\# semaphore with start value '1'
fd \= os.eventfd(1, os.EFD\_SEMAPHORE | os.EFD\_CLOEXEC)
try:
    \# acquire semaphore
    v \= os.eventfd\_read(fd)
    try:
        do\_work()
    finally:
        \# release semaphore
        os.eventfd\_write(fd, v)
finally:
    os.close(fd)

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.10.

os.eventfd\_read(_fd_)[¶](https://docs.python.org/3/library/os.html#os.eventfd_read "Link to this definition")

Read value from an [`eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd")
 file descriptor and return a 64 bit unsigned int. The function does not verify that _fd_ is an `eventfd()`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27

Added in version 3.10.

os.eventfd\_write(_fd_, _value_)[¶](https://docs.python.org/3/library/os.html#os.eventfd_write "Link to this definition")

Add value to an [`eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd")
 file descriptor. _value_ must be a 64 bit unsigned int. The function does not verify that _fd_ is an `eventfd()`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27

Added in version 3.10.

os.EFD\_CLOEXEC[¶](https://docs.python.org/3/library/os.html#os.EFD_CLOEXEC "Link to this definition")

Set close-on-exec flag for new [`eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd")
 file descriptor.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27

Added in version 3.10.

os.EFD\_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.EFD_NONBLOCK "Link to this definition")

Set [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK")
 status flag for new [`eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd")
 file descriptor.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27

Added in version 3.10.

os.EFD\_SEMAPHORE[¶](https://docs.python.org/3/library/os.html#os.EFD_SEMAPHORE "Link to this definition")

Provide semaphore-like semantics for reads from an [`eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd")
 file descriptor. On read the internal counter is decremented by one.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.30

Added in version 3.10.

### Timer File Descriptors[¶](https://docs.python.org/3/library/os.html#timer-file-descriptors "Link to this heading")

Added in version 3.13.

These functions provide support for Linux’s _timer file descriptor_ API. Naturally, they are all only available on Linux.

os.timerfd\_create(_clockid_, _/_, _\*_, _flags\=0_)[¶](https://docs.python.org/3/library/os.html#os.timerfd_create "Link to this definition")

Create and return a timer file descriptor (_timerfd_).

The file descriptor returned by `timerfd_create()` supports:

*   [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read")
    
*   [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select")
    
*   [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll")
    

The file descriptor’s [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read")
 method can be called with a buffer size of 8. If the timer has already expired one or more times, `read()` returns the number of expirations with the host’s endianness, which may be converted to an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 by `int.from_bytes(x, byteorder=sys.byteorder)`.

[`select()`](https://docs.python.org/3/library/select.html#select.select "select.select")
 and [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll")
 can be used to wait until timer expires and the file descriptor is readable.

_clockid_ must be a valid [clock ID](https://docs.python.org/3/library/time.html#time-clock-id-constants)
, as defined in the [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.")
 module:

*   [`time.CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME")
    
*   [`time.CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC")
    
*   [`time.CLOCK_BOOTTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_BOOTTIME "time.CLOCK_BOOTTIME")
     (Since Linux 3.15 for timerfd\_create)
    

If _clockid_ is [`time.CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME")
, a settable system-wide real-time clock is used. If the system clock is changed, the timer setting needs to be updated. To cancel the timer when the system clock is changed, see [`TFD_TIMER_CANCEL_ON_SET`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_CANCEL_ON_SET "os.TFD_TIMER_CANCEL_ON_SET")
.

If _clockid_ is [`time.CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC")
, a non-settable monotonically increasing clock is used. Even if the system clock is changed, the timer setting will not be affected.

If _clockid_ is [`time.CLOCK_BOOTTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_BOOTTIME "time.CLOCK_BOOTTIME")
, it is the same as [`time.CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC")
 except it includes any time that the system is suspended.

The file descriptor’s behaviour can be modified by specifying a _flags_ value. Any of the following variables may be used, combined using bitwise OR (the `|` operator):

*   [`TFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "os.TFD_NONBLOCK")
    
*   [`TFD_CLOEXEC`](https://docs.python.org/3/library/os.html#os.TFD_CLOEXEC "os.TFD_CLOEXEC")
    

If [`TFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "os.TFD_NONBLOCK")
 is not set as a flag, [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read")
 blocks until the timer expires. If it is set as a flag, `read()` doesn’t block, but if there hasn’t been an expiration since the last call to read, `read()` raises [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 with `errno` set to [`errno.EAGAIN`](https://docs.python.org/3/library/errno.html#errno.EAGAIN "errno.EAGAIN")
.

[`TFD_CLOEXEC`](https://docs.python.org/3/library/os.html#os.TFD_CLOEXEC "os.TFD_CLOEXEC")
 is always set by Python automatically.

The file descriptor must be closed with [`os.close()`](https://docs.python.org/3/library/os.html#os.close "os.close")
 when it is no longer needed, or else the file descriptor will be leaked.

See also

The _[timerfd\_create(2)](https://manpages.debian.org/timerfd_create(2))
_ man page.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

os.timerfd\_settime(_fd_, _/_, _\*_, _flags\=0_, _initial\=0.0_, _interval\=0.0_)[¶](https://docs.python.org/3/library/os.html#os.timerfd_settime "Link to this definition")

Alter a timer file descriptor’s internal timer. This function operates the same interval timer as [`timerfd_settime_ns()`](https://docs.python.org/3/library/os.html#os.timerfd_settime_ns "os.timerfd_settime_ns")
.

_fd_ must be a valid timer file descriptor.

The timer’s behaviour can be modified by specifying a _flags_ value. Any of the following variables may be used, combined using bitwise OR (the `|` operator):

*   [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME")
    
*   [`TFD_TIMER_CANCEL_ON_SET`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_CANCEL_ON_SET "os.TFD_TIMER_CANCEL_ON_SET")
    

The timer is disabled by setting _initial_ to zero (`0`). If _initial_ is greater than zero, the timer is enabled. If _initial_ is less than zero, it raises an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exception with `errno` set to [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL")
.

By default the timer will fire when _initial_ seconds have elapsed.

However, if the [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME")
 flag is set, the timer will fire when the timer’s clock (set by _clockid_ in [`timerfd_create()`](https://docs.python.org/3/library/os.html#os.timerfd_create "os.timerfd_create")
) reaches _initial_ seconds.

The timer’s interval is set by the _interval_ real number. If _interval_ is zero, the timer only fires once, on the initial expiration. If _interval_ is greater than zero, the timer fires every time _interval_ seconds have elapsed since the previous expiration. If _interval_ is less than zero, it raises [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 with `errno` set to [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL")
.

If the [`TFD_TIMER_CANCEL_ON_SET`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_CANCEL_ON_SET "os.TFD_TIMER_CANCEL_ON_SET")
 flag is set along with [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME")
 and the clock for this timer is [`time.CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME")
, the timer is marked as cancelable if the real-time clock is changed discontinuously. Reading the descriptor is aborted with the error [`errno.ECANCELED`](https://docs.python.org/3/library/errno.html#errno.ECANCELED "errno.ECANCELED")
.

Linux manages system clock as UTC. A daylight-savings time transition is done by changing time offset only and doesn’t cause discontinuous system clock change.

Discontinuous system clock change will be caused by the following events:

*   `settimeofday`
    
*   `clock_settime`
    
*   set the system date and time by `date` command
    

Return a two-item tuple of (`next_expiration`, `interval`) from the previous timer state, before this function executed.

See also

_[timerfd\_create(2)](https://manpages.debian.org/timerfd_create(2))
_, _[timerfd\_settime(2)](https://manpages.debian.org/timerfd_settime(2))
_, _[settimeofday(2)](https://manpages.debian.org/settimeofday(2))
_, _[clock\_settime(2)](https://manpages.debian.org/clock_settime(2))
_, and _[date(1)](https://manpages.debian.org/date(1))
_.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

os.timerfd\_settime\_ns(_fd_, _/_, _\*_, _flags\=0_, _initial\=0_, _interval\=0_)[¶](https://docs.python.org/3/library/os.html#os.timerfd_settime_ns "Link to this definition")

Similar to [`timerfd_settime()`](https://docs.python.org/3/library/os.html#os.timerfd_settime "os.timerfd_settime")
, but use time as nanoseconds. This function operates the same interval timer as `timerfd_settime()`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

os.timerfd\_gettime(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.timerfd_gettime "Link to this definition")

Return a two-item tuple of floats (`next_expiration`, `interval`).

`next_expiration` denotes the relative time until the timer next fires, regardless of if the [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME")
 flag is set.

`interval` denotes the timer’s interval. If zero, the timer will only fire once, after `next_expiration` seconds have elapsed.

See also

_[timerfd\_gettime(2)](https://manpages.debian.org/timerfd_gettime(2))
_

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

os.timerfd\_gettime\_ns(_fd_, _/_)[¶](https://docs.python.org/3/library/os.html#os.timerfd_gettime_ns "Link to this definition")

Similar to [`timerfd_gettime()`](https://docs.python.org/3/library/os.html#os.timerfd_gettime "os.timerfd_gettime")
, but return time as nanoseconds.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

os.TFD\_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "Link to this definition")

A flag for the [`timerfd_create()`](https://docs.python.org/3/library/os.html#os.timerfd_create "os.timerfd_create")
 function, which sets the [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK")
 status flag for the new timer file descriptor. If [`TFD_NONBLOCK`](https://docs.python.org/3/library/os.html#os.TFD_NONBLOCK "os.TFD_NONBLOCK")
 is not set as a flag, [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read")
 blocks.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

os.TFD\_CLOEXEC[¶](https://docs.python.org/3/library/os.html#os.TFD_CLOEXEC "Link to this definition")

A flag for the [`timerfd_create()`](https://docs.python.org/3/library/os.html#os.timerfd_create "os.timerfd_create")
 function, If [`TFD_CLOEXEC`](https://docs.python.org/3/library/os.html#os.TFD_CLOEXEC "os.TFD_CLOEXEC")
 is set as a flag, set close-on-exec flag for new file descriptor.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

os.TFD\_TIMER\_ABSTIME[¶](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "Link to this definition")

A flag for the [`timerfd_settime()`](https://docs.python.org/3/library/os.html#os.timerfd_settime "os.timerfd_settime")
 and [`timerfd_settime_ns()`](https://docs.python.org/3/library/os.html#os.timerfd_settime_ns "os.timerfd_settime_ns")
 functions. If this flag is set, _initial_ is interpreted as an absolute value on the timer’s clock (in UTC seconds or nanoseconds since the Unix Epoch).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

os.TFD\_TIMER\_CANCEL\_ON\_SET[¶](https://docs.python.org/3/library/os.html#os.TFD_TIMER_CANCEL_ON_SET "Link to this definition")

A flag for the [`timerfd_settime()`](https://docs.python.org/3/library/os.html#os.timerfd_settime "os.timerfd_settime")
 and [`timerfd_settime_ns()`](https://docs.python.org/3/library/os.html#os.timerfd_settime_ns "os.timerfd_settime_ns")
 functions along with [`TFD_TIMER_ABSTIME`](https://docs.python.org/3/library/os.html#os.TFD_TIMER_ABSTIME "os.TFD_TIMER_ABSTIME")
. The timer is cancelled when the time of the underlying clock changes discontinuously.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.27 with glibc >= 2.8

Added in version 3.13.

### Linux extended attributes[¶](https://docs.python.org/3/library/os.html#linux-extended-attributes "Link to this heading")

Added in version 3.3.

These functions are all available on Linux only.

os.getxattr(_path_, _attribute_, _\*_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.getxattr "Link to this definition")

Return the value of the extended filesystem attribute _attribute_ for _path_. _attribute_ can be bytes or str (directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface). If it is str, it is encoded with the filesystem encoding.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
 and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.getxattr` with arguments `path`, `attribute`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 for _path_ and _attribute_.

os.listxattr(_path\=None_, _\*_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.listxattr "Link to this definition")

Return a list of the extended filesystem attributes on _path_. The attributes in the list are represented as strings decoded with the filesystem encoding. If _path_ is `None`, `listxattr()` will examine the current directory.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
 and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.listxattr` with argument `path`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.15: `os.listxattr(-1)` now fails with `OSError(errno.EBADF)` rather than listing extended attributes of the current directory.

os.removexattr(_path_, _attribute_, _\*_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.removexattr "Link to this definition")

Removes the extended filesystem attribute _attribute_ from _path_. _attribute_ should be bytes or str (directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface). If it is a string, it is encoded with the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
 and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.removexattr` with arguments `path`, `attribute`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 for _path_ and _attribute_.

os.setxattr(_path_, _attribute_, _value_, _flags\=0_, _\*_, _follow\_symlinks\=True_)[¶](https://docs.python.org/3/library/os.html#os.setxattr "Link to this definition")

Set the extended filesystem attribute _attribute_ on _path_ to _value_. _attribute_ must be a bytes or str with no embedded NULs (directly or indirectly through the [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface). If it is a str, it is encoded with the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
. _flags_ may be [`XATTR_REPLACE`](https://docs.python.org/3/library/os.html#os.XATTR_REPLACE "os.XATTR_REPLACE")
 or [`XATTR_CREATE`](https://docs.python.org/3/library/os.html#os.XATTR_CREATE "os.XATTR_CREATE")
. If `XATTR_REPLACE` is given and the attribute does not exist, `ENODATA` will be raised. If `XATTR_CREATE` is given and the attribute already exists, the attribute will not be created and `EEXISTS` will be raised.

This function can support [specifying a file descriptor](https://docs.python.org/3/library/os.html#path-fd)
 and [not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
.

Note

A bug in Linux kernel versions less than 2.6.39 caused the flags argument to be ignored on some filesystems.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.setxattr` with arguments `path`, `attribute`, `value`, `flags`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
 for _path_ and _attribute_.

os.XATTR\_SIZE\_MAX[¶](https://docs.python.org/3/library/os.html#os.XATTR_SIZE_MAX "Link to this definition")

The maximum size the value of an extended attribute can be. Currently, this is 64 KiB on Linux.

os.XATTR\_CREATE[¶](https://docs.python.org/3/library/os.html#os.XATTR_CREATE "Link to this definition")

This is a possible value for the flags argument in [`setxattr()`](https://docs.python.org/3/library/os.html#os.setxattr "os.setxattr")
. It indicates the operation must create an attribute.

os.XATTR\_REPLACE[¶](https://docs.python.org/3/library/os.html#os.XATTR_REPLACE "Link to this definition")

This is a possible value for the flags argument in [`setxattr()`](https://docs.python.org/3/library/os.html#os.setxattr "os.setxattr")
. It indicates the operation must replace an existing attribute.

Process Management[¶](https://docs.python.org/3/library/os.html#process-management "Link to this heading")

-----------------------------------------------------------------------------------------------------------

These functions may be used to create and manage processes.

The various [`exec*`](https://docs.python.org/3/library/os.html#os.execl "os.execl")
 functions take a list of arguments for the new program loaded into the process. In each case, the first of these arguments is passed to the new program as its own name rather than as an argument a user may have typed on a command line. For the C programmer, this is the `argv[0]` passed to a program’s `main()`. For example, `os.execv('/bin/echo', ['foo', 'bar'])` will only print `bar` on standard output; `foo` will seem to be ignored.

os.abort()[¶](https://docs.python.org/3/library/os.html#os.abort "Link to this definition")

Generate a [`SIGABRT`](https://docs.python.org/3/library/signal.html#signal.SIGABRT "signal.SIGABRT")
 signal to the current process. On Unix, the default behavior is to produce a core dump; on Windows, the process immediately returns an exit code of `3`. Be aware that calling this function will not call the Python signal handler registered for `SIGABRT` with [`signal.signal()`](https://docs.python.org/3/library/signal.html#signal.signal "signal.signal")
.

os.add\_dll\_directory(_path_)[¶](https://docs.python.org/3/library/os.html#os.add_dll_directory "Link to this definition")

Add a path to the DLL search path.

This search path is used when resolving dependencies for imported extension modules (the module itself is resolved through [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
), and also by [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
.

Remove the directory by calling **close()** on the returned object or using it in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement.

See the [Microsoft documentation](https://msdn.microsoft.com/44228cf2-6306-466c-8f16-f513cd3ba8b5)
 for more information about how DLLs are loaded.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.add_dll_directory` with argument `path`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Added in version 3.8: Previous versions of CPython would resolve DLLs using the default behavior for the current process. This led to inconsistencies, such as only sometimes searching `PATH` or the current working directory, and OS functions such as `AddDllDirectory` having no effect.

In 3.8, the two primary ways DLLs are loaded now explicitly override the process-wide behavior to ensure consistency. See the [porting notes](https://docs.python.org/3/whatsnew/3.8.html#bpo-36085-whatsnew)
 for information on updating libraries.

os.execl(_path_, _arg0_, _arg1_, _..._)[¶](https://docs.python.org/3/library/os.html#os.execl "Link to this definition")

os.execle(_path_, _arg0_, _arg1_, _..._, _env_)[¶](https://docs.python.org/3/library/os.html#os.execle "Link to this definition")

os.execlp(_file_, _arg0_, _arg1_, _..._)[¶](https://docs.python.org/3/library/os.html#os.execlp "Link to this definition")

os.execlpe(_file_, _arg0_, _arg1_, _..._, _env_)[¶](https://docs.python.org/3/library/os.html#os.execlpe "Link to this definition")

os.execv(_path_, _args_)[¶](https://docs.python.org/3/library/os.html#os.execv "Link to this definition")

os.execve(_path_, _args_, _env_)[¶](https://docs.python.org/3/library/os.html#os.execve "Link to this definition")

os.execvp(_file_, _args_)[¶](https://docs.python.org/3/library/os.html#os.execvp "Link to this definition")

os.execvpe(_file_, _args_, _env_)[¶](https://docs.python.org/3/library/os.html#os.execvpe "Link to this definition")

These functions all execute a new program, replacing the current process; they do not return. On Unix, the new executable is loaded into the current process, and will have the same process id as the caller. Errors will be reported as [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exceptions.

The current process is replaced immediately. Open file objects and descriptors are not flushed, so if there may be data buffered on these open files, you should flush them using [`flush()`](https://docs.python.org/3/library/io.html#io.IOBase.flush "io.IOBase.flush")
 or [`os.fsync()`](https://docs.python.org/3/library/os.html#os.fsync "os.fsync")
 before calling an `exec*` function.

The “l” and “v” variants of the `exec*` functions differ in how command-line arguments are passed. The “l” variants are perhaps the easiest to work with if the number of parameters is fixed when the code is written; the individual parameters simply become additional parameters to the `execl*()` functions. The “v” variants are good when the number of parameters is variable, with the arguments being passed in a list or tuple as the _args_ parameter. In either case, the arguments to the child process should start with the name of the command being run, but this is not enforced.

The variants which include a “p” near the end (`execlp()`, `execlpe()`, `execvp()`, and `execvpe()`) will use the `PATH` environment variable to locate the program _file_. When the environment is being replaced (using one of the `exec*e` variants, discussed in the next paragraph), the new environment is used as the source of the `PATH` variable. The other variants, `execl()`, `execle()`, `execv()`, and `execve()`, will not use the `PATH` variable to locate the executable; _path_ must contain an appropriate absolute or relative path. Relative paths must include at least one slash, even on Windows, as plain names will not be resolved.

For `execle()`, `execlpe()`, `execve()`, and `execvpe()` (note that these all end in “e”), the _env_ parameter must be a mapping which is used to define the environment variables for the new process (these are used instead of the current process’ environment); the functions `execl()`, `execlp()`, `execv()`, and `execvp()` all cause the new process to inherit the environment of the current process.

For `execve()` on some platforms, _path_ may also be specified as an open file descriptor. This functionality may not be supported on your platform; you can check whether or not it is available using [`os.supports_fd`](https://docs.python.org/3/library/os.html#os.supports_fd "os.supports_fd")
. If it is unavailable, using it will raise a [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.exec` with arguments `path`, `args`, `env`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI, not Android, not iOS.

Changed in version 3.3: Added support for specifying _path_ as an open file descriptor for `execve()`.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

os.\_exit(_n_)[¶](https://docs.python.org/3/library/os.html#os._exit "Link to this definition")

Exit the process with status _n_, without calling cleanup handlers, flushing stdio buffers, etc.

Note

The standard way to exit is [`sys.exit(n)`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit")
. `_exit()` should normally only be used in the child process after a [`fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
.

The following exit codes are defined and can be used with [`_exit()`](https://docs.python.org/3/library/os.html#os._exit "os._exit")
, although they are not required. These are typically used for system programs written in Python, such as a mail server’s external command delivery program.

Note

Some of these may not be available on all Unix platforms, since there is some variation. These constants are defined where they are defined by the underlying platform.

os.EX\_OK[¶](https://docs.python.org/3/library/os.html#os.EX_OK "Link to this definition")

Exit code that means no error occurred. May be taken from the defined value of `EXIT_SUCCESS` on some platforms. Generally has a value of zero.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

os.EX\_USAGE[¶](https://docs.python.org/3/library/os.html#os.EX_USAGE "Link to this definition")

Exit code that means the command was used incorrectly, such as when the wrong number of arguments are given.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_DATAERR[¶](https://docs.python.org/3/library/os.html#os.EX_DATAERR "Link to this definition")

Exit code that means the input data was incorrect.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_NOINPUT[¶](https://docs.python.org/3/library/os.html#os.EX_NOINPUT "Link to this definition")

Exit code that means an input file did not exist or was not readable.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_NOUSER[¶](https://docs.python.org/3/library/os.html#os.EX_NOUSER "Link to this definition")

Exit code that means a specified user did not exist.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_NOHOST[¶](https://docs.python.org/3/library/os.html#os.EX_NOHOST "Link to this definition")

Exit code that means a specified host did not exist.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_UNAVAILABLE[¶](https://docs.python.org/3/library/os.html#os.EX_UNAVAILABLE "Link to this definition")

Exit code that means that a required service is unavailable.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_SOFTWARE[¶](https://docs.python.org/3/library/os.html#os.EX_SOFTWARE "Link to this definition")

Exit code that means an internal software error was detected.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_OSERR[¶](https://docs.python.org/3/library/os.html#os.EX_OSERR "Link to this definition")

Exit code that means an operating system error was detected, such as the inability to fork or create a pipe.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_OSFILE[¶](https://docs.python.org/3/library/os.html#os.EX_OSFILE "Link to this definition")

Exit code that means some system file did not exist, could not be opened, or had some other kind of error.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_CANTCREAT[¶](https://docs.python.org/3/library/os.html#os.EX_CANTCREAT "Link to this definition")

Exit code that means a user specified output file could not be created.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_IOERR[¶](https://docs.python.org/3/library/os.html#os.EX_IOERR "Link to this definition")

Exit code that means that an error occurred while doing I/O on some file.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_TEMPFAIL[¶](https://docs.python.org/3/library/os.html#os.EX_TEMPFAIL "Link to this definition")

Exit code that means a temporary failure occurred. This indicates something that may not really be an error, such as a network connection that couldn’t be made during a retryable operation.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_PROTOCOL[¶](https://docs.python.org/3/library/os.html#os.EX_PROTOCOL "Link to this definition")

Exit code that means that a protocol exchange was illegal, invalid, or not understood.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_NOPERM[¶](https://docs.python.org/3/library/os.html#os.EX_NOPERM "Link to this definition")

Exit code that means that there were insufficient permissions to perform the operation (but not intended for file system problems).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_CONFIG[¶](https://docs.python.org/3/library/os.html#os.EX_CONFIG "Link to this definition")

Exit code that means that some kind of configuration error occurred.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.EX\_NOTFOUND[¶](https://docs.python.org/3/library/os.html#os.EX_NOTFOUND "Link to this definition")

Exit code that means something like “an entry was not found”.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.fork()[¶](https://docs.python.org/3/library/os.html#os.fork "Link to this definition")

Fork a child process. Return `0` in the child and the child’s process id in the parent. If an error occurs [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised.

Note that some platforms including FreeBSD <= 6.3 and Cygwin have known issues when using `fork()` from a thread.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.fork` with no arguments.

Warning

If you use TLS sockets in an application calling `fork()`, see the warning in the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
 documentation.

Warning

On macOS the use of this function is unsafe when mixed with using higher-level system APIs, and that includes using [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")
.

Changed in version 3.8: Calling `fork()` in a subinterpreter is no longer supported ([`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 is raised).

Changed in version 3.12: If Python is able to detect that your process has multiple threads, `os.fork()` now raises a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
.

We chose to surface this as a warning, when detectable, to better inform developers of a design problem that the POSIX platform specifically notes as not supported. Even in code that _appears_ to work, it has never been safe to mix threading with `os.fork()` on POSIX platforms. The CPython runtime itself has always made API calls that are not safe for use in the child process when threads existed in the parent (such as `malloc` and `free`).

Users of macOS or users of libc or malloc implementations other than those typically found in glibc to date are among those already more likely to experience deadlocks running such code.

See [this discussion on fork being incompatible with threads](https://discuss.python.org/t/33555)
 for technical details of why we’re surfacing this longstanding platform compatibility problem to developers.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: POSIX, not WASI, not Android, not iOS.

os.forkpty()[¶](https://docs.python.org/3/library/os.html#os.forkpty "Link to this definition")

Fork a child process, using a new pseudo-terminal as the child’s controlling terminal. Return a pair of `(pid, fd)`, where _pid_ is `0` in the child, the new child’s process id in the parent, and _fd_ is the file descriptor of the master end of the pseudo-terminal. For a more portable approach, use the [`pty`](https://docs.python.org/3/library/pty.html#module-pty "pty: Pseudo-Terminal Handling for Unix.")
 module. If an error occurs [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised.

The returned file descriptor _fd_ is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.forkpty` with no arguments.

Warning

On macOS the use of this function is unsafe when mixed with using higher-level system APIs, and that includes using [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")
.

Changed in version 3.8: Calling `forkpty()` in a subinterpreter is no longer supported ([`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 is raised).

Changed in version 3.12: If Python is able to detect that your process has multiple threads, this now raises a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
. See the longer explanation on [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
.

Changed in version 3.15: The returned file descriptor is now made non-inheritable.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.kill(_pid_, _sig_, _/_)[¶](https://docs.python.org/3/library/os.html#os.kill "Link to this definition")

Send signal _sig_ to the process _pid_. Constants for the specific signals available on the host platform are defined in the [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")
 module.

Windows: The [`signal.CTRL_C_EVENT`](https://docs.python.org/3/library/signal.html#signal.CTRL_C_EVENT "signal.CTRL_C_EVENT")
 and [`signal.CTRL_BREAK_EVENT`](https://docs.python.org/3/library/signal.html#signal.CTRL_BREAK_EVENT "signal.CTRL_BREAK_EVENT")
 signals are special signals which can only be sent to console processes which share a common console window, e.g., some subprocesses. Any other value for _sig_ will cause the process to be unconditionally killed by the TerminateProcess API, and the exit code will be set to _sig_.

See also [`signal.pthread_kill()`](https://docs.python.org/3/library/signal.html#signal.pthread_kill "signal.pthread_kill")
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.kill` with arguments `pid`, `sig`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI, not iOS.

Changed in version 3.2: Added Windows support.

os.killpg(_pgid_, _sig_, _/_)[¶](https://docs.python.org/3/library/os.html#os.killpg "Link to this definition")

Send the signal _sig_ to the process group _pgid_.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.killpg` with arguments `pgid`, `sig`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not iOS.

os.nice(_increment_, _/_)[¶](https://docs.python.org/3/library/os.html#os.nice "Link to this definition")

Add _increment_ to the process’s “niceness”. Return the new niceness.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

os.pidfd\_open(_pid_, _flags\=0_)[¶](https://docs.python.org/3/library/os.html#os.pidfd_open "Link to this definition")

Return a file descriptor referring to the process _pid_ with _flags_ set. This descriptor can be used to perform process management without races and signals.

See the _[pidfd\_open(2)](https://manpages.debian.org/pidfd_open(2))
_ man page for more details.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 5.3, Android >= [`build-time`](https://docs.python.org/3/library/sys.html#sys.getandroidapilevel "sys.getandroidapilevel")
 API level 31

Added in version 3.9.

os.PIDFD\_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.PIDFD_NONBLOCK "Link to this definition")

This flag indicates that the file descriptor will be non-blocking. If the process referred to by the file descriptor has not yet terminated, then an attempt to wait on the file descriptor using _[waitid(2)](https://manpages.debian.org/waitid(2))
_ will immediately return the error [`EAGAIN`](https://docs.python.org/3/library/errno.html#errno.EAGAIN "errno.EAGAIN")
 rather than blocking.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 5.10

Added in version 3.12.

os.plock(_op_, _/_)[¶](https://docs.python.org/3/library/os.html#os.plock "Link to this definition")

Lock program segments into memory. The value of _op_ (defined in `<sys/lock.h>`) determines which segments are locked.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not macOS, not iOS.

os.popen(_cmd_, _mode\='r'_, _buffering\=\-1_)[¶](https://docs.python.org/3/library/os.html#os.popen "Link to this definition")

Open a pipe to or from command _cmd_. The return value is an open file object connected to the pipe, which can be read or written depending on whether _mode_ is `'r'` (default) or `'w'`. The _buffering_ argument have the same meaning as the corresponding argument to the built-in [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 function. The returned file object reads or writes text strings rather than bytes.

The `close` method returns [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 if the subprocess exited successfully, or the subprocess’s return code if there was an error. On POSIX systems, if the return code is positive it represents the return value of the process left-shifted by one byte. If the return code is negative, the process was terminated by the signal given by the negated value of the return code. (For example, the return value might be `- signal.SIGKILL` if the subprocess was killed.) On Windows systems, the return value contains the signed integer return code from the child process.

On Unix, [`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode")
 can be used to convert the `close` method result (exit status) into an exit code if it is not `None`. On Windows, the `close` method result is directly the exit code (or `None`).

This is implemented using [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
; see that class’s documentation for more powerful ways to manage and communicate with subprocesses.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI, not Android, not iOS.

Note

The [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
 affects encodings used for _cmd_ and pipe contents.

`popen()` is a simple wrapper around [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
. Use `subprocess.Popen` or [`subprocess.run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run")
 to control options like encodings.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.14: The [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
 module is recommended instead.

os.posix\_spawn(_path_, _argv_, _env_, _\*_, _file\_actions\=None_, _setpgroup\=None_, _resetids\=False_, _setsid\=False_, _setsigmask\=()_, _setsigdef\=()_, _scheduler\=None_)[¶](https://docs.python.org/3/library/os.html#os.posix_spawn "Link to this definition")

Wraps the `posix_spawn()` C library API for use from Python.

Most users should use [`subprocess.run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run")
 instead of `posix_spawn()`.

The positional-only arguments _path_, _args_, and _env_ are similar to [`execve()`](https://docs.python.org/3/library/os.html#os.execve "os.execve")
. _env_ is allowed to be `None`, in which case current process’ environment is used.

The _path_ parameter is the path to the executable file. The _path_ should contain a directory. Use [`posix_spawnp()`](https://docs.python.org/3/library/os.html#os.posix_spawnp "os.posix_spawnp")
 to pass an executable file without directory.

The _file\_actions_ argument may be a sequence of tuples describing actions to take on specific file descriptors in the child process between the C library implementation’s `fork()` and `exec()` steps. The first item in each tuple must be one of the three type indicator listed below describing the remaining tuple elements:

os.POSIX\_SPAWN\_OPEN[¶](https://docs.python.org/3/library/os.html#os.POSIX_SPAWN_OPEN "Link to this definition")

(`os.POSIX_SPAWN_OPEN`, _fd_, _path_, _flags_, _mode_)

Performs `os.dup2(os.open(path, flags, mode), fd)`.

os.POSIX\_SPAWN\_CLOSE[¶](https://docs.python.org/3/library/os.html#os.POSIX_SPAWN_CLOSE "Link to this definition")

(`os.POSIX_SPAWN_CLOSE`, _fd_)

Performs `os.close(fd)`.

os.POSIX\_SPAWN\_DUP2[¶](https://docs.python.org/3/library/os.html#os.POSIX_SPAWN_DUP2 "Link to this definition")

(`os.POSIX_SPAWN_DUP2`, _fd_, _new\_fd_)

Performs `os.dup2(fd, new_fd)`.

os.POSIX\_SPAWN\_CLOSEFROM[¶](https://docs.python.org/3/library/os.html#os.POSIX_SPAWN_CLOSEFROM "Link to this definition")

(`os.POSIX_SPAWN_CLOSEFROM`, _fd_)

Performs `os.closerange(fd, INF)`.

These tuples correspond to the C library `posix_spawn_file_actions_addopen()`, `posix_spawn_file_actions_addclose()`, `posix_spawn_file_actions_adddup2()`, and `posix_spawn_file_actions_addclosefrom_np()` API calls used to prepare for the `posix_spawn()` call itself.

The _setpgroup_ argument will set the process group of the child to the value specified. If the value specified is 0, the child’s process group ID will be made the same as its process ID. If the value of _setpgroup_ is not set, the child will inherit the parent’s process group ID. This argument corresponds to the C library `POSIX_SPAWN_SETPGROUP` flag.

If the _resetids_ argument is `True` it will reset the effective UID and GID of the child to the real UID and GID of the parent process. If the argument is `False`, then the child retains the effective UID and GID of the parent. In either case, if the set-user-ID and set-group-ID permission bits are enabled on the executable file, their effect will override the setting of the effective UID and GID. This argument corresponds to the C library `POSIX_SPAWN_RESETIDS` flag.

If the _setsid_ argument is `True`, it will create a new session ID for `posix_spawn`. _setsid_ requires `POSIX_SPAWN_SETSID` or `POSIX_SPAWN_SETSID_NP` flag. Otherwise, [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
 is raised.

The _setsigmask_ argument will set the signal mask to the signal set specified. If the parameter is not used, then the child inherits the parent’s signal mask. This argument corresponds to the C library `POSIX_SPAWN_SETSIGMASK` flag.

The _setsigdef_ argument will reset the disposition of all signals in the set specified. This argument corresponds to the C library `POSIX_SPAWN_SETSIGDEF` flag.

The _scheduler_ argument must be a tuple containing the (optional) scheduler policy and an instance of [`sched_param`](https://docs.python.org/3/library/os.html#os.sched_param "os.sched_param")
 with the scheduler parameters. A value of `None` in the place of the scheduler policy indicates that is not being provided. This argument is a combination of the C library `POSIX_SPAWN_SETSCHEDPARAM` and `POSIX_SPAWN_SETSCHEDULER` flags.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.posix_spawn` with arguments `path`, `argv`, `env`.

Added in version 3.8.

Changed in version 3.13: _env_ parameter accepts `None`. `os.POSIX_SPAWN_CLOSEFROM` is available on platforms where `posix_spawn_file_actions_addclosefrom_np()` exists.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.posix\_spawnp(_path_, _argv_, _env_, _\*_, _file\_actions\=None_, _setpgroup\=None_, _resetids\=False_, _setsid\=False_, _setsigmask\=()_, _setsigdef\=()_, _scheduler\=None_)[¶](https://docs.python.org/3/library/os.html#os.posix_spawnp "Link to this definition")

Wraps the `posix_spawnp()` C library API for use from Python.

Similar to [`posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn")
 except that the system searches for the _executable_ file in the list of directories specified by the `PATH` environment variable (in the same way as for `execvp(3)`).

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.posix_spawn` with arguments `path`, `argv`, `env`.

Added in version 3.8.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: POSIX, not WASI, not Android, not iOS.

See [`posix_spawn()`](https://docs.python.org/3/library/os.html#os.posix_spawn "os.posix_spawn")
 documentation.

os.register\_at\_fork(_\*_, _before\=None_, _after\_in\_parent\=None_, _after\_in\_child\=None_)[¶](https://docs.python.org/3/library/os.html#os.register_at_fork "Link to this definition")

Register callables to be executed when a new child process is forked using [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
 or similar process cloning APIs. The parameters are optional and keyword-only. Each specifies a different call point.

*   _before_ is a function called before forking a child process.
    
*   _after\_in\_parent_ is a function called from the parent process after forking a child process.
    
*   _after\_in\_child_ is a function called from the child process.
    

These calls are only made if control is expected to return to the Python interpreter. A typical [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
 launch will not trigger them as the child is not going to re-enter the interpreter.

Functions registered for execution before forking are called in reverse registration order. Functions registered for execution after forking (either in the parent or in the child) are called in registration order.

Note that `fork()` calls made by third-party C code may not call those functions, unless it explicitly calls [`PyOS_BeforeFork()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_BeforeFork "PyOS_BeforeFork")
, [`PyOS_AfterFork_Parent()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Parent "PyOS_AfterFork_Parent")
 and [`PyOS_AfterFork_Child()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Child "PyOS_AfterFork_Child")
.

There is no way to unregister a function.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

Added in version 3.7.

os.spawnl(_mode_, _file_, _..._)[¶](https://docs.python.org/3/library/os.html#os.spawnl "Link to this definition")

os.spawnle(_mode_, _file_, _..._, _env_)[¶](https://docs.python.org/3/library/os.html#os.spawnle "Link to this definition")

os.spawnlp(_mode_, _file_, _..._)[¶](https://docs.python.org/3/library/os.html#os.spawnlp "Link to this definition")

os.spawnlpe(_mode_, _file_, _..._, _env_)[¶](https://docs.python.org/3/library/os.html#os.spawnlpe "Link to this definition")

os.spawnv(_mode_, _file_, _args_)[¶](https://docs.python.org/3/library/os.html#os.spawnv "Link to this definition")

os.spawnve(_mode_, _file_, _args_, _env_)[¶](https://docs.python.org/3/library/os.html#os.spawnve "Link to this definition")

os.spawnvp(_mode_, _file_, _args_)[¶](https://docs.python.org/3/library/os.html#os.spawnvp "Link to this definition")

os.spawnvpe(_mode_, _file_, _args_, _env_)[¶](https://docs.python.org/3/library/os.html#os.spawnvpe "Link to this definition")

Execute the program _file_ in a new process.

(Note that the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
 module provides more powerful facilities for spawning new processes and retrieving their results; using that module is preferable to using these functions. Check especially the [Replacing Older Functions with the subprocess Module](https://docs.python.org/3/library/subprocess.html#subprocess-replacements)
 section.)

If _mode_ is [`P_NOWAIT`](https://docs.python.org/3/library/os.html#os.P_NOWAIT "os.P_NOWAIT")
, this function returns the process id of the new process; if _mode_ is [`P_WAIT`](https://docs.python.org/3/library/os.html#os.P_WAIT "os.P_WAIT")
, returns the process’s exit code if it exits normally, or `-signal`, where _signal_ is the signal that killed the process. On Windows, the process id will actually be the process handle, so can be used with the [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
 function.

Note on VxWorks, this function doesn’t return `-signal` when the new process is killed. Instead it raises OSError exception.

The “l” and “v” variants of the `spawn*` functions differ in how command-line arguments are passed. The “l” variants are perhaps the easiest to work with if the number of parameters is fixed when the code is written; the individual parameters simply become additional parameters to the `spawnl*()` functions. The “v” variants are good when the number of parameters is variable, with the arguments being passed in a list or tuple as the _args_ parameter. In either case, the arguments to the child process must start with the name of the command being run.

The variants which include a second “p” near the end (`spawnlp()`, `spawnlpe()`, `spawnvp()`, and `spawnvpe()`) will use the `PATH` environment variable to locate the program _file_. When the environment is being replaced (using one of the `spawn*e` variants, discussed in the next paragraph), the new environment is used as the source of the `PATH` variable. The other variants, `spawnl()`, `spawnle()`, `spawnv()`, and `spawnve()`, will not use the `PATH` variable to locate the executable; _file_ must contain an appropriate absolute or relative path.

For `spawnle()`, `spawnlpe()`, `spawnve()`, and `spawnvpe()` (note that these all end in “e”), the _env_ parameter must be a mapping which is used to define the environment variables for the new process (they are used instead of the current process’ environment); the functions `spawnl()`, `spawnlp()`, `spawnv()`, and `spawnvp()` all cause the new process to inherit the environment of the current process. Note that keys and values in the _env_ dictionary must be strings; invalid keys or values will cause the function to fail, with a return value of `127`.

As an example, the following calls to `spawnlp()` and `spawnvpe()` are equivalent:

Copy

import os
os.spawnlp(os.P\_WAIT, 'cp', 'cp', 'index.html', '/dev/null')

L \= \['cp', 'index.html', '/dev/null'\]
os.spawnvpe(os.P\_WAIT, 'cp', L, os.environ)

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.spawn` with arguments `mode`, `file`, `args`, `env`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI, not Android, not iOS.

`spawnlp()`, `spawnlpe()`, `spawnvp()` and `spawnvpe()` are not available on Windows. `spawnle()` and `spawnve()` are not thread-safe on Windows; we advise you to use the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
 module instead.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.14: The [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
 module is recommended instead.

os.P\_NOWAIT[¶](https://docs.python.org/3/library/os.html#os.P_NOWAIT "Link to this definition")

os.P\_NOWAITO[¶](https://docs.python.org/3/library/os.html#os.P_NOWAITO "Link to this definition")

Possible values for the _mode_ parameter to the [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl")
 family of functions. If either of these values is given, the `spawn*` functions will return as soon as the new process has been created, with the process id as the return value.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

os.P\_WAIT[¶](https://docs.python.org/3/library/os.html#os.P_WAIT "Link to this definition")

Possible value for the _mode_ parameter to the [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl")
 family of functions. If this is given as _mode_, the `spawn*` functions will not return until the new process has run to completion and will return the exit code of the process the run is successful, or `-signal` if a signal kills the process.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

os.P\_DETACH[¶](https://docs.python.org/3/library/os.html#os.P_DETACH "Link to this definition")

os.P\_OVERLAY[¶](https://docs.python.org/3/library/os.html#os.P_OVERLAY "Link to this definition")

Possible values for the _mode_ parameter to the [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl")
 family of functions. These are less portable than those listed above. [`P_DETACH`](https://docs.python.org/3/library/os.html#os.P_DETACH "os.P_DETACH")
 is similar to [`P_NOWAIT`](https://docs.python.org/3/library/os.html#os.P_NOWAIT "os.P_NOWAIT")
, but the new process is detached from the console of the calling process. If [`P_OVERLAY`](https://docs.python.org/3/library/os.html#os.P_OVERLAY "os.P_OVERLAY")
 is used, the current process will be replaced; the `spawn*` function will not return.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

os.startfile(_path_\[, _operation_\]\[, _arguments_\]\[, _cwd_\]\[, _show\_cmd_\])[¶](https://docs.python.org/3/library/os.html#os.startfile "Link to this definition")

Start a file with its associated application.

When _operation_ is not specified, this acts like double-clicking the file in Windows Explorer, or giving the file name as an argument to the **start** command from the interactive command shell: the file is opened with whatever application (if any) its extension is associated.

When another _operation_ is given, it must be a “command verb” that specifies what should be done with the file. Common verbs documented by Microsoft are `'open'`, `'print'` and `'edit'` (to be used on files) as well as `'explore'` and `'find'` (to be used on directories).

When launching an application, specify _arguments_ to be passed as a single string. This argument may have no effect when using this function to launch a document.

The default working directory is inherited, but may be overridden by the _cwd_ argument. This should be an absolute path. A relative _path_ will be resolved against this argument.

Use _show\_cmd_ to override the default window style. Whether this has any effect will depend on the application being launched. Values are integers as supported by the Win32 `ShellExecute()` function.

`startfile()` returns as soon as the associated application is launched. There is no option to wait for the application to close, and no way to retrieve the application’s exit status. The _path_ parameter is relative to the current directory or _cwd_. If you want to use an absolute path, make sure the first character is not a slash (`'/'`) Use [`pathlib`](https://docs.python.org/3/library/pathlib.html#module-pathlib "pathlib: Object-oriented filesystem paths")
 or the [`os.path.normpath()`](https://docs.python.org/3/library/os.path.html#os.path.normpath "os.path.normpath")
 function to ensure that paths are properly encoded for Win32.

To reduce interpreter startup overhead, the Win32 `ShellExecute()` function is not resolved until this function is first called. If the function cannot be resolved, [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
 will be raised.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.startfile` with arguments `path`, `operation`.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.startfile/2` with arguments `path`, `operation`, `arguments`, `cwd`, `show_cmd`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Changed in version 3.10: Added the _arguments_, _cwd_ and _show\_cmd_ arguments, and the `os.startfile/2` audit event.

os.system(_command_)[¶](https://docs.python.org/3/library/os.html#os.system "Link to this definition")

Execute the command (a string) in a subshell. This is implemented by calling the Standard C function `system()`, and has the same limitations. Changes to [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
, etc. are not reflected in the environment of the executed command. If _command_ generates any output, it will be sent to the interpreter standard output stream. The C standard does not specify the meaning of the return value of the C function, so the return value of the Python function is system-dependent.

On Unix, the return value is the exit status of the process encoded in the format specified for [`wait()`](https://docs.python.org/3/library/os.html#os.wait "os.wait")
.

On Windows, the return value is that returned by the system shell after running _command_. The shell is given by the Windows environment variable `COMSPEC`: it is usually **cmd.exe**, which returns the exit status of the command run; on systems using a non-native shell, consult your shell documentation.

The [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
 module provides more powerful facilities for spawning new processes and retrieving their results; using that module is recommended to using this function. See the [Replacing Older Functions with the subprocess Module](https://docs.python.org/3/library/subprocess.html#subprocess-replacements)
 section in the `subprocess` documentation for some helpful recipes.

On Unix, [`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode")
 can be used to convert the result (exit status) into an exit code. On Windows, the result is directly the exit code.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `os.system` with argument `command`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI, not Android, not iOS.

os.times()[¶](https://docs.python.org/3/library/os.html#os.times "Link to this definition")

Returns the current global process times. The return value is an object with five attributes:

*   `user` - user time
    
*   `system` - system time
    
*   `children_user` - user time of all child processes
    
*   `children_system` - system time of all child processes
    
*   `elapsed` - elapsed real time since a fixed point in the past
    

For backwards compatibility, this object also behaves like a five-tuple containing `user`, `system`, `children_user`, `children_system`, and `elapsed` in that order.

See the Unix manual page _[times(2)](https://manpages.debian.org/times(2))
_ and [times(3)](https://man.freebsd.org/cgi/man.cgi?time(3))
 manual page on Unix or [the GetProcessTimes MSDN](https://docs.microsoft.com/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesstimes)
 on Windows. On Windows, only `user` and `system` are known; the other attributes are zero.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

Changed in version 3.3: Return type changed from a tuple to a tuple-like object with named attributes.

os.wait()[¶](https://docs.python.org/3/library/os.html#os.wait "Link to this definition")

Wait for completion of a child process, and return a tuple containing its pid and exit status indication: a 16-bit number, whose low byte is the signal number that killed the process, and whose high byte is the exit status (if the signal number is zero); the high bit of the low byte is set if a core file was produced.

If there are no children that could be waited for, [`ChildProcessError`](https://docs.python.org/3/builtins/exceptions.html#ChildProcessError "ChildProcessError")
 is raised.

[`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode")
 can be used to convert the exit status into an exit code.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

See also

The other `wait*()` functions documented below can be used to wait for the completion of a specific child process and have more options. [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
 is the only one also available on Windows.

os.waitid(_idtype_, _id_, _options_, _/_)[¶](https://docs.python.org/3/library/os.html#os.waitid "Link to this definition")

Wait for the completion of a child process.

_idtype_ can be [`P_PID`](https://docs.python.org/3/library/os.html#os.P_PID "os.P_PID")
, [`P_PGID`](https://docs.python.org/3/library/os.html#os.P_PGID "os.P_PGID")
, [`P_ALL`](https://docs.python.org/3/library/os.html#os.P_ALL "os.P_ALL")
, or (on Linux) [`P_PIDFD`](https://docs.python.org/3/library/os.html#os.P_PIDFD "os.P_PIDFD")
. The interpretation of _id_ depends on it; see their individual descriptions.

_options_ is an OR combination of flags. At least one of [`WEXITED`](https://docs.python.org/3/library/os.html#os.WEXITED "os.WEXITED")
, [`WSTOPPED`](https://docs.python.org/3/library/os.html#os.WSTOPPED "os.WSTOPPED")
 or [`WCONTINUED`](https://docs.python.org/3/library/os.html#os.WCONTINUED "os.WCONTINUED")
 is required; [`WNOHANG`](https://docs.python.org/3/library/os.html#os.WNOHANG "os.WNOHANG")
 and [`WNOWAIT`](https://docs.python.org/3/library/os.html#os.WNOWAIT "os.WNOWAIT")
 are additional optional flags.

The return value is an object representing the data contained in the `siginfo_t` structure with the following attributes:

*   `si_pid` (process ID)
    
*   `si_uid` (real user ID of the child)
    
*   `si_signo` (always [`SIGCHLD`](https://docs.python.org/3/library/signal.html#signal.SIGCHLD "signal.SIGCHLD")
    )
    
*   `si_status` (the exit status or signal number, depending on `si_code`)
    
*   `si_code` (see [`CLD_EXITED`](https://docs.python.org/3/library/os.html#os.CLD_EXITED "os.CLD_EXITED")
     for possible values)
    

If [`WNOHANG`](https://docs.python.org/3/library/os.html#os.WNOHANG "os.WNOHANG")
 is specified and there are no matching children in the requested state, `None` is returned. Otherwise, if there are no matching children that could be waited for, [`ChildProcessError`](https://docs.python.org/3/builtins/exceptions.html#ChildProcessError "ChildProcessError")
 is raised.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

Added in version 3.3.

Changed in version 3.13: This function is now available on macOS as well.

os.waitpid(_pid_, _options_, _/_)[¶](https://docs.python.org/3/library/os.html#os.waitpid "Link to this definition")

The details of this function differ on Unix and Windows.

On Unix: Wait for completion of a child process given by process id _pid_, and return a tuple containing its process id and exit status indication (encoded as for [`wait()`](https://docs.python.org/3/library/os.html#os.wait "os.wait")
). The semantics of the call are affected by the value of the integer _options_, which should be `0` for normal operation.

If _pid_ is greater than `0`, `waitpid()` requests status information for that specific process. If _pid_ is `0`, the request is for the status of any child in the process group of the current process. If _pid_ is `-1`, the request pertains to any child of the current process. If _pid_ is less than `-1`, status is requested for any process in the process group `-pid` (the absolute value of _pid_).

_options_ is an OR combination of flags. If it contains [`WNOHANG`](https://docs.python.org/3/library/os.html#os.WNOHANG "os.WNOHANG")
 and there are no matching children in the requested state, `(0, 0)` is returned. Otherwise, if there are no matching children that could be waited for, [`ChildProcessError`](https://docs.python.org/3/builtins/exceptions.html#ChildProcessError "ChildProcessError")
 is raised. Other options that can be used are [`WUNTRACED`](https://docs.python.org/3/library/os.html#os.WUNTRACED "os.WUNTRACED")
 and [`WCONTINUED`](https://docs.python.org/3/library/os.html#os.WCONTINUED "os.WCONTINUED")
.

On Windows: Wait for completion of a process given by process handle _pid_, and return a tuple containing _pid_, and its exit status shifted left by 8 bits (shifting makes cross-platform use of the function easier). A _pid_ less than or equal to `0` has no special meaning on Windows, and raises an exception. The value of integer _options_ has no effect. _pid_ can refer to any process whose id is known, not necessarily a child process. The [`spawn*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl")
 functions called with [`P_NOWAIT`](https://docs.python.org/3/library/os.html#os.P_NOWAIT "os.P_NOWAIT")
 return suitable process handles.

[`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode")
 can be used to convert the exit status into an exit code.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI, not Android, not iOS.

Changed in version 3.5: If the system call is interrupted and the signal handler does not raise an exception, the function now retries the system call instead of raising an [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
 exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

os.wait3(_options_)[¶](https://docs.python.org/3/library/os.html#os.wait3 "Link to this definition")

Similar to [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
, except no process id argument is given and a 3-element tuple containing the child’s process id, exit status indication, and resource usage information is returned. Refer to [`resource.getrusage()`](https://docs.python.org/3/library/resource.html#resource.getrusage "resource.getrusage")
 for details on resource usage information. The _options_ argument is the same as that provided to `waitpid()` and [`wait4()`](https://docs.python.org/3/library/os.html#os.wait4 "os.wait4")
.

[`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode")
 can be used to convert the exit status into an exitcode.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.wait4(_pid_, _options_)[¶](https://docs.python.org/3/library/os.html#os.wait4 "Link to this definition")

Similar to [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
, except a 3-element tuple, containing the child’s process id, exit status indication, and resource usage information is returned. Refer to [`resource.getrusage()`](https://docs.python.org/3/library/resource.html#resource.getrusage "resource.getrusage")
 for details on resource usage information. The arguments to `wait4()` are the same as those provided to `waitpid()`.

[`waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode")
 can be used to convert the exit status into an exitcode.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.P\_PID[¶](https://docs.python.org/3/library/os.html#os.P_PID "Link to this definition")

os.P\_PGID[¶](https://docs.python.org/3/library/os.html#os.P_PGID "Link to this definition")

os.P\_ALL[¶](https://docs.python.org/3/library/os.html#os.P_ALL "Link to this definition")

os.P\_PIDFD[¶](https://docs.python.org/3/library/os.html#os.P_PIDFD "Link to this definition")

These are the possible values for _idtype_ in [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid")
. They affect how _id_ is interpreted:

*   `P_PID` - wait for the child whose PID is _id_.
    
*   `P_PGID` - wait for any child whose progress group ID is _id_.
    
*   `P_ALL` - wait for any child; _id_ is ignored.
    
*   `P_PIDFD` - wait for the child identified by the file descriptor _id_ (a process file descriptor created with [`pidfd_open()`](https://docs.python.org/3/library/os.html#os.pidfd_open "os.pidfd_open")
    ).
    

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

Note

`P_PIDFD` is only available on Linux >= 5.4.

Added in version 3.3.

Added in version 3.9: The `P_PIDFD` constant.

os.WCONTINUED[¶](https://docs.python.org/3/library/os.html#os.WCONTINUED "Link to this definition")

This _options_ flag for [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
, [`wait3()`](https://docs.python.org/3/library/os.html#os.wait3 "os.wait3")
, [`wait4()`](https://docs.python.org/3/library/os.html#os.wait4 "os.wait4")
, and [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid")
 causes child processes to be reported if they have been continued from a job control stop since they were last reported.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.WEXITED[¶](https://docs.python.org/3/library/os.html#os.WEXITED "Link to this definition")

This _options_ flag for [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid")
 causes child processes that have terminated to be reported.

The other `wait*` functions always report children that have terminated, so this option is not available for them.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

Added in version 3.3.

os.WSTOPPED[¶](https://docs.python.org/3/library/os.html#os.WSTOPPED "Link to this definition")

This _options_ flag for [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid")
 causes child processes that have been stopped by the delivery of a signal to be reported.

This option is not available for the other `wait*` functions.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

Added in version 3.3.

os.WUNTRACED[¶](https://docs.python.org/3/library/os.html#os.WUNTRACED "Link to this definition")

This _options_ flag for [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
, [`wait3()`](https://docs.python.org/3/library/os.html#os.wait3 "os.wait3")
, and [`wait4()`](https://docs.python.org/3/library/os.html#os.wait4 "os.wait4")
 causes child processes to also be reported if they have been stopped but their current state has not been reported since they were stopped.

This option is not available for [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.WNOHANG[¶](https://docs.python.org/3/library/os.html#os.WNOHANG "Link to this definition")

This _options_ flag causes [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
, [`wait3()`](https://docs.python.org/3/library/os.html#os.wait3 "os.wait3")
, [`wait4()`](https://docs.python.org/3/library/os.html#os.wait4 "os.wait4")
, and [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid")
 to return right away if no child process status is available immediately.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.WNOWAIT[¶](https://docs.python.org/3/library/os.html#os.WNOWAIT "Link to this definition")

This _options_ flag causes [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid")
 to leave the child in a waitable state, so that a later `wait*()` call can be used to retrieve the child status information again.

This option is not available for the other `wait*` functions.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.CLD\_EXITED[¶](https://docs.python.org/3/library/os.html#os.CLD_EXITED "Link to this definition")

os.CLD\_KILLED[¶](https://docs.python.org/3/library/os.html#os.CLD_KILLED "Link to this definition")

os.CLD\_DUMPED[¶](https://docs.python.org/3/library/os.html#os.CLD_DUMPED "Link to this definition")

os.CLD\_TRAPPED[¶](https://docs.python.org/3/library/os.html#os.CLD_TRAPPED "Link to this definition")

os.CLD\_STOPPED[¶](https://docs.python.org/3/library/os.html#os.CLD_STOPPED "Link to this definition")

os.CLD\_CONTINUED[¶](https://docs.python.org/3/library/os.html#os.CLD_CONTINUED "Link to this definition")

These are the possible values for `si_code` in the result returned by [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

Added in version 3.3.

Changed in version 3.9: Added `CLD_KILLED` and `CLD_STOPPED` values.

os.waitstatus\_to\_exitcode(_status_)[¶](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "Link to this definition")

Convert a wait status to an exit code.

On Unix:

*   If the process exited normally (if `WIFEXITED(status)` is true), return the process exit status (return `WEXITSTATUS(status)`): result greater than or equal to 0.
    
*   If the process was terminated by a signal (if `WIFSIGNALED(status)` is true), return `-signum` where _signum_ is the number of the signal that caused the process to terminate (return `-WTERMSIG(status)`): result less than 0.
    
*   Otherwise, raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
    .
    

On Windows, return _status_ shifted right by 8 bits.

On Unix, if the process is being traced or if [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
 was called with [`WUNTRACED`](https://docs.python.org/3/library/os.html#os.WUNTRACED "os.WUNTRACED")
 option, the caller must first check if `WIFSTOPPED(status)` is true. This function must not be called if `WIFSTOPPED(status)` is true.

See also

[`WIFEXITED()`](https://docs.python.org/3/library/os.html#os.WIFEXITED "os.WIFEXITED")
, [`WEXITSTATUS()`](https://docs.python.org/3/library/os.html#os.WEXITSTATUS "os.WEXITSTATUS")
, [`WIFSIGNALED()`](https://docs.python.org/3/library/os.html#os.WIFSIGNALED "os.WIFSIGNALED")
, [`WTERMSIG()`](https://docs.python.org/3/library/os.html#os.WTERMSIG "os.WTERMSIG")
, [`WIFSTOPPED()`](https://docs.python.org/3/library/os.html#os.WIFSTOPPED "os.WIFSTOPPED")
, [`WSTOPSIG()`](https://docs.python.org/3/library/os.html#os.WSTOPSIG "os.WSTOPSIG")
 functions.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows, not WASI, not Android, not iOS.

Added in version 3.9.

The following functions take a process status code as returned by [`system()`](https://docs.python.org/3/library/os.html#os.system "os.system")
, [`wait()`](https://docs.python.org/3/library/os.html#os.wait "os.wait")
, or [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
 as a parameter. They may be used to determine the disposition of a process.

os.WCOREDUMP(_status_, _/_)[¶](https://docs.python.org/3/library/os.html#os.WCOREDUMP "Link to this definition")

Return `True` if a core dump was generated for the process, otherwise return `False`.

This function should be employed only if [`WIFSIGNALED()`](https://docs.python.org/3/library/os.html#os.WIFSIGNALED "os.WIFSIGNALED")
 is true.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.WIFCONTINUED(_status_)[¶](https://docs.python.org/3/library/os.html#os.WIFCONTINUED "Link to this definition")

Return `True` if a stopped child has been resumed by delivery of [`SIGCONT`](https://docs.python.org/3/library/signal.html#signal.SIGCONT "signal.SIGCONT")
 (if the process has been continued from a job control stop), otherwise return `False`.

See [`WCONTINUED`](https://docs.python.org/3/library/os.html#os.WCONTINUED "os.WCONTINUED")
 option.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.WIFSTOPPED(_status_)[¶](https://docs.python.org/3/library/os.html#os.WIFSTOPPED "Link to this definition")

Return `True` if the process was stopped by delivery of a signal, otherwise return `False`.

`WIFSTOPPED()` only returns `True` if the [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
 call was done using [`WUNTRACED`](https://docs.python.org/3/library/os.html#os.WUNTRACED "os.WUNTRACED")
 option or when the process is being traced (see _[ptrace(2)](https://manpages.debian.org/ptrace(2))
_).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.WIFSIGNALED(_status_)[¶](https://docs.python.org/3/library/os.html#os.WIFSIGNALED "Link to this definition")

Return `True` if the process was terminated by a signal, otherwise return `False`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.WIFEXITED(_status_)[¶](https://docs.python.org/3/library/os.html#os.WIFEXITED "Link to this definition")

Return `True` if the process exited terminated normally, that is, by calling `exit()` or `_exit()`, or by returning from `main()`; otherwise return `False`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.WEXITSTATUS(_status_)[¶](https://docs.python.org/3/library/os.html#os.WEXITSTATUS "Link to this definition")

Return the process exit status.

This function should be employed only if [`WIFEXITED()`](https://docs.python.org/3/library/os.html#os.WIFEXITED "os.WIFEXITED")
 is true.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.WSTOPSIG(_status_)[¶](https://docs.python.org/3/library/os.html#os.WSTOPSIG "Link to this definition")

Return the signal which caused the process to stop.

This function should be employed only if [`WIFSTOPPED()`](https://docs.python.org/3/library/os.html#os.WIFSTOPPED "os.WIFSTOPPED")
 is true.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

os.WTERMSIG(_status_)[¶](https://docs.python.org/3/library/os.html#os.WTERMSIG "Link to this definition")

Return the number of the signal that caused the process to terminate.

This function should be employed only if [`WIFSIGNALED()`](https://docs.python.org/3/library/os.html#os.WIFSIGNALED "os.WIFSIGNALED")
 is true.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

Interface to the scheduler[¶](https://docs.python.org/3/library/os.html#interface-to-the-scheduler "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

These functions control how a process is allocated CPU time by the operating system. They are only available on some Unix platforms. For more detailed information, consult your Unix manpages.

Added in version 3.3.

The following scheduling policies are exposed if they are supported by the operating system.

os.SCHED\_OTHER[¶](https://docs.python.org/3/library/os.html#os.SCHED_OTHER "Link to this definition")

The default scheduling policy.

os.SCHED\_BATCH[¶](https://docs.python.org/3/library/os.html#os.SCHED_BATCH "Link to this definition")

Scheduling policy for CPU-intensive processes that tries to preserve interactivity on the rest of the computer.

os.SCHED\_DEADLINE[¶](https://docs.python.org/3/library/os.html#os.SCHED_DEADLINE "Link to this definition")

Scheduling policy for tasks with deadline constraints.

Added in version 3.14.

os.SCHED\_IDLE[¶](https://docs.python.org/3/library/os.html#os.SCHED_IDLE "Link to this definition")

Scheduling policy for extremely low priority background tasks.

os.SCHED\_NORMAL[¶](https://docs.python.org/3/library/os.html#os.SCHED_NORMAL "Link to this definition")

Alias for [`SCHED_OTHER`](https://docs.python.org/3/library/os.html#os.SCHED_OTHER "os.SCHED_OTHER")
.

Added in version 3.14.

os.SCHED\_SPORADIC[¶](https://docs.python.org/3/library/os.html#os.SCHED_SPORADIC "Link to this definition")

Scheduling policy for sporadic server programs.

os.SCHED\_FIFO[¶](https://docs.python.org/3/library/os.html#os.SCHED_FIFO "Link to this definition")

A First In First Out scheduling policy.

os.SCHED\_RR[¶](https://docs.python.org/3/library/os.html#os.SCHED_RR "Link to this definition")

A round-robin scheduling policy.

os.SCHED\_RESET\_ON\_FORK[¶](https://docs.python.org/3/library/os.html#os.SCHED_RESET_ON_FORK "Link to this definition")

This flag can be OR’ed with any other scheduling policy. When a process with this flag set forks, its child’s scheduling policy and priority are reset to the default.

class os.sched\_param(_sched\_priority_)[¶](https://docs.python.org/3/library/os.html#os.sched_param "Link to this definition")

This class represents tunable scheduling parameters used in [`sched_setparam()`](https://docs.python.org/3/library/os.html#os.sched_setparam "os.sched_setparam")
, [`sched_setscheduler()`](https://docs.python.org/3/library/os.html#os.sched_setscheduler "os.sched_setscheduler")
, and [`sched_getparam()`](https://docs.python.org/3/library/os.html#os.sched_getparam "os.sched_getparam")
. It is immutable.

At the moment, there is only one possible parameter:

sched\_priority[¶](https://docs.python.org/3/library/os.html#os.sched_param.sched_priority "Link to this definition")

The scheduling priority for a scheduling policy.

os.sched\_get\_priority\_min(_policy_)[¶](https://docs.python.org/3/library/os.html#os.sched_get_priority_min "Link to this definition")

Get the minimum priority value for _policy_. _policy_ is one of the scheduling policy constants above.

os.sched\_get\_priority\_max(_policy_)[¶](https://docs.python.org/3/library/os.html#os.sched_get_priority_max "Link to this definition")

Get the maximum priority value for _policy_. _policy_ is one of the scheduling policy constants above.

os.sched\_setscheduler(_pid_, _policy_, _param_, _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_setscheduler "Link to this definition")

Set the scheduling policy for the process with PID _pid_. A _pid_ of 0 means the calling process. _policy_ is one of the scheduling policy constants above. _param_ is a [`sched_param`](https://docs.python.org/3/library/os.html#os.sched_param "os.sched_param")
 instance.

os.sched\_getscheduler(_pid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_getscheduler "Link to this definition")

Return the scheduling policy for the process with PID _pid_. A _pid_ of 0 means the calling process. The result is one of the scheduling policy constants above.

os.sched\_setparam(_pid_, _param_, _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_setparam "Link to this definition")

Set the scheduling parameters for the process with PID _pid_. A _pid_ of 0 means the calling process. _param_ is a [`sched_param`](https://docs.python.org/3/library/os.html#os.sched_param "os.sched_param")
 instance.

os.sched\_getparam(_pid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_getparam "Link to this definition")

Return the scheduling parameters as a [`sched_param`](https://docs.python.org/3/library/os.html#os.sched_param "os.sched_param")
 instance for the process with PID _pid_. A _pid_ of 0 means the calling process.

os.sched\_rr\_get\_interval(_pid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_rr_get_interval "Link to this definition")

Return the round-robin quantum in seconds for the process with PID _pid_. A _pid_ of 0 means the calling process.

os.sched\_yield()[¶](https://docs.python.org/3/library/os.html#os.sched_yield "Link to this definition")

Voluntarily relinquish the CPU. See _[sched\_yield(2)](https://manpages.debian.org/sched_yield(2))
_ for details.

os.sched\_setaffinity(_pid_, _mask_, _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_setaffinity "Link to this definition")

Restrict the process with PID _pid_ (or the current process if zero) to a set of CPUs. _mask_ is an iterable of integers representing the set of CPUs to which the process should be restricted.

os.sched\_getaffinity(_pid_, _/_)[¶](https://docs.python.org/3/library/os.html#os.sched_getaffinity "Link to this definition")

Return the set of CPUs the process with PID _pid_ is restricted to.

If _pid_ is zero, return the set of CPUs the calling thread of the current process is restricted to.

See also the [`process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
 function.

Miscellaneous System Information[¶](https://docs.python.org/3/library/os.html#miscellaneous-system-information "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

os.confstr(_name_, _/_)[¶](https://docs.python.org/3/library/os.html#os.confstr "Link to this definition")

Return string-valued system configuration values. _name_ specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (POSIX, Unix 95, Unix 98, and others). Some platforms define additional names as well. The names known to the host operating system are given as the keys of the `confstr_names` dictionary. For configuration variables not included in that mapping, passing an integer for _name_ is also accepted.

If the configuration value specified by _name_ isn’t defined, `None` is returned.

If _name_ is a string and is not known, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. If a specific value for _name_ is not supported by the host system, even if it is included in `confstr_names`, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised with [`errno.EINVAL`](https://docs.python.org/3/library/errno.html#errno.EINVAL "errno.EINVAL")
 for the error number.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

os.confstr\_names[¶](https://docs.python.org/3/library/os.html#os.confstr_names "Link to this definition")

Dictionary mapping names accepted by [`confstr()`](https://docs.python.org/3/library/os.html#os.confstr "os.confstr")
 to the integer values defined for those names by the host operating system. This can be used to determine the set of names known to the system.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

os.cpu\_count()[¶](https://docs.python.org/3/library/os.html#os.cpu_count "Link to this definition")

Return the number of logical CPUs in the **system**. Returns `None` if undetermined.

The [`process_cpu_count()`](https://docs.python.org/3/library/os.html#os.process_cpu_count "os.process_cpu_count")
 function can be used to get the number of logical CPUs usable by the calling thread of the **current process**.

Added in version 3.4.

Changed in version 3.13: If [`-X cpu_count`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 is given or [`PYTHON_CPU_COUNT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT)
 is set, `cpu_count()` returns the override value _n_.

os.getloadavg()[¶](https://docs.python.org/3/library/os.html#os.getloadavg "Link to this definition")

Return the number of processes in the system run queue averaged over the last 1, 5, and 15 minutes or raises [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 if the load average was unobtainable.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

os.process\_cpu\_count()[¶](https://docs.python.org/3/library/os.html#os.process_cpu_count "Link to this definition")

Get the number of logical CPUs usable by the calling thread of the **current process**. Returns `None` if undetermined. It can be less than [`cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count")
 depending on the CPU affinity.

The [`cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count")
 function can be used to get the number of logical CPUs in the **system**.

If [`-X cpu_count`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 is given or [`PYTHON_CPU_COUNT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CPU_COUNT)
 is set, `process_cpu_count()` returns the override value _n_.

See also the [`sched_getaffinity()`](https://docs.python.org/3/library/os.html#os.sched_getaffinity "os.sched_getaffinity")
 function.

Added in version 3.13.

os.sysconf(_name_, _/_)[¶](https://docs.python.org/3/library/os.html#os.sysconf "Link to this definition")

Return integer-valued system configuration values. If the configuration value specified by _name_ isn’t defined, `-1` is returned. The comments regarding the _name_ parameter for [`confstr()`](https://docs.python.org/3/library/os.html#os.confstr "os.confstr")
 apply here as well; the dictionary that provides information on the known names is given by `sysconf_names`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

os.sysconf\_names[¶](https://docs.python.org/3/library/os.html#os.sysconf_names "Link to this definition")

Dictionary mapping names accepted by [`sysconf()`](https://docs.python.org/3/library/os.html#os.sysconf "os.sysconf")
 to the integer values defined for those names by the host operating system. This can be used to determine the set of names known to the system.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Changed in version 3.11: Add `'SC_MINSIGSTKSZ'` name.

The following data values are used to support path manipulation operations. These are defined for all platforms.

Higher-level operations on pathnames are defined in the [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
 module.

os.curdir[¶](https://docs.python.org/3/library/os.html#os.curdir "Link to this definition")

The constant string used by the operating system to refer to the current directory. This is `'.'` for Windows and POSIX. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
.

os.pardir[¶](https://docs.python.org/3/library/os.html#os.pardir "Link to this definition")

The constant string used by the operating system to refer to the parent directory. This is `'..'` for Windows and POSIX. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
.

os.sep[¶](https://docs.python.org/3/library/os.html#os.sep "Link to this definition")

The character used by the operating system to separate pathname components. This is `'/'` for POSIX and `'\\'` for Windows. Note that knowing this is not sufficient to be able to parse or concatenate pathnames — use [`os.path.split()`](https://docs.python.org/3/library/os.path.html#os.path.split "os.path.split")
 and [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join "os.path.join")
 — but it is occasionally useful. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
.

os.altsep[¶](https://docs.python.org/3/library/os.html#os.altsep "Link to this definition")

An alternative character used by the operating system to separate pathname components, or `None` if only one separator character exists. This is set to `'/'` on Windows systems where `sep` is a backslash. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
.

os.extsep[¶](https://docs.python.org/3/library/os.html#os.extsep "Link to this definition")

The character which separates the base filename from the extension; for example, the `'.'` in `os.py`. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
.

os.pathsep[¶](https://docs.python.org/3/library/os.html#os.pathsep "Link to this definition")

The character conventionally used by the operating system to separate search path components (as in `PATH`), such as `':'` for POSIX or `';'` for Windows. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
.

os.defpath[¶](https://docs.python.org/3/library/os.html#os.defpath "Link to this definition")

The default search path used by [`exec*p*`](https://docs.python.org/3/library/os.html#os.execl "os.execl")
 and [`spawn*p*`](https://docs.python.org/3/library/os.html#os.spawnl "os.spawnl")
 if the environment doesn’t have a `'PATH'` key. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
.

os.linesep[¶](https://docs.python.org/3/library/os.html#os.linesep "Link to this definition")

The string used to separate (or, rather, terminate) lines on the current platform. This may be a single character, such as `'\n'` for POSIX, or multiple characters, for example, `'\r\n'` for Windows. Do not use _os.linesep_ as a line terminator when writing files opened in text mode (the default); use a single `'\n'` instead, on all platforms.

os.devnull[¶](https://docs.python.org/3/library/os.html#os.devnull "Link to this definition")

The file path of the null device. For example: `'/dev/null'` for POSIX, `'nul'` for Windows. Also available via [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")
.

os.RTLD\_LAZY[¶](https://docs.python.org/3/library/os.html#os.RTLD_LAZY "Link to this definition")

os.RTLD\_NOW[¶](https://docs.python.org/3/library/os.html#os.RTLD_NOW "Link to this definition")

os.RTLD\_GLOBAL[¶](https://docs.python.org/3/library/os.html#os.RTLD_GLOBAL "Link to this definition")

os.RTLD\_LOCAL[¶](https://docs.python.org/3/library/os.html#os.RTLD_LOCAL "Link to this definition")

os.RTLD\_NODELETE[¶](https://docs.python.org/3/library/os.html#os.RTLD_NODELETE "Link to this definition")

os.RTLD\_NOLOAD[¶](https://docs.python.org/3/library/os.html#os.RTLD_NOLOAD "Link to this definition")

os.RTLD\_DEEPBIND[¶](https://docs.python.org/3/library/os.html#os.RTLD_DEEPBIND "Link to this definition")

Flags for use with the [`setdlopenflags()`](https://docs.python.org/3/library/sys.html#sys.setdlopenflags "sys.setdlopenflags")
 and [`getdlopenflags()`](https://docs.python.org/3/library/sys.html#sys.getdlopenflags "sys.getdlopenflags")
 functions. See the Unix manual page _[dlopen(3)](https://manpages.debian.org/dlopen(3))
_ for what the different flags mean.

Added in version 3.3.

Random numbers[¶](https://docs.python.org/3/library/os.html#random-numbers "Link to this heading")

---------------------------------------------------------------------------------------------------

os.getrandom(_size_, _flags\=0_)[¶](https://docs.python.org/3/library/os.html#os.getrandom "Link to this definition")

Get up to _size_ random bytes. The function can return less bytes than requested.

These bytes can be used to seed user-space random number generators or for cryptographic purposes.

`getrandom()` relies on entropy gathered from device drivers and other sources of environmental noise. Unnecessarily reading large quantities of data will have a negative impact on other users of the `/dev/random` and `/dev/urandom` devices.

The flags argument is a bit mask that can contain zero or more of the following values ORed together: [`os.GRND_RANDOM`](https://docs.python.org/3/library/os.html#os.GRND_RANDOM "os.GRND_RANDOM")
 and [`GRND_NONBLOCK`](https://docs.python.org/3/library/os.html#os.GRND_NONBLOCK "os.GRND_NONBLOCK")
.

See also the [Linux getrandom() manual page](https://man7.org/linux/man-pages/man2/getrandom.2.html)
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 3.17.

Added in version 3.6.

os.urandom(_size_, _/_)[¶](https://docs.python.org/3/library/os.html#os.urandom "Link to this definition")

Return a bytestring of _size_ random bytes suitable for cryptographic use.

This function returns random bytes from an OS-specific randomness source. The returned data should be unpredictable enough for cryptographic applications, though its exact quality depends on the OS implementation.

On Linux, if the `getrandom()` syscall is available, it is used in blocking mode: block until the system urandom entropy pool is initialized (128 bits of entropy are collected by the kernel). See the [**PEP 524**](https://peps.python.org/pep-0524/)
 for the rationale. On Linux, the [`getrandom()`](https://docs.python.org/3/library/os.html#os.getrandom "os.getrandom")
 function can be used to get random bytes in non-blocking mode (using the [`GRND_NONBLOCK`](https://docs.python.org/3/library/os.html#os.GRND_NONBLOCK "os.GRND_NONBLOCK")
 flag) or to poll until the system urandom entropy pool is initialized.

On a Unix-like system, random bytes are read from the `/dev/urandom` device. If the `/dev/urandom` device is not available or not readable, the [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
 exception is raised.

On Windows, it will use `BCryptGenRandom()`.

See also

The [`secrets`](https://docs.python.org/3/library/secrets.html#module-secrets "secrets: Generate secure random numbers for managing secrets.")
 module provides higher level functions. For an easy-to-use interface to the random number generator provided by your platform, please see [`random.SystemRandom`](https://docs.python.org/3/library/random.html#random.SystemRandom "random.SystemRandom")
.

Changed in version 3.5: On Linux 3.17 and newer, the `getrandom()` syscall is now used when available. On OpenBSD 5.6 and newer, the C `getentropy()` function is now used. These functions avoid the usage of an internal file descriptor.

Changed in version 3.5.2: On Linux, if the `getrandom()` syscall blocks (the urandom entropy pool is not initialized yet), fall back on reading `/dev/urandom`.

Changed in version 3.6: On Linux, `getrandom()` is now used in blocking mode to increase the security.

Changed in version 3.11: On Windows, `BCryptGenRandom()` is used instead of `CryptGenRandom()` which is deprecated.

os.GRND\_NONBLOCK[¶](https://docs.python.org/3/library/os.html#os.GRND_NONBLOCK "Link to this definition")

By default, when reading from `/dev/random`, [`getrandom()`](https://docs.python.org/3/library/os.html#os.getrandom "os.getrandom")
 blocks if no random bytes are available, and when reading from `/dev/urandom`, it blocks if the entropy pool has not yet been initialized.

If the `GRND_NONBLOCK` flag is set, then [`getrandom()`](https://docs.python.org/3/library/os.html#os.getrandom "os.getrandom")
 does not block in these cases, but instead immediately raises [`BlockingIOError`](https://docs.python.org/3/builtins/exceptions.html#BlockingIOError "BlockingIOError")
.

Added in version 3.6.

os.GRND\_RANDOM[¶](https://docs.python.org/3/library/os.html#os.GRND_RANDOM "Link to this definition")

If this bit is set, then random bytes are drawn from the `/dev/random` pool instead of the `/dev/urandom` pool.

Added in version 3.6.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html#)
    *   [File Names, Command Line Arguments, and Environment Variables](https://docs.python.org/3/library/os.html#file-names-command-line-arguments-and-environment-variables)
        
    *   [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#python-utf-8-mode)
        
    *   [Process Parameters](https://docs.python.org/3/library/os.html#process-parameters)
        
    *   [File Object Creation](https://docs.python.org/3/library/os.html#file-object-creation)
        
    *   [File Descriptor Operations](https://docs.python.org/3/library/os.html#file-descriptor-operations)
        *   [Querying the size of a terminal](https://docs.python.org/3/library/os.html#querying-the-size-of-a-terminal)
            
        *   [Inheritance of File Descriptors](https://docs.python.org/3/library/os.html#inheritance-of-file-descriptors)
            
    *   [Files and Directories](https://docs.python.org/3/library/os.html#files-and-directories)
        *   [Timer File Descriptors](https://docs.python.org/3/library/os.html#timer-file-descriptors)
            
        *   [Linux extended attributes](https://docs.python.org/3/library/os.html#linux-extended-attributes)
            
    *   [Process Management](https://docs.python.org/3/library/os.html#process-management)
        
    *   [Interface to the scheduler](https://docs.python.org/3/library/os.html#interface-to-the-scheduler)
        
    *   [Miscellaneous System Information](https://docs.python.org/3/library/os.html#miscellaneous-system-information)
        
    *   [Random numbers](https://docs.python.org/3/library/os.html#random-numbers)
        

#### Previous topic

[Generic Operating System Services](https://docs.python.org/3/library/allos.html "previous chapter")

#### Next topic

[`io` — Core tools for working with streams](https://docs.python.org/3/library/io.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=os+%E2%80%94+Miscellaneous+operating+system+interfaces&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fos.html&pagesource=library%2Fos.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/os.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/io.html "io — Core tools for working with streams")
     |
*   [previous](https://docs.python.org/3/library/allos.html "Generic Operating System Services")
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
*   [Generic Operating System Services](https://docs.python.org/3/library/allos.html)
     »
*   [`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
    
*    
    
    |
*   Theme Auto Light Dark |