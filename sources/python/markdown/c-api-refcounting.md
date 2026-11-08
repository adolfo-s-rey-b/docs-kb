### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/exceptions.html "Exception Handling")
     |
*   [previous](https://docs.python.org/3/c-api/veryhigh.html "The Very High Level Layer")
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
*   [Reference Counting](https://docs.python.org/3/c-api/refcounting.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Reference Counting[¶](https://docs.python.org/3/c-api/refcounting.html#reference-counting "Link to this heading")

==================================================================================================================

The functions and macros in this section are used for managing reference counts of Python objects.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 Py\_REFCNT([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Get the reference count of the Python object _o_.

Note that the returned value may not actually reflect how many references to the object are actually held. For example, some objects are [immortal](https://docs.python.org/3/glossary.html#term-immortal)
 and have a very high refcount that does not reflect the actual number of references. Consequently, do not rely on the returned value to be accurate, other than a value of 0 or 1.

Use the [`Py_SET_REFCNT()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_SET_REFCNT "Py_SET_REFCNT")
 function to set an object reference count.

Note

On [free-threaded builds](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 of Python, returning 1 isn’t sufficient to determine if it’s safe to treat _o_ as having no access by other threads. Use [`PyUnstable_Object_IsUniquelyReferenced()`](https://docs.python.org/3/c-api/object.html#c.PyUnstable_Object_IsUniquelyReferenced "PyUnstable_Object_IsUniquelyReferenced")
 for that instead.

See also the function [`PyUnstable_Object_IsUniqueReferencedTemporary()`](https://docs.python.org/3/c-api/object.html#c.PyUnstable_Object_IsUniqueReferencedTemporary "PyUnstable_Object_IsUniqueReferencedTemporary")
.

Changed in version 3.10: [`Py_REFCNT()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT")
 is changed to the inline static function.

Changed in version 3.11: The parameter type is no longer const [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

void Py\_SET\_REFCNT([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 refcnt)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_SET_REFCNT "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.9._

Set the object _o_ reference counter to _refcnt_.

On [Python build with Free Threading](https://docs.python.org/3/using/configure.html#free-threading-build)
, if _refcnt_ is larger than `UINT32_MAX`, the object is made [immortal](https://docs.python.org/3/glossary.html#term-immortal)
.

This function has no effect on [immortal](https://docs.python.org/3/glossary.html#term-immortal)
 objects.

Added in version 3.9.

Changed in version 3.12: Immortal objects are not modified.

void Py\_INCREF([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Indicate taking a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to object _o_, indicating it is in use and should not be destroyed.

This function has no effect on [immortal](https://docs.python.org/3/glossary.html#term-immortal)
 objects.

This function is usually used to convert a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 to a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 in-place. The [`Py_NewRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_NewRef "Py_NewRef")
 function can be used to create a new strong reference.

When done using the object, release is by calling [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
.

The object must not be `NULL`; if you aren’t sure that it isn’t `NULL`, use [`Py_XINCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XINCREF "Py_XINCREF")
.

Do not expect this function to actually modify _o_ in any way. For at least [**some objects**](https://peps.python.org/pep-0683/)
, this function has no effect.

Changed in version 3.12: Immortal objects are not modified.

void Py\_XINCREF([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_XINCREF "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "Py_INCREF")
, but the object _o_ can be `NULL`, in which case this has no effect.

See also [`Py_XNewRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XNewRef "Py_XNewRef")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_NewRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_NewRef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Create a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to an object: call [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "Py_INCREF")
 on _o_ and return the object _o_.

When the [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 is no longer needed, [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 should be called on it to release the reference.

The object _o_ must not be `NULL`; use [`Py_XNewRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XNewRef "Py_XNewRef")
 if _o_ can be `NULL`.

For example:

Py\_INCREF(obj);
self\->attr \= obj;

can be written as:

self\->attr \= Py\_NewRef(obj);

See also [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "Py_INCREF")
.

Added in version 3.10.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_XNewRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_XNewRef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Similar to [`Py_NewRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_NewRef "Py_NewRef")
, but the object _o_ can be NULL.

If the object _o_ is `NULL`, the function just returns `NULL`.

Added in version 3.10.

void Py\_DECREF([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Release a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to object _o_, indicating the reference is no longer used.

This function has no effect on [immortal](https://docs.python.org/3/glossary.html#term-immortal)
 objects.

Once the last [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 is released (i.e. the object’s reference count reaches 0), the object’s type’s deallocation function (which must not be `NULL`) is invoked.

This function is usually used to delete a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 before exiting its scope.

The object must not be `NULL`; if you aren’t sure that it isn’t `NULL`, use [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF")
.

Do not expect this function to actually modify _o_ in any way. For at least [**some objects**](https://peps.python.org/pep-0683/)
, this function has no effect.

Warning

The deallocation function can cause arbitrary Python code to be invoked (e.g. when a class instance with a [`__del__()`](https://docs.python.org/3/reference/datamodel.html#object.__del__ "object.__del__")
 method is deallocated). While exceptions in such code are not propagated, the executed code has free access to all Python global variables. This means that any object that is reachable from a global variable should be in a consistent state before [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
 is invoked. For example, code to delete an object from a list should copy a reference to the deleted object in a temporary variable, update the list data structure, and then call `Py_DECREF()` for the temporary variable.

Changed in version 3.12: Immortal objects are not modified.

void Py\_XDECREF([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
, but the object _o_ can be `NULL`, in which case this has no effect. The same warning from `Py_DECREF()` applies here as well.

void Py\_CLEAR([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_CLEAR "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Release a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 for object _o_. The object may be `NULL`, in which case the macro has no effect; otherwise the effect is the same as for [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
, except that the argument is also set to `NULL`. The warning for `Py_DECREF()` does not apply with respect to the object passed because the macro carefully uses a temporary variable and sets the argument to `NULL` before releasing the reference.

It is a good idea to use this macro whenever releasing a reference to an object that might be traversed during garbage collection.

Changed in version 3.12: The macro argument is now only evaluated once. If the argument has side effects, these are no longer duplicated.

void Py\_IncRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_IncRef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Indicate taking a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to object _o_. A function version of [`Py_XINCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XINCREF "Py_XINCREF")
. It can be used for runtime dynamic embedding of Python.

void Py\_DecRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_DecRef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Release a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to object _o_. A function version of [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF")
. It can be used for runtime dynamic embedding of Python.

Py\_SETREF(dst, src)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_SETREF "Link to this definition")
  

Macro safely releasing a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to object _dst_ and setting _dst_ to _src_.

As in case of [`Py_CLEAR()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_CLEAR "Py_CLEAR")
, “the obvious” code can be deadly:

Py\_DECREF(dst);
dst \= src;

The safe way is:

Py\_SETREF(dst, src);

That arranges to set _dst_ to _src_ _before_ releasing the reference to the old value of _dst_, so that any code triggered as a side-effect of _dst_ getting torn down no longer believes _dst_ points to a valid object.

Added in version 3.6.

Changed in version 3.12: The macro arguments are now only evaluated once. If an argument has side effects, these are no longer duplicated.

Py\_XSETREF(dst, src)[¶](https://docs.python.org/3/c-api/refcounting.html#c.Py_XSETREF "Link to this definition")
  

Variant of [`Py_SETREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_SETREF "Py_SETREF")
 macro that uses [`Py_XDECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "Py_XDECREF")
 instead of [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
.

Added in version 3.6.

Changed in version 3.12: The macro arguments are now only evaluated once. If an argument has side effects, these are no longer duplicated.

#### Previous topic

[The Very High Level Layer](https://docs.python.org/3/c-api/veryhigh.html "previous chapter")

#### Next topic

[Exception Handling](https://docs.python.org/3/c-api/exceptions.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Reference+Counting&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Frefcounting.html&pagesource=c-api%2Frefcounting.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/refcounting.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/exceptions.html "Exception Handling")
     |
*   [previous](https://docs.python.org/3/c-api/veryhigh.html "The Very High Level Layer")
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
*   [Reference Counting](https://docs.python.org/3/c-api/refcounting.html)
    
*    
    
    |
*   Theme Auto Light Dark |