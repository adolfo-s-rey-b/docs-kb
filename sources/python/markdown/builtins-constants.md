### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/builtins/functions.html "Built-in functions")
     |
*   [previous](https://docs.python.org/3/builtins/stdtypes.html "Built-in Types")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python built-ins reference](https://docs.python.org/3/builtins/index.html)
     »
*   [Built-in Constants](https://docs.python.org/3/builtins/constants.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Built-in Constants[¶](https://docs.python.org/3/builtins/constants.html#built-in-constants "Link to this heading")

===================================================================================================================

A small number of constants live in the built-in namespace. They are:

False[¶](https://docs.python.org/3/builtins/constants.html#False "Link to this definition")

The false value of the [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 type. Assignments to `False` are illegal and raise a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
.

True[¶](https://docs.python.org/3/builtins/constants.html#True "Link to this definition")

The true value of the [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 type. Assignments to `True` are illegal and raise a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
.

None[¶](https://docs.python.org/3/builtins/constants.html#None "Link to this definition")

An object frequently used to represent the absence of a value, as when default arguments are not passed to a function. Assignments to `None` are illegal and raise a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
. `None` is the sole instance of the [`NoneType`](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType")
 type.

NotImplemented[¶](https://docs.python.org/3/builtins/constants.html#NotImplemented "Link to this definition")

A special value which should be returned by the binary special methods (e.g. [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
, [`__lt__()`](https://docs.python.org/3/reference/datamodel.html#object.__lt__ "object.__lt__")
, [`__add__()`](https://docs.python.org/3/reference/datamodel.html#object.__add__ "object.__add__")
, [`__rsub__()`](https://docs.python.org/3/reference/datamodel.html#object.__rsub__ "object.__rsub__")
, etc.) to indicate that the operation is not implemented with respect to the other type; may be returned by the in-place binary special methods (e.g. [`__imul__()`](https://docs.python.org/3/reference/datamodel.html#object.__imul__ "object.__imul__")
, [`__iand__()`](https://docs.python.org/3/reference/datamodel.html#object.__iand__ "object.__iand__")
, etc.) for the same purpose. It should not be evaluated in a boolean context. `NotImplemented` is the sole instance of the [`types.NotImplementedType`](https://docs.python.org/3/library/types.html#types.NotImplementedType "types.NotImplementedType")
 type.

Note

When a binary (or in-place) method returns `NotImplemented` the interpreter will try the reflected operation on the other type (or some other fallback, depending on the operator). If all attempts return `NotImplemented`, the interpreter will raise an appropriate exception. Incorrectly returning `NotImplemented` will result in a misleading error message or the `NotImplemented` value being returned to Python code.

See [Implementing the arithmetic operations](https://docs.python.org/3/library/numbers.html#implementing-the-arithmetic-operations)
 for examples.

Caution

`NotImplemented` and `NotImplementedError` are not interchangeable. This constant should only be used as described above; see [`NotImplementedError`](https://docs.python.org/3/builtins/exceptions.html#NotImplementedError "NotImplementedError")
 for details on correct usage of the exception.

Changed in version 3.9: Evaluating `NotImplemented` in a boolean context was deprecated.

Changed in version 3.14: Evaluating `NotImplemented` in a boolean context now raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
. It previously evaluated to [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 and emitted a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")
 since Python 3.9.

Ellipsis[¶](https://docs.python.org/3/builtins/constants.html#Ellipsis "Link to this definition")

The same as the ellipsis literal “`...`”, an object frequently used to indicate that something is omitted. Assignment to `Ellipsis` is possible, but assignment to `...` raises a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
. `Ellipsis` is the sole instance of the [`types.EllipsisType`](https://docs.python.org/3/library/types.html#types.EllipsisType "types.EllipsisType")
 type.

\_\_debug\_\_[¶](https://docs.python.org/3/builtins/constants.html#debug__ "Link to this definition")

This constant is true if Python was not started with an [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O)
 option. See also the [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert)
 statement.

Note

The names [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
, [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
, [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
 and [`__debug__`](https://docs.python.org/3/builtins/constants.html#debug__ "__debug__")
 cannot be reassigned (assignments to them, even as an attribute name, raise [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
), so they can be considered “true” constants.

Constants added by the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module[¶](https://docs.python.org/3/builtins/constants.html#constants-added-by-the-site-module "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module (which is imported automatically during startup, except if the [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S)
 command-line option is given) adds several constants to the built-in namespace. They are useful for the interactive interpreter shell and should not be used in programs.

quit(_code\=None_)[¶](https://docs.python.org/3/builtins/constants.html#quit "Link to this definition")

exit(_code\=None_)[¶](https://docs.python.org/3/builtins/constants.html#exit "Link to this definition")

Objects that when printed, print a message like “Use quit() or Ctrl-D (i.e. EOF) to exit”, and when accessed directly in the interactive interpreter or called as functions, raise [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
 with the specified exit code.

help

Object that when printed, prints the message “Type help() for interactive help, or help(object) for help about object.”, and when accessed directly in the interactive interpreter, invokes the built-in help system (see [`help()`](https://docs.python.org/3/builtins/functions.html#help "help")
).

copyright[¶](https://docs.python.org/3/builtins/constants.html#copyright "Link to this definition")

credits[¶](https://docs.python.org/3/builtins/constants.html#credits "Link to this definition")

Objects that when printed or called, print the text of copyright or credits, respectively.

license[¶](https://docs.python.org/3/builtins/constants.html#license "Link to this definition")

Object that when printed, prints the message “Type license() to see the full license text”, and when called, displays the full license text in a pager-like fashion (one screen at a time).

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Built-in Constants](https://docs.python.org/3/builtins/constants.html#)
    *   [Constants added by the `site` module](https://docs.python.org/3/builtins/constants.html#constants-added-by-the-site-module)
        

#### Previous topic

[Built-in Types](https://docs.python.org/3/builtins/stdtypes.html "previous chapter")

#### Next topic

[Built-in functions](https://docs.python.org/3/builtins/functions.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Built-in+Constants&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fbuiltins%2Fconstants.html&pagesource=builtins%2Fconstants.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/builtins/constants.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/builtins/functions.html "Built-in functions")
     |
*   [previous](https://docs.python.org/3/builtins/stdtypes.html "Built-in Types")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python built-ins reference](https://docs.python.org/3/builtins/index.html)
     »
*   [Built-in Constants](https://docs.python.org/3/builtins/constants.html)
    
*    
    
    |
*   Theme Auto Light Dark |