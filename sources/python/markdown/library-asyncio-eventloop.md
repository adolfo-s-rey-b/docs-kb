### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-future.html "Futures")
     |
*   [previous](https://docs.python.org/3/library/asyncio-tools.html "Command-line introspection tools")
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
*   [Event loop](https://docs.python.org/3/library/asyncio-eventloop.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Event loop[¶](https://docs.python.org/3/library/asyncio-eventloop.html#event-loop "Link to this heading")

==========================================================================================================

**Source code:** [Lib/asyncio/events.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/events.py)
, [Lib/asyncio/base\_events.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/base_events.py)

* * *

Preface

The event loop is the core of every asyncio application. Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.

Application developers should typically use the high-level asyncio functions, such as [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
, and should rarely need to reference the loop object or call its methods. This section is intended mostly for authors of lower-level code, libraries, and frameworks, who need finer control over the event loop behavior.

Obtaining the Event Loop

The following low-level functions can be used to get, set, or create an event loop:

asyncio.get\_running\_loop()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_running_loop "Link to this definition")

Return the running event loop in the current OS thread.

Raise a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 if there is no running event loop.

This function can only be called from a coroutine or a callback.

Added in version 3.7.

asyncio.get\_event\_loop()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop "Link to this definition")

Get the current event loop.

When called from a coroutine or a callback (e.g. scheduled with call\_soon or similar API), this function will always return the running event loop.

If there is no running event loop set, the function will return the result of the `get_event_loop_policy().get_event_loop()` call.

Because this function has rather complex behavior (especially when custom event loop policies are in use), using the [`get_running_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_running_loop "asyncio.get_running_loop")
 function is preferred to `get_event_loop()` in coroutines and callbacks.

As noted above, consider using the higher-level [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
 function, instead of using these lower level functions to manually create and close an event loop.

Changed in version 3.14: Raises a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 if there is no current event loop.

Note

The `asyncio` policy system is deprecated and will be removed in Python 3.16; from there on, this function will return the current running event loop if present else it will return the loop set by [`set_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.set_event_loop "asyncio.set_event_loop")
.

asyncio.set\_event\_loop(_loop_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.set_event_loop "Link to this definition")

Set _loop_ as the current event loop for the current OS thread.

asyncio.new\_event\_loop()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.new_event_loop "Link to this definition")

Create and return a new event loop object.

Note that the behaviour of [`get_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.get_event_loop "asyncio.get_event_loop")
, [`set_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.set_event_loop "asyncio.set_event_loop")
, and [`new_event_loop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.new_event_loop "asyncio.new_event_loop")
 functions can be altered by [setting a custom event loop policy](https://docs.python.org/3/library/asyncio-policy.html#asyncio-policies)
.

Contents

This documentation page contains the following sections:

*   The [Event Loop Methods](https://docs.python.org/3/library/asyncio-eventloop.html#event-loop-methods)
     section is the reference documentation of the event loop APIs;
    
*   The [Callback Handles](https://docs.python.org/3/library/asyncio-eventloop.html#callback-handles)
     section documents the [`Handle`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Handle "asyncio.Handle")
     and [`TimerHandle`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.TimerHandle "asyncio.TimerHandle")
     instances which are returned from scheduling methods such as [`loop.call_soon()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")
     and [`loop.call_later()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_later "asyncio.loop.call_later")
    ;
    
*   The [Server Objects](https://docs.python.org/3/library/asyncio-eventloop.html#server-objects)
     section documents types returned from event loop methods like [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
    ;
    
*   The [Event Loop Implementations](https://docs.python.org/3/library/asyncio-eventloop.html#event-loop-implementations)
     section documents the [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
     and [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
     classes;
    
*   The [Examples](https://docs.python.org/3/library/asyncio-eventloop.html#examples)
     section showcases how to work with some event loop APIs.
    

Event loop methods[¶](https://docs.python.org/3/library/asyncio-eventloop.html#event-loop-methods "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

Event loops have **low-level** APIs for the following:

### [Running and stopping the loop](https://docs.python.org/3/library/asyncio-eventloop.html#id1)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#running-and-stopping-the-loop "Link to this heading")

loop.run\_until\_complete(_future_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_until_complete "Link to this definition")

Run until the _future_ (an instance of [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
) has completed.

If the argument is a [coroutine object](https://docs.python.org/3/library/asyncio-task.html#coroutine)
 it is implicitly scheduled to run as a [`asyncio.Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
.

Return the Future’s result or raise its exception.

loop.run\_forever()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_forever "Link to this definition")

Run the event loop until [`stop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.stop "asyncio.loop.stop")
 is called.

If [`stop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.stop "asyncio.loop.stop")
 is called before `run_forever()` is called, the loop will poll the I/O selector once with a timeout of zero, run all callbacks scheduled in response to I/O events (and those that were already scheduled), and then exit.

If [`stop()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.stop "asyncio.loop.stop")
 is called while `run_forever()` is running, the loop will run the current batch of callbacks and then exit. Note that new callbacks scheduled by callbacks will not run in this case; instead, they will run the next time `run_forever()` or [`run_until_complete()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_until_complete "asyncio.loop.run_until_complete")
 is called.

loop.stop()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.stop "Link to this definition")

Stop the event loop.

loop.is\_running()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.is_running "Link to this definition")

Return `True` if the event loop is currently running.

loop.is\_closed()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.is_closed "Link to this definition")

Return `True` if the event loop was closed.

loop.close()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.close "Link to this definition")

Close the event loop.

The loop must not be running when this function is called. Any pending callbacks will be discarded.

This method clears all queues and shuts down the executor, but does not wait for the executor to finish.

This method is idempotent and irreversible. No other methods should be called after the event loop is closed.

async loop.shutdown\_asyncgens()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_asyncgens "Link to this definition")

Schedule all currently open [asynchronous generator](https://docs.python.org/3/glossary.html#term-asynchronous-generator)
 objects to close with an [`aclose()`](https://docs.python.org/3/builtins/stdtypes.html#agen.aclose "agen.aclose")
 call. After calling this method, the event loop will issue a warning if a new asynchronous generator is iterated. This should be used to reliably finalize all scheduled asynchronous generators.

Note that there is no need to call this function when [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
 is used.

Example:

Copy

try:
    loop.run\_forever()
finally:
    loop.run\_until\_complete(loop.shutdown\_asyncgens())
    loop.close()

Added in version 3.6.

async loop.shutdown\_default\_executor(_timeout\=None_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_default_executor "Link to this definition")

Schedule the closure of the default executor and wait for it to join all of the threads in the [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor")
. Once this method has been called, using the default executor with [`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")
 will raise a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
.

The _timeout_ parameter specifies the amount of time (in [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 seconds) the executor will be given to finish joining. With the default, `None`, the executor is allowed an unlimited amount of time.

If the _timeout_ is reached, a [`RuntimeWarning`](https://docs.python.org/3/builtins/exceptions.html#RuntimeWarning "RuntimeWarning")
 is emitted and the default executor is terminated without waiting for its threads to finish joining.

Note

Do not call this method when using [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
, as the latter handles default executor shutdown automatically.

Added in version 3.9.

Changed in version 3.12: Added the _timeout_ parameter.

### [Scheduling callbacks](https://docs.python.org/3/library/asyncio-eventloop.html#id2)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#scheduling-callbacks "Link to this heading")

loop.call\_soon(_callback_, _\*args_, _context\=None_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "Link to this definition")

Schedule the _callback_ [callback](https://docs.python.org/3/glossary.html#term-callback)
 to be called with _args_ arguments at the next iteration of the event loop.

Return an instance of [`asyncio.Handle`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Handle "asyncio.Handle")
, which can be used later to cancel the callback.

Callbacks are called in the order in which they are registered. Each callback will be called exactly once.

The optional keyword-only _context_ argument specifies a custom [`contextvars.Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
 for the _callback_ to run in. Callbacks use the current context when no _context_ is provided.

Unlike [`call_soon_threadsafe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe")
, this method is not thread-safe.

loop.call\_soon\_threadsafe(_callback_, _\*args_, _context\=None_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "Link to this definition")

A thread-safe variant of [`call_soon()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")
. When scheduling callbacks from another thread, this function _must_ be used, since `call_soon()` is not thread-safe.

This function is safe to be called from a reentrant context or signal handler, however, it is not safe or fruitful to use the returned handle in such contexts.

Raises [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 if called on a loop that’s been closed. This can happen on a secondary thread when the main application is shutting down.

See the [concurrency and multithreading](https://docs.python.org/3/library/asyncio-dev.html#asyncio-multithreading)
 section of the documentation.

Changed in version 3.7: The _context_ keyword-only parameter was added. See [**PEP 567**](https://peps.python.org/pep-0567/)
 for more details.

Note

Most [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")
 scheduling functions don’t allow passing keyword arguments. To do that, use [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
:

Copy

\# will schedule "print("Hello", flush=True)"
loop.call\_soon(
    functools.partial(print, "Hello", flush\=True))

Using partial objects is usually more convenient than using lambdas, as asyncio can render partial objects better in debug and error messages.

### [Scheduling delayed callbacks](https://docs.python.org/3/library/asyncio-eventloop.html#id3)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#scheduling-delayed-callbacks "Link to this heading")

Event loop provides mechanisms to schedule callback functions to be called at some point in the future. Event loop uses monotonic clocks to track time.

loop.call\_later(_delay_, _callback_, _\*args_, _context\=None_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_later "Link to this definition")

Schedule _callback_ to be called after the given _delay_ number of seconds (can be either an int or a float).

An instance of [`asyncio.TimerHandle`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.TimerHandle "asyncio.TimerHandle")
 is returned which can be used to cancel the callback.

_callback_ will be called exactly once. If two callbacks are scheduled for exactly the same time, the order in which they are called is undefined.

The optional positional _args_ will be passed to the callback when it is called. Use [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 [to pass keyword arguments](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-pass-keywords)
 to _callback_.

An optional keyword-only _context_ argument allows specifying a custom [`contextvars.Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
 for the _callback_ to run in. The current context is used when no _context_ is provided.

Note

For performance, callbacks scheduled with `loop.call_later()` may run up to one clock-resolution early (see `time.get_clock_info('monotonic').resolution`).

Changed in version 3.7: The _context_ keyword-only parameter was added. See [**PEP 567**](https://peps.python.org/pep-0567/)
 for more details.

Changed in version 3.8: In Python 3.7 and earlier with the default event loop implementation, the _delay_ could not exceed one day. This has been fixed in Python 3.8.

loop.call\_at(_when_, _callback_, _\*args_, _context\=None_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_at "Link to this definition")

Schedule _callback_ to be called at the given absolute timestamp _when_ (an int or a float), using the same time reference as [`loop.time()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.time "asyncio.loop.time")
.

This method’s behavior is the same as [`call_later()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_later "asyncio.loop.call_later")
.

An instance of [`asyncio.TimerHandle`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.TimerHandle "asyncio.TimerHandle")
 is returned which can be used to cancel the callback.

Note

For performance, callbacks scheduled with `loop.call_at()` may run up to one clock-resolution early (see `time.get_clock_info('monotonic').resolution`).

Changed in version 3.7: The _context_ keyword-only parameter was added. See [**PEP 567**](https://peps.python.org/pep-0567/)
 for more details.

Changed in version 3.8: In Python 3.7 and earlier with the default event loop implementation, the difference between _when_ and the current time could not exceed one day. This has been fixed in Python 3.8.

loop.time()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.time "Link to this definition")

Return the current time, as a [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 value, according to the event loop’s internal monotonic clock.

Note

Changed in version 3.8: In Python 3.7 and earlier timeouts (relative _delay_ or absolute _when_) should not exceed one day. This has been fixed in Python 3.8.

See also

The [`asyncio.sleep()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep "asyncio.sleep")
 function.

### [Creating futures and tasks](https://docs.python.org/3/library/asyncio-eventloop.html#id4)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#creating-futures-and-tasks "Link to this heading")

loop.create\_future()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_future "Link to this definition")

Create an [`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
 object attached to the event loop.

This is the preferred way to create Futures in asyncio. This lets third-party event loops provide alternative implementations of the Future object (with better performance or instrumentation).

Added in version 3.5.2.

loop.create\_task(_coro_, _\*_, _name\=None_, _context\=None_, _eager\_start\=None_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task "Link to this definition")

Schedule the execution of [coroutine](https://docs.python.org/3/library/asyncio-task.html#coroutine)
 _coro_. Return a [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
 object.

Third-party event loops can use their own subclass of [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
 for interoperability. In this case, the result type is a subclass of `Task`.

The full function signature is largely the same as that of the [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
 constructor (or factory) - all of the keyword arguments to this function are passed through to that interface.

If the _name_ argument is provided and not `None`, it is set as the name of the task using [`Task.set_name()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.set_name "asyncio.Task.set_name")
.

An optional keyword-only _context_ argument allows specifying a custom [`contextvars.Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
 for the _coro_ to run in. The current context copy is created when no _context_ is provided.

An optional keyword-only _eager\_start_ argument allows specifying if the task should execute eagerly during the call to create\_task, or be scheduled later. If _eager\_start_ is not passed the mode set by [`loop.set_task_factory()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_task_factory "asyncio.loop.set_task_factory")
 will be used.

Changed in version 3.8: Added the _name_ parameter.

Changed in version 3.11: Added the _context_ parameter.

Changed in version 3.13.3: Added `kwargs` which passes on arbitrary extra parameters, including `name` and `context`.

Changed in version 3.13.4: Rolled back the change that passes on _name_ and _context_ (if it is None), while still passing on other arbitrary keyword arguments (to avoid breaking backwards compatibility with 3.13.3).

Changed in version 3.14: All _kwargs_ are now passed on. The _eager\_start_ parameter works with eager task factories.

loop.set\_task\_factory(_factory_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_task_factory "Link to this definition")

Set a task factory that will be used by [`loop.create_task()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task")
.

If _factory_ is `None` the default task factory will be set. Otherwise, _factory_ must be a _callable_ with the signature matching `(loop, coro, **kwargs)`, where _loop_ is a reference to the active event loop, and _coro_ is a coroutine object. The callable must pass on all _kwargs_, and return a [`asyncio.Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
\-compatible object.

Changed in version 3.13.3: Required that all _kwargs_ are passed on to [`asyncio.Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
.

Changed in version 3.13.4: _name_ is no longer passed to task factories. _context_ is no longer passed to task factories if it is `None`.

Changed in version 3.14: _name_ and _context_ are now unconditionally passed on to task factories again.

loop.get\_task\_factory()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.get_task_factory "Link to this definition")

Return a task factory or `None` if the default one is in use.

### [Opening network connections](https://docs.python.org/3/library/asyncio-eventloop.html#id5)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#opening-network-connections "Link to this heading")

async loop.create\_connection(_protocol\_factory_, _host\=None_, _port\=None_, _\*_, _ssl\=None_, _family\=0_, _proto\=0_, _flags\=0_, _sock\=None_, _local\_addr\=None_, _server\_hostname\=None_, _ssl\_handshake\_timeout\=None_, _ssl\_shutdown\_timeout\=None_, _happy\_eyeballs\_delay\=None_, _interleave\=None_, _all\_errors\=False_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "Link to this definition")

Open a streaming transport connection to a given address specified by _host_ and _port_.

The socket family can be either [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
 or [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
 depending on _host_ (or the _family_ argument, if provided).

The socket type will be [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")
.

_protocol\_factory_ must be a callable returning an [asyncio protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-protocol)
 implementation.

This method will try to establish the connection in the background. When successful, it returns a `(transport, protocol)` pair.

The chronological synopsis of the underlying operation is as follows:

1.  The connection is established and a [transport](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-transport)
     is created for it.
    
2.  _protocol\_factory_ is called without arguments and is expected to return a [protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-protocol)
     instance.
    
3.  The protocol instance is coupled with the transport by calling its [`connection_made()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseProtocol.connection_made "asyncio.BaseProtocol.connection_made")
     method.
    
4.  A `(transport, protocol)` tuple is returned on success.
    

The created transport is an implementation-dependent bidirectional stream.

Other arguments:

*   _ssl_: if given and not false, a SSL/TLS transport is created (by default a plain TCP transport is created). If _ssl_ is a [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
     object, this context is used to create the transport; if _ssl_ is [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
    , a default context returned from [`ssl.create_default_context()`](https://docs.python.org/3/library/ssl.html#ssl.create_default_context "ssl.create_default_context")
     is used.
    
    See also
    
    [SSL/TLS security considerations](https://docs.python.org/3/library/ssl.html#ssl-security)
    
*   _server\_hostname_ sets or overrides the hostname that the target server’s certificate will be matched against. Should only be passed if _ssl_ is not `None`. By default the value of the _host_ argument is used. If _host_ is empty, there is no default and you must pass a value for _server\_hostname_. If _server\_hostname_ is an empty string, hostname matching is disabled (which is a serious security risk, allowing for potential man-in-the-middle attacks).
    
*   _family_, _proto_, _flags_ are the optional address family, protocol and flags to be passed through to getaddrinfo() for _host_ resolution. If given, these should all be integers from the corresponding [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.")
     module constants.
    
*   _happy\_eyeballs\_delay_, if given, enables Happy Eyeballs for this connection. It should be a floating-point number representing the amount of time in seconds to wait for a connection attempt to complete, before starting the next attempt in parallel. This is the “Connection Attempt Delay” as defined in [**RFC 8305**](https://datatracker.ietf.org/doc/html/rfc8305.html)
    . A sensible default value recommended by the RFC is `0.25` (250 milliseconds).
    
*   _interleave_ controls address reordering when a host name resolves to multiple IP addresses. If `0` or unspecified, no reordering is done, and addresses are tried in the order returned by [`getaddrinfo()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo")
    . If a positive integer is specified, the addresses are interleaved by address family, and the given integer is interpreted as “First Address Family Count” as defined in [**RFC 8305**](https://datatracker.ietf.org/doc/html/rfc8305.html)
    . The default is `0` if _happy\_eyeballs\_delay_ is not specified, and `1` if it is.
    
*   _sock_, if given, should be an existing, already connected [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
     object to be used by the transport. If _sock_ is given, none of _host_, _port_, _family_, _proto_, _flags_, _happy\_eyeballs\_delay_, _interleave_ and _local\_addr_ should be specified.
    
    Note
    
    The _sock_ argument transfers ownership of the socket to the transport created. To close the socket, call the transport’s [`close()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.close "asyncio.BaseTransport.close")
     method.
    
*   _local\_addr_, if given, is a `(local_host, local_port)` tuple used to bind the socket locally. The _local\_host_ and _local\_port_ are looked up using `getaddrinfo()`, similarly to _host_ and _port_.
    
*   _ssl\_handshake\_timeout_ is (for a TLS connection) the time in seconds to wait for the TLS handshake to complete before aborting the connection. `60.0` seconds if `None` (default).
    
*   _ssl\_shutdown\_timeout_ is the time in seconds to wait for the SSL shutdown to complete before aborting the connection. `30.0` seconds if `None` (default).
    
*   _all\_errors_ determines what exceptions are raised when a connection cannot be created. By default, only a single `Exception` is raised: the first exception if there is only one or all errors have same message, or a single `OSError` with the error messages combined. When `all_errors` is `True`, an `ExceptionGroup` will be raised containing all exceptions (even if there is only one).
    

Changed in version 3.5: Added support for SSL/TLS in [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
.

Changed in version 3.6: The socket option [socket.TCP\_NODELAY](https://docs.python.org/3/library/socket.html#socket-unix-constants)
 is set by default for all TCP connections.

Changed in version 3.7: Added the _ssl\_handshake\_timeout_ parameter.

Changed in version 3.8: Added the _happy\_eyeballs\_delay_ and _interleave_ parameters.

Happy Eyeballs Algorithm: Success with Dual-Stack Hosts. When a server’s IPv4 path and protocol are working, but the server’s IPv6 path and protocol are not working, a dual-stack client application experiences significant connection delay compared to an IPv4-only client. This is undesirable because it causes the dual-stack client to have a worse user experience. This document specifies requirements for algorithms that reduce this user-visible delay and provides an algorithm.

For more information: [https://datatracker.ietf.org/doc/html/rfc6555](https://datatracker.ietf.org/doc/html/rfc6555)

Changed in version 3.11: Added the _ssl\_shutdown\_timeout_ parameter.

Changed in version 3.12: _all\_errors_ was added.

Changed in version 3.15: Raises a `ValueError` if `ssl.check_hostname` is `True` and `server_hostname` is not supplied.

See also

The [`open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection")
 function is a high-level alternative API. It returns a pair of ([`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")
, [`StreamWriter`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter")
) that can be used directly in async/await code.

async loop.create\_datagram\_endpoint(_protocol\_factory_, _local\_addr\=None_, _remote\_addr\=None_, _\*_, _family\=0_, _proto\=0_, _flags\=0_, _reuse\_port\=None_, _allow\_broadcast\=None_, _sock\=None_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint "Link to this definition")

Create a datagram connection.

The socket family can be either [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
, [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
, or [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
, depending on _host_ (or the _family_ argument, if provided).

The socket type will be [`SOCK_DGRAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "socket.SOCK_DGRAM")
.

_protocol\_factory_ must be a callable returning a [protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-protocol)
 implementation.

A tuple of `(transport, protocol)` is returned on success.

Other arguments:

*   _local\_addr_, if given, is a `(local_host, local_port)` tuple used to bind the socket locally. The _local\_host_ and _local\_port_ are looked up using [`getaddrinfo()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo")
    .
    
    Note
    
    On Windows, when using the proactor event loop with `local_addr=None`, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
     with `errno.WSAEINVAL` will be raised when running it.
    
*   _remote\_addr_, if given, is a `(remote_host, remote_port)` tuple used to connect the socket to a remote address. The _remote\_host_ and _remote\_port_ are looked up using [`getaddrinfo()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo")
    .
    
*   _family_, _proto_, _flags_ are the optional address family, protocol and flags to be passed through to [`getaddrinfo()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo")
     for _host_ resolution. If given, these should all be integers from the corresponding [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.")
     module constants.
    
*   _reuse\_port_ tells the kernel to allow this endpoint to be bound to the same port as other existing endpoints are bound to, so long as they all set this flag when being created. This option is not supported on Windows and some Unixes. If the [socket.SO\_REUSEPORT](https://docs.python.org/3/library/socket.html#socket-unix-constants)
     constant is not defined then this capability is unsupported.
    
*   _allow\_broadcast_ tells the kernel to allow this endpoint to send messages to the broadcast address.
    
*   _sock_ can optionally be specified in order to use a preexisting, already connected, [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
     object to be used by the transport. If specified, _local\_addr_ and _remote\_addr_ should be omitted (must be [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
    ).
    
    Note
    
    The _sock_ argument transfers ownership of the socket to the transport created. To close the socket, call the transport’s [`close()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.close "asyncio.BaseTransport.close")
     method.
    

See [UDP echo client protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-udp-echo-client-protocol)
 and [UDP echo server protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-udp-echo-server-protocol)
 examples.

Changed in version 3.4.4: The _family_, _proto_, _flags_, _reuse\_address_, _reuse\_port_, _allow\_broadcast_, and _sock_ parameters were added.

Changed in version 3.8: Added support for Windows.

Changed in version 3.8.1: The _reuse\_address_ parameter is no longer supported, as using [socket.SO\_REUSEADDR](https://docs.python.org/3/library/socket.html#socket-unix-constants)
 poses a significant security concern for UDP. Explicitly passing `reuse_address=True` will raise an exception.

When multiple processes with differing UIDs assign sockets to an identical UDP socket address with `SO_REUSEADDR`, incoming packets can become randomly distributed among the sockets.

For supported platforms, _reuse\_port_ can be used as a replacement for similar functionality. With _reuse\_port_, [socket.SO\_REUSEPORT](https://docs.python.org/3/library/socket.html#socket-unix-constants)
 is used instead, which specifically prevents processes with differing UIDs from assigning sockets to the same socket address.

Changed in version 3.11: The _reuse\_address_ parameter, disabled since Python 3.8.1, 3.7.6 and 3.6.10, has been entirely removed.

async loop.create\_unix\_connection(_protocol\_factory_, _path\=None_, _\*_, _ssl\=None_, _sock\=None_, _server\_hostname\=None_, _ssl\_handshake\_timeout\=None_, _ssl\_shutdown\_timeout\=None_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "Link to this definition")

Create a Unix connection.

The socket family will be [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
; socket type will be [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")
.

A tuple of `(transport, protocol)` is returned on success.

_path_ is the name of a Unix domain socket and is required, unless a _sock_ parameter is specified. Abstract Unix sockets, [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
, and [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
 paths are supported.

See the documentation of the [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
 method for information about arguments to this method.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Changed in version 3.7: Added the _ssl\_handshake\_timeout_ parameter. The _path_ parameter can now be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.11: Added the _ssl\_shutdown\_timeout_ parameter.

### [Creating network servers](https://docs.python.org/3/library/asyncio-eventloop.html#id6)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#creating-network-servers "Link to this heading")

async loop.create\_server(_protocol\_factory_, _host\=None_, _port\=None_, _\*_, _family\=socket.AF\_UNSPEC_, _flags\=socket.AI\_PASSIVE_, _sock\=None_, _backlog\=100_, _ssl\=None_, _reuse\_address\=None_, _reuse\_port\=None_, _keep\_alive\=None_, _ssl\_handshake\_timeout\=None_, _ssl\_shutdown\_timeout\=None_, _start\_serving\=True_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "Link to this definition")

Create a TCP server (socket type [`SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")
) listening on _port_ of the _host_ address.

Returns a [`Server`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server "asyncio.Server")
 object.

Arguments:

*   _protocol\_factory_ must be a callable returning a [protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-protocol)
     implementation.
    
*   The _host_ parameter can be set to several types which determine where the server would be listening:
    
    *   If _host_ is a string, the TCP server is bound to a single network interface specified by _host_.
        
    *   If _host_ is a sequence of strings, the TCP server is bound to all network interfaces specified by the sequence.
        
    *   If _host_ is an empty string or `None`, all interfaces are assumed and a list of multiple sockets will be returned (most likely one for IPv4 and another one for IPv6).
        
*   The _port_ parameter can be set to specify which port the server should listen on. If `0` or `None` (the default), a random unused port will be selected (note that if _host_ resolves to multiple network interfaces, a different random port will be selected for each interface).
    
*   _family_ can be set to either [`socket.AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
     or [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
     to force the socket to use IPv4 or IPv6. If not set, the _family_ will be determined from host name (defaults to [`AF_UNSPEC`](https://docs.python.org/3/library/socket.html#socket.AF_UNSPEC "socket.AF_UNSPEC")
    ).
    
*   _flags_ is a bitmask for [`getaddrinfo()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo")
    .
    
*   _sock_ can optionally be specified in order to use a preexisting socket object. If specified, _host_ and _port_ must not be specified.
    
    Note
    
    The _sock_ argument transfers ownership of the socket to the server created. To close the socket, call the server’s [`close()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.close "asyncio.Server.close")
     method.
    
*   _backlog_ is the maximum number of queued connections passed to [`listen()`](https://docs.python.org/3/library/socket.html#socket.socket.listen "socket.socket.listen")
     (defaults to 100).
    
*   _ssl_ can be set to an [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
     instance to enable TLS over the accepted connections.
    
*   _reuse\_address_ tells the kernel to reuse a local socket in `TIME_WAIT` state, without waiting for its natural timeout to expire. If not specified will automatically be set to `True` on Unix.
    
*   _reuse\_port_ tells the kernel to allow this endpoint to be bound to the same port as other existing endpoints are bound to, so long as they all set this flag when being created. This option is not supported on Windows.
    
*   _keep\_alive_ set to `True` keeps connections active by enabling the periodic transmission of messages.
    

Changed in version 3.13: Added the _keep\_alive_ parameter.

*   _ssl\_handshake\_timeout_ is (for a TLS server) the time in seconds to wait for the TLS handshake to complete before aborting the connection. `60.0` seconds if `None` (default).
    
*   _ssl\_shutdown\_timeout_ is the time in seconds to wait for the SSL shutdown to complete before aborting the connection. `30.0` seconds if `None` (default).
    
*   _start\_serving_ set to `True` (the default) causes the created server to start accepting connections immediately. When set to `False`, the user should await on [`Server.start_serving()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.start_serving "asyncio.Server.start_serving")
     or [`Server.serve_forever()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.serve_forever "asyncio.Server.serve_forever")
     to make the server to start accepting connections.
    

Changed in version 3.5: Added support for SSL/TLS in [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
.

Changed in version 3.5.1: The _host_ parameter can be a sequence of strings.

Changed in version 3.6: Added _ssl\_handshake\_timeout_ and _start\_serving_ parameters. The socket option [socket.TCP\_NODELAY](https://docs.python.org/3/library/socket.html#socket-unix-constants)
 is set by default for all TCP connections.

Changed in version 3.11: Added the _ssl\_shutdown\_timeout_ parameter.

See also

The [`start_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server")
 function is a higher-level alternative API that returns a pair of [`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")
 and [`StreamWriter`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter")
 that can be used in an async/await code.

async loop.create\_unix\_server(_protocol\_factory_, _path\=None_, _\*_, _sock\=None_, _backlog\=100_, _ssl\=None_, _ssl\_handshake\_timeout\=None_, _ssl\_shutdown\_timeout\=None_, _start\_serving\=True_, _cleanup\_socket\=True_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_server "Link to this definition")

Similar to [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
 but works with the [`AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX")
 socket family.

_path_ is the name of a Unix domain socket, and is required, unless a _sock_ argument is provided. Abstract Unix sockets, [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
, and [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
 paths are supported.

If _cleanup\_socket_ is true then the Unix socket will automatically be removed from the filesystem when the server is closed, unless the socket has been replaced after the server has been created.

See the documentation of the [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
 method for information about arguments to this method.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Changed in version 3.7: Added the _ssl\_handshake\_timeout_ and _start\_serving_ parameters. The _path_ parameter can now be a [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")
 object.

Changed in version 3.11: Added the _ssl\_shutdown\_timeout_ parameter.

Changed in version 3.13: Added the _cleanup\_socket_ parameter.

async loop.connect\_accepted\_socket(_protocol\_factory_, _sock_, _\*_, _ssl\=None_, _ssl\_handshake\_timeout\=None_, _ssl\_shutdown\_timeout\=None_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_accepted_socket "Link to this definition")

Wrap an already accepted connection into a transport/protocol pair.

This method can be used by servers that accept connections outside of asyncio but that use asyncio to handle them.

Parameters:

*   _protocol\_factory_ must be a callable returning a [protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-protocol)
     implementation.
    
*   _sock_ is a preexisting socket object returned from [`socket.accept`](https://docs.python.org/3/library/socket.html#socket.socket.accept "socket.socket.accept")
    .
    
    Note
    
    The _sock_ argument transfers ownership of the socket to the transport created. To close the socket, call the transport’s [`close()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.close "asyncio.BaseTransport.close")
     method.
    
*   _ssl_ can be set to an [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
     to enable SSL over the accepted connections.
    
*   _ssl\_handshake\_timeout_ is (for an SSL connection) the time in seconds to wait for the SSL handshake to complete before aborting the connection. `60.0` seconds if `None` (default).
    
*   _ssl\_shutdown\_timeout_ is the time in seconds to wait for the SSL shutdown to complete before aborting the connection. `30.0` seconds if `None` (default).
    

Returns a `(transport, protocol)` pair.

Added in version 3.5.3.

Changed in version 3.7: Added the _ssl\_handshake\_timeout_ parameter.

Changed in version 3.11: Added the _ssl\_shutdown\_timeout_ parameter.

### [Transferring files](https://docs.python.org/3/library/asyncio-eventloop.html#id7)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#transferring-files "Link to this heading")

async loop.sendfile(_transport_, _file_, _offset\=0_, _count\=None_, _\*_, _fallback\=True_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sendfile "Link to this definition")

Send a _file_ over a _transport_. Return the total number of bytes sent.

The method uses high-performance [`os.sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile")
 if available.

_file_ must be a regular file object opened in binary mode.

_offset_ tells from where to start reading the file. If specified, _count_ is the total number of bytes to transmit as opposed to sending the file until EOF is reached. File position is always updated, even when this method raises an error, and [`file.tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell")
 can be used to obtain the actual number of bytes sent.

_fallback_ set to `True` makes asyncio to manually read and send the file when the platform does not support the sendfile system call (e.g. Windows or SSL socket on Unix).

Raise [`SendfileNotAvailableError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.SendfileNotAvailableError "asyncio.SendfileNotAvailableError")
 if the system does not support the _sendfile_ syscall and _fallback_ is `False`.

Added in version 3.7.

### [TLS upgrade](https://docs.python.org/3/library/asyncio-eventloop.html#id8)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#tls-upgrade "Link to this heading")

async loop.start\_tls(_transport_, _protocol_, _sslcontext_, _\*_, _server\_side\=False_, _server\_hostname\=None_, _ssl\_handshake\_timeout\=None_, _ssl\_shutdown\_timeout\=None_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.start_tls "Link to this definition")

Upgrade an existing transport-based connection to TLS.

Create a TLS coder/decoder instance and insert it between the _transport_ and the _protocol_. The coder/decoder implements both _transport_\-facing protocol and _protocol_\-facing transport.

Return the created two-interface instance. After _await_, the _protocol_ must stop using the original _transport_ and communicate with the returned object only because the coder caches _protocol_\-side data and sporadically exchanges extra TLS session packets with _transport_.

In some situations (e.g. when the passed transport is already closing) this may return `None`.

Parameters:

*   _transport_ and _protocol_ instances that methods like [`create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
     and [`create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
     return.
    
*   _sslcontext_: a configured instance of [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
    .
    
*   _server\_side_ pass `True` when a server-side connection is being upgraded (like the one created by [`create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
    ).
    
*   _server\_hostname_: sets or overrides the host name that the target server’s certificate will be matched against.
    
*   _ssl\_handshake\_timeout_ is (for a TLS connection) the time in seconds to wait for the TLS handshake to complete before aborting the connection. `60.0` seconds if `None` (default).
    
*   _ssl\_shutdown\_timeout_ is the time in seconds to wait for the SSL shutdown to complete before aborting the connection. `30.0` seconds if `None` (default).
    

Added in version 3.7.

Changed in version 3.11: Added the _ssl\_shutdown\_timeout_ parameter.

### [Watching file descriptors](https://docs.python.org/3/library/asyncio-eventloop.html#id9)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#watching-file-descriptors "Link to this heading")

loop.add\_reader(_fd_, _callback_, _\*args_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_reader "Link to this definition")

Start monitoring the _fd_ file descriptor for read availability and invoke _callback_ with the specified arguments once _fd_ is available for reading.

Any preexisting callback registered for _fd_ is cancelled and replaced by _callback_.

loop.remove\_reader(_fd_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.remove_reader "Link to this definition")

Stop monitoring the _fd_ file descriptor for read availability. Returns `True` if _fd_ was previously being monitored for reads.

loop.add\_writer(_fd_, _callback_, _\*args_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_writer "Link to this definition")

Start monitoring the _fd_ file descriptor for write availability and invoke _callback_ with the specified arguments _args_ once _fd_ is available for writing.

Any preexisting callback registered for _fd_ is cancelled and replaced by _callback_.

Use [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 [to pass keyword arguments](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-pass-keywords)
 to _callback_.

loop.remove\_writer(_fd_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.remove_writer "Link to this definition")

Stop monitoring the _fd_ file descriptor for write availability. Returns `True` if _fd_ was previously being monitored for writes.

See also [Platform Support](https://docs.python.org/3/library/asyncio-platforms.html#asyncio-platform-support)
 section for some limitations of these methods.

### [Working with socket objects directly](https://docs.python.org/3/library/asyncio-eventloop.html#id10)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#working-with-socket-objects-directly "Link to this heading")

In general, protocol implementations that use transport-based APIs such as [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
 and [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
 are faster than implementations that work with sockets directly. However, there are some use cases when performance is not critical, and working with [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
 objects directly is more convenient.

async loop.sock\_recv(_sock_, _nbytes_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_recv "Link to this definition")

Receive up to _nbytes_ from _sock_. Asynchronous version of [`socket.recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv")
.

Return the received data as a bytes object.

_sock_ must be a non-blocking socket.

Changed in version 3.7: Even though this method was always documented as a coroutine method, releases before Python 3.7 returned a [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
. Since Python 3.7 this is an `async def` method.

async loop.sock\_recv\_into(_sock_, _buf_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_recv_into "Link to this definition")

Receive data from _sock_ into the _buf_ buffer. Modeled after the blocking [`socket.recv_into()`](https://docs.python.org/3/library/socket.html#socket.socket.recv_into "socket.socket.recv_into")
 method.

Return the number of bytes written to the buffer.

_sock_ must be a non-blocking socket.

Added in version 3.7.

async loop.sock\_recvfrom(_sock_, _bufsize_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_recvfrom "Link to this definition")

Receive a datagram of up to _bufsize_ from _sock_. Asynchronous version of [`socket.recvfrom()`](https://docs.python.org/3/library/socket.html#socket.socket.recvfrom "socket.socket.recvfrom")
.

Return a tuple of (received data, remote address).

_sock_ must be a non-blocking socket.

Added in version 3.11.

async loop.sock\_recvfrom\_into(_sock_, _buf_, _nbytes\=0_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_recvfrom_into "Link to this definition")

Receive a datagram of up to _nbytes_ from _sock_ into _buf_. Asynchronous version of [`socket.recvfrom_into()`](https://docs.python.org/3/library/socket.html#socket.socket.recvfrom_into "socket.socket.recvfrom_into")
.

Return a tuple of (number of bytes received, remote address).

_sock_ must be a non-blocking socket.

Added in version 3.11.

async loop.sock\_sendall(_sock_, _data_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_sendall "Link to this definition")

Send _data_ to the _sock_ socket. Asynchronous version of [`socket.sendall()`](https://docs.python.org/3/library/socket.html#socket.socket.sendall "socket.socket.sendall")
.

This method continues to send to the socket until either all data in _data_ has been sent or an error occurs. `None` is returned on success. On error, an exception is raised. Additionally, there is no way to determine how much data, if any, was successfully processed by the receiving end of the connection.

_sock_ must be a non-blocking socket.

Changed in version 3.7: Even though the method was always documented as a coroutine method, before Python 3.7 it returned a [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
. Since Python 3.7, this is an `async def` method.

async loop.sock\_sendto(_sock_, _data_, _address_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_sendto "Link to this definition")

Send a datagram from _sock_ to _address_. Asynchronous version of [`socket.sendto()`](https://docs.python.org/3/library/socket.html#socket.socket.sendto "socket.socket.sendto")
.

Return the number of bytes sent.

_sock_ must be a non-blocking socket.

Added in version 3.11.

async loop.sock\_connect(_sock_, _address_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_connect "Link to this definition")

Connect _sock_ to a remote socket at _address_.

Asynchronous version of [`socket.connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect")
.

_sock_ must be a non-blocking socket.

With [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
, _address_ does not need to be resolved: for [`AF_INET`](https://docs.python.org/3/library/socket.html#socket.AF_INET "socket.AF_INET")
 and [`AF_INET6`](https://docs.python.org/3/library/socket.html#socket.AF_INET6 "socket.AF_INET6")
 sockets, `sock_connect` first checks whether _address_ is already resolved by calling [`socket.inet_pton()`](https://docs.python.org/3/library/socket.html#socket.inet_pton "socket.inet_pton")
, and uses [`loop.getaddrinfo()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo")
 to resolve it if it is not.

[`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
, the default event loop on Windows, does not resolve _address_. The host must already be a numeric IP address; passing a host name raises [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
. Resolve the address with [`loop.getaddrinfo()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "asyncio.loop.getaddrinfo")
 first, or use [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
, which resolves the address on every platform.

Changed in version 3.5.2: With [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
, `address` no longer needs to be resolved.

See also

[`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
 and [`asyncio.open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection")
.

async loop.sock\_accept(_sock_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_accept "Link to this definition")

Accept a connection. Modeled after the blocking [`socket.accept()`](https://docs.python.org/3/library/socket.html#socket.socket.accept "socket.socket.accept")
 method.

The socket must be bound to an address and listening for connections. The return value is a pair `(conn, address)` where _conn_ is a _new_ socket object usable to send and receive data on the connection, and _address_ is the address bound to the socket on the other end of the connection.

_sock_ must be a non-blocking socket.

Changed in version 3.7: Even though the method was always documented as a coroutine method, before Python 3.7 it returned a [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
. Since Python 3.7, this is an `async def` method.

See also

[`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
 and [`start_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server")
.

async loop.sock\_sendfile(_sock_, _file_, _offset\=0_, _count\=None_, _\*_, _fallback\=True_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_sendfile "Link to this definition")

Send a file using high-performance [`os.sendfile`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile")
 if possible. Return the total number of bytes sent.

Asynchronous version of [`socket.sendfile()`](https://docs.python.org/3/library/socket.html#socket.socket.sendfile "socket.socket.sendfile")
.

_sock_ must be a non-blocking [`socket.SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")
 [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
.

_file_ must be a regular file object open in binary mode.

_offset_ tells from where to start reading the file. If specified, _count_ is the total number of bytes to transmit as opposed to sending the file until EOF is reached. File position is always updated, even when this method raises an error, and [`file.tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell")
 can be used to obtain the actual number of bytes sent.

_fallback_, when set to `True`, makes asyncio manually read and send the file when the platform does not support the sendfile syscall (e.g. Windows or SSL socket on Unix).

Raise [`SendfileNotAvailableError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.SendfileNotAvailableError "asyncio.SendfileNotAvailableError")
 if the system does not support _sendfile_ syscall and _fallback_ is `False`.

_sock_ must be a non-blocking socket.

Added in version 3.7.

### [DNS](https://docs.python.org/3/library/asyncio-eventloop.html#id11)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#dns "Link to this heading")

async loop.getaddrinfo(_host_, _port_, _\*_, _family\=0_, _type\=0_, _proto\=0_, _flags\=0_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getaddrinfo "Link to this definition")

Asynchronous version of [`socket.getaddrinfo()`](https://docs.python.org/3/library/socket.html#socket.getaddrinfo "socket.getaddrinfo")
.

async loop.getnameinfo(_sockaddr_, _flags\=0_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.getnameinfo "Link to this definition")

Asynchronous version of [`socket.getnameinfo()`](https://docs.python.org/3/library/socket.html#socket.getnameinfo "socket.getnameinfo")
.

Note

Both _getaddrinfo_ and _getnameinfo_ internally utilize their synchronous versions through the loop’s default thread pool executor. When this executor is saturated, these methods may experience delays, which higher-level networking libraries may report as increased timeouts. To mitigate this, consider using a custom executor for other user tasks, or setting a default executor with a larger number of workers.

Changed in version 3.7: Both _getaddrinfo_ and _getnameinfo_ methods were always documented to return a coroutine, but prior to Python 3.7 they were, in fact, returning [`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
 objects. Starting with Python 3.7 both methods are coroutines.

### [Working with pipes](https://docs.python.org/3/library/asyncio-eventloop.html#id12)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#working-with-pipes "Link to this heading")

async loop.connect\_read\_pipe(_protocol\_factory_, _pipe_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "Link to this definition")

Register the read end of _pipe_ in the event loop.

_protocol\_factory_ must be a callable returning an [asyncio protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-protocol)
 implementation.

_pipe_ is a [file-like object](https://docs.python.org/3/glossary.html#term-file-object)
. See [Supported pipe objects](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-pipe-objects)
 for the objects supported as _pipe_.

Return pair `(transport, protocol)`, where _transport_ supports the [`ReadTransport`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.ReadTransport "asyncio.ReadTransport")
 interface and _protocol_ is an object instantiated by the _protocol\_factory_.

With [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
 event loop, the _pipe_ is set to non-blocking mode.

async loop.connect\_write\_pipe(_protocol\_factory_, _pipe_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "Link to this definition")

Register the write end of _pipe_ in the event loop.

_protocol\_factory_ must be a callable returning an [asyncio protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-protocol)
 implementation.

_pipe_ is a [file-like object](https://docs.python.org/3/glossary.html#term-file-object)
. See [Supported pipe objects](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-pipe-objects)
 for the objects supported as _pipe_.

Return pair `(transport, protocol)`, where _transport_ supports [`WriteTransport`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport "asyncio.WriteTransport")
 interface and _protocol_ is an object instantiated by the _protocol\_factory_.

With [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
 event loop, the _pipe_ is set to non-blocking mode.

Supported pipe objects

These methods only work with objects the operating system can poll for readiness or perform overlapped I/O on. Regular files on disk are **not** supported on any platform. There is no asynchronous file I/O in asyncio; use [`loop.run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")
 to read and write regular files without blocking the event loop.

On Unix, with [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
, _pipe_ must wrap one of the following:

*   a pipe, such as an end of an [`os.pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe")
     pair or a FIFO created with [`os.mkfifo()`](https://docs.python.org/3/library/os.html#os.mkfifo "os.mkfifo")
    ;
    
*   a socket;
    
*   a character device, such as a terminal.
    

On Windows, where only [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
 implements these methods, _pipe_ must wrap a handle opened for overlapped I/O (that is, created with the `FILE_FLAG_OVERLAPPED` flag), since the handle has to be associated with an I/O completion port. Handles that were not opened for overlapped I/O are rejected. In particular, the standard streams ([`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout")
 and [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
), console handles, and the pipes created by [`os.pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe")
 are **not** opened for overlapped I/O and therefore cannot be used with these methods.

Note

[`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
 does not support the above methods on Windows. Use [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
 instead for Windows.

See also

The [`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")
 and [`loop.subprocess_shell()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell")
 methods.

### [Unix signals](https://docs.python.org/3/library/asyncio-eventloop.html#id13)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#unix-signals "Link to this heading")

loop.add\_signal\_handler(_signum_, _callback_, _\*args_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler "Link to this definition")

Set _callback_ as the handler for the _signum_ signal, passing _args_ as positional arguments.

The callback will be invoked by _loop_, along with other queued callbacks and runnable coroutines of that event loop. Unlike signal handlers registered using [`signal.signal()`](https://docs.python.org/3/library/signal.html#signal.signal "signal.signal")
, a callback registered with this function is allowed to interact with the event loop.

Raise [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if the signal number is invalid or uncatchable. Raise [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 if there is a problem setting up the handler.

Use [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 [to pass keyword arguments](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-pass-keywords)
 to _callback_.

Like [`signal.signal()`](https://docs.python.org/3/library/signal.html#signal.signal "signal.signal")
, this function must be invoked in the main thread.

loop.remove\_signal\_handler(_sig_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.remove_signal_handler "Link to this definition")

Remove the handler for the _sig_ signal.

Return `True` if the signal handler was removed, or `False` if no handler was set for the given signal.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

See also

The [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")
 module.

### [Executing code in thread or process pools](https://docs.python.org/3/library/asyncio-eventloop.html#id14)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#executing-code-in-thread-or-process-pools "Link to this heading")

awaitable loop.run\_in\_executor(_executor_, _func_, _\*args_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "Link to this definition")

Arrange for _func_ to be called in the specified executor passing _args_ as positional arguments.

The _executor_ argument should be an [`concurrent.futures.Executor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor "concurrent.futures.Executor")
 instance. The default executor is used if _executor_ is `None`. The default executor can be set by [`loop.set_default_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_default_executor "asyncio.loop.set_default_executor")
, otherwise, a [`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor")
 will be lazy-initialized and used by [`run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")
 if needed.

Example:

Copy

import asyncio
import concurrent.futures

def blocking\_io():
    \# File operations (such as logging) can block the
    \# event loop: run them in a thread pool.
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)

def cpu\_bound():
    \# CPU-bound operations will block the event loop:
    \# in general it is preferable to run them in a
    \# process pool.
    return sum(i \* i for i in range(10 \*\* 7))

async def main():
    loop \= asyncio.get\_running\_loop()

    \## Options:

    \# 1. Run in the default loop's executor:
    result \= await loop.run\_in\_executor(
        None, blocking\_io)
    print('default thread pool', result)

    \# 2. Run in a custom thread pool:
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result \= await loop.run\_in\_executor(
            pool, blocking\_io)
        print('custom thread pool', result)

    \# 3. Run in a custom process pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result \= await loop.run\_in\_executor(
            pool, cpu\_bound)
        print('custom process pool', result)

    \# 4. Run in a custom interpreter pool:
    with concurrent.futures.InterpreterPoolExecutor() as pool:
        result \= await loop.run\_in\_executor(
            pool, cpu\_bound)
        print('custom interpreter pool', result)

if \_\_name\_\_ \== '\_\_main\_\_':
    asyncio.run(main())

Note that the entry point guard (`if __name__ == '__main__'`) is required for option 3 due to the peculiarities of [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
, which is used by [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor")
. See [Safe importing of main module](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-safe-main-import)
.

This method returns a [`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
 object.

Use [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 [to pass keyword arguments](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-pass-keywords)
 to _func_.

Changed in version 3.5.3: `loop.run_in_executor()` no longer configures the `max_workers` of the thread pool executor it creates, instead leaving it up to the thread pool executor ([`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor")
) to set the default.

loop.set\_default\_executor(_executor_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_default_executor "Link to this definition")

Set _executor_ as the default executor used by [`run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor")
. _executor_ must be an instance of [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor")
, which includes [`InterpreterPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor "concurrent.futures.InterpreterPoolExecutor")
.

Changed in version 3.11: _executor_ must be an instance of [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor")
.

### [Error handling API](https://docs.python.org/3/library/asyncio-eventloop.html#id15)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#error-handling-api "Link to this heading")

Allows customizing how exceptions are handled in the event loop.

loop.set\_exception\_handler(_handler_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_exception_handler "Link to this definition")

Set _handler_ as the new event loop exception handler.

If _handler_ is `None`, the default exception handler will be set. Otherwise, _handler_ must be a callable with the signature matching `(loop, context)`, where `loop` is a reference to the active event loop, and `context` is a `dict` object containing the details of the exception (see [`call_exception_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_exception_handler "asyncio.loop.call_exception_handler")
 documentation for details about context).

If the handler is called on behalf of a [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
 or [`Handle`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Handle "asyncio.Handle")
, it is run in the [`contextvars.Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
 of that task or callback handle.

Changed in version 3.12: The handler may be called in the [`Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
 of the task or handle where the exception originated.

loop.get\_exception\_handler()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.get_exception_handler "Link to this definition")

Return the current exception handler, or `None` if no custom exception handler was set.

Added in version 3.5.2.

loop.default\_exception\_handler(_context_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.default_exception_handler "Link to this definition")

Default exception handler.

This is called when an exception occurs and no exception handler is set. This can be called by a custom exception handler that wants to defer to the default handler behavior.

_context_ parameter has the same meaning as in [`call_exception_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_exception_handler "asyncio.loop.call_exception_handler")
.

loop.call\_exception\_handler(_context_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_exception_handler "Link to this definition")

Call the current event loop exception handler.

_context_ is a `dict` object containing the following keys (new keys may be introduced in future Python versions):

*   ‘message’: Error message;
    
*   ‘exception’ (optional): Exception object;
    
*   ‘future’ (optional): [`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
     instance;
    
*   ‘task’ (optional): [`asyncio.Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
     instance;
    
*   ‘handle’ (optional): [`asyncio.Handle`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Handle "asyncio.Handle")
     instance;
    
*   ‘protocol’ (optional): [Protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-protocol)
     instance;
    
*   ‘transport’ (optional): [Transport](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-transport)
     instance;
    
*   ‘socket’ (optional): [`socket.socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
     instance;
    
*   ‘source\_traceback’ (optional): Traceback of the source;
    
*   ‘handle\_traceback’ (optional): Traceback of the handle;
    
*   ‘asyncgen’ (optional): Asynchronous generator that caused the exception.
    

Note

This method should not be overloaded in subclassed event loops. For custom exception handling, use the [`set_exception_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_exception_handler "asyncio.loop.set_exception_handler")
 method.

### [Enabling debug mode](https://docs.python.org/3/library/asyncio-eventloop.html#id16)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#enabling-debug-mode "Link to this heading")

loop.get\_debug()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.get_debug "Link to this definition")

Get the debug mode ([`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
) of the event loop.

The default value is `True` if the environment variable [`PYTHONASYNCIODEBUG`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONASYNCIODEBUG)
 is set to a non-empty string, `False` otherwise.

loop.set\_debug(_enabled: [bool](https://docs.python.org/3/builtins/functions.html#bool "bool")
_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_debug "Link to this definition")

Set the debug mode of the event loop.

Changed in version 3.7: The new [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
 can now also be used to enable the debug mode.

loop.slow\_callback\_duration[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.slow_callback_duration "Link to this definition")

This attribute can be used to set the minimum execution duration in seconds that is considered “slow”. When debug mode is enabled, “slow” callbacks are logged.

Default value is 100 milliseconds.

See also

The [debug mode of asyncio](https://docs.python.org/3/library/asyncio-dev.html#asyncio-debug-mode)
.

### [Running subprocesses](https://docs.python.org/3/library/asyncio-eventloop.html#id17)
[¶](https://docs.python.org/3/library/asyncio-eventloop.html#running-subprocesses "Link to this heading")

Methods described in this subsections are low-level. In regular async/await code consider using the high-level [`asyncio.create_subprocess_shell()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_shell "asyncio.create_subprocess_shell")
 and [`asyncio.create_subprocess_exec()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "asyncio.create_subprocess_exec")
 convenience functions instead.

Note

On Windows, the default event loop [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
 supports subprocesses, whereas [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
 does not. See [Subprocess Support on Windows](https://docs.python.org/3/library/asyncio-platforms.html#asyncio-windows-subprocess)
 for details.

async loop.subprocess\_exec(_protocol\_factory_, _\*args_, _stdin\=subprocess.PIPE_, _stdout\=subprocess.PIPE_, _stderr\=subprocess.PIPE_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "Link to this definition")

Create a subprocess from one or more string arguments specified by _args_.

_args_ must be a list of strings represented by:

*   [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    ;
    
*   or [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    , encoded to the [filesystem encoding](https://docs.python.org/3/library/os.html#filesystem-encoding)
    .
    

The first string specifies the program executable, and the remaining strings specify the arguments. Together, string arguments form the `argv` of the program.

This is similar to the standard library [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
 class called with `shell=False` and the list of strings passed as the first argument; however, where `Popen` takes a single argument which is list of strings, _subprocess\_exec_ takes multiple string arguments.

The _protocol\_factory_ must be a callable returning a subclass of the [`asyncio.SubprocessProtocol`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol "asyncio.SubprocessProtocol")
 class.

Other parameters:

*   _stdin_ can be any of these:
    
    *   a file-like object
        
    *   an existing file descriptor (a positive integer), for example those created with [`os.pipe()`](https://docs.python.org/3/library/os.html#os.pipe "os.pipe")
        
    *   the [`subprocess.PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE")
         constant (default) which will create a new pipe and connect it,
        
    *   the value `None` which will make the subprocess inherit the file descriptor from this process
        
    *   the [`subprocess.DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL")
         constant which indicates that the special [`os.devnull`](https://docs.python.org/3/library/os.html#os.devnull "os.devnull")
         file will be used
        
*   _stdout_ can be any of these:
    
    *   a file-like object
        
    *   the [`subprocess.PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE")
         constant (default) which will create a new pipe and connect it,
        
    *   the value `None` which will make the subprocess inherit the file descriptor from this process
        
    *   the [`subprocess.DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL")
         constant which indicates that the special [`os.devnull`](https://docs.python.org/3/library/os.html#os.devnull "os.devnull")
         file will be used
        
*   _stderr_ can be any of these:
    
    *   a file-like object
        
    *   the [`subprocess.PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE")
         constant (default) which will create a new pipe and connect it,
        
    *   the value `None` which will make the subprocess inherit the file descriptor from this process
        
    *   the [`subprocess.DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL")
         constant which indicates that the special [`os.devnull`](https://docs.python.org/3/library/os.html#os.devnull "os.devnull")
         file will be used
        
    *   the [`subprocess.STDOUT`](https://docs.python.org/3/library/subprocess.html#subprocess.STDOUT "subprocess.STDOUT")
         constant which will connect the standard error stream to the process’ standard output stream
        
*   All other keyword arguments are passed to [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
     without interpretation, except for _bufsize_, _universal\_newlines_, _shell_, _text_, _encoding_ and _errors_, which should not be specified at all.
    
    The `asyncio` subprocess API does not support decoding the streams as text. [`bytes.decode()`](https://docs.python.org/3/builtins/stdtypes.html#bytes.decode "bytes.decode")
     can be used to convert the bytes returned from the stream to text.
    

If a file-like object passed as _stdin_, _stdout_ or _stderr_ represents a pipe, then the other side of this pipe should be registered with [`connect_write_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe")
 or [`connect_read_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe")
 for use with the event loop.

See the constructor of the [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
 class for documentation on other arguments.

Returns a pair of `(transport, protocol)`, where _transport_ conforms to the [`asyncio.SubprocessTransport`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport "asyncio.SubprocessTransport")
 base class and _protocol_ is an object instantiated by the _protocol\_factory_.

If the transport is closed or is garbage collected, the child process is killed if it is still running.

async loop.subprocess\_shell(_protocol\_factory_, _cmd_, _\*_, _stdin\=subprocess.PIPE_, _stdout\=subprocess.PIPE_, _stderr\=subprocess.PIPE_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "Link to this definition")

Create a subprocess from _cmd_, which can be a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 or a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 string encoded to the [filesystem encoding](https://docs.python.org/3/library/os.html#filesystem-encoding)
, using the platform’s “shell” syntax.

This is similar to the standard library [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
 class called with `shell=True`.

The _protocol\_factory_ must be a callable returning a subclass of the [`SubprocessProtocol`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessProtocol "asyncio.SubprocessProtocol")
 class.

See [`subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")
 for more details about the remaining arguments.

Returns a pair of `(transport, protocol)`, where _transport_ conforms to the [`SubprocessTransport`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.SubprocessTransport "asyncio.SubprocessTransport")
 base class and _protocol_ is an object instantiated by the _protocol\_factory_.

If the transport is closed or is garbage collected, the child process is killed if it is still running.

Note

It is the application’s responsibility to ensure that all whitespace and special characters are quoted appropriately to avoid [shell injection](https://en.wikipedia.org/wiki/Shell_injection#Shell_injection)
 vulnerabilities. The [`shlex.quote()`](https://docs.python.org/3/library/shlex.html#shlex.quote "shlex.quote")
 function can be used to properly escape whitespace and special characters in strings that are going to be used to construct shell commands.

Callback handles[¶](https://docs.python.org/3/library/asyncio-eventloop.html#callback-handles "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

class asyncio.Handle[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Handle "Link to this definition")

A callback wrapper object returned by [`loop.call_soon()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")
, [`loop.call_soon_threadsafe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe")
.

get\_context()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Handle.get_context "Link to this definition")

Return the [`contextvars.Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context")
 object associated with the handle.

Added in version 3.12.

cancel()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Handle.cancel "Link to this definition")

Cancel the callback. If the callback has already been canceled or executed, this method has no effect.

cancelled()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Handle.cancelled "Link to this definition")

Return `True` if the callback was cancelled.

Added in version 3.7.

class asyncio.TimerHandle[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.TimerHandle "Link to this definition")

A callback wrapper object returned by [`loop.call_later()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_later "asyncio.loop.call_later")
, and [`loop.call_at()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_at "asyncio.loop.call_at")
.

This class is a subclass of [`Handle`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Handle "asyncio.Handle")
.

when()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.TimerHandle.when "Link to this definition")

Return a scheduled callback time as [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 seconds.

The time is an absolute timestamp, using the same time reference as [`loop.time()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.time "asyncio.loop.time")
.

Added in version 3.7.

Server objects[¶](https://docs.python.org/3/library/asyncio-eventloop.html#server-objects "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Server objects are created by [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
, [`loop.create_unix_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server")
, [`start_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server")
, and [`start_unix_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_unix_server "asyncio.start_unix_server")
 functions.

Do not instantiate the [`Server`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server "asyncio.Server")
 class directly.

class asyncio.Server[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server "Link to this definition")

_Server_ objects are asynchronous context managers. When used in an `async with` statement, it’s guaranteed that the Server object is closed and not accepting new connections when the `async with` statement is completed:

Copy

srv \= await loop.create\_server(...)

async with srv:
    \# some code

\# At this point, srv is closed and no longer accepts new connections.

Changed in version 3.7: Server object is an asynchronous context manager since Python 3.7.

Changed in version 3.11: This class was exposed publicly as `asyncio.Server` in Python 3.9.11, 3.10.3 and 3.11.

close()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.close "Link to this definition")

Stop serving: close listening sockets and set the [`sockets`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.sockets "asyncio.Server.sockets")
 attribute to `None`.

The sockets that represent existing incoming client connections are left open.

The server is closed asynchronously; use the [`wait_closed()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.wait_closed "asyncio.Server.wait_closed")
 coroutine to wait until the server is closed (and no more connections are active).

close\_clients()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.close_clients "Link to this definition")

Close all existing incoming client connections.

Calls [`close()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.close "asyncio.BaseTransport.close")
 on all associated transports.

[`close()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.close "asyncio.Server.close")
 should be called before `close_clients()` when closing the server to avoid races with new clients connecting.

Added in version 3.13.

abort\_clients()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.abort_clients "Link to this definition")

Close all existing incoming client connections immediately, without waiting for pending operations to complete.

Calls [`abort()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.abort "asyncio.WriteTransport.abort")
 on all associated transports.

[`close()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.close "asyncio.Server.close")
 should be called before `abort_clients()` when closing the server to avoid races with new clients connecting.

Added in version 3.13.

get\_loop()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.get_loop "Link to this definition")

Return the event loop associated with the server object.

Added in version 3.7.

async start\_serving()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.start_serving "Link to this definition")

Start accepting connections.

This method is idempotent, so it can be called when the server is already serving.

The _start\_serving_ keyword-only parameter to [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
 and [`asyncio.start_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server")
 allows creating a Server object that is not accepting connections initially. In this case `Server.start_serving()`, or [`Server.serve_forever()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.serve_forever "asyncio.Server.serve_forever")
 can be used to make the Server start accepting connections.

Added in version 3.7.

async serve\_forever()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.serve_forever "Link to this definition")

Start accepting connections until the coroutine is cancelled. Cancellation of `serve_forever` task causes the server to be closed.

This method can be called if the server is already accepting connections. Only one `serve_forever` task can exist per one _Server_ object.

Example:

Copy

async def client\_connected(reader, writer):
    \# Communicate with the client with
    \# reader/writer streams.  For example:
    await reader.readline()

async def main(host, port):
    srv \= await asyncio.start\_server(
        client\_connected, host, port)
    await srv.serve\_forever()

asyncio.run(main('127.0.0.1', 0))

Added in version 3.7.

is\_serving()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.is_serving "Link to this definition")

Return `True` if the server is accepting new connections.

Added in version 3.7.

async wait\_closed()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.wait_closed "Link to this definition")

Wait until the [`close()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.close "asyncio.Server.close")
 method completes and all active connections have finished.

Changed in version 3.12: `wait_closed()` now waits until the server is closed and all active connections have finished. Previously, it returned immediately if the server was already closed, even if connections were still active.

sockets[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.sockets "Link to this definition")

List of socket-like objects, `asyncio.trsock.TransportSocket`, which the server is listening on.

Changed in version 3.7: Prior to Python 3.7 `Server.sockets` used to return an internal list of server sockets directly. In 3.7 a copy of that list is returned.

Event loop implementations[¶](https://docs.python.org/3/library/asyncio-eventloop.html#event-loop-implementations "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

asyncio ships with two different event loop implementations: [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
 and [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
.

By default asyncio is configured to use [`EventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.EventLoop "asyncio.EventLoop")
.

class asyncio.SelectorEventLoop[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "Link to this definition")

A subclass of [`AbstractEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop "asyncio.AbstractEventLoop")
 based on the [`selectors`](https://docs.python.org/3/library/selectors.html#module-selectors "selectors: High-level I/O multiplexing.")
 module.

Uses the most efficient _selector_ available for the given platform. It is also possible to manually configure the exact selector implementation to be used:

Copy

import asyncio
import selectors

async def main():
   ...

loop\_factory \= lambda: asyncio.SelectorEventLoop(selectors.SelectSelector())
asyncio.run(main(), loop\_factory\=loop\_factory)

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, Windows.

class asyncio.ProactorEventLoop[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "Link to this definition")

A subclass of [`AbstractEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop "asyncio.AbstractEventLoop")
 for Windows that uses “I/O Completion Ports” (IOCP).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

See also

[MSDN documentation on I/O Completion Ports](https://learn.microsoft.com/windows/win32/fileio/i-o-completion-ports)
.

class asyncio.EventLoop[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.EventLoop "Link to this definition")

> An alias to the most efficient available subclass of [`AbstractEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop "asyncio.AbstractEventLoop")
>  for the given platform.
> 
> It is an alias to [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
>  on Unix and [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
>  on Windows.

Added in version 3.13.

class asyncio.AbstractEventLoop[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop "Link to this definition")

Abstract base class for asyncio-compliant event loops.

The [Event loop methods](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop-methods)
 section lists all methods that an alternative implementation of `AbstractEventLoop` should have defined.

class asyncio.BaseEventLoop[¶](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.BaseEventLoop "Link to this definition")

A base class that partially implements [`AbstractEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop "asyncio.AbstractEventLoop")
 to simplify writing custom event loops.

It provides default implementations of many [`AbstractEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop "asyncio.AbstractEventLoop")
 methods, so subclasses have fewer methods to implement themselves. In return, a subclass is expected to implement a number of internal, protected methods. See [Writing a custom event loop](https://docs.python.org/3/library/asyncio-extending.html#writing-custom-event-loop)
 for more information.

Examples[¶](https://docs.python.org/3/library/asyncio-eventloop.html#examples "Link to this heading")

------------------------------------------------------------------------------------------------------

Note that all examples in this section **purposefully** show how to use the low-level event loop APIs, such as [`loop.run_forever()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_forever "asyncio.loop.run_forever")
 and [`loop.call_soon()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")
. Modern asyncio applications rarely need to be written this way; consider using the high-level functions like [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
.

### Hello World with call\_soon()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#hello-world-with-call-soon "Link to this heading")

An example using the [`loop.call_soon()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon")
 method to schedule a callback. The callback displays `"Hello World"` and then stops the event loop:

Copy

import asyncio

def hello\_world(loop):
    """A callback to print 'Hello World' and stop the event loop"""
    print('Hello World')
    loop.stop()

loop \= asyncio.new\_event\_loop()

\# Schedule a call to hello\_world()
loop.call\_soon(hello\_world, loop)

\# Blocking call interrupted by loop.stop()
try:
    loop.run\_forever()
finally:
    loop.close()

See also

A similar [Hello World](https://docs.python.org/3/library/asyncio-task.html#coroutine)
 example created with a coroutine and the [`run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
 function.

### Display the current date with call\_later()[¶](https://docs.python.org/3/library/asyncio-eventloop.html#display-the-current-date-with-call-later "Link to this heading")

An example of a callback displaying the current date every second. The callback uses the [`loop.call_later()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_later "asyncio.loop.call_later")
 method to reschedule itself after 1 second, and eventually stops the event loop:

Copy

import asyncio
import datetime as dt

def display\_date(end\_time, loop):
    print(dt.datetime.now())
    if (loop.time() + 1.0) < end\_time:
        loop.call\_later(1, display\_date, end\_time, loop)
    else:
        loop.stop()

loop \= asyncio.new\_event\_loop()

\# Schedule the first call to display\_date()
end\_time \= loop.time() + 5.0
loop.call\_soon(display\_date, end\_time, loop)

\# Blocking call interrupted by loop.stop()
try:
    loop.run\_forever()
finally:
    loop.close()

See also

A similar [current date](https://docs.python.org/3/library/asyncio-task.html#asyncio-example-sleep)
 example created with a coroutine and the [`run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
 function.

### Watch a file descriptor for read events[¶](https://docs.python.org/3/library/asyncio-eventloop.html#watch-a-file-descriptor-for-read-events "Link to this heading")

Wait until a file descriptor received some data using the [`loop.add_reader()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_reader "asyncio.loop.add_reader")
 method and then close the event loop:

Copy

import asyncio
from socket import socketpair

\# Create a pair of connected file descriptors
rsock, wsock \= socketpair()

loop \= asyncio.new\_event\_loop()

def reader():
    data \= rsock.recv(100)
    print("Received:", data.decode())

    \# We are done: unregister the file descriptor
    loop.remove\_reader(rsock)

    \# Stop the event loop
    loop.stop()

\# Register the file descriptor for read event
loop.add\_reader(rsock, reader)

\# Simulate the reception of data from the network
loop.call\_soon(wsock.send, 'abc'.encode())

try:
    \# Run the event loop
    loop.run\_forever()
finally:
    \# We are done. Close sockets and the event loop.
    rsock.close()
    wsock.close()
    loop.close()

See also

*   A similar [example](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-example-create-connection)
     using transports, protocols, and the [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
     method.
    
*   Another similar [example](https://docs.python.org/3/library/asyncio-stream.html#asyncio-example-create-connection-streams)
     using the high-level [`asyncio.open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection")
     function and streams.
    

### Set signal handlers for SIGINT and SIGTERM[¶](https://docs.python.org/3/library/asyncio-eventloop.html#set-signal-handlers-for-sigint-and-sigterm "Link to this heading")

(This `signal` example only works on Unix.)

Register handlers for signals [`SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT")
 and [`SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "signal.SIGTERM")
 using the [`loop.add_signal_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler "asyncio.loop.add_signal_handler")
 method:

Copy

import asyncio
import functools
import os
import signal

def ask\_exit(signame, loop):
    print("got signal %s: exit" % signame)
    loop.stop()

async def main():
    loop \= asyncio.get\_running\_loop()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add\_signal\_handler(
            getattr(signal, signame),
            functools.partial(ask\_exit, signame, loop))

    await asyncio.sleep(3600)

print("Event loop running for 1 hour, press Ctrl+C to interrupt.")
print(f"pid {os.getpid()}: send SIGINT or SIGTERM to exit.")

asyncio.run(main())

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Event loop](https://docs.python.org/3/library/asyncio-eventloop.html#)
    *   [Event loop methods](https://docs.python.org/3/library/asyncio-eventloop.html#event-loop-methods)
        *   [Running and stopping the loop](https://docs.python.org/3/library/asyncio-eventloop.html#running-and-stopping-the-loop)
            
        *   [Scheduling callbacks](https://docs.python.org/3/library/asyncio-eventloop.html#scheduling-callbacks)
            
        *   [Scheduling delayed callbacks](https://docs.python.org/3/library/asyncio-eventloop.html#scheduling-delayed-callbacks)
            
        *   [Creating futures and tasks](https://docs.python.org/3/library/asyncio-eventloop.html#creating-futures-and-tasks)
            
        *   [Opening network connections](https://docs.python.org/3/library/asyncio-eventloop.html#opening-network-connections)
            
        *   [Creating network servers](https://docs.python.org/3/library/asyncio-eventloop.html#creating-network-servers)
            
        *   [Transferring files](https://docs.python.org/3/library/asyncio-eventloop.html#transferring-files)
            
        *   [TLS upgrade](https://docs.python.org/3/library/asyncio-eventloop.html#tls-upgrade)
            
        *   [Watching file descriptors](https://docs.python.org/3/library/asyncio-eventloop.html#watching-file-descriptors)
            
        *   [Working with socket objects directly](https://docs.python.org/3/library/asyncio-eventloop.html#working-with-socket-objects-directly)
            
        *   [DNS](https://docs.python.org/3/library/asyncio-eventloop.html#dns)
            
        *   [Working with pipes](https://docs.python.org/3/library/asyncio-eventloop.html#working-with-pipes)
            
        *   [Unix signals](https://docs.python.org/3/library/asyncio-eventloop.html#unix-signals)
            
        *   [Executing code in thread or process pools](https://docs.python.org/3/library/asyncio-eventloop.html#executing-code-in-thread-or-process-pools)
            
        *   [Error handling API](https://docs.python.org/3/library/asyncio-eventloop.html#error-handling-api)
            
        *   [Enabling debug mode](https://docs.python.org/3/library/asyncio-eventloop.html#enabling-debug-mode)
            
        *   [Running subprocesses](https://docs.python.org/3/library/asyncio-eventloop.html#running-subprocesses)
            
    *   [Callback handles](https://docs.python.org/3/library/asyncio-eventloop.html#callback-handles)
        
    *   [Server objects](https://docs.python.org/3/library/asyncio-eventloop.html#server-objects)
        
    *   [Event loop implementations](https://docs.python.org/3/library/asyncio-eventloop.html#event-loop-implementations)
        
    *   [Examples](https://docs.python.org/3/library/asyncio-eventloop.html#examples)
        *   [Hello World with call\_soon()](https://docs.python.org/3/library/asyncio-eventloop.html#hello-world-with-call-soon)
            
        *   [Display the current date with call\_later()](https://docs.python.org/3/library/asyncio-eventloop.html#display-the-current-date-with-call-later)
            
        *   [Watch a file descriptor for read events](https://docs.python.org/3/library/asyncio-eventloop.html#watch-a-file-descriptor-for-read-events)
            
        *   [Set signal handlers for SIGINT and SIGTERM](https://docs.python.org/3/library/asyncio-eventloop.html#set-signal-handlers-for-sigint-and-sigterm)
            

#### Previous topic

[Command-line introspection tools](https://docs.python.org/3/library/asyncio-tools.html "previous chapter")

#### Next topic

[Futures](https://docs.python.org/3/library/asyncio-future.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Event+loop&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-eventloop.html&pagesource=library%2Fasyncio-eventloop.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-eventloop.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-future.html "Futures")
     |
*   [previous](https://docs.python.org/3/library/asyncio-tools.html "Command-line introspection tools")
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
*   [Event loop](https://docs.python.org/3/library/asyncio-eventloop.html)
    
*    
    
    |
*   Theme Auto Light Dark |