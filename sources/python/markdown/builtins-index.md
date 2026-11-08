### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/builtins/stdtypes.html "Built-in Types")
     |
*   [previous](https://docs.python.org/3/reference/grammar.html "10. Full Grammar specification")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python built-ins reference](https://docs.python.org/3/builtins/index.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Python built-ins reference[¶](https://docs.python.org/3/builtins/index.html#python-built-ins-reference "Link to this heading")

===============================================================================================================================

Python comes with a number of built-in functions and classes.

The built-in classes include data types that would normally be considered part of the “core” of a language, such as numbers and lists. For these types, the Python language core defines the form of literals and places some constraints on their semantics, but does not fully define the semantics.

The built-ins also include functions and exceptions — objects that can be used by all Python code without the need of an [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
 statement. Some of these are defined by the core language, but many are not essential for the core semantics and are only described here.

See also

In addition to the built-ins, Python provides an extensive importable standard library, see [The Python standard library](https://docs.python.org/3/library/index.html#library-index)
.

*   [Built-in Types](https://docs.python.org/3/builtins/stdtypes.html)
    *   [Truth Value Testing](https://docs.python.org/3/builtins/stdtypes.html#truth-value-testing)
        
    *   [Boolean Operations — `and`, `or`, `not`](https://docs.python.org/3/builtins/stdtypes.html#boolean-operations-and-or-not)
        
    *   [Comparisons](https://docs.python.org/3/builtins/stdtypes.html#comparisons)
        
    *   [Numeric Types — `int`, `float`, `complex`](https://docs.python.org/3/builtins/stdtypes.html#numeric-types-int-float-complex)
        
    *   [Boolean Type - `bool`](https://docs.python.org/3/builtins/stdtypes.html#boolean-type-bool)
        
    *   [Iteration-related types](https://docs.python.org/3/builtins/stdtypes.html#iteration-related-types)
        
    *   [Sequence Types — `list`, `tuple`, `range`](https://docs.python.org/3/builtins/stdtypes.html#sequence-types-list-tuple-range)
        
    *   [Text and Binary Sequence Type Methods Summary](https://docs.python.org/3/builtins/stdtypes.html#text-and-binary-sequence-type-methods-summary)
        
    *   [Text Sequence Type — `str`](https://docs.python.org/3/builtins/stdtypes.html#text-sequence-type-str)
        
    *   [Binary Sequence Types — `bytes`, `bytearray`, `memoryview`](https://docs.python.org/3/builtins/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)
        
    *   [Set Types — `set`, `frozenset`](https://docs.python.org/3/builtins/stdtypes.html#set-types-set-frozenset)
        
    *   [Mapping types — `dict`, `frozendict`](https://docs.python.org/3/builtins/stdtypes.html#mapping-types-dict-frozendict)
        
    *   [Context Manager Types](https://docs.python.org/3/builtins/stdtypes.html#context-manager-types)
        
    *   [Type Annotation Types — Generic Alias, Union](https://docs.python.org/3/builtins/stdtypes.html#type-annotation-types-generic-alias-union)
        
    *   [Other Built-in Types](https://docs.python.org/3/builtins/stdtypes.html#other-built-in-types)
        
    *   [Special Attributes](https://docs.python.org/3/builtins/stdtypes.html#special-attributes)
        
    *   [Integer string conversion length limitation](https://docs.python.org/3/builtins/stdtypes.html#integer-string-conversion-length-limitation)
        
*   [Built-in Constants](https://docs.python.org/3/builtins/constants.html)
    *   [Constants added by the `site` module](https://docs.python.org/3/builtins/constants.html#constants-added-by-the-site-module)
        
*   [Built-in functions](https://docs.python.org/3/builtins/functions.html)
    
*   [Built-in Exceptions](https://docs.python.org/3/builtins/exceptions.html)
    *   [Exception context](https://docs.python.org/3/builtins/exceptions.html#exception-context)
        
    *   [Inheriting from built-in exceptions](https://docs.python.org/3/builtins/exceptions.html#inheriting-from-built-in-exceptions)
        
    *   [Base classes](https://docs.python.org/3/builtins/exceptions.html#base-classes)
        
    *   [Concrete exceptions](https://docs.python.org/3/builtins/exceptions.html#concrete-exceptions)
        
    *   [Warnings](https://docs.python.org/3/builtins/exceptions.html#warnings)
        
    *   [Exception groups](https://docs.python.org/3/builtins/exceptions.html#exception-groups)
        
    *   [Exception hierarchy](https://docs.python.org/3/builtins/exceptions.html#exception-hierarchy)
        
*   [Thread Safety Guarantees](https://docs.python.org/3/builtins/threadsafety.html)
    *   [Thread safety levels](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-levels)
        
    *   [Thread safety for list objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-list-objects)
        
    *   [Thread safety for dict objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-dict-objects)
        
    *   [Thread safety for set objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-set-objects)
        
    *   [Thread safety for bytearray objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-bytearray-objects)
        
    *   [Thread safety for memoryview objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-memoryview-objects)
        
*   [Time complexity of operations on built-in types](https://docs.python.org/3/builtins/time-complexity.html)
    *   [`list`](https://docs.python.org/3/builtins/time-complexity.html#list)
        
    *   [`tuple`](https://docs.python.org/3/builtins/time-complexity.html#tuple)
        
    *   [`dict`, `frozendict`](https://docs.python.org/3/builtins/time-complexity.html#dict-frozendict)
        
    *   [`set`, `frozenset`](https://docs.python.org/3/builtins/time-complexity.html#set-frozenset)
        
    *   [`str`, `bytes`, `bytearray`](https://docs.python.org/3/builtins/time-complexity.html#str-bytes-bytearray)
        
    *   [`memoryview`](https://docs.python.org/3/builtins/time-complexity.html#memoryview)
        
    *   [`range`](https://docs.python.org/3/builtins/time-complexity.html#range)
        
    *   [Notes](https://docs.python.org/3/builtins/time-complexity.html#notes)
        

#### Previous topic

[10\. Full Grammar specification](https://docs.python.org/3/reference/grammar.html "previous chapter")

#### Next topic

[Built-in Types](https://docs.python.org/3/builtins/stdtypes.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Python+built-ins+reference&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fbuiltins%2Findex.html&pagesource=builtins%2Findex.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/builtins/index.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/builtins/stdtypes.html "Built-in Types")
     |
*   [previous](https://docs.python.org/3/reference/grammar.html "10. Full Grammar specification")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python built-ins reference](https://docs.python.org/3/builtins/index.html)
    
*    
    
    |
*   Theme Auto Light Dark |