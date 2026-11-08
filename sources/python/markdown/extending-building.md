### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/windows.html "Building C and C++ Extensions on Windows")
     |
*   [previous](https://docs.python.org/3/extending/newtypes.html "Defining Extension Types: Assorted Topics")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)
     »
*   [Building C and C++ Extensions](https://docs.python.org/3/extending/building.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Building C and C++ Extensions[¶](https://docs.python.org/3/extending/building.html#building-c-and-c-extensions "Link to this heading")

=======================================================================================================================================

A C extension for CPython is a shared library (for example, a `.so` file on Linux, `.pyd` on Windows), which exports an _initialization function_.

See [Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html#extension-modules)
 for details.

Building C and C++ Extensions with setuptools[¶](https://docs.python.org/3/extending/building.html#building-c-and-c-extensions-with-setuptools "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Building, packaging and distributing extension modules is best done with third-party tools, and is out of scope of this document. One suitable tool is Setuptools, whose documentation can be found at [https://setuptools.pypa.io/en/latest/setuptools.html](https://setuptools.pypa.io/en/latest/setuptools.html)
.

The [`distutils`](https://docs.python.org/3/library/distutils.html#module-distutils "distutils: Removed in 3.12. (deprecated)")
 module, which was included in the standard library until Python 3.12, is now maintained as part of Setuptools.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Building C and C++ Extensions](https://docs.python.org/3/extending/building.html#)
    *   [Building C and C++ Extensions with setuptools](https://docs.python.org/3/extending/building.html#building-c-and-c-extensions-with-setuptools)
        

#### Previous topic

[Defining Extension Types: Assorted Topics](https://docs.python.org/3/extending/newtypes.html "previous chapter")

#### Next topic

[Building C and C++ Extensions on Windows](https://docs.python.org/3/extending/windows.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Building+C+and+C%2B%2B+Extensions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fextending%2Fbuilding.html&pagesource=extending%2Fbuilding.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/extending/building.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/windows.html "Building C and C++ Extensions on Windows")
     |
*   [previous](https://docs.python.org/3/extending/newtypes.html "Defining Extension Types: Assorted Topics")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)
     »
*   [Building C and C++ Extensions](https://docs.python.org/3/extending/building.html)
    
*    
    
    |
*   Theme Auto Light Dark |