### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/import.html "Importing Modules")
     |
*   [previous](https://docs.python.org/3/c-api/utilities.html "Utilities")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Operating System Utilities](https://docs.python.org/3/c-api/sys.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Operating System Utilities[¶](https://docs.python.org/3/c-api/sys.html#operating-system-utilities "Link to this heading")

==========================================================================================================================

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyOS\_FSPath([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*path)[¶](https://docs.python.org/3/c-api/sys.html#c.PyOS_FSPath "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.6._

Return the file system representation for _path_. If the object is a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object, then a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 is returned. If the object implements the [`os.PathLike`](https://docs.python.org/3/library/os.html#os.PathLike "os.PathLike")
 interface, then [`__fspath__()`](https://docs.python.org/3/library/os.html#os.PathLike.__fspath__ "os.PathLike.__fspath__")
 is returned as long as it is a `str` or `bytes` object. Otherwise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised and `NULL` is returned.

Added in version 3.6.

int Py\_FdIsInteractive(FILE \*fp, const char \*filename)[¶](https://docs.python.org/3/c-api/sys.html#c.Py_FdIsInteractive "Link to this definition")
  

Return true (nonzero) if the standard I/O file _fp_ with name _filename_ is deemed interactive. This is the case for files for which `isatty(fileno(fp))` is true. If the [`PyConfig.interactive`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.interactive "PyConfig.interactive")
 is non-zero, this function also returns true if the _filename_ pointer is `NULL` or if the name is equal to one of the strings `'<stdin>'` or `'???'`.

This function must not be called before Python is initialized.

void PyOS\_BeforeFork()[¶](https://docs.python.org/3/c-api/sys.html#c.PyOS_BeforeFork "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on platforms with fork() since version 3.7._

Function to prepare some internal state before a process fork. This should be called before calling `fork()` or any similar function that clones the current process. Only available on systems where `fork()` is defined.

Warning

The C `fork()` call should only be made from the [“main” thread](https://docs.python.org/3/c-api/threads.html#fork-and-threads)
 (of the [“main” interpreter](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
). The same is true for `PyOS_BeforeFork()`.

Added in version 3.7.

void PyOS\_AfterFork\_Parent()[¶](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Parent "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on platforms with fork() since version 3.7._

Function to update some internal state after a process fork. This should be called from the parent process after calling `fork()` or any similar function that clones the current process, regardless of whether process cloning was successful. Only available on systems where `fork()` is defined.

Warning

The C `fork()` call should only be made from the [“main” thread](https://docs.python.org/3/c-api/threads.html#fork-and-threads)
 (of the [“main” interpreter](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
). The same is true for `PyOS_AfterFork_Parent()`.

Added in version 3.7.

void PyOS\_AfterFork\_Child()[¶](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Child "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on platforms with fork() since version 3.7._

Function to update internal interpreter state after a process fork. This must be called from the child process after calling `fork()`, or any similar function that clones the current process, if there is any chance the process will call back into the Python interpreter. Only available on systems where `fork()` is defined.

Warning

The C `fork()` call should only be made from the [“main” thread](https://docs.python.org/3/c-api/threads.html#fork-and-threads)
 (of the [“main” interpreter](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
). The same is true for `PyOS_AfterFork_Child()`.

Added in version 3.7.

See also

[`os.register_at_fork()`](https://docs.python.org/3/library/os.html#os.register_at_fork "os.register_at_fork")
 allows registering custom Python functions to be called by [`PyOS_BeforeFork()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_BeforeFork "PyOS_BeforeFork")
, [`PyOS_AfterFork_Parent()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Parent "PyOS_AfterFork_Parent")
 and [`PyOS_AfterFork_Child()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Child "PyOS_AfterFork_Child")
.

void PyOS\_AfterFork()[¶](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on platforms with fork()._

Function to update some internal state after a process fork; this should be called in the new process if the Python interpreter will continue to be used. If a new executable is loaded into the new process, this function does not need to be called.

Deprecated since version 3.7: This function is superseded by [`PyOS_AfterFork_Child()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Child "PyOS_AfterFork_Child")
.

int PyOS\_CheckStack()[¶](https://docs.python.org/3/c-api/sys.html#c.PyOS_CheckStack "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on platforms with USE\_STACKCHECK since version 3.7._

Return true when the interpreter runs out of stack space. This is a reliable check, but is only available when `USE_STACKCHECK` is defined (currently on certain versions of Windows using the Microsoft Visual C++ compiler). `USE_STACKCHECK` will be defined automatically; you should never change the definition in your own code.

typedef void (\*PyOS\_sighandler\_t)(int)[¶](https://docs.python.org/3/c-api/sys.html#c.PyOS_sighandler_t "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyOS\_sighandler\_t](https://docs.python.org/3/c-api/sys.html#c.PyOS_sighandler_t "PyOS_sighandler_t")
 PyOS\_getsig(int i)[¶](https://docs.python.org/3/c-api/sys.html#c.PyOS_getsig "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the current signal handler for signal _i_. This is a thin wrapper around either `sigaction()` or `signal()`. Do not call those functions directly!

[PyOS\_sighandler\_t](https://docs.python.org/3/c-api/sys.html#c.PyOS_sighandler_t "PyOS_sighandler_t")
 PyOS\_setsig(int i, [PyOS\_sighandler\_t](https://docs.python.org/3/c-api/sys.html#c.PyOS_sighandler_t "PyOS_sighandler_t")
 h)[¶](https://docs.python.org/3/c-api/sys.html#c.PyOS_setsig "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the signal handler for signal _i_ to be _h_; return the old signal handler. This is a thin wrapper around either `sigaction()` or `signal()`. Do not call those functions directly!

int PyOS\_InterruptOccurred(void)[¶](https://docs.python.org/3/c-api/sys.html#c.PyOS_InterruptOccurred "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Check if a `SIGINT` signal has been received.

Returns `1` if a `SIGINT` has occurred and clears the signal flag, or `0` otherwise.

In most cases, you should prefer [`PyErr_CheckSignals()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_CheckSignals "PyErr_CheckSignals")
 over this function. `PyErr_CheckSignals()` invokes the appropriate signal handlers for all pending signals, allowing Python code to handle the signal properly. This function only detects `SIGINT` and does not invoke any Python signal handlers.

This function is async-signal-safe and this function cannot fail. The caller must hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

wchar\_t \*Py\_DecodeLocale(const char \*arg, size\_t \*size)[¶](https://docs.python.org/3/c-api/sys.html#c.Py_DecodeLocale "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Warning

This function should not be called directly: use the [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
 API with the [`PyConfig_SetBytesString()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_SetBytesString "PyConfig_SetBytesString")
 function which ensures that [Python is preinitialized](https://docs.python.org/3/c-api/init_config.html#c-preinit)
.

This function must not be called before [Python is preinitialized](https://docs.python.org/3/c-api/init_config.html#c-preinit)
 and so that the LC\_CTYPE locale is properly configured: see the [`Py_PreInitialize()`](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitialize "Py_PreInitialize")
 function.

Decode a byte string from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
. If the error handler is [surrogateescape error handler](https://docs.python.org/3/library/codecs.html#surrogateescape)
, undecodable bytes are decoded as characters in range U+DC80..U+DCFF; and if a byte sequence can be decoded as a surrogate character, the bytes are escaped using the surrogateescape error handler instead of decoding them.

Return a pointer to a newly allocated wide character string, use [`PyMem_RawFree()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawFree "PyMem_RawFree")
 to free the memory. If size is not `NULL`, write the number of wide characters excluding the null character into `*size`

Return `NULL` on decoding error or memory allocation error. If _size_ is not `NULL`, `*size` is set to `(size_t)-1` on memory error or set to `(size_t)-2` on decoding error.

The [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 are selected by [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read")
: see [`filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")
 and [`filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")
 members of [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
.

Decoding errors should never happen, unless there is a bug in the C library.

Use the [`Py_EncodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_EncodeLocale "Py_EncodeLocale")
 function to encode the character string back to a byte string.

See also

The [`PyUnicode_DecodeFSDefaultAndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeFSDefaultAndSize "PyUnicode_DecodeFSDefaultAndSize")
 and [`PyUnicode_DecodeLocaleAndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLocaleAndSize "PyUnicode_DecodeLocaleAndSize")
 functions.

Added in version 3.5.

Changed in version 3.7: The function now uses the UTF-8 encoding in the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
.

Changed in version 3.8: The function now uses the UTF-8 encoding on Windows if [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding "PyPreConfig.legacy_windows_fs_encoding")
 is zero;

char \*Py\_EncodeLocale(const wchar\_t \*text, size\_t \*error\_pos)[¶](https://docs.python.org/3/c-api/sys.html#c.Py_EncodeLocale "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Encode a wide character string to the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
. If the error handler is [surrogateescape error handler](https://docs.python.org/3/library/codecs.html#surrogateescape)
, surrogate characters in the range U+DC80..U+DCFF are converted to bytes 0x80..0xFF.

Return a pointer to a newly allocated byte string, use [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
 to free the memory. Return `NULL` on encoding error or memory allocation error.

If error\_pos is not `NULL`, `*error_pos` is set to `(size_t)-1` on success, or set to the index of the invalid character on encoding error.

The [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 are selected by [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read")
: see [`filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")
 and [`filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")
 members of [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
.

Use the [`Py_DecodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_DecodeLocale "Py_DecodeLocale")
 function to decode the bytes string back to a wide character string.

Warning

This function must not be called before [Python is preinitialized](https://docs.python.org/3/c-api/init_config.html#c-preinit)
 and so that the LC\_CTYPE locale is properly configured: see the [`Py_PreInitialize()`](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitialize "Py_PreInitialize")
 function.

See also

The [`PyUnicode_EncodeFSDefault()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeFSDefault "PyUnicode_EncodeFSDefault")
 and [`PyUnicode_EncodeLocale()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeLocale "PyUnicode_EncodeLocale")
 functions.

Added in version 3.5.

Changed in version 3.7: The function now uses the UTF-8 encoding in the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
.

Changed in version 3.8: The function now uses the UTF-8 encoding on Windows if [`PyPreConfig.legacy_windows_fs_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.legacy_windows_fs_encoding "PyPreConfig.legacy_windows_fs_encoding")
 is zero.

FILE \*Py\_fopen([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*path, const char \*mode)[¶](https://docs.python.org/3/c-api/sys.html#c.Py_fopen "Link to this definition")
  

Similar to `fopen()`, but _path_ is a Python object and an exception is set on error.

_path_ must be a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object, a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object, or a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

On success, return the new file pointer. On error, set an exception and return `NULL`.

The file must be closed by [`Py_fclose()`](https://docs.python.org/3/c-api/sys.html#c.Py_fclose "Py_fclose")
 rather than calling directly `fclose()`.

The file descriptor is created non-inheritable ([**PEP 446**](https://peps.python.org/pep-0446/)
).

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

Added in version 3.14.

int Py\_fclose(FILE \*file)[¶](https://docs.python.org/3/c-api/sys.html#c.Py_fclose "Link to this definition")
  

Close a file that was opened by [`Py_fopen()`](https://docs.python.org/3/c-api/sys.html#c.Py_fopen "Py_fopen")
.

On success, return `0`. On error, return `EOF` and `errno` is set to indicate the error. In either case, any further access (including another call to [`Py_fclose()`](https://docs.python.org/3/c-api/sys.html#c.Py_fclose "Py_fclose")
) to the stream results in undefined behavior.

Added in version 3.14.

System Functions[¶](https://docs.python.org/3/c-api/sys.html#system-functions "Link to this heading")

======================================================================================================

These are utility functions that make functionality from the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
 module accessible to C code. They all work with the current interpreter thread’s `sys` module’s dict, which is contained in the internal thread state structure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySys\_GetAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_GetAttr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Get the attribute _name_ of the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
 module. Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
. Raise [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 and return `NULL` if it does not exist or if the `sys` module cannot be found.

If the non-existing object should not be treated as a failure, you can use [`PySys_GetOptionalAttr()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetOptionalAttr "PySys_GetOptionalAttr")
 instead.

Added in version 3.15.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySys\_GetAttrString(const char \*name)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_GetAttrString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

This is the same as [`PySys_GetAttr()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetAttr "PySys_GetAttr")
, but _name_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

If the non-existing object should not be treated as a failure, you can use [`PySys_GetOptionalAttrString()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetOptionalAttrString "PySys_GetOptionalAttrString")
 instead.

Added in version 3.15.

int PySys\_GetOptionalAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_GetOptionalAttr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Variant of [`PySys_GetAttr()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetAttr "PySys_GetAttr")
 which doesn’t raise exception if the object does not exist.

*   Set _\*result_ to a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     to the object and return `1` if the object exists.
    
*   Set _\*result_ to `NULL` and return `0` without setting an exception if the object does not exist.
    
*   Set an exception, set _\*result_ to `NULL`, and return `-1`, if an error occurred.
    

Added in version 3.15.

int PySys\_GetOptionalAttrString(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_GetOptionalAttrString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

This is the same as [`PySys_GetOptionalAttr()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetOptionalAttr "PySys_GetOptionalAttr")
, but _name_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

Added in version 3.15.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySys\_GetObject(const char \*name)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_GetObject "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PySys_GetAttrString()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetAttrString "PySys_GetAttrString")
, but return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 and return `NULL` _without_ setting exception on failure.

Preserves exception that was set before the call.

int PySys\_SetObject(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*v)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_SetObject "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set _name_ in the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
 module to _v_ unless _v_ is `NULL`, in which case _name_ is deleted from the sys module. Returns `0` on success, `-1` on error.

void PySys\_WriteStdout(const char \*format, ...)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_WriteStdout "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Write the output string described by _format_ to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
. No exceptions are raised, even if truncation occurs (see below).

_format_ should limit the total size of the formatted output string to 1000 bytes or less – after 1000 bytes, the output string is truncated. In particular, this means that no unrestricted “%s” formats should occur; these should be limited using “%.<N>s” where <N> is a decimal number calculated so that <N> plus the maximum size of other formatted text does not exceed 1000 bytes. Also watch out for “%f”, which can print hundreds of digits for very large numbers.

If a problem occurs, or [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 is unset, the formatted message is written to the real (C level) _stdout_.

void PySys\_WriteStderr(const char \*format, ...)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_WriteStderr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

As [`PySys_WriteStdout()`](https://docs.python.org/3/c-api/sys.html#c.PySys_WriteStdout "PySys_WriteStdout")
, but write to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 or _stderr_ instead.

void PySys\_FormatStdout(const char \*format, ...)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_FormatStdout "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Function similar to PySys\_WriteStdout() but format the message using [`PyUnicode_FromFormatV()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormatV "PyUnicode_FromFormatV")
 and don’t truncate the message to an arbitrary length.

Added in version 3.2.

void PySys\_FormatStderr(const char \*format, ...)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_FormatStderr "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

As [`PySys_FormatStdout()`](https://docs.python.org/3/c-api/sys.html#c.PySys_FormatStdout "PySys_FormatStdout")
, but write to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 or _stderr_ instead.

Added in version 3.2.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySys\_GetXOptions()[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_GetXOptions "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return the current dictionary of [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 options, similarly to [`sys._xoptions`](https://docs.python.org/3/library/sys.html#sys._xoptions "sys._xoptions")
. On error, `NULL` is returned and an exception is set.

Added in version 3.2.

int PySys\_Audit(const char \*event, const char \*format, ...)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_Audit "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Raise an auditing event with any active hooks. Return zero for success and non-zero with an exception set on failure.

The _event_ string argument must not be _NULL_.

If any hooks have been added, _format_ and other arguments will be used to construct a tuple to pass. Apart from `N`, the same format characters as used in [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue")
 are available. If the built value is not a tuple, it will be added into a single-element tuple.

The `N` format option must not be used. It consumes a reference, but since there is no way to know whether arguments to this function will be consumed, using it may cause reference leaks.

Note that `#` format characters should always be treated as [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
, regardless of whether `PY_SSIZE_T_CLEAN` was defined.

[`sys.audit()`](https://docs.python.org/3/library/sys.html#sys.audit "sys.audit")
 performs the same function from Python code.

See also [`PySys_AuditTuple()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AuditTuple "PySys_AuditTuple")
.

Added in version 3.8.

Changed in version 3.8.2: Require [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 for `#` format characters. Previously, an unavoidable deprecation warning was raised.

int PySys\_AuditTuple(const char \*event, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_AuditTuple "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Similar to [`PySys_Audit()`](https://docs.python.org/3/c-api/sys.html#c.PySys_Audit "PySys_Audit")
, but pass arguments as a Python object. _args_ must be a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
. To pass no arguments, _args_ can be _NULL_.

Added in version 3.13.

int PySys\_AddAuditHook([Py\_AuditHookFunction](https://docs.python.org/3/c-api/sys.html#c.Py_AuditHookFunction "Py_AuditHookFunction")
 hook, void \*userData)[¶](https://docs.python.org/3/c-api/sys.html#c.PySys_AddAuditHook "Link to this definition")
  

Append the callable _hook_ to the list of active auditing hooks. Return zero on success and non-zero on failure. If the runtime has been initialized, also set an error on failure. Hooks added through this API are called for all interpreters created by the runtime.

The _userData_ pointer is passed into the hook function. Since hook functions may be called from different runtimes, this pointer should not refer directly to Python state.

This function is safe to call before [`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
. When called after runtime initialization, existing audit hooks are notified and may silently abort the operation by raising an error subclassed from [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
 (other errors will not be silenced).

The hook function is always called with an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 by the Python interpreter that raised the event.

See [**PEP 578**](https://peps.python.org/pep-0578/)
 for a detailed description of auditing. Functions in the runtime and standard library that raise events are listed in the [audit events table](https://docs.python.org/3/library/audit_events.html#audit-events)
. Details are in each function’s documentation.

If the interpreter is initialized, this function raises an auditing event `sys.addaudithook` with no arguments. If any existing hooks raise an exception derived from [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
, the new hook will not be added and the exception is cleared. As a result, callers cannot assume that their hook has been added unless they control all existing hooks.

typedef int (\*Py\_AuditHookFunction)(const char \*event, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args, void \*userData)[¶](https://docs.python.org/3/c-api/sys.html#c.Py_AuditHookFunction "Link to this definition")
  

The type of the hook function. _event_ is the C string event argument passed to [`PySys_Audit()`](https://docs.python.org/3/c-api/sys.html#c.PySys_Audit "PySys_Audit")
 or [`PySys_AuditTuple()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AuditTuple "PySys_AuditTuple")
. _args_ is guaranteed to be a [`PyTupleObject`](https://docs.python.org/3/c-api/tuple.html#c.PyTupleObject "PyTupleObject")
. _userData_ is the argument passed to PySys\_AddAuditHook().

Added in version 3.8.

Process Control[¶](https://docs.python.org/3/c-api/sys.html#process-control "Link to this heading")

====================================================================================================

void Py\_FatalError(const char \*message)[¶](https://docs.python.org/3/c-api/sys.html#c.Py_FatalError "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Print a fatal error message and kill the process. No cleanup is performed. This function should only be invoked when a condition is detected that would make it dangerous to continue using the Python interpreter; e.g., when the object administration appears to be corrupted. On Unix, the standard C library function `abort()` is called which will attempt to produce a `core` file.

The `Py_FatalError()` function is replaced with a macro which logs automatically the name of the current function, unless the `Py_LIMITED_API` macro is defined.

Changed in version 3.9: Log the function name automatically.

void Py\_Exit(int status)[¶](https://docs.python.org/3/c-api/sys.html#c.Py_Exit "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Exit the current process. This calls [`Py_FinalizeEx()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_FinalizeEx "Py_FinalizeEx")
 and then calls the standard C library function `exit(status)`. If `Py_FinalizeEx()` indicates an error, the exit status is set to 120.

Changed in version 3.6: Errors from finalization no longer ignored.

int Py\_AtExit(void (\*func)())[¶](https://docs.python.org/3/c-api/sys.html#c.Py_AtExit "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Register a cleanup function to be called by [`Py_FinalizeEx()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_FinalizeEx "Py_FinalizeEx")
. The cleanup function will be called with no arguments and should return no value. At most 32 cleanup functions can be registered. When the registration is successful, [`Py_AtExit()`](https://docs.python.org/3/c-api/sys.html#c.Py_AtExit "Py_AtExit")
 returns `0`; on failure, it returns `-1`. The cleanup function registered last is called first. Each cleanup function will be called at most once. Since Python’s internal finalization will have completed before the cleanup function, no Python APIs should be called by _func_.

See also

[`PyUnstable_AtExit()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PyUnstable_AtExit "PyUnstable_AtExit")
 for passing a `void *data` argument.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Operating System Utilities](https://docs.python.org/3/c-api/sys.html#)
    
*   [System Functions](https://docs.python.org/3/c-api/sys.html#system-functions)
    
*   [Process Control](https://docs.python.org/3/c-api/sys.html#process-control)
    

#### Previous topic

[Utilities](https://docs.python.org/3/c-api/utilities.html "previous chapter")

#### Next topic

[Importing Modules](https://docs.python.org/3/c-api/import.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Operating+System+Utilities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fsys.html&pagesource=c-api%2Fsys.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/sys.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/import.html "Importing Modules")
     |
*   [previous](https://docs.python.org/3/c-api/utilities.html "Utilities")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Operating System Utilities](https://docs.python.org/3/c-api/sys.html)
    
*    
    
    |
*   Theme Auto Light Dark |