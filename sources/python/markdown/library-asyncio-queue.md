### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-exceptions.html "Exceptions")
     |
*   [previous](https://docs.python.org/3/library/asyncio-subprocess.html "Subprocesses")
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
*   [Queues](https://docs.python.org/3/library/asyncio-queue.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Queues[¶](https://docs.python.org/3/library/asyncio-queue.html#queues "Link to this heading")

==============================================================================================

**Source code:** [Lib/asyncio/queues.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/queues.py)

* * *

asyncio queues are designed to be similar to classes of the [`queue`](https://docs.python.org/3/library/queue.html#module-queue "queue: A synchronized queue class.")
 module. Although asyncio queues are not thread-safe, they are designed to be used specifically in async/await code.

Note that methods of asyncio queues don’t have a _timeout_ parameter; use [`asyncio.wait_for()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for "asyncio.wait_for")
 function to do queue operations with a timeout.

See also the [Examples](https://docs.python.org/3/library/asyncio-queue.html#examples)
 section below.

Queue[¶](https://docs.python.org/3/library/asyncio-queue.html#queue "Link to this heading")

--------------------------------------------------------------------------------------------

class asyncio.Queue(_maxsize\=0_)[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue "Link to this definition")

A first in, first out (FIFO) queue.

If _maxsize_ is less than or equal to zero, the queue size is infinite. If it is an integer greater than `0`, then `await put()` blocks when the queue reaches _maxsize_ until an item is removed by [`get()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.get "asyncio.Queue.get")
.

Unlike the standard library threading [`queue`](https://docs.python.org/3/library/queue.html#module-queue "queue: A synchronized queue class.")
, the size of the queue is always known and can be returned by calling the [`qsize()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.qsize "asyncio.Queue.qsize")
 method.

Changed in version 3.10: Removed the _loop_ parameter.

This class is [not thread safe](https://docs.python.org/3/library/asyncio-dev.html#asyncio-multithreading)
.

maxsize[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.maxsize "Link to this definition")

Number of items allowed in the queue.

empty()[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.empty "Link to this definition")

Return `True` if the queue is empty, `False` otherwise.

full()[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.full "Link to this definition")

Return `True` if there are [`maxsize`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.maxsize "asyncio.Queue.maxsize")
 items in the queue.

If the queue was initialized with `maxsize=0` (the default), then `full()` never returns `True`.

async get()[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.get "Link to this definition")

Remove and return an item from the queue. If queue is empty, wait until an item is available.

Raises [`QueueShutDown`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueShutDown "asyncio.QueueShutDown")
 if the queue has been shut down and is empty, or if the queue has been shut down immediately.

get\_nowait()[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.get_nowait "Link to this definition")

Return an item if one is immediately available, else raise [`QueueEmpty`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueEmpty "asyncio.QueueEmpty")
.

Raises [`QueueShutDown`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueShutDown "asyncio.QueueShutDown")
 if the queue has been shut down and is empty.

async join()[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.join "Link to this definition")

Block until all items in the queue have been received and processed.

The count of unfinished tasks goes up whenever an item is added to the queue. The count goes down whenever a consumer coroutine calls [`task_done()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.task_done "asyncio.Queue.task_done")
 to indicate that the item was retrieved and all work on it is complete. When the count of unfinished tasks drops to zero, `join()` unblocks.

async put(_item_)[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.put "Link to this definition")

Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.

Raises [`QueueShutDown`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueShutDown "asyncio.QueueShutDown")
 if the queue has been shut down.

put\_nowait(_item_)[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.put_nowait "Link to this definition")

Put an item into the queue without blocking.

If no free slot is immediately available, raise [`QueueFull`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueFull "asyncio.QueueFull")
.

Raises [`QueueShutDown`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueShutDown "asyncio.QueueShutDown")
 if the queue has been shut down.

qsize()[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.qsize "Link to this definition")

Return the number of items in the queue.

shutdown(_immediate\=False_)[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.shutdown "Link to this definition")

Put a `Queue` instance into a shutdown mode.

The queue can no longer grow. Future calls to [`put()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.put "asyncio.Queue.put")
 raise [`QueueShutDown`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueShutDown "asyncio.QueueShutDown")
. Currently blocked callers of `put()` will be unblocked and will raise `QueueShutDown` in the formerly awaiting task.

If _immediate_ is false (the default), the queue can be wound down normally with [`get()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.get "asyncio.Queue.get")
 calls to extract tasks that have already been loaded.

And if [`task_done()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.task_done "asyncio.Queue.task_done")
 is called for each remaining task, a pending [`join()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.join "asyncio.Queue.join")
 will be unblocked normally.

Once the queue is empty, future calls to [`get()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.get "asyncio.Queue.get")
 will raise [`QueueShutDown`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueShutDown "asyncio.QueueShutDown")
.

If _immediate_ is true, the queue is terminated immediately. The queue is drained to be completely empty and the count of unfinished tasks is reduced by the number of tasks drained. If unfinished tasks is zero, callers of [`join()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.join "asyncio.Queue.join")
 are unblocked. Also, blocked callers of [`get()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.get "asyncio.Queue.get")
 are unblocked and will raise [`QueueShutDown`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueShutDown "asyncio.QueueShutDown")
 because the queue is empty.

Use caution when using [`join()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.join "asyncio.Queue.join")
 with _immediate_ set to true. This unblocks the join even when no work has been done on the tasks, violating the usual invariant for joining a queue.

Added in version 3.13.

task\_done()[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.task_done "Link to this definition")

Indicate that a formerly enqueued work item is complete.

Used by queue consumers. For each [`get()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.get "asyncio.Queue.get")
 used to fetch a work item, a subsequent call to `task_done()` tells the queue that the processing on the work item is complete.

If a [`join()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.join "asyncio.Queue.join")
 is currently blocking, it will resume when all items have been processed (meaning that a `task_done()` call was received for every item that had been [`put()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.put "asyncio.Queue.put")
 into the queue).

Raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if called more times than there were items placed in the queue.

Priority Queue[¶](https://docs.python.org/3/library/asyncio-queue.html#priority-queue "Link to this heading")

--------------------------------------------------------------------------------------------------------------

class asyncio.PriorityQueue[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.PriorityQueue "Link to this definition")

A variant of [`Queue`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue "asyncio.Queue")
; retrieves entries in priority order (lowest first).

Entries are typically tuples of the form `(priority_number, data)`.

LIFO Queue[¶](https://docs.python.org/3/library/asyncio-queue.html#lifo-queue "Link to this heading")

------------------------------------------------------------------------------------------------------

class asyncio.LifoQueue[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.LifoQueue "Link to this definition")

A variant of [`Queue`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue "asyncio.Queue")
 that retrieves most recently added entries first (last in, first out).

Exceptions[¶](https://docs.python.org/3/library/asyncio-queue.html#exceptions "Link to this heading")

------------------------------------------------------------------------------------------------------

exception asyncio.QueueEmpty[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueEmpty "Link to this definition")

This exception is raised when the [`get_nowait()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.get_nowait "asyncio.Queue.get_nowait")
 method is called on an empty queue.

exception asyncio.QueueFull[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueFull "Link to this definition")

Exception raised when the [`put_nowait()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.put_nowait "asyncio.Queue.put_nowait")
 method is called on a queue that has reached its _maxsize_.

exception asyncio.QueueShutDown[¶](https://docs.python.org/3/library/asyncio-queue.html#asyncio.QueueShutDown "Link to this definition")

Exception raised when [`put()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.put "asyncio.Queue.put")
, [`put_nowait()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.put_nowait "asyncio.Queue.put_nowait")
, [`get()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.get "asyncio.Queue.get")
 or [`get_nowait()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.get_nowait "asyncio.Queue.get_nowait")
 is called on a queue which has been shut down.

Added in version 3.13.

Examples[¶](https://docs.python.org/3/library/asyncio-queue.html#examples "Link to this heading")

--------------------------------------------------------------------------------------------------

Queues can be used to distribute workload between several concurrent tasks:

Copy

import asyncio
import random
import time

async def worker(name, queue):
    while True:
        \# Get a "work item" out of the queue.
        sleep\_for \= await queue.get()

        \# Sleep for the "sleep\_for" seconds.
        await asyncio.sleep(sleep\_for)

        \# Notify the queue that the "work item" has been processed.
        queue.task\_done()

        print(f'{name} has slept for {sleep\_for:.2f} seconds')

async def main():
    \# Create a queue that we will use to store our "workload".
    queue \= asyncio.Queue()

    \# Generate random timings and put them into the queue.
    total\_sleep\_time \= 0
    for \_ in range(20):
        sleep\_for \= random.uniform(0.05, 1.0)
        total\_sleep\_time += sleep\_for
        queue.put\_nowait(sleep\_for)

    \# Create three worker tasks to process the queue concurrently.
    tasks \= \[\]
    for i in range(3):
        task \= asyncio.create\_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    \# Wait until the queue is fully processed.
    started\_at \= time.monotonic()
    await queue.join()
    total\_slept\_for \= time.monotonic() \- started\_at

    \# Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    \# Wait until all worker tasks are cancelled.
    await asyncio.gather(\*tasks, return\_exceptions\=True)

    print('====')
    print(f'3 workers slept in parallel for {total\_slept\_for:.2f} seconds')
    print(f'total expected sleep time: {total\_sleep\_time:.2f} seconds')

asyncio.run(main())

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Queues](https://docs.python.org/3/library/asyncio-queue.html#)
    *   [Queue](https://docs.python.org/3/library/asyncio-queue.html#queue)
        
    *   [Priority Queue](https://docs.python.org/3/library/asyncio-queue.html#priority-queue)
        
    *   [LIFO Queue](https://docs.python.org/3/library/asyncio-queue.html#lifo-queue)
        
    *   [Exceptions](https://docs.python.org/3/library/asyncio-queue.html#exceptions)
        
    *   [Examples](https://docs.python.org/3/library/asyncio-queue.html#examples)
        

#### Previous topic

[Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html "previous chapter")

#### Next topic

[Exceptions](https://docs.python.org/3/library/asyncio-exceptions.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Queues&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-queue.html&pagesource=library%2Fasyncio-queue.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-queue.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-exceptions.html "Exceptions")
     |
*   [previous](https://docs.python.org/3/library/asyncio-subprocess.html "Subprocesses")
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
*   [Queues](https://docs.python.org/3/library/asyncio-queue.html)
    
*    
    
    |
*   Theme Auto Light Dark |