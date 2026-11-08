### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/module.html "Module Objects")
     |
*   [previous](https://docs.python.org/3/c-api/code.html "Code Objects")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [File objects](https://docs.python.org/3/c-api/file.html)
    
*    
    
    |
*   Theme Auto Light Dark |

File objects[¶](https://docs.python.org/3/c-api/file.html#file-objects "Link to this heading")

===============================================================================================

These APIs are a minimal emulation of the Python 2 C API for built-in file objects, which used to rely on the buffered I/O (FILE\*) support from the C standard library. In Python 3, files and streams use the new [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
 module, which defines several layers over the low-level unbuffered I/O of the operating system. The functions described below are convenience C wrappers over these new APIs, and meant mostly for internal error reporting in the interpreter; third-party code is advised to access the `io` APIs instead.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFile\_FromFd(int fd, const char \*name, const char \*mode, int buffering, const char \*encoding, const char \*errors, const char \*newline, int closefd)[¶](https://docs.python.org/3/c-api/file.html#c.PyFile_FromFd "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a Python file object from the file descriptor of an already opened file _fd_. The arguments _name_, _encoding_, _errors_ and _newline_ can be `NULL` to use the defaults; _buffering_ can be _\-1_ to use the default. _name_ is ignored and kept for backward compatibility. Return `NULL` on failure. For a more comprehensive description of the arguments, please refer to the [`io.open()`](https://docs.python.org/3/library/io.html#io.open "io.open")
 function documentation.

Warning

Since Python streams have their own buffering layer, mixing them with OS-level file descriptors can produce various issues (such as unexpected ordering of data).

Changed in version 3.2: Ignore _name_ attribute.

int PyObject\_AsFileDescriptor([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/file.html#c.PyObject_AsFileDescriptor "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the file descriptor associated with _p_ as an int. If the object is an integer, its value is returned. If not, the object’s [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method is called if it exists; the method must return an integer, which is returned as the file descriptor value. Sets an exception and returns `-1` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFile\_GetLine([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, int n)[¶](https://docs.python.org/3/c-api/file.html#c.PyFile_GetLine "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Equivalent to `p.readline([n])`, this function reads one line from the object _p_. _p_ may be a file object or any object with a [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline")
 method. If _n_ is `0`, exactly one line is read, regardless of the length of the line. If _n_ is greater than `0`, no more than _n_ bytes will be read from the file; a partial line can be returned. In both cases, an empty string is returned if the end of the file is reached immediately. If _n_ is less than `0`, however, one line is read regardless of length, but [`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
 is raised if the end of the file is reached immediately.

char \*Py\_UniversalNewlineFgets(char \*buf, int n, FILE \*stream, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*fobj)[¶](https://docs.python.org/3/c-api/file.html#c.Py_UniversalNewlineFgets "Link to this definition")
  

Read a line from the C stream _stream_ into the buffer _buf_, like the C standard library function `fgets()`, but treating all of `\n`, `\r` and `\r\n` as line endings (see [universal newlines](https://docs.python.org/3/glossary.html#term-universal-newlines)
). Any `\r` or `\r\n` read from the stream is stored in _buf_ as a single `\n`.

At most `n - 1` characters are stored in _buf_; reading stops after a newline has been stored or when the end of the file is reached. The result is always null-terminated. _stream_ should be opened in binary mode, so that the C library does not perform its own newline translation.

Return _buf_ on success. Return `NULL` if no characters could be read, because _stream_ is at end of file, a read error occurred, or _n_ is less than 2. Like `fgets()`, this function does not distinguish between end of file and a read error, and it does not set an exception.

_fobj_ exists only for backward compatibility and must be `NULL`.

int PyFile\_SetOpenCodeHook([Py\_OpenCodeHookFunction](https://docs.python.org/3/c-api/file.html#c.Py_OpenCodeHookFunction "Py_OpenCodeHookFunction")
 handler)[¶](https://docs.python.org/3/c-api/file.html#c.PyFile_SetOpenCodeHook "Link to this definition")
  

Overrides the normal behavior of [`io.open_code()`](https://docs.python.org/3/library/io.html#io.open_code "io.open_code")
 to pass its parameter through the provided handler.

The _handler_ is a function of type:

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*Py\_OpenCodeHookFunction)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, void\*)[¶](https://docs.python.org/3/c-api/file.html#c.Py_OpenCodeHookFunction "Link to this definition")
  

Equivalent of [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*)(PyObject \*path, void \*userData), where _path_ is guaranteed to be [`PyUnicodeObject`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeObject "PyUnicodeObject")
.

The _userData_ pointer is passed into the hook function. Since hook functions may be called from different runtimes, this pointer should not refer directly to Python state.

As this hook is intentionally used during import, avoid importing new modules during its execution unless they are known to be frozen or available in `sys.modules`.

Once a hook has been set, it cannot be removed or replaced, and later calls to [`PyFile_SetOpenCodeHook()`](https://docs.python.org/3/c-api/file.html#c.PyFile_SetOpenCodeHook "PyFile_SetOpenCodeHook")
 will fail. On failure, the function returns -1 and sets an exception if the interpreter has been initialized.

This function is safe to call before [`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `setopencodehook` with no arguments.

Added in version 3.8.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFile\_OpenCodeObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*path)[¶](https://docs.python.org/3/c-api/file.html#c.PyFile_OpenCodeObject "Link to this definition")
  

Open _path_ with the mode `'rb'`. _path_ must be a Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object. The behavior of this function may be overridden by [`PyFile_SetOpenCodeHook()`](https://docs.python.org/3/c-api/file.html#c.PyFile_SetOpenCodeHook "PyFile_SetOpenCodeHook")
 to allow for some preprocessing of the text.

This is analogous to [`io.open_code()`](https://docs.python.org/3/library/io.html#io.open_code "io.open_code")
 in Python.

On success, this function returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to a Python file object. On failure, this function returns `NULL` with an exception set.

Added in version 3.8.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFile\_OpenCode(const char \*path)[¶](https://docs.python.org/3/c-api/file.html#c.PyFile_OpenCode "Link to this definition")
  

Similar to [`PyFile_OpenCodeObject()`](https://docs.python.org/3/c-api/file.html#c.PyFile_OpenCodeObject "PyFile_OpenCodeObject")
, but _path_ is a UTF-8 encoded const char\*.

Added in version 3.8.

int PyFile\_WriteObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, int flags)[¶](https://docs.python.org/3/c-api/file.html#c.PyFile_WriteObject "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Write object _obj_ to file object _p_. The only supported flag for _flags_ is [`Py_PRINT_RAW`](https://docs.python.org/3/c-api/object.html#c.Py_PRINT_RAW "Py_PRINT_RAW")
; if given, the [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 of the object is written instead of the [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
.

If _obj_ is `NULL`, write the string `"<NULL>"`.

Return `0` on success or `-1` on failure; the appropriate exception will be set.

int PyFile\_WriteString(const char \*s, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/file.html#c.PyFile_WriteString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Write string _s_ to file object _p_. Return `0` on success or `-1` on failure; the appropriate exception will be set.

Soft-deprecated API[¶](https://docs.python.org/3/c-api/file.html#soft-deprecated-api "Link to this heading")

-------------------------------------------------------------------------------------------------------------

These are APIs that were included in Python’s C API by mistake. They are documented solely for completeness; use other `PyFile*` APIs instead.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFile\_NewStdPrinter(int fd)[¶](https://docs.python.org/3/c-api/file.html#c.PyFile_NewStdPrinter "Link to this definition")
  

Use [`PyFile_FromFd()`](https://docs.python.org/3/c-api/file.html#c.PyFile_FromFd "PyFile_FromFd")
 with defaults (`fd, NULL, "w", -1, NULL, NULL, NULL, 0`) instead.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyStdPrinter\_Type[¶](https://docs.python.org/3/c-api/file.html#c.PyStdPrinter_Type "Link to this definition")
  

Type of file-like objects used internally at Python startup when [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
 is not yet available. Use Python [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 or [`PyFile_FromFd()`](https://docs.python.org/3/c-api/file.html#c.PyFile_FromFd "PyFile_FromFd")
 to create file objects instead.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

PY\_STDIOTEXTMODE[¶](https://docs.python.org/3/c-api/file.html#c.PY_STDIOTEXTMODE "Link to this definition")
  

The string literal `"b"`, used to open files in binary mode. Exposed for backwards compatibility only.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.2.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [File objects](https://docs.python.org/3/c-api/file.html#)
    *   [Soft-deprecated API](https://docs.python.org/3/c-api/file.html#soft-deprecated-api)
        

#### Previous topic

[Code Objects](https://docs.python.org/3/c-api/code.html "previous chapter")

#### Next topic

[Module Objects](https://docs.python.org/3/c-api/module.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=File+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Ffile.html&pagesource=c-api%2Ffile.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/file.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/module.html "Module Objects")
     |
*   [previous](https://docs.python.org/3/c-api/code.html "Code Objects")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [File objects](https://docs.python.org/3/c-api/file.html)
    
*    
    
    |
*   Theme Auto Light Dark |