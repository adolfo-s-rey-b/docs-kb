### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/codec.html "Codec registry and support functions")
     |
*   [previous](https://docs.python.org/3/c-api/hash.html "PyHash API")
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
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Reflection](https://docs.python.org/3/c-api/reflection.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Reflection[¶](https://docs.python.org/3/c-api/reflection.html#reflection "Link to this heading")

=================================================================================================

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyEval\_GetBuiltins(void)[¶](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetBuiltins "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Deprecated since version 3.13: Use [`PyEval_GetFrameBuiltins()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameBuiltins "PyEval_GetFrameBuiltins")
 instead.

Return a dictionary of the builtins in the current execution frame, or the interpreter of the thread state if no frame is currently executing.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyEval\_GetLocals(void)[¶](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetLocals "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Deprecated since version 3.13: Use either [`PyEval_GetFrameLocals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameLocals "PyEval_GetFrameLocals")
 to obtain the same behaviour as calling [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
 in Python code, or else call [`PyFrame_GetLocals()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals")
 on the result of [`PyEval_GetFrame()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrame "PyEval_GetFrame")
 to access the [`f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 attribute of the currently executing frame.

Return a mapping providing access to the local variables in the current execution frame, or `NULL` if no frame is currently executing.

Refer to [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
 for details of the mapping returned at different scopes.

As this function returns a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
, the dictionary returned for [optimized scopes](https://docs.python.org/3/glossary.html#term-optimized-scope)
 is cached on the frame object and will remain alive as long as the frame object does. Unlike [`PyEval_GetFrameLocals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameLocals "PyEval_GetFrameLocals")
 and [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
, subsequent calls to this function in the same frame will update the contents of the cached dictionary to reflect changes in the state of the local variables rather than returning a new snapshot.

Changed in version 3.13: As part of [**PEP 667**](https://peps.python.org/pep-0667/)
, [`PyFrame_GetLocals()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals")
, [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
, and [`FrameType.f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 no longer make use of the shared cache dictionary. Refer to the [What’s New entry](https://docs.python.org/3/whatsnew/3.13.html#whatsnew313-locals-semantics)
 for additional details.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyEval\_GetGlobals(void)[¶](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetGlobals "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Deprecated since version 3.13: Use [`PyEval_GetFrameGlobals()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameGlobals "PyEval_GetFrameGlobals")
 instead.

Return a dictionary of the global variables in the current execution frame, or `NULL` if no frame is currently executing.

[PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*PyEval\_GetFrame(void)[¶](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrame "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
’s frame, which is `NULL` if no frame is currently executing.

See also [`PyThreadState_GetFrame()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_GetFrame "PyThreadState_GetFrame")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyEval\_GetFrameBuiltins(void)[¶](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameBuiltins "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Return a dictionary of the builtins in the current execution frame, or the interpreter of the thread state if no frame is currently executing.

Added in version 3.13.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyEval\_GetFrameLocals(void)[¶](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameLocals "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Return a dictionary of the local variables in the current execution frame, or `NULL` if no frame is currently executing. Equivalent to calling [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")
 in Python code.

To access [`f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")
 on the current frame without making an independent snapshot in [optimized scopes](https://docs.python.org/3/glossary.html#term-optimized-scope)
, call [`PyFrame_GetLocals()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLocals "PyFrame_GetLocals")
 on the result of [`PyEval_GetFrame()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrame "PyEval_GetFrame")
.

Added in version 3.13.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyEval\_GetFrameGlobals(void)[¶](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFrameGlobals "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Return a dictionary of the global variables in the current execution frame, or `NULL` if no frame is currently executing. Equivalent to calling [`globals()`](https://docs.python.org/3/builtins/functions.html#globals "globals")
 in Python code.

Added in version 3.13.

const char \*PyEval\_GetFuncName([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func)[¶](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFuncName "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the name of _func_ if it is a function, class or instance object, else the name of _func_s type.

For a Python function or method, the returned pointer refers to the function’s name and must not be retained across operations that may change that name. In the free-threaded build, copy the string before detaching the thread state or executing Python code if the name may be modified concurrently.

const char \*PyEval\_GetFuncDesc([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*func)[¶](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFuncDesc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a description string, depending on the type of _func_. Return values include “()” for functions and methods, “ constructor”, “ instance”, and “ object”. Concatenated with the result of [`PyEval_GetFuncName()`](https://docs.python.org/3/c-api/reflection.html#c.PyEval_GetFuncName "PyEval_GetFuncName")
, the result will be a description of _func_.

#### Previous topic

[PyHash API](https://docs.python.org/3/c-api/hash.html "previous chapter")

#### Next topic

[Codec registry and support functions](https://docs.python.org/3/c-api/codec.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Reflection&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Freflection.html&pagesource=c-api%2Freflection.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/reflection.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/codec.html "Codec registry and support functions")
     |
*   [previous](https://docs.python.org/3/c-api/hash.html "PyHash API")
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
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Reflection](https://docs.python.org/3/c-api/reflection.html)
    
*    
    
    |
*   Theme Auto Light Dark |