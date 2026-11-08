### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/iterator.html "Iterator Objects")
     |
*   [previous](https://docs.python.org/3/c-api/file.html "File objects")
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
*   [Module Objects](https://docs.python.org/3/c-api/module.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Module Objects[¶](https://docs.python.org/3/c-api/module.html#module-objects "Link to this heading")

=====================================================================================================

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyModule\_Type[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python module type. This is exposed to Python programs as [`types.ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType")
.

int PyModule\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_Check "Link to this definition")
  

Return true if _p_ is a module object, or a subtype of a module object. This function always succeeds.

int PyModule\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_CheckExact "Link to this definition")
  

Return true if _p_ is a module object, but not a subtype of [`PyModule_Type`](https://docs.python.org/3/c-api/module.html#c.PyModule_Type "PyModule_Type")
. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModule\_NewObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_NewObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return a new module object with [`module.__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")
 set to _name_. The module’s `__name__`, [`__doc__`](https://docs.python.org/3/reference/datamodel.html#module.__doc__ "module.__doc__")
, [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
 and [`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")
 attributes are filled in (all but `__name__` are set to `None`). The caller is responsible for setting a [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__")
 attribute.

Return `NULL` with an exception set on error.

Added in version 3.3.

Changed in version 3.4: [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
 and [`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")
 are now set to `None`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModule\_New(const char \*name)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyModule_NewObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_NewObject "PyModule_NewObject")
, but the name is a UTF-8 encoded string instead of a Unicode object.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModule\_GetDict([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_GetDict "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the dictionary object that implements _module_’s namespace; this object is the same as the [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
 attribute of the module object. If _module_ is not a module object (or a subtype of a module object), [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 is raised and `NULL` is returned.

It is recommended extensions use other `PyModule_*` and `PyObject_*` functions rather than directly manipulate a module’s [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
.

The returned reference is borrowed from the module; it is valid until the module is destroyed.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModule\_GetNameObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_GetNameObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return _module_’s [`__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")
 value. If the module does not provide one, or if it is not a string, [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 is raised and `NULL` is returned.

Added in version 3.3.

const char \*PyModule\_GetName([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_GetName "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyModule_GetNameObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetNameObject "PyModule_GetNameObject")
 but return the name encoded to `'utf-8'`.

The returned buffer is only valid until the module is renamed or destroyed. Note that Python code may rename a module by setting its [`__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")
 attribute.

[PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*PyModule\_GetDef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_GetDef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a pointer to the [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 struct from which the module was created, or `NULL` if the module wasn’t created from a definition.

On error, return `NULL` with an exception set. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to tell this case apart from a missing `PyModuleDef`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModule\_GetFilenameObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilenameObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the name of the file from which _module_ was loaded using _module_’s [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__")
 attribute. If this is not defined, or if it is not a string, raise [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 and return `NULL`; otherwise return a reference to a Unicode object.

Added in version 3.2.

const char \*PyModule\_GetFilename([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilename "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyModule_GetFilenameObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilenameObject "PyModule_GetFilenameObject")
 but return the filename encoded to ‘utf-8’.

The returned buffer is only valid until the module’s [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__")
 attribute is reassigned or the module is destroyed.

Deprecated since version 3.2: [`PyModule_GetFilename()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilename "PyModule_GetFilename")
 raises [`UnicodeEncodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeEncodeError "UnicodeEncodeError")
 on unencodable filenames, use [`PyModule_GetFilenameObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilenameObject "PyModule_GetFilenameObject")
 instead.

Module definition[¶](https://docs.python.org/3/c-api/module.html#module-definition "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Modules created using the C API are typically defined using an array of [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 structs, which provides a “description” of how a module should be created. See [Definition slots](https://docs.python.org/3/c-api/slots.html#capi-slots)
 for more information on slots in general.

Changed in version 3.15: Previously, a [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 struct was necessary to define modules. The older way of defining modules is still available: consult either the [Module definition struct](https://docs.python.org/3/c-api/module.html#pymoduledef)
 section or earlier versions of this documentation if you plan to support earlier Python versions.

The slots array is usually used to define an extension module’s “main” module object (see [Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html#extension-modules)
 for details). It can also be used to [create extension modules dynamically](https://docs.python.org/3/c-api/module.html#module-from-slots)
.

Unless specified otherwise, the same slot ID may not be repeated in an array of slots.

### Metadata slots[¶](https://docs.python.org/3/c-api/module.html#metadata-slots "Link to this heading")

Py\_mod\_name[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_name "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for the name of the new module, as a NUL-terminated UTF8-encoded `const char *`.

Note that modules are typically created using a [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")
, and when they are, the name from the spec will be used instead of `Py_mod_name`. However, it is still recommended to include this slot for introspection and debugging purposes.

Added in version 3.15: Use [`PyModuleDef.m_name`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_name "PyModuleDef.m_name")
 instead to support previous versions.

Py\_mod\_doc[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_doc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for the docstring of the new module, as a NUL-terminated UTF8-encoded `const char *`.

Usually it is set to a variable created with [`PyDoc_STRVAR`](https://docs.python.org/3/c-api/intro.html#c.PyDoc_STRVAR "PyDoc_STRVAR")
.

Added in version 3.15: Use [`PyModuleDef.m_doc`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_doc "PyModuleDef.m_doc")
 instead to support previous versions.

### Feature slots[¶](https://docs.python.org/3/c-api/module.html#feature-slots "Link to this heading")

Py\_mod\_abi[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_abi "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 whose value points to a [`PyABIInfo`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo "PyABIInfo")
 structure describing the ABI that the extension is using.

A suitable `PyABIInfo` variable can be defined using the [`PyABIInfo_VAR`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_VAR "PyABIInfo_VAR")
 macro, as in:

PyABIInfo\_VAR(abi\_info);

static PySlot mymodule\_slots\[\] \= {
   PySlot\_DATA(Py\_mod\_abi, &abi\_info),
   ...
};

When creating a module, Python checks the value of this slot using [`PyABIInfo_Check()`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_Check "PyABIInfo_Check")
.

This slot is required, except for modules created from [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
.

Added in version 3.15.

Py\_mod\_multiple\_interpreters[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_multiple_interpreters "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 whose value is one of:

Py\_MOD\_MULTIPLE\_INTERPRETERS\_NOT\_SUPPORTED[¶](https://docs.python.org/3/c-api/module.html#c.Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED "Link to this definition")
  

The module does not support being imported in subinterpreters.

Py\_MOD\_MULTIPLE\_INTERPRETERS\_SUPPORTED[¶](https://docs.python.org/3/c-api/module.html#c.Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED "Link to this definition")
  

The module supports being imported in subinterpreters, but only when they share the main interpreter’s GIL. (See [Isolating Extension Modules](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extensions-howto)
.)

Py\_MOD\_PER\_INTERPRETER\_GIL\_SUPPORTED[¶](https://docs.python.org/3/c-api/module.html#c.Py_MOD_PER_INTERPRETER_GIL_SUPPORTED "Link to this definition")
  

The module supports being imported in subinterpreters, even when they have their own GIL. (See [Isolating Extension Modules](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extensions-howto)
.)

This slot determines whether or not importing this module in a subinterpreter will fail.

If `Py_mod_multiple_interpreters` is not specified, the import machinery defaults to `Py_MOD_MULTIPLE_INTERPRETERS_SUPPORTED`.

For historical reasons, the values are declared as pointers (`void *`). When using [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 arrays, use [`PySlot_DATA`](https://docs.python.org/3/c-api/slots.html#c.PySlot_DATA "PySlot_DATA")
 for `Py_mod_multiple_interpreters`:

PySlot\_DATA(Py\_mod\_multiple\_interpreters,
            Py\_MOD\_PER\_INTERPRETER\_GIL\_SUPPORTED)

Added in version 3.12.

Py\_mod\_gil[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_gil "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 whose value is one of:

Py\_MOD\_GIL\_USED[¶](https://docs.python.org/3/c-api/module.html#c.Py_MOD_GIL_USED "Link to this definition")
  

The module depends on the presence of the global interpreter lock (GIL), and may access global state without synchronization.

Py\_MOD\_GIL\_NOT\_USED[¶](https://docs.python.org/3/c-api/module.html#c.Py_MOD_GIL_NOT_USED "Link to this definition")
  

The module is safe to run without an active GIL.

This slot is ignored by Python builds not configured with [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
. Otherwise, it determines whether or not importing this module will cause the GIL to be automatically enabled. See [Free-threaded CPython](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-free-threaded-cpython)
 for more detail.

If `Py_mod_gil` is not specified, the import machinery defaults to `Py_MOD_GIL_USED`.

For historical reasons, the values are declared as pointers (`void *`). When using [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 arrays, use [`PySlot_DATA`](https://docs.python.org/3/c-api/slots.html#c.PySlot_DATA "PySlot_DATA")
 for `Py_mod_gil`:

PySlot\_DATA(Py\_mod\_gil, Py\_MOD\_GIL\_NOT\_USED)

Added in version 3.13.

### Creation and initialization slots[¶](https://docs.python.org/3/c-api/module.html#creation-and-initialization-slots "Link to this heading")

Py\_mod\_create[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_create "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for a function that creates the module object itself. The function must have the signature:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*create\_module([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*spec, [PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def)[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_create.create_module "Link to this definition")
  

The function will be called with:

*   _spec_: a `ModuleSpec`\-like object, meaning that any attributes defined for [`importlib.machinery.ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")
     have matching semantics. However, any of the attributes may be missing.
    
*   _def_: `NULL`, or the module definition if the module is created from one.
    

The function should return a new module object, or set an error and return `NULL`.

This function should be kept minimal. In particular, it should not call arbitrary Python code, as trying to import the same module again may result in an infinite loop.

If `Py_mod_create` is not specified, the import machinery will create a normal module object using [`PyModule_New()`](https://docs.python.org/3/c-api/module.html#c.PyModule_New "PyModule_New")
. The name is taken from _spec_, not the definition, to allow extension modules to dynamically adjust to their place in the module hierarchy and be imported under different names through symlinks, all while sharing a single module definition.

There is no requirement for the returned object to be an instance of [`PyModule_Type`](https://docs.python.org/3/c-api/module.html#c.PyModule_Type "PyModule_Type")
. However, some slots may only be used with `PyModule_Type` instances; in particular:

*   [`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
    ,
    
*   [module state slots](https://docs.python.org/3/c-api/module.html#ext-module-state-slots)
     (`Py_mod_state_*`),
    
*   [`Py_mod_token`](https://docs.python.org/3/c-api/module.html#c.Py_mod_token "Py_mod_token")
    .
    

Added in version 3.5.

Changed in version 3.15: The _spec_ argument may be a `ModuleSpec`\-like object, rather than a true [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")
 instance. Note that previous versions of CPython did not enforce this.

The _def_ argument may now be `NULL`, since modules are not necessarily made from definitions.

Py\_mod\_exec[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for a function that will _execute_, or initialize, the module. This function does the equivalent to executing the code of a Python module: typically, it adds classes and constants to the module. The signature of the function is:

int exec\_module([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec.exec_module "Link to this definition")
  

See the [Support functions](https://docs.python.org/3/c-api/module.html#capi-module-support-functions)
 section for some useful functions to call.

For backwards compatibility, the [`PyModuleDef.m_slots`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_slots "PyModuleDef.m_slots")
 array may contain multiple `Py_mod_exec` slots; these are processed in the order they appear in the array. Elsewhere (that is, in arguments to [`PyModule_FromSlotsAndSpec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromSlotsAndSpec "PyModule_FromSlotsAndSpec")
 and in return values of `PyModExport__<name>_`), repeating the slot is not allowed.

Added in version 3.5.

Changed in version 3.15: Repeated `Py_mod_exec` slots are disallowed, except in [`PyModuleDef.m_slots`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_slots "PyModuleDef.m_slots")
.

Py\_mod\_methods[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_methods "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for a table of module-level functions, as an array of [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 values suitable as the _functions_ argument to [`PyModule_AddFunctions()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddFunctions "PyModule_AddFunctions")
.

Like other slot IDs, a slots array may only contain one `Py_mod_methods` entry. To add functions from multiple [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 arrays, call [`PyModule_AddFunctions()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddFunctions "PyModule_AddFunctions")
 in the [`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
 function.

The table must be statically allocated (or otherwise guaranteed to outlive the module object).

Added in version 3.15: Use [`PyModuleDef.m_methods`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_methods "PyModuleDef.m_methods")
 instead to support previous versions.

Module state[¶](https://docs.python.org/3/c-api/module.html#module-state "Link to this heading")

-------------------------------------------------------------------------------------------------

Extension modules can have _module state_ – a piece of memory that is allocated on module creation, and freed when the module object is deallocated. The module state is specified using [dedicated slots](https://docs.python.org/3/c-api/module.html#ext-module-state-slots)
.

A typical use of module state is storing an exception type – or indeed _any_ type object defined by the module –

Unlike the module’s Python attributes, Python code cannot replace or delete data stored in module state.

Keeping per-module information in attributes and module state, rather than in static globals, makes module objects _isolated_ and safer for use in multiple sub-interpreters. It also helps Python do an orderly clean-up when it shuts down.

Extensions that keep references to Python objects as part of module state must implement [`Py_mod_state_traverse`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_traverse "Py_mod_state_traverse")
 and [`Py_mod_state_clear`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_clear "Py_mod_state_clear")
 functions to avoid reference leaks.

To retrieve the state from a given module, use the following functions:

void \*PyModule\_GetState([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the “state” of the module, that is, a pointer to the block of memory allocated at module creation time, or `NULL`. See [`Py_mod_state_size`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_size "Py_mod_state_size")
.

On error, return `NULL` with an exception set. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to tell this case apart from missing module state.

int PyModule\_GetStateSize([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*result)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_GetStateSize "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Set _\*result_ to the size of _module_’s state, as specified using [`Py_mod_state_size`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_size "Py_mod_state_size")
 (or [`PyModuleDef.m_size`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_size "PyModuleDef.m_size")
), and return 0.

On error, set _\*result_ to -1, and return -1 with an exception set.

Added in version 3.15.

### Slots for defining module state[¶](https://docs.python.org/3/c-api/module.html#slots-for-defining-module-state "Link to this heading")

The following [`slot IDs`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 are available for defining the module state.

Py\_mod\_state\_size[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_size "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for the size of the module state, in bytes.

Setting the value to a non-negative value means that the module can be re-initialized and specifies the additional amount of memory it requires for its state.

See [**PEP 3121**](https://peps.python.org/pep-3121/)
 for more details.

Use [`PyModule_GetStateSize()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetStateSize "PyModule_GetStateSize")
 to retrieve the size of a given module.

Added in version 3.15: Use [`PyModuleDef.m_size`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_size "PyModuleDef.m_size")
 instead to support previous versions.

Py\_mod\_state\_traverse[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_traverse "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for a traversal function to call during GC traversal of the module object.

The signature of the function, and meanings of the arguments, is similar as for [`PyTypeObject.tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
:

int traverse\_module\_state([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, [visitproc](https://docs.python.org/3/c-api/gcsupport.html#c.visitproc "visitproc")
 visit, void \*arg)[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_traverse.traverse_module_state "Link to this definition")
  

This function is not called if the module state was requested but is not allocated yet. This is the case immediately after the module is created and before the module is executed ([`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
 function). More precisely, this function is not called if the state size ([`Py_mod_state_size`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_size "Py_mod_state_size")
) is greater than 0 and the module state (as returned by [`PyModule_GetState()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "PyModule_GetState")
) is `NULL`.

Added in version 3.15: Use [`PyModuleDef.m_traverse`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_traverse "PyModuleDef.m_traverse")
 instead to support previous versions.

Py\_mod\_state\_clear[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_clear "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for a clear function to call during GC clearing of the module object.

The signature of the function is:

int clear\_module\_state([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_clear.clear_module_state "Link to this definition")
  

This function is not called if the module state was requested but is not allocated yet. This is the case immediately after the module is created and before the module is executed ([`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
 function). More precisely, this function is not called if the state size ([`Py_mod_state_size`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_size "Py_mod_state_size")
) is greater than 0 and the module state (as returned by [`PyModule_GetState()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "PyModule_GetState")
) is `NULL`.

Like [`PyTypeObject.tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
, this function is not _always_ called before a module is deallocated. For example, when reference counting is enough to determine that an object is no longer used, the cyclic garbage collector is not involved and the [`Py_mod_state_free`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_free "Py_mod_state_free")
 function is called directly.

Added in version 3.15: Use [`PyModuleDef.m_clear`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_clear "PyModuleDef.m_clear")
 instead to support previous versions.

Py\_mod\_state\_free[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_free "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for a function to call during deallocation of the module object.

The signature of the function is:

int free\_module\_state([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_free.free_module_state "Link to this definition")
  

This function is not called if the module state was requested but is not allocated yet. This is the case immediately after the module is created and before the module is executed ([`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
 function). More precisely, this function is not called if the state size ([`Py_mod_state_size`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_size "Py_mod_state_size")
) is greater than 0 and the module state (as returned by [`PyModule_GetState()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "PyModule_GetState")
) is `NULL`.

Added in version 3.15: Use [`PyModuleDef.m_free`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_free "PyModuleDef.m_free")
 instead to support previous versions.

### Module token[¶](https://docs.python.org/3/c-api/module.html#module-token "Link to this heading")

Each module may have an associated _token_: a pointer-sized value intended to identify of the module state’s memory layout. This means that if you have a module object, but you are not sure if it “belongs” to your extension, you can check using code like this:

PyObject \*module \= <the module in question\>;

void \*module\_token;
if (PyModule\_GetToken(module, &module\_token) < 0) {
    return NULL;
}
if (module\_token != your\_token) {
    PyErr\_SetString(PyExc\_ValueError, "unexpected module");
    return NULL;
}

// This module's state has the expected memory layout; it's safe to cast
struct my\_state \*state \= (struct my\_state\*)PyModule\_GetState(module);

A module’s token – and the _your\_token_ value to use in the above code – is:

*   For modules created with [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
    : the address of that `PyModuleDef`;
    
*   For modules defined with the [`Py_mod_token`](https://docs.python.org/3/c-api/module.html#c.Py_mod_token "Py_mod_token")
     slot: the value of that slot;
    
*   For modules created from an `PyModExport_*` [export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
    : the slots array that the export hook returned (unless overridden with [`Py_mod_token`](https://docs.python.org/3/c-api/module.html#c.Py_mod_token "Py_mod_token")
    ).
    

Py\_mod\_token[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_token "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for the module token.

If you use this slot to set the module token (rather than rely on the default), you must ensure that:

*   The pointer outlives the class, so it’s not reused for something else while the class exists.
    
*   It “belongs” to the extension module where the class lives, so it will not clash with other extensions.
    
*   If the token points to a [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
     struct, the module should behave as if it was created from that `PyModuleDef`. In particular, the module state must have matching layout and semantics.
    

Modules created from [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 always use the address of the `PyModuleDef` as the token. This means that `Py_mod_token` cannot be used in [`PyModuleDef.m_slots`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_slots "PyModuleDef.m_slots")
.

Added in version 3.15.

int PyModule\_GetToken([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, void \*\*result)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_GetToken "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Set _\*result_ to the module token for _module_ and return 0.

On error, set _\*result_ to NULL, and return -1 with an exception set.

Added in version 3.15.

See also [`PyType_GetModuleByToken()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByToken "PyType_GetModuleByToken")
.

Creating extension modules dynamically[¶](https://docs.python.org/3/c-api/module.html#creating-extension-modules-dynamically "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

The following functions may be used to create an extension module dynamically, rather than from an extension’s [export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModule\_FromSlotsAndSpec(const [PySlot](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 \*slots, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*spec)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_FromSlotsAndSpec "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Create a new module object, given an array of [slots](https://docs.python.org/3/c-api/module.html#pymoduledef-slot)
 and the [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")
 _spec_.

The _slots_ argument must point to an array of [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 structures, terminated by an entry with slot ID of 0 (typically written as [`PySlot_END`](https://docs.python.org/3/c-api/slots.html#c.PySlot_END "PySlot_END")
). The array must include a [`Py_mod_abi`](https://docs.python.org/3/c-api/module.html#c.Py_mod_abi "Py_mod_abi")
 entry.

The _spec_ argument may be any `ModuleSpec`\-like object, as described in [`Py_mod_create`](https://docs.python.org/3/c-api/module.html#c.Py_mod_create "Py_mod_create")
 documentation. Currently, the _spec_ must have a `name` attribute.

On success, return the new module. On error, return `NULL` with an exception set.

Note that this does not process the module’s execution slot ([`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
). Both `PyModule_FromSlotsAndSpec()` and [`PyModule_Exec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Exec "PyModule_Exec")
 must be called to fully initialize a module. (See also [Multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
.)

Added in version 3.15.

int PyModule\_Exec([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_Exec "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Execute the [`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
 slot(s) of _module_.

On success, return 0. On error, return -1 with an exception set.

For clarity: If _module_ has no slots, for example if it uses [legacy single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#single-phase-initialization)
, this function does nothing and returns 0.

Added in version 3.15.

Module definition struct[¶](https://docs.python.org/3/c-api/module.html#module-definition-struct "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

Traditionally, extension modules were defined using a _module definition_ as the “description” of how a module should be created. Rather than using an array of [slots](https://docs.python.org/3/c-api/module.html#pymoduledef-slot)
 directly, the definition has dedicated members for most common functionality, and allows additional slots as an extension mechanism.

This way of defining modules is still available and there are no plans to remove it.

type PyModuleDef[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (see below)._

The module definition struct, which holds information needed to create a module object.

This structure must be statically allocated (or be otherwise guaranteed to be valid while any modules created from it exist). Usually, there is only one variable of this type for each extension module defined this way.

The struct, including all members, is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable-abi)
 for non-free-threaded builds (`abi3`). In the Stable ABI for free-threaded builds (`abi3t`), this struct is opaque, and unusable in practice; see [Module definition](https://docs.python.org/3/c-api/module.html#pymoduledef-slot)
 for a replacement.

[PyModuleDef\_Base](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Base "PyModuleDef_Base")
 m\_base[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_base "Link to this definition")
  

Always initialize this member to [`PyModuleDef_HEAD_INIT`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_HEAD_INIT "PyModuleDef_HEAD_INIT")
:

type PyModuleDef\_Base[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Base "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (see below)._

The type of `PyModuleDef.m_base`.

The struct is part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable-abi)
 for non-free-threaded builds (`abi3`). In the Stable ABI for Free-Threaded Builds (`abi3t`), this struct is opaque, and unusable in practice.

PyModuleDef\_HEAD\_INIT[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_HEAD_INIT "Link to this definition")
  

The required initial value for `PyModuleDef.m_base`.

const char \*m\_name[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_name "Link to this definition")
  

Corresponds to the [`Py_mod_name`](https://docs.python.org/3/c-api/module.html#c.Py_mod_name "Py_mod_name")
 slot.

const char \*m\_doc[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_doc "Link to this definition")
  

These members correspond to the [`Py_mod_doc`](https://docs.python.org/3/c-api/module.html#c.Py_mod_doc "Py_mod_doc")
 slot. Setting this to NULL is equivalent to omitting the slot.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 m\_size[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_size "Link to this definition")
  

Corresponds to the [`Py_mod_state_size`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_size "Py_mod_state_size")
 slot. Setting this to zero is equivalent to omitting the slot.

When using [legacy single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#single-phase-initialization)
 or when creating modules dynamically using [`PyModule_Create()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Create "PyModule_Create")
 or [`PyModule_Create2()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Create2 "PyModule_Create2")
, `m_size` may be set to -1. This indicates that the module does not support sub-interpreters, because it has global state.

[PyMethodDef](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 \*m\_methods[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_methods "Link to this definition")
  

Corresponds to the [`Py_mod_methods`](https://docs.python.org/3/c-api/module.html#c.Py_mod_methods "Py_mod_methods")
 slot. Setting this to NULL is equivalent to omitting the slot.

[PyModuleDef\_Slot](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot "PyModuleDef_Slot")
 \*m\_slots[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_slots "Link to this definition")
  

An array of additional slots, terminated by a `{0, NULL}` entry. Note that the entries use the older [`PyModuleDef_Slot`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot "PyModuleDef_Slot")
 structure, rather than [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
.

If the array contains slots corresponding to [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 members, the values must match. For example, if you use [`Py_mod_name`](https://docs.python.org/3/c-api/module.html#c.Py_mod_name "Py_mod_name")
 in `m_slots`, [`PyModuleDef.m_name`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_name "PyModuleDef.m_name")
 must be set to the same pointer (not just an equal string).

Changed in version 3.5: Prior to version 3.5, this member was always set to `NULL`, and was defined as:

> [inquiry](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry")
>  m\_reload[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_slots.m_reload "Link to this definition")
>   

type PyModuleDef\_Slot[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members) since version 3.5._

Older structure defining additional slots of a module.

Note that a `PyModuleDef_Slot` array may be included in a `PySlot` array using [`Py_mod_slots`](https://docs.python.org/3/c-api/module.html#c.Py_mod_slots "Py_mod_slots")
, and vice versa using [`Py_slot_subslots`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_subslots "Py_slot_subslots")
.

Each `PyModuleDef_Slot` structure `modslot` is interpreted as the following [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 structure:

(PySlot){
   .sl\_id\=modslot.slot,
   .sl\_flags\=PySlot\_INTPTR | sub\_static,
   .sl\_ptr\=modslot.value
}

where `sub_static` is `PySlot_STATIC` if the slot requires the flag (such as for [`Py_mod_methods`](https://docs.python.org/3/c-api/module.html#c.Py_mod_methods "Py_mod_methods")
), or if this flag is present on the “parent” `Py_mod_slots` slot (if any).

int slot[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot.slot "Link to this definition")
  

Corresponds to [`PySlot.sl_id`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
.

void \*value[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot.value "Link to this definition")
  

Corresponds to [`PySlot.sl_ptr`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_ptr "PySlot.sl_ptr")
.

Added in version 3.5.

[traverseproc](https://docs.python.org/3/c-api/gcsupport.html#c.traverseproc "traverseproc")
 m\_traverse[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_traverse "Link to this definition")
  

[inquiry](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry")
 m\_clear[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_clear "Link to this definition")
  

[freefunc](https://docs.python.org/3/c-api/typeobj.html#c.freefunc "freefunc")
 m\_free[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_free "Link to this definition")
  

These members correspond to the [`Py_mod_state_traverse`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_traverse "Py_mod_state_traverse")
, [`Py_mod_state_clear`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_clear "Py_mod_state_clear")
, and [`Py_mod_state_free`](https://docs.python.org/3/c-api/module.html#c.Py_mod_state_free "Py_mod_state_free")
 slots, respectively.

Setting these members to NULL is equivalent to omitting the corresponding slots.

Changed in version 3.9: [`m_traverse`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_traverse "m_traverse")
, [`m_clear`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_clear "m_clear")
 and [`m_free`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_free "m_free")
 functions are no longer called before the module state is allocated.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyModuleDef\_Type[¶](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.5._

The type of `PyModuleDef` objects.

Py\_mod\_slots[¶](https://docs.python.org/3/c-api/module.html#c.Py_mod_slots "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 that works like [`Py_slot_subslots`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_subslots "Py_slot_subslots")
, except it specifies an array of [`PyModuleDef_Slot`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef_Slot "PyModuleDef_Slot")
 structures.

Added in version 3.15.

The following API can be used to create modules from a `PyModuleDef` struct:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModule\_Create([PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_Create "Link to this definition")
  

_Return value: New reference._

Create a new module object, given the definition in _def_. This is a macro that calls [`PyModule_Create2()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Create2 "PyModule_Create2")
 with _module\_api\_version_ set to [`PYTHON_API_VERSION`](https://docs.python.org/3/c-api/module.html#c.PYTHON_API_VERSION "PYTHON_API_VERSION")
, or to [`PYTHON_ABI_VERSION`](https://docs.python.org/3/c-api/module.html#c.PYTHON_ABI_VERSION "PYTHON_ABI_VERSION")
 if using the [limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModule\_Create2([PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def, int module\_api\_version)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_Create2 "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a new module object, given the definition in _def_, assuming the API version _module\_api\_version_. If that version does not match the version of the running interpreter, a [`RuntimeWarning`](https://docs.python.org/3/builtins/exceptions.html#RuntimeWarning "RuntimeWarning")
 is emitted.

Return `NULL` with an exception set on error.

This function does not support slots. The [`m_slots`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_slots "PyModuleDef.m_slots")
 member of _def_ must be `NULL`.

Note

Most uses of this function should be using [`PyModule_Create()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Create "PyModule_Create")
 instead; only use this if you are sure you need it.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModule\_FromDefAndSpec([PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*spec)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_FromDefAndSpec "Link to this definition")
  

_Return value: New reference._

This macro calls [`PyModule_FromDefAndSpec2()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromDefAndSpec2 "PyModule_FromDefAndSpec2")
 with _module\_api\_version_ set to [`PYTHON_API_VERSION`](https://docs.python.org/3/c-api/module.html#c.PYTHON_API_VERSION "PYTHON_API_VERSION")
, or to [`PYTHON_ABI_VERSION`](https://docs.python.org/3/c-api/module.html#c.PYTHON_ABI_VERSION "PYTHON_ABI_VERSION")
 if using the [limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
.

Added in version 3.5.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: Prefer [`PyModule_FromSlotsAndSpec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromSlotsAndSpec "PyModule_FromSlotsAndSpec")
 in new code.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyModule\_FromDefAndSpec2([PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*spec, int module\_api\_version)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_FromDefAndSpec2 "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Create a new module object, given the definition in _def_ and the ModuleSpec _spec_, assuming the API version _module\_api\_version_. If that version does not match the version of the running interpreter, a [`RuntimeWarning`](https://docs.python.org/3/builtins/exceptions.html#RuntimeWarning "RuntimeWarning")
 is emitted.

Return `NULL` with an exception set on error.

Note that this does not process execution slots ([`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
). Both `PyModule_FromDefAndSpec` and `PyModule_ExecDef` must be called to fully initialize a module.

Note

Most uses of this function should be using [`PyModule_FromDefAndSpec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromDefAndSpec "PyModule_FromDefAndSpec")
 instead; only use this if you are sure you need it.

Added in version 3.5.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: Prefer [`PyModule_FromSlotsAndSpec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromSlotsAndSpec "PyModule_FromSlotsAndSpec")
 in new code.

int PyModule\_ExecDef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, [PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_ExecDef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Process any execution slots ([`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
) given in _def_.

Added in version 3.5.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: To run a module’s own execution slots, prefer [`PyModule_Exec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Exec "PyModule_Exec")
, which works on modules that were not created from a [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 structure.

PYTHON\_API\_VERSION[¶](https://docs.python.org/3/c-api/module.html#c.PYTHON_API_VERSION "Link to this definition")
  

PYTHON\_API\_STRING[¶](https://docs.python.org/3/c-api/module.html#c.PYTHON_API_STRING "Link to this definition")
  

The C API version, as an integer (`1013`) and string (`"1013"`), respectively. Defined for backwards compatibility.

Currently, this constant is not updated in new Python versions, and is not useful for versioning. This may change in the future.

PYTHON\_ABI\_VERSION[¶](https://docs.python.org/3/c-api/module.html#c.PYTHON_ABI_VERSION "Link to this definition")
  

PYTHON\_ABI\_STRING[¶](https://docs.python.org/3/c-api/module.html#c.PYTHON_ABI_STRING "Link to this definition")
  

Defined as `3` and `"3"`, respectively, for backwards compatibility.

Currently, this constant is not updated in new Python versions, and is not useful for versioning. This may change in the future.

Support functions[¶](https://docs.python.org/3/c-api/module.html#support-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------

The following functions are provided to help initialize a module object. They are intended for a module’s execution slot ([`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec")
), the initialization function for legacy [single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#single-phase-initialization)
, or code that creates modules dynamically.

int PyModule\_AddObjectRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Add an object to _module_ as _name_. This is a convenience function which can be used from the module’s initialization function.

On success, return `0`. On error, raise an exception and return `-1`.

Example usage:

static int
add\_spam(PyObject \*module, int value)
{
    PyObject \*obj \= PyLong\_FromLong(value);
    if (obj \== NULL) {
        return \-1;
    }
    int res \= PyModule\_AddObjectRef(module, "spam", obj);
    Py\_DECREF(obj);
    return res;
 }

To be convenient, the function accepts `NULL` _value_ with an exception set. In this case, return `-1` and just leave the raised exception unchanged.

The example can also be written without checking explicitly if _obj_ is `NULL`:

static int
add\_spam(PyObject \*module, int value)
{
    PyObject \*obj \= PyLong\_FromLong(value);
    int res \= PyModule\_AddObjectRef(module, "spam", obj);
    Py\_XDECREF(obj);
    return res;
 }

Note that `Py_XDECREF()` should be used instead of `Py_DECREF()` in this case, since _obj_ can be `NULL`.

The number of different _name_ strings passed to this function should be kept small, usually by only using statically allocated strings as _name_. For names that aren’t known at compile time, prefer calling [`PyUnicode_FromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromString "PyUnicode_FromString")
 and [`PyObject_SetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetAttr "PyObject_SetAttr")
 directly. For more details, see [`PyUnicode_InternFromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternFromString "PyUnicode_InternFromString")
, which may be used internally to create a key object.

Added in version 3.10.

int PyModule\_Add([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_Add "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Similar to [`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef")
, but “[steals](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _value_ (even on error). It can be called with a result of function that returns a new reference without bothering to check its result or even saving it to a variable.

Example usage:

if (PyModule\_Add(module, "spam", PyBytes\_FromString(value)) < 0) {
    goto error;
}

Added in version 3.13.

int PyModule\_AddObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObject "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef")
, but [steals](https://docs.python.org/3/glossary.html#term-steal)
 a reference to _value_ on success (if it returns `0`).

The new [`PyModule_Add()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Add "PyModule_Add")
 or [`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef")
 functions are recommended, since it is easy to introduce reference leaks by misusing the [`PyModule_AddObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObject "PyModule_AddObject")
 function.

Note

Unlike other functions that steal references, `PyModule_AddObject()` only releases the reference to _value_ **on success**.

This means that its return value must be checked, and calling code must [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF")
 _value_ manually on error.

Example usage:

PyObject \*obj \= PyBytes\_FromString(value);
if (PyModule\_AddObject(module, "spam", obj) < 0) {
    // If 'obj' is not NULL and PyModule\_AddObject() failed,
    // 'obj' strong reference must be deleted with Py\_XDECREF().
    // If 'obj' is NULL, Py\_XDECREF() does nothing.
    Py\_XDECREF(obj);
    goto error;
}
// PyModule\_AddObject() stole a reference to obj:
// Py\_XDECREF(obj) is not needed here.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.13.

int PyModule\_AddIntConstant([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, const char \*name, long value)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_AddIntConstant "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Add an integer constant to _module_ as _name_. This convenience function can be used from the module’s initialization function. Return `-1` with an exception set on error, `0` on success.

This is a convenience function that calls [`PyLong_FromLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong "PyLong_FromLong")
 and [`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef")
; see their documentation for details.

int PyModule\_AddStringConstant([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, const char \*name, const char \*value)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_AddStringConstant "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Add a string constant to _module_ as _name_. This convenience function can be used from the module’s initialization function. The string _value_ must be `NULL`\-terminated. Return `-1` with an exception set on error, `0` on success.

This is a convenience function that calls [`PyUnicode_InternFromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternFromString "PyUnicode_InternFromString")
 and [`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef")
; see their documentation for details.

PyModule\_AddIntMacro(module, macro)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_AddIntMacro "Link to this definition")
  

Add an int constant to _module_. The name and the value are taken from _macro_. For example `PyModule_AddIntMacro(module, AF_INET)` adds the int constant _AF\_INET_ with the value of _AF\_INET_ to _module_. Return `-1` with an exception set on error, `0` on success.

PyModule\_AddStringMacro(module, macro)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_AddStringMacro "Link to this definition")
  

Add a string constant to _module_.

int PyModule\_AddType([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_AddType "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Add a type object to _module_. The type object is finalized by calling internally [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
. The name of the type object is taken from the last component of [`tp_name`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_name "PyTypeObject.tp_name")
 after dot. Return `-1` with an exception set on error, `0` on success.

Added in version 3.9.

int PyModule\_AddFunctions([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, [PyMethodDef](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 \*functions)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_AddFunctions "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Add the functions from the `NULL` terminated _functions_ array to _module_. Refer to the [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 documentation for details on individual entries (due to the lack of a shared module namespace, module level “functions” implemented in C typically receive the module as their first parameter, making them similar to instance methods on Python classes).

This function is called automatically when creating a module from `PyModuleDef` (such as when using [Multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
, `PyModule_Create`, or `PyModule_FromDefAndSpec`). Some module authors may prefer defining functions in multiple [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 arrays; in that case they should call this function directly.

The _functions_ array must be statically allocated (or otherwise guaranteed to outlive the module object).

Added in version 3.5.

int PyModule\_SetDocString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, const char \*docstring)[¶](https://docs.python.org/3/c-api/module.html#c.PyModule_SetDocString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Set the docstring for _module_ to _docstring_. This function is called automatically when creating a module from `PyModuleDef` (such as when using [Multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
, `PyModule_Create`, or `PyModule_FromDefAndSpec`).

Return `0` on success. Return `-1` with an exception set on error.

Added in version 3.5.

int PyUnstable\_Module\_SetGIL([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, void \*gil)[¶](https://docs.python.org/3/c-api/module.html#c.PyUnstable_Module_SetGIL "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Indicate that _module_ does or does not support running without the global interpreter lock (GIL), using one of the values from [`Py_mod_gil`](https://docs.python.org/3/c-api/module.html#c.Py_mod_gil "Py_mod_gil")
. It must be called during _module_’s initialization function when using [Legacy single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#single-phase-initialization)
. If this function is not called during module initialization, the import machinery assumes the module does not support running without the GIL. This function is only available in Python builds configured with [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
. Return `-1` with an exception set on error, `0` on success.

Added in version 3.13.

### Module lookup (single-phase initialization)[¶](https://docs.python.org/3/c-api/module.html#module-lookup-single-phase-initialization "Link to this heading")

The legacy [single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#single-phase-initialization)
 initialization scheme creates singleton modules that can be looked up in the context of the current interpreter. This allows the module object to be retrieved later with only a reference to the module definition.

These functions will not work on modules created using multi-phase initialization, since multiple such modules can be created from a single definition.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyState\_FindModule([PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def)[¶](https://docs.python.org/3/c-api/module.html#c.PyState_FindModule "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the module object that was created from _def_ for the current interpreter. This method requires that the module object has been attached to the interpreter state with [`PyState_AddModule()`](https://docs.python.org/3/c-api/module.html#c.PyState_AddModule "PyState_AddModule")
 beforehand. In case the corresponding module object is not found or has not been attached to the interpreter state yet, it returns `NULL`.

int PyState\_AddModule([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, [PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def)[¶](https://docs.python.org/3/c-api/module.html#c.PyState_AddModule "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.3._

Attaches the module object passed to the function to the interpreter state. This allows the module object to be accessible via [`PyState_FindModule()`](https://docs.python.org/3/c-api/module.html#c.PyState_FindModule "PyState_FindModule")
.

Only effective on modules created using single-phase initialization.

Python calls `PyState_AddModule` automatically after importing a module that uses [single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#single-phase-initialization)
, so it is unnecessary (but harmless) to call it from module initialization code. An explicit call is needed only if the module’s own init code subsequently calls `PyState_FindModule`. The function is mainly intended for implementing alternative import mechanisms (either by calling it directly, or by referring to its implementation for details of the required state updates).

If a module was attached previously using the same _def_, it is replaced by the new _module_.

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

Return `-1` with an exception set on error, `0` on success.

Added in version 3.3.

int PyState\_RemoveModule([PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def)[¶](https://docs.python.org/3/c-api/module.html#c.PyState_RemoveModule "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.3._

Removes the module object created from _def_ from the interpreter state. Return `-1` with an exception set on error, `0` on success.

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

Added in version 3.3.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Module Objects](https://docs.python.org/3/c-api/module.html#)
    *   [Module definition](https://docs.python.org/3/c-api/module.html#module-definition)
        *   [Metadata slots](https://docs.python.org/3/c-api/module.html#metadata-slots)
            
        *   [Feature slots](https://docs.python.org/3/c-api/module.html#feature-slots)
            
        *   [Creation and initialization slots](https://docs.python.org/3/c-api/module.html#creation-and-initialization-slots)
            
    *   [Module state](https://docs.python.org/3/c-api/module.html#module-state)
        *   [Slots for defining module state](https://docs.python.org/3/c-api/module.html#slots-for-defining-module-state)
            
        *   [Module token](https://docs.python.org/3/c-api/module.html#module-token)
            
    *   [Creating extension modules dynamically](https://docs.python.org/3/c-api/module.html#creating-extension-modules-dynamically)
        
    *   [Module definition struct](https://docs.python.org/3/c-api/module.html#module-definition-struct)
        
    *   [Support functions](https://docs.python.org/3/c-api/module.html#support-functions)
        *   [Module lookup (single-phase initialization)](https://docs.python.org/3/c-api/module.html#module-lookup-single-phase-initialization)
            

#### Previous topic

[File objects](https://docs.python.org/3/c-api/file.html "previous chapter")

#### Next topic

[Iterator Objects](https://docs.python.org/3/c-api/iterator.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Module+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fmodule.html&pagesource=c-api%2Fmodule.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/module.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/iterator.html "Iterator Objects")
     |
*   [previous](https://docs.python.org/3/c-api/file.html "File objects")
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
*   [Module Objects](https://docs.python.org/3/c-api/module.html)
    
*    
    
    |
*   Theme Auto Light Dark |