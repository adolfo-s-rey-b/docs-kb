### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/init_config.html "Python Initialization Configuration")
     |
*   [previous](https://docs.python.org/3/c-api/subinterpreters.html "Multiple interpreters in a Python process")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Profiling and tracing](https://docs.python.org/3/c-api/profiling.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Profiling and tracing[¶](https://docs.python.org/3/c-api/profiling.html#profiling-and-tracing "Link to this heading")

======================================================================================================================

The Python interpreter provides some low-level support for attaching profiling and execution tracing facilities. These are used for profiling, debugging, and coverage analysis tools.

This C interface allows the profiling or tracing code to avoid the overhead of calling through Python-level callable objects, making a direct C function call instead. The essential attributes of the facility have not changed; the interface allows trace functions to be installed per-thread, and the basic events reported to the trace function are the same as had been reported to the Python-level trace functions in previous versions.

typedef int (\*Py\_tracefunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, [PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame, int what, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*arg)[¶](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Link to this definition")
  

The type of the trace function registered using [`PyEval_SetProfile()`](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetProfile "PyEval_SetProfile")
 and [`PyEval_SetTrace()`](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetTrace "PyEval_SetTrace")
. The first parameter is the object passed to the registration function as _obj_, _frame_ is the frame object to which the event pertains, _what_ is one of the constants [`PyTrace_CALL`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_CALL "PyTrace_CALL")
, [`PyTrace_EXCEPTION`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_EXCEPTION "PyTrace_EXCEPTION")
, [`PyTrace_LINE`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_LINE "PyTrace_LINE")
, [`PyTrace_RETURN`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_RETURN "PyTrace_RETURN")
, [`PyTrace_C_CALL`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_CALL "PyTrace_C_CALL")
, [`PyTrace_C_EXCEPTION`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_EXCEPTION "PyTrace_C_EXCEPTION")
, [`PyTrace_C_RETURN`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_RETURN "PyTrace_C_RETURN")
, or [`PyTrace_OPCODE`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_OPCODE "PyTrace_OPCODE")
, and _arg_ depends on the value of _what_:

| Value of _what_ | Meaning of _arg_ |
| --- | --- |
| [`PyTrace_CALL`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_CALL "PyTrace_CALL") | Always [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "Py_None")<br>. |
| [`PyTrace_EXCEPTION`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_EXCEPTION "PyTrace_EXCEPTION") | Exception information as returned by [`sys.exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info")<br>. |
| [`PyTrace_LINE`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_LINE "PyTrace_LINE") | Always [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "Py_None")<br>. |
| [`PyTrace_RETURN`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_RETURN "PyTrace_RETURN") | Value being returned to the caller, or `NULL` if caused by an exception. |
| [`PyTrace_C_CALL`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_CALL "PyTrace_C_CALL") | Function object being called. |
| [`PyTrace_C_EXCEPTION`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_EXCEPTION "PyTrace_C_EXCEPTION") | Function object being called. |
| [`PyTrace_C_RETURN`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_RETURN "PyTrace_C_RETURN") | Function object being called. |
| [`PyTrace_OPCODE`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_OPCODE "PyTrace_OPCODE") | Always [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "Py_None")<br>. |

int PyTrace\_CALL[¶](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_CALL "Link to this definition")
  

The value of the _what_ parameter to a [`Py_tracefunc`](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 function when a new call to a function or method is being reported, or a new entry into a generator. Note that the creation of the iterator for a generator function is not reported as there is no control transfer to the Python bytecode in the corresponding frame.

int PyTrace\_EXCEPTION[¶](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_EXCEPTION "Link to this definition")
  

The value of the _what_ parameter to a [`Py_tracefunc`](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 function when an exception has been raised. The callback function is called with this value for _what_ when after any bytecode is processed after which the exception becomes set within the frame being executed. The effect of this is that as exception propagation causes the Python stack to unwind, the callback is called upon return to each frame as the exception propagates. Only trace functions receive these events; they are not needed by the profiler.

int PyTrace\_LINE[¶](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_LINE "Link to this definition")
  

The value passed as the _what_ parameter to a [`Py_tracefunc`](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 function (but not a profiling function) when a line-number event is being reported. It may be disabled for a frame by setting [`f_trace_lines`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_lines "frame.f_trace_lines")
 to _0_ on that frame.

int PyTrace\_RETURN[¶](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_RETURN "Link to this definition")
  

The value for the _what_ parameter to [`Py_tracefunc`](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 functions when a call is about to return.

int PyTrace\_C\_CALL[¶](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_CALL "Link to this definition")
  

The value for the _what_ parameter to [`Py_tracefunc`](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 functions when a C function is about to be called.

int PyTrace\_C\_EXCEPTION[¶](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_EXCEPTION "Link to this definition")
  

The value for the _what_ parameter to [`Py_tracefunc`](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 functions when a C function has raised an exception.

int PyTrace\_C\_RETURN[¶](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_RETURN "Link to this definition")
  

The value for the _what_ parameter to [`Py_tracefunc`](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 functions when a C function has returned.

int PyTrace\_OPCODE[¶](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_OPCODE "Link to this definition")
  

The value for the _what_ parameter to [`Py_tracefunc`](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 functions (but not profiling functions) when a new opcode is about to be executed. This event is not emitted by default: it must be explicitly requested by setting [`f_trace_opcodes`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_opcodes "frame.f_trace_opcodes")
 to _1_ on the frame.

void PyEval\_SetProfile([Py\_tracefunc](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 func, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetProfile "Link to this definition")
  

Set the profiler function to _func_. The _obj_ parameter is passed to the function as its first parameter, and may be any Python object, or `NULL`. If the profile function needs to maintain state, using a different value for _obj_ for each thread provides a convenient and thread-safe place to store it. The profile function is called for all monitored events except [`PyTrace_LINE`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_LINE "PyTrace_LINE")
 [`PyTrace_OPCODE`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_OPCODE "PyTrace_OPCODE")
 and [`PyTrace_EXCEPTION`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_EXCEPTION "PyTrace_EXCEPTION")
.

See also the [`sys.setprofile()`](https://docs.python.org/3/library/sys.html#sys.setprofile "sys.setprofile")
 function.

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

void PyEval\_SetProfileAllThreads([Py\_tracefunc](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 func, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetProfileAllThreads "Link to this definition")
  

Like [`PyEval_SetProfile()`](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetProfile "PyEval_SetProfile")
 but sets the profile function in all running threads belonging to the current interpreter instead of the setting it only on the current thread.

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

As [`PyEval_SetProfile()`](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetProfile "PyEval_SetProfile")
, this function ignores any exceptions raised while setting the profile functions in all threads.

Added in version 3.12.

void PyEval\_SetTrace([Py\_tracefunc](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 func, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetTrace "Link to this definition")
  

Set the tracing function to _func_. This is similar to [`PyEval_SetProfile()`](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetProfile "PyEval_SetProfile")
, except the tracing function does receive line-number events and per-opcode events, but does not receive any event related to C function objects being called. Any trace function registered using [`PyEval_SetTrace()`](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetTrace "PyEval_SetTrace")
 will not receive [`PyTrace_C_CALL`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_CALL "PyTrace_C_CALL")
, [`PyTrace_C_EXCEPTION`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_EXCEPTION "PyTrace_C_EXCEPTION")
 or [`PyTrace_C_RETURN`](https://docs.python.org/3/c-api/profiling.html#c.PyTrace_C_RETURN "PyTrace_C_RETURN")
 as a value for the _what_ parameter.

See also the [`sys.settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace")
 function.

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

void PyEval\_SetTraceAllThreads([Py\_tracefunc](https://docs.python.org/3/c-api/profiling.html#c.Py_tracefunc "Py_tracefunc")
 func, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetTraceAllThreads "Link to this definition")
  

Like [`PyEval_SetTrace()`](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetTrace "PyEval_SetTrace")
 but sets the tracing function in all running threads belonging to the current interpreter instead of the setting it only on the current thread.

The caller must have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

As [`PyEval_SetTrace()`](https://docs.python.org/3/c-api/profiling.html#c.PyEval_SetTrace "PyEval_SetTrace")
, this function ignores any exceptions raised while setting the trace functions in all threads.

Added in version 3.12.

Reference tracing[¶](https://docs.python.org/3/c-api/profiling.html#reference-tracing "Link to this heading")

==============================================================================================================

Added in version 3.13.

typedef int (\*PyRefTracer)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, int event, void \*data)[¶](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer "Link to this definition")
  

The type of the trace function registered using [`PyRefTracer_SetTracer()`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_SetTracer "PyRefTracer_SetTracer")
. The first parameter is a Python object that has been just created (when **event** is set to [`PyRefTracer_CREATE`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_CREATE "PyRefTracer_CREATE")
) or about to be destroyed (when **event** is set to [`PyRefTracer_DESTROY`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_DESTROY "PyRefTracer_DESTROY")
). The **data** argument is the opaque pointer that was provided when `PyRefTracer_SetTracer()` was called.

If a new tracing function is registered replacing the current one, a call to the trace function will be made with the object set to **NULL** and **event** set to [`PyRefTracer_TRACKER_REMOVED`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_TRACKER_REMOVED "PyRefTracer_TRACKER_REMOVED")
. This will happen just before the new function is registered.

Added in version 3.13.

int PyRefTracer\_CREATE[¶](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_CREATE "Link to this definition")
  

The value for the _event_ parameter to [`PyRefTracer`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer "PyRefTracer")
 functions when a Python object has been created.

int PyRefTracer\_DESTROY[¶](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_DESTROY "Link to this definition")
  

The value for the _event_ parameter to [`PyRefTracer`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer "PyRefTracer")
 functions when a Python object has been destroyed.

int PyRefTracer\_TRACKER\_REMOVED[¶](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_TRACKER_REMOVED "Link to this definition")
  

The value for the _event_ parameter to [`PyRefTracer`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer "PyRefTracer")
 functions when the current tracer is about to be replaced by a new one.

Added in version 3.14.

int PyRefTracer\_SetTracer([PyRefTracer](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer "PyRefTracer")
 tracer, void \*data)[¶](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_SetTracer "Link to this definition")
  

Register a reference tracer function. The function will be called when a new Python object has been created or when an object is going to be destroyed. If **data** is provided it must be an opaque pointer that will be provided when the tracer function is called. Return `0` on success. Set an exception and return `-1` on error.

Note that tracer functions **must not** create Python objects inside or otherwise the call will be re-entrant. The tracer also **must not** clear any existing exception or set an exception. A [thread state](https://docs.python.org/3/glossary.html#term-thread-state)
 will be active every time the tracer function is called.

There must be an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 when calling this function.

If another tracer function was already registered, the old function will be called with **event** set to [`PyRefTracer_TRACKER_REMOVED`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_TRACKER_REMOVED "PyRefTracer_TRACKER_REMOVED")
 just before the new function is registered.

Added in version 3.13.

[PyRefTracer](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer "PyRefTracer")
 PyRefTracer\_GetTracer(void \*\*data)[¶](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_GetTracer "Link to this definition")
  

Get the registered reference tracer function and the value of the opaque data pointer that was registered when [`PyRefTracer_SetTracer()`](https://docs.python.org/3/c-api/profiling.html#c.PyRefTracer_SetTracer "PyRefTracer_SetTracer")
 was called. If no tracer was registered this function will return NULL and will set the **data** pointer to NULL.

There must be an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 when calling this function.

Added in version 3.13.

Performance statistics[¶](https://docs.python.org/3/c-api/profiling.html#performance-statistics "Link to this heading")

========================================================================================================================

PYSTATS\_MAX\_UOP\_ID[¶](https://docs.python.org/3/c-api/profiling.html#c.PYSTATS_MAX_UOP_ID "Link to this definition")
  

Largest micro-operation identifier for which CPython allocates performance statistics counters. Available only in builds configured with [`--enable-pystats`](https://docs.python.org/3/using/configure.html#cmdoption-enable-pystats)
.

This constant is intended for internal use only and is not useful to extension modules.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.2.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Profiling and tracing](https://docs.python.org/3/c-api/profiling.html#)
    
*   [Reference tracing](https://docs.python.org/3/c-api/profiling.html#reference-tracing)
    
*   [Performance statistics](https://docs.python.org/3/c-api/profiling.html#performance-statistics)
    

#### Previous topic

[Multiple interpreters in a Python process](https://docs.python.org/3/c-api/subinterpreters.html "previous chapter")

#### Next topic

[Python Initialization Configuration](https://docs.python.org/3/c-api/init_config.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Profiling+and+tracing&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fprofiling.html&pagesource=c-api%2Fprofiling.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/profiling.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/init_config.html "Python Initialization Configuration")
     |
*   [previous](https://docs.python.org/3/c-api/subinterpreters.html "Multiple interpreters in a Python process")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Profiling and tracing](https://docs.python.org/3/c-api/profiling.html)
    
*    
    
    |
*   Theme Auto Light Dark |