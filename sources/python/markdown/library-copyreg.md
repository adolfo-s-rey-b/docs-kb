### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/shelve.html "shelve — Python object persistence")
     |
*   [previous](https://docs.python.org/3/library/pickle.html "pickle — Python object serialization")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Data Persistence](https://docs.python.org/3/library/persistence.html)
     »
*   [`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`copyreg` — Register `pickle` support functions[¶](https://docs.python.org/3/library/copyreg.html#module-copyreg "Link to this heading")

=========================================================================================================================================

**Source code:** [Lib/copyreg.py](https://github.com/python/cpython/tree/3.15/Lib/copyreg.py)

* * *

The `copyreg` module offers a way to define functions used while pickling specific objects. The [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
 and [`copy`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.")
 modules use those functions when pickling/copying those objects. The module provides configuration information about object constructors which are not classes. Such constructors may be factory functions or class instances.

copyreg.constructor(_object_)[¶](https://docs.python.org/3/library/copyreg.html#copyreg.constructor "Link to this definition")

Declares _object_ to be a valid constructor. If _object_ is not callable (and hence not valid as a constructor), raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

copyreg.pickle(_type_, _function_, _constructor\_ob\=None_)[¶](https://docs.python.org/3/library/copyreg.html#copyreg.pickle "Link to this definition")

Declares that _function_ should be used as a “reduction” function for objects of type _type_. _function_ must return either a string or a tuple containing between two and six elements. See the [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table")
 for more details on the interface of _function_.

The _constructor\_ob_ parameter is a legacy feature and is now ignored, but if passed it must be a callable.

Note that the [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table")
 attribute of a pickler object or subclass of [`pickle.Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler")
 can also be used for declaring reduction functions.

Example[¶](https://docs.python.org/3/library/copyreg.html#example "Link to this heading")

------------------------------------------------------------------------------------------

The example below would like to show how to register a pickle function and how it will be used:

Copy

\>>> import copyreg, copy, pickle
\>>> class C:
...     def \_\_init\_\_(self, a):
...         self.a \= a
...
\>>> def pickle\_c(c):
...     print("pickling a C instance...")
...     return C, (c.a,)
...
\>>> copyreg.pickle(C, pickle\_c)
\>>> c \= C(1)
\>>> d \= copy.copy(c)
pickling a C instance...
\>>> p \= pickle.dumps(c)
pickling a C instance...

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html#)
    *   [Example](https://docs.python.org/3/library/copyreg.html#example)
        

#### Previous topic

[`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html "previous chapter")

#### Next topic

[`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=copyreg+%E2%80%94+Register+pickle+support+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcopyreg.html&pagesource=library%2Fcopyreg.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/copyreg.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/shelve.html "shelve — Python object persistence")
     |
*   [previous](https://docs.python.org/3/library/pickle.html "pickle — Python object serialization")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Data Persistence](https://docs.python.org/3/library/persistence.html)
     »
*   [`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html)
    
*    
    
    |
*   Theme Auto Light Dark |