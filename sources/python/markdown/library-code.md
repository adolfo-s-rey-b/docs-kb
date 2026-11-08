### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/codeop.html "codeop — Compile Python code")
     |
*   [previous](https://docs.python.org/3/library/custominterp.html "Custom Python Interpreters")
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
*   [`code` — Interpreter base classes](https://docs.python.org/3/library/code.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`code` — Interpreter base classes[¶](https://docs.python.org/3/library/code.html#module-code "Link to this heading")

=====================================================================================================================

**Source code:** [Lib/code.py](https://github.com/python/cpython/tree/3.15/Lib/code.py)

* * *

The `code` module provides facilities to implement read-eval-print loops in Python. Two classes and convenience functions are included which can be used to build applications which provide an interactive interpreter prompt.

class code.InteractiveInterpreter(_locals\=None_)[¶](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter "Link to this definition")

This class deals with parsing and interpreter state (the user’s namespace); it does not deal with input buffering or prompting or input file naming (the filename is always passed in explicitly). The optional _locals_ argument specifies a mapping to use as the namespace in which code will be executed; it defaults to a newly created dictionary with key `'__name__'` set to `'__console__'` and key `'__doc__'` set to `None`.

Note that functions and classes objects created under an `InteractiveInterpreter` instance will belong to the namespace specified by _locals_. They are only pickleable if _locals_ is the namespace of an existing module.

class code.InteractiveConsole(_locals\=None_, _filename\='<console>'_, _\*_, _local\_exit\=False_)[¶](https://docs.python.org/3/library/code.html#code.InteractiveConsole "Link to this definition")

Closely emulate the behavior of the interactive Python interpreter. This class builds on [`InteractiveInterpreter`](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter "code.InteractiveInterpreter")
 and adds prompting using the familiar `sys.ps1` and `sys.ps2`, and input buffering. If _local\_exit_ is true, `exit()` and `quit()` in the console will not raise [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
, but instead return to the calling code.

Changed in version 3.13: Added _local\_exit_ parameter.

code.interact(_banner\=None_, _readfunc\=None_, _local\=None_, _exitmsg\=None_, _local\_exit\=False_)[¶](https://docs.python.org/3/library/code.html#code.interact "Link to this definition")

Convenience function to run a read-eval-print loop. This creates a new instance of [`InteractiveConsole`](https://docs.python.org/3/library/code.html#code.InteractiveConsole "code.InteractiveConsole")
 and sets _readfunc_ to be used as the [`InteractiveConsole.raw_input()`](https://docs.python.org/3/library/code.html#code.InteractiveConsole.raw_input "code.InteractiveConsole.raw_input")
 method, if provided. If _local_ is provided, it is passed to the `InteractiveConsole` constructor for use as the default namespace for the interpreter loop. If _local\_exit_ is provided, it is passed to the `InteractiveConsole` constructor. The [`interact()`](https://docs.python.org/3/library/code.html#code.InteractiveConsole.interact "code.InteractiveConsole.interact")
 method of the instance is then run with _banner_ and _exitmsg_ passed as the banner and exit message to use, if provided. The console object is discarded after use.

Changed in version 3.6: Added _exitmsg_ parameter.

Changed in version 3.13: Added _local\_exit_ parameter.

code.compile\_command(_source_, _filename\='<input>'_, _symbol\='single'_)[¶](https://docs.python.org/3/library/code.html#code.compile_command "Link to this definition")

This function is useful for programs that want to emulate Python’s interpreter main loop (a.k.a. the read-eval-print loop). The tricky part is to determine when the user has entered an incomplete command that can be completed by entering more text (as opposed to a complete command or a syntax error). This function _almost_ always makes the same decision as the real interpreter main loop.

_source_ is the source string; _filename_ is the optional filename from which source was read, defaulting to `'<input>'`; and _symbol_ is the optional grammar start symbol, which should be `'single'` (the default), `'eval'` or `'exec'`.

Returns a code object (the same as `compile(source, filename, symbol)`) if the command is complete and valid; `None` if the command is incomplete; raises [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
 if the command is complete and contains a syntax error, or raises [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 or [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if the command contains an invalid literal.

Interactive Interpreter Objects[¶](https://docs.python.org/3/library/code.html#interactive-interpreter-objects "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

InteractiveInterpreter.runsource(_source_, _filename\='<input>'_, _symbol\='single'_)[¶](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.runsource "Link to this definition")

Compile and run some source in the interpreter. Arguments are the same as for [`compile_command()`](https://docs.python.org/3/library/code.html#code.compile_command "code.compile_command")
; the default for _filename_ is `'<input>'`, and for _symbol_ is `'single'`. One of several things can happen:

*   The input is incorrect; [`compile_command()`](https://docs.python.org/3/library/code.html#code.compile_command "code.compile_command")
     raised an exception (usually [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
    ). A syntax traceback will be printed by calling the [`showsyntaxerror()`](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.showsyntaxerror "code.InteractiveInterpreter.showsyntaxerror")
     method. `runsource()` returns `False`.
    
*   The input is incomplete, and more input is required; [`compile_command()`](https://docs.python.org/3/library/code.html#code.compile_command "code.compile_command")
     returned `None`. `runsource()` returns `True`.
    
*   The input is complete; [`compile_command()`](https://docs.python.org/3/library/code.html#code.compile_command "code.compile_command")
     returned a code object. The code is executed by calling the [`runcode()`](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.runcode "code.InteractiveInterpreter.runcode")
     (which also handles run-time exceptions, except for [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
    ). `runsource()` returns `False`.
    

The return value can be used to decide whether to use `sys.ps1` or `sys.ps2` to prompt the next line.

InteractiveInterpreter.runcode(_code_)[¶](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.runcode "Link to this definition")

Execute a code object. When an exception occurs, [`showtraceback()`](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.showtraceback "code.InteractiveInterpreter.showtraceback")
 is called to display a traceback. All exceptions are caught except [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
, which is allowed to propagate.

A note about [`KeyboardInterrupt`](https://docs.python.org/3/builtins/exceptions.html#KeyboardInterrupt "KeyboardInterrupt")
: this exception may occur elsewhere in this code, and may not always be caught. The caller should be prepared to deal with it.

InteractiveInterpreter.showsyntaxerror(_filename\=None_)[¶](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.showsyntaxerror "Link to this definition")

Display the syntax error that just occurred. This does not display a stack trace because there isn’t one for syntax errors. If _filename_ is given, it is stuffed into the exception instead of the default filename provided by Python’s parser, because it always uses `'<string>'` when reading from a string. The output is written by the [`write()`](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.write "code.InteractiveInterpreter.write")
 method.

InteractiveInterpreter.showtraceback()[¶](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.showtraceback "Link to this definition")

Display the exception that just occurred. We remove the first stack item because it is within the interpreter object implementation. The output is written by the [`write()`](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.write "code.InteractiveInterpreter.write")
 method.

Changed in version 3.5: The full chained traceback is displayed instead of just the primary traceback.

InteractiveInterpreter.write(_data_)[¶](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.write "Link to this definition")

Write a string to the standard error stream (`sys.stderr`). Derived classes should override this to provide the appropriate output handling as needed.

Interactive Console Objects[¶](https://docs.python.org/3/library/code.html#interactive-console-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

The [`InteractiveConsole`](https://docs.python.org/3/library/code.html#code.InteractiveConsole "code.InteractiveConsole")
 class is a subclass of [`InteractiveInterpreter`](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter "code.InteractiveInterpreter")
, and so offers all the methods of the interpreter objects as well as the following additions.

InteractiveConsole.interact(_banner\=None_, _exitmsg\=None_)[¶](https://docs.python.org/3/library/code.html#code.InteractiveConsole.interact "Link to this definition")

Closely emulate the interactive Python console. The optional _banner_ argument specify the banner to print before the first interaction; by default it prints a banner similar to the one printed by the standard Python interpreter, followed by the class name of the console object in parentheses (so as not to confuse this with the real interpreter – since it’s so close!).

The optional _exitmsg_ argument specifies an exit message printed when exiting. Pass the empty string to suppress the exit message. If _exitmsg_ is not given or `None`, a default message is printed.

Changed in version 3.4: To suppress printing any banner, pass an empty string.

Changed in version 3.6: Print an exit message when exiting.

InteractiveConsole.push(_line_)[¶](https://docs.python.org/3/library/code.html#code.InteractiveConsole.push "Link to this definition")

Push a line of source text to the interpreter. The line should not have a trailing newline; it may have internal newlines. The line is appended to a buffer and the interpreter’s [`runsource()`](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.runsource "code.InteractiveInterpreter.runsource")
 method is called with the concatenated contents of the buffer as source. If this indicates that the command was executed or invalid, the buffer is reset; otherwise, the command is incomplete, and the buffer is left as it was after the line was appended. The return value is `True` if more input is required, `False` if the line was dealt with in some way (this is the same as `runsource()`).

InteractiveConsole.resetbuffer()[¶](https://docs.python.org/3/library/code.html#code.InteractiveConsole.resetbuffer "Link to this definition")

Remove any unhandled source text from the input buffer.

InteractiveConsole.raw\_input(_prompt\=''_)[¶](https://docs.python.org/3/library/code.html#code.InteractiveConsole.raw_input "Link to this definition")

Write a prompt and read a line. The returned line does not include the trailing newline. When the user enters the EOF key sequence, [`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
 is raised. The base implementation reads from `sys.stdin`; a subclass may replace this with a different implementation.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`code` — Interpreter base classes](https://docs.python.org/3/library/code.html#)
    *   [Interactive Interpreter Objects](https://docs.python.org/3/library/code.html#interactive-interpreter-objects)
        
    *   [Interactive Console Objects](https://docs.python.org/3/library/code.html#interactive-console-objects)
        

#### Previous topic

[Custom Python Interpreters](https://docs.python.org/3/library/custominterp.html "previous chapter")

#### Next topic

[`codeop` — Compile Python code](https://docs.python.org/3/library/codeop.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=code+%E2%80%94+Interpreter+base+classes&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcode.html&pagesource=library%2Fcode.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/code.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/codeop.html "codeop — Compile Python code")
     |
*   [previous](https://docs.python.org/3/library/custominterp.html "Custom Python Interpreters")
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
*   [`code` — Interpreter base classes](https://docs.python.org/3/library/code.html)
    
*    
    
    |
*   Theme Auto Light Dark |