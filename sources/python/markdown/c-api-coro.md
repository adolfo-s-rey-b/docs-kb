### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/contextvars.html "Context Variables Objects")
     |
*   [previous](https://docs.python.org/3/c-api/gen.html "Generator Objects")
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
*   [Coroutine Objects](https://docs.python.org/3/c-api/coro.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Coroutine Objects[¶](https://docs.python.org/3/c-api/coro.html#coroutine-objects "Link to this heading")

=========================================================================================================

Added in version 3.5.

Coroutine objects are what functions declared with an `async` keyword return.

type PyCoroObject[¶](https://docs.python.org/3/c-api/coro.html#c.PyCoroObject "Link to this definition")
  

The C structure used for coroutine objects.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyCoro\_Type[¶](https://docs.python.org/3/c-api/coro.html#c.PyCoro_Type "Link to this definition")
  

The type object corresponding to coroutine objects.

int PyCoro\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ob)[¶](https://docs.python.org/3/c-api/coro.html#c.PyCoro_CheckExact "Link to this definition")
  

Return true if _ob_’s type is [`PyCoro_Type`](https://docs.python.org/3/c-api/coro.html#c.PyCoro_Type "PyCoro_Type")
; _ob_ must not be `NULL`. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCoro\_New([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*qualname)[¶](https://docs.python.org/3/c-api/coro.html#c.PyCoro_New "Link to this definition")
  

_Return value: New reference._

Create and return a new coroutine object based on the _frame_ object, with `__name__` and `__qualname__` set to _name_ and _qualname_. A reference to _frame_ is stolen by this function. The _frame_ argument must not be `NULL`.

#### Previous topic

[Generator Objects](https://docs.python.org/3/c-api/gen.html "previous chapter")

#### Next topic

[Context Variables Objects](https://docs.python.org/3/c-api/contextvars.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Coroutine+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fcoro.html&pagesource=c-api%2Fcoro.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/coro.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/contextvars.html "Context Variables Objects")
     |
*   [previous](https://docs.python.org/3/c-api/gen.html "Generator Objects")
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
*   [Coroutine Objects](https://docs.python.org/3/c-api/coro.html)
    
*    
    
    |
*   Theme Auto Light Dark |