### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/stable.html "C API and ABI Stability")
     |
*   [previous](https://docs.python.org/3/c-api/index.html "Python/C API reference manual")
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
*   [Introduction](https://docs.python.org/3/c-api/intro.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Introduction[¶](https://docs.python.org/3/c-api/intro.html#introduction "Link to this heading")

================================================================================================

The Application Programmer’s Interface to Python gives C and C++ programmers access to the Python interpreter at a variety of levels. The API is equally usable from C++, but for brevity it is generally referred to as the Python/C API. There are two fundamentally different reasons for using the Python/C API. The first reason is to write _extension modules_ for specific purposes; these are C modules that extend the Python interpreter. This is probably the most common use. The second reason is to use Python as a component in a larger application; this technique is generally referred to as _embedding_ Python in an application.

Writing an extension module is a relatively well-understood process, where a “cookbook” approach works well. There are several tools that automate the process to some extent. While people have embedded Python in other applications since its early existence, the process of embedding Python is less straightforward than writing an extension.

Many API functions are useful independent of whether you’re embedding or extending Python; moreover, most applications that embed Python will need to provide a custom extension as well, so it’s probably a good idea to become familiar with writing an extension before attempting to embed Python in a real application.

Language version compatibility[¶](https://docs.python.org/3/c-api/intro.html#language-version-compatibility "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

Python’s C API is compatible with C11 and C++11 versions of C and C++.

This is a lower limit: the C API does not require features from later C/C++ versions. You do _not_ need to enable your compiler’s “c11 mode”.

Coding standards[¶](https://docs.python.org/3/c-api/intro.html#coding-standards "Link to this heading")

--------------------------------------------------------------------------------------------------------

If you’re writing C code for inclusion in CPython, you **must** follow the guidelines and standards defined in [**PEP 7**](https://peps.python.org/pep-0007/)
. These guidelines apply regardless of the version of Python you are contributing to. Following these conventions is not necessary for your own third party extension modules, unless you eventually expect to contribute them to Python.

Include Files[¶](https://docs.python.org/3/c-api/intro.html#include-files "Link to this heading")

--------------------------------------------------------------------------------------------------

All function, type and macro definitions needed to use the Python/C API are included in your code by the following line:

#define PY\_SSIZE\_T\_CLEAN
#include <Python.h>

This implies inclusion of the following standard headers: `<stdio.h>`, `<string.h>`, `<errno.h>`, `<limits.h>`, `<assert.h>` and `<stdlib.h>` (if available).

Note

Since Python may define some pre-processor definitions which affect the standard headers on some systems, you _must_ include `Python.h` before any standard headers are included.

It is recommended to always define `PY_SSIZE_T_CLEAN` before including `Python.h`. See [Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html#arg-parsing)
 for a description of this macro.

All user visible names defined by Python.h (except those defined by the included standard headers) have one of the prefixes `Py` or `_Py`. Names beginning with `_Py` are for internal use by the Python implementation and should not be used by extension writers. Structure member names do not have a reserved prefix.

Note

User code should never define names that begin with `Py` or `_Py`. This confuses the reader, and jeopardizes the portability of the user code to future Python versions, which may define additional names beginning with one of these prefixes.

The header files are typically installed with Python. On Unix, these are located in the directories `_prefix_/include/pythonversion/` and `_exec_prefix_/include/pythonversion/`, where [`prefix`](https://docs.python.org/3/using/configure.html#cmdoption-prefix)
 and [`exec_prefix`](https://docs.python.org/3/using/configure.html#cmdoption-exec-prefix)
 are defined by the corresponding parameters to Python’s **configure** script and _version_ is `'%d.%d' % sys.version_info[:2]`. On Windows, the headers are installed in `_prefix_/include`, where `prefix` is the installation directory specified to the installer.

To include the headers, place both directories (if different) on your compiler’s search path for includes. Do _not_ place the parent directories on the search path and then use `#include <pythonX.Y/Python.h>`; this will break on multi-platform builds since the platform independent headers under [`prefix`](https://docs.python.org/3/using/configure.html#cmdoption-prefix)
 include the platform specific headers from [`exec_prefix`](https://docs.python.org/3/using/configure.html#cmdoption-exec-prefix)
.

C++ users should note that although the API is defined entirely using C, the header files properly declare the entry points to be `extern "C"`. As a result, there is no need to do anything special to use the API from C++.

### System includes[¶](https://docs.python.org/3/c-api/intro.html#system-includes "Link to this heading")

> `Python.h` includes several standard header files. C extensions should include the standard headers that they use, and should not rely on these implicit includes. The implicit includes are:
> 
> *   `<assert.h>`
>     
> *   `<intrin.h>` (on Windows)
>     
> *   `<inttypes.h>`
>     
> *   `<limits.h>`
>     
> *   `<math.h>`
>     
> *   `<stdarg.h>`
>     
> *   `<string.h>`
>     
> *   `<wchar.h>`
>     
> *   `<sys/types.h>` (if present)
>     
> 
> The following are included for backwards compatibility, unless using [Limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
>  3.13 or newer:
> 
> *   `<ctype.h>`
>     
> *   `<unistd.h>` (on POSIX)
>     
> 
> The following are included for backwards compatibility, unless using [Limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
>  3.11 or newer:
> 
> *   `<errno.h>`
>     
> *   `<stdio.h>`
>     
> *   `<stdlib.h>`
>     

Note

Since Python may define some pre-processor definitions which affect the standard headers on some systems, you _must_ include `Python.h` before any standard headers are included.

Useful macros[¶](https://docs.python.org/3/c-api/intro.html#useful-macros "Link to this heading")

--------------------------------------------------------------------------------------------------

Several useful macros are defined in the Python header files. Many are defined closer to where they are useful (for example, [`Py_RETURN_NONE`](https://docs.python.org/3/c-api/none.html#c.Py_RETURN_NONE "Py_RETURN_NONE")
, [`PyMODINIT_FUNC`](https://docs.python.org/3/c-api/extension-modules.html#c.PyMODINIT_FUNC "PyMODINIT_FUNC")
). Others of a more general utility are defined here. This is not necessarily a complete listing.

Py\_CAN\_START\_THREADS[¶](https://docs.python.org/3/c-api/intro.html#c.Py_CAN_START_THREADS "Link to this definition")
  

If this macro is defined, then the current system is able to start threads.

Currently, all systems supported by CPython (per [**PEP 11**](https://peps.python.org/pep-0011/)
), with the exception of some WebAssembly platforms, support starting threads.

Added in version 3.13.

Py\_GETENV(s)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_GETENV "Link to this definition")
  

Like `getenv(_s_)`, but returns `NULL` if [`-E`](https://docs.python.org/3/using/cmdline.html#cmdoption-E)
 was passed on the command line (see [`PyConfig.use_environment`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment")
).

### Docstring macros[¶](https://docs.python.org/3/c-api/intro.html#docstring-macros "Link to this heading")

PyDoc\_STRVAR(name, str)[¶](https://docs.python.org/3/c-api/intro.html#c.PyDoc_STRVAR "Link to this definition")
  

Creates a variable with name _name_ that can be used in docstrings. If Python is built without docstrings ([`--without-doc-strings`](https://docs.python.org/3/using/configure.html#cmdoption-without-doc-strings)
), the value will be an empty string.

Example:

PyDoc\_STRVAR(pop\_doc, "Remove and return the rightmost element.");

static PyMethodDef deque\_methods\[\] \= {
    // ...
    {"pop", (PyCFunction)deque\_pop, METH\_NOARGS, pop\_doc},
    // ...
}

Expands to `PyDoc_VAR(_name_) = PyDoc_STR(_str_)`.

PyDoc\_STR(str)[¶](https://docs.python.org/3/c-api/intro.html#c.PyDoc_STR "Link to this definition")
  

Expands to the given input string, or an empty string if docstrings are disabled ([`--without-doc-strings`](https://docs.python.org/3/using/configure.html#cmdoption-without-doc-strings)
).

Example:

static PyMethodDef pysqlite\_row\_methods\[\] \= {
    {"keys", (PyCFunction)pysqlite\_row\_keys, METH\_NOARGS,
        PyDoc\_STR("Returns the keys of the row.")},
    {NULL, NULL}
};

PyDoc\_VAR(name)[¶](https://docs.python.org/3/c-api/intro.html#c.PyDoc_VAR "Link to this definition")
  

Declares a static character array variable with the given _name_. Expands to `static const char _name_[]`

For example:

PyDoc\_VAR(python\_doc) \= PyDoc\_STR(
   "A genus of constricting snakes in the Pythonidae family native "
   "to the tropics and subtropics of the Eastern Hemisphere.");

### General utility macros[¶](https://docs.python.org/3/c-api/intro.html#general-utility-macros "Link to this heading")

The following macros are for common tasks not specific to Python.

Py\_UNUSED(arg)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_UNUSED "Link to this definition")
  

Use this for unused arguments in a function definition to silence compiler warnings. Example: `int func(int a, int Py_UNUSED(b)) { return a; }`.

Added in version 3.4.

Py\_GCC\_ATTRIBUTE(name)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_GCC_ATTRIBUTE "Link to this definition")
  

Use a GCC attribute _name_, hiding it from compilers that don’t support GCC attributes (such as MSVC).

This expands to `__attribute__((_name)_)` on a GCC compiler, and expands to nothing on compilers that don’t support GCC attributes.

#### Numeric utilities[¶](https://docs.python.org/3/c-api/intro.html#numeric-utilities "Link to this heading")

Py\_ABS(x)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_ABS "Link to this definition")
  

Return the absolute value of `x`.

The argument may be evaluated more than once. Consequently, do not pass an expression with side-effects directly to this macro.

If the result cannot be represented (for example, if `x` has `INT_MIN` value for int type), the behavior is undefined.

Corresponds roughly to `((_x_) < 0 ? -(_x_) : (_x_))`

Added in version 3.3.

Py\_MAX(x, y)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_MAX "Link to this definition")
  

Py\_MIN(x, y)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_MIN "Link to this definition")
  

Return the larger or smaller of the arguments, respectively.

Any arguments may be evaluated more than once. Consequently, do not pass an expression with side-effects directly to this macro.

`Py_MAX` corresponds roughly to `(((_x_) > (_y_)) ? (_x_) : (_y_))`.

Added in version 3.3.

Py\_ARITHMETIC\_RIGHT\_SHIFT(type, integer, positions)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_ARITHMETIC_RIGHT_SHIFT "Link to this definition")
  

Similar to `_integer_ >> _positions_`, but forces sign extension, as the C standard does not define whether a right-shift of a signed integer will perform sign extension or a zero-fill.

_integer_ should be any signed integer type. _positions_ is the number of positions to shift to the right.

Both _integer_ and _positions_ can be evaluated more than once; consequently, avoid directly passing a function call or some other operation with side-effects to this macro. Instead, store the result as a variable and then pass it.

_type_ is unused and only kept for backwards compatibility. Historically, _type_ was used to cast _integer_.

Changed in version 3.1: This macro is now valid for all signed integer types, not just those for which `unsigned type` is legal. As a result, _type_ is no longer used.

Py\_CHARMASK(c)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_CHARMASK "Link to this definition")
  

Argument must be a character or an integer in the range \[-128, 127\] or \[0, 255\]. This macro returns `c` cast to an `unsigned char`.

PY\_BIG\_ENDIAN[¶](https://docs.python.org/3/c-api/intro.html#c.PY_BIG_ENDIAN "Link to this definition")
  

PY\_LITTLE\_ENDIAN[¶](https://docs.python.org/3/c-api/intro.html#c.PY_LITTLE_ENDIAN "Link to this definition")
  

Constants describing the byte order of the platform that Python was built for. Exactly one of them is `1` and the other is `0`.

#### Assertion utilities[¶](https://docs.python.org/3/c-api/intro.html#assertion-utilities "Link to this heading")

Py\_UNREACHABLE()[¶](https://docs.python.org/3/c-api/intro.html#c.Py_UNREACHABLE "Link to this definition")
  

Use this when you have a code path that cannot be reached by design. For example, in the `default:` clause in a `switch` statement for which all possible values are covered in `case` statements. Use this in places where you might be tempted to put an `assert(0)` or `abort()` call.

In release mode, the macro helps the compiler to optimize the code, and avoids a warning about unreachable code. For example, the macro is implemented with `__builtin_unreachable()` on GCC in release mode.

In debug mode, and on unsupported compilers, the macro expands to a call to [`Py_FatalError()`](https://docs.python.org/3/c-api/sys.html#c.Py_FatalError "Py_FatalError")
.

A use for `Py_UNREACHABLE()` is following a call to a function that never returns but that is not declared `_Noreturn`.

If a code path is very unlikely code but can be reached under exceptional case, this macro must not be used. For example, under low memory condition or if a system call returns a value out of the expected range. In this case, it’s better to report the error to the caller. If the error cannot be reported to caller, [`Py_FatalError()`](https://docs.python.org/3/c-api/sys.html#c.Py_FatalError "Py_FatalError")
 can be used.

Added in version 3.7.

Py\_SAFE\_DOWNCAST(value, larger, smaller)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_SAFE_DOWNCAST "Link to this definition")
  

Cast _value_ to type _smaller_ from type _larger_, validating that no information was lost.

On release builds of Python, this is roughly equivalent to `((_smaller_) _value_)` (in C++, `static_cast<_smaller_>(_value_)` will be used instead).

On debug builds (implying that [`Py_DEBUG`](https://docs.python.org/3/c-api/intro.html#c.Py_DEBUG "Py_DEBUG")
 is defined), this asserts that no information was lost with the cast from _larger_ to _smaller_.

_value_, _larger_, and _smaller_ may all be evaluated more than once in the expression; consequently, do not pass an expression with side-effects directly to this macro.

Py\_BUILD\_ASSERT(cond)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_BUILD_ASSERT "Link to this definition")
  

Asserts a compile-time condition _cond_, as a statement. The build will fail if the condition is false or cannot be evaluated at compile time.

Corresponds roughly to `static_assert(_cond_)` on C23 and above.

For example:

Py\_BUILD\_ASSERT(sizeof(PyTime\_t) \== sizeof(int64\_t));

Added in version 3.3.

Py\_BUILD\_ASSERT\_EXPR(cond)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_BUILD_ASSERT_EXPR "Link to this definition")
  

Asserts a compile-time condition _cond_, as an expression that evaluates to `0`. The build will fail if the condition is false or cannot be evaluated at compile time.

For example:

#define foo\_to\_char(foo) \\
    ((char \*)(foo) + Py\_BUILD\_ASSERT\_EXPR(offsetof(struct foo, string) == 0))

Added in version 3.3.

#### Type size utilities[¶](https://docs.python.org/3/c-api/intro.html#type-size-utilities "Link to this heading")

Py\_ARRAY\_LENGTH(array)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_ARRAY_LENGTH "Link to this definition")
  

Compute the length of a statically allocated C array at compile time.

The _array_ argument must be a C array with a size known at compile time. Passing an array with an unknown size, such as a heap-allocated array, will result in a compilation error on some compilers, or otherwise produce incorrect results.

This is roughly equivalent to:

sizeof(array) / sizeof((array)\[0\])

Py\_MEMBER\_SIZE(type, member)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_MEMBER_SIZE "Link to this definition")
  

Return the size of a structure (_type_) _member_ in bytes.

Corresponds roughly to `sizeof(((_type_ *)NULL)->_member_)`.

Added in version 3.6.

#### Macro definition utilities[¶](https://docs.python.org/3/c-api/intro.html#macro-definition-utilities "Link to this heading")

Py\_FORCE\_EXPANSION(X)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_FORCE_EXPANSION "Link to this definition")
  

This is equivalent to `_X_`, which is useful for token-pasting in macros, as macro expansions in _X_ are forcefully evaluated by the preprocessor.

Py\_STRINGIFY(x)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_STRINGIFY "Link to this definition")
  

Convert `x` to a C string. For example, `Py_STRINGIFY(123)` returns `"123"`.

Added in version 3.4.

### Declaration utilities[¶](https://docs.python.org/3/c-api/intro.html#declaration-utilities "Link to this heading")

The following macros can be used in declarations. They are most useful for defining the C API itself, and have limited use for extension authors. Most of them expand to compiler-specific spellings of common extensions to the C language.

Py\_ALWAYS\_INLINE[¶](https://docs.python.org/3/c-api/intro.html#c.Py_ALWAYS_INLINE "Link to this definition")
  

Ask the compiler to always inline a static inline function. The compiler can ignore it and decide to not inline the function.

Corresponds to `always_inline` attribute in GCC and `__forceinline` in MSVC.

It can be used to inline performance critical static inline functions when building Python in debug mode with function inlining disabled. For example, MSC disables function inlining when building in debug mode.

Marking blindly a static inline function with Py\_ALWAYS\_INLINE can result in worse performances (due to increased code size for example). The compiler is usually smarter than the developer for the cost/benefit analysis.

If Python is [built in debug mode](https://docs.python.org/3/using/configure.html#debug-build)
 (if the [`Py_DEBUG`](https://docs.python.org/3/c-api/intro.html#c.Py_DEBUG "Py_DEBUG")
 macro is defined), the [`Py_ALWAYS_INLINE`](https://docs.python.org/3/c-api/intro.html#c.Py_ALWAYS_INLINE "Py_ALWAYS_INLINE")
 macro does nothing.

It must be specified before the function return type. Usage:

static inline Py\_ALWAYS\_INLINE int random(void) { return 4; }

Added in version 3.11.

Py\_NO\_INLINE[¶](https://docs.python.org/3/c-api/intro.html#c.Py_NO_INLINE "Link to this definition")
  

Disable inlining on a function. For example, it reduces the C stack consumption: useful on LTO+PGO builds which heavily inline code (see [bpo-33720](https://bugs.python.org/issue?@action=redirect&bpo=33720)
).

Corresponds to the `noinline` attribute/specification on GCC and MSVC.

Usage:

Py\_NO\_INLINE static int random(void) { return 4; }

Added in version 3.11.

Py\_DEPRECATED(version)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_DEPRECATED "Link to this definition")
  

Use this to declare APIs that were deprecated in a specific CPython version. The macro must be placed before the symbol name.

Example:

Py\_DEPRECATED(3.8) PyAPI\_FUNC(int) Py\_OldFunction(void);

Changed in version 3.8: MSVC support was added.

Py\_LOCAL(type)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_LOCAL "Link to this definition")
  

Declare a function returning the specified _type_ using a fast-calling qualifier for functions that are local to the current file. Semantically, this is equivalent to `static _type_`.

Py\_LOCAL\_INLINE(type)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_LOCAL_INLINE "Link to this definition")
  

Equivalent to [`Py_LOCAL`](https://docs.python.org/3/c-api/intro.html#c.Py_LOCAL "Py_LOCAL")
 but additionally requests the function be inlined.

Py\_LOCAL\_SYMBOL[¶](https://docs.python.org/3/c-api/intro.html#c.Py_LOCAL_SYMBOL "Link to this definition")
  

Macro used to declare a symbol as local to the shared library (hidden). On supported platforms, it ensures the symbol is not exported.

On compatible versions of GCC/Clang, it expands to `__attribute__((visibility("hidden")))`.

Py\_EXPORTED\_SYMBOL[¶](https://docs.python.org/3/c-api/intro.html#c.Py_EXPORTED_SYMBOL "Link to this definition")
  

Macro used to declare a symbol (function or data) as exported. On Windows, this expands to `__declspec(dllexport)`. On compatible versions of GCC/Clang, it expands to `__attribute__((visibility("default")))`. This macro is for defining the C API itself; extension modules should not use it.

Py\_IMPORTED\_SYMBOL[¶](https://docs.python.org/3/c-api/intro.html#c.Py_IMPORTED_SYMBOL "Link to this definition")
  

Macro used to declare a symbol as imported. On Windows, this expands to `__declspec(dllimport)`. This macro is for defining the C API itself; extension modules should not use it.

PyAPI\_FUNC(type)[¶](https://docs.python.org/3/c-api/intro.html#c.PyAPI_FUNC "Link to this definition")
  

Macro used by CPython to declare a function as part of the C API. Its expansion depends on the platform and build configuration. This macro is intended for defining CPython’s C API itself; extension modules should not use it for their own symbols.

PyAPI\_DATA(type)[¶](https://docs.python.org/3/c-api/intro.html#c.PyAPI_DATA "Link to this definition")
  

Macro used by CPython to declare a public global variable as part of the C API. Its expansion depends on the platform and build configuration. This macro is intended for defining CPython’s C API itself; extension modules should not use it for their own symbols.

### Outdated macros[¶](https://docs.python.org/3/c-api/intro.html#outdated-macros "Link to this heading")

The following [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 macros have been used to features that have been standardized in C11 (or previous standards).

Py\_ALIGNED(num)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_ALIGNED "Link to this definition")
  

On some GCC-like compilers, specify alignment to _num_ bytes. This does nothing on other compilers.

Use the standard `alignas` specifier rather than this macro.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

PY\_FORMAT\_SIZE\_T[¶](https://docs.python.org/3/c-api/intro.html#c.PY_FORMAT_SIZE_T "Link to this definition")
  

The `printf()` formatting modifier for `size_t`. Use `"z"` directly instead.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

Py\_LL(number)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_LL "Link to this definition")
  

Py\_ULL(number)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_ULL "Link to this definition")
  

Use _number_ as a `long long` or `unsigned long long` integer literal, respectively.

Expands to _number_ followed by `LL` or `LLU`, respectively, but will expand to some compiler-specific suffixes on some older compilers.

Consider using the C99 standard suffixes `LL` and `LLU` directly.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

PY\_LONG\_LONG[¶](https://docs.python.org/3/c-api/intro.html#c.PY_LONG_LONG "Link to this definition")
  

PY\_INT32\_T[¶](https://docs.python.org/3/c-api/intro.html#c.PY_INT32_T "Link to this definition")
  

PY\_UINT32\_T[¶](https://docs.python.org/3/c-api/intro.html#c.PY_UINT32_T "Link to this definition")
  

PY\_INT64\_T[¶](https://docs.python.org/3/c-api/intro.html#c.PY_INT64_T "Link to this definition")
  

PY\_UINT64\_T[¶](https://docs.python.org/3/c-api/intro.html#c.PY_UINT64_T "Link to this definition")
  

Aliases for the types `long long`, `int32_t`, `uint32_t`. `int64_t` and `uint64_t`, respectively. Historically, these types needed compiler-specific extensions.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

PY\_LLONG\_MIN[¶](https://docs.python.org/3/c-api/intro.html#c.PY_LLONG_MIN "Link to this definition")
  

PY\_LLONG\_MAX[¶](https://docs.python.org/3/c-api/intro.html#c.PY_LLONG_MAX "Link to this definition")
  

PY\_ULLONG\_MAX[¶](https://docs.python.org/3/c-api/intro.html#c.PY_ULLONG_MAX "Link to this definition")
  

PY\_SIZE\_MAX[¶](https://docs.python.org/3/c-api/intro.html#c.PY_SIZE_MAX "Link to this definition")
  

Aliases for the values `LLONG_MIN`, `LLONG_MAX`, `ULLONG_MAX`, and `SIZE_MAX`, respectively. Use these standard names instead.

The required header, `<limits.h>`, [is included](https://docs.python.org/3/c-api/intro.html#capi-system-includes)
 in `Python.h`.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

Py\_MEMCPY(dest, src, n)[¶](https://docs.python.org/3/c-api/intro.html#c.Py_MEMCPY "Link to this definition")
  

This is an alias to `memcpy()`.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.14: Use `memcpy()` directly instead.

Py\_UNICODE\_SIZE[¶](https://docs.python.org/3/c-api/intro.html#c.Py_UNICODE_SIZE "Link to this definition")
  

Size of the `wchar_t` type. Use `sizeof(wchar_t)` or `WCHAR_WIDTH/8` instead.

The required header for the latter, `<limits.h>`, [is included](https://docs.python.org/3/c-api/intro.html#capi-system-includes)
 in `Python.h`.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

Py\_UNICODE\_WIDE[¶](https://docs.python.org/3/c-api/intro.html#c.Py_UNICODE_WIDE "Link to this definition")
  

Defined if `wchar_t` can hold a Unicode character (UCS-4). Use `sizeof(wchar_t) >= 4` instead

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

Py\_VA\_COPY[¶](https://docs.python.org/3/c-api/intro.html#c.Py_VA_COPY "Link to this definition")
  

This is an alias to the C99-standard `va_copy` function.

Historically, this would use a compiler-specific method to copy a `va_list`.

Changed in version 3.6: This is now an alias to `va_copy`.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

Objects, Types and Reference Counts[¶](https://docs.python.org/3/c-api/intro.html#objects-types-and-reference-counts "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

Most Python/C API functions have one or more arguments as well as a return value of type [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*. This type is a pointer to an opaque data type representing an arbitrary Python object. Since all Python object types are treated the same way by the Python language in most situations (e.g., assignments, scope rules, and argument passing), it is only fitting that they should be represented by a single C type. Almost all Python objects live on the heap: you never declare an automatic or static variable of type [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
, only pointer variables of type PyObject\* can be declared. The sole exception are the type objects; since these must never be deallocated, they are typically static [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 objects.

All Python objects (even Python integers) have a _type_ and a _reference count_. An object’s type determines what kind of object it is (e.g., an integer, a list, or a user-defined function; there are many more as explained in [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types)
). For each of the well-known types there is a macro to check whether an object is of that type; for instance, `PyList_Check(a)` is true if (and only if) the object pointed to by _a_ is a Python list.

### Reference Counts[¶](https://docs.python.org/3/c-api/intro.html#reference-counts "Link to this heading")

The reference count is important because today’s computers have a finite (and often severely limited) memory size; it counts how many different places there are that have a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to an object. Such a place could be another object, or a global (or static) C variable, or a local variable in some C function. When the last strong reference to an object is released (i.e. its reference count becomes zero), the object is deallocated. If it contains references to other objects, those references are released. Those other objects may be deallocated in turn, if there are no more references to them, and so on. (There’s an obvious problem with objects that reference each other here; for now, the solution is “don’t do that.”)

Reference counts are always manipulated explicitly. The normal way is to use the macro [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "Py_INCREF")
 to take a new reference to an object (i.e. increment its reference count by one), and [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 to release that reference (i.e. decrement the reference count by one). The `Py_DECREF()` macro is considerably more complex than the incref one, since it must check whether the reference count becomes zero and then cause the object’s deallocator to be called. The deallocator is a function pointer contained in the object’s type structure. The type-specific deallocator takes care of releasing references for other objects contained in the object if this is a compound object type, such as a list, as well as performing any additional finalization that’s needed. There’s no chance that the reference count can overflow; at least as many bits are used to hold the reference count as there are distinct memory locations in virtual memory (assuming `sizeof(Py_ssize_t) >= sizeof(void*)`). Thus, the reference count increment is a simple operation.

It is not necessary to hold a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 (i.e. increment the reference count) for every local variable that contains a pointer to an object. In theory, the object’s reference count goes up by one when the variable is made to point to it and it goes down by one when the variable goes out of scope. However, these two cancel each other out, so at the end the reference count hasn’t changed. The only real reason to use the reference count is to prevent the object from being deallocated as long as our variable is pointing to it. If we know that there is at least one other reference to the object that lives at least as long as our variable, there is no need to take a new strong reference (i.e. increment the reference count) temporarily. An important situation where this arises is in objects that are passed as arguments to C functions in an extension module that are called from Python; the call mechanism guarantees to hold a reference to every argument for the duration of the call.

However, a common pitfall is to extract an object from a list and hold on to it for a while without taking a new reference. Some other operation might conceivably remove the object from the list, releasing that reference, and possibly deallocating it. The real danger is that innocent-looking operations may invoke arbitrary Python code which could do this; there is a code path which allows control to flow back to the user from a [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
, so almost any operation is potentially dangerous.

A safe approach is to always use the generic operations (functions whose name begins with `PyObject_`, `PyNumber_`, `PySequence_` or `PyMapping_`). These operations always create a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 (i.e. increment the reference count) of the object they return. This leaves the caller with the responsibility to call [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 when they are done with the result; this soon becomes second nature.

#### Reference Count Details[¶](https://docs.python.org/3/c-api/intro.html#reference-count-details "Link to this heading")

The reference count behavior of functions in the Python/C API is best explained in terms of _ownership of references_. Ownership pertains to references, never to objects (objects are not owned: they are always shared). “Owning a reference” means being responsible for calling Py\_DECREF on it when the reference is no longer needed. Ownership can also be transferred, meaning that the code that receives ownership of the reference then becomes responsible for eventually releasing it by calling [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 or [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF")
 when it’s no longer needed—or passing on this responsibility (usually to its caller). When a function passes ownership of a reference on to its caller, the caller is said to receive a _new_ reference. When no ownership is transferred, the caller is said to _borrow_ the reference. Nothing needs to be done for a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
.

Conversely, when a calling function passes in a reference to an object, there are two possibilities: the function _steals_ a reference to the object, or it does not.

_Stealing a reference_ means that when you pass a reference to a function, that function assumes that it now owns that reference. Since the new owner can use `Py_DECREF()` at its discretion, you (the caller) must not use that reference after the call.

Few functions steal references; the two notable exceptions are [`PyList_SetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_SetItem "PyList_SetItem")
 and [`PyTuple_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SetItem "PyTuple_SetItem")
, which steal a reference to the item (but not to the tuple or list into which the item is put!). These functions were designed to steal a reference because of a common idiom for populating a tuple or list with newly created objects; for example, the code to create the tuple `(1, 2, "three")` could look like this (forgetting about error handling for the moment; a better way to code this is shown below):

PyObject \*t;

t \= PyTuple\_New(3);
PyTuple\_SetItem(t, 0, PyLong\_FromLong(1L));
PyTuple\_SetItem(t, 1, PyLong\_FromLong(2L));
PyTuple\_SetItem(t, 2, PyUnicode\_FromString("three"));

Here, [`PyLong_FromLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong "PyLong_FromLong")
 returns a new reference which is immediately stolen by [`PyTuple_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SetItem "PyTuple_SetItem")
. When you want to keep using an object although the reference to it will be stolen, use [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "Py_INCREF")
 to grab another reference before calling the reference-stealing function.

Incidentally, [`PyTuple_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SetItem "PyTuple_SetItem")
 is the _only_ way to set tuple items; [`PySequence_SetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_SetItem "PySequence_SetItem")
 and [`PyObject_SetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetItem "PyObject_SetItem")
 refuse to do this since tuples are an immutable data type. You should only use `PyTuple_SetItem()` for tuples that you are creating yourself.

Equivalent code for populating a list can be written using [`PyList_New()`](https://docs.python.org/3/c-api/list.html#c.PyList_New "PyList_New")
 and [`PyList_SetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_SetItem "PyList_SetItem")
.

However, in practice, you will rarely use these ways of creating and populating a tuple or list. There’s a generic function, [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue")
, that can create most common objects from C values, directed by a _format string_. For example, the above two blocks of code could be replaced by the following (which also takes care of the error checking):

PyObject \*tuple, \*list;

tuple \= Py\_BuildValue("(iis)", 1, 2, "three");
list \= Py\_BuildValue("\[iis\]", 1, 2, "three");

It is much more common to use [`PyObject_SetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetItem "PyObject_SetItem")
 and friends with items whose references you are only borrowing, like arguments that were passed in to the function you are writing. In that case, their behaviour regarding references is much saner, since you don’t have to take a new reference just so you can give that reference away (“have it be stolen”). For example, this function sets all items of a list (actually, any mutable sequence) to a given item:

int
set\_all(PyObject \*target, PyObject \*item)
{
    Py\_ssize\_t i, n;

    n \= PyObject\_Length(target);
    if (n < 0)
        return \-1;
    for (i \= 0; i < n; i++) {
        PyObject \*index \= PyLong\_FromSsize\_t(i);
        if (!index)
            return \-1;
        if (PyObject\_SetItem(target, index, item) < 0) {
            Py\_DECREF(index);
            return \-1;
        }
        Py\_DECREF(index);
    }
    return 0;
}

The situation is slightly different for function return values. While passing a reference to most functions does not change your ownership responsibilities for that reference, many functions that return a reference to an object give you ownership of the reference. The reason is simple: in many cases, the returned object is created on the fly, and the reference you get is the only reference to the object. Therefore, the generic functions that return object references, like [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
 and [`PySequence_GetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetItem "PySequence_GetItem")
, always return a new reference (the caller becomes the owner of the reference).

It is important to realize that whether you own a reference returned by a function depends on which function you call only — _the plumage_ (the type of the object passed as an argument to the function) _doesn’t enter into it!_ Thus, if you extract an item from a list using [`PyList_GetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem "PyList_GetItem")
, you don’t own the reference — but if you obtain the same item from the same list using [`PySequence_GetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetItem "PySequence_GetItem")
 (which happens to take exactly the same arguments), you do own a reference to the returned object.

Here is an example of how you could write a function that computes the sum of the items in a list of integers; once using [`PyList_GetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem "PyList_GetItem")
, and once using [`PySequence_GetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetItem "PySequence_GetItem")
.

long
sum\_list(PyObject \*list)
{
    Py\_ssize\_t i, n;
    long total \= 0, value;
    PyObject \*item;

    n \= PyList\_Size(list);
    if (n < 0)
        return \-1; /\* Not a list \*/
    for (i \= 0; i < n; i++) {
        item \= PyList\_GetItem(list, i); /\* Can't fail \*/
        if (!PyLong\_Check(item)) continue; /\* Skip non-integers \*/
        value \= PyLong\_AsLong(item);
        if (value \== \-1 && PyErr\_Occurred())
            /\* Integer too big to fit in a C long, bail out \*/
            return \-1;
        total += value;
    }
    return total;
}

long
sum\_sequence(PyObject \*sequence)
{
    Py\_ssize\_t i, n;
    long total \= 0, value;
    PyObject \*item;
    n \= PySequence\_Length(sequence);
    if (n < 0)
        return \-1; /\* Has no length \*/
    for (i \= 0; i < n; i++) {
        item \= PySequence\_GetItem(sequence, i);
        if (item \== NULL)
            return \-1; /\* Not a sequence, or other failure \*/
        if (PyLong\_Check(item)) {
            value \= PyLong\_AsLong(item);
            Py\_DECREF(item);
            if (value \== \-1 && PyErr\_Occurred())
                /\* Integer too big to fit in a C long, bail out \*/
                return \-1;
            total += value;
        }
        else {
            Py\_DECREF(item); /\* Discard reference ownership \*/
        }
    }
    return total;
}

### Types[¶](https://docs.python.org/3/c-api/intro.html#types "Link to this heading")

There are few other data types that play a significant role in the Python/C API; most are simple C types such as int, long, double and char\*. A few structure types are used to describe static tables used to list the functions exported by a module or the data attributes of a new object type, and another is used to describe the value of a complex number. These will be discussed together with the functions that use them.

type Py\_ssize\_t[¶](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

A signed integral type such that `sizeof(Py_ssize_t) == sizeof(size_t)`. C99 doesn’t define such a thing directly (size\_t is an unsigned integral type). See [**PEP 353**](https://peps.python.org/pep-0353/)
 for details.

Py\_INVALID\_SIZE[¶](https://docs.python.org/3/c-api/intro.html#c.Py_INVALID_SIZE "Link to this definition")
  

A constant of type [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 with value `-1`, representing an invalid size.

PY\_SSIZE\_T\_MAX[¶](https://docs.python.org/3/c-api/intro.html#c.PY_SSIZE_T_MAX "Link to this definition")
  

PY\_SSIZE\_T\_MIN[¶](https://docs.python.org/3/c-api/intro.html#c.PY_SSIZE_T_MIN "Link to this definition")
  

The limit values (largest positive one and smallest negative one, respectively) of type [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
.

PY\_DWORD\_MAX[¶](https://docs.python.org/3/c-api/intro.html#c.PY_DWORD_MAX "Link to this definition")
  

The maximum value of the Windows `DWORD` type. Expands to `0xffffffff` on all platforms.

Exceptions[¶](https://docs.python.org/3/c-api/intro.html#exceptions "Link to this heading")

--------------------------------------------------------------------------------------------

The Python programmer only needs to deal with exceptions if specific error handling is required; unhandled exceptions are automatically propagated to the caller, then to the caller’s caller, and so on, until they reach the top-level interpreter, where they are reported to the user accompanied by a stack traceback.

For C programmers, however, error checking always has to be explicit. All functions in the Python/C API can raise exceptions, unless an explicit claim is made otherwise in a function’s documentation. In general, when a function encounters an error, it sets an exception, discards any object references that it owns, and returns an error indicator. If not documented otherwise, this indicator is either `NULL` or `-1`, depending on the function’s return type. A few functions return a Boolean true/false result, with false indicating an error. Very few functions return no explicit error indicator or have an ambiguous return value, and require explicit testing for errors with [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
. These exceptions are always explicitly documented.

Exception state is maintained in per-thread storage (this is equivalent to using global storage in an unthreaded application). A thread can be in one of two states: an exception has occurred, or not. The function [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 can be used to check for this: it returns a borrowed reference to the exception type object when an exception has occurred, and `NULL` otherwise. There are a number of functions to set the exception state: [`PyErr_SetString()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetString "PyErr_SetString")
 is the most common (though not the most general) function to set the exception state, and [`PyErr_Clear()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Clear "PyErr_Clear")
 clears the exception state.

The full exception state consists of three objects (all of which can be `NULL`): the exception type, the corresponding exception value, and the traceback. These have the same meanings as the Python result of `sys.exc_info()`; however, they are not the same: the Python objects represent the last exception being handled by a Python [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 … [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
 statement, while the C level exception state only exists while an exception is being passed on between C functions until it reaches the Python bytecode interpreter’s main loop, which takes care of transferring it to `sys.exc_info()` and friends.

Note that starting with Python 1.5, the preferred, thread-safe way to access the exception state from Python code is to call the function [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info")
, which returns the per-thread exception state for Python code. Also, the semantics of both ways to access the exception state have changed so that a function which catches an exception will save and restore its thread’s exception state so as to preserve the exception state of its caller. This prevents common bugs in exception handling code caused by an innocent-looking function overwriting the exception being handled; it also reduces the often unwanted lifetime extension for objects that are referenced by the stack frames in the traceback.

As a general principle, a function that calls another function to perform some task should check whether the called function raised an exception, and if so, pass the exception state on to its caller. It should discard any object references that it owns, and return an error indicator, but it should _not_ set another exception — that would overwrite the exception that was just raised, and lose important information about the exact cause of the error.

A simple example of detecting exceptions and passing them on is shown in the `sum_sequence()` example above. It so happens that this example doesn’t need to clean up any owned references when it detects an error. The following example function shows some error cleanup. First, to remind you why you like Python, we show the equivalent Python code:

def incr\_item(dict, key):
    try:
        item \= dict\[key\]
    except KeyError:
        item \= 0
    dict\[key\] \= item + 1

Here is the corresponding C code, in all its glory:

int
incr\_item(PyObject \*dict, PyObject \*key)
{
    /\* Objects all initialized to NULL for Py\_XDECREF \*/
    PyObject \*item \= NULL, \*const\_one \= NULL, \*incremented\_item \= NULL;
    int rv \= \-1; /\* Return value initialized to -1 (failure) \*/

    item \= PyObject\_GetItem(dict, key);
    if (item \== NULL) {
        /\* Handle KeyError only: \*/
        if (!PyErr\_ExceptionMatches(PyExc\_KeyError))
            goto error;

        /\* Clear the error and use zero: \*/
        PyErr\_Clear();
        item \= PyLong\_FromLong(0L);
        if (item \== NULL)
            goto error;
    }
    const\_one \= PyLong\_FromLong(1L);
    if (const\_one \== NULL)
        goto error;

    incremented\_item \= PyNumber\_Add(item, const\_one);
    if (incremented\_item \== NULL)
        goto error;

    if (PyObject\_SetItem(dict, key, incremented\_item) < 0)
        goto error;
    rv \= 0; /\* Success \*/
    /\* Continue with cleanup code \*/

 error:
    /\* Cleanup code, shared by success and failure path \*/

    /\* Use Py\_XDECREF() to ignore NULL references \*/
    Py\_XDECREF(item);
    Py\_XDECREF(const\_one);
    Py\_XDECREF(incremented\_item);

    return rv; /\* -1 for error, 0 for success \*/
}

This example represents an endorsed use of the `goto` statement in C! It illustrates the use of [`PyErr_ExceptionMatches()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_ExceptionMatches "PyErr_ExceptionMatches")
 and [`PyErr_Clear()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Clear "PyErr_Clear")
 to handle specific exceptions, and the use of [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF")
 to dispose of owned references that may be `NULL` (note the `'X'` in the name; [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 would crash when confronted with a `NULL` reference). It is important that the variables used to hold owned references are initialized to `NULL` for this to work; likewise, the proposed return value is initialized to `-1` (failure) and only set to success after the final call made is successful.

Embedding Python[¶](https://docs.python.org/3/c-api/intro.html#embedding-python "Link to this heading")

--------------------------------------------------------------------------------------------------------

The one important task that only embedders (as opposed to extension writers) of the Python interpreter have to worry about is the initialization, and possibly the finalization, of the Python interpreter. Most functionality of the interpreter can only be used after the interpreter has been initialized.

The basic initialization function is [`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
. This initializes the table of loaded modules, and creates the fundamental modules [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")
, [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.")
, and [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
. It also initializes the module search path (`sys.path`).

[`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
 does not set the “script argument list” (`sys.argv`). If this variable is needed by Python code that will be executed later, setting [`PyConfig.argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.argv "PyConfig.argv")
 and [`PyConfig.parse_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.parse_argv "PyConfig.parse_argv")
 must be set: see [Python Initialization Configuration](https://docs.python.org/3/c-api/init_config.html#init-config)
.

On most systems (in particular, on Unix and Windows, although the details are slightly different), [`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
 calculates the module search path based upon its best guess for the location of the standard Python interpreter executable, assuming that the Python library is found in a fixed location relative to the Python interpreter executable. In particular, it looks for a directory named `lib/python_X.Y_` relative to the parent directory where the executable named `python` is found on the shell command search path (the environment variable `PATH`).

For instance, if the Python executable is found in `/usr/local/bin/python`, it will assume that the libraries are in `/usr/local/lib/python_X.Y_`. (In fact, this particular path is also the “fallback” location, used when no executable file named `python` is found along `PATH`.) The user can override this behavior by setting the environment variable [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
, or insert additional directories in front of the standard path by setting [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
.

The embedding application can steer the search by setting [`PyConfig.program_name`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.program_name "PyConfig.program_name")
 _before_ calling [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
. Note that [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)
 still overrides this and [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
 is still inserted in front of the standard path.

Sometimes, it is desirable to “uninitialize” Python. For instance, the application may want to start over (make another call to [`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
) or the application is simply done with its use of Python and wants to free memory allocated by Python. This can be accomplished by calling [`Py_FinalizeEx()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_FinalizeEx "Py_FinalizeEx")
. The function [`Py_IsInitialized()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IsInitialized "Py_IsInitialized")
 returns true if Python is currently in the initialized state. More information about these functions is given in a later chapter. Notice that `Py_FinalizeEx()` does _not_ free all memory allocated by the Python interpreter, e.g. memory allocated by extension modules currently cannot be released.

Debugging Builds[¶](https://docs.python.org/3/c-api/intro.html#debugging-builds "Link to this heading")

--------------------------------------------------------------------------------------------------------

Python can be built with several macros to enable extra checks of the interpreter and extension modules. These checks tend to add a large amount of overhead to the runtime so they are not enabled by default.

A full list of the various types of debugging builds is in the file `Misc/SpecialBuilds.txt` in the Python source distribution. Builds are available that support tracing of reference counts, debugging the memory allocator, or low-level profiling of the main interpreter loop. Only the most frequently used builds will be described in the remainder of this section.

Py\_DEBUG[¶](https://docs.python.org/3/c-api/intro.html#c.Py_DEBUG "Link to this definition")
  

Compiling the interpreter with the `Py_DEBUG` macro defined produces what is generally meant by [a debug build of Python](https://docs.python.org/3/using/configure.html#debug-build)
.

On Unix, `Py_DEBUG` can be enabled by adding [`--with-pydebug`](https://docs.python.org/3/using/configure.html#cmdoption-with-pydebug)
 to the `./configure` command. This will also disable compiler optimization.

On Windows, selecting a debug build (e.g., by passing the [`-d`](https://docs.python.org/3/using/cmdline.html#cmdoption-d)
 option to `PCbuild/build.bat`) automatically enables `Py_DEBUG`. Additionally, the presence of the not-Python-specific `_DEBUG` macro, when defined by the compiler, will also implicitly enable `Py_DEBUG`.

In addition to the reference count debugging described below, extra checks are performed. See [Python Debug Build](https://docs.python.org/3/using/configure.html#debug-build)
 for more details.

Defining `Py_TRACE_REFS` enables reference tracing (see the [`configure --with-trace-refs option`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs)
). When defined, a circular doubly linked list of active objects is maintained by adding two extra fields to every [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
. Total allocations are tracked as well. Upon exit, all existing references are printed. (In interactive mode this happens after every statement run by the interpreter.)

Please refer to `Misc/SpecialBuilds.txt` in the Python source distribution for more detailed information.

Recommended third party tools[¶](https://docs.python.org/3/c-api/intro.html#recommended-third-party-tools "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The following third party tools offer both simpler and more sophisticated approaches to creating C, C++ and Rust extensions for Python:

*   [Cython](https://cython.org/)
    
*   [cffi](https://cffi.readthedocs.io/)
    
*   [HPy](https://hpyproject.org/)
    
*   [nanobind](https://github.com/wjakob/nanobind)
     (C++)
    
*   [Numba](https://numba.pydata.org/)
    
*   [pybind11](https://pybind11.readthedocs.io/)
     (C++)
    
*   [PyO3](https://pyo3.rs/)
     (Rust)
    
*   [SWIG](https://www.swig.org/)
    

Using tools such as these can help avoid writing code that is tightly bound to a particular version of CPython, avoid reference counting errors, and focus more on your own code than on using the CPython API. In general, new versions of Python can be supported by updating the tool, and your code will often use newer and more efficient APIs automatically. Some tools also support compiling for other implementations of Python from a single set of sources.

These projects are not supported by the same people who maintain Python, and issues need to be raised with the projects directly. Remember to check that the project is still maintained and supported, as the list above may become outdated.

See also

[Python Packaging User Guide: Binary Extensions](https://packaging.python.org/guides/packaging-binary-extensions/)

The Python Packaging User Guide not only covers several available tools that simplify the creation of binary extensions, but also discusses the various reasons why creating an extension module may be desirable in the first place.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Introduction](https://docs.python.org/3/c-api/intro.html#)
    *   [Language version compatibility](https://docs.python.org/3/c-api/intro.html#language-version-compatibility)
        
    *   [Coding standards](https://docs.python.org/3/c-api/intro.html#coding-standards)
        
    *   [Include Files](https://docs.python.org/3/c-api/intro.html#include-files)
        *   [System includes](https://docs.python.org/3/c-api/intro.html#system-includes)
            
    *   [Useful macros](https://docs.python.org/3/c-api/intro.html#useful-macros)
        *   [Docstring macros](https://docs.python.org/3/c-api/intro.html#docstring-macros)
            
        *   [General utility macros](https://docs.python.org/3/c-api/intro.html#general-utility-macros)
            *   [Numeric utilities](https://docs.python.org/3/c-api/intro.html#numeric-utilities)
                
            *   [Assertion utilities](https://docs.python.org/3/c-api/intro.html#assertion-utilities)
                
            *   [Type size utilities](https://docs.python.org/3/c-api/intro.html#type-size-utilities)
                
            *   [Macro definition utilities](https://docs.python.org/3/c-api/intro.html#macro-definition-utilities)
                
        *   [Declaration utilities](https://docs.python.org/3/c-api/intro.html#declaration-utilities)
            
        *   [Outdated macros](https://docs.python.org/3/c-api/intro.html#outdated-macros)
            
    *   [Objects, Types and Reference Counts](https://docs.python.org/3/c-api/intro.html#objects-types-and-reference-counts)
        *   [Reference Counts](https://docs.python.org/3/c-api/intro.html#reference-counts)
            *   [Reference Count Details](https://docs.python.org/3/c-api/intro.html#reference-count-details)
                
        *   [Types](https://docs.python.org/3/c-api/intro.html#types)
            
    *   [Exceptions](https://docs.python.org/3/c-api/intro.html#exceptions)
        
    *   [Embedding Python](https://docs.python.org/3/c-api/intro.html#embedding-python)
        
    *   [Debugging Builds](https://docs.python.org/3/c-api/intro.html#debugging-builds)
        
    *   [Recommended third party tools](https://docs.python.org/3/c-api/intro.html#recommended-third-party-tools)
        

#### Previous topic

[Python/C API reference manual](https://docs.python.org/3/c-api/index.html "previous chapter")

#### Next topic

[C API and ABI Stability](https://docs.python.org/3/c-api/stable.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Introduction&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fintro.html&pagesource=c-api%2Fintro.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/intro.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/stable.html "C API and ABI Stability")
     |
*   [previous](https://docs.python.org/3/c-api/index.html "Python/C API reference manual")
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
*   [Introduction](https://docs.python.org/3/c-api/intro.html)
    
*    
    
    |
*   Theme Auto Light Dark |