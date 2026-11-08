### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/long.html "Integer Objects")
     |
*   [previous](https://docs.python.org/3/c-api/type.html "Type Objects")
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
*   [The `None` Object](https://docs.python.org/3/c-api/none.html)
    
*    
    
    |
*   Theme Auto Light Dark |

The `None` Object[¶](https://docs.python.org/3/c-api/none.html#the-none-object "Link to this heading")

=======================================================================================================

Note that the [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 for `None` is not directly exposed in the Python/C API. Since `None` is a singleton, testing for object identity (using `==` in C) is sufficient. There is no `PyNone_Check()` function for the same reason.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_None[¶](https://docs.python.org/3/c-api/none.html#c.Py_None "Link to this definition")
  

The Python `None` object, denoting lack of value. This object has no methods and is [immortal](https://docs.python.org/3/glossary.html#term-immortal)
.

Changed in version 3.12: [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "Py_None")
 is [immortal](https://docs.python.org/3/glossary.html#term-immortal)
.

Py\_RETURN\_NONE[¶](https://docs.python.org/3/c-api/none.html#c.Py_RETURN_NONE "Link to this definition")
  

Return [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "Py_None")
 from a function.

#### Previous topic

[Type Objects](https://docs.python.org/3/c-api/type.html "previous chapter")

#### Next topic

[Integer Objects](https://docs.python.org/3/c-api/long.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=The+None+Object&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fnone.html&pagesource=c-api%2Fnone.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/none.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/long.html "Integer Objects")
     |
*   [previous](https://docs.python.org/3/c-api/type.html "Type Objects")
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
*   [The `None` Object](https://docs.python.org/3/c-api/none.html)
    
*    
    
    |
*   Theme Auto Light Dark |