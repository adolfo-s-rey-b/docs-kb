### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/index.html "Python Setup and Usage")
     |
*   [previous](https://docs.python.org/3/tutorial/floatingpoint.html "15. Floating-Point Arithmetic: Issues and Limitations")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
     »
*   [16\. Appendix](https://docs.python.org/3/tutorial/appendix.html)
    
*    
    
    |
*   Theme Auto Light Dark |

16\. Appendix[¶](https://docs.python.org/3/tutorial/appendix.html#appendix "Link to this heading")

===================================================================================================

16.1. Interactive Mode[¶](https://docs.python.org/3/tutorial/appendix.html#interactive-mode "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

There are two variants of the interactive [REPL](https://docs.python.org/3/glossary.html#term-REPL)
. The classic basic interpreter is supported on all platforms with minimal line control capabilities.

Since Python 3.13, a new interactive shell is used by default. This one supports color, multiline editing, history browsing, and paste mode. To disable color, see [Controlling color](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
 for details. Function keys provide some additional functionality. F1 enters the interactive help browser [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
. F2 allows for browsing command-line history with neither output nor the [\>>>](https://docs.python.org/3/glossary.html#term-0)
 and […](https://docs.python.org/3/glossary.html#term-...)
 prompts. F3 enters “paste mode”, which makes pasting larger blocks of code easier. Press F3 to return to the regular prompt.

When using the new interactive shell, exit the shell by typing exit or quit. Adding call parentheses after those commands is not required.

If the new interactive shell is not desired, it can be disabled via the [`PYTHON_BASIC_REPL`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_BASIC_REPL)
 environment variable.

### 16.1.1. Error Handling[¶](https://docs.python.org/3/tutorial/appendix.html#error-handling "Link to this heading")

When an error occurs, the interpreter prints an error message and a stack trace. In interactive mode, it then returns to the primary prompt; when input came from a file, it exits with a nonzero exit status after printing the stack trace. (Exceptions handled by an [`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
 clause in a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 statement are not errors in this context.) Some errors are unconditionally fatal and cause an exit with a nonzero exit status; this applies to internal inconsistencies and some cases of running out of memory. All error messages are written to the standard error stream; normal output from executed commands is written to standard output.

Typing the interrupt character (usually Control\-C or Delete) to the primary or secondary prompt cancels the input and returns to the primary prompt. [\[1\]](https://docs.python.org/3/tutorial/appendix.html#id2)
 Typing an interrupt while a command is executing raises the [`KeyboardInterrupt`](https://docs.python.org/3/builtins/exceptions.html#KeyboardInterrupt "KeyboardInterrupt")
 exception, which may be handled by a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 statement.

### 16.1.2. Executable Python Scripts[¶](https://docs.python.org/3/tutorial/appendix.html#executable-python-scripts "Link to this heading")

On BSD’ish Unix systems, Python scripts can be made directly executable, like shell scripts, by putting the line

Copy

#!/usr/bin/env python3

(assuming that the interpreter is on the user’s `PATH`) at the beginning of the script and giving the file an executable mode. The `#!` must be the first two characters of the file. On some platforms, this first line must end with a Unix-style line ending (`'\n'`), not a Windows (`'\r\n'`) line ending. Note that the hash, or pound, character, `'#'`, is used to start a comment in Python.

The script can be given an executable mode, or permission, using the **chmod** command.

Copy

$ chmod +x myscript.py

On Windows systems, there is no notion of an “executable mode”. The Python installer automatically associates `.py` files with `python.exe` so that a double-click on a Python file will run it as a script. The extension can also be `.pyw`, in that case, the console window that normally appears is suppressed.

### 16.1.3. The Interactive Startup File[¶](https://docs.python.org/3/tutorial/appendix.html#the-interactive-startup-file "Link to this heading")

When you use Python interactively, it is frequently handy to have some standard commands executed every time the interpreter is started. You can do this by setting an environment variable named [`PYTHONSTARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP)
 to the name of a file containing your start-up commands. This is similar to the `.profile` feature of the Unix shells.

This file is only read in interactive sessions, not when Python reads commands from a script, and not when `/dev/tty` is given as the explicit source of commands (which otherwise behaves like an interactive session). It is executed in the same namespace where interactive commands are executed, so that objects that it defines or imports can be used without qualification in the interactive session. You can also change the prompts `sys.ps1` and `sys.ps2` in this file.

If you want to read an additional start-up file from the current directory, you can program this in the global start-up file using code like `if os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read())`. If you want to use the startup file in a script, you must do this explicitly in the script:

Copy

import os
filename \= os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup\_file \= fobj.read()
    exec(startup\_file)

### 16.1.4. The Customization Modules[¶](https://docs.python.org/3/tutorial/appendix.html#the-customization-modules "Link to this heading")

Python provides two hooks to let you customize it: sitecustomize and usercustomize. To see how it works, you need first to find the location of your user site-packages directory. Start Python and run this code:

Copy

\>>> import site
\>>> site.getusersitepackages()
'/home/user/.local/lib/python3.x/site-packages'

Now you can create a file named `usercustomize.py` in that directory and put anything you want in it. It will affect every invocation of Python, unless it is started with the [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s)
 option to disable the automatic import.

sitecustomize works in the same way, but is typically created by an administrator of the computer in the global site-packages directory, and is imported before usercustomize. See the documentation of the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module for more details.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [16\. Appendix](https://docs.python.org/3/tutorial/appendix.html#)
    *   [16.1. Interactive Mode](https://docs.python.org/3/tutorial/appendix.html#interactive-mode)
        *   [16.1.1. Error Handling](https://docs.python.org/3/tutorial/appendix.html#error-handling)
            
        *   [16.1.2. Executable Python Scripts](https://docs.python.org/3/tutorial/appendix.html#executable-python-scripts)
            
        *   [16.1.3. The Interactive Startup File](https://docs.python.org/3/tutorial/appendix.html#the-interactive-startup-file)
            
        *   [16.1.4. The Customization Modules](https://docs.python.org/3/tutorial/appendix.html#the-customization-modules)
            

#### Previous topic

[15\. Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html "previous chapter")

#### Next topic

[Python Setup and Usage](https://docs.python.org/3/using/index.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=16.+Appendix&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Ftutorial%2Fappendix.html&pagesource=tutorial%2Fappendix.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/tutorial/appendix.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/using/index.html "Python Setup and Usage")
     |
*   [previous](https://docs.python.org/3/tutorial/floatingpoint.html "15. Floating-Point Arithmetic: Issues and Limitations")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
     »
*   [16\. Appendix](https://docs.python.org/3/tutorial/appendix.html)
    
*    
    
    |
*   Theme Auto Light Dark |