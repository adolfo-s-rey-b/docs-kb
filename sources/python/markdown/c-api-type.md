### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/none.html "The None Object")
     |
*   [previous](https://docs.python.org/3/c-api/concrete.html "Concrete Objects Layer")
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
*   [Type Objects](https://docs.python.org/3/c-api/type.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Type Objects[¶](https://docs.python.org/3/c-api/type.html#type-objects "Link to this heading")

===============================================================================================

type PyTypeObject[¶](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (as an opaque struct)._

The C structure of the objects used to describe built-in types.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyType\_Type[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the type object for type objects; it is the same object as [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
 in the Python layer.

int PyType\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Check "Link to this definition")
  

Return non-zero if the object _o_ is a type object, including instances of types derived from the standard type object. Return 0 in all other cases. This function always succeeds.

int PyType\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_CheckExact "Link to this definition")
  

Return non-zero if the object _o_ is a type object, but not a subtype of the standard type object. Return 0 in all other cases. This function always succeeds.

unsigned int PyType\_ClearCache()[¶](https://docs.python.org/3/c-api/type.html#c.PyType_ClearCache "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Clear the internal lookup cache. Return the current version tag.

unsigned long PyType\_GetFlags([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetFlags "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
 member of _type_. This function is primarily meant for use with `Py_LIMITED_API`; the individual flag bits are guaranteed to be stable across Python releases, but access to `tp_flags` itself is not part of the [limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
.

Added in version 3.2.

Changed in version 3.4: The return type is now `unsigned long` rather than `long`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GetDict([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetDict "Link to this definition")
  

Return the type object’s internal namespace, which is otherwise only exposed via a read-only proxy ([`cls.__dict__`](https://docs.python.org/3/reference/datamodel.html#type.__dict__ "type.__dict__")
). This is a replacement for accessing [`tp_dict`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dict "PyTypeObject.tp_dict")
 directly. The returned dictionary must be treated as read-only.

This function is meant for specific embedding and language-binding cases, where direct access to the dict is necessary and indirect access (e.g. via the proxy or [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
) isn’t adequate.

Extension modules should continue to use `tp_dict`, directly or indirectly, when setting up their own types.

Added in version 3.12.

void PyType\_Modified([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Modified "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Invalidate the internal lookup cache for the type and all of its subtypes. This function must be called after any manual modification of the attributes or base classes of the type.

int PyType\_AddWatcher([PyType\_WatchCallback](https://docs.python.org/3/c-api/type.html#c.PyType_WatchCallback "PyType_WatchCallback")
 callback)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_AddWatcher "Link to this definition")
  

Register _callback_ as a type watcher. Return a non-negative integer ID which must be passed to future calls to [`PyType_Watch()`](https://docs.python.org/3/c-api/type.html#c.PyType_Watch "PyType_Watch")
. In case of error (e.g. no more watcher IDs available), return `-1` and set an exception.

In free-threaded builds, [`PyType_AddWatcher()`](https://docs.python.org/3/c-api/type.html#c.PyType_AddWatcher "PyType_AddWatcher")
 is not thread-safe, so it must be called at start up (before spawning the first thread).

Added in version 3.12.

int PyType\_ClearWatcher(int watcher\_id)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_ClearWatcher "Link to this definition")
  

Clear watcher identified by _watcher\_id_ (previously returned from [`PyType_AddWatcher()`](https://docs.python.org/3/c-api/type.html#c.PyType_AddWatcher "PyType_AddWatcher")
). Return `0` on success, `-1` on error (e.g. if _watcher\_id_ was never registered.)

An extension should never call `PyType_ClearWatcher` with a _watcher\_id_ that was not returned to it by a previous call to [`PyType_AddWatcher()`](https://docs.python.org/3/c-api/type.html#c.PyType_AddWatcher "PyType_AddWatcher")
.

Added in version 3.12.

int PyType\_Watch(int watcher\_id, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Watch "Link to this definition")
  

Mark _type_ as watched. The callback granted _watcher\_id_ by [`PyType_AddWatcher()`](https://docs.python.org/3/c-api/type.html#c.PyType_AddWatcher "PyType_AddWatcher")
 will be called whenever [`PyType_Modified()`](https://docs.python.org/3/c-api/type.html#c.PyType_Modified "PyType_Modified")
 reports a change to _type_. (The callback may be called only once for a series of consecutive modifications to _type_, if `_PyType_Lookup()` is not called on _type_ between the modifications; this is an implementation detail and subject to change.)

The callback is also invoked when a watched heap type is deallocated.

An extension should never call `PyType_Watch` with a _watcher\_id_ that was not returned to it by a previous call to [`PyType_AddWatcher()`](https://docs.python.org/3/c-api/type.html#c.PyType_AddWatcher "PyType_AddWatcher")
.

Added in version 3.12.

Changed in version 3.15: The callback is now also invoked when a watched heap type is deallocated.

int PyType\_Unwatch(int watcher\_id, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Unwatch "Link to this definition")
  

Mark _type_ as not watched. This undoes a previous call to [`PyType_Watch()`](https://docs.python.org/3/c-api/type.html#c.PyType_Watch "PyType_Watch")
. _type_ must not be `NULL`.

An extension should never call this function with a _watcher\_id_ that was not returned to it by a previous call to [`PyType_AddWatcher()`](https://docs.python.org/3/c-api/type.html#c.PyType_AddWatcher "PyType_AddWatcher")
.

On success, this function returns `0`. On failure, this function returns `-1` with an exception set.

Added in version 3.12.

typedef int (\*PyType\_WatchCallback)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_WatchCallback "Link to this definition")
  

Type of a type-watcher callback function.

The callback must not modify _type_ or cause [`PyType_Modified()`](https://docs.python.org/3/c-api/type.html#c.PyType_Modified "PyType_Modified")
 to be called on _type_ or any type in its MRO; violating this rule could cause infinite recursion.

The callback may be called during type deallocation. In this case, the type object is temporarily resurrected (its reference count is at least 1) and all its attributes are still valid. However, the callback should not store new strong references to the type, as this would resurrect the object and prevent its deallocation.

Added in version 3.12.

Changed in version 3.15: The callback may now be called during deallocation of a watched heap type.

int PyType\_HasFeature([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*o, int feature)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_HasFeature "Link to this definition")
  

Return non-zero if the type object _o_ sets the feature _feature_. Type features are denoted by single bit flags.

int PyType\_FastSubclass([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, int flag)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_FastSubclass "Link to this definition")
  

Return non-zero if the type object _type_ sets the subclass flag _flag_. Subclass flags are denoted by [`Py_TPFLAGS_*_SUBCLASS`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_LONG_SUBCLASS "Py_TPFLAGS_LONG_SUBCLASS")
. This function is used by many `_Check` functions for common types.

See also

[`PyObject_TypeCheck()`](https://docs.python.org/3/c-api/object.html#c.PyObject_TypeCheck "PyObject_TypeCheck")
, which is used as a slower alternative in `_Check` functions for types that don’t come with subclass flags.

int PyType\_IS\_GC([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*o)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_IS_GC "Link to this definition")
  

Return true if the type object includes support for the cycle detector; this tests the type flag [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
.

int PyType\_IsSubtype([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*a, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*b)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_IsSubtype "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return true if _a_ is a subtype of _b_.

This function only checks for actual subtypes, which means that [`__subclasscheck__()`](https://docs.python.org/3/reference/datamodel.html#type.__subclasscheck__ "type.__subclasscheck__")
 is not called on _b_. Call [`PyObject_IsSubclass()`](https://docs.python.org/3/c-api/object.html#c.PyObject_IsSubclass "PyObject_IsSubclass")
 to do the same check that [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")
 would do.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GenericAlloc([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 nitems)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Generic handler for the [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot of a type object. Uses Python’s default memory allocation mechanism to allocate memory for a new instance, zeros the memory, then initializes the memory as if by calling [`PyObject_Init()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_Init "PyObject_Init")
 or [`PyObject_InitVar()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_InitVar "PyObject_InitVar")
.

Do not call this directly to allocate memory for an object; call the type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot instead.

For types that support garbage collection (i.e., the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag is set), this function behaves like [`PyObject_GC_New`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "PyObject_GC_New")
 or [`PyObject_GC_NewVar`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_NewVar "PyObject_GC_NewVar")
 (except the memory is guaranteed to be zeroed before initialization), and should be paired with [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
 in [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
. Otherwise, it behaves like [`PyObject_New`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New")
 or [`PyObject_NewVar`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar")
 (except the memory is guaranteed to be zeroed before initialization) and should be paired with [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
 in `tp_free`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GenericNew([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*kwds)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GenericNew "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Generic handler for the [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 slot of a type object. Creates a new instance using the type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot and returns the resulting object.

int PyType\_Ready([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Finalize a type object. This should be called on all type objects to finish their initialization. This function is responsible for adding inherited slots from a type’s base class. Return `0` on success, or return `-1` and sets an exception on error.

Note

If some of the base classes implements the GC protocol and the provided type does not include the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 in its flags, then the GC protocol will be automatically implemented from its parents. On the contrary, if the type being created does include `Py_TPFLAGS_HAVE_GC` in its flags then it **must** implement the GC protocol itself by at least implementing the [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 handle.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GetName([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetName "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Return the type’s name. Equivalent to getting the type’s [`__name__`](https://docs.python.org/3/reference/datamodel.html#type.__name__ "type.__name__")
 attribute.

Added in version 3.11.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GetQualName([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetQualName "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Return the type’s qualified name. Equivalent to getting the type’s [`__qualname__`](https://docs.python.org/3/reference/datamodel.html#type.__qualname__ "type.__qualname__")
 attribute.

Added in version 3.11.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GetFullyQualifiedName([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetFullyQualifiedName "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Return the type’s fully qualified name. Equivalent to `f"{type.__module__}.{type.__qualname__}"`, or [`type.__qualname__`](https://docs.python.org/3/reference/datamodel.html#type.__qualname__ "type.__qualname__")
 if [`type.__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__")
 is not a string or is equal to `"builtins"`.

Added in version 3.13.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GetModuleName([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleName "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Return the type’s module name. Equivalent to getting the [`type.__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__")
 attribute.

Added in version 3.13.

void \*PyType\_GetSlot([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, int slot)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.4._

Return the function pointer stored in the given slot. If the result is `NULL`, this indicates that either the slot is `NULL`, or that the function was called with invalid parameters. Callers will typically cast the result pointer into the appropriate function type.

See [`PyType_Slot.slot`](https://docs.python.org/3/c-api/type.html#c.PyType_Slot.slot "PyType_Slot.slot")
 for possible values of the _slot_ argument.

Added in version 3.4.

Changed in version 3.10: [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot")
 can now accept all types. Previously, it was limited to [heap types](https://docs.python.org/3/c-api/typeobj.html#heap-types)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GetModule([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetModule "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Return the module object associated with the given type when the type was created using [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec")
.

The returned reference is [borrowed](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 from _type_, and will be valid as long as you hold a reference to _type_. Do not release it with [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 or similar.

If no module is associated with the given type, sets [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 and returns `NULL`.

This function is usually used to get the module in which a method is defined. Note that in such a method, `PyType_GetModule(Py_TYPE(self))` may not return the intended result. `Py_TYPE(self)` may be a _subclass_ of the intended class, and subclasses are not necessarily defined in the same module as their superclass. See [`PyCMethod`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod "PyCMethod")
 to get the class that defines the method. See [`PyType_GetModuleByToken()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByToken "PyType_GetModuleByToken")
 for cases when `PyCMethod` cannot be used.

Added in version 3.9.

void \*PyType\_GetModuleState([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleState "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Return the state of the module object associated with the given type. This is a shortcut for calling [`PyModule_GetState()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "PyModule_GetState")
 on the result of [`PyType_GetModule()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModule "PyType_GetModule")
.

If no module is associated with the given type, sets [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 and returns `NULL`.

If the _type_ has an associated module but its state is `NULL`, returns `NULL` without setting an exception.

Added in version 3.9.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GetModuleByToken([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, const void \*mod\_token)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByToken "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Find the first superclass whose module has the given [module token](https://docs.python.org/3/c-api/module.html#ext-module-token)
, and return that module.

If no module is found, raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 and returns `NULL`.

This function is intended to be used together with [`PyModule_GetState()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "PyModule_GetState")
 to get module state from slot methods (such as [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
 or [`nb_add`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_add "PyNumberMethods.nb_add")
) and other places where a method’s defining class cannot be passed using the [`PyCMethod`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod "PyCMethod")
 calling convention.

Added in version 3.15.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GetModuleByDef([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, struct [PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 \*def)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByDef "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Find the first superclass whose module was created from the given [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 _def_, or whose [module token](https://docs.python.org/3/c-api/module.html#ext-module-token)
 is equal to _def_, and return that module.

Note that modules created from a [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")
 always have their token set to the `PyModuleDef`’s address. In other words, this function is equivalent to [`PyType_GetModuleByToken()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByToken "PyType_GetModuleByToken")
, except that it:

*   returns a borrowed reference, and
    
*   has a non-`void*` argument type (which is a cosmetic difference in C).
    

The returned reference is [borrowed](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 from _type_, and will be valid as long as you hold a reference to _type_. Do not release it with [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 or similar.

Added in version 3.11.

int PyType\_GetBaseByToken([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, void \*tp\_token, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_GetBaseByToken "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Find the first superclass in _type_’s [method resolution order](https://docs.python.org/3/glossary.html#term-method-resolution-order)
 whose [`Py_tp_token`](https://docs.python.org/3/c-api/type.html#c.Py_tp_token "Py_tp_token")
 token is equal to _tp\_token_.

*   If found, set _\*result_ to a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     to it and return `1`.
    
*   If not found, set _\*result_ to `NULL` and return `0`.
    
*   On error, set _\*result_ to `NULL` and return `-1` with an exception set.
    

The _result_ argument may be `NULL`, in which case _\*result_ is not set. Use this if you need only the return value.

The _tp\_token_ argument may not be `NULL`.

Added in version 3.14.

int PyUnstable\_Type\_AssignVersionTag([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyUnstable_Type_AssignVersionTag "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Attempt to assign a version tag to the given type.

Returns 1 if the type already had a valid version tag or a new one was assigned, or 0 if a new tag could not be assigned.

Added in version 3.12.

int PyType\_SUPPORTS\_WEAKREFS([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_SUPPORTS_WEAKREFS "Link to this definition")
  

Return true if instances of _type_ support creating weak references, false otherwise. This function always succeeds. _type_ must not be `NULL`.

See also

*   [Weak Reference Objects](https://docs.python.org/3/c-api/weakref.html#weakrefobjects)
    
*   [`weakref`](https://docs.python.org/3/library/weakref.html#module-weakref "weakref: Support for weak references and weak dictionaries.")
    

Creating Heap-Allocated Types[¶](https://docs.python.org/3/c-api/type.html#creating-heap-allocated-types "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

The following function is used to create [heap types](https://docs.python.org/3/c-api/typeobj.html#heap-types)
:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_FromSlots(const [PySlot](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 \*slots)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Create and return a [heap type](https://docs.python.org/3/c-api/typeobj.html#heap-types)
 from a `PySlot` array. See [Definition slots](https://docs.python.org/3/c-api/slots.html#capi-slots)
 for general information on slots, and [Type slot IDs](https://docs.python.org/3/c-api/type.html#pyslot-type-slot-ids)
 for slots specific to type creation.

This function calls [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 on the new type.

Note that this function does _not_ fully match the behavior of calling [`type()`](https://docs.python.org/3/builtins/functions.html#type "type")
 or using the [`class`](https://docs.python.org/3/reference/compound_stmts.html#class)
 statement. With user-provided base types or metaclasses, prefer [calling](https://docs.python.org/3/c-api/call.html#capi-call)
 `type` (or the metaclass) over `PyType_From*` functions. Specifically:

*   [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
     is not called on the new class (and it must be set to `type.__new__`).
    
*   [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")
     is not called on the new class.
    
*   [`__init_subclass__()`](https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__ "object.__init_subclass__")
     is not called on any bases.
    
*   [`__set_name__()`](https://docs.python.org/3/reference/datamodel.html#object.__set_name__ "object.__set_name__")
     is not called on new descriptors.
    

Slots are typically defined as a global static constant arrays. However, sometimes slot values are not statically known at compile time. For example, slots like [`Py_tp_bases`](https://docs.python.org/3/c-api/type.html#c.Py_tp_bases "Py_tp_bases")
, [`Py_tp_metaclass`](https://docs.python.org/3/c-api/type.html#c.Py_tp_metaclass "Py_tp_metaclass")
 and [`Py_tp_module`](https://docs.python.org/3/c-api/type.html#c.Py_tp_module "Py_tp_module")
 require live Python objects. In this case, it is recommended to put such slots on the stack, and use [`Py_slot_subslots`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_subslots "Py_slot_subslots")
 to refer to an array of static slots. For example:

static const PySlot my\_slots\[\] \= {
   PySlot\_STATIC\_DATA(Py\_tp\_name, "MyClass"),
   PySlot\_FUNC(Py\_tp\_repr, my\_repr\_func),
   ...
   PySlot\_END
};

PyObject \*make\_my\_class(PyObject \*module) {
   PySlot all\_slots\[\] \= {
      PySlot\_STATIC\_DATA(Py\_slot\_subslots, my\_slots),
      PySlot\_DATA(Py\_tp\_module, module),
      PySlot\_END
   };
   return PyType\_FromSlots(all\_slots);
}

Heap types created without the [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Py_TPFLAGS_IMMUTABLETYPE")
 flag may be modified, for example by setting attributes on them, as with classes defined in Python code. Sometimes, such modifications are necessary to fully initialize a type, but you may wish to prevent users from changing the type after the initialization is done:

int PyType\_Freeze([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Freeze "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Make a type immutable: set the [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Py_TPFLAGS_IMMUTABLETYPE")
 flag.

All base classes of _type_ must be immutable.

On success, return `0`. On error, set an exception and return `-1`.

The type must not be used before it’s made immutable. For example, type instances must not be created before the type is made immutable.

Added in version 3.14.

### Type slot IDs[¶](https://docs.python.org/3/c-api/type.html#type-slot-ids "Link to this heading")

Most type slot IDs are named like the field names of the structures [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
, [`PyNumberMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods "PyNumberMethods")
, [`PySequenceMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods "PySequenceMethods")
, [`PyMappingMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PyMappingMethods "PyMappingMethods")
 and [`PyAsyncMethods`](https://docs.python.org/3/c-api/typeobj.html#c.PyAsyncMethods "PyAsyncMethods")
 with an added `Py_` prefix. For example, use:

*   [`Py_tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_dealloc "Py_tp_dealloc")
     to set [`PyTypeObject.tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
    
*   [`Py_nb_add`](https://docs.python.org/3/c-api/typeobj.html#c.Py_nb_add "Py_nb_add")
     to set [`PyNumberMethods.nb_add`](https://docs.python.org/3/c-api/typeobj.html#c.PyNumberMethods.nb_add "PyNumberMethods.nb_add")
    
*   [`Py_sq_length`](https://docs.python.org/3/c-api/typeobj.html#c.Py_sq_length "Py_sq_length")
     to set [`PySequenceMethods.sq_length`](https://docs.python.org/3/c-api/typeobj.html#c.PySequenceMethods.sq_length "PySequenceMethods.sq_length")
    

The following slots need additional considerations when specified as slots:

*   [`Py_tp_name`](https://docs.python.org/3/c-api/type.html#c.Py_tp_name "Py_tp_name")
    
*   [`Py_tp_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_basicsize "Py_tp_basicsize")
     and [`Py_tp_extra_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_extra_basicsize "Py_tp_extra_basicsize")
    
*   [`Py_tp_itemsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_itemsize "Py_tp_itemsize")
    
*   [`Py_tp_flags`](https://docs.python.org/3/c-api/type.html#c.Py_tp_flags "Py_tp_flags")
    

Additional slots do not directly correspond to a `PyTypeObject` struct field:

*   [`Py_tp_token`](https://docs.python.org/3/c-api/type.html#c.Py_tp_token "Py_tp_token")
    
*   [`Py_tp_metaclass`](https://docs.python.org/3/c-api/type.html#c.Py_tp_metaclass "Py_tp_metaclass")
    
*   [`Py_tp_module`](https://docs.python.org/3/c-api/type.html#c.Py_tp_module "Py_tp_module")
    

The following “offset” fields cannot be set using [`PyType_Slot`](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
:

*   [`tp_weaklistoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset "PyTypeObject.tp_weaklistoffset")
     (use [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF "Py_TPFLAGS_MANAGED_WEAKREF")
     instead if possible)
    
*   [`tp_dictoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dictoffset "PyTypeObject.tp_dictoffset")
     (use [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
     instead if possible)
    
*   [`tp_vectorcall_offset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall_offset "PyTypeObject.tp_vectorcall_offset")
     (use `"__vectorcalloffset__"` in [PyMemberDef](https://docs.python.org/3/c-api/structures.html#pymemberdef-offsets)
    )
    

If it is not possible to switch to a `MANAGED` flag (for example, for vectorcall or to support Python older than 3.12), specify the offset in [`Py_tp_members`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_members "Py_tp_members")
. See [PyMemberDef documentation](https://docs.python.org/3/c-api/structures.html#pymemberdef-offsets)
 for details.

The following internal fields cannot be set at all when creating a heap type:

*   [`tp_dict`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dict "PyTypeObject.tp_dict")
    , [`tp_mro`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_mro "PyTypeObject.tp_mro")
    , [`tp_cache`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_cache "PyTypeObject.tp_cache")
    , [`tp_subclasses`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_subclasses "PyTypeObject.tp_subclasses")
    , and [`tp_weaklist`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklist "PyTypeObject.tp_weaklist")
    .
    

The [`Py_tp_base`](https://docs.python.org/3/c-api/type.html#c.Py_tp_base "Py_tp_base")
 slot is equivalent to [`Py_tp_bases`](https://docs.python.org/3/c-api/type.html#c.Py_tp_bases "Py_tp_bases")
; both may be set either to a type or a tuple of types. If both are specified, the value of `Py_tp_bases` is used.

Slot values may not be `NULL`, except for the following:

*   [`Py_tp_doc`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_doc "Py_tp_doc")
    
*   [`Py_tp_token`](https://docs.python.org/3/c-api/type.html#c.Py_tp_token "Py_tp_token")
     (for clarity, prefer [`Py_TP_USE_SPEC`](https://docs.python.org/3/c-api/type.html#c.Py_TP_USE_SPEC "Py_TP_USE_SPEC")
     rather than `NULL`)
    

Changed in version 3.9: Slots in [`PyBufferProcs`](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs "PyBufferProcs")
 may be set in the unlimited API.

Changed in version 3.11: [`bf_getbuffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs.bf_getbuffer "PyBufferProcs.bf_getbuffer")
 and [`bf_releasebuffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyBufferProcs.bf_releasebuffer "PyBufferProcs.bf_releasebuffer")
 are now available under the [limited API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
.

Changed in version 3.14: The field [`tp_vectorcall`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall "PyTypeObject.tp_vectorcall")
 can now be set using [`Py_tp_vectorcall`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_vectorcall "Py_tp_vectorcall")
. See the field’s documentation for details.

Changed in version 3.15: The [`Py_tp_bases`](https://docs.python.org/3/c-api/type.html#c.Py_tp_bases "Py_tp_bases")
 slot may be set to a single type object, making it equivalent to the [`Py_tp_base`](https://docs.python.org/3/c-api/type.html#c.Py_tp_base "Py_tp_base")
 slot. Previously, a tuple of types was required.

The following slots correspond to fields in the underlying type structure, but need extra remarks for use as slots:

Py\_tp\_name[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_name "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for the name of the type, used to set [`PyTypeObject.tp_name`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_name "PyTypeObject.tp_name")
.

This slot (or [`PyType_Spec.name`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.name "PyType_Spec.name")
) is required to create a type.

This may not be used in [`PyType_Spec.slots`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.slots "PyType_Spec.slots")
. Use [`PyType_Spec.name`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.name "PyType_Spec.name")
 instead.

**CPython implementation detail:** CPython processes slots in order. It is recommended to put `Py_tp_name` at the beginning of the slots array, so that if processing of a later slots fails, error messages can include the name.

Added in version 3.15.

Py\_tp\_basicsize[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_basicsize "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for the size of the instance in bytes. It is used to set [`PyTypeObject.tp_basicsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_basicsize "PyTypeObject.tp_basicsize")
.

The value must be positive.

This may not be used in [`PyType_Spec.slots`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.slots "PyType_Spec.slots")
. Use [`PyType_Spec.basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
 instead.

This slot may not be used with [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot")
. Use [`PyTypeObject.tp_basicsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_basicsize "PyTypeObject.tp_basicsize")
 instead if needed, but be aware that a type’s size is often considered an implementation detail.

Added in version 3.15.

Py\_tp\_extra\_basicsize[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_extra_basicsize "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for type data size in bytes, that is, how much space instances of the class need _in addition_ to space needed for superclasses.

The value is used, together with the size of superclasses, to set [`PyTypeObject.tp_basicsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_basicsize "PyTypeObject.tp_basicsize")
. Python will insert padding as needed to meet `tp_basicsize`’s alignment requirements.

Use [`PyObject_GetTypeData()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetTypeData "PyObject_GetTypeData")
 to get a pointer to subclass-specific memory reserved this way.

The value must be positive. To specify that instances need no additional size (that is, size should be inherited), omit the `Py_tp_extra_basicsize` slot rather than set it to zero.

Specifying both [`Py_tp_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_basicsize "Py_tp_basicsize")
 and `Py_tp_extra_basicsize` is an error.

This may not be used in [`PyType_Spec.slots`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.slots "PyType_Spec.slots")
. Use negative [`PyType_Spec.basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
 instead.

This slot may not be used with [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot")
.

Added in version 3.15.

Py\_tp\_itemsize[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_itemsize "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for the size of one element of a variable-size type, in bytes. Used to set [`PyTypeObject.tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
. See `tp_itemsize` documentation for caveats.

The value must be positive.

If this slot is missing, [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
 is inherited. Extending arbitrary variable-sized classes is dangerous, since some types use a fixed offset for variable-sized memory, which can then overlap fixed-sized memory used by a subclass. To help prevent mistakes, inheriting `itemsize` is only possible in the following situations:

*   The base is not variable-sized (its [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
     is zero).
    
*   The requested [`PyType_Spec.basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
     is positive, suggesting that the memory layout of the base class is known.
    
*   The requested [`PyType_Spec.basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
     is zero, suggesting that the subclass does not access the instance’s memory directly.
    
*   With the [`Py_TPFLAGS_ITEMS_AT_END`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_ITEMS_AT_END "Py_TPFLAGS_ITEMS_AT_END")
     flag.
    

This may not be used in [`PyType_Spec.slots`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.slots "PyType_Spec.slots")
. Use [`PyType_Spec.itemsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.itemsize "PyType_Spec.itemsize")
 instead.

This slot may not be used with [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot")
.

Added in version 3.15.

Py\_tp\_flags[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_flags "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for type flags, used to set [`PyTypeObject.tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
.

The `Py_TPFLAGS_HEAPTYPE` flag is not set, [`PyType_FromSpecWithBases()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpecWithBases "PyType_FromSpecWithBases")
 sets it automatically.

This may not be used in [`PyType_Spec.slots`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.slots "PyType_Spec.slots")
. Use negative [`PyType_Spec.basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
 instead.

This slot may not be used with [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot")
. Use [`PyType_GetFlags()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetFlags "PyType_GetFlags")
 instead.

Added in version 3.15.

Py\_tp\_bases[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_bases "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for base types, used to set [`PyTypeObject.tp_bases`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_bases "PyTypeObject.tp_bases")
.

The slot can be set to a tuple of type objects which the newly created type should inherit from, like the “positional arguments” of a Python [class definition](https://docs.python.org/3/reference/compound_stmts.html#class)
.

Alternately, the slot can be set to a single type object to specify a single base. The effect is the same as specifying a one-element tuple.

Changed in version 3.15: Previously, `Py_tp_bases` required a tuple of types.

Py\_tp\_base[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_base "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Equivalent to [`Py_tp_bases`](https://docs.python.org/3/c-api/type.html#c.Py_tp_bases "Py_tp_bases")
 (with `s` at the end). If both are specified, `Py_tp_bases` takes priority and this slot is ignored.

Changed in version 3.15: Previously, `Py_tp_base` required a single type, not a tuple.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: When not targeting older Python versions, prefer `Py_tp_bases`.

The following slots do not correspond to public fields in the underlying structures:

Py\_tp\_metaclass[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_metaclass "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for the metaclass used to construct the resulting type object. When omitted the metaclass is derived from bases ([`Py_tp_bases`](https://docs.python.org/3/c-api/type.html#c.Py_tp_bases "Py_tp_bases")
 or the _bases_ argument of [`PyType_FromMetaclass()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromMetaclass "PyType_FromMetaclass")
).

Metaclasses that override [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 are not supported, except if `tp_new` is `NULL`.

This may not be used in [`PyType_Spec.slots`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.slots "PyType_Spec.slots")
. Use [`PyType_FromMetaclass()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromMetaclass "PyType_FromMetaclass")
 to specify a metaclass with `PyType_Spec`.

This slot may not be used with [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot")
. Use [`Py_TYPE()`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
 on the type object instead.

Added in version 3.15.

Py\_tp\_module[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_module "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for recording the module in which the new class is defined.

The value must be a module object. The module is associated with the new type and can later be retrieved with [`PyType_GetModule()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModule "PyType_GetModule")
. The associated module is not inherited by subclasses; it must be specified for each class individually.

This may not be used in [`PyType_Spec.slots`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.slots "PyType_Spec.slots")
. Use [`PyType_FromMetaclass()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromMetaclass "PyType_FromMetaclass")
 to specify a module with `PyType_Spec`.

This slot may not be used with [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot")
. Use [`PyType_GetModule()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModule "PyType_GetModule")
 instead.

Added in version 3.15.

Py\_tp\_token[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_token "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 for recording a static memory layout ID for a class.

If the class is defined using a [`PyType_Spec`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "PyType_Spec")
, and that spec is statically allocated, the token can be set to the spec using the special value [`Py_TP_USE_SPEC`](https://docs.python.org/3/c-api/type.html#c.Py_TP_USE_SPEC "Py_TP_USE_SPEC")
:

static PyType\_Slot foo\_slots\[\] \= {
   {Py\_tp\_token, Py\_TP\_USE\_SPEC},

It can also be set to an arbitrary pointer, but you must ensure that:

*   The pointer outlives the class, so it’s not reused for something else while the class exists.
    
*   It “belongs” to the extension module where the class lives, so it will not clash with other extensions.
    

Use [`PyType_GetBaseByToken()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetBaseByToken "PyType_GetBaseByToken")
 to check if a class’s superclass has a given token – that is, check whether the memory layout is compatible.

To get the token for a given class (without considering superclasses), use [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot")
 with `Py_tp_token`.

Added in version 3.14.

Py\_TP\_USE\_SPEC[¶](https://docs.python.org/3/c-api/type.html#c.Py_TP_USE_SPEC "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Used as a value with [`Py_tp_token`](https://docs.python.org/3/c-api/type.html#c.Py_tp_token "Py_tp_token")
 to set the token to the class’s [`PyType_Spec`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "PyType_Spec")
. May only be used for classes defined using `PyType_Spec`.

Expands to `NULL`.

Added in version 3.14.

Py\_tp\_slots[¶](https://docs.python.org/3/c-api/type.html#c.Py_tp_slots "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

[`Slot ID`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
 that works like [`Py_slot_subslots`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_subslots "Py_slot_subslots")
, except it specifies an array of [`PyType_Slot`](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 structures.

Added in version 3.15.

Soft-deprecated API[¶](https://docs.python.org/3/c-api/type.html#soft-deprecated-api "Link to this heading")

-------------------------------------------------------------------------------------------------------------

The following functions are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
. They will continue to work, but new features will be added as slots for [`PyType_FromSlots()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "PyType_FromSlots")
, not as arguments to new `PyType_From*` functions.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_FromMetaclass([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*metaclass, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, [PyType\_Spec](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "PyType_Spec")
 \*spec, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*bases)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_FromMetaclass "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Create and return a [heap type](https://docs.python.org/3/c-api/typeobj.html#heap-types)
 from the _spec_ (see [`Py_TPFLAGS_HEAPTYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HEAPTYPE "Py_TPFLAGS_HEAPTYPE")
).

A non-`NULL` _metaclass_ argument corresponds to the [`Py_tp_metaclass`](https://docs.python.org/3/c-api/type.html#c.Py_tp_metaclass "Py_tp_metaclass")
 slot.

A non-`NULL` _bases_ argument corresponds to the [`Py_tp_bases`](https://docs.python.org/3/c-api/type.html#c.Py_tp_bases "Py_tp_bases")
 slot, and takes precedence over [`Py_tp_base`](https://docs.python.org/3/c-api/type.html#c.Py_tp_base "Py_tp_base")
 and `Py_tp_bases` slots.

A non-`NULL` _module_ argument corresponds to the [`Py_tp_module`](https://docs.python.org/3/c-api/type.html#c.Py_tp_module "Py_tp_module")
 slot.

This function calls [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
 on the new type.

Note that this function does _not_ fully match the behavior of calling [`type()`](https://docs.python.org/3/builtins/functions.html#type "type")
 or using the [`class`](https://docs.python.org/3/reference/compound_stmts.html#class)
 statement. See the note in [`PyType_FromSlots()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "PyType_FromSlots")
 documentation for details.

Added in version 3.12.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: Prefer [`PyType_FromSlots()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "PyType_FromSlots")
 in new code.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_FromModuleAndSpec([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, [PyType\_Spec](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "PyType_Spec")
 \*spec, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*bases)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Equivalent to `PyType_FromMetaclass(NULL, module, spec, bases)`.

Added in version 3.9.

Changed in version 3.10: The function now accepts a single class as the _bases_ argument and `NULL` as the `tp_doc` slot.

Changed in version 3.12: The function now finds and uses a metaclass corresponding to the provided base classes. Previously, only [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
 instances were returned.

The [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 of the metaclass is _ignored_. which may result in incomplete initialization. Creating classes whose metaclass overrides `tp_new` is deprecated.

Changed in version 3.14: Creating classes whose metaclass overrides [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 is no longer allowed.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: Prefer [`PyType_FromSlots()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "PyType_FromSlots")
 in new code.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_FromSpecWithBases([PyType\_Spec](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "PyType_Spec")
 \*spec, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*bases)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpecWithBases "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.3._

Equivalent to `PyType_FromMetaclass(NULL, NULL, spec, bases)`.

Added in version 3.3.

Changed in version 3.12: The function now finds and uses a metaclass corresponding to the provided base classes. Previously, only [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
 instances were returned.

The [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 of the metaclass is _ignored_. which may result in incomplete initialization. Creating classes whose metaclass overrides `tp_new` is deprecated.

Changed in version 3.14: Creating classes whose metaclass overrides [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 is no longer allowed.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: Prefer [`PyType_FromSlots()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "PyType_FromSlots")
 in new code.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_FromSpec([PyType\_Spec](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "PyType_Spec")
 \*spec)[¶](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Equivalent to `PyType_FromMetaclass(NULL, NULL, spec, NULL)`.

Changed in version 3.12: The function now finds and uses a metaclass corresponding to the base classes provided in _Py\_tp\_base\[s\]_ slots. Previously, only [`type`](https://docs.python.org/3/builtins/functions.html#type "type")
 instances were returned.

The [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 of the metaclass is _ignored_. which may result in incomplete initialization. Creating classes whose metaclass overrides `tp_new` is deprecated.

Changed in version 3.14: Creating classes whose metaclass overrides [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 is no longer allowed.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15: Prefer [`PyType_FromSlots()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "PyType_FromSlots")
 in new code.

type PyType\_Spec[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Spec "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members)._

Structure defining a type’s behavior, used for soft-deprecated functions like [`PyType_FromMetaclass()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromMetaclass "PyType_FromMetaclass")
.

This structure contains several members that can instead be specified as [slots](https://docs.python.org/3/c-api/type.html#pyslot-type-slot-ids)
 for [`PyType_FromSlots()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "PyType_FromSlots")
, and an array of slot entries with a simpler structure.

const char \*name[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.name "Link to this definition")
  

Corresponds to [`Py_tp_name`](https://docs.python.org/3/c-api/type.html#c.Py_tp_name "Py_tp_name")
.

int basicsize[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "Link to this definition")
  

If positive, corresponds to [`Py_tp_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_basicsize "Py_tp_basicsize")
.

If negative, corresponds to [`Py_tp_extra_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_extra_basicsize "Py_tp_extra_basicsize")
 set to the absolute value.

Changed in version 3.12: Previously, this field could not be negative.

int itemsize[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.itemsize "Link to this definition")
  

Corresponds to [`Py_tp_itemsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_itemsize "Py_tp_itemsize")
.

unsigned int flags[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.flags "Link to this definition")
  

Corresponds to [`Py_tp_flags`](https://docs.python.org/3/c-api/type.html#c.Py_tp_flags "Py_tp_flags")
.

[PyType\_Slot](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 \*slots[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.slots "Link to this definition")
  

Array of [`PyType_Slot`](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "PyType_Slot")
 (not [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
) structures.

Terminated by the special slot value `{0, NULL}`. Each slot ID should be specified at most once.

type PyType\_Slot[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Slot "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members)._

Structure defining optional functionality of a type, used for soft-deprecated functions like [`PyType_FromMetaclass()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromMetaclass "PyType_FromMetaclass")
.

Note that a `PyType_Slot` array may be included in a `PySlot` array using [`Py_tp_slots`](https://docs.python.org/3/c-api/type.html#c.Py_tp_slots "Py_tp_slots")
, and vice versa using [`Py_slot_subslots`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_subslots "Py_slot_subslots")
.

Each `PyType_Slot` structure `tpslot` is interpreted as the following [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 structure:

(PySlot){
   .sl\_id\=tpslot.slot,
   .sl\_flags\=PySlot\_INTPTR | sub\_static,
   .sl\_ptr\=tpslot.pfunc
}

where `sub_static` is `PySlot_STATIC` if the slot requires the flag (such as for [`Py_tp_methods`](https://docs.python.org/3/c-api/typeobj.html#c.Py_tp_methods "Py_tp_methods")
), or if this flag is present on the “parent” `Py_tp_slots` slot (if any).

int slot[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Slot.slot "Link to this definition")
  

Corresponds to [`PySlot.sl_id`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_id "PySlot.sl_id")
.

void \*pfunc[¶](https://docs.python.org/3/c-api/type.html#c.PyType_Slot.pfunc "Link to this definition")
  

Corresponds to [`PySlot.sl_ptr`](https://docs.python.org/3/c-api/slots.html#c.PySlot.sl_ptr "PySlot.sl_ptr")
.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Type Objects](https://docs.python.org/3/c-api/type.html#)
    *   [Creating Heap-Allocated Types](https://docs.python.org/3/c-api/type.html#creating-heap-allocated-types)
        *   [Type slot IDs](https://docs.python.org/3/c-api/type.html#type-slot-ids)
            
    *   [Soft-deprecated API](https://docs.python.org/3/c-api/type.html#soft-deprecated-api)
        

#### Previous topic

[Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html "previous chapter")

#### Next topic

[The `None` Object](https://docs.python.org/3/c-api/none.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Type+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Ftype.html&pagesource=c-api%2Ftype.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/type.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/none.html "The None Object")
     |
*   [previous](https://docs.python.org/3/c-api/concrete.html "Concrete Objects Layer")
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
*   [Type Objects](https://docs.python.org/3/c-api/type.html)
    
*    
    
    |
*   Theme Auto Light Dark |