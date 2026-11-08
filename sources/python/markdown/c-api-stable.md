### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/veryhigh.html "The Very High Level Layer")
     |
*   [previous](https://docs.python.org/3/c-api/intro.html "Introduction")
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
*   [C API and ABI Stability](https://docs.python.org/3/c-api/stable.html)
    
*    
    
    |
*   Theme Auto Light Dark |

C API and ABI Stability[¶](https://docs.python.org/3/c-api/stable.html#c-api-and-abi-stability "Link to this heading")

=======================================================================================================================

Unless documented otherwise, Python’s C API is covered by the Backwards Compatibility Policy, [**PEP 387**](https://peps.python.org/pep-0387/)
. Most changes to it are source-compatible (typically by only adding new API). Changing existing API or removing API is only done after a deprecation period or to fix serious issues.

CPython’s Application Binary Interface (ABI) is forward- and backwards-compatible across a minor release (if these are compiled the same way; see [Platform Considerations](https://docs.python.org/3/c-api/stable.html#stable-abi-platform)
 below). So, code compiled for Python 3.10.0 will work on 3.10.8 and vice versa, but will need to be compiled separately for 3.9.x and 3.11.x.

There are two tiers of C API with different stability expectations:

*   [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
    , may change in minor versions without a deprecation period. It is marked by the `PyUnstable` prefix in names.
    
*   [Limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
    , is compatible across several minor releases. When [`Py_LIMITED_API`](https://docs.python.org/3/c-api/stable.html#c.Py_LIMITED_API "Py_LIMITED_API")
     is defined, only this subset is exposed from `Python.h`.
    

These are discussed in more detail below.

Names prefixed by an underscore, such as `_Py_InternalState`, are private API that can change without notice even in patch releases. If you need to use this API, consider reaching out to [CPython developers](https://discuss.python.org/c/core-dev/c-api/30)
 to discuss adding public API for your use case.

Unstable C API[¶](https://docs.python.org/3/c-api/stable.html#unstable-c-api "Link to this heading")

-----------------------------------------------------------------------------------------------------

Any API named with the `PyUnstable` prefix exposes CPython implementation details, and may change in every minor release (e.g. from 3.9 to 3.10) without any deprecation warnings. However, it will not change in a bugfix release (e.g. from 3.10.0 to 3.10.1).

It is generally intended for specialized, low-level tools like debuggers.

Projects that use this API are expected to follow CPython development and spend extra effort adjusting to changes.

Stable Application Binary Interfaces[¶](https://docs.python.org/3/c-api/stable.html#stable-application-binary-interfaces "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Python’s _Stable ABI_ allows extensions to be compatible with multiple versions of Python, without recompilation.

Note

For simplicity, this document talks about _extensions_, but Stable ABI works the same way for all uses of the API – for example, embedding Python.

There are two Stable ABIs:

*   `abi3`, introduced in Python 3.2, is compatible with **non**\-[free-threaded](https://docs.python.org/3/glossary.html#term-free-threaded-build)
     builds of CPython.
    
*   `abi3t`, introduced in Python 3.15, is compatible with [free-threaded](https://docs.python.org/3/glossary.html#term-free-threaded-build)
     builds of CPython. It has stricter API limitations than `abi3`.
    
    > Added in version 3.15: `abi3t` was added in [**PEP 803**](https://peps.python.org/pep-0803/)
    

It is possible for an extension to be compiled for _both_ `abi3` and `abi3t` at the same time; the result will be compatible with both free-threaded and non-free-threaded builds of Python. Currently, this has no downsides compared to compiling for `abi3t` only.

Each Stable ABI is versioned using the first two numbers of the Python version. For example, Stable ABI 3.14 corresponds to Python 3.14. An extension compiled for Stable ABI 3.x is ABI-compatible with Python 3.x and above.

Extensions that target a stable ABI must only use a limited subset of the C API. This subset is known as the _Limited API_; its contents are [listed below](https://docs.python.org/3/c-api/stable.html#limited-api-list)
.

On Windows, extensions that use a Stable ABI should be linked against `python3.dll` rather than a version-specific library such as `python39.dll`. This library only exposes the relevant symbols.

On some platforms, Python will look for and load shared library files named with the `abi3` or `abi3t` tag (for example, `mymodule.abi3.so`). [Free-threaded](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 interpreters only recognize the `abi3t` tag, while non-free-threaded ones will prefer `abi3` but fall back to `abi3t`. Thus, extensions compatible with both ABIs should use the `abi3t` tag.

Python does not necessarily check that extensions it loads have compatible ABI. Extension authors are encouraged to add a check using the [`Py_mod_abi`](https://docs.python.org/3/c-api/module.html#c.Py_mod_abi "Py_mod_abi")
 slot or the [`PyABIInfo_Check()`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_Check "PyABIInfo_Check")
 function, but the user (or their packaging tool) is ultimately responsible for ensuring that, for example, extensions built for Stable ABI 3.10 are not installed for lower versions of Python.

All functions in Stable ABI are present as functions in Python’s shared library, not solely as macros. This makes them usable in languages that don’t use the C preprocessor, including Python’s [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
.

### Compiling for Stable ABI[¶](https://docs.python.org/3/c-api/stable.html#compiling-for-stable-abi "Link to this heading")

Note

Build tools (such as, for example, meson-python, scikit-build-core, or Setuptools) often have a mechanism for setting macros and synchronizing them with extension filenames and other metadata. Prefer using such a mechanism, if it exists, over defining the macros manually.

The rest of this section is mainly relevant for tool authors, and for people who compile extensions manually.

See also

[list of recommended tools](https://packaging.python.org/en/latest/guides/tool-recommendations/#build-backends-for-extension-modules)
 in the Python Packaging User Guide

To compile for a Stable ABI, define one or both of the following macros to the lowest Python version your extension should support, in [`Py_PACK_VERSION`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_PACK_VERSION "Py_PACK_VERSION")
 format. Typically, you should choose a specific value rather than the version of the Python headers you are compiling against.

The macros must be defined before including `Python.h`. Since [`Py_PACK_VERSION`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_PACK_VERSION "Py_PACK_VERSION")
 is not available at this point, you will need to use the numeric value directly. For reference, the values for a few recent Python versions are:

0x30a0000  /\* Py\_PACK\_VERSION(3,10) \*/
0x30b0000  /\* Py\_PACK\_VERSION(3,11) \*/
0x30c0000  /\* Py\_PACK\_VERSION(3,12) \*/
0x30d0000  /\* Py\_PACK\_VERSION(3,13) \*/
0x30e0000  /\* Py\_PACK\_VERSION(3,14) \*/
0x30f0000  /\* Py\_PACK\_VERSION(3,15) \*/

When one of the macros is defined, `Python.h` will only expose API that is compatible with the given Stable ABI – that is, the [Limited API](https://docs.python.org/3/c-api/stable.html#limited-api-list)
 plus some definitions that need to be visible to the compiler but should not be used directly. When both are defined, `Python.h` will only expose API compatible with both Stable ABIs.

Py\_LIMITED\_API[¶](https://docs.python.org/3/c-api/stable.html#c.Py_LIMITED_API "Link to this definition")
  

Target `abi3`, that is, non-[free-threaded builds](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 of CPython. See [above](https://docs.python.org/3/c-api/stable.html#abi3-compiling)
 for common information.

Py\_TARGET\_ABI3T[¶](https://docs.python.org/3/c-api/stable.html#c.Py_TARGET_ABI3T "Link to this definition")
  

Target `abi3t`, that is, [free-threaded builds](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 of CPython. See [above](https://docs.python.org/3/c-api/stable.html#abi3-compiling)
 for common information.

Added in version 3.15.

Both macros specify a target ABI; the different naming style is due to backwards compatibility.

Historical note

You can also define `Py_LIMITED_API` as `3`. This works the same as `0x03020000` (Python 3.2, the version that introduced Stable ABI).

When both are defined, `Python.h` may, or may not, redefine `Py_LIMITED_API` to match `Py_TARGET_ABI3T`.

On a [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 – that is, when [`Py_GIL_DISABLED`](https://docs.python.org/3/using/configure.html#c.Py_GIL_DISABLED "Py_GIL_DISABLED")
 is defined – `Py_TARGET_ABI3T` defaults to the value of `Py_LIMITED_API`. This means that there are two ways to build for both `abi3` and `abi3t`:

*   define both `Py_LIMITED_API` and `Py_TARGET_ABI3T`, or
    
*   define only `Py_LIMITED_API` and:
    
    *   on Windows, define `Py_GIL_DISABLED`;
        
    *   on other systems, use the headers of free-threaded build of Python.
        

### Stable ABI Scope and Performance[¶](https://docs.python.org/3/c-api/stable.html#stable-abi-scope-and-performance "Link to this heading")

The goal for Stable ABI is to allow everything that is possible with the full C API, but possibly with a performance penalty. Generally, compatibility with Stable ABI will require some changes to an extension’s source code.

For example, while [`PyList_GetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem "PyList_GetItem")
 is available, its “unsafe” macro variant [`PyList_GET_ITEM()`](https://docs.python.org/3/c-api/list.html#c.PyList_GET_ITEM "PyList_GET_ITEM")
 is not. The macro can be faster because it can rely on version-specific implementation details of the list object.

For another example, when _not_ compiling for Stable ABI, some C API functions are inlined or replaced by macros. Compiling for Stable ABI disables this inlining, allowing stability as Python’s data structures are improved, but possibly reducing performance.

By leaving out the `Py_LIMITED_API` or `Py_TARGET_ABI3T` definition, it is possible to compile Stable-ABI-compatible source for a version-specific ABI. A potentially faster version-specific extension can then be distributed alongside a version compiled for Stable ABI – a slower but more compatible fallback.

### Stable ABI Caveats[¶](https://docs.python.org/3/c-api/stable.html#stable-abi-caveats "Link to this heading")

Note that compiling for Stable ABI is _not_ a complete guarantee that code will be compatible with the expected Python versions. Stable ABI prevents _ABI_ issues, like linker errors due to missing symbols or data corruption due to changes in structure layouts or function signatures. However, other changes in Python can change the _behavior_ of extensions.

One issue that the [`Py_TARGET_ABI3T`](https://docs.python.org/3/c-api/stable.html#c.Py_TARGET_ABI3T "Py_TARGET_ABI3T")
 and [`Py_LIMITED_API`](https://docs.python.org/3/c-api/stable.html#c.Py_LIMITED_API "Py_LIMITED_API")
 macros do not guard against is calling a function with arguments that are invalid in a lower Python version. For example, consider a function that starts accepting `NULL` for an argument. In Python 3.9, `NULL` now selects a default behavior, but in Python 3.8, the argument will be used directly, causing a `NULL` dereference and crash. A similar argument works for fields of structs.

For these reasons, we recommend testing an extension with _all_ minor Python versions it supports.

We also recommend reviewing documentation of all used API to check if it is explicitly part of the Limited API. Even with `Py_LIMITED_API` defined, a few private declarations are exposed for technical reasons (or even unintentionally, as bugs).

Also note that while compiling with `Py_LIMITED_API` 3.8 means that the extension should _load_ on Python 3.12, and _compile_ with Python 3.12, the same source will not necessarily compile with `Py_LIMITED_API` set to 3.12. In general, parts of the Limited API may be deprecated and removed, provided that Stable ABI stays stable.

Platform Considerations[¶](https://docs.python.org/3/c-api/stable.html#platform-considerations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

ABI stability depends not only on Python, but also on the compiler used, lower-level libraries and compiler options. For the purposes of the [Stable ABIs](https://docs.python.org/3/c-api/stable.html#stable-abi)
, these details define a “platform”. They usually depend on the OS type and processor architecture

It is the responsibility of each particular distributor of Python to ensure that all Python versions on a particular platform are built in a way that does not break the Stable ABIs, or the version-specific ABIs. This is the case with Windows and macOS releases from `python.org` and many third-party distributors.

ABI Checking[¶](https://docs.python.org/3/c-api/stable.html#abi-checking "Link to this heading")

-------------------------------------------------------------------------------------------------

Added in version 3.15.

Python includes a rudimentary check for ABI compatibility.

This check is not comprehensive. It only guards against common cases of incompatible modules being installed for the wrong interpreter. It also does not take [platform incompatibilities](https://docs.python.org/3/c-api/stable.html#stable-abi-platform)
 into account. It can only be done after an extension is successfully loaded.

Despite these limitations, it is recommended that extension modules use this mechanism, so that detectable incompatibilities raise exceptions rather than crash.

Most modules can use this check via the [`Py_mod_abi`](https://docs.python.org/3/c-api/module.html#c.Py_mod_abi "Py_mod_abi")
 slot and the [`PyABIInfo_VAR`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_VAR "PyABIInfo_VAR")
 macro, for example like this:

PyABIInfo\_VAR(abi\_info);

static PyModuleDef\_Slot mymodule\_slots\[\] \= {
   {Py\_mod\_abi, &abi\_info},
   ...
};

The full API is described below for advanced use cases.

int PyABIInfo\_Check([PyABIInfo](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo "PyABIInfo")
 \*info, const char \*module\_name)[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_Check "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Verify that the given _info_ is compatible with the currently running interpreter.

Return 0 on success. On failure, raise an exception and return -1.

If the ABI is incompatible, the raised exception will be [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
.

The _module\_name_ argument can be `NULL`, or point to a NUL-terminated UTF-8-encoded string used for error messages.

Note that if _info_ describes the ABI that the current code uses (as defined by [`PyABIInfo_VAR`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_VAR "PyABIInfo_VAR")
, for example), using any other Python C API may lead to crashes. In particular, it is not safe to examine the raised exception.

Added in version 3.15.

PyABIInfo\_VAR(NAME)[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_VAR "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Define a static [`PyABIInfo`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo "PyABIInfo")
 variable with the given _NAME_ that describes the ABI that the current code will use. This macro expands to:

static PyABIInfo NAME \= {
    1, 0,
    PyABIInfo\_DEFAULT\_FLAGS,
    PY\_VERSION\_HEX,
    PyABIInfo\_DEFAULT\_ABI\_VERSION
}

Added in version 3.15.

type PyABIInfo[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members) since version 3.15._

uint8\_t abiinfo\_major\_version[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo.abiinfo_major_version "Link to this definition")
  

The major version of [`PyABIInfo`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo "PyABIInfo")
. Can be set to:

*   `0` to skip all checking, or
    
*   `1` to specify this version of `PyABIInfo`.
    

uint8\_t abiinfo\_minor\_version[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo.abiinfo_minor_version "Link to this definition")
  

The minor version of [`PyABIInfo`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo "PyABIInfo")
. Must be set to `0`; larger values are reserved for backwards-compatible future versions of `PyABIInfo`.

uint16\_t flags[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo.flags "Link to this definition")
  

This field is usually set to the following macro:

PyABIInfo\_DEFAULT\_FLAGS[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_DEFAULT_FLAGS "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Default flags, based on current values of macros such as [`Py_LIMITED_API`](https://docs.python.org/3/c-api/stable.html#c.Py_LIMITED_API "Py_LIMITED_API")
 and [`Py_GIL_DISABLED`](https://docs.python.org/3/using/configure.html#c.Py_GIL_DISABLED "Py_GIL_DISABLED")
.

Alternately, the field can be set to the following flags, combined by bitwise OR. Unused bits must be set to zero.

ABI variant – one of:

> PyABIInfo\_STABLE[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_STABLE "Link to this definition")
>   
> 
> _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
>  since version 3.15._
> 
> Specifies that Stable ABI is used.
> 
> PyABIInfo\_INTERNAL[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_INTERNAL "Link to this definition")
>   
> 
> Specifies ABI specific to a particular build of CPython. Internal use only.

Free-threading compatibility – one of:

> PyABIInfo\_FREETHREADED[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_FREETHREADED "Link to this definition")
>   
> 
> _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
>  since version 3.15._
> 
> Specifies ABI compatible with [free-threaded builds](https://docs.python.org/3/glossary.html#term-free-threaded-build)
>  of CPython. (That is, ones compiled with [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
> ; with `t` in [`sys.abiflags`](https://docs.python.org/3/library/sys.html#sys.abiflags "sys.abiflags")
> )
> 
> PyABIInfo\_GIL[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_GIL "Link to this definition")
>   
> 
> _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
>  since version 3.15._
> 
> Specifies ABI compatible with non-free-threaded builds of CPython (ones compiled _without_ [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
> ).
> 
> PyABIInfo\_FREETHREADING\_AGNOSTIC[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_FREETHREADING_AGNOSTIC "Link to this definition")
>   
> 
> _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
>  since version 3.15._
> 
> Specifies ABI compatible with both free-threaded and non-free-threaded builds of CPython, that is, both `abi3` and `abi3t`.

uint32\_t build\_version[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo.build_version "Link to this definition")
  

The version of the Python headers used to build the code, in the format used by [`PY_VERSION_HEX`](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_VERSION_HEX "PY_VERSION_HEX")
.

This can be set to `0` to skip any checks related to this field. This option is meant mainly for projects that do not use the CPython headers directly, and do not emulate a specific version of them.

uint32\_t abi\_version[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo.abi_version "Link to this definition")
  

The ABI version.

For Stable ABI, this field should be the value of [`Py_LIMITED_API`](https://docs.python.org/3/c-api/stable.html#c.Py_LIMITED_API "Py_LIMITED_API")
 or [`Py_TARGET_ABI3T`](https://docs.python.org/3/c-api/stable.html#c.Py_TARGET_ABI3T "Py_TARGET_ABI3T")
. If both are defined, use the smaller value. (If `Py_LIMITED_API` is `3`; use [Py\_PACK\_VERSION](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_PACK_VERSION "Py_PACK_VERSION")
(3, 2) instead of `3`.)

Otherwise, it should be set to [`PY_VERSION_HEX`](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_VERSION_HEX "PY_VERSION_HEX")
.

It can also be set to `0` to skip any checks related to this field.

PyABIInfo\_DEFAULT\_ABI\_VERSION[¶](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_DEFAULT_ABI_VERSION "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

The value that should be used for this field, based on current values of macros such as [`Py_LIMITED_API`](https://docs.python.org/3/c-api/stable.html#c.Py_LIMITED_API "Py_LIMITED_API")
, [`PY_VERSION_HEX`](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_VERSION_HEX "PY_VERSION_HEX")
 and [`Py_GIL_DISABLED`](https://docs.python.org/3/using/configure.html#c.Py_GIL_DISABLED "Py_GIL_DISABLED")
.

Added in version 3.15.

Contents of Limited API[¶](https://docs.python.org/3/c-api/stable.html#contents-of-limited-api "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

This is the definitive list of [Limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
 for Python 3.15:

*   [`METH_CLASS`](https://docs.python.org/3/c-api/structures.html#c.METH_CLASS "METH_CLASS")
    
*   [`METH_COEXIST`](https://docs.python.org/3/c-api/structures.html#c.METH_COEXIST "METH_COEXIST")
    
*   [`METH_FASTCALL`](https://docs.python.org/3/c-api/structures.html#c.METH_FASTCALL "METH_FASTCALL")
    
*   [`METH_METHOD`](https://docs.python.org/3/c-api/structures.html#c.METH_METHOD "METH_METHOD")
    
*   [`METH_NOARGS`](https://docs.python.org/3/c-api/structures.html#c.METH_NOARGS "METH_NOARGS")
    
*   [`METH_O`](https://docs.python.org/3/c-api/structures.html#c.METH_O "METH_O")
    
*   [`METH_STATIC`](https://docs.python.org/3/c-api/structures.html#c.METH_STATIC "METH_STATIC")
    
*   [`METH_VARARGS`](https://docs.python.org/3/c-api/structures.html#c.METH_VARARGS "METH_VARARGS")
    
*   [`PY_VECTORCALL_ARGUMENTS_OFFSET`](https://docs.python.org/3/c-api/call.html#c.PY_VECTORCALL_ARGUMENTS_OFFSET "PY_VECTORCALL_ARGUMENTS_OFFSET")
    
*   [`PyABIInfo`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo "PyABIInfo")
    
*   [`PyABIInfo_Check()`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_Check "PyABIInfo_Check")
    
*   [`PyABIInfo_DEFAULT_ABI_VERSION`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_DEFAULT_ABI_VERSION "PyABIInfo_DEFAULT_ABI_VERSION")
    
*   [`PyABIInfo_DEFAULT_FLAGS`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_DEFAULT_FLAGS "PyABIInfo_DEFAULT_FLAGS")
    
*   [`PyABIInfo_FREETHREADED`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_FREETHREADED "PyABIInfo_FREETHREADED")
    
*   [`PyABIInfo_FREETHREADING_AGNOSTIC`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_FREETHREADING_AGNOSTIC "PyABIInfo_FREETHREADING_AGNOSTIC")
    
*   [`PyABIInfo_GIL`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_GIL "PyABIInfo_GIL")
    
*   [`PyABIInfo_STABLE`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_STABLE "PyABIInfo_STABLE")
    
*   [`PyABIInfo_VAR`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_VAR "PyABIInfo_VAR")
    
*   [`PyAIter_Check()`](https://docs.python.org/3/c-api/iter.html#c.PyAIter_Check "PyAIter_Check")
    
*   [`PyArg_Parse()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_Parse "PyArg_Parse")
    
*   [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
    
*   [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords")
    
*   [`PyArg_UnpackTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple "PyArg_UnpackTuple")
    
*   [`PyArg_VaParse()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_VaParse "PyArg_VaParse")
    
*   [`PyArg_VaParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_VaParseTupleAndKeywords "PyArg_VaParseTupleAndKeywords")
    
*   [`PyArg_ValidateKeywordArguments()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ValidateKeywordArguments "PyArg_ValidateKeywordArguments")
    
*   [`PyBUF_ANY_CONTIGUOUS`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_ANY_CONTIGUOUS "PyBUF_ANY_CONTIGUOUS")
    
*   [`PyBUF_CONTIG`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_CONTIG "PyBUF_CONTIG")
    
*   [`PyBUF_CONTIG_RO`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_CONTIG_RO "PyBUF_CONTIG_RO")
    
*   [`PyBUF_C_CONTIGUOUS`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_C_CONTIGUOUS "PyBUF_C_CONTIGUOUS")
    
*   [`PyBUF_FORMAT`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_FORMAT "PyBUF_FORMAT")
    
*   [`PyBUF_FULL`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_FULL "PyBUF_FULL")
    
*   [`PyBUF_FULL_RO`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_FULL_RO "PyBUF_FULL_RO")
    
*   [`PyBUF_F_CONTIGUOUS`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_F_CONTIGUOUS "PyBUF_F_CONTIGUOUS")
    
*   [`PyBUF_INDIRECT`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_INDIRECT "PyBUF_INDIRECT")
    
*   [`PyBUF_MAX_NDIM`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_MAX_NDIM "PyBUF_MAX_NDIM")
    
*   [`PyBUF_ND`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_ND "PyBUF_ND")
    
*   [`PyBUF_READ`](https://docs.python.org/3/c-api/memoryview.html#c.PyBUF_READ "PyBUF_READ")
    
*   [`PyBUF_RECORDS`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_RECORDS "PyBUF_RECORDS")
    
*   [`PyBUF_RECORDS_RO`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_RECORDS_RO "PyBUF_RECORDS_RO")
    
*   [`PyBUF_SIMPLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_SIMPLE "PyBUF_SIMPLE")
    
*   [`PyBUF_STRIDED`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_STRIDED "PyBUF_STRIDED")
    
*   [`PyBUF_STRIDED_RO`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_STRIDED_RO "PyBUF_STRIDED_RO")
    
*   [`PyBUF_STRIDES`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_STRIDES "PyBUF_STRIDES")
    
*   [`PyBUF_WRITABLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITABLE "PyBUF_WRITABLE")
    
*   [`PyBUF_WRITE`](https://docs.python.org/3/c-api/memoryview.html#c.PyBUF_WRITE "PyBUF_WRITE")
    
*   [`PyBaseObject_Type`](https://docs.python.org/3/c-api/structures.html#c.PyBaseObject_Type "PyBaseObject_Type")
    
*   [`PyBool_FromLong()`](https://docs.python.org/3/c-api/bool.html#c.PyBool_FromLong "PyBool_FromLong")
    
*   [`PyBool_Type`](https://docs.python.org/3/c-api/bool.html#c.PyBool_Type "PyBool_Type")
    
*   [`PyBuffer_FillContiguousStrides()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_FillContiguousStrides "PyBuffer_FillContiguousStrides")
    
*   [`PyBuffer_FillInfo()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_FillInfo "PyBuffer_FillInfo")
    
*   [`PyBuffer_FromContiguous()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_FromContiguous "PyBuffer_FromContiguous")
    
*   [`PyBuffer_GetPointer()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_GetPointer "PyBuffer_GetPointer")
    
*   [`PyBuffer_IsContiguous()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_IsContiguous "PyBuffer_IsContiguous")
    
*   [`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
    
*   [`PyBuffer_SizeFromFormat()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_SizeFromFormat "PyBuffer_SizeFromFormat")
    
*   [`PyBuffer_ToContiguous()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_ToContiguous "PyBuffer_ToContiguous")
    
*   [`PyByteArrayIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyByteArrayIter_Type "PyByteArrayIter_Type")
    
*   [`PyByteArray_AsString()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_AsString "PyByteArray_AsString")
    
*   [`PyByteArray_Concat()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Concat "PyByteArray_Concat")
    
*   [`PyByteArray_FromObject()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_FromObject "PyByteArray_FromObject")
    
*   [`PyByteArray_FromStringAndSize()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_FromStringAndSize "PyByteArray_FromStringAndSize")
    
*   [`PyByteArray_Resize()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Resize "PyByteArray_Resize")
    
*   [`PyByteArray_Size()`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Size "PyByteArray_Size")
    
*   [`PyByteArray_Type`](https://docs.python.org/3/c-api/bytearray.html#c.PyByteArray_Type "PyByteArray_Type")
    
*   [`PyBytesIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyBytesIter_Type "PyBytesIter_Type")
    
*   [`PyBytes_AsString()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_AsString "PyBytes_AsString")
    
*   [`PyBytes_AsStringAndSize()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_AsStringAndSize "PyBytes_AsStringAndSize")
    
*   [`PyBytes_Concat()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Concat "PyBytes_Concat")
    
*   [`PyBytes_ConcatAndDel()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_ConcatAndDel "PyBytes_ConcatAndDel")
    
*   [`PyBytes_DecodeEscape()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_DecodeEscape "PyBytes_DecodeEscape")
    
*   [`PyBytes_FromFormat()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromFormat "PyBytes_FromFormat")
    
*   [`PyBytes_FromFormatV()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromFormatV "PyBytes_FromFormatV")
    
*   [`PyBytes_FromObject()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromObject "PyBytes_FromObject")
    
*   [`PyBytes_FromString()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromString "PyBytes_FromString")
    
*   [`PyBytes_FromStringAndSize()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromStringAndSize "PyBytes_FromStringAndSize")
    
*   [`PyBytes_Repr()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Repr "PyBytes_Repr")
    
*   [`PyBytes_Size()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Size "PyBytes_Size")
    
*   [`PyBytes_Type`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Type "PyBytes_Type")
    
*   [`PyCFunction`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction "PyCFunction")
    
*   [`PyCFunctionFast`](https://docs.python.org/3/c-api/structures.html#c.PyCFunctionFast "PyCFunctionFast")
    
*   [`PyCFunctionFastWithKeywords`](https://docs.python.org/3/c-api/structures.html#c.PyCFunctionFastWithKeywords "PyCFunctionFastWithKeywords")
    
*   [`PyCFunctionWithKeywords`](https://docs.python.org/3/c-api/structures.html#c.PyCFunctionWithKeywords "PyCFunctionWithKeywords")
    
*   [`PyCFunction_GetFlags()`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GetFlags "PyCFunction_GetFlags")
    
*   [`PyCFunction_GetFunction()`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GetFunction "PyCFunction_GetFunction")
    
*   [`PyCFunction_GetSelf()`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GetSelf "PyCFunction_GetSelf")
    
*   [`PyCFunction_New()`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_New "PyCFunction_New")
    
*   [`PyCFunction_NewEx()`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_NewEx "PyCFunction_NewEx")
    
*   [`PyCFunction_Type`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_Type "PyCFunction_Type")
    
*   [`PyCMethod_New()`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod_New "PyCMethod_New")
    
*   [`PyCallIter_New()`](https://docs.python.org/3/c-api/iterator.html#c.PyCallIter_New "PyCallIter_New")
    
*   [`PyCallIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyCallIter_Type "PyCallIter_Type")
    
*   [`PyCallable_Check()`](https://docs.python.org/3/c-api/call.html#c.PyCallable_Check "PyCallable_Check")
    
*   [`PyCapsule_Destructor`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Destructor "PyCapsule_Destructor")
    
*   [`PyCapsule_GetContext()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_GetContext "PyCapsule_GetContext")
    
*   [`PyCapsule_GetDestructor()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_GetDestructor "PyCapsule_GetDestructor")
    
*   [`PyCapsule_GetName()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_GetName "PyCapsule_GetName")
    
*   [`PyCapsule_GetPointer()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_GetPointer "PyCapsule_GetPointer")
    
*   [`PyCapsule_Import()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Import "PyCapsule_Import")
    
*   [`PyCapsule_IsValid()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_IsValid "PyCapsule_IsValid")
    
*   [`PyCapsule_New()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_New "PyCapsule_New")
    
*   [`PyCapsule_SetContext()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_SetContext "PyCapsule_SetContext")
    
*   [`PyCapsule_SetDestructor()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_SetDestructor "PyCapsule_SetDestructor")
    
*   [`PyCapsule_SetName()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_SetName "PyCapsule_SetName")
    
*   [`PyCapsule_SetPointer()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_SetPointer "PyCapsule_SetPointer")
    
*   [`PyCapsule_Type`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Type "PyCapsule_Type")
    
*   [`PyClassMethodDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyClassMethodDescr_Type "PyClassMethodDescr_Type")
    
*   [`PyCodec_BackslashReplaceErrors()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_BackslashReplaceErrors "PyCodec_BackslashReplaceErrors")
    
*   [`PyCodec_Decode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")
    
*   [`PyCodec_Decoder()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decoder "PyCodec_Decoder")
    
*   [`PyCodec_Encode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")
    
*   [`PyCodec_Encoder()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encoder "PyCodec_Encoder")
    
*   [`PyCodec_IgnoreErrors()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_IgnoreErrors "PyCodec_IgnoreErrors")
    
*   [`PyCodec_IncrementalDecoder()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_IncrementalDecoder "PyCodec_IncrementalDecoder")
    
*   [`PyCodec_IncrementalEncoder()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_IncrementalEncoder "PyCodec_IncrementalEncoder")
    
*   [`PyCodec_KnownEncoding()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_KnownEncoding "PyCodec_KnownEncoding")
    
*   [`PyCodec_LookupError()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_LookupError "PyCodec_LookupError")
    
*   [`PyCodec_NameReplaceErrors()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_NameReplaceErrors "PyCodec_NameReplaceErrors")
    
*   [`PyCodec_Register()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Register "PyCodec_Register")
    
*   [`PyCodec_RegisterError()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_RegisterError "PyCodec_RegisterError")
    
*   [`PyCodec_ReplaceErrors()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_ReplaceErrors "PyCodec_ReplaceErrors")
    
*   [`PyCodec_StreamReader()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_StreamReader "PyCodec_StreamReader")
    
*   [`PyCodec_StreamWriter()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_StreamWriter "PyCodec_StreamWriter")
    
*   [`PyCodec_StrictErrors()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_StrictErrors "PyCodec_StrictErrors")
    
*   [`PyCodec_Unregister()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Unregister "PyCodec_Unregister")
    
*   [`PyCodec_XMLCharRefReplaceErrors()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_XMLCharRefReplaceErrors "PyCodec_XMLCharRefReplaceErrors")
    
*   [`PyComplex_FromDoubles()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_FromDoubles "PyComplex_FromDoubles")
    
*   [`PyComplex_ImagAsDouble()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_ImagAsDouble "PyComplex_ImagAsDouble")
    
*   [`PyComplex_RealAsDouble()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_RealAsDouble "PyComplex_RealAsDouble")
    
*   [`PyComplex_Type`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_Type "PyComplex_Type")
    
*   [`PyCriticalSection`](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection "PyCriticalSection")
    
*   [`PyCriticalSection2`](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection2 "PyCriticalSection2")
    
*   [`PyCriticalSection2_Begin()`](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection2_Begin "PyCriticalSection2_Begin")
    
*   [`PyCriticalSection2_End()`](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection2_End "PyCriticalSection2_End")
    
*   [`PyCriticalSection_Begin()`](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection_Begin "PyCriticalSection_Begin")
    
*   [`PyCriticalSection_End()`](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection_End "PyCriticalSection_End")
    
*   [`PyDescr_NewClassMethod()`](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewClassMethod "PyDescr_NewClassMethod")
    
*   [`PyDescr_NewGetSet()`](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewGetSet "PyDescr_NewGetSet")
    
*   [`PyDescr_NewMember()`](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewMember "PyDescr_NewMember")
    
*   [`PyDescr_NewMethod()`](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewMethod "PyDescr_NewMethod")
    
*   [`PyDictItems_Type`](https://docs.python.org/3/c-api/dict.html#c.PyDictItems_Type "PyDictItems_Type")
    
*   [`PyDictIterItem_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyDictIterItem_Type "PyDictIterItem_Type")
    
*   [`PyDictIterKey_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyDictIterKey_Type "PyDictIterKey_Type")
    
*   [`PyDictIterValue_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyDictIterValue_Type "PyDictIterValue_Type")
    
*   [`PyDictKeys_Type`](https://docs.python.org/3/c-api/dict.html#c.PyDictKeys_Type "PyDictKeys_Type")
    
*   [`PyDictProxy_New()`](https://docs.python.org/3/c-api/dict.html#c.PyDictProxy_New "PyDictProxy_New")
    
*   [`PyDictProxy_Type`](https://docs.python.org/3/c-api/dict.html#c.PyDictProxy_Type "PyDictProxy_Type")
    
*   [`PyDictRevIterItem_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyDictRevIterItem_Type "PyDictRevIterItem_Type")
    
*   [`PyDictRevIterKey_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyDictRevIterKey_Type "PyDictRevIterKey_Type")
    
*   [`PyDictRevIterValue_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyDictRevIterValue_Type "PyDictRevIterValue_Type")
    
*   [`PyDictValues_Type`](https://docs.python.org/3/c-api/dict.html#c.PyDictValues_Type "PyDictValues_Type")
    
*   [`PyDict_Clear()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Clear "PyDict_Clear")
    
*   [`PyDict_Contains()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Contains "PyDict_Contains")
    
*   [`PyDict_Copy()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Copy "PyDict_Copy")
    
*   [`PyDict_DelItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_DelItem "PyDict_DelItem")
    
*   [`PyDict_DelItemString()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_DelItemString "PyDict_DelItemString")
    
*   [`PyDict_GetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem "PyDict_GetItem")
    
*   [`PyDict_GetItemRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemRef "PyDict_GetItemRef")
    
*   [`PyDict_GetItemString()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemString "PyDict_GetItemString")
    
*   [`PyDict_GetItemStringRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemStringRef "PyDict_GetItemStringRef")
    
*   [`PyDict_GetItemWithError()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemWithError "PyDict_GetItemWithError")
    
*   [`PyDict_Items()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Items "PyDict_Items")
    
*   [`PyDict_Keys()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Keys "PyDict_Keys")
    
*   [`PyDict_Merge()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Merge "PyDict_Merge")
    
*   [`PyDict_MergeFromSeq2()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_MergeFromSeq2 "PyDict_MergeFromSeq2")
    
*   [`PyDict_New()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_New "PyDict_New")
    
*   [`PyDict_Next()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Next "PyDict_Next")
    
*   [`PyDict_SetDefaultRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetDefaultRef "PyDict_SetDefaultRef")
    
*   [`PyDict_SetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetItem "PyDict_SetItem")
    
*   [`PyDict_SetItemString()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetItemString "PyDict_SetItemString")
    
*   [`PyDict_Size()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Size "PyDict_Size")
    
*   [`PyDict_Type`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Type "PyDict_Type")
    
*   [`PyDict_Update()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Update "PyDict_Update")
    
*   [`PyDict_Values()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Values "PyDict_Values")
    
*   [`PyEllipsis_Type`](https://docs.python.org/3/c-api/slice.html#c.PyEllipsis_Type "PyEllipsis_Type")
    
*   [`PyEnum_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyEnum_Type "PyEnum_Type")
    
*   [`PyErr_BadArgument()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_BadArgument "PyErr_BadArgument")
    
*   [`PyErr_BadInternalCall()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_BadInternalCall "PyErr_BadInternalCall")
    
*   [`PyErr_CheckSignals()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_CheckSignals "PyErr_CheckSignals")
    
*   [`PyErr_Clear()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Clear "PyErr_Clear")
    
*   [`PyErr_Display()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Display "PyErr_Display")
    
*   [`PyErr_DisplayException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_DisplayException "PyErr_DisplayException")
    
*   [`PyErr_ExceptionMatches()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_ExceptionMatches "PyErr_ExceptionMatches")
    
*   [`PyErr_Fetch()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Fetch "PyErr_Fetch")
    
*   [`PyErr_Format()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Format "PyErr_Format")
    
*   [`PyErr_FormatV()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_FormatV "PyErr_FormatV")
    
*   [`PyErr_GetExcInfo()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetExcInfo "PyErr_GetExcInfo")
    
*   [`PyErr_GetHandledException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetHandledException "PyErr_GetHandledException")
    
*   [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
    
*   [`PyErr_GivenExceptionMatches()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GivenExceptionMatches "PyErr_GivenExceptionMatches")
    
*   [`PyErr_NewException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NewException "PyErr_NewException")
    
*   [`PyErr_NewExceptionWithDoc()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NewExceptionWithDoc "PyErr_NewExceptionWithDoc")
    
*   [`PyErr_NoMemory()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NoMemory "PyErr_NoMemory")
    
*   [`PyErr_NormalizeException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NormalizeException "PyErr_NormalizeException")
    
*   [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
    
*   [`PyErr_Print()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Print "PyErr_Print")
    
*   [`PyErr_PrintEx()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_PrintEx "PyErr_PrintEx")
    
*   [`PyErr_ProgramText()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_ProgramText "PyErr_ProgramText")
    
*   [`PyErr_ResourceWarning()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_ResourceWarning "PyErr_ResourceWarning")
    
*   [`PyErr_Restore()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Restore "PyErr_Restore")
    
*   [`PyErr_SetExcFromWindowsErr()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErr "PyErr_SetExcFromWindowsErr")
    
*   [`PyErr_SetExcFromWindowsErrWithFilename()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErrWithFilename "PyErr_SetExcFromWindowsErrWithFilename")
    
*   [`PyErr_SetExcFromWindowsErrWithFilenameObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErrWithFilenameObject "PyErr_SetExcFromWindowsErrWithFilenameObject")
    
*   [`PyErr_SetExcFromWindowsErrWithFilenameObjects()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcFromWindowsErrWithFilenameObjects "PyErr_SetExcFromWindowsErrWithFilenameObjects")
    
*   [`PyErr_SetExcInfo()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetExcInfo "PyErr_SetExcInfo")
    
*   [`PyErr_SetFromErrno()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrno "PyErr_SetFromErrno")
    
*   [`PyErr_SetFromErrnoWithFilename()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrnoWithFilename "PyErr_SetFromErrnoWithFilename")
    
*   [`PyErr_SetFromErrnoWithFilenameObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrnoWithFilenameObject "PyErr_SetFromErrnoWithFilenameObject")
    
*   [`PyErr_SetFromErrnoWithFilenameObjects()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromErrnoWithFilenameObjects "PyErr_SetFromErrnoWithFilenameObjects")
    
*   [`PyErr_SetFromWindowsErr()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromWindowsErr "PyErr_SetFromWindowsErr")
    
*   [`PyErr_SetFromWindowsErrWithFilename()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetFromWindowsErrWithFilename "PyErr_SetFromWindowsErrWithFilename")
    
*   [`PyErr_SetHandledException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetHandledException "PyErr_SetHandledException")
    
*   [`PyErr_SetImportError()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetImportError "PyErr_SetImportError")
    
*   [`PyErr_SetImportErrorSubclass()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetImportErrorSubclass "PyErr_SetImportErrorSubclass")
    
*   [`PyErr_SetInterrupt()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetInterrupt "PyErr_SetInterrupt")
    
*   [`PyErr_SetInterruptEx()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetInterruptEx "PyErr_SetInterruptEx")
    
*   [`PyErr_SetNone()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetNone "PyErr_SetNone")
    
*   [`PyErr_SetObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetObject "PyErr_SetObject")
    
*   [`PyErr_SetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetRaisedException "PyErr_SetRaisedException")
    
*   [`PyErr_SetString()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetString "PyErr_SetString")
    
*   [`PyErr_SyntaxLocation()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SyntaxLocation "PyErr_SyntaxLocation")
    
*   [`PyErr_SyntaxLocationEx()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SyntaxLocationEx "PyErr_SyntaxLocationEx")
    
*   [`PyErr_WarnEx()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnEx "PyErr_WarnEx")
    
*   [`PyErr_WarnExplicit()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnExplicit "PyErr_WarnExplicit")
    
*   [`PyErr_WarnFormat()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WarnFormat "PyErr_WarnFormat")
    
*   [`PyErr_WriteUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WriteUnraisable "PyErr_WriteUnraisable")
    
*   [`PyEval_AcquireThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_AcquireThread "PyEval_AcquireThread")
    
*   [`PyEval_EvalCode()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalCode "PyEval_EvalCode")
    
*   [`PyEval_EvalCodeEx()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalCodeEx "PyEval_EvalCodeEx")
    
*   [`PyEval_EvalFrame()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalFrame "PyEval_EvalFrame")
    
*   [`PyEval_EvalFrameEx()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalFrameEx "PyEval_EvalFrameEx")
    
*   [`PyEval_GetBuiltins()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetBuiltins "PyEval_GetBuiltins")
    
*   [`PyEval_GetFrame()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrame "PyEval_GetFrame")
    
*   [`PyEval_GetFrameBuiltins()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameBuiltins "PyEval_GetFrameBuiltins")
    
*   [`PyEval_GetFrameGlobals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameGlobals "PyEval_GetFrameGlobals")
    
*   [`PyEval_GetFrameLocals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameLocals "PyEval_GetFrameLocals")
    
*   [`PyEval_GetFuncDesc()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFuncDesc "PyEval_GetFuncDesc")
    
*   [`PyEval_GetFuncName()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFuncName "PyEval_GetFuncName")
    
*   [`PyEval_GetGlobals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetGlobals "PyEval_GetGlobals")
    
*   [`PyEval_GetLocals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetLocals "PyEval_GetLocals")
    
*   [`PyEval_InitThreads()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_InitThreads "PyEval_InitThreads")
    
*   [`PyEval_ReleaseThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_ReleaseThread "PyEval_ReleaseThread")
    
*   [`PyEval_RestoreThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_RestoreThread "PyEval_RestoreThread")
    
*   [`PyEval_SaveThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_SaveThread "PyEval_SaveThread")
    
*   [`PyExc_ArithmeticError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ArithmeticError "PyExc_ArithmeticError")
    
*   [`PyExc_AssertionError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_AssertionError "PyExc_AssertionError")
    
*   [`PyExc_AttributeError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_AttributeError "PyExc_AttributeError")
    
*   [`PyExc_BaseException`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BaseException "PyExc_BaseException")
    
*   [`PyExc_BaseExceptionGroup`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BaseExceptionGroup "PyExc_BaseExceptionGroup")
    
*   [`PyExc_BlockingIOError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BlockingIOError "PyExc_BlockingIOError")
    
*   [`PyExc_BrokenPipeError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BrokenPipeError "PyExc_BrokenPipeError")
    
*   [`PyExc_BufferError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BufferError "PyExc_BufferError")
    
*   [`PyExc_BytesWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_BytesWarning "PyExc_BytesWarning")
    
*   [`PyExc_ChildProcessError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ChildProcessError "PyExc_ChildProcessError")
    
*   [`PyExc_ConnectionAbortedError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionAbortedError "PyExc_ConnectionAbortedError")
    
*   [`PyExc_ConnectionError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionError "PyExc_ConnectionError")
    
*   [`PyExc_ConnectionRefusedError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionRefusedError "PyExc_ConnectionRefusedError")
    
*   [`PyExc_ConnectionResetError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ConnectionResetError "PyExc_ConnectionResetError")
    
*   [`PyExc_DeprecationWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_DeprecationWarning "PyExc_DeprecationWarning")
    
*   [`PyExc_EOFError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_EOFError "PyExc_EOFError")
    
*   [`PyExc_EncodingWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_EncodingWarning "PyExc_EncodingWarning")
    
*   [`PyExc_EnvironmentError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_EnvironmentError "PyExc_EnvironmentError")
    
*   [`PyExc_Exception`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_Exception "PyExc_Exception")
    
*   [`PyExc_FileExistsError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_FileExistsError "PyExc_FileExistsError")
    
*   [`PyExc_FileNotFoundError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_FileNotFoundError "PyExc_FileNotFoundError")
    
*   [`PyExc_FloatingPointError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_FloatingPointError "PyExc_FloatingPointError")
    
*   [`PyExc_FutureWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_FutureWarning "PyExc_FutureWarning")
    
*   [`PyExc_GeneratorExit`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_GeneratorExit "PyExc_GeneratorExit")
    
*   [`PyExc_IOError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_IOError "PyExc_IOError")
    
*   [`PyExc_ImportError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ImportError "PyExc_ImportError")
    
*   [`PyExc_ImportWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ImportWarning "PyExc_ImportWarning")
    
*   [`PyExc_IndentationError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_IndentationError "PyExc_IndentationError")
    
*   [`PyExc_IndexError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_IndexError "PyExc_IndexError")
    
*   [`PyExc_InterruptedError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_InterruptedError "PyExc_InterruptedError")
    
*   [`PyExc_IsADirectoryError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_IsADirectoryError "PyExc_IsADirectoryError")
    
*   [`PyExc_KeyError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_KeyError "PyExc_KeyError")
    
*   [`PyExc_KeyboardInterrupt`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_KeyboardInterrupt "PyExc_KeyboardInterrupt")
    
*   [`PyExc_LookupError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_LookupError "PyExc_LookupError")
    
*   [`PyExc_MemoryError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_MemoryError "PyExc_MemoryError")
    
*   [`PyExc_ModuleNotFoundError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ModuleNotFoundError "PyExc_ModuleNotFoundError")
    
*   [`PyExc_NameError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_NameError "PyExc_NameError")
    
*   [`PyExc_NotADirectoryError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_NotADirectoryError "PyExc_NotADirectoryError")
    
*   [`PyExc_NotImplementedError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_NotImplementedError "PyExc_NotImplementedError")
    
*   [`PyExc_OSError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_OSError "PyExc_OSError")
    
*   [`PyExc_OverflowError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_OverflowError "PyExc_OverflowError")
    
*   [`PyExc_PendingDeprecationWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_PendingDeprecationWarning "PyExc_PendingDeprecationWarning")
    
*   [`PyExc_PermissionError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_PermissionError "PyExc_PermissionError")
    
*   [`PyExc_ProcessLookupError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ProcessLookupError "PyExc_ProcessLookupError")
    
*   [`PyExc_RecursionError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_RecursionError "PyExc_RecursionError")
    
*   [`PyExc_ReferenceError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ReferenceError "PyExc_ReferenceError")
    
*   [`PyExc_ResourceWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ResourceWarning "PyExc_ResourceWarning")
    
*   [`PyExc_RuntimeError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_RuntimeError "PyExc_RuntimeError")
    
*   [`PyExc_RuntimeWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_RuntimeWarning "PyExc_RuntimeWarning")
    
*   [`PyExc_StopAsyncIteration`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_StopAsyncIteration "PyExc_StopAsyncIteration")
    
*   [`PyExc_StopIteration`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_StopIteration "PyExc_StopIteration")
    
*   [`PyExc_SyntaxError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_SyntaxError "PyExc_SyntaxError")
    
*   [`PyExc_SyntaxWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_SyntaxWarning "PyExc_SyntaxWarning")
    
*   [`PyExc_SystemError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_SystemError "PyExc_SystemError")
    
*   [`PyExc_SystemExit`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_SystemExit "PyExc_SystemExit")
    
*   [`PyExc_TabError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_TabError "PyExc_TabError")
    
*   [`PyExc_TimeoutError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_TimeoutError "PyExc_TimeoutError")
    
*   [`PyExc_TypeError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_TypeError "PyExc_TypeError")
    
*   [`PyExc_UnboundLocalError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnboundLocalError "PyExc_UnboundLocalError")
    
*   [`PyExc_UnicodeDecodeError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnicodeDecodeError "PyExc_UnicodeDecodeError")
    
*   [`PyExc_UnicodeEncodeError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnicodeEncodeError "PyExc_UnicodeEncodeError")
    
*   [`PyExc_UnicodeError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnicodeError "PyExc_UnicodeError")
    
*   [`PyExc_UnicodeTranslateError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnicodeTranslateError "PyExc_UnicodeTranslateError")
    
*   [`PyExc_UnicodeWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UnicodeWarning "PyExc_UnicodeWarning")
    
*   [`PyExc_UserWarning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_UserWarning "PyExc_UserWarning")
    
*   [`PyExc_ValueError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ValueError "PyExc_ValueError")
    
*   [`PyExc_Warning`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_Warning "PyExc_Warning")
    
*   [`PyExc_WindowsError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_WindowsError "PyExc_WindowsError")
    
*   [`PyExc_ZeroDivisionError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_ZeroDivisionError "PyExc_ZeroDivisionError")
    
*   [`PyExceptionClass_Name()`](https://docs.python.org/3/c-api/exceptions.html#c.PyExceptionClass_Name "PyExceptionClass_Name")
    
*   [`PyException_GetArgs()`](https://docs.python.org/3/c-api/exceptions.html#c.PyException_GetArgs "PyException_GetArgs")
    
*   [`PyException_GetCause()`](https://docs.python.org/3/c-api/exceptions.html#c.PyException_GetCause "PyException_GetCause")
    
*   [`PyException_GetContext()`](https://docs.python.org/3/c-api/exceptions.html#c.PyException_GetContext "PyException_GetContext")
    
*   [`PyException_GetTraceback()`](https://docs.python.org/3/c-api/exceptions.html#c.PyException_GetTraceback "PyException_GetTraceback")
    
*   [`PyException_SetArgs()`](https://docs.python.org/3/c-api/exceptions.html#c.PyException_SetArgs "PyException_SetArgs")
    
*   [`PyException_SetCause()`](https://docs.python.org/3/c-api/exceptions.html#c.PyException_SetCause "PyException_SetCause")
    
*   [`PyException_SetContext()`](https://docs.python.org/3/c-api/exceptions.html#c.PyException_SetContext "PyException_SetContext")
    
*   [`PyException_SetTraceback()`](https://docs.python.org/3/c-api/exceptions.html#c.PyException_SetTraceback "PyException_SetTraceback")
    
*   [`PyFile_FromFd()`](https://docs.python.org/3/c-api/file.html#c.PyFile_FromFd "PyFile_FromFd")
    
*   [`PyFile_GetLine()`](https://docs.python.org/3/c-api/file.html#c.PyFile_GetLine "PyFile_GetLine")
    
*   [`PyFile_WriteObject()`](https://docs.python.org/3/c-api/file.html#c.PyFile_WriteObject "PyFile_WriteObject")
    
*   [`PyFile_WriteString()`](https://docs.python.org/3/c-api/file.html#c.PyFile_WriteString "PyFile_WriteString")
    
*   [`PyFilter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyFilter_Type "PyFilter_Type")
    
*   [`PyFloat_AsDouble()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_AsDouble "PyFloat_AsDouble")
    
*   [`PyFloat_FromDouble()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_FromDouble "PyFloat_FromDouble")
    
*   [`PyFloat_FromString()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_FromString "PyFloat_FromString")
    
*   [`PyFloat_GetInfo()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_GetInfo "PyFloat_GetInfo")
    
*   [`PyFloat_GetMax()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_GetMax "PyFloat_GetMax")
    
*   [`PyFloat_GetMin()`](https://docs.python.org/3/c-api/float.html#c.PyFloat_GetMin "PyFloat_GetMin")
    
*   [`PyFloat_Type`](https://docs.python.org/3/c-api/float.html#c.PyFloat_Type "PyFloat_Type")
    
*   [`PyFrameObject`](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
    
*   [`PyFrame_GetCode()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetCode "PyFrame_GetCode")
    
*   [`PyFrame_GetLineNumber()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLineNumber "PyFrame_GetLineNumber")
    
*   [`PyFrozenSet_New()`](https://docs.python.org/3/c-api/set.html#c.PyFrozenSet_New "PyFrozenSet_New")
    
*   [`PyFrozenSet_Type`](https://docs.python.org/3/c-api/set.html#c.PyFrozenSet_Type "PyFrozenSet_Type")
    
*   [`PyGC_Collect()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_Collect "PyGC_Collect")
    
*   [`PyGC_Disable()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_Disable "PyGC_Disable")
    
*   [`PyGC_Enable()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_Enable "PyGC_Enable")
    
*   [`PyGC_IsEnabled()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_IsEnabled "PyGC_IsEnabled")
    
*   [`PyGILState_Ensure()`](https://docs.python.org/3/c-api/threads.html#c.PyGILState_Ensure "PyGILState_Ensure")
    
*   [`PyGILState_GetThisThreadState()`](https://docs.python.org/3/c-api/threads.html#c.PyGILState_GetThisThreadState "PyGILState_GetThisThreadState")
    
*   [`PyGILState_Release()`](https://docs.python.org/3/c-api/threads.html#c.PyGILState_Release "PyGILState_Release")
    
*   [`PyGILState_STATE`](https://docs.python.org/3/c-api/threads.html#c.PyGILState_STATE "PyGILState_STATE")
    
*   [`PyGetSetDef`](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")
    
*   [`PyGetSetDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyGetSetDescr_Type "PyGetSetDescr_Type")
    
*   [`PyImport_AddModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModule "PyImport_AddModule")
    
*   [`PyImport_AddModuleObject()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModuleObject "PyImport_AddModuleObject")
    
*   [`PyImport_AddModuleRef()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModuleRef "PyImport_AddModuleRef")
    
*   [`PyImport_AppendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AppendInittab "PyImport_AppendInittab")
    
*   [`PyImport_ExecCodeModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModule "PyImport_ExecCodeModule")
    
*   [`PyImport_ExecCodeModuleEx()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleEx "PyImport_ExecCodeModuleEx")
    
*   [`PyImport_ExecCodeModuleObject()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleObject "PyImport_ExecCodeModuleObject")
    
*   [`PyImport_ExecCodeModuleWithPathnames()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleWithPathnames "PyImport_ExecCodeModuleWithPathnames")
    
*   [`PyImport_GetImporter()`](https://docs.python.org/3/c-api/import.html#c.PyImport_GetImporter "PyImport_GetImporter")
    
*   [`PyImport_GetMagicNumber()`](https://docs.python.org/3/c-api/import.html#c.PyImport_GetMagicNumber "PyImport_GetMagicNumber")
    
*   [`PyImport_GetMagicTag()`](https://docs.python.org/3/c-api/import.html#c.PyImport_GetMagicTag "PyImport_GetMagicTag")
    
*   [`PyImport_GetModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_GetModule "PyImport_GetModule")
    
*   [`PyImport_GetModuleDict()`](https://docs.python.org/3/c-api/import.html#c.PyImport_GetModuleDict "PyImport_GetModuleDict")
    
*   [`PyImport_Import()`](https://docs.python.org/3/c-api/import.html#c.PyImport_Import "PyImport_Import")
    
*   [`PyImport_ImportFrozenModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportFrozenModule "PyImport_ImportFrozenModule")
    
*   [`PyImport_ImportFrozenModuleObject()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportFrozenModuleObject "PyImport_ImportFrozenModuleObject")
    
*   [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
    
*   [`PyImport_ImportModuleLevel()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleLevel "PyImport_ImportModuleLevel")
    
*   [`PyImport_ImportModuleLevelObject()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleLevelObject "PyImport_ImportModuleLevelObject")
    
*   [`PyImport_ReloadModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ReloadModule "PyImport_ReloadModule")
    
*   [`PyIndex_Check()`](https://docs.python.org/3/c-api/number.html#c.PyIndex_Check "PyIndex_Check")
    
*   [`PyInterpreterGuard`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PyInterpreterGuard "PyInterpreterGuard")
    
*   [`PyInterpreterGuard_Close()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PyInterpreterGuard_Close "PyInterpreterGuard_Close")
    
*   [`PyInterpreterGuard_FromCurrent()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PyInterpreterGuard_FromCurrent "PyInterpreterGuard_FromCurrent")
    
*   [`PyInterpreterGuard_FromView()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PyInterpreterGuard_FromView "PyInterpreterGuard_FromView")
    
*   [`PyInterpreterState`](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState "PyInterpreterState")
    
*   [`PyInterpreterState_Clear()`](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState_Clear "PyInterpreterState_Clear")
    
*   [`PyInterpreterState_Delete()`](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState_Delete "PyInterpreterState_Delete")
    
*   [`PyInterpreterState_Get()`](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState_Get "PyInterpreterState_Get")
    
*   [`PyInterpreterState_GetDict()`](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState_GetDict "PyInterpreterState_GetDict")
    
*   [`PyInterpreterState_GetID()`](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState_GetID "PyInterpreterState_GetID")
    
*   [`PyInterpreterState_New()`](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterState_New "PyInterpreterState_New")
    
*   [`PyInterpreterView`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PyInterpreterView "PyInterpreterView")
    
*   [`PyInterpreterView_Close()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PyInterpreterView_Close "PyInterpreterView_Close")
    
*   [`PyInterpreterView_FromCurrent()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PyInterpreterView_FromCurrent "PyInterpreterView_FromCurrent")
    
*   [`PyInterpreterView_FromMain()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PyInterpreterView_FromMain "PyInterpreterView_FromMain")
    
*   [`PyIter_Check()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_Check "PyIter_Check")
    
*   [`PyIter_Next()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_Next "PyIter_Next")
    
*   [`PyIter_NextItem()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_NextItem "PyIter_NextItem")
    
*   [`PyIter_Send()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_Send "PyIter_Send")
    
*   [`PyListIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyListIter_Type "PyListIter_Type")
    
*   [`PyListRevIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyListRevIter_Type "PyListRevIter_Type")
    
*   [`PyList_Append()`](https://docs.python.org/3/c-api/list.html#c.PyList_Append "PyList_Append")
    
*   [`PyList_AsTuple()`](https://docs.python.org/3/c-api/list.html#c.PyList_AsTuple "PyList_AsTuple")
    
*   [`PyList_GetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem "PyList_GetItem")
    
*   [`PyList_GetItemRef()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItemRef "PyList_GetItemRef")
    
*   [`PyList_GetSlice()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetSlice "PyList_GetSlice")
    
*   [`PyList_Insert()`](https://docs.python.org/3/c-api/list.html#c.PyList_Insert "PyList_Insert")
    
*   [`PyList_New()`](https://docs.python.org/3/c-api/list.html#c.PyList_New "PyList_New")
    
*   [`PyList_Reverse()`](https://docs.python.org/3/c-api/list.html#c.PyList_Reverse "PyList_Reverse")
    
*   [`PyList_SetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_SetItem "PyList_SetItem")
    
*   [`PyList_SetSlice()`](https://docs.python.org/3/c-api/list.html#c.PyList_SetSlice "PyList_SetSlice")
    
*   [`PyList_Size()`](https://docs.python.org/3/c-api/list.html#c.PyList_Size "PyList_Size")
    
*   [`PyList_Sort()`](https://docs.python.org/3/c-api/list.html#c.PyList_Sort "PyList_Sort")
    
*   [`PyList_Type`](https://docs.python.org/3/c-api/list.html#c.PyList_Type "PyList_Type")
    
*   [`PyLongExport`](https://docs.python.org/3/c-api/long.html#c.PyLongExport "PyLongExport")
    
*   [`PyLongLayout`](https://docs.python.org/3/c-api/long.html#c.PyLongLayout "PyLongLayout")
    
*   [`PyLongObject`](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
    
*   [`PyLongRangeIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyLongRangeIter_Type "PyLongRangeIter_Type")
    
*   [`PyLongWriter`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter "PyLongWriter")
    
*   [`PyLongWriter_Create()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Create "PyLongWriter_Create")
    
*   [`PyLongWriter_Discard()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Discard "PyLongWriter_Discard")
    
*   [`PyLongWriter_Finish()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Finish "PyLongWriter_Finish")
    
*   [`PyLong_AsDouble()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsDouble "PyLong_AsDouble")
    
*   [`PyLong_AsInt()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsInt "PyLong_AsInt")
    
*   [`PyLong_AsInt32()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsInt32 "PyLong_AsInt32")
    
*   [`PyLong_AsInt64()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsInt64 "PyLong_AsInt64")
    
*   [`PyLong_AsLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLong "PyLong_AsLong")
    
*   [`PyLong_AsLongAndOverflow()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLongAndOverflow "PyLong_AsLongAndOverflow")
    
*   [`PyLong_AsLongLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLongLong "PyLong_AsLongLong")
    
*   [`PyLong_AsLongLongAndOverflow()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsLongLongAndOverflow "PyLong_AsLongLongAndOverflow")
    
*   [`PyLong_AsNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsNativeBytes "PyLong_AsNativeBytes")
    
*   [`PyLong_AsSize_t()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsSize_t "PyLong_AsSize_t")
    
*   [`PyLong_AsSsize_t()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsSsize_t "PyLong_AsSsize_t")
    
*   [`PyLong_AsUInt32()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUInt32 "PyLong_AsUInt32")
    
*   [`PyLong_AsUInt64()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUInt64 "PyLong_AsUInt64")
    
*   [`PyLong_AsUnsignedLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUnsignedLong "PyLong_AsUnsignedLong")
    
*   [`PyLong_AsUnsignedLongLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUnsignedLongLong "PyLong_AsUnsignedLongLong")
    
*   [`PyLong_AsUnsignedLongLongMask()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUnsignedLongLongMask "PyLong_AsUnsignedLongLongMask")
    
*   [`PyLong_AsUnsignedLongMask()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsUnsignedLongMask "PyLong_AsUnsignedLongMask")
    
*   [`PyLong_AsVoidPtr()`](https://docs.python.org/3/c-api/long.html#c.PyLong_AsVoidPtr "PyLong_AsVoidPtr")
    
*   [`PyLong_Export()`](https://docs.python.org/3/c-api/long.html#c.PyLong_Export "PyLong_Export")
    
*   [`PyLong_FreeExport()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FreeExport "PyLong_FreeExport")
    
*   [`PyLong_FromDouble()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromDouble "PyLong_FromDouble")
    
*   [`PyLong_FromInt32()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromInt32 "PyLong_FromInt32")
    
*   [`PyLong_FromInt64()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromInt64 "PyLong_FromInt64")
    
*   [`PyLong_FromLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong "PyLong_FromLong")
    
*   [`PyLong_FromLongLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLongLong "PyLong_FromLongLong")
    
*   [`PyLong_FromNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromNativeBytes "PyLong_FromNativeBytes")
    
*   [`PyLong_FromSize_t()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromSize_t "PyLong_FromSize_t")
    
*   [`PyLong_FromSsize_t()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromSsize_t "PyLong_FromSsize_t")
    
*   [`PyLong_FromString()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromString "PyLong_FromString")
    
*   [`PyLong_FromUInt32()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUInt32 "PyLong_FromUInt32")
    
*   [`PyLong_FromUInt64()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUInt64 "PyLong_FromUInt64")
    
*   [`PyLong_FromUnsignedLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUnsignedLong "PyLong_FromUnsignedLong")
    
*   [`PyLong_FromUnsignedLongLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUnsignedLongLong "PyLong_FromUnsignedLongLong")
    
*   [`PyLong_FromUnsignedNativeBytes()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUnsignedNativeBytes "PyLong_FromUnsignedNativeBytes")
    
*   [`PyLong_FromVoidPtr()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromVoidPtr "PyLong_FromVoidPtr")
    
*   [`PyLong_GetInfo()`](https://docs.python.org/3/c-api/long.html#c.PyLong_GetInfo "PyLong_GetInfo")
    
*   [`PyLong_GetNativeLayout()`](https://docs.python.org/3/c-api/long.html#c.PyLong_GetNativeLayout "PyLong_GetNativeLayout")
    
*   [`PyLong_Type`](https://docs.python.org/3/c-api/long.html#c.PyLong_Type "PyLong_Type")
    
*   [`PyMODEXPORT_FUNC`](https://docs.python.org/3/c-api/extension-modules.html#c.PyMODEXPORT_FUNC "PyMODEXPORT_FUNC")
    
*   [`PyMap_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyMap_Type "PyMap_Type")
    
*   [`PyMapping_Check()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Check "PyMapping_Check")
    
*   [`PyMapping_GetItemString()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetItemString "PyMapping_GetItemString")
    
*   [`PyMapping_GetOptionalItem()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetOptionalItem "PyMapping_GetOptionalItem")
    
*   [`PyMapping_GetOptionalItemString()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetOptionalItemString "PyMapping_GetOptionalItemString")
    
*   [`PyMapping_HasKey()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKey "PyMapping_HasKey")
    
*   [`PyMapping_HasKeyString()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyString "PyMapping_HasKeyString")
    
*   [`PyMapping_HasKeyStringWithError()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyStringWithError "PyMapping_HasKeyStringWithError")
    
*   [`PyMapping_HasKeyWithError()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyWithError "PyMapping_HasKeyWithError")
    
*   [`PyMapping_Items()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Items "PyMapping_Items")
    
*   [`PyMapping_Keys()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Keys "PyMapping_Keys")
    
*   [`PyMapping_Length()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Length "PyMapping_Length")
    
*   [`PyMapping_SetItemString()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_SetItemString "PyMapping_SetItemString")
    
*   [`PyMapping_Size()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Size "PyMapping_Size")
    
*   [`PyMapping_Values()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Values "PyMapping_Values")
    
*   [`PyMem_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Calloc "PyMem_Calloc")
    
*   [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
    
*   [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
    
*   [`PyMem_RawCalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawCalloc "PyMem_RawCalloc")
    
*   [`PyMem_RawFree()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawFree "PyMem_RawFree")
    
*   [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
    
*   [`PyMem_RawRealloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
    
*   [`PyMem_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "PyMem_Realloc")
    
*   [`PyMemberDef`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")
    
*   [`PyMemberDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyMemberDescr_Type "PyMemberDescr_Type")
    
*   [`PyMember_GetOne()`](https://docs.python.org/3/c-api/structures.html#c.PyMember_GetOne "PyMember_GetOne")
    
*   [`PyMember_SetOne()`](https://docs.python.org/3/c-api/structures.html#c.PyMember_SetOne "PyMember_SetOne")
    
*   [`PyMemoryView_FromBuffer()`](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromBuffer "PyMemoryView_FromBuffer")
    
*   [`PyMemoryView_FromMemory()`](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromMemory "PyMemoryView_FromMemory")
    
*   [`PyMemoryView_FromObject()`](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromObject "PyMemoryView_FromObject")
    
*   [`PyMemoryView_GetContiguous()`](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_GetContiguous "PyMemoryView_GetContiguous")
    
*   [`PyMemoryView_Type`](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_Type "PyMemoryView_Type")
    
*   [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
    
*   [`PyMethodDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyMethodDescr_Type "PyMethodDescr_Type")
    
*   [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
    
*   [`PyModuleDef_Base`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Base "PyModuleDef_Base")
    
*   [`PyModuleDef_Init()`](https://docs.python.org/3/c-api/extension-modules.html#c.PyModuleDef_Init "PyModuleDef_Init")
    
*   [`PyModuleDef_Slot`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot "PyModuleDef_Slot")
    
*   [`PyModuleDef_Type`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Type "PyModuleDef_Type")
    
*   [`PyModule_Add()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Add "PyModule_Add")
    
*   [`PyModule_AddFunctions()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddFunctions "PyModule_AddFunctions")
    
*   [`PyModule_AddIntConstant()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddIntConstant "PyModule_AddIntConstant")
    
*   [`PyModule_AddObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObject "PyModule_AddObject")
    
*   [`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef")
    
*   [`PyModule_AddStringConstant()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddStringConstant "PyModule_AddStringConstant")
    
*   [`PyModule_AddType()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddType "PyModule_AddType")
    
*   [`PyModule_Create2()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Create2 "PyModule_Create2")
    
*   [`PyModule_Exec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Exec "PyModule_Exec")
    
*   [`PyModule_ExecDef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_ExecDef "PyModule_ExecDef")
    
*   [`PyModule_FromDefAndSpec2()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromDefAndSpec2 "PyModule_FromDefAndSpec2")
    
*   [`PyModule_FromSlotsAndSpec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromSlotsAndSpec "PyModule_FromSlotsAndSpec")
    
*   [`PyModule_GetDef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetDef "PyModule_GetDef")
    
*   [`PyModule_GetDict()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetDict "PyModule_GetDict")
    
*   [`PyModule_GetFilename()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilename "PyModule_GetFilename")
    
*   [`PyModule_GetFilenameObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilenameObject "PyModule_GetFilenameObject")
    
*   [`PyModule_GetName()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetName "PyModule_GetName")
    
*   [`PyModule_GetNameObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetNameObject "PyModule_GetNameObject")
    
*   [`PyModule_GetState()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "PyModule_GetState")
    
*   [`PyModule_GetStateSize()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetStateSize "PyModule_GetStateSize")
    
*   [`PyModule_GetState_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyModule_GetState_DuringGC "PyModule_GetState_DuringGC")
    
*   [`PyModule_GetToken()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetToken "PyModule_GetToken")
    
*   [`PyModule_GetToken_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyModule_GetToken_DuringGC "PyModule_GetToken_DuringGC")
    
*   [`PyModule_New()`](https://docs.python.org/3/c-api/module.html#c.PyModule_New "PyModule_New")
    
*   [`PyModule_NewObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_NewObject "PyModule_NewObject")
    
*   [`PyModule_SetDocString()`](https://docs.python.org/3/c-api/module.html#c.PyModule_SetDocString "PyModule_SetDocString")
    
*   [`PyModule_Type`](https://docs.python.org/3/c-api/module.html#c.PyModule_Type "PyModule_Type")
    
*   [`PyNumber_Absolute()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Absolute "PyNumber_Absolute")
    
*   [`PyNumber_Add()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Add "PyNumber_Add")
    
*   [`PyNumber_And()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_And "PyNumber_And")
    
*   [`PyNumber_AsSsize_t()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_AsSsize_t "PyNumber_AsSsize_t")
    
*   [`PyNumber_Check()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Check "PyNumber_Check")
    
*   [`PyNumber_Divmod()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Divmod "PyNumber_Divmod")
    
*   [`PyNumber_Float()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Float "PyNumber_Float")
    
*   [`PyNumber_FloorDivide()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_FloorDivide "PyNumber_FloorDivide")
    
*   [`PyNumber_InPlaceAdd()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceAdd "PyNumber_InPlaceAdd")
    
*   [`PyNumber_InPlaceAnd()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceAnd "PyNumber_InPlaceAnd")
    
*   [`PyNumber_InPlaceFloorDivide()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceFloorDivide "PyNumber_InPlaceFloorDivide")
    
*   [`PyNumber_InPlaceLshift()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceLshift "PyNumber_InPlaceLshift")
    
*   [`PyNumber_InPlaceMatrixMultiply()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceMatrixMultiply "PyNumber_InPlaceMatrixMultiply")
    
*   [`PyNumber_InPlaceMultiply()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceMultiply "PyNumber_InPlaceMultiply")
    
*   [`PyNumber_InPlaceOr()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceOr "PyNumber_InPlaceOr")
    
*   [`PyNumber_InPlacePower()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlacePower "PyNumber_InPlacePower")
    
*   [`PyNumber_InPlaceRemainder()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceRemainder "PyNumber_InPlaceRemainder")
    
*   [`PyNumber_InPlaceRshift()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceRshift "PyNumber_InPlaceRshift")
    
*   [`PyNumber_InPlaceSubtract()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceSubtract "PyNumber_InPlaceSubtract")
    
*   [`PyNumber_InPlaceTrueDivide()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceTrueDivide "PyNumber_InPlaceTrueDivide")
    
*   [`PyNumber_InPlaceXor()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceXor "PyNumber_InPlaceXor")
    
*   [`PyNumber_Index()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Index "PyNumber_Index")
    
*   [`PyNumber_Invert()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Invert "PyNumber_Invert")
    
*   [`PyNumber_Long()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Long "PyNumber_Long")
    
*   [`PyNumber_Lshift()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Lshift "PyNumber_Lshift")
    
*   [`PyNumber_MatrixMultiply()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_MatrixMultiply "PyNumber_MatrixMultiply")
    
*   [`PyNumber_Multiply()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Multiply "PyNumber_Multiply")
    
*   [`PyNumber_Negative()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Negative "PyNumber_Negative")
    
*   [`PyNumber_Or()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Or "PyNumber_Or")
    
*   [`PyNumber_Positive()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Positive "PyNumber_Positive")
    
*   [`PyNumber_Power()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Power "PyNumber_Power")
    
*   [`PyNumber_Remainder()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Remainder "PyNumber_Remainder")
    
*   [`PyNumber_Rshift()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Rshift "PyNumber_Rshift")
    
*   [`PyNumber_Subtract()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Subtract "PyNumber_Subtract")
    
*   [`PyNumber_ToBase()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_ToBase "PyNumber_ToBase")
    
*   [`PyNumber_TrueDivide()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_TrueDivide "PyNumber_TrueDivide")
    
*   [`PyNumber_Xor()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Xor "PyNumber_Xor")
    
*   [`PyOS_AfterFork()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork "PyOS_AfterFork")
    
*   [`PyOS_AfterFork_Child()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Child "PyOS_AfterFork_Child")
    
*   [`PyOS_AfterFork_Parent()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Parent "PyOS_AfterFork_Parent")
    
*   [`PyOS_BeforeFork()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_BeforeFork "PyOS_BeforeFork")
    
*   [`PyOS_CheckStack()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_CheckStack "PyOS_CheckStack")
    
*   [`PyOS_FSPath()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_FSPath "PyOS_FSPath")
    
*   [`PyOS_InputHook`](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_InputHook "PyOS_InputHook")
    
*   [`PyOS_InterruptOccurred()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_InterruptOccurred "PyOS_InterruptOccurred")
    
*   [`PyOS_double_to_string()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_double_to_string "PyOS_double_to_string")
    
*   [`PyOS_getsig()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_getsig "PyOS_getsig")
    
*   [`PyOS_mystricmp()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_mystricmp "PyOS_mystricmp")
    
*   [`PyOS_mystrnicmp()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_mystrnicmp "PyOS_mystrnicmp")
    
*   [`PyOS_setsig()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_setsig "PyOS_setsig")
    
*   [`PyOS_sighandler_t`](https://docs.python.org/3/c-api/sys.html#c.PyOS_sighandler_t "PyOS_sighandler_t")
    
*   [`PyOS_snprintf()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_snprintf "PyOS_snprintf")
    
*   [`PyOS_string_to_double()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_string_to_double "PyOS_string_to_double")
    
*   [`PyOS_strtol()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_strtol "PyOS_strtol")
    
*   [`PyOS_strtoul()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_strtoul "PyOS_strtoul")
    
*   [`PyOS_vsnprintf()`](https://docs.python.org/3/c-api/conversion.html#c.PyOS_vsnprintf "PyOS_vsnprintf")
    
*   [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
    
*   [`PyObject.ob_refcnt`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_refcnt "PyObject.ob_refcnt")
    
*   [`PyObject.ob_type`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_type "PyObject.ob_type")
    
*   [`PyObject_ASCII()`](https://docs.python.org/3/c-api/object.html#c.PyObject_ASCII "PyObject_ASCII")
    
*   [`PyObject_AsFileDescriptor()`](https://docs.python.org/3/c-api/file.html#c.PyObject_AsFileDescriptor "PyObject_AsFileDescriptor")
    
*   [`PyObject_Bytes()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Bytes "PyObject_Bytes")
    
*   [`PyObject_Call()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Call "PyObject_Call")
    
*   [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")
    
*   [`PyObject_CallFunction()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallFunction "PyObject_CallFunction")
    
*   [`PyObject_CallFunctionObjArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallFunctionObjArgs "PyObject_CallFunctionObjArgs")
    
*   [`PyObject_CallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethod "PyObject_CallMethod")
    
*   [`PyObject_CallMethodObjArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethodObjArgs "PyObject_CallMethodObjArgs")
    
*   [`PyObject_CallNoArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallNoArgs "PyObject_CallNoArgs")
    
*   [`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject "PyObject_CallObject")
    
*   [`PyObject_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Calloc "PyObject_Calloc")
    
*   [`PyObject_CheckBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_CheckBuffer "PyObject_CheckBuffer")
    
*   [`PyObject_ClearWeakRefs()`](https://docs.python.org/3/c-api/weakref.html#c.PyObject_ClearWeakRefs "PyObject_ClearWeakRefs")
    
*   [`PyObject_CopyData()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_CopyData "PyObject_CopyData")
    
*   [`PyObject_DelAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelAttr "PyObject_DelAttr")
    
*   [`PyObject_DelAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelAttrString "PyObject_DelAttrString")
    
*   [`PyObject_DelItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelItem "PyObject_DelItem")
    
*   [`PyObject_DelItemString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelItemString "PyObject_DelItemString")
    
*   [`PyObject_Dir()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Dir "PyObject_Dir")
    
*   [`PyObject_Format()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Format "PyObject_Format")
    
*   [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
    
*   [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
    
*   [`PyObject_GC_IsFinalized()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_IsFinalized "PyObject_GC_IsFinalized")
    
*   [`PyObject_GC_IsTracked()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_IsTracked "PyObject_GC_IsTracked")
    
*   [`PyObject_GC_Track()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Track "PyObject_GC_Track")
    
*   [`PyObject_GC_UnTrack()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_UnTrack "PyObject_GC_UnTrack")
    
*   [`PyObject_GenericGetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericGetAttr "PyObject_GenericGetAttr")
    
*   [`PyObject_GenericGetDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericGetDict "PyObject_GenericGetDict")
    
*   [`PyObject_GenericSetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericSetAttr "PyObject_GenericSetAttr")
    
*   [`PyObject_GenericSetDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GenericSetDict "PyObject_GenericSetDict")
    
*   [`PyObject_GetAIter()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAIter "PyObject_GetAIter")
    
*   [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
    
*   [`PyObject_GetAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttrString "PyObject_GetAttrString")
    
*   [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
    
*   [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
    
*   [`PyObject_GetIter()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetIter "PyObject_GetIter")
    
*   [`PyObject_GetOptionalAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttr "PyObject_GetOptionalAttr")
    
*   [`PyObject_GetOptionalAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetOptionalAttrString "PyObject_GetOptionalAttrString")
    
*   [`PyObject_GetTypeData()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetTypeData "PyObject_GetTypeData")
    
*   [`PyObject_GetTypeData_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GetTypeData_DuringGC "PyObject_GetTypeData_DuringGC")
    
*   [`PyObject_HasAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttr "PyObject_HasAttr")
    
*   [`PyObject_HasAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrString "PyObject_HasAttrString")
    
*   [`PyObject_HasAttrStringWithError()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrStringWithError "PyObject_HasAttrStringWithError")
    
*   [`PyObject_HasAttrWithError()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HasAttrWithError "PyObject_HasAttrWithError")
    
*   [`PyObject_Hash()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Hash "PyObject_Hash")
    
*   [`PyObject_HashNotImplemented()`](https://docs.python.org/3/c-api/object.html#c.PyObject_HashNotImplemented "PyObject_HashNotImplemented")
    
*   [`PyObject_Init()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_Init "PyObject_Init")
    
*   [`PyObject_InitVar()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_InitVar "PyObject_InitVar")
    
*   [`PyObject_IsInstance()`](https://docs.python.org/3/c-api/object.html#c.PyObject_IsInstance "PyObject_IsInstance")
    
*   [`PyObject_IsSubclass()`](https://docs.python.org/3/c-api/object.html#c.PyObject_IsSubclass "PyObject_IsSubclass")
    
*   [`PyObject_IsTrue()`](https://docs.python.org/3/c-api/object.html#c.PyObject_IsTrue "PyObject_IsTrue")
    
*   [`PyObject_Length()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Length "PyObject_Length")
    
*   [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
    
*   [`PyObject_Not()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Not "PyObject_Not")
    
*   [`PyObject_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Realloc "PyObject_Realloc")
    
*   [`PyObject_Repr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Repr "PyObject_Repr")
    
*   [`PyObject_RichCompare()`](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompare "PyObject_RichCompare")
    
*   [`PyObject_RichCompareBool()`](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompareBool "PyObject_RichCompareBool")
    
*   [`PyObject_SelfIter()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SelfIter "PyObject_SelfIter")
    
*   [`PyObject_SetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetAttr "PyObject_SetAttr")
    
*   [`PyObject_SetAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetAttrString "PyObject_SetAttrString")
    
*   [`PyObject_SetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetItem "PyObject_SetItem")
    
*   [`PyObject_Size()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Size "PyObject_Size")
    
*   [`PyObject_Str()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Str "PyObject_Str")
    
*   [`PyObject_Type()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Type "PyObject_Type")
    
*   [`PyObject_Vectorcall()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Vectorcall "PyObject_Vectorcall")
    
*   [`PyObject_VectorcallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_VectorcallMethod "PyObject_VectorcallMethod")
    
*   [`PyProperty_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyProperty_Type "PyProperty_Type")
    
*   [`PyRangeIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyRangeIter_Type "PyRangeIter_Type")
    
*   [`PyRange_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyRange_Type "PyRange_Type")
    
*   [`PyReversed_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyReversed_Type "PyReversed_Type")
    
*   [`PySeqIter_New()`](https://docs.python.org/3/c-api/iterator.html#c.PySeqIter_New "PySeqIter_New")
    
*   [`PySeqIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PySeqIter_Type "PySeqIter_Type")
    
*   [`PySequence_Check()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Check "PySequence_Check")
    
*   [`PySequence_Concat()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Concat "PySequence_Concat")
    
*   [`PySequence_Contains()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Contains "PySequence_Contains")
    
*   [`PySequence_Count()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Count "PySequence_Count")
    
*   [`PySequence_DelItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_DelItem "PySequence_DelItem")
    
*   [`PySequence_DelSlice()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_DelSlice "PySequence_DelSlice")
    
*   [`PySequence_Fast()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast "PySequence_Fast")
    
*   [`PySequence_GetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetItem "PySequence_GetItem")
    
*   [`PySequence_GetSlice()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetSlice "PySequence_GetSlice")
    
*   [`PySequence_In()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_In "PySequence_In")
    
*   [`PySequence_InPlaceConcat()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_InPlaceConcat "PySequence_InPlaceConcat")
    
*   [`PySequence_InPlaceRepeat()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_InPlaceRepeat "PySequence_InPlaceRepeat")
    
*   [`PySequence_Index()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Index "PySequence_Index")
    
*   [`PySequence_Length()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Length "PySequence_Length")
    
*   [`PySequence_List()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_List "PySequence_List")
    
*   [`PySequence_Repeat()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Repeat "PySequence_Repeat")
    
*   [`PySequence_SetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_SetItem "PySequence_SetItem")
    
*   [`PySequence_SetSlice()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_SetSlice "PySequence_SetSlice")
    
*   [`PySequence_Size()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Size "PySequence_Size")
    
*   [`PySequence_Tuple()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Tuple "PySequence_Tuple")
    
*   [`PySetIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PySetIter_Type "PySetIter_Type")
    
*   [`PySet_Add()`](https://docs.python.org/3/c-api/set.html#c.PySet_Add "PySet_Add")
    
*   [`PySet_Clear()`](https://docs.python.org/3/c-api/set.html#c.PySet_Clear "PySet_Clear")
    
*   [`PySet_Contains()`](https://docs.python.org/3/c-api/set.html#c.PySet_Contains "PySet_Contains")
    
*   [`PySet_Discard()`](https://docs.python.org/3/c-api/set.html#c.PySet_Discard "PySet_Discard")
    
*   [`PySet_New()`](https://docs.python.org/3/c-api/set.html#c.PySet_New "PySet_New")
    
*   [`PySet_Pop()`](https://docs.python.org/3/c-api/set.html#c.PySet_Pop "PySet_Pop")
    
*   [`PySet_Size()`](https://docs.python.org/3/c-api/set.html#c.PySet_Size "PySet_Size")
    
*   [`PySet_Type`](https://docs.python.org/3/c-api/set.html#c.PySet_Type "PySet_Type")
    
*   [`PySlice_AdjustIndices()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_AdjustIndices "PySlice_AdjustIndices")
    
*   [`PySlice_GetIndices()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_GetIndices "PySlice_GetIndices")
    
*   [`PySlice_GetIndicesEx()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_GetIndicesEx "PySlice_GetIndicesEx")
    
*   [`PySlice_New()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_New "PySlice_New")
    
*   [`PySlice_Type`](https://docs.python.org/3/c-api/slice.html#c.PySlice_Type "PySlice_Type")
    
*   [`PySlice_Unpack()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_Unpack "PySlice_Unpack")
    
*   [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
    
*   [`PySlot_DATA`](https://docs.python.org/3/c-api/slots.html#c.PySlot_DATA "PySlot_DATA")
    
*   [`PySlot_END`](https://docs.python.org/3/c-api/slots.html#c.PySlot_END "PySlot_END")
    
*   [`PySlot_FUNC`](https://docs.python.org/3/c-api/slots.html#c.PySlot_FUNC "PySlot_FUNC")
    
*   [`PySlot_INT64`](https://docs.python.org/3/c-api/slots.html#c.PySlot_INT64 "PySlot_INT64")
    
*   [`PySlot_INTPTR`](https://docs.python.org/3/c-api/slots.html#c.PySlot_INTPTR "PySlot_INTPTR")
    
*   [`PySlot_OPTIONAL`](https://docs.python.org/3/c-api/slots.html#c.PySlot_OPTIONAL "PySlot_OPTIONAL")
    
*   [`PySlot_PTR`](https://docs.python.org/3/c-api/slots.html#c.PySlot_PTR "PySlot_PTR")
    
*   [`PySlot_PTR_STATIC`](https://docs.python.org/3/c-api/slots.html#c.PySlot_PTR_STATIC "PySlot_PTR_STATIC")
    
*   [`PySlot_SIZE`](https://docs.python.org/3/c-api/slots.html#c.PySlot_SIZE "PySlot_SIZE")
    
*   [`PySlot_STATIC`](https://docs.python.org/3/c-api/slots.html#c.PySlot_STATIC "PySlot_STATIC")
    
*   [`PySlot_STATIC_DATA`](https://docs.python.org/3/c-api/slots.html#c.PySlot_STATIC_DATA "PySlot_STATIC_DATA")
    
*   [`PySlot_UINT64`](https://docs.python.org/3/c-api/slots.html#c.PySlot_UINT64 "PySlot_UINT64")
    
*   [`PyState_AddModule()`](https://docs.python.org/3/c-api/module.html#c.PyState_AddModule "PyState_AddModule")
    
*   [`PyState_FindModule()`](https://docs.python.org/3/c-api/module.html#c.PyState_FindModule "PyState_FindModule")
    
*   [`PyState_RemoveModule()`](https://docs.python.org/3/c-api/module.html#c.PyState_RemoveModule "PyState_RemoveModule")
    
*   [`PyStructSequence_Desc`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Desc "PyStructSequence_Desc")
    
*   [`PyStructSequence_Field`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_Field "PyStructSequence_Field")
    
*   [`PyStructSequence_GetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_GetItem "PyStructSequence_GetItem")
    
*   [`PyStructSequence_New()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_New "PyStructSequence_New")
    
*   [`PyStructSequence_NewType()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_NewType "PyStructSequence_NewType")
    
*   [`PyStructSequence_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_SetItem "PyStructSequence_SetItem")
    
*   [`PyStructSequence_UnnamedField`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_UnnamedField "PyStructSequence_UnnamedField")
    
*   [`PySuper_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PySuper_Type "PySuper_Type")
    
*   [`PySys_Audit()`](https://docs.python.org/3/c-api/sys.html#c.PySys_Audit "PySys_Audit")
    
*   [`PySys_AuditTuple()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AuditTuple "PySys_AuditTuple")
    
*   [`PySys_FormatStderr()`](https://docs.python.org/3/c-api/sys.html#c.PySys_FormatStderr "PySys_FormatStderr")
    
*   [`PySys_FormatStdout()`](https://docs.python.org/3/c-api/sys.html#c.PySys_FormatStdout "PySys_FormatStdout")
    
*   [`PySys_GetAttr()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetAttr "PySys_GetAttr")
    
*   [`PySys_GetAttrString()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetAttrString "PySys_GetAttrString")
    
*   [`PySys_GetObject()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetObject "PySys_GetObject")
    
*   [`PySys_GetOptionalAttr()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetOptionalAttr "PySys_GetOptionalAttr")
    
*   [`PySys_GetOptionalAttrString()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetOptionalAttrString "PySys_GetOptionalAttrString")
    
*   [`PySys_GetXOptions()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetXOptions "PySys_GetXOptions")
    
*   [`PySys_SetArgv()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PySys_SetArgv "PySys_SetArgv")
    
*   [`PySys_SetArgvEx()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.PySys_SetArgvEx "PySys_SetArgvEx")
    
*   [`PySys_SetObject()`](https://docs.python.org/3/c-api/sys.html#c.PySys_SetObject "PySys_SetObject")
    
*   [`PySys_WriteStderr()`](https://docs.python.org/3/c-api/sys.html#c.PySys_WriteStderr "PySys_WriteStderr")
    
*   [`PySys_WriteStdout()`](https://docs.python.org/3/c-api/sys.html#c.PySys_WriteStdout "PySys_WriteStdout")
    
*   [`PyThreadState`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState "PyThreadState")
    
*   [`PyThreadStateToken`](https://docs.python.org/3/c-api/threads.html#c.PyThreadStateToken "PyThreadStateToken")
    
*   [`PyThreadState_Clear()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_Clear "PyThreadState_Clear")
    
*   [`PyThreadState_Delete()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_Delete "PyThreadState_Delete")
    
*   [`PyThreadState_Ensure()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_Ensure "PyThreadState_Ensure")
    
*   [`PyThreadState_EnsureFromView()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_EnsureFromView "PyThreadState_EnsureFromView")
    
*   [`PyThreadState_Get()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_Get "PyThreadState_Get")
    
*   [`PyThreadState_GetDict()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetDict "PyThreadState_GetDict")
    
*   [`PyThreadState_GetFrame()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetFrame "PyThreadState_GetFrame")
    
*   [`PyThreadState_GetID()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetID "PyThreadState_GetID")
    
*   [`PyThreadState_GetInterpreter()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetInterpreter "PyThreadState_GetInterpreter")
    
*   [`PyThreadState_New()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_New "PyThreadState_New")
    
*   [`PyThreadState_Release()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_Release "PyThreadState_Release")
    
*   [`PyThreadState_SetAsyncExc()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_SetAsyncExc "PyThreadState_SetAsyncExc")
    
*   [`PyThreadState_Swap()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_Swap "PyThreadState_Swap")
    
*   [`PyThread_GetInfo()`](https://docs.python.org/3/c-api/threads.html#c.PyThread_GetInfo "PyThread_GetInfo")
    
*   [`PyThread_ReInitTLS()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_ReInitTLS "PyThread_ReInitTLS")
    
*   [`PyThread_acquire_lock()`](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_acquire_lock "PyThread_acquire_lock")
    
*   [`PyThread_acquire_lock_timed()`](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_acquire_lock_timed "PyThread_acquire_lock_timed")
    
*   [`PyThread_allocate_lock()`](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_allocate_lock "PyThread_allocate_lock")
    
*   [`PyThread_create_key()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_create_key "PyThread_create_key")
    
*   [`PyThread_delete_key()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_delete_key "PyThread_delete_key")
    
*   [`PyThread_delete_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_delete_key_value "PyThread_delete_key_value")
    
*   [`PyThread_exit_thread()`](https://docs.python.org/3/c-api/threads.html#c.PyThread_exit_thread "PyThread_exit_thread")
    
*   [`PyThread_free_lock()`](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_free_lock "PyThread_free_lock")
    
*   [`PyThread_get_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_get_key_value "PyThread_get_key_value")
    
*   [`PyThread_get_stacksize()`](https://docs.python.org/3/c-api/threads.html#c.PyThread_get_stacksize "PyThread_get_stacksize")
    
*   [`PyThread_get_thread_ident()`](https://docs.python.org/3/c-api/threads.html#c.PyThread_get_thread_ident "PyThread_get_thread_ident")
    
*   [`PyThread_get_thread_native_id()`](https://docs.python.org/3/c-api/threads.html#c.PyThread_get_thread_native_id "PyThread_get_thread_native_id")
    
*   [`PyThread_init_thread()`](https://docs.python.org/3/c-api/threads.html#c.PyThread_init_thread "PyThread_init_thread")
    
*   [`PyThread_release_lock()`](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_release_lock "PyThread_release_lock")
    
*   [`PyThread_set_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_set_key_value "PyThread_set_key_value")
    
*   [`PyThread_set_stacksize()`](https://docs.python.org/3/c-api/threads.html#c.PyThread_set_stacksize "PyThread_set_stacksize")
    
*   [`PyThread_start_new_thread()`](https://docs.python.org/3/c-api/threads.html#c.PyThread_start_new_thread "PyThread_start_new_thread")
    
*   [`PyThread_tss_alloc()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_alloc "PyThread_tss_alloc")
    
*   [`PyThread_tss_create()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_create "PyThread_tss_create")
    
*   [`PyThread_tss_delete()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_delete "PyThread_tss_delete")
    
*   [`PyThread_tss_free()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_free "PyThread_tss_free")
    
*   [`PyThread_tss_get()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_get "PyThread_tss_get")
    
*   [`PyThread_tss_is_created()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_is_created "PyThread_tss_is_created")
    
*   [`PyThread_tss_set()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_set "PyThread_tss_set")
    
*   [`PyTraceBack_Here()`](https://docs.python.org/3/c-api/exceptions.html#c.PyTraceBack_Here "PyTraceBack_Here")
    
*   [`PyTraceBack_Print()`](https://docs.python.org/3/c-api/exceptions.html#c.PyTraceBack_Print "PyTraceBack_Print")
    
*   [`PyTraceBack_Type`](https://docs.python.org/3/c-api/exceptions.html#c.PyTraceBack_Type "PyTraceBack_Type")
    
*   [`PyTupleIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyTupleIter_Type "PyTupleIter_Type")
    
*   [`PyTuple_GetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_GetItem "PyTuple_GetItem")
    
*   [`PyTuple_GetSlice()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_GetSlice "PyTuple_GetSlice")
    
*   [`PyTuple_New()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_New "PyTuple_New")
    
*   [`PyTuple_Pack()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Pack "PyTuple_Pack")
    
*   [`PyTuple_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SetItem "PyTuple_SetItem")
    
*   [`PyTuple_Size()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Size "PyTuple_Size")
    
*   [`PyTuple_Type`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Type "PyTuple_Type")
    
*   [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
    
*   [`PyType_ClearCache()`](https://docs.python.org/3/c-api/type.html#c.PyType_ClearCache "PyType_ClearCache")
    
*   [`PyType_Freeze()`](https://docs.python.org/3/c-api/type.html#c.PyType_Freeze "PyType_Freeze")
    
*   [`PyType_FromMetaclass()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromMetaclass "PyType_FromMetaclass")
    
*   [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec")
    
*   [`PyType_FromSlots()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "PyType_FromSlots")
    
*   [`PyType_FromSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec "PyType_FromSpec")
    
*   [`PyType_FromSpecWithBases()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpecWithBases "PyType_FromSpecWithBases")
    
*   [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
    
*   [`PyType_GenericNew()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericNew "PyType_GenericNew")
    
*   [`PyType_GetBaseByToken()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetBaseByToken "PyType_GetBaseByToken")
    
*   [`PyType_GetBaseByToken_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetBaseByToken_DuringGC "PyType_GetBaseByToken_DuringGC")
    
*   [`PyType_GetFlags()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetFlags "PyType_GetFlags")
    
*   [`PyType_GetFullyQualifiedName()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetFullyQualifiedName "PyType_GetFullyQualifiedName")
    
*   [`PyType_GetModule()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModule "PyType_GetModule")
    
*   [`PyType_GetModuleByDef()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByDef "PyType_GetModuleByDef")
    
*   [`PyType_GetModuleByToken()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByToken "PyType_GetModuleByToken")
    
*   [`PyType_GetModuleByToken_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetModuleByToken_DuringGC "PyType_GetModuleByToken_DuringGC")
    
*   [`PyType_GetModuleName()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleName "PyType_GetModuleName")
    
*   [`PyType_GetModuleState()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleState "PyType_GetModuleState")
    
*   [`PyType_GetModuleState_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetModuleState_DuringGC "PyType_GetModuleState_DuringGC")
    
*   [`PyType_GetModule_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetModule_DuringGC "PyType_GetModule_DuringGC")
    
*   [`PyType_GetName()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetName "PyType_GetName")
    
*   [`PyType_GetQualName()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetQualName "PyType_GetQualName")
    
*   [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot")
    
*   [`PyType_GetTypeDataSize()`](https://docs.python.org/3/c-api/object.html#c.PyType_GetTypeDataSize "PyType_GetTypeDataSize")
    
*   [`PyType_IsSubtype()`](https://docs.python.org/3/c-api/type.html#c.PyType_IsSubtype "PyType_IsSubtype")
    
*   [`PyType_Modified()`](https://docs.python.org/3/c-api/type.html#c.PyType_Modified "PyType_Modified")
    
*   [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
    
*   [`PyType_Slot`](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
    
*   [`PyType_Spec`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "PyType_Spec")
    
*   [`PyType_Type`](https://docs.python.org/3/c-api/type.html#c.PyType_Type "PyType_Type")
    
*   [`PyUnicodeDecodeError_Create()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_Create "PyUnicodeDecodeError_Create")
    
*   [`PyUnicodeDecodeError_GetEncoding()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_GetEncoding "PyUnicodeDecodeError_GetEncoding")
    
*   [`PyUnicodeDecodeError_GetEnd()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_GetEnd "PyUnicodeDecodeError_GetEnd")
    
*   [`PyUnicodeDecodeError_GetObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_GetObject "PyUnicodeDecodeError_GetObject")
    
*   [`PyUnicodeDecodeError_GetReason()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_GetReason "PyUnicodeDecodeError_GetReason")
    
*   [`PyUnicodeDecodeError_GetStart()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_GetStart "PyUnicodeDecodeError_GetStart")
    
*   [`PyUnicodeDecodeError_SetEnd()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_SetEnd "PyUnicodeDecodeError_SetEnd")
    
*   [`PyUnicodeDecodeError_SetReason()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_SetReason "PyUnicodeDecodeError_SetReason")
    
*   [`PyUnicodeDecodeError_SetStart()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeDecodeError_SetStart "PyUnicodeDecodeError_SetStart")
    
*   [`PyUnicodeEncodeError_GetEncoding()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_GetEncoding "PyUnicodeEncodeError_GetEncoding")
    
*   [`PyUnicodeEncodeError_GetEnd()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_GetEnd "PyUnicodeEncodeError_GetEnd")
    
*   [`PyUnicodeEncodeError_GetObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_GetObject "PyUnicodeEncodeError_GetObject")
    
*   [`PyUnicodeEncodeError_GetReason()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_GetReason "PyUnicodeEncodeError_GetReason")
    
*   [`PyUnicodeEncodeError_GetStart()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_GetStart "PyUnicodeEncodeError_GetStart")
    
*   [`PyUnicodeEncodeError_SetEnd()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_SetEnd "PyUnicodeEncodeError_SetEnd")
    
*   [`PyUnicodeEncodeError_SetReason()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_SetReason "PyUnicodeEncodeError_SetReason")
    
*   [`PyUnicodeEncodeError_SetStart()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeEncodeError_SetStart "PyUnicodeEncodeError_SetStart")
    
*   [`PyUnicodeIter_Type`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeIter_Type "PyUnicodeIter_Type")
    
*   [`PyUnicodeTranslateError_GetEnd()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_GetEnd "PyUnicodeTranslateError_GetEnd")
    
*   [`PyUnicodeTranslateError_GetObject()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_GetObject "PyUnicodeTranslateError_GetObject")
    
*   [`PyUnicodeTranslateError_GetReason()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_GetReason "PyUnicodeTranslateError_GetReason")
    
*   [`PyUnicodeTranslateError_GetStart()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_GetStart "PyUnicodeTranslateError_GetStart")
    
*   [`PyUnicodeTranslateError_SetEnd()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_SetEnd "PyUnicodeTranslateError_SetEnd")
    
*   [`PyUnicodeTranslateError_SetReason()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_SetReason "PyUnicodeTranslateError_SetReason")
    
*   [`PyUnicodeTranslateError_SetStart()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnicodeTranslateError_SetStart "PyUnicodeTranslateError_SetStart")
    
*   [`PyUnicode_Append()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Append "PyUnicode_Append")
    
*   [`PyUnicode_AppendAndDel()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AppendAndDel "PyUnicode_AppendAndDel")
    
*   [`PyUnicode_AsASCIIString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsASCIIString "PyUnicode_AsASCIIString")
    
*   [`PyUnicode_AsCharmapString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsCharmapString "PyUnicode_AsCharmapString")
    
*   [`PyUnicode_AsEncodedString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsEncodedString "PyUnicode_AsEncodedString")
    
*   [`PyUnicode_AsLatin1String()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsLatin1String "PyUnicode_AsLatin1String")
    
*   [`PyUnicode_AsMBCSString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsMBCSString "PyUnicode_AsMBCSString")
    
*   [`PyUnicode_AsRawUnicodeEscapeString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsRawUnicodeEscapeString "PyUnicode_AsRawUnicodeEscapeString")
    
*   [`PyUnicode_AsUCS4()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUCS4 "PyUnicode_AsUCS4")
    
*   [`PyUnicode_AsUCS4Copy()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUCS4Copy "PyUnicode_AsUCS4Copy")
    
*   [`PyUnicode_AsUTF16String()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF16String "PyUnicode_AsUTF16String")
    
*   [`PyUnicode_AsUTF32String()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF32String "PyUnicode_AsUTF32String")
    
*   [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize "PyUnicode_AsUTF8AndSize")
    
*   [`PyUnicode_AsUTF8String()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8String "PyUnicode_AsUTF8String")
    
*   [`PyUnicode_AsUnicodeEscapeString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUnicodeEscapeString "PyUnicode_AsUnicodeEscapeString")
    
*   [`PyUnicode_AsWideChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsWideChar "PyUnicode_AsWideChar")
    
*   [`PyUnicode_AsWideCharString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsWideCharString "PyUnicode_AsWideCharString")
    
*   [`PyUnicode_BuildEncodingMap()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_BuildEncodingMap "PyUnicode_BuildEncodingMap")
    
*   [`PyUnicode_Compare()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Compare "PyUnicode_Compare")
    
*   [`PyUnicode_CompareWithASCIIString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CompareWithASCIIString "PyUnicode_CompareWithASCIIString")
    
*   [`PyUnicode_Concat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Concat "PyUnicode_Concat")
    
*   [`PyUnicode_Contains()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Contains "PyUnicode_Contains")
    
*   [`PyUnicode_Count()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Count "PyUnicode_Count")
    
*   [`PyUnicode_Decode()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Decode "PyUnicode_Decode")
    
*   [`PyUnicode_DecodeASCII()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeASCII "PyUnicode_DecodeASCII")
    
*   [`PyUnicode_DecodeCharmap()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeCharmap "PyUnicode_DecodeCharmap")
    
*   [`PyUnicode_DecodeCodePageStateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeCodePageStateful "PyUnicode_DecodeCodePageStateful")
    
*   [`PyUnicode_DecodeFSDefault()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeFSDefault "PyUnicode_DecodeFSDefault")
    
*   [`PyUnicode_DecodeFSDefaultAndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeFSDefaultAndSize "PyUnicode_DecodeFSDefaultAndSize")
    
*   [`PyUnicode_DecodeLatin1()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLatin1 "PyUnicode_DecodeLatin1")
    
*   [`PyUnicode_DecodeLocale()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLocale "PyUnicode_DecodeLocale")
    
*   [`PyUnicode_DecodeLocaleAndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLocaleAndSize "PyUnicode_DecodeLocaleAndSize")
    
*   [`PyUnicode_DecodeMBCS()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeMBCS "PyUnicode_DecodeMBCS")
    
*   [`PyUnicode_DecodeMBCSStateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeMBCSStateful "PyUnicode_DecodeMBCSStateful")
    
*   [`PyUnicode_DecodeRawUnicodeEscape()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeRawUnicodeEscape "PyUnicode_DecodeRawUnicodeEscape")
    
*   [`PyUnicode_DecodeUTF16()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF16 "PyUnicode_DecodeUTF16")
    
*   [`PyUnicode_DecodeUTF16Stateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF16Stateful "PyUnicode_DecodeUTF16Stateful")
    
*   [`PyUnicode_DecodeUTF32()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF32 "PyUnicode_DecodeUTF32")
    
*   [`PyUnicode_DecodeUTF32Stateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF32Stateful "PyUnicode_DecodeUTF32Stateful")
    
*   [`PyUnicode_DecodeUTF7()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF7 "PyUnicode_DecodeUTF7")
    
*   [`PyUnicode_DecodeUTF7Stateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF7Stateful "PyUnicode_DecodeUTF7Stateful")
    
*   [`PyUnicode_DecodeUTF8()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF8 "PyUnicode_DecodeUTF8")
    
*   [`PyUnicode_DecodeUTF8Stateful()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUTF8Stateful "PyUnicode_DecodeUTF8Stateful")
    
*   [`PyUnicode_DecodeUnicodeEscape()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeUnicodeEscape "PyUnicode_DecodeUnicodeEscape")
    
*   [`PyUnicode_EncodeCodePage()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeCodePage "PyUnicode_EncodeCodePage")
    
*   [`PyUnicode_EncodeFSDefault()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeFSDefault "PyUnicode_EncodeFSDefault")
    
*   [`PyUnicode_EncodeLocale()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeLocale "PyUnicode_EncodeLocale")
    
*   [`PyUnicode_Equal()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Equal "PyUnicode_Equal")
    
*   [`PyUnicode_EqualToUTF8()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EqualToUTF8 "PyUnicode_EqualToUTF8")
    
*   [`PyUnicode_EqualToUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EqualToUTF8AndSize "PyUnicode_EqualToUTF8AndSize")
    
*   [`PyUnicode_FSConverter()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FSConverter "PyUnicode_FSConverter")
    
*   [`PyUnicode_FSDecoder()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FSDecoder "PyUnicode_FSDecoder")
    
*   [`PyUnicode_Find()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Find "PyUnicode_Find")
    
*   [`PyUnicode_FindChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FindChar "PyUnicode_FindChar")
    
*   [`PyUnicode_Format()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Format "PyUnicode_Format")
    
*   [`PyUnicode_FromEncodedObject()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromEncodedObject "PyUnicode_FromEncodedObject")
    
*   [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
    
*   [`PyUnicode_FromFormatV()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormatV "PyUnicode_FromFormatV")
    
*   [`PyUnicode_FromObject()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromObject "PyUnicode_FromObject")
    
*   [`PyUnicode_FromOrdinal()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromOrdinal "PyUnicode_FromOrdinal")
    
*   [`PyUnicode_FromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromString "PyUnicode_FromString")
    
*   [`PyUnicode_FromStringAndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromStringAndSize "PyUnicode_FromStringAndSize")
    
*   [`PyUnicode_FromWideChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromWideChar "PyUnicode_FromWideChar")
    
*   [`PyUnicode_GetDefaultEncoding()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetDefaultEncoding "PyUnicode_GetDefaultEncoding")
    
*   [`PyUnicode_GetLength()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetLength "PyUnicode_GetLength")
    
*   [`PyUnicode_InternFromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternFromString "PyUnicode_InternFromString")
    
*   [`PyUnicode_InternInPlace()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternInPlace "PyUnicode_InternInPlace")
    
*   [`PyUnicode_IsIdentifier()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_IsIdentifier "PyUnicode_IsIdentifier")
    
*   [`PyUnicode_Join()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Join "PyUnicode_Join")
    
*   [`PyUnicode_Partition()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Partition "PyUnicode_Partition")
    
*   [`PyUnicode_RPartition()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_RPartition "PyUnicode_RPartition")
    
*   [`PyUnicode_RSplit()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_RSplit "PyUnicode_RSplit")
    
*   [`PyUnicode_ReadChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_ReadChar "PyUnicode_ReadChar")
    
*   [`PyUnicode_Replace()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Replace "PyUnicode_Replace")
    
*   [`PyUnicode_Resize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Resize "PyUnicode_Resize")
    
*   [`PyUnicode_RichCompare()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_RichCompare "PyUnicode_RichCompare")
    
*   [`PyUnicode_Split()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Split "PyUnicode_Split")
    
*   [`PyUnicode_Splitlines()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Splitlines "PyUnicode_Splitlines")
    
*   [`PyUnicode_Substring()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Substring "PyUnicode_Substring")
    
*   [`PyUnicode_Tailmatch()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Tailmatch "PyUnicode_Tailmatch")
    
*   [`PyUnicode_Translate()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Translate "PyUnicode_Translate")
    
*   [`PyUnicode_Type`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Type "PyUnicode_Type")
    
*   [`PyUnicode_WriteChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_WriteChar "PyUnicode_WriteChar")
    
*   [`PyVarObject`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
    
*   [`PyVarObject.ob_base`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_base "PyVarObject.ob_base")
    
*   [`PyVarObject.ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
    
*   [`PyVectorcall_Call()`](https://docs.python.org/3/c-api/call.html#c.PyVectorcall_Call "PyVectorcall_Call")
    
*   [`PyVectorcall_NARGS()`](https://docs.python.org/3/c-api/call.html#c.PyVectorcall_NARGS "PyVectorcall_NARGS")
    
*   `PyWeakReference`
    
*   [`PyWeakref_GetRef()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef")
    
*   [`PyWeakref_NewProxy()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_NewProxy "PyWeakref_NewProxy")
    
*   [`PyWeakref_NewRef()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_NewRef "PyWeakref_NewRef")
    
*   [`PyWrapperDescr_Type`](https://docs.python.org/3/c-api/descriptor.html#c.PyWrapperDescr_Type "PyWrapperDescr_Type")
    
*   [`PyWrapper_New()`](https://docs.python.org/3/c-api/descriptor.html#c.PyWrapper_New "PyWrapper_New")
    
*   [`PyZip_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyZip_Type "PyZip_Type")
    
*   [`Py_ASNATIVEBYTES_ALLOW_INDEX`](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_ALLOW_INDEX "Py_ASNATIVEBYTES_ALLOW_INDEX")
    
*   [`Py_ASNATIVEBYTES_BIG_ENDIAN`](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_BIG_ENDIAN "Py_ASNATIVEBYTES_BIG_ENDIAN")
    
*   [`Py_ASNATIVEBYTES_DEFAULTS`](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_DEFAULTS "Py_ASNATIVEBYTES_DEFAULTS")
    
*   [`Py_ASNATIVEBYTES_LITTLE_ENDIAN`](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_LITTLE_ENDIAN "Py_ASNATIVEBYTES_LITTLE_ENDIAN")
    
*   [`Py_ASNATIVEBYTES_NATIVE_ENDIAN`](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_NATIVE_ENDIAN "Py_ASNATIVEBYTES_NATIVE_ENDIAN")
    
*   [`Py_ASNATIVEBYTES_REJECT_NEGATIVE`](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_REJECT_NEGATIVE "Py_ASNATIVEBYTES_REJECT_NEGATIVE")
    
*   [`Py_ASNATIVEBYTES_UNSIGNED_BUFFER`](https://docs.python.org/3/c-api/long.html#c.Py_ASNATIVEBYTES_UNSIGNED_BUFFER "Py_ASNATIVEBYTES_UNSIGNED_BUFFER")
    
*   [`Py_AUDIT_READ`](https://docs.python.org/3/c-api/structures.html#c.Py_AUDIT_READ "Py_AUDIT_READ")
    
*   [`Py_AddPendingCall()`](https://docs.python.org/3/c-api/threads.html#c.Py_AddPendingCall "Py_AddPendingCall")
    
*   [`Py_AtExit()`](https://docs.python.org/3/c-api/sys.html#c.Py_AtExit "Py_AtExit")
    
*   [`Py_BEGIN_ALLOW_THREADS`](https://docs.python.org/3/c-api/threads.html#c.Py_BEGIN_ALLOW_THREADS "Py_BEGIN_ALLOW_THREADS")
    
*   [`Py_BEGIN_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION "Py_BEGIN_CRITICAL_SECTION")
    
*   [`Py_BEGIN_CRITICAL_SECTION2`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2 "Py_BEGIN_CRITICAL_SECTION2")
    
*   [`Py_BLOCK_THREADS`](https://docs.python.org/3/c-api/threads.html#c.Py_BLOCK_THREADS "Py_BLOCK_THREADS")
    
*   [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue")
    
*   [`Py_BytesMain()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_BytesMain "Py_BytesMain")
    
*   [`Py_CLEAR`](https://docs.python.org/3/c-api/refcounting.html#c.Py_CLEAR "Py_CLEAR")
    
*   [`Py_CompileString()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileString "Py_CompileString")
    
*   [`Py_DECREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
    
*   [`Py_DecRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DecRef "Py_DecRef")
    
*   [`Py_DecodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_DecodeLocale "Py_DecodeLocale")
    
*   [`Py_END_ALLOW_THREADS`](https://docs.python.org/3/c-api/threads.html#c.Py_END_ALLOW_THREADS "Py_END_ALLOW_THREADS")
    
*   [`Py_END_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_END_CRITICAL_SECTION "Py_END_CRITICAL_SECTION")
    
*   [`Py_END_CRITICAL_SECTION2`](https://docs.python.org/3/c-api/synchronization.html#c.Py_END_CRITICAL_SECTION2 "Py_END_CRITICAL_SECTION2")
    
*   [`Py_EncodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_EncodeLocale "Py_EncodeLocale")
    
*   [`Py_EndInterpreter()`](https://docs.python.org/3/c-api/subinterpreters.html#c.Py_EndInterpreter "Py_EndInterpreter")
    
*   [`Py_EnterRecursiveCall()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_EnterRecursiveCall "Py_EnterRecursiveCall")
    
*   [`Py_Exit()`](https://docs.python.org/3/c-api/sys.html#c.Py_Exit "Py_Exit")
    
*   [`Py_FatalError()`](https://docs.python.org/3/c-api/sys.html#c.Py_FatalError "Py_FatalError")
    
*   `Py_FileSystemDefaultEncodeErrors`
    
*   `Py_FileSystemDefaultEncoding`
    
*   [`Py_Finalize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Finalize "Py_Finalize")
    
*   [`Py_FinalizeEx()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_FinalizeEx "Py_FinalizeEx")
    
*   [`Py_GenericAlias()`](https://docs.python.org/3/c-api/typehints.html#c.Py_GenericAlias "Py_GenericAlias")
    
*   [`Py_GenericAliasType`](https://docs.python.org/3/c-api/typehints.html#c.Py_GenericAliasType "Py_GenericAliasType")
    
*   [`Py_GetBuildInfo()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_GetBuildInfo "Py_GetBuildInfo")
    
*   [`Py_GetCompiler()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_GetCompiler "Py_GetCompiler")
    
*   [`Py_GetConstant()`](https://docs.python.org/3/c-api/object.html#c.Py_GetConstant "Py_GetConstant")
    
*   [`Py_GetConstantBorrowed()`](https://docs.python.org/3/c-api/object.html#c.Py_GetConstantBorrowed "Py_GetConstantBorrowed")
    
*   [`Py_GetCopyright()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_GetCopyright "Py_GetCopyright")
    
*   [`Py_GetPlatform()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_GetPlatform "Py_GetPlatform")
    
*   [`Py_GetRecursionLimit()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_GetRecursionLimit "Py_GetRecursionLimit")
    
*   [`Py_GetVersion()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_GetVersion "Py_GetVersion")
    
*   `Py_HasFileSystemDefaultEncoding`
    
*   [`Py_INCREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "Py_INCREF")
    
*   [`Py_IS_TYPE()`](https://docs.python.org/3/c-api/structures.html#c.Py_IS_TYPE "Py_IS_TYPE")
    
*   [`Py_IncRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_IncRef "Py_IncRef")
    
*   [`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
    
*   [`Py_InitializeEx()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeEx "Py_InitializeEx")
    
*   [`Py_Is()`](https://docs.python.org/3/c-api/structures.html#c.Py_Is "Py_Is")
    
*   [`Py_IsFalse()`](https://docs.python.org/3/c-api/structures.html#c.Py_IsFalse "Py_IsFalse")
    
*   [`Py_IsFinalizing()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IsFinalizing "Py_IsFinalizing")
    
*   [`Py_IsInitialized()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_IsInitialized "Py_IsInitialized")
    
*   [`Py_IsNone()`](https://docs.python.org/3/c-api/structures.html#c.Py_IsNone "Py_IsNone")
    
*   [`Py_IsTrue()`](https://docs.python.org/3/c-api/structures.html#c.Py_IsTrue "Py_IsTrue")
    
*   [`Py_LeaveRecursiveCall()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_LeaveRecursiveCall "Py_LeaveRecursiveCall")
    
*   [`Py_Main()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Main "Py_Main")
    
*   [`Py_MakePendingCalls()`](https://docs.python.org/3/c-api/threads.html#c.Py_MakePendingCalls "Py_MakePendingCalls")
    
*   [`Py_NewInterpreter()`](https://docs.python.org/3/c-api/subinterpreters.html#c.Py_NewInterpreter "Py_NewInterpreter")
    
*   [`Py_NewRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_NewRef "Py_NewRef")
    
*   [`Py_PACK_FULL_VERSION()`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_PACK_FULL_VERSION "Py_PACK_FULL_VERSION")
    
*   [`Py_PACK_VERSION()`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_PACK_VERSION "Py_PACK_VERSION")
    
*   [`Py_READONLY`](https://docs.python.org/3/c-api/structures.html#c.Py_READONLY "Py_READONLY")
    
*   [`Py_REFCNT()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT")
    
*   [`Py_RELATIVE_OFFSET`](https://docs.python.org/3/c-api/structures.html#c.Py_RELATIVE_OFFSET "Py_RELATIVE_OFFSET")
    
*   [`Py_ReprEnter()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_ReprEnter "Py_ReprEnter")
    
*   [`Py_ReprLeave()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_ReprLeave "Py_ReprLeave")
    
*   [`Py_SET_REFCNT`](https://docs.python.org/3/c-api/refcounting.html#c.Py_SET_REFCNT "Py_SET_REFCNT")
    
*   [`Py_SET_SIZE()`](https://docs.python.org/3/c-api/structures.html#c.Py_SET_SIZE "Py_SET_SIZE")
    
*   [`Py_SET_TYPE`](https://docs.python.org/3/c-api/structures.html#c.Py_SET_TYPE "Py_SET_TYPE")
    
*   [`Py_SIZE()`](https://docs.python.org/3/c-api/structures.html#c.Py_SIZE "Py_SIZE")
    
*   [`Py_SetProgramName()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_SetProgramName "Py_SetProgramName")
    
*   [`Py_SetPythonHome()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_SetPythonHome "Py_SetPythonHome")
    
*   [`Py_SetRecursionLimit()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_SetRecursionLimit "Py_SetRecursionLimit")
    
*   [`Py_TPFLAGS_BASETYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_BASETYPE "Py_TPFLAGS_BASETYPE")
    
*   [`Py_TPFLAGS_DEFAULT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_DEFAULT "Py_TPFLAGS_DEFAULT")
    
*   [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
    
*   [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL "Py_TPFLAGS_HAVE_VECTORCALL")
    
*   [`Py_TPFLAGS_ITEMS_AT_END`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_ITEMS_AT_END "Py_TPFLAGS_ITEMS_AT_END")
    
*   [`Py_TPFLAGS_METHOD_DESCRIPTOR`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_METHOD_DESCRIPTOR "Py_TPFLAGS_METHOD_DESCRIPTOR")
    
*   [`Py_TP_USE_SPEC`](https://docs.python.org/3/c-api/type.html#c.Py_TP_USE_SPEC "Py_TP_USE_SPEC")
    
*   [`Py_TYPE()`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
    
*   [`Py_T_BOOL`](https://docs.python.org/3/c-api/structures.html#c.Py_T_BOOL "Py_T_BOOL")
    
*   [`Py_T_BYTE`](https://docs.python.org/3/c-api/structures.html#c.Py_T_BYTE "Py_T_BYTE")
    
*   [`Py_T_CHAR`](https://docs.python.org/3/c-api/structures.html#c.Py_T_CHAR "Py_T_CHAR")
    
*   [`Py_T_DOUBLE`](https://docs.python.org/3/c-api/structures.html#c.Py_T_DOUBLE "Py_T_DOUBLE")
    
*   [`Py_T_FLOAT`](https://docs.python.org/3/c-api/structures.html#c.Py_T_FLOAT "Py_T_FLOAT")
    
*   [`Py_T_INT`](https://docs.python.org/3/c-api/structures.html#c.Py_T_INT "Py_T_INT")
    
*   [`Py_T_LONG`](https://docs.python.org/3/c-api/structures.html#c.Py_T_LONG "Py_T_LONG")
    
*   [`Py_T_LONGLONG`](https://docs.python.org/3/c-api/structures.html#c.Py_T_LONGLONG "Py_T_LONGLONG")
    
*   [`Py_T_OBJECT_EX`](https://docs.python.org/3/c-api/structures.html#c.Py_T_OBJECT_EX "Py_T_OBJECT_EX")
    
*   [`Py_T_PYSSIZET`](https://docs.python.org/3/c-api/structures.html#c.Py_T_PYSSIZET "Py_T_PYSSIZET")
    
*   [`Py_T_SHORT`](https://docs.python.org/3/c-api/structures.html#c.Py_T_SHORT "Py_T_SHORT")
    
*   [`Py_T_STRING`](https://docs.python.org/3/c-api/structures.html#c.Py_T_STRING "Py_T_STRING")
    
*   [`Py_T_STRING_INPLACE`](https://docs.python.org/3/c-api/structures.html#c.Py_T_STRING_INPLACE "Py_T_STRING_INPLACE")
    
*   [`Py_T_UBYTE`](https://docs.python.org/3/c-api/structures.html#c.Py_T_UBYTE "Py_T_UBYTE")
    
*   [`Py_T_UINT`](https://docs.python.org/3/c-api/structures.html#c.Py_T_UINT "Py_T_UINT")
    
*   [`Py_T_ULONG`](https://docs.python.org/3/c-api/structures.html#c.Py_T_ULONG "Py_T_ULONG")
    
*   [`Py_T_ULONGLONG`](https://docs.python.org/3/c-api/structures.html#c.Py_T_ULONGLONG "Py_T_ULONGLONG")
    
*   [`Py_T_USHORT`](https://docs.python.org/3/c-api/structures.html#c.Py_T_USHORT "Py_T_USHORT")
    
*   [`Py_UCS4`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
    
*   [`Py_UNBLOCK_THREADS`](https://docs.python.org/3/c-api/threads.html#c.Py_UNBLOCK_THREADS "Py_UNBLOCK_THREADS")
    
*   `Py_UTF8Mode`
    
*   [`Py_VaBuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_VaBuildValue "Py_VaBuildValue")
    
*   [`Py_Version`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_Version "Py_Version")
    
*   [`Py_XDECREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF")
    
*   [`Py_XINCREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XINCREF "Py_XINCREF")
    
*   [`Py_XNewRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XNewRef "Py_XNewRef")
    
*   [`Py_am_aiter`](https://docs.python.org/3/c-api/typeobj.html#c.Py_am_aiter "Py_am_aiter")
    
*   [`Py_am_anext`](https://docs.python.org/3/c-api/typeobj.html#c.Py_am_anext "Py_am_anext")
    
*   [`Py_am_await`](https://docs.python.org/3/c-api/typeobj.html#c.Py_am_await "Py_am_await")
    
*   [`Py_am_send`](https://docs.python.org/3/c-api/typeobj.html#c.Py_am_send "Py_am_send")
    
*   [`Py_bf_getbuffer`](https://docs.python.org/3/c-api/typeobj.html#c.Py_bf_getbuffer "Py_bf_getbuffer")
    
*   [`Py_bf_releasebuffer`](https://docs.python.org/3/c-api/typeobj.html#c.Py_bf_releasebuffer "Py_bf_releasebuffer")
    
*   [`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
    
*   `Py_intptr_t`
    
*   [`Py_mod_abi`](https://docs.python.org/3/c-api/module.html#c.Py_mod_abi "Py_mod_abi")
    
*   [`Py_mod_create`](https://docs.python.org/3/c-api/module.html#c.Py_mod_create "Py_mod_create")
    
*   [`Py_mod_doc`](https://docs.python.org/3/c-api/module.html#c.Py_mod_doc "Py_mod_doc")
    
*   [`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
    
*   [`Py_mod_gil`](https://docs.python.org/3/c-api/module.html#c.Py_mod_gil "Py_mod_gil")
    
*   [`Py_mod_methods`](https://docs.python.org/3/c-api/module.html#c.Py_mod_methods "Py_mod_methods")
    
*   [`Py_mod_multiple_interpreters`](https://docs.python.org/3/c-api/module.html#c.Py_mod_multiple_interpreters "Py_mod_multiple_interpreters")
    
*   [`Py_mod_name`](https://docs.python.org/3/c-api/module.html#c.Py_mod_name "Py_mod_name")
    
*   [`Py_mod_slots`](https://docs.python.org/3/c-api/module.html#c.Py_mod_slots "Py_mod_slots")
    
*   [`Py_mod_state_clear`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_clear "Py_mod_state_clear")
    
*   [`Py_mod_state_free`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_free "Py_mod_state_free")
    
*   [`Py_mod_state_size`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_size "Py_mod_state_size")
    
*   [`Py_mod_state_traverse`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_traverse "Py_mod_state_traverse")
    
*   [`Py_mod_token`](https://docs.python.org/3/c-api/module.html#c.Py_mod_token "Py_mod_token")
    
*   [`Py_mp_ass_subscript`](https://docs.python.org/3/c-api/typeobj.html#c.Py_mp_ass_subscript "Py_mp_ass_subscript")
    
*   [`Py_mp_length`](https://docs.python.org/3/c-api/typeobj.html#c.Py_mp_length "Py_mp_length")
    
*   [`Py_mp_subscript`](https://docs.python.org/3/c-api/typeobj.html#c.Py_mp_subscript "Py_mp_subscript")
    
*   [`Py_nb_absolute`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_absolute "Py_nb_absolute")
    
*   [`Py_nb_add`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_add "Py_nb_add")
    
*   [`Py_nb_and`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_and "Py_nb_and")
    
*   [`Py_nb_bool`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_bool "Py_nb_bool")
    
*   [`Py_nb_divmod`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_divmod "Py_nb_divmod")
    
*   [`Py_nb_float`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_float "Py_nb_float")
    
*   [`Py_nb_floor_divide`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_floor_divide "Py_nb_floor_divide")
    
*   [`Py_nb_index`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_index "Py_nb_index")
    
*   [`Py_nb_inplace_add`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_add "Py_nb_inplace_add")
    
*   [`Py_nb_inplace_and`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_and "Py_nb_inplace_and")
    
*   [`Py_nb_inplace_floor_divide`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_floor_divide "Py_nb_inplace_floor_divide")
    
*   [`Py_nb_inplace_lshift`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_lshift "Py_nb_inplace_lshift")
    
*   [`Py_nb_inplace_matrix_multiply`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_matrix_multiply "Py_nb_inplace_matrix_multiply")
    
*   [`Py_nb_inplace_multiply`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_multiply "Py_nb_inplace_multiply")
    
*   [`Py_nb_inplace_or`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_or "Py_nb_inplace_or")
    
*   [`Py_nb_inplace_power`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_power "Py_nb_inplace_power")
    
*   [`Py_nb_inplace_remainder`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_remainder "Py_nb_inplace_remainder")
    
*   [`Py_nb_inplace_rshift`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_rshift "Py_nb_inplace_rshift")
    
*   [`Py_nb_inplace_subtract`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_subtract "Py_nb_inplace_subtract")
    
*   [`Py_nb_inplace_true_divide`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_true_divide "Py_nb_inplace_true_divide")
    
*   [`Py_nb_inplace_xor`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_inplace_xor "Py_nb_inplace_xor")
    
*   [`Py_nb_int`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_int "Py_nb_int")
    
*   [`Py_nb_invert`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_invert "Py_nb_invert")
    
*   [`Py_nb_lshift`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_lshift "Py_nb_lshift")
    
*   [`Py_nb_matrix_multiply`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_matrix_multiply "Py_nb_matrix_multiply")
    
*   [`Py_nb_multiply`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_multiply "Py_nb_multiply")
    
*   [`Py_nb_negative`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_negative "Py_nb_negative")
    
*   [`Py_nb_or`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_or "Py_nb_or")
    
*   [`Py_nb_positive`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_positive "Py_nb_positive")
    
*   [`Py_nb_power`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_power "Py_nb_power")
    
*   [`Py_nb_remainder`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_remainder "Py_nb_remainder")
    
*   [`Py_nb_rshift`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_rshift "Py_nb_rshift")
    
*   [`Py_nb_subtract`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_subtract "Py_nb_subtract")
    
*   [`Py_nb_true_divide`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_true_divide "Py_nb_true_divide")
    
*   [`Py_nb_xor`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_xor "Py_nb_xor")
    
*   [`Py_slot_end`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_end "Py_slot_end")
    
*   [`Py_slot_invalid`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_invalid "Py_slot_invalid")
    
*   [`Py_slot_subslots`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_subslots "Py_slot_subslots")
    
*   [`Py_sq_ass_item`](https://docs.python.org/3/c-api/typeobj.html#c.Py_sq_ass_item "Py_sq_ass_item")
    
*   [`Py_sq_concat`](https://docs.python.org/3/c-api/typeobj.html#c.Py_sq_concat "Py_sq_concat")
    
*   [`Py_sq_contains`](https://docs.python.org/3/c-api/typeobj.html#c.Py_sq_contains "Py_sq_contains")
    
*   [`Py_sq_inplace_concat`](https://docs.python.org/3/c-api/typeobj.html#c.Py_sq_inplace_concat "Py_sq_inplace_concat")
    
*   [`Py_sq_inplace_repeat`](https://docs.python.org/3/c-api/typeobj.html#c.Py_sq_inplace_repeat "Py_sq_inplace_repeat")
    
*   [`Py_sq_item`](https://docs.python.org/3/c-api/typeobj.html#c.Py_sq_item "Py_sq_item")
    
*   [`Py_sq_length`](https://docs.python.org/3/c-api/typeobj.html#c.Py_sq_length "Py_sq_length")
    
*   [`Py_sq_repeat`](https://docs.python.org/3/c-api/typeobj.html#c.Py_sq_repeat "Py_sq_repeat")
    
*   [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
    
*   [`Py_tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_alloc "Py_tp_alloc")
    
*   [`Py_tp_base`](https://docs.python.org/3/c-api/type.html#c.Py_tp_base "Py_tp_base")
    
*   [`Py_tp_bases`](https://docs.python.org/3/c-api/type.html#c.Py_tp_bases "Py_tp_bases")
    
*   [`Py_tp_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_basicsize "Py_tp_basicsize")
    
*   [`Py_tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_call "Py_tp_call")
    
*   [`Py_tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_clear "Py_tp_clear")
    
*   [`Py_tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_dealloc "Py_tp_dealloc")
    
*   [`Py_tp_del`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_del "Py_tp_del")
    
*   [`Py_tp_descr_get`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_descr_get "Py_tp_descr_get")
    
*   [`Py_tp_descr_set`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_descr_set "Py_tp_descr_set")
    
*   [`Py_tp_doc`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_doc "Py_tp_doc")
    
*   [`Py_tp_extra_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_extra_basicsize "Py_tp_extra_basicsize")
    
*   [`Py_tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_finalize "Py_tp_finalize")
    
*   [`Py_tp_flags`](https://docs.python.org/3/c-api/type.html#c.Py_tp_flags "Py_tp_flags")
    
*   [`Py_tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_free "Py_tp_free")
    
*   [`Py_tp_getattr`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_getattr "Py_tp_getattr")
    
*   [`Py_tp_getattro`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_getattro "Py_tp_getattro")
    
*   [`Py_tp_getset`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_getset "Py_tp_getset")
    
*   [`Py_tp_hash`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_hash "Py_tp_hash")
    
*   [`Py_tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_init "Py_tp_init")
    
*   [`Py_tp_is_gc`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_is_gc "Py_tp_is_gc")
    
*   [`Py_tp_itemsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_itemsize "Py_tp_itemsize")
    
*   [`Py_tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_iter "Py_tp_iter")
    
*   [`Py_tp_iternext`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_iternext "Py_tp_iternext")
    
*   [`Py_tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_members "Py_tp_members")
    
*   [`Py_tp_metaclass`](https://docs.python.org/3/c-api/type.html#c.Py_tp_metaclass "Py_tp_metaclass")
    
*   [`Py_tp_methods`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_methods "Py_tp_methods")
    
*   [`Py_tp_module`](https://docs.python.org/3/c-api/type.html#c.Py_tp_module "Py_tp_module")
    
*   [`Py_tp_name`](https://docs.python.org/3/c-api/type.html#c.Py_tp_name "Py_tp_name")
    
*   [`Py_tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_new "Py_tp_new")
    
*   [`Py_tp_repr`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_repr "Py_tp_repr")
    
*   [`Py_tp_richcompare`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_richcompare "Py_tp_richcompare")
    
*   [`Py_tp_setattr`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_setattr "Py_tp_setattr")
    
*   [`Py_tp_setattro`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_setattro "Py_tp_setattro")
    
*   [`Py_tp_slots`](https://docs.python.org/3/c-api/type.html#c.Py_tp_slots "Py_tp_slots")
    
*   [`Py_tp_str`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_str "Py_tp_str")
    
*   [`Py_tp_token`](https://docs.python.org/3/c-api/type.html#c.Py_tp_token "Py_tp_token")
    
*   [`Py_tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_traverse "Py_tp_traverse")
    
*   [`Py_tp_vectorcall`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_vectorcall "Py_tp_vectorcall")
    
*   `Py_uintptr_t`
    
*   [`allocfunc`](https://docs.python.org/3/c-api/typeobj.html#c.allocfunc "allocfunc")
    
*   [`binaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.binaryfunc "binaryfunc")
    
*   [`descrgetfunc`](https://docs.python.org/3/c-api/typeobj.html#c.descrgetfunc "descrgetfunc")
    
*   [`descrsetfunc`](https://docs.python.org/3/c-api/typeobj.html#c.descrsetfunc "descrsetfunc")
    
*   [`destructor`](https://docs.python.org/3/c-api/typeobj.html#c.destructor "destructor")
    
*   [`getattrfunc`](https://docs.python.org/3/c-api/typeobj.html#c.getattrfunc "getattrfunc")
    
*   [`getattrofunc`](https://docs.python.org/3/c-api/typeobj.html#c.getattrofunc "getattrofunc")
    
*   [`getbufferproc`](https://docs.python.org/3/c-api/typeobj.html#c.getbufferproc "getbufferproc")
    
*   [`getiterfunc`](https://docs.python.org/3/c-api/typeobj.html#c.getiterfunc "getiterfunc")
    
*   [`getter`](https://docs.python.org/3/c-api/structures.html#c.getter "getter")
    
*   [`hashfunc`](https://docs.python.org/3/c-api/typeobj.html#c.hashfunc "hashfunc")
    
*   [`initproc`](https://docs.python.org/3/c-api/typeobj.html#c.initproc "initproc")
    
*   [`inquiry`](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry")
    
*   [`iternextfunc`](https://docs.python.org/3/c-api/typeobj.html#c.iternextfunc "iternextfunc")
    
*   [`lenfunc`](https://docs.python.org/3/c-api/typeobj.html#c.lenfunc "lenfunc")
    
*   [`newfunc`](https://docs.python.org/3/c-api/typeobj.html#c.newfunc "newfunc")
    
*   [`objobjargproc`](https://docs.python.org/3/c-api/typeobj.html#c.objobjargproc "objobjargproc")
    
*   [`objobjproc`](https://docs.python.org/3/c-api/typeobj.html#c.objobjproc "objobjproc")
    
*   [`releasebufferproc`](https://docs.python.org/3/c-api/typeobj.html#c.releasebufferproc "releasebufferproc")
    
*   [`reprfunc`](https://docs.python.org/3/c-api/typeobj.html#c.reprfunc "reprfunc")
    
*   [`richcmpfunc`](https://docs.python.org/3/c-api/typeobj.html#c.richcmpfunc "richcmpfunc")
    
*   [`setattrfunc`](https://docs.python.org/3/c-api/typeobj.html#c.setattrfunc "setattrfunc")
    
*   [`setattrofunc`](https://docs.python.org/3/c-api/typeobj.html#c.setattrofunc "setattrofunc")
    
*   [`setter`](https://docs.python.org/3/c-api/structures.html#c.setter "setter")
    
*   [`ssizeargfunc`](https://docs.python.org/3/c-api/typeobj.html#c.ssizeargfunc "ssizeargfunc")
    
*   [`ssizeobjargproc`](https://docs.python.org/3/c-api/typeobj.html#c.ssizeobjargproc "ssizeobjargproc")
    
*   `ssizessizeargfunc`
    
*   `ssizessizeobjargproc`
    
*   `symtable`
    
*   [`ternaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.ternaryfunc "ternaryfunc")
    
*   [`traverseproc`](https://docs.python.org/3/c-api/gcsupport.html#c.traverseproc "traverseproc")
    
*   [`unaryfunc`](https://docs.python.org/3/c-api/typeobj.html#c.unaryfunc "unaryfunc")
    
*   [`vectorcallfunc`](https://docs.python.org/3/c-api/call.html#c.vectorcallfunc "vectorcallfunc")
    
*   [`visitproc`](https://docs.python.org/3/c-api/gcsupport.html#c.visitproc "visitproc")
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [C API and ABI Stability](https://docs.python.org/3/c-api/stable.html#)
    *   [Unstable C API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
        
    *   [Stable Application Binary Interfaces](https://docs.python.org/3/c-api/stable.html#stable-application-binary-interfaces)
        *   [Compiling for Stable ABI](https://docs.python.org/3/c-api/stable.html#compiling-for-stable-abi)
            
        *   [Stable ABI Scope and Performance](https://docs.python.org/3/c-api/stable.html#stable-abi-scope-and-performance)
            
        *   [Stable ABI Caveats](https://docs.python.org/3/c-api/stable.html#stable-abi-caveats)
            
    *   [Platform Considerations](https://docs.python.org/3/c-api/stable.html#platform-considerations)
        
    *   [ABI Checking](https://docs.python.org/3/c-api/stable.html#abi-checking)
        
    *   [Contents of Limited API](https://docs.python.org/3/c-api/stable.html#contents-of-limited-api)
        

#### Previous topic

[Introduction](https://docs.python.org/3/c-api/intro.html "previous chapter")

#### Next topic

[The Very High Level Layer](https://docs.python.org/3/c-api/veryhigh.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=C+API+and+ABI+Stability&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fstable.html&pagesource=c-api%2Fstable.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/stable.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/veryhigh.html "The Very High Level Layer")
     |
*   [previous](https://docs.python.org/3/c-api/intro.html "Introduction")
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
*   [C API and ABI Stability](https://docs.python.org/3/c-api/stable.html)
    
*    
    
    |
*   Theme Auto Light Dark |