### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/_thread.html "_thread — Low-level threading API")
     |
*   [previous](https://docs.python.org/3/library/queue.html "queue — A synchronized queue class")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Concurrent Execution](https://docs.python.org/3/library/concurrency.html)
     »
*   [`contextvars` — Context Variables](https://docs.python.org/3/library/contextvars.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`contextvars` — Context Variables[¶](https://docs.python.org/3/library/contextvars.html#module-contextvars "Link to this heading")

===================================================================================================================================

* * *

This module provides APIs to manage, store, and access context-local state. The [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar")
 class is used to declare and work with _Context Variables_. The [`copy_context()`](https://docs.python.org/3/library/contextvars.html#contextvars.copy_context "contextvars.copy_context")
 function and the [`Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
 class should be used to manage the current context in asynchronous frameworks.

Context managers that have state should use Context Variables instead of [`threading.local()`](https://docs.python.org/3/library/threading.html#threading.local "threading.local")
 to prevent their state from bleeding to other code unexpectedly, when used in concurrent code.

See also [**PEP 567**](https://peps.python.org/pep-0567/)
 for additional details.

Added in version 3.7.

Context Variables[¶](https://docs.python.org/3/library/contextvars.html#context-variables "Link to this heading")

------------------------------------------------------------------------------------------------------------------

class contextvars.ContextVar(_name_\[, _\*_, _default_\])[¶](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "Link to this definition")

This class is used to declare a new Context Variable, e.g.:

Copy

var: ContextVar\[int\] \= ContextVar('var', default\=42)

The required _name_ parameter is used for introspection and debug purposes.

The optional keyword-only _default_ parameter is returned by [`ContextVar.get()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.get "contextvars.ContextVar.get")
 when no value for the variable is found in the current context.

**Important:** Context Variables should be created at the top module level and never in closures. [`Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
 objects hold strong references to context variables which prevents context variables from being properly garbage collected.

`ContextVar`s are [generic](https://docs.python.org/3/library/typing.html#generics)
 over the type of their contained value.

name[¶](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.name "Link to this definition")

The name of the variable. This is a read-only property.

Added in version 3.7.1.

get(\[_default_\])[¶](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.get "Link to this definition")

Return a value for the context variable for the current context.

If there is no value for the variable in the current context, the method will:

*   return the value of the _default_ argument of the method, if provided; or
    
*   return the default value for the context variable, if it was created with one; or
    
*   raise a [`LookupError`](https://docs.python.org/3/builtins/exceptions.html#LookupError "LookupError")
    .
    

set(_value_)[¶](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.set "Link to this definition")

Call to set a new value for the context variable in the current context.

The required _value_ argument is the new value for the context variable.

Returns a [`Token`](https://docs.python.org/3/library/contextvars.html#contextvars.Token "contextvars.Token")
 object that can be used to restore the variable to its previous value via the [`ContextVar.reset()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.reset "contextvars.ContextVar.reset")
 method.

For convenience, the token object can be used as a context manager to avoid calling [`ContextVar.reset()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.reset "contextvars.ContextVar.reset")
 manually:

Copy

var \= ContextVar('var', default\='default value')

with var.set('new value'):
    assert var.get() \== 'new value'

assert var.get() \== 'default value'

It is a shorthand for:

Copy

var \= ContextVar('var', default\='default value')

token \= var.set('new value')
try:
    assert var.get() \== 'new value'
finally:
    var.reset(token)

assert var.get() \== 'default value'

Added in version 3.14: Added support for using tokens as context managers.

reset(_token_)[¶](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.reset "Link to this definition")

Reset the context variable to the value it had before the [`ContextVar.set()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.set "contextvars.ContextVar.set")
 that created the _token_ was used.

For example:

Copy

var \= ContextVar('var')

token \= var.set('new value')
\# code that uses 'var'; var.get() returns 'new value'.
var.reset(token)

\# After the reset call the var has no value again, so
\# var.get() would raise a LookupError.

The same _token_ cannot be used twice.

class contextvars.Token[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Token "Link to this definition")

_Token_ objects are returned by the [`ContextVar.set()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.set "contextvars.ContextVar.set")
 method. They can be passed to the [`ContextVar.reset()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.reset "contextvars.ContextVar.reset")
 method to revert the value of the variable to what it was before the corresponding _set_. A single token cannot reset a context variable more than once.

Tokens support the [context manager protocol](https://docs.python.org/3/reference/datamodel.html#context-managers)
 to automatically reset context variables. See [`ContextVar.set()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.set "contextvars.ContextVar.set")
.

Tokens are [generic](https://docs.python.org/3/library/typing.html#generics)
 over the same type as the [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar")
 which created them.

Added in version 3.14: Added support for usage as a context manager.

var[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Token.var "Link to this definition")

A read-only property. Points to the [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar")
 object that created the token.

old\_value[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Token.old_value "Link to this definition")

A read-only property. Set to the value the variable had before the [`ContextVar.set()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.set "contextvars.ContextVar.set")
 method call that created the token. It points to [`Token.MISSING`](https://docs.python.org/3/library/contextvars.html#contextvars.Token.MISSING "contextvars.Token.MISSING")
 if the variable was not set before the call.

MISSING[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Token.MISSING "Link to this definition")

A marker object used by [`Token.old_value`](https://docs.python.org/3/library/contextvars.html#contextvars.Token.old_value "contextvars.Token.old_value")
.

Manual Context Management[¶](https://docs.python.org/3/library/contextvars.html#manual-context-management "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

contextvars.copy\_context()[¶](https://docs.python.org/3/library/contextvars.html#contextvars.copy_context "Link to this definition")

Returns a copy of the current [`Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
 object.

The following snippet gets a copy of the current context and prints all variables and their values that are set in it:

Copy

ctx: Context \= copy\_context()
print(list(ctx.items()))

The function has an _O_(1) complexity, i.e. works equally fast for contexts with a few context variables and for contexts that have a lot of them.

class contextvars.Context[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context "Link to this definition")

A mapping of [`ContextVars`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar")
 to their values.

`Context()` creates an empty context with no values in it. To get a copy of the current context use the [`copy_context()`](https://docs.python.org/3/library/contextvars.html#contextvars.copy_context "contextvars.copy_context")
 function.

Each thread has its own effective stack of `Context` objects. The [current context](https://docs.python.org/3/glossary.html#term-current-context)
 is the `Context` object at the top of the current thread’s stack. All `Context` objects in the stacks are considered to be _entered_.

_Entering_ a context, which can be done by calling its [`run()`](https://docs.python.org/3/library/contextvars.html#contextvars.Context.run "contextvars.Context.run")
 method, makes the context the current context by pushing it onto the top of the current thread’s context stack.

_Exiting_ from the current context, which can be done by returning from the callback passed to the [`run()`](https://docs.python.org/3/library/contextvars.html#contextvars.Context.run "contextvars.Context.run")
 method, restores the current context to what it was before the context was entered by popping the context off the top of the context stack.

Since each thread has its own context stack, [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar")
 objects behave in a similar fashion to [`threading.local()`](https://docs.python.org/3/library/threading.html#threading.local "threading.local")
 when values are assigned in different threads.

Attempting to enter an already entered context, including contexts entered in other threads, raises a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
.

After exiting a context, it can later be re-entered (from any thread).

Any changes to [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar")
 values via the [`ContextVar.set()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.set "contextvars.ContextVar.set")
 method are recorded in the current context. The [`ContextVar.get()`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar.get "contextvars.ContextVar.get")
 method returns the value associated with the current context. Exiting a context effectively reverts any changes made to context variables while the context was entered (if needed, the values can be restored by re-entering the context).

Context implements the [`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping")
 interface.

run(_callable_, _\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.run "Link to this definition")

Enters the Context, executes `callable(*args, **kwargs)`, then exits the Context. Returns _callable_’s return value, or propagates an exception if one occurred.

Example:

Copy

import contextvars

var \= contextvars.ContextVar('var')
var.set('spam')
print(var.get())  \# 'spam'

ctx \= contextvars.copy\_context()

def main():
    \# 'var' was set to 'spam' before
    \# calling 'copy\_context()' and 'ctx.run(main)', so:
    print(var.get())  \# 'spam'
    print(ctx\[var\])  \# 'spam'

    var.set('ham')

    \# Now, after setting 'var' to 'ham':
    print(var.get())  \# 'ham'
    print(ctx\[var\])  \# 'ham'

\# Any changes that the 'main' function makes to 'var'
\# will be contained in 'ctx'.
ctx.run(main)

\# The 'main()' function was run in the 'ctx' context,
\# so changes to 'var' are contained in it:
print(ctx\[var\])  \# 'ham'

\# However, outside of 'ctx', 'var' is still set to 'spam':
print(var.get())  \# 'spam'

copy()[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.copy "Link to this definition")

Return a shallow copy of the context object.

var in context

Return `True` if the _context_ has a value for _var_ set; return `False` otherwise.

context\[var\]

Return the value of the _var_ [`ContextVar`](https://docs.python.org/3/library/contextvars.html#contextvars.ContextVar "contextvars.ContextVar")
 variable. If the variable is not set in the context object, a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is raised.

get(_var_\[, _default_\])[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.get "Link to this definition")

Return the value for _var_ if _var_ has the value in the context object. Return _default_ otherwise. If _default_ is not given, return `None`.

iter(context)

Return an iterator over the variables stored in the context object.

len(proxy)

Return the number of variables set in the context object.

keys()[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.keys "Link to this definition")

Return a list of all variables in the context object.

values()[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.values "Link to this definition")

Return a list of all variables’ values in the context object.

items()[¶](https://docs.python.org/3/library/contextvars.html#contextvars.Context.items "Link to this definition")

Return a list of 2-tuples containing all variables and their values in the context object.

asyncio support[¶](https://docs.python.org/3/library/contextvars.html#asyncio-support "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Context variables are natively supported in [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
 and are ready to be used without any extra configuration. For example, here is a simple echo server, that uses a context variable to make the address of a remote client available in the Task that handles that client:

Copy

import asyncio
import contextvars

client\_addr\_var \= contextvars.ContextVar('client\_addr')

def render\_goodbye():
    \# The address of the currently handled client can be accessed
    \# without passing it explicitly to this function.

    client\_addr \= client\_addr\_var.get()
    return f'Good bye, client @ {client\_addr}\\r\\n'.encode()

async def handle\_request(reader, writer):
    addr \= writer.transport.get\_extra\_info('socket').getpeername()
    client\_addr\_var.set(addr)

    \# In any code that we call, it is now possible to get the
    \# client's address by calling 'client\_addr\_var.get()'.

    while True:
        line \= await reader.readline()
        print(line)
        if not line.strip():
            break

    writer.write(b'HTTP/1.1 200 OK\\r\\n')  \# status line
    writer.write(b'\\r\\n')  \# headers
    writer.write(render\_goodbye())  \# body
    writer.close()

async def main():
    srv \= await asyncio.start\_server(
        handle\_request, '127.0.0.1', 8081)

    async with srv:
        await srv.serve\_forever()

asyncio.run(main())

\# To test it you can use telnet or curl:
\#     telnet 127.0.0.1 8081
\#     curl 127.0.0.1:8081

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`contextvars` — Context Variables](https://docs.python.org/3/library/contextvars.html#)
    *   [Context Variables](https://docs.python.org/3/library/contextvars.html#context-variables)
        
    *   [Manual Context Management](https://docs.python.org/3/library/contextvars.html#manual-context-management)
        
    *   [asyncio support](https://docs.python.org/3/library/contextvars.html#asyncio-support)
        

#### Previous topic

[`queue` — A synchronized queue class](https://docs.python.org/3/library/queue.html "previous chapter")

#### Next topic

[`_thread` — Low-level threading API](https://docs.python.org/3/library/_thread.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=contextvars+%E2%80%94+Context+Variables&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcontextvars.html&pagesource=library%2Fcontextvars.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/contextvars.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/_thread.html "_thread — Low-level threading API")
     |
*   [previous](https://docs.python.org/3/library/queue.html "queue — A synchronized queue class")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Concurrent Execution](https://docs.python.org/3/library/concurrency.html)
     »
*   [`contextvars` — Context Variables](https://docs.python.org/3/library/contextvars.html)
    
*    
    
    |
*   Theme Auto Light Dark |