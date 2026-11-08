### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/installing/index.html "Installing Python modules")
     |
*   [previous](https://docs.python.org/3/c-api/apiabiversion.html "API and ABI Versioning")
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
*   [Monitoring C API](https://docs.python.org/3/c-api/monitoring.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Monitoring C API[¶](https://docs.python.org/3/c-api/monitoring.html#monitoring-c-api "Link to this heading")

=============================================================================================================

Added in version 3.13.

An extension may need to interact with the event monitoring system. Subscribing to events and registering callbacks can be done via the Python API exposed in [`sys.monitoring`](https://docs.python.org/3/library/sys.monitoring.html#module-sys.monitoring "sys.monitoring: Access and control event monitoring")
.

Generating Execution Events[¶](https://docs.python.org/3/c-api/monitoring.html#generating-execution-events "Link to this heading")

===================================================================================================================================

The functions below make it possible for an extension to fire monitoring events as it emulates the execution of Python code. Each of these functions accepts a `PyMonitoringState` struct which contains concise information about the activation state of events, as well as the event arguments, which include a `PyObject*` representing the code object, the instruction offset and sometimes additional, event-specific arguments (see [`sys.monitoring`](https://docs.python.org/3/library/sys.monitoring.html#module-sys.monitoring "sys.monitoring: Access and control event monitoring")
 for details about the signatures of the different event callbacks). The `codelike` argument should be an instance of [`types.CodeType`](https://docs.python.org/3/library/types.html#types.CodeType "types.CodeType")
 or of a type that emulates it.

The VM disables tracing when firing an event, so there is no need for user code to do that.

Monitoring functions should not be called with an exception set, except those listed below as working with the current exception.

type PyMonitoringState[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "Link to this definition")
  

Representation of the state of an event type. It is allocated by the user while its contents are maintained by the monitoring API functions described below.

All of the functions below return 0 on success and -1 (with an exception set) on error.

See [`sys.monitoring`](https://docs.python.org/3/library/sys.monitoring.html#module-sys.monitoring "sys.monitoring: Access and control event monitoring")
 for descriptions of the events.

int PyMonitoring\_FirePyStartEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyStartEvent "Link to this definition")
  

Fire a `PY_START` event.

int PyMonitoring\_FirePyResumeEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyResumeEvent "Link to this definition")
  

Fire a `PY_RESUME` event.

int PyMonitoring\_FirePyReturnEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*retval)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyReturnEvent "Link to this definition")
  

Fire a `PY_RETURN` event.

int PyMonitoring\_FirePyYieldEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*retval)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyYieldEvent "Link to this definition")
  

Fire a `PY_YIELD` event.

int PyMonitoring\_FireCallEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*arg0)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireCallEvent "Link to this definition")
  

Fire a `CALL` event.

int PyMonitoring\_FireLineEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset, int lineno)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireLineEvent "Link to this definition")
  

Fire a `LINE` event.

int PyMonitoring\_FireJumpEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*target\_offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireJumpEvent "Link to this definition")
  

Fire a `JUMP` event.

int PyMonitoring\_FireBranchLeftEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*target\_offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireBranchLeftEvent "Link to this definition")
  

Fire a `BRANCH_LEFT` event.

int PyMonitoring\_FireBranchRightEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*target\_offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireBranchRightEvent "Link to this definition")
  

Fire a `BRANCH_RIGHT` event.

int PyMonitoring\_FireCReturnEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*retval)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireCReturnEvent "Link to this definition")
  

Fire a `C_RETURN` event.

int PyMonitoring\_FirePyThrowEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyThrowEvent "Link to this definition")
  

Fire a `PY_THROW` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
).

int PyMonitoring\_FireRaiseEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireRaiseEvent "Link to this definition")
  

Fire a `RAISE` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
).

int PyMonitoring\_FireCRaiseEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireCRaiseEvent "Link to this definition")
  

Fire a `C_RAISE` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
).

int PyMonitoring\_FireReraiseEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireReraiseEvent "Link to this definition")
  

Fire a `RERAISE` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
).

int PyMonitoring\_FireExceptionHandledEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireExceptionHandledEvent "Link to this definition")
  

Fire an `EXCEPTION_HANDLED` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
).

int PyMonitoring\_FirePyUnwindEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FirePyUnwindEvent "Link to this definition")
  

Fire a `PY_UNWIND` event with the current exception (as returned by [`PyErr_GetRaisedException()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_GetRaisedException "PyErr_GetRaisedException")
).

int PyMonitoring\_FireStopIterationEvent([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*codelike, int32\_t offset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_FireStopIterationEvent "Link to this definition")
  

Fire a `STOP_ITERATION` event. If `value` is an instance of [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
, it is used. Otherwise, a new `StopIteration` instance is created with `value` as its argument.

Managing the Monitoring State[¶](https://docs.python.org/3/c-api/monitoring.html#managing-the-monitoring-state "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

Monitoring states can be managed with the help of monitoring scopes. A scope would typically correspond to a Python function.

int PyMonitoring\_EnterScope([PyMonitoringState](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoringState "PyMonitoringState")
 \*state\_array, uint64\_t \*version, const uint8\_t \*event\_types, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 length)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_EnterScope "Link to this definition")
  

Enter a monitored scope. `event_types` is an array of the event IDs for events that may be fired from the scope. For example, the ID of a `PY_START` event is the value `PY_MONITORING_EVENT_PY_START`, which is numerically equal to the base-2 logarithm of `sys.monitoring.events.PY_START`. `state_array` is an array with a monitoring state entry for each event in `event_types`, it is allocated by the user but populated by `PyMonitoring_EnterScope()` with information about the activation state of the event. The size of `event_types` (and hence also of `state_array`) is given in `length`.

The `version` argument is a pointer to a value which should be allocated by the user together with `state_array` and initialized to 0, and then set only by `PyMonitoring_EnterScope()` itself. It allows this function to determine whether event states have changed since the previous call, and to return quickly if they have not.

The scopes referred to here are lexical scopes: a function, class or method. `PyMonitoring_EnterScope()` should be called whenever the lexical scope is entered. Scopes can be reentered, reusing the same _state\_array_ and _version_, in situations like when emulating a recursive Python function. When a code-like’s execution is paused, such as when emulating a generator, the scope needs to be exited and re-entered.

The macros for _event\_types_ are:

 
| Macro | Event |
| --- | --- |
| PY\_MONITORING\_EVENT\_BRANCH\_LEFT[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_BRANCH_LEFT "Link to this definition") | [`BRANCH_LEFT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT) |
| PY\_MONITORING\_EVENT\_BRANCH\_RIGHT[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_BRANCH_RIGHT "Link to this definition") | [`BRANCH_RIGHT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_RIGHT) |
| PY\_MONITORING\_EVENT\_CALL[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_CALL "Link to this definition") | [`CALL`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-CALL) |
| PY\_MONITORING\_EVENT\_C\_RAISE[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_C_RAISE "Link to this definition") | [`C_RAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-C_RAISE) |
| PY\_MONITORING\_EVENT\_C\_RETURN[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_C_RETURN "Link to this definition") | [`C_RETURN`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-C_RETURN) |
| PY\_MONITORING\_EVENT\_EXCEPTION\_HANDLED[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_EXCEPTION_HANDLED "Link to this definition") | [`EXCEPTION_HANDLED`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-EXCEPTION_HANDLED) |
| PY\_MONITORING\_EVENT\_INSTRUCTION[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_INSTRUCTION "Link to this definition") | [`INSTRUCTION`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-INSTRUCTION) |
| PY\_MONITORING\_EVENT\_JUMP[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_JUMP "Link to this definition") | [`JUMP`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-JUMP) |
| PY\_MONITORING\_EVENT\_LINE[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_LINE "Link to this definition") | [`LINE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-LINE) |
| PY\_MONITORING\_EVENT\_PY\_RESUME[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_PY_RESUME "Link to this definition") | [`PY_RESUME`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_RESUME) |
| PY\_MONITORING\_EVENT\_PY\_RETURN[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_PY_RETURN "Link to this definition") | [`PY_RETURN`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_RETURN) |
| PY\_MONITORING\_EVENT\_PY\_START[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_PY_START "Link to this definition") | [`PY_START`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_START) |
| PY\_MONITORING\_EVENT\_PY\_THROW[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_PY_THROW "Link to this definition") | [`PY_THROW`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_THROW) |
| PY\_MONITORING\_EVENT\_PY\_UNWIND[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_PY_UNWIND "Link to this definition") | [`PY_UNWIND`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_UNWIND) |
| PY\_MONITORING\_EVENT\_PY\_YIELD[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_PY_YIELD "Link to this definition") | [`PY_YIELD`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_YIELD) |
| PY\_MONITORING\_EVENT\_RAISE[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_RAISE "Link to this definition") | [`RAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RAISE) |
| PY\_MONITORING\_EVENT\_RERAISE[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_RERAISE "Link to this definition") | [`RERAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RERAISE) |
| PY\_MONITORING\_EVENT\_STOP\_ITERATION[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_STOP_ITERATION "Link to this definition") | [`STOP_ITERATION`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-STOP_ITERATION) |
| PY\_MONITORING\_EVENT\_BRANCH[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_BRANCH "Link to this definition")<br>  <br><br>Deprecated since version 3.14: Use [`PY_MONITORING_EVENT_BRANCH_LEFT`](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_BRANCH_LEFT "PY_MONITORING_EVENT_BRANCH_LEFT")<br> and [`PY_MONITORING_EVENT_BRANCH_RIGHT`](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_EVENT_BRANCH_RIGHT "PY_MONITORING_EVENT_BRANCH_RIGHT")<br> instead. | [`BRANCH_LEFT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT)<br> and [`BRANCH_RIGHT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_RIGHT) |

int PyMonitoring\_ExitScope(void)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PyMonitoring_ExitScope "Link to this definition")
  

Exit the last scope that was entered with `PyMonitoring_EnterScope()`.

int PY\_MONITORING\_IS\_INSTRUMENTED\_EVENT(uint8\_t ev)[¶](https://docs.python.org/3/c-api/monitoring.html#c.PY_MONITORING_IS_INSTRUMENTED_EVENT "Link to this definition")
  

Return true if the event corresponding to the event ID _ev_ is a [local event](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-local)
.

Added in version 3.13.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.14.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Monitoring C API](https://docs.python.org/3/c-api/monitoring.html#)
    
*   [Generating Execution Events](https://docs.python.org/3/c-api/monitoring.html#generating-execution-events)
    *   [Managing the Monitoring State](https://docs.python.org/3/c-api/monitoring.html#managing-the-monitoring-state)
        

#### Previous topic

[API and ABI Versioning](https://docs.python.org/3/c-api/apiabiversion.html "previous chapter")

#### Next topic

[Installing Python modules](https://docs.python.org/3/installing/index.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Monitoring+C+API&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fmonitoring.html&pagesource=c-api%2Fmonitoring.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/monitoring.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/installing/index.html "Installing Python modules")
     |
*   [previous](https://docs.python.org/3/c-api/apiabiversion.html "API and ABI Versioning")
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
*   [Monitoring C API](https://docs.python.org/3/c-api/monitoring.html)
    
*    
    
    |
*   Theme Auto Light Dark |