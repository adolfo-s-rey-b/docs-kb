### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/method.html "Instance Method Objects")
     |
*   [previous](https://docs.python.org/3/c-api/set.html "Set Objects")
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
*   [Function Objects](https://docs.python.org/3/c-api/function.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Function Objects[¶](https://docs.python.org/3/c-api/function.html#function-objects "Link to this heading")

===========================================================================================================

There are a few functions specific to Python functions.

type PyFunctionObject[¶](https://docs.python.org/3/c-api/function.html#c.PyFunctionObject "Link to this definition")
  

The C structure used for functions.

In the free-threaded build, direct access to mutable fields requires synchronization if another thread may modify the function. See [C API Extension Support for Free Threading](https://docs.python.org/3/howto/free-threading-extensions.html#freethreading-extensions-howto)
.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyFunction\_Type[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_Type "Link to this definition")
  

This is an instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 and represents the Python function type. It is exposed to Python programmers as `types.FunctionType`.

int PyFunction\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_Check "Link to this definition")
  

Return true if _o_ is a function object (has type [`PyFunction_Type`](https://docs.python.org/3/c-api/function.html#c.PyFunction_Type "PyFunction_Type")
). The parameter must not be `NULL`. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_New([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*code, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_New "Link to this definition")
  

_Return value: New reference._

Return a new function object associated with the code object _code_. _globals_ must be a dictionary with the global variables accessible to the function.

The function’s docstring and name are retrieved from the code object. [`__module__`](https://docs.python.org/3/reference/datamodel.html#function.__module__ "function.__module__")
 is retrieved from _globals_. The argument defaults, annotations and closure are set to `NULL`. [`__qualname__`](https://docs.python.org/3/reference/datamodel.html#function.__qualname__ "function.__qualname__")
 is set to the same value as the code object’s [`co_qualname`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_qualname "codeobject.co_qualname")
 field.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_NewWithQualName([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*code, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*qualname)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_NewWithQualName "Link to this definition")
  

_Return value: New reference._

As [`PyFunction_New()`](https://docs.python.org/3/c-api/function.html#c.PyFunction_New "PyFunction_New")
, but also allows setting the function object’s [`__qualname__`](https://docs.python.org/3/reference/datamodel.html#function.__qualname__ "function.__qualname__")
 attribute. _qualname_ should be a unicode object or `NULL`; if `NULL`, the `__qualname__` attribute is set to the same value as the code object’s [`co_qualname`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_qualname "codeobject.co_qualname")
 field.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GetCode([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GetCode "Link to this definition")
  

_Return value: Borrowed reference._

Return the code object associated with the function object _op_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GetGlobals([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GetGlobals "Link to this definition")
  

_Return value: Borrowed reference._

Return the globals dictionary associated with the function object _op_.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GetModule([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GetModule "Link to this definition")
  

_Return value: Borrowed reference._

Return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 to the [`__module__`](https://docs.python.org/3/reference/datamodel.html#function.__module__ "function.__module__")
 attribute of the [function object](https://docs.python.org/3/reference/datamodel.html#user-defined-funcs)
 _op_. It can be _NULL_.

This is normally a [`string`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 containing the module name, but can be set to any other object by Python code.

In the free-threaded build, if the attribute may be modified concurrently, convert the borrowed reference to a strong reference with [`Py_XNewRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XNewRef "Py_XNewRef")
 immediately, before calling any other Python API. The same applies to [`PyFunction_GET_MODULE()`](https://docs.python.org/3/c-api/function.html#c.PyFunction_GET_MODULE "PyFunction_GET_MODULE")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GetDefaults([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GetDefaults "Link to this definition")
  

_Return value: Borrowed reference._

Return the argument default values of the function object _op_. This can be a tuple of arguments or `NULL`.

int PyFunction\_SetDefaults([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*defaults)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_SetDefaults "Link to this definition")
  

Set the argument default values for the function object _op_. _defaults_ must be `Py_None` or a tuple.

Raises [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 and returns `-1` on failure.

void PyFunction\_SetVectorcall([PyFunctionObject](https://docs.python.org/3/c-api/function.html#c.PyFunctionObject "PyFunctionObject")
 \*func, [vectorcallfunc](https://docs.python.org/3/c-api/call.html#c.vectorcallfunc "vectorcallfunc")
 vectorcall)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_SetVectorcall "Link to this definition")
  

Set the vectorcall field of a given function object _func_.

Warning: extensions using this API must preserve the behavior of the unaltered (default) vectorcall function!

Added in version 3.12.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GetKwDefaults([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GetKwDefaults "Link to this definition")
  

_Return value: Borrowed reference._

Return the keyword-only argument default values of the function object _op_. This can be a dictionary of arguments or `NULL`.

int PyFunction\_SetKwDefaults([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*defaults)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_SetKwDefaults "Link to this definition")
  

Set the keyword-only argument default values of the function object _op_. _defaults_ must be a dictionary of keyword-only arguments or `Py_None`.

This function returns `0` on success, and returns `-1` with an exception set on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GetClosure([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GetClosure "Link to this definition")
  

_Return value: Borrowed reference._

Return the closure associated with the function object _op_. This can be `NULL` or a tuple of cell objects.

int PyFunction\_SetClosure([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*closure)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_SetClosure "Link to this definition")
  

Set the closure associated with the function object _op_. _closure_ must be `Py_None` or a tuple of cell objects.

Raises [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 and returns `-1` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GetAnnotations([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GetAnnotations "Link to this definition")
  

_Return value: Borrowed reference._

Return the annotations of the function object _op_. This can be a mutable dictionary or `NULL`.

int PyFunction\_SetAnnotations([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*annotations)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_SetAnnotations "Link to this definition")
  

Set the annotations for the function object _op_. _annotations_ must be a dictionary or `Py_None`.

Raises [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")
 and returns `-1` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GET\_CODE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GET_CODE "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GET\_GLOBALS([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GET_GLOBALS "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GET\_MODULE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GET_MODULE "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GET\_DEFAULTS([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GET_DEFAULTS "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GET\_KW\_DEFAULTS([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GET_KW_DEFAULTS "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GET\_CLOSURE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GET_CLOSURE "Link to this definition")
  

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFunction\_GET\_ANNOTATIONS([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_GET_ANNOTATIONS "Link to this definition")
  

_Return value: Borrowed reference._

These functions are similar to their `PyFunction_Get*` counterparts, but do not do type checking. Passing anything other than an instance of [`PyFunction_Type`](https://docs.python.org/3/c-api/function.html#c.PyFunction_Type "PyFunction_Type")
 is undefined behavior.

int PyFunction\_AddWatcher([PyFunction\_WatchCallback](https://docs.python.org/3/c-api/function.html#c.PyFunction_WatchCallback "PyFunction_WatchCallback")
 callback)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_AddWatcher "Link to this definition")
  

Register _callback_ as a function watcher for the current interpreter. Return an ID which may be passed to [`PyFunction_ClearWatcher()`](https://docs.python.org/3/c-api/function.html#c.PyFunction_ClearWatcher "PyFunction_ClearWatcher")
. In case of error (e.g. no more watcher IDs available), return `-1` and set an exception.

Added in version 3.12.

int PyFunction\_ClearWatcher(int watcher\_id)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_ClearWatcher "Link to this definition")
  

Clear watcher identified by _watcher\_id_ previously returned from [`PyFunction_AddWatcher()`](https://docs.python.org/3/c-api/function.html#c.PyFunction_AddWatcher "PyFunction_AddWatcher")
 for the current interpreter. Return `0` on success, or `-1` and set an exception on error (e.g. if the given _watcher\_id_ was never registered.)

Added in version 3.12.

type PyFunction\_WatchEvent[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_WatchEvent "Link to this definition")
  

> Enumeration of possible function watcher events:
> 
> *   `PyFunction_EVENT_CREATE`
>     
> *   `PyFunction_EVENT_DESTROY`
>     
> *   `PyFunction_EVENT_MODIFY_CODE`
>     
> *   `PyFunction_EVENT_MODIFY_DEFAULTS`
>     
> *   `PyFunction_EVENT_MODIFY_KWDEFAULTS`
>     

Added in version 3.12:

*   `PyFunction_EVENT_MODIFY_QUALNAME`
    

Added in version 3.15.

PY\_FOREACH\_FUNC\_EVENT(V)[¶](https://docs.python.org/3/c-api/function.html#c.PY_FOREACH_FUNC_EVENT "Link to this definition")
  

Apply the macro _V_ to each suffix of [`PyFunction_WatchEvent`](https://docs.python.org/3/c-api/function.html#c.PyFunction_WatchEvent "PyFunction_WatchEvent")
 constants. Currently expands to `V(CREATE) V(DESTROY) V(MODIFY_CODE) V(MODIFY_DEFAULTS) V(MODIFY_KWDEFAULTS) V(MODIFY_QUALNAME)`. The macro _V_ must accept one event name and supply any punctuation needed between expansions.

typedef int (\*PyFunction\_WatchCallback)([PyFunction\_WatchEvent](https://docs.python.org/3/c-api/function.html#c.PyFunction_WatchEvent "PyFunction_WatchEvent")
 event, [PyFunctionObject](https://docs.python.org/3/c-api/function.html#c.PyFunctionObject "PyFunctionObject")
 \*func, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*new\_value)[¶](https://docs.python.org/3/c-api/function.html#c.PyFunction_WatchCallback "Link to this definition")
  

Type of a function watcher callback function.

If _event_ is `PyFunction_EVENT_CREATE` or `PyFunction_EVENT_DESTROY` then _new\_value_ will be `NULL`. Otherwise, _new\_value_ will hold a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 to the new value that is about to be stored in _func_ for the attribute that is being modified.

The callback may inspect but must not modify _func_; doing so could have unpredictable effects, including infinite recursion.

If _event_ is `PyFunction_EVENT_CREATE`, then the callback is invoked after _func_ has been fully initialized. Otherwise, the callback is invoked before the modification to _func_ takes place, so the prior state of _func_ can be inspected. The runtime is permitted to optimize away the creation of function objects when possible. In such cases no event will be emitted. Although this creates the possibility of an observable difference of runtime behavior depending on optimization decisions, it does not change the semantics of the Python code being executed.

If _event_ is `PyFunction_EVENT_DESTROY`, taking a reference in the callback to the about-to-be-destroyed function will resurrect it, preventing it from being freed at this time. When the resurrected object is destroyed later, any watcher callbacks active at that time will be called again.

If the callback sets an exception, it must return `-1`; this exception will be printed as an unraisable exception using [`PyErr_WriteUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_WriteUnraisable "PyErr_WriteUnraisable")
. Otherwise it should return `0`.

There may already be a pending exception set on entry to the callback. In this case, the callback should return `0` with the same exception still set. This means the callback may not call any other API that can set an exception unless it saves and clears the exception state first, and restores it before returning.

Added in version 3.12.

#### Previous topic

[Set Objects](https://docs.python.org/3/c-api/set.html "previous chapter")

#### Next topic

[Instance Method Objects](https://docs.python.org/3/c-api/method.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Function+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Ffunction.html&pagesource=c-api%2Ffunction.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/function.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/method.html "Instance Method Objects")
     |
*   [previous](https://docs.python.org/3/c-api/set.html "Set Objects")
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
*   [Function Objects](https://docs.python.org/3/c-api/function.html)
    
*    
    
    |
*   Theme Auto Light Dark |