### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/set.html "Set Objects")
     |
*   [previous](https://docs.python.org/3/c-api/list.html "List Objects")
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
*   [Dictionary objects](https://docs.python.org/3/c-api/dict.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Dictionary objects[¶](https://docs.python.org/3/c-api/dict.html#dictionary-objects "Link to this heading")

===========================================================================================================

type PyDictObject[¶](https://docs.python.org/3/c-api/dict.html#c.PyDictObject "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents a Python dictionary object.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDict\_Type[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python dictionary type. This is the same object as [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 in the Python layer.

int PyDict\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Check "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return true if _p_ is a dict object or an instance of a subtype of the dict type. This function always succeeds.

int PyDict\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_CheckExact "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return true if _p_ is a dict object, but not an instance of a subtype of the dict type. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDict\_New()[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a new empty dictionary, or `NULL` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDictProxy\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*mapping)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDictProxy_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a [`types.MappingProxyType`](https://docs.python.org/3/library/types.html#types.MappingProxyType "types.MappingProxyType")
 object for a mapping which enforces read-only behavior. This is normally used to create a view to prevent modification of the dictionary for non-dynamic class types.

The first argument can be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
, a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
, or a mapping.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDictProxy\_Type[¶](https://docs.python.org/3/c-api/dict.html#c.PyDictProxy_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object for mapping proxy objects created by [`PyDictProxy_New()`](https://docs.python.org/3/c-api/dict.html#c.PyDictProxy_New "PyDictProxy_New")
 and for the read-only `__dict__` attribute of many built-in types. A [`PyDictProxy_Type`](https://docs.python.org/3/c-api/dict.html#c.PyDictProxy_Type "PyDictProxy_Type")
 instance provides a dynamic, read-only view of an underlying dictionary: changes to the underlying dictionary are reflected in the proxy, but the proxy itself does not support mutation operations. This corresponds to [`types.MappingProxyType`](https://docs.python.org/3/library/types.html#types.MappingProxyType "types.MappingProxyType")
 in Python.

void PyDict\_Clear([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Clear "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Empty an existing dictionary of all key-value pairs.

Do nothing if the argument is not a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a `dict` subclass.

int PyDict\_Contains([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Contains "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Determine if dictionary _p_ contains _key_. If an item in _p_ matches _key_, return `1`, otherwise return `0`. On error, return `-1`. This is equivalent to the Python expression `key in p`.

The first argument can be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

Note

The operation is atomic on [free threading](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 when _key_ is [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

int PyDict\_ContainsString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, const char \*key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_ContainsString "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

This is the same as [`PyDict_Contains()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Contains "PyDict_Contains")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

The first argument can be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

Added in version 3.13.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDict\_Copy([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Copy "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a new dictionary that contains the same key-value pairs as _p_.

int PyDict\_SetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*val)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetItem "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Insert _val_ into the dictionary _p_ with a key of _key_. _key_ must be [hashable](https://docs.python.org/3/glossary.html#term-hashable)
; if it isn’t, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 will be raised. Return `0` on success or `-1` on failure. This function _does not_ “[steal](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _val_.

Note

The operation is atomic on [free threading](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 when _key_ is [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

int PyDict\_SetItemString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, const char \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*val)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetItemString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

This is the same as [`PyDict_SetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetItem "PyDict_SetItem")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

int PyDict\_DelItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_DelItem "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Remove the entry in dictionary _p_ with key _key_. _key_ must be [hashable](https://docs.python.org/3/glossary.html#term-hashable)
; if it isn’t, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised. If _key_ is not in the dictionary, [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is raised. Return `0` on success or `-1` on failure.

Note

The operation is atomic on [free threading](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 when _key_ is [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

int PyDict\_DelItemString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, const char \*key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_DelItemString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

This is the same as [`PyDict_DelItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_DelItem "PyDict_DelItem")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

int PyDict\_GetItemRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemRef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Return a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the object from dictionary _p_ which has a key _key_:

*   If the key is present, set _\*result_ to a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     to the value and return `1`.
    
*   If the key is missing, set _\*result_ to `NULL` and return `0`.
    
*   On error, raise an exception, set _\*result_ to `NULL` and return `-1`.
    

The first argument can be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

Note

The operation is atomic on [free threading](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 when _key_ is [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Added in version 3.13.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

See also the [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
 function.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDict\_GetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 to the object from dictionary _p_ which has a key _key_. Return `NULL` if the key _key_ is missing _without_ setting an exception.

The first argument can be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

Note

Exceptions that occur while this calls [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
 and [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
 methods are silently ignored. Prefer the [`PyDict_GetItemWithError()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemWithError "PyDict_GetItemWithError")
 function instead.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, the returned [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 may become invalid if another thread modifies the dictionary concurrently. Prefer [`PyDict_GetItemRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemRef "PyDict_GetItemRef")
, which returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
.

Changed in version 3.10: Calling this API without an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 had been allowed for historical reason. It is no longer allowed.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDict\_GetItemWithError([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemWithError "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Variant of [`PyDict_GetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem "PyDict_GetItem")
 that does not suppress exceptions. Return `NULL` **with** an exception set if an exception occurred. Return `NULL` **without** an exception set if the key wasn’t present.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, the returned [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 may become invalid if another thread modifies the dictionary concurrently. Prefer [`PyDict_GetItemRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemRef "PyDict_GetItemRef")
, which returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDict\_GetItemString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, const char \*key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemString "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

This is the same as [`PyDict_GetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem "PyDict_GetItem")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

Note

Exceptions that occur while this calls [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
 and [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
 methods or while creating the temporary [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object are silently ignored. Prefer using the [`PyDict_GetItemWithError()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemWithError "PyDict_GetItemWithError")
 function with your own [`PyUnicode_FromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromString "PyUnicode_FromString")
 _key_ instead.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, the returned [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 may become invalid if another thread modifies the dictionary concurrently. Prefer [`PyDict_GetItemStringRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemStringRef "PyDict_GetItemStringRef")
, which returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

int PyDict\_GetItemStringRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, const char \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemStringRef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Similar to [`PyDict_GetItemRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemRef "PyDict_GetItemRef")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

Added in version 3.13.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDict\_SetDefault([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*defaultobj)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetDefault "Link to this definition")
  

_Return value: Borrowed reference._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

This is the same as the Python-level [`dict.setdefault()`](https://docs.python.org/3/builtins/stdtypes.html#dict.setdefault "dict.setdefault")
. If present, it returns the value corresponding to _key_ from the dictionary _p_. If the key is not in the dict, it is inserted with value _defaultobj_ and _defaultobj_ is returned. This function evaluates the hash function of _key_ only once, instead of evaluating it independently for the lookup and the insertion.

Added in version 3.4.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, the returned [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 may become invalid if another thread modifies the dictionary concurrently. Prefer [`PyDict_SetDefaultRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetDefaultRef "PyDict_SetDefaultRef")
, which returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
.

int PyDict\_SetDefaultRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*default\_value, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetDefaultRef "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Inserts _default\_value_ into the dictionary _p_ with a key of _key_ if the key is not already present in the dictionary. If _result_ is not `NULL`, then _\*result_ is set to a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to either _default\_value_, if the key was not present, or the existing value, if _key_ was already present in the dictionary. Returns `1` if the key was present and _default\_value_ was not inserted, or `0` if the key was not present and _default\_value_ was inserted. On failure, returns `-1`, sets an exception, and sets `*result` to `NULL`.

For clarity: if you have a strong reference to _default\_value_ before calling this function, then after it returns, you hold a strong reference to both _default\_value_ and _\*result_ (if it’s not `NULL`). These may refer to the same object: in that case you hold two separate references to it.

Note

The operation is atomic on [free threading](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 when _key_ is [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Added in version 3.13.

int PyDict\_Pop([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Pop "Link to this definition")
  

_Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Remove _key_ from dictionary _p_ and optionally return the removed value. Do not raise [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 if the key is missing.

*   If the key is present, set _\*result_ to a new reference to the removed value if _result_ is not `NULL`, and return `1`.
    
*   If the key is missing, set _\*result_ to `NULL` if _result_ is not `NULL`, and return `0`.
    
*   On error, raise an exception and return `-1`.
    

Similar to [`dict.pop()`](https://docs.python.org/3/builtins/stdtypes.html#dict.pop "dict.pop")
, but without the default value and not raising [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 if the key is missing.

Note

The operation is atomic on [free threading](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 when _key_ is [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Added in version 3.13.

int PyDict\_PopString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, const char \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_PopString "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Similar to [`PyDict_Pop()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Pop "PyDict_Pop")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

Added in version 3.13.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDict\_Items([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Items "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a [`PyListObject`](https://docs.python.org/3/c-api/list.html#c.PyListObject "PyListObject")
 containing all the items from the dictionary.

The first argument can be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDict\_Keys([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Keys "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a [`PyListObject`](https://docs.python.org/3/c-api/list.html#c.PyListObject "PyListObject")
 containing all the keys from the dictionary.

The first argument can be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyDict\_Values([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Values "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a [`PyListObject`](https://docs.python.org/3/c-api/list.html#c.PyListObject "PyListObject")
 containing all the values from the dictionary _p_.

The first argument can be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyDict\_Size([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Size "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return the number of items in the dictionary. This is equivalent to `len(p)` on a dictionary.

The argument can be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyDict\_GET\_SIZE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_GET_SIZE "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Similar to [`PyDict_Size()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Size "PyDict_Size")
, but without error checking.

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

int PyDict\_Next([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*ppos, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*pkey, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*pvalue)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Next "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Iterate over all key-value pairs in the dictionary _p_. The [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 referred to by _ppos_ must be initialized to `0` prior to the first call to this function to start the iteration; the function returns true for each pair in the dictionary, and false once all pairs have been reported. The parameters _pkey_ and _pvalue_ should either point to [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* variables that will be filled in with each key and value, respectively, or may be `NULL`. Any references returned through them are borrowed. _ppos_ should not be altered during iteration. Its value represents offsets within the internal dictionary structure, and since the structure is sparse, the offsets are not consecutive.

The first argument can be a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

For example:

PyObject \*key, \*value;
Py\_ssize\_t pos \= 0;

while (PyDict\_Next(self\->dict, &pos, &key, &value)) {
    /\* do something interesting with the values... \*/
    ...
}

The dictionary _p_ should not be mutated during iteration. It is safe to modify the values of the keys as you iterate over the dictionary, but only so long as the set of keys does not change. For example:

PyObject \*key, \*value;
Py\_ssize\_t pos \= 0;

while (PyDict\_Next(self\->dict, &pos, &key, &value)) {
    long i \= PyLong\_AsLong(value);
    if (i \== \-1 && PyErr\_Occurred()) {
        return \-1;
    }
    PyObject \*o \= PyLong\_FromLong(i + 1);
    if (o \== NULL)
        return \-1;
    if (PyDict\_SetItem(self\->dict, key, o) < 0) {
        Py\_DECREF(o);
        return \-1;
    }
    Py\_DECREF(o);
}

The function is not thread-safe in the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build without external synchronization for a mutable [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
. You can use [`Py_BEGIN_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION "Py_BEGIN_CRITICAL_SECTION")
 to lock the dictionary while iterating over it:

Py\_BEGIN\_CRITICAL\_SECTION(self\->dict);
while (PyDict\_Next(self\->dict, &pos, &key, &value)) {
    ...
}
Py\_END\_CRITICAL\_SECTION();

The function is thread-safe on a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

Note

On the free-threaded build, this function can be used safely inside a critical section. However, the references returned for _pkey_ and _pvalue_ are [borrowed](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 and are only valid while the critical section is held. If you need to use these objects outside the critical section or when the critical section can be suspended, create a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 (for example, using [`Py_NewRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_NewRef "Py_NewRef")
).

Changed in version 3.15: Also accept [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
.

int PyDict\_Merge([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*a, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*b, int override)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Merge "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Iterate over mapping object _b_ adding key-value pairs to dictionary _a_. _b_ may be a dictionary, or any object supporting [`PyMapping_Keys()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Keys "PyMapping_Keys")
 and [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
. If _override_ is true, existing pairs in _a_ will be replaced if a matching key is found in _b_, otherwise pairs will only be added if there is not a matching key in _a_. Return `0` on success or `-1` if an exception was raised.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, when _b_ is a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 (with the standard iterator), both _a_ and _b_ are locked for the duration of the operation. When _b_ is a non-dict mapping, only _a_ is locked; _b_ may be concurrently modified by another thread.

int PyDict\_Update([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*a, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*b)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Update "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

This is the same as `PyDict_Merge(a, b, 1)` in C, and is similar to `a.update(b)` in Python except that [`PyDict_Update()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Update "PyDict_Update")
 doesn’t fall back to the iterating over a sequence of key value pairs if the second argument has no “keys” attribute. Return `0` on success or `-1` if an exception was raised.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, when _b_ is a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 (with the standard iterator), both _a_ and _b_ are locked for the duration of the operation. When _b_ is a non-dict mapping, only _a_ is locked; _b_ may be concurrently modified by another thread.

int PyDict\_MergeFromSeq2([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*a, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*seq2, int override)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_MergeFromSeq2 "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Update or merge into dictionary _a_, from the key-value pairs in _seq2_. _seq2_ must be an iterable object producing iterable objects of length 2, viewed as key-value pairs. In case of duplicate keys, the last wins if _override_ is true, else the first wins. Return `0` on success or `-1` if an exception was raised. Equivalent Python (except for the return value):

def PyDict\_MergeFromSeq2(a, seq2, override):
    for key, value in seq2:
        if override or key not in a:
            a\[key\] \= value

Note

In the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build, only _a_ is locked. The iteration over _seq2_ is not synchronized; _seq2_ may be concurrently modified by another thread.

int PyDict\_AddWatcher([PyDict\_WatchCallback](https://docs.python.org/3/c-api/dict.html#c.PyDict_WatchCallback "PyDict_WatchCallback")
 callback)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_AddWatcher "Link to this definition")
  

_Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Register _callback_ as a dictionary watcher. Return a non-negative integer id which must be passed to future calls to [`PyDict_Watch()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Watch "PyDict_Watch")
. In case of error (e.g. no more watcher IDs available), return `-1` and set an exception.

Note

This function is not internally synchronized. In the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build, callers should ensure no concurrent calls to [`PyDict_AddWatcher()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_AddWatcher "PyDict_AddWatcher")
 or [`PyDict_ClearWatcher()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_ClearWatcher "PyDict_ClearWatcher")
 are in progress.

Added in version 3.12.

int PyDict\_ClearWatcher(int watcher\_id)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_ClearWatcher "Link to this definition")
  

_Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Clear watcher identified by _watcher\_id_ previously returned from [`PyDict_AddWatcher()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_AddWatcher "PyDict_AddWatcher")
. Return `0` on success, `-1` on error (e.g. if the given _watcher\_id_ was never registered.)

Note

This function is not internally synchronized. In the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build, callers should ensure no concurrent calls to [`PyDict_AddWatcher()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_AddWatcher "PyDict_AddWatcher")
 or [`PyDict_ClearWatcher()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_ClearWatcher "PyDict_ClearWatcher")
 are in progress.

Added in version 3.12.

int PyDict\_Watch(int watcher\_id, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*dict)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Watch "Link to this definition")
  

_Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Mark dictionary _dict_ as watched. The callback granted _watcher\_id_ by [`PyDict_AddWatcher()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_AddWatcher "PyDict_AddWatcher")
 will be called when _dict_ is modified or deallocated. Return `0` on success or `-1` on error.

Added in version 3.12.

int PyDict\_Unwatch(int watcher\_id, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*dict)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_Unwatch "Link to this definition")
  

_Thread safety: [Safe to call without external synchronization on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-distinct)
._

Mark dictionary _dict_ as no longer watched. The callback granted _watcher\_id_ by [`PyDict_AddWatcher()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_AddWatcher "PyDict_AddWatcher")
 will no longer be called when _dict_ is modified or deallocated. The dict must previously have been watched by this watcher. Return `0` on success or `-1` on error.

Added in version 3.12.

type PyDict\_WatchEvent[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_WatchEvent "Link to this definition")
  

Enumeration of possible dictionary watcher events: `PyDict_EVENT_ADDED`, `PyDict_EVENT_MODIFIED`, `PyDict_EVENT_DELETED`, `PyDict_EVENT_CLONED`, `PyDict_EVENT_CLEARED`, or `PyDict_EVENT_DEALLOCATED`.

Added in version 3.12.

PY\_FOREACH\_DICT\_EVENT(V)[¶](https://docs.python.org/3/c-api/dict.html#c.PY_FOREACH_DICT_EVENT "Link to this definition")
  

Apply the macro _V_ to each suffix of [`PyDict_WatchEvent`](https://docs.python.org/3/c-api/dict.html#c.PyDict_WatchEvent "PyDict_WatchEvent")
 constants. Currently expands to `V(ADDED) V(MODIFIED) V(DELETED) V(CLONED) V(CLEARED) V(DEALLOCATED)`. The macro _V_ must accept one event name and supply any punctuation needed between expansions.

typedef int (\*PyDict\_WatchCallback)([PyDict\_WatchEvent](https://docs.python.org/3/c-api/dict.html#c.PyDict_WatchEvent "PyDict_WatchEvent")
 event, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*dict, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*new\_value)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDict_WatchCallback "Link to this definition")
  

Type of a dict watcher callback function.

If _event_ is `PyDict_EVENT_CLEARED` or `PyDict_EVENT_DEALLOCATED`, both _key_ and _new\_value_ will be `NULL`. If _event_ is `PyDict_EVENT_ADDED` or `PyDict_EVENT_MODIFIED`, _new\_value_ will be the new value for _key_. If _event_ is `PyDict_EVENT_DELETED`, _key_ is being deleted from the dictionary and _new\_value_ will be `NULL`.

`PyDict_EVENT_CLONED` occurs when _dict_ was previously empty and another dict is merged into it. To maintain efficiency of this operation, per-key `PyDict_EVENT_ADDED` events are not issued in this case; instead a single `PyDict_EVENT_CLONED` is issued, and _key_ will be the source dictionary.

The callback may inspect but must not modify _dict_; doing so could have unpredictable effects, including infinite recursion. Do not trigger Python code execution in the callback, as it could modify the dict as a side effect.

If _event_ is `PyDict_EVENT_DEALLOCATED`, taking a new reference in the callback to the about-to-be-destroyed dictionary will resurrect it and prevent it from being freed at this time. When the resurrected object is destroyed later, any watcher callbacks active at that time will be called again.

Callbacks occur before the notified modification to _dict_ takes place, so the prior state of _dict_ can be inspected.

If the callback sets an exception, it must return `-1`; this exception will be printed as an unraisable exception using [`PyErr_WriteUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WriteUnraisable "PyErr_WriteUnraisable")
. Otherwise it should return `0`.

There may already be a pending exception set on entry to the callback. In this case, the callback should return `0` with the same exception still set. This means the callback may not call any other API that can set an exception unless it saves and clears the exception state first, and restores it before returning.

Added in version 3.12.

Dictionary view objects[¶](https://docs.python.org/3/c-api/dict.html#dictionary-view-objects "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

int PyDictViewSet\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDictViewSet_Check "Link to this definition")
  

Return true if _op_ is a view of a set inside a dictionary. This is currently equivalent to [PyDictKeys\_Check](https://docs.python.org/3/c-api/dict.html#c.PyDictKeys_Check "PyDictKeys_Check")
([op](https://docs.python.org/3/c-api/dict.html#c.PyDictViewSet_Check "op")
) || [PyDictItems\_Check](https://docs.python.org/3/c-api/dict.html#c.PyDictItems_Check "PyDictItems_Check")
(op). This function always succeeds.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDictKeys\_Type[¶](https://docs.python.org/3/c-api/dict.html#c.PyDictKeys_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Type object for a view of dictionary keys. In Python, this is the type of the object returned by [`dict.keys()`](https://docs.python.org/3/builtins/stdtypes.html#dict.keys "dict.keys")
.

int PyDictKeys\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDictKeys_Check "Link to this definition")
  

Return true if _op_ is an instance of a dictionary keys view. This function always succeeds.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDictValues\_Type[¶](https://docs.python.org/3/c-api/dict.html#c.PyDictValues_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Type object for a view of dictionary values. In Python, this is the type of the object returned by [`dict.values()`](https://docs.python.org/3/builtins/stdtypes.html#dict.values "dict.values")
.

int PyDictValues\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDictValues_Check "Link to this definition")
  

Return true if _op_ is an instance of a dictionary values view. This function always succeeds.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDictItems\_Type[¶](https://docs.python.org/3/c-api/dict.html#c.PyDictItems_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Type object for a view of dictionary items. In Python, this is the type of the object returned by [`dict.items()`](https://docs.python.org/3/builtins/stdtypes.html#dict.items "dict.items")
.

int PyDictItems\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/dict.html#c.PyDictItems_Check "Link to this definition")
  

Return true if _op_ is an instance of a dictionary items view. This function always succeeds.

Frozen dictionary objects[¶](https://docs.python.org/3/c-api/dict.html#frozen-dictionary-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

Added in version 3.15.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyFrozenDict\_Type[¶](https://docs.python.org/3/c-api/dict.html#c.PyFrozenDict_Type "Link to this definition")
  

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python frozen dictionary type. This is the same object as [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
 in the Python layer.

int PyAnyDict\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyAnyDict_Check "Link to this definition")
  

Return true if _p_ is a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 object, a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
 object, or an instance of a subtype of the `dict` or `frozendict` type. This function always succeeds.

int PyAnyDict\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyAnyDict_CheckExact "Link to this definition")
  

Return true if _p_ is a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 object or a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
 object, but not an instance of a subtype of the `dict` or `frozendict` type. This function always succeeds.

int PyFrozenDict\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyFrozenDict_Check "Link to this definition")
  

Return true if _p_ is a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
 object or an instance of a subtype of the `frozendict` type. This function always succeeds.

int PyFrozenDict\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/dict.html#c.PyFrozenDict_CheckExact "Link to this definition")
  

Return true if _p_ is a [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
 object, but not an instance of a subtype of the `frozendict` type. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFrozenDict\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*iterable)[¶](https://docs.python.org/3/c-api/dict.html#c.PyFrozenDict_New "Link to this definition")
  

Return a new [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
 from an iterable, or `NULL` on failure with an exception set.

Create an empty dictionary if _iterable_ is `NULL`.

Ordered dictionaries[¶](https://docs.python.org/3/c-api/dict.html#ordered-dictionaries "Link to this heading")

---------------------------------------------------------------------------------------------------------------

Python’s C API provides interface for [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict")
 from C. Since Python 3.7, dictionaries are ordered by default, so there is usually little need for these functions; prefer `PyDict*` where possible.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyODict\_Type[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_Type "Link to this definition")
  

Type object for ordered dictionaries. This is the same object as [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict")
 in the Python layer.

int PyODict\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*od)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_Check "Link to this definition")
  

Return true if _od_ is an ordered dictionary object or an instance of a subtype of the [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict")
 type. This function always succeeds.

int PyODict\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*od)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_CheckExact "Link to this definition")
  

Return true if _od_ is an ordered dictionary object, but not an instance of a subtype of the [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict")
 type. This function always succeeds.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyODictKeys\_Type[¶](https://docs.python.org/3/c-api/dict.html#c.PyODictKeys_Type "Link to this definition")
  

Analogous to [`PyDictKeys_Type`](https://docs.python.org/3/c-api/dict.html#c.PyDictKeys_Type "PyDictKeys_Type")
 for ordered dictionaries.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyODictValues\_Type[¶](https://docs.python.org/3/c-api/dict.html#c.PyODictValues_Type "Link to this definition")
  

Analogous to [`PyDictValues_Type`](https://docs.python.org/3/c-api/dict.html#c.PyDictValues_Type "PyDictValues_Type")
 for ordered dictionaries.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyODictItems\_Type[¶](https://docs.python.org/3/c-api/dict.html#c.PyODictItems_Type "Link to this definition")
  

Analogous to [`PyDictItems_Type`](https://docs.python.org/3/c-api/dict.html#c.PyDictItems_Type "PyDictItems_Type")
 for ordered dictionaries.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyODict\_New(void)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_New "Link to this definition")
  

Return a new empty ordered dictionary, or `NULL` on failure.

This is analogous to [`PyDict_New()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_New "PyDict_New")
.

int PyODict\_SetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*od, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_SetItem "Link to this definition")
  

Insert _value_ into the ordered dictionary _od_ with a key of _key_. Return `0` on success or `-1` with an exception set on failure.

This is analogous to [`PyDict_SetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetItem "PyDict_SetItem")
.

int PyODict\_DelItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*od, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_DelItem "Link to this definition")
  

Remove the entry in the ordered dictionary _od_ with key _key_. Return `0` on success or `-1` with an exception set on failure.

This is analogous to [`PyDict_DelItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_DelItem "PyDict_DelItem")
.

These are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 aliases to `PyDict` APIs:

| `PyODict` | `PyDict` |
| --- | --- |
| PyODict\_GetItem(od, key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_GetItem "Link to this definition") | [`PyDict_GetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem "PyDict_GetItem") |
| PyODict\_GetItemWithError(od, key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_GetItemWithError "Link to this definition") | [`PyDict_GetItemWithError()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemWithError "PyDict_GetItemWithError") |
| PyODict\_GetItemString(od, key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_GetItemString "Link to this definition") | [`PyDict_GetItemString()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemString "PyDict_GetItemString") |
| PyODict\_Contains(od, key)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_Contains "Link to this definition") | [`PyDict_Contains()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Contains "PyDict_Contains") |
| PyODict\_Size(od)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_Size "Link to this definition") | [`PyDict_Size()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Size "PyDict_Size") |
| PyODict\_SIZE(od)[¶](https://docs.python.org/3/c-api/dict.html#c.PyODict_SIZE "Link to this definition") | [`PyDict_GET_SIZE()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GET_SIZE "PyDict_GET_SIZE") |

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Dictionary objects](https://docs.python.org/3/c-api/dict.html#)
    *   [Dictionary view objects](https://docs.python.org/3/c-api/dict.html#dictionary-view-objects)
        
    *   [Frozen dictionary objects](https://docs.python.org/3/c-api/dict.html#frozen-dictionary-objects)
        
    *   [Ordered dictionaries](https://docs.python.org/3/c-api/dict.html#ordered-dictionaries)
        

#### Previous topic

[List Objects](https://docs.python.org/3/c-api/list.html "previous chapter")

#### Next topic

[Set Objects](https://docs.python.org/3/c-api/set.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Dictionary+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fdict.html&pagesource=c-api%2Fdict.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/dict.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/set.html "Set Objects")
     |
*   [previous](https://docs.python.org/3/c-api/list.html "List Objects")
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
*   [Dictionary objects](https://docs.python.org/3/c-api/dict.html)
    
*    
    
    |
*   Theme Auto Light Dark |