### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-subprocess.html "Subprocesses")
     |
*   [previous](https://docs.python.org/3/library/asyncio-stream.html "Streams")
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
*   [Synchronization Primitives](https://docs.python.org/3/library/asyncio-sync.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Synchronization Primitives[¶](https://docs.python.org/3/library/asyncio-sync.html#synchronization-primitives "Link to this heading")

=====================================================================================================================================

**Source code:** [Lib/asyncio/locks.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/locks.py)

* * *

asyncio synchronization primitives are designed to be similar to those of the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
 module with two important caveats:

*   asyncio primitives are not thread-safe, therefore they should not be used for OS thread synchronization (use [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
     for that);
    
*   methods of these synchronization primitives do not accept the _timeout_ argument; use the [`asyncio.wait_for()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for "asyncio.wait_for")
     function to perform operations with timeouts.
    

asyncio has the following basic synchronization primitives:

*   [`Lock`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock "asyncio.Lock")
    
*   [`Event`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event "asyncio.Event")
    
*   [`Condition`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition "asyncio.Condition")
    
*   [`Semaphore`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore "asyncio.Semaphore")
    
*   [`BoundedSemaphore`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.BoundedSemaphore "asyncio.BoundedSemaphore")
    
*   [`Barrier`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier "asyncio.Barrier")
    

* * *

Lock[¶](https://docs.python.org/3/library/asyncio-sync.html#lock "Link to this heading")

-----------------------------------------------------------------------------------------

class asyncio.Lock[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock "Link to this definition")

Implements a mutex lock for asyncio tasks. Not thread-safe.

An asyncio lock can be used to guarantee exclusive access to a shared resource.

The preferred way to use a Lock is an [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
 statement:

Copy

lock \= asyncio.Lock()

\# ... later
async with lock:
    \# access shared state

which is equivalent to:

Copy

lock \= asyncio.Lock()

\# ... later
await lock.acquire()
try:
    \# access shared state
finally:
    lock.release()

Changed in version 3.10: Removed the _loop_ parameter.

async acquire()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock.acquire "Link to this definition")

Acquire the lock.

This method waits until the lock is _unlocked_, sets it to _locked_ and returns `True`.

When more than one coroutine is blocked in `acquire()` waiting for the lock to be unlocked, only one coroutine eventually proceeds.

Acquiring a lock is _fair_: the coroutine that proceeds will be the first coroutine that started waiting on the lock.

release()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock.release "Link to this definition")

Release the lock.

When the lock is _locked_, reset it to _unlocked_ and return.

If the lock is _unlocked_, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 is raised.

locked()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock.locked "Link to this definition")

Return `True` if the lock is _locked_.

Event[¶](https://docs.python.org/3/library/asyncio-sync.html#event "Link to this heading")

-------------------------------------------------------------------------------------------

class asyncio.Event[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event "Link to this definition")

An event object. Not thread-safe.

An asyncio event can be used to notify multiple asyncio tasks that some event has happened.

An Event object manages an internal flag that can be set to _true_ with the [`set()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event.set "asyncio.Event.set")
 method and reset to _false_ with the [`clear()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event.clear "asyncio.Event.clear")
 method. The [`wait()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event.wait "asyncio.Event.wait")
 method blocks until the flag is set to _true_. The flag is set to _false_ initially.

Changed in version 3.10: Removed the _loop_ parameter.

Example:

Copy

async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... got it!')

async def main():
    \# Create an Event object.
    event \= asyncio.Event()

    \# Spawn a Task to wait until 'event' is set.
    waiter\_task \= asyncio.create\_task(waiter(event))

    \# Sleep for 1 second and set the event.
    await asyncio.sleep(1)
    event.set()

    \# Wait until the waiter task is finished.
    await waiter\_task

asyncio.run(main())

async wait()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event.wait "Link to this definition")

Wait until the event is set.

If the event is set, return `True` immediately. Otherwise block until another task calls [`set()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event.set "asyncio.Event.set")
.

set()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event.set "Link to this definition")

Set the event.

All tasks waiting for event to be set will be immediately awakened.

clear()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event.clear "Link to this definition")

Clear (unset) the event.

Subsequent tasks awaiting on [`wait()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event.wait "asyncio.Event.wait")
 will now block until the [`set()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event.set "asyncio.Event.set")
 method is called again.

is\_set()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event.is_set "Link to this definition")

Return `True` if the event is set.

Condition[¶](https://docs.python.org/3/library/asyncio-sync.html#condition "Link to this heading")

---------------------------------------------------------------------------------------------------

class asyncio.Condition(_lock\=None_)[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition "Link to this definition")

A Condition object. Not thread-safe.

An asyncio condition primitive can be used by a task to wait for some event to happen and then get exclusive access to a shared resource.

In essence, a Condition object combines the functionality of an [`Event`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event "asyncio.Event")
 and a [`Lock`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock "asyncio.Lock")
. It is possible to have multiple Condition objects share one Lock, which allows coordinating exclusive access to a shared resource between different tasks interested in particular states of that shared resource.

The optional _lock_ argument must be a [`Lock`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock "asyncio.Lock")
 object or `None`. In the latter case a new Lock object is created automatically.

Changed in version 3.10: Removed the _loop_ parameter.

The preferred way to use a Condition is an [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
 statement:

Copy

cond \= asyncio.Condition()

\# ... later
async with cond:
    await cond.wait()

which is equivalent to:

Copy

cond \= asyncio.Condition()

\# ... later
await cond.acquire()
try:
    await cond.wait()
finally:
    cond.release()

async acquire()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.acquire "Link to this definition")

Acquire the underlying lock.

This method waits until the underlying lock is _unlocked_, sets it to _locked_ and returns `True`.

notify(_n\=1_)[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.notify "Link to this definition")

Wake up _n_ tasks (1 by default) waiting on this condition. If fewer than _n_ tasks are waiting they are all awakened.

The lock must be acquired before this method is called and released shortly after. If called with an _unlocked_ lock a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 error is raised.

locked()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.locked "Link to this definition")

Return `True` if the underlying lock is acquired.

notify\_all()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.notify_all "Link to this definition")

Wake up all tasks waiting on this condition.

This method acts like [`notify()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.notify "asyncio.Condition.notify")
, but wakes up all waiting tasks.

The lock must be acquired before this method is called and released shortly after. If called with an _unlocked_ lock a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 error is raised.

release()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.release "Link to this definition")

Release the underlying lock.

When invoked on an unlocked lock, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 is raised.

async wait()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.wait "Link to this definition")

Wait until notified.

If the calling task has not acquired the lock when this method is called, a [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 is raised.

This method releases the underlying lock, and then blocks until it is awakened by a [`notify()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.notify "asyncio.Condition.notify")
 or [`notify_all()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.notify_all "asyncio.Condition.notify_all")
 call. Once awakened, the Condition re-acquires its lock and this method returns `True`.

Note that a task _may_ return from this call spuriously, which is why the caller should always re-check the state and be prepared to `wait()` again. For this reason, you may prefer to use [`wait_for()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.wait_for "asyncio.Condition.wait_for")
 instead.

async wait\_for(_predicate_)[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.wait_for "Link to this definition")

Wait until a predicate becomes _true_.

The predicate must be a callable which result will be interpreted as a boolean value. The method will repeatedly [`wait()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition.wait "asyncio.Condition.wait")
 until the predicate evaluates to _true_. The final value is the return value.

Semaphore[¶](https://docs.python.org/3/library/asyncio-sync.html#semaphore "Link to this heading")

---------------------------------------------------------------------------------------------------

class asyncio.Semaphore(_value\=1_)[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore "Link to this definition")

A Semaphore object. Not thread-safe.

A semaphore manages an internal counter which is decremented by each [`acquire()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore.acquire "asyncio.Semaphore.acquire")
 call and incremented by each [`release()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore.release "asyncio.Semaphore.release")
 call. The counter can never go below zero; when `acquire()` finds that it is zero, it blocks, waiting until some task calls `release()`.

The optional _value_ argument gives the initial value for the internal counter (`1` by default). If the given value is less than `0` a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised.

Changed in version 3.10: Removed the _loop_ parameter.

The preferred way to use a Semaphore is an [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
 statement:

Copy

sem \= asyncio.Semaphore(10)

\# ... later
async with sem:
    \# work with shared resource

which is equivalent to:

Copy

sem \= asyncio.Semaphore(10)

\# ... later
await sem.acquire()
try:
    \# work with shared resource
finally:
    sem.release()

async acquire()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore.acquire "Link to this definition")

Acquire a semaphore.

If the internal counter is greater than zero, decrement it by one and return `True` immediately. If it is zero, wait until a [`release()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore.release "asyncio.Semaphore.release")
 is called and return `True`.

locked()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore.locked "Link to this definition")

Returns `True` if semaphore can not be acquired immediately.

release()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore.release "Link to this definition")

Release a semaphore, incrementing the internal counter by one. Can wake up a task waiting to acquire the semaphore.

Unlike [`BoundedSemaphore`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.BoundedSemaphore "asyncio.BoundedSemaphore")
, `Semaphore` allows making more `release()` calls than `acquire()` calls.

BoundedSemaphore[¶](https://docs.python.org/3/library/asyncio-sync.html#boundedsemaphore "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

class asyncio.BoundedSemaphore(_value\=1_)[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.BoundedSemaphore "Link to this definition")

A bounded semaphore object. Not thread-safe.

Bounded Semaphore is a version of [`Semaphore`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore "asyncio.Semaphore")
 that raises a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 in [`release()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore.release "asyncio.Semaphore.release")
 if it increases the internal counter above the initial _value_.

Changed in version 3.10: Removed the _loop_ parameter.

Barrier[¶](https://docs.python.org/3/library/asyncio-sync.html#barrier "Link to this heading")

-----------------------------------------------------------------------------------------------

class asyncio.Barrier(_parties_)[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier "Link to this definition")

A barrier object. Not thread-safe.

A barrier is a simple synchronization primitive that allows to block until _parties_ number of tasks are waiting on it. Tasks can wait on the [`wait()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier.wait "asyncio.Barrier.wait")
 method and would be blocked until the specified number of tasks end up waiting on `wait()`. At that point all of the waiting tasks would unblock simultaneously.

[`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
 can be used as an alternative to awaiting on [`wait()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier.wait "asyncio.Barrier.wait")
.

The barrier can be reused any number of times.

Example:

Copy

async def example\_barrier():
   \# barrier with 3 parties
   b \= asyncio.Barrier(3)

   \# create 2 new waiting tasks
   asyncio.create\_task(b.wait())
   asyncio.create\_task(b.wait())

   await asyncio.sleep(0)
   print(b)

   \# The third .wait() call passes the barrier
   await b.wait()
   print(b)
   print("barrier passed")

   await asyncio.sleep(0)
   print(b)

asyncio.run(example\_barrier())

Result of this example is:

Copy

<asyncio.locks.Barrier object at 0x... \[filling, waiters:2/3\]\>
<asyncio.locks.Barrier object at 0x... \[draining, waiters:0/3\]\>
barrier passed
<asyncio.locks.Barrier object at 0x... \[filling, waiters:0/3\]\>

Added in version 3.11.

async wait()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier.wait "Link to this definition")

Pass the barrier. When all the tasks party to the barrier have called this function, they are all unblocked simultaneously.

When a waiting or blocked task in the barrier is cancelled, this task exits the barrier which stays in the same state. If the state of the barrier is “filling”, the number of waiting task decreases by 1.

The return value is an integer in the range of 0 to `parties-1`, different for each task. This can be used to select a task to do some special housekeeping, e.g.:

Copy

...
async with barrier as position:
   if position \== 0:
      \# Only one task prints this
      print('End of \*draining phase\*')

This method may raise a [`BrokenBarrierError`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.BrokenBarrierError "asyncio.BrokenBarrierError")
 exception if the barrier is broken or reset while a task is waiting. It could raise a [`CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError")
 if a task is cancelled.

async reset()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier.reset "Link to this definition")

Return the barrier to the default, empty state. Any tasks waiting on it will receive the [`BrokenBarrierError`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.BrokenBarrierError "asyncio.BrokenBarrierError")
 exception.

If a barrier is broken it may be better to just leave it and create a new one.

async abort()[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier.abort "Link to this definition")

Put the barrier into a broken state. This causes any active or future calls to [`wait()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier.wait "asyncio.Barrier.wait")
 to fail with the [`BrokenBarrierError`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.BrokenBarrierError "asyncio.BrokenBarrierError")
. Use this for example if one of the tasks needs to abort, to avoid infinite waiting tasks.

parties[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier.parties "Link to this definition")

The number of tasks required to pass the barrier.

n\_waiting[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier.n_waiting "Link to this definition")

The number of tasks currently waiting in the barrier while filling.

broken[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier.broken "Link to this definition")

A boolean that is `True` if the barrier is in the broken state.

exception asyncio.BrokenBarrierError[¶](https://docs.python.org/3/library/asyncio-sync.html#asyncio.BrokenBarrierError "Link to this definition")

This exception, a subclass of [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
, is raised when the [`Barrier`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier "asyncio.Barrier")
 object is reset or broken.

* * *

Changed in version 3.9: Acquiring a lock using `await lock` or `yield from lock` and/or [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement (`with await lock`, `with (yield from lock)`) was removed. Use `async with lock` instead.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Synchronization Primitives](https://docs.python.org/3/library/asyncio-sync.html#)
    *   [Lock](https://docs.python.org/3/library/asyncio-sync.html#lock)
        
    *   [Event](https://docs.python.org/3/library/asyncio-sync.html#event)
        
    *   [Condition](https://docs.python.org/3/library/asyncio-sync.html#condition)
        
    *   [Semaphore](https://docs.python.org/3/library/asyncio-sync.html#semaphore)
        
    *   [BoundedSemaphore](https://docs.python.org/3/library/asyncio-sync.html#boundedsemaphore)
        
    *   [Barrier](https://docs.python.org/3/library/asyncio-sync.html#barrier)
        

#### Previous topic

[Streams](https://docs.python.org/3/library/asyncio-stream.html "previous chapter")

#### Next topic

[Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Synchronization+Primitives&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-sync.html&pagesource=library%2Fasyncio-sync.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-sync.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-subprocess.html "Subprocesses")
     |
*   [previous](https://docs.python.org/3/library/asyncio-stream.html "Streams")
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
*   [Synchronization Primitives](https://docs.python.org/3/library/asyncio-sync.html)
    
*    
    
    |
*   Theme Auto Light Dark |