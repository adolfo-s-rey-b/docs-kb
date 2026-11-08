### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/gen.html "Generator Objects")
     |
*   [previous](https://docs.python.org/3/c-api/sentinel.html "Sentinel objects")
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
*   [Frame objects](https://docs.python.org/3/c-api/frame.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Frame objects[¶](https://docs.python.org/3/c-api/frame.html#frame-objects "Link to this heading")

==================================================================================================

type PyFrameObject[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (as an opaque struct)._

The C structure of the objects used to describe frame objects.

There are no public members in this structure.

Changed in version 3.11: The members of this structure were removed from the public C API. Refer to the [What’s New entry](https://docs.python.org/3/whatsnew/3.11.html#pyframeobject-3-11-hiding)
 for details.

The [`PyEval_GetFrame()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrame "PyEval_GetFrame")
 and [`PyThreadState_GetFrame()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetFrame "PyThreadState_GetFrame")
 functions can be used to get a frame object.

See also [Reflection](https://docs.python.org/3/c-api/reflection.html#reflection)
.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyFrame\_Type[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_Type "Link to this definition")
  

The type of frame objects. It is the same object as [`types.FrameType`](https://docs.python.org/3/library/types.html#types.FrameType "types.FrameType")
 in the Python layer.

Changed in version 3.11: Previously, this type was only available after including `<frameobject.h>`.

[PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*PyFrame\_New([PyThreadState](https://docs.python.org/3/c-api/threads.html#c.PyThreadState "PyThreadState")
 \*tstate, [PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*code, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_New "Link to this definition")
  

Create a new frame object. This function returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the new frame object on success, and returns `NULL` with an exception set on failure.

int PyFrame\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_Check "Link to this definition")
  

Return non-zero if _obj_ is a frame object.

Changed in version 3.11: Previously, this function was only available after including `<frameobject.h>`.

[PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*PyFrame\_GetBack([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetBack "Link to this definition")
  

_Return value: New reference._

Get the _frame_ next outer frame.

Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
, or `NULL` if _frame_ has no outer frame. This raises no exceptions.

Added in version 3.9.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFrame\_GetBuiltins([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetBuiltins "Link to this definition")
  

_Return value: New reference._

Get the _frame_’s [`f_builtins`](https://docs.python.org/3/reference/datamodel.html#frame.f_builtins "frame.f_builtins")
 attribute.

Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
. The result cannot be `NULL`.

Added in version 3.11.

[PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*PyFrame\_GetCode([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetCode "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Get the _frame_ code.

Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
.

The result (frame code) cannot be `NULL`.

Added in version 3.9.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFrame\_GetGenerator([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetGenerator "Link to this definition")
  

_Return value: New reference._

Get the generator, coroutine, or async generator that owns this frame, or `NULL` if this frame is not owned by a generator. Does not raise an exception, even if the return value is `NULL`.

Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
, or `NULL`.

Added in version 3.11.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFrame\_GetGlobals([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetGlobals "Link to this definition")
  

_Return value: New reference._

Get the _frame_’s [`f_globals`](https://docs.python.org/3/reference/datamodel.html#frame.f_globals "frame.f_globals")
 attribute.

Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
. The result cannot be `NULL`.

Added in version 3.11.

int PyFrame\_GetLasti([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLasti "Link to this definition")
  

Get the _frame_’s [`f_lasti`](https://docs.python.org/3/reference/datamodel.html#frame.f_lasti "frame.f_lasti")
 attribute.

Added in version 3.11.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFrame\_GetVar([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetVar "Link to this definition")
  

_Return value: New reference._

Get the variable _name_ of _frame_.

*   Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
     to the variable value on success.
    
*   Raise [`NameError`](https://docs.python.org/3/builtins/exceptions.html#NameError "NameError")
     and return `NULL` if the variable does not exist.
    
*   Raise an exception and return `NULL` on error.
    

_name_ type must be a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
.

Added in version 3.12.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFrame\_GetVarString([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame, const char \*name)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetVarString "Link to this definition")
  

_Return value: New reference._

Similar to [`PyFrame_GetVar()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetVar "PyFrame_GetVar")
, but the variable name is a C string encoded in UTF-8.

Added in version 3.12.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyFrame\_GetLocals([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLocals "Link to this definition")
  

_Return value: New reference._

Get the _frame_’s [`f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 attribute. If the frame refers to an [optimized scope](https://docs.python.org/3/glossary.html#term-optimized-scope)
, this returns a write-through proxy object that allows modifying the locals. In all other cases (classes, modules, [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
, [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
) it returns the mapping representing the frame locals directly (as described for [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
).

Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
.

Added in version 3.11.

Changed in version 3.13: As part of [**PEP 667**](https://peps.python.org/pep-0667/)
, return an instance of [`PyFrameLocalsProxy_Type`](https://docs.python.org/3/c-api/frame.html#c.PyFrameLocalsProxy_Type "PyFrameLocalsProxy_Type")
.

int PyFrame\_GetLineNumber([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*frame)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLineNumber "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.10._

Return the line number that _frame_ is currently executing.

Frame locals proxies[¶](https://docs.python.org/3/c-api/frame.html#frame-locals-proxies "Link to this heading")

----------------------------------------------------------------------------------------------------------------

Added in version 3.13.

The [`f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 attribute on a [frame object](https://docs.python.org/3/reference/datamodel.html#frame-objects)
 is an instance of a “frame-locals proxy”. The proxy object exposes a write-through view of the underlying locals dictionary for the frame. This ensures that the variables exposed by `f_locals` are always up to date with the live local variables in the frame itself.

See [**PEP 667**](https://peps.python.org/pep-0667/)
 for more information.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyFrameLocalsProxy\_Type[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrameLocalsProxy_Type "Link to this definition")
  

The type of frame [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
 proxy objects.

int PyFrameLocalsProxy\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrameLocalsProxy_Check "Link to this definition")
  

Return non-zero if _obj_ is a frame [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
 proxy.

Legacy local variable APIs[¶](https://docs.python.org/3/c-api/frame.html#legacy-local-variable-apis "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

These APIs are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
. As of Python 3.13, they do nothing. They exist solely for backwards compatibility.

void PyFrame\_LocalsToFast([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*f, int clear)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_LocalsToFast "Link to this definition")
  

Prior to Python 3.13, this function would copy the [`f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 attribute of _f_ to the internal “fast” array of local variables, allowing changes in frame objects to be visible to the interpreter. If _clear_ was true, this function would process variables that were unset in the locals dictionary.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.13: This function now does nothing.

void PyFrame\_FastToLocals([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*f)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_FastToLocals "Link to this definition")
  

Prior to Python 3.13, this function would copy the internal “fast” array of local variables (which is used by the interpreter) to the [`f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 attribute of _f_, allowing changes in local variables to be visible to frame objects.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.13: This function now does nothing.

int PyFrame\_FastToLocalsWithError([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*f)[¶](https://docs.python.org/3/c-api/frame.html#c.PyFrame_FastToLocalsWithError "Link to this definition")
  

Prior to Python 3.13, this function was similar to [`PyFrame_FastToLocals()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_FastToLocals "PyFrame_FastToLocals")
, but would return `0` on success, and `-1` with an exception set on failure.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.13: This function now does nothing.

See also

[**PEP 667**](https://peps.python.org/pep-0667/)

Internal frames[¶](https://docs.python.org/3/c-api/frame.html#internal-frames "Link to this heading")

------------------------------------------------------------------------------------------------------

Unless using [**PEP 523**](https://peps.python.org/pep-0523/)
, you will not need this.

struct \_PyInterpreterFrame[¶](https://docs.python.org/3/c-api/frame.html#c._PyInterpreterFrame "Link to this definition")
  

The interpreter’s internal frame representation.

Added in version 3.11.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyUnstable\_InterpreterFrame\_GetCode(struct [\_PyInterpreterFrame](https://docs.python.org/3/c-api/frame.html#c._PyInterpreterFrame "_PyInterpreterFrame")
 \*frame);[¶](https://docs.python.org/3/c-api/frame.html#c.PyUnstable_InterpreterFrame_GetCode "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

> Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
>  to the code object for the frame.

Added in version 3.12.

int PyUnstable\_InterpreterFrame\_GetLasti(struct [\_PyInterpreterFrame](https://docs.python.org/3/c-api/frame.html#c._PyInterpreterFrame "_PyInterpreterFrame")
 \*frame);[¶](https://docs.python.org/3/c-api/frame.html#c.PyUnstable_InterpreterFrame_GetLasti "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Return the byte offset into the last executed instruction.

Added in version 3.12.

int PyUnstable\_InterpreterFrame\_GetLine(struct [\_PyInterpreterFrame](https://docs.python.org/3/c-api/frame.html#c._PyInterpreterFrame "_PyInterpreterFrame")
 \*frame);[¶](https://docs.python.org/3/c-api/frame.html#c.PyUnstable_InterpreterFrame_GetLine "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Return the currently executing line number, or -1 if there is no line number.

Added in version 3.12.

const [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 \*PyUnstable\_ExecutableKinds[¶](https://docs.python.org/3/c-api/frame.html#c.PyUnstable_ExecutableKinds "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

An array of executable kinds (executor types) for frames, used for internal debugging and tracing.

Tools like debuggers and profilers can use this to identify the type of execution context associated with a frame (such as to filter out internal frames). The entries are indexed by the following constants:

| Constant | Description |
| --- | --- |
| PyUnstable\_EXECUTABLE\_KIND\_SKIP[¶](https://docs.python.org/3/c-api/frame.html#c.PyUnstable_ExecutableKinds.PyUnstable_EXECUTABLE_KIND_SKIP "Link to this definition")<br>  <br><br>_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)<br>. It may change without warning in minor releases._ | The frame is internal (For example: inlined) and should be skipped by tools. |
| PyUnstable\_EXECUTABLE\_KIND\_PY\_FUNCTION[¶](https://docs.python.org/3/c-api/frame.html#c.PyUnstable_ExecutableKinds.PyUnstable_EXECUTABLE_KIND_PY_FUNCTION "Link to this definition")<br>  <br><br>_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)<br>. It may change without warning in minor releases._ | The frame corresponds to a standard Python function. |
| PyUnstable\_EXECUTABLE\_KIND\_BUILTIN\_FUNCTION[¶](https://docs.python.org/3/c-api/frame.html#c.PyUnstable_ExecutableKinds.PyUnstable_EXECUTABLE_KIND_BUILTIN_FUNCTION "Link to this definition")<br>  <br><br>_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)<br>. It may change without warning in minor releases._ | The frame corresponds to a function defined in native code. |
| PyUnstable\_EXECUTABLE\_KIND\_METHOD\_DESCRIPTOR[¶](https://docs.python.org/3/c-api/frame.html#c.PyUnstable_ExecutableKinds.PyUnstable_EXECUTABLE_KIND_METHOD_DESCRIPTOR "Link to this definition")<br>  <br><br>_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)<br>. It may change without warning in minor releases._ | The frame corresponds to a method on a class instance. |

Note that reading the executable kind from a frame is currently only possible with undocumented internal APIs.

Added in version 3.13.

PyUnstable\_EXECUTABLE\_KINDS[¶](https://docs.python.org/3/c-api/frame.html#c.PyUnstable_EXECUTABLE_KINDS "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

The number of entries in [`PyUnstable_ExecutableKinds`](https://docs.python.org/3/c-api/frame.html#c.PyUnstable_ExecutableKinds "PyUnstable_ExecutableKinds")
.

Added in version 3.13.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Frame objects](https://docs.python.org/3/c-api/frame.html#)
    *   [Frame locals proxies](https://docs.python.org/3/c-api/frame.html#frame-locals-proxies)
        
    *   [Legacy local variable APIs](https://docs.python.org/3/c-api/frame.html#legacy-local-variable-apis)
        
    *   [Internal frames](https://docs.python.org/3/c-api/frame.html#internal-frames)
        

#### Previous topic

[Sentinel objects](https://docs.python.org/3/c-api/sentinel.html "previous chapter")

#### Next topic

[Generator Objects](https://docs.python.org/3/c-api/gen.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Frame+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fframe.html&pagesource=c-api%2Fframe.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/frame.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/gen.html "Generator Objects")
     |
*   [previous](https://docs.python.org/3/c-api/sentinel.html "Sentinel objects")
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
*   [Frame objects](https://docs.python.org/3/c-api/frame.html)
    
*    
    
    |
*   Theme Auto Light Dark |