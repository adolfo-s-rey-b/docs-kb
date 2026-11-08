### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/descriptor.html "Descriptor Objects")
     |
*   [previous](https://docs.python.org/3/c-api/module.html "Module Objects")
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
*   [Iterator Objects](https://docs.python.org/3/c-api/iterator.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Iterator Objects[¶](https://docs.python.org/3/c-api/iterator.html#iterator-objects "Link to this heading")

===========================================================================================================

Python provides two general-purpose iterator objects. The first, a sequence iterator, works with an arbitrary sequence supporting the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__")
 method. The second works with a callable object and a sentinel value, calling the callable for each item in the sequence, and ending the iteration when the sentinel value is returned.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PySeqIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PySeqIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Type object for iterator objects returned by [`PySeqIter_New()`](https://docs.python.org/3/c-api/iterator.html#c.PySeqIter_New "PySeqIter_New")
 and the one-argument form of the [`iter()`](https://docs.python.org/3/builtins/functions.html#iter "iter")
 built-in function for built-in sequence types.

int PySeqIter\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/iterator.html#c.PySeqIter_Check "Link to this definition")
  

Return true if the type of _op_ is [`PySeqIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PySeqIter_Type "PySeqIter_Type")
. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySeqIter\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*seq)[¶](https://docs.python.org/3/c-api/iterator.html#c.PySeqIter_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return an iterator that works with a general sequence object, _seq_. The iteration ends when the sequence raises [`IndexError`](https://docs.python.org/3/builtins/exceptions.html#IndexError "IndexError")
 for the subscripting operation.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyCallIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyCallIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Type object for iterator objects returned by [`PyCallIter_New()`](https://docs.python.org/3/c-api/iterator.html#c.PyCallIter_New "PyCallIter_New")
 and the two-argument form of the [`iter()`](https://docs.python.org/3/builtins/functions.html#iter "iter")
 built-in function.

int PyCallIter\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/iterator.html#c.PyCallIter_Check "Link to this definition")
  

Return true if the type of _op_ is [`PyCallIter_Type`](https://docs.python.org/3/c-api/iterator.html#c.PyCallIter_Type "PyCallIter_Type")
. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCallIter\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*sentinel)[¶](https://docs.python.org/3/c-api/iterator.html#c.PyCallIter_New "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a new iterator. The first parameter, _callable_, can be any Python callable object that can be called with no parameters; each call to it should return the next item in the iteration. When _callable_ returns a value equal to _sentinel_, the iteration will be terminated.

Range Objects[¶](https://docs.python.org/3/c-api/iterator.html#range-objects "Link to this heading")

-----------------------------------------------------------------------------------------------------

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyRange\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyRange_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

The type object for [`range`](https://docs.python.org/3/builtins/stdtypes.html#range "range")
 objects.

int PyRange\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/iterator.html#c.PyRange_Check "Link to this definition")
  

Return true if the object _o_ is an instance of a [`range`](https://docs.python.org/3/builtins/stdtypes.html#range "range")
 object. This function always succeeds.

Builtin Iterator Types[¶](https://docs.python.org/3/c-api/iterator.html#builtin-iterator-types "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

These are built-in iteration types that are included in Python’s C API, but provide no additional functions. They are here for completeness.

These pointers are part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
.

| C type | Python type |
| --- | --- |
| [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")<br> PyEnum\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyEnum_Type "Link to this definition") | [`enumerate`](https://docs.python.org/3/builtins/functions.html#enumerate "enumerate") |
| [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")<br> PyFilter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyFilter_Type "Link to this definition") | [`filter`](https://docs.python.org/3/builtins/functions.html#filter "filter") |
| [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")<br> PyMap\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyMap_Type "Link to this definition") | [`map`](https://docs.python.org/3/builtins/functions.html#map "map") |
| [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")<br> PyReversed\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyReversed_Type "Link to this definition") | [`reversed`](https://docs.python.org/3/builtins/functions.html#reversed "reversed") |
| [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")<br> PyZip\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyZip_Type "Link to this definition") | [`zip`](https://docs.python.org/3/builtins/functions.html#zip "zip") |

Other Iterator Objects[¶](https://docs.python.org/3/c-api/iterator.html#other-iterator-objects "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyByteArrayIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyByteArrayIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyBytesIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyBytesIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyListIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyListIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyListRevIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyListRevIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PySetIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PySetIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyTupleIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyTupleIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyRangeIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyRangeIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyLongRangeIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyLongRangeIter_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDictIterKey\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyDictIterKey_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDictRevIterKey\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyDictRevIterKey_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.8._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDictIterValue\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyDictIterValue_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDictRevIterValue\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyDictRevIterValue_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.8._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDictIterItem\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyDictIterItem_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyDictRevIterItem\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyDictRevIterItem_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.8._

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyODictIter\_Type[¶](https://docs.python.org/3/c-api/iterator.html#c.PyODictIter_Type "Link to this definition")
  

Type objects for iterators of various built-in objects.

Do not create instances of these directly; prefer calling [`PyObject_GetIter()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetIter "PyObject_GetIter")
 instead.

Note that there is no guarantee that a given built-in type uses a given iterator type. For example, iterating over [`range`](https://docs.python.org/3/builtins/stdtypes.html#range "range")
 will use one of two iterator types depending on the size of the range. Other types may start using a similar scheme in the future, without warning.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Iterator Objects](https://docs.python.org/3/c-api/iterator.html#)
    *   [Range Objects](https://docs.python.org/3/c-api/iterator.html#range-objects)
        
    *   [Builtin Iterator Types](https://docs.python.org/3/c-api/iterator.html#builtin-iterator-types)
        
    *   [Other Iterator Objects](https://docs.python.org/3/c-api/iterator.html#other-iterator-objects)
        

#### Previous topic

[Module Objects](https://docs.python.org/3/c-api/module.html "previous chapter")

#### Next topic

[Descriptor Objects](https://docs.python.org/3/c-api/descriptor.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Iterator+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fiterator.html&pagesource=c-api%2Fiterator.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/iterator.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/descriptor.html "Descriptor Objects")
     |
*   [previous](https://docs.python.org/3/c-api/module.html "Module Objects")
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
*   [Iterator Objects](https://docs.python.org/3/c-api/iterator.html)
    
*    
    
    |
*   Theme Auto Light Dark |