### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/mapping.html "Mapping Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/number.html "Number Protocol")
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
*   [Sequence Protocol](https://docs.python.org/3/c-api/sequence.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Sequence Protocol[¶](https://docs.python.org/3/c-api/sequence.html#sequence-protocol "Link to this heading")

=============================================================================================================

int PySequence\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Check "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return `1` if the object provides the sequence protocol, and `0` otherwise. Note that it returns `1` for Python classes with a [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 method, unless they are [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 subclasses, since in general it is impossible to determine what type of keys the class supports. This function always succeeds.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PySequence\_Size([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Size "Link to this definition")
  

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PySequence\_Length([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Length "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Returns the number of objects in sequence _o_ on success, and `-1` on failure. This is equivalent to the Python expression `len(o)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_Concat([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Concat "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the concatenation of _o1_ and _o2_ on success, and `NULL` on failure. This is the equivalent of the Python expression `o1 + o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_Repeat([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 count)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Repeat "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the result of repeating sequence object _o_ _count_ times, or `NULL` on failure. This is the equivalent of the Python expression `o * count`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_InPlaceConcat([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o1, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o2)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_InPlaceConcat "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the concatenation of _o1_ and _o2_ on success, and `NULL` on failure. The operation is done _in-place_ when _o1_ supports it. This is the equivalent of the Python expression `o1 += o2`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_InPlaceRepeat([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 count)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_InPlaceRepeat "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the result of repeating sequence object _o_ _count_ times, or `NULL` on failure. The operation is done _in-place_ when _o_ supports it. This is the equivalent of the Python expression `o *= count`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_GetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetItem "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the _i_th element of _o_, or `NULL` on failure. This is the equivalent of the Python expression `o[i]`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_GetSlice([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i1, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i2)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetSlice "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the slice of sequence object _o_ between _i1_ and _i2_, or `NULL` on failure. This is the equivalent of the Python expression `o[i1:i2]`.

int PySequence\_SetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*v)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_SetItem "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Assign object _v_ to the _i_th element of _o_. Raise an exception and return `-1` on failure; return `0` on success. This is the equivalent of the Python statement `o[i] = v`. This function _does not_ “[steal](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _v_.

If _v_ is `NULL`, the element is deleted, but this feature is deprecated in favour of using [`PySequence_DelItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_DelItem "PySequence_DelItem")
.

int PySequence\_DelItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_DelItem "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Delete the _i_th element of object _o_. Returns `-1` on failure. This is the equivalent of the Python statement `del o[i]`.

int PySequence\_SetSlice([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i1, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i2, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*v)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_SetSlice "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Assign the sequence object _v_ to the slice in sequence object _o_ from _i1_ to _i2_. This is the equivalent of the Python statement `o[i1:i2] = v`.

int PySequence\_DelSlice([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i1, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i2)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_DelSlice "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Delete the slice in sequence object _o_ from _i1_ to _i2_. Returns `-1` on failure. This is the equivalent of the Python statement `del o[i1:i2]`.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PySequence\_Count([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Count "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the number of occurrences of _value_ in _o_, that is, return the number of keys for which `o[key] == value`. On failure, return `-1`. This is equivalent to the Python expression `o.count(value)`.

int PySequence\_Contains([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Contains "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Determine if _o_ contains _value_. If an item in _o_ is equal to _value_, return `1`, otherwise return `0`. On error, return `-1`. This is equivalent to the Python expression `value in o`.

int PySequence\_In([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_In "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Alias for [`PySequence_Contains()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Contains "PySequence_Contains")
.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.14: The function should no longer be used to write new code.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PySequence\_Index([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Index "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the first index _i_ for which `o[i] == value`. On error, return `-1`. This is equivalent to the Python expression `o.index(value)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_List([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_List "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a list object with the same contents as the sequence or iterable _o_, or `NULL` on failure. The returned list is guaranteed to be new. This is equivalent to the Python expression `list(o)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_Tuple([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Tuple "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a tuple object with the same contents as the sequence or iterable _o_, or `NULL` on failure. If _o_ is a tuple, a new reference will be returned, otherwise a tuple will be constructed with the appropriate contents. This is equivalent to the Python expression `tuple(o)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_Fast([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, const char \*m)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the sequence or iterable _o_ as an object usable by the other `PySequence_Fast*` family of functions. If the object is not a sequence or iterable, raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 with _m_ as the message text. Returns `NULL` on failure.

The `PySequence_Fast*` functions are thus named because they assume _o_ is a [`PyTupleObject`](https://docs.python.org/3/c-api/tuple.html#c.PyTupleObject "PyTupleObject")
 or a [`PyListObject`](https://docs.python.org/3/c-api/list.html#c.PyListObject "PyListObject")
 and access the data fields of _o_ directly.

As a CPython implementation detail, if _o_ is already a sequence or list, it will be returned.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PySequence\_Fast\_GET\_SIZE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast_GET_SIZE "Link to this definition")
  

Returns the length of _o_, assuming that _o_ was returned by [`PySequence_Fast()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast "PySequence_Fast")
 and that _o_ is not `NULL`. The size can also be retrieved by calling [`PySequence_Size()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Size "PySequence_Size")
 on _o_, but [`PySequence_Fast_GET_SIZE()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast_GET_SIZE "PySequence_Fast_GET_SIZE")
 is faster because it can assume _o_ is a list or tuple.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_Fast\_GET\_ITEM([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast_GET_ITEM "Link to this definition")
  

_Return value: Borrowed reference._

Return the _i_th element of _o_, assuming that _o_ was returned by [`PySequence_Fast()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast "PySequence_Fast")
, _o_ is not `NULL`, and that _i_ is within bounds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*PySequence\_Fast\_ITEMS([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast_ITEMS "Link to this definition")
  

Return the underlying array of PyObject pointers. Assumes that _o_ was returned by [`PySequence_Fast()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast "PySequence_Fast")
 and _o_ is not `NULL`.

Note, if a list gets resized, the reallocation may relocate the items array. So, only use the underlying array pointer in contexts where the sequence cannot change.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySequence\_ITEM([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i)[¶](https://docs.python.org/3/c-api/sequence.html#c.PySequence_ITEM "Link to this definition")
  

_Return value: New reference._

Return the _i_th element of _o_ or `NULL` on failure. Faster form of [`PySequence_GetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetItem "PySequence_GetItem")
 but without checking that [`PySequence_Check()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Check "PySequence_Check")
 on _o_ is true and without adjustment for negative indices.

#### Previous topic

[Number Protocol](https://docs.python.org/3/c-api/number.html "previous chapter")

#### Next topic

[Mapping Protocol](https://docs.python.org/3/c-api/mapping.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Sequence+Protocol&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fsequence.html&pagesource=c-api%2Fsequence.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/sequence.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/mapping.html "Mapping Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/number.html "Number Protocol")
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
*   [Sequence Protocol](https://docs.python.org/3/c-api/sequence.html)
    
*    
    
    |
*   Theme Auto Light Dark |