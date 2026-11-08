### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/extension-modules.html "Defining extension modules")
     |
*   [previous](https://docs.python.org/3/c-api/refcounting.html "Reference Counting")
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
*   [Exception Handling](https://docs.python.org/3/c-api/exceptions.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Exception Handling[¶](https://docs.python.org/3/c-api/exceptions.html#exception-handling "Link to this heading")

=================================================================================================================

The functions described in this chapter will let you handle and raise Python exceptions. It is important to understand some of the basics of Python exception handling. It works somewhat like the POSIX `errno` variable: there is a global indicator (per thread) of the last error that occurred. Most C API functions don’t clear this on success, but will set it to indicate the cause of the error on failure. Most C API functions also return an error indicator, usually `NULL` if they are supposed to return a pointer, or `-1` if they return an integer (exception: the `PyArg_*` functions return `1` for success and `0` for failure).

Concretely, the error indicator consists of three object pointers: the exception’s type, the exception’s value, and the traceback object. Any of those pointers can be `NULL` if non-set (although some combinations are forbidden, for example you can’t have a non-`NULL` traceback if the exception type is `NULL`).

When a function must fail because some function it called failed, it generally doesn’t set the error indicator; the function it called already set it. It is responsible for either handling the error and clearing the exception or returning after cleaning up any resources it holds (such as object references or memory allocations); it should _not_ continue normally if it is not prepared to handle the error. If returning due to an error, it is important to indicate to the caller that an error has been set. If the error is not handled or carefully propagated, additional calls into the Python/C API may not behave as intended and may fail in mysterious ways.

Note

The error indicator is **not** the result of [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info")
. The former corresponds to an exception that is not yet caught (and is therefore still propagating), while the latter returns an exception after it is caught (and has therefore stopped propagating).

Printing and clearing[¶](https://docs.python.org/3/c-api/exceptions.html#printing-and-clearing "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

void PyErr\_Clear()[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Clear "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Clear the error indicator. If the error indicator is not set, there is no effect.

void PyErr\_PrintEx(int set\_sys\_last\_vars)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_PrintEx "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Print a standard traceback to `sys.stderr` and clear the error indicator. **Unless** the error is a `SystemExit`, in that case no traceback is printed and the Python process will exit with the error code specified by the `SystemExit` instance.

Call this function **only** when the error indicator is set. Otherwise it will cause a fatal error!

If _set\_sys\_last\_vars_ is nonzero, the variable [`sys.last_exc`](https://docs.python.org/3/library/sys.html#sys.last_exc "sys.last_exc")
 is set to the printed exception. For backwards compatibility, the deprecated variables [`sys.last_type`](https://docs.python.org/3/library/sys.html#sys.last_type "sys.last_type")
, [`sys.last_value`](https://docs.python.org/3/library/sys.html#sys.last_value "sys.last_value")
 and [`sys.last_traceback`](https://docs.python.org/3/library/sys.html#sys.last_traceback "sys.last_traceback")
 are also set to the type, value and traceback of this exception, respectively.

Changed in version 3.12: The setting of [`sys.last_exc`](https://docs.python.org/3/library/sys.html#sys.last_exc "sys.last_exc")
 was added.

void PyErr\_Print()[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Print "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Alias for `PyErr_PrintEx(1)`.

void PyErr\_WriteUnraisable([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WriteUnraisable "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Call [`sys.unraisablehook()`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook")
 using the current exception and _obj_ argument.

This utility function prints a warning message to `sys.stderr` when an exception has been set but it is impossible for the interpreter to actually raise the exception. It is used, for example, when an exception occurs in an [`__del__()`](https://docs.python.org/3/reference/datamodel.html#object.__del__ "object.__del__")
 method.

The function is called with a single argument _obj_ that identifies the context in which the unraisable exception occurred. If possible, the repr of _obj_ will be printed in the warning message. If _obj_ is `NULL`, only the traceback is printed.

An exception must be set when calling this function.

Changed in version 3.4: Print a traceback. Print only traceback if _obj_ is `NULL`.

Changed in version 3.8: Use [`sys.unraisablehook()`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook")
.

void PyErr\_FormatUnraisable(const char \*format, ...)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_FormatUnraisable "Link to this definition")
  

Similar to [`PyErr_WriteUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WriteUnraisable "PyErr_WriteUnraisable")
, but the _format_ and subsequent parameters help format the warning message; they have the same meaning and values as in [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
. `PyErr_WriteUnraisable(obj)` is roughly equivalent to `PyErr_FormatUnraisable("Exception ignored in: %R", obj)`. If _format_ is `NULL`, only the traceback is printed.

Added in version 3.13.

void PyErr\_DisplayException([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_DisplayException "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Print the standard traceback display of `exc` to `sys.stderr`, including chained exceptions and notes.

Added in version 3.12.

void PyErr\_Display([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*unused, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*tb)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Display "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Legacy variant of [`PyErr_DisplayException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_DisplayException "PyErr_DisplayException")
.

Print the exception _value_ with its traceback to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
. If _value_ has no traceback set, _tb_ is used as its traceback. The first argument is ignored.

If [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 is `None`, nothing is printed. If `sys.stderr` is not set, the exception is dumped to the C `stderr` stream instead.

Deprecated since version 3.12: Use [`PyErr_DisplayException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_DisplayException "PyErr_DisplayException")
 instead.

Raising exceptions[¶](https://docs.python.org/3/c-api/exceptions.html#raising-exceptions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

These functions help you set the current thread’s error indicator. For convenience, some of these functions will always return a `NULL` pointer for use in a `return` statement.

void PyErr\_SetString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, const char \*message)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the most common way to set the error indicator. The first argument specifies the exception type; it is normally one of the standard exceptions, e.g. [`PyExc_RuntimeError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_RuntimeError "PyExc_RuntimeError")
. You need not create a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to it (e.g. with [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "Py_INCREF")
). The second argument is an error message; it is decoded from `'utf-8'`.

void PyErr\_SetObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetObject "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is similar to [`PyErr_SetString()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetString "PyErr_SetString")
 but lets you specify an arbitrary Python object for the “value” of the exception.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_Format([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exception, const char \*format, ...)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Format "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function sets the error indicator and returns `NULL`. _exception_ should be a Python exception class. The _format_ and subsequent parameters help format the error message; they have the same meaning and values as in [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
. _format_ is an ASCII-encoded string.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_FormatV([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exception, const char \*format, va\_list vargs)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_FormatV "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

Same as [`PyErr_Format()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Format "PyErr_Format")
, but taking a `va_list` argument rather than a variable number of arguments.

Added in version 3.5.

void PyErr\_SetNone([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetNone "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is a shorthand for `PyErr_SetObject(type, Py_None)`.

int PyErr\_BadArgument()[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_BadArgument "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is a shorthand for `PyErr_SetString(PyExc_TypeError, message)`, where _message_ indicates that a built-in operation was invoked with an illegal argument. It is mostly for internal use.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_NoMemory()[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NoMemory "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is a shorthand for `PyErr_SetNone(PyExc_MemoryError)`; it returns `NULL` so an object allocation function can write `return PyErr_NoMemory();` when it runs out of memory.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetFromErrno([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrno "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is a convenience function to raise an exception when a C library function has returned an error and set the C variable `errno`. It constructs a tuple object whose first item is the integer `errno` value and whose second item is the corresponding error message (gotten from `strerror()`), and then calls `PyErr_SetObject(type, object)`. On Unix, when the `errno` value is `EINTR`, indicating an interrupted system call, this calls [`PyErr_CheckSignals()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_CheckSignals "PyErr_CheckSignals")
, and if that set the error indicator, leaves it set to that. The function always returns `NULL`, so a wrapper function around a system call can write `return PyErr_SetFromErrno(type);` when the system call returns an error.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetFromErrnoWithFilenameObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filenameObject)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrnoWithFilenameObject "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyErr_SetFromErrno()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrno "PyErr_SetFromErrno")
, with the additional behavior that if _filenameObject_ is not `NULL`, it is passed to the constructor of _type_ as a third parameter. In the case of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exception, this is used to define the `filename` attribute of the exception instance.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetFromErrnoWithFilenameObjects([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filenameObject, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filenameObject2)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrnoWithFilenameObjects "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Similar to [`PyErr_SetFromErrnoWithFilenameObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrnoWithFilenameObject "PyErr_SetFromErrnoWithFilenameObject")
, but takes a second filename object, for raising errors when a function that takes two filenames fails.

Added in version 3.4.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetFromErrnoWithFilename([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, const char \*filename)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrnoWithFilename "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyErr_SetFromErrnoWithFilenameObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrnoWithFilenameObject "PyErr_SetFromErrnoWithFilenameObject")
, but the filename is given as a C string. _filename_ is decoded from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetFromWindowsErr(int ierr)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromWindowsErr "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

This is a convenience function to raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
. If called with _ierr_ of `0`, the error code returned by a call to `GetLastError()` is used instead. It calls the Win32 function `FormatMessage()` to retrieve the Windows description of error code given by _ierr_ or `GetLastError()`, then it constructs a `OSError` object with the [`winerror`](https://docs.python.org/3/builtins/exceptions.html#OSError.winerror "OSError.winerror")
 attribute set to the error code, the [`strerror`](https://docs.python.org/3/builtins/exceptions.html#OSError.strerror "OSError.strerror")
 attribute set to the corresponding error message (gotten from `FormatMessage()`), and then calls `PyErr_SetObject(PyExc_OSError, object)`. This function always returns `NULL`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetExcFromWindowsErr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, int ierr)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErr "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

Similar to [`PyErr_SetFromWindowsErr()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromWindowsErr "PyErr_SetFromWindowsErr")
, with an additional parameter specifying the exception type to be raised.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetFromWindowsErrWithFilename(int ierr, const char \*filename)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromWindowsErrWithFilename "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

Similar to [`PyErr_SetFromWindowsErr()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromWindowsErr "PyErr_SetFromWindowsErr")
, with the additional behavior that if _filename_ is not `NULL`, it is decoded from the filesystem encoding ([`os.fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode")
) and passed to the constructor of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 as a third parameter to be used to define the `filename` attribute of the exception instance.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetExcFromWindowsErrWithFilenameObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, int ierr, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErrWithFilenameObject "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

Similar to [`PyErr_SetExcFromWindowsErr()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErr "PyErr_SetExcFromWindowsErr")
, with the additional behavior that if _filename_ is not `NULL`, it is passed to the constructor of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 as a third parameter to be used to define the `filename` attribute of the exception instance.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetExcFromWindowsErrWithFilenameObjects([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, int ierr, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename2)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErrWithFilenameObjects "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

Similar to [`PyErr_SetExcFromWindowsErrWithFilenameObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErrWithFilenameObject "PyErr_SetExcFromWindowsErrWithFilenameObject")
, but accepts a second filename object.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Added in version 3.4.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetExcFromWindowsErrWithFilename([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, int ierr, const char \*filename)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErrWithFilename "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 on Windows since version 3.7._

Similar to [`PyErr_SetFromWindowsErrWithFilename()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromWindowsErrWithFilename "PyErr_SetFromWindowsErrWithFilename")
, with an additional parameter specifying the exception type to be raised.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetImportError([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*msg, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*path)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetImportError "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

This is a convenience function to raise [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
. _msg_ will be set as the exception’s message string. _name_ and _path_, both of which can be `NULL`, will be set as the `ImportError`’s respective `name` and `path` attributes.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_SetImportErrorSubclass([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exception, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*msg, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*path)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetImportErrorSubclass "Link to this definition")
  

_Return value: Always NULL._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.6._

Much like [`PyErr_SetImportError()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetImportError "PyErr_SetImportError")
 but this function allows for specifying a subclass of [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
 to raise.

Added in version 3.6.

void PyErr\_SyntaxLocationObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename, int lineno, int col\_offset)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SyntaxLocationObject "Link to this definition")
  

Set file, line, and offset information for the current exception. If the current exception is not a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
, then it sets additional attributes, which make the exception printing subsystem think the exception is a `SyntaxError`.

Added in version 3.4.

void PyErr\_RangedSyntaxLocationObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename, int lineno, int col\_offset, int end\_lineno, int end\_col\_offset)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_RangedSyntaxLocationObject "Link to this definition")
  

Similar to [`PyErr_SyntaxLocationObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SyntaxLocationObject "PyErr_SyntaxLocationObject")
, but also sets the _end\_lineno_ and _end\_col\_offset_ information for the current exception.

Added in version 3.10.

void PyErr\_SyntaxLocationEx(const char \*filename, int lineno, int col\_offset)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SyntaxLocationEx "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Like [`PyErr_SyntaxLocationObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SyntaxLocationObject "PyErr_SyntaxLocationObject")
, but _filename_ is a byte string decoded from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

Added in version 3.2.

void PyErr\_SyntaxLocation(const char \*filename, int lineno)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SyntaxLocation "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Like [`PyErr_SyntaxLocationEx()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SyntaxLocationEx "PyErr_SyntaxLocationEx")
, but the _col\_offset_ parameter is omitted.

void PyErr\_BadInternalCall()[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_BadInternalCall "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is a shorthand for `PyErr_SetString(PyExc_SystemError, message)`, where _message_ indicates that an internal operation (e.g. a Python/C API function) was invoked with an illegal argument. It is mostly for internal use.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_ProgramTextObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename, int lineno)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_ProgramTextObject "Link to this definition")
  

Get the source line in _filename_ at line _lineno_. _filename_ should be a Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object.

On success, this function returns a Python string object with the found line. On failure, this function returns `NULL` without an exception set.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_ProgramText(const char \*filename, int lineno)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_ProgramText "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyErr_ProgramTextObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_ProgramTextObject "PyErr_ProgramTextObject")
, but _filename_ is a const char\*, which is decoded with the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
, instead of a Python object reference.

Issuing warnings[¶](https://docs.python.org/3/c-api/exceptions.html#issuing-warnings "Link to this heading")

-------------------------------------------------------------------------------------------------------------

Use these functions to issue warnings from C code. They mirror similar functions exported by the Python [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
 module. They normally print a warning message to _sys.stderr_; however, it is also possible that the user has specified that warnings are to be turned into errors, and in that case they will raise an exception. It is also possible that the functions raise an exception because of a problem with the warning machinery. The return value is `0` if no exception is raised, or `-1` if an exception is raised. (It is not possible to determine whether a warning message is actually printed, nor what the reason is for the exception; this is intentional.) If an exception is raised, the caller should do its normal exception handling (for example, [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 owned references and return an error value).

int PyErr\_WarnEx([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*category, const char \*message, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 stack\_level)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnEx "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Issue a warning message. The _category_ argument is a warning category (see below) or `NULL`; the _message_ argument is a UTF-8 encoded string. _stack\_level_ is a positive number giving a number of stack frames; the warning will be issued from the currently executing line of code in that stack frame. A _stack\_level_ of 1 is the function calling [`PyErr_WarnEx()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnEx "PyErr_WarnEx")
, 2 is the function above that, and so forth.

Warning categories must be subclasses of [`PyExc_Warning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_Warning "PyExc_Warning")
; `PyExc_Warning` is a subclass of [`PyExc_Exception`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_Exception "PyExc_Exception")
; the default warning category is [`PyExc_RuntimeWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_RuntimeWarning "PyExc_RuntimeWarning")
. The standard Python warning categories are available as global variables whose names are enumerated at [Warning types](https://docs.python.org/3/c-api/exceptions.html#standardwarningcategories)
.

For information about warning control, see the documentation for the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
 module and the [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W)
 option in the command line documentation. There is no C API for warning control.

int PyErr\_Warn([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*category, const char \*message)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Warn "Link to this definition")
  

Equivalent to [PyErr\_WarnEx](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnEx "PyErr_WarnEx")
([category](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Warn "category")
, [message](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Warn "message")
, 1).

int PyErr\_WarnExplicitObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*category, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*message, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename, int lineno, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*registry)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnExplicitObject "Link to this definition")
  

Issue a warning message with explicit control over all warning attributes. This is a straightforward wrapper around the Python function [`warnings.warn_explicit()`](https://docs.python.org/3/library/warnings.html#warnings.warn_explicit "warnings.warn_explicit")
; see there for more information. The _module_ and _registry_ arguments may be set to `NULL` to get the default effect described there.

Added in version 3.4.

int PyErr\_WarnExplicit([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*category, const char \*message, const char \*filename, int lineno, const char \*module, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*registry)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnExplicit "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyErr_WarnExplicitObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnExplicitObject "PyErr_WarnExplicitObject")
 except that _message_ and _module_ are UTF-8 encoded strings, and _filename_ is decoded from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

int PyErr\_WarnFormat([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*category, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 stack\_level, const char \*format, ...)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnFormat "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Function similar to [`PyErr_WarnEx()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnEx "PyErr_WarnEx")
, but uses [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
 to format the warning message. _format_ is an ASCII-encoded string.

Added in version 3.2.

int PyErr\_WarnExplicitFormat([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*category, const char \*filename, int lineno, const char \*module, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*registry, const char \*format, ...)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnExplicitFormat "Link to this definition")
  

Similar to [`PyErr_WarnExplicit()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnExplicit "PyErr_WarnExplicit")
, but uses [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
 to format the warning message. _format_ is an ASCII-encoded string.

Added in version 3.2.

int PyErr\_ResourceWarning([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*source, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 stack\_level, const char \*format, ...)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_ResourceWarning "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.6._

Function similar to [`PyErr_WarnFormat()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnFormat "PyErr_WarnFormat")
, but _category_ is [`ResourceWarning`](https://docs.python.org/3/builtins/exceptions.html#ResourceWarning "ResourceWarning")
 and it passes _source_ to `warnings.WarningMessage`.

Added in version 3.6.

Querying the error indicator[¶](https://docs.python.org/3/c-api/exceptions.html#querying-the-error-indicator "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_Occurred()[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Test whether the error indicator is set. If set, return the exception _type_ (the first argument to the last call to one of the `PyErr_Set*` functions or to [`PyErr_Restore()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Restore "PyErr_Restore")
). If not set, return `NULL`. You do not own a reference to the return value, so you do not need to [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 it.

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

Note

Do not compare the return value to a specific exception; use [`PyErr_ExceptionMatches()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_ExceptionMatches "PyErr_ExceptionMatches")
 instead, shown below. (The comparison could easily fail since the exception may be an instance instead of a class, in the case of a class exception, or it may be a subclass of the expected exception.)

int PyErr\_ExceptionMatches([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_ExceptionMatches "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Equivalent to `PyErr_GivenExceptionMatches(PyErr_Occurred(), exc)`. This should only be called when an exception is actually set; a memory access violation will occur if no exception has been raised.

int PyErr\_GivenExceptionMatches([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*given, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GivenExceptionMatches "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return true if the _given_ exception matches the exception type in _exc_. If _exc_ is a class object, this also returns true when _given_ is an instance of a subclass. If _exc_ is a tuple, all exception types in the tuple (and recursively in subtuples) are searched for a match.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_GetRaisedException(void)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Return the exception currently being raised, clearing the error indicator at the same time. Return `NULL` if the error indicator is not set.

This function is used by code that needs to catch exceptions, or code that needs to save and restore the error indicator temporarily.

For example:

{
   PyObject \*exc \= PyErr\_GetRaisedException();

   /\* ... code that might produce other errors ... \*/

   PyErr\_SetRaisedException(exc);
}

See also

[`PyErr_GetHandledException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetHandledException "PyErr_GetHandledException")
, to save the exception currently being handled.

Added in version 3.12.

void PyErr\_SetRaisedException([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetRaisedException "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Set _exc_ as the exception currently being raised, clearing the existing exception if one is set. If _exc_ is `NULL`, just clear the existing exception.

_exc_ must be a valid exception or `NULL`.

This call “[steals](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _exc_.

Added in version 3.12.

void PyErr\_Fetch([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*ptype, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*pvalue, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*ptraceback)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Fetch "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Deprecated since version 3.12: Use [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
 instead.

Retrieve the error indicator into three variables whose addresses are passed. If the error indicator is not set, set all three variables to `NULL`. If it is set, it will be cleared and you own a reference to each object retrieved. The value and traceback object may be `NULL` even when the type object is not.

Note

This function is normally only used by legacy code that needs to catch exceptions or save and restore the error indicator temporarily.

For example:

{
   PyObject \*type, \*value, \*traceback;
   PyErr\_Fetch(&type, &value, &traceback);

   /\* ... code that might produce other errors ... \*/

   PyErr\_Restore(type, value, traceback);
}

void PyErr\_Restore([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*traceback)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Restore "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Deprecated since version 3.12: Use [`PyErr_SetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetRaisedException "PyErr_SetRaisedException")
 instead.

Set the error indicator from the three objects, _type_, _value_, and _traceback_, clearing the existing exception if one is set. If the objects are `NULL`, the error indicator is cleared. Do not pass a `NULL` type and non-`NULL` value or traceback. The exception type should be a class. Do not pass an invalid exception type or value. (Violating these rules will cause subtle problems later.) This call takes away a reference to each object: you must own a reference to each object before the call and after the call you no longer own these references. (If you don’t understand this, don’t use this function. I warned you.)

Note

This function is normally only used by legacy code that needs to save and restore the error indicator temporarily. Use [`PyErr_Fetch()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Fetch "PyErr_Fetch")
 to save the current error indicator.

void PyErr\_NormalizeException([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*exc, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*val, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*tb)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NormalizeException "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Deprecated since version 3.12: Use [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
 instead, to avoid any possible de-normalization.

Under certain circumstances, the values returned by [`PyErr_Fetch()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Fetch "PyErr_Fetch")
 below can be “unnormalized”, meaning that `*exc` is a class object but `*val` is not an instance of the same class. This function can be used to instantiate the class in that case. If the values are already normalized, nothing happens. The delayed normalization is implemented to improve performance.

Note

This function _does not_ implicitly set the [`__traceback__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__")
 attribute on the exception value. If setting the traceback appropriately is desired, the following additional snippet is needed:

if (tb != NULL) {
  PyException\_SetTraceback(val, tb);
}

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_GetHandledException(void)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetHandledException "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Retrieve the active exception instance, as would be returned by [`sys.exception()`](https://docs.python.org/3/library/sys.html#sys.exception "sys.exception")
. This refers to an exception that was _already caught_, not to an exception that was freshly raised. Returns a new reference to the exception or `NULL`. Does not modify the interpreter’s exception state.

Note

This function is not normally used by code that wants to handle exceptions. Rather, it can be used when code needs to save and restore the exception state temporarily. Use [`PyErr_SetHandledException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetHandledException "PyErr_SetHandledException")
 to restore or clear the exception state.

Added in version 3.11.

void PyErr\_SetHandledException([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetHandledException "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Set the active exception, as known from `sys.exception()`. This refers to an exception that was _already caught_, not to an exception that was freshly raised. To clear the exception state, pass `NULL`.

Note

This function is not normally used by code that wants to handle exceptions. Rather, it can be used when code needs to save and restore the exception state temporarily. Use [`PyErr_GetHandledException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetHandledException "PyErr_GetHandledException")
 to get the exception state.

Added in version 3.11.

void PyErr\_GetExcInfo([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*ptype, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*pvalue, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*ptraceback)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetExcInfo "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Retrieve the old-style representation of the exception info, as known from [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info")
. This refers to an exception that was _already caught_, not to an exception that was freshly raised. Returns new references for the three objects, any of which may be `NULL`. Does not modify the exception info state. This function is kept for backwards compatibility. Prefer using [`PyErr_GetHandledException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetHandledException "PyErr_GetHandledException")
.

Note

This function is not normally used by code that wants to handle exceptions. Rather, it can be used when code needs to save and restore the exception state temporarily. Use [`PyErr_SetExcInfo()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcInfo "PyErr_SetExcInfo")
 to restore or clear the exception state.

Added in version 3.3.

void PyErr\_SetExcInfo([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*traceback)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcInfo "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Set the exception info, as known from `sys.exc_info()`. This refers to an exception that was _already caught_, not to an exception that was freshly raised. This function “[steals](https://docs.python.org/3/glossary.html#term-steal)
” the references of the arguments. To clear the exception state, pass `NULL` for all three arguments. This function is kept for backwards compatibility. Prefer using [`PyErr_SetHandledException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetHandledException "PyErr_SetHandledException")
.

Note

This function is not normally used by code that wants to handle exceptions. Rather, it can be used when code needs to save and restore the exception state temporarily. Use [`PyErr_GetExcInfo()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetExcInfo "PyErr_GetExcInfo")
 to read the exception state.

Added in version 3.3.

Changed in version 3.11: The `type` and `traceback` arguments are no longer used and can be NULL. The interpreter now derives them from the exception instance (the `value` argument). The function still “[steals](https://docs.python.org/3/glossary.html#term-steal)
” references of all three arguments.

Signal Handling[¶](https://docs.python.org/3/c-api/exceptions.html#signal-handling "Link to this heading")

-----------------------------------------------------------------------------------------------------------

int PyErr\_CheckSignals()[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_CheckSignals "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Handle external interruptions, such as signals or activating a debugger, whose processing has been delayed until it is safe to run Python code and/or raise exceptions.

For example, pressing Ctrl\-C causes a terminal to send the [`signal.SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT")
 signal. This function executes the corresponding Python signal handler, which, by default, raises the [`KeyboardInterrupt`](https://docs.python.org/3/builtins/exceptions.html#KeyboardInterrupt "KeyboardInterrupt")
 exception.

`PyErr_CheckSignals()` should be called by long-running C code frequently enough so that the response appears immediate to humans.

Handlers invoked by this function currently include:

*   Signal handlers, including Python functions registered using the [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")
     module.
    
    Signal handlers are only run in the main thread of the main interpreter.
    
    (This is where the function got the name: originally, signals were the only way to interrupt the interpreter.)
    
*   Running the garbage collector, if necessary.
    
*   Executing a pending [remote debugger](https://docs.python.org/3/howto/remote_debugging.html#remote-debugging)
     script.
    
*   Raise the exception set by [`PyThreadState_SetAsyncExc()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_SetAsyncExc "PyThreadState_SetAsyncExc")
    .
    

If any handler raises an exception, immediately return `-1` with that exception set. Any remaining interruptions are left to be processed on the next [`PyErr_CheckSignals()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_CheckSignals "PyErr_CheckSignals")
 invocation, if appropriate.

If all handlers finish successfully, or there are no handlers to run, return `0`.

Changed in version 3.12: This function may now invoke the garbage collector.

Changed in version 3.14: This function may now execute a remote debugger script, if remote debugging is enabled.

Changed in version 3.15: The exception set by [`PyThreadState_SetAsyncExc()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_SetAsyncExc "PyThreadState_SetAsyncExc")
 is now raised.

void PyErr\_SetInterrupt()[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetInterrupt "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Simulate the effect of a `SIGINT` signal arriving. This is equivalent to `PyErr_SetInterruptEx(SIGINT)`.

Note

This function is async-signal-safe. It can be called without an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 and from a C signal handler.

int PyErr\_SetInterruptEx(int signum)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetInterruptEx "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Simulate the effect of a signal arriving. The next time [`PyErr_CheckSignals()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_CheckSignals "PyErr_CheckSignals")
 is called, the Python signal handler for the given signal number will be called.

This function can be called by C code that sets up its own signal handling and wants Python signal handlers to be invoked as expected when an interruption is requested (for example when the user presses Ctrl-C to interrupt an operation).

If the given signal isn’t handled by Python (it was set to [`signal.SIG_DFL`](https://docs.python.org/3/library/signal.html#signal.SIG_DFL "signal.SIG_DFL")
 or [`signal.SIG_IGN`](https://docs.python.org/3/library/signal.html#signal.SIG_IGN "signal.SIG_IGN")
), it will be ignored.

If _signum_ is outside of the allowed range of signal numbers, `-1` is returned. Otherwise, `0` is returned. The error indicator is never changed by this function.

Note

This function is async-signal-safe. It can be called without an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 and from a C signal handler.

Added in version 3.10.

int PySignal\_SetWakeupFd(int fd)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PySignal_SetWakeupFd "Link to this definition")
  

This utility function specifies a file descriptor to which the signal number is written as a single byte whenever a signal is received. _fd_ must be non-blocking. It returns the previous such file descriptor.

The value `-1` disables the feature; this is the initial state. This is equivalent to [`signal.set_wakeup_fd()`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "signal.set_wakeup_fd")
 in Python, but without any error checking. _fd_ should be a valid file descriptor. The function should only be called from the main thread.

Changed in version 3.5: On Windows, the function now also supports socket handles.

Exception Classes[¶](https://docs.python.org/3/c-api/exceptions.html#exception-classes "Link to this heading")

---------------------------------------------------------------------------------------------------------------

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_NewException(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*base, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*dict)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NewException "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This utility function creates and returns a new exception class. The _name_ argument must be the name of the new exception, a C string of the form `module.classname`. The _base_ and _dict_ arguments are normally `NULL`. This creates a class object derived from [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
 (accessible in C as [`PyExc_Exception`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_Exception "PyExc_Exception")
).

The [`__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__")
 attribute of the new class is set to the first part (up to the last dot) of the _name_ argument, and the class name is set to the last part (after the last dot). The _base_ argument can be used to specify alternate base classes; it can either be only one class or a tuple of classes. The _dict_ argument can be used to specify a dictionary of class variables and methods.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyErr\_NewExceptionWithDoc(const char \*name, const char \*doc, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*base, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*dict)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NewExceptionWithDoc "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Same as [`PyErr_NewException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NewException "PyErr_NewException")
, except that the new exception class can easily be given a docstring: If _doc_ is non-`NULL`, it will be used as the docstring for the exception class.

Added in version 3.2.

int PyExceptionClass\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExceptionClass_Check "Link to this definition")
  

Return non-zero if _ob_ is an exception class, zero otherwise. This function always succeeds.

const char \*PyExceptionClass\_Name([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExceptionClass_Name "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.8._

Return [`tp_name`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_name "PyTypeObject.tp_name")
 of the exception class _ob_.

PyException\_HEAD[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyException_HEAD "Link to this definition")
  

This is a macro including the base fields for an exception object.

This was included in Python’s C API by mistake and is not designed for use in extensions. For creating custom exception objects, use [`PyErr_NewException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NewException "PyErr_NewException")
 or otherwise create a class inheriting from [`PyExc_BaseException`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BaseException "PyExc_BaseException")
.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

Exception Objects[¶](https://docs.python.org/3/c-api/exceptions.html#exception-objects "Link to this heading")

---------------------------------------------------------------------------------------------------------------

int PyExceptionInstance\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExceptionInstance_Check "Link to this definition")
  

Return true if _op_ is an instance of [`BaseException`](https://docs.python.org/3/builtins/exceptions.html#BaseException "BaseException")
, false otherwise. This function always succeeds.

PyExceptionInstance\_Class(op)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExceptionInstance_Class "Link to this definition")
  

Equivalent to [`Py_TYPE(op)`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyException\_GetTraceback([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ex)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyException_GetTraceback "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the traceback associated with the exception as a new reference, as accessible from Python through the [`__traceback__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__")
 attribute. If there is no traceback associated, this returns `NULL`.

int PyException\_SetTraceback([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ex, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*tb)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyException_SetTraceback "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the traceback associated with the exception to _tb_. Use `Py_None` to clear it.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyException\_GetContext([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ex)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyException_GetContext "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the context (another exception instance during whose handling _ex_ was raised) associated with the exception as a new reference, as accessible from Python through the [`__context__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__context__ "BaseException.__context__")
 attribute. If there is no context associated, this returns `NULL`.

void PyException\_SetContext([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ex, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ctx)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyException_SetContext "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the context associated with the exception to _ctx_. Use `NULL` to clear it. There is no type check to make sure that _ctx_ is an exception instance. This “[steals](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _ctx_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyException\_GetCause([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ex)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyException_GetCause "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the cause (either an exception instance, or `None`, set by `raise ... from ...`) associated with the exception as a new reference, as accessible from Python through the [`__cause__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__cause__ "BaseException.__cause__")
 attribute.

void PyException\_SetCause([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ex, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*cause)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyException_SetCause "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the cause associated with the exception to _cause_. Use `NULL` to clear it. There is no type check to make sure that _cause_ is either an exception instance or `None`. This “[steals](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _cause_.

The [`__suppress_context__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__suppress_context__ "BaseException.__suppress_context__")
 attribute is implicitly set to `True` by this function.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyException\_GetArgs([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ex)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyException_GetArgs "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Return [`args`](https://docs.python.org/3/builtins/exceptions.html#BaseException.args "BaseException.args")
 of exception _ex_.

void PyException\_SetArgs([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ex, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyException_SetArgs "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Set [`args`](https://docs.python.org/3/builtins/exceptions.html#BaseException.args "BaseException.args")
 of exception _ex_ to _args_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnstable\_Exc\_PrepReraiseStar([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*orig, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*excs)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnstable_Exc_PrepReraiseStar "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Implement part of the interpreter’s implementation of `except*`. _orig_ is the original exception that was caught, and _excs_ is the list of the exceptions that need to be raised. This list contains the unhandled part of _orig_, if any, as well as the exceptions that were raised from the `except*` clauses (so they have a different traceback from _orig_) and those that were reraised (and have the same traceback as _orig_). Return the [`ExceptionGroup`](https://docs.python.org/3/builtins/exceptions.html#ExceptionGroup "ExceptionGroup")
 that needs to be reraised in the end, or `None` if there is nothing to reraise.

Added in version 3.12.

Unicode Exception Objects[¶](https://docs.python.org/3/c-api/exceptions.html#unicode-exception-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

The following functions are used to create and modify Unicode exceptions from C.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicodeDecodeError\_Create(const char \*encoding, const char \*object, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 end, const char \*reason)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_Create "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a [`UnicodeDecodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeDecodeError "UnicodeDecodeError")
 object with the attributes _encoding_, _object_, _length_, _start_, _end_ and _reason_. _encoding_ and _reason_ are UTF-8 encoded strings.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicodeDecodeError\_GetEncoding([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_GetEncoding "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicodeEncodeError\_GetEncoding([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_GetEncoding "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the _encoding_ attribute of the given exception object.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicodeDecodeError\_GetObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_GetObject "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicodeEncodeError\_GetObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_GetObject "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicodeTranslateError\_GetObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_GetObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the _object_ attribute of the given exception object.

int PyUnicodeDecodeError\_GetStart([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*start)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_GetStart "Link to this definition")
  

int PyUnicodeEncodeError\_GetStart([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*start)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_GetStart "Link to this definition")
  

int PyUnicodeTranslateError\_GetStart([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*start)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_GetStart "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get the _start_ attribute of the given exception object and place it into _\*start_. _start_ must not be `NULL`. Return `0` on success, `-1` on failure.

If the [`UnicodeError.object`](https://docs.python.org/3/builtins/exceptions.html#UnicodeError.object "UnicodeError.object")
 is an empty sequence, the resulting _start_ is `0`. Otherwise, it is clipped to `[0, len(object) - 1]`.

See also

[`UnicodeError.start`](https://docs.python.org/3/builtins/exceptions.html#UnicodeError.start "UnicodeError.start")

int PyUnicodeDecodeError\_SetStart([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_SetStart "Link to this definition")
  

int PyUnicodeEncodeError\_SetStart([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_SetStart "Link to this definition")
  

int PyUnicodeTranslateError\_SetStart([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 start)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_SetStart "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the _start_ attribute of the given exception object to _start_. Return `0` on success, `-1` on failure.

Note

While passing a negative _start_ does not raise an exception, the corresponding getters will not consider it as a relative offset.

int PyUnicodeDecodeError\_GetEnd([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*end)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_GetEnd "Link to this definition")
  

int PyUnicodeEncodeError\_GetEnd([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*end)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_GetEnd "Link to this definition")
  

int PyUnicodeTranslateError\_GetEnd([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*end)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_GetEnd "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get the _end_ attribute of the given exception object and place it into _\*end_. _end_ must not be `NULL`. Return `0` on success, `-1` on failure.

If the [`UnicodeError.object`](https://docs.python.org/3/builtins/exceptions.html#UnicodeError.object "UnicodeError.object")
 is an empty sequence, the resulting _end_ is `0`. Otherwise, it is clipped to `[1, len(object)]`.

int PyUnicodeDecodeError\_SetEnd([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 end)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_SetEnd "Link to this definition")
  

int PyUnicodeEncodeError\_SetEnd([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 end)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_SetEnd "Link to this definition")
  

int PyUnicodeTranslateError\_SetEnd([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 end)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_SetEnd "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the _end_ attribute of the given exception object to _end_. Return `0` on success, `-1` on failure.

See also

[`UnicodeError.end`](https://docs.python.org/3/builtins/exceptions.html#UnicodeError.end "UnicodeError.end")

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicodeDecodeError\_GetReason([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_GetReason "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicodeEncodeError\_GetReason([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_GetReason "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnicodeTranslateError\_GetReason([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_GetReason "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the _reason_ attribute of the given exception object.

int PyUnicodeDecodeError\_SetReason([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, const char \*reason)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_SetReason "Link to this definition")
  

int PyUnicodeEncodeError\_SetReason([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, const char \*reason)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_SetReason "Link to this definition")
  

int PyUnicodeTranslateError\_SetReason([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exc, const char \*reason)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_SetReason "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the _reason_ attribute of the given exception object to _reason_. Return `0` on success, `-1` on failure.

Recursion Control[¶](https://docs.python.org/3/c-api/exceptions.html#recursion-control "Link to this heading")

---------------------------------------------------------------------------------------------------------------

These two functions provide a way to perform safe recursive calls at the C level, both in the core and in extension modules. They are needed if the recursive code does not necessarily invoke Python code (which tracks its recursion depth automatically). They are also not needed for _tp\_call_ implementations because the [call protocol](https://docs.python.org/3/c-api/call.html#call)
 takes care of recursion handling.

int Py\_EnterRecursiveCall(const char \*where)[¶](https://docs.python.org/3/c-api/exceptions.html#c.Py_EnterRecursiveCall "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.9._

Marks a point where a recursive C-level call is about to be performed.

The function then checks if the stack limit is reached. If this is the case, a [`RecursionError`](https://docs.python.org/3/builtins/exceptions.html#RecursionError "RecursionError")
 is set and a nonzero value is returned. Otherwise, zero is returned.

The check is based on the remaining C stack space of the current thread, not on a count of calls, so it is unaffected by [`Py_SetRecursionLimit()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_SetRecursionLimit "Py_SetRecursionLimit")
 and [`sys.setrecursionlimit()`](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit "sys.setrecursionlimit")
.

_where_ should be a UTF-8 encoded string such as `" in instance check"` to be concatenated to the [`RecursionError`](https://docs.python.org/3/builtins/exceptions.html#RecursionError "RecursionError")
 message caused by the recursion depth limit.

See also

The [`PyUnstable_ThreadState_SetStackProtection()`](https://docs.python.org/3/c-api/threads.html#c.PyUnstable_ThreadState_SetStackProtection "PyUnstable_ThreadState_SetStackProtection")
 function.

Changed in version 3.9: This function is now also available in the [limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
.

Changed in version 3.14: The check is based on the remaining C stack space. Previously, a separate counter of C-level calls was used.

void Py\_LeaveRecursiveCall(void)[¶](https://docs.python.org/3/c-api/exceptions.html#c.Py_LeaveRecursiveCall "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.9._

Ends a [`Py_EnterRecursiveCall()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_EnterRecursiveCall "Py_EnterRecursiveCall")
. Must be called once for each _successful_ invocation of `Py_EnterRecursiveCall()`.

Changed in version 3.9: This function is now also available in the [limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
.

Properly implementing [`tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "PyTypeObject.tp_repr")
 for container types requires special recursion handling. In addition to protecting the stack, `tp_repr` also needs to track objects to prevent cycles. The following two functions facilitate this functionality. Effectively, these are the C equivalent to [`@reprlib.recursive_repr`](https://docs.python.org/3/library/reprlib.html#reprlib.recursive_repr "reprlib.recursive_repr")
.

int Py\_ReprEnter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*object)[¶](https://docs.python.org/3/c-api/exceptions.html#c.Py_ReprEnter "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Called at the beginning of the [`tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "PyTypeObject.tp_repr")
 implementation to detect cycles.

If the object has already been processed, the function returns a positive integer. In that case the [`tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "PyTypeObject.tp_repr")
 implementation should return a string object indicating a cycle. As examples, [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 objects return `{...}` and [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 objects return `[...]`.

The function will return a negative integer if the recursion limit is reached. In that case the [`tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "PyTypeObject.tp_repr")
 implementation should typically return `NULL`.

Otherwise, the function returns zero and the [`tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_repr "PyTypeObject.tp_repr")
 implementation can continue normally.

void Py\_ReprLeave([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*object)[¶](https://docs.python.org/3/c-api/exceptions.html#c.Py_ReprLeave "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Ends a [`Py_ReprEnter()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_ReprEnter "Py_ReprEnter")
. Must be called once for each invocation of `Py_ReprEnter()` that returns zero.

int Py\_GetRecursionLimit(void)[¶](https://docs.python.org/3/c-api/exceptions.html#c.Py_GetRecursionLimit "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get the recursion limit for the current interpreter. It can be set with [`Py_SetRecursionLimit()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_SetRecursionLimit "Py_SetRecursionLimit")
. The recursion limit prevents the Python interpreter stack from growing infinitely.

This function cannot fail, and the caller must hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

See also

[`sys.getrecursionlimit()`](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit "sys.getrecursionlimit")

void Py\_SetRecursionLimit(int new\_limit)[¶](https://docs.python.org/3/c-api/exceptions.html#c.Py_SetRecursionLimit "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set the recursion limit for the current interpreter.

This function cannot fail, and the caller must hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

See also

[`sys.setrecursionlimit()`](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit "sys.setrecursionlimit")

Exception and warning types[¶](https://docs.python.org/3/c-api/exceptions.html#exception-and-warning-types "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

All standard Python exceptions and warning categories are available as global variables whose names are `PyExc_` followed by the Python exception name. These have the type [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*; they are all class objects.

For completeness, here are all the variables:

### Exception types[¶](https://docs.python.org/3/c-api/exceptions.html#exception-types "Link to this heading")

These pointers are part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since the version in the _S.ABI_ column (or since 3.2 when _S.ABI_ is empty). Exceptions marked N/A are _not_ part of the Stable ABI.

| C name | S.ABI | Python name |
| --- | --- | --- |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_BaseException[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BaseException "Link to this definition") |     | [`BaseException`](https://docs.python.org/3/builtins/exceptions.html#BaseException "BaseException") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_BaseExceptionGroup[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BaseExceptionGroup "Link to this definition") | 3.11 | [`BaseExceptionGroup`](https://docs.python.org/3/builtins/exceptions.html#BaseExceptionGroup "BaseExceptionGroup") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_Exception[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_Exception "Link to this definition") |     | [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ArithmeticError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ArithmeticError "Link to this definition") |     | [`ArithmeticError`](https://docs.python.org/3/builtins/exceptions.html#ArithmeticError "ArithmeticError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_AssertionError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_AssertionError "Link to this definition") |     | [`AssertionError`](https://docs.python.org/3/builtins/exceptions.html#AssertionError "AssertionError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_AttributeError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_AttributeError "Link to this definition") |     | [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_BlockingIOError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BlockingIOError "Link to this definition") | 3.7 | [`BlockingIOError`](https://docs.python.org/3/builtins/exceptions.html#BlockingIOError "BlockingIOError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_BrokenPipeError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BrokenPipeError "Link to this definition") | 3.7 | [`BrokenPipeError`](https://docs.python.org/3/builtins/exceptions.html#BrokenPipeError "BrokenPipeError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_BufferError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BufferError "Link to this definition") |     | [`BufferError`](https://docs.python.org/3/builtins/exceptions.html#BufferError "BufferError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ChildProcessError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ChildProcessError "Link to this definition") | 3.7 | [`ChildProcessError`](https://docs.python.org/3/builtins/exceptions.html#ChildProcessError "ChildProcessError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ConnectionAbortedError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionAbortedError "Link to this definition") | 3.7 | [`ConnectionAbortedError`](https://docs.python.org/3/builtins/exceptions.html#ConnectionAbortedError "ConnectionAbortedError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ConnectionError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionError "Link to this definition") | 3.7 | [`ConnectionError`](https://docs.python.org/3/builtins/exceptions.html#ConnectionError "ConnectionError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ConnectionRefusedError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionRefusedError "Link to this definition") | 3.7 | [`ConnectionRefusedError`](https://docs.python.org/3/builtins/exceptions.html#ConnectionRefusedError "ConnectionRefusedError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ConnectionResetError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionResetError "Link to this definition") | 3.7 | [`ConnectionResetError`](https://docs.python.org/3/builtins/exceptions.html#ConnectionResetError "ConnectionResetError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_EOFError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_EOFError "Link to this definition") |     | [`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_FileExistsError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_FileExistsError "Link to this definition") | 3.7 | [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_FileNotFoundError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_FileNotFoundError "Link to this definition") | 3.7 | [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_FloatingPointError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_FloatingPointError "Link to this definition") |     | [`FloatingPointError`](https://docs.python.org/3/builtins/exceptions.html#FloatingPointError "FloatingPointError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_GeneratorExit[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_GeneratorExit "Link to this definition") |     | [`GeneratorExit`](https://docs.python.org/3/builtins/exceptions.html#GeneratorExit "GeneratorExit") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ImportCycleError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ImportCycleError "Link to this definition") | N/A | [`ImportCycleError`](https://docs.python.org/3/builtins/exceptions.html#ImportCycleError "ImportCycleError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ImportError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ImportError "Link to this definition") |     | [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_IndentationError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_IndentationError "Link to this definition") |     | [`IndentationError`](https://docs.python.org/3/builtins/exceptions.html#IndentationError "IndentationError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_IndexError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_IndexError "Link to this definition") |     | [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_InterruptedError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_InterruptedError "Link to this definition") | 3.7 | [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_IsADirectoryError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_IsADirectoryError "Link to this definition") | 3.7 | [`IsADirectoryError`](https://docs.python.org/3/builtins/exceptions.html#IsADirectoryError "IsADirectoryError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_KeyError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_KeyError "Link to this definition") |     | [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_KeyboardInterrupt[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_KeyboardInterrupt "Link to this definition") |     | [`KeyboardInterrupt`](https://docs.python.org/3/builtins/exceptions.html#KeyboardInterrupt "KeyboardInterrupt") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_LookupError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_LookupError "Link to this definition") |     | [`LookupError`](https://docs.python.org/3/builtins/exceptions.html#LookupError "LookupError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_MemoryError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_MemoryError "Link to this definition") |     | [`MemoryError`](https://docs.python.org/3/builtins/exceptions.html#MemoryError "MemoryError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ModuleNotFoundError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ModuleNotFoundError "Link to this definition") | 3.6 | [`ModuleNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#ModuleNotFoundError "ModuleNotFoundError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_NameError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_NameError "Link to this definition") |     | [`NameError`](https://docs.python.org/3/builtins/exceptions.html#NameError "NameError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_NotADirectoryError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_NotADirectoryError "Link to this definition") | 3.7 | [`NotADirectoryError`](https://docs.python.org/3/builtins/exceptions.html#NotADirectoryError "NotADirectoryError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_NotImplementedError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_NotImplementedError "Link to this definition") |     | [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_OSError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_OSError "Link to this definition") |     | [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_OverflowError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_OverflowError "Link to this definition") |     | [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_PermissionError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_PermissionError "Link to this definition") | 3.7 | [`PermissionError`](https://docs.python.org/3/builtins/exceptions.html#PermissionError "PermissionError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ProcessLookupError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ProcessLookupError "Link to this definition") | 3.7 | [`ProcessLookupError`](https://docs.python.org/3/builtins/exceptions.html#ProcessLookupError "ProcessLookupError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_PythonFinalizationError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_PythonFinalizationError "Link to this definition") |     | [`PythonFinalizationError`](https://docs.python.org/3/builtins/exceptions.html#PythonFinalizationError "PythonFinalizationError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_RecursionError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_RecursionError "Link to this definition") | 3.7 | [`RecursionError`](https://docs.python.org/3/builtins/exceptions.html#RecursionError "RecursionError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ReferenceError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ReferenceError "Link to this definition") |     | [`ReferenceError`](https://docs.python.org/3/builtins/exceptions.html#ReferenceError "ReferenceError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_RuntimeError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_RuntimeError "Link to this definition") |     | [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_StopAsyncIteration[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_StopAsyncIteration "Link to this definition") | 3.7 | [`StopAsyncIteration`](https://docs.python.org/3/builtins/exceptions.html#StopAsyncIteration "StopAsyncIteration") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_StopIteration[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_StopIteration "Link to this definition") |     | [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_SyntaxError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_SyntaxError "Link to this definition") |     | [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_SystemError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_SystemError "Link to this definition") |     | [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_SystemExit[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_SystemExit "Link to this definition") |     | [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_TabError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_TabError "Link to this definition") |     | [`TabError`](https://docs.python.org/3/builtins/exceptions.html#TabError "TabError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_TimeoutError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_TimeoutError "Link to this definition") | 3.7 | [`TimeoutError`](https://docs.python.org/3/builtins/exceptions.html#TimeoutError "TimeoutError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_TypeError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_TypeError "Link to this definition") |     | [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_UnboundLocalError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnboundLocalError "Link to this definition") |     | [`UnboundLocalError`](https://docs.python.org/3/builtins/exceptions.html#UnboundLocalError "UnboundLocalError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_UnicodeDecodeError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnicodeDecodeError "Link to this definition") |     | [`UnicodeDecodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeDecodeError "UnicodeDecodeError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_UnicodeEncodeError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnicodeEncodeError "Link to this definition") |     | [`UnicodeEncodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeEncodeError "UnicodeEncodeError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_UnicodeError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnicodeError "Link to this definition") |     | [`UnicodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeError "UnicodeError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_UnicodeTranslateError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnicodeTranslateError "Link to this definition") |     | [`UnicodeTranslateError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeTranslateError "UnicodeTranslateError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ValueError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ValueError "Link to this definition") |     | [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ZeroDivisionError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ZeroDivisionError "Link to this definition") |     | [`ZeroDivisionError`](https://docs.python.org/3/builtins/exceptions.html#ZeroDivisionError "ZeroDivisionError") |

Added in version 3.3: [`PyExc_BlockingIOError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BlockingIOError "PyExc_BlockingIOError")
, [`PyExc_BrokenPipeError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BrokenPipeError "PyExc_BrokenPipeError")
, [`PyExc_ChildProcessError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ChildProcessError "PyExc_ChildProcessError")
, [`PyExc_ConnectionError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionError "PyExc_ConnectionError")
, [`PyExc_ConnectionAbortedError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionAbortedError "PyExc_ConnectionAbortedError")
, [`PyExc_ConnectionRefusedError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionRefusedError "PyExc_ConnectionRefusedError")
, [`PyExc_ConnectionResetError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionResetError "PyExc_ConnectionResetError")
, [`PyExc_FileExistsError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_FileExistsError "PyExc_FileExistsError")
, [`PyExc_FileNotFoundError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_FileNotFoundError "PyExc_FileNotFoundError")
, [`PyExc_InterruptedError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_InterruptedError "PyExc_InterruptedError")
, [`PyExc_IsADirectoryError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_IsADirectoryError "PyExc_IsADirectoryError")
, [`PyExc_NotADirectoryError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_NotADirectoryError "PyExc_NotADirectoryError")
, [`PyExc_PermissionError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_PermissionError "PyExc_PermissionError")
, [`PyExc_ProcessLookupError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ProcessLookupError "PyExc_ProcessLookupError")
 and [`PyExc_TimeoutError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_TimeoutError "PyExc_TimeoutError")
 were introduced following [**PEP 3151**](https://peps.python.org/pep-3151/)
.

Added in version 3.5: [`PyExc_StopAsyncIteration`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_StopAsyncIteration "PyExc_StopAsyncIteration")
 and [`PyExc_RecursionError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_RecursionError "PyExc_RecursionError")
.

Added in version 3.6: [`PyExc_ModuleNotFoundError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ModuleNotFoundError "PyExc_ModuleNotFoundError")
.

Added in version 3.11: [`PyExc_BaseExceptionGroup`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BaseExceptionGroup "PyExc_BaseExceptionGroup")
.

### OSError aliases[¶](https://docs.python.org/3/c-api/exceptions.html#oserror-aliases "Link to this heading")

The following are a compatibility aliases to [`PyExc_OSError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_OSError "PyExc_OSError")
.

Changed in version 3.3: These aliases used to be separate exception types.

| C name | Python name | Notes |
| --- | --- | --- |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_EnvironmentError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_EnvironmentError "Link to this definition")<br>  <br><br>_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)<br>._ | [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError") |     |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_IOError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_IOError "Link to this definition")<br>  <br><br>_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)<br>._ | [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError") |     |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_WindowsError[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_WindowsError "Link to this definition")<br>  <br><br>_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)<br> on Windows since version 3.7._ | [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError") | [\[win\]](https://docs.python.org/3/c-api/exceptions.html#win) |

Notes:

\[[win](https://docs.python.org/3/c-api/exceptions.html#id1)\
\]

`PyExc_WindowsError` is only defined on Windows; protect code that uses this by testing that the preprocessor macro `MS_WINDOWS` is defined.

### Warning types[¶](https://docs.python.org/3/c-api/exceptions.html#warning-types "Link to this heading")

These pointers are part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since the version in the _S.ABI_ column (or since 3.2 when _S.ABI_ is empty).

| C name | S.ABI | Python name |
| --- | --- | --- |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_Warning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_Warning "Link to this definition") |     | [`Warning`](https://docs.python.org/3/builtins/exceptions.html#Warning "Warning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_BytesWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BytesWarning "Link to this definition") |     | [`BytesWarning`](https://docs.python.org/3/builtins/exceptions.html#BytesWarning "BytesWarning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_DeprecationWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_DeprecationWarning "Link to this definition") |     | [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_EncodingWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_EncodingWarning "Link to this definition") | 3.10 | [`EncodingWarning`](https://docs.python.org/3/builtins/exceptions.html#EncodingWarning "EncodingWarning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_FutureWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_FutureWarning "Link to this definition") |     | [`FutureWarning`](https://docs.python.org/3/builtins/exceptions.html#FutureWarning "FutureWarning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ImportWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ImportWarning "Link to this definition") |     | [`ImportWarning`](https://docs.python.org/3/builtins/exceptions.html#ImportWarning "ImportWarning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_PendingDeprecationWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_PendingDeprecationWarning "Link to this definition") |     | [`PendingDeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_ResourceWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ResourceWarning "Link to this definition") | 3.7 | [`ResourceWarning`](https://docs.python.org/3/builtins/exceptions.html#ResourceWarning "ResourceWarning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_RuntimeWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_RuntimeWarning "Link to this definition") |     | [`RuntimeWarning`](https://docs.python.org/3/builtins/exceptions.html#RuntimeWarning "RuntimeWarning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_SyntaxWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_SyntaxWarning "Link to this definition") |     | [`SyntaxWarning`](https://docs.python.org/3/builtins/exceptions.html#SyntaxWarning "SyntaxWarning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_UnicodeWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnicodeWarning "Link to this definition") |     | [`UnicodeWarning`](https://docs.python.org/3/builtins/exceptions.html#UnicodeWarning "UnicodeWarning") |
| [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br> \*PyExc\_UserWarning[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UserWarning "Link to this definition") |     | [`UserWarning`](https://docs.python.org/3/builtins/exceptions.html#UserWarning "UserWarning") |

Added in version 3.2: [`PyExc_ResourceWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ResourceWarning "PyExc_ResourceWarning")
.

Added in version 3.10: [`PyExc_EncodingWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_EncodingWarning "PyExc_EncodingWarning")
.

Tracebacks[¶](https://docs.python.org/3/c-api/exceptions.html#tracebacks "Link to this heading")

-------------------------------------------------------------------------------------------------

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyTraceBack\_Type[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyTraceBack_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Type object for traceback objects. This is available as [`types.TracebackType`](https://docs.python.org/3/library/types.html#types.TracebackType "types.TracebackType")
 in the Python layer.

int PyTraceBack\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyTraceBack_Check "Link to this definition")
  

Return true if _op_ is a traceback object, false otherwise. This function does not account for subtypes.

int PyTraceBack\_Here([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*f)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyTraceBack_Here "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Replace the [`__traceback__`](https://docs.python.org/3/builtins/exceptions.html#BaseException.__traceback__ "BaseException.__traceback__")
 attribute on the current exception with a new traceback prepending _f_ to the existing chain.

Calling this function without an exception set is undefined behavior.

This function returns `0` on success, and returns `-1` with an exception set on failure.

int PyTraceBack\_Print([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*tb, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*f)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyTraceBack_Print "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Write the traceback _tb_ into the file _f_.

This function returns `0` on success, and returns `-1` with an exception set on failure.

const char \*PyUnstable\_DumpTraceback(int fd, [PyThreadState](https://docs.python.org/3/c-api/threads.html#c.PyThreadState "PyThreadState")
 \*tstate)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnstable_DumpTraceback "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Write a trace of the Python stack in _tstate_ into the file _fd_. The format looks like:

Traceback (most recent call first):
  File "xxx", line xxx in <xxx\>
  File "xxx", line xxx in <xxx\>
  ...
  File "xxx", line xxx in <xxx\>

This function is meant to debug situations such as segfaults, fatal errors, and similar. The file and function names it outputs are encoded to ASCII with backslashreplace and truncated to 500 characters. It writes only the first 100 frames; further frames are truncated with the line `...`.

This function will return `NULL` on success, or an error message on error.

This function is intended for use in crash scenarios such as signal handlers for SIGSEGV, where the interpreter may be in an inconsistent state. Given that it reads interpreter data structures that may be partially modified, the function might produce incomplete output or it may even crash itself.

The caller does not need to hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
, nor does _tstate_ need to be attached.

Added in version 3.15.

const char \*PyUnstable\_DumpTracebackThreads(int fd, [PyInterpreterState](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState "PyInterpreterState")
 \*interp, [PyThreadState](https://docs.python.org/3/c-api/threads.html#c.PyThreadState "PyThreadState")
 \*current\_tstate, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 max\_threads)[¶](https://docs.python.org/3/c-api/exceptions.html#c.PyUnstable_DumpTracebackThreads "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Write the traces of all Python threads in _interp_ into the file _fd_.

If _interp_ is `NULL` then this function will try to identify the current interpreter using thread-specific storage. If it cannot, it will return an error.

If _current\_tstate_ is not `NULL` then it will be used to identify what the current thread is in the written output. If it is `NULL` then this function will identify the current thread using thread-specific storage. It is not an error if the function is unable to get the current Python thread state.

This function will return `NULL` on success, or an error message on error.

This function is meant to debug situations such as segfaults, fatal errors, and similar. It calls [`PyUnstable_DumpTraceback()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnstable_DumpTraceback "PyUnstable_DumpTraceback")
 for each thread. It only writes the tracebacks of the first _max\_threads_ threads, further output is truncated with the line `...`. If _max\_threads_ is 0, the function will use a default value of 100 for the argument.

This function is intended for use in crash scenarios such as signal handlers for SIGSEGV, where the interpreter may be in an inconsistent state. Given that it reads interpreter data structures that may be partially modified, the function might produce incomplete output or it may even crash itself.

The caller does not need to hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
, nor does _current\_tstate_ need to be attached.

Warning

On the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, this function is not thread-safe. If another thread deletes its [thread state](https://docs.python.org/3/glossary.html#term-thread-state)
 while this function is being called, the process will likely crash.

Added in version 3.15.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Exception Handling](https://docs.python.org/3/c-api/exceptions.html#)
    *   [Printing and clearing](https://docs.python.org/3/c-api/exceptions.html#printing-and-clearing)
        
    *   [Raising exceptions](https://docs.python.org/3/c-api/exceptions.html#raising-exceptions)
        
    *   [Issuing warnings](https://docs.python.org/3/c-api/exceptions.html#issuing-warnings)
        
    *   [Querying the error indicator](https://docs.python.org/3/c-api/exceptions.html#querying-the-error-indicator)
        
    *   [Signal Handling](https://docs.python.org/3/c-api/exceptions.html#signal-handling)
        
    *   [Exception Classes](https://docs.python.org/3/c-api/exceptions.html#exception-classes)
        
    *   [Exception Objects](https://docs.python.org/3/c-api/exceptions.html#exception-objects)
        
    *   [Unicode Exception Objects](https://docs.python.org/3/c-api/exceptions.html#unicode-exception-objects)
        
    *   [Recursion Control](https://docs.python.org/3/c-api/exceptions.html#recursion-control)
        
    *   [Exception and warning types](https://docs.python.org/3/c-api/exceptions.html#exception-and-warning-types)
        *   [Exception types](https://docs.python.org/3/c-api/exceptions.html#exception-types)
            
        *   [OSError aliases](https://docs.python.org/3/c-api/exceptions.html#oserror-aliases)
            
        *   [Warning types](https://docs.python.org/3/c-api/exceptions.html#warning-types)
            
    *   [Tracebacks](https://docs.python.org/3/c-api/exceptions.html#tracebacks)
        

#### Previous topic

[Reference Counting](https://docs.python.org/3/c-api/refcounting.html "previous chapter")

#### Next topic

[Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Exception+Handling&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fexceptions.html&pagesource=c-api%2Fexceptions.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/exceptions.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/extension-modules.html "Defining extension modules")
     |
*   [previous](https://docs.python.org/3/c-api/refcounting.html "Reference Counting")
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
*   [Exception Handling](https://docs.python.org/3/c-api/exceptions.html)
    
*    
    
    |
*   Theme Auto Light Dark |