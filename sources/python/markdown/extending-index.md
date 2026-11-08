### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/first-extension-module.html "Your first C API extension module")
     |
*   [previous](https://docs.python.org/3/library/security_warnings.html "Security Considerations")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Extending and Embedding the Python Interpreter[¶](https://docs.python.org/3/extending/index.html#extending-and-embedding-the-python-interpreter "Link to this heading")

========================================================================================================================================================================

This document describes how to write modules in C or C++ to extend the Python interpreter with new modules. Those modules can do what Python code does – define functions, object types and methods – but also interact with native libraries or achieve better performance by avoiding the overhead of an interpreter. The document also describes how to embed the Python interpreter in another application, for use as an extension language. Finally, it shows how to compile and link extension modules so that they can be loaded dynamically (at run time) into the interpreter, if the underlying operating system supports this feature.

This document assumes basic knowledge about C and Python. For an informal introduction to Python, see [The Python Tutorial](https://docs.python.org/3/tutorial/index.html#tutorial-index)
. [The Python Language Reference](https://docs.python.org/3/reference/index.html#reference-index)
 gives a more formal definition of the language. [Python built-ins reference](https://docs.python.org/3/builtins/index.html#builtins-index)
 documents the built-in functions and object types, and [The Python standard library](https://docs.python.org/3/library/index.html#library-index)
 documents the modules (both built-in and written in Python) that give the language its wide application range.

For a detailed description of the whole Python/C API, see the separate [Python/C API reference manual](https://docs.python.org/3/c-api/index.html#c-api-index)
.

To support extensions, Python’s C API (Application Programmers Interface) defines a set of functions, macros and variables that provide access to most aspects of the Python run-time system. The Python API is incorporated in a C source file by including the header `"Python.h"`.

Note

The C extension interface is specific to CPython, and extension modules do not work on other Python implementations. In many cases, it is possible to avoid writing C extensions and preserve portability to other implementations. For example, if your use case is calling C library functions or system calls, you should consider using the [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
 module or the [cffi](https://cffi.readthedocs.io/)
 library rather than writing custom C code. These modules let you write Python code to interface with C code and are more portable between implementations of Python than writing and compiling a C extension module.

Recommended third party tools[¶](https://docs.python.org/3/extending/index.html#recommended-third-party-tools "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

This document only covers the basic tools for creating extensions provided as part of this version of CPython. Some [third party tools](https://docs.python.org/3/c-api/intro.html#c-api-tools)
 offer both simpler and more sophisticated approaches to creating C and C++ extensions for Python.

While this document is aimed at extension authors, it should also be helpful to the authors of such tools. For example, the tutorial module can serve as a simple test case for a build tool or sample expected output of a code generator.

C API Tutorial[¶](https://docs.python.org/3/extending/index.html#c-api-tutorial "Link to this heading")

--------------------------------------------------------------------------------------------------------

This tutorial describes how to write a simple module in C or C++, using the Python C API – that is, using the basic tools provided as part of this version of CPython.

1.  [Your first C API extension module](https://docs.python.org/3/extending/first-extension-module.html#first-extension-module)
    

Guides for intermediate topics[¶](https://docs.python.org/3/extending/index.html#guides-for-intermediate-topics "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

This section of the guide covers creating C and C++ extensions without assistance from third party tools. It is intended primarily for creators of those tools, rather than being a recommended way to create your own C extensions.

*   [Using the C API: Assorted topics](https://docs.python.org/3/extending/extending.html#extending-intro)
    
*   [Defining Extension Types: Tutorial](https://docs.python.org/3/extending/newtypes_tutorial.html#defining-new-types)
    
*   [Defining Extension Types: Assorted Topics](https://docs.python.org/3/extending/newtypes.html#new-types-topics)
    
*   [Building C and C++ Extensions](https://docs.python.org/3/extending/building.html#building)
    
*   [Building C and C++ Extensions on Windows](https://docs.python.org/3/extending/windows.html#building-on-windows)
    

Embedding the CPython runtime in a larger application[¶](https://docs.python.org/3/extending/index.html#embedding-the-cpython-runtime-in-a-larger-application "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes, rather than creating an extension that runs inside the Python interpreter as the main application, it is desirable to instead embed the CPython runtime inside a larger application. This section covers some of the details involved in doing that successfully.

*   [Embedding Python in Another Application](https://docs.python.org/3/extending/embedding.html#embedding)
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html#)
    *   [Recommended third party tools](https://docs.python.org/3/extending/index.html#recommended-third-party-tools)
        
    *   [C API Tutorial](https://docs.python.org/3/extending/index.html#c-api-tutorial)
        
    *   [Guides for intermediate topics](https://docs.python.org/3/extending/index.html#guides-for-intermediate-topics)
        
    *   [Embedding the CPython runtime in a larger application](https://docs.python.org/3/extending/index.html#embedding-the-cpython-runtime-in-a-larger-application)
        

#### Previous topic

[Security Considerations](https://docs.python.org/3/library/security_warnings.html "previous chapter")

#### Next topic

[Your first C API extension module](https://docs.python.org/3/extending/first-extension-module.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Extending+and+Embedding+the+Python+Interpreter&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fextending%2Findex.html&pagesource=extending%2Findex.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/extending/index.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/first-extension-module.html "Your first C API extension module")
     |
*   [previous](https://docs.python.org/3/library/security_warnings.html "Security Considerations")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)
    
*    
    
    |
*   Theme Auto Light Dark |