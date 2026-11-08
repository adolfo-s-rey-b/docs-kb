### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/traceback.html "traceback — Print or retrieve a stack traceback")
     |
*   [previous](https://docs.python.org/3/library/abc.html "abc — Abstract Base Classes")
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
*   [`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`atexit` — Exit handlers[¶](https://docs.python.org/3/library/atexit.html#module-atexit "Link to this heading")

================================================================================================================

* * *

The `atexit` module defines functions to register and unregister _exit handlers_: functions that are automatically executed “at exit”, that is, upon normal program termination (for instance, if [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit")
 is called or the main module’s execution completes) or, more generally, upon [interpreter shutdown](https://docs.python.org/3/glossary.html#term-interpreter-shutdown)
.

At exit, all registered exit handlers are called in the _reverse_ order in which they were registered. If you register `A`, `B`, and `C`, at interpreter shutdown time they will be run in the order `C`, `B`, `A`. The assumption is that lower level modules will normally be imported before higher level modules and thus must be cleaned up later.

If an exception is raised during execution of an exit handler, a traceback is printed (unless [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
 is raised) and the exception information is saved. After all exit handlers have had a chance to run, the last exception to be raised is re-raised.

In programs that use multiple interpreters, each interpreter has its own stack of exit handlers, which are executed when the interpreter shuts down (for example, with [`concurrent.interpreters.Interpreter.close()`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter.close "concurrent.interpreters.Interpreter.close")
 or the C API [`Py_EndInterpreter()`](https://docs.python.org/3/c-api/subinterpreters.html#c.Py_EndInterpreter "Py_EndInterpreter")
). Registration functions in this module only affect the interpreter they are called from.

**Note:** Exit handlers are not called when the program is killed by a signal not handled by Python, when a Python fatal internal error is detected, or when [`os._exit()`](https://docs.python.org/3/library/os.html#os._exit "os._exit")
 is called.

**Note:** The effect of registering or unregistering functions from within a cleanup function is undefined.

Warning

When writing exit handlers, especially in C API extensions, keep in mind that other exit handlers may still run arbitrary Python code after you clean up. Such code should succeed or fail with an exception, rather than crash.

Changed in version 3.12: Attempts to start a new thread or [`os.fork()`](https://docs.python.org/3/library/os.html#os.fork "os.fork")
 a new process in an exit handler now leads to [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
. Previously, this could cause race conditions between the main Python runtime thread freeing thread states while internal [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
 routines or the new process try to use that state, which could lead to crashes rather than clean shutdown.

Changed in version 3.7: When used with subinterpreters, registered functions are local to the interpreter they were registered in.

atexit.register(_func_, _\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/atexit.html#atexit.register "Link to this definition")

Register _func_ as an exit handler. Any optional arguments that are to be passed to _func_ must be passed as arguments to `register()`. It is possible to register the same function and arguments more than once.

This function returns _func_, which makes it possible to use it as a decorator.

atexit.unregister(_func_)[¶](https://docs.python.org/3/library/atexit.html#atexit.unregister "Link to this definition")

Remove _func_ from the list of exit handlers. `unregister()` silently does nothing if _func_ was not previously registered. If _func_ has been registered more than once, every occurrence of that function in the `atexit` call stack will be removed. Equality comparisons (`==`) are used internally during unregistration, so function references do not need to have matching identities.

See also

Module [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")

Useful example of `atexit` to read and write [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
 history files.

`atexit` Example[¶](https://docs.python.org/3/library/atexit.html#atexit-example "Link to this heading")

---------------------------------------------------------------------------------------------------------

The following simple example demonstrates how a module can initialize a counter from a file when it is imported and save the counter’s updated value automatically when the program terminates without relying on the application making an explicit call into this module at termination.

Copy

try:
    with open('counterfile') as infile:
        \_count \= int(infile.read())
except FileNotFoundError:
    \_count \= 0

def incrcounter(n):
    global \_count
    \_count \= \_count + n

def savecounter():
    with open('counterfile', 'w') as outfile:
        outfile.write('%d' % \_count)

import atexit

atexit.register(savecounter)

Positional and keyword arguments may also be passed to [`register()`](https://docs.python.org/3/library/atexit.html#atexit.register "atexit.register")
 to be passed along to the registered function when it is called:

Copy

def goodbye(name, adjective):
    print('Goodbye %s, it was %s to meet you.' % (name, adjective))

import atexit

atexit.register(goodbye, 'Donny', 'nice')
\# or:
atexit.register(goodbye, adjective\='nice', name\='Donny')

Usage as a [decorator](https://docs.python.org/3/glossary.html#term-decorator)
:

Copy

import atexit

@atexit.register
def goodbye():
    print('You are now leaving the Python sector.')

This only works with functions that can be called without arguments.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html#)
    *   [`atexit` Example](https://docs.python.org/3/library/atexit.html#atexit-example)
        

#### Previous topic

[`abc` — Abstract Base Classes](https://docs.python.org/3/library/abc.html "previous chapter")

#### Next topic

[`traceback` — Print or retrieve a stack traceback](https://docs.python.org/3/library/traceback.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=atexit+%E2%80%94+Exit+handlers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fatexit.html&pagesource=library%2Fatexit.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/atexit.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/traceback.html "traceback — Print or retrieve a stack traceback")
     |
*   [previous](https://docs.python.org/3/library/abc.html "abc — Abstract Base Classes")
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
*   [`atexit` — Exit handlers](https://docs.python.org/3/library/atexit.html)
    
*    
    
    |
*   Theme Auto Light Dark |