### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/subprocess.html "subprocess — Subprocess management")
     |
*   [previous](https://docs.python.org/3/library/concurrent.futures.html "concurrent.futures — Launching parallel tasks")
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
*   [`concurrent.interpreters` — Multiple interpreters in the same process](https://docs.python.org/3/library/concurrent.interpreters.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`concurrent.interpreters` — Multiple interpreters in the same process[¶](https://docs.python.org/3/library/concurrent.interpreters.html#module-concurrent.interpreters "Link to this heading")

===============================================================================================================================================================================================

Added in version 3.14.

**Source code:** [Lib/concurrent/interpreters](https://github.com/python/cpython/tree/3.15/Lib/concurrent/interpreters)

* * *

The `concurrent.interpreters` module constructs higher-level interfaces on top of the lower level `_interpreters` module.

The module is primarily meant to provide a basic API for managing interpreters (AKA “subinterpreters”) and running things in them. Running mostly involves switching to an interpreter (in the current thread) and calling a function in that execution context.

For concurrency, interpreters themselves (and this module) don’t provide much more than isolation, which on its own isn’t useful. Actual concurrency is available separately through [`threads`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
 – see [below](https://docs.python.org/3/library/concurrent.interpreters.html#interp-concurrency)
.

See also

[`InterpreterPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.InterpreterPoolExecutor "concurrent.futures.InterpreterPoolExecutor")

Combines threads with interpreters in a familiar interface.

[Isolating Extension Modules](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extensions-howto)

How to update an extension module to support multiple interpreters.

[**PEP 554**](https://peps.python.org/pep-0554/)

[**PEP 734**](https://peps.python.org/pep-0734/)

[**PEP 684**](https://peps.python.org/pep-0684/)

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

Key details[¶](https://docs.python.org/3/library/concurrent.interpreters.html#key-details "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Before we dive in further, there are a small number of details to keep in mind about using multiple interpreters:

*   [isolated](https://docs.python.org/3/library/concurrent.interpreters.html#interp-isolation)
    , by default
    
*   no implicit threads
    
*   not all PyPI packages support use in multiple interpreters yet
    

Introduction[¶](https://docs.python.org/3/library/concurrent.interpreters.html#introduction "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

An “interpreter” is effectively the execution context of the Python runtime. It contains all of the state the runtime needs to execute a program. This includes things like the import state and builtins. (Each thread, even if there’s only the main thread, has some extra runtime state, in addition to the current interpreter, related to the current exception and the bytecode eval loop.)

The concept and functionality of the interpreter have been a part of Python since version 2.2, but the feature was only available through the C-API and not well known, and the [isolation](https://docs.python.org/3/library/concurrent.interpreters.html#interp-isolation)
 was relatively incomplete until version 3.12.

### Multiple Interpreters and Isolation[¶](https://docs.python.org/3/library/concurrent.interpreters.html#multiple-interpreters-and-isolation "Link to this heading")

A Python implementation may support using multiple interpreters in the same process. CPython has this support. Each interpreter is effectively isolated from the others (with a limited number of carefully managed process-global exceptions to the rule).

That isolation is primarily useful as a strong separation between distinct logical components of a program, where you want to have careful control of how those components interact.

Note

Interpreters in the same process can technically never be strictly isolated from one another since there are few restrictions on memory access within the same process. The Python runtime makes a best effort at isolation but extension modules may easily violate that. Therefore, do not use multiple interpreters in security-sensitive situations, where they shouldn’t have access to each other’s data.

### Running in an Interpreter[¶](https://docs.python.org/3/library/concurrent.interpreters.html#running-in-an-interpreter "Link to this heading")

Running in a different interpreter involves switching to it in the current thread and then calling some function. The runtime will execute the function using the current interpreter’s state. The `concurrent.interpreters` module provides a basic API for creating and managing interpreters, as well as the switch-and-call operation.

No other threads are automatically started for the operation. There is [a helper](https://docs.python.org/3/library/concurrent.interpreters.html#interp-call-in-thread)
 for that though. There is another dedicated helper for calling the builtin [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 in an interpreter.

When [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 (or [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
) are called in an interpreter, they run using the interpreter’s `__main__` module as the “globals” namespace. The same is true for functions that aren’t associated with any module. This is the same as how scripts invoked from the command-line run in the `__main__` module.

### Concurrency and Parallelism[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrency-and-parallelism "Link to this heading")

As noted earlier, interpreters do not provide any concurrency on their own. They strictly represent the isolated execution context the runtime will use _in the current thread_. That isolation makes them similar to processes, but they still enjoy in-process efficiency, like threads.

All that said, interpreters do naturally support certain flavors of concurrency. There’s a powerful side effect of that isolation. It enables a different approach to concurrency than you can take with async or threads. It’s a similar concurrency model to CSP or the actor model, a model which is relatively easy to reason about.

You can take advantage of that concurrency model in a single thread, switching back and forth between interpreters, Stackless-style. However, this model is more useful when you combine interpreters with multiple threads. This mostly involves starting a new thread, where you switch to another interpreter and run what you want there.

Each actual thread in Python, even if you’re only running in the main thread, has its own _current_ execution context. Multiple threads can use the same interpreter or different ones.

At a high level, you can think of the combination of threads and interpreters as threads with opt-in sharing.

As a significant bonus, interpreters are sufficiently isolated that they do not share the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
, which means combining threads with multiple interpreters enables full multi-core parallelism. (This has been the case since Python 3.12.)

### Communication Between Interpreters[¶](https://docs.python.org/3/library/concurrent.interpreters.html#communication-between-interpreters "Link to this heading")

In practice, multiple interpreters are useful only if we have a way to communicate between them. This usually involves some form of message passing, but can even mean sharing data in some carefully managed way.

With this in mind, the `concurrent.interpreters` module provides a [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue")
 implementation, available through [`create_queue()`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.create_queue "concurrent.interpreters.create_queue")
.

### “Sharing” Objects[¶](https://docs.python.org/3/library/concurrent.interpreters.html#sharing-objects "Link to this heading")

Any data actually shared between interpreters loses the thread-safety provided by the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
. There are various options for dealing with this in extension modules. However, from Python code the lack of thread-safety means objects can’t actually be shared, with a few exceptions. Instead, a copy must be created, which means mutable objects won’t stay in sync.

By default, most objects are copied with [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
 when they are passed to another interpreter. Nearly all of the immutable builtin objects are either directly shared or copied efficiently. For example:

*   [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
    
*   [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
     ([`True`](https://docs.python.org/3/builtins/constants.html#True "True")
     and [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
    )
    
*   [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    
*   [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
    
*   [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
    
*   [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
    
*   [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
     (of similarly supported objects)
    

There are a small number of Python types that actually share mutable data between interpreters:

*   [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
    
*   [`Queue`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue "concurrent.interpreters.Queue")
    

Reference[¶](https://docs.python.org/3/library/concurrent.interpreters.html#reference "Link to this heading")

--------------------------------------------------------------------------------------------------------------

This module defines the following functions:

concurrent.interpreters.list\_all()[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.list_all "Link to this definition")

Return a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 of [`Interpreter`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter "concurrent.interpreters.Interpreter")
 objects, one for each existing interpreter.

concurrent.interpreters.get\_current()[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.get_current "Link to this definition")

Return an [`Interpreter`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter "concurrent.interpreters.Interpreter")
 object for the currently running interpreter.

concurrent.interpreters.get\_main()[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.get_main "Link to this definition")

Return an [`Interpreter`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter "concurrent.interpreters.Interpreter")
 object for the main interpreter. This is the interpreter the runtime created to run the [REPL](https://docs.python.org/3/glossary.html#term-REPL)
 or the script given at the command-line. It is usually the only one.

concurrent.interpreters.create()[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.create "Link to this definition")

Initialize a new (idle) Python interpreter and return a [`Interpreter`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter "concurrent.interpreters.Interpreter")
 object for it.

concurrent.interpreters.create\_queue(_maxsize\=0_)[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.create_queue "Link to this definition")

Initialize a new cross-interpreter queue and return a [`Queue`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue "concurrent.interpreters.Queue")
 object for it.

_maxsize_ is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will be blocked once this size has been reached, until queue items are consumed. If _maxsize_ is less than or equal to zero, the queue size is infinite.

### Interpreter objects[¶](https://docs.python.org/3/library/concurrent.interpreters.html#interpreter-objects "Link to this heading")

class concurrent.interpreters.Interpreter(_id_)[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter "Link to this definition")

A single interpreter in the current process.

Generally, `Interpreter` shouldn’t be called directly. Instead, use [`create()`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.create "concurrent.interpreters.create")
 or one of the other module functions.

id[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter.id "Link to this definition")

(read-only)

The underlying interpreter’s ID.

whence[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter.whence "Link to this definition")

(read-only)

A string describing where the interpreter came from.

is\_running()[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter.is_running "Link to this definition")

Return `True` if the interpreter is currently executing code in its `__main__` module and `False` otherwise.

close()[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter.close "Link to this definition")

Finalize and destroy the interpreter.

prepare\_main(_ns\=None_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter.prepare_main "Link to this definition")

Bind objects in the interpreter’s `__main__` module.

Some objects are actually shared and some are copied efficiently, but most are copied via [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
. See [“Sharing” Objects](https://docs.python.org/3/library/concurrent.interpreters.html#interp-object-sharing)
.

exec(_code_, _/_)[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter.exec "Link to this definition")

Run the given source code in the interpreter (in the current thread).

call(_callable_, _/_, _\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter.call "Link to this definition")

Return the result of running the given function in the interpreter (in the current thread).

call\_in\_thread(_callable_, _/_, _\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Interpreter.call_in_thread "Link to this definition")

Run the given function in the interpreter (in a new thread).

### Exceptions[¶](https://docs.python.org/3/library/concurrent.interpreters.html#exceptions "Link to this heading")

exception concurrent.interpreters.InterpreterError[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.InterpreterError "Link to this definition")

This exception, a subclass of [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
, is raised when an interpreter-related error happens.

exception concurrent.interpreters.InterpreterNotFoundError[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.InterpreterNotFoundError "Link to this definition")

This exception, a subclass of [`InterpreterError`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.InterpreterError "concurrent.interpreters.InterpreterError")
, is raised when the targeted interpreter no longer exists.

exception concurrent.interpreters.ExecutionFailed[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.ExecutionFailed "Link to this definition")

This exception, a subclass of [`InterpreterError`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.InterpreterError "concurrent.interpreters.InterpreterError")
, is raised when the running code raised an uncaught exception.

excinfo[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.ExecutionFailed.excinfo "Link to this definition")

A basic snapshot of the exception raised in the other interpreter.

exception concurrent.interpreters.NotShareableError[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.NotShareableError "Link to this definition")

This exception, a subclass of [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
, is raised when an object cannot be sent to another interpreter.

### Communicating Between Interpreters[¶](https://docs.python.org/3/library/concurrent.interpreters.html#communicating-between-interpreters "Link to this heading")

class concurrent.interpreters.Queue(_id_)[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue "Link to this definition")

A wrapper around a low-level, cross-interpreter queue, which implements all the methods of [`queue.Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue")
 except for [`task_done()`](https://docs.python.org/3/library/queue.html#queue.Queue.task_done "queue.Queue.task_done")
, [`join()`](https://docs.python.org/3/library/queue.html#queue.Queue.join "queue.Queue.join")
 and [`shutdown()`](https://docs.python.org/3/library/queue.html#queue.Queue.shutdown "queue.Queue.shutdown")
. The underlying queue can only be created through [`create_queue()`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.create_queue "concurrent.interpreters.create_queue")
.

Some objects are actually shared and some are copied efficiently, but most are copied via [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
. See [“Sharing” Objects](https://docs.python.org/3/library/concurrent.interpreters.html#interp-object-sharing)
.

id[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.id "Link to this definition")

(read-only)

The queue’s ID.

qsize()[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.qsize "Link to this definition")

Return the number of items in the queue.

empty()[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.empty "Link to this definition")

Return `True` if the queue is empty, `False` otherwise.

full()[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.full "Link to this definition")

Return `True` if the queue is full, `False` otherwise.

put(_obj_, _block\=True_, _timeout\=None_)[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.put "Link to this definition")

Put _obj_ into the queue. If optional args _block_ is true and _timeout_ is `None` (the default), block if necessary until a free slot is available. If _timeout_ is a positive number, it blocks at most _timeout_ seconds and raises the [`QueueFull`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.QueueFull "concurrent.interpreters.QueueFull")
 exception if no free slot was available within that time. Otherwise (_block_ is false), put an object on the queue if a free slot is immediately available, else raise the `QueueFull` exception (_timeout_ is ignored in that case).

put\_nowait(_obj_)[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.put_nowait "Link to this definition")

Equivalent to `put(obj, block=False)`.

get(_block\=True_, _timeout\=None_)[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.get "Link to this definition")

Remove and return an object from the queue. If optional args _block_ is true and _timeout_ is `None` (the default), block if necessary until an object is available. If _timeout_ is a positive number, it blocks at most _timeout_ seconds and raises the [`QueueEmpty`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.QueueEmpty "concurrent.interpreters.QueueEmpty")
 exception if no object was available within that time. Otherwise (_block_ is false), return an object if one is immediately available, else raise the `QueueEmpty` exception (_timeout_ is ignored in that case).

get\_nowait()[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.get_nowait "Link to this definition")

Equivalent to `get(block=False)`.

exception concurrent.interpreters.QueueEmpty[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.QueueEmpty "Link to this definition")

This exception, a subclass of [`queue.Empty`](https://docs.python.org/3/library/queue.html#queue.Empty "queue.Empty")
, is raised from [`Queue.get()`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.get "concurrent.interpreters.Queue.get")
 and [`Queue.get_nowait()`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.get_nowait "concurrent.interpreters.Queue.get_nowait")
 when the queue is empty.

exception concurrent.interpreters.QueueFull[¶](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.QueueFull "Link to this definition")

This exception, a subclass of [`queue.Full`](https://docs.python.org/3/library/queue.html#queue.Full "queue.Full")
, is raised from [`Queue.put()`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.put "concurrent.interpreters.Queue.put")
 and [`Queue.put_nowait()`](https://docs.python.org/3/library/concurrent.interpreters.html#concurrent.interpreters.Queue.put_nowait "concurrent.interpreters.Queue.put_nowait")
 when the queue is full.

Basic usage[¶](https://docs.python.org/3/library/concurrent.interpreters.html#basic-usage "Link to this heading")

------------------------------------------------------------------------------------------------------------------

Creating an interpreter and running code in it:

Copy

from concurrent import interpreters

interp \= interpreters.create()

\# Run in the current OS thread.

interp.exec('print("spam!")')

interp.exec("""if True:
    print('spam!')
    """)

from textwrap import dedent
interp.exec(dedent("""
    print('spam!')
    """))

def run(arg):
    return arg

res \= interp.call(run, 'spam!')
print(res)

def run():
    print('spam!')

interp.call(run)

\# Run in new OS thread.

t \= interp.call\_in\_thread(run)
t.join()

Communicating between interpreters with a queue:

Copy

from concurrent import interpreters

interp \= interpreters.create()
queue \= interpreters.create\_queue()

def worker(queue):
    queue.put('spam!')

t \= interp.call\_in\_thread(worker, queue)
print(queue.get())
t.join()

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`concurrent.interpreters` — Multiple interpreters in the same process](https://docs.python.org/3/library/concurrent.interpreters.html#)
    *   [Key details](https://docs.python.org/3/library/concurrent.interpreters.html#key-details)
        
    *   [Introduction](https://docs.python.org/3/library/concurrent.interpreters.html#introduction)
        *   [Multiple Interpreters and Isolation](https://docs.python.org/3/library/concurrent.interpreters.html#multiple-interpreters-and-isolation)
            
        *   [Running in an Interpreter](https://docs.python.org/3/library/concurrent.interpreters.html#running-in-an-interpreter)
            
        *   [Concurrency and Parallelism](https://docs.python.org/3/library/concurrent.interpreters.html#concurrency-and-parallelism)
            
        *   [Communication Between Interpreters](https://docs.python.org/3/library/concurrent.interpreters.html#communication-between-interpreters)
            
        *   [“Sharing” Objects](https://docs.python.org/3/library/concurrent.interpreters.html#sharing-objects)
            
    *   [Reference](https://docs.python.org/3/library/concurrent.interpreters.html#reference)
        *   [Interpreter objects](https://docs.python.org/3/library/concurrent.interpreters.html#interpreter-objects)
            
        *   [Exceptions](https://docs.python.org/3/library/concurrent.interpreters.html#exceptions)
            
        *   [Communicating Between Interpreters](https://docs.python.org/3/library/concurrent.interpreters.html#communicating-between-interpreters)
            
    *   [Basic usage](https://docs.python.org/3/library/concurrent.interpreters.html#basic-usage)
        

#### Previous topic

[`concurrent.futures` — Launching parallel tasks](https://docs.python.org/3/library/concurrent.futures.html "previous chapter")

#### Next topic

[`subprocess` — Subprocess management](https://docs.python.org/3/library/subprocess.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=concurrent.interpreters+%E2%80%94+Multiple+interpreters+in+the+same+process&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fconcurrent.interpreters.html&pagesource=library%2Fconcurrent.interpreters.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/concurrent.interpreters.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/subprocess.html "subprocess — Subprocess management")
     |
*   [previous](https://docs.python.org/3/library/concurrent.futures.html "concurrent.futures — Launching parallel tasks")
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
*   [`concurrent.interpreters` — Multiple interpreters in the same process](https://docs.python.org/3/library/concurrent.interpreters.html)
    
*    
    
    |
*   Theme Auto Light Dark |