### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/gc.html "gc — Garbage Collector interface")
     |
*   [previous](https://docs.python.org/3/library/traceback.html "traceback — Print or retrieve a stack traceback")
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
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)
     »
*   [`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`__future__` — Future statement definitions[¶](https://docs.python.org/3/library/__future__.html#module-__future__ "Link to this heading")

===========================================================================================================================================

**Source code:** [Lib/\_\_future\_\_.py](https://github.com/python/cpython/tree/3.15/Lib/__future__.py)

* * *

Imports of the form `from __future__ import feature` are called [future statements](https://docs.python.org/3/reference/simple_stmts.html#future)
. These are special-cased by the Python compiler to allow the use of new Python features in modules containing the future statement before the release in which the feature becomes standard.

While these future statements are given additional special meaning by the Python compiler, they are still executed like any other import statement and the `__future__` exists and is handled by the import system the same way any other Python module would be. This design serves three purposes:

*   To avoid confusing existing tools that analyze import statements and expect to find the modules they’re importing.
    
*   To document when incompatible changes were introduced, and when they will be — or were — made mandatory. This is a form of executable documentation, and can be inspected programmatically via importing `__future__` and examining its contents.
    
*   To ensure that [future statements](https://docs.python.org/3/reference/simple_stmts.html#future)
     run under releases prior to Python 2.1 at least yield runtime exceptions (the import of `__future__` will fail, because there was no module of that name prior to 2.1).
    

Module Contents[¶](https://docs.python.org/3/library/__future__.html#module-contents "Link to this heading")

-------------------------------------------------------------------------------------------------------------

No feature description will ever be deleted from `__future__`. Since its introduction in Python 2.1 the following features have found their way into the language using this mechanism:

| feature | optional in | mandatory in | effect |
| --- | --- | --- | --- |
| \_\_future\_\_.nested\_scopes[¶](https://docs.python.org/3/library/__future__.html#future__.nested_scopes "Link to this definition") | 2.1.0b1 | 2.2 | [**PEP 227**](https://peps.python.org/pep-0227/)<br>: _Statically Nested Scopes_ |
| \_\_future\_\_.generators[¶](https://docs.python.org/3/library/__future__.html#future__.generators "Link to this definition") | 2.2.0a1 | 2.3 | [**PEP 255**](https://peps.python.org/pep-0255/)<br>: _Simple Generators_ |
| \_\_future\_\_.division[¶](https://docs.python.org/3/library/__future__.html#future__.division "Link to this definition") | 2.2.0a2 | 3.0 | [**PEP 238**](https://peps.python.org/pep-0238/)<br>: _Changing the Division Operator_ |
| \_\_future\_\_.absolute\_import[¶](https://docs.python.org/3/library/__future__.html#future__.absolute_import "Link to this definition") | 2.5.0a1 | 3.0 | [**PEP 328**](https://peps.python.org/pep-0328/)<br>: _Imports: Multi-Line and Absolute/Relative_ |
| \_\_future\_\_.with\_statement[¶](https://docs.python.org/3/library/__future__.html#future__.with_statement "Link to this definition") | 2.5.0a1 | 2.6 | [**PEP 343**](https://peps.python.org/pep-0343/)<br>: _The “with” Statement_ |
| \_\_future\_\_.print\_function[¶](https://docs.python.org/3/library/__future__.html#future__.print_function "Link to this definition") | 2.6.0a2 | 3.0 | [**PEP 3105**](https://peps.python.org/pep-3105/)<br>: _Make print a function_ |
| \_\_future\_\_.unicode\_literals[¶](https://docs.python.org/3/library/__future__.html#future__.unicode_literals "Link to this definition") | 2.6.0a2 | 3.0 | [**PEP 3112**](https://peps.python.org/pep-3112/)<br>: _Bytes literals in Python 3000_ |
| \_\_future\_\_.generator\_stop[¶](https://docs.python.org/3/library/__future__.html#future__.generator_stop "Link to this definition") | 3.5.0b1 | 3.7 | [**PEP 479**](https://peps.python.org/pep-0479/)<br>: _StopIteration handling inside generators_ |
| \_\_future\_\_.annotations[¶](https://docs.python.org/3/library/__future__.html#future__.annotations "Link to this definition") | 3.7.0b1 | Never [\[1\]](https://docs.python.org/3/library/__future__.html#id2) | [**PEP 563**](https://peps.python.org/pep-0563/)<br>: _Postponed evaluation of annotations_, [**PEP 649**](https://peps.python.org/pep-0649/)<br>: _Deferred evaluation of annotations using descriptors_ |

class \_\_future\_\_.\_Feature[¶](https://docs.python.org/3/library/__future__.html#future__._Feature "Link to this definition")

Each statement in `__future__.py` is of the form:

Copy

FeatureName \= \_Feature(OptionalRelease, MandatoryRelease,
                       CompilerFlag)

where, normally, _OptionalRelease_ is less than _MandatoryRelease_, and both are 5-tuples of the same form as [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")
:

Copy

(PY\_MAJOR\_VERSION, \# the 2 in 2.1.0a3; an int
 PY\_MINOR\_VERSION, \# the 1; an int
 PY\_MICRO\_VERSION, \# the 0; an int
 PY\_RELEASE\_LEVEL, \# "alpha", "beta", "candidate" or "final"; string
 PY\_RELEASE\_SERIAL \# the 3; an int
)

\_Feature.getOptionalRelease()[¶](https://docs.python.org/3/library/__future__.html#future__._Feature.getOptionalRelease "Link to this definition")

_OptionalRelease_ records the first release in which the feature was accepted.

\_Feature.getMandatoryRelease()[¶](https://docs.python.org/3/library/__future__.html#future__._Feature.getMandatoryRelease "Link to this definition")

In the case of a _MandatoryRelease_ that has not yet occurred, _MandatoryRelease_ predicts the release in which the feature will become part of the language.

Else _MandatoryRelease_ records when the feature became part of the language; in releases at or after that, modules no longer need a future statement to use the feature in question, but may continue to use such imports.

_MandatoryRelease_ may also be `None`, meaning that a planned feature got dropped or that it is not yet decided.

\_Feature.compiler\_flag[¶](https://docs.python.org/3/library/__future__.html#future__._Feature.compiler_flag "Link to this definition")

_CompilerFlag_ is the (bitfield) flag that should be passed in the fourth argument to the built-in function [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
 to enable the feature in dynamically compiled code. This flag is stored in the `_Feature.compiler_flag` attribute on [`_Feature`](https://docs.python.org/3/library/__future__.html#future__._Feature "__future__._Feature")
 instances.

See also

[Future statements](https://docs.python.org/3/reference/simple_stmts.html#future)

How the compiler treats future imports.

[**PEP 236**](https://peps.python.org/pep-0236/)
 - Back to the \_\_future\_\_

The original proposal for the \_\_future\_\_ mechanism.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html#)
    *   [Module Contents](https://docs.python.org/3/library/__future__.html#module-contents)
        

#### Previous topic

[`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html "previous chapter")

#### Next topic

[`gc` — Garbage Collector interface](https://docs.python.org/3/library/gc.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=__future__+%E2%80%94+Future+statement+definitions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2F__future__.html&pagesource=library%2F__future__.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/__future__.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/gc.html "gc — Garbage Collector interface")
     |
*   [previous](https://docs.python.org/3/library/traceback.html "traceback — Print or retrieve a stack traceback")
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
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)
     »
*   [`__future__` — Future statement definitions](https://docs.python.org/3/library/__future__.html)
    
*    
    
    |
*   Theme Auto Light Dark |