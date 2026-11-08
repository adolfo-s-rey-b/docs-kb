### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/apiabiversion.html "API and ABI Versioning")
     |
*   [previous](https://docs.python.org/3/c-api/typeobj.html "Type Object Structures")
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
*   [Supporting Cyclic Garbage Collection](https://docs.python.org/3/c-api/gcsupport.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Supporting Cyclic Garbage Collection[¶](https://docs.python.org/3/c-api/gcsupport.html#supporting-cyclic-garbage-collection "Link to this heading")

====================================================================================================================================================

Python’s support for detecting and collecting garbage which involves circular references requires support from object types which are “containers” for other objects which may also be containers. Types which do not store references to other objects, or which only store references to atomic types (such as numbers or strings), do not need to provide any explicit support for garbage collection.

To create a container type, the [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
 field of the type object must include the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 and provide an implementation of the [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 handler. If instances of the type are mutable, a [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 implementation must also be provided.

[`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")

Objects with a type with this flag set must conform with the rules documented here. For convenience these objects will be referred to as container objects.

Constructors for container types must conform to two rules:

1.  The memory for the object must be allocated using [`PyObject_GC_New`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "PyObject_GC_New")
     or [`PyObject_GC_NewVar`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_NewVar "PyObject_GC_NewVar")
    .
    
2.  Once all the fields which may contain references to other containers are initialized, it must call [`PyObject_GC_Track()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Track "PyObject_GC_Track")
    .
    

Similarly, the deallocator for the object must conform to a similar pair of rules:

1.  Before fields which refer to other containers are invalidated, [`PyObject_GC_UnTrack()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_UnTrack "PyObject_GC_UnTrack")
     must be called.
    
2.  The object’s memory must be deallocated using [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
    .
    
    Warning
    
    If a type adds the Py\_TPFLAGS\_HAVE\_GC, then it _must_ implement at least a [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
     handler or explicitly use one from a base class.
    
    When calling [`PyType_Ready()`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "PyType_Ready")
     or some of the APIs that indirectly call it like [`PyType_FromSpecWithBases()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpecWithBases "PyType_FromSpecWithBases")
     or [`PyType_FromSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec "PyType_FromSpec")
     the interpreter will automatically populate the [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
    , [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
     and [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
     fields if the type inherits from a class that implements the garbage collector protocol and the child class does _not_ include the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
     flag.
    

PyObject\_GC\_New(TYPE, typeobj)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "Link to this definition")
  

Analogous to [`PyObject_New`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New")
 but for container objects with the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag set.

Do not call this directly to allocate memory for an object; call the type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot instead.

When populating a type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot, [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
 is preferred over a custom function that simply calls this macro.

Memory allocated by this macro must be freed with [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
 (usually called via the object’s [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 slot).

See also

*   [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
    
*   [`PyObject_New`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New")
    
*   [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
    
*   [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
    

PyObject\_GC\_NewVar(TYPE, typeobj, size)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_NewVar "Link to this definition")
  

Analogous to [`PyObject_NewVar`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar")
 but for container objects with the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag set.

Do not call this directly to allocate memory for an object; call the type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot instead.

When populating a type’s [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
 slot, [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
 is preferred over a custom function that simply calls this macro.

Memory allocated by this macro must be freed with [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
 (usually called via the object’s [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 slot).

See also

*   [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
    
*   [`PyObject_NewVar`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar")
    
*   [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
    
*   [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
    

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnstable\_Object\_GC\_NewWithExtraData([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, size\_t extra\_size)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyUnstable_Object_GC_NewWithExtraData "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Analogous to [`PyObject_GC_New`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "PyObject_GC_New")
 but allocates _extra\_size_ bytes at the end of the object (at offset [`tp_basicsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_basicsize "PyTypeObject.tp_basicsize")
). The allocated memory is initialized to zeros, except for the [`Python object header`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
.

The extra data will be deallocated with the object, but otherwise it is not managed by Python.

Memory allocated by this function must be freed with [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
 (usually called via the object’s [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 slot).

Warning

The function is marked as unstable because the final mechanism for reserving extra data after an instance is not yet decided. For allocating a variable number of fields, prefer using [`PyVarObject`](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
 and [`tp_itemsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_itemsize "PyTypeObject.tp_itemsize")
 instead.

Added in version 3.12.

PyObject\_GC\_Resize(TYPE, op, newsize)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Resize "Link to this definition")
  

Resize an object allocated by [`PyObject_GC_NewVar`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_NewVar "PyObject_GC_NewVar")
. Returns the resized object of type `TYPE*` (refers to any C type) or `NULL` on failure.

_op_ must be of type [PyVarObject](https://docs.python.org/3/c-api/structures.html#c.PyVarObject "PyVarObject")
\* and must not be tracked by the collector yet. _newsize_ must be of type [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
.

void PyObject\_GC\_Track([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Track "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Adds the object _op_ to the set of container objects tracked by the collector. The collector can run at unexpected times so objects must be valid while being tracked. This should be called once all the fields followed by the [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 handler become valid, usually near the end of the constructor.

int PyObject\_IS\_GC([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_IS_GC "Link to this definition")
  

Returns non-zero if the object implements the garbage collector protocol, otherwise returns 0.

The object cannot be tracked by the garbage collector if this function returns 0.

int PyObject\_GC\_IsTracked([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_IsTracked "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.9._

Returns 1 if the object type of _op_ implements the GC protocol and _op_ is being currently tracked by the garbage collector and 0 otherwise.

This is analogous to the Python function [`gc.is_tracked()`](https://docs.python.org/3/library/gc.html#gc.is_tracked "gc.is_tracked")
.

Added in version 3.9.

int PyObject\_GC\_IsFinalized([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_IsFinalized "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.9._

Returns 1 if the object type of _op_ implements the GC protocol and _op_ has been already finalized by the garbage collector and 0 otherwise.

This is analogous to the Python function [`gc.is_finalized()`](https://docs.python.org/3/library/gc.html#gc.is_finalized "gc.is_finalized")
.

Added in version 3.9.

void PyObject\_GC\_Del(void \*op)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Releases memory allocated to an object using [`PyObject_GC_New`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "PyObject_GC_New")
 or [`PyObject_GC_NewVar`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_NewVar "PyObject_GC_NewVar")
.

Do not call this directly to free an object’s memory; call the type’s [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 slot instead.

Do not use this for memory allocated by [`PyObject_New`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New")
, [`PyObject_NewVar`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar")
, or related allocation functions; use [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
 instead.

See also

*   [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
     is the non-GC equivalent of this function.
    
*   [`PyObject_GC_New`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "PyObject_GC_New")
    
*   [`PyObject_GC_NewVar`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_NewVar "PyObject_GC_NewVar")
    
*   [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
    
*   [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
    

void PyObject\_GC\_UnTrack(void \*op)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_UnTrack "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Remove the object _op_ from the set of container objects tracked by the collector. Note that [`PyObject_GC_Track()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Track "PyObject_GC_Track")
 can be called again on this object to add it back to the set of tracked objects. The deallocator ([`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
 handler) should call this for the object before any of the fields used by the [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 handler become invalid.

Changed in version 3.8: The `_PyObject_GC_TRACK()` and `_PyObject_GC_UNTRACK()` macros have been removed from the public C API.

The [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 handler accepts a function parameter of this type:

typedef int (\*visitproc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*object, void \*arg)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.visitproc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Type of the visitor function passed to the [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 handler. The function should be called with an object to traverse as _object_ and the third parameter to the `tp_traverse` handler as _arg_. The Python core uses several visitor functions to implement cyclic garbage detection; it’s not expected that users will need to write their own visitor functions.

The [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 handler must be of the [`inquiry`](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "inquiry")
 type, or `NULL` if the object is immutable.

typedef int (\*inquiry)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.inquiry "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Drop references that may have created reference cycles. Immutable objects do not have to define this method since they can never directly create reference cycles. Note that the object must still be valid after calling this method (don’t just call [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 on a reference). The collector will call this method if it detects that this object is involved in a reference cycle.

Traversal[¶](https://docs.python.org/3/c-api/gcsupport.html#traversal "Link to this heading")

----------------------------------------------------------------------------------------------

The [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 handler must have the following type:

typedef int (\*traverseproc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*self, [visitproc](https://docs.python.org/3/c-api/gcsupport.html#c.visitproc "visitproc")
 visit, void \*arg)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.traverseproc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Traversal function for a garbage-collected object, used by the garbage collector to detect reference cycles. Implementations must call the _visit_ function for each object directly contained by _self_, with the parameters to _visit_ being the contained object and the _arg_ value passed to the handler. The _visit_ function must not be called with a `NULL` object argument. If _visit_ returns a non-zero value, that value should be returned immediately. Otherwise, return zero.

A typical `tp_traverse` function calls the [`Py_VISIT()`](https://docs.python.org/3/c-api/gcsupport.html#c.Py_VISIT "Py_VISIT")
 convenience macro on each of the instance’s members that are Python objects that the instance owns. For example, this is a (slightly outdated) traversal function for the [`threading.local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local")
 class:

static int
local\_traverse(PyObject \*op, visitproc visit, void \*arg)
{
    localobject \*self \= (localobject \*) op;
    Py\_VISIT(Py\_TYPE(self));
    Py\_VISIT(self\->args);
    Py\_VISIT(self\->kw);
    Py\_VISIT(self\->dict);
    return 0;
}

Note

[`Py_VISIT()`](https://docs.python.org/3/c-api/gcsupport.html#c.Py_VISIT "Py_VISIT")
 requires the _visit_ and _arg_ parameters to `local_traverse()` to have these specific names; don’t name them just anything.

Instances of [heap-allocated types](https://docs.python.org/3/c-api/typeobj.html#heap-types)
 hold a reference to their type. Their traversal function must therefore visit the type:

Py\_VISIT(Py\_TYPE(self));

Alternately, the type may delegate this responsibility by calling `tp_traverse` of a heap-allocated superclass (or another heap-allocated type, if applicable). If they do not, the type object may not be garbage-collected.

If the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")
 bit is set in the [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
 field, the traverse function must call [`PyObject_VisitManagedDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_VisitManagedDict "PyObject_VisitManagedDict")
 like this:

int err \= PyObject\_VisitManagedDict((PyObject\*)self, visit, arg);
if (err) {
    return err;
}

Only the members that the instance _owns_ (by having [strong references](https://docs.python.org/3/glossary.html#term-strong-reference)
 to them) must be visited. For instance, if an object supports weak references via the [`tp_weaklist`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklist "PyTypeObject.tp_weaklist")
 slot, the pointer supporting the linked list (what _tp\_weaklist_ points to) must **not** be visited as the instance does not directly own the weak references to itself.

The traversal function has a limitation:

Warning

The traversal function must not have any side effects. Implementations may not modify the reference counts of any Python objects nor create or destroy any Python objects, directly or indirectly.

This means that _most_ Python C API functions may not be used, since they can raise a new exception, return a new reference to a result object, have internal logic that uses side effects. Also, unless documented otherwise, functions that happen to not have side effects may start having them in future versions, without warning.

For a list of safe functions, see a [separate section](https://docs.python.org/3/c-api/gcsupport.html#duringgc-functions)
 below.

If an error occurs during traversal, ignore it and return 0. If `tp_traverse` fails to visit some strong references, garbage reference cycles involving the skipped references will not be reliably broken, but correctness won’t be affected. For example, if traversal requires a lock that cannot be acquired promptly, skip the traversal. The garbage collector will visit your object again in a future pass.

Note

The [`Py_VISIT()`](https://docs.python.org/3/c-api/gcsupport.html#c.Py_VISIT "Py_VISIT")
 call may be skipped for those members that provably cannot participate in reference cycles. In the `local_traverse` example above, there is also a `self->key` member, but it can only be `NULL` or a Python string and therefore cannot be part of a reference cycle.

On the other hand, even if you know a member can never be part of a cycle, as a debugging aid you may want to visit it anyway just so the [`gc`](https://docs.python.org/3/library/gc.html#module-gc "gc: Interface to the cycle-detecting garbage collector.")
 module’s [`get_referents()`](https://docs.python.org/3/library/gc.html#gc.get_referents "gc.get_referents")
 function will include it.

Note

The [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 function can be called from any thread.

**CPython implementation detail:** Garbage collection is a “stop-the-world” operation: even in [free threading](https://docs.python.org/3/glossary.html#term-free-threading)
 builds, only one thread state is [attached](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 when `tp_traverse` handlers run.

Changed in version 3.9: Heap-allocated types are expected to visit `Py_TYPE(self)` in `tp_traverse`. In earlier versions of Python, due to [bug 40217](https://bugs.python.org/issue40217)
, doing this may lead to crashes in subclasses.

To simplify writing [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 handlers, a [`Py_VISIT()`](https://docs.python.org/3/c-api/gcsupport.html#c.Py_VISIT "Py_VISIT")
 macro is provided. In order to use this macro, the `tp_traverse` implementation must name its arguments exactly _visit_ and _arg_:

Py\_VISIT(o)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.Py_VISIT "Link to this definition")
  

If the [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* _o_ is not `NULL`, call the _visit_ callback, with arguments _o_ and _arg_. If _visit_ returns a non-zero value, then return it.

This corresponds roughly to:

#define Py\_VISIT(o)                             \\
   if (o) {                                    \\
      int visit\_result = visit(o, arg);         \\
      if (visit\_result != 0) {                  \\
         return visit\_result;                   \\
      }                                         \\
   }

### Traversal-safe functions[¶](https://docs.python.org/3/c-api/gcsupport.html#traversal-safe-functions "Link to this heading")

The following functions and macros are safe to use in a [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 handler:

*   the _visit_ function passed to `tp_traverse`
    
*   [`Py_VISIT()`](https://docs.python.org/3/c-api/gcsupport.html#c.Py_VISIT "Py_VISIT")
    
*   [`Py_SIZE()`](https://docs.python.org/3/c-api/structures.html#c.Py_SIZE "Py_SIZE")
    
*   [`Py_TYPE()`](https://docs.python.org/3/c-api/structures.html#c.Py_TYPE "Py_TYPE")
    : if called from a `tp_traverse` handler, `Py_TYPE()`’s result will be valid for the duration of the handler call
    
*   [`PyObject_VisitManagedDict()`](https://docs.python.org/3/c-api/object.html#c.PyObject_VisitManagedDict "PyObject_VisitManagedDict")
    
*   [`PyObject_TypeCheck()`](https://docs.python.org/3/c-api/object.html#c.PyObject_TypeCheck "PyObject_TypeCheck")
    , [`PyType_IsSubtype()`](https://docs.python.org/3/c-api/type.html#c.PyType_IsSubtype "PyType_IsSubtype")
    , [`PyType_HasFeature()`](https://docs.python.org/3/c-api/type.html#c.PyType_HasFeature "PyType_HasFeature")
    
*   `Py_<type>__Check` and `Py_<type>__CheckExact` – for example, [`PyTuple_Check()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Check "PyTuple_Check")
    
*   [“DuringGC” functions](https://docs.python.org/3/c-api/gcsupport.html#duringgc-functions)
    

### “DuringGC” functions[¶](https://docs.python.org/3/c-api/gcsupport.html#duringgc-functions "Link to this heading")

The following functions should _only_ be used in a [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
 handler; calling them in other contexts may have unintended consequences.

These functions act like their counterparts without the `_DuringGC` suffix, but they are guaranteed to not have side effects, they do not set an exception on failure, and they return/set [borrowed references](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 as detailed in the individual documentation.

Note that these functions may fail (return `NULL` or `-1`), but as they do not set an exception, no error information is available. In some cases, failure is not distinguishable from a successful `NULL` result.

void \*PyObject\_GetTypeData\_DuringGC([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*cls)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GetTypeData_DuringGC "Link to this definition")
  

void \*PyObject\_GetItemData\_DuringGC([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GetItemData_DuringGC "Link to this definition")
  

void \*PyType\_GetModuleState\_DuringGC([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetModuleState_DuringGC "Link to this definition")
  

void \*PyModule\_GetState\_DuringGC([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyModule_GetState_DuringGC "Link to this definition")
  

int PyModule\_GetToken\_DuringGC([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*module, void \*\*result)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyModule_GetToken_DuringGC "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

See [“DuringGC” functions](https://docs.python.org/3/c-api/gcsupport.html#duringgc-functions)
 for common information.

Added in version 3.15.

See also

[`PyObject_GetTypeData()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetTypeData "PyObject_GetTypeData")
, [`PyObject_GetItemData()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItemData "PyObject_GetItemData")
, [`PyType_GetModuleState()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleState "PyType_GetModuleState")
, [`PyModule_GetState()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "PyModule_GetState")
, [`PyModule_GetToken()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetToken "PyModule_GetToken")
, [`PyType_GetBaseByToken()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetBaseByToken "PyType_GetBaseByToken")

int PyType\_GetBaseByToken\_DuringGC([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, void \*tp\_token, [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetBaseByToken_DuringGC "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

See [“DuringGC” functions](https://docs.python.org/3/c-api/gcsupport.html#duringgc-functions)
 for common information.

Sets _\*result_ to a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 rather than a strong one. The reference is valid for the duration of the `tp_traverse` handler call.

Added in version 3.15.

See also

[`PyType_GetBaseByToken()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetBaseByToken "PyType_GetBaseByToken")

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GetModule\_DuringGC([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetModule_DuringGC "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyType\_GetModuleByToken\_DuringGC([PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*type, const void \*mod\_token)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetModuleByToken_DuringGC "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

See [“DuringGC” functions](https://docs.python.org/3/c-api/gcsupport.html#duringgc-functions)
 for common information.

These functions return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
, which is valid for the duration of the `tp_traverse` handler call.

Added in version 3.15.

See also

[`PyType_GetModule()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModule "PyType_GetModule")
, [`PyType_GetModuleByToken()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleByToken "PyType_GetModuleByToken")

Controlling the Garbage Collector State[¶](https://docs.python.org/3/c-api/gcsupport.html#controlling-the-garbage-collector-state "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

The C-API provides the following functions for controlling garbage collection runs.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyGC\_Collect(void)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_Collect "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Perform a full garbage collection, if the garbage collector is enabled. (Note that [`gc.collect()`](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect")
 runs it unconditionally.)

Returns the number of collected + unreachable objects which cannot be collected. If the garbage collector is disabled or already collecting, returns `0` immediately. Errors during garbage collection are passed to [`sys.unraisablehook`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook")
. This function does not raise exceptions.

int PyGC\_Enable(void)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_Enable "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Enable the garbage collector: similar to [`gc.enable()`](https://docs.python.org/3/library/gc.html#gc.enable "gc.enable")
. Returns the previous state, 0 for disabled and 1 for enabled.

Added in version 3.10.

int PyGC\_Disable(void)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_Disable "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Disable the garbage collector: similar to [`gc.disable()`](https://docs.python.org/3/library/gc.html#gc.disable "gc.disable")
. Returns the previous state, 0 for disabled and 1 for enabled.

Added in version 3.10.

int PyGC\_IsEnabled(void)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_IsEnabled "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Query the state of the garbage collector: similar to [`gc.isenabled()`](https://docs.python.org/3/library/gc.html#gc.isenabled "gc.isenabled")
. Returns the current state, 0 for disabled and 1 for enabled.

Added in version 3.10.

Querying Garbage Collector State[¶](https://docs.python.org/3/c-api/gcsupport.html#querying-garbage-collector-state "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

The C-API provides the following interface for querying information about the garbage collector.

void PyUnstable\_GC\_VisitObjects([gcvisitobjects\_t](https://docs.python.org/3/c-api/gcsupport.html#c.gcvisitobjects_t "gcvisitobjects_t")
 callback, void \*arg)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.PyUnstable_GC_VisitObjects "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Run supplied _callback_ on all live GC-capable objects. _arg_ is passed through to all invocations of _callback_.

Warning

If new objects are (de)allocated by the callback it is undefined if they will be visited.

Garbage collection is disabled during operation. Explicitly running a collection in the callback may lead to undefined behaviour e.g. visiting the same objects multiple times or not at all.

Added in version 3.12.

typedef int (\*gcvisitobjects\_t)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*object, void \*arg)[¶](https://docs.python.org/3/c-api/gcsupport.html#c.gcvisitobjects_t "Link to this definition")
  

Type of the visitor function to be passed to [`PyUnstable_GC_VisitObjects()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyUnstable_GC_VisitObjects "PyUnstable_GC_VisitObjects")
. _arg_ is the same as the _arg_ passed to `PyUnstable_GC_VisitObjects`. Return `1` to continue iteration, return `0` to stop iteration. Other return values are reserved for now so behavior on returning anything else is undefined.

Added in version 3.12.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Supporting Cyclic Garbage Collection](https://docs.python.org/3/c-api/gcsupport.html#)
    *   [Traversal](https://docs.python.org/3/c-api/gcsupport.html#traversal)
        *   [Traversal-safe functions](https://docs.python.org/3/c-api/gcsupport.html#traversal-safe-functions)
            
        *   [“DuringGC” functions](https://docs.python.org/3/c-api/gcsupport.html#duringgc-functions)
            
    *   [Controlling the Garbage Collector State](https://docs.python.org/3/c-api/gcsupport.html#controlling-the-garbage-collector-state)
        
    *   [Querying Garbage Collector State](https://docs.python.org/3/c-api/gcsupport.html#querying-garbage-collector-state)
        

#### Previous topic

[Type Object Structures](https://docs.python.org/3/c-api/typeobj.html "previous chapter")

#### Next topic

[API and ABI Versioning](https://docs.python.org/3/c-api/apiabiversion.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Supporting+Cyclic+Garbage+Collection&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fgcsupport.html&pagesource=c-api%2Fgcsupport.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/gcsupport.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/apiabiversion.html "API and ABI Versioning")
     |
*   [previous](https://docs.python.org/3/c-api/typeobj.html "Type Object Structures")
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
*   [Supporting Cyclic Garbage Collection](https://docs.python.org/3/c-api/gcsupport.html)
    
*    
    
    |
*   Theme Auto Light Dark |