### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/abc.html "abc — Abstract Base Classes")
     |
*   [previous](https://docs.python.org/3/library/dataclasses.html "dataclasses — Data Classes")
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
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)
     »
*   [`contextlib` — Utilities for `with`\-statement contexts](https://docs.python.org/3/library/contextlib.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`contextlib` — Utilities for `with`\-statement contexts[¶](https://docs.python.org/3/library/contextlib.html#module-contextlib "Link to this heading")

=======================================================================================================================================================

**Source code:** [Lib/contextlib.py](https://github.com/python/cpython/tree/3.15/Lib/contextlib.py)

* * *

This module provides utilities for common tasks involving the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement. For more information see also [Context Manager Types](https://docs.python.org/3/builtins/stdtypes.html#typecontextmanager)
 and [With Statement Context Managers](https://docs.python.org/3/reference/datamodel.html#context-managers)
.

Utilities[¶](https://docs.python.org/3/library/contextlib.html#utilities "Link to this heading")

-------------------------------------------------------------------------------------------------

Functions and classes provided:

class contextlib.AbstractContextManager[¶](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractContextManager "Link to this definition")

An [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 for classes that implement [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 and [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
. A default implementation for `__enter__()` is provided which returns `self` while `__exit__()` is an abstract method which by default returns `None`. See also the definition of [Context Manager Types](https://docs.python.org/3/builtins/stdtypes.html#typecontextmanager)
.

Added in version 3.6.

class contextlib.AbstractAsyncContextManager[¶](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractAsyncContextManager "Link to this definition")

An [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class)
 for classes that implement [`__aenter__()`](https://docs.python.org/3/reference/datamodel.html#object.__aenter__ "object.__aenter__")
 and [`__aexit__()`](https://docs.python.org/3/reference/datamodel.html#object.__aexit__ "object.__aexit__")
. A default implementation for `__aenter__()` is provided which returns `self` while `__aexit__()` is an abstract method which by default returns `None`. See also the definition of [Asynchronous Context Managers](https://docs.python.org/3/reference/datamodel.html#async-context-managers)
.

Added in version 3.7.

@contextlib.contextmanager[¶](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager "Link to this definition")

This function is a [decorator](https://docs.python.org/3/glossary.html#term-decorator)
 that can be used to define a factory function for [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement context managers, without needing to create a class or separate [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 and [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 methods.

While many objects natively support use in with statements, sometimes a resource needs to be managed that isn’t a context manager in its own right, and doesn’t implement a `close()` method for use with `contextlib.closing`.

An abstract example would be the following to ensure correct resource management:

Copy

from contextlib import contextmanager

@contextmanager
def managed\_resource(\*args, \*\*kwds):
    \# Code to acquire resource, e.g.:
    resource \= acquire\_resource(\*args, \*\*kwds)
    try:
        yield resource
    finally:
        \# Code to release resource, e.g.:
        release\_resource(resource)

The function can then be used like this:

Copy

\>>> with managed\_resource(timeout\=3600) as resource:
...     \# Resource is released at the end of this block,
...     \# even if code in the block raises an exception

The function being decorated must return a [generator](https://docs.python.org/3/glossary.html#term-generator)
\-iterator when called. This iterator must yield exactly one value, which will be bound to the targets in the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement’s `as` clause, if any.

At the point where the generator yields, the block nested in the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement is executed. The generator is then resumed after the block is exited. If an unhandled exception occurs in the block, it is reraised inside the generator at the point where the yield occurred. Thus, you can use a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
…[`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
…[`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 statement to trap the error (if any), or ensure that some cleanup takes place. If an exception is trapped merely in order to log it or to perform some action (rather than to suppress it entirely), the generator must reraise that exception. Otherwise the generator context manager will indicate to the `with` statement that the exception has been handled, and execution will resume with the statement immediately following the `with` statement.

[`@contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager "contextlib.contextmanager")
 uses [`ContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator "contextlib.ContextDecorator")
 so the context managers it creates can be used as decorators as well as in [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statements. When used as a decorator, a new generator instance is implicitly created on each function call (this allows the otherwise “one-shot” context managers created by `@contextmanager` to meet the requirement that context managers support multiple invocations in order to be used as decorators).

Changed in version 3.2: Use of [`ContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator "contextlib.ContextDecorator")
.

@contextlib.asynccontextmanager[¶](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager "Link to this definition")

Similar to [`@contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager "contextlib.contextmanager")
, but creates an [asynchronous context manager](https://docs.python.org/3/reference/datamodel.html#async-context-managers)
.

This function is a [decorator](https://docs.python.org/3/glossary.html#term-decorator)
 that can be used to define a factory function for [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
 statement asynchronous context managers, without needing to create a class or separate [`__aenter__()`](https://docs.python.org/3/reference/datamodel.html#object.__aenter__ "object.__aenter__")
 and [`__aexit__()`](https://docs.python.org/3/reference/datamodel.html#object.__aexit__ "object.__aexit__")
 methods. It must be applied to an [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)
 function.

A simple example:

Copy

from contextlib import asynccontextmanager

@asynccontextmanager
async def get\_connection():
    conn \= await acquire\_db\_connection()
    try:
        yield conn
    finally:
        await release\_db\_connection(conn)

async def get\_all\_users():
    async with get\_connection() as conn:
        return conn.query('SELECT ...')

Added in version 3.7.

Context managers defined with [`@asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager "contextlib.asynccontextmanager")
 can be used either as decorators or with [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
 statements:

Copy

import time
from contextlib import asynccontextmanager

@asynccontextmanager
async def timeit():
    now \= time.monotonic()
    try:
        yield
    finally:
        print(f'it took {time.monotonic() \- now}s to run')

@timeit()
async def main():
    \# ... async code ...

When used as a decorator, a new generator instance is implicitly created on each function call. This allows the otherwise “one-shot” context managers created by [`@asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager "contextlib.asynccontextmanager")
 to meet the requirement that context managers support multiple invocations in order to be used as decorators.

Changed in version 3.10: Async context managers created with [`@asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager "contextlib.asynccontextmanager")
 can be used as decorators.

contextlib.closing(_thing_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.closing "Link to this definition")

Return a context manager that closes _thing_ upon completion of the block. This is basically equivalent to:

Copy

from contextlib import contextmanager

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()

And lets you write code like this:

Copy

from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

without needing to explicitly close `page`. Even if an error occurs, `page.close()` will be called when the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 block is exited.

Note

Most types managing resources support the [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
 protocol, which closes _thing_ on leaving the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement. As such, `closing()` is most useful for third party types that don’t support context managers. This example is purely for illustration purposes, as [`urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen")
 would normally be used in a context manager.

contextlib.aclosing(_thing_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.aclosing "Link to this definition")

Return an async context manager that calls the `aclose()` method of _thing_ upon completion of the block. This is basically equivalent to:

Copy

from contextlib import asynccontextmanager

@asynccontextmanager
async def aclosing(thing):
    try:
        yield thing
    finally:
        await thing.aclose()

Significantly, `aclosing()` supports deterministic cleanup of async generators when they happen to exit early by [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
 or an exception. For example:

Copy

from contextlib import aclosing

async with aclosing(my\_generator()) as values:
    async for value in values:
        if value \== 42:
            break

This pattern ensures that the generator’s async exit code is executed in the same context as its iterations (so that exceptions and context variables work as expected, and the exit code isn’t run after the lifetime of some task it depends on).

Added in version 3.10.

contextlib.nullcontext(_enter\_result\=None_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.nullcontext "Link to this definition")

Return a context manager that returns _enter\_result_ from [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
, but otherwise does nothing. It is intended to be used as a stand-in for an optional context manager, for example:

Copy

def myfunction(arg, ignore\_exceptions\=False):
    if ignore\_exceptions:
        \# Use suppress to ignore all exceptions.
        cm \= contextlib.suppress(Exception)
    else:
        \# Do not ignore any exceptions, cm has no effect.
        cm \= contextlib.nullcontext()
    with cm:
        \# Do something

An example using _enter\_result_:

Copy

def process\_file(file\_or\_path):
    if isinstance(file\_or\_path, str):
        \# If string, open file
        cm \= open(file\_or\_path)
    else:
        \# Caller is responsible for closing file
        cm \= nullcontext(file\_or\_path)

    with cm as file:
        \# Perform processing on the file

It can also be used as a stand-in for [asynchronous context managers](https://docs.python.org/3/reference/datamodel.html#async-context-managers)
:

Copy

async def send\_http(session\=None):
    if not session:
        \# If no http session, create it with aiohttp
        cm \= aiohttp.ClientSession()
    else:
        \# Caller is responsible for closing the session
        cm \= nullcontext(session)

    async with cm as session:
        \# Send http requests with session

Added in version 3.7.

Changed in version 3.10: [asynchronous context manager](https://docs.python.org/3/glossary.html#term-asynchronous-context-manager)
 support was added.

contextlib.suppress(_\*exceptions_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.suppress "Link to this definition")

Return a context manager that suppresses any of the specified exceptions if they occur in the body of a `with` statement and then resumes execution with the first statement following the end of the `with` statement.

As with any other mechanism that completely suppresses exceptions, this context manager should be used only to cover very specific errors where silently continuing with program execution is known to be the right thing to do.

For example:

Copy

from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('somefile.tmp')

with suppress(FileNotFoundError):
    os.remove('someotherfile.tmp')

This code is equivalent to:

Copy

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

try:
    os.remove('someotherfile.tmp')
except FileNotFoundError:
    pass

This context manager is [reentrant](https://docs.python.org/3/library/contextlib.html#reentrant-cms)
.

If the code within the `with` block raises a [`BaseExceptionGroup`](https://docs.python.org/3/builtins/exceptions.html#BaseExceptionGroup "BaseExceptionGroup")
, suppressed exceptions are removed from the group. Any exceptions of the group which are not suppressed are re-raised in a new group which is created using the original group’s [`derive()`](https://docs.python.org/3/builtins/exceptions.html#BaseExceptionGroup.derive "BaseExceptionGroup.derive")
 method.

Added in version 3.4.

Changed in version 3.12: `suppress` now supports suppressing exceptions raised as part of a [`BaseExceptionGroup`](https://docs.python.org/3/builtins/exceptions.html#BaseExceptionGroup "BaseExceptionGroup")
.

contextlib.redirect\_stdout(_new\_target_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout "Link to this definition")

Context manager for temporarily redirecting [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 to another [file object](https://docs.python.org/3/glossary.html#term-file-object)
.

This tool adds flexibility to existing functions or classes whose output is hardwired to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
.

For example, the output of [`help()`](https://docs.python.org/3/builtins/functions.html#help "help")
 normally is sent to _sys.stdout_. You can capture that output in a string by redirecting the output to an [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")
 object. The replacement stream is returned from the [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 method and so is available as the target of the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement:

Copy

with redirect\_stdout(io.StringIO()) as f:
    help(pow)
s \= f.getvalue()

To send the output of [`help()`](https://docs.python.org/3/builtins/functions.html#help "help")
 to a file on disk, redirect the output to a regular file:

Copy

with open('help.txt', 'w') as f:
    with redirect\_stdout(f):
        help(pow)

To send the output of [`help()`](https://docs.python.org/3/builtins/functions.html#help "help")
 to _sys.stderr_:

Copy

with redirect\_stdout(sys.stderr):
    help(pow)

Note that the global side effect on [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 means that this context manager is not suitable for use in library code and most threaded applications. It also has no effect on the output of subprocesses. However, it is still a useful approach for many utility scripts.

This context manager is [reentrant](https://docs.python.org/3/library/contextlib.html#reentrant-cms)
.

Added in version 3.4.

contextlib.redirect\_stderr(_new\_target_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stderr "Link to this definition")

Similar to [`redirect_stdout()`](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout "contextlib.redirect_stdout")
 but redirecting the global [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 to another [file object](https://docs.python.org/3/glossary.html#term-file-object)
.

This context manager is [reentrant](https://docs.python.org/3/library/contextlib.html#reentrant-cms)
.

Added in version 3.5.

contextlib.chdir(_path_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.chdir "Link to this definition")

Non parallel-safe context manager to change the current working directory. As this changes a global state, the working directory, it is not suitable for use in most threaded or async contexts. It is also not suitable for most non-linear code execution, like generators, where the program execution is temporarily relinquished – unless explicitly desired, you should not yield when this context manager is active.

This is a simple wrapper around [`chdir()`](https://docs.python.org/3/library/os.html#os.chdir "os.chdir")
, it changes the current working directory upon entering and restores the old one on exit.

This context manager is [reentrant](https://docs.python.org/3/library/contextlib.html#reentrant-cms)
.

Added in version 3.11.

class contextlib.ContextDecorator[¶](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator "Link to this definition")

A base class that enables a context manager to also be used as a decorator.

Context managers inheriting from `ContextDecorator` have to implement [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 and [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 as normal. `__exit__` retains its optional exception handling even when used as a decorator.

`ContextDecorator` is used by [`@contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager "contextlib.contextmanager")
, so you get this functionality automatically.

Example of `ContextDecorator`:

Copy

from contextlib import ContextDecorator

class mycontext(ContextDecorator):
    def \_\_enter\_\_(self):
        print('Starting')
        return self

    def \_\_exit\_\_(self, \*exc):
        print('Finishing')
        return False

The class can then be used like this:

Copy

\>>> @mycontext()
... def function():
...     print('The bit in the middle')
...
\>>> function()
Starting
The bit in the middle
Finishing

\>>> with mycontext():
...     print('The bit in the middle')
...
Starting
The bit in the middle
Finishing

This change is just syntactic sugar for any construct of the following form:

Copy

def f():
    with cm():
        \# Do stuff

`ContextDecorator` lets you instead write:

Copy

@cm()
def f():
    \# Do stuff

It makes it clear that the `cm` applies to the whole function, rather than just a piece of it (and saving an indentation level is nice, too).

Existing context managers that already have a base class can be extended by using `ContextDecorator` as a mixin class:

Copy

from contextlib import ContextDecorator

class mycontext(ContextBaseClass, ContextDecorator):
    def \_\_enter\_\_(self):
        return self

    def \_\_exit\_\_(self, \*exc):
        return False

Note

As the decorated function must be able to be called multiple times, the underlying context manager must support use in multiple [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statements. If this is not the case, then the original construct with the explicit `with` statement inside the function should be used.

When the decorated callable is a generator function, coroutine function, or asynchronous generator function, the returned wrapper is of the same kind and keeps the context manager open for the lifetime of the iteration or await rather than only for the call that creates the generator or coroutine object. Wrapped generators and asynchronous generators are explicitly closed when iteration ends, as if by [`closing()`](https://docs.python.org/3/library/contextlib.html#contextlib.closing "contextlib.closing")
 or [`aclosing()`](https://docs.python.org/3/library/contextlib.html#contextlib.aclosing "contextlib.aclosing")
.

Note

For asynchronous generators the wrapper re-yields each value with `async for`; values sent with [`asend()`](https://docs.python.org/3/builtins/stdtypes.html#agen.asend "agen.asend")
 and exceptions thrown with [`athrow()`](https://docs.python.org/3/builtins/stdtypes.html#agen.athrow "agen.athrow")
 are not forwarded to the wrapped generator.

Added in version 3.2.

Changed in version 3.15: Decorating a generator function, coroutine function, or asynchronous generator function now keeps the context manager open across iteration or await. Previously the context manager exited as soon as the generator or coroutine object was created.

class contextlib.AsyncContextDecorator[¶](https://docs.python.org/3/library/contextlib.html#contextlib.AsyncContextDecorator "Link to this definition")

Similar to [`ContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator "contextlib.ContextDecorator")
, but the context manager is entered and exited with [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
. Decorate coroutine functions and asynchronous generator functions with this class; the returned wrapper is of the same kind.

Note

Synchronous functions and generators are accepted, but the wrapper is always asynchronous, so the decorated callable must then be awaited or iterated with `async for`. If that change of calling convention is not intended, use [`ContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator "contextlib.ContextDecorator")
 instead.

Example of `AsyncContextDecorator`:

Copy

from asyncio import run
from contextlib import AsyncContextDecorator

class mycontext(AsyncContextDecorator):
    async def \_\_aenter\_\_(self):
        print('Starting')
        return self

    async def \_\_aexit\_\_(self, \*exc):
        print('Finishing')
        return False

The class can then be used like this:

Copy

\>>> @mycontext()
... async def function():
...     print('The bit in the middle')
...
\>>> run(function())
Starting
The bit in the middle
Finishing

\>>> async def function():
...    async with mycontext():
...         print('The bit in the middle')
...
\>>> run(function())
Starting
The bit in the middle
Finishing

Added in version 3.10.

Changed in version 3.15: Decorating an asynchronous generator function now keeps the context manager open across iteration. Previously the context manager exited as soon as the generator object was created. Synchronous functions and synchronous generator functions are also now accepted, with an asynchronous wrapper returned.

class contextlib.ExitStack[¶](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "Link to this definition")

A context manager that is designed to make it easy to programmatically combine other context managers and cleanup functions, especially those that are optional or otherwise driven by input data.

For example, a set of files may easily be handled in a single with statement as follows:

Copy

with ExitStack() as stack:
    files \= \[stack.enter\_context(open(fname)) for fname in filenames\]
    \# All opened files will automatically be closed at the end of
    \# the with statement, even if attempts to open files later
    \# in the list raise an exception

The [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 method returns the `ExitStack` instance, and performs no additional operations.

Each instance maintains a stack of registered callbacks that are called in reverse order when the instance is closed (either explicitly or implicitly at the end of a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement). Note that callbacks are _not_ invoked implicitly when the context stack instance is garbage collected.

This stack model is used so that context managers that acquire their resources in their `__init__` method (such as file objects) can be handled correctly.

Since registered callbacks are invoked in the reverse order of registration, this ends up behaving as if multiple nested [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statements had been used with the registered set of callbacks. This even extends to exception handling - if an inner callback suppresses or replaces an exception, then outer callbacks will be passed arguments based on that updated state.

This is a relatively low level API that takes care of the details of correctly unwinding the stack of exit callbacks. It provides a suitable foundation for higher level context managers that manipulate the exit stack in application specific ways.

Added in version 3.3.

enter\_context(_cm_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.enter_context "Link to this definition")

Enters a new context manager and adds its [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 method to the callback stack. The return value is the result of the context manager’s own [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 method.

These context managers may suppress exceptions just as they normally would if used directly as part of a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement.

Changed in version 3.11: Raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 instead of [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 if _cm_ is not a context manager.

Changed in version 3.15: Added support for arbitrary descriptors `__enter__()` and `__exit__()`.

push(_exit_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.push "Link to this definition")

Adds a context manager’s [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 method to the callback stack.

As `__enter__` is _not_ invoked, this method can be used to cover part of an [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 implementation with a context manager’s own [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 method.

If passed an object that is not a context manager, this method assumes it is a callback with the same signature as a context manager’s [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 method and adds it directly to the callback stack.

By returning true values, these callbacks can suppress exceptions the same way context manager [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 methods can.

The passed in object is returned from the function, allowing this method to be used as a function decorator.

Changed in version 3.15: Added support for arbitrary descriptors `__exit__()`.

callback(_callback_, _/_, _\*args_, _\*\*kwds_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.callback "Link to this definition")

Accepts an arbitrary callback function and arguments and adds it to the callback stack.

Unlike the other methods, callbacks added this way cannot suppress exceptions (as they are never passed the exception details).

The passed in callback is returned from the function, allowing this method to be used as a function decorator.

pop\_all()[¶](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.pop_all "Link to this definition")

Transfers the callback stack to a fresh `ExitStack` instance and returns it. No callbacks are invoked by this operation - instead, they will now be invoked when the new stack is closed (either explicitly or implicitly at the end of a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement).

For example, a group of files can be opened as an “all or nothing” operation as follows:

Copy

with ExitStack() as stack:
    files \= \[stack.enter\_context(open(fname)) for fname in filenames\]
    \# Hold onto the close method, but don't call it yet.
    close\_files \= stack.pop\_all().close
    \# If opening any file fails, all previously opened files will be
    \# closed automatically. If all files are opened successfully,
    \# they will remain open even after the with statement ends.
    \# close\_files() can then be invoked explicitly to close them all.

close()[¶](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.close "Link to this definition")

Immediately unwinds the callback stack, invoking callbacks in the reverse order of registration. For any context managers and exit callbacks registered, the arguments passed in will indicate that no exception occurred.

class contextlib.AsyncExitStack[¶](https://docs.python.org/3/library/contextlib.html#contextlib.AsyncExitStack "Link to this definition")

An [asynchronous context manager](https://docs.python.org/3/reference/datamodel.html#async-context-managers)
, similar to [`ExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
, that supports combining both synchronous and asynchronous context managers, as well as having coroutines for cleanup logic.

The [`close()`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.close "contextlib.ExitStack.close")
 method is not implemented; [`aclose()`](https://docs.python.org/3/library/contextlib.html#contextlib.AsyncExitStack.aclose "contextlib.AsyncExitStack.aclose")
 must be used instead.

async enter\_async\_context(_cm_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.AsyncExitStack.enter_async_context "Link to this definition")

Similar to [`ExitStack.enter_context()`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.enter_context "contextlib.ExitStack.enter_context")
 but expects an asynchronous context manager.

Changed in version 3.11: Raises [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 instead of [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 if _cm_ is not an asynchronous context manager.

Changed in version 3.15: Added support for arbitrary descriptors `__aenter__()` and `__aexit__()`.

push\_async\_exit(_exit_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.AsyncExitStack.push_async_exit "Link to this definition")

Similar to [`ExitStack.push()`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.push "contextlib.ExitStack.push")
 but expects either an asynchronous context manager or a coroutine function.

Changed in version 3.15: Added support for arbitrary descriptors `__aexit__()`.

push\_async\_callback(_callback_, _/_, _\*args_, _\*\*kwds_)[¶](https://docs.python.org/3/library/contextlib.html#contextlib.AsyncExitStack.push_async_callback "Link to this definition")

Similar to [`ExitStack.callback()`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.callback "contextlib.ExitStack.callback")
 but expects a coroutine function.

async aclose()[¶](https://docs.python.org/3/library/contextlib.html#contextlib.AsyncExitStack.aclose "Link to this definition")

Similar to [`ExitStack.close()`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.close "contextlib.ExitStack.close")
 but properly handles awaitables.

Continuing the example for [`@asynccontextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager "contextlib.asynccontextmanager")
:

Copy

async with AsyncExitStack() as stack:
    connections \= \[await stack.enter\_async\_context(get\_connection())\
        for i in range(5)\]
    \# All opened connections will automatically be released at the end of
    \# the async with statement, even if attempts to open a connection
    \# later in the list raise an exception.

Added in version 3.7.

Examples and Recipes[¶](https://docs.python.org/3/library/contextlib.html#examples-and-recipes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

This section describes some examples and recipes for making effective use of the tools provided by `contextlib`.

### Supporting a variable number of context managers[¶](https://docs.python.org/3/library/contextlib.html#supporting-a-variable-number-of-context-managers "Link to this heading")

The primary use case for [`ExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
 is the one given in the class documentation: supporting a variable number of context managers and other cleanup operations in a single [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement. The variability may come from the number of context managers needed being driven by user input (such as opening a user specified collection of files), or from some of the context managers being optional:

Copy

with ExitStack() as stack:
    for resource in resources:
        stack.enter\_context(resource)
    if need\_special\_resource():
        special \= acquire\_special\_resource()
        stack.callback(release\_special\_resource, special)
    \# Perform operations that use the acquired resources

As shown, [`ExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
 also makes it quite easy to use [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statements to manage arbitrary resources that don’t natively support the context management protocol.

### Catching exceptions from `__enter__` methods[¶](https://docs.python.org/3/library/contextlib.html#catching-exceptions-from-enter-methods "Link to this heading")

It is occasionally desirable to catch exceptions from an [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 method implementation, _without_ inadvertently catching exceptions from the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement body or the context manager’s [`__exit__()`](https://docs.python.org/3/reference/datamodel.html#object.__exit__ "object.__exit__")
 method. By using [`ExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
 the steps in the context management protocol can be separated slightly in order to allow this:

Copy

stack \= ExitStack()
try:
    x \= stack.enter\_context(cm)
except Exception:
    \# handle \_\_enter\_\_ exception
else:
    with stack:
        \# Handle normal case

Actually needing to do this is likely to indicate that the underlying API should be providing a direct resource management interface for use with [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
/[`except`](https://docs.python.org/3/reference/compound_stmts.html#except)
/[`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 statements, but not all APIs are well designed in that regard. When a context manager is the only resource management API provided, then [`ExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
 can make it easier to handle various situations that can’t be handled directly in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement.

### Cleaning up in an `__enter__` implementation[¶](https://docs.python.org/3/library/contextlib.html#cleaning-up-in-an-enter-implementation "Link to this heading")

As noted in the documentation of [`ExitStack.push()`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.push "contextlib.ExitStack.push")
, this method can be useful in cleaning up an already allocated resource if later steps in the [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 implementation fail.

Here’s an example of doing this for a context manager that accepts resource acquisition and release functions, along with an optional validation function, and maps them to the context management protocol:

Copy

from contextlib import contextmanager, AbstractContextManager, ExitStack

class ResourceManager(AbstractContextManager):

    def \_\_init\_\_(self, acquire\_resource, release\_resource, check\_resource\_ok\=None):
        self.acquire\_resource \= acquire\_resource
        self.release\_resource \= release\_resource
        if check\_resource\_ok is None:
            def check\_resource\_ok(resource):
                return True
        self.check\_resource\_ok \= check\_resource\_ok

    @contextmanager
    def \_cleanup\_on\_error(self):
        with ExitStack() as stack:
            stack.push(self)
            yield
            \# The validation check passed and didn't raise an exception
            \# Accordingly, we want to keep the resource, and pass it
            \# back to our caller
            stack.pop\_all()

    def \_\_enter\_\_(self):
        resource \= self.acquire\_resource()
        with self.\_cleanup\_on\_error():
            if not self.check\_resource\_ok(resource):
                msg \= "Failed validation for {!r}"
                raise RuntimeError(msg.format(resource))
        return resource

    def \_\_exit\_\_(self, \*exc\_details):
        \# We don't need to duplicate any of our resource release logic
        self.release\_resource()

### Replacing any use of `try-finally` and flag variables[¶](https://docs.python.org/3/library/contextlib.html#replacing-any-use-of-try-finally-and-flag-variables "Link to this heading")

A pattern you will sometimes see is a `try-finally` statement with a flag variable to indicate whether or not the body of the `finally` clause should be executed. In its simplest form (that can’t already be handled just by using an `except` clause instead), it looks something like this:

Copy

cleanup\_needed \= True
try:
    result \= perform\_operation()
    if result:
        cleanup\_needed \= False
finally:
    if cleanup\_needed:
        cleanup\_resources()

As with any `try` statement based code, this can cause problems for development and review, because the setup code and the cleanup code can end up being separated by arbitrarily long sections of code.

[`ExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
 makes it possible to instead register a callback for execution at the end of a `with` statement, and then later decide to skip executing that callback:

Copy

from contextlib import ExitStack

with ExitStack() as stack:
    stack.callback(cleanup\_resources)
    result \= perform\_operation()
    if result:
        stack.pop\_all()

This allows the intended cleanup behaviour to be made explicit up front, rather than requiring a separate flag variable.

If a particular application uses this pattern a lot, it can be simplified even further by means of a small helper class:

Copy

from contextlib import ExitStack

class Callback(ExitStack):
    def \_\_init\_\_(self, callback, /, \*args, \*\*kwds):
        super().\_\_init\_\_()
        self.callback(callback, \*args, \*\*kwds)

    def cancel(self):
        self.pop\_all()

with Callback(cleanup\_resources) as cb:
    result \= perform\_operation()
    if result:
        cb.cancel()

If the resource cleanup isn’t already neatly bundled into a standalone function, then it is still possible to use the decorator form of [`ExitStack.callback()`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack.callback "contextlib.ExitStack.callback")
 to declare the resource cleanup in advance:

Copy

from contextlib import ExitStack

with ExitStack() as stack:
    @stack.callback
    def cleanup\_resources():
        ...
    result \= perform\_operation()
    if result:
        stack.pop\_all()

Due to the way the decorator protocol works, a callback function declared this way cannot take any parameters. Instead, any resources to be released must be accessed as closure variables.

### Using a context manager as a function decorator[¶](https://docs.python.org/3/library/contextlib.html#using-a-context-manager-as-a-function-decorator "Link to this heading")

[`ContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator "contextlib.ContextDecorator")
 makes it possible to use a context manager in both an ordinary `with` statement and also as a function decorator.

For example, it is sometimes useful to wrap functions or groups of statements with a logger that can track the time of entry and time of exit. Rather than writing both a function decorator and a context manager for the task, inheriting from [`ContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator "contextlib.ContextDecorator")
 provides both capabilities in a single definition:

Copy

from contextlib import ContextDecorator
import logging

logging.basicConfig(level\=logging.INFO)

class track\_entry\_and\_exit(ContextDecorator):
    def \_\_init\_\_(self, name):
        self.name \= name

    def \_\_enter\_\_(self):
        logging.info('Entering: %s', self.name)

    def \_\_exit\_\_(self, exc\_type, exc, exc\_tb):
        logging.info('Exiting: %s', self.name)

Instances of this class can be used as both a context manager:

Copy

with track\_entry\_and\_exit('widget loader'):
    print('Some time consuming activity goes here')
    load\_widget()

And also as a function decorator:

Copy

@track\_entry\_and\_exit('widget loader')
def activity():
    print('Some time consuming activity goes here')
    load\_widget()

Note that there is one additional limitation when using context managers as function decorators: there’s no way to access the return value of [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
. If that value is needed, then it is still necessary to use an explicit `with` statement.

See also

[**PEP 343**](https://peps.python.org/pep-0343/)
 - The “with” statement

The specification, background, and examples for the Python [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement.

Single use, reusable and reentrant context managers[¶](https://docs.python.org/3/library/contextlib.html#single-use-reusable-and-reentrant-context-managers "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Most context managers are written in a way that means they can only be used effectively in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement once. These single use context managers must be created afresh each time they’re used - attempting to use them a second time will trigger an exception or otherwise not work correctly.

This common limitation means that it is generally advisable to create context managers directly in the header of the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement where they are used (as shown in all of the usage examples above).

Files are an example of effectively single use context managers, since the first [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement will close the file, preventing any further IO operations using that file object.

Context managers created using [`@contextmanager`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager "contextlib.contextmanager")
 are also single use context managers, and will complain about the underlying generator failing to yield if an attempt is made to use them a second time:

Copy

\>>> from contextlib import contextmanager
\>>> @contextmanager
... def singleuse():
...     print("Before")
...     yield
...     print("After")
...
\>>> cm \= singleuse()
\>>> with cm:
...     pass
...
Before
After
\>>> with cm:
...     pass
...
Traceback (most recent call last):
    ...
RuntimeError: generator didn't yield

### Reentrant context managers[¶](https://docs.python.org/3/library/contextlib.html#reentrant-context-managers "Link to this heading")

More sophisticated context managers may be “reentrant”. These context managers can not only be used in multiple [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statements, but may also be used _inside_ a `with` statement that is already using the same context manager.

[`threading.RLock`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock")
 is an example of a reentrant context manager, as are [`suppress()`](https://docs.python.org/3/library/contextlib.html#contextlib.suppress "contextlib.suppress")
, [`redirect_stdout()`](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout "contextlib.redirect_stdout")
, and [`chdir()`](https://docs.python.org/3/library/contextlib.html#contextlib.chdir "contextlib.chdir")
. Here’s a very simple example of reentrant use:

Copy

\>>> from contextlib import redirect\_stdout
\>>> from io import StringIO
\>>> stream \= StringIO()
\>>> write\_to\_stream \= redirect\_stdout(stream)
\>>> with write\_to\_stream:
...     print("This is written to the stream rather than stdout")
...     with write\_to\_stream:
...         print("This is also written to the stream")
...
\>>> print("This is written directly to stdout")
This is written directly to stdout
\>>> print(stream.getvalue())
This is written to the stream rather than stdout
This is also written to the stream

Real world examples of reentrancy are more likely to involve multiple functions calling each other and hence be far more complicated than this example.

Note also that being reentrant is _not_ the same thing as being thread safe. [`redirect_stdout()`](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout "contextlib.redirect_stdout")
, for example, is definitely not thread safe, as it makes a global modification to the system state by binding [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 to a different stream.

### Reusable context managers[¶](https://docs.python.org/3/library/contextlib.html#reusable-context-managers "Link to this heading")

Distinct from both single use and reentrant context managers are “reusable” context managers (or, to be completely explicit, “reusable, but not reentrant” context managers, since reentrant context managers are also reusable). These context managers support being used multiple times, but will fail (or otherwise not work correctly) if the specific context manager instance has already been used in a containing with statement.

[`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock")
 is an example of a reusable, but not reentrant, context manager (for a reentrant lock, it is necessary to use [`threading.RLock`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock")
 instead).

Another example of a reusable, but not reentrant, context manager is [`ExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
, as it invokes _all_ currently registered callbacks when leaving any with statement, regardless of where those callbacks were added:

Copy

\>>> from contextlib import ExitStack
\>>> stack \= ExitStack()
\>>> with stack:
...     stack.callback(print, "Callback: from first context")
...     print("Leaving first context")
...
Leaving first context
Callback: from first context
\>>> with stack:
...     stack.callback(print, "Callback: from second context")
...     print("Leaving second context")
...
Leaving second context
Callback: from second context
\>>> with stack:
...     stack.callback(print, "Callback: from outer context")
...     with stack:
...         stack.callback(print, "Callback: from inner context")
...         print("Leaving inner context")
...     print("Leaving outer context")
...
Leaving inner context
Callback: from inner context
Callback: from outer context
Leaving outer context

As the output from the example shows, reusing a single stack object across multiple with statements works correctly, but attempting to nest them will cause the stack to be cleared at the end of the innermost with statement, which is unlikely to be desirable behaviour.

Using separate [`ExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
 instances instead of reusing a single instance avoids that problem:

Copy

\>>> from contextlib import ExitStack
\>>> with ExitStack() as outer\_stack:
...     outer\_stack.callback(print, "Callback: from outer context")
...     with ExitStack() as inner\_stack:
...         inner\_stack.callback(print, "Callback: from inner context")
...         print("Leaving inner context")
...     print("Leaving outer context")
...
Leaving inner context
Callback: from inner context
Leaving outer context
Callback: from outer context

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`contextlib` — Utilities for `with`\-statement contexts](https://docs.python.org/3/library/contextlib.html#)
    *   [Utilities](https://docs.python.org/3/library/contextlib.html#utilities)
        
    *   [Examples and Recipes](https://docs.python.org/3/library/contextlib.html#examples-and-recipes)
        *   [Supporting a variable number of context managers](https://docs.python.org/3/library/contextlib.html#supporting-a-variable-number-of-context-managers)
            
        *   [Catching exceptions from `__enter__` methods](https://docs.python.org/3/library/contextlib.html#catching-exceptions-from-enter-methods)
            
        *   [Cleaning up in an `__enter__` implementation](https://docs.python.org/3/library/contextlib.html#cleaning-up-in-an-enter-implementation)
            
        *   [Replacing any use of `try-finally` and flag variables](https://docs.python.org/3/library/contextlib.html#replacing-any-use-of-try-finally-and-flag-variables)
            
        *   [Using a context manager as a function decorator](https://docs.python.org/3/library/contextlib.html#using-a-context-manager-as-a-function-decorator)
            
    *   [Single use, reusable and reentrant context managers](https://docs.python.org/3/library/contextlib.html#single-use-reusable-and-reentrant-context-managers)
        *   [Reentrant context managers](https://docs.python.org/3/library/contextlib.html#reentrant-context-managers)
            
        *   [Reusable context managers](https://docs.python.org/3/library/contextlib.html#reusable-context-managers)
            

#### Previous topic

[`dataclasses` — Data Classes](https://docs.python.org/3/library/dataclasses.html "previous chapter")

#### Next topic

[`abc` — Abstract Base Classes](https://docs.python.org/3/library/abc.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=contextlib+%E2%80%94+Utilities+for+with-statement+contexts&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fcontextlib.html&pagesource=library%2Fcontextlib.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/contextlib.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/abc.html "abc — Abstract Base Classes")
     |
*   [previous](https://docs.python.org/3/library/dataclasses.html "dataclasses — Data Classes")
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
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)
     »
*   [`contextlib` — Utilities for `with`\-statement contexts](https://docs.python.org/3/library/contextlib.html)
    
*    
    
    |
*   Theme Auto Light Dark |