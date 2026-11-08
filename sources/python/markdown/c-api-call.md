### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/number.html "Number Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/object.html "Object Protocol")
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
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
     »
*   [Call Protocol](https://docs.python.org/3/c-api/call.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Call Protocol[¶](https://docs.python.org/3/c-api/call.html#call-protocol "Link to this heading")

=================================================================================================

CPython supports two different calling protocols: _tp\_call_ and vectorcall.

The _tp\_call_ Protocol[¶](https://docs.python.org/3/c-api/call.html#the-tp-call-protocol "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Instances of classes that set [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call")
 are callable. The signature of the slot is:

PyObject \*tp\_call(PyObject \*callable, PyObject \*args, PyObject \*kwargs);

A call is made using a tuple for the positional arguments and a dict for the keyword arguments, similarly to `callable(*args, **kwargs)` in Python code. _args_ must be non-NULL (use an empty tuple if there are no arguments) but _kwargs_ may be _NULL_ if there are no keyword arguments.

This convention is not only used by _tp\_call_: [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
 and [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
 also pass arguments this way.

To call an object, use [`PyObject_Call()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Call "PyObject_Call")
 or another [call API](https://docs.python.org/3/c-api/call.html#capi-call)
.

The Vectorcall Protocol[¶](https://docs.python.org/3/c-api/call.html#the-vectorcall-protocol "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

Added in version 3.9.

The vectorcall protocol was introduced in [**PEP 590**](https://peps.python.org/pep-0590/)
 as an additional protocol for making calls more efficient.

As rule of thumb, CPython will prefer the vectorcall for internal calls if the callable supports it. However, this is not a hard rule. Additionally, some third-party extensions use _tp\_call_ directly (rather than using [`PyObject_Call()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Call "PyObject_Call")
). Therefore, a class supporting vectorcall must also implement [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call")
. Moreover, the callable must behave the same regardless of which protocol is used. The recommended way to achieve this is by setting `tp_call` to [`PyVectorcall_Call()`](https://docs.python.org/3/c-api/call.html#c.PyVectorcall_Call "PyVectorcall_Call")
. This bears repeating:

Warning

A class supporting vectorcall **must** also implement [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call")
 with the same semantics.

Changed in version 3.12: The [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL "Py_TPFLAGS_HAVE_VECTORCALL")
 flag is now removed from a class when the class’s [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__")
 method is reassigned. (This internally sets [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call")
 only, and thus may make it behave differently than the vectorcall function.) In earlier Python versions, vectorcall should only be used with [`immutable`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Py_TPFLAGS_IMMUTABLETYPE")
 or static types.

A class should not implement vectorcall if that would be slower than _tp\_call_. For example, if the callee needs to convert the arguments to an args tuple and kwargs dict anyway, then there is no point in implementing vectorcall.

Classes can implement the vectorcall protocol by enabling the [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL "Py_TPFLAGS_HAVE_VECTORCALL")
 flag and setting [`tp_vectorcall_offset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_vectorcall_offset "PyTypeObject.tp_vectorcall_offset")
 to the offset inside the object structure where a _vectorcallfunc_ appears. This is a pointer to a function with the following signature:

typedef [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*vectorcallfunc)([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*const \*args, size\_t nargsf, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*kwnames)[¶](https://docs.python.org/3/c-api/call.html#c.vectorcallfunc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

*   _callable_ is the object being called.
    
*   _args_ is a C array consisting of the positional arguments followed by the values of the keyword arguments. This can be _NULL_ if there are no arguments.
    
*   _nargsf_ is the number of positional arguments plus possibly the [`PY_VECTORCALL_ARGUMENTS_OFFSET`](https://docs.python.org/3/c-api/call.html#c.PY_VECTORCALL_ARGUMENTS_OFFSET "PY_VECTORCALL_ARGUMENTS_OFFSET")
     flag. To get the actual number of positional arguments from _nargsf_, use [`PyVectorcall_NARGS()`](https://docs.python.org/3/c-api/call.html#c.PyVectorcall_NARGS "PyVectorcall_NARGS")
    .
    
*   _kwnames_ is a tuple containing the names of the keyword arguments; in other words, the keys of the kwargs dict. These names must be strings (instances of `str` or a subclass) and they must be unique. If there are no keyword arguments, then _kwnames_ can instead be _NULL_.
    

PY\_VECTORCALL\_ARGUMENTS\_OFFSET[¶](https://docs.python.org/3/c-api/call.html#c.PY_VECTORCALL_ARGUMENTS_OFFSET "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

If this flag is set in a vectorcall _nargsf_ argument, the callee is allowed to temporarily change `args[-1]`. In other words, _args_ points to argument 1 (not 0) in the allocated vector. The callee must restore the value of `args[-1]` before returning.

For [`PyObject_VectorcallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_VectorcallMethod "PyObject_VectorcallMethod")
, this flag means instead that `args[0]` may be changed.

Whenever they can do so cheaply (without additional allocation), callers are encouraged to use [`PY_VECTORCALL_ARGUMENTS_OFFSET`](https://docs.python.org/3/c-api/call.html#c.PY_VECTORCALL_ARGUMENTS_OFFSET "PY_VECTORCALL_ARGUMENTS_OFFSET")
. Doing so will allow callables such as bound methods to make their onward calls (which include a prepended _self_ argument) very efficiently.

Added in version 3.8.

To call an object that implements vectorcall, use a [call API](https://docs.python.org/3/c-api/call.html#capi-call)
 function as with any other callable. [`PyObject_Vectorcall()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Vectorcall "PyObject_Vectorcall")
 will usually be most efficient.

### Recursion Control[¶](https://docs.python.org/3/c-api/call.html#recursion-control "Link to this heading")

When using _tp\_call_, callees do not need to worry about [recursion](https://docs.python.org/3/c-api/exceptions.html#recursion)
: CPython uses [`Py_EnterRecursiveCall()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_EnterRecursiveCall "Py_EnterRecursiveCall")
 and [`Py_LeaveRecursiveCall()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_LeaveRecursiveCall "Py_LeaveRecursiveCall")
 for calls made using _tp\_call_.

For efficiency, this is not the case for calls done using vectorcall: the callee should use _Py\_EnterRecursiveCall_ and _Py\_LeaveRecursiveCall_ if needed.

### Vectorcall Support API[¶](https://docs.python.org/3/c-api/call.html#vectorcall-support-api "Link to this heading")

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyVectorcall\_NARGS(size\_t nargsf)[¶](https://docs.python.org/3/c-api/call.html#c.PyVectorcall_NARGS "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Given a vectorcall _nargsf_ argument, return the actual number of arguments. Currently equivalent to:

(Py\_ssize\_t)(nargsf & ~PY\_VECTORCALL\_ARGUMENTS\_OFFSET)

However, the function `PyVectorcall_NARGS` should be used to allow for future extensions.

Added in version 3.8.

[vectorcallfunc](https://docs.python.org/3/c-api/call.html#c.vectorcallfunc "vectorcallfunc")
 PyVectorcall\_Function([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/call.html#c.PyVectorcall_Function "Link to this definition")
  

If _op_ does not support the vectorcall protocol (either because the type does not or because the specific instance does not), return _NULL_. Otherwise, return the vectorcall function pointer stored in _op_. This function never raises an exception.

This is mostly useful to check whether or not _op_ supports vectorcall, which can be done by checking `PyVectorcall_Function(op) != NULL`.

Added in version 3.9.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyVectorcall\_Call([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*tuple, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*dict)[¶](https://docs.python.org/3/c-api/call.html#c.PyVectorcall_Call "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Call _callable_’s [`vectorcallfunc`](https://docs.python.org/3/c-api/call.html#c.vectorcallfunc "vectorcallfunc")
 with positional and keyword arguments given in a tuple and dict, respectively.

This is a specialized function, intended to be put in the [`tp_call`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_call "PyTypeObject.tp_call")
 slot or be used in an implementation of `tp_call`. It does not check the [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL "Py_TPFLAGS_HAVE_VECTORCALL")
 flag and it does not fall back to `tp_call`.

Added in version 3.8.

Object Calling API[¶](https://docs.python.org/3/c-api/call.html#object-calling-api "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Various functions are available for calling a Python object. Each converts its arguments to a convention supported by the called object – either _tp\_call_ or vectorcall. In order to do as little conversion as possible, pick one that best fits the format of data you have available.

The following table summarizes the available functions; please see individual documentation for details.

| Function | callable | args | kwargs |
| --- | --- | --- | --- |
| [`PyObject_Call()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Call "PyObject_Call") | `PyObject *` | tuple | dict/`NULL` |
| [`PyObject_CallNoArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallNoArgs "PyObject_CallNoArgs") | `PyObject *` | —   | —   |
| [`PyObject_CallOneArg()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallOneArg "PyObject_CallOneArg") | `PyObject *` | 1 object | —   |
| [`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject "PyObject_CallObject") | `PyObject *` | tuple/`NULL` | —   |
| [`PyObject_CallFunction()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallFunction "PyObject_CallFunction") | `PyObject *` | format | —   |
| [`PyObject_CallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethod "PyObject_CallMethod") | obj + `char*` | format | —   |
| [`PyObject_CallFunctionObjArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallFunctionObjArgs "PyObject_CallFunctionObjArgs") | `PyObject *` | variadic | —   |
| [`PyObject_CallMethodObjArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethodObjArgs "PyObject_CallMethodObjArgs") | obj + name | variadic | —   |
| [`PyObject_CallMethodNoArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethodNoArgs "PyObject_CallMethodNoArgs") | obj + name | —   | —   |
| [`PyObject_CallMethodOneArg()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethodOneArg "PyObject_CallMethodOneArg") | obj + name | 1 object | —   |
| [`PyObject_Vectorcall()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Vectorcall "PyObject_Vectorcall") | `PyObject *` | vectorcall | vectorcall |
| [`PyObject_VectorcallDict()`](https://docs.python.org/3/c-api/call.html#c.PyObject_VectorcallDict "PyObject_VectorcallDict") | `PyObject *` | vectorcall | dict/`NULL` |
| [`PyObject_VectorcallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_VectorcallMethod "PyObject_VectorcallMethod") | arg + name | vectorcall | vectorcall |

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_Call([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*kwargs)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_Call "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Call a callable Python object _callable_, with arguments given by the tuple _args_, and named arguments given by the dictionary _kwargs_.

_args_ must not be _NULL_; use an empty tuple if no arguments are needed. If no named arguments are needed, _kwargs_ can be _NULL_.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

This is the equivalent of the Python expression: `callable(*args, **kwargs)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_CallNoArgs([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_CallNoArgs "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Call a callable Python object _callable_ without any arguments. It is the most efficient way to call a callable Python object without any argument.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

Added in version 3.9.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_CallOneArg([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*arg)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_CallOneArg "Link to this definition")
  

_Return value: New reference._

Call a callable Python object _callable_ with exactly 1 positional argument _arg_ and no keyword arguments.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

Added in version 3.9.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_CallObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*args)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Call a callable Python object _callable_, with arguments given by the tuple _args_. If no arguments are needed, then _args_ can be _NULL_.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

This is the equivalent of the Python expression: `callable(*args)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_CallFunction([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, const char \*format, ...)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_CallFunction "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Call a callable Python object _callable_, with a variable number of C arguments. The C arguments are described using a [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue")
 style format string. The format can be _NULL_, indicating that no arguments are provided.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

This is the equivalent of the Python expression: `callable(*args)`.

Note that if you only pass [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* args, [`PyObject_CallFunctionObjArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallFunctionObjArgs "PyObject_CallFunctionObjArgs")
 is a faster alternative.

Changed in version 3.4: The type of _format_ was changed from `char *`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_CallMethod([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, const char \*name, const char \*format, ...)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethod "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Call the method named _name_ of object _obj_ with a variable number of C arguments. The C arguments are described by a [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue")
 format string that should produce a tuple.

The format can be _NULL_, indicating that no arguments are provided.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

This is the equivalent of the Python expression: `obj.name(arg1, arg2, ...)`.

Note that if you only pass [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* args, [`PyObject_CallMethodObjArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethodObjArgs "PyObject_CallMethodObjArgs")
 is a faster alternative.

Changed in version 3.4: The types of _name_ and _format_ were changed from `char *`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_CallFunctionObjArgs([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, ...)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_CallFunctionObjArgs "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Call a callable Python object _callable_, with a variable number of [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* arguments. The arguments are provided as a variable number of parameters followed by _NULL_.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

This is the equivalent of the Python expression: `callable(arg1, arg2, ...)`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_CallMethodObjArgs([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, ...)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethodObjArgs "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Call a method of the Python object _obj_, where the name of the method is given as a Python string object in _name_. It is called with a variable number of [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* arguments. The arguments are provided as a variable number of parameters followed by _NULL_.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_CallMethodNoArgs([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethodNoArgs "Link to this definition")
  

Call a method of the Python object _obj_ without arguments, where the name of the method is given as a Python string object in _name_.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

Added in version 3.9.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_CallMethodOneArg([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*arg)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethodOneArg "Link to this definition")
  

Call a method of the Python object _obj_ with a single positional argument _arg_, where the name of the method is given as a Python string object in _name_.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

Added in version 3.9.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_Vectorcall([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*const \*args, size\_t nargsf, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*kwnames)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_Vectorcall "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Call a callable Python object _callable_. The arguments are the same as for [`vectorcallfunc`](https://docs.python.org/3/c-api/call.html#c.vectorcallfunc "vectorcallfunc")
. If _callable_ supports [vectorcall](https://docs.python.org/3/c-api/call.html#vectorcall)
, this directly calls the vectorcall function stored in _callable_.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

Added in version 3.8: as `_PyObject_Vectorcall`

Changed in version 3.9: Renamed to the current name, without the leading underscore. The old provisional name is [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_VectorcallDict([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*callable, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*const \*args, size\_t nargsf, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*kwdict)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_VectorcallDict "Link to this definition")
  

Call _callable_ with positional arguments passed exactly as in the [vectorcall](https://docs.python.org/3/c-api/call.html#vectorcall)
 protocol, but with keyword arguments passed as a dictionary _kwdict_. The _args_ array contains only the positional arguments.

Regardless of which protocol is used internally, a conversion of arguments needs to be done. Therefore, this function should only be used if the caller already has a dictionary ready to use for the keyword arguments, but not a tuple for the positional arguments.

Added in version 3.9.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyObject\_VectorcallMethod([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*const \*args, size\_t nargsf, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*kwnames)[¶](https://docs.python.org/3/c-api/call.html#c.PyObject_VectorcallMethod "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.12._

Call a method using the vectorcall calling convention. The name of the method is given as a Python string _name_. The object whose method is called is _args\[0\]_, and the _args_ array starting at _args\[1\]_ represents the arguments of the call. There must be at least one positional argument. _nargsf_ is the number of positional arguments including _args\[0\]_, plus [`PY_VECTORCALL_ARGUMENTS_OFFSET`](https://docs.python.org/3/c-api/call.html#c.PY_VECTORCALL_ARGUMENTS_OFFSET "PY_VECTORCALL_ARGUMENTS_OFFSET")
 if the value of `args[0]` may temporarily be changed. Keyword arguments can be passed just like in [`PyObject_Vectorcall()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Vectorcall "PyObject_Vectorcall")
.

If the object has the [`Py_TPFLAGS_METHOD_DESCRIPTOR`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_METHOD_DESCRIPTOR "Py_TPFLAGS_METHOD_DESCRIPTOR")
 feature, this will call the unbound method object with the full _args_ vector as arguments.

Return the result of the call on success, or raise an exception and return _NULL_ on failure.

Added in version 3.9.

Call Support API[¶](https://docs.python.org/3/c-api/call.html#call-support-api "Link to this heading")

-------------------------------------------------------------------------------------------------------

int PyCallable\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/call.html#c.PyCallable_Check "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Determine if the object _o_ is callable. Return `1` if the object is callable and `0` otherwise. This function always succeeds.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Call Protocol](https://docs.python.org/3/c-api/call.html#)
    *   [The _tp\_call_ Protocol](https://docs.python.org/3/c-api/call.html#the-tp-call-protocol)
        
    *   [The Vectorcall Protocol](https://docs.python.org/3/c-api/call.html#the-vectorcall-protocol)
        *   [Recursion Control](https://docs.python.org/3/c-api/call.html#recursion-control)
            
        *   [Vectorcall Support API](https://docs.python.org/3/c-api/call.html#vectorcall-support-api)
            
    *   [Object Calling API](https://docs.python.org/3/c-api/call.html#object-calling-api)
        
    *   [Call Support API](https://docs.python.org/3/c-api/call.html#call-support-api)
        

#### Previous topic

[Object Protocol](https://docs.python.org/3/c-api/object.html "previous chapter")

#### Next topic

[Number Protocol](https://docs.python.org/3/c-api/number.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Call+Protocol&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fcall.html&pagesource=c-api%2Fcall.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/call.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/number.html "Number Protocol")
     |
*   [previous](https://docs.python.org/3/c-api/object.html "Object Protocol")
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
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
     »
*   [Call Protocol](https://docs.python.org/3/c-api/call.html)
    
*    
    
    |
*   Theme Auto Light Dark |