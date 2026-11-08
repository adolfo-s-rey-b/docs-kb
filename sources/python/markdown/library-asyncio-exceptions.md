### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-graph.html "Call graph introspection")
     |
*   [previous](https://docs.python.org/3/library/asyncio-queue.html "Queues")
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
*   [Exceptions](https://docs.python.org/3/library/asyncio-exceptions.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Exceptions[¶](https://docs.python.org/3/library/asyncio-exceptions.html#exceptions "Link to this heading")

===========================================================================================================

**Source code:** [Lib/asyncio/exceptions.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/exceptions.py)

* * *

exception asyncio.TimeoutError[¶](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.TimeoutError "Link to this definition")

A deprecated alias of `TimeoutError`, raised when the operation has exceeded the given deadline.

Changed in version 3.11: This class was made an alias of `TimeoutError`.

exception asyncio.CancelledError[¶](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "Link to this definition")

The operation has been cancelled.

This exception can be caught to perform custom operations when asyncio Tasks are cancelled. In almost all situations the exception must be re-raised.

Changed in version 3.8: `CancelledError` is now a subclass of [`BaseException`](https://docs.python.org/3/builtins/exceptions.html#BaseException "BaseException")
 rather than [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
.

exception asyncio.InvalidStateError[¶](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.InvalidStateError "Link to this definition")

Invalid internal state of [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
 or [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future")
.

Can be raised in situations like setting a result value for a _Future_ object that already has a result value set.

exception asyncio.SendfileNotAvailableError[¶](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.SendfileNotAvailableError "Link to this definition")

The “sendfile” syscall is not available for the given socket or file type.

A subclass of [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
.

exception asyncio.IncompleteReadError[¶](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.IncompleteReadError "Link to this definition")

The requested read operation did not complete fully.

Raised by the [asyncio stream APIs](https://docs.python.org/3/library/asyncio-stream.html#asyncio-streams)
.

This exception is a subclass of [`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
.

expected[¶](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.IncompleteReadError.expected "Link to this definition")

The total number ([`int`](https://docs.python.org/3/builtins/functions.html#int "int")
) of expected bytes.

partial[¶](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.IncompleteReadError.partial "Link to this definition")

A string of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 read before the end of stream was reached.

exception asyncio.LimitOverrunError[¶](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.LimitOverrunError "Link to this definition")

Reached the buffer size limit while looking for a separator.

Raised by the [asyncio stream APIs](https://docs.python.org/3/library/asyncio-stream.html#asyncio-streams)
.

consumed[¶](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.LimitOverrunError.consumed "Link to this definition")

The total number of to be consumed bytes.

#### Previous topic

[Queues](https://docs.python.org/3/library/asyncio-queue.html "previous chapter")

#### Next topic

[Call graph introspection](https://docs.python.org/3/library/asyncio-graph.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Exceptions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-exceptions.html&pagesource=library%2Fasyncio-exceptions.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-exceptions.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-graph.html "Call graph introspection")
     |
*   [previous](https://docs.python.org/3/library/asyncio-queue.html "Queues")
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
*   [Exceptions](https://docs.python.org/3/library/asyncio-exceptions.html)
    
*    
    
    |
*   Theme Auto Light Dark |