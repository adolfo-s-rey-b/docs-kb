### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/coro.html "Coroutine Objects")
     |
*   [previous](https://docs.python.org/3/c-api/frame.html "Frame objects")
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
*   [Generator Objects](https://docs.python.org/3/c-api/gen.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Generator Objects[¶](https://docs.python.org/3/c-api/gen.html#generator-objects "Link to this heading")

========================================================================================================

Generator objects are what Python uses to implement generator iterators. They are normally created by calling a generator function, rather than explicitly calling [`PyGen_New()`](https://docs.python.org/3/c-api/gen.html#c.PyGen_New "PyGen_New")
 or [`PyGen_NewWithQualName()`](https://docs.python.org/3/c-api/gen.html#c.PyGen_NewWithQualName "PyGen_NewWithQualName")
.

type PyGenObject[¶](https://docs.python.org/3/c-api/gen.html#c.PyGenObject "Link to this definition")
  

The C structure used for generator objects.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyGen\_Type[¶](https://docs.python.org/3/c-api/gen.html#c.PyGen_Type "Link to this definition")
  

The type object corresponding to generator objects.

int PyGen\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/gen.html#c.PyGen_Check "Link to this definition")
  

Return true if _ob_ is a generator object; _ob_ must not be `NULL`. This function always succeeds.

int PyGen\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/gen.html#c.PyGen_CheckExact "Link to this definition")
  

Return true if _ob_’s type is [`PyGen_Type`](https://docs.python.org/3/c-api/gen.html#c.PyGen_Type "PyGen_Type")
; _ob_ must not be `NULL`. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyGen\_New([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame)[¶](https://docs.python.org/3/c-api/gen.html#c.PyGen_New "Link to this definition")
  

_Return value: New reference._

Create and return a new generator object based on the _frame_ object. A reference to _frame_ is “[stolen](https://docs.python.org/3/glossary.html#term-steal)
” by this function (even on error). The argument must not be `NULL`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyGen\_NewWithQualName([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*qualname)[¶](https://docs.python.org/3/c-api/gen.html#c.PyGen_NewWithQualName "Link to this definition")
  

_Return value: New reference._

Create and return a new generator object based on the _frame_ object, with `__name__` and `__qualname__` set to _name_ and _qualname_. A reference to _frame_ is “[stolen](https://docs.python.org/3/glossary.html#term-steal)
” by this function (even on error). The _frame_ argument must not be `NULL`.

[PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*PyGen\_GetCode([PyGenObject](https://docs.python.org/3/c-api/gen.html#c.PyGenObject "PyGenObject")
 \*gen)[¶](https://docs.python.org/3/c-api/gen.html#c.PyGen_GetCode "Link to this definition")
  

Return a new [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the code object wrapped by _gen_. This function always succeeds.

Asynchronous Generator Objects[¶](https://docs.python.org/3/c-api/gen.html#asynchronous-generator-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

See also

[**PEP 525**](https://peps.python.org/pep-0525/)

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyAsyncGen\_Type[¶](https://docs.python.org/3/c-api/gen.html#c.PyAsyncGen_Type "Link to this definition")
  

The type object corresponding to asynchronous generator objects. This is available as [`types.AsyncGeneratorType`](https://docs.python.org/3/library/types.html#types.AsyncGeneratorType "types.AsyncGeneratorType")
 in the Python layer.

Added in version 3.6.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyAsyncGen\_New([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*qualname)[¶](https://docs.python.org/3/c-api/gen.html#c.PyAsyncGen_New "Link to this definition")
  

Create a new asynchronous generator wrapping _frame_, with `__name__` and `__qualname__` set to _name_ and _qualname_. _frame_ is “[stolen](https://docs.python.org/3/glossary.html#term-steal)
” by this function (even on error) and must not be `NULL`.

On success, this function returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the new asynchronous generator. On failure, this function returns `NULL` with an exception set.

Added in version 3.6.

int PyAsyncGen\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/gen.html#c.PyAsyncGen_CheckExact "Link to this definition")
  

Return true if _op_ is an asynchronous generator object, false otherwise. This function always succeeds.

Added in version 3.6.

Deprecated API[¶](https://docs.python.org/3/c-api/gen.html#deprecated-api "Link to this heading")

--------------------------------------------------------------------------------------------------

PyAsyncGenASend\_CheckExact(op)[¶](https://docs.python.org/3/c-api/gen.html#c.PyAsyncGenASend_CheckExact "Link to this definition")
  

This is an API that was included in Python’s C API by mistake.

It is solely here for completeness; do not use this API.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.14.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Generator Objects](https://docs.python.org/3/c-api/gen.html#)
    *   [Asynchronous Generator Objects](https://docs.python.org/3/c-api/gen.html#asynchronous-generator-objects)
        
    *   [Deprecated API](https://docs.python.org/3/c-api/gen.html#deprecated-api)
        

#### Previous topic

[Frame objects](https://docs.python.org/3/c-api/frame.html "previous chapter")

#### Next topic

[Coroutine Objects](https://docs.python.org/3/c-api/coro.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Generator+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fgen.html&pagesource=c-api%2Fgen.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/gen.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/coro.html "Coroutine Objects")
     |
*   [previous](https://docs.python.org/3/c-api/frame.html "Frame objects")
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
*   [Generator Objects](https://docs.python.org/3/c-api/gen.html)
    
*    
    
    |
*   Theme Auto Light Dark |