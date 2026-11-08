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
*   [Pending removal in future versions](https://docs.python.org/3/deprecations/c-api-pending-removal-in-future.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pending removal in future versions[¶](https://docs.python.org/3/deprecations/c-api-pending-removal-in-future.html#pending-removal-in-future-versions "Link to this heading")

=============================================================================================================================================================================

The following APIs are deprecated and will be removed, although there is currently no date scheduled for their removal.

*   [`Py_TPFLAGS_HAVE_FINALIZE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_FINALIZE "Py_TPFLAGS_HAVE_FINALIZE")
    : Unneeded since Python 3.8.
    
*   [`PyErr_Fetch()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Fetch "PyErr_Fetch")
    : Use [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
     instead.
    
*   [`PyErr_NormalizeException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_NormalizeException "PyErr_NormalizeException")
    : Use [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
     instead.
    
*   [`PyErr_Restore()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Restore "PyErr_Restore")
    : Use [`PyErr_SetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetRaisedException "PyErr_SetRaisedException")
     instead.
    
*   [`PyModule_GetFilename()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilename "PyModule_GetFilename")
    : Use [`PyModule_GetFilenameObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetFilenameObject "PyModule_GetFilenameObject")
     instead.
    
*   [`PyOS_AfterFork()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork "PyOS_AfterFork")
    : Use [`PyOS_AfterFork_Child()`](https://docs.python.org/3/c-api/sys.html#c.PyOS_AfterFork_Child "PyOS_AfterFork_Child")
     instead.
    
*   [`PySlice_GetIndicesEx()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_GetIndicesEx "PySlice_GetIndicesEx")
    : Use [`PySlice_Unpack()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_Unpack "PySlice_Unpack")
     and [`PySlice_AdjustIndices()`](https://docs.python.org/3/c-api/slice.html#c.PySlice_AdjustIndices "PySlice_AdjustIndices")
     instead.
    
*   [`PyUnicode_READY()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READY "PyUnicode_READY")
    : Unneeded since Python 3.12
    
*   `PyErr_Display()`: Use [`PyErr_DisplayException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_DisplayException "PyErr_DisplayException")
     instead.
    
*   `_PyErr_ChainExceptions()`: Use `_PyErr_ChainExceptions1()` instead.
    
*   `PyBytesObject.ob_shash` member: call [`PyObject_Hash()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Hash "PyObject_Hash")
     instead.
    
*   Thread Local Storage (TLS) API:
    
    *   [`PyThread_create_key()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_create_key "PyThread_create_key")
        : Use [`PyThread_tss_alloc()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_alloc "PyThread_tss_alloc")
         instead.
        
    *   [`PyThread_delete_key()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_delete_key "PyThread_delete_key")
        : Use [`PyThread_tss_free()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_free "PyThread_tss_free")
         instead.
        
    *   [`PyThread_set_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_set_key_value "PyThread_set_key_value")
        : Use [`PyThread_tss_set()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_set "PyThread_tss_set")
         instead.
        
    *   [`PyThread_get_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_get_key_value "PyThread_get_key_value")
        : Use [`PyThread_tss_get()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_get "PyThread_tss_get")
         instead.
        
    *   [`PyThread_delete_key_value()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_delete_key_value "PyThread_delete_key_value")
        : Use [`PyThread_tss_delete()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_delete "PyThread_tss_delete")
         instead.
        
    *   [`PyThread_ReInitTLS()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_ReInitTLS "PyThread_ReInitTLS")
        : Unneeded since Python 3.7.
        

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pending+removal+in+future+versions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fdeprecations%2Fc-api-pending-removal-in-future.html&pagesource=deprecations%2Fc-api-pending-removal-in-future.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/deprecations/c-api-pending-removal-in-future.rst?plain=1)
    

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
*   [Pending removal in future versions](https://docs.python.org/3/deprecations/c-api-pending-removal-in-future.html)
    
*    
    
    |
*   Theme Auto Light Dark |