### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/binary.html "Binary Data Services")
     |
*   [previous](https://docs.python.org/3/library/readline.html "readline — GNU readline interface")
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
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
     »
*   [`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`rlcompleter` — Completion function for GNU readline[¶](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "Link to this heading")

======================================================================================================================================================

**Source code:** [Lib/rlcompleter.py](https://github.com/python/cpython/tree/3.15/Lib/rlcompleter.py)

* * *

The `rlcompleter` module defines a completion function suitable to be passed to [`set_completer()`](https://docs.python.org/3/library/readline.html#readline.set_completer "readline.set_completer")
 in the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
 module.

When this module is imported on a Unix platform with the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
 module available, an instance of the [`Completer`](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer "rlcompleter.Completer")
 class is automatically created and its [`complete()`](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer.complete "rlcompleter.Completer.complete")
 method is set as the [readline completer](https://docs.python.org/3/library/readline.html#readline-completion)
. The method provides completion of valid Python [identifiers and keywords](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
.

Example:

Copy

\>>> import rlcompleter
\>>> import readline
\>>> readline.parse\_and\_bind("tab: complete")
\>>> readline. <TAB PRESSED\>
readline.\_\_doc\_\_          readline.get\_line\_buffer(  readline.read\_init\_file(
readline.\_\_file\_\_         readline.insert\_text(      readline.set\_completer(
readline.\_\_name\_\_         readline.parse\_and\_bind(
\>>> readline.

The `rlcompleter` module is designed for use with Python’s [interactive mode](https://docs.python.org/3/tutorial/interpreter.html#tut-interactive)
. Unless Python is run with the [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S)
 option, the module is automatically imported and configured (see [Readline configuration](https://docs.python.org/3/library/site.html#rlcompleter-config)
).

On platforms without [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
, the [`Completer`](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer "rlcompleter.Completer")
 class defined by this module can still be used for custom purposes.

class rlcompleter.Completer[¶](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer "Link to this definition")

Completer objects have the following method:

complete(_text_, _state_)[¶](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer.complete "Link to this definition")

Return the next possible completion for _text_.

When called by the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
 module, this method is called successively with `state == 0, 1, 2, ...` until the method returns `None`.

If called for _text_ that doesn’t include a period character (`'.'`), it will complete from names currently defined in [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.")
, [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")
 and keywords (as defined by the [`keyword`](https://docs.python.org/3/library/keyword.html#module-keyword "keyword: Test whether a string is a keyword in Python.")
 module).

If called for a dotted name, it will try to evaluate anything without obvious side-effects (functions will not be evaluated, but it can generate calls to [`__getattr__()`](https://docs.python.org/3/reference/datamodel.html#object.__getattr__ "object.__getattr__")
) up to the last part, and find matches for the rest via the [`dir()`](https://docs.python.org/3/builtins/functions.html#dir "dir")
 function. Any exception raised during the evaluation of the expression is caught, silenced and [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 is returned.

#### Previous topic

[`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html "previous chapter")

#### Next topic

[Binary Data Services](https://docs.python.org/3/library/binary.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=rlcompleter+%E2%80%94+Completion+function+for+GNU+readline&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Frlcompleter.html&pagesource=library%2Frlcompleter.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/rlcompleter.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/binary.html "Binary Data Services")
     |
*   [previous](https://docs.python.org/3/library/readline.html "readline — GNU readline interface")
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
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
     »
*   [`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html)
    
*    
    
    |
*   Theme Auto Light Dark |