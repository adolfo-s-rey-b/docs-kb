[Skip to main content](https://numpy.org/doc/stable/reference/thread_safety.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Thread Safety[#](https://numpy.org/doc/stable/reference/thread_safety.html#thread-safety "Link to this heading")

=================================================================================================================

NumPy supports use in a multithreaded context via the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "(in Python v3.14)")
 module in the standard library. Many NumPy operations release the [GIL](https://docs.python.org/3/glossary.html#term-GIL "(in Python v3.14)")
, so unlike many situations in Python, it is possible to improve parallel performance by exploiting multithreaded parallelism in Python.

The easiest performance gains happen when each worker thread owns its own array or set of array objects, with no data directly shared between threads. Because NumPy releases the GIL for many low-level operations, threads that spend most of the time in low-level code will run in parallel.

It is possible to share NumPy arrays between threads, but extreme care must be taken to avoid creating thread safety issues when mutating arrays that are shared between multiple threads. If two threads simultaneously read from and write to the same array, they will at best produce inconsistent, racey results that are not reproducible, let alone correct. It is also possible to crash the Python interpreter by, for example, resizing an array while another thread is reading from it to compute a ufunc operation.

In the future, we may add locking to [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 to make writing multithreaded algorithms using NumPy arrays safer, but for now we suggest focusing on read-only access of arrays that are shared between threads, or adding your own locking if you need to mutation and multithreading.

Note that operations that _do not_ release the GIL will see no performance gains from use of the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "(in Python v3.14)")
 module, and instead might be better served with [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "(in Python v3.14)")
. In particular, operations on arrays with `dtype=np.object_` do not release the GIL.

Context-local state[#](https://numpy.org/doc/stable/reference/thread_safety.html#context-local-state "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

NumPy maintains some state for ufuncs context-local basis, which means each thread in a multithreaded program or task in an asyncio program has its own independent configuration of the [`numpy.errstate`](https://numpy.org/doc/stable/reference/generated/numpy.errstate.html#numpy.errstate "numpy.errstate")
 (see [Floating point error handling](https://numpy.org/doc/stable/reference/routines.err.html)
), and of [Text formatting options](https://numpy.org/doc/stable/reference/routines.io.html#text-formatting-options)
.

You can update state stored in a context variable by entering a context manager. As soon as the context manager exits, the state will be reset to its value before entering the context manager.

Free-threaded Python[#](https://numpy.org/doc/stable/reference/thread_safety.html#free-threaded-python "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

New in version 2.1.

Starting with NumPy 2.1 and CPython 3.13, NumPy also has experimental support for python runtimes with the GIL disabled. See [https://py-free-threading.github.io](https://py-free-threading.github.io/)
 for more information about installing and using [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading "(in Python v3.14)")
 Python, as well as information about supporting it in libraries that depend on NumPy.

Because free-threaded Python does not have a global interpreter lock to serialize access to Python objects, there are more opportunities for threads to mutate shared state and create thread safety issues. In addition to the limitations about locking of the [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 object noted above, this also means that arrays with `dtype=np.object_` are not protected by the GIL, creating data races for python objects that are not possible outside free-threaded python.

C-API Threading Support[#](https://numpy.org/doc/stable/reference/thread_safety.html#c-api-threading-support "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

For developers writing C extensions that interact with NumPy, several parts of the [C-API array documentation](https://numpy.org/doc/stable/reference/c-api/array.html)
 provide detailed information about multithreading considerations.

See Also[#](https://numpy.org/doc/stable/reference/thread_safety.html#see-also "Link to this heading")

-------------------------------------------------------------------------------------------------------

*   [Multithreaded generation](https://numpy.org/doc/stable/reference/random/multithreading.html)
     - Practical example of using NumPy’s random number generators in a multithreaded context with [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures "(in Python v3.14)")
    .
    

On this page