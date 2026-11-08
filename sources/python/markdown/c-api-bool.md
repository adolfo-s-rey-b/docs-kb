### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/float.html "Floating-Point Objects")
     |
*   [previous](https://docs.python.org/3/c-api/long.html "Integer Objects")
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
*   [Boolean Objects](https://docs.python.org/3/c-api/bool.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Boolean Objects[¶](https://docs.python.org/3/c-api/bool.html#boolean-objects "Link to this heading")

=====================================================================================================

Booleans in Python are implemented as a subclass of integers. There are only two booleans, [`Py_False`](https://docs.python.org/3/c-api/bool.html#c.Py_False "Py_False")
 and [`Py_True`](https://docs.python.org/3/c-api/bool.html#c.Py_True "Py_True")
. As such, the normal creation and deletion functions don’t apply to booleans. The following macros are available, however.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyBool\_Type[¶](https://docs.python.org/3/c-api/bool.html#c.PyBool_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python boolean type; it is the same object as [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 in the Python layer.

int PyBool\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/bool.html#c.PyBool_Check "Link to this definition")
  

Return true if _o_ is of type [`PyBool_Type`](https://docs.python.org/3/c-api/bool.html#c.PyBool_Type "PyBool_Type")
. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_False[¶](https://docs.python.org/3/c-api/bool.html#c.Py_False "Link to this definition")
  

The Python `False` object. This object is [immortal](https://docs.python.org/3/glossary.html#term-immortal)
.

Changed in version 3.12: [`Py_False`](https://docs.python.org/3/c-api/bool.html#c.Py_False "Py_False")
 is [immortal](https://docs.python.org/3/glossary.html#term-immortal)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_True[¶](https://docs.python.org/3/c-api/bool.html#c.Py_True "Link to this definition")
  

The Python `True` object. This object is [immortal](https://docs.python.org/3/glossary.html#term-immortal)
.

Changed in version 3.12: [`Py_True`](https://docs.python.org/3/c-api/bool.html#c.Py_True "Py_True")
 is [immortal](https://docs.python.org/3/glossary.html#term-immortal)
.

Py\_RETURN\_FALSE[¶](https://docs.python.org/3/c-api/bool.html#c.Py_RETURN_FALSE "Link to this definition")
  

Return [`Py_False`](https://docs.python.org/3/c-api/bool.html#c.Py_False "Py_False")
 from a function.

Py\_RETURN\_TRUE[¶](https://docs.python.org/3/c-api/bool.html#c.Py_RETURN_TRUE "Link to this definition")
  

Return [`Py_True`](https://docs.python.org/3/c-api/bool.html#c.Py_True "Py_True")
 from a function.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyBool\_FromLong(long v)[¶](https://docs.python.org/3/c-api/bool.html#c.PyBool_FromLong "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return [`Py_True`](https://docs.python.org/3/c-api/bool.html#c.Py_True "Py_True")
 or [`Py_False`](https://docs.python.org/3/c-api/bool.html#c.Py_False "Py_False")
, depending on the truth value of _v_.

#### Previous topic

[Integer Objects](https://docs.python.org/3/c-api/long.html "previous chapter")

#### Next topic

[Floating-Point Objects](https://docs.python.org/3/c-api/float.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Boolean+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fbool.html&pagesource=c-api%2Fbool.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/bool.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/float.html "Floating-Point Objects")
     |
*   [previous](https://docs.python.org/3/c-api/long.html "Integer Objects")
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
*   [Boolean Objects](https://docs.python.org/3/c-api/bool.html)
    
*    
    
    |
*   Theme Auto Light Dark |