### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/curses.html "Curses C API")
     |
*   [previous](https://docs.python.org/3/c-api/contextvars.html "Context Variables Objects")
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
*   [Objects for Type Hinting](https://docs.python.org/3/c-api/typehints.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Objects for Type Hinting[¶](https://docs.python.org/3/c-api/typehints.html#objects-for-type-hinting "Link to this heading")

============================================================================================================================

Various built-in types for type hinting are provided. Currently, two types exist – [GenericAlias](https://docs.python.org/3/builtins/stdtypes.html#types-genericalias)
 and [Union](https://docs.python.org/3/builtins/stdtypes.html#types-union)
. Only `GenericAlias` is exposed to C.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_GenericAlias([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*origin, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args)[¶](https://docs.python.org/3/c-api/typehints.html#c.Py_GenericAlias "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.9._

Create a [GenericAlias](https://docs.python.org/3/builtins/stdtypes.html#types-genericalias)
 object. Equivalent to calling the Python class [`types.GenericAlias`](https://docs.python.org/3/library/types.html#types.GenericAlias "types.GenericAlias")
. The _origin_ and _args_ arguments set the `GenericAlias`‘s `__origin__` and `__args__` attributes respectively. _origin_ should be a [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
\*, and _args_ can be a [PyTupleObject](https://docs.python.org/3/c-api/tuple.html#c.PyTupleObject "PyTupleObject")
\* or any `PyObject*`. If _args_ passed is not a tuple, a 1-tuple is automatically constructed and `__args__` is set to `(args,)`. Minimal checking is done for the arguments, so the function will succeed even if _origin_ is not a type. The `GenericAlias`‘s `__parameters__` attribute is constructed lazily from `__args__`. On failure, an exception is raised and `NULL` is returned.

Here’s an example of how to make an extension type generic:

...
static PyMethodDef my\_obj\_methods\[\] \= {
    // Other methods.
    ...
    {"\_\_class\_getitem\_\_", Py\_GenericAlias, METH\_O|METH\_CLASS, "my\_obj is generic over its contained type"}
    ...
}

See also

The data model method [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__")
.

Added in version 3.9.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 Py\_GenericAliasType[¶](https://docs.python.org/3/c-api/typehints.html#c.Py_GenericAliasType "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.9._

The C type of the object returned by [`Py_GenericAlias()`](https://docs.python.org/3/c-api/typehints.html#c.Py_GenericAlias "Py_GenericAlias")
. Equivalent to [`types.GenericAlias`](https://docs.python.org/3/library/types.html#types.GenericAlias "types.GenericAlias")
 in Python.

Added in version 3.9.

#### Previous topic

[Context Variables Objects](https://docs.python.org/3/c-api/contextvars.html "previous chapter")

#### Next topic

[Curses C API](https://docs.python.org/3/c-api/curses.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Objects+for+Type+Hinting&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Ftypehints.html&pagesource=c-api%2Ftypehints.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/typehints.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/curses.html "Curses C API")
     |
*   [previous](https://docs.python.org/3/c-api/contextvars.html "Context Variables Objects")
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
*   [Objects for Type Hinting](https://docs.python.org/3/c-api/typehints.html)
    
*    
    
    |
*   Theme Auto Light Dark |