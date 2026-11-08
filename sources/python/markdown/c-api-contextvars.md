### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/typehints.html "Objects for Type Hinting")
     |
*   [previous](https://docs.python.org/3/c-api/coro.html "Coroutine Objects")
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
*   [Context Variables Objects](https://docs.python.org/3/c-api/contextvars.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Context Variables Objects[¶](https://docs.python.org/3/c-api/contextvars.html#context-variables-objects "Link to this heading")

================================================================================================================================

Added in version 3.7.

Changed in version 3.7.1:

Note

In Python 3.7.1 the signatures of all context variables C APIs were **changed** to use [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 pointers instead of [`PyContext`](https://docs.python.org/3/c-api/contextvars.html#c.PyContext "PyContext")
, [`PyContextVar`](https://docs.python.org/3/c-api/contextvars.html#c.PyContextVar "PyContextVar")
, and [`PyContextToken`](https://docs.python.org/3/c-api/contextvars.html#c.PyContextToken "PyContextToken")
, e.g.:

// in 3.7.0:
PyContext \*PyContext\_New(void);

// in 3.7.1+:
PyObject \*PyContext\_New(void);

See [bpo-34762](https://bugs.python.org/issue?@action=redirect&bpo=34762)
 for more details.

This section details the public C API for the [`contextvars`](https://docs.python.org/3/library/contextvars.html#module-contextvars "contextvars: Context Variables")
 module.

type PyContext[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext "Link to this definition")
  

The C structure used to represent a [`contextvars.Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
 object.

type PyContextVar[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextVar "Link to this definition")
  

The C structure used to represent a [`contextvars.ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar")
 object.

type PyContextToken[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextToken "Link to this definition")
  

The C structure used to represent a [`contextvars.Token`](https://docs.python.org/3/library/contextvars.html#contextvars.Token "contextvars.Token")
 object.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyContext\_Type[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_Type "Link to this definition")
  

The type object representing the _context_ type.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyContextVar\_Type[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextVar_Type "Link to this definition")
  

The type object representing the _context variable_ type.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyContextToken\_Type[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextToken_Type "Link to this definition")
  

The type object representing the _context variable token_ type.

Type-check macros:

int PyContext\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_CheckExact "Link to this definition")
  

Return true if _o_ is of type [`PyContext_Type`](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_Type "PyContext_Type")
. _o_ must not be `NULL`. This function always succeeds.

int PyContextVar\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextVar_CheckExact "Link to this definition")
  

Return true if _o_ is of type [`PyContextVar_Type`](https://docs.python.org/3/c-api/contextvars.html#c.PyContextVar_Type "PyContextVar_Type")
. _o_ must not be `NULL`. This function always succeeds.

int PyContextToken\_CheckExact([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*o)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextToken_CheckExact "Link to this definition")
  

Return true if _o_ is of type [`PyContextToken_Type`](https://docs.python.org/3/c-api/contextvars.html#c.PyContextToken_Type "PyContextToken_Type")
. _o_ must not be `NULL`. This function always succeeds.

Context object management functions:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyContext\_New(void)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_New "Link to this definition")
  

_Return value: New reference._

Create a new empty context object. Returns `NULL` if an error has occurred.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyContext\_Copy([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ctx)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_Copy "Link to this definition")
  

_Return value: New reference._

Create a shallow copy of the passed _ctx_ context object. Returns `NULL` if an error has occurred.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyContext\_CopyCurrent(void)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_CopyCurrent "Link to this definition")
  

_Return value: New reference._

Create a shallow copy of the current thread context. Returns `NULL` if an error has occurred.

int PyContext\_Enter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ctx)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_Enter "Link to this definition")
  

Set _ctx_ as the current context for the current thread. Returns `0` on success, and `-1` on error.

int PyContext\_Exit([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*ctx)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_Exit "Link to this definition")
  

Deactivate the _ctx_ context and restore the previous context as the current context for the current thread. Returns `0` on success, and `-1` on error.

int PyContext\_AddWatcher([PyContext\_WatchCallback](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_WatchCallback "PyContext_WatchCallback")
 callback)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_AddWatcher "Link to this definition")
  

Register _callback_ as a context object watcher for the current interpreter. Return an ID which may be passed to [`PyContext_ClearWatcher()`](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_ClearWatcher "PyContext_ClearWatcher")
. In case of error (e.g. no more watcher IDs available), return `-1` and set an exception.

Added in version 3.14.

int PyContext\_ClearWatcher(int watcher\_id)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_ClearWatcher "Link to this definition")
  

Clear watcher identified by _watcher\_id_ previously returned from [`PyContext_AddWatcher()`](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_AddWatcher "PyContext_AddWatcher")
 for the current interpreter. Return `0` on success, or `-1` and set an exception on error (e.g. if the given _watcher\_id_ was never registered.)

Added in version 3.14.

type PyContextEvent[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextEvent "Link to this definition")
  

Enumeration of possible context object watcher events:

*   `Py_CONTEXT_SWITCHED`: The [current context](https://docs.python.org/3/glossary.html#term-current-context)
     has switched to a different context. The object passed to the watch callback is the now-current [`contextvars.Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
     object, or None if no context is current.
    

Added in version 3.14.

typedef int (\*PyContext\_WatchCallback)([PyContextEvent](https://docs.python.org/3/c-api/contextvars.html#c.PyContextEvent "PyContextEvent")
 event, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContext_WatchCallback "Link to this definition")
  

Context object watcher callback function. The object passed to the callback is event-specific; see [`PyContextEvent`](https://docs.python.org/3/c-api/contextvars.html#c.PyContextEvent "PyContextEvent")
 for details.

If the callback returns with an exception set, it must return `-1`; this exception will be printed as an unraisable exception using [`PyErr_FormatUnraisable()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_FormatUnraisable "PyErr_FormatUnraisable")
. Otherwise it should return `0`.

There may already be a pending exception set on entry to the callback. In this case, the callback should return `0` with the same exception still set. This means the callback may not call any other API that can set an exception unless it saves and clears the exception state first, and restores it before returning.

Added in version 3.14.

Context variable functions:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyContextVar\_New(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*def)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextVar_New "Link to this definition")
  

_Return value: New reference._

Create a new `ContextVar` object. The _name_ parameter is used for introspection and debug purposes. The _def_ parameter specifies a default value for the context variable, or `NULL` for no default. If an error has occurred, this function returns `NULL`.

int PyContextVar\_Get([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*var, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*default\_value, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*\*value)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextVar_Get "Link to this definition")
  

Get the value of a context variable. Returns `-1` if an error has occurred during lookup, and `0` if no error occurred, whether or not a value was found.

If the context variable was found, _value_ will be a pointer to it. If the context variable was _not_ found, _value_ will point to:

*   _default\_value_, if not `NULL`;
    
*   the default value of _var_, if not `NULL`;
    
*   `NULL`
    

Except for `NULL`, the function returns a new reference.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyContextVar\_Set([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*var, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextVar_Set "Link to this definition")
  

_Return value: New reference._

Set the value of _var_ to _value_ in the current context. Returns a new token object for this change, or `NULL` if an error has occurred.

int PyContextVar\_Reset([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*var, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*token)[¶](https://docs.python.org/3/c-api/contextvars.html#c.PyContextVar_Reset "Link to this definition")
  

Reset the state of the _var_ context variable to that it was in before [`PyContextVar_Set()`](https://docs.python.org/3/c-api/contextvars.html#c.PyContextVar_Set "PyContextVar_Set")
 that returned the _token_ was called. This function returns `0` on success and `-1` on error.

#### Previous topic

[Coroutine Objects](https://docs.python.org/3/c-api/coro.html "previous chapter")

#### Next topic

[Objects for Type Hinting](https://docs.python.org/3/c-api/typehints.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Context+Variables+Objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fcontextvars.html&pagesource=c-api%2Fcontextvars.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/contextvars.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/typehints.html "Objects for Type Hinting")
     |
*   [previous](https://docs.python.org/3/c-api/coro.html "Coroutine Objects")
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
*   [Context Variables Objects](https://docs.python.org/3/c-api/contextvars.html)
    
*    
    
    |
*   Theme Auto Light Dark |