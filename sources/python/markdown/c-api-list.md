### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/dict.html "Dictionary objects")
     |
*   [previous](https://docs.python.org/3/c-api/tuple.html "Tuple Objects")
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
*   [List Objects](https://docs.python.org/3/c-api/list.html)
    
*    
    
    |
*   Theme Auto Light Dark |

List Objects[¶](https://docs.python.org/3/c-api/list.html#list-objects "Link to this heading")

===============================================================================================

type PyListObject[¶](https://docs.python.org/3/c-api/list.html#c.PyListObject "Link to this definition")
  

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 represents a Python list object.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyList\_Type[¶](https://docs.python.org/3/c-api/list.html#c.PyList_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python list type. This is the same object as [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 in the Python layer.

int PyList\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_Check "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return true if _p_ is a list object or an instance of a subtype of the list type. This function always succeeds.

int PyList\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*p)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_CheckExact "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return true if _p_ is a list object, but not an instance of a subtype of the list type. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyList\_New([Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a new list of length _len_ on success, or `NULL` on failure.

Note

If _len_ is greater than zero, the returned list object’s items are set to `NULL`. Thus you cannot use abstract API functions such as [`PySequence_SetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_SetItem "PySequence_SetItem")
 or expose the object to Python code before setting all items to a real object with [`PyList_SetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_SetItem "PyList_SetItem")
 or [`PyList_SET_ITEM()`](https://docs.python.org/3/c-api/list.html#c.PyList_SET_ITEM "PyList_SET_ITEM")
. The following APIs are safe APIs before the list is fully initialized: `PyList_SetItem()` and `PyList_SET_ITEM()`.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyList\_Size([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_Size "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return the length of the list object in _list_; this is equivalent to `len(list)` on a list object.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyList\_GET\_SIZE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_GET_SIZE "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Similar to [`PyList_Size()`](https://docs.python.org/3/c-api/list.html#c.PyList_Size "PyList_Size")
, but without error checking.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyList\_GetItemRef([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_GetItemRef "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return the object at position _index_ in the list pointed to by _list_. The position must be non-negative; indexing from the end of the list is not supported. If _index_ is out of bounds (`<0 or >=len(list)`), return `NULL` and set an [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 exception.

Added in version 3.13.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyList\_GetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Like [`PyList_GetItemRef()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItemRef "PyList_GetItemRef")
, but returns a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 instead of a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, the returned [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 may become invalid if another thread modifies the list concurrently. Prefer [`PyList_GetItemRef()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItemRef "PyList_GetItemRef")
, which returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyList\_GET\_ITEM([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_GET_ITEM "Link to this definition")
  

_Return value: Borrowed reference._ _Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Similar to [`PyList_GetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem "PyList_GetItem")
, but without error checking.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, the returned [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 may become invalid if another thread modifies the list concurrently. Prefer [`PyList_GetItemRef()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItemRef "PyList_GetItemRef")
, which returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
.

int PyList\_SetItem([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*item)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_SetItem "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Set the item at index _index_ in list to _item_. Return `0` on success. If _index_ is out of bounds, return `-1` and set an [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 exception.

Note

This function “[steals](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _item_, even on error. On success, it discards a reference to an item already in the list at the affected position (unless it was `NULL`).

void PyList\_SET\_ITEM([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 i, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_SET_ITEM "Link to this definition")
  

_Thread safety: [Safe to call from multiple threads with external synchronization only](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-compatible)
._

Macro form of [`PyList_SetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_SetItem "PyList_SetItem")
 without error checking. This is normally only used to fill in new lists where there is no previous content.

Bounds checking is performed as an assertion if Python is built in [debug mode](https://docs.python.org/3/using/configure.html#debug-build)
 or [`with assertions`](https://docs.python.org/3/using/configure.html#cmdoption-with-assertions)
.

Note

This macro “[steals](https://docs.python.org/3/glossary.html#term-steal)
” a reference to _item_, and, unlike [`PyList_SetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_SetItem "PyList_SetItem")
, does _not_ discard a reference to any item that is being replaced; any reference in _list_ at position _i_ will be leaked.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, this macro has no internal synchronization. It is normally only used to fill in new lists where no other thread has a reference to the list. If the list may be shared, use [`PyList_SetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_SetItem "PyList_SetItem")
 instead, which uses a [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock)
.

int PyList\_Insert([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*item)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_Insert "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Insert the item _item_ into list _list_ in front of index _index_. Return `0` if successful; return `-1` and set an exception if unsuccessful. Analogous to `list.insert(index, item)`.

int PyList\_Append([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*item)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_Append "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Append the object _item_ at the end of list _list_. Return `0` if successful; return `-1` and set an exception if unsuccessful. Analogous to `list.append(item)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyList\_GetSlice([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 low, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 high)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_GetSlice "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a list of the objects in _list_ containing the objects _between_ _low_ and _high_. Return `NULL` and set an exception if unsuccessful. Analogous to `list[low:high]`. Indexing from the end of the list is not supported.

int PyList\_SetSlice([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 low, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 high, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*itemlist)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_SetSlice "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Set the slice of _list_ between _low_ and _high_ to the contents of _itemlist_. Analogous to `list[low:high] = itemlist`. The _itemlist_ may be `NULL`, indicating the assignment of an empty list (slice deletion). Return `0` on success, `-1` on failure. Indexing from the end of the list is not supported.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, when _itemlist_ is a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
, both _list_ and _itemlist_ are locked for the duration of the operation. For other iterables (or `NULL`), only _list_ is locked.

int PyList\_Extend([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*iterable)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_Extend "Link to this definition")
  

_Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Extend _list_ with the contents of _iterable_. This is the same as `PyList_SetSlice(list, PY_SSIZE_T_MAX, PY_SSIZE_T_MAX, iterable)` and analogous to `list.extend(iterable)` or `list += iterable`.

Raise an exception and return `-1` if _list_ is not a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 object. Return 0 on success.

Added in version 3.13.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, when _iterable_ is a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
, [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
, [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
, or dict view, both _list_ and _iterable_ (or its underlying dict) are locked for the duration of the operation. For other iterables, only _list_ is locked; _iterable_ may be concurrently modified by another thread.

int PyList\_Clear([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_Clear "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Remove all items from _list_. This is the same as `PyList_SetSlice(list, 0, PY_SSIZE_T_MAX, NULL)` and analogous to `list.clear()` or `del list[:]`.

Raise an exception and return `-1` if _list_ is not a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 object. Return 0 on success.

Added in version 3.13.

int PyList\_Sort([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_Sort "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Sort the items of _list_ in place. Return `0` on success, `-1` on failure. This is equivalent to `list.sort()`.

Note

In the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, element comparison via [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__")
 can execute arbitrary Python code, during which the [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock)
 may be temporarily released. For built-in types ([`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
), the lock is not released during comparison.

int PyList\_Reverse([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_Reverse "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Safe for concurrent use on the same object](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-shared)
._

Reverse the items of _list_ in place. Return `0` on success, `-1` on failure. This is the equivalent of `list.reverse()`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyList\_AsTuple([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*list)[¶](https://docs.python.org/3/c-api/list.html#c.PyList_AsTuple "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._ _Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Return a new tuple object containing the contents of _list_; equivalent to `tuple(list)`.

#### Previous topic

[Tuple Objects](https://docs.python.org/3/c-api/tuple.html "previous chapter")

#### Next topic

[Dictionary objects](https://docs.python.org/3/c-api/dict.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=List+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Flist.html&pagesource=c-api%2Flist.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/list.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/dict.html "Dictionary objects")
     |
*   [previous](https://docs.python.org/3/c-api/tuple.html "Tuple Objects")
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
*   [List Objects](https://docs.python.org/3/c-api/list.html)
    
*    
    
    |
*   Theme Auto Light Dark |