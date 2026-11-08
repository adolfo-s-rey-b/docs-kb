### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pdb.html "pdb — The Python Debugger")
     |
*   [previous](https://docs.python.org/3/library/bdb.html "bdb — Debugger framework")
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
*   [Debugging and profiling](https://docs.python.org/3/library/debug.html)
     »
*   [`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`faulthandler` — Dump the Python traceback[¶](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "Link to this heading")

==============================================================================================================================================

Added in version 3.3.

* * *

This module contains functions to dump Python tracebacks explicitly, on a fault, after a timeout, or on a user signal. Call [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable")
 to install fault handlers for the [`SIGSEGV`](https://docs.python.org/3/library/signal.html#signal.SIGSEGV "signal.SIGSEGV")
, [`SIGFPE`](https://docs.python.org/3/library/signal.html#signal.SIGFPE "signal.SIGFPE")
, [`SIGABRT`](https://docs.python.org/3/library/signal.html#signal.SIGABRT "signal.SIGABRT")
, [`SIGBUS`](https://docs.python.org/3/library/signal.html#signal.SIGBUS "signal.SIGBUS")
, and [`SIGILL`](https://docs.python.org/3/library/signal.html#signal.SIGILL "signal.SIGILL")
 signals. You can also enable them at startup by setting the [`PYTHONFAULTHANDLER`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER)
 environment variable or by using the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `faulthandler` command line option.

The fault handler is compatible with system fault handlers like Apport or the Windows fault handler. The module uses an alternative stack for signal handlers if the `sigaltstack()` function is available. This allows it to dump the traceback even on a stack overflow.

The fault handler is called on catastrophic cases and therefore can only use signal-safe functions (e.g. it cannot allocate memory on the heap). Because of this limitation traceback dumping is minimal compared to normal Python tracebacks:

*   Only ASCII is supported. The `backslashreplace` error handler is used on encoding.
    
*   Each string is limited to 500 characters.
    
*   Only the filename, the function name and the line number are displayed. (no source code)
    
*   It is limited to 100 frames per thread, and 100 threads (configurable via _max\_threads_).
    
*   The order is reversed: the most recent call is shown first.
    

By default, the Python traceback is written to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
. To see tracebacks, applications must be run in the terminal. A log file can alternatively be passed to [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable")
.

The module is implemented in C, so tracebacks can be dumped on a crash or when Python is deadlocked.

The [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
 calls [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable")
 at Python startup.

See also

Module [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")

Interactive source code debugger for Python programs.

Module [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.")

Standard interface to extract, format and print stack traces of Python programs.

Dumping the traceback[¶](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

faulthandler.dump\_traceback(_file\=sys.stderr_, _all\_threads\=True_, _\*_, _max\_threads\=100_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback "Link to this definition")

Dump the tracebacks of all threads into _file_. If _all\_threads_ is `False`, dump only the current thread. _max\_threads_ caps the number of threads dumped.

See also

[`traceback.print_tb()`](https://docs.python.org/3/library/traceback.html#traceback.print_tb "traceback.print_tb")
, which can be used to print a traceback object.

Changed in version 3.5: Added support for passing file descriptor to this function.

Changed in version 3.15: Added the _max\_threads_ keyword argument.

Dumping the C stack[¶](https://docs.python.org/3/library/faulthandler.html#dumping-the-c-stack "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Added in version 3.14.

faulthandler.dump\_c\_stack(_file\=sys.stderr_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_c_stack "Link to this definition")

Dump the C stack trace of the current thread into _file_.

If the Python build does not support it or the operating system does not provide a stack trace, then this prints an error in place of a dumped C stack.

### C Stack Compatibility[¶](https://docs.python.org/3/library/faulthandler.html#c-stack-compatibility "Link to this heading")

If the system does not support the C-level _[backtrace(3)](https://manpages.debian.org/backtrace(3))
_ or _[dladdr1(3)](https://manpages.debian.org/dladdr1(3))
_, then C stack dumps will not work. An error will be printed instead of the stack.

Additionally, some compilers do not support [CPython’s](https://docs.python.org/3/glossary.html#term-CPython)
 implementation of C stack dumps. As a result, a different error may be printed instead of the stack, even if the operating system supports dumping stacks.

Note

Dumping C stacks can be arbitrarily slow, depending on the DWARF level of the binaries in the call stack.

Fault handler state[¶](https://docs.python.org/3/library/faulthandler.html#fault-handler-state "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

faulthandler.enable(_file\=sys.stderr_, _all\_threads\=True_, _c\_stack\=True_, _\*_, _max\_threads\=100_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "Link to this definition")

Enable the fault handler: install handlers for the [`SIGSEGV`](https://docs.python.org/3/library/signal.html#signal.SIGSEGV "signal.SIGSEGV")
, [`SIGFPE`](https://docs.python.org/3/library/signal.html#signal.SIGFPE "signal.SIGFPE")
, [`SIGABRT`](https://docs.python.org/3/library/signal.html#signal.SIGABRT "signal.SIGABRT")
, [`SIGBUS`](https://docs.python.org/3/library/signal.html#signal.SIGBUS "signal.SIGBUS")
 and [`SIGILL`](https://docs.python.org/3/library/signal.html#signal.SIGILL "signal.SIGILL")
 signals to dump the Python traceback. If _all\_threads_ is `True`, produce tracebacks for every running thread. Otherwise, dump only the current thread.

The _file_ must be kept open until the fault handler is disabled: see [issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#faulthandler-fd)
.

If _c\_stack_ is `True`, then the C stack trace is printed after the Python traceback, unless the system does not support it. See [`dump_c_stack()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_c_stack "faulthandler.dump_c_stack")
 for more information on compatibility.

_max\_threads_ caps the number of threads dumped when a fatal signal fires.

Changed in version 3.5: Added support for passing file descriptor to this function.

Changed in version 3.6: On Windows, a handler for Windows exception is also installed.

Changed in version 3.10: The dump now mentions if a garbage collector collection is running if _all\_threads_ is true.

Changed in version 3.14: Only the current thread is dumped if the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
 is disabled to prevent the risk of data races.

Changed in version 3.14: The dump now displays the C stack trace if _c\_stack_ is true.

Changed in version 3.15: Added the _max\_threads_ keyword argument.

faulthandler.disable()[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.disable "Link to this definition")

Disable the fault handler: uninstall the signal handlers installed by [`enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable")
.

faulthandler.is\_enabled()[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.is_enabled "Link to this definition")

Check if the fault handler is enabled.

Dumping the tracebacks after a timeout[¶](https://docs.python.org/3/library/faulthandler.html#dumping-the-tracebacks-after-a-timeout "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

faulthandler.dump\_traceback\_later(_timeout_, _repeat\=False_, _file\=sys.stderr_, _exit\=False_, _\*_, _max\_threads\=100_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "Link to this definition")

Dump the tracebacks of all threads, after a timeout of _timeout_ seconds, or every _timeout_ seconds if _repeat_ is `True`. If _exit_ is `True`, call `_exit()` with status=1 after dumping the tracebacks. (Note `_exit()` exits the process immediately, which means it doesn’t do any cleanup like flushing file buffers.) If the function is called twice, the new call replaces previous parameters and resets the timeout. The timer has a sub-second resolution. _max\_threads_ caps the number of threads dumped.

The _file_ must be kept open until the traceback is dumped or [`cancel_dump_traceback_later()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.cancel_dump_traceback_later "faulthandler.cancel_dump_traceback_later")
 is called: see [issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#faulthandler-fd)
.

This function is implemented using a watchdog thread.

Changed in version 3.5: Added support for passing file descriptor to this function.

Changed in version 3.7: This function is now always available.

Changed in version 3.15: Added the _max\_threads_ keyword argument.

faulthandler.cancel\_dump\_traceback\_later()[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.cancel_dump_traceback_later "Link to this definition")

Cancel the last call to [`dump_traceback_later()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "faulthandler.dump_traceback_later")
.

Dumping the traceback on a user signal[¶](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback-on-a-user-signal "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

faulthandler.register(_signum_, _file\=sys.stderr_, _all\_threads\=True_, _chain\=False_, _\*_, _max\_threads\=100_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.register "Link to this definition")

Register a user signal: install a handler for the _signum_ signal to dump the traceback of all threads, or of the current thread if _all\_threads_ is `False`, into _file_. Call the previous handler if chain is `True`. _max\_threads_ caps the number of threads dumped.

The _file_ must be kept open until the signal is unregistered by [`unregister()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.unregister "faulthandler.unregister")
: see [issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#faulthandler-fd)
.

Not available on Windows.

Changed in version 3.5: Added support for passing file descriptor to this function.

Changed in version 3.15: Added the _max\_threads_ keyword argument.

faulthandler.unregister(_signum_)[¶](https://docs.python.org/3/library/faulthandler.html#faulthandler.unregister "Link to this definition")

Unregister a user signal: uninstall the handler of the _signum_ signal installed by [`register()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.register "faulthandler.register")
. Return `True` if the signal was registered, `False` otherwise.

Not available on Windows.

Issue with file descriptors[¶](https://docs.python.org/3/library/faulthandler.html#issue-with-file-descriptors "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

[`enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable")
, [`dump_traceback_later()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "faulthandler.dump_traceback_later")
 and [`register()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.register "faulthandler.register")
 keep the file descriptor of their _file_ argument. If the file is closed and its file descriptor is reused by a new file, or if [`os.dup2()`](https://docs.python.org/3/library/os.html#os.dup2 "os.dup2")
 is used to replace the file descriptor, the traceback will be written into a different file. Call these functions again each time that the file is replaced.

Example[¶](https://docs.python.org/3/library/faulthandler.html#example "Link to this heading")

-----------------------------------------------------------------------------------------------

Example of a segmentation fault on Linux with and without enabling the fault handler:

Copy

$ python \-c "import ctypes; ctypes.string\_at(0)"
Segmentation fault

$ python \-q \-X faulthandler
\>>> import ctypes
\>>> ctypes.string\_at(0)
Fatal Python error: Segmentation fault

Current thread 0x00007fb899f39700 (most recent call first):
  File "/opt/python/Lib/ctypes/\_\_init\_\_.py", line 486 in string\_at
  File "<stdin>", line 1 in <module>

Current thread's C stack trace (most recent call first):
  Binary file "/opt/python/python", at \_Py\_DumpStack+0x42 \[0x5b27f7d7147e\]
  Binary file "/opt/python/python", at +0x32dcbd \[0x5b27f7d85cbd\]
  Binary file "/opt/python/python", at +0x32df8a \[0x5b27f7d85f8a\]
  Binary file "/usr/lib/libc.so.6", at +0x3def0 \[0x77b73226bef0\]
  Binary file "/usr/lib/libc.so.6", at +0x17ef9c \[0x77b7323acf9c\]
  Binary file "/opt/python/build/lib.linux-x86\_64-3.15/\_ctypes.cpython-315d-x86\_64-linux-gnu.so", at +0xcdf6 \[0x77b7315dddf6\]
  Binary file "/usr/lib/libffi.so.8", at +0x7976 \[0x77b73158f976\]
  Binary file "/usr/lib/libffi.so.8", at +0x413c \[0x77b73158c13c\]
  Binary file "/usr/lib/libffi.so.8", at ffi\_call+0x12e \[0x77b73158ef0e\]
  Binary file "/opt/python/build/lib.linux-x86\_64-3.15/\_ctypes.cpython-315d-x86\_64-linux-gnu.so", at +0x15a33 \[0x77b7315e6a33\]
  Binary file "/opt/python/build/lib.linux-x86\_64-3.15/\_ctypes.cpython-315d-x86\_64-linux-gnu.so", at +0x164fa \[0x77b7315e74fa\]
  Binary file "/opt/python/build/lib.linux-x86\_64-3.15/\_ctypes.cpython-315d-x86\_64-linux-gnu.so", at +0xc624 \[0x77b7315dd624\]
  Binary file "/opt/python/python", at \_PyObject\_MakeTpCall+0xce \[0x5b27f7b73883\]
  Binary file "/opt/python/python", at +0x11bab6 \[0x5b27f7b73ab6\]
  Binary file "/opt/python/python", at PyObject\_Vectorcall+0x23 \[0x5b27f7b73b04\]
  Binary file "/opt/python/python", at \_PyEval\_EvalFrameDefault+0x490c \[0x5b27f7cbb302\]
  Binary file "/opt/python/python", at +0x2818e6 \[0x5b27f7cd98e6\]
  Binary file "/opt/python/python", at +0x281aab \[0x5b27f7cd9aab\]
  Binary file "/opt/python/python", at PyEval\_EvalCode+0xc5 \[0x5b27f7cd9ba3\]
  Binary file "/opt/python/python", at +0x255957 \[0x5b27f7cad957\]
  Binary file "/opt/python/python", at +0x255ab4 \[0x5b27f7cadab4\]
  Binary file "/opt/python/python", at \_PyEval\_EvalFrameDefault+0x6c3e \[0x5b27f7cbd634\]
  Binary file "/opt/python/python", at +0x2818e6 \[0x5b27f7cd98e6\]
  Binary file "/opt/python/python", at +0x281aab \[0x5b27f7cd9aab\]
  Binary file "/opt/python/python", at +0x11b6e1 \[0x5b27f7b736e1\]
  Binary file "/opt/python/python", at +0x11d348 \[0x5b27f7b75348\]
  Binary file "/opt/python/python", at +0x11d626 \[0x5b27f7b75626\]
  Binary file "/opt/python/python", at PyObject\_Call+0x20 \[0x5b27f7b7565e\]
  Binary file "/opt/python/python", at +0x32a67a \[0x5b27f7d8267a\]
  Binary file "/opt/python/python", at +0x32a7f8 \[0x5b27f7d827f8\]
  Binary file "/opt/python/python", at +0x32ac1b \[0x5b27f7d82c1b\]
  Binary file "/opt/python/python", at Py\_RunMain+0x31 \[0x5b27f7d82ebe\]
  <truncated rest of calls>
Segmentation fault

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html#)
    *   [Dumping the traceback](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback)
        
    *   [Dumping the C stack](https://docs.python.org/3/library/faulthandler.html#dumping-the-c-stack)
        *   [C Stack Compatibility](https://docs.python.org/3/library/faulthandler.html#c-stack-compatibility)
            
    *   [Fault handler state](https://docs.python.org/3/library/faulthandler.html#fault-handler-state)
        
    *   [Dumping the tracebacks after a timeout](https://docs.python.org/3/library/faulthandler.html#dumping-the-tracebacks-after-a-timeout)
        
    *   [Dumping the traceback on a user signal](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback-on-a-user-signal)
        
    *   [Issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#issue-with-file-descriptors)
        
    *   [Example](https://docs.python.org/3/library/faulthandler.html#example)
        

#### Previous topic

[`bdb` — Debugger framework](https://docs.python.org/3/library/bdb.html "previous chapter")

#### Next topic

[`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=faulthandler+%E2%80%94+Dump+the+Python+traceback&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffaulthandler.html&pagesource=library%2Ffaulthandler.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/faulthandler.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pdb.html "pdb — The Python Debugger")
     |
*   [previous](https://docs.python.org/3/library/bdb.html "bdb — Debugger framework")
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
*   [Debugging and profiling](https://docs.python.org/3/library/debug.html)
     »
*   [`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html)
    
*    
    
    |
*   Theme Auto Light Dark |