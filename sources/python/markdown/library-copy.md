### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pprint.html "pprint — Data pretty printer")
     |
*   [previous](https://docs.python.org/3/library/types.html "types — Dynamic type creation and names for built-in types")
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
*   [Data Types](https://docs.python.org/3/library/datatypes.html)
     »
*   [`copy` — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`copy` — Shallow and deep copy operations[¶](https://docs.python.org/3/library/copy.html#module-copy "Link to this heading")

=============================================================================================================================

**Source code:** [Lib/copy.py](https://github.com/python/cpython/tree/3.15/Lib/copy.py)

* * *

Assignment statements in Python do not copy objects, they create bindings between a target and an object. For collections that are mutable or contain mutable items, a copy is sometimes needed so one can change one copy without changing the other. This module provides generic shallow and deep copy operations (explained below).

Interface summary:

copy.copy(_obj_)[¶](https://docs.python.org/3/library/copy.html#copy.copy "Link to this definition")

Return a shallow copy of _obj_.

copy.deepcopy(_obj_\[, _memo_\])[¶](https://docs.python.org/3/library/copy.html#copy.deepcopy "Link to this definition")

Return a deep copy of _obj_.

copy.replace(_obj_, _/_, _\*\*changes_)[¶](https://docs.python.org/3/library/copy.html#copy.replace "Link to this definition")

Creates a new object of the same type as _obj_, replacing fields with values from _changes_.

Added in version 3.13.

exception copy.Error[¶](https://docs.python.org/3/library/copy.html#copy.Error "Link to this definition")

Raised for module specific errors.

The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):

*   A _shallow copy_ constructs a new compound object and then (to the extent possible) inserts _references_ into it to the objects found in the original.
    
*   A _deep copy_ constructs a new compound object and then, recursively, inserts _copies_ into it of the objects found in the original.
    

Two problems often exist with deep copy operations that don’t exist with shallow copy operations:

*   Recursive objects (compound objects that, directly or indirectly, contain a reference to themselves) may cause a recursive loop.
    
*   Because deep copy copies everything it may copy too much, such as data which is intended to be shared between copies.
    

The [`deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "copy.deepcopy")
 function avoids these problems by:

*   keeping a `memo` dictionary of objects already copied during the current copying pass; and
    
*   letting user-defined classes override the copying operation or the set of components copied.
    

This module does not copy types like module, method, stack trace, stack frame, file, socket, window, or any similar types. It does “copy” functions and classes (shallow and deeply), by returning the original object unchanged; this is compatible with the way these are treated by the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
 module.

Shallow copies of many collections can be made using the corresponding `copy()` method (such as [`list.copy()`](https://docs.python.org/3/builtins/stdtypes.html#list.copy "list.copy")
, [`dict.copy()`](https://docs.python.org/3/builtins/stdtypes.html#dict.copy "dict.copy")
 or [`set.copy()`](https://docs.python.org/3/builtins/stdtypes.html#set.copy "set.copy")
), and of sequences (such as lists or bytearrays) by making a slice of the entire sequence (`sequence[:]`). However, these methods and slicing can create an instance of the base type when copying an instance of a subclass, whereas [`copy.copy()`](https://docs.python.org/3/library/copy.html#copy.copy "copy.copy")
 normally returns an instance of the same type.

Classes can use the same interfaces to control copying that they use to control pickling. See the description of module [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
 for information on these methods. In fact, the `copy` module uses the registered pickle functions from the [`copyreg`](https://docs.python.org/3/library/copyreg.html#module-copyreg "copyreg: Register pickle support functions.")
 module.

In order for a class to define its own copy implementation, it can define special methods [`__copy__()`](https://docs.python.org/3/library/copy.html#object.__copy__ "object.__copy__")
 and [`__deepcopy__()`](https://docs.python.org/3/library/copy.html#object.__deepcopy__ "object.__deepcopy__")
.

object.\_\_copy\_\_(_self_)[¶](https://docs.python.org/3/library/copy.html#object.__copy__ "Link to this definition")

Called to implement the shallow copy operation; no additional arguments are passed.

object.\_\_deepcopy\_\_(_self_, _memo_)[¶](https://docs.python.org/3/library/copy.html#object.__deepcopy__ "Link to this definition")

Called to implement the deep copy operation; it is passed one argument, the _memo_ dictionary. If the `__deepcopy__` implementation needs to make a deep copy of a component, it should call the [`deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "copy.deepcopy")
 function with the component as first argument and the _memo_ dictionary as second argument. The _memo_ dictionary should be treated as an opaque object.

Function `copy.replace()` is more limited than [`copy()`](https://docs.python.org/3/library/copy.html#copy.copy "copy.copy")
 and [`deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "copy.deepcopy")
, and only supports named tuples created by [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
, [`dataclasses`](https://docs.python.org/3/library/dataclasses.html#module-dataclasses "dataclasses: Generate special methods on user-defined classes.")
, and other classes which define method [`__replace__()`](https://docs.python.org/3/library/copy.html#object.__replace__ "object.__replace__")
.

object.\_\_replace\_\_(_self_, _/_, _\*\*changes_)[¶](https://docs.python.org/3/library/copy.html#object.__replace__ "Link to this definition")

This method should create a new object of the same type, replacing fields with values from _changes_.

Added in version 3.13.

See also

Module [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")

Discussion of the special methods used to support object state retrieval and restoration.

#### Previous topic

[`types` — Dynamic type creation and names for built-in types](https://docs.python.org/3/library/types.html "previous chapter")

#### Next topic

[`pprint` — Data pretty printer](https://docs.python.org/3/library/pprint.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=copy+%E2%80%94+Shallow+and+deep+copy+operations&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcopy.html&pagesource=library%2Fcopy.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/copy.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pprint.html "pprint — Data pretty printer")
     |
*   [previous](https://docs.python.org/3/library/types.html "types — Dynamic type creation and names for built-in types")
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
*   [Data Types](https://docs.python.org/3/library/datatypes.html)
     »
*   [`copy` — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html)
    
*    
    
    |
*   Theme Auto Light Dark |