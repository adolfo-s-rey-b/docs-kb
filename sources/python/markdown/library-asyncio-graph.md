### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-tools.html "Command-line introspection tools")
     |
*   [previous](https://docs.python.org/3/library/asyncio-exceptions.html "Exceptions")
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
*   [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html)
     »
*   [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
     »
*   [Call graph introspection](https://docs.python.org/3/library/asyncio-graph.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Call graph introspection[¶](https://docs.python.org/3/library/asyncio-graph.html#call-graph-introspection "Link to this heading")

==================================================================================================================================

**Source code:** [Lib/asyncio/graph.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/graph.py)

* * *

asyncio has powerful runtime call graph introspection utilities to trace the entire call graph of a running _coroutine_ or _task_, or a suspended _future_. These utilities and the underlying machinery can be used from within a Python program or by external profilers and debuggers.

See also

[Command-line introspection tools](https://docs.python.org/3/library/asyncio-tools.html#asyncio-introspection-tools)

Command-line tools for inspecting tasks in another running Python process.

Added in version 3.14.

asyncio.print\_call\_graph(_future\=None_, _/_, _\*_, _file\=None_, _depth\=1_, _limit\=None_)[¶](https://docs.python.org/3/library/asyncio-graph.html#asyncio.print_call_graph "Link to this definition")

Print the async call graph for the current task or the provided [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
 or [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
.

This function prints entries starting from the top frame and going down towards the invocation point.

The function receives an optional _future_ argument. If not passed, the current running task will be used.

If the function is called on _the current task_, the optional keyword-only _depth_ argument can be used to skip the specified number of frames from top of the stack.

If the optional keyword-only _limit_ argument is provided, each call stack in the resulting graph is truncated to include at most `abs(limit)` entries. If _limit_ is positive, the entries left are the closest to the invocation point. If _limit_ is negative, the topmost entries are left. If _limit_ is omitted or `None`, all entries are present. If _limit_ is `0`, the call stack is not printed at all, only “awaited by” information is printed.

If _file_ is omitted or `None`, the function will print to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
.

**Example:**

The following Python code:

Copy

import asyncio

async def test():
    asyncio.print\_call\_graph()

async def main():
    async with asyncio.TaskGroup() as g:
        g.create\_task(test(), name\='test')

asyncio.run(main())

will print:

Copy

\* Task(name\='test', id\=0x1039f0fe0)
+ Call stack:
|   File 't2.py', line 4, in async test()
+ Awaited by:
   \* Task(name\='Task-1', id\=0x103a5e060)
      + Call stack:
      |   File 'taskgroups.py', line 107, in async TaskGroup.\_\_aexit\_\_()
      |   File 't2.py', line 7, in async main()

asyncio.format\_call\_graph(_future\=None_, _/_, _\*_, _depth\=1_, _limit\=None_)[¶](https://docs.python.org/3/library/asyncio-graph.html#asyncio.format_call_graph "Link to this definition")

Like [`print_call_graph()`](https://docs.python.org/3/library/asyncio-graph.html#asyncio.print_call_graph "asyncio.print_call_graph")
, but returns a string. If _future_ is `None` and there’s no current task, the function returns an empty string.

asyncio.capture\_call\_graph(_future\=None_, _/_, _\*_, _depth\=1_, _limit\=None_)[¶](https://docs.python.org/3/library/asyncio-graph.html#asyncio.capture_call_graph "Link to this definition")

Capture the async call graph for the current task or the provided [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
 or [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
.

The function receives an optional _future_ argument. If not passed, the current running task will be used. If there’s no current task, the function returns `None`.

If the function is called on _the current task_, the optional keyword-only _depth_ argument can be used to skip the specified number of frames from top of the stack.

Returns a `FutureCallGraph` data class object:

*   `FutureCallGraph(future, call_stack, awaited_by)`
    
    > Where _future_ is a reference to a [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
    >  or a [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
    >  (or their subclasses.)
    > 
    > `call_stack` is a tuple of `FrameCallGraphEntry` objects.
    > 
    > `awaited_by` is a tuple of `FutureCallGraph` objects.
    
*   `FrameCallGraphEntry(frame)`
    
    > Where _frame_ is a frame object of a regular Python function in the call stack.
    

Low level utility functions[¶](https://docs.python.org/3/library/asyncio-graph.html#low-level-utility-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

To introspect an async call graph asyncio requires cooperation from control flow structures, such as [`shield()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.shield "asyncio.shield")
 or [`TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup")
. Any time an intermediate [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
 object with low-level APIs like [`Future.add_done_callback()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.add_done_callback "asyncio.Future.add_done_callback")
 is involved, the following two functions should be used to inform asyncio about how exactly such intermediate future objects are connected with the tasks they wrap or control.

asyncio.future\_add\_to\_awaited\_by(_future_, _waiter_, _/_)[¶](https://docs.python.org/3/library/asyncio-graph.html#asyncio.future_add_to_awaited_by "Link to this definition")

Record that _future_ is awaited on by _waiter_.

Both _future_ and _waiter_ must be instances of [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
 or [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
 or their subclasses, otherwise the call would have no effect.

A call to `future_add_to_awaited_by()` must be followed by an eventual call to the [`future_discard_from_awaited_by()`](https://docs.python.org/3/library/asyncio-graph.html#asyncio.future_discard_from_awaited_by "asyncio.future_discard_from_awaited_by")
 function with the same arguments.

asyncio.future\_discard\_from\_awaited\_by(_future_, _waiter_, _/_)[¶](https://docs.python.org/3/library/asyncio-graph.html#asyncio.future_discard_from_awaited_by "Link to this definition")

Record that _future_ is no longer awaited on by _waiter_.

Both _future_ and _waiter_ must be instances of [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
 or [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
 or their subclasses, otherwise the call would have no effect.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Call graph introspection](https://docs.python.org/3/library/asyncio-graph.html#)
    *   [Low level utility functions](https://docs.python.org/3/library/asyncio-graph.html#low-level-utility-functions)
        

#### Previous topic

[Exceptions](https://docs.python.org/3/library/asyncio-exceptions.html "previous chapter")

#### Next topic

[Command-line introspection tools](https://docs.python.org/3/library/asyncio-tools.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Call+graph+introspection&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-graph.html&pagesource=library%2Fasyncio-graph.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-graph.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-tools.html "Command-line introspection tools")
     |
*   [previous](https://docs.python.org/3/library/asyncio-exceptions.html "Exceptions")
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
*   [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html)
     »
*   [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
     »
*   [Call graph introspection](https://docs.python.org/3/library/asyncio-graph.html)
    
*    
    
    |
*   Theme Auto Light Dark |