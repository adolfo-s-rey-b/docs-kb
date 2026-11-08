### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/tutorial/introduction.html "3. An Informal Introduction to Python")
     |
*   [previous](https://docs.python.org/3/tutorial/appetite.html "1. Whetting Your Appetite")
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
*   [2\. Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
    
*    
    
    |
*   Theme Auto Light Dark |

2\. Using the Python Interpreter[¶](https://docs.python.org/3/tutorial/interpreter.html#using-the-python-interpreter "Link to this heading")

=============================================================================================================================================

2.1. Invoking the Interpreter[¶](https://docs.python.org/3/tutorial/interpreter.html#invoking-the-interpreter "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

The Python interpreter is usually installed as `/usr/local/bin/python3.15` on those machines where it is available; putting `/usr/local/bin` in your Unix shell’s search path makes it possible to start it by typing the command:

python3.15

to the shell. [\[1\]](https://docs.python.org/3/tutorial/interpreter.html#id2)
 Since the choice of the directory where the interpreter lives is an installation option, other places are possible; check with your local Python guru or system administrator. (E.g., `/usr/local/python` is a popular alternative location.)

On Windows machines where you have installed Python from the [Microsoft Store](https://docs.python.org/3/using/windows.html#windows-store)
, the `python3.15` command will be available. If you have the [py.exe launcher](https://docs.python.org/3/using/windows.html#launcher)
 installed, you can use the `py` command. See [Python install manager](https://docs.python.org/3/using/windows.html#setting-envvars)
 for other ways to launch Python.

Typing an end-of-file character (Control\-D on Unix, Control\-Z on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn’t work, you can exit the interpreter by typing the following command: `quit()`.

The interpreter’s line-editing features include interactive editing, history substitution and code completion on most systems. Perhaps the quickest check to see whether command line editing is supported is typing a word in on the Python prompt, then pressing Left arrow (or Control\-b). If the cursor moves, you have command line editing; see Appendix [Interactive Input Editing and History Substitution](https://docs.python.org/3/tutorial/interactive.html#tut-interacting)
 for an introduction to the keys. If nothing appears to happen, or if a sequence like `^[[D` or `^B` appears, command line editing isn’t available; you’ll only be able to use backspace to remove characters from the current line.\
\
The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a _script_ from that file.\
\
A second way of starting the interpreter is `python -c command [arg] ...`, which executes the statement(s) in _command_, analogous to the shell’s [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c)\
 option. Since Python statements often contain spaces or other characters that are special to the shell, it is usually advised to quote _command_ in its entirety.\
\
Some Python modules are also useful as scripts. These can be invoked using `python -m module [arg] ...`, which executes the source file for _module_ as if you had spelled out its full name on the command line.\
\
When a script file is used, it is sometimes useful to be able to run the script and enter interactive mode afterwards. This can be done by passing [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i)\
 before the script.\
\
All command line options are described in [Command line and environment](https://docs.python.org/3/using/cmdline.html#using-on-general)\
.\
\
### 2.1.1. Argument Passing[¶](https://docs.python.org/3/tutorial/interpreter.html#argument-passing "Link to this heading")\
\
When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assigned to the `argv` variable in the `sys` module. You can access this list by executing `import sys`. The length of the list is at least one; when no script and no arguments are given, `sys.argv[0]` is an empty string. When the script name is given as `'-'` (meaning standard input), `sys.argv[0]` is set to `'-'`. When [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c)\
 _command_ is used, `sys.argv[0]` is set to `'-c'`. When [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m)\
 _module_ is used, `sys.argv[0]` is set to the full name of the located module. Options found after `-c` _command_ or `-m` _module_ are not consumed by the Python interpreter’s option processing but left in `sys.argv` for the command or module to handle.\
\
### 2.1.2. Interactive Mode[¶](https://docs.python.org/3/tutorial/interpreter.html#interactive-mode "Link to this heading")\
\
When commands are read from a tty, the interpreter is said to be in _interactive mode_. In this mode it prompts for the next command with the _primary prompt_, usually three greater-than signs (`>>>`); for continuation lines it prompts with the _secondary prompt_, by default three dots (`...`). The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt:\
\
Copy\
\
$ python3.15\
Python 3.15 (default, May 7 2025, 15:46:04)\
\[GCC 10.2.0\] on linux\
Type "help", "copyright", "credits" or "license" for more information.\
\>>>\
\
Continuation lines are needed when entering a multi-line construct. As an example, take a look at this [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)\
 statement:\
\
Copy\
\
\>>> the\_world\_is\_flat \= True\
\>>> if the\_world\_is\_flat:\
...     print("Be careful not to fall off!")\
...\
Be careful not to fall off!\
\
For more on interactive mode, see [Interactive Mode](https://docs.python.org/3/tutorial/appendix.html#tut-interac)\
.\
\
2.2. The Interpreter and Its Environment[¶](https://docs.python.org/3/tutorial/interpreter.html#the-interpreter-and-its-environment "Link to this heading")\
\
------------------------------------------------------------------------------------------------------------------------------------------------------------\
\
### 2.2.1. Source Code Encoding[¶](https://docs.python.org/3/tutorial/interpreter.html#source-code-encoding "Link to this heading")\
\
By default, Python source files are treated as encoded in UTF-8. In that encoding, characters of most languages in the world can be used simultaneously in string literals, identifiers and comments — although the standard library only uses ASCII characters for identifiers, a convention that any portable code should follow. To display all these characters properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all the characters in the file.\
\
To declare an encoding other than the default one, a special comment line should be added as the _first_ line of the file. The syntax is as follows:\
\
Copy\
\
\# -\*- coding: encoding -\*-\
\
where _encoding_ is one of the valid [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")\
 supported by Python.\
\
For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:\
\
Copy\
\
\# -\*- coding: cp1252 -\*-\
\
One exception to the _first line_ rule is when the source code starts with a [UNIX “shebang” line](https://docs.python.org/3/tutorial/appendix.html#tut-scripts)\
. In this case, the encoding declaration should be added as the second line of the file. For example:\
\
Copy\
\
#!/usr/bin/env python3\
\# -\*- coding: cp1252 -\*-\
\
Footnotes\
\
### [Table of Contents](https://docs.python.org/3/contents.html)\
\
*   [2\. Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html#)\
    *   [2.1. Invoking the Interpreter](https://docs.python.org/3/tutorial/interpreter.html#invoking-the-interpreter)\
        *   [2.1.1. Argument Passing](https://docs.python.org/3/tutorial/interpreter.html#argument-passing)\
            \
        *   [2.1.2. Interactive Mode](https://docs.python.org/3/tutorial/interpreter.html#interactive-mode)\
            \
    *   [2.2. The Interpreter and Its Environment](https://docs.python.org/3/tutorial/interpreter.html#the-interpreter-and-its-environment)\
        *   [2.2.1. Source Code Encoding](https://docs.python.org/3/tutorial/interpreter.html#source-code-encoding)\
            \
\
#### Previous topic\
\
[1\. Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html "previous chapter")\
\
#### Next topic\
\
[3\. An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=2.+Using+the+Python+Interpreter&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Ftutorial%2Finterpreter.html&pagesource=tutorial%2Finterpreter.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/tutorial/interpreter.rst?plain=1)\
    \
\
«\
\
### Navigation\
\
*   [index](https://docs.python.org/3/genindex.html "General Index")\
    \
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")\
     |\
*   [next](https://docs.python.org/3/tutorial/introduction.html "3. An Informal Introduction to Python")\
     |\
*   [previous](https://docs.python.org/3/tutorial/appetite.html "1. Whetting Your Appetite")\
     |\
*   ![Python logo](https://docs.python.org/3/_static/py.svg)\
*   [Python](https://www.python.org/)\
     »\
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文\
    \
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6\
    \
\
*   [3.15.2 documentation](https://docs.python.org/3/index.html)\
     »\
*   [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)\
     »\
*   [2\. Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |