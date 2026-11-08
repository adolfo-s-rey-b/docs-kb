### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-threading.html "asyncio and free-threaded Python")
     |
*   [previous](https://docs.python.org/3/library/asyncio-llapi-index.html "Low-level API Index")
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
*   [Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Developing with asyncio[¶](https://docs.python.org/3/library/asyncio-dev.html#developing-with-asyncio "Link to this heading")

==============================================================================================================================

Asynchronous programming is different from classic “sequential” programming.

This page lists common mistakes and traps and explains how to avoid them.

Debug Mode[¶](https://docs.python.org/3/library/asyncio-dev.html#debug-mode "Link to this heading")

----------------------------------------------------------------------------------------------------

By default asyncio runs in production mode. In order to ease the development asyncio has a _debug mode_.

There are several ways to enable asyncio debug mode:

*   Setting the [`PYTHONASYNCIODEBUG`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONASYNCIODEBUG)
     environment variable to `1`.
    
*   Using the [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
    .
    
*   Passing `debug=True` to [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
    .
    
*   Calling [`loop.set_debug()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_debug "asyncio.loop.set_debug")
    .
    

In addition to enabling the debug mode, consider also:

*   setting the log level of the [asyncio logger](https://docs.python.org/3/library/asyncio-dev.html#asyncio-logger)
     to [`logging.DEBUG`](https://docs.python.org/3/library/logging.html#logging.DEBUG "logging.DEBUG")
    , for example the following snippet of code can be run at startup of the application:
    
    Copy
    
    logging.basicConfig(level\=logging.DEBUG)
    
*   configuring the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")
     module to display [`ResourceWarning`](https://docs.python.org/3/builtins/exceptions.html#ResourceWarning "ResourceWarning")
     warnings. One way of doing that is by using the [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W)
     `default` command line option.
    

When the debug mode is enabled:

*   Many non-threadsafe asyncio APIs (such as [`loop.call_soon()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")
     and [`loop.call_at()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_at "asyncio.loop.call_at")
     methods) raise an exception if they are called from a wrong thread.
    
*   The execution time of the I/O selector is logged if it takes too long to perform an I/O operation.
    
*   Callbacks taking longer than 100 milliseconds are logged. The [`loop.slow_callback_duration`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.slow_callback_duration "asyncio.loop.slow_callback_duration")
     attribute can be used to set the minimum execution duration in seconds that is considered “slow”.
    

Concurrency and Multithreading[¶](https://docs.python.org/3/library/asyncio-dev.html#concurrency-and-multithreading "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

An event loop runs in a thread (typically the main thread) and executes all callbacks and Tasks in its thread. While a Task is running in the event loop, no other Tasks can run in the same thread. When a Task executes an `await` expression, the running Task gets suspended, and the event loop executes the next Task.

To schedule a [callback](https://docs.python.org/3/glossary.html#term-callback)
 from another OS thread, the [`loop.call_soon_threadsafe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe")
 method should be used. Example:

Copy

loop.call\_soon\_threadsafe(callback, \*args)

Almost all asyncio objects are not thread safe, which is typically not a problem unless there is code that works with them from outside of a Task or a callback. If there’s a need for such code to call a low-level asyncio API, the [`loop.call_soon_threadsafe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe")
 method should be used, e.g.:

Copy

loop.call\_soon\_threadsafe(fut.cancel)

To schedule a coroutine object from a different OS thread, the [`run_coroutine_threadsafe()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe "asyncio.run_coroutine_threadsafe")
 function should be used. It returns a [`concurrent.futures.Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future")
 to access the result:

Copy

async def coro\_func():
     return await asyncio.sleep(1, 42)

\# Later in another OS thread:

future \= asyncio.run\_coroutine\_threadsafe(coro\_func(), loop)
\# Wait for the result:
result \= future.result()

To handle signals the event loop must be run in the main thread.

The [`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")
 method can be used with a [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor")
 or [`InterpreterPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor "concurrent.futures.InterpreterPoolExecutor")
 to execute blocking code in a different OS thread without blocking the OS thread that the event loop runs in.

There is currently no way to schedule coroutines or callbacks directly from a different process (such as one started with [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
). The [Event loop methods](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop-methods)
 section lists APIs that can read from pipes and watch file descriptors without blocking the event loop. In addition, asyncio’s [Subprocess](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio-subprocess)
 APIs provide a way to start a process and communicate with it from the event loop. Lastly, the aforementioned [`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")
 method can also be used with a [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor")
 to execute code in a different process.

Running Blocking Code[¶](https://docs.python.org/3/library/asyncio-dev.html#running-blocking-code "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

Blocking (CPU-bound) code should not be called directly. For example, if a function performs a CPU-intensive calculation for 1 second, all concurrent asyncio Tasks and IO operations would be delayed by 1 second.

An executor can be used to run a task in a different thread, including in a different interpreter, or even in a different process to avoid blocking the OS thread with the event loop. See the [`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")
 method for more details.

Logging[¶](https://docs.python.org/3/library/asyncio-dev.html#logging "Link to this heading")

----------------------------------------------------------------------------------------------

asyncio uses the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
 module and all logging is performed via the `"asyncio"` logger.

The default log level is [`logging.INFO`](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO")
, which can be easily adjusted:

Copy

logging.getLogger("asyncio").setLevel(logging.WARNING)

Network logging can block the event loop. It is recommended to use a separate thread for handling logs or use non-blocking IO. For example, see [Dealing with handlers that block](https://docs.python.org/3/howto/logging-cookbook.html#blocking-handlers)
.

Detect never-awaited coroutines[¶](https://docs.python.org/3/library/asyncio-dev.html#detect-never-awaited-coroutines "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

When a coroutine function is called, but not awaited (e.g. `coro()` instead of `await coro()`) or the coroutine is not scheduled with [`asyncio.create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task")
, asyncio will emit a [`RuntimeWarning`](https://docs.python.org/3/builtins/exceptions.html#RuntimeWarning "RuntimeWarning")
:

Copy

import asyncio

async def test():
    print("never scheduled")

async def main():
    test()

asyncio.run(main())

Output:

Copy

test.py:7: RuntimeWarning: coroutine 'test' was never awaited
  test()

Output in debug mode:

Copy

test.py:7: RuntimeWarning: coroutine 'test' was never awaited
Coroutine created at (most recent call last)
  File "../t.py", line 9, in <module\>
    asyncio.run(main(), debug\=True)

  < .. \>

  File "../t.py", line 7, in main
    test()
  test()

The usual fix is to either await the coroutine or call the [`asyncio.create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task")
 function:

Copy

async def main():
    await test()

Detect never-retrieved exceptions[¶](https://docs.python.org/3/library/asyncio-dev.html#detect-never-retrieved-exceptions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

If a [`Future.set_exception()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.set_exception "asyncio.Future.set_exception")
 is called but the Future object is never awaited on, the exception would never be propagated to the user code. In this case, asyncio would emit a log message when the Future object is garbage collected.

Example of an unhandled exception:

Copy

import asyncio

async def bug():
    raise Exception("not consumed")

async def main():
    asyncio.create\_task(bug())

asyncio.run(main())

Output:

Copy

Task exception was never retrieved
future: <Task finished coro\=<bug() done, defined at test.py:3\>
  exception\=Exception('not consumed')\>

Traceback (most recent call last):
  File "test.py", line 4, in bug
    raise Exception("not consumed")
Exception: not consumed

[Enable the debug mode](https://docs.python.org/3/library/asyncio-dev.html#asyncio-debug-mode)
 to get the traceback where the task was created:

Copy

asyncio.run(main(), debug\=True)

Output in debug mode:

Copy

Task exception was never retrieved
future: <Task finished coro\=<bug() done, defined at test.py:3\>
    exception\=Exception('not consumed') created at asyncio/tasks.py:321\>

source\_traceback: Object created at (most recent call last):
  File "../t.py", line 9, in <module\>
    asyncio.run(main(), debug\=True)

< .. \>

Traceback (most recent call last):
  File "../t.py", line 4, in bug
    raise Exception("not consumed")
Exception: not consumed

Asynchronous generators best practices[¶](https://docs.python.org/3/library/asyncio-dev.html#asynchronous-generators-best-practices "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

Writing correct and efficient asyncio code requires awareness of certain pitfalls. This section outlines essential best practices that can save you hours of debugging.

### Close asynchronous generators explicitly[¶](https://docs.python.org/3/library/asyncio-dev.html#close-asynchronous-generators-explicitly "Link to this heading")

It is recommended to manually close the [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator-iterator)
. If a generator exits early - for example, due to an exception raised in the body of an `async for` loop - its asynchronous cleanup code may run in an unexpected context. This can occur after the tasks it depends on have completed, or during the event loop shutdown when the async-generator’s garbage collection hook is called.

To avoid this, explicitly close the generator by calling its [`aclose()`](https://docs.python.org/3/builtins/stdtypes.html#agen.aclose "agen.aclose")
 method, or use the [`contextlib.aclosing()`](https://docs.python.org/3/library/contextlib.html#contextlib.aclosing "contextlib.aclosing")
 context manager:

Copy

import asyncio
import contextlib

async def gen():
  yield 1
  yield 2

async def func():
  async with contextlib.aclosing(gen()) as g:
    async for x in g:
      break  \# Don't iterate until the end

asyncio.run(func())

As noted above, the cleanup code for these asynchronous generators is deferred. The following example demonstrates that the finalization of an asynchronous generator can occur in an unexpected order:

Copy

import asyncio
work\_done \= False

async def cursor():
    try:
        yield 1
    finally:
        assert work\_done

async def rows():
    global work\_done
    try:
        yield 2
    finally:
        await asyncio.sleep(0.1) \# imitate some async work
        work\_done \= True

async def main():
    async for c in cursor():
        async for r in rows():
            break
        break

asyncio.run(main())

For this example, we get the following output:

Copy

unhandled exception during asyncio.run() shutdown
task: <Task finished name\='Task-3' coro\=<<async\_generator\_athrow without \_\_name\_\_\>()\> exception\=AssertionError()\>
Traceback (most recent call last):
  File "example.py", line 6, in cursor
    yield 1
asyncio.exceptions.CancelledError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "example.py", line 8, in cursor
    assert work\_done
           ^^^^^^^^^
AssertionError

The `cursor()` asynchronous generator was finalized before the `rows` generator - an unexpected behavior.

The example can be fixed by explicitly closing the `cursor` and `rows` async-generators:

Copy

async def main():
    async with contextlib.aclosing(cursor()) as cursor\_gen:
        async for c in cursor\_gen:
            async with contextlib.aclosing(rows()) as rows\_gen:
                async for r in rows\_gen:
                    break
            break

### Create asynchronous generators only when the event loop is running[¶](https://docs.python.org/3/library/asyncio-dev.html#create-asynchronous-generators-only-when-the-event-loop-is-running "Link to this heading")

It is recommended to create [asynchronous generators](https://docs.python.org/3/glossary.html#term-asynchronous-generator-iterator)
 only after the event loop has been created.

To ensure that asynchronous generators close reliably, the event loop uses the [`sys.set_asyncgen_hooks()`](https://docs.python.org/3/library/sys.html#sys.set_asyncgen_hooks "sys.set_asyncgen_hooks")
 function to register callback functions. These callbacks update the list of running asynchronous generators to keep it in a consistent state.

When the [`loop.shutdown_asyncgens()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_asyncgens "asyncio.loop.shutdown_asyncgens")
 function is called, the running generators are stopped gracefully and the list is cleared.

The asynchronous generator invokes the corresponding system hook during its first iteration. At the same time, the generator records that the hook has been called and does not call it again.

Therefore, if iteration begins before the event loop is created, the event loop will not be able to add the generator to its list of active generators because the hooks are set after the generator attempts to call them. Consequently, the event loop will not be able to terminate the generator if necessary.

Consider the following example:

Copy

import asyncio

async def agenfn():
    try:
        yield 10
    finally:
        await asyncio.sleep(0)

with asyncio.Runner() as runner:
    agen \= agenfn()
    print(runner.run(anext(agen)))
    del agen

Output:

Copy

10
Exception ignored while closing generator <async\_generator object agenfn at 0x000002F71CD10D70\>:
Traceback (most recent call last):
  File "example.py", line 13, in <module\>
    del agen
        ^^^^
RuntimeError: async generator ignored GeneratorExit

This example can be fixed as follows:

Copy

import asyncio

async def agenfn():
    try:
        yield 10
    finally:
        await asyncio.sleep(0)

async def main():
    agen \= agenfn()
    print(await anext(agen))
    del agen

asyncio.run(main())

### Avoid concurrent iteration and closure of the same generator[¶](https://docs.python.org/3/library/asyncio-dev.html#avoid-concurrent-iteration-and-closure-of-the-same-generator "Link to this heading")

Async generators may be reentered while another [`__anext__()`](https://docs.python.org/3/builtins/stdtypes.html#agen.__anext__ "agen.__anext__")
 / [`athrow()`](https://docs.python.org/3/builtins/stdtypes.html#agen.athrow "agen.athrow")
 / [`aclose()`](https://docs.python.org/3/builtins/stdtypes.html#agen.aclose "agen.aclose")
 call is in progress. This may lead to an inconsistent state of the async generator and can cause errors.

Let’s consider the following example:

Copy

import asyncio

async def consumer():
    for idx in range(100):
        await asyncio.sleep(0)
        message \= yield idx
        print('received', message)

async def amain():
    agenerator \= consumer()
    await agenerator.asend(None)

    fa \= asyncio.create\_task(agenerator.asend('A'))
    fb \= asyncio.create\_task(agenerator.asend('B'))
    await fa
    await fb

asyncio.run(amain())

Output:

Copy

received A
Traceback (most recent call last):
  File "test.py", line 38, in <module\>
    asyncio.run(amain())
    \~~~~~~~~~~~^^^^^^^^^
  File "Lib/asyncio/runners.py", line 204, in run
    return runner.run(main)
           \~~~~~~~~~~^^^^^^
  File "Lib/asyncio/runners.py", line 127, in run
    return self.\_loop.run\_until\_complete(task)
           \~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "Lib/asyncio/base\_events.py", line 719, in run\_until\_complete
    return future.result()
           \~~~~~~~~~~~~~^^
  File "test.py", line 36, in amain
    await fb
RuntimeError: anext(): asynchronous generator is already running

Therefore, it is recommended to avoid using asynchronous generators in parallel tasks or across multiple event loops.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html#)
    *   [Debug Mode](https://docs.python.org/3/library/asyncio-dev.html#debug-mode)
        
    *   [Concurrency and Multithreading](https://docs.python.org/3/library/asyncio-dev.html#concurrency-and-multithreading)
        
    *   [Running Blocking Code](https://docs.python.org/3/library/asyncio-dev.html#running-blocking-code)
        
    *   [Logging](https://docs.python.org/3/library/asyncio-dev.html#logging)
        
    *   [Detect never-awaited coroutines](https://docs.python.org/3/library/asyncio-dev.html#detect-never-awaited-coroutines)
        
    *   [Detect never-retrieved exceptions](https://docs.python.org/3/library/asyncio-dev.html#detect-never-retrieved-exceptions)
        
    *   [Asynchronous generators best practices](https://docs.python.org/3/library/asyncio-dev.html#asynchronous-generators-best-practices)
        *   [Close asynchronous generators explicitly](https://docs.python.org/3/library/asyncio-dev.html#close-asynchronous-generators-explicitly)
            
        *   [Create asynchronous generators only when the event loop is running](https://docs.python.org/3/library/asyncio-dev.html#create-asynchronous-generators-only-when-the-event-loop-is-running)
            
        *   [Avoid concurrent iteration and closure of the same generator](https://docs.python.org/3/library/asyncio-dev.html#avoid-concurrent-iteration-and-closure-of-the-same-generator)
            

#### Previous topic

[Low-level API Index](https://docs.python.org/3/library/asyncio-llapi-index.html "previous chapter")

#### Next topic

[asyncio and free-threaded Python](https://docs.python.org/3/library/asyncio-threading.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Developing+with+asyncio&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-dev.html&pagesource=library%2Fasyncio-dev.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-dev.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-threading.html "asyncio and free-threaded Python")
     |
*   [previous](https://docs.python.org/3/library/asyncio-llapi-index.html "Low-level API Index")
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
*   [Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html)
    
*    
    
    |
*   Theme Auto Light Dark |