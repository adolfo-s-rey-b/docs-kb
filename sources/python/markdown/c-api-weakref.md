### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/capsule.html "Capsules")
     |
*   [previous](https://docs.python.org/3/c-api/picklebuffer.html "Pickle buffer objects")
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
*   [Weak Reference Objects](https://docs.python.org/3/c-api/weakref.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Weak Reference Objects[¶](https://docs.python.org/3/c-api/weakref.html#weak-reference-objects "Link to this heading")

======================================================================================================================

Python supports _weak references_ as first-class objects. There are two specific object types which directly implement weak references. The first is a simple reference object, and the second acts as a proxy for the original object as much as it can.

int PyWeakref\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_Check "Link to this definition")
  

Return non-zero if _ob_ is either a reference or proxy object. This function always succeeds.

int PyWeakref\_CheckRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_CheckRef "Link to this definition")
  

Return non-zero if _ob_ is a reference object or a subclass of the reference type. This function always succeeds.

int PyWeakref\_CheckRefExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_CheckRefExact "Link to this definition")
  

Return non-zero if _ob_ is a reference object, but not a subclass of the reference type. This function always succeeds.

int PyWeakref\_CheckProxy([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_CheckProxy "Link to this definition")
  

Return non-zero if _ob_ is a proxy object. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyWeakref\_NewRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callback)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_NewRef "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a weak reference object for the object _ob_. This will always return a new reference, but is not guaranteed to create a new object; an existing reference object may be returned. The second parameter, _callback_, can be a callable object that receives notification when _ob_ is garbage collected; it should accept a single parameter, which will be the weak reference object itself. _callback_ may also be `None` or `NULL`. If _ob_ is not a weakly referenceable object, this will raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 and return `NULL`.

See also

[`PyType_SUPPORTS_WEAKREFS()`](https://docs.python.org/3/c-api/type.html#c.PyType_SUPPORTS_WEAKREFS "PyType_SUPPORTS_WEAKREFS")
 for checking if _ob_ is weakly referenceable.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyWeakref\_NewProxy([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callback)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_NewProxy "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a weak reference proxy object for the object _ob_. This will always return a new reference, but is not guaranteed to create a new object; an existing proxy object may be returned. The second parameter, _callback_, can be a callable object that receives notification when _ob_ is garbage collected; it should accept a single parameter, which will be the weak reference object itself. _callback_ may also be `None` or `NULL`. If _ob_ weakly referenceable object, this will raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 and return `NULL`.

See also

[`PyType_SUPPORTS_WEAKREFS()`](https://docs.python.org/3/c-api/type.html#c.PyType_SUPPORTS_WEAKREFS "PyType_SUPPORTS_WEAKREFS")
 for checking if _ob_ is weakly referenceable.

int PyWeakref\_GetRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ref, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*pobj)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_GetRef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Get a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the referenced object from a weak reference, _ref_, into _\*pobj_.

*   On success, set _\*pobj_ to a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     to the referenced object and return 1.
    
*   If the reference is dead, set _\*pobj_ to `NULL` and return 0.
    
*   On error, raise an exception and return -1.
    

Added in version 3.13.

int PyWeakref\_IsDead([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ref)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_IsDead "Link to this definition")
  

Test if the weak reference _ref_ is dead. Returns 1 if the reference is dead, 0 if it is alive, and -1 with an error set if _ref_ is not a weak reference object.

Added in version 3.14.

void PyObject\_ClearWeakRefs([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*object)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyObject_ClearWeakRefs "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This function is called by the [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
 handler to clear weak references.

This iterates through the weak references for _object_ and calls callbacks for those references which have one. It returns when all callbacks have been attempted.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*PyObject\_GET\_WEAKREFS\_LISTPTR([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*object)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyObject_GET_WEAKREFS_LISTPTR "Link to this definition")
  

Return a pointer to an internal linked list of weak references to _object_. _object_ must support weak references and must not be `NULL`.

This function is intended for internal use only. Do not access or modify the weak reference list through the returned pointer.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.2.

void PyUnstable\_Object\_ClearWeakRefsNoCallbacks([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*object)[¶](https://docs.python.org/3/c-api/weakref.html#c.PyUnstable_Object_ClearWeakRefsNoCallbacks "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Clears the weakrefs for _object_ without calling the callbacks.

This function is called by the [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
 handler for types with finalizers (i.e., [`__del__()`](https://docs.python.org/3/reference/datamodel.html#object.__del__ "object.__del__")
). The handler for those objects first calls [`PyObject_ClearWeakRefs()`](https://docs.python.org/3/c-api/weakref.html#c.PyObject_ClearWeakRefs "PyObject_ClearWeakRefs")
 to clear weakrefs and call their callbacks, then the finalizer, and finally this function to clear any weakrefs that may have been created by the finalizer.

In most circumstances, it’s more appropriate to use [`PyObject_ClearWeakRefs()`](https://docs.python.org/3/c-api/weakref.html#c.PyObject_ClearWeakRefs "PyObject_ClearWeakRefs")
 to clear weakrefs instead of this function.

Added in version 3.13.

#### Previous topic

[Pickle buffer objects](https://docs.python.org/3/c-api/picklebuffer.html "previous chapter")

#### Next topic

[Capsules](https://docs.python.org/3/c-api/capsule.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Weak+Reference+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fweakref.html&pagesource=c-api%2Fweakref.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/weakref.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/capsule.html "Capsules")
     |
*   [previous](https://docs.python.org/3/c-api/picklebuffer.html "Pickle buffer objects")
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
*   [Weak Reference Objects](https://docs.python.org/3/c-api/weakref.html)
    
*    
    
    |
*   Theme Auto Light Dark |