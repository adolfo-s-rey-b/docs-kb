### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/frame.html "Frame objects")
     |
*   [previous](https://docs.python.org/3/c-api/capsule.html "Capsules")
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
*   [Sentinel objects](https://docs.python.org/3/c-api/sentinel.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Sentinel objects[¶](https://docs.python.org/3/c-api/sentinel.html#sentinel-objects "Link to this heading")

===========================================================================================================

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PySentinel\_Type[¶](https://docs.python.org/3/c-api/sentinel.html#c.PySentinel_Type "Link to this definition")
  

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python [`sentinel`](https://docs.python.org/3/builtins/functions.html#sentinel "sentinel")
 type. This is the same object as `sentinel`.

Added in version 3.15.

int PySentinel\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/sentinel.html#c.PySentinel_Check "Link to this definition")
  

Return true if _o_ is a [`sentinel`](https://docs.python.org/3/builtins/functions.html#sentinel "sentinel")
 object or a subtype. The `sentinel` type does not currently allow subclasses, so this check is exact. Future Python versions may choose to allow subtyping. This function always succeeds.

Added in version 3.15.

int PySentinel\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/sentinel.html#c.PySentinel_CheckExact "Link to this definition")
  

Return true if _o_ is a [`sentinel`](https://docs.python.org/3/builtins/functions.html#sentinel "sentinel")
 object, but not a subtype. The `sentinel` type does not currently allow subclasses. Future Python versions may choose to allow subtyping. This function always succeeds.

Added in version 3.15.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PySentinel\_New(const char \*name, const char \*module\_name, const char \*repr)[¶](https://docs.python.org/3/c-api/sentinel.html#c.PySentinel_New "Link to this definition")
  

_Return value: New reference._

Return a new [`sentinel`](https://docs.python.org/3/builtins/functions.html#sentinel "sentinel")
 object with [`__name__`](https://docs.python.org/3/builtins/functions.html#sentinel.__name__ "sentinel.__name__")
 set to _name_ and [`__module__`](https://docs.python.org/3/builtins/functions.html#sentinel.__module__ "sentinel.__module__")
 set to _module\_name_. _name_ must not be `NULL`. If _module\_name_ is `NULL`, `__module__` is set to `None`. If _repr_ is `NULL`, `repr()` returns `__name__`. Return `NULL` with an exception set on failure.

For pickling to work, _module\_name_ must be the name of an importable module, and the sentinel must be accessible from that module under a path matching _name_. Pickle treats _name_ as a global variable name in _module\_name_ (see [`object.__reduce__()`](https://docs.python.org/3/library/pickle.html#object.__reduce__ "object.__reduce__")
).

Added in version 3.15.

#### Previous topic

[Capsules](https://docs.python.org/3/c-api/capsule.html "previous chapter")

#### Next topic

[Frame objects](https://docs.python.org/3/c-api/frame.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Sentinel+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fsentinel.html&pagesource=c-api%2Fsentinel.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/sentinel.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/frame.html "Frame objects")
     |
*   [previous](https://docs.python.org/3/c-api/capsule.html "Capsules")
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
*   [Sentinel objects](https://docs.python.org/3/c-api/sentinel.html)
    
*    
    
    |
*   Theme Auto Light Dark |