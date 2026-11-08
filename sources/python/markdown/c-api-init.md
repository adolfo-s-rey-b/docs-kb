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
*   [Initialization, finalization, and threads](https://docs.python.org/3/c-api/init.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Initialization, finalization, and threads[¶](https://docs.python.org/3/c-api/init.html#initialization-finalization-and-threads "Link to this heading")

=======================================================================================================================================================

This page has been split up into the following:

*   [Interpreter initialization and finalization](https://docs.python.org/3/c-api/interp-lifecycle.html#initialization)
    
*   [Thread states and the global interpreter lock](https://docs.python.org/3/c-api/threads.html#threads)
    
*   [Synchronization primitives](https://docs.python.org/3/c-api/synchronization.html#synchronization)
    
*   [Thread-local storage support](https://docs.python.org/3/c-api/tls.html#thread-local-storage)
    
*   [Multiple interpreters in a Python process](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
    
*   [Profiling and tracing](https://docs.python.org/3/c-api/profiling.html#profiling)
    

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Initialization%2C+finalization%2C+and+threads&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Finit.html&pagesource=c-api%2Finit.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/init.rst?plain=1)
    

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
*   [Initialization, finalization, and threads](https://docs.python.org/3/c-api/init.html)
    
*    
    
    |
*   Theme Auto Light Dark |