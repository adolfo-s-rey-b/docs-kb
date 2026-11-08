### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/cmdlinelibs.html "Command-line interface libraries")
     |
*   [previous](https://docs.python.org/3/library/errno.html "errno — Standard errno system symbols")
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
*   [`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`ctypes` — A foreign function library for Python[¶](https://docs.python.org/3/library/ctypes.html#module-ctypes "Link to this heading")

========================================================================================================================================

**Source code:** [Lib/ctypes](https://github.com/python/cpython/tree/3.15/Lib/ctypes)

* * *

`ctypes` is a foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module)
. If it is missing from your copy of CPython, look for documentation from your distributor (that is, whoever provided Python to you). If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements)
.

Warning

`ctypes` provides low-level access to native libraries and the process’s memory, bypassing Python’s safety mechanisms and allowing execution of arbitrary native code. Incorrect use can corrupt data and objects, reveal sensitive information, cause crashes, or otherwise compromise the running process.

ctypes tutorial[¶](https://docs.python.org/3/library/ctypes.html#ctypes-tutorial "Link to this heading")

---------------------------------------------------------------------------------------------------------

Note: Some code samples reference the ctypes [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int")
 type. On platforms where `sizeof(long) == sizeof(int)` it is an alias to [`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "ctypes.c_long")
. So, you should not be confused if `c_long` is printed if you would expect `c_int` — they are actually the same type.

### Loading dynamic link libraries[¶](https://docs.python.org/3/library/ctypes.html#loading-dynamic-link-libraries "Link to this heading")

`ctypes` exports the [`cdll`](https://docs.python.org/3/library/ctypes.html#ctypes.cdll "ctypes.cdll")
, and on Windows [`windll`](https://docs.python.org/3/library/ctypes.html#ctypes.windll "ctypes.windll")
 and [`oledll`](https://docs.python.org/3/library/ctypes.html#ctypes.oledll "ctypes.oledll")
 objects, for loading dynamic link libraries.

You load libraries by accessing them as attributes of these objects. `cdll` loads libraries which export functions using the standard `cdecl` calling convention, while `windll` libraries call functions using the `stdcall` calling convention. [`oledll`](https://docs.python.org/3/library/ctypes.html#ctypes.oledll "ctypes.oledll")
 also uses the `stdcall` calling convention, and assumes the functions return a Windows `HRESULT` error code. The error code is used to automatically raise an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exception when the function call fails.

Changed in version 3.3: Windows errors used to raise [`WindowsError`](https://docs.python.org/3/builtins/exceptions.html#WindowsError "WindowsError")
, which is now an alias of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

Here are some examples for Windows. Note that `msvcrt` is the MS standard C library containing most standard C functions, and uses the `cdecl` calling convention:

Copy

\>>> from ctypes import \*
\>>> print(windll.kernel32)
<WinDLL 'kernel32', handle ... at ...>
\>>> print(cdll.msvcrt)
<CDLL 'msvcrt', handle ... at ...>
\>>> libc \= cdll.msvcrt
\>>>

Windows appends the usual `.dll` file suffix automatically.

Note

Accessing the standard C library through `cdll.msvcrt` will use an outdated version of the library that may be incompatible with the one being used by Python. Where possible, use native Python functionality, or else import and use the `msvcrt` module.

Other systems require the filename _including_ the extension to load a library, so attribute access can not be used to load libraries. Either the [`LoadLibrary()`](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader.LoadLibrary "ctypes.LibraryLoader.LoadLibrary")
 method of the dll loaders should be used, or you should load the library by creating an instance of [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL")
 by calling the constructor.

For example, on Linux:

Copy

\>>> cdll.LoadLibrary("libc.so.6")
<CDLL 'libc.so.6', handle ... at ...>
\>>> libc \= CDLL("libc.so.6")
\>>> libc
<CDLL 'libc.so.6', handle ... at ...>
\>>>

On macOS:

Copy

\>>> cdll.LoadLibrary("libc.dylib")
<CDLL 'libc.dylib', handle ... at ...>
\>>> libc \= CDLL("libc.dylib")
\>>> libc
<CDLL 'libc.dylib', handle ... at ...>

### Accessing functions from loaded dlls[¶](https://docs.python.org/3/library/ctypes.html#accessing-functions-from-loaded-dlls "Link to this heading")

Functions are accessed as attributes of dll objects:

Copy

\>>> libc.printf
<\_FuncPtr object at 0x...>
\>>> print(windll.kernel32.GetModuleHandleA)
<\_FuncPtr object at 0x...>
\>>> print(windll.kernel32.MyOwnFunction)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ctypes.py", line 239, in \_\_getattr\_\_
    func \= \_StdcallFuncPtr(name, self)
AttributeError: function 'MyOwnFunction' not found
\>>>

Note that win32 system dlls like `kernel32` and `user32` often export ANSI as well as UNICODE versions of a function. The UNICODE version is exported with a `W` appended to the name, while the ANSI version is exported with an `A` appended to the name. The win32 `GetModuleHandle` function, which returns a _module handle_ for a given module name, has the following C prototype, and a macro is used to expose one of them as `GetModuleHandle` depending on whether UNICODE is defined or not:

Copy

/\* ANSI version \*/
HMODULE GetModuleHandleA(LPCSTR lpModuleName);
/\* UNICODE version \*/
HMODULE GetModuleHandleW(LPCWSTR lpModuleName);

_windll_ does not try to select one of them by magic, you must access the version you need by specifying `GetModuleHandleA` or `GetModuleHandleW` explicitly, and then call it with bytes or string objects respectively.

Sometimes, dlls export functions with names which aren’t valid Python identifiers, like `"??2@YAPAXI@Z"`. In this case you have to use [`getattr()`](https://docs.python.org/3/builtins/functions.html#getattr "getattr")
 to retrieve the function:

Copy

\>>> getattr(cdll.msvcrt, "??2@YAPAXI@Z")
<\_FuncPtr object at 0x...>
\>>>

On Windows, some dlls export functions not by name but by ordinal. These functions can be accessed by indexing the dll object with the ordinal number:

Copy

\>>> cdll.kernel32\[1\]
<\_FuncPtr object at 0x...>
\>>> cdll.kernel32\[0\]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ctypes.py", line 310, in \_\_getitem\_\_
    func \= \_StdcallFuncPtr(name, self)
AttributeError: function ordinal 0 not found
\>>>

### Calling functions[¶](https://docs.python.org/3/library/ctypes.html#calling-functions "Link to this heading")

You can call these functions like any other Python callable. This example uses the `rand()` function, which takes no arguments and returns a pseudo-random integer:

Copy

\>>> print(libc.rand())
1804289383

On Windows, you can call the `GetModuleHandleA()` function, which returns a win32 module handle (passing `None` as single argument to call it with a `NULL` pointer):

Copy

\>>> print(hex(windll.kernel32.GetModuleHandleA(None)))
0x1d000000
\>>>

`ctypes` cannot determine a function’s calling convention or signature. Consult the function’s C header file or documentation to choose the correct calling convention and set the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 attribute, as described in [Specifying the required argument types (function prototypes)](https://docs.python.org/3/library/ctypes.html#ctypes-specifying-required-argument-types)
. Without `argtypes`, the number of arguments is not checked. Calling a function with an incorrect calling convention or with incorrect arguments can corrupt memory or crash Python.

On Windows, `ctypes` uses win32 structured exception handling to prevent crashes from general protection faults when functions are called with invalid argument values:

Copy

\>>> windll.kernel32.GetModuleHandleA(32)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: exception: access violation reading 0x00000020
\>>>

The [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.")
 module can help debug crashes, such as segmentation faults produced by erroneous C library calls.

`None`, integers, bytes objects and (unicode) strings are the only native Python objects that can directly be used as parameters in these function calls. `None` is passed as a C `NULL` pointer, bytes objects and strings are passed as pointer to the memory block that contains their data (char\* or wchar\_t\*). Python integers are passed as the platform’s default C int type, their value is masked to fit into the C type.

Before we move on calling functions with other parameter types, we have to learn more about `ctypes` data types.

### Fundamental data types[¶](https://docs.python.org/3/library/ctypes.html#fundamental-data-types "Link to this heading")

`ctypes` defines a number of primitive C compatible data types:

| ctypes type | C type | Python type | [`_type_`](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData._type_ "ctypes._SimpleCData._type_") |
| --- | --- | --- | --- |
| [`c_bool`](https://docs.python.org/3/library/ctypes.html#ctypes.c_bool "ctypes.c_bool") | \_Bool | [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool") | `'?'` |
| [`c_char`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "ctypes.c_char") | char | 1-character [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes") | `'c'` |
| [`c_wchar`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar "ctypes.c_wchar") | `wchar_t` | 1-character [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str") | `'u'` |
| [`c_byte`](https://docs.python.org/3/library/ctypes.html#ctypes.c_byte "ctypes.c_byte") | char | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | `'b'` |
| [`c_ubyte`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ubyte "ctypes.c_ubyte") | unsigned char | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | `'B'` |
| [`c_short`](https://docs.python.org/3/library/ctypes.html#ctypes.c_short "ctypes.c_short") | short | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | `'h'` |
| [`c_ushort`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ushort "ctypes.c_ushort") | unsigned short | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | `'H'` |
| [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int") | int | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | `'i'` \* |
| [`c_int8`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int8 "ctypes.c_int8") | `int8_t` | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_int16`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int16 "ctypes.c_int16") | `int16_t` | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_int32`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int32 "ctypes.c_int32") | `int32_t` | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_int64`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int64 "ctypes.c_int64") | `int64_t` | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_uint`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint "ctypes.c_uint") | unsigned int | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | `'I'` \* |
| [`c_uint8`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint8 "ctypes.c_uint8") | `uint8_t` | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_uint16`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint16 "ctypes.c_uint16") | `uint16_t` | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_uint32`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint32 "ctypes.c_uint32") | `uint32_t` | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_uint64`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint64 "ctypes.c_uint64") | `uint64_t` | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "ctypes.c_long") | long | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | `'l'` |
| [`c_ulong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulong "ctypes.c_ulong") | unsigned long | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | `'L'` |
| [`c_longlong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "ctypes.c_longlong") | long long | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | `'q'` \* |
| [`c_ulonglong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulonglong "ctypes.c_ulonglong") | unsigned long long | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | `'Q'` \* |
| [`c_size_t`](https://docs.python.org/3/library/ctypes.html#ctypes.c_size_t "ctypes.c_size_t") | `size_t` | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_ssize_t`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ssize_t "ctypes.c_ssize_t") | [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_time_t`](https://docs.python.org/3/library/ctypes.html#ctypes.c_time_t "ctypes.c_time_t") | `time_t` | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") | \*  |
| [`c_float`](https://docs.python.org/3/library/ctypes.html#ctypes.c_float "ctypes.c_float") | float | [`float`](https://docs.python.org/3/builtins/functions.html#float "float") | `'f'` |
| [`c_double`](https://docs.python.org/3/library/ctypes.html#ctypes.c_double "ctypes.c_double") | double | [`float`](https://docs.python.org/3/builtins/functions.html#float "float") | `'d'` |
| [`c_longdouble`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longdouble "ctypes.c_longdouble") | long double | [`float`](https://docs.python.org/3/builtins/functions.html#float "float") | `'g'` \* |
| [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p") | char\* (NUL terminated) | [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")<br> or `None` | `'z'` |
| [`c_wchar_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar_p "ctypes.c_wchar_p") | wchar\_t\* (NUL terminated) | [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")<br> or `None` | `'Z'` |
| [`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p") | void\* | [`int`](https://docs.python.org/3/builtins/functions.html#int "int")<br> or `None` | `'P'` |
| [`py_object`](https://docs.python.org/3/library/ctypes.html#ctypes.py_object "ctypes.py_object") | [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br>\* | [`object`](https://docs.python.org/3/builtins/functions.html#object "object") | `'O'` |
| [VARIANT\_BOOL](https://docs.python.org/3/library/ctypes.html#ctypes-wintypes) | short int | [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool") | `'v'` |

Additionally, if IEC 60559 compatible complex arithmetic (Annex G) is supported in both C and `libffi`, the following complex types are available:

| ctypes type | C type | Python type | [`_type_`](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData._type_ "ctypes._SimpleCData._type_") |
| --- | --- | --- | --- |
| [`c_float_complex`](https://docs.python.org/3/library/ctypes.html#ctypes.c_float_complex "ctypes.c_float_complex") | float complex | [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex") | `'Zf'` |
| [`c_double_complex`](https://docs.python.org/3/library/ctypes.html#ctypes.c_double_complex "ctypes.c_double_complex") | double complex | [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex") | `'Zd'` |
| [`c_longdouble_complex`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longdouble_complex "ctypes.c_longdouble_complex") | long double complex | [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex") | `'Zg'` |

Changed in version 3.15: The [`_type_`](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData._type_ "ctypes._SimpleCData._type_")
 types `F`, `D` and `G` have been replaced with `Zf`, `Zd` and `Zg`.

All these types can be created by calling them with an optional initializer of the correct type and value:

Copy

\>>> c\_int()
c\_long(0)
\>>> c\_wchar\_p("Hello, World")
c\_wchar\_p(140018365411392)
\>>> c\_ushort(\-3)
c\_ushort(65533)
\>>>

The constructors for numeric types will convert input using [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__ "object.__bool__")
, [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__")
 (for `int`), [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__")
 or [`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__")
. This means [`c_bool`](https://docs.python.org/3/library/ctypes.html#ctypes.c_bool "ctypes.c_bool")
 accepts any object with a truth value:

Copy

\>>> empty\_list \= \[\]
\>>> c\_bool(empty\_list)
c\_bool(False)

Since these types are mutable, their value can also be changed afterwards:

Copy

\>>> i \= c\_int(42)
\>>> print(i)
c\_long(42)
\>>> print(i.value)
42
\>>> i.value \= \-99
\>>> print(i.value)
\-99
\>>>

Assigning a new value to instances of the pointer types [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p")
, [`c_wchar_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar_p "ctypes.c_wchar_p")
, and [`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p")
 changes the _memory location_ they point to, _not the contents_ of the memory block (of course not, because Python string objects are immutable):

Copy

\>>> s \= "Hello, World"
\>>> c\_s \= c\_wchar\_p(s)
\>>> print(c\_s)
c\_wchar\_p(139966785747344)
\>>> print(c\_s.value)
Hello, World
\>>> c\_s.value \= "Hi, there"
\>>> print(c\_s)              \# the memory location has changed
c\_wchar\_p(139966783348904)
\>>> print(c\_s.value)
Hi, there
\>>> print(s)                \# first object is unchanged
Hello, World
\>>>

You should be careful, however, not to pass them to functions expecting pointers to mutable memory. If you need mutable memory blocks, ctypes has a [`create_string_buffer()`](https://docs.python.org/3/library/ctypes.html#ctypes.create_string_buffer "ctypes.create_string_buffer")
 function which creates these in various ways. The current memory block contents can be accessed (or changed) with the `raw` property; if you want to access it as NUL terminated string, use the `value` property:

Copy

\>>> from ctypes import \*
\>>> p \= create\_string\_buffer(3)            \# create a 3 byte buffer, initialized to NUL bytes
\>>> print(sizeof(p), repr(p.raw))
3 b'\\x00\\x00\\x00'
\>>> p \= create\_string\_buffer(b"Hello")     \# create a buffer containing a NUL terminated string
\>>> print(sizeof(p), repr(p.raw))
6 b'Hello\\x00'
\>>> print(repr(p.value))
b'Hello'
\>>> p \= create\_string\_buffer(b"Hello", 10) \# create a 10 byte buffer
\>>> print(sizeof(p), repr(p.raw))
10 b'Hello\\x00\\x00\\x00\\x00\\x00'
\>>> p.value \= b"Hi"
\>>> print(sizeof(p), repr(p.raw))
10 b'Hi\\x00lo\\x00\\x00\\x00\\x00\\x00'
\>>>

The [`create_string_buffer()`](https://docs.python.org/3/library/ctypes.html#ctypes.create_string_buffer "ctypes.create_string_buffer")
 function replaces the old `c_buffer()` function (which is still available as an alias). To create a mutable memory block containing unicode characters of the C type `wchar_t`, use the [`create_unicode_buffer()`](https://docs.python.org/3/library/ctypes.html#ctypes.create_unicode_buffer "ctypes.create_unicode_buffer")
 function.

### Calling functions, continued[¶](https://docs.python.org/3/library/ctypes.html#calling-functions-continued "Link to this heading")

Note that printf prints to the real standard output channel, _not_ to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
, so these examples will only work at the console prompt, not from within _IDLE_ or _PythonWin_:

Copy

\>>> printf \= libc.printf
\>>> printf(b"Hello, %s\\n", b"World!")
Hello, World!
14
\>>> printf(b"Hello, %S\\n", "World!")
Hello, World!
14
\>>> printf(b"%d bottles of beer\\n", 42)
42 bottles of beer
19
\>>> printf(b"%f bottles of beer\\n", 42.5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ctypes.ArgumentError: argument 2: TypeError: Don't know how to convert parameter 2
\>>>

As has been mentioned before, all Python types except integers, strings, and bytes objects have to be wrapped in their corresponding `ctypes` type, so that they can be converted to the required C data type:

Copy

\>>> printf(b"An int %d, a double %f\\n", 1234, c\_double(3.14))
An int 1234, a double 3.140000
31
\>>>

### Calling variadic functions[¶](https://docs.python.org/3/library/ctypes.html#calling-variadic-functions "Link to this heading")

On a lot of platforms calling variadic functions through ctypes is exactly the same as calling functions with a fixed number of parameters. On some platforms, and in particular ARM64 for Apple Platforms, the calling convention for variadic functions is different than that for regular functions.

On those platforms it is required to specify the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 attribute for the regular, non-variadic, function arguments:

Copy

libc.printf.argtypes \= \[ctypes.c\_char\_p\]

Because specifying the attribute does not inhibit portability it is advised to always specify [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 for all variadic functions.

### Calling functions with your own custom data types[¶](https://docs.python.org/3/library/ctypes.html#calling-functions-with-your-own-custom-data-types "Link to this heading")

You can also customize `ctypes` argument conversion to allow instances of your own classes be used as function arguments. `ctypes` looks for an `_as_parameter_` attribute and uses this as the function argument. The attribute must be an integer, string, bytes, a `ctypes` instance, or an object with an `_as_parameter_` attribute:

Copy

\>>> class Bottles:
...     def \_\_init\_\_(self, number):
...         self.\_as\_parameter\_ \= number
...
\>>> bottles \= Bottles(42)
\>>> printf(b"%d bottles of beer\\n", bottles)
42 bottles of beer
19
\>>>

If you don’t want to store the instance’s data in the `_as_parameter_` instance variable, you could define a [`@property`](https://docs.python.org/3/builtins/functions.html#property "property")
 which makes the attribute available on request.

### Specifying the required argument types (function prototypes)[¶](https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes "Link to this heading")

It is possible to specify the required argument types of functions exported from DLLs by setting the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 attribute.

[`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 must be a sequence of C data types (the `printf()` function is probably not a good example here, because it takes a variable number and different types of parameters depending on the format string, on the other hand this is quite handy to experiment with this feature):

Copy

\>>> printf.argtypes \= \[c\_char\_p, c\_char\_p, c\_int, c\_double\]
\>>> printf(b"String '%s', Int %d, Double %f\\n", b"Hi", 10, 2.2)
String 'Hi', Int 10, Double 2.200000
37
\>>>

Specifying a format protects against incompatible argument types (just as a prototype for a C function), and tries to convert the arguments to valid types:

Copy

\>>> printf(b"%d %d %d", 1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ctypes.ArgumentError: argument 2: TypeError: 'int' object cannot be interpreted as ctypes.c\_char\_p
\>>> printf(b"%s %d %f\\n", b"X", 2, 3)
X 2 3.000000
13
\>>>

Setting [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 also causes `ctypes` to raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 if too few arguments are passed:

Copy

\>>> printf(b"%s %d %f\\n", b"X", 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: this function takes at least 4 arguments (3 given)

Functions using the `stdcall` calling convention require exactly as many arguments as there are items in [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
. Functions using the `cdecl` calling convention accept additional arguments, to support variadic functions. The declaration must match the function’s actual signature; ctypes cannot verify this.

If you have defined your own classes which you pass to function calls, you have to implement a [`from_param()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "ctypes._CData.from_param")
 class method for them to be able to use them in the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 sequence. The `from_param()` class method receives the Python object passed to the function call, it should do a typecheck or whatever is needed to make sure this object is acceptable, and then return the object itself, its `_as_parameter_` attribute, or whatever you want to pass as the C function argument in this case. Again, the result should be an integer, string, bytes, a `ctypes` instance, or an object with an `_as_parameter_` attribute.

### Return types[¶](https://docs.python.org/3/library/ctypes.html#return-types "Link to this heading")

By default functions are assumed to return the C int type. Other return types can be specified by setting the [`restype`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "ctypes._CFuncPtr.restype")
 attribute of the function object.

The C prototype of `time()` is `time_t time(time_t *)`. Because `time_t` might be of a different type than the default return type int, you should specify the `restype` attribute:

Copy

\>>> libc.time.restype \= c\_time\_t

The argument types can be specified using [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
:

Copy

\>>> libc.time.argtypes \= (POINTER(c\_time\_t),)

To call the function with a `NULL` pointer as first argument, use `None`:

Copy

\>>> print(libc.time(None))
1150640792

Here is a more advanced example, it uses the `strchr()` function, which expects a string pointer and a char, and returns a pointer to a string:

Copy

\>>> strchr \= libc.strchr
\>>> strchr(b"abcdef", ord("d"))
8059983
\>>> strchr.restype \= c\_char\_p    \# c\_char\_p is a pointer to a string
\>>> strchr(b"abcdef", ord("d"))
b'def'
\>>> print(strchr(b"abcdef", ord("x")))
None
\>>>

If you want to avoid the [`ord("x")`](https://docs.python.org/3/builtins/functions.html#ord "ord")
 calls above, you can set the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 attribute, and the second argument will be converted from a single character Python bytes object into a C char:

Copy

\>>> strchr.restype \= c\_char\_p
\>>> strchr.argtypes \= \[c\_char\_p, c\_char\]
\>>> strchr(b"abcdef", b"d")
b'def'
\>>> strchr(b"abcdef", b"def")
Traceback (most recent call last):
ctypes.ArgumentError: argument 2: TypeError: one character bytes, bytearray or integer expected
\>>> print(strchr(b"abcdef", b"x"))
None
\>>> strchr(b"abcdef", b"d")
b'def'
\>>>

You can also use a callable Python object (a function or a class for example) as the [`restype`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "ctypes._CFuncPtr.restype")
 attribute, if the foreign function returns an integer. The callable will be called with the _integer_ the C function returns, and the result of this call will be used as the result of your function call. This is useful to check for error return values and automatically raise an exception:

Copy

\>>> GetModuleHandle \= windll.kernel32.GetModuleHandleA
\>>> def ValidHandle(value):
...     if value \== 0:
...         raise WinError()
...     return value
...
\>>>
\>>> GetModuleHandle.restype \= ValidHandle
\>>> GetModuleHandle(None)
486539264
\>>> GetModuleHandle("something silly")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in ValidHandle
OSError: \[Errno 126\] The specified module could not be found.
\>>>

`WinError` is a function which will call Windows `FormatMessage()` api to get the string representation of an error code, and _returns_ an exception. `WinError` takes an optional error code parameter, if no one is used, it calls [`GetLastError()`](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "ctypes.GetLastError")
 to retrieve it.

Please note that a much more powerful error checking mechanism is available through the [`errcheck`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "ctypes._CFuncPtr.errcheck")
 attribute; see the reference manual for details.

### Passing pointers (or: passing parameters by reference)[¶](https://docs.python.org/3/library/ctypes.html#passing-pointers-or-passing-parameters-by-reference "Link to this heading")

Sometimes a C api function expects a _pointer_ to a data type as parameter, probably to write into the corresponding location, or if the data is too large to be passed by value. This is also known as _passing parameters by reference_.

`ctypes` exports the [`byref()`](https://docs.python.org/3/library/ctypes.html#ctypes.byref "ctypes.byref")
 function which is used to pass parameters by reference. The same effect can be achieved with the [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer")
 function, although `pointer()` does a lot more work since it constructs a real pointer object, so it is faster to use `byref()` if you don’t need the pointer object in Python itself:

Copy

\>>> i \= c\_int()
\>>> f \= c\_float()
\>>> s \= create\_string\_buffer(b'\\000' \* 32)
\>>> print(i.value, f.value, repr(s.value))
0 0.0 b''
\>>> libc.sscanf(b"1 3.14 Hello", b"%d %f %s",
...             byref(i), byref(f), s)
3
\>>> print(i.value, f.value, repr(s.value))
1 3.1400001049 b'Hello'
\>>>

### Structures and unions[¶](https://docs.python.org/3/library/ctypes.html#structures-and-unions "Link to this heading")

Structures and unions must derive from the [`Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure")
 and [`Union`](https://docs.python.org/3/library/ctypes.html#ctypes.Union "ctypes.Union")
 base classes which are defined in the `ctypes` module. Each subclass must define a [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 attribute. `_fields_` must be a list of _2-tuples_, containing a _field name_ and a _field type_.

The field type must be a `ctypes` type like [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int")
, or any other derived `ctypes` type: structure, union, array, pointer.

Here is a simple example of a POINT structure, which contains two integers named _x_ and _y_, and also shows how to initialize a structure in the constructor:

Copy

\>>> from ctypes import \*
\>>> class POINT(Structure):
...     \_fields\_ \= \[("x", c\_int),\
...                 ("y", c\_int)\]
...
\>>> point \= POINT(10, 20)
\>>> print(point.x, point.y)
10 20
\>>> point \= POINT(y\=5)
\>>> print(point.x, point.y)
0 5
\>>> POINT(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: too many initializers
\>>>

You can, however, build much more complicated structures. A structure can itself contain other structures by using a structure as a field type.

Here is a RECT structure which contains two POINTs named _upperleft_ and _lowerright_:

Copy

\>>> class RECT(Structure):
...     \_fields\_ \= \[("upperleft", POINT),\
...                 ("lowerright", POINT)\]
...
\>>> rc \= RECT(point)
\>>> print(rc.upperleft.x, rc.upperleft.y)
0 5
\>>> print(rc.lowerright.x, rc.lowerright.y)
0 0
\>>>

Nested structures can also be initialized in the constructor in several ways:

Copy

\>>> r \= RECT(POINT(1, 2), POINT(3, 4))
\>>> r \= RECT((1, 2), (3, 4))

Field [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)
s can be retrieved from the _class_, they are useful for debugging because they can provide useful information. See [`CField`](https://docs.python.org/3/library/ctypes.html#ctypes.CField "ctypes.CField")
:

Copy

\>>> POINT.x
<ctypes.CField 'x' type=c\_int, ofs=0, size=4>
\>>> POINT.y
<ctypes.CField 'y' type=c\_int, ofs=4, size=4>
\>>>

Warning

`ctypes` does not support passing unions or structures with bit-fields to functions by value. While this may work on 32-bit x86, it’s not guaranteed by the library to work in the general case. Unions and structures with bit-fields should always be passed to functions by pointer.

### Structure/union layout, alignment and byte order[¶](https://docs.python.org/3/library/ctypes.html#structure-union-layout-alignment-and-byte-order "Link to this heading")

By default, Structure and Union fields are laid out in the same way the C compiler does it. It is possible to override this behavior entirely by specifying a [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_")
 class attribute in the subclass definition; see the attribute documentation for details.

The [`_align_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._align_ "ctypes.Structure._align_")
 class attribute specifies the minimum alignment for the structure itself. See the attribute documentation for details.

`ctypes` uses the native byte order for Structures and Unions. To build structures with non-native byte order, you can use one of the [`BigEndianStructure`](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianStructure "ctypes.BigEndianStructure")
, [`LittleEndianStructure`](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianStructure "ctypes.LittleEndianStructure")
, [`BigEndianUnion`](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianUnion "ctypes.BigEndianUnion")
, and [`LittleEndianUnion`](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianUnion "ctypes.LittleEndianUnion")
 base classes. These classes cannot contain pointer fields.

### Bit fields in structures and unions[¶](https://docs.python.org/3/library/ctypes.html#bit-fields-in-structures-and-unions "Link to this heading")

It is possible to create structures and unions containing bit fields. Bit fields are only possible for integer fields, the bit width is specified as the third item in the [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 tuples:

Copy

\>>> class Int(Structure):
...     \_fields\_ \= \[("first\_16", c\_int, 16),\
...                 ("second\_16", c\_int, 16)\]
...
\>>> print(Int.first\_16)
<ctypes.CField 'first\_16' type=c\_int, ofs=0, bit\_size=16, bit\_offset=0>
\>>> print(Int.second\_16)
<ctypes.CField 'second\_16' type=c\_int, ofs=0, bit\_size=16, bit\_offset=16>

It is important to note that bit field allocation and layout in memory are not defined as a C standard; their implementation is compiler-specific. By default, Python will attempt to match the behavior of a “native” compiler for the current platform. See the [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_")
 attribute for details on the default behavior and how to change it.

### Arrays[¶](https://docs.python.org/3/library/ctypes.html#arrays "Link to this heading")

Arrays are sequences, containing a fixed number of instances of the same type.

The recommended way to create array types is by multiplying a data type with a positive integer:

Copy

TenPointsArrayType \= POINT \* 10

Here is an example of a somewhat artificial data type, a structure containing 4 POINTs among other stuff:

Copy

\>>> from ctypes import \*
\>>> class POINT(Structure):
...     \_fields\_ \= ("x", c\_int), ("y", c\_int)
...
\>>> class MyStruct(Structure):
...     \_fields\_ \= \[("a", c\_int),\
...                 ("b", c\_float),\
...                 ("point\_array", POINT \* 4)\]
\>>>
\>>> print(len(MyStruct().point\_array))
4
\>>>

Instances are created in the usual way, by calling the class:

Copy

arr \= TenPointsArrayType()
for pt in arr:
    print(pt.x, pt.y)

The above code print a series of `0 0` lines, because the array contents is initialized to zeros.

Initializers of the correct type can also be specified:

Copy

\>>> from ctypes import \*
\>>> TenIntegers \= c\_int \* 10
\>>> ii \= TenIntegers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
\>>> print(ii)
<c\_long\_Array\_10 object at 0x...>
\>>> for i in ii: print(i, end\=" ")
...
1 2 3 4 5 6 7 8 9 10
\>>>

### Pointers[¶](https://docs.python.org/3/library/ctypes.html#pointers "Link to this heading")

Pointer instances are created by calling the [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer")
 function on a `ctypes` type:

Copy

\>>> from ctypes import \*
\>>> i \= c\_int(42)
\>>> pi \= pointer(i)
\>>>

Pointer instances have a [`contents`](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer.contents "ctypes._Pointer.contents")
 attribute which returns the object to which the pointer points, the `i` object above:

Copy

\>>> pi.contents
c\_long(42)
\>>>

Note that `ctypes` does not have OOR (original object return), it constructs a new, equivalent object each time you retrieve an attribute:

Copy

\>>> pi.contents is i
False
\>>> pi.contents is pi.contents
False
\>>>

Assigning another [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int")
 instance to the pointer’s contents attribute would cause the pointer to point to the memory location where this is stored:

Copy

\>>> i \= c\_int(99)
\>>> pi.contents \= i
\>>> pi.contents
c\_long(99)
\>>>

Pointer instances can also be indexed with integers:

Copy

\>>> pi\[0\]
99
\>>>

Assigning to an integer index changes the pointed to value:

Copy

\>>> print(i)
c\_long(99)
\>>> pi\[0\] \= 22
\>>> print(i)
c\_long(22)
\>>>

It is also possible to use indexes different from 0, but you must know what you’re doing, just as in C: You can access or change arbitrary memory locations. Generally you only use this feature if you receive a pointer from a C function, and you _know_ that the pointer actually points to an array instead of a single item.

Warning

Because pointer objects support subscription, they implicitly support [iteration](https://docs.python.org/3/glossary.html#term-iterator)
. Unless doing this in a controlled manner, such as by manually calling [`next()`](https://docs.python.org/3/builtins/functions.html#next "next")
 on a [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer")
 iterator, this will typically lead to infinite loops or crashes, because ctypes has no way of knowing when to stop iteration. In other words, a `pointer` iterator will infinitely yield arbitrary memory.

Behind the scenes, the [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer")
 function does more than simply create pointer instances, it has to create pointer _types_ first. This is done with the [`POINTER()`](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "ctypes.POINTER")
 function, which accepts any `ctypes` type, and returns a new type:

Copy

\>>> PI \= POINTER(c\_int)
\>>> PI
<class 'ctypes.LP\_c\_long'>
\>>> PI(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected c\_long instead of int
\>>> PI(c\_int(42))
<ctypes.LP\_c\_long object at 0x...>
\>>>

Calling the pointer type without an argument creates a `NULL` pointer. `NULL` pointers have a `False` boolean value:

Copy

\>>> null\_ptr \= POINTER(c\_int)()
\>>> print(bool(null\_ptr))
False
\>>>

`ctypes` checks for `NULL` when dereferencing pointers (but dereferencing invalid non-`NULL` pointers would crash Python):

Copy

\>>> null\_ptr\[0\]
Traceback (most recent call last):
    ....
ValueError: NULL pointer access
\>>>

\>>> null\_ptr\[0\] \= 1234
Traceback (most recent call last):
    ....
ValueError: NULL pointer access
\>>>

### Thread safety without the GIL[¶](https://docs.python.org/3/library/ctypes.html#thread-safety-without-the-gil "Link to this heading")

From Python 3.13 onward, the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
 can be disabled on the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
. In ctypes, reads and writes to a single object concurrently is safe, but not across multiple objects:

> Copy
> 
> \>>> number \= c\_int(42)
> \>>> pointer\_a \= pointer(number)
> \>>> pointer\_b \= pointer(number)

In the above, it’s only safe for one object to read and write to the address at once if the GIL is disabled. So, `pointer_a` can be shared and written to across multiple threads, but only if `pointer_b` is not also attempting to do the same. If this is an issue, consider using a [`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock")
 to synchronize access to memory:

> Copy
> 
> \>>> import threading
> \>>> lock \= threading.Lock()
> \>>> \# Thread 1
> \>>> with lock:
> ...    pointer\_a\[0\] \= 24
> \>>> \# Thread 2
> \>>> with lock:
> ...    pointer\_b\[0\] \= 42

### Type conversions[¶](https://docs.python.org/3/library/ctypes.html#type-conversions "Link to this heading")

Usually, ctypes does strict type checking. This means, if you have `POINTER(c_int)` in the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 list of a function or as the type of a member field in a structure definition, only instances of exactly the same type are accepted. There are some exceptions to this rule, where ctypes accepts other objects. For example, you can pass compatible array instances instead of pointer types. So, for `POINTER(c_int)`, ctypes accepts an array of c\_int:

Copy

\>>> class Bar(Structure):
...     \_fields\_ \= \[("count", c\_int), ("values", POINTER(c\_int))\]
...
\>>> bar \= Bar()
\>>> bar.values \= (c\_int \* 3)(1, 2, 3)
\>>> bar.count \= 3
\>>> for i in range(bar.count):
...     print(bar.values\[i\])
...
1
2
3
\>>>

In addition, if a function argument is explicitly declared to be a pointer type (such as `POINTER(c_int)`) in [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
, an object of the pointed type (`c_int` in this case) can be passed to the function. ctypes will apply the required [`byref()`](https://docs.python.org/3/library/ctypes.html#ctypes.byref "ctypes.byref")
 conversion in this case automatically.

To set a POINTER type field to `NULL`, you can assign `None`:

Copy

\>>> bar.values \= None
\>>>

Sometimes you have instances of incompatible types. In C, you can cast one type into another type. `ctypes` provides a [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast")
 function which can be used in the same way. The `Bar` structure defined above accepts `POINTER(c_int)` pointers or [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int")
 arrays for its `values` field, but not instances of other types:

Copy

\>>> bar.values \= (c\_byte \* 4)()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: incompatible types, c\_byte\_Array\_4 instance instead of LP\_c\_long instance
\>>>

For these cases, the [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast")
 function is handy.

The [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast")
 function can be used to cast a ctypes instance into a pointer to a different ctypes data type. `cast()` takes two parameters, a ctypes object that is or can be converted to a pointer of some kind, and a ctypes pointer type. It returns an instance of the second argument, which references the same memory block as the first argument:

Copy

\>>> a \= (c\_byte \* 4)()
\>>> cast(a, POINTER(c\_int))
<ctypes.LP\_c\_long object at ...>
\>>>

So, [`cast()`](https://docs.python.org/3/library/ctypes.html#ctypes.cast "ctypes.cast")
 can be used to assign to the `values` field of `Bar` the structure:

Copy

\>>> bar \= Bar()
\>>> bar.values \= cast((c\_byte \* 4)(), POINTER(c\_int))
\>>> print(bar.values\[0\])
0
\>>>

### Incomplete Types[¶](https://docs.python.org/3/library/ctypes.html#incomplete-types "Link to this heading")

_Incomplete Types_ are structures, unions or arrays whose members are not yet specified. In C, they are specified by forward declarations, which are defined later:

Copy

struct cell; /\* forward declaration \*/

struct cell {
    char \*name;
    struct cell \*next;
};

The straightforward translation into ctypes code would be this, but it does not work:

Copy

\>>> class cell(Structure):
...     \_fields\_ \= \[("name", c\_char\_p),\
...                 ("next", POINTER(cell))\]
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in cell
NameError: name 'cell' is not defined
\>>>

because the new `class cell` is not available in the class statement itself. In `ctypes`, we can define the `cell` class and set the [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 attribute later, after the class statement:

Copy

\>>> from ctypes import \*
\>>> class cell(Structure):
...     pass
...
\>>> cell.\_fields\_ \= \[("name", c\_char\_p),\
...                  ("next", POINTER(cell))\]
\>>>

Let’s try it. We create two instances of `cell`, and let them point to each other, and finally follow the pointer chain a few times:

Copy

\>>> c1 \= cell()
\>>> c1.name \= b"foo"
\>>> c2 \= cell()
\>>> c2.name \= b"bar"
\>>> c1.next \= pointer(c2)
\>>> c2.next \= pointer(c1)
\>>> p \= c1
\>>> for i in range(8):
...     print(p.name, end\=" ")
...     p \= p.next\[0\]
...
b'foo' b'bar' b'foo' b'bar' b'foo' b'bar' b'foo' b'bar'
\>>>

### Callback functions[¶](https://docs.python.org/3/library/ctypes.html#callback-functions "Link to this heading")

`ctypes` allows creating C callable function pointers from Python callables. These are sometimes called _callback functions_.

First, you must create a class for the callback function. The class knows the calling convention, the return type, and the number and types of arguments this function will receive.

The [`CFUNCTYPE()`](https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE "ctypes.CFUNCTYPE")
 factory function creates types for callback functions using the `cdecl` calling convention. On Windows, the [`WINFUNCTYPE()`](https://docs.python.org/3/library/ctypes.html#ctypes.WINFUNCTYPE "ctypes.WINFUNCTYPE")
 factory function creates types for callback functions using the `stdcall` calling convention.

Both of these factory functions are called with the result type as first argument, and the callback functions expected argument types as the remaining arguments.

I will present an example here which uses the standard C library’s `qsort()` function, that is used to sort items with the help of a callback function. `qsort()` will be used to sort an array of integers:

Copy

\>>> IntArray5 \= c\_int \* 5
\>>> ia \= IntArray5(5, 1, 7, 33, 99)
\>>> qsort \= libc.qsort
\>>> qsort.restype \= None
\>>>

`qsort()` must be called with a pointer to the data to sort, the number of items in the data array, the size of one item, and a pointer to the comparison function, the callback. The callback will then be called with two pointers to items, and it must return a negative integer if the first item is smaller than the second, a zero if they are equal, and a positive integer otherwise.

So our callback function receives pointers to integers, and must return an integer. First we create the `type` for the callback function:

Copy

\>>> CMPFUNC \= CFUNCTYPE(c\_int, POINTER(c\_int), POINTER(c\_int))
\>>>

To get started, here is a simple callback that shows the values it gets passed:

Copy

\>>> def py\_cmp\_func(a, b):
...     print("py\_cmp\_func", a\[0\], b\[0\])
...     return 0
...
\>>> cmp\_func \= CMPFUNC(py\_cmp\_func)
\>>>

The result:

Copy

\>>> qsort(ia, len(ia), sizeof(c\_int), cmp\_func)
py\_cmp\_func 5 1
py\_cmp\_func 33 99
py\_cmp\_func 7 33
py\_cmp\_func 5 7
py\_cmp\_func 1 7
\>>>

Now we can actually compare the two items and return a useful result:

Copy

\>>> def py\_cmp\_func(a, b):
...     print("py\_cmp\_func", a\[0\], b\[0\])
...     return a\[0\] \- b\[0\]
...
\>>>
\>>> qsort(ia, len(ia), sizeof(c\_int), CMPFUNC(py\_cmp\_func))
py\_cmp\_func 5 1
py\_cmp\_func 33 99
py\_cmp\_func 7 33
py\_cmp\_func 1 7
py\_cmp\_func 5 7
\>>>

As we can easily check, our array is sorted now:

Copy

\>>> for i in ia: print(i, end\=" ")
...
1 5 7 33 99
\>>>

The function factories can be used as decorator factories, so we may as well write:

Copy

\>>> @CFUNCTYPE(c\_int, POINTER(c\_int), POINTER(c\_int))
... def py\_cmp\_func(a, b):
...     print("py\_cmp\_func", a\[0\], b\[0\])
...     return a\[0\] \- b\[0\]
...
\>>> qsort(ia, len(ia), sizeof(c\_int), py\_cmp\_func)
py\_cmp\_func 5 1
py\_cmp\_func 33 99
py\_cmp\_func 7 33
py\_cmp\_func 1 7
py\_cmp\_func 5 7
\>>>

Note

Make sure you keep references to [`CFUNCTYPE()`](https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE "ctypes.CFUNCTYPE")
 objects as long as they are used from C code. `ctypes` doesn’t, and if you don’t, they may be garbage collected, crashing your program when a callback is made.

Also, note that if the callback function is called in a thread created outside of Python’s control (e.g. by the foreign code that calls the callback), ctypes creates a new dummy Python thread on every invocation. This behavior is correct for most purposes, but it means that values stored with [`threading.local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local")
 will _not_ survive across different callbacks, even when those calls are made from the same C thread.

### Accessing values exported from dlls[¶](https://docs.python.org/3/library/ctypes.html#accessing-values-exported-from-dlls "Link to this heading")

Some shared libraries not only export functions, they also export variables. An example in the Python library itself is the [`Py_Version`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_Version "Py_Version")
, Python runtime version number encoded in a single constant integer.

`ctypes` can access values like this with the [`in_dll()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.in_dll "ctypes._CData.in_dll")
 class methods of the type. _pythonapi_ is a predefined symbol giving access to the Python C api:

Copy

\>>> version \= ctypes.c\_int.in\_dll(ctypes.pythonapi, "Py\_Version")
\>>> print(hex(version.value))
0x30c00a0

An extended example which also demonstrates the use of pointers accesses the `_PyImport_FrozenBootstrap` pointer exported by Python. It points to an array of [`_frozen`](https://docs.python.org/3/c-api/import.html#c._frozen "_frozen")
 records describing frozen modules used during startup, terminated by one whose members are all `NULL` or zero. This is similar to the [`PyImport_FrozenModules`](https://docs.python.org/3/c-api/import.html#c.PyImport_FrozenModules "PyImport_FrozenModules")
 table, which third-party code can use to provide additional frozen modules.

We can read this table with `ctypes`:

Copy

\>>> from ctypes import \*
\>>>
\>>> class struct\_frozen(Structure):
...     \_fields\_ \= \[("name", c\_char\_p),\
...                 ("code", POINTER(c\_ubyte)),\
...                 ("size", c\_int),\
...                 ("is\_package", c\_int),\
...                \]
...
\>>>

We have defined the [`_frozen`](https://docs.python.org/3/c-api/import.html#c._frozen "_frozen")
 data type, so we can get the pointer to the table:

Copy

\>>> FrozenTable \= POINTER(struct\_frozen)
\>>> table \= FrozenTable.in\_dll(pythonapi, "\_PyImport\_FrozenBootstrap")
\>>>

Since `table` is a `pointer` to the array of `struct_frozen` records, we can iterate over it, but we just have to make sure that our loop terminates, because pointers have no size. Sooner or later it would probably crash with an access violation or whatever, so it’s better to break out of the loop when we hit the `NULL` entry:

Copy

\>>> for item in table:
...     if item.name is None:
...         break
...     print(item.name.decode("ascii"), item.size)
...
\_frozen\_importlib 31764
\_frozen\_importlib\_external 41499
zipimport 12345
\>>>

Frozen packages are indicated by a nonzero `is_package` member. Python also includes frozen modules and packages used for testing, such as `__hello__` and `__phello__`, in a separate table, `_PyImport_FrozenTest`.

### Surprises[¶](https://docs.python.org/3/library/ctypes.html#surprises "Link to this heading")

There are some edges in `ctypes` where you might expect something other than what actually happens.

Consider the following example:

Copy

\>>> from ctypes import \*
\>>> class POINT(Structure):
...     \_fields\_ \= ("x", c\_int), ("y", c\_int)
...
\>>> class RECT(Structure):
...     \_fields\_ \= ("a", POINT), ("b", POINT)
...
\>>> p1 \= POINT(1, 2)
\>>> p2 \= POINT(3, 4)
\>>> rc \= RECT(p1, p2)
\>>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
1 2 3 4
\>>> \# now swap the two points
\>>> rc.a, rc.b \= rc.b, rc.a
\>>> print(rc.a.x, rc.a.y, rc.b.x, rc.b.y)
3 4 3 4
\>>>

Hm. We certainly expected the last statement to print `3 4 1 2`. What happened? Here are the steps of the `rc.a, rc.b = rc.b, rc.a` line above:

Copy

\>>> temp0, temp1 \= rc.b, rc.a
\>>> rc.a \= temp0
\>>> rc.b \= temp1
\>>>

Note that `temp0` and `temp1` are objects still using the internal buffer of the `rc` object above. So executing `rc.a = temp0` copies the buffer contents of `temp0` into `rc` ‘s buffer. This, in turn, changes the contents of `temp1`. So, the last assignment `rc.b = temp1`, doesn’t have the expected effect.

Keep in mind that retrieving sub-objects from Structure, Unions, and Arrays doesn’t _copy_ the sub-object, instead it retrieves a wrapper object accessing the root-object’s underlying buffer.

Another example that may behave differently from what one would expect is this:

Copy

\>>> s \= c\_char\_p()
\>>> s.value \= b"abc def ghi"
\>>> s.value
b'abc def ghi'
\>>> s.value is s.value
False
\>>>

Note

Objects instantiated from [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p")
 can only have their value set to bytes or integers.

Why is it printing `False`? ctypes instances are objects containing a memory block plus some [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)
s accessing the contents of the memory. Storing a Python object in the memory block does not store the object itself, instead the `contents` of the object is stored. Accessing the contents again constructs a new Python object each time!

### Variable-sized data types[¶](https://docs.python.org/3/library/ctypes.html#variable-sized-data-types "Link to this heading")

`ctypes` provides some support for variable-sized arrays and structures.

The [`resize()`](https://docs.python.org/3/library/ctypes.html#ctypes.resize "ctypes.resize")
 function can be used to resize the memory buffer of an existing ctypes object. The function takes the object as first argument, and the requested size in bytes as the second argument. The memory block cannot be made smaller than the natural memory block specified by the objects type, a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised if this is tried:

Copy

\>>> short\_array \= (c\_short \* 4)()
\>>> print(sizeof(short\_array))
8
\>>> resize(short\_array, 4)
Traceback (most recent call last):
    ...
ValueError: minimum size is 8
\>>> resize(short\_array, 32)
\>>> sizeof(short\_array)
32
\>>> sizeof(type(short\_array))
8
\>>>

This is nice and fine, but how would one access the additional elements contained in this array? Since the type still only knows about 4 elements, we get errors accessing other elements:

Copy

\>>> short\_array\[:\]
\[0, 0, 0, 0\]
\>>> short\_array\[7\]
Traceback (most recent call last):
    ...
IndexError: invalid index
\>>>

Another way to use variable-sized data types with `ctypes` is to use the dynamic nature of Python, and (re-)define the data type after the required size is already known, on a case by case basis.

ctypes reference[¶](https://docs.python.org/3/library/ctypes.html#ctypes-reference "Link to this heading")

-----------------------------------------------------------------------------------------------------------

### Loading shared libraries[¶](https://docs.python.org/3/library/ctypes.html#loading-shared-libraries "Link to this heading")

There are several ways to load shared libraries into the Python process. One way is to instantiate [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL")
 or one of its subclasses:

class ctypes.CDLL(_name_, _mode\=DEFAULT\_MODE_, _handle\=None_, _use\_errno\=False_, _use\_last\_error\=False_, _winmode\=None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "Link to this definition")

Represents a loaded shared library.

Functions in this library use the standard C calling convention, and are assumed to return int. The Python [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
 is released before calling any function exported by these libraries, and reacquired afterwards. For different function behavior, use a subclass: [`OleDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.OleDLL "ctypes.OleDLL")
, [`WinDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.WinDLL "ctypes.WinDLL")
, or [`PyDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL "ctypes.PyDLL")
.

If you have an existing [`handle`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL._handle "ctypes.CDLL._handle")
 to an already loaded shared library, it can be passed as the _handle_ argument to wrap the opened library in a new `CDLL` object. In this case, _name_ is only used to set the [`_name`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL._name "ctypes.CDLL._name")
 attribute, but it may be adjusted and/or validated.

If _handle_ is `None`, the underlying platform’s _[dlopen(3)](https://manpages.debian.org/dlopen(3))
_ or [LoadLibraryExW](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexw)
 function is used to load the library into the process, and to get a handle to it.

_name_ is the pathname of the shared library to open. If _name_ does not contain a path separator, the library is found in a platform-specific way.

On Windows, the `.DLL` suffix may be missing. (For details, see [LoadLibraryExW](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexw)
 documentation.) Other platform-specific prefixes and suffixes (for example, `lib`, `.so`, `.dylib`, or version numbers) must be present in _name_; they are not added automatically. See [Finding shared libraries](https://docs.python.org/3/library/ctypes.html#ctypes-finding-shared-libraries)
 for more information.

On non-Windows systems, _name_ can be `None`. In this case, `dlopen()` is called with `NULL`, which opens the main program as a “library”. (Some systems do the same if _name_ is empty; `None`/`NULL` is more portable.)

CPython implementation detail

Since CPython is linked to `libc`, a `None` _name_ is often used to access the C standard library:

Copy

\>>> printf \= ctypes.CDLL(None).printf
\>>> printf.argtypes \= \[ctypes.c\_char\_p\]
\>>> printf(b"hello\\n")
hello
6

To access the Python C API, prefer [`ctypes.pythonapi`](https://docs.python.org/3/library/ctypes.html#ctypes.pythonapi "ctypes.pythonapi")
 which works across platforms.

The _mode_ parameter can be used to specify how the library is loaded. For details, consult the _[dlopen(3)](https://manpages.debian.org/dlopen(3))
_ manpage. On Windows, _mode_ is ignored. On posix systems, RTLD\_NOW is always added, and is not configurable.

The _use\_errno_ parameter, when set to true, enables a ctypes mechanism that allows accessing the system [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.")
 error number in a safe way. `ctypes` maintains a thread-local copy of the system’s `errno` variable; if you call foreign functions created with `use_errno=True` then the `errno` value before the function call is swapped with the ctypes private copy, the same happens immediately after the function call. This mechanism only works for libraries that use the same C runtime library as the interpreter itself. A library linked against a different C runtime (for example, a different CRT on Windows) has its own `errno`, which `ctypes` cannot observe.

The function [`ctypes.get_errno()`](https://docs.python.org/3/library/ctypes.html#ctypes.get_errno "ctypes.get_errno")
 returns the value of the ctypes private copy, and the function [`ctypes.set_errno()`](https://docs.python.org/3/library/ctypes.html#ctypes.set_errno "ctypes.set_errno")
 changes the ctypes private copy to a new value and returns the former value.

The _use\_last\_error_ parameter, when set to true, enables the same mechanism for the Windows error code which is managed by the [`GetLastError()`](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "ctypes.GetLastError")
 and `SetLastError()` Windows API functions; [`ctypes.get_last_error()`](https://docs.python.org/3/library/ctypes.html#ctypes.get_last_error "ctypes.get_last_error")
 and [`ctypes.set_last_error()`](https://docs.python.org/3/library/ctypes.html#ctypes.set_last_error "ctypes.set_last_error")
 are used to request and change the ctypes private copy of the windows error code.

The _winmode_ parameter is used on Windows to specify how the library is loaded (since _mode_ is ignored). It takes any value that is valid for the Win32 API [LoadLibraryExW](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexw)
 flags parameter. When omitted, the default is to use the flags that result in the most secure DLL load, which avoids issues such as DLL hijacking. Passing the full path to the DLL is the safest way to ensure the correct library and dependencies are loaded.

On Windows creating a `CDLL` instance may fail even if the DLL name exists. When a dependent DLL of the loaded DLL is not found, a [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 error is raised with the message _“\[WinError 126\] The specified module could not be found”._ This error message does not contain the name of the missing DLL because the Windows API does not return this information making this error hard to diagnose. To resolve this error and determine which DLL is not found, you need to find the list of dependent DLLs and determine which one is not found using Windows debugging and tracing tools.

See also

[Microsoft DUMPBIN tool](https://learn.microsoft.com/en-us/cpp/build/reference/dumpbin-reference?view=msvc-170)
 – A tool to find DLL dependents.

Changed in version 3.8: Added _winmode_ parameter.

Changed in version 3.12: The _name_ parameter can now be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Instances of this class have no public methods. Functions exported by the shared library can be accessed as attributes or by index. Please note that accessing the function through an attribute caches the result and therefore accessing it repeatedly returns the same object each time. On the other hand, accessing it through an index returns a new object each time:

Copy

\>>> from ctypes import CDLL
\>>> libc \= CDLL("libc.so.6")  \# On Linux
\>>> libc.time \== libc.time
True
\>>> libc\['time'\] \== libc\['time'\]
False

The following public attributes are available. Their name starts with an underscore to not clash with exported function names:

\_handle[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL._handle "Link to this definition")

The system handle used to access the library.

\_name[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL._name "Link to this definition")

The name of the library passed in the constructor.

class ctypes.OleDLL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.OleDLL "Link to this definition")

See [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL")
, the superclass, for common information.

Functions in this library use the `stdcall` calling convention, and are assumed to return the windows specific [`HRESULT`](https://docs.python.org/3/library/ctypes.html#ctypes.HRESULT "ctypes.HRESULT")
 code. `HRESULT` values contain information specifying whether the function call failed or succeeded, together with additional error code. If the return value signals a failure, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is automatically raised.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

Changed in version 3.3: [`WindowsError`](https://docs.python.org/3/builtins/exceptions.html#WindowsError "WindowsError")
 used to be raised, which is now an alias of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

class ctypes.WinDLL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.WinDLL "Link to this definition")

See [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL")
, the superclass, for common information.

Functions in these libraries use the `stdcall` calling convention, and are assumed to return int by default.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

class ctypes.PyDLL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL "Link to this definition")

See [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL")
, the superclass, for common information.

When functions in this library are called, the Python GIL is _not_ released during the function call, and after the function execution the Python error flag is checked. If the error flag is set, a Python exception is raised.

Thus, this is only useful to call Python C API functions directly.

ctypes.RTLD\_GLOBAL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.RTLD_GLOBAL "Link to this definition")

Flag to use as _mode_ parameter. On platforms where this flag is not available, it is defined as the integer zero.

ctypes.RTLD\_LOCAL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.RTLD_LOCAL "Link to this definition")

Flag to use as _mode_ parameter. On platforms where this is not available, it is the same as _RTLD\_GLOBAL_.

ctypes.DEFAULT\_MODE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.DEFAULT_MODE "Link to this definition")

The default mode which is used to load shared libraries. On OSX 10.3, this is _RTLD\_GLOBAL_, otherwise it is the same as _RTLD\_LOCAL_.

Shared libraries can also be loaded by using one of the prefabricated objects, which are instances of the [`LibraryLoader`](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader "ctypes.LibraryLoader")
 class, either by calling the [`LoadLibrary()`](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader.LoadLibrary "ctypes.LibraryLoader.LoadLibrary")
 method, or by retrieving the library as attribute of the loader instance.

class ctypes.LibraryLoader(_dlltype_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader "Link to this definition")

Class which loads shared libraries. _dlltype_ should be one of the [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL")
, [`PyDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL "ctypes.PyDLL")
, [`WinDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.WinDLL "ctypes.WinDLL")
, or [`OleDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.OleDLL "ctypes.OleDLL")
 types.

`__getattr__()` has special behavior: It allows loading a shared library by accessing it as attribute of a library loader instance. The result is cached, so repeated attribute accesses return the same library each time.

LoadLibrary(_name_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.LibraryLoader.LoadLibrary "Link to this definition")

Load a shared library into the process and return it. This method always returns a new instance of the library.

These prefabricated library loaders are available:

> ctypes.cdll[¶](https://docs.python.org/3/library/ctypes.html#ctypes.cdll "Link to this definition")
> 
> Creates [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL")
>  instances.
> 
> ctypes.windll[¶](https://docs.python.org/3/library/ctypes.html#ctypes.windll "Link to this definition")
> 
> Creates [`WinDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.WinDLL "ctypes.WinDLL")
>  instances.
> 
> [Availability](https://docs.python.org/3/library/intro.html#availability)
> : Windows
> 
> ctypes.oledll[¶](https://docs.python.org/3/library/ctypes.html#ctypes.oledll "Link to this definition")
> 
> Creates [`OleDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.OleDLL "ctypes.OleDLL")
>  instances.
> 
> [Availability](https://docs.python.org/3/library/intro.html#availability)
> : Windows
> 
> ctypes.pydll[¶](https://docs.python.org/3/library/ctypes.html#ctypes.pydll "Link to this definition")
> 
> Creates [`PyDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL "ctypes.PyDLL")
>  instances.
> 
> ctypes.pythonapi[¶](https://docs.python.org/3/library/ctypes.html#ctypes.pythonapi "Link to this definition")
> 
> An instance of [`PyDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.PyDLL "ctypes.PyDLL")
>  that exposes Python C API functions as attributes. Note that all these functions are assumed to return C int, which is of course not always the truth, so you have to assign the correct `restype` attribute to use these functions.
> 
> Note
> 
> If the Python interpreter is statically linked, this may be `None`.

Loading a library through any of these objects raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.dlopen` with string argument `name`, the name used to load the library.

Accessing a function on a loaded library raises an auditing event `ctypes.dlsym` with arguments `library` (the library object) and `name` (the symbol’s name as a string or integer).

In cases when only the library handle is available rather than the object, accessing a function raises an auditing event `ctypes.dlsym/handle` with arguments `handle` (the raw library handle) and `name`.

### Finding shared libraries[¶](https://docs.python.org/3/library/ctypes.html#finding-shared-libraries "Link to this heading")

When programming in a compiled language, shared libraries are accessed when compiling/linking a program, and when the program is run. The programmer specifies a short name; the C compiler, linker, and runtime dynamic library loader then interact in system-specific ways to find the filename of the library to load.

While the mapping from short names to filenames is not consistently exposed by platforms, the `ctypes.util` module provides a function, `find_library()`, that attempts to match it. However, as backwards compatibility concerns make it difficult to adjust its behavior for new platforms and configurations, the function is [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
.

If wrapping a shared library with `ctypes`, consider determining the shared library name at development time, and hardcoding it into the wrapper module instead of using `find_library()` to locate the library at runtime. Also consider adding a configuration option or environment variable to let users select a library to use, and then perhaps use `find_library()` as a default or fallback.

ctypes.util.find\_library(_name_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_library "Link to this definition")

Try to find a library and return a pathname.

_name_ is the “short” library name without any prefix like `lib`, suffix like `.so`, `.dylib` or version number. (This is the form used for the posix linker option `-l`.) The result is in a format suitable for passing to [`CDLL`](https://docs.python.org/3/library/ctypes.html#ctypes.CDLL "ctypes.CDLL")
.

If no library can be found, return `None`.

The exact functionality is system dependent, and is _not guaranteed_ to match the behavior of the compiler, linker, and loader used for (or by) Python. It is recommended to only use this function as a default or fallback,

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: This function is kept for use in cases where it works, but not expected to be updated for additional platforms and configurations.

On Linux, `find_library()` tries to run external programs (`/sbin/ldconfig`, `gcc`, `objdump` and `ld`) to find the library file. If the output of these programs does not correspond to the dynamic linker used by Python, the result of this function may be misleading.

Changed in version 3.6: On Linux, the value of the environment variable `LD_LIBRARY_PATH` is used when searching for libraries, if a library cannot be found by any other means.

Here are some examples:

Copy

\>>> from ctypes.util import find\_library
\>>> find\_library("m")
'libm.so.6'
\>>> find\_library("c")
'libc.so.6'
\>>> find\_library("bz2")
'libbz2.so.1.0'
\>>>

On macOS and Android, `find_library()` uses the system’s standard naming schemes and paths to locate the library, and returns a full pathname if successful:

Copy

\>>> from ctypes.util import find\_library
\>>> find\_library("c")
'/usr/lib/libc.dylib'
\>>> find\_library("m")
'/usr/lib/libm.dylib'
\>>> find\_library("bz2")
'/usr/lib/libbz2.dylib'
\>>> find\_library("AGL")
'/System/Library/Frameworks/AGL.framework/AGL'
\>>>

On Windows, `find_library()` searches along the system search path, and returns the full pathname, but since there is no predefined naming scheme a call like `find_library("c")` will fail and return `None`.

ctypes.util.find\_msvcrt()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.util.find_msvcrt "Link to this definition")

Returns the filename of the VC runtime library used by Python, and by the extension modules.

If the name of the library cannot be determined, `None` is returned. Notably, this will happen for recent versions of the VC runtime library, which are not directly loadable.

If you need to free memory, for example, allocated by an extension module with a call to the `free(void *)`, it is important that you use the function in the same library that allocated the memory.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

### Listing loaded shared libraries[¶](https://docs.python.org/3/library/ctypes.html#listing-loaded-shared-libraries "Link to this heading")

When writing code that relies on code loaded from shared libraries, it can be useful to know which shared libraries have already been loaded into the current process.

The `ctypes.util` module provides the [`dllist()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.dllist "ctypes.util.dllist")
 function, which calls the different APIs provided by the various platforms to help determine which shared libraries have already been loaded into the current process.

The exact output of this function will be system dependent. On most platforms, the first entry of this list represents the current process itself, which may be an empty string. For example, on glibc-based Linux, the return may look like:

Copy

\>>> from ctypes.util import dllist
\>>> dllist()
\['', 'linux-vdso.so.1', '/lib/x86\_64-linux-gnu/libm.so.6', '/lib/x86\_64-linux-gnu/libc.so.6', ... \]

### Foreign functions[¶](https://docs.python.org/3/library/ctypes.html#foreign-functions "Link to this heading")

As explained in the previous section, foreign functions can be accessed as attributes of loaded shared libraries. The function objects created in this way by default accept any number of arguments, accept any ctypes data instances as arguments, and return the default result type specified by the library loader.

They are instances of a private local class `_FuncPtr` (not exposed in `ctypes`) which inherits from the private [`_CFuncPtr`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr "ctypes._CFuncPtr")
 class:

Copy

\>>> import ctypes
\>>> lib \= ctypes.CDLL(None)
\>>> issubclass(lib.\_FuncPtr, ctypes.\_CFuncPtr)
True
\>>> lib.\_FuncPtr is ctypes.\_CFuncPtr
False

class ctypes.\_CFuncPtr[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr "Link to this definition")

Base class for C callable foreign functions.

Instances of foreign functions are also C compatible data types; they represent C function pointers.

This behavior can be customized by assigning to special attributes of the foreign function object.

restype[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "Link to this definition")

Assign a ctypes type to specify the result type of the foreign function. Use `None` for void, a function not returning anything.

It is possible to assign a callable Python object that is not a ctypes type, in this case the function is assumed to return a C int, and the callable will be called with this integer, allowing further processing or error checking. Using this is deprecated, for more flexible post processing or error checking use a ctypes data type as `restype` and assign a callable to the [`errcheck`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "ctypes._CFuncPtr.errcheck")
 attribute.

argtypes[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "Link to this definition")

Assign a tuple of ctypes types to specify the argument types that the function accepts. [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised if the function is called with fewer arguments than the length of this tuple. Functions using the `stdcall` calling convention also raise `TypeError` if called with more arguments; functions using the `cdecl` calling convention accept additional, unspecified arguments as well.

When a foreign function is called, each actual argument is passed to the [`from_param()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "ctypes._CData.from_param")
 class method of the items in the [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 tuple, this method allows adapting the actual argument to an object that the foreign function accepts. For example, a [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p")
 item in the `argtypes` tuple will adapt a bytes object passed as an argument to a C pointer to its contents. It does not accept a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object.

New: It is now possible to put items in argtypes which are not ctypes types, but each item must have a [`from_param()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "ctypes._CData.from_param")
 method which returns a value usable as argument (integer, string, ctypes instance). This allows defining adapters that can adapt custom objects as function parameters.

errcheck[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "Link to this definition")

Assign a Python function or another callable to this attribute. The callable will be called with three or more arguments:

callable(_result_, _func_, _arguments_)

_result_ is what the foreign function returns, as specified by the `restype` attribute.

_func_ is the foreign function object itself, this allows reusing the same callable object to check or post process the results of several functions.

_arguments_ is a tuple containing the parameters passed to the function call, including any output parameters that `ctypes` created for the call; this allows specializing the behavior on the arguments used.

If the callable returns the _arguments_ tuple it received, unchanged, `ctypes` continues its normal processing of the result, which includes returning output parameters (see [Function prototypes](https://docs.python.org/3/library/ctypes.html#ctypes-function-prototypes)
). Any other object returned by the callable is returned from the foreign function call instead. The callable can also check the result value and raise an exception if the foreign function call failed.

For example, this callable raises an exception when the foreign function signals failure with a negative return value, and otherwise leaves the result to `ctypes`:

Copy

def errcheck(result, func, arguments):
    if result < 0:
        raise RuntimeError(f"call failed with error {result}")
    return arguments

This one instead replaces the result, converting a C `int` used as a boolean into a [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
:

Copy

def errcheck(result, func, arguments):
    return result != 0

On Windows, when a foreign function call raises a system exception (for example, due to an access violation), it will be captured and replaced with a suitable Python exception. Further, an auditing event `ctypes.set_exception` with argument `code` will be raised, allowing an audit hook to replace the exception with its own.

Some ways to invoke foreign function calls as well as some of the functions in this module may raise an auditing event `ctypes.call_function` with arguments `function pointer` and `arguments`.

### Function prototypes[¶](https://docs.python.org/3/library/ctypes.html#function-prototypes "Link to this heading")

Foreign functions can also be created by instantiating function prototypes. Function prototypes are similar to function prototypes in C; they describe a function (return type, argument types, calling convention) without defining an implementation. The factory functions must be called with the desired result type and the argument types of the function, and can be used as decorator factories, and as such, be applied to functions through the `@wrapper` syntax. See [Callback functions](https://docs.python.org/3/library/ctypes.html#ctypes-callback-functions)
 for examples.

ctypes.CFUNCTYPE(_restype_, _\*argtypes_, _use\_errno\=False_, _use\_last\_error\=False_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE "Link to this definition")

The returned function prototype creates functions that use the standard C calling convention. The function will release the GIL during the call. If _use\_errno_ is set to true, the ctypes private copy of the system [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.")
 variable is exchanged with the real `errno` value before and after the call; _use\_last\_error_ does the same for the Windows error code.

ctypes.WINFUNCTYPE(_restype_, _\*argtypes_, _use\_errno\=False_, _use\_last\_error\=False_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.WINFUNCTYPE "Link to this definition")

The returned function prototype creates functions that use the `stdcall` calling convention. The function will release the GIL during the call. _use\_errno_ and _use\_last\_error_ have the same meaning as above.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

ctypes.PYFUNCTYPE(_restype_, _\*argtypes_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.PYFUNCTYPE "Link to this definition")

The returned function prototype creates functions that use the Python calling convention. Unlike [`CFUNCTYPE()`](https://docs.python.org/3/library/ctypes.html#ctypes.CFUNCTYPE "ctypes.CFUNCTYPE")
 and [`WINFUNCTYPE()`](https://docs.python.org/3/library/ctypes.html#ctypes.WINFUNCTYPE "ctypes.WINFUNCTYPE")
, ctypes does _not_ release the GIL before calling the foreign function, so the function may safely use the Python C API. Note that this does not prevent the GIL from being released _during_ the call.

Function prototypes created by these factory functions can be instantiated in different ways, depending on the type and number of the parameters in the call:

prototype(_address_)

Returns a foreign function at the specified address which must be an integer.

prototype(_callable_)

Create a C callable function (a callback function) from a Python _callable_.

prototype(_func\_spec_\[, _paramflags_\])

Returns a foreign function exported by a shared library. _func\_spec_ must be a 2-tuple `(name_or_ordinal, library)`. The first item is the name of the exported function as string, or the ordinal of the exported function as small integer. The second item is the shared library instance.

prototype(_vtbl\_index_, _name_\[, _paramflags_\[, _iid_\]\])

Returns a foreign function that will call a COM method. _vtbl\_index_ is the index into the virtual function table, a small non-negative integer. _name_ is name of the COM method. _iid_ is an optional pointer to the interface identifier which is used in extended error reporting.

If _iid_ is not specified, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised if the COM method call fails. If _iid_ is specified, a [`COMError`](https://docs.python.org/3/library/ctypes.html#ctypes.COMError "ctypes.COMError")
 is raised instead.

COM methods use a special calling convention: They require a pointer to the COM interface as first argument, in addition to those parameters that are specified in the `argtypes` tuple.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

The optional _paramflags_ parameter creates foreign function wrappers with much more functionality than the features described above.

_paramflags_ must be a tuple of the same length as [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
.

Each item in this tuple contains further information about a parameter, it must be a tuple containing one, two, or three items.

The first item is an integer containing a combination of direction flags for the parameter:

> 1
> 
> Specifies an input parameter to the function.
> 
> 2
> 
> Output parameter. The foreign function fills in a value.
> 
> 4
> 
> Input parameter which defaults to the integer zero.

The optional second item is the parameter name as string. If this is specified, the foreign function can be called with named parameters.

The optional third item is the default value for this parameter.

The following example demonstrates how to wrap the Windows `MessageBoxW` function so that it supports default parameters and named arguments. The C declaration from the windows header file is this:

Copy

WINUSERAPI int WINAPI
MessageBoxW(
    HWND hWnd,
    LPCWSTR lpText,
    LPCWSTR lpCaption,
    UINT uType);

Here is the wrapping with `ctypes`:

Copy

\>>> from ctypes import c\_int, WINFUNCTYPE, windll
\>>> from ctypes.wintypes import HWND, LPCWSTR, UINT
\>>> prototype \= WINFUNCTYPE(c\_int, HWND, LPCWSTR, LPCWSTR, UINT)
\>>> paramflags \= (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", "Hello from ctypes"), (1, "flags", 0)
\>>> MessageBox \= prototype(("MessageBoxW", windll.user32), paramflags)

The `MessageBox` foreign function can now be called in these ways:

Copy

\>>> MessageBox()
\>>> MessageBox(text\="Spam, spam, spam")
\>>> MessageBox(flags\=2, text\="foo bar")

A second example demonstrates output parameters. The win32 `GetWindowRect` function retrieves the dimensions of a specified window by copying them into `RECT` structure that the caller has to supply. Here is the C declaration:

Copy

WINUSERAPI BOOL WINAPI
GetWindowRect(
     HWND hWnd,
     LPRECT lpRect);

Here is the wrapping with `ctypes`:

Copy

\>>> from ctypes import POINTER, WINFUNCTYPE, windll, WinError
\>>> from ctypes.wintypes import BOOL, HWND, RECT
\>>> prototype \= WINFUNCTYPE(BOOL, HWND, POINTER(RECT))
\>>> paramflags \= (1, "hwnd"), (2, "lprect")
\>>> GetWindowRect \= prototype(("GetWindowRect", windll.user32), paramflags)
\>>>

Functions with output parameters will automatically return the output parameter value if there is a single one, or a tuple containing the output parameter values when there are more than one, so the GetWindowRect function now returns a RECT instance, when called.

Output parameters can be combined with the [`errcheck`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "ctypes._CFuncPtr.errcheck")
 protocol to do further output processing and error checking. The win32 `GetWindowRect` api function returns a `BOOL` to signal success or failure, so this function could do the error checking, and raises an exception when the api call failed:

Copy

\>>> def errcheck(result, func, args):
...     if not result:
...         raise WinError()
...     return args
...
\>>> GetWindowRect.errcheck \= errcheck
\>>>

If the [`errcheck`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.errcheck "ctypes._CFuncPtr.errcheck")
 function returns the argument tuple it receives unchanged, `ctypes` continues the normal processing it does on the output parameters. If you want to return a tuple of window coordinates instead of a `RECT` instance, you can retrieve the fields in the function and return them instead, the normal processing will no longer take place:

Copy

\>>> def errcheck(result, func, args):
...     if not result:
...         raise WinError()
...     rc \= args\[1\]
...     return rc.left, rc.top, rc.bottom, rc.right
...
\>>> GetWindowRect.errcheck \= errcheck
\>>>

### Utility functions[¶](https://docs.python.org/3/library/ctypes.html#utility-functions "Link to this heading")

ctypes.addressof(_obj_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.addressof "Link to this definition")

Returns the address of the memory buffer as integer. _obj_ must be an instance of a ctypes type.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.addressof` with argument `obj`.

ctypes.alignment(_obj\_or\_type_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.alignment "Link to this definition")

Returns the alignment requirements of a ctypes type. _obj\_or\_type_ must be a ctypes type or instance.

ctypes.byref(_obj_\[, _offset_\])[¶](https://docs.python.org/3/library/ctypes.html#ctypes.byref "Link to this definition")

Returns a light-weight pointer to _obj_, which must be an instance of a ctypes type. _offset_ defaults to zero, and must be an integer that will be added to the internal pointer value.

`byref(obj, offset)` corresponds to this C code:

Copy

(((char \*)&obj) + offset)

The returned object can only be used as a foreign function call parameter. It behaves similar to `pointer(obj)`, but the construction is a lot faster.

ctypes.CopyComPointer(_src_, _dst_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CopyComPointer "Link to this definition")

Copies a COM pointer from _src_ to _dst_ and returns the Windows specific `HRESULT` value.

If _src_ is not `NULL`, its `AddRef` method is called, incrementing the reference count.

In contrast, the reference count of _dst_ will not be decremented before assigning the new value. Unless _dst_ is `NULL`, the caller is responsible for decrementing the reference count by calling its `Release` method when necessary.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

Added in version 3.14.

ctypes.cast(_obj_, _type_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.cast "Link to this definition")

This function is similar to the cast operator in C. It returns a new instance of _type_ which points to the same memory block as _obj_. _type_ must be a pointer type, and _obj_ must be an object that can be interpreted as a pointer.

ctypes.create\_string\_buffer(_init_, _size\=None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.create_string_buffer "Link to this definition")

ctypes.create\_string\_buffer(_size_)

This function creates a mutable character buffer. The returned object is a ctypes array of [`c_char`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "ctypes.c_char")
.

If _size_ is given (and not `None`), it must be an [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
. It specifies the size of the returned array.

If the _init_ argument is given, it must be [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
. It is used to initialize the array items. Bytes not initialized this way are set to zero (NUL).

If _size_ is not given (or if it is `None`), the buffer is made one element larger than _init_, effectively adding a NUL terminator.

If both arguments are given, _size_ must not be less than `len(init)`.

Warning

If _size_ is equal to `len(init)`, a NUL terminator is not added. Do not treat such a buffer as a C string.

For example:

Copy

\>>> bytes(create\_string\_buffer(2))
b'\\x00\\x00'
\>>> bytes(create\_string\_buffer(b'ab'))
b'ab\\x00'
\>>> bytes(create\_string\_buffer(b'ab', 2))
b'ab'
\>>> bytes(create\_string\_buffer(b'ab', 4))
b'ab\\x00\\x00'
\>>> bytes(create\_string\_buffer(b'abcdef', 2))
Traceback (most recent call last):
   ...
ValueError: byte string too long

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.create_string_buffer` with arguments `init`, `size`.

ctypes.create\_unicode\_buffer(_init_, _size\=None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.create_unicode_buffer "Link to this definition")

ctypes.create\_unicode\_buffer(_size_)

This function creates a mutable unicode character buffer. The returned object is a ctypes array of [`c_wchar`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar "ctypes.c_wchar")
.

The function takes the same arguments as [`create_string_buffer()`](https://docs.python.org/3/library/ctypes.html#ctypes.create_string_buffer "ctypes.create_string_buffer")
 except _init_ must be a string and _size_ counts [`c_wchar`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar "ctypes.c_wchar")
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.create_unicode_buffer` with arguments `init`, `size`.

ctypes.DllCanUnloadNow()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.DllCanUnloadNow "Link to this definition")

This function is a hook which allows implementing in-process COM servers with ctypes. It is called from the DllCanUnloadNow function that the \_ctypes extension dll exports.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

ctypes.DllGetClassObject()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.DllGetClassObject "Link to this definition")

This function is a hook which allows implementing in-process COM servers with ctypes. It is called from the DllGetClassObject function that the `_ctypes` extension dll exports.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

ctypes.util.dllist()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.util.dllist "Link to this definition")

Try to provide a list of paths of the shared libraries loaded into the current process. These paths are not normalized or processed in any way. The function can raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 if the underlying platform APIs fail. The exact functionality is system dependent.

On most platforms, the first element of the list represents the current executable file. It may be an empty string.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows, macOS, iOS, glibc, BSD libc, musl

Added in version 3.14.

ctypes.FormatError(\[_code_\])[¶](https://docs.python.org/3/library/ctypes.html#ctypes.FormatError "Link to this definition")

Returns a textual description of the error code _code_. If no error code is specified, the last error code is used by calling the Windows API function [`GetLastError()`](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "ctypes.GetLastError")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

ctypes.GetLastError()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "Link to this definition")

Returns the last error code set by Windows in the calling thread. This function calls the Windows `GetLastError()` function directly, it does not return the ctypes-private copy of the error code.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

ctypes.get\_errno()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.get_errno "Link to this definition")

Returns the current value of the ctypes-private copy of the system [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.")
 variable in the calling thread.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.get_errno` with no arguments.

ctypes.get\_last\_error()[¶](https://docs.python.org/3/library/ctypes.html#ctypes.get_last_error "Link to this definition")

Returns the current value of the ctypes-private copy of the system `LastError` variable in the calling thread.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.get_last_error` with no arguments.

ctypes.memmove(_dst_, _src_, _count_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.memmove "Link to this definition")

Same as the standard C memmove library function: copies _count_ bytes from _src_ to _dst_. _dst_ and _src_ must be integers or ctypes instances that can be converted to pointers.

ctypes.memset(_dst_, _c_, _count_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.memset "Link to this definition")

Same as the standard C memset library function: fills the memory block at address _dst_ with _count_ bytes of value _c_. _dst_ must be an integer specifying an address, or a ctypes instance.

ctypes.POINTER(_type_, _/_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "Link to this definition")

Create or return a ctypes pointer type. Pointer types are cached and reused internally, so calling this function repeatedly is cheap. _type_ must be a ctypes type.

**CPython implementation detail:** The resulting pointer type is cached in the `__pointer_type__` attribute of _type_. It is possible to set this attribute before the first call to `POINTER` in order to set a custom pointer type. However, doing this is discouraged: manually creating a suitable pointer type is difficult without relying on implementation details that may change in future Python versions.

ctypes.pointer(_obj_, _/_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "Link to this definition")

Create a new pointer instance, pointing to _obj_. The returned object is of the type `POINTER(type(obj))`.

Note: If you just want to pass a pointer to an object to a foreign function call, you should use `byref(obj)` which is much faster.

ctypes.resize(_obj_, _size_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.resize "Link to this definition")

This function resizes the internal memory buffer of _obj_, which must be an instance of a ctypes type. It is not possible to make the buffer smaller than the native size of the objects type, as given by `sizeof(type(obj))`, but it is possible to enlarge the buffer.

ctypes.set\_errno(_value_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.set_errno "Link to this definition")

Set the current value of the ctypes-private copy of the system [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.")
 variable in the calling thread to _value_ and return the previous value.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.set_errno` with argument `errno`.

ctypes.set\_last\_error(_value_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.set_last_error "Link to this definition")

Sets the current value of the ctypes-private copy of the system `LastError` variable in the calling thread to _value_ and return the previous value.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.set_last_error` with argument `error`.

ctypes.sizeof(_obj\_or\_type_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.sizeof "Link to this definition")

Returns the size in bytes of a ctypes type or instance memory buffer. Does the same as the C `sizeof` operator.

ctypes.string\_at(_ptr_, _size\=\-1_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.string_at "Link to this definition")

Return the byte string at _void \*ptr_. If _size_ is specified, it is used as size, otherwise the string is assumed to be zero-terminated.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.string_at` with arguments `ptr`, `size`.

ctypes.WinError(_code\=None_, _descr\=None_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.WinError "Link to this definition")

Creates an instance of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
. If _code_ is not specified, [`GetLastError()`](https://docs.python.org/3/library/ctypes.html#ctypes.GetLastError "ctypes.GetLastError")
 is called to determine the error code. If _descr_ is not specified, [`FormatError()`](https://docs.python.org/3/library/ctypes.html#ctypes.FormatError "ctypes.FormatError")
 is called to get a textual description of the error.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

Changed in version 3.3: An instance of [`WindowsError`](https://docs.python.org/3/builtins/exceptions.html#WindowsError "WindowsError")
 used to be created, which is now an alias of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

ctypes.wstring\_at(_ptr_, _size\=\-1_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wstring_at "Link to this definition")

Return the wide-character string at _void \*ptr_. If _size_ is specified, it is used as the number of characters of the string, otherwise the string is assumed to be zero-terminated.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.wstring_at` with arguments `ptr`, `size`.

ctypes.memoryview\_at(_ptr_, _size_, _readonly\=False_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.memoryview_at "Link to this definition")

Return a [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
 object of length _size_ that references memory starting at _void \*ptr_.

If _readonly_ is true, the returned `memoryview` object can not be used to modify the underlying memory. (Changes made by other means will still be reflected in the returned object.)

This function is similar to [`string_at()`](https://docs.python.org/3/library/ctypes.html#ctypes.string_at "ctypes.string_at")
 with the key difference of not making a copy of the specified memory. It is a semantically equivalent (but more efficient) alternative to `memoryview((c_byte * size).from_address(ptr))`. (While [`from_address()`](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_address "ctypes._CData.from_address")
 only takes integers, _ptr_ can also be given as a [`ctypes.POINTER`](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "ctypes.POINTER")
 or a [`byref()`](https://docs.python.org/3/library/ctypes.html#ctypes.byref "ctypes.byref")
 object.)

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.memoryview_at` with arguments `address`, `size`, `readonly`.

Added in version 3.14.

### Data types[¶](https://docs.python.org/3/library/ctypes.html#data-types "Link to this heading")

class ctypes.\_CData[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData "Link to this definition")

This non-public class is the common base class of all ctypes data types. Among other things, all ctypes type instances contain a memory block that hold C compatible data; the address of the memory block is returned by the [`addressof()`](https://docs.python.org/3/library/ctypes.html#ctypes.addressof "ctypes.addressof")
 helper function. Another instance variable is exposed as [`_objects`](https://docs.python.org/3/library/ctypes.html#ctypes._CData._objects "ctypes._CData._objects")
; this contains other Python objects that need to be kept alive in case the memory block contains pointers.

Common methods of ctypes data types, these are all class methods (to be exact, they are methods of the [metaclass](https://docs.python.org/3/glossary.html#term-metaclass)
):

from\_buffer(_source_\[, _offset_\])[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_buffer "Link to this definition")

This method returns a ctypes instance that shares the buffer of the _source_ object. The _source_ object must support the writeable buffer interface. The optional _offset_ parameter specifies an offset into the source buffer in bytes; the default is zero. If the source buffer is not large enough a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.cdata/buffer` with arguments `pointer`, `size`, `offset`.

from\_buffer\_copy(_source_\[, _offset_\])[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_buffer_copy "Link to this definition")

This method creates a ctypes instance, copying the buffer from the _source_ object buffer which must be readable. The optional _offset_ parameter specifies an offset into the source buffer in bytes; the default is zero. If the source buffer is not large enough a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.cdata/buffer` with arguments `pointer`, `size`, `offset`.

from\_address(_address_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_address "Link to this definition")

This method returns a ctypes type instance using the memory specified by _address_ which must be an integer.

This method, and others that indirectly call this method, raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `ctypes.cdata` with argument `address`.

from\_param(_obj_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.from_param "Link to this definition")

This method adapts _obj_ to a ctypes type. It is called with the actual object used in a foreign function call when the type is present in the foreign function’s [`argtypes`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.argtypes "ctypes._CFuncPtr.argtypes")
 tuple; it must return an object that can be used as a function call parameter.

All ctypes data types have a default implementation of this classmethod that normally returns _obj_ if that is an instance of the type. Some types accept other objects as well.

in\_dll(_library_, _name_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.in_dll "Link to this definition")

This method returns a ctypes type instance exported by a shared library. _name_ is the name of the symbol that exports the data, _library_ is the loaded shared library.

Common class variables of ctypes data types:

\_\_pointer\_type\_\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData.__pointer_type__ "Link to this definition")

The pointer type that was created by calling [`POINTER()`](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "ctypes.POINTER")
 for corresponding ctypes data type. If a pointer type was not yet created, the attribute is missing.

Added in version 3.14.

Common instance variables of ctypes data types:

\_b\_base\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData._b_base_ "Link to this definition")

Sometimes ctypes data instances do not own the memory block they contain, instead they share part of the memory block of a base object. The [`_b_base_`](https://docs.python.org/3/library/ctypes.html#ctypes._CData._b_base_ "ctypes._CData._b_base_")
 read-only member is the root ctypes object that owns the memory block.

\_b\_needsfree\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData._b_needsfree_ "Link to this definition")

This read-only variable is true when the ctypes data instance has allocated the memory block itself, false otherwise.

\_objects[¶](https://docs.python.org/3/library/ctypes.html#ctypes._CData._objects "Link to this definition")

This member is either `None` or a dictionary containing Python objects that need to be kept alive so that the memory block contents is kept valid. This object is only exposed for debugging; never modify the contents of this dictionary.

### Fundamental data types[¶](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types-2 "Link to this heading")

class ctypes.\_SimpleCData[¶](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData "Link to this definition")

This non-public class is the base class of all fundamental ctypes data types. It is mentioned here because it contains the common attributes of the fundamental ctypes data types. `_SimpleCData` is a subclass of [`_CData`](https://docs.python.org/3/library/ctypes.html#ctypes._CData "ctypes._CData")
, so it inherits their methods and attributes. ctypes data types that are not and do not contain pointers can now be pickled.

Instances have a single attribute:

value[¶](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData.value "Link to this definition")

This attribute contains the actual value of the instance. For integer and pointer types, it is an integer, for character types, it is a single character bytes object or string, for character pointer types it is a Python bytes object or string.

When the `value` attribute is retrieved from a ctypes instance, usually a new object is returned each time. `ctypes` does _not_ implement original object return, always a new object is constructed. The same is true for all other ctypes object instances.

Each subclass has a class attribute:

\_type\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData._type_ "Link to this definition")

Class attribute that contains an internal type code, as a string. See [Fundamental data types](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types)
 for a summary.

Types marked \* in the summary may be (or always are) aliases of a different `_SimpleCData` subclass, and will not necessarily use the listed type code. For example, if the platform’s long, long long and time\_t C types are the same, then [`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "ctypes.c_long")
, [`c_longlong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "ctypes.c_longlong")
 and [`c_time_t`](https://docs.python.org/3/library/ctypes.html#ctypes.c_time_t "ctypes.c_time_t")
 all refer to a single class, `c_long`, whose [`_type_`](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData._type_ "ctypes._SimpleCData._type_")
 code is `'l'`. The `'q'` code will be unused.

See also

The [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.")
 and [struct](https://docs.python.org/3/library/struct.html#type-codes)
 modules, as well as third-party modules like [numpy](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__)
, use similar – but slightly different – type codes.

Fundamental data types, when returned as foreign function call results, or, for example, by retrieving structure field members or array items, are transparently converted to native Python types. In other words, if a foreign function has a [`restype`](https://docs.python.org/3/library/ctypes.html#ctypes._CFuncPtr.restype "ctypes._CFuncPtr.restype")
 of [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p")
, you will receive a Python bytes object or `None` for a `NULL` pointer, _not_ a `c_char_p` instance.

Subclasses of fundamental data types do _not_ inherit this behavior. So, if a foreign functions `restype` is a subclass of [`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p")
, you will receive an instance of this subclass from the function call. Of course, you can get the value of the pointer by accessing the `value` attribute.

These are the fundamental ctypes data types:

class ctypes.c\_byte[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_byte "Link to this definition")

Represents the C signed char datatype, and interprets the value as small integer. The constructor accepts an optional integer initializer; no overflow checking is done.

class ctypes.c\_char[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "Link to this definition")

Represents the C char datatype, and interprets the value as a single character. The constructor accepts an optional string initializer, the length of the string must be exactly one character.

class ctypes.c\_char\_p[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "Link to this definition")

Represents the C char\* datatype when it points to a zero-terminated string. For a general character pointer that may also point to binary data, `POINTER(c_char)` must be used. The constructor accepts an integer address, or a bytes object.

class ctypes.c\_double[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_double "Link to this definition")

Represents the C double datatype. The constructor accepts an optional float initializer.

class ctypes.c\_longdouble[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_longdouble "Link to this definition")

Represents the C long double datatype. The constructor accepts an optional float initializer. On platforms where `sizeof(long double) == sizeof(double)` it is an alias to [`c_double`](https://docs.python.org/3/library/ctypes.html#ctypes.c_double "ctypes.c_double")
.

class ctypes.c\_float[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_float "Link to this definition")

Represents the C float datatype. The constructor accepts an optional float initializer.

class ctypes.c\_double\_complex[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_double_complex "Link to this definition")

Represents the C double complex datatype, if available. The constructor accepts an optional [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
 initializer.

Added in version 3.14.

class ctypes.c\_float\_complex[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_float_complex "Link to this definition")

Represents the C float complex datatype, if available. The constructor accepts an optional [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
 initializer.

Added in version 3.14.

class ctypes.c\_longdouble\_complex[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_longdouble_complex "Link to this definition")

Represents the C long double complex datatype, if available. The constructor accepts an optional [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")
 initializer.

Added in version 3.14.

class ctypes.c\_int[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "Link to this definition")

Represents the C signed int datatype. The constructor accepts an optional integer initializer; no overflow checking is done. On platforms where `sizeof(int) == sizeof(long)` it is an alias to [`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "ctypes.c_long")
.

class ctypes.c\_int8[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_int8 "Link to this definition")

Represents the C 8-bit signed int datatype. It is an alias for [`c_byte`](https://docs.python.org/3/library/ctypes.html#ctypes.c_byte "ctypes.c_byte")
.

class ctypes.c\_int16[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_int16 "Link to this definition")

Represents the C 16-bit signed int datatype. Usually an alias for [`c_short`](https://docs.python.org/3/library/ctypes.html#ctypes.c_short "ctypes.c_short")
.

class ctypes.c\_int32[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_int32 "Link to this definition")

Represents the C 32-bit signed int datatype. Usually an alias for [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int")
.

class ctypes.c\_int64[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_int64 "Link to this definition")

Represents the C 64-bit signed int datatype. Usually an alias for [`c_longlong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "ctypes.c_longlong")
.

class ctypes.c\_long[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "Link to this definition")

Represents the C signed long datatype. The constructor accepts an optional integer initializer; no overflow checking is done.

class ctypes.c\_longlong[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "Link to this definition")

Represents the C signed long long datatype. The constructor accepts an optional integer initializer; no overflow checking is done. On platforms where `sizeof(long long) == sizeof(long)` it is an alias to [`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "ctypes.c_long")
.

class ctypes.c\_short[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_short "Link to this definition")

Represents the C signed short datatype. The constructor accepts an optional integer initializer; no overflow checking is done.

class ctypes.c\_size\_t[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_size_t "Link to this definition")

Represents the C `size_t` datatype. Usually an alias for another unsigned integer type.

class ctypes.c\_ssize\_t[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_ssize_t "Link to this definition")

Represents the [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 datatype. This is a signed version of `size_t`; that is, the POSIX `ssize_t` type. Usually an alias for another integer type.

Added in version 3.2.

class ctypes.c\_time\_t[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_time_t "Link to this definition")

Represents the C `time_t` datatype. Usually an alias for another integer type.

Added in version 3.12.

class ctypes.c\_ubyte[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_ubyte "Link to this definition")

Represents the C unsigned char datatype, it interprets the value as small integer. The constructor accepts an optional integer initializer; no overflow checking is done.

class ctypes.c\_uint[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint "Link to this definition")

Represents the C unsigned int datatype. The constructor accepts an optional integer initializer; no overflow checking is done. On platforms where `sizeof(int) == sizeof(long)` it is an alias for [`c_ulong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulong "ctypes.c_ulong")
.

class ctypes.c\_uint8[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint8 "Link to this definition")

Represents the C 8-bit unsigned int datatype. It is an alias for [`c_ubyte`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ubyte "ctypes.c_ubyte")
.

class ctypes.c\_uint16[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint16 "Link to this definition")

Represents the C 16-bit unsigned int datatype. Usually an alias for [`c_ushort`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ushort "ctypes.c_ushort")
.

class ctypes.c\_uint32[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint32 "Link to this definition")

Represents the C 32-bit unsigned int datatype. Usually an alias for [`c_uint`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint "ctypes.c_uint")
.

class ctypes.c\_uint64[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint64 "Link to this definition")

Represents the C 64-bit unsigned int datatype. Usually an alias for [`c_ulonglong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulonglong "ctypes.c_ulonglong")
.

class ctypes.c\_ulong[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulong "Link to this definition")

Represents the C unsigned long datatype. The constructor accepts an optional integer initializer; no overflow checking is done.

class ctypes.c\_ulonglong[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulonglong "Link to this definition")

Represents the C unsigned long long datatype. The constructor accepts an optional integer initializer; no overflow checking is done. On platforms where `sizeof(long long) == sizeof(long)` it is an alias to [`c_ulong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulong "ctypes.c_ulong")
.

class ctypes.c\_ushort[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_ushort "Link to this definition")

Represents the C unsigned short datatype. The constructor accepts an optional integer initializer; no overflow checking is done.

class ctypes.c\_void\_p[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "Link to this definition")

Represents the C void\* type. The value is represented as integer. The constructor accepts an optional integer initializer.

class ctypes.c\_wchar[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar "Link to this definition")

Represents the C `wchar_t` datatype, and interprets the value as a single character unicode string. The constructor accepts an optional string initializer, the length of the string must be exactly one character.

class ctypes.c\_wchar\_p[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar_p "Link to this definition")

Represents the C wchar\_t\* datatype, which must be a pointer to a zero-terminated wide character string. The constructor accepts an integer address, or a string.

class ctypes.c\_bool[¶](https://docs.python.org/3/library/ctypes.html#ctypes.c_bool "Link to this definition")

Represent the C bool datatype (more accurately, \_Bool from C99). Its value can be `True` or `False`, and the constructor accepts any object that has a truth value.

class ctypes.HRESULT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.HRESULT "Link to this definition")

Represents a `HRESULT` value, which contains success or error information for a function or method call.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

class ctypes.py\_object[¶](https://docs.python.org/3/library/ctypes.html#ctypes.py_object "Link to this definition")

Represents the C [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* datatype. Calling this without an argument creates a `NULL` PyObject\* pointer.

Changed in version 3.14: `py_object` is now a [generic type](https://docs.python.org/3/glossary.html#term-generic-type)
.

### Windows data types[¶](https://docs.python.org/3/library/ctypes.html#module-ctypes.wintypes "Link to this heading")

**Source code:** [Lib/ctypes/wintypes.py](https://github.com/python/cpython/tree/3.15/Lib/ctypes/wintypes.py)

The `ctypes.wintypes` module provides types for use with Windows APIs. Most are aliases for types defined in `ctypes`. See Microsoft’s [Windows data types](https://learn.microsoft.com/en-us/windows/win32/winprog/windows-data-types)
 documentation for the corresponding C definitions. On non-Windows platforms, the sizes and layouts of these types may differ from their Windows counterparts.

Changed in version 3.14: Added [`HCONV`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HCONV "ctypes.wintypes.HCONV")
, [`HCONVLIST`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HCONVLIST "ctypes.wintypes.HCONVLIST")
, [`HCURSOR`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HCURSOR "ctypes.wintypes.HCURSOR")
, [`HDDEDATA`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HDDEDATA "ctypes.wintypes.HDDEDATA")
, [`HDROP`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HDROP "ctypes.wintypes.HDROP")
, [`HFILE`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HFILE "ctypes.wintypes.HFILE")
, [`HRESULT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HRESULT "ctypes.wintypes.HRESULT")
, and [`HSZ`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HSZ "ctypes.wintypes.HSZ")
.

For example:

Copy

\>>> from ctypes import POINTER
\>>> from ctypes.wintypes import LPRECT, RECT, SHORT
\>>> SHORT(\-1).value
\-1
\>>> rect \= RECT(0, 0, 100, 50)
\>>> rect.right, rect.bottom
(100, 50)
\>>> LPRECT is POINTER(RECT)
True

#### Simple types[¶](https://docs.python.org/3/library/ctypes.html#simple-types "Link to this heading")

The following names are aliases for fundamental `ctypes` types:

| Windows types | `ctypes` type |
| --- | --- |
| class ctypes.wintypes.BYTE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.BYTE "Link to this definition")<br><br>class ctypes.wintypes.BOOLEAN[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.BOOLEAN "Link to this definition") | [`c_ubyte`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ubyte "ctypes.c_ubyte") |
| class ctypes.wintypes.CHAR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.CHAR "Link to this definition") | [`c_char`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char "ctypes.c_char") |
| class ctypes.wintypes.WCHAR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WCHAR "Link to this definition") | [`c_wchar`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar "ctypes.c_wchar") |
| class ctypes.wintypes.WORD[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WORD "Link to this definition")<br><br>class ctypes.wintypes.USHORT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.USHORT "Link to this definition")<br><br>class ctypes.wintypes.ATOM[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.ATOM "Link to this definition")<br><br>class ctypes.wintypes.LANGID[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LANGID "Link to this definition") | [`c_ushort`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ushort "ctypes.c_ushort") |
| class ctypes.wintypes.DWORD[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.DWORD "Link to this definition")<br><br>class ctypes.wintypes.ULONG[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.ULONG "Link to this definition")<br><br>class ctypes.wintypes.COLORREF[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.COLORREF "Link to this definition")<br><br>class ctypes.wintypes.LCID[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LCID "Link to this definition")<br><br>class ctypes.wintypes.LCTYPE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LCTYPE "Link to this definition")<br><br>class ctypes.wintypes.LGRPID[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LGRPID "Link to this definition") | [`c_ulong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulong "ctypes.c_ulong") |
| class ctypes.wintypes.BOOL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.BOOL "Link to this definition")<br><br>class ctypes.wintypes.LONG[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LONG "Link to this definition")<br><br>class ctypes.wintypes.HRESULT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HRESULT "Link to this definition") | [`c_long`](https://docs.python.org/3/library/ctypes.html#ctypes.c_long "ctypes.c_long") |
| class ctypes.wintypes.INT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.INT "Link to this definition")<br><br>class ctypes.wintypes.HFILE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HFILE "Link to this definition") | [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int") |
| class ctypes.wintypes.UINT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.UINT "Link to this definition") | [`c_uint`](https://docs.python.org/3/library/ctypes.html#ctypes.c_uint "ctypes.c_uint") |
| class ctypes.wintypes.SHORT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SHORT "Link to this definition") | [`c_short`](https://docs.python.org/3/library/ctypes.html#ctypes.c_short "ctypes.c_short") |
| class ctypes.wintypes.DOUBLE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.DOUBLE "Link to this definition") | [`c_double`](https://docs.python.org/3/library/ctypes.html#ctypes.c_double "ctypes.c_double") |
| class ctypes.wintypes.FLOAT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.FLOAT "Link to this definition") | [`c_float`](https://docs.python.org/3/library/ctypes.html#ctypes.c_float "ctypes.c_float") |
| class ctypes.wintypes.LARGE\_INTEGER[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LARGE_INTEGER "Link to this definition") | [`c_longlong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longlong "ctypes.c_longlong") |
| class ctypes.wintypes.ULARGE\_INTEGER[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.ULARGE_INTEGER "Link to this definition") | [`c_ulonglong`](https://docs.python.org/3/library/ctypes.html#ctypes.c_ulonglong "ctypes.c_ulonglong") |
| class ctypes.wintypes.LPCSTR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPCSTR "Link to this definition")<br><br>class ctypes.wintypes.LPSTR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPSTR "Link to this definition") | [`c_char_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_char_p "ctypes.c_char_p") |
| class ctypes.wintypes.LPCOLESTR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPCOLESTR "Link to this definition")<br><br>class ctypes.wintypes.LPOLESTR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPOLESTR "Link to this definition")<br><br>class ctypes.wintypes.OLESTR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.OLESTR "Link to this definition")<br><br>class ctypes.wintypes.LPCWSTR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPCWSTR "Link to this definition")<br><br>class ctypes.wintypes.LPWSTR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPWSTR "Link to this definition") | [`c_wchar_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_wchar_p "ctypes.c_wchar_p") |
| class ctypes.wintypes.LPCVOID[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPCVOID "Link to this definition")<br><br>class ctypes.wintypes.LPVOID[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPVOID "Link to this definition") | [`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p") |

[`LARGE_INTEGER`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LARGE_INTEGER "ctypes.wintypes.LARGE_INTEGER")
 and [`ULARGE_INTEGER`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.ULARGE_INTEGER "ctypes.wintypes.ULARGE_INTEGER")
 expose an integer `value` attribute, with no `LowPart`, `HighPart`, or `QuadPart` fields.

class ctypes.wintypes.WPARAM[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WPARAM "Link to this definition")

An unsigned integer type with the same size as [`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p")
.

class ctypes.wintypes.LPARAM[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPARAM "Link to this definition")

A signed integer type with the same size as [`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p")
.

class ctypes.wintypes.VARIANT\_BOOL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.VARIANT_BOOL "Link to this definition")

A 16-bit Boolean type whose `value` attribute is a Python [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
. Assigning to `value` stores `-1` for a true value and `0` for a false value.

#### Handle types[¶](https://docs.python.org/3/library/ctypes.html#handle-types "Link to this heading")

class ctypes.wintypes.HANDLE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HANDLE "Link to this definition")

An alias for [`c_void_p`](https://docs.python.org/3/library/ctypes.html#ctypes.c_void_p "ctypes.c_void_p")
, used to represent Windows handles.

class ctypes.wintypes.HACCEL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HACCEL "Link to this definition")

class ctypes.wintypes.HBITMAP[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HBITMAP "Link to this definition")

class ctypes.wintypes.HBRUSH[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HBRUSH "Link to this definition")

class ctypes.wintypes.HCOLORSPACE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HCOLORSPACE "Link to this definition")

class ctypes.wintypes.HCONV[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HCONV "Link to this definition")

class ctypes.wintypes.HCONVLIST[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HCONVLIST "Link to this definition")

class ctypes.wintypes.HCURSOR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HCURSOR "Link to this definition")

class ctypes.wintypes.HDC[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HDC "Link to this definition")

class ctypes.wintypes.HDDEDATA[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HDDEDATA "Link to this definition")

class ctypes.wintypes.HDESK[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HDESK "Link to this definition")

class ctypes.wintypes.HDROP[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HDROP "Link to this definition")

class ctypes.wintypes.HDWP[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HDWP "Link to this definition")

class ctypes.wintypes.HENHMETAFILE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HENHMETAFILE "Link to this definition")

class ctypes.wintypes.HFONT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HFONT "Link to this definition")

class ctypes.wintypes.HGDIOBJ[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HGDIOBJ "Link to this definition")

class ctypes.wintypes.HGLOBAL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HGLOBAL "Link to this definition")

class ctypes.wintypes.HHOOK[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HHOOK "Link to this definition")

class ctypes.wintypes.HICON[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HICON "Link to this definition")

class ctypes.wintypes.HINSTANCE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HINSTANCE "Link to this definition")

class ctypes.wintypes.HKEY[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HKEY "Link to this definition")

class ctypes.wintypes.HKL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HKL "Link to this definition")

class ctypes.wintypes.HLOCAL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HLOCAL "Link to this definition")

class ctypes.wintypes.HMENU[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HMENU "Link to this definition")

class ctypes.wintypes.HMETAFILE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HMETAFILE "Link to this definition")

class ctypes.wintypes.HMODULE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HMODULE "Link to this definition")

class ctypes.wintypes.HMONITOR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HMONITOR "Link to this definition")

class ctypes.wintypes.HPALETTE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HPALETTE "Link to this definition")

class ctypes.wintypes.HPEN[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HPEN "Link to this definition")

class ctypes.wintypes.HRGN[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HRGN "Link to this definition")

class ctypes.wintypes.HRSRC[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HRSRC "Link to this definition")

class ctypes.wintypes.HSTR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HSTR "Link to this definition")

class ctypes.wintypes.HSZ[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HSZ "Link to this definition")

class ctypes.wintypes.HTASK[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HTASK "Link to this definition")

class ctypes.wintypes.HWINSTA[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HWINSTA "Link to this definition")

class ctypes.wintypes.HWND[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HWND "Link to this definition")

class ctypes.wintypes.SC\_HANDLE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SC_HANDLE "Link to this definition")

class ctypes.wintypes.SERVICE\_STATUS\_HANDLE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SERVICE_STATUS_HANDLE "Link to this definition")

Aliases for [`HANDLE`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HANDLE "ctypes.wintypes.HANDLE")
 for use with specific Windows APIs. [`HFILE`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HFILE "ctypes.wintypes.HFILE")
 is an alias for [`INT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.INT "ctypes.wintypes.INT")
 and is listed among the simple types above.

#### Structures[¶](https://docs.python.org/3/library/ctypes.html#structures "Link to this heading")

The following types are subclasses of [`ctypes.Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure")
.

class ctypes.wintypes.RECT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.RECT "Link to this definition")

class ctypes.wintypes.RECTL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.RECTL "Link to this definition")

class ctypes.wintypes.tagRECT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.tagRECT "Link to this definition")

A rectangle with `left`, `top`, `right`, and `bottom` fields, all of type [`LONG`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LONG "ctypes.wintypes.LONG")
.

class ctypes.wintypes.SMALL\_RECT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SMALL_RECT "Link to this definition")

A rectangle with `Left`, `Top`, `Right`, and `Bottom` fields, all of type [`SHORT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SHORT "ctypes.wintypes.SHORT")
.

class ctypes.wintypes.POINT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.POINT "Link to this definition")

class ctypes.wintypes.POINTL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.POINTL "Link to this definition")

class ctypes.wintypes.tagPOINT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.tagPOINT "Link to this definition")

A point with `x` and `y` fields, both of type [`LONG`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LONG "ctypes.wintypes.LONG")
.

class ctypes.wintypes.SIZE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SIZE "Link to this definition")

class ctypes.wintypes.SIZEL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SIZEL "Link to this definition")

class ctypes.wintypes.tagSIZE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.tagSIZE "Link to this definition")

Dimensions with `cx` and `cy` fields, both of type [`LONG`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LONG "ctypes.wintypes.LONG")
.

class ctypes.wintypes.FILETIME[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.FILETIME "Link to this definition")

A file time with `dwLowDateTime` and `dwHighDateTime` fields, both of type [`DWORD`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.DWORD "ctypes.wintypes.DWORD")
.

class ctypes.wintypes.MSG[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.MSG "Link to this definition")

class ctypes.wintypes.tagMSG[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.tagMSG "Link to this definition")

A Windows message with the following fields:

| Field | Type |
| --- | --- |
| `hWnd` | [`HWND`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HWND "ctypes.wintypes.HWND") |
| `message` | [`UINT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.UINT "ctypes.wintypes.UINT") |
| `wParam` | [`WPARAM`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WPARAM "ctypes.wintypes.WPARAM") |
| `lParam` | [`LPARAM`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPARAM "ctypes.wintypes.LPARAM") |
| `time` | [`DWORD`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.DWORD "ctypes.wintypes.DWORD") |
| `pt` | [`POINT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.POINT "ctypes.wintypes.POINT") |

class ctypes.wintypes.WIN32\_FIND\_DATAA[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WIN32_FIND_DATAA "Link to this definition")

class ctypes.wintypes.WIN32\_FIND\_DATAW[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WIN32_FIND_DATAW "Link to this definition")

Structures used by Windows file-search functions, with the following fields. `WIN32_FIND_DATAA` uses [`CHAR`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.CHAR "ctypes.wintypes.CHAR")
 for its file names, and `WIN32_FIND_DATAW` uses [`WCHAR`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WCHAR "ctypes.wintypes.WCHAR")
.

| Fields | Type |
| --- | --- |
| `dwFileAttributes` | [`DWORD`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.DWORD "ctypes.wintypes.DWORD") |
| `ftCreationTime`, `ftLastAccessTime`, `ftLastWriteTime` | [`FILETIME`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.FILETIME "ctypes.wintypes.FILETIME") |
| `nFileSizeHigh`, `nFileSizeLow` | [`DWORD`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.DWORD "ctypes.wintypes.DWORD") |
| `dwReserved0`, `dwReserved1` | [`DWORD`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.DWORD "ctypes.wintypes.DWORD") |
| `cFileName` | An array of [`MAX_PATH`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.MAX_PATH "ctypes.wintypes.MAX_PATH")<br> characters |
| `cAlternateFileName` | An array of 14 characters |

#### Pointer types[¶](https://docs.python.org/3/library/ctypes.html#pointer-types "Link to this heading")

The following names are aliases for `ctypes.POINTER(T)`, where _T_ is the type in the second column:

| Pointer types | Referenced type |
| --- | --- |
| class ctypes.wintypes.LPBOOL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPBOOL "Link to this definition")<br><br>class ctypes.wintypes.PBOOL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PBOOL "Link to this definition") | [`BOOL`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.BOOL "ctypes.wintypes.BOOL") |
| class ctypes.wintypes.PBOOLEAN[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PBOOLEAN "Link to this definition") | [`BOOLEAN`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.BOOLEAN "ctypes.wintypes.BOOLEAN") |
| class ctypes.wintypes.LPBYTE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPBYTE "Link to this definition")<br><br>class ctypes.wintypes.PBYTE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PBYTE "Link to this definition") | [`BYTE`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.BYTE "ctypes.wintypes.BYTE") |
| class ctypes.wintypes.PCHAR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PCHAR "Link to this definition") | [`CHAR`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.CHAR "ctypes.wintypes.CHAR") |
| class ctypes.wintypes.LPCOLORREF[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPCOLORREF "Link to this definition") | [`COLORREF`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.COLORREF "ctypes.wintypes.COLORREF") |
| class ctypes.wintypes.LPDWORD[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPDWORD "Link to this definition")<br><br>class ctypes.wintypes.PDWORD[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PDWORD "Link to this definition") | [`DWORD`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.DWORD "ctypes.wintypes.DWORD") |
| class ctypes.wintypes.LPFILETIME[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPFILETIME "Link to this definition")<br><br>class ctypes.wintypes.PFILETIME[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PFILETIME "Link to this definition") | [`FILETIME`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.FILETIME "ctypes.wintypes.FILETIME") |
| class ctypes.wintypes.PFLOAT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PFLOAT "Link to this definition") | [`FLOAT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.FLOAT "ctypes.wintypes.FLOAT") |
| class ctypes.wintypes.LPHANDLE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPHANDLE "Link to this definition")<br><br>class ctypes.wintypes.PHANDLE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PHANDLE "Link to this definition") | [`HANDLE`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HANDLE "ctypes.wintypes.HANDLE") |
| class ctypes.wintypes.PHKEY[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PHKEY "Link to this definition") | [`HKEY`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HKEY "ctypes.wintypes.HKEY") |
| class ctypes.wintypes.LPHKL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPHKL "Link to this definition") | [`HKL`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.HKL "ctypes.wintypes.HKL") |
| class ctypes.wintypes.LPINT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPINT "Link to this definition")<br><br>class ctypes.wintypes.PINT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PINT "Link to this definition") | [`INT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.INT "ctypes.wintypes.INT") |
| class ctypes.wintypes.PLARGE\_INTEGER[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PLARGE_INTEGER "Link to this definition") | [`LARGE_INTEGER`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LARGE_INTEGER "ctypes.wintypes.LARGE_INTEGER") |
| class ctypes.wintypes.PLCID[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PLCID "Link to this definition") | [`LCID`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LCID "ctypes.wintypes.LCID") |
| class ctypes.wintypes.LPLONG[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPLONG "Link to this definition")<br><br>class ctypes.wintypes.PLONG[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PLONG "Link to this definition") | [`LONG`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LONG "ctypes.wintypes.LONG") |
| class ctypes.wintypes.LPMSG[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPMSG "Link to this definition")<br><br>class ctypes.wintypes.PMSG[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PMSG "Link to this definition") | [`MSG`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.MSG "ctypes.wintypes.MSG") |
| class ctypes.wintypes.LPPOINT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPPOINT "Link to this definition")<br><br>class ctypes.wintypes.PPOINT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PPOINT "Link to this definition") | [`POINT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.POINT "ctypes.wintypes.POINT") |
| class ctypes.wintypes.PPOINTL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PPOINTL "Link to this definition") | [`POINTL`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.POINTL "ctypes.wintypes.POINTL") |
| class ctypes.wintypes.LPRECT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPRECT "Link to this definition")<br><br>class ctypes.wintypes.PRECT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PRECT "Link to this definition") | [`RECT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.RECT "ctypes.wintypes.RECT") |
| class ctypes.wintypes.LPRECTL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPRECTL "Link to this definition")<br><br>class ctypes.wintypes.PRECTL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PRECTL "Link to this definition") | [`RECTL`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.RECTL "ctypes.wintypes.RECTL") |
| class ctypes.wintypes.LPSC\_HANDLE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPSC_HANDLE "Link to this definition") | [`SC_HANDLE`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SC_HANDLE "ctypes.wintypes.SC_HANDLE") |
| class ctypes.wintypes.PSHORT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PSHORT "Link to this definition") | [`SHORT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SHORT "ctypes.wintypes.SHORT") |
| class ctypes.wintypes.LPSIZE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPSIZE "Link to this definition")<br><br>class ctypes.wintypes.PSIZE[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PSIZE "Link to this definition") | [`SIZE`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SIZE "ctypes.wintypes.SIZE") |
| class ctypes.wintypes.LPSIZEL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPSIZEL "Link to this definition")<br><br>class ctypes.wintypes.PSIZEL[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PSIZEL "Link to this definition") | [`SIZEL`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SIZEL "ctypes.wintypes.SIZEL") |
| class ctypes.wintypes.PSMALL\_RECT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PSMALL_RECT "Link to this definition") | [`SMALL_RECT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.SMALL_RECT "ctypes.wintypes.SMALL_RECT") |
| class ctypes.wintypes.LPUINT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPUINT "Link to this definition")<br><br>class ctypes.wintypes.PUINT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PUINT "Link to this definition") | [`UINT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.UINT "ctypes.wintypes.UINT") |
| class ctypes.wintypes.PULARGE\_INTEGER[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PULARGE_INTEGER "Link to this definition") | [`ULARGE_INTEGER`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.ULARGE_INTEGER "ctypes.wintypes.ULARGE_INTEGER") |
| class ctypes.wintypes.PULONG[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PULONG "Link to this definition") | [`ULONG`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.ULONG "ctypes.wintypes.ULONG") |
| class ctypes.wintypes.PUSHORT[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PUSHORT "Link to this definition") | [`USHORT`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.USHORT "ctypes.wintypes.USHORT") |
| class ctypes.wintypes.PWCHAR[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PWCHAR "Link to this definition") | [`WCHAR`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WCHAR "ctypes.wintypes.WCHAR") |
| class ctypes.wintypes.LPWIN32\_FIND\_DATAA[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPWIN32_FIND_DATAA "Link to this definition")<br><br>class ctypes.wintypes.PWIN32\_FIND\_DATAA[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PWIN32_FIND_DATAA "Link to this definition") | [`WIN32_FIND_DATAA`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WIN32_FIND_DATAA "ctypes.wintypes.WIN32_FIND_DATAA") |
| class ctypes.wintypes.LPWIN32\_FIND\_DATAW[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPWIN32_FIND_DATAW "Link to this definition")<br><br>class ctypes.wintypes.PWIN32\_FIND\_DATAW[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PWIN32_FIND_DATAW "Link to this definition") | [`WIN32_FIND_DATAW`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WIN32_FIND_DATAW "ctypes.wintypes.WIN32_FIND_DATAW") |
| class ctypes.wintypes.LPWORD[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.LPWORD "Link to this definition")<br><br>class ctypes.wintypes.PWORD[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.PWORD "Link to this definition") | [`WORD`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WORD "ctypes.wintypes.WORD") |

#### Constants and functions[¶](https://docs.python.org/3/library/ctypes.html#constants-and-functions "Link to this heading")

ctypes.wintypes.MAX\_PATH[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.MAX_PATH "Link to this definition")

The value `260`, used as the size of the file-name arrays in [`WIN32_FIND_DATAA`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WIN32_FIND_DATAA "ctypes.wintypes.WIN32_FIND_DATAA")
 and [`WIN32_FIND_DATAW`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.WIN32_FIND_DATAW "ctypes.wintypes.WIN32_FIND_DATAW")
.

ctypes.wintypes.RGB(_red_, _green_, _blue_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.RGB "Link to this definition")

Return a [`COLORREF`](https://docs.python.org/3/library/ctypes.html#ctypes.wintypes.COLORREF "ctypes.wintypes.COLORREF")
 value as a Python integer. The _red_, _green_, and _blue_ arguments are integers from `0` to `255`, specifying the intensity of each color component:

Copy

\>>> from ctypes.wintypes import RGB
\>>> hex(RGB(255, 128, 0))
'0x80ff'

### Structured data types[¶](https://docs.python.org/3/library/ctypes.html#structured-data-types "Link to this heading")

class ctypes.Union(_\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Union "Link to this definition")

Abstract base class for unions in native byte order.

Unions share common attributes and behavior with structures; see [`Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure")
 documentation for details.

class ctypes.BigEndianUnion(_\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianUnion "Link to this definition")

Abstract base class for unions in _big endian_ byte order.

Added in version 3.11.

class ctypes.LittleEndianUnion(_\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianUnion "Link to this definition")

Abstract base class for unions in _little endian_ byte order.

Added in version 3.11.

class ctypes.BigEndianStructure(_\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.BigEndianStructure "Link to this definition")

Abstract base class for structures in _big endian_ byte order.

class ctypes.LittleEndianStructure(_\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.LittleEndianStructure "Link to this definition")

Abstract base class for structures in _little endian_ byte order.

Structures and unions with non-native byte order cannot contain pointer type fields, or any other data types containing pointer type fields.

class ctypes.Structure(_\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "Link to this definition")

Abstract base class for structures in _native_ byte order.

Concrete structure and union types must be created by subclassing one of these types, and at least define a [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 class variable. `ctypes` will create [descriptor](https://docs.python.org/3/glossary.html#term-descriptor)
s which allow reading and writing the fields by direct attribute accesses.

\_fields\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "Link to this definition")

A sequence defining the structure fields. The items must be 2-tuples or 3-tuples. The first item is the name of the field, the second item specifies the type of the field; it can be any ctypes data type.

For integer type fields like [`c_int`](https://docs.python.org/3/library/ctypes.html#ctypes.c_int "ctypes.c_int")
, a third optional item can be given. It must be a small positive integer defining the bit width of the field.

Field names must be unique within one structure or union. This is not checked, only one field can be accessed when names are repeated.

It is possible to define the [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 class variable _after_ the class statement that defines the Structure subclass, this allows creating data types that directly or indirectly reference themselves:

Copy

class List(Structure):
    pass
List.\_fields\_ \= \[("pnext", POINTER(List)),\
                 ...\
                \]

The `_fields_` class variable can only be set once. Later assignments will raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
.

Additionally, the `_fields_` class variable must be defined before the structure or union type is first used, for example when an instance or subclass is created. Later assignments to `_fields_` will raise an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
. If `_fields_` has not been set before such use, the structure or union will have no own fields, as if `_fields_` was empty.

Sub-subclasses of structure types inherit the fields of the base class plus the [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 defined in the sub-subclass, if any.

\_pack\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "Link to this definition")

An optional small integer that allows overriding the alignment of structure fields in the instance.

This is only implemented for the MSVC-compatible memory layout (see [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_")
).

Setting `_pack_` to 0 is the same as not setting it at all. Otherwise, the value must be a positive power of two. The effect is equivalent to `#pragma pack(N)` in C, except `ctypes` may allow larger _n_ than what the compiler accepts.

`_pack_` must already be defined when [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 is assigned, otherwise it will have no effect.

Deprecated since version 3.14, will be removed in version 3.19: For historical reasons, if `_pack_` is non-zero, the MSVC-compatible layout will be used by default. On non-Windows platforms, this default is deprecated and is slated to become an error in Python 3.19. If it is intended, set [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_")
 to `'ms'` explicitly.

\_align\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._align_ "Link to this definition")

An optional small integer that allows increasing the alignment of the structure when being packed or unpacked to/from memory.

The value must not be negative. The effect is equivalent to `__attribute__((aligned(N)))` on GCC or `#pragma align(N)` on MSVC, except `ctypes` may allow values that the compiler would reject.

`_align_` can only _increase_ a structure’s alignment requirements. Setting it to 0 or 1 has no effect.

Using values that are not powers of two is discouraged and may lead to surprising behavior.

`_align_` must already be defined when [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 is assigned, otherwise it will have no effect.

Added in version 3.13.

\_layout\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "Link to this definition")

An optional string naming the struct/union layout. It can currently be set to:

*   `"ms"`: the layout used by the Microsoft compiler (MSVC). On GCC and Clang, this layout can be selected with `__attribute__((ms_struct))`.
    
*   `"gcc-sysv"`: the layout used by GCC with the System V or “SysV-like” data model, as used on Linux and macOS. With this layout, [`_pack_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "ctypes.Structure._pack_")
     must be unset or zero.
    

If not set explicitly, `ctypes` will use a default that matches the platform conventions. This default may change in future Python releases (for example, when a new platform gains official support, or when a difference between similar platforms is found). Currently the default will be:

*   On Windows: `"ms"`
    
*   When [`_pack_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "ctypes.Structure._pack_")
     is specified: `"ms"`. (This is deprecated; see `_pack_` documentation.)
    
*   Otherwise: `"gcc-sysv"`
    

`_layout_` must already be defined when [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 is assigned, otherwise it will have no effect.

Added in version 3.14.

\_anonymous\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._anonymous_ "Link to this definition")

An optional sequence that lists the names of unnamed (anonymous) fields. [`_anonymous_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._anonymous_ "ctypes.Structure._anonymous_")
 must be already defined when [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 is assigned, otherwise it will have no effect.

The fields listed in this variable must be structure or union type fields. `ctypes` will create descriptors in the structure type that allows accessing the nested fields directly, without the need to create the structure or union field.

Here is an example type (Windows):

Copy

class TYPEDESC(Structure):
    pass

class \_U(Union):
    \_fields\_ \= \[("lptdesc", POINTER(TYPEDESC)),\
                ("lpadesc", POINTER(ARRAYDESC)),\
                ("hreftype", HREFTYPE)\]

TYPEDESC.\_anonymous\_ \= ("u",)
TYPEDESC.\_fields\_ \= \[("u", \_U),\
                    ("vt", VARTYPE)\]

The `TYPEDESC` structure describes a COM data type, the `vt` field specifies which one of the union fields is valid. Since the `u` field is defined as anonymous field, it is now possible to access the members directly off the TYPEDESC instance. `td.lptdesc` and `td.u.lptdesc` are equivalent, but the former is faster since it does not need to create a temporary union instance:

Copy

some\_type \= TYPEDESC()
td \= TYPEDESC()
td.vt \= VT\_PTR
td.lptdesc \= pointer(some\_type)
td.u.lptdesc \= pointer(some\_type)

It is possible to define sub-subclasses of structures, they inherit the fields of the base class. If the subclass definition has a separate [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
 variable, the fields specified in this are appended to the fields of the base class.

Structure and union constructors accept both positional and keyword arguments. Positional arguments are used to initialize member fields in the same order as they are appear in [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
. Keyword arguments in the constructor are interpreted as attribute assignments, so they will initialize `_fields_` with the same name, or create new attributes for names not present in `_fields_`.

class ctypes.CField(_\*args_, _\*\*kw_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField "Link to this definition")

Descriptor for fields of a [`Structure`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure "ctypes.Structure")
 and [`Union`](https://docs.python.org/3/library/ctypes.html#ctypes.Union "ctypes.Union")
. For example:

Copy

\>>> class Color(Structure):
...     \_fields\_ \= (
...         ('red', c\_uint8),
...         ('green', c\_uint8),
...         ('blue', c\_uint8),
...         ('intense', c\_bool, 1),
...         ('blinking', c\_bool, 1),
...    )
...
\>>> Color.red
<ctypes.CField 'red' type=c\_ubyte, ofs=0, size=1>
\>>> Color.green.type
<class 'ctypes.c\_ubyte'>
\>>> Color.blue.byte\_offset
2
\>>> Color.intense
<ctypes.CField 'intense' type=c\_bool, ofs=3, bit\_size=1, bit\_offset=0>
\>>> Color.blinking.bit\_offset
1

All attributes are read-only.

`CField` objects are created via [`_fields_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._fields_ "ctypes.Structure._fields_")
; do not instantiate the class directly.

Added in version 3.14: Previously, descriptors only had `offset` and `size` attributes and a readable string representation; the `CField` class was not available directly.

name[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.name "Link to this definition")

Name of the field, as a string.

type[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.type "Link to this definition")

Type of the field, as a [ctypes class](https://docs.python.org/3/library/ctypes.html#ctypes-data-types)
.

offset[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.offset "Link to this definition")

byte\_offset[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.byte_offset "Link to this definition")

Offset of the field, in bytes.

For bitfields, this is the offset of the underlying byte-aligned _storage unit_; see [`bit_offset`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.bit_offset "ctypes.CField.bit_offset")
.

byte\_size[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.byte_size "Link to this definition")

Size of the field, in bytes.

For bitfields, this is the size of the underlying _storage unit_. Typically, it has the same size as the bitfield’s type.

size[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.size "Link to this definition")

For non-bitfields, equivalent to [`byte_size`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.byte_size "ctypes.CField.byte_size")
.

For bitfields, this contains a backwards-compatible bit-packed value that combines [`bit_size`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.bit_size "ctypes.CField.bit_size")
 and [`bit_offset`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.bit_offset "ctypes.CField.bit_offset")
. Prefer using the explicit attributes instead.

is\_bitfield[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.is_bitfield "Link to this definition")

True if this is a bitfield.

bit\_offset[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.bit_offset "Link to this definition")

bit\_size[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.bit_size "Link to this definition")

The location of a bitfield within its _storage unit_, that is, within [`byte_size`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.byte_size "ctypes.CField.byte_size")
 bytes of memory starting at [`byte_offset`](https://docs.python.org/3/library/ctypes.html#ctypes.CField.byte_offset "ctypes.CField.byte_offset")
.

To get the field’s value, read the storage unit as an integer, [shift right](https://docs.python.org/3/reference/expressions.html#shifting)
 by `bit_offset` and take the `bit_size` least significant bits.

For non-bitfields, `bit_offset` is zero and `bit_size` is equal to `byte_size * 8`.

is\_anonymous[¶](https://docs.python.org/3/library/ctypes.html#ctypes.CField.is_anonymous "Link to this definition")

True if this field is anonymous, that is, it contains nested sub-fields that should be merged into a containing structure or union.

### Arrays and pointers[¶](https://docs.python.org/3/library/ctypes.html#arrays-and-pointers "Link to this heading")

class ctypes.Array(_\*args_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Array "Link to this definition")

Abstract base class for arrays.

The recommended way to create concrete array types is by multiplying any `ctypes` data type with a non-negative integer. Alternatively, you can subclass this type and define [`_length_`](https://docs.python.org/3/library/ctypes.html#ctypes.Array._length_ "ctypes.Array._length_")
 and [`_type_`](https://docs.python.org/3/library/ctypes.html#ctypes.Array._type_ "ctypes.Array._type_")
 class variables. Array elements can be read and written using standard subscript and slice accesses; for slice reads, the resulting object is _not_ itself an `Array`.

Arrays are [generic](https://docs.python.org/3/library/typing.html#generics)
 over the type of their elements.

\_length\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Array._length_ "Link to this definition")

A positive integer specifying the number of elements in the array. Out-of-range subscripts result in an [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
. Will be returned by [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
.

\_type\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes.Array._type_ "Link to this definition")

Specifies the type of each element in the array.

Array subclass constructors accept positional arguments, used to initialize the elements in order.

ctypes.ARRAY(_type_, _length_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.ARRAY "Link to this definition")

Create an array. Equivalent to `type * length`, where _type_ is a `ctypes` data type and _length_ an integer.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.14: In favor of multiplication.

class ctypes.\_Pointer[¶](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer "Link to this definition")

Private, abstract base class for pointers.

Concrete pointer types are created by calling [`POINTER()`](https://docs.python.org/3/library/ctypes.html#ctypes.POINTER "ctypes.POINTER")
 with the type that will be pointed to; this is done automatically by [`pointer()`](https://docs.python.org/3/library/ctypes.html#ctypes.pointer "ctypes.pointer")
.

If a pointer points to an array, its elements can be read and written using standard subscript and slice accesses. Pointer objects have no size, so [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
 will raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. Negative subscripts will read from the memory _before_ the pointer (as in C), and out-of-range subscripts will probably crash with an access violation (if you’re lucky).

\_type\_[¶](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer._type_ "Link to this definition")

Specifies the type pointed to.

contents[¶](https://docs.python.org/3/library/ctypes.html#ctypes._Pointer.contents "Link to this definition")

Returns the object to which to pointer points. Assigning to this attribute changes the pointer to point to the assigned object.

### Exceptions[¶](https://docs.python.org/3/library/ctypes.html#exceptions "Link to this heading")

exception ctypes.ArgumentError[¶](https://docs.python.org/3/library/ctypes.html#ctypes.ArgumentError "Link to this definition")

This exception is raised when a foreign function call cannot convert one of the passed arguments.

exception ctypes.COMError(_hresult_, _text_, _details_)[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError "Link to this definition")

This exception is raised when a COM method call failed.

hresult[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError.hresult "Link to this definition")

The integer value representing the error code.

text[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError.text "Link to this definition")

The error message.

details[¶](https://docs.python.org/3/library/ctypes.html#ctypes.COMError.details "Link to this definition")

The 5-tuple `(descr, source, helpfile, helpcontext, progid)`.

_descr_ is the textual description. _source_ is the language-dependent `ProgID` for the class or application that raised the error. _helpfile_ is the path of the help file. _helpcontext_ is the help context identifier. _progid_ is the `ProgID` of the interface that defined the error.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows

Added in version 3.14.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html#)
    *   [ctypes tutorial](https://docs.python.org/3/library/ctypes.html#ctypes-tutorial)
        *   [Loading dynamic link libraries](https://docs.python.org/3/library/ctypes.html#loading-dynamic-link-libraries)
            
        *   [Accessing functions from loaded dlls](https://docs.python.org/3/library/ctypes.html#accessing-functions-from-loaded-dlls)
            
        *   [Calling functions](https://docs.python.org/3/library/ctypes.html#calling-functions)
            
        *   [Fundamental data types](https://docs.python.org/3/library/ctypes.html#fundamental-data-types)
            
        *   [Calling functions, continued](https://docs.python.org/3/library/ctypes.html#calling-functions-continued)
            
        *   [Calling variadic functions](https://docs.python.org/3/library/ctypes.html#calling-variadic-functions)
            
        *   [Calling functions with your own custom data types](https://docs.python.org/3/library/ctypes.html#calling-functions-with-your-own-custom-data-types)
            
        *   [Specifying the required argument types (function prototypes)](https://docs.python.org/3/library/ctypes.html#specifying-the-required-argument-types-function-prototypes)
            
        *   [Return types](https://docs.python.org/3/library/ctypes.html#return-types)
            
        *   [Passing pointers (or: passing parameters by reference)](https://docs.python.org/3/library/ctypes.html#passing-pointers-or-passing-parameters-by-reference)
            
        *   [Structures and unions](https://docs.python.org/3/library/ctypes.html#structures-and-unions)
            
        *   [Structure/union layout, alignment and byte order](https://docs.python.org/3/library/ctypes.html#structure-union-layout-alignment-and-byte-order)
            
        *   [Bit fields in structures and unions](https://docs.python.org/3/library/ctypes.html#bit-fields-in-structures-and-unions)
            
        *   [Arrays](https://docs.python.org/3/library/ctypes.html#arrays)
            
        *   [Pointers](https://docs.python.org/3/library/ctypes.html#pointers)
            
        *   [Thread safety without the GIL](https://docs.python.org/3/library/ctypes.html#thread-safety-without-the-gil)
            
        *   [Type conversions](https://docs.python.org/3/library/ctypes.html#type-conversions)
            
        *   [Incomplete Types](https://docs.python.org/3/library/ctypes.html#incomplete-types)
            
        *   [Callback functions](https://docs.python.org/3/library/ctypes.html#callback-functions)
            
        *   [Accessing values exported from dlls](https://docs.python.org/3/library/ctypes.html#accessing-values-exported-from-dlls)
            
        *   [Surprises](https://docs.python.org/3/library/ctypes.html#surprises)
            
        *   [Variable-sized data types](https://docs.python.org/3/library/ctypes.html#variable-sized-data-types)
            
    *   [ctypes reference](https://docs.python.org/3/library/ctypes.html#ctypes-reference)
        *   [Loading shared libraries](https://docs.python.org/3/library/ctypes.html#loading-shared-libraries)
            
        *   [Finding shared libraries](https://docs.python.org/3/library/ctypes.html#finding-shared-libraries)
            
        *   [Listing loaded shared libraries](https://docs.python.org/3/library/ctypes.html#listing-loaded-shared-libraries)
            
        *   [Foreign functions](https://docs.python.org/3/library/ctypes.html#foreign-functions)
            
        *   [Function prototypes](https://docs.python.org/3/library/ctypes.html#function-prototypes)
            
        *   [Utility functions](https://docs.python.org/3/library/ctypes.html#utility-functions)
            
        *   [Data types](https://docs.python.org/3/library/ctypes.html#data-types)
            
        *   [Fundamental data types](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types-2)
            
        *   [Windows data types](https://docs.python.org/3/library/ctypes.html#module-ctypes.wintypes)
            *   [Simple types](https://docs.python.org/3/library/ctypes.html#simple-types)
                
            *   [Handle types](https://docs.python.org/3/library/ctypes.html#handle-types)
                
            *   [Structures](https://docs.python.org/3/library/ctypes.html#structures)
                
            *   [Pointer types](https://docs.python.org/3/library/ctypes.html#pointer-types)
                
            *   [Constants and functions](https://docs.python.org/3/library/ctypes.html#constants-and-functions)
                
        *   [Structured data types](https://docs.python.org/3/library/ctypes.html#structured-data-types)
            
        *   [Arrays and pointers](https://docs.python.org/3/library/ctypes.html#arrays-and-pointers)
            
        *   [Exceptions](https://docs.python.org/3/library/ctypes.html#exceptions)
            

#### Previous topic

[`errno` — Standard errno system symbols](https://docs.python.org/3/library/errno.html "previous chapter")

#### Next topic

[Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=ctypes+%E2%80%94+A+foreign+function+library+for+Python&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fctypes.html&pagesource=library%2Fctypes.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/ctypes.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/cmdlinelibs.html "Command-line interface libraries")
     |
*   [previous](https://docs.python.org/3/library/errno.html "errno — Standard errno system symbols")
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
*   [`ctypes` — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html)
    
*    
    
    |
*   Theme Auto Light Dark |