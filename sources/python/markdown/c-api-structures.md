### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/typeobj.html "Type Object Structures")
     |
*   [previous](https://docs.python.org/3/c-api/lifecycle.html "Object Life Cycle")
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
*   [Common Object Structures](https://docs.python.org/3/c-api/structures.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Common Object Structures[¶](https://docs.python.org/3/c-api/structures.html#common-object-structures "Link to this heading")

=============================================================================================================================

There are a large number of structures which are used in the definition of object types for Python. This section describes these structures and how they are used.

Base object types and macros[¶](https://docs.python.org/3/c-api/structures.html#base-object-types-and-macros "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

All Python objects ultimately share a small number of fields at the beginning of the object’s representation in memory. These are represented by the [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 and [`PyVarObject`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 types, which are defined, in turn, by the expansions of some macros also used, whether directly or indirectly, in the definition of all other Python objects. Additional macros can be found under [reference counting](https://docs.python.org/3/c-api/refcounting.html#countingrefs)
.

type PyObject[¶](https://docs.python.org/3/c-api/structures.html#c.PyObject "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (see below)._

All object types are extensions of this type. This is a type which contains the information Python needs to treat a pointer to an object as an object. In a normal “release” build, it contains only the object’s reference count and a pointer to the corresponding type object. Nothing is actually declared to be a [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
, but every pointer to a Python object can be cast to a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

The members must not be accessed directly; instead use macros such as [`Py_REFCNT`](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT")
 and [`Py_TYPE`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
.

In the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable-abi)
 for Free-Threaded Builds (`abi3t`), this struct is opaque; its size and layout may change between Python versions. In Stable ABI for non-free-threaded builds (`abi3`), the `ob_refcnt` and `ob_type` fields are available, but using them directly is discouraged.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 ob\_refcnt[¶](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_refcnt "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The object’s reference count, as returned by [`Py_REFCNT`](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT")
. Do not use this field directly; instead use functions and macros such as `Py_REFCNT`, [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "Py_INCREF")
 and [`Py_DecRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DecRef "Py_DecRef")
.

The field type may be different from `Py_ssize_t`, depending on build configuration and platform.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*ob\_type[¶](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The object’s type. Do not use this field directly; use [`Py_TYPE`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
 and [`Py_SET_TYPE()`](https://docs.python.org/3/c-api/structures.html#c.Py_SET_TYPE "Py_SET_TYPE")
 instead.

[PyMutex](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 ob\_mutex[¶](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_mutex "Link to this definition")
  

A [per-object lock](https://docs.python.org/3/howto/free-threading-extensions.html#per-object-locks)
, present only in the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build (when [`Py_GIL_DISABLED`](https://docs.python.org/3/using/configure.html#c.Py_GIL_DISABLED "Py_GIL_DISABLED")
 is defined).

This field is **reserved for use by the critical section API** ([`Py_BEGIN_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION "Py_BEGIN_CRITICAL_SECTION")
 / [`Py_END_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_END_CRITICAL_SECTION "Py_END_CRITICAL_SECTION")
). Do **not** lock it directly with `PyMutex_Lock`; doing so can cause deadlocks. If you need your own lock, add a separate [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 field to your object struct.

Added in version 3.13.

type PyVarObject[¶](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (see below)._

An extension of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 that adds the [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 field. This is intended for objects that have some notion of _length_.

As with `PyObject`, the members must not be accessed directly; instead use macros such as [`Py_SIZE`](https://docs.python.org/3/c-api/structures.html#c.Py_SIZE "Py_SIZE")
, [`Py_REFCNT`](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT")
 and [`Py_TYPE`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
.

In the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable-abi)
 for Free-Threaded Builds (`abi3t`), this struct is opaque; its size and layout may change between Python versions. In Stable ABI for non-free-threaded builds (`abi3`), the `ob_base` and `ob_size` fields are available, but using them directly is discouraged.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 ob\_base[¶](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_base "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Common object header. Typically, this field is not accessed directly; instead `PyVarObject` can be cast to [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 ob\_size[¶](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

A size field, whose contents should be considered an object’s internal implementation detail.

Do not use this field directly; use [`Py_SIZE`](https://docs.python.org/3/c-api/structures.html#c.Py_SIZE "Py_SIZE")
 instead.

Object creation functions such as [`PyObject_NewVar()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar")
 will generally set this field to the requested size (number of items). After creation, arbitrary values can be stored in `ob_size` using [`Py_SET_SIZE`](https://docs.python.org/3/c-api/structures.html#c.Py_SET_SIZE "Py_SET_SIZE")
.

To get an object’s publicly exposed length, as returned by the Python function [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
, use [`PyObject_Length()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Length "PyObject_Length")
 instead.

PyObject\_HEAD[¶](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "Link to this definition")
  

This is a macro used when declaring new types which represent objects without a varying length. The PyObject\_HEAD macro expands to:

PyObject ob\_base;

See documentation of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 above.

PyObject\_VAR\_HEAD[¶](https://docs.python.org/3/c-api/structures.html#c.PyObject_VAR_HEAD "Link to this definition")
  

This is a macro used when declaring new types which represent objects with a length that varies from instance to instance. The PyObject\_VAR\_HEAD macro expands to:

PyVarObject ob\_base;

See documentation of [`PyVarObject`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 above.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyBaseObject\_Type[¶](https://docs.python.org/3/c-api/structures.html#c.PyBaseObject_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The base class of all other objects, the same as [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
 in Python.

int Py\_Is([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*x, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*y)[¶](https://docs.python.org/3/c-api/structures.html#c.Py_Is "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Test if the _x_ object is the _y_ object, the same as `x is y` in Python.

Added in version 3.10.

int Py\_IsNone([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*x)[¶](https://docs.python.org/3/c-api/structures.html#c.Py_IsNone "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Test if an object is the `None` singleton, the same as `x is None` in Python.

Added in version 3.10.

int Py\_IsTrue([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*x)[¶](https://docs.python.org/3/c-api/structures.html#c.Py_IsTrue "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Test if an object is the `True` singleton, the same as `x is True` in Python.

Added in version 3.10.

int Py\_IsFalse([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*x)[¶](https://docs.python.org/3/c-api/structures.html#c.Py_IsFalse "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Test if an object is the `False` singleton, the same as `x is False` in Python.

Added in version 3.10.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*Py\_TYPE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Get the type of the Python object _o_.

The returned reference is [borrowed](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 from _o_. Do not release it with [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 or similar.

Changed in version 3.11: [`Py_TYPE()`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
 is changed to an inline static function. The parameter type is no longer const [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

int Py\_IS\_TYPE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/structures.html#c.Py_IS_TYPE "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Return non-zero if the object _o_ type is _type_. Return zero otherwise. Equivalent to: `Py_TYPE(o) == type`.

Added in version 3.9.

void Py\_SET\_TYPE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/structures.html#c.Py_SET_TYPE "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.9._

Set the type of object _o_ to _type_, without any checking or reference counting.

This is a very low-level operation. Consider instead setting the Python attribute [`__class__`](https://docs.python.org/3/reference/datamodel.html#object.__class__ "object.__class__")
 using [`PyObject_SetAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetAttrString "PyObject_SetAttrString")
 or similar.

Note that assigning an incompatible type can lead to undefined behavior.

If _type_ is a [heap type](https://docs.python.org/3/c-api/typeobj.html#heap-types)
, the caller must create a new reference to it. Similarly, if the old type of _o_ is a heap type, the caller must release a reference to that type.

Added in version 3.9.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 Py\_SIZE([PyVarObject](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 \*o)[¶](https://docs.python.org/3/c-api/structures.html#c.Py_SIZE "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Get the [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 field of _o_.

Changed in version 3.11: [`Py_SIZE()`](https://docs.python.org/3/c-api/structures.html#c.Py_SIZE "Py_SIZE")
 is changed to an inline static function. The parameter type is no longer const [PyVarObject](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
\*.

void Py\_SET\_SIZE([PyVarObject](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size)[¶](https://docs.python.org/3/c-api/structures.html#c.Py_SET_SIZE "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Set the [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 field of _o_ to _size_.

Added in version 3.9.

PyObject\_HEAD\_INIT(type)[¶](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD_INIT "Link to this definition")
  

This is a macro which expands to initialization values for a new [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 type. This macro expands to:

\_PyObject\_EXTRA\_INIT
1, type,

PyVarObject\_HEAD\_INIT(type, size)[¶](https://docs.python.org/3/c-api/structures.html#c.PyVarObject_HEAD_INIT "Link to this definition")
  

This is a macro which expands to initialization values for a new [`PyVarObject`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 type, including the [`ob_size`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject.ob_size "PyVarObject.ob_size")
 field. This macro expands to:

\_PyObject\_EXTRA\_INIT
1, type, size,

Implementing functions and methods[¶](https://docs.python.org/3/c-api/structures.html#implementing-functions-and-methods "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

type PyCFunction[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Type of the functions used to implement most Python callables in C. Functions of this type take two [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* parameters and return one such value. If the return value is `NULL`, an exception shall have been set. If not `NULL`, the return value is interpreted as the return value of the function as exposed in Python. The function must return a new reference.

The function signature is:

PyObject \*PyCFunction(PyObject \*self,
                      PyObject \*args);

type PyCFunctionWithKeywords[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunctionWithKeywords "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Type of the functions used to implement Python callables in C with signature [METH\_VARARGS | METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#meth-varargs-meth-keywords)
. The function signature is:

PyObject \*PyCFunctionWithKeywords(PyObject \*self,
                                  PyObject \*args,
                                  PyObject \*kwargs);

type PyCFunctionFast[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunctionFast "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Type of the functions used to implement Python callables in C with signature [`METH_FASTCALL`](https://docs.python.org/3/c-api/structures.html#c.METH_FASTCALL "METH_FASTCALL")
. The function signature is:

PyObject \*PyCFunctionFast(PyObject \*self,
                          PyObject \*const \*args,
                          Py\_ssize\_t nargs);

type PyCFunctionFastWithKeywords[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunctionFastWithKeywords "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Type of the functions used to implement Python callables in C with signature [METH\_FASTCALL | METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#meth-fastcall-meth-keywords)
. The function signature is:

PyObject \*PyCFunctionFastWithKeywords(PyObject \*self,
                                      PyObject \*const \*args,
                                      Py\_ssize\_t nargs,
                                      PyObject \*kwnames);

type PyCMethod[¶](https://docs.python.org/3/c-api/structures.html#c.PyCMethod "Link to this definition")
  

Type of the functions used to implement Python callables in C with signature [METH\_METHOD | METH\_FASTCALL | METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#meth-method-meth-fastcall-meth-keywords)
. The function signature is:

PyObject \*PyCMethod(PyObject \*self,
                    PyTypeObject \*defining\_class,
                    PyObject \*const \*args,
                    Py\_ssize\_t nargs,
                    PyObject \*kwnames)

Added in version 3.9.

type PyMethodDef[¶](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members)._

Structure used to describe a method of an extension type. This structure has four fields:

const char \*ml\_name[¶](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_name "Link to this definition")
  

Name of the method.

A `NULL` _ml\_name_ marks the end of a `PyMethodDef` array.

[PyCFunction](https://docs.python.org/3/c-api/structures.html#c.PyCFunction "PyCFunction")
 ml\_meth[¶](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_meth "Link to this definition")
  

Pointer to the C implementation.

int ml\_flags[¶](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_flags "Link to this definition")
  

Flags bits indicating how the call should be constructed.

const char \*ml\_doc[¶](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_doc "Link to this definition")
  

Points to the contents of the docstring.

The [`ml_meth`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_meth "PyMethodDef.ml_meth")
 is a C function pointer. The functions may be of different types, but they always return [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*. If the function is not of the [`PyCFunction`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction "PyCFunction")
, the compiler will require a cast in the method table. Even though `PyCFunction` defines the first parameter as PyObject\*, it is common that the method implementation uses the specific C type of the _self_ object.

The [`ml_flags`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_flags "PyMethodDef.ml_flags")
 field is a bitfield which can include the following flags. The individual flags indicate either a calling convention or a binding convention.

There are these calling conventions:

METH\_VARARGS[¶](https://docs.python.org/3/c-api/structures.html#c.METH_VARARGS "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the typical calling convention, where the methods have the type [`PyCFunction`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction "PyCFunction")
. The function expects two [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* values. The first one is the _self_ object for methods; for module functions, it is the module object. The second parameter (often called _args_) is a tuple object representing all arguments. This parameter is typically processed using [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
 or [`PyArg_UnpackTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple "PyArg_UnpackTuple")
.

METH\_KEYWORDS[¶](https://docs.python.org/3/c-api/structures.html#c.METH_KEYWORDS "Link to this definition")
  

Can only be used in certain combinations with other flags: [METH\_VARARGS | METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#meth-varargs-meth-keywords)
, [METH\_FASTCALL | METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#meth-fastcall-meth-keywords)
 and [METH\_METHOD | METH\_FASTCALL | METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#meth-method-meth-fastcall-meth-keywords)
.

[METH\_VARARGS](https://docs.python.org/3/c-api/structures.html#c.METH_VARARGS "METH_VARARGS")
 | [METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#c.METH_KEYWORDS "METH_KEYWORDS")

Methods with these flags must be of type [`PyCFunctionWithKeywords`](https://docs.python.org/3/c-api/structures.html#c.PyCFunctionWithKeywords "PyCFunctionWithKeywords")
. The function expects three parameters: _self_, _args_, _kwargs_ where _kwargs_ is a dictionary of all the keyword arguments or possibly `NULL` if there are no keyword arguments. The parameters are typically processed using [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "PyArg_ParseTupleAndKeywords")
.

METH\_FASTCALL[¶](https://docs.python.org/3/c-api/structures.html#c.METH_FASTCALL "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Fast calling convention supporting only positional arguments. The methods have the type [`PyCFunctionFast`](https://docs.python.org/3/c-api/structures.html#c.PyCFunctionFast "PyCFunctionFast")
. The first parameter is _self_, the second parameter is a C array of [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* values indicating the arguments and the third parameter is the number of arguments (the length of the array).

Added in version 3.7.

Changed in version 3.10: `METH_FASTCALL` is now part of the [stable ABI](https://docs.python.org/3/c-api/stable.html#stable-abi)
.

[METH\_FASTCALL](https://docs.python.org/3/c-api/structures.html#c.METH_FASTCALL "METH_FASTCALL")
 | [METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#c.METH_KEYWORDS "METH_KEYWORDS")

Extension of [`METH_FASTCALL`](https://docs.python.org/3/c-api/structures.html#c.METH_FASTCALL "METH_FASTCALL")
 supporting also keyword arguments, with methods of type [`PyCFunctionFastWithKeywords`](https://docs.python.org/3/c-api/structures.html#c.PyCFunctionFastWithKeywords "PyCFunctionFastWithKeywords")
. Keyword arguments are passed the same way as in the [vectorcall protocol](https://docs.python.org/3/c-api/call.html#vectorcall)
: there is an additional fourth [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* parameter which is a tuple representing the names of the keyword arguments (which are guaranteed to be strings) or possibly `NULL` if there are no keywords. The values of the keyword arguments are stored in the _args_ array, after the positional arguments.

Added in version 3.7.

METH\_METHOD[¶](https://docs.python.org/3/c-api/structures.html#c.METH_METHOD "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Can only be used in the combination with other flags: [METH\_METHOD | METH\_FASTCALL | METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#meth-method-meth-fastcall-meth-keywords)
.

[METH\_METHOD](https://docs.python.org/3/c-api/structures.html#c.METH_METHOD "METH_METHOD")
 | [METH\_FASTCALL](https://docs.python.org/3/c-api/structures.html#c.METH_FASTCALL "METH_FASTCALL")
 | [METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#c.METH_KEYWORDS "METH_KEYWORDS")

Extension of [METH\_FASTCALL | METH\_KEYWORDS](https://docs.python.org/3/c-api/structures.html#meth-fastcall-meth-keywords)
 supporting the _defining class_, that is, the class that contains the method in question. The defining class might be a superclass of `Py_TYPE(self)`.

The method needs to be of type [`PyCMethod`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod "PyCMethod")
, the same as for `METH_FASTCALL | METH_KEYWORDS` with `defining_class` argument added after `self`.

Added in version 3.9.

METH\_NOARGS[¶](https://docs.python.org/3/c-api/structures.html#c.METH_NOARGS "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Methods without parameters don’t need to check whether arguments are given if they are listed with the [`METH_NOARGS`](https://docs.python.org/3/c-api/structures.html#c.METH_NOARGS "METH_NOARGS")
 flag. They need to be of type [`PyCFunction`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction "PyCFunction")
. The first parameter is typically named _self_ and will hold a reference to the module or object instance. In all cases the second parameter will be `NULL`.

The function must have 2 parameters. Since the second parameter is unused, [`Py_UNUSED`](https://docs.python.org/3/c-api/intro.html#c.Py_UNUSED "Py_UNUSED")
 can be used to prevent a compiler warning.

METH\_O[¶](https://docs.python.org/3/c-api/structures.html#c.METH_O "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Methods with a single object argument can be listed with the [`METH_O`](https://docs.python.org/3/c-api/structures.html#c.METH_O "METH_O")
 flag, instead of invoking [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
 with a `"O"` argument. They have the type [`PyCFunction`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction "PyCFunction")
, with the _self_ parameter, and a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* parameter representing the single argument.

These two constants are not used to indicate the calling convention but the binding when used with methods of classes. These may not be used for functions defined for modules. At most one of these flags may be set for any given method.

METH\_CLASS[¶](https://docs.python.org/3/c-api/structures.html#c.METH_CLASS "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The method will be passed the type object as the first parameter rather than an instance of the type. This is used to create _class methods_, similar to what is created when using the [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
 built-in decorator.

METH\_STATIC[¶](https://docs.python.org/3/c-api/structures.html#c.METH_STATIC "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The method will be passed `NULL` as the first parameter rather than an instance of the type. This is used to create _static methods_, similar to what is created when using the [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
 built-in decorator.

One other constant controls whether a method is loaded in place of another definition with the same method name.

METH\_COEXIST[¶](https://docs.python.org/3/c-api/structures.html#c.METH_COEXIST "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The method will be loaded in place of existing definitions. Without _METH\_COEXIST_, the default is to skip repeated definitions. Since slot wrappers are loaded before the method table, the existence of a _sq\_contains_ slot, for example, would generate a wrapped method named [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__")
 and preclude the loading of a corresponding PyCFunction with the same name. With the flag defined, the PyCFunction will be loaded in place of the wrapper object and will co-exist with the slot. This is helpful because calls to PyCFunctions are optimized more than wrapper object calls.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyCMethod\_Type[¶](https://docs.python.org/3/c-api/structures.html#c.PyCMethod_Type "Link to this definition")
  

The type object corresponding to Python C method objects. This is available as [`types.BuiltinMethodType`](https://docs.python.org/3/library/types.html#types.BuiltinMethodType "types.BuiltinMethodType")
 in the Python layer.

int PyCMethod\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCMethod_Check "Link to this definition")
  

Return true if _op_ is an instance of the [`PyCMethod_Type`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod_Type "PyCMethod_Type")
 type or a subtype of it. This function always succeeds.

int PyCMethod\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCMethod_CheckExact "Link to this definition")
  

This is the same as [`PyCMethod_Check()`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod_Check "PyCMethod_Check")
, but does not account for subtypes.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCMethod\_New([PyMethodDef](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 \*ml, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*cls)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCMethod_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.9._

Turn _ml_ into a Python [callable](https://docs.python.org/3/glossary.html#term-callable)
 object. The caller must ensure that _ml_ outlives the callable. Typically, _ml_ is defined as a static variable.

The _self_ parameter will be passed as the _self_ argument to the C function in `ml->ml_meth` when invoked. _self_ can be `NULL`.

The [callable](https://docs.python.org/3/glossary.html#term-callable)
 object’s `__module__` attribute can be set from the given _module_ argument. _module_ should be a Python string, which will be used as name of the module the function is defined in. If unavailable, it can be set to [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 or `NULL`.

See also

[`function.__module__`](https://docs.python.org/3/reference/datamodel.html#function.__module__ "function.__module__")

The _cls_ parameter will be passed as the _defining\_class_ argument to the C function. Must be set if [`METH_METHOD`](https://docs.python.org/3/c-api/structures.html#c.METH_METHOD "METH_METHOD")
 is set on `ml->ml_flags`.

Added in version 3.9.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyCFunction\_Type[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object corresponding to Python C function objects. This is available as [`types.BuiltinFunctionType`](https://docs.python.org/3/library/types.html#types.BuiltinFunctionType "types.BuiltinFunctionType")
 in the Python layer.

int PyCFunction\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_Check "Link to this definition")
  

Return true if _op_ is an instance of the [`PyCFunction_Type`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_Type "PyCFunction_Type")
 type or a subtype of it. This function always succeeds.

int PyCFunction\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_CheckExact "Link to this definition")
  

This is the same as [`PyCFunction_Check()`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_Check "PyCFunction_Check")
, but does not account for subtypes.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCFunction\_NewEx([PyMethodDef](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 \*ml, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_NewEx "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Equivalent to `PyCMethod_New(ml, self, module, NULL)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCFunction\_New([PyMethodDef](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 \*ml, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.4._

Equivalent to `PyCMethod_New(ml, self, NULL, NULL)`.

int PyCFunction\_GetFlags([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GetFlags "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get the function’s flags on _func_ as they were passed to [`ml_flags`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_flags "PyMethodDef.ml_flags")
.

If _func_ is not a C function object, this fails with an exception. _func_ must not be `NULL`.

This function returns the function’s flags on success, and `-1` with an exception set on failure.

int PyCFunction\_GET\_FLAGS([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GET_FLAGS "Link to this definition")
  

This is the same as [`PyCFunction_GetFlags()`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GetFlags "PyCFunction_GetFlags")
, but without error or type checking.

[PyCFunction](https://docs.python.org/3/c-api/structures.html#c.PyCFunction "PyCFunction")
 PyCFunction\_GetFunction([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GetFunction "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get the function pointer on _func_ as it was passed to [`ml_meth`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_meth "PyMethodDef.ml_meth")
.

If _func_ is not a C function object, this fails with an exception. _func_ must not be `NULL`.

This function returns the function pointer on success, and `NULL` with an exception set on failure.

int PyCFunction\_GET\_FUNCTION([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GET_FUNCTION "Link to this definition")
  

This is the same as [`PyCFunction_GetFunction()`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GetFunction "PyCFunction_GetFunction")
, but without error or type checking.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCFunction\_GetSelf([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GetSelf "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get the “self” object on _func_. This is the object that would be passed to the first argument of a [`PyCFunction`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction "PyCFunction")
. For C function objects created through a [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 on a [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
, this is the resulting module object.

If _func_ is not a C function object, this fails with an exception. _func_ must not be `NULL`.

This function returns a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 to the “self” object on success, and `NULL` with an exception set on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCFunction\_GET\_SELF([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GET_SELF "Link to this definition")
  

This is the same as [`PyCFunction_GetSelf()`](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GetSelf "PyCFunction_GetSelf")
, but without error or type checking.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*PyCFunction\_GET\_CLASS([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func)[¶](https://docs.python.org/3/c-api/structures.html#c.PyCFunction_GET_CLASS "Link to this definition")
  

Return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 to the defining class of _func_ if its [`ml_flags`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef.ml_flags "PyMethodDef.ml_flags")
 includes [`METH_METHOD`](https://docs.python.org/3/c-api/structures.html#c.METH_METHOD "METH_METHOD")
. Otherwise, return `NULL` without setting an exception.

_func_ must be a C function object and must not be `NULL`. This function does not perform error or type checking.

Added in version 3.9.

Accessing attributes of extension types[¶](https://docs.python.org/3/c-api/structures.html#accessing-attributes-of-extension-types "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

type PyMemberDef[¶](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members)._

Structure which describes an attribute of a type which corresponds to a C struct member. When defining a class, put a NULL-terminated array of these structures in the [`tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_members "PyTypeObject.tp_members")
 slot.

Its fields are, in order:

const char \*name[¶](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.name "Link to this definition")
  

Name of the member. A NULL value marks the end of a `PyMemberDef[]` array.

The string should be static, no copy is made of it.

int type[¶](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.type "Link to this definition")
  

The type of the member in the C struct. See [Member types](https://docs.python.org/3/c-api/structures.html#pymemberdef-types)
 for the possible values.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 offset[¶](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.offset "Link to this definition")
  

The offset in bytes that the member is located on the type’s object struct.

int flags[¶](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.flags "Link to this definition")
  

Zero or more of the [Member flags](https://docs.python.org/3/c-api/structures.html#pymemberdef-flags)
, combined using bitwise OR.

const char \*doc[¶](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.doc "Link to this definition")
  

The docstring, or NULL. The string should be static, no copy is made of it. Typically, it is defined using [`PyDoc_STR`](https://docs.python.org/3/c-api/intro.html#c.PyDoc_STR "PyDoc_STR")
.

By default (when [`flags`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.flags "PyMemberDef.flags")
 is `0`), members allow both read and write access. Use the [`Py_READONLY`](https://docs.python.org/3/c-api/structures.html#c.Py_READONLY "Py_READONLY")
 flag for read-only access. Certain types, like [`Py_T_STRING`](https://docs.python.org/3/c-api/structures.html#c.Py_T_STRING "Py_T_STRING")
, imply `Py_READONLY`. Only [`Py_T_OBJECT_EX`](https://docs.python.org/3/c-api/structures.html#c.Py_T_OBJECT_EX "Py_T_OBJECT_EX")
 (and legacy [`T_OBJECT`](https://docs.python.org/3/c-api/structures.html#c.T_OBJECT "T_OBJECT")
) members can be deleted.

For heap-allocated types (created using [`PyType_FromSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec "PyType_FromSpec")
 or similar), `PyMemberDef` may contain a definition for the special member `"__vectorcalloffset__"`, corresponding to [`tp_vectorcall_offset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall_offset "PyTypeObject.tp_vectorcall_offset")
 in type objects. This member must be defined with `Py_T_PYSSIZET`, and either `Py_READONLY` or `Py_READONLY | Py_RELATIVE_OFFSET`. For example:

static PyMemberDef spam\_type\_members\[\] \= {
    {"\_\_vectorcalloffset\_\_", Py\_T\_PYSSIZET,
     offsetof(Spam\_object, vectorcall), Py\_READONLY},
    {NULL}  /\* Sentinel \*/
};

(You may need to `#include <stddef.h>` for `offsetof()`.)

The legacy offsets [`tp_dictoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dictoffset "PyTypeObject.tp_dictoffset")
 and [`tp_weaklistoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset "PyTypeObject.tp_weaklistoffset")
 can be defined similarly using `"__dictoffset__"` and `"__weaklistoffset__"` members, but extensions are strongly encouraged to use [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
 and [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF "Py_TPFLAGS_MANAGED_WEAKREF")
 instead.

Changed in version 3.12: `PyMemberDef` is always available. Previously, it required including `"structmember.h"`.

Changed in version 3.14: [`Py_RELATIVE_OFFSET`](https://docs.python.org/3/c-api/structures.html#c.Py_RELATIVE_OFFSET "Py_RELATIVE_OFFSET")
 is now allowed for `"__vectorcalloffset__"`, `"__dictoffset__"` and `"__weaklistoffset__"`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMember\_GetOne(const char \*obj\_addr, struct [PyMemberDef](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")
 \*m)[¶](https://docs.python.org/3/c-api/structures.html#c.PyMember_GetOne "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Get an attribute belonging to the object at address _obj\_addr_. The attribute is described by `PyMemberDef` _m_. Returns `NULL` on error.

Changed in version 3.12: `PyMember_GetOne` is always available. Previously, it required including `"structmember.h"`.

int PyMember\_SetOne(char \*obj\_addr, struct [PyMemberDef](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")
 \*m, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/structures.html#c.PyMember_SetOne "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Set an attribute belonging to the object at address _obj\_addr_ to object _o_. The attribute to set is described by `PyMemberDef` _m_. Returns `0` if successful and a negative value on failure.

Changed in version 3.12: `PyMember_SetOne` is always available. Previously, it required including `"structmember.h"`.

### Member flags[¶](https://docs.python.org/3/c-api/structures.html#member-flags "Link to this heading")

The following flags can be used with [`PyMemberDef.flags`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.flags "PyMemberDef.flags")
:

Py\_READONLY[¶](https://docs.python.org/3/c-api/structures.html#c.Py_READONLY "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Not writable.

Py\_AUDIT\_READ[¶](https://docs.python.org/3/c-api/structures.html#c.Py_AUDIT_READ "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Emit an `object.__getattr__` [audit event](https://docs.python.org/3/library/audit_events.html#audit-events)
 before reading.

Py\_RELATIVE\_OFFSET[¶](https://docs.python.org/3/c-api/structures.html#c.Py_RELATIVE_OFFSET "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Indicates that the [`offset`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.offset "PyMemberDef.offset")
 of this `PyMemberDef` entry indicates an offset from the subclass-specific data, rather than from `PyObject`.

Can only be used as part of the [`Py_tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_members "Py_tp_members")
 [`slot`](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 when creating a class using negative [`basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
. It is mandatory in that case. When setting [`tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_members "PyTypeObject.tp_members")
 from the slot during class creation, Python clears the flag and sets [`PyMemberDef.offset`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.offset "PyMemberDef.offset")
 to the offset from the `PyObject` struct.

Changed in version 3.10: The `RESTRICTED`, `READ_RESTRICTED` and `WRITE_RESTRICTED` macros available with `#include "structmember.h"` are deprecated. `READ_RESTRICTED` and `RESTRICTED` are equivalent to [`Py_AUDIT_READ`](https://docs.python.org/3/c-api/structures.html#c.Py_AUDIT_READ "Py_AUDIT_READ")
; `WRITE_RESTRICTED` does nothing.

Changed in version 3.12: The `READONLY` macro was renamed to [`Py_READONLY`](https://docs.python.org/3/c-api/structures.html#c.Py_READONLY "Py_READONLY")
. The [`PY_AUDIT_READ`](https://docs.python.org/3/c-api/structures.html#c.PY_AUDIT_READ "PY_AUDIT_READ")
 macro was renamed with the `Py_` prefix. The new names are now always available. Previously, these required `#include "structmember.h"`. The header is still available and it provides the old names.

PY\_AUDIT\_READ[¶](https://docs.python.org/3/c-api/structures.html#c.PY_AUDIT_READ "Link to this definition")
  

Soft-deprecated alias of [`Py_AUDIT_READ`](https://docs.python.org/3/c-api/structures.html#c.Py_AUDIT_READ "Py_AUDIT_READ")
 (note capitalization of the `y`). Only available with `#include "structmember.h"`.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.12: Use [`Py_AUDIT_READ`](https://docs.python.org/3/c-api/structures.html#c.Py_AUDIT_READ "Py_AUDIT_READ")
 instead.

PY\_WRITE\_RESTRICTED[¶](https://docs.python.org/3/c-api/structures.html#c.PY_WRITE_RESTRICTED "Link to this definition")
  

A member flag that has no effect, retained solely for backwards compatibility. This is only available with `#include "structmember.h"`.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.2: Omit this flag instead.

### Member types[¶](https://docs.python.org/3/c-api/structures.html#member-types "Link to this heading")

[`PyMemberDef.type`](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef.type "PyMemberDef.type")
 can be one of the following macros corresponding to various C types. When the member is accessed in Python, it will be converted to the equivalent Python type. When it is set from Python, it will be converted back to the C type. If that is not possible, an exception such as [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 or [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised.

Unless marked (D), attributes defined this way cannot be deleted using e.g. [`del`](https://docs.python.org/3/reference/simple_stmts.html#del)
 or [`delattr()`](https://docs.python.org/3/builtins/functions.html#delattr "delattr")
.

These values are available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12.

| Macro name | C type | Python type |
| --- | --- | --- |
| Py\_T\_BYTE[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_BYTE "Link to this definition") | char | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_SHORT[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_SHORT "Link to this definition") | short | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_INT[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_INT "Link to this definition") | int | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_LONG[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_LONG "Link to this definition") | long | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_LONGLONG[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_LONGLONG "Link to this definition") | long long | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_UBYTE[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_UBYTE "Link to this definition") | unsigned char | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_UINT[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_UINT "Link to this definition") | unsigned int | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_USHORT[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_USHORT "Link to this definition") | unsigned short | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_ULONG[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_ULONG "Link to this definition") | unsigned long | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_ULONGLONG[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_ULONGLONG "Link to this definition") | unsigned long long | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_PYSSIZET[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_PYSSIZET "Link to this definition") | [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") | [`int`](https://docs.python.org/3/builtins/functions.html#int "int") |
| Py\_T\_FLOAT[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_FLOAT "Link to this definition") | float | [`float`](https://docs.python.org/3/builtins/functions.html#float "float") |
| Py\_T\_DOUBLE[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_DOUBLE "Link to this definition") | double | [`float`](https://docs.python.org/3/builtins/functions.html#float "float") |
| Py\_T\_BOOL[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_BOOL "Link to this definition") | char (written as 0 or 1) | [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool") |
| Py\_T\_STRING[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_STRING "Link to this definition") | const char\* (\*) | [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")<br> (RO) |
| Py\_T\_STRING\_INPLACE[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_STRING_INPLACE "Link to this definition") | const char\[\] (\*) | [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")<br> (RO) |
| Py\_T\_CHAR[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_CHAR "Link to this definition") | char (0-127) | [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")<br> (\*\*) |
| Py\_T\_OBJECT\_EX[¶](https://docs.python.org/3/c-api/structures.html#c.Py_T_OBJECT_EX "Link to this definition") | [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")<br>\* | [`object`](https://docs.python.org/3/builtins/functions.html#object "object")<br> (D) |

> (\*): Zero-terminated, UTF8-encoded C string. With `Py_T_STRING` the C representation is a pointer; with `Py_T_STRING_INPLACE` the string is stored directly in the structure.
> 
> (\*\*): String of length 1. Only ASCII is accepted.
> 
> (RO): Implies [`Py_READONLY`](https://docs.python.org/3/c-api/structures.html#c.Py_READONLY "Py_READONLY")
> .
> 
> (D): Can be deleted, in which case the pointer is set to `NULL`. Reading a `NULL` pointer raises [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
> .

Added in version 3.12: In previous versions, the macros were only available with `#include "structmember.h"` and were named without the `Py_` prefix (e.g. as `T_INT`). The header is still available and contains the old names, along with the following deprecated types:

T\_OBJECT[¶](https://docs.python.org/3/c-api/structures.html#c.T_OBJECT "Link to this definition")
  

Like `Py_T_OBJECT_EX`, but `NULL` is converted to `None`. This results in surprising behavior in Python: deleting the attribute effectively sets it to `None`.

T\_NONE[¶](https://docs.python.org/3/c-api/structures.html#c.T_NONE "Link to this definition")
  

Always `None`. Must be used with [`Py_READONLY`](https://docs.python.org/3/c-api/structures.html#c.Py_READONLY "Py_READONLY")
.

### Defining Getters and Setters[¶](https://docs.python.org/3/c-api/structures.html#defining-getters-and-setters "Link to this heading")

type PyGetSetDef[¶](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members)._

Structure to define property-like access for a type. See also description of the [`PyTypeObject.tp_getset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_getset "PyTypeObject.tp_getset")
 slot.

const char \*name[¶](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef.name "Link to this definition")
  

attribute name

[getter](https://docs.python.org/3/c-api/structures.html#c.getter "getter")
 get[¶](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef.get "Link to this definition")
  

C function to get the attribute.

[setter](https://docs.python.org/3/c-api/structures.html#c.setter "setter")
 set[¶](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef.set "Link to this definition")
  

Optional C function to set or delete the attribute. If `NULL`, the attribute is read-only.

const char \*doc[¶](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef.doc "Link to this definition")
  

optional docstring

void \*closure[¶](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef.closure "Link to this definition")
  

Optional user data pointer, providing additional data for getter and setter.

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*getter)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, void\*)[¶](https://docs.python.org/3/c-api/structures.html#c.getter "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The `get` function takes one [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* parameter (the instance) and a user data pointer (the associated `closure`):

It should return a new reference on success or `NULL` with a set exception on failure.

typedef int (\*setter)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, void\*)[¶](https://docs.python.org/3/c-api/structures.html#c.setter "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

`set` functions take two [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* parameters (the instance and the value to be set) and a user data pointer (the associated `closure`):

In case the attribute should be deleted the second parameter is `NULL`. Should return `0` on success or `-1` with a set exception on failure.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Common Object Structures](https://docs.python.org/3/c-api/structures.html#)
    *   [Base object types and macros](https://docs.python.org/3/c-api/structures.html#base-object-types-and-macros)
        
    *   [Implementing functions and methods](https://docs.python.org/3/c-api/structures.html#implementing-functions-and-methods)
        
    *   [Accessing attributes of extension types](https://docs.python.org/3/c-api/structures.html#accessing-attributes-of-extension-types)
        *   [Member flags](https://docs.python.org/3/c-api/structures.html#member-flags)
            
        *   [Member types](https://docs.python.org/3/c-api/structures.html#member-types)
            
        *   [Defining Getters and Setters](https://docs.python.org/3/c-api/structures.html#defining-getters-and-setters)
            

#### Previous topic

[Object Life Cycle](https://docs.python.org/3/c-api/lifecycle.html "previous chapter")

#### Next topic

[Type Object Structures](https://docs.python.org/3/c-api/typeobj.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Common+Object+Structures&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fstructures.html&pagesource=c-api%2Fstructures.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/structures.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/typeobj.html "Type Object Structures")
     |
*   [previous](https://docs.python.org/3/c-api/lifecycle.html "Object Life Cycle")
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
*   [Common Object Structures](https://docs.python.org/3/c-api/structures.html)
    
*    
    
    |
*   Theme Auto Light Dark |