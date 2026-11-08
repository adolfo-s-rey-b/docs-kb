### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/enum.html "enum — Support for enumerations")
     |
*   [previous](https://docs.python.org/3/library/pprint.html "pprint — Data pretty printer")
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
*   [`reprlib` — Alternate `repr()` implementation](https://docs.python.org/3/library/reprlib.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`reprlib` — Alternate [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
 implementation[¶](https://docs.python.org/3/library/reprlib.html#module-reprlib "Link to this heading")

=========================================================================================================================================================================================================

**Source code:** [Lib/reprlib.py](https://github.com/python/cpython/tree/3.15/Lib/reprlib.py)

* * *

The `reprlib` module provides a means for producing object representations with limits on the size of the resulting strings. This is used in the Python debugger and may be useful in other contexts as well.

This module provides a class, an instance, and a function:

class reprlib.Repr(_\*_, _maxlevel\=6_, _maxtuple\=6_, _maxlist\=6_, _maxarray\=5_, _maxdict\=4_, _maxset\=6_, _maxfrozenset\=6_, _maxdeque\=6_, _maxstring\=30_, _maxlong\=40_, _maxother\=30_, _fillvalue\='...'_, _indent\=None_)[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr "Link to this definition")

Class which provides formatting services useful in implementing functions similar to the built-in [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
; size limits for different object types are added to avoid the generation of representations which are excessively long.

The keyword arguments of the constructor can be used as a shortcut to set the attributes of the `Repr` instance. Which means that the following initialization:

Copy

aRepr \= reprlib.Repr(maxlevel\=3)

Is equivalent to:

Copy

aRepr \= reprlib.Repr()
aRepr.maxlevel \= 3

See section [Repr Objects](https://docs.python.org/3/library/reprlib.html#id1)
 for more information about `Repr` attributes.

Changed in version 3.12: Allow attributes to be set via keyword arguments.

reprlib.aRepr[¶](https://docs.python.org/3/library/reprlib.html#reprlib.aRepr "Link to this definition")

This is an instance of [`Repr`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr "reprlib.Repr")
 which is used to provide the [`repr()`](https://docs.python.org/3/library/reprlib.html#reprlib.repr "reprlib.repr")
 function described below. Changing the attributes of this object will affect the size limits used by `repr()` and the Python debugger.

reprlib.repr(_obj_)[¶](https://docs.python.org/3/library/reprlib.html#reprlib.repr "Link to this definition")

This is the [`repr()`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.repr "reprlib.Repr.repr")
 method of `aRepr`. It returns a string similar to that returned by the built-in function of the same name, but with limits on most sizes.

In addition to size-limiting tools, the module also provides a decorator for detecting recursive calls to [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__")
 and substituting a placeholder string instead.

@reprlib.recursive\_repr(_fillvalue\='...'_)[¶](https://docs.python.org/3/library/reprlib.html#reprlib.recursive_repr "Link to this definition")

Decorator for [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__")
 methods to detect recursive calls within the same thread. If a recursive call is made, the _fillvalue_ is returned, otherwise, the usual `__repr__()` call is made. For example:

Copy

\>>> from reprlib import recursive\_repr
\>>> class MyList(list):
...     @recursive\_repr()
...     def \_\_repr\_\_(self):
...         return '<' + '|'.join(map(repr, self)) + '>'
...
\>>> m \= MyList('abc')
\>>> m.append(m)
\>>> m.append('x')
\>>> print(m)
<'a'|'b'|'c'|...|'x'>

Added in version 3.2.

Repr Objects[¶](https://docs.python.org/3/library/reprlib.html#repr-objects "Link to this heading")

----------------------------------------------------------------------------------------------------

[`Repr`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr "reprlib.Repr")
 instances provide several attributes which can be used to provide size limits for the representations of different object types, and methods which format specific object types.

Repr.fillvalue[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.fillvalue "Link to this definition")

This string is displayed for recursive references. It defaults to `...`.

Added in version 3.11.

Repr.maxlevel[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxlevel "Link to this definition")

Depth limit on the creation of recursive representations. The default is `6`.

Repr.maxdict[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxdict "Link to this definition")

Repr.maxlist[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxlist "Link to this definition")

Repr.maxtuple[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxtuple "Link to this definition")

Repr.maxset[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxset "Link to this definition")

Repr.maxfrozenset[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxfrozenset "Link to this definition")

Repr.maxdeque[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxdeque "Link to this definition")

Repr.maxarray[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxarray "Link to this definition")

Limits on the number of entries represented for the named object type. The default is `4` for [`maxdict`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxdict "reprlib.Repr.maxdict")
, `5` for [`maxarray`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxarray "reprlib.Repr.maxarray")
, and `6` for the others.

Repr.maxlong[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxlong "Link to this definition")

Maximum number of characters in the representation for an integer. Digits are dropped from the middle. The default is `40`.

Repr.maxstring[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxstring "Link to this definition")

Limit on the number of characters in the representation of the string. Note that the “normal” representation of the string is used as the character source: if escape sequences are needed in the representation, these may be mangled when the representation is shortened. The default is `30`.

Repr.maxother[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxother "Link to this definition")

This limit is used to control the size of object types for which no specific formatting method is available on the [`Repr`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr "reprlib.Repr")
 object. It is applied in a similar manner as [`maxstring`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.maxstring "reprlib.Repr.maxstring")
. The default is `20`.

Repr.indent[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.indent "Link to this definition")

If this attribute is set to `None` (the default), the output is formatted with no line breaks or indentation, like the standard [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
. For example:

Copy

\>>> example \= \[\
...     1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: \[\]}}, 'ham'\]
\>>> import reprlib
\>>> aRepr \= reprlib.Repr()
\>>> print(aRepr.repr(example))
\[1, 'spam', {'a': 2, 'b': 'spam eggs', 'c': {3: 4.5, 6: \[\]}}, 'ham'\]

If `indent` is set to a string, each recursion level is placed on its own line, indented by that string:

Copy

\>>> aRepr.indent \= '-->'
\>>> print(aRepr.repr(example))
\[\
\-->1,\
\-->'spam',\
\-->{\
\-->-->'a': 2,\
\-->-->'b': 'spam eggs',\
\-->-->'c': {\
\-->-->-->3: 4.5,\
\-->-->-->6: \[\],\
\-->-->},\
\-->},\
\-->'ham',\
\]

Setting `indent` to a positive integer value behaves as if it was set to a string with that number of spaces:

Copy

\>>> aRepr.indent \= 4
\>>> print(aRepr.repr(example))
\[\
    1,\
    'spam',\
    {\
        'a': 2,\
        'b': 'spam eggs',\
        'c': {\
            3: 4.5,\
            6: \[\],\
        },\
    },\
    'ham',\
\]

Added in version 3.12.

Repr.repr(_obj_)[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.repr "Link to this definition")

The equivalent to the built-in [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
 that uses the formatting imposed by the instance.

Repr.repr1(_obj_, _level_)[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.repr1 "Link to this definition")

Recursive implementation used by [`repr()`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.repr "reprlib.Repr.repr")
. This uses the type of _obj_ to determine which formatting method to call, passing it _obj_ and _level_. The type-specific methods should call `repr1()` to perform recursive formatting, with `level - 1` for the value of _level_ in the recursive call.

Repr.repr\_TYPE(_obj_, _level_)

Formatting methods for specific types are implemented as methods with a name based on the type name. In the method name, **TYPE** is replaced by `'_'.join(type(obj).__name__.split())`. Dispatch to these methods is handled by [`repr1()`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.repr1 "reprlib.Repr.repr1")
. Type-specific methods which need to recursively format a value should call `self.repr1(subobj, level - 1)`.

Subclassing Repr Objects[¶](https://docs.python.org/3/library/reprlib.html#subclassing-repr-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

The use of dynamic dispatching by [`Repr.repr1()`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.repr1 "reprlib.Repr.repr1")
 allows subclasses of [`Repr`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr "reprlib.Repr")
 to add support for additional built-in object types or to modify the handling of types already supported. This example shows how special support for file objects could be added:

Copy

import reprlib
import sys

class MyRepr(reprlib.Repr):

    def repr\_TextIOWrapper(self, obj, level):
        if obj.name in {'<stdin>', '<stdout>', '<stderr>'}:
            return obj.name
        return repr(obj)

aRepr \= MyRepr()
print(aRepr.repr(sys.stdin))         \# prints '<stdin>'

<stdin>

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`reprlib` — Alternate `repr()` implementation](https://docs.python.org/3/library/reprlib.html#)
    *   [Repr Objects](https://docs.python.org/3/library/reprlib.html#repr-objects)
        
    *   [Subclassing Repr Objects](https://docs.python.org/3/library/reprlib.html#subclassing-repr-objects)
        

#### Previous topic

[`pprint` — Data pretty printer](https://docs.python.org/3/library/pprint.html "previous chapter")

#### Next topic

[`enum` — Support for enumerations](https://docs.python.org/3/library/enum.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=reprlib+%E2%80%94+Alternate+repr%28%29+implementation&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Freprlib.html&pagesource=library%2Freprlib.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/reprlib.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/enum.html "enum — Support for enumerations")
     |
*   [previous](https://docs.python.org/3/library/pprint.html "pprint — Data pretty printer")
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
*   [`reprlib` — Alternate `repr()` implementation](https://docs.python.org/3/library/reprlib.html)
    
*    
    
    |
*   Theme Auto Light Dark |