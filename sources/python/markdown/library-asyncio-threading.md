### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/socket.html "socket — Low-level networking interface")
     |
*   [previous](https://docs.python.org/3/library/asyncio-dev.html "Developing with asyncio")
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
*   [asyncio and free-threaded Python](https://docs.python.org/3/library/asyncio-threading.html)
    
*    
    
    |
*   Theme Auto Light Dark |

asyncio and free-threaded Python[¶](https://docs.python.org/3/library/asyncio-threading.html#asyncio-and-free-threaded-python "Link to this heading")

======================================================================================================================================================

asyncio uses an event loop as a scheduler to enable highly efficient concurrency by switching between tasks to allow non-blocking I/O operations. This results in better performance for I/O-bound use cases. It also allows off-loading CPU-bound work to a thread or process pool, but that is still limited by the [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
 in CPython.

However, in [free-threaded Python](https://docs.python.org/3/howto/free-threading-python.html#freethreading-python-howto)
, the GIL is disabled and Python can run true multi-threaded code. This means that asyncio can now take advantage of multiple CPU cores without the limitations imposed by the GIL.

Since Python 3.14, asyncio has first-class support for free-threaded Python, and the implementation of asyncio is safe to use in a multi-threaded environment.

A single event loop on one core can handle many connections concurrently, but the Python code that runs to handle each one still executes serially. Once requests involve a non-trivial amount of per-request computation, that handling becomes the bottleneck, and a single core can no longer keep up. Combining asyncio with threads is most useful here: by running an event loop per thread, the handling of different requests can run in parallel across multiple CPU cores. It is also useful when you need to run blocking or CPU-bound code from an asyncio application.

See also

[Scaling asyncio on Free-Threaded Python](https://labs.quansight.org/blog/scaling-asyncio-on-free-threaded-python)
, a blog post by Kumar Aditya which explains the internal changes that make asyncio safe and efficient under free-threaded Python, together with benchmarks of the resulting improvements.

Thread safety considerations[¶](https://docs.python.org/3/library/asyncio-threading.html#thread-safety-considerations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

While asyncio is designed to be thread-safe in a free-threaded Python environment, there are still some considerations to keep in mind when using asyncio with threads:

1.  **Event loop**: Each thread should have its own event loop which should not be shared across threads. This ensures that the event loop can manage its own tasks and callbacks without interference from other threads.
    
2.  **Task management**: Tasks and futures created in one thread should not be awaited or manipulated from another thread.
    
3.  **Thread-safe APIs**: When interacting with asyncio from multiple threads, it’s important to use thread-safe APIs provided by asyncio, such as [`asyncio.run_coroutine_threadsafe()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe "asyncio.run_coroutine_threadsafe")
     for submitting coroutines to an event loop from another thread. If you need to call a callback from a different thread, you can use [`loop.call_soon_threadsafe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon_threadsafe "asyncio.loop.call_soon_threadsafe")
     to schedule it safely.
    
4.  **Synchronization**: The synchronization primitives provided by asyncio (like [`asyncio.Lock`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock "asyncio.Lock")
     and [`asyncio.Event`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event "asyncio.Event")
    ) are not designed to be used across threads. If you need to synchronize between threads, you should use the synchronization primitives from the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
     module instead.
    

Using asyncio with threads[¶](https://docs.python.org/3/library/asyncio-threading.html#using-asyncio-with-threads "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

asyncio supports running one event loop per thread, which allows you to take advantage of multiple CPU cores in a free-threaded Python environment. Each thread can run its own event loop, and tasks can be scheduled on those loops independently.

Here’s an example of how to use asyncio with threads:

Copy

import asyncio
import threading

async def worker(name: str) \-> None:
    print(f"Worker {name} starting")
    await asyncio.sleep(1)
    print(f"Worker {name} done")

def run\_loop(name: str) \-> None:
    asyncio.run(worker(name))

threads \= \[\
    threading.Thread(target\=run\_loop, args\=(f"T{i}",))\
    for i in range(4)\
\]
for t in threads:
    t.start()
for t in threads:
    t.join()

In this example, each thread creates its own event loop with [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")
 and runs a coroutine on it. The threads execute concurrently, and in a free-threaded build they can run on separate CPU cores in parallel.

Producer/consumer across threads[¶](https://docs.python.org/3/library/asyncio-threading.html#producer-consumer-across-threads "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

When a regular (non-asyncio) thread needs to hand work to an asyncio event loop running in another thread, use a thread-safe primitive such as [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue")
 rather than [`asyncio.Queue`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue "asyncio.Queue")
, which is only safe within a single event loop.:

Copy

import asyncio
import queue
import threading

def producer(q: queue.Queue\[int\]) \-> None:
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
    q.shutdown()

async def consumer(q: queue.Queue\[int\]) \-> None:
    while True:
        try:
            item \= q.get\_nowait()
        except queue.Empty:
            await asyncio.sleep(0.1)
            continue
        except queue.ShutDown:
            break
        print(f"Consumed {item}")
        await asyncio.sleep(item)

q: queue.Queue\[int\] \= queue.Queue()
consumer\_thread \= threading.Thread(
    target\=lambda: asyncio.run(consumer(q))
)
consumer\_thread.start()
producer(q)
consumer\_thread.join()

The producer runs on the main thread while the consumer runs inside an event loop on its own thread, yet they communicate safely through `queue.Queue`. When the queue is empty the consumer sleeps briefly and tries again. When the producer is done it calls [`shutdown()`](https://docs.python.org/3/library/queue.html#queue.Queue.shutdown "queue.Queue.shutdown")
, which causes subsequent [`get_nowait()`](https://docs.python.org/3/library/queue.html#queue.Queue.get_nowait "queue.Queue.get_nowait")
 calls to raise [`queue.ShutDown`](https://docs.python.org/3/library/queue.html#queue.ShutDown "queue.ShutDown")
 so the consumer can exit cleanly.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [asyncio and free-threaded Python](https://docs.python.org/3/library/asyncio-threading.html#)
    *   [Thread safety considerations](https://docs.python.org/3/library/asyncio-threading.html#thread-safety-considerations)
        
    *   [Using asyncio with threads](https://docs.python.org/3/library/asyncio-threading.html#using-asyncio-with-threads)
        
    *   [Producer/consumer across threads](https://docs.python.org/3/library/asyncio-threading.html#producer-consumer-across-threads)
        

#### Previous topic

[Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html "previous chapter")

#### Next topic

[`socket` — Low-level networking interface](https://docs.python.org/3/library/socket.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=asyncio+and+free-threaded+Python&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-threading.html&pagesource=library%2Fasyncio-threading.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-threading.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/socket.html "socket — Low-level networking interface")
     |
*   [previous](https://docs.python.org/3/library/asyncio-dev.html "Developing with asyncio")
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
*   [asyncio and free-threaded Python](https://docs.python.org/3/library/asyncio-threading.html)
    
*    
    
    |
*   Theme Auto Light Dark |