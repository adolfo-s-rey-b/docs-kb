### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Pending removal in Python 3.20](https://docs.python.org/3/deprecations/c-api-pending-removal-in-3.20.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pending removal in Python 3.20[¶](https://docs.python.org/3/deprecations/c-api-pending-removal-in-3.20.html#pending-removal-in-python-3-20 "Link to this heading")

===================================================================================================================================================================

*   `_PyObject_CallMethodId()`, `_PyObject_GetAttrId()` and `_PyUnicode_FromId()` are deprecated since 3.15 and will be removed in 3.20. Instead, use [`PyUnicode_InternFromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternFromString "PyUnicode_InternFromString")
     and cache the result in the module state, then call [`PyObject_CallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethod "PyObject_CallMethod")
     or [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
    . (Contributed by Victor Stinner in [gh-141049](https://github.com/python/cpython/issues/141049)
    .)
    
*   The `cval` field in [`PyComplexObject`](https://docs.python.org/3/c-api/complex.html#c.PyComplexObject "PyComplexObject")
     ([gh-128813](https://github.com/python/cpython/issues/128813)
    ). Use [`PyComplex_AsCComplex()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_AsCComplex "PyComplex_AsCComplex")
     and [`PyComplex_FromCComplex()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_FromCComplex "PyComplex_FromCComplex")
     to convert a Python complex number to/from the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")
     representation.
    
*   Macros `Py_MATH_PIl` and `Py_MATH_El`.
    

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pending+removal+in+Python+3.20&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fc-api-pending-removal-in-3.20.html&pagesource=deprecations%2Fc-api-pending-removal-in-3.20.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/c-api-pending-removal-in-3.20.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Pending removal in Python 3.20](https://docs.python.org/3/deprecations/c-api-pending-removal-in-3.20.html)
    
*    
    
    |
*   Theme Auto Light Dark |