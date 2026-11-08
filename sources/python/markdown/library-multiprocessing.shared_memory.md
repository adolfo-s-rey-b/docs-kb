### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/concurrent.html "The concurrent package")
     |
*   [previous](https://docs.python.org/3/library/multiprocessing.html "multiprocessing — Process-based parallelism")
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
*   [`multiprocessing.shared_memory` — Shared memory for direct access across processes](https://docs.python.org/3/library/multiprocessing.shared_memory.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`multiprocessing.shared_memory` — Shared memory for direct access across processes[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#module-multiprocessing.shared_memory "Link to this heading")

========================================================================================================================================================================================================================

**Source code:** [Lib/multiprocessing/shared\_memory.py](https://github.com/python/cpython/tree/3.15/Lib/multiprocessing/shared_memory.py)

Added in version 3.8.

* * *

This module provides a class, [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory")
, for the allocation and management of shared memory to be accessed by one or more processes on a multicore or symmetric multiprocessor (SMP) machine. To assist with the life-cycle management of shared memory especially across distinct processes, a [`BaseManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager "multiprocessing.managers.BaseManager")
 subclass, [`SharedMemoryManager`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager "multiprocessing.managers.SharedMemoryManager")
, is also provided in the [`multiprocessing.managers`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.managers "multiprocessing.managers: Share data between process with shared objects.")
 module.

In this module, shared memory refers to “POSIX style” shared memory blocks (though is not necessarily implemented explicitly as such) and does not refer to “distributed shared memory”. This style of shared memory permits distinct processes to potentially read and write to a common (or shared) region of volatile memory. Processes are conventionally limited to only have access to their own process memory space but shared memory permits the sharing of data between processes, avoiding the need to instead send messages between processes containing that data. Sharing data directly via memory can provide significant performance benefits compared to sharing data via disk or socket or other communications requiring the serialization/deserialization and copying of data.

class multiprocessing.shared\_memory.SharedMemory(_name\=None_, _create\=False_, _size\=0_, _\*_, _track\=True_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "Link to this definition")

Create an instance of the `SharedMemory` class for either creating a new shared memory block or attaching to an existing shared memory block. Each shared memory block is assigned a unique name. In this way, one process can create a shared memory block with a particular name and a different process can attach to that same shared memory block using that same name.

As a resource for sharing data across processes, shared memory blocks may outlive the original process that created them. When one process no longer needs access to a shared memory block that might still be needed by other processes, the [`close()`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.close "multiprocessing.shared_memory.SharedMemory.close")
 method should be called. When a shared memory block is no longer needed by any process, the [`unlink()`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.unlink "multiprocessing.shared_memory.SharedMemory.unlink")
 method should be called to ensure proper cleanup.

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     _|_ [_None_](https://docs.python.org/3/builtins/constants.html#None "None")
    ) – The unique name for the requested shared memory, specified as a string. When creating a new shared memory block, if `None` (the default) is supplied for the name, a novel name will be generated.
    
*   **create** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "bool")
    ) – Control whether a new shared memory block is created (`True`) or an existing shared memory block is attached (`False`).
    
*   **size** ([_int_](https://docs.python.org/3/builtins/functions.html#int "int")
    ) – The requested number of bytes when creating a new shared memory block. Because some platforms choose to allocate chunks of memory based upon that platform’s memory page size, the exact size of the shared memory block may be larger or equal to the size requested. When attaching to an existing shared memory block, the _size_ parameter is ignored.
    
*   **track** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "bool")
    ) – When `True`, register the shared memory block with a resource tracker process on platforms where the OS does not do this automatically. The resource tracker ensures proper cleanup of the shared memory even if all other processes with access to the memory exit without doing so. Python processes created from a common ancestor using [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.")
     facilities share a single resource tracker process, and the lifetime of shared memory segments is handled automatically among these processes. Python processes created in any other way will receive their own resource tracker when accessing shared memory with _track_ enabled. This will cause the shared memory to be deleted by the resource tracker of the first process that terminates. To avoid this issue, users of [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
     or standalone Python processes should set _track_ to `False` when there is already another process in place that does the bookkeeping. _track_ is ignored on Windows, which has its own tracking and automatically deletes shared memory when all handles to it have been closed.
    

Changed in version 3.13: Added the _track_ parameter.

close()[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.close "Link to this definition")

Close the file descriptor/handle to the shared memory from this instance. `close()` should be called once access to the shared memory block from this instance is no longer needed. Depending on operating system, the underlying memory may or may not be freed even if all handles to it have been closed. To ensure proper cleanup, use the [`unlink()`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.unlink "multiprocessing.shared_memory.SharedMemory.unlink")
 method.

unlink()[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.unlink "Link to this definition")

Delete the underlying shared memory block. This should be called only once per shared memory block regardless of the number of handles to it, even in other processes. `unlink()` and [`close()`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.close "multiprocessing.shared_memory.SharedMemory.close")
 can be called in any order, but trying to access data inside a shared memory block after `unlink()` may result in memory access errors, depending on platform.

This method has no effect on Windows, where the only way to delete a shared memory block is to close all handles.

buf[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.buf "Link to this definition")

A memoryview of contents of the shared memory block.

name[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.name "Link to this definition")

Read-only access to the unique name of the shared memory block.

size[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.size "Link to this definition")

Read-only access to size in bytes of the shared memory block.

The following example demonstrates low-level use of [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory")
 instances:

Copy

\>>> from multiprocessing import shared\_memory
\>>> shm\_a \= shared\_memory.SharedMemory(create\=True, size\=10)
\>>> type(shm\_a.buf)
<class 'memoryview'>
\>>> buffer \= shm\_a.buf
\>>> len(buffer)
10
\>>> buffer\[:4\] \= bytearray(\[22, 33, 44, 55\])  \# Modify multiple at once
\>>> buffer\[4\] \= 100                           \# Modify single byte at a time
\>>> \# Attach to an existing shared memory block
\>>> shm\_b \= shared\_memory.SharedMemory(shm\_a.name)
\>>> import array
\>>> array.array('b', shm\_b.buf\[:5\])  \# Copy the data into a new array.array
array('b', \[22, 33, 44, 55, 100\])
\>>> shm\_b.buf\[:5\] \= b'howdy'  \# Modify via shm\_b using bytes
\>>> bytes(shm\_a.buf\[:5\])      \# Access via shm\_a
b'howdy'
\>>> shm\_b.close()   \# Close each SharedMemory instance
\>>> shm\_a.close()
\>>> shm\_a.unlink()  \# Call unlink only once to release the shared memory

The following example demonstrates a practical use of the [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory")
 class with [NumPy arrays](https://numpy.org/)
, accessing the same `numpy.ndarray` from two distinct Python shells:

Copy

\>>> \# In the first Python interactive shell
\>>> import numpy as np
\>>> a \= np.array(\[1, 1, 2, 3, 5, 8\])  \# Start with an existing NumPy array
\>>> from multiprocessing import shared\_memory
\>>> shm \= shared\_memory.SharedMemory(create\=True, size\=a.nbytes)
\>>> \# Now create a NumPy array backed by shared memory
\>>> b \= np.ndarray(a.shape, dtype\=a.dtype, buffer\=shm.buf)
\>>> b\[:\] \= a\[:\]  \# Copy the original data into shared memory
\>>> b
array(\[1, 1, 2, 3, 5, 8\])
\>>> type(b)
<class 'numpy.ndarray'>
\>>> type(a)
<class 'numpy.ndarray'>
\>>> shm.name  \# We did not specify a name so one was chosen for us
'psm\_21467\_46075'

\>>> \# In either the same shell or a new Python shell on the same machine
\>>> import numpy as np
\>>> from multiprocessing import shared\_memory
\>>> \# Attach to the existing shared memory block
\>>> existing\_shm \= shared\_memory.SharedMemory(name\='psm\_21467\_46075')
\>>> \# Note that a.shape is (6,) and a.dtype is np.int64 in this example
\>>> c \= np.ndarray((6,), dtype\=np.int64, buffer\=existing\_shm.buf)
\>>> c
array(\[1, 1, 2, 3, 5, 8\])
\>>> c\[\-1\] \= 888
\>>> c
array(\[  1,   1,   2,   3,   5, 888\])

\>>> \# Back in the first Python interactive shell, b reflects this change
\>>> b
array(\[  1,   1,   2,   3,   5, 888\])

\>>> \# Clean up from within the second Python shell
\>>> del c  \# Unnecessary; merely emphasizing the array is no longer used
\>>> existing\_shm.close()

\>>> \# Clean up from within the first Python shell
\>>> del b  \# Unnecessary; merely emphasizing the array is no longer used
\>>> shm.close()
\>>> shm.unlink()  \# Free and release the shared memory block at the very end

class multiprocessing.managers.SharedMemoryManager(\[_address_\[, _authkey_\]\])[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager "Link to this definition")

A subclass of [`multiprocessing.managers.BaseManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager "multiprocessing.managers.BaseManager")
 which can be used for the management of shared memory blocks across processes.

A call to [`start()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.start "multiprocessing.managers.BaseManager.start")
 on a `SharedMemoryManager` instance causes a new process to be started. This new process’s sole purpose is to manage the life cycle of all shared memory blocks created through it. To trigger the release of all shared memory blocks managed by that process, call [`shutdown()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager.shutdown "multiprocessing.managers.BaseManager.shutdown")
 on the instance. This triggers a [`unlink()`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.unlink "multiprocessing.shared_memory.SharedMemory.unlink")
 call on all of the [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory")
 objects managed by that process and then stops the process itself. By creating `SharedMemory` instances through a `SharedMemoryManager`, we avoid the need to manually track and trigger the freeing of shared memory resources.

This class provides methods for creating and returning [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory")
 instances and for creating a list-like object ([`ShareableList`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList "multiprocessing.shared_memory.ShareableList")
) backed by shared memory.

Refer to [`BaseManager`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.BaseManager "multiprocessing.managers.BaseManager")
 for a description of the inherited _address_ and _authkey_ optional input arguments and how they may be used to connect to an existing `SharedMemoryManager` service from other processes.

SharedMemory(_size_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager.SharedMemory "Link to this definition")

Create and return a new [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory")
 object with the specified _size_ in bytes.

ShareableList(_sequence_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager.ShareableList "Link to this definition")

Create and return a new [`ShareableList`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList "multiprocessing.shared_memory.ShareableList")
 object, initialized by the values from the input _sequence_.

The following example demonstrates the basic mechanisms of a [`SharedMemoryManager`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager "multiprocessing.managers.SharedMemoryManager")
:

Copy

\>>> from multiprocessing.managers import SharedMemoryManager
\>>> smm \= SharedMemoryManager()
\>>> smm.start()  \# Start the process that manages the shared memory blocks
\>>> sl \= smm.ShareableList(range(4))
\>>> sl
ShareableList(\[0, 1, 2, 3\], name='psm\_6572\_7512')
\>>> raw\_shm \= smm.SharedMemory(size\=128)
\>>> another\_sl \= smm.ShareableList('alpha')
\>>> another\_sl
ShareableList(\['a', 'l', 'p', 'h', 'a'\], name='psm\_6572\_12221')
\>>> smm.shutdown()  \# Calls unlink() on sl, raw\_shm, and another\_sl

The following example depicts a potentially more convenient pattern for using [`SharedMemoryManager`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager "multiprocessing.managers.SharedMemoryManager")
 objects via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement to ensure that all shared memory blocks are released after they are no longer needed:

Copy

\>>> with SharedMemoryManager() as smm:
...     sl \= smm.ShareableList(range(2000))
...     \# Divide the work among two processes, storing partial results in sl
...     p1 \= Process(target\=do\_work, args\=(sl, 0, 1000))
...     p2 \= Process(target\=do\_work, args\=(sl, 1000, 2000))
...     p1.start()
...     p2.start()  \# A multiprocessing.Pool might be more efficient
...     p1.join()
...     p2.join()   \# Wait for all work to complete in both processes
...     total\_result \= sum(sl)  \# Consolidate the partial results now in sl

When using a [`SharedMemoryManager`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.managers.SharedMemoryManager "multiprocessing.managers.SharedMemoryManager")
 in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement, the shared memory blocks created using that manager are all released when the `with` statement’s code block finishes execution.

class multiprocessing.shared\_memory.ShareableList(_sequence\=None_, _\*_, _name\=None_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList "Link to this definition")

Provide a mutable list-like object where all values stored within are stored in a shared memory block. This constrains storable values to the following built-in data types:

*   [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
     (signed 64-bit)
    
*   [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
    
*   [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
    
*   [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     (less than 10M bytes each when encoded as UTF-8)
    
*   [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     (less than 10M bytes each)
    
*   `None`
    

It also notably differs from the built-in [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 type in that these lists can not change their overall length (i.e. no `append()`, `insert()`, etc.) and do not support the dynamic creation of new `ShareableList` instances via slicing.

_sequence_ is used in populating a new `ShareableList` full of values. Set to `None` to instead attach to an already existing `ShareableList` by its unique shared memory name.

_name_ is the unique name for the requested shared memory, as described in the definition for [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory")
. When attaching to an existing `ShareableList`, specify its shared memory block’s unique name while leaving _sequence_ set to `None`.

Note

A known issue exists for [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 values. If they end with `\x00` nul bytes or characters, those may be _silently stripped_ when fetching them by index from the `ShareableList`. This `.rstrip(b'\x00')` behavior is considered a bug and may go away in the future. See [gh-106939](https://github.com/python/cpython/issues/106939)
.

For applications where rstripping of trailing nulls is a problem, work around it by always unconditionally appending an extra non-0 byte to the end of such values when storing and unconditionally removing it when fetching:

Copy

\>>> from multiprocessing import shared\_memory
\>>> nul\_bug\_demo \= shared\_memory.ShareableList(\['?\\x00', b'\\x03\\x02\\x01\\x00\\x00\\x00'\])
\>>> nul\_bug\_demo\[0\]
'?'
\>>> nul\_bug\_demo\[1\]
b'\\x03\\x02\\x01'
\>>> nul\_bug\_demo.shm.unlink()
\>>> padded \= shared\_memory.ShareableList(\['?\\x00\\x07', b'\\x03\\x02\\x01\\x00\\x00\\x00\\x07'\])
\>>> padded\[0\]\[:\-1\]
'?\\x00'
\>>> padded\[1\]\[:\-1\]
b'\\x03\\x02\\x01\\x00\\x00\\x00'
\>>> padded.shm.unlink()

count(_value_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList.count "Link to this definition")

Return the number of occurrences of _value_.

index(_value_)[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList.index "Link to this definition")

Return first index position of _value_. Raise [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if _value_ is not present.

format[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList.format "Link to this definition")

Read-only attribute containing the [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")
 packing format used by all currently stored values.

shm[¶](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList.shm "Link to this definition")

The [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory")
 instance where the values are stored.

The following example demonstrates basic use of a [`ShareableList`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList "multiprocessing.shared_memory.ShareableList")
 instance:

Copy

\>>> from multiprocessing import shared\_memory
\>>> a \= shared\_memory.ShareableList(\['howdy', b'HoWdY', \-273.154, 100, None, True, 42\])
\>>> \[ type(entry) for entry in a \]
\[<class 'str'>, <class 'bytes'>, <class 'float'>, <class 'int'>, <class 'NoneType'>, <class 'bool'>, <class 'int'>\]
\>>> a\[2\]
\-273.154
\>>> a\[2\] \= \-78.5
\>>> a\[2\]
\-78.5
\>>> a\[2\] \= 'dry ice'  \# Changing data types is supported as well
\>>> a\[2\]
'dry ice'
\>>> a\[2\] \= 'larger than previously allocated storage space'
Traceback (most recent call last):
  ...
ValueError: exceeds available storage for existing str
\>>> a\[2\]
'dry ice'
\>>> len(a)
7
\>>> a.index(42)
6
\>>> a.count(b'howdy')
0
\>>> a.count(b'HoWdY')
1
\>>> a.shm.close()
\>>> a.shm.unlink()
\>>> del a  \# Use of a ShareableList after call to unlink() is unsupported

The following example depicts how one, two, or many processes may access the same [`ShareableList`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList "multiprocessing.shared_memory.ShareableList")
 by supplying the name of the shared memory block behind it:

Copy

\>>> b \= shared\_memory.ShareableList(range(5))         \# In a first process
\>>> c \= shared\_memory.ShareableList(name\=b.shm.name)  \# In a second process
\>>> c
ShareableList(\[0, 1, 2, 3, 4\], name='...')
\>>> c\[\-1\] \= \-999
\>>> b\[\-1\]
\-999
\>>> b.shm.close()
\>>> c.shm.close()
\>>> c.shm.unlink()

The following examples demonstrates that [`ShareableList`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.ShareableList "multiprocessing.shared_memory.ShareableList")
 (and underlying [`SharedMemory`](https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory "multiprocessing.shared_memory.SharedMemory")
) objects can be pickled and unpickled if needed. Note, that it will still be the same shared object. This happens, because the deserialized object has the same unique name and is just attached to an existing object with the same name (if the object is still alive):

Copy

\>>> import pickle
\>>> from multiprocessing import shared\_memory
\>>> sl \= shared\_memory.ShareableList(range(10))
\>>> list(sl)
\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]

Copy

\>>> deserialized\_sl \= pickle.loads(pickle.dumps(sl))
\>>> list(deserialized\_sl)
\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]

Copy

\>>> sl\[0\] \= \-1
\>>> deserialized\_sl\[1\] \= \-2
\>>> list(sl)
\[-1, -2, 2, 3, 4, 5, 6, 7, 8, 9\]
\>>> list(deserialized\_sl)
\[-1, -2, 2, 3, 4, 5, 6, 7, 8, 9\]

Copy

\>>> sl.shm.close()
\>>> sl.shm.unlink()

#### Previous topic

[`multiprocessing` — Process-based parallelism](https://docs.python.org/3/library/multiprocessing.html "previous chapter")

#### Next topic

[The `concurrent` package](https://docs.python.org/3/library/concurrent.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=multiprocessing.shared_memory+%E2%80%94+Shared+memory+for+direct+access+across+processes&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fmultiprocessing.shared_memory.html&pagesource=library%2Fmultiprocessing.shared_memory.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/multiprocessing.shared_memory.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/concurrent.html "The concurrent package")
     |
*   [previous](https://docs.python.org/3/library/multiprocessing.html "multiprocessing — Process-based parallelism")
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
*   [`multiprocessing.shared_memory` — Shared memory for direct access across processes](https://docs.python.org/3/library/multiprocessing.shared_memory.html)
    
*    
    
    |
*   Theme Auto Light Dark |