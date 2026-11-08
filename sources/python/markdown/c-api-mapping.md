### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/iter.html "Iterator Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/sequence.html "Sequence Protocol")
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
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
     »
*   [Mapping Protocol](https://docs.python.org/3/c-api/mapping.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Mapping Protocol[¶](https://docs.python.org/3/c-api/mapping.html#mapping-protocol "Link to this heading")

==========================================================================================================

See also [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
, [`PyObject_SetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetItem "PyObject_SetItem")
 and [`PyObject_DelItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelItem "PyObject_DelItem")
.

int PyMapping\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Check "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return `1` if the object provides the mapping protocol or supports slicing, and `0` otherwise. Note that it returns `1` for Python classes with a [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 method, since in general it is impossible to determine what type of keys the class supports. This function always succeeds.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyMapping\_Size([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Size "Link to this definition")
  

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyMapping\_Length([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Length "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the number of keys in object _o_ on success, and `-1` on failure. This is equivalent to the Python expression `len(o)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMapping\_GetItemString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*key)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetItemString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the same as [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

int PyMapping\_GetOptionalItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetOptionalItem "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Variant of [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
 which doesn’t raise [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 if the key is not found.

If the key is found, return `1` and set _\*result_ to a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the corresponding value. If the key is not found, return `0` and set _\*result_ to `NULL`; the [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is silenced. If an error other than `KeyError` is raised, return `-1` and set _\*result_ to `NULL`.

Added in version 3.13.

int PyMapping\_GetOptionalItemString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, const char \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*result)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetOptionalItemString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

This is the same as [`PyMapping_GetOptionalItem()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetOptionalItem "PyMapping_GetOptionalItem")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

Added in version 3.13.

int PyMapping\_SetItemString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*key, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*v)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_SetItemString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the same as [`PyObject_SetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetItem "PyObject_SetItem")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

int PyMapping\_DelItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_DelItem "Link to this definition")
  

This is an alias of [`PyObject_DelItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelItem "PyObject_DelItem")
.

int PyMapping\_DelItemString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*key)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_DelItemString "Link to this definition")
  

This is the same as [`PyObject_DelItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_DelItem "PyObject_DelItem")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

int PyMapping\_HasKeyWithError([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyWithError "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Return `1` if the mapping object has the key _key_ and `0` otherwise. This is equivalent to the Python expression `key in o`. On failure, return `-1`.

Added in version 3.13.

int PyMapping\_HasKeyStringWithError([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*key)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyStringWithError "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

This is the same as [`PyMapping_HasKeyWithError()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyWithError "PyMapping_HasKeyWithError")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

Added in version 3.13.

int PyMapping\_HasKey([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*key)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKey "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return `1` if the mapping object has the key _key_ and `0` otherwise. This is equivalent to the Python expression `key in o`. This function always succeeds.

Note

Exceptions which occur when this calls the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 method are silently ignored. For proper error handling, use [`PyMapping_HasKeyWithError()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyWithError "PyMapping_HasKeyWithError")
, [`PyMapping_GetOptionalItem()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetOptionalItem "PyMapping_GetOptionalItem")
 or [`PyObject_GetItem()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetItem "PyObject_GetItem")
 instead.

int PyMapping\_HasKeyString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*key)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyString "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the same as [`PyMapping_HasKey()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKey "PyMapping_HasKey")
, but _key_ is specified as a const char\* UTF-8 encoded bytes string, rather than a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

Note

Exceptions that occur when this calls the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 method or while creating the temporary [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object are silently ignored. For proper error handling, use [`PyMapping_HasKeyStringWithError()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_HasKeyStringWithError "PyMapping_HasKeyStringWithError")
, [`PyMapping_GetOptionalItemString()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetOptionalItemString "PyMapping_GetOptionalItemString")
 or [`PyMapping_GetItemString()`](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_GetItemString "PyMapping_GetItemString")
 instead.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMapping\_Keys([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Keys "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

On success, return a list of the keys in object _o_. On failure, return `NULL`.

Changed in version 3.7: Previously, the function returned a list or a tuple.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMapping\_Values([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Values "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

On success, return a list of the values in object _o_. On failure, return `NULL`.

Changed in version 3.7: Previously, the function returned a list or a tuple.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMapping\_Items([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/mapping.html#c.PyMapping_Items "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

On success, return a list of the items in object _o_, where each item is a tuple containing a key-value pair. On failure, return `NULL`.

Changed in version 3.7: Previously, the function returned a list or a tuple.

#### Previous topic

[Sequence Protocol](https://docs.python.org/3/c-api/sequence.html "previous chapter")

#### Next topic

[Iterator Protocol](https://docs.python.org/3/c-api/iter.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Mapping+Protocol&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fmapping.html&pagesource=c-api%2Fmapping.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/mapping.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/iter.html "Iterator Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/sequence.html "Sequence Protocol")
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
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
     »
*   [Mapping Protocol](https://docs.python.org/3/c-api/mapping.html)
    
*    
    
    |
*   Theme Auto Light Dark |