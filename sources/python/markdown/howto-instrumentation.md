### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/perf_profiling.html "Python support for the perf map compatible profilers")
     |
*   [previous](https://docs.python.org/3/howto/ipaddress.html "An introduction to the ipaddress module")
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
*   [Instrumenting CPython with DTrace and SystemTap](https://docs.python.org/3/howto/instrumentation.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Instrumenting CPython with DTrace and SystemTap[¶](https://docs.python.org/3/howto/instrumentation.html#instrumenting-cpython-with-dtrace-and-systemtap "Link to this heading")

================================================================================================================================================================================

DTrace and SystemTap are monitoring tools, each providing a way to inspect what the processes on a computer system are doing. They both use domain-specific languages allowing a user to write scripts which:

*   filter which processes are to be observed
    
*   gather data from the processes of interest
    
*   generate reports on the data
    

As of Python 3.6, CPython can be built with embedded “markers”, also known as “probes”, that can be observed by a DTrace or SystemTap script, making it easier to monitor what the CPython processes on a system are doing.

**CPython implementation detail:** DTrace markers are implementation details of the CPython interpreter. No guarantees are made about probe compatibility between versions of CPython. DTrace scripts can stop working or work incorrectly without warning when changing CPython versions.

Enabling the static markers[¶](https://docs.python.org/3/howto/instrumentation.html#enabling-the-static-markers "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

macOS comes with built-in support for DTrace. On Linux, in order to build CPython with the embedded markers for SystemTap, the SystemTap development tools must be installed.

On a Linux machine, this can be done via:

Copy

$ yum install systemtap-sdt-devel

or:

Copy

$ sudo apt-get install systemtap-sdt-dev

CPython must then be [`configured with the --with-dtrace option`](https://docs.python.org/3/using/configure.html#cmdoption-with-dtrace)
:

checking for --with-dtrace... yes

On macOS, you can list available DTrace probes by running a Python process in the background and listing all probes made available by the Python provider:

Copy

$ python3.6 \-q &
$ sudo dtrace \-l \-P python$!  \# or: dtrace -l -m python3.6

   ID   PROVIDER            MODULE                          FUNCTION NAME
29564 python18035        python3.6          \_PyEval\_EvalFrameDefault function-entry
29565 python18035        python3.6             dtrace\_function\_entry function-entry
29566 python18035        python3.6          \_PyEval\_EvalFrameDefault function-return
29567 python18035        python3.6            dtrace\_function\_return function-return
29568 python18035        python3.6                           collect gc-done
29569 python18035        python3.6                           collect gc-start
29570 python18035        python3.6          \_PyEval\_EvalFrameDefault line
29571 python18035        python3.6                 maybe\_dtrace\_line line

On Linux, you can verify if the SystemTap static markers are present in the built binary by seeing if it contains a “.note.stapsdt” section.

Copy

$ readelf \-S ./python | grep .note.stapsdt
\[30\] .note.stapsdt        NOTE         0000000000000000 00308d78

If you’ve built Python as a shared library (with the [`--enable-shared`](https://docs.python.org/3/using/configure.html#cmdoption-enable-shared)
 configure option), you need to look instead within the shared library. For example:

Copy

$ readelf \-S libpython3.3dm.so.1.0 | grep .note.stapsdt
\[29\] .note.stapsdt        NOTE         0000000000000000 00365b68

Sufficiently modern readelf can print the metadata:

Copy

$ readelf \-n ./python

Displaying notes found at file offset 0x00000254 with length 0x00000020:
    Owner                 Data size          Description
    GNU                  0x00000010          NT\_GNU\_ABI\_TAG (ABI version tag)
        OS: Linux, ABI: 2.6.32

Displaying notes found at file offset 0x00000274 with length 0x00000024:
    Owner                 Data size          Description
    GNU                  0x00000014          NT\_GNU\_BUILD\_ID (unique build ID bitstring)
        Build ID: df924a2b08a7e89f6e11251d4602022977af2670

Displaying notes found at file offset 0x002d6c30 with length 0x00000144:
    Owner                 Data size          Description
    stapsdt              0x00000031          NT\_STAPSDT (SystemTap probe descriptors)
        Provider: python
        Name: gc\_\_start
        Location: 0x00000000004371c3, Base: 0x0000000000630ce2, Semaphore: 0x00000000008d6bf6
        Arguments: -4@%ebx
    stapsdt              0x00000030          NT\_STAPSDT (SystemTap probe descriptors)
        Provider: python
        Name: gc\_\_done
        Location: 0x00000000004374e1, Base: 0x0000000000630ce2, Semaphore: 0x00000000008d6bf8
        Arguments: -8@%rax
    stapsdt              0x00000045          NT\_STAPSDT (SystemTap probe descriptors)
        Provider: python
        Name: function\_\_entry
        Location: 0x000000000053db6c, Base: 0x0000000000630ce2, Semaphore: 0x00000000008d6be8
        Arguments: 8@%rbp 8@%r12 -4@%eax
    stapsdt              0x00000046          NT\_STAPSDT (SystemTap probe descriptors)
        Provider: python
        Name: function\_\_return
        Location: 0x000000000053dba8, Base: 0x0000000000630ce2, Semaphore: 0x00000000008d6bea
        Arguments: 8@%rbp 8@%r12 -4@%eax

The above metadata contains information for SystemTap describing how it can patch strategically placed machine code instructions to enable the tracing hooks used by a SystemTap script.

Static DTrace probes[¶](https://docs.python.org/3/howto/instrumentation.html#static-dtrace-probes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

The following example DTrace script can be used to show the call/return hierarchy of a Python script, only tracing within the invocation of a function called “start”. In other words, import-time function invocations are not going to be listed:

self int indent;

python$target:::function-entry
/copyinstr(arg1) == "start"/
{
        self->trace = 1;
}

python$target:::function-entry
/self->trace/
{
        printf("%d\\t%\*s:", timestamp, 15, probename);
        printf("%\*s", self->indent, "");
        printf("%s:%s:%d\\n", basename(copyinstr(arg0)), copyinstr(arg1), arg2);
        self->indent++;
}

python$target:::function-return
/self->trace/
{
        self->indent--;
        printf("%d\\t%\*s:", timestamp, 15, probename);
        printf("%\*s", self->indent, "");
        printf("%s:%s:%d\\n", basename(copyinstr(arg0)), copyinstr(arg1), arg2);
}

python$target:::function-return
/copyinstr(arg1) == "start"/
{
        self->trace = 0;
}

It can be invoked like this:

Copy

$ sudo dtrace \-q \-s call\_stack.d \-c "python3.6 script.py"

The output looks like this:

156641360502280  function-entry:call\_stack.py:start:23
156641360518804  function-entry: call\_stack.py:function\_1:1
156641360532797  function-entry:  call\_stack.py:function\_3:9
156641360546807 function-return:  call\_stack.py:function\_3:10
156641360563367 function-return: call\_stack.py:function\_1:2
156641360578365  function-entry: call\_stack.py:function\_2:5
156641360591757  function-entry:  call\_stack.py:function\_1:1
156641360605556  function-entry:   call\_stack.py:function\_3:9
156641360617482 function-return:   call\_stack.py:function\_3:10
156641360629814 function-return:  call\_stack.py:function\_1:2
156641360642285 function-return: call\_stack.py:function\_2:6
156641360656770  function-entry: call\_stack.py:function\_3:9
156641360669707 function-return: call\_stack.py:function\_3:10
156641360687853  function-entry: call\_stack.py:function\_4:13
156641360700719 function-return: call\_stack.py:function\_4:14
156641360719640  function-entry: call\_stack.py:function\_5:18
156641360732567 function-return: call\_stack.py:function\_5:21
156641360747370 function-return:call\_stack.py:start:28

Static SystemTap markers[¶](https://docs.python.org/3/howto/instrumentation.html#static-systemtap-markers "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The low-level way to use the SystemTap integration is to use the static markers directly. This requires you to explicitly state the binary file containing them.

For example, this SystemTap script can be used to show the call/return hierarchy of a Python script:

probe process("python").mark("function\_\_entry") {
     filename = user\_string($arg1);
     funcname = user\_string($arg2);
     lineno = $arg3;

     printf("%s => %s in %s:%d\\\\n",
            thread\_indent(1), funcname, filename, lineno);
}

probe process("python").mark("function\_\_return") {
    filename = user\_string($arg1);
    funcname = user\_string($arg2);
    lineno = $arg3;

    printf("%s <= %s in %s:%d\\\\n",
           thread\_indent(-1), funcname, filename, lineno);
}

It can be invoked like this:

Copy

$ stap \\
  show-call-hierarchy.stp \\
  \-c "./python test.py"

The output looks like this:

11408 python(8274):        => \_\_contains\_\_ in Lib/\_abcoll.py:362
11414 python(8274):         => \_\_getitem\_\_ in Lib/os.py:425
11418 python(8274):          => encode in Lib/os.py:490
11424 python(8274):          <= encode in Lib/os.py:493
11428 python(8274):         <= \_\_getitem\_\_ in Lib/os.py:426
11433 python(8274):        <= \_\_contains\_\_ in Lib/\_abcoll.py:366

where the columns are:

*   time in microseconds since start of script
    
*   name of executable
    
*   PID of process
    

and the remainder indicates the call/return hierarchy as the script executes.

For a [`--enable-shared`](https://docs.python.org/3/using/configure.html#cmdoption-enable-shared)
 build of CPython, the markers are contained within the libpython shared library, and the probe’s dotted path needs to reflect this. For example, this line from the above example:

probe process("python").mark("function\_\_entry") {

should instead read:

probe process("python").library("libpython3.6dm.so.1.0").mark("function\_\_entry") {

(assuming a [debug build](https://docs.python.org/3/using/configure.html#debug-build)
 of CPython 3.6)

Available static markers[¶](https://docs.python.org/3/howto/instrumentation.html#available-static-markers "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

function\_\_entry(str filename, str funcname, int lineno)

This marker indicates that execution of a Python function has begun. It is only triggered for pure-Python (bytecode) functions.

The filename, function name, and line number are provided back to the tracing script as positional arguments, which must be accessed using `$arg1`, `$arg2`, `$arg3`:

> *   `$arg1` : `(const char *)` filename, accessible using `user_string($arg1)`
>     
> *   `$arg2` : `(const char *)` function name, accessible using `user_string($arg2)`
>     
> *   `$arg3` : `int` line number
>     

function\_\_return(str filename, str funcname, int lineno)

This marker is the converse of `function__entry()`, and indicates that execution of a Python function has ended (either via `return`, or via an exception). It is only triggered for pure-Python (bytecode) functions.

The arguments are the same as for `function__entry()`

line(str filename, str funcname, int lineno)

This marker indicates a Python line is about to be executed. It is the equivalent of line-by-line tracing with a Python profiler. It is not triggered within C functions.

The arguments are the same as for `function__entry()`.

gc\_\_start(int generation)

Fires when the Python interpreter starts a garbage collection cycle. `arg0` is the generation to scan, like [`gc.collect()`](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect")
.

gc\_\_done(long collected)

Fires when the Python interpreter finishes a garbage collection cycle. `arg0` is the number of collected objects.

import\_\_find\_\_load\_\_start(str modulename)

Fires before [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 attempts to find and load the module. `arg0` is the module name.

Added in version 3.7.

import\_\_find\_\_load\_\_done(str modulename, int found)

Fires after [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
’s find\_and\_load function is called. `arg0` is the module name, `arg1` indicates if module was successfully loaded.

Added in version 3.7.

audit(str event, void \*tuple)

Fires when [`sys.audit()`](https://docs.python.org/3/library/sys.html#sys.audit "sys.audit")
 or [`PySys_Audit()`](https://docs.python.org/3/c-api/sys.html#c.PySys_Audit "PySys_Audit")
 is called. `arg0` is the event name as C string, `arg1` is a [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 pointer to a tuple object.

Added in version 3.8.

### C Entry Points[¶](https://docs.python.org/3/howto/instrumentation.html#c-entry-points "Link to this heading")

To simplify triggering of DTrace markers, Python’s C API comes with a number of helper functions that mirror each static marker. On builds of Python without DTrace enabled, these do nothing.

In general, it is not necessary to call these yourself, as Python will do it for you.

  
| C API Function | Static Marker | Notes |
| --- | --- | --- |
| void PyDTrace\_LINE(const char \*arg0, const char \*arg1, int arg2)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_LINE "Link to this definition") | `line()` |     |
| void PyDTrace\_FUNCTION\_ENTRY(const char \*arg0, const char \*arg1, int arg2)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_FUNCTION_ENTRY "Link to this definition") | `function__entry()` |     |
| void PyDTrace\_FUNCTION\_RETURN(const char \*arg0, const char \*arg1, int arg2)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_FUNCTION_RETURN "Link to this definition") | `function__return()` |     |
| void PyDTrace\_GC\_START(int arg0)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_GC_START "Link to this definition") | `gc__start()` |     |
| void PyDTrace\_GC\_DONE([Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")<br> arg0)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_GC_DONE "Link to this definition") | `gc__done()` |     |
| void PyDTrace\_INSTANCE\_NEW\_START(int arg0)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_INSTANCE_NEW_START "Link to this definition") | `instance__new__start()` | Not used by Python |
| void PyDTrace\_INSTANCE\_NEW\_DONE(int arg0)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_INSTANCE_NEW_DONE "Link to this definition") | `instance__new__done()` | Not used by Python |
| void PyDTrace\_INSTANCE\_DELETE\_START(int arg0)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_INSTANCE_DELETE_START "Link to this definition") | `instance__delete__start()` | Not used by Python |
| void PyDTrace\_INSTANCE\_DELETE\_DONE(int arg0)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_INSTANCE_DELETE_DONE "Link to this definition") | `instance__delete__done()` | Not used by Python |
| void PyDTrace\_IMPORT\_FIND\_LOAD\_START(const char \*arg0)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_IMPORT_FIND_LOAD_START "Link to this definition") | `import__find__load__start()` |     |
| void PyDTrace\_IMPORT\_FIND\_LOAD\_DONE(const char \*arg0, int arg1)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_IMPORT_FIND_LOAD_DONE "Link to this definition") | `import__find__load__done()` |     |
| void PyDTrace\_AUDIT(const char \*arg0, void \*arg1)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_AUDIT "Link to this definition") | `audit()` |     |

### C Probing Checks[¶](https://docs.python.org/3/howto/instrumentation.html#c-probing-checks "Link to this heading")

int PyDTrace\_LINE\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_LINE_ENABLED "Link to this definition")
  

int PyDTrace\_FUNCTION\_ENTRY\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_FUNCTION_ENTRY_ENABLED "Link to this definition")
  

int PyDTrace\_FUNCTION\_RETURN\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_FUNCTION_RETURN_ENABLED "Link to this definition")
  

int PyDTrace\_GC\_START\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_GC_START_ENABLED "Link to this definition")
  

int PyDTrace\_GC\_DONE\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_GC_DONE_ENABLED "Link to this definition")
  

int PyDTrace\_INSTANCE\_NEW\_START\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_INSTANCE_NEW_START_ENABLED "Link to this definition")
  

int PyDTrace\_INSTANCE\_NEW\_DONE\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_INSTANCE_NEW_DONE_ENABLED "Link to this definition")
  

int PyDTrace\_INSTANCE\_DELETE\_START\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_INSTANCE_DELETE_START_ENABLED "Link to this definition")
  

int PyDTrace\_INSTANCE\_DELETE\_DONE\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_INSTANCE_DELETE_DONE_ENABLED "Link to this definition")
  

int PyDTrace\_IMPORT\_FIND\_LOAD\_START\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_IMPORT_FIND_LOAD_START_ENABLED "Link to this definition")
  

int PyDTrace\_IMPORT\_FIND\_LOAD\_DONE\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_IMPORT_FIND_LOAD_DONE_ENABLED "Link to this definition")
  

int PyDTrace\_AUDIT\_ENABLED(void)[¶](https://docs.python.org/3/howto/instrumentation.html#c.PyDTrace_AUDIT_ENABLED "Link to this definition")
  

All calls to `PyDTrace` functions must be guarded by a call to one of these functions. This allows Python to minimize performance impact when probing is disabled.

On builds without DTrace enabled, these functions do nothing and return `0`.

SystemTap Tapsets[¶](https://docs.python.org/3/howto/instrumentation.html#systemtap-tapsets "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

The higher-level way to use the SystemTap integration is to use a “tapset”: SystemTap’s equivalent of a library, which hides some of the lower-level details of the static markers.

Here is a tapset file, based on a non-shared build of CPython:

/\*
   Provide a higher-level wrapping around the function\_\_entry and
   function\_\_return markers:
 \*/
probe python.function.entry = process("python").mark("function\_\_entry")
{
    filename = user\_string($arg1);
    funcname = user\_string($arg2);
    lineno = $arg3;
    frameptr = $arg4
}
probe python.function.return = process("python").mark("function\_\_return")
{
    filename = user\_string($arg1);
    funcname = user\_string($arg2);
    lineno = $arg3;
    frameptr = $arg4
}

If this file is installed in SystemTap’s tapset directory (e.g. `/usr/share/systemtap/tapset`), then these additional probepoints become available:

python.function.entry(str filename, str funcname, int lineno, frameptr)

This probe point indicates that execution of a Python function has begun. It is only triggered for pure-Python (bytecode) functions.

python.function.return(str filename, str funcname, int lineno, frameptr)

This probe point is the converse of `python.function.entry`, and indicates that execution of a Python function has ended (either via `return`, or via an exception). It is only triggered for pure-Python (bytecode) functions.

Examples[¶](https://docs.python.org/3/howto/instrumentation.html#examples "Link to this heading")

--------------------------------------------------------------------------------------------------

This SystemTap script uses the tapset above to more cleanly implement the example given above of tracing the Python function-call hierarchy, without needing to directly name the static markers:

probe python.function.entry
{
  printf("%s => %s in %s:%d\\n",
         thread\_indent(1), funcname, filename, lineno);
}

probe python.function.return
{
  printf("%s <= %s in %s:%d\\n",
         thread\_indent(-1), funcname, filename, lineno);
}

The following script uses the tapset above to provide a top-like view of all running CPython code, showing the top 20 most frequently entered bytecode frames, each second, across the whole system:

global fn\_calls;

probe python.function.entry
{
    fn\_calls\[pid(), filename, funcname, lineno\] += 1;
}

probe timer.ms(1000) {
    printf("\\033\[2J\\033\[1;1H") /\* clear screen \*/\
    printf("%6s %80s %6s %30s %6s\\n",\
           "PID", "FILENAME", "LINE", "FUNCTION", "CALLS")\
    foreach (\[pid, filename, funcname, lineno\] in fn\_calls- limit 20) {\
        printf("%6d %80s %6d %30s %6d\\n",\
            pid, filename, lineno, funcname,\
            fn\_calls\[pid, filename, funcname, lineno\]);\
    }\
    delete fn\_calls;\
}\
\
### [Table of Contents](https://docs.python.org/3/contents.html)\
\
*   [Instrumenting CPython with DTrace and SystemTap](https://docs.python.org/3/howto/instrumentation.html#)\
    *   [Enabling the static markers](https://docs.python.org/3/howto/instrumentation.html#enabling-the-static-markers)\
        \
    *   [Static DTrace probes](https://docs.python.org/3/howto/instrumentation.html#static-dtrace-probes)\
        \
    *   [Static SystemTap markers](https://docs.python.org/3/howto/instrumentation.html#static-systemtap-markers)\
        \
    *   [Available static markers](https://docs.python.org/3/howto/instrumentation.html#available-static-markers)\
        *   [C Entry Points](https://docs.python.org/3/howto/instrumentation.html#c-entry-points)\
            \
        *   [C Probing Checks](https://docs.python.org/3/howto/instrumentation.html#c-probing-checks)\
            \
    *   [SystemTap Tapsets](https://docs.python.org/3/howto/instrumentation.html#systemtap-tapsets)\
        \
    *   [Examples](https://docs.python.org/3/howto/instrumentation.html#examples)\
        \
\
#### Previous topic\
\
[An introduction to the ipaddress module](https://docs.python.org/3/howto/ipaddress.html "previous chapter")\
\
#### Next topic\
\
[Python support for the `perf map` compatible profilers](https://docs.python.org/3/howto/perf_profiling.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Instrumenting+CPython+with+DTrace+and+SystemTap&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fhowto%2Finstrumentation.html&pagesource=howto%2Finstrumentation.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/howto/instrumentation.rst?plain=1)\
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
*   [next](https://docs.python.org/3/howto/perf_profiling.html "Python support for the perf map compatible profilers")\
     |\
*   [previous](https://docs.python.org/3/howto/ipaddress.html "An introduction to the ipaddress module")\
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
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)\
     »\
*   [Instrumenting CPython with DTrace and SystemTap](https://docs.python.org/3/howto/instrumentation.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |