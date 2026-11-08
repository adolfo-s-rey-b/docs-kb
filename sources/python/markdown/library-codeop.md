### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/modules.html "Importing Modules")
     |
*   [previous](https://docs.python.org/3/library/code.html "code — Interpreter base classes")
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
*   [Custom Python Interpreters](https://docs.python.org/3/library/custominterp.html)
     »
*   [`codeop` — Compile Python code](https://docs.python.org/3/library/codeop.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`codeop` — Compile Python code[¶](https://docs.python.org/3/library/codeop.html#module-codeop "Link to this heading")

======================================================================================================================

**Source code:** [Lib/codeop.py](https://github.com/python/cpython/tree/3.15/Lib/codeop.py)

* * *

The `codeop` module provides utilities upon which the Python read-eval-print loop can be emulated, as is done in the [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.")
 module. As a result, you probably don’t want to use the module directly; if you want to include such a loop in your program you probably want to use the `code` module instead.

There are two parts to this job:

1.  Being able to tell if a line of input completes a Python statement: in short, telling whether to print ‘`>>>`’ or ‘`...`’ next.
    
2.  Remembering which future statements the user has entered, so subsequent input can be compiled with these in effect.
    

The `codeop` module provides a way of doing each of these things, and a way of doing them both.

To do just the former:

codeop.compile\_command(_source_, _filename\='<input>'_, _symbol\='single'_)[¶](https://docs.python.org/3/library/codeop.html#codeop.compile_command "Link to this definition")

Tries to compile _source_, which should be a string of Python code and return a code object if _source_ is valid Python code. In that case, the filename attribute of the code object will be _filename_, which defaults to `'<input>'`. Returns `None` if _source_ is _not_ valid Python code, but is a prefix of valid Python code.

If there is a problem with _source_, an exception will be raised. [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
 is raised if there is invalid Python syntax, and [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 or [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if there is an invalid literal.

The _symbol_ argument determines whether _source_ is compiled as a statement (`'single'`, the default), as a sequence of [statement](https://docs.python.org/3/glossary.html#term-statement)
 (`'exec'`) or as an [expression](https://docs.python.org/3/glossary.html#term-expression)
 (`'eval'`). Any other value will cause [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 to be raised.

Note

It is possible (but not likely) that the parser stops parsing with a successful outcome before reaching the end of the source; in this case, trailing symbols may be ignored instead of causing an error. For example, a backslash followed by two newlines may be followed by arbitrary garbage. This will be fixed once the API for the parser is better.

class codeop.Compile[¶](https://docs.python.org/3/library/codeop.html#codeop.Compile "Link to this definition")

Instances of this class have [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__")
 methods identical in signature to the built-in function [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
, but with the difference that if the instance compiles program text containing a [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions")
 statement, the instance ‘remembers’ and compiles all subsequent program texts with the statement in force.

class codeop.CommandCompiler[¶](https://docs.python.org/3/library/codeop.html#codeop.CommandCompiler "Link to this definition")

Instances of this class have [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__")
 methods identical in signature to [`compile_command()`](https://docs.python.org/3/library/codeop.html#codeop.compile_command "codeop.compile_command")
; the difference is that if the instance compiles program text containing a [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions")
 statement, the instance ‘remembers’ and compiles all subsequent program texts with the statement in force.

#### Previous topic

[`code` — Interpreter base classes](https://docs.python.org/3/library/code.html "previous chapter")

#### Next topic

[Importing Modules](https://docs.python.org/3/library/modules.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=codeop+%E2%80%94+Compile+Python+code&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcodeop.html&pagesource=library%2Fcodeop.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/codeop.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/modules.html "Importing Modules")
     |
*   [previous](https://docs.python.org/3/library/code.html "code — Interpreter base classes")
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
*   [Custom Python Interpreters](https://docs.python.org/3/library/custominterp.html)
     »
*   [`codeop` — Compile Python code](https://docs.python.org/3/library/codeop.html)
    
*    
    
    |
*   Theme Auto Light Dark |