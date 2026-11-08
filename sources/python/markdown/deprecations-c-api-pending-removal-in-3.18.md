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
*   [Pending removal in Python 3.18](https://docs.python.org/3/deprecations/c-api-pending-removal-in-3.18.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pending removal in Python 3.18[¶](https://docs.python.org/3/deprecations/c-api-pending-removal-in-3.18.html#pending-removal-in-python-3-18 "Link to this heading")

===================================================================================================================================================================

*   The following private functions are deprecated and planned for removal in Python 3.18:
    
    *   `_PyBytes_Join()`: use [`PyBytes_Join()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Join "PyBytes_Join")
        .
        
    *   `_PyDict_GetItemStringWithError()`: use [`PyDict_GetItemStringRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemStringRef "PyDict_GetItemStringRef")
        .
        
    *   `_PyDict_Pop()`: use [`PyDict_Pop()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Pop "PyDict_Pop")
        .
        
    *   `_PyLong_Sign()`: use [`PyLong_GetSign()`](https://docs.python.org/3/c-api/long.html#c.PyLong_GetSign "PyLong_GetSign")
        .
        
    *   `_PyLong_FromDigits()` and `_PyLong_New()`: use [`PyLongWriter_Create()`](https://docs.python.org/3/c-api/long.html#c.PyLongWriter_Create "PyLongWriter_Create")
        .
        
    *   `_PyThreadState_UncheckedGet()`: use [`PyThreadState_GetUnchecked()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetUnchecked "PyThreadState_GetUnchecked")
        .
        
    *   `_PyUnicode_AsString()`: use [`PyUnicode_AsUTF8()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8 "PyUnicode_AsUTF8")
        .
        
    *   `_PyUnicodeWriter_Init()`: replace `_PyUnicodeWriter_Init(&writer)` with [`writer = PyUnicodeWriter_Create(0)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Create "PyUnicodeWriter_Create")
        .
        
    *   `_PyUnicodeWriter_Finish()`: replace `_PyUnicodeWriter_Finish(&writer)` with [`PyUnicodeWriter_Finish(writer)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Finish "PyUnicodeWriter_Finish")
        .
        
    *   `_PyUnicodeWriter_Dealloc()`: replace `_PyUnicodeWriter_Dealloc(&writer)` with [`PyUnicodeWriter_Discard(writer)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_Discard "PyUnicodeWriter_Discard")
        .
        
    *   `_PyUnicodeWriter_WriteChar()`: replace `_PyUnicodeWriter_WriteChar(&writer, ch)` with [`PyUnicodeWriter_WriteChar(writer, ch)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteChar "PyUnicodeWriter_WriteChar")
        .
        
    *   `_PyUnicodeWriter_WriteStr()`: replace `_PyUnicodeWriter_WriteStr(&writer, str)` with [`PyUnicodeWriter_WriteStr(writer, str)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteStr "PyUnicodeWriter_WriteStr")
        .
        
    *   `_PyUnicodeWriter_WriteSubstring()`: replace `_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)` with [`PyUnicodeWriter_WriteSubstring(writer, str, start, end)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteSubstring "PyUnicodeWriter_WriteSubstring")
        .
        
    *   `_PyUnicodeWriter_WriteASCIIString()`: replace `_PyUnicodeWriter_WriteASCIIString(&writer, str, size)` with [`PyUnicodeWriter_WriteASCII(writer, str, size)`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteASCII "PyUnicodeWriter_WriteASCII")
        .
        
    *   `_PyUnicodeWriter_WriteLatin1String()`: replace `_PyUnicodeWriter_WriteLatin1String(&writer, str, size)` by decoding the string with [`PyUnicode_DecodeLatin1()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DecodeLatin1 "PyUnicode_DecodeLatin1")
        , writing the result with [`PyUnicodeWriter_WriteStr()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeWriter_WriteStr "PyUnicodeWriter_WriteStr")
        , and releasing the result with [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
        .
        
    *   `_PyUnicodeWriter_Prepare()`: (no replacement).
        
    *   `_PyUnicodeWriter_PrepareKind()`: (no replacement).
        
    *   `_Py_HashPointer()`: use [`Py_HashPointer()`](https://docs.python.org/3/c-api/hash.html#c.Py_HashPointer "Py_HashPointer")
        .
        
    *   `_Py_fopen_obj()`: use [`Py_fopen()`](https://docs.python.org/3/c-api/sys.html#c.Py_fopen "Py_fopen")
        .
        
    
    The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat/)
     can be used to get these new public functions on Python 3.13 and older. (Contributed by Victor Stinner in [gh-128863](https://github.com/python/cpython/issues/128863)
    .)
    

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pending+removal+in+Python+3.18&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fc-api-pending-removal-in-3.18.html&pagesource=deprecations%2Fc-api-pending-removal-in-3.18.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/c-api-pending-removal-in-3.18.rst?plain=1)
    

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
*   [Pending removal in Python 3.18](https://docs.python.org/3/deprecations/c-api-pending-removal-in-3.18.html)
    
*    
    
    |
*   Theme Auto Light Dark |