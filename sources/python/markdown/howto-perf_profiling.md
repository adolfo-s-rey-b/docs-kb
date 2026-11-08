### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/annotations.html "Annotations Best Practices")
     |
*   [previous](https://docs.python.org/3/howto/instrumentation.html "Instrumenting CPython with DTrace and SystemTap")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [Python support for the `perf map` compatible profilers](https://docs.python.org/3/howto/perf_profiling.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Python support for the `perf map` compatible profilers[¶](https://docs.python.org/3/howto/perf_profiling.html#python-support-for-the-perf-map-compatible-profilers "Link to this heading")

===========================================================================================================================================================================================

[The Linux perf profiler](https://perf.wiki.kernel.org/)
 and [samply](https://github.com/mstange/samply)
 are powerful tools that allow you to profile and obtain information about the performance of your application. Both tools have vibrant ecosystems that aid with the analysis of the data they produce.

The main problem with using these profilers with Python applications is that they only get information about native symbols, that is, the names of functions and procedures written in C. This means that the names and file names of Python functions in your code will not appear in the profiler output.

Since Python 3.12, the interpreter can run in a special mode that allows Python functions to appear in the output of compatible profilers. When this mode is enabled, the interpreter will interpose a small piece of code compiled on the fly before the execution of every Python function and it will teach the profiler the relationship between this piece of code and the associated Python function using [perf map files](https://docs.python.org/3/c-api/perfmaps.html)
.

Note

Support for profiling is available on Linux and macOS on select architectures. Perf is available on Linux, while samply can be used on both Linux and macOS. samply support on macOS is available starting from Python 3.15. Check the output of the `configure` build step or check the output of `python -m sysconfig | grep HAVE_PERF_TRAMPOLINE` to see if your system is supported.

For example, consider the following script:

Copy

def foo(n):
    result \= 0
    for \_ in range(n):
        result += 1
    return result

def bar(n):
    foo(n)

def baz(n):
    bar(n)

if \_\_name\_\_ \== "\_\_main\_\_":
    baz(1000000)

We can run `perf` to sample CPU stack traces at 9999 hertz:

Copy

$ perf record \-F 9999 \-g \-o perf.data python my\_script.py

Then we can use `perf report` to analyze the data:

Copy

$ perf report \--stdio \-n \-g

\# Children      Self       Samples  Command     Shared Object       Symbol
\# ........  ........  ............  ..........  ..................  ..........................................
#
    91.08%     0.00%             0  python.exe  python.exe          \[.\] \_start
            |
            ---\_start
            |
                --90.71%--\_\_libc\_start\_main
                        Py\_BytesMain
                        |
                        |--56.88%--pymain\_run\_python.constprop.0
                        |          |
                        |          |--56.13%--\_PyRun\_AnyFileObject
                        |          |          \_PyRun\_SimpleFileObject
                        |          |          |
                        |          |          |--55.02%--run\_mod
                        |          |          |          |
                        |          |          |           --54.65%--PyEval\_EvalCode
                        |          |          |                     \_PyEval\_EvalFrameDefault
                        |          |          |                     PyObject\_Vectorcall
                        |          |          |                     \_PyEval\_Vector
                        |          |          |                     \_PyEval\_EvalFrameDefault
                        |          |          |                     PyObject\_Vectorcall
                        |          |          |                     \_PyEval\_Vector
                        |          |          |                     \_PyEval\_EvalFrameDefault
                        |          |          |                     PyObject\_Vectorcall
                        |          |          |                     \_PyEval\_Vector
                        |          |          |                     |
                        |          |          |                     |--51.67%--\_PyEval\_EvalFrameDefault
                        |          |          |                     |          |
                        |          |          |                     |          |--11.52%--\_PyCompactLong\_Add
                        |          |          |                     |          |          |
                        |          |          |                     |          |          |--2.97%--\_PyObject\_Malloc
...

As you can see, the Python functions are not shown in the output, only `_PyEval_EvalFrameDefault` (the function that evaluates the Python bytecode) shows up. Unfortunately that’s not very useful because all Python functions use the same C function to evaluate bytecode so we cannot know which Python function corresponds to which bytecode-evaluating function.

Instead, if we run the same experiment with `perf` support enabled we get:

Copy

$ perf report \--stdio \-n \-g

\# Children      Self       Samples  Command     Shared Object       Symbol
\# ........  ........  ............  ..........  ..................  .....................................................................
#
    90.58%     0.36%             1  python.exe  python.exe          \[.\] \_start
            |
            ---\_start
            |
                --89.86%--\_\_libc\_start\_main
                        Py\_BytesMain
                        |
                        |--55.43%--pymain\_run\_python.constprop.0
                        |          |
                        |          |--54.71%--\_PyRun\_AnyFileObject
                        |          |          \_PyRun\_SimpleFileObject
                        |          |          |
                        |          |          |--53.62%--run\_mod
                        |          |          |          |
                        |          |          |           --53.26%--PyEval\_EvalCode
                        |          |          |                     py::<module>:/src/script.py
                        |          |          |                     \_PyEval\_EvalFrameDefault
                        |          |          |                     PyObject\_Vectorcall
                        |          |          |                     \_PyEval\_Vector
                        |          |          |                     py::baz:/src/script.py
                        |          |          |                     \_PyEval\_EvalFrameDefault
                        |          |          |                     PyObject\_Vectorcall
                        |          |          |                     \_PyEval\_Vector
                        |          |          |                     py::bar:/src/script.py
                        |          |          |                     \_PyEval\_EvalFrameDefault
                        |          |          |                     PyObject\_Vectorcall
                        |          |          |                     \_PyEval\_Vector
                        |          |          |                     py::foo:/src/script.py
                        |          |          |                     |
                        |          |          |                     |--51.81%--\_PyEval\_EvalFrameDefault
                        |          |          |                     |          |
                        |          |          |                     |          |--13.77%--\_PyCompactLong\_Add
                        |          |          |                     |          |          |
                        |          |          |                     |          |          |--3.26%--\_PyObject\_Malloc

Using the samply profiler[¶](https://docs.python.org/3/howto/perf_profiling.html#using-the-samply-profiler "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

samply is a modern profiler that can be used as an alternative to perf. It uses the same perf map files that Python generates, making it compatible with Python’s profiling support. samply is particularly useful on macOS where perf is not available.

To use samply with Python, first install it following the instructions at [https://github.com/mstange/samply](https://github.com/mstange/samply)
, then run:

Copy

$ samply record PYTHONPERFSUPPORT\=1 python my\_script.py

This will open a web interface where you can analyze the profiling data interactively. The advantage of samply is that it provides a modern web-based interface for analyzing profiling data and works on both Linux and macOS.

On macOS, samply support requires Python 3.15 or later. Also on macOS, samply can’t profile signed Python executables due to restrictions by macOS. You can profile with Python binaries that you’ve compiled yourself, or which are unsigned or locally-signed (such as anything installed by Homebrew). In order to attach to running processes on macOS, run `samply setup` once (and every time samply is updated) to self-sign the samply binary.

How to enable `perf` profiling support[¶](https://docs.python.org/3/howto/perf_profiling.html#how-to-enable-perf-profiling-support "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

`perf` profiling support can be enabled either from the start using the environment variable [`PYTHONPERFSUPPORT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPERFSUPPORT)
 or the [`-X perf`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 option, or dynamically using [`sys.activate_stack_trampoline()`](https://docs.python.org/3/library/sys.html#sys.activate_stack_trampoline "sys.activate_stack_trampoline")
 and [`sys.deactivate_stack_trampoline()`](https://docs.python.org/3/library/sys.html#sys.deactivate_stack_trampoline "sys.deactivate_stack_trampoline")
.

The `sys` functions take precedence over the `-X` option, the `-X` option takes precedence over the environment variable.

Example, using the environment variable:

Copy

$ PYTHONPERFSUPPORT\=1 perf record \-F 9999 \-g \-o perf.data python my\_script.py
$ perf report \-g \-i perf.data

Example, using the `-X` option:

Copy

$ perf record \-F 9999 \-g \-o perf.data python \-X perf my\_script.py
$ perf report \-g \-i perf.data

Example, using the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
 APIs in file `example.py`:

Copy

import sys

sys.activate\_stack\_trampoline("perf")
do\_profiled\_stuff()
sys.deactivate\_stack\_trampoline()

non\_profiled\_stuff()

…then:

Copy

$ perf record \-F 9999 \-g \-o perf.data python ./example.py
$ perf report \-g \-i perf.data

How to obtain the best results[¶](https://docs.python.org/3/howto/perf_profiling.html#how-to-obtain-the-best-results "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

For best results, keep frame pointers enabled. On supported GCC-compatible toolchains, CPython builds itself with `-fno-omit-frame-pointer` and similar flags (see [`--without-frame-pointers`](https://docs.python.org/3/using/configure.html#cmdoption-without-frame-pointers)
 for details). These flags allow profilers to unwind using only the frame pointer and not on DWARF debug information. This is because as the code that is interposed to allow `perf` support is dynamically generated it doesn’t have any DWARF debugging information available.

You can check if your system has been compiled with this flag by running:

Copy

$ python \-m sysconfig | grep 'no-omit-frame-pointer'

If you don’t see any output it means that your interpreter has not been compiled with frame pointers and therefore it may not be able to show Python functions in the output of `perf`.

How to work without frame pointers[¶](https://docs.python.org/3/howto/perf_profiling.html#how-to-work-without-frame-pointers "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

If you are working with a Python interpreter that has been compiled without frame pointers, you can still use the `perf` profiler, but the overhead will be a bit higher because Python needs to generate unwinding information for every Python function call on the fly. Additionally, `perf` will take more time to process the data because it will need to use the DWARF debugging information to unwind the stack and this is a slow process.

To enable this mode, you can use the environment variable [`PYTHON_PERF_JIT_SUPPORT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PERF_JIT_SUPPORT)
 or the [`-X perf_jit`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 option, which will enable the JIT mode for the `perf` profiler.

Note

Due to a bug in the `perf` tool, only `perf` versions higher than v6.8 will work with the JIT mode. The fix was also backported to the v6.7.2 version of the tool.

Note that when checking the version of the `perf` tool (which can be done by running `perf version`) you must take into account that some distros add some custom version numbers including a `-` character. This means that `perf 6.7-3` is not necessarily `perf 6.7.3`.

When using the perf JIT mode, you need an extra step before you can run `perf report`. You need to call the `perf inject` command to inject the JIT information into the `perf.data` file.:

Copy

$ perf record \-F 9999 \-g \-k 1 \--call-graph dwarf \-o perf.data python \-Xperf\_jit my\_script.py
$ perf inject \-i perf.data \--jit \--output perf.jit.data
$ perf report \-g \-i perf.jit.data

or using the environment variable:

Copy

$ PYTHON\_PERF\_JIT\_SUPPORT\=1 perf record \-F 9999 \-g \--call-graph dwarf \-o perf.data python my\_script.py
$ perf inject \-i perf.data \--jit \--output perf.jit.data
$ perf report \-g \-i perf.jit.data

`perf inject --jit` command will read `perf.data`, automatically pick up the perf dump file that Python creates (in `/tmp/jit-$PID.dump`), and then create `perf.jit.data` which merges all the JIT information together. It should also create a lot of `jitted-XXXX-N.so` files in the current directory which are ELF images for all the JIT trampolines that were created by Python.

Warning

When using `--call-graph dwarf`, the `perf` tool will take snapshots of the stack of the process being profiled and save the information in the `perf.data` file. By default, the size of the stack dump is 8192 bytes, but you can change the size by passing it after a comma like `--call-graph dwarf,16384`.

The size of the stack dump is important because if the size is too small `perf` will not be able to unwind the stack and the output will be incomplete. On the other hand, if the size is too big, then `perf` won’t be able to sample the process as frequently as it would like as the overhead will be higher.

The stack size is particularly important when profiling Python code compiled with low optimization levels (like `-O0`), as these builds tend to have larger stack frames. If you are compiling Python with `-O0` and not seeing Python functions in your profiling output, try increasing the stack dump size to 65528 bytes (the maximum):

Copy

$ perf record \-F 9999 \-g \-k 1 \--call-graph dwarf,65528 \-o perf.data python \-Xperf\_jit my\_script.py

Different compilation flags can significantly impact stack sizes:

*   Builds with `-O0` typically have much larger stack frames than those with `-O1` or higher
    
*   Adding optimizations (`-O1`, `-O2`, etc.) typically reduces stack size
    
*   Frame pointers (`-fno-omit-frame-pointer`) generally provide more reliable stack unwinding
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Python support for the `perf map` compatible profilers](https://docs.python.org/3/howto/perf_profiling.html#)
    *   [Using the samply profiler](https://docs.python.org/3/howto/perf_profiling.html#using-the-samply-profiler)
        
    *   [How to enable `perf` profiling support](https://docs.python.org/3/howto/perf_profiling.html#how-to-enable-perf-profiling-support)
        
    *   [How to obtain the best results](https://docs.python.org/3/howto/perf_profiling.html#how-to-obtain-the-best-results)
        
    *   [How to work without frame pointers](https://docs.python.org/3/howto/perf_profiling.html#how-to-work-without-frame-pointers)
        

#### Previous topic

[Instrumenting CPython with DTrace and SystemTap](https://docs.python.org/3/howto/instrumentation.html "previous chapter")

#### Next topic

[Annotations Best Practices](https://docs.python.org/3/howto/annotations.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Python+support+for+the+perf+map+compatible+profilers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fhowto%2Fperf_profiling.html&pagesource=howto%2Fperf_profiling.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/howto/perf_profiling.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/annotations.html "Annotations Best Practices")
     |
*   [previous](https://docs.python.org/3/howto/instrumentation.html "Instrumenting CPython with DTrace and SystemTap")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [Python support for the `perf map` compatible profilers](https://docs.python.org/3/howto/perf_profiling.html)
    
*    
    
    |
*   Theme Auto Light Dark |