### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/slots.html "Definition slots")
     |
*   [previous](https://docs.python.org/3/c-api/exceptions.html "Exception Handling")
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
*   [Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Defining extension modules[¶](https://docs.python.org/3/c-api/extension-modules.html#defining-extension-modules "Link to this heading")

========================================================================================================================================

A C extension for CPython is a shared library (for example, a `.so` file on Linux, `.pyd` DLL on Windows), which is loadable into the Python process (for example, it is compiled with compatible compiler settings), and which exports an _export hook_ function (or an old-style [initialization function](https://docs.python.org/3/c-api/extension-modules.html#extension-pyinit)
).

To be importable by default (that is, by [`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader "importlib.machinery.ExtensionFileLoader")
), the shared library must be available on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
, and must be named after the module name plus an extension listed in [`importlib.machinery.EXTENSION_SUFFIXES`](https://docs.python.org/3/library/importlib.html#importlib.machinery.EXTENSION_SUFFIXES "importlib.machinery.EXTENSION_SUFFIXES")
.

Note

Building, packaging and distributing extension modules is best done with third-party tools, and is out of scope of this document. One suitable tool is Setuptools, whose documentation can be found at [https://setuptools.pypa.io/en/latest/setuptools.html](https://setuptools.pypa.io/en/latest/setuptools.html)
.

Extension export hook[¶](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

Added in version 3.15: Support for the `PyModExport__<name>_` export hook was added in Python 3.15. The older way of defining modules is still available: consult either the [PyInit function](https://docs.python.org/3/c-api/extension-modules.html#extension-pyinit)
 section or earlier versions of this documentation if you plan to support earlier Python versions.

The export hook must be an exported function with the following signature:

[PySlot](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 \*PyModExport\_modulename(void)[¶](https://docs.python.org/3/c-api/extension-modules.html#c.PyModExport_modulename "Link to this definition")
  

For modules with ASCII-only names, the [export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
 must be named `PyModExport__<name>_`, with `<name>` replaced by the module’s name.

For non-ASCII module names, the export hook must instead be named `PyModExportU__<name>_` (note the `U`), with `<name>` encoded using Python’s _punycode_ encoding with hyphens replaced by underscores. In Python:

Copy

def hook\_name(name):
    try:
        suffix \= b'\_' + name.encode('ascii')
    except UnicodeEncodeError:
        suffix \= b'U\_' + name.encode('punycode').replace(b'-', b'\_')
    return b'PyModExport' + suffix

The export hook returns an array of [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 entries, terminated by an entry with a slot ID of `0`. These slots describe how the module should be created and initialized.

This array must remain valid and constant until interpreter shutdown. Typically, it should use `static` storage. Prefer using the [`Py_mod_create`](https://docs.python.org/3/c-api/module.html#c.Py_mod_create "Py_mod_create")
 and [`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
 slots for any dynamic behavior.

The export hook may return `NULL` with an exception set to signal failure.

It is recommended to define the export hook function using a helper macro:

PyMODEXPORT\_FUNC[¶](https://docs.python.org/3/c-api/extension-modules.html#c.PyMODEXPORT_FUNC "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Declare an extension module export hook. This macro:

*   specifies the [PySlot](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
    \* return type,
    
*   adds any special linkage declarations required by the platform, and
    
*   for C++, declares the function as `extern "C"`.
    

For example, a module called `spam` would be defined like this:

PyABIInfo\_VAR(abi\_info);

static PySlot spam\_slots\[\] \= {
    PySlot\_STATIC\_DATA(Py\_mod\_abi, &abi\_info),
    PySlot\_STATIC\_DATA(Py\_mod\_name, "spam"),
    PySlot\_FUNC(Py\_mod\_exec, spam\_init\_function),
    ...
    PySlot\_END
};

PyMODEXPORT\_FUNC
PyModExport\_spam(void)
{
    return spam\_slots;
}

The export hook is typically the only non-`static` item defined in the module’s C source.

The hook should be kept short. If it does more than `return` a static array, several caveats apply:

*   If you need to use any Python C API, it is recommended to call [`PyABIInfo_Check()`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_Check "PyABIInfo_Check")
     first to raise an exception, rather than crash, in common cases of ABI mismatch.
    
*   Code in the export hook must never rely on the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
    : [free-threaded builds](https://docs.python.org/3/glossary.html#term-free-threaded-build)
     of Python can only check the [`Py_mod_gil`](https://docs.python.org/3/c-api/module.html#c.Py_mod_gil "Py_mod_gil")
     slot (or the lack of it) after the hook returns,
    
*   Similarly, the hook may be called in any subinterpreter, since the [`Py_mod_multiple_interpreters`](https://docs.python.org/3/c-api/module.html#c.Py_mod_multiple_interpreters "Py_mod_multiple_interpreters")
     slot (or lack of it) is only checked after the hook returns.
    

For example:

PyMODEXPORT\_FUNC
PyModExport\_modulename(void)
{
   if (PyABIInfo\_Check(&abi\_info, "modulename") < 0) {
      /\* ABI mismatch. It's not safe to examine the raised exception. \*/
      return NULL;
   }

   /\* use Python API (as little as possible); don't rely on GIL \*/

   return modulename\_slots;
}

Note

It is possible to export multiple modules from a single shared library by defining multiple export hooks. However, importing them requires a custom importer or suitably named copies/links of the extension file, because Python’s import machinery only finds the function corresponding to the filename. See the [Multiple modules in one library](https://peps.python.org/pep-0489/#multiple-modules-in-one-library)
 section in [**PEP 489**](https://peps.python.org/pep-0489/)
 for details.

Multi-phase initialization[¶](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

The process of creating an extension module follows several phases:

*   Python finds and calls the export hook to get information on how to create the module.
    
*   Before any substantial code is executed, Python can determine which capabilities the module supports, and it can adjust the environment or refuse loading an incompatible extension. Slots like [`Py_mod_abi`](https://docs.python.org/3/c-api/module.html#c.Py_mod_abi "Py_mod_abi")
    , [`Py_mod_gil`](https://docs.python.org/3/c-api/module.html#c.Py_mod_gil "Py_mod_gil")
     and [`Py_mod_multiple_interpreters`](https://docs.python.org/3/c-api/module.html#c.Py_mod_multiple_interpreters "Py_mod_multiple_interpreters")
     influence this step.
    
*   By default, Python itself then creates the module object – that is, it does the equivalent of calling [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
     when creating an object. This step can be overridden using the [`Py_mod_create`](https://docs.python.org/3/c-api/module.html#c.Py_mod_create "Py_mod_create")
     slot.
    
*   Python sets initial module attributes like [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
     and [`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")
    , and inserts the module object into [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")
    .
    
*   Afterwards, the module object is initialized in an extension-specific way – the equivalent of [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
     when creating an object, or of executing top-level code in a Python-language module. The behavior is specified using the [`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
     slot.
    

This is called _multi-phase initialization_ to distinguish it from the legacy (but still supported) [single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#single-phase-initialization)
, where an initialization function returns a fully constructed module.

Changed in version 3.5: Added support for multi-phase initialization ([**PEP 489**](https://peps.python.org/pep-0489/)
).

Multiple module instances[¶](https://docs.python.org/3/c-api/extension-modules.html#multiple-module-instances "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

By default, extension modules are not singletons. For example, if the [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")
 entry is removed and the module is re-imported, a new module object is created and, typically, populated with fresh method and type objects. The old module is subject to normal garbage collection. This mirrors the behavior of pure-Python modules.

Additional module instances may be created in [sub-interpreters](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
 or after Python runtime reinitialization ([`Py_Finalize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Finalize "Py_Finalize")
 and [`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
). In these cases, sharing Python objects between module instances would likely cause crashes or undefined behavior.

To avoid such issues, each instance of an extension module should be _isolated_: changes to one instance should not implicitly affect the others, and all state owned by the module, including references to Python objects, should be specific to a particular module instance. See [Isolating Extension Modules](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extensions-howto)
 for more details and a practical guide.

A simpler way to avoid these issues is [raising an error on repeated initialization](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extensions-optout)
.

All modules are expected to support [sub-interpreters](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
, or otherwise explicitly signal a lack of support. This is usually achieved by isolation or blocking repeated initialization, as above. A module may also be limited to the main interpreter using the [`Py_mod_multiple_interpreters`](https://docs.python.org/3/c-api/module.html#c.Py_mod_multiple_interpreters "Py_mod_multiple_interpreters")
 slot.

`PyInit` function[¶](https://docs.python.org/3/c-api/extension-modules.html#pyinit-function "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: This functionality will not get new features, but there are no plans to remove it.

Instead of [`PyModExport_modulename()`](https://docs.python.org/3/c-api/extension-modules.html#c.PyModExport_modulename "PyModExport_modulename")
, an extension module can define an older-style _initialization function_ with the signature:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyInit\_modulename(void)[¶](https://docs.python.org/3/c-api/extension-modules.html#c.PyInit_modulename "Link to this definition")
  

Its name should be `PyInit__<name>_`, with `<name>` replaced by the name of the module. For non-ASCII module names, use `PyInitU__<name>_` instead, with `<name>` encoded in the same way as for the [export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
 (that is, using Punycode with underscores).

If a module exports both `PyInit__<name>_` and `PyModExport__<name>_`, the `PyInit__<name>_` function is ignored.

Like with [`PyMODEXPORT_FUNC`](https://docs.python.org/3/c-api/extension-modules.html#c.PyMODEXPORT_FUNC "PyMODEXPORT_FUNC")
, it is recommended to define the initialization function using a helper macro:

PyMODINIT\_FUNC[¶](https://docs.python.org/3/c-api/extension-modules.html#c.PyMODINIT_FUNC "Link to this definition")
  

Declare an extension module initialization function. This macro:

*   specifies the [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
    \* return type,
    
*   adds any special linkage declarations required by the platform, and
    
*   for C++, declares the function as `extern "C"`.
    

Normally, the initialization function (`PyInit_modulename`) returns a [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 instance with non-`NULL` [`m_slots`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_slots "PyModuleDef.m_slots")
. This allows Python to use [multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
.

Before it is returned, the `PyModuleDef` instance must be initialized using the following function:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModuleDef\_Init([PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def)[¶](https://docs.python.org/3/c-api/extension-modules.html#c.PyModuleDef_Init "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

Ensure a module definition is a properly initialized Python object that correctly reports its type and a reference count.

Return _def_ cast to `PyObject*`, or `NULL` if an error occurred.

Calling this function is required before returning a [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 from a module initialization function. It should not be used in other contexts.

Note that Python assumes that `PyModuleDef` structures are statically allocated. This function may return either a new reference or a borrowed one; this reference must not be released.

Added in version 3.5.

For example, a module called `spam` would be defined like this:

static struct PyModuleDef spam\_module \= {
    .m\_base \= PyModuleDef\_HEAD\_INIT,
    .m\_name \= "spam",
    ...
};

PyMODINIT\_FUNC
PyInit\_spam(void)
{
    return PyModuleDef\_Init(&spam\_module);
}

### Legacy single-phase initialization[¶](https://docs.python.org/3/c-api/extension-modules.html#legacy-single-phase-initialization "Link to this heading")

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: Single-phase initialization is a legacy mechanism to initialize extension modules, with known drawbacks and design flaws. Extension module authors are encouraged to use multi-phase initialization instead.

However, there are no plans to remove support for it.

In single-phase initialization, the old-style [initialization function](https://docs.python.org/3/c-api/extension-modules.html#extension-pyinit)
 (`PyInit_modulename`) should create, populate and return a module object. This is typically done using [`PyModule_Create()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Create "PyModule_Create")
 and functions like [`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef")
.

Single-phase initialization differs from the [default](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
 in the following ways:

*   Single-phase modules with [`PyModuleDef.m_size`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_size "PyModuleDef.m_size")
     set to -1 are, or rather _contain_, “singletons”.
    
    When such a module is first initialized, Python saves the contents of the module’s `__dict__` (that is, typically, the module’s functions and types).
    
    For subsequent imports, Python does not call the initialization function again. Instead, it creates a new module object with a new `__dict__`, and copies the saved contents to it. Modules are matched to the saved contents by a (_module\_name_, _file\_name_) tuple where:
    
    *   _module\_name_ is the module’s full dotted name, taken from [`ModuleSpec.name`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.name "importlib.machinery.ModuleSpec.name")
         (or the equivalent argument of the importing function). Note that names that the initialization function uses to create the module (for example, [`PyModuleDef.m_name`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_name "PyModuleDef.m_name")
        ) are not taken into account.
        
    *   _file\_name_ is the extension’s file name. It is unset for modules not loaded from a file, such as built-ins and modules added with [`PyImport_CreateModuleFromInitfunc()`](https://docs.python.org/3/c-api/import.html#c.PyImport_CreateModuleFromInitfunc "PyImport_CreateModuleFromInitfunc")
         or [`PyImport_AppendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AppendInittab "PyImport_AppendInittab")
        .
        
    
    As part of the first initialization, Python also adds the module to [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")
     under its name. For example, given a single-phase module `_testsinglephase` [\[1\]](https://docs.python.org/3/c-api/extension-modules.html#testsinglephase)
     that defines a function `sum` and an exception class `error`:
    
    Copy
    
    \>>> import sys
    \>>> import \_testsinglephase as one
    \>>> del sys.modules\['\_testsinglephase'\]
    \>>> import \_testsinglephase as two
    \>>> one is two
    False
    \>>> one.\_\_dict\_\_ is two.\_\_dict\_\_
    False
    \>>> one.sum is two.sum
    True
    \>>> one.error is two.error
    True
    
    The exact behavior should be considered a CPython implementation detail.
    
*   For single-phase modules with non-negative [`PyModuleDef.m_size`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_size "PyModuleDef.m_size")
    , Python may cache a pointer to the initialization function under the (_module\_name_, _file\_name_) key as for `m_size == -1`.
    
    Subsequent imports that specify a different initialization function (for example, using [`PyImport_CreateModuleFromInitfunc()`](https://docs.python.org/3/c-api/import.html#c.PyImport_CreateModuleFromInitfunc "PyImport_CreateModuleFromInitfunc")
    ) may call either the cached function or the provided “new” one.
    
    The exact behavior should again be considered a CPython implementation detail.
    
*   To work around the fact that `PyInit_modulename` does not take a _spec_ argument, some state of the import machinery is saved and applied to the first suitable module created during the `PyInit_modulename` call. Specifically, when a sub-module is imported, this mechanism prepends the parent package name to the name of the module.
    
    A single-phase `PyInit_modulename` function should create “its” module object as soon as possible, before any other module objects can be created.
    
*   Non-ASCII module names (`PyInitU_modulename`) are not supported.
    
*   Single-phase modules support module lookup functions like [`PyState_FindModule()`](https://docs.python.org/3/c-api/module.html#c.PyState_FindModule "PyState_FindModule")
    .
    
*   The module’s [`PyModuleDef.m_slots`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_slots "PyModuleDef.m_slots")
     must be NULL.
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html#)
    *   [Extension export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
        
    *   [Multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
        
    *   [Multiple module instances](https://docs.python.org/3/c-api/extension-modules.html#multiple-module-instances)
        
    *   [`PyInit` function](https://docs.python.org/3/c-api/extension-modules.html#pyinit-function)
        *   [Legacy single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#legacy-single-phase-initialization)
            

#### Previous topic

[Exception Handling](https://docs.python.org/3/c-api/exceptions.html "previous chapter")

#### Next topic

[Definition slots](https://docs.python.org/3/c-api/slots.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Defining+extension+modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fextension-modules.html&pagesource=c-api%2Fextension-modules.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/extension-modules.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/slots.html "Definition slots")
     |
*   [previous](https://docs.python.org/3/c-api/exceptions.html "Exception Handling")
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
*   [Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html)
    
*    
    
    |
*   Theme Auto Light Dark |