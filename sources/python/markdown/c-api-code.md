### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/file.html "File objects")
     |
*   [previous](https://docs.python.org/3/c-api/cell.html "Cell Objects")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Code Objects](https://docs.python.org/3/c-api/code.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Code Objects[¶](https://docs.python.org/3/c-api/code.html#code-objects "Link to this heading")

===============================================================================================

Code objects are a low-level detail of the CPython implementation. Each one represents a chunk of executable code that hasn’t yet been bound into a function.

type PyCodeObject[¶](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "Link to this definition")
  

The C structure of the objects used to describe code objects. The fields of this type are subject to change at any time.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyCode\_Type[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_Type "Link to this definition")
  

This is an instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 representing the Python [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)
.

int PyCode\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*co)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_Check "Link to this definition")
  

Return true if _co_ is a [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)
. This function always succeeds.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyCode\_GetNumFree([PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*co)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_GetNumFree "Link to this definition")
  

Return the number of [free (closure) variables](https://docs.python.org/3/glossary.html#term-closure-variable)
 in a code object.

int PyUnstable\_Code\_GetFirstFree([PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*co)[¶](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_GetFirstFree "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Return the position of the first [free (closure) variable](https://docs.python.org/3/glossary.html#term-closure-variable)
 in a code object.

Changed in version 3.13: Renamed from `PyCode_GetFirstFree` as part of [Unstable C API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. The old name is deprecated, but will remain available until the signature changes again.

[PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*PyUnstable\_Code\_New(int argcount, int kwonlyargcount, int nlocals, int stacksize, int flags, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*code, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*consts, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*names, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*varnames, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*freevars, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*cellvars, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*qualname, int firstlineno, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*linetable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exceptiontable)[¶](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_New "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Return a new code object. If you need a dummy code object to create a frame, use [`PyCode_NewEmpty()`](https://docs.python.org/3/c-api/code.html#c.PyCode_NewEmpty "PyCode_NewEmpty")
 instead.

Since the definition of the bytecode changes often, calling [`PyUnstable_Code_New()`](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_New "PyUnstable_Code_New")
 directly can bind you to a precise Python version.

The many arguments of this function are inter-dependent in complex ways, meaning that subtle changes to values are likely to result in incorrect execution or VM crashes. Use this function only with extreme care.

Changed in version 3.11: Added `qualname` and `exceptiontable` parameters.

Changed in version 3.12: Renamed from `PyCode_New` as part of [Unstable C API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. The old name is deprecated, but will remain available until the signature changes again.

[PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*PyUnstable\_Code\_NewWithPosOnlyArgs(int argcount, int posonlyargcount, int kwonlyargcount, int nlocals, int stacksize, int flags, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*code, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*consts, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*names, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*varnames, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*freevars, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*cellvars, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*qualname, int firstlineno, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*linetable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exceptiontable)[¶](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_NewWithPosOnlyArgs "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Similar to [`PyUnstable_Code_New()`](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_New "PyUnstable_Code_New")
, but with an extra “posonlyargcount” for positional-only arguments. The same caveats that apply to `PyUnstable_Code_New` also apply to this function.

Added in version 3.8: as `PyCode_NewWithPosOnlyArgs`

Changed in version 3.11: Added `qualname` and `exceptiontable` parameters.

Changed in version 3.12: Renamed to `PyUnstable_Code_NewWithPosOnlyArgs`. The old name is deprecated, but will remain available until the signature changes again.

[PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*PyCode\_NewEmpty(const char \*filename, const char \*funcname, int firstlineno)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_NewEmpty "Link to this definition")
  

_Return value: New reference._

Return a new empty code object with the specified filename, function name, and first line number. The resulting code object will raise an `Exception` if executed.

int PyCode\_Addr2Line([PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*co, int byte\_offset)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_Addr2Line "Link to this definition")
  

Return the line number of the instruction that occurs on or before `byte_offset` and ends after it. This may be `O(N)` in the number of instructions in the code object, so it is not performant for iterating over all the line numbers in a code object.

If you just need the line number of a frame, use [`PyFrame_GetLineNumber()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLineNumber "PyFrame_GetLineNumber")
 instead.

int PyCode\_Addr2Location([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*co, int byte\_offset, int \*start\_line, int \*start\_column, int \*end\_line, int \*end\_column)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_Addr2Location "Link to this definition")
  

Sets the passed `int` pointers to the source code line and column numbers for the instruction at `byte_offset`. Sets the value to `0` when information is not available for any particular element.

Returns `1` if the function succeeds and 0 otherwise.

Added in version 3.11.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCode\_GetCode([PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*co)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_GetCode "Link to this definition")
  

Equivalent to the Python code `getattr(co, 'co_code')`. Returns a strong reference to a [`PyBytesObject`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesObject "PyBytesObject")
 representing the bytecode in a code object. On error, `NULL` is returned and an exception is raised.

This `PyBytesObject` may be created on-demand by the interpreter and does not necessarily represent the bytecode actually executed by CPython. The primary use case for this function is debuggers and profilers.

Added in version 3.11.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCode\_GetVarnames([PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*co)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_GetVarnames "Link to this definition")
  

Equivalent to the Python code `getattr(co, 'co_varnames')`. Returns a new reference to a [`PyTupleObject`](https://docs.python.org/3/c-api/tuple.html#c.PyTupleObject "PyTupleObject")
 containing the names of the local variables. On error, `NULL` is returned and an exception is raised.

Added in version 3.11.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCode\_GetCellvars([PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*co)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_GetCellvars "Link to this definition")
  

Equivalent to the Python code `getattr(co, 'co_cellvars')`. Returns a new reference to a [`PyTupleObject`](https://docs.python.org/3/c-api/tuple.html#c.PyTupleObject "PyTupleObject")
 containing the names of the local variables that are referenced by nested functions. On error, `NULL` is returned and an exception is raised.

Added in version 3.11.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCode\_GetFreevars([PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*co)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_GetFreevars "Link to this definition")
  

Equivalent to the Python code `getattr(co, 'co_freevars')`. Returns a new reference to a [`PyTupleObject`](https://docs.python.org/3/c-api/tuple.html#c.PyTupleObject "PyTupleObject")
 containing the names of the [free (closure) variables](https://docs.python.org/3/glossary.html#term-closure-variable)
. On error, `NULL` is returned and an exception is raised.

Added in version 3.11.

int PyCode\_AddWatcher([PyCode\_WatchCallback](https://docs.python.org/3/c-api/code.html#c.PyCode_WatchCallback "PyCode_WatchCallback")
 callback)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_AddWatcher "Link to this definition")
  

Register _callback_ as a code object watcher for the current interpreter. Return an ID which may be passed to [`PyCode_ClearWatcher()`](https://docs.python.org/3/c-api/code.html#c.PyCode_ClearWatcher "PyCode_ClearWatcher")
. In case of error (e.g. no more watcher IDs available), return `-1` and set an exception.

Added in version 3.12.

int PyCode\_ClearWatcher(int watcher\_id)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_ClearWatcher "Link to this definition")
  

Clear watcher identified by _watcher\_id_ previously returned from [`PyCode_AddWatcher()`](https://docs.python.org/3/c-api/code.html#c.PyCode_AddWatcher "PyCode_AddWatcher")
 for the current interpreter. Return `0` on success, or `-1` and set an exception on error (e.g. if the given _watcher\_id_ was never registered.)

Added in version 3.12.

type PyCodeEvent[¶](https://docs.python.org/3/c-api/code.html#c.PyCodeEvent "Link to this definition")
  

Enumeration of possible code object watcher events: - `PY_CODE_EVENT_CREATE` - `PY_CODE_EVENT_DESTROY`

Added in version 3.12.

PY\_FOREACH\_CODE\_EVENT(V)[¶](https://docs.python.org/3/c-api/code.html#c.PY_FOREACH_CODE_EVENT "Link to this definition")
  

Apply the macro _V_ to each suffix of [`PyCodeEvent`](https://docs.python.org/3/c-api/code.html#c.PyCodeEvent "PyCodeEvent")
 constants. Currently expands to `V(CREATE) V(DESTROY)`. The macro _V_ must accept one event name and supply any punctuation needed between expansions.

typedef int (\*PyCode\_WatchCallback)([PyCodeEvent](https://docs.python.org/3/c-api/code.html#c.PyCodeEvent "PyCodeEvent")
 event, [PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*co)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_WatchCallback "Link to this definition")
  

Type of a code object watcher callback function.

If _event_ is `PY_CODE_EVENT_CREATE`, then the callback is invoked after _co_ has been fully initialized. Otherwise, the callback is invoked before the destruction of _co_ takes place, so the prior state of _co_ can be inspected.

If _event_ is `PY_CODE_EVENT_DESTROY`, taking a reference in the callback to the about-to-be-destroyed code object will resurrect it and prevent it from being freed at this time. When the resurrected object is destroyed later, any watcher callbacks active at that time will be called again.

Users of this API should not rely on internal runtime implementation details. Such details may include, but are not limited to, the exact order and timing of creation and destruction of code objects. While changes in these details may result in differences observable by watchers (including whether a callback is invoked or not), it does not change the semantics of the Python code being executed.

If the callback sets an exception, it must return `-1`; this exception will be printed as an unraisable exception using [`PyErr_WriteUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WriteUnraisable "PyErr_WriteUnraisable")
. Otherwise it should return `0`.

There may already be a pending exception set on entry to the callback. In this case, the callback should return `0` with the same exception still set. This means the callback may not call any other API that can set an exception unless it saves and clears the exception state first, and restores it before returning.

Added in version 3.12.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyCode\_Optimize([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*code, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*consts, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*names, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*lnotab\_obj)[¶](https://docs.python.org/3/c-api/code.html#c.PyCode_Optimize "Link to this definition")
  

This is a function that does nothing.

Prior to Python 3.10, this function would perform basic optimizations to a code object.

Changed in version 3.10: This function now does nothing.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.13.

Code Object Flags[¶](https://docs.python.org/3/c-api/code.html#code-object-flags "Link to this heading")

=========================================================================================================

Code objects contain a bit-field of flags, which can be retrieved as the [`co_flags`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_flags "codeobject.co_flags")
 Python attribute (for example using [`PyObject_GetAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttrString "PyObject_GetAttrString")
), and set using a _flags_ argument to [`PyUnstable_Code_New()`](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_New "PyUnstable_Code_New")
 and similar functions.

Flags whose names start with `CO_FUTURE_` correspond to features normally selectable by [future statements](https://docs.python.org/3/reference/simple_stmts.html#future)
. These flags can be used in [`PyCompilerFlags.cf_flags`](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags.cf_flags "PyCompilerFlags.cf_flags")
. Note that many `CO_FUTURE_` flags are mandatory in current versions of Python, and setting them has no effect.

The following flags are available. For their meaning, see the linked documentation of their Python equivalents.

| Flag | Meaning |
| --- | --- |
| CO\_OPTIMIZED[¶](https://docs.python.org/3/c-api/code.html#c.CO_OPTIMIZED "Link to this definition") | [`inspect.CO_OPTIMIZED`](https://docs.python.org/3/library/inspect.html#inspect.CO_OPTIMIZED "inspect.CO_OPTIMIZED") |
| CO\_NEWLOCALS[¶](https://docs.python.org/3/c-api/code.html#c.CO_NEWLOCALS "Link to this definition") | [`inspect.CO_NEWLOCALS`](https://docs.python.org/3/library/inspect.html#inspect.CO_NEWLOCALS "inspect.CO_NEWLOCALS") |
| CO\_VARARGS[¶](https://docs.python.org/3/c-api/code.html#c.CO_VARARGS "Link to this definition") | [`inspect.CO_VARARGS`](https://docs.python.org/3/library/inspect.html#inspect.CO_VARARGS "inspect.CO_VARARGS") |
| CO\_VARKEYWORDS[¶](https://docs.python.org/3/c-api/code.html#c.CO_VARKEYWORDS "Link to this definition") | [`inspect.CO_VARKEYWORDS`](https://docs.python.org/3/library/inspect.html#inspect.CO_VARKEYWORDS "inspect.CO_VARKEYWORDS") |
| CO\_NESTED[¶](https://docs.python.org/3/c-api/code.html#c.CO_NESTED "Link to this definition") | [`inspect.CO_NESTED`](https://docs.python.org/3/library/inspect.html#inspect.CO_NESTED "inspect.CO_NESTED") |
| CO\_GENERATOR[¶](https://docs.python.org/3/c-api/code.html#c.CO_GENERATOR "Link to this definition") | [`inspect.CO_GENERATOR`](https://docs.python.org/3/library/inspect.html#inspect.CO_GENERATOR "inspect.CO_GENERATOR") |
| CO\_COROUTINE[¶](https://docs.python.org/3/c-api/code.html#c.CO_COROUTINE "Link to this definition") | [`inspect.CO_COROUTINE`](https://docs.python.org/3/library/inspect.html#inspect.CO_COROUTINE "inspect.CO_COROUTINE") |
| CO\_ITERABLE\_COROUTINE[¶](https://docs.python.org/3/c-api/code.html#c.CO_ITERABLE_COROUTINE "Link to this definition") | [`inspect.CO_ITERABLE_COROUTINE`](https://docs.python.org/3/library/inspect.html#inspect.CO_ITERABLE_COROUTINE "inspect.CO_ITERABLE_COROUTINE") |
| CO\_ASYNC\_GENERATOR[¶](https://docs.python.org/3/c-api/code.html#c.CO_ASYNC_GENERATOR "Link to this definition") | [`inspect.CO_ASYNC_GENERATOR`](https://docs.python.org/3/library/inspect.html#inspect.CO_ASYNC_GENERATOR "inspect.CO_ASYNC_GENERATOR") |
| CO\_HAS\_DOCSTRING[¶](https://docs.python.org/3/c-api/code.html#c.CO_HAS_DOCSTRING "Link to this definition") | [`inspect.CO_HAS_DOCSTRING`](https://docs.python.org/3/library/inspect.html#inspect.CO_HAS_DOCSTRING "inspect.CO_HAS_DOCSTRING") |
| CO\_METHOD[¶](https://docs.python.org/3/c-api/code.html#c.CO_METHOD "Link to this definition") | [`inspect.CO_METHOD`](https://docs.python.org/3/library/inspect.html#inspect.CO_METHOD "inspect.CO_METHOD") |
| CO\_FUTURE\_DIVISION[¶](https://docs.python.org/3/c-api/code.html#c.CO_FUTURE_DIVISION "Link to this definition") | no effect ([`__future__.division`](https://docs.python.org/3/library/__future__.html#future__.division "__future__.division")<br>) |
| CO\_FUTURE\_ABSOLUTE\_IMPORT[¶](https://docs.python.org/3/c-api/code.html#c.CO_FUTURE_ABSOLUTE_IMPORT "Link to this definition") | no effect ([`__future__.absolute_import`](https://docs.python.org/3/library/__future__.html#future__.absolute_import "__future__.absolute_import")<br>) |
| CO\_FUTURE\_WITH\_STATEMENT[¶](https://docs.python.org/3/c-api/code.html#c.CO_FUTURE_WITH_STATEMENT "Link to this definition") | no effect ([`__future__.with_statement`](https://docs.python.org/3/library/__future__.html#future__.with_statement "__future__.with_statement")<br>) |
| CO\_FUTURE\_PRINT\_FUNCTION[¶](https://docs.python.org/3/c-api/code.html#c.CO_FUTURE_PRINT_FUNCTION "Link to this definition") | no effect ([`__future__.print_function`](https://docs.python.org/3/library/__future__.html#future__.print_function "__future__.print_function")<br>) |
| CO\_FUTURE\_UNICODE\_LITERALS[¶](https://docs.python.org/3/c-api/code.html#c.CO_FUTURE_UNICODE_LITERALS "Link to this definition") | no effect ([`__future__.unicode_literals`](https://docs.python.org/3/library/__future__.html#future__.unicode_literals "__future__.unicode_literals")<br>) |
| CO\_FUTURE\_GENERATOR\_STOP[¶](https://docs.python.org/3/c-api/code.html#c.CO_FUTURE_GENERATOR_STOP "Link to this definition") | no effect ([`__future__.generator_stop`](https://docs.python.org/3/library/__future__.html#future__.generator_stop "__future__.generator_stop")<br>) |
| CO\_FUTURE\_ANNOTATIONS[¶](https://docs.python.org/3/c-api/code.html#c.CO_FUTURE_ANNOTATIONS "Link to this definition") | [`__future__.annotations`](https://docs.python.org/3/library/__future__.html#future__.annotations "__future__.annotations") |

Extra information[¶](https://docs.python.org/3/c-api/code.html#extra-information "Link to this heading")

=========================================================================================================

To support low-level extensions to frame evaluation, such as external just-in-time compilers, it is possible to attach arbitrary extra data to code objects.

These functions are part of the unstable C API tier: this functionality is a CPython implementation detail, and the API may change without deprecation warnings.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyUnstable\_Eval\_RequestCodeExtraIndex([freefunc](https://docs.python.org/3/c-api/typeobj.html#c.freefunc "freefunc")
 free)[¶](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Eval_RequestCodeExtraIndex "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Return a new opaque index value used to adding data to code objects.

You generally call this function once (per interpreter). Use the result with [`PyUnstable_Code_GetExtra()`](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_GetExtra "PyUnstable_Code_GetExtra")
 and [`PyUnstable_Code_SetExtra()`](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_SetExtra "PyUnstable_Code_SetExtra")
 to manipulate data on individual code objects.

If _free_ is not `NULL`: when a code object is deallocated, _free_ will be called on non-`NULL` data stored under the new index. Use [`Py_DecRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DecRef "Py_DecRef")
 when storing [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
.

Added in version 3.6: as `_PyEval_RequestCodeExtraIndex`

Changed in version 3.12: Renamed to `PyUnstable_Eval_RequestCodeExtraIndex`. The old private name is deprecated, but will be available until the API changes.

int PyUnstable\_Code\_GetExtra([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*code, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index, void \*\*extra)[¶](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_GetExtra "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Set _extra_ to the extra data stored under the given index. Return 0 on success. Set an exception and return -1 on failure.

If no data was set under the index, set _extra_ to `NULL` and return 0 without setting an exception.

Added in version 3.6: as `_PyCode_GetExtra`

Changed in version 3.12: Renamed to `PyUnstable_Code_GetExtra`. The old private name is deprecated, but will be available until the API changes.

int PyUnstable\_Code\_SetExtra([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*code, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 index, void \*extra)[¶](https://docs.python.org/3/c-api/code.html#c.PyUnstable_Code_SetExtra "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Set the extra data stored under the given index to _extra_. Return 0 on success. Set an exception and return -1 on failure.

Added in version 3.6: as `_PyCode_SetExtra`

Changed in version 3.12: Renamed to `PyUnstable_Code_SetExtra`. The old private name is deprecated, but will be available until the API changes.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Code Objects](https://docs.python.org/3/c-api/code.html#)
    
*   [Code Object Flags](https://docs.python.org/3/c-api/code.html#code-object-flags)
    
*   [Extra information](https://docs.python.org/3/c-api/code.html#extra-information)
    

#### Previous topic

[Cell Objects](https://docs.python.org/3/c-api/cell.html "previous chapter")

#### Next topic

[File objects](https://docs.python.org/3/c-api/file.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Code+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fcode.html&pagesource=c-api%2Fcode.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/code.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/file.html "File objects")
     |
*   [previous](https://docs.python.org/3/c-api/cell.html "Cell Objects")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Code Objects](https://docs.python.org/3/c-api/code.html)
    
*    
    
    |
*   Theme Auto Light Dark |