### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/remote_debugging.html "Remote debugging attachment protocol")
     |
*   [previous](https://docs.python.org/3/howto/free-threading-extensions.html "C API Extension Support for Free Threading")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [Migrating to Stable ABI for free threading (`abi3t`)](https://docs.python.org/3/howto/abi3t-migration.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Migrating to Stable ABI for free threading (`abi3t`)[¶](https://docs.python.org/3/howto/abi3t-migration.html#migrating-to-stable-abi-for-free-threading-abi3t "Link to this heading")

======================================================================================================================================================================================

Starting with the 3.15 release, CPython supports a variant of the Stable ABI that supports [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 Python: the Stable ABI for Free-Threaded Builds, or `abi3t` for short. This document describes how to adapt C API extensions to support free threading.

Why do this[¶](https://docs.python.org/3/howto/abi3t-migration.html#why-do-this "Link to this heading")

--------------------------------------------------------------------------------------------------------

The typical reason to use the Stable ABI is to reduce the number of artifacts that you need to build and distribute for each version of your library.

Without the Stable ABI, you must build a separate shared library, and typically a _wheel_ distribution, for each feature version of CPython you wish to support. For example, each tag in the following table represents a separate library/wheel:

| CPython version | Non-free-threaded | Free-threaded |
| --- | --- | --- |
| 3.12 | `cpython-312` | —   |
| 3.13 | `cpython-313` | `cpython-313t` |
| 3.14 | `cpython-314` | `cpython-314t` |
| 3.15 | `cpython-315` | `cpython-315t` |
| 3.16 | `cpython-316` | `cpython-316t` |
| Later versions | `cpython-3_XX_` | `cpython-3_XX_t` |

That’s a lot of builds, especially when multiplied by the number of supported platforms.

With the Stable ABI (`abi3`, introduced in CPython 3.2), a single extension (per platform) can cover all _non-free-threaded_ builds of CPython:

| CPython version | Non-free-threaded | Free-threaded |
| --- | --- | --- |
| 3.12 | `abi3` | —   |
| 3.13 | `cpython-313t` |
| 3.14 | `cpython-314t` |
| 3.15 | `cpython-315t` |
| 3.16 | `cpython-316t` |
| Later versions | `cpython-3_XX_t` |

The Stable ABI for free-threaded builds (`abi3t`), introduced in CPython 3.15, does the same for free-threaded builds. And it’s compatible with non-free-threaded ones as well:

| CPython version | Non-free-threaded | Free-threaded |
| --- | --- | --- |
| 3.12 | `abi3` \* | —   |
| 3.13 | `cpython-313t` |
| 3.14 | `cpython-314t` |
| 3.15 | `abi3t` |     |
| 3.16 |
| Later versions |

\* (As above, the `abi3` extension is compatible with all non-free-threaded builds; even the 3.15+ ones that this table “attributes” to `abi3t`.)

### Why _not_ do this[¶](https://docs.python.org/3/howto/abi3t-migration.html#why-not-do-this "Link to this heading")

There are two main downsides to the Stable ABI.

First, your extension may become slower, since the Stable ABI prioritizes compatibility over performance. The difference is usually not noticeable, and often can be mitigated by using the same source to build both a Stable ABI build and a few version-specific ones for “tier 1” CPython versions.

Second, not all of the C API is available. Extensions need to be ported to build for the Stable ABI, which may be difficult or, in rare cases, impossible.

Specifically, `abi3t` requires APIs added in CPython 3.15. If you want to build your extension for older versions of CPython from the same source, you have two main options:

*   Use preprocessor conditionals.
    
    When following this guide, use `#ifdef Py_TARGET_ABI3T` blocks whenever you are told to do a change that breaks the build on CPython versions you care about. Keep the pre-existing code in `#else` blocks.
    
    For hand-written C extensions, this approach is reasonable down to CPython 3.12, due to additions introduced in [**PEP 697**](https://peps.python.org/pep-0697/)
    . Keeping compatibility with 3.11 and below may be worth it for code generators (for example, Cython).
    
*   Do not port to `abi3t`, and continue building separate extensions for each version of CPython, until you can drop support for the older versions.
    
    This is a valid approach. Not all extensions need to switch to `abi3t` right now.
    

Prerequisites[¶](https://docs.python.org/3/howto/abi3t-migration.html#prerequisites "Link to this heading")

------------------------------------------------------------------------------------------------------------

This guide assumes that you have an extension written directly in C (or C++), which you want to port to `abi3t`.

If your extension uses a code generator (like Cython) or language binding (like PyO3), it’s best to wait until that tool has support for `abi3t`. If you maintain such a tool, you might be able to adapt the instructions here for your tool.

### Non-free-threaded Stable ABI[¶](https://docs.python.org/3/howto/abi3t-migration.html#non-free-threaded-stable-abi "Link to this heading")

Your extension should support the non-free-threaded Stable ABI (`abi3`). If not, either port it first, or follow this guide but be prepared to fix issues it does not mention.

### Free-threading support[¶](https://docs.python.org/3/howto/abi3t-migration.html#free-threading-support "Link to this heading")

While it’s technically not a hard prerequisite, you will most likely want to prepare your extension for free threading before you port it to `abi3t`. See [C API Extension Support for Free Threading](https://docs.python.org/3/howto/free-threading-extensions.html#freethreading-extensions-howto)
 for instructions.

See also

[Porting Extension Modules to Support Free-Threading](https://py-free-threading.github.io/porting/)
: A community-maintained porting guide for extension authors.

### Isolating extension modules[¶](https://docs.python.org/3/howto/abi3t-migration.html#isolating-extension-modules "Link to this heading")

Your module should use [multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
, and it should either be isolated or limit itself to be loaded at most once per process. If it is not your case, follow [Isolating Extension Modules](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extensions-howto)
 first. (See the [opt-out section](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extensions-optout)
 for a shortcut.)

### Avoiding variable-sized types[¶](https://docs.python.org/3/howto/abi3t-migration.html#avoiding-variable-sized-types "Link to this heading")

If your extension defines variable-sized types (using [`Py_tp_itemsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_itemsize "Py_tp_itemsize")
 or [`PyTypeObject.tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
), it cannot be ported to `abi3t` 3.15.

Setting up the build[¶](https://docs.python.org/3/howto/abi3t-migration.html#setting-up-the-build "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

If you use a build tool, search its documentation for “`abi3t`”, and follow any instructions to select the ABI. For reference, here are direct links for several popular build tools:

*   [meson-python](https://mesonbuild.com/meson-python/how-to-guides/limited-api.html#the-abi3t-stable-abi)
    
*   [scikit-build-core](https://scikit-build-core.readthedocs.io/en/stable/configuration/#customizing-the-output-wheel)
    
*   [Maturin](https://www.maturin.rs/bindings#py_limited_apiabi3)
    

You may want to verify that the tool set the right flag by temporarily adding the following just after `#include <Python.h>`:

#if Py\_TARGET\_ABI3T+0 < 0x30f0000
#error "abi3t define is not set!"
#endif

This should result in a different error than “`abi3t` define is not set”. (If you get no error at all, either the module is already ported or you’re not compiling the code you changed.)

See also

[Building and distributing abi3t extensions](https://py-free-threading.github.io/abi3t/)
: Build configuration and wheel testing examples in the community-maintained Python Free-Threading Guide.

Note

If your build tool doesn’t support `abi3t` yet, set the following macro before including `Python.h`:

#define Py\_TARGET\_ABI3T 0x30f0000

or specify it as a compiler flag, for example:

\-DPy\_TARGET\_ABI3T\=0x30f0000

Once your extension builds with this setting, it will be compatible with CPython 3.15 and above.

If you set this macro manually, you will later need to name and tag the resulting extension manually as well. This is covered in [Tagging and distribution](https://docs.python.org/3/howto/abi3t-migration.html#abi3t-migration-tagging)
 below.

This guide will ask you to make a series of changes. After each one, verify that your extension still builds in the original (non-`abi3t`) configuration, and ideally run tests on all Python versions you support. This will ensure that nothing breaks as you are porting.

Module export hook[¶](https://docs.python.org/3/howto/abi3t-migration.html#module-export-hook "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

Unless you’ve done this step already, your extension module defines a [module initialization function](https://docs.python.org/3/c-api/extension-modules.html#extension-pyinit)
 named `PyInit__<modname>_` (where `modname` is the name of your module). You will need to port it to a [module export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
, `PyModExport__<modname>_`, a feature added in CPython 3.15 in [**PEP 793**](https://peps.python.org/pep-0793/)
.

Your existing init function should look like this (with your own names for `<modname>` and `<moddef>`):

PyMODINIT\_FUNC
PyInit\_<modname\>(void)
{
    return PyModuleDef\_Init(&<moddef\>);
}

If there is some code before the `return`, move it to a [`Py_mod_create`](https://docs.python.org/3/c-api/module.html#c.Py_mod_create "Py_mod_create")
 or [`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
 slot function. See the [PyInit documentation](https://docs.python.org/3/c-api/extension-modules.html#extension-pyinit)
 for related information.

The function references a `PyModuleDef` object (`<moddef>` in the code above). Its definition should be similar to the following, with different values and perhaps some fields unnnamed or left out:

static PyModuleDef <moddef\> \= {
    PyModuleDef\_HEAD\_INIT,
    .m\_name \= "my\_module",
    .m\_doc \= "my docstring",
    .m\_size \= sizeof(my\_state\_struct),
    .m\_methods \= my\_methods,
    .m\_slots \= my\_slots,
    .m\_traverse \= my\_traverse,
    .m\_clear \= my\_clear,
    .m\_free \= my\_free,
};

Remove this definition and the `PyInit` function (or put them in an `#ifndef Py_TARGET_ABI3T` block, to retain backwards compatibility), and replace them with the following:

PyABIInfo\_VAR(abi\_info);

static PySlot my\_slot\_array\[\] \= {
    PySlot\_STATIC\_DATA(Py\_mod\_abi, &abi\_info),
    PySlot\_STATIC\_DATA(Py\_mod\_name, "my\_module"),
    PySlot\_STATIC\_DATA(Py\_mod\_doc, "my docstring"),
    PySlot\_SIZE(Py\_mod\_state\_size, sizeof(my\_state\_struct)),
    PySlot\_STATIC\_DATA(Py\_mod\_methods, my\_methods),
    PySlot\_STATIC\_DATA(Py\_mod\_slots, my\_slots),
    PySlot\_FUNC(Py\_mod\_state\_traverse, my\_traverse),
    PySlot\_FUNC(Py\_mod\_state\_clear, my\_clear),
    PySlot\_FUNC(Py\_mod\_state\_free, my\_free),
    PySlot\_END
};

PyMODEXPORT\_FUNC
PyModExport\_<modname\>(void)
{
    return my\_slot\_array;
}

Leave out any fields that were missing (except the new [`Py_mod_abi`](https://docs.python.org/3/c-api/module.html#c.Py_mod_abi "Py_mod_abi")
), and substitute your own values.

See the [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 and [export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
 documentation for details on this API.

As in the example, your `PyModExport_` function should _only_ return a pointer to static data. If you cannot avoid additional code, refer to the [caveats in PyModExport documentation](https://docs.python.org/3/c-api/extension-modules.html#pymodexport-api-caveats)
.

Note

When building for Windows using the [Setuptools](https://setuptools.pypa.io/)
 build tool, removing the `PyInit__<modname>_` function may result in the linker error `LINK : error LNK2001: unresolved external symbol PyInit__<modname>_`. This is caused by Setuptools passing an `/EXPORT` linker flag, which is redundant since Python 3.15 (see [gh-141671](https://github.com/python/cpython/issues/141671)
). A workaround is to add a dummy `PyInit__<modname>_` function to your code. Python 3.15+ will never call this function if `PyModExport__<modname>_` is present, so it can always fail:

// Workaround for https://github.com/pypa/distutils/issues/387
PyMODINIT\_FUNC
PyInit\_<modname\>(void)
{
    PyErr\_SetString(PyExc\_SystemError,
                    "PyInit\_\* called for module with PyModExport\_\*");
    return NULL;
}

(This issue is present in Setuptools 84.0.0; it might be fixed in newer versions.)

### Existing slots[¶](https://docs.python.org/3/howto/abi3t-migration.html#existing-slots "Link to this heading")

If you have a `Py_mod_slots` slot, check the array it refers to. It should be a [`PyModuleDef_Slot`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot "PyModuleDef_Slot")
 array like the following:

static PyObject \*create\_module(PyObject \*spec, PyModuleDef \*def) { ... }
static int my\_first\_module\_exec(PyObject \*module) { ... }
static int my\_second\_module\_exec(PyObject \*module) { ... }

static PyModuleDef\_Slot my\_slots\[\] \= {
   {Py\_mod\_gil, Py\_MOD\_GIL\_NOT\_USED},
   {Py\_mod\_multiple\_interpreters, Py\_MOD\_PER\_INTERPRETER\_GIL\_SUPPORTED},
   {Py\_mod\_create, create\_module},
   {Py\_mod\_exec, my\_first\_module\_exec},
   {Py\_mod\_exec, my\_second\_module\_exec},
   {0, NULL}
};

#### `Py_mod_create`[¶](https://docs.python.org/3/howto/abi3t-migration.html#py-mod-create "Link to this heading")

If you have a [`Py_mod_create`](https://docs.python.org/3/c-api/module.html#c.Py_mod_create "Py_mod_create")
 entry, make sure the function can be called with `NULL` as its second argument (instead of the [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
, which you are removing). Often, this argument isn’t used at all; you can check by renaming it:

static PyObject \*create\_module(PyObject \*spec, PyModuleDef \*\_unused) { ... }

If the argument is used, find a different way to pass in the data. Commonly, the information is static and you can refer to it directly. (If you’re reusing a single function for several different modules, consider defining several functions instead.)

#### Multiple `Py_mod_exec`[¶](https://docs.python.org/3/howto/abi3t-migration.html#multiple-py-mod-exec "Link to this heading")

If you have _more than one_ [`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
 entry, consolidate them: create a new function that calls the others, and replace existing slots with it.

static int my\_module\_exec(PyObject \*module) {
   if (my\_first\_module\_exec(module) < 0) return \-1;
   if (my\_second\_module\_exec(module) < 0) return \-1;
   return 0;
}

static PyModuleDef\_Slot my\_slots\[\] \= {
   ...
   /\* (remove other Py\_mod\_exec slots) \*/
   ...
   {Py\_mod\_exec, my\_module\_exec},
   {0, NULL}
};

If the functions aren’t used elsewhere, you can combine their bodies instead.

#### Merging slot arrays[¶](https://docs.python.org/3/howto/abi3t-migration.html#merging-slot-arrays "Link to this heading")

Optionally, when you break compatibility with Python 3.14, you may clean up the code by moving slots into the [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 array, and converting the definitions to [`PySlot_DATA`](https://docs.python.org/3/c-api/slots.html#c.PySlot_DATA "PySlot_DATA")
 and [`PySlot_FUNC`](https://docs.python.org/3/c-api/slots.html#c.PySlot_FUNC "PySlot_FUNC")
:

static PySlot my\_slot\_array\[\] \= {
    ...
    PySlot\_DATA(Py\_mod\_gil, Py\_MOD\_GIL\_NOT\_USED),
    PySlot\_DATA(Py\_mod\_multiple\_interpreters,
         Py\_MOD\_PER\_INTERPRETER\_GIL\_SUPPORTED),
    PySlot\_FUNC(Py\_mod\_create, create\_module),
    PySlot\_FUNC(Py\_mod\_exec, my\_module\_exec),
    PySlot\_END
};

If you do this, delete the original [`PyModuleDef_Slot`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot "PyModuleDef_Slot")
 array and its `Py_mod_slots` entry.

### Associated `PyModuleDef`[¶](https://docs.python.org/3/howto/abi3t-migration.html#associated-pymoduledef "Link to this heading")

Since the new API does not use a `PyModuleDef` structure, a definition will not be associated with the resulting module. This changes the behavior of the following functions:

*   [`PyModule_GetDef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetDef "PyModule_GetDef")
    
*   [`PyType_GetModuleByDef()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByDef "PyType_GetModuleByDef")
    

Check your code for these. If you do not use them, you can skip this section.

These functions are typically used for two purposes:

1.  To get the definition the module was created with. This is no longer possible using the new API. Modules no longer keep a reference to the definition, so you will need to figure out a different way to pass the relevant data around.
    

2.  To check if a given module object is “yours”. This use case is now served by [module tokens](https://docs.python.org/3/c-api/module.html#ext-module-token)
     – opaque pointers that identify a module. To use a token, declare (or reuse) a unique static variable, for example:
    
    static char my\_token;
    
    and add a pointer to it in a new entry to your module’s `PySlot` array:
    
    static PySlot my\_slot\_array\[\] \= {
       ...
       PySlot\_STATIC\_DATA(Py\_mod\_token, &my\_token),   PySlot\_END
    };
    
    Then, switch from [`PyModule_GetDef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetDef "PyModule_GetDef")
     calls such as:
    
    PyModuleDef \*def \= PyModule\_GetDef(module);
    
    to [`PyModule_GetToken()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetToken "PyModule_GetToken")
     (which uses an output argument and may fail with an exception):
    
    void \*token;
    if (PyModule\_GetToken(module, &token) < 0) {
        /\* handle error \*/
    }
    
    and from [`PyType_GetModuleByDef()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByDef "PyType_GetModuleByDef")
     calls such as:
    
    PyObject \*module \= PyType\_GetModuleByDef(type, my\_def);
    /\* handle error; use module \*/
    
    to [`PyType_GetModuleByToken()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByToken "PyType_GetModuleByToken")
     (which returns a strong reference):
    
    PyObject \*module \= PyType\_GetModuleByToken(type, &my\_token);
    /\* handle error; use module \*/
    Py\_XDECREF(module);
    

`PyObject` opaqueness[¶](https://docs.python.org/3/howto/abi3t-migration.html#pyobject-opaqueness "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

The [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 and [`PyVarObject`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 structures are opaque in `abi3t`.

Accessing their members is prohibited. If you do this, switch to getter/setter functions mentioned in their documentation:

*   [`PyObject.ob_type`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_type "PyObject.ob_type")
    
*   [`PyObject.ob_refcnt`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_refcnt "PyObject.ob_refcnt")
    
*   [`PyVarObject.ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
    

Also, the _size_ of the [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 structures is unknown to the compiler. It can – and _does_ – change between different CPython builds.

Note

While the size is available at runtime (for example as `sys.getsizeof(object())` in Python code), you should resist the temptation to calculate pointer offsets from it. The object memory layout is subject to change in future `abi3t` implementations.

### Custom type definitions[¶](https://docs.python.org/3/howto/abi3t-migration.html#custom-type-definitions "Link to this heading")

Since `PyObject` is opaque, the traditional way of defining custom types no longer works:

typedef struct {
   PyObject\_HEAD  // expands to \`PyObject ob\_base;\` which has unknown size

   int my\_data;
} CustomObject;

static PyType\_Spec CustomType\_spec \= {
   ...
   .basicsize \= sizeof(CustomObject),
   ...
};

Most likely, all your class definitions, _and_ all code that accesses your classes’ data, will need to be rewritten. This will probably be the biggest change you need to support `abi3t`.

For each such type, instead of defining a `struct` for the entire instance, define one with only the “additional” fields – ones specific to your class, not its superclasses:

typedef struct {
   int my\_data;
} CustomObjectData;

Change the name. Almost all code that uses the struct will need to change (notably, pointers to the new structure cannot be cast to/from `PyObject*`), and changing the name will highlight the usages as compiler errors. (If you use `typeof`, C++ `auto`, or similar ways to avoid typing the type name, this won’t work. Be extra careful, and consider running tools to detect undefined behavior.)

Then, to create the class, use _negative_ `basicsize` to indicate “extra” storage space rather than _total_ instance size:

static PyType\_Spec CustomType\_spec \= {
   ...
   .basicsize \= \-sizeof(CustomObjectData), /\* note the minus sign \*/
   ...
};

If you use [`Py_tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_members "Py_tp_members")
, set the [`Py_RELATIVE_OFFSET`](https://docs.python.org/3/c-api/structures.html#c.Py_RELATIVE_OFFSET "Py_RELATIVE_OFFSET")
 flag on each member and specify the [`offset`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.offset "PyMemberDef.offset")
 relative to your new struct.

### Custom type data access[¶](https://docs.python.org/3/howto/abi3t-migration.html#custom-type-data-access "Link to this heading")

Then comes the hard part: in all code that needs to access this struct, you will need an additional [`PyObject_GetTypeData()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetTypeData "PyObject_GetTypeData")
 call to retrieve a `CustomObjectData *` pointer from `PyObject *`:

PyObject \*obj \= ...;
CustomObjectData \*data \= PyObject\_GetTypeData(obj, cls);

Note that this call requires the _type object_ for your class (`cls`).

If your class is not subclassable (that is, it does not use the [`Py_TPFLAGS_BASETYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_BASETYPE "Py_TPFLAGS_BASETYPE")
 flag), `cls` will be `Py_TYPE(obj)`. Otherwise, **DO NOT USE** `Py_TYPE` with `PyObject_GetTypeData()`: it might return memory reserved to an unrelated subclass! For example, if a user makes a subclass like this:

Copy

class Sub(YourCustomClass):
   \_\_slots\_\_ \= ('a', 'b')

then `Py_TYPE(obj)` is `Sub`, and the underlying memory may look like this:

╭─ PyObject \*obj
│              ╭─ the pointer you want
│              │                    ╭─ PyObject\_GetTypeData(obj, Py\_TYPE(obj))
▼              ▼                    ▼
┌──────────┬───┬────────────────┬───┬─────────────┬───┬─────────────┐
│ PyObject │...│ CustomTypeData │...│ PyObject \*a │...│ PyObject \*b │
└──────────┴───┴────────────────┴───┴─────────────┴───┴─────────────┘

(Ellipses indicate possible padding. Note that this memory layout is not guaranteed: future versions of Python may add different padding or even switch the order of the structures.)

There are two main ways to get the right class:

*   In instance methods, your implementation may use the [`PyCMethod`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod "PyCMethod")
     signature (and the [`METH_METHOD`](https://docs.python.org/3/c-api/structures.html#c.METH_METHOD "METH_METHOD")
     bit in [`PyMethodDef.ml_flags`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_flags "PyMethodDef.ml_flags")
    ), and get the class as the `defining_class` argument.
    
*   Otherwise, give your class a unique static token using the [`Py_tp_token`](https://docs.python.org/3/c-api/type.html#c.Py_tp_token "Py_tp_token")
     slot, and use:
    
    PyTypeObject \*cls;
    if (PyType\_GetBaseByToken(Py\_TYPE(obj), my\_tp\_token, &cls) < 0) {
        /\* handle error \*/
    }
    CustomObjectData \*data \= PyObject\_GetTypeData(obj, cls);
    Py\_DECREF(cls);
    
    Type tokens work similarly to module tokens covered [earlier in this guide](https://docs.python.org/3/howto/abi3t-migration.html#abi3t-migration-module-token)
    .
    

Avoid build-time conditionals[¶](https://docs.python.org/3/howto/abi3t-migration.html#avoid-build-time-conditionals "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

Check your code for API that identifies the version of Python used to _build_ your extension. This no longer corresponds to the Python your extension runs on, so code that uses this information often needs changing. The macros to check for are:

*   [`PY_VERSION_HEX`](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_VERSION_HEX "PY_VERSION_HEX")
    , [`PY_MAJOR_VERSION`](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_MAJOR_VERSION "PY_MAJOR_VERSION")
    , [`PY_MINOR_VERSION`](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_MINOR_VERSION "PY_MINOR_VERSION")
    :
    
    *   to get the run-time version, use [`Py_Version`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_Version "Py_Version")
        ;
        
    *   to determine what C API is available, use [`Py_TARGET_ABI3T`](https://docs.python.org/3/c-api/stable.html#c.Py_TARGET_ABI3T "Py_TARGET_ABI3T")
        . This macro is set to the minimum supported version.
        
*   [`Py_GIL_DISABLED`](https://docs.python.org/3/using/configure.html#c.Py_GIL_DISABLED "Py_GIL_DISABLED")
    : under `abi3t`, this macro is always defined. Code that works with free-threaded Python _should_ also work with the GIL enabled (since the GIL can be enabled at run time), and usually _does_ (unless it, for some reason, requires more than one [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
     at one time).
    

Further code changes[¶](https://docs.python.org/3/howto/abi3t-migration.html#further-code-changes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

If you are still left with compiler errors or warnings, find a way to fix them. Alas, this guide is limited, and cannot cover all possible code changes extensions may need.

If you find a problem that other extension authors might run into, consider [reporting an issue](https://docs.python.org/3/bugs.html#reporting-documentation-bugs)
 (or sending a pull request) for this guide.

It is possible your issue cannot be fixed for the current version of `abi3t`. In that case, reporting it may help it get prioritized for the next version of CPython.

Tagging and distribution[¶](https://docs.python.org/3/howto/abi3t-migration.html#tagging-and-distribution "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

If you are using a build tool with `abi3t` support, your extension is ready, but you might want to check that it was built correctly.

Extensions built with `abi3t` should have the following extension:

*   On Windows: `.pyd` (like any other extension);
    
*   Linux, macOS, and other systems that use the `.so` suffix: `.abi3t.so` (**not** `.cpython-315t.so` or `.abi3.so`). Note that both free-threaded and non-free-threaded builds will load `.abi3t.so` extensions;
    
*   Other systems: consult your distributor, and perhaps update this guide.
    

If you distribute the extension as a _wheel_, use the following tags:

*   Python tag: `cp3_XX_`, where _XX_ is the minimum Python version the extension is built for. (For example, `cp315` if you set `Py_TARGET_ABI3T` to `0x30f0000`. See [Compiling for Stable ABI](https://docs.python.org/3/c-api/stable.html#abi3-compiling)
     for more values.)
    
*   ABI tag: `abi3.abi3t`. This is a _compressed tag set_ that indicates support for both non-free-threaded and free-threaded builds.
    

For example, the wheel filename may look like this:

myproject-1.0-cp315-abi3.abi3t-macosx\_11\_0\_arm64.whl

See also

[Platform Compatibility Tags](https://packaging.python.org/en/latest/specifications/platform-compatibility-tags/)
 in the PyPA package distribution metadata.

If the filename or tags are incorrect, fix them.

Testing[¶](https://docs.python.org/3/howto/abi3t-migration.html#testing "Link to this heading")

------------------------------------------------------------------------------------------------

Note that when you build an extension compatible with multiple versions of CPython, you should always _test_ it with each version it supports (for example, 3.15, 3.16, and so on). The Stable ABI only guarantees _ABI_ compatibility; there may also be behavior changes – both intentional ones (covered by [**PEP 387**](https://peps.python.org/pep-0387/)
) and bugs.

Be sure to run tests on both free-threaded and non-free-threaded builds of CPython.

If they pass, congratulations! You have an `abi3t` extension.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Migrating to Stable ABI for free threading (`abi3t`)](https://docs.python.org/3/howto/abi3t-migration.html#)
    *   [Why do this](https://docs.python.org/3/howto/abi3t-migration.html#why-do-this)
        *   [Why _not_ do this](https://docs.python.org/3/howto/abi3t-migration.html#why-not-do-this)
            
    *   [Prerequisites](https://docs.python.org/3/howto/abi3t-migration.html#prerequisites)
        *   [Non-free-threaded Stable ABI](https://docs.python.org/3/howto/abi3t-migration.html#non-free-threaded-stable-abi)
            
        *   [Free-threading support](https://docs.python.org/3/howto/abi3t-migration.html#free-threading-support)
            
        *   [Isolating extension modules](https://docs.python.org/3/howto/abi3t-migration.html#isolating-extension-modules)
            
        *   [Avoiding variable-sized types](https://docs.python.org/3/howto/abi3t-migration.html#avoiding-variable-sized-types)
            
    *   [Setting up the build](https://docs.python.org/3/howto/abi3t-migration.html#setting-up-the-build)
        
    *   [Module export hook](https://docs.python.org/3/howto/abi3t-migration.html#module-export-hook)
        *   [Existing slots](https://docs.python.org/3/howto/abi3t-migration.html#existing-slots)
            *   [`Py_mod_create`](https://docs.python.org/3/howto/abi3t-migration.html#py-mod-create)
                
            *   [Multiple `Py_mod_exec`](https://docs.python.org/3/howto/abi3t-migration.html#multiple-py-mod-exec)
                
            *   [Merging slot arrays](https://docs.python.org/3/howto/abi3t-migration.html#merging-slot-arrays)
                
        *   [Associated `PyModuleDef`](https://docs.python.org/3/howto/abi3t-migration.html#associated-pymoduledef)
            
    *   [`PyObject` opaqueness](https://docs.python.org/3/howto/abi3t-migration.html#pyobject-opaqueness)
        *   [Custom type definitions](https://docs.python.org/3/howto/abi3t-migration.html#custom-type-definitions)
            
        *   [Custom type data access](https://docs.python.org/3/howto/abi3t-migration.html#custom-type-data-access)
            
    *   [Avoid build-time conditionals](https://docs.python.org/3/howto/abi3t-migration.html#avoid-build-time-conditionals)
        
    *   [Further code changes](https://docs.python.org/3/howto/abi3t-migration.html#further-code-changes)
        
    *   [Tagging and distribution](https://docs.python.org/3/howto/abi3t-migration.html#tagging-and-distribution)
        
    *   [Testing](https://docs.python.org/3/howto/abi3t-migration.html#testing)
        

#### Previous topic

[C API Extension Support for Free Threading](https://docs.python.org/3/howto/free-threading-extensions.html "previous chapter")

#### Next topic

[Remote debugging attachment protocol](https://docs.python.org/3/howto/remote_debugging.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Migrating+to+Stable+ABI+for+free+threading+%28abi3t%29&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fhowto%2Fabi3t-migration.html&pagesource=howto%2Fabi3t-migration.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/howto/abi3t-migration.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/remote_debugging.html "Remote debugging attachment protocol")
     |
*   [previous](https://docs.python.org/3/howto/free-threading-extensions.html "C API Extension Support for Free Threading")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [Migrating to Stable ABI for free threading (`abi3t`)](https://docs.python.org/3/howto/abi3t-migration.html)
    
*    
    
    |
*   Theme Auto Light Dark |