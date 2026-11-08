### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/lifecycle.html "Object Life Cycle")
     |
*   [previous](https://docs.python.org/3/c-api/objimpl.html "Object Implementation Support")
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
*   [Object Implementation Support](https://docs.python.org/3/c-api/objimpl.html)
     »
*   [Allocating objects on the heap](https://docs.python.org/3/c-api/allocation.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Allocating objects on the heap[¶](https://docs.python.org/3/c-api/allocation.html#allocating-objects-on-the-heap "Link to this heading")

=========================================================================================================================================

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\_PyObject\_New([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/allocation.html#c._PyObject_New "Link to this definition")
  

_Return value: New reference._

[PyVarObject](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 \*\_PyObject\_NewVar([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/allocation.html#c._PyObject_NewVar "Link to this definition")
  

_Return value: New reference._

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_Init([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_Init "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Initialize a newly allocated object _op_ with its type and initial reference. Returns the initialized object. Other fields of the object are not initialized. Despite its name, this function is unrelated to the object’s [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
 method ([`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
 slot). Specifically, this function does **not** call the object’s `__init__()` method.

In general, consider this function to be a low-level routine. Use [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 where possible. For implementing `tp_alloc` for your type, prefer [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
 or [`PyObject_New()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New")
.

Note

This function only initializes the object’s memory corresponding to the initial [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 structure. It does not zero the rest.

[PyVarObject](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 \*PyObject\_InitVar([PyVarObject](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 \*op, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_InitVar "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This does everything [`PyObject_Init()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_Init "PyObject_Init")
 does, and also initializes the length information for a variable-size object.

Note

This function only initializes some of the object’s memory. It does not zero the rest.

PyObject\_New(TYPE, typeobj)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "Link to this definition")
  

Allocates a new Python object using the C structure type _TYPE_ and the Python type object _typeobj_ (`PyTypeObject*`) by calling [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
 to allocate memory and initializing it like [`PyObject_Init()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_Init "PyObject_Init")
. The caller will own the only reference to the object (i.e. its reference count will be one).

Avoid calling this directly to allocate memory for an object; call the type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot instead.

When populating a type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot, [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
 is preferred over a custom function that simply calls this macro.

This macro does not call [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
, [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 ([`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
), or [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
 ([`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
).

This cannot be used for objects with [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 set in [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
; use [`PyObject_GC_New`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "PyObject_GC_New")
 instead.

Memory allocated by this macro must be freed with [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
 (usually called via the object’s [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 slot).

Note

The returned memory is not guaranteed to have been completely zeroed before it was initialized.

Note

This macro does not construct a fully initialized object of the given type; it merely allocates memory and prepares it for further initialization by [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
. To construct a fully initialized object, call _typeobj_ instead. For example:

PyObject \*foo \= PyObject\_CallNoArgs((PyObject \*)&PyFoo\_Type);

See also

*   [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
    
*   [`PyObject_GC_New`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "PyObject_GC_New")
    
*   [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
    
*   [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
    

PyObject\_NewVar(TYPE, typeobj, size)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "Link to this definition")
  

Like [`PyObject_New`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New")
 except:

*   It allocates enough memory for the _TYPE_ structure plus _size_ (`Py_ssize_t`) fields of the size given by the [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
     field of _typeobj_.
    
*   The memory is initialized like [`PyObject_InitVar()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_InitVar "PyObject_InitVar")
    .
    

This is useful for implementing objects like tuples, which are able to determine their size at construction time. Embedding the array of fields into the same allocation decreases the number of allocations, improving the memory management efficiency.

Avoid calling this directly to allocate memory for an object; call the type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot instead.

When populating a type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot, [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
 is preferred over a custom function that simply calls this macro.

This cannot be used for objects with [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 set in [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
; use [`PyObject_GC_NewVar`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_NewVar "PyObject_GC_NewVar")
 instead.

Memory allocated by this function must be freed with [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
 (usually called via the object’s [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 slot).

Note

The returned memory is not guaranteed to have been completely zeroed before it was initialized.

Note

This macro does not construct a fully initialized object of the given type; it merely allocates memory and prepares it for further initialization by [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
. To construct a fully initialized object, call _typeobj_ instead. For example:

PyObject \*list\_instance \= PyObject\_CallNoArgs((PyObject \*)&PyList\_Type);

See also

*   [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
    
*   [`PyObject_GC_NewVar`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_NewVar "PyObject_GC_NewVar")
    
*   [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
    
*   [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
    

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \_Py\_NoneStruct[¶](https://docs.python.org/3/c-api/allocation.html#c._Py_NoneStruct "Link to this definition")
  

Object which is visible in Python as `None`. This should only be accessed using the [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "Py_None")
 macro, which evaluates to a pointer to this object.

See also

[Module Objects](https://docs.python.org/3/c-api/module.html#moduleobjects)

To allocate and create extension modules.

Soft-deprecated aliases[¶](https://docs.python.org/3/c-api/allocation.html#soft-deprecated-aliases "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.

These are aliases to existing functions and macros. They exist solely for backwards compatibility.

| Soft-deprecated alias | Function |
| --- | --- |
| PyObject\_NEW(type, typeobj)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NEW "Link to this definition") | [`PyObject_New`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New") |
| PyObject\_NEW\_VAR(type, typeobj, n)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NEW_VAR "Link to this definition") | [`PyObject_NewVar`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar") |
| PyObject\_INIT(op, typeobj)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_INIT "Link to this definition") | [`PyObject_Init()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_Init "PyObject_Init") |
| PyObject\_INIT\_VAR(op, typeobj, n)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_INIT_VAR "Link to this definition") | [`PyObject_InitVar()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_InitVar "PyObject_InitVar") |
| PyObject\_MALLOC(n)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_MALLOC "Link to this definition") | [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc") |
| PyObject\_REALLOC(p, n)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_REALLOC "Link to this definition") | [`PyObject_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Realloc "PyObject_Realloc") |
| PyObject\_FREE(p)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_FREE "Link to this definition") | [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free") |
| PyObject\_DEL(p)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_DEL "Link to this definition") | [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free") |
| PyObject\_Del(p)[¶](https://docs.python.org/3/c-api/allocation.html#c.PyObject_Del "Link to this definition") | [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free") |

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Allocating objects on the heap](https://docs.python.org/3/c-api/allocation.html#)
    *   [Soft-deprecated aliases](https://docs.python.org/3/c-api/allocation.html#soft-deprecated-aliases)
        

#### Previous topic

[Object Implementation Support](https://docs.python.org/3/c-api/objimpl.html "previous chapter")

#### Next topic

[Object Life Cycle](https://docs.python.org/3/c-api/lifecycle.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Allocating+objects+on+the+heap&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fallocation.html&pagesource=c-api%2Fallocation.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/allocation.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/lifecycle.html "Object Life Cycle")
     |
*   [previous](https://docs.python.org/3/c-api/objimpl.html "Object Implementation Support")
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
*   [Object Implementation Support](https://docs.python.org/3/c-api/objimpl.html)
     »
*   [Allocating objects on the heap](https://docs.python.org/3/c-api/allocation.html)
    
*    
    
    |
*   Theme Auto Light Dark |