### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/objimpl.html "Object Implementation Support")
     |
*   [previous](https://docs.python.org/3/c-api/init_config.html "Python Initialization Configuration")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Memory Management](https://docs.python.org/3/c-api/memory.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Memory Management[¶](https://docs.python.org/3/c-api/memory.html#memory-management "Link to this heading")

===========================================================================================================

Overview[¶](https://docs.python.org/3/c-api/memory.html#overview "Link to this heading")

-----------------------------------------------------------------------------------------

Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the _Python memory manager_. The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching.

At the lowest level, a raw memory allocator ensures that there is enough room in the private heap for storing all Python-related data by interacting with the memory manager of the operating system. On top of the raw memory allocator, several object-specific allocators operate on the same heap and implement distinct memory management policies adapted to the peculiarities of every object type. For example, integer objects are managed differently within the heap than strings, tuples or dictionaries because integers imply different storage requirements and speed/space tradeoffs. The Python memory manager thus delegates some of the work to the object-specific allocators, but ensures that the latter operate within the bounds of the private heap.

It is important to understand that the management of the Python heap is performed by the interpreter itself and that the user has no control over it, even if they regularly manipulate object pointers to memory blocks inside that heap. The allocation of heap space for Python objects and other internal buffers is performed on demand by the Python memory manager through the Python/C API functions listed in this document.

To avoid memory corruption, extension writers should never try to operate on Python objects with the functions exported by the C library: `malloc()`, `calloc()`, `realloc()` and `free()`. This will result in mixed calls between the C allocator and the Python memory manager with fatal consequences, because they implement different algorithms and operate on different heaps. However, one may safely allocate and release memory blocks with the C library allocator for individual purposes, as shown in the following example:

PyObject \*res;
char \*buf \= (char \*) malloc(BUFSIZ); /\* for I/O \*/

if (buf \== NULL)
    return PyErr\_NoMemory();
...Do some I/O operation involving buf...
res \= PyBytes\_FromString(buf);
free(buf); /\* malloc'ed \*/
return res;

In this example, the memory request for the I/O buffer is handled by the C library allocator. The Python memory manager is involved only in the allocation of the bytes object returned as a result.

In most situations, however, it is recommended to allocate memory from the Python heap specifically because the latter is under control of the Python memory manager. For example, this is required when the interpreter is extended with new object types written in C. Another reason for using the Python heap is the desire to _inform_ the Python memory manager about the memory needs of the extension module. Even when the requested memory is used exclusively for internal, highly specific purposes, delegating all memory requests to the Python memory manager causes the interpreter to have a more accurate image of its memory footprint as a whole. Consequently, under certain circumstances, the Python memory manager may or may not trigger appropriate actions, like garbage collection, memory compaction or other preventive procedures. Note that by using the C library allocator as shown in the previous example, the allocated memory for the I/O buffer completely escapes the Python memory manager.

See also

The [`PYTHONMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC)
 environment variable can be used to configure the memory allocators used by Python.

The [`PYTHONMALLOCSTATS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOCSTATS)
 environment variable can be used to print statistics of the [pymalloc memory allocator](https://docs.python.org/3/c-api/memory.html#pymalloc)
 every time a new pymalloc object arena is created, and on shutdown.

Allocator Domains[¶](https://docs.python.org/3/c-api/memory.html#allocator-domains "Link to this heading")

-----------------------------------------------------------------------------------------------------------

All allocating functions belong to one of three different “domains” (see also [`PyMemAllocatorDomain`](https://docs.python.org/3/c-api/memory.html#c.PyMemAllocatorDomain "PyMemAllocatorDomain")
). These domains represent different allocation strategies and are optimized for different purposes. The specific details on how every domain allocates memory or what internal functions each domain calls is considered an implementation detail, but for debugging purposes a simplified table can be found at [Default Memory Allocators](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
. The APIs used to allocate and free a block of memory must be from the same domain. For example, [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
 must be used to free memory allocated using [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
.

The three allocation domains are:

*   Raw domain: intended for allocating memory for general-purpose memory buffers where the allocation _must_ go to the system allocator or where the allocator can operate without an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
    . The memory is requested directly from the system. See [Raw Memory Interface](https://docs.python.org/3/c-api/memory.html#raw-memoryinterface)
    .
    
*   “Mem” domain: intended for allocating memory for Python buffers and general-purpose memory buffers where the allocation must be performed with an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
    . The memory is taken from the Python private heap. See [Memory Interface](https://docs.python.org/3/c-api/memory.html#memoryinterface)
    .
    
*   Object domain: intended for allocating memory for Python objects. The memory is taken from the Python private heap. See [Object allocators](https://docs.python.org/3/c-api/memory.html#objectinterface)
    .
    

Note

The [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build requires that only Python objects are allocated using the “object” domain and that all Python objects are allocated using that domain. This differs from the prior Python versions, where this was only a best practice and not a hard requirement.

For example, buffers (non-Python objects) should be allocated using [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
, [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
, or `malloc()`, but not [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
.

See [Memory Allocation APIs](https://docs.python.org/3/howto/free-threading-extensions.html#free-threaded-memory-allocation)
.

Raw Memory Interface[¶](https://docs.python.org/3/c-api/memory.html#raw-memory-interface "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

The following function sets are wrappers to the system allocator. These functions are thread-safe, so a [thread state](https://docs.python.org/3/glossary.html#term-thread-state)
 does not need to be [attached](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

The [default raw memory allocator](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
 uses the following functions: `malloc()`, `calloc()`, `realloc()` and `free()`; call `malloc(1)` (or `calloc(1, 1)`) when requesting zero bytes.

Added in version 3.4.

void \*PyMem\_RawMalloc(size\_t n)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Allocates _n_ bytes and returns a pointer of type void\* to the allocated memory, or `NULL` if the request fails.

Requesting zero bytes returns a distinct non-`NULL` pointer if possible, as if `PyMem_RawMalloc(1)` had been called instead. The memory will not have been initialized in any way.

void \*PyMem\_RawCalloc(size\_t nelem, size\_t elsize)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawCalloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Allocates _nelem_ elements each of size _elsize_ bytes and returns a pointer of type void\* to the allocated memory, or `NULL` if the request fails. The memory is initialized to zeros.

Requesting zero elements or elements of size zero bytes returns a distinct non-`NULL` pointer if possible, as if `PyMem_RawCalloc(1, 1)` had been called instead.

Added in version 3.5.

void \*PyMem\_RawRealloc(void \*p, size\_t n)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Resizes the memory block pointed to by _p_ to _n_ bytes. The contents will be unchanged to the minimum of the old and the new sizes.

If _p_ is `NULL`, the call is equivalent to `PyMem_RawMalloc(n)`; else if _n_ is equal to zero, the memory block is resized but is not freed, and the returned pointer is non-`NULL`.

Unless _p_ is `NULL`, it must have been returned by a previous call to [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
, [`PyMem_RawRealloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
 or [`PyMem_RawCalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawCalloc "PyMem_RawCalloc")
.

If the request fails, [`PyMem_RawRealloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
 returns `NULL` and _p_ remains a valid pointer to the previous memory area.

void PyMem\_RawFree(void \*p)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawFree "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Frees the memory block pointed to by _p_, which must have been returned by a previous call to [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
, [`PyMem_RawRealloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
 or [`PyMem_RawCalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawCalloc "PyMem_RawCalloc")
. Otherwise, or if `PyMem_RawFree(p)` has been called before, undefined behavior occurs.

If _p_ is `NULL`, no operation is performed.

Memory Interface[¶](https://docs.python.org/3/c-api/memory.html#memory-interface "Link to this heading")

---------------------------------------------------------------------------------------------------------

The following function sets, modeled after the ANSI C standard, but specifying behavior when requesting zero bytes, are available for allocating and releasing memory from the Python heap.

In the GIL-enabled build (default build) the [default memory allocator](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
 uses the [pymalloc memory allocator](https://docs.python.org/3/c-api/memory.html#pymalloc)
, whereas in the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
, the default is the [mimalloc memory allocator](https://docs.python.org/3/c-api/memory.html#mimalloc)
 instead.

Warning

There must be an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 when using these functions.

Changed in version 3.6: The default allocator is now pymalloc instead of system `malloc()`.

Changed in version 3.13: In the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build, the default allocator is now [mimalloc](https://docs.python.org/3/c-api/memory.html#mimalloc)
.

void \*PyMem\_Malloc(size\_t n)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Allocates _n_ bytes and returns a pointer of type void\* to the allocated memory, or `NULL` if the request fails.

Requesting zero bytes returns a distinct non-`NULL` pointer if possible, as if `PyMem_Malloc(1)` had been called instead. The memory will not have been initialized in any way.

void \*PyMem\_Calloc(size\_t nelem, size\_t elsize)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_Calloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Allocates _nelem_ elements each of size _elsize_ bytes and returns a pointer of type void\* to the allocated memory, or `NULL` if the request fails. The memory is initialized to zeros.

Requesting zero elements or elements of size zero bytes returns a distinct non-`NULL` pointer if possible, as if `PyMem_Calloc(1, 1)` had been called instead.

Added in version 3.5.

void \*PyMem\_Realloc(void \*p, size\_t n)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Resizes the memory block pointed to by _p_ to _n_ bytes. The contents will be unchanged to the minimum of the old and the new sizes.

If _p_ is `NULL`, the call is equivalent to `PyMem_Malloc(n)`; else if _n_ is equal to zero, the memory block is resized but is not freed, and the returned pointer is non-`NULL`.

Unless _p_ is `NULL`, it must have been returned by a previous call to [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
, [`PyMem_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "PyMem_Realloc")
 or [`PyMem_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Calloc "PyMem_Calloc")
.

If the request fails, [`PyMem_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "PyMem_Realloc")
 returns `NULL` and _p_ remains a valid pointer to the previous memory area.

void PyMem\_Free(void \*p)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Frees the memory block pointed to by _p_, which must have been returned by a previous call to [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
, [`PyMem_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "PyMem_Realloc")
 or [`PyMem_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Calloc "PyMem_Calloc")
. Otherwise, or if `PyMem_Free(p)` has been called before, undefined behavior occurs.

If _p_ is `NULL`, no operation is performed.

The following type-oriented macros are provided for convenience. Note that _TYPE_ refers to any C type.

PyMem\_New(TYPE, n)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_New "Link to this definition")
  

Same as [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
, but allocates `(n * sizeof(TYPE))` bytes of memory. Returns a pointer cast to `TYPE*`. The memory will not have been initialized in any way.

PyMem\_Resize(p, TYPE, n)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_Resize "Link to this definition")
  

Same as [`PyMem_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "PyMem_Realloc")
, but the memory block is resized to `(n * sizeof(TYPE))` bytes. Returns a pointer cast to `TYPE*`. On return, _p_ will be a pointer to the new memory area, or `NULL` in the event of failure.

This is a C preprocessor macro; _p_ is always reassigned. Save the original value of _p_ to avoid losing memory when handling errors.

void PyMem\_Del(void \*p)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_Del "Link to this definition")
  

Same as [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
.

### Deprecated aliases[¶](https://docs.python.org/3/c-api/memory.html#deprecated-aliases "Link to this heading")

These are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 aliases to existing functions and macros. They exist solely for backwards compatibility.

| Deprecated alias | Corresponding function or macro |
| --- | --- |
| PyMem\_MALLOC(size)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_MALLOC "Link to this definition") | [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc") |
| PyMem\_NEW(type, size)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_NEW "Link to this definition") | [`PyMem_New`](https://docs.python.org/3/c-api/memory.html#c.PyMem_New "PyMem_New") |
| PyMem\_REALLOC(ptr, size)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_REALLOC "Link to this definition") | [`PyMem_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "PyMem_Realloc") |
| PyMem\_RESIZE(ptr, type, size)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_RESIZE "Link to this definition") | [`PyMem_Resize`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Resize "PyMem_Resize") |
| PyMem\_FREE(ptr)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_FREE "Link to this definition") | [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free") |
| PyMem\_DEL(ptr)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_DEL "Link to this definition") | [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free") |

Changed in version 3.4: The macros are now aliases of the corresponding functions and macros. Previously, their behavior was the same, but their use did not necessarily preserve binary compatibility across Python versions.

Deprecated since version 2.0.

Object allocators[¶](https://docs.python.org/3/c-api/memory.html#object-allocators "Link to this heading")

-----------------------------------------------------------------------------------------------------------

The following function sets, modeled after the ANSI C standard, but specifying behavior when requesting zero bytes, are available for allocating and releasing memory from the Python heap.

Note

There is no guarantee that the memory returned by these allocators can be successfully cast to a Python object when intercepting the allocating functions in this domain by the methods described in the [Customize Memory Allocators](https://docs.python.org/3/c-api/memory.html#customize-memory-allocators)
 section.

The [default object allocator](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
 uses the [pymalloc memory allocator](https://docs.python.org/3/c-api/memory.html#pymalloc)
. In the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build, the default is the [mimalloc memory allocator](https://docs.python.org/3/c-api/memory.html#mimalloc)
 instead.

Warning

There must be an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 when using these functions.

void \*PyObject\_Malloc(size\_t n)[¶](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Allocates _n_ bytes and returns a pointer of type void\* to the allocated memory, or `NULL` if the request fails.

Requesting zero bytes returns a distinct non-`NULL` pointer if possible, as if `PyObject_Malloc(1)` had been called instead. The memory will not have been initialized in any way.

void \*PyObject\_Calloc(size\_t nelem, size\_t elsize)[¶](https://docs.python.org/3/c-api/memory.html#c.PyObject_Calloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Allocates _nelem_ elements each of size _elsize_ bytes and returns a pointer of type void\* to the allocated memory, or `NULL` if the request fails. The memory is initialized to zeros.

Requesting zero elements or elements of size zero bytes returns a distinct non-`NULL` pointer if possible, as if `PyObject_Calloc(1, 1)` had been called instead.

Added in version 3.5.

void \*PyObject\_Realloc(void \*p, size\_t n)[¶](https://docs.python.org/3/c-api/memory.html#c.PyObject_Realloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Resizes the memory block pointed to by _p_ to _n_ bytes. The contents will be unchanged to the minimum of the old and the new sizes.

If _p_ is `NULL`, the call is equivalent to `PyObject_Malloc(n)`; else if _n_ is equal to zero, the memory block is resized but is not freed, and the returned pointer is non-`NULL`.

Unless _p_ is `NULL`, it must have been returned by a previous call to [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
, [`PyObject_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Realloc "PyObject_Realloc")
 or [`PyObject_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Calloc "PyObject_Calloc")
.

If the request fails, [`PyObject_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Realloc "PyObject_Realloc")
 returns `NULL` and _p_ remains a valid pointer to the previous memory area.

void PyObject\_Free(void \*p)[¶](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Frees the memory block pointed to by _p_, which must have been returned by a previous call to [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
, [`PyObject_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Realloc "PyObject_Realloc")
 or [`PyObject_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Calloc "PyObject_Calloc")
. Otherwise, or if `PyObject_Free(p)` has been called before, undefined behavior occurs.

If _p_ is `NULL`, no operation is performed.

Do not call this directly to free an object’s memory; call the type’s [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
 slot instead.

Do not use this for memory allocated by [`PyObject_GC_New`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_New "PyObject_GC_New")
 or [`PyObject_GC_NewVar`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_NewVar "PyObject_GC_NewVar")
; use [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
 instead.

See also

*   [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
     is the equivalent of this function for memory allocated by types that support garbage collection.
    
*   [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
    
*   [`PyObject_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Realloc "PyObject_Realloc")
    
*   [`PyObject_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Calloc "PyObject_Calloc")
    
*   [`PyObject_New`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New")
    
*   [`PyObject_NewVar`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar")
    
*   [`PyType_GenericAlloc()`](https://docs.python.org/3/c-api/type.html#c.PyType_GenericAlloc "PyType_GenericAlloc")
    
*   [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
    

Default Memory Allocators[¶](https://docs.python.org/3/c-api/memory.html#default-memory-allocators "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

Default memory allocators:

| Configuration | Name | PyMem\_RawMalloc | PyMem\_Malloc | PyObject\_Malloc |
| --- | --- | --- | --- | --- |
| Release build | `"pymalloc"` | `malloc` | `pymalloc` | `pymalloc` |
| Debug build | `"pymalloc_debug"` | `malloc` + debug | `pymalloc` + debug | `pymalloc` + debug |
| Release build, without pymalloc | `"malloc"` | `malloc` | `malloc` | `malloc` |
| Debug build, without pymalloc | `"malloc_debug"` | `malloc` + debug | `malloc` + debug | `malloc` + debug |
| Free-threaded build | `"mimalloc"` | `mimalloc` | `mimalloc` | `mimalloc` |
| Free-threaded debug build | `"mimalloc_debug"` | `mimalloc` + debug | `mimalloc` + debug | `mimalloc` + debug |

Legend:

*   Name: value for [`PYTHONMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC)
     environment variable.
    
*   `malloc`: system allocators from the standard C library, C functions: `malloc()`, `calloc()`, `realloc()` and `free()`.
    
*   `pymalloc`: [pymalloc memory allocator](https://docs.python.org/3/c-api/memory.html#pymalloc)
    .
    
*   `mimalloc`: [mimalloc memory allocator](https://docs.python.org/3/c-api/memory.html#mimalloc)
    .
    
*   “+ debug”: with [debug hooks on the Python memory allocators](https://docs.python.org/3/c-api/memory.html#pymem-debug-hooks)
    .
    
*   “Debug build”: [Python build in debug mode](https://docs.python.org/3/using/configure.html#debug-build)
    .
    

Customize Memory Allocators[¶](https://docs.python.org/3/c-api/memory.html#customize-memory-allocators "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

Added in version 3.4.

type PyMemAllocatorEx[¶](https://docs.python.org/3/c-api/memory.html#c.PyMemAllocatorEx "Link to this definition")
  

Structure used to describe a memory block allocator. The structure has the following fields:

| Field | Meaning |
| --- | --- |
| `void *ctx` | user context passed as first argument |
| `void* malloc(void *ctx, size_t size)` | allocate a memory block |
| `void* calloc(void *ctx, size_t nelem, size_t elsize)` | allocate a memory block initialized with zeros |
| `void* realloc(void *ctx, void *ptr, size_t new_size)` | allocate or resize a memory block |
| `void free(void *ctx, void *ptr)` | free a memory block |

Changed in version 3.5: The `PyMemAllocator` structure was renamed to [`PyMemAllocatorEx`](https://docs.python.org/3/c-api/memory.html#c.PyMemAllocatorEx "PyMemAllocatorEx")
 and a new `calloc` field was added.

type PyMemAllocatorDomain[¶](https://docs.python.org/3/c-api/memory.html#c.PyMemAllocatorDomain "Link to this definition")
  

Enum used to identify an allocator domain. Domains:

PYMEM\_DOMAIN\_RAW[¶](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_RAW "Link to this definition")
  

Functions:

*   [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
    
*   [`PyMem_RawRealloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
    
*   [`PyMem_RawCalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawCalloc "PyMem_RawCalloc")
    
*   [`PyMem_RawFree()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawFree "PyMem_RawFree")
    

PYMEM\_DOMAIN\_MEM[¶](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_MEM "Link to this definition")
  

Functions:

*   [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
    ,
    
*   [`PyMem_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "PyMem_Realloc")
    
*   [`PyMem_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Calloc "PyMem_Calloc")
    
*   [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
    

PYMEM\_DOMAIN\_OBJ[¶](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "Link to this definition")
  

Functions:

*   [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
    
*   [`PyObject_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Realloc "PyObject_Realloc")
    
*   [`PyObject_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Calloc "PyObject_Calloc")
    
*   [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
    

void PyMem\_GetAllocator([PyMemAllocatorDomain](https://docs.python.org/3/c-api/memory.html#c.PyMemAllocatorDomain "PyMemAllocatorDomain")
 domain, [PyMemAllocatorEx](https://docs.python.org/3/c-api/memory.html#c.PyMemAllocatorEx "PyMemAllocatorEx")
 \*allocator)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_GetAllocator "Link to this definition")
  

Get the memory block allocator of the specified domain.

void PyMem\_SetAllocator([PyMemAllocatorDomain](https://docs.python.org/3/c-api/memory.html#c.PyMemAllocatorDomain "PyMemAllocatorDomain")
 domain, [PyMemAllocatorEx](https://docs.python.org/3/c-api/memory.html#c.PyMemAllocatorEx "PyMemAllocatorEx")
 \*allocator)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_SetAllocator "Link to this definition")
  

Set the memory block allocator of the specified domain.

The new allocator must return a distinct non-`NULL` pointer when requesting zero bytes.

For the [`PYMEM_DOMAIN_RAW`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_RAW "PYMEM_DOMAIN_RAW")
 domain, the allocator must be thread-safe: a [thread state](https://docs.python.org/3/glossary.html#term-thread-state)
 is not [attached](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 when the allocator is called.

For the remaining domains, the allocator must also be thread-safe: the allocator may be called in different interpreters that do not share a [GIL](https://docs.python.org/3/glossary.html#term-GIL)
.

If the new allocator is not a hook (does not call the previous allocator), the [`PyMem_SetupDebugHooks()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_SetupDebugHooks "PyMem_SetupDebugHooks")
 function must be called to reinstall the debug hooks on top on the new allocator.

See also [`PyPreConfig.allocator`](https://docs.python.org/3/c-api/init_config.html#c.PyPreConfig.allocator "PyPreConfig.allocator")
 and [Preinitialize Python with PyPreConfig](https://docs.python.org/3/c-api/init_config.html#c-preinit)
.

Warning

[`PyMem_SetAllocator()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_SetAllocator "PyMem_SetAllocator")
 does have the following contract:

*   It can be called after [`Py_PreInitialize()`](https://docs.python.org/3/c-api/init_config.html#c.Py_PreInitialize "Py_PreInitialize")
     and before [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
     to install a custom memory allocator. There are no restrictions over the installed allocator other than the ones imposed by the domain (for instance, the Raw Domain allows the allocator to be called without an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
    ). See [the section on allocator domains](https://docs.python.org/3/c-api/memory.html#id1)
     for more information.
    
*   If called after Python has finish initializing (after [`Py_InitializeFromConfig()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_InitializeFromConfig "Py_InitializeFromConfig")
     has been called) the allocator **must** wrap the existing allocator. Substituting the current allocator for some other arbitrary one is **not supported**.
    

Changed in version 3.12: All allocators must be thread-safe.

void PyMem\_SetupDebugHooks(void)[¶](https://docs.python.org/3/c-api/memory.html#c.PyMem_SetupDebugHooks "Link to this definition")
  

Setup [debug hooks in the Python memory allocators](https://docs.python.org/3/c-api/memory.html#pymem-debug-hooks)
 to detect memory errors.

Debug hooks on the Python memory allocators[¶](https://docs.python.org/3/c-api/memory.html#debug-hooks-on-the-python-memory-allocators "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

When [Python is built in debug mode](https://docs.python.org/3/using/configure.html#debug-build)
, the [`PyMem_SetupDebugHooks()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_SetupDebugHooks "PyMem_SetupDebugHooks")
 function is called at the [Python preinitialization](https://docs.python.org/3/c-api/init_config.html#c-preinit)
 to setup debug hooks on Python memory allocators to detect memory errors.

The [`PYTHONMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC)
 environment variable can be used to install debug hooks on a Python compiled in release mode (ex: `PYTHONMALLOC=debug`).

The [`PyMem_SetupDebugHooks()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_SetupDebugHooks "PyMem_SetupDebugHooks")
 function can be used to set debug hooks after calling [`PyMem_SetAllocator()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_SetAllocator "PyMem_SetAllocator")
.

These debug hooks fill dynamically allocated memory blocks with special, recognizable bit patterns. Newly allocated memory is filled with the byte `0xCD` (`PYMEM_CLEANBYTE`), freed memory is filled with the byte `0xDD` (`PYMEM_DEADBYTE`). Memory blocks are surrounded by “forbidden bytes” filled with the byte `0xFD` (`PYMEM_FORBIDDENBYTE`). Strings of these bytes are unlikely to be valid addresses, floats, or ASCII strings.

Runtime checks:

*   Detect API violations. For example, detect if [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
     is called on a memory block allocated by [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
    .
    
*   Detect write before the start of the buffer (buffer underflow).
    
*   Detect write after the end of the buffer (buffer overflow).
    
*   Check that there is an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
     when allocator functions of [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "PYMEM_DOMAIN_OBJ")
     (ex: [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
    ) and [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_MEM "PYMEM_DOMAIN_MEM")
     (ex: [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
    ) domains are called.
    

On error, the debug hooks use the [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")
 module to get the traceback where a memory block was allocated. The traceback is only displayed if `tracemalloc` is tracing Python memory allocations and the memory block was traced.

Let _S_ = `sizeof(size_t)`. `2*S` bytes are added at each end of each block of _N_ bytes requested. The memory layout is like so, where p represents the address returned by a malloc-like or realloc-like function (`p[i:j]` means the slice of bytes from `*(p+i)` inclusive up to `*(p+j)` exclusive; note that the treatment of negative indices differs from a Python slice):

`p[-2*S:-S]`

Number of bytes originally asked for. This is a size\_t, big-endian (easier to read in a memory dump).

`p[-S]`

API identifier (ASCII character):

*   `'r'` for [`PYMEM_DOMAIN_RAW`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_RAW "PYMEM_DOMAIN_RAW")
    .
    
*   `'m'` for [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_MEM "PYMEM_DOMAIN_MEM")
    .
    
*   `'o'` for [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "PYMEM_DOMAIN_OBJ")
    .
    

`p[-S+1:0]`

Copies of PYMEM\_FORBIDDENBYTE. Used to catch under- writes and reads.

`p[0:N]`

The requested memory, filled with copies of PYMEM\_CLEANBYTE, used to catch reference to uninitialized memory. When a realloc-like function is called requesting a larger memory block, the new excess bytes are also filled with PYMEM\_CLEANBYTE. When a free-like function is called, these are overwritten with PYMEM\_DEADBYTE, to catch reference to freed memory. When a realloc- like function is called requesting a smaller memory block, the excess old bytes are also filled with PYMEM\_DEADBYTE.

`p[N:N+S]`

Copies of PYMEM\_FORBIDDENBYTE. Used to catch over- writes and reads.

`p[N+S:N+2*S]`

Only used if the `PYMEM_DEBUG_SERIALNO` macro is defined (not defined by default).

A serial number, incremented by 1 on each call to a malloc-like or realloc-like function. Big-endian `size_t`. If “bad memory” is detected later, the serial number gives an excellent way to set a breakpoint on the next run, to capture the instant at which this block was passed out. The static function bumpserialno() in obmalloc.c is the only place the serial number is incremented, and exists so you can set such a breakpoint easily.

A realloc-like or free-like function first checks that the PYMEM\_FORBIDDENBYTE bytes at each end are intact. If they’ve been altered, diagnostic output is written to stderr, and the program is aborted via Py\_FatalError(). The other main failure mode is provoking a memory error when a program reads up one of the special bit patterns and tries to use it as an address. If you get in a debugger then and look at the object, you’re likely to see that it’s entirely filled with PYMEM\_DEADBYTE (meaning freed memory is getting used) or PYMEM\_CLEANBYTE (meaning uninitialized memory is getting used).

Changed in version 3.6: The [`PyMem_SetupDebugHooks()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_SetupDebugHooks "PyMem_SetupDebugHooks")
 function now also works on Python compiled in release mode. On error, the debug hooks now use [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")
 to get the traceback where a memory block was allocated. The debug hooks now also check if there is an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 when functions of [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "PYMEM_DOMAIN_OBJ")
 and [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_MEM "PYMEM_DOMAIN_MEM")
 domains are called.

Changed in version 3.8: Byte patterns `0xCB` (`PYMEM_CLEANBYTE`), `0xDB` (`PYMEM_DEADBYTE`) and `0xFB` (`PYMEM_FORBIDDENBYTE`) have been replaced with `0xCD`, `0xDD` and `0xFD` to use the same values than Windows CRT debug `malloc()` and `free()`.

The pymalloc allocator[¶](https://docs.python.org/3/c-api/memory.html#the-pymalloc-allocator "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

Python has a _pymalloc_ allocator optimized for small objects (smaller or equal to 512 bytes) with a short lifetime. It uses memory mappings called “arenas” with a fixed size of either 256 KiB on 32-bit platforms or 1 MiB on 64-bit platforms. When Python is configured with [`--with-pymalloc-hugepages`](https://docs.python.org/3/using/configure.html#cmdoption-with-pymalloc-hugepages)
, the arena size on 64-bit platforms is increased to 2 MiB to match the huge page size, and arena allocation will attempt to use huge pages (`MAP_HUGETLB` on Linux, `MEM_LARGE_PAGES` on Windows) with automatic fallback to regular pages. It falls back to [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
 and [`PyMem_RawRealloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
 for allocations larger than 512 bytes.

_pymalloc_ is the [default allocator](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
 of the [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_MEM "PYMEM_DOMAIN_MEM")
 (ex: [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
) and [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "PYMEM_DOMAIN_OBJ")
 (ex: [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
) domains.

The arena allocator uses the following functions:

*   `VirtualAlloc()` and `VirtualFree()` on Windows,
    
*   `mmap()` and `munmap()` if available,
    
*   `malloc()` and `free()` otherwise.
    

This allocator is disabled if Python is configured with the [`--without-pymalloc`](https://docs.python.org/3/using/configure.html#cmdoption-without-pymalloc)
 option. It can also be disabled at runtime using the [`PYTHONMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC)
 environment variable (ex: `PYTHONMALLOC=malloc`).

Typically, it makes sense to disable the pymalloc allocator when building Python with AddressSanitizer ([`--with-address-sanitizer`](https://docs.python.org/3/using/configure.html#cmdoption-with-address-sanitizer)
) which helps uncover low level bugs within the C code.

### Customize pymalloc Arena Allocator[¶](https://docs.python.org/3/c-api/memory.html#customize-pymalloc-arena-allocator "Link to this heading")

Added in version 3.4.

type PyObjectArenaAllocator[¶](https://docs.python.org/3/c-api/memory.html#c.PyObjectArenaAllocator "Link to this definition")
  

Structure used to describe an arena allocator. The structure has three fields:

| Field | Meaning |
| --- | --- |
| `void *ctx` | user context passed as first argument |
| `void* alloc(void *ctx, size_t size)` | allocate an arena of size bytes |
| `void free(void *ctx, void *ptr, size_t size)` | free an arena |

void PyObject\_GetArenaAllocator([PyObjectArenaAllocator](https://docs.python.org/3/c-api/memory.html#c.PyObjectArenaAllocator "PyObjectArenaAllocator")
 \*allocator)[¶](https://docs.python.org/3/c-api/memory.html#c.PyObject_GetArenaAllocator "Link to this definition")
  

Get the arena allocator.

void PyObject\_SetArenaAllocator([PyObjectArenaAllocator](https://docs.python.org/3/c-api/memory.html#c.PyObjectArenaAllocator "PyObjectArenaAllocator")
 \*allocator)[¶](https://docs.python.org/3/c-api/memory.html#c.PyObject_SetArenaAllocator "Link to this definition")
  

Set the arena allocator.

The mimalloc allocator[¶](https://docs.python.org/3/c-api/memory.html#the-mimalloc-allocator "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

Added in version 3.13.

Python supports the [mimalloc](https://github.com/microsoft/mimalloc/)
 allocator when the underlying platform support is available. mimalloc is a general purpose allocator with excellent performance characteristics, initially developed by Daan Leijen for the runtime systems of the Koka and Lean languages.

Unlike [pymalloc](https://docs.python.org/3/c-api/memory.html#pymalloc)
, which is optimized for small objects (512 bytes or fewer), mimalloc handles allocations of any size.

In the [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 build, mimalloc is the default and **required** allocator for the [`PYMEM_DOMAIN_MEM`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_MEM "PYMEM_DOMAIN_MEM")
 and [`PYMEM_DOMAIN_OBJ`](https://docs.python.org/3/c-api/memory.html#c.PYMEM_DOMAIN_OBJ "PYMEM_DOMAIN_OBJ")
 domains. It cannot be disabled in free-threaded builds. The free-threaded build uses per-thread mimalloc heaps, which allows allocation and deallocation to proceed without locking in most cases.

In the default (non-free-threaded) build, mimalloc is available but not the default allocator. It can be selected at runtime using [`PYTHONMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC)
`=mimalloc` (or `mimalloc_debug` to include [debug hooks](https://docs.python.org/3/c-api/memory.html#pymem-debug-hooks)
). It can be disabled at build time using the [`--without-mimalloc`](https://docs.python.org/3/using/configure.html#cmdoption-without-mimalloc)
 configure option, but this option cannot be combined with [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
.

tracemalloc C API[¶](https://docs.python.org/3/c-api/memory.html#tracemalloc-c-api "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Added in version 3.7.

int PyTraceMalloc\_Track(unsigned int domain, uintptr\_t ptr, size\_t size)[¶](https://docs.python.org/3/c-api/memory.html#c.PyTraceMalloc_Track "Link to this definition")
  

Track an allocated memory block in the [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")
 module.

Return `0` on success, return `-1` on error (failed to allocate memory to store the trace). Return `-2` if tracemalloc is disabled.

If memory block is already tracked, update the existing trace.

int PyTraceMalloc\_Untrack(unsigned int domain, uintptr\_t ptr)[¶](https://docs.python.org/3/c-api/memory.html#c.PyTraceMalloc_Untrack "Link to this definition")
  

Untrack an allocated memory block in the [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.")
 module. Do nothing if the block was not tracked.

Return `-2` if tracemalloc is disabled, otherwise return `0`.

Examples[¶](https://docs.python.org/3/c-api/memory.html#examples "Link to this heading")

-----------------------------------------------------------------------------------------

Here is the example from section [Overview](https://docs.python.org/3/c-api/memory.html#memoryoverview)
, rewritten so that the I/O buffer is allocated from the Python heap by using the first function set:

PyObject \*res;
char \*buf \= (char \*) PyMem\_Malloc(BUFSIZ); /\* for I/O \*/

if (buf \== NULL)
    return PyErr\_NoMemory();
/\* ...Do some I/O operation involving buf... \*/
res \= PyBytes\_FromString(buf);
PyMem\_Free(buf); /\* allocated with PyMem\_Malloc \*/
return res;

The same code using the type-oriented function set:

PyObject \*res;
char \*buf \= PyMem\_New(char, BUFSIZ); /\* for I/O \*/

if (buf \== NULL)
    return PyErr\_NoMemory();
/\* ...Do some I/O operation involving buf... \*/
res \= PyBytes\_FromString(buf);
PyMem\_Free(buf); /\* allocated with PyMem\_New \*/
return res;

Note that in the two examples above, the buffer is always manipulated via functions belonging to the same set. Indeed, it is required to use the same memory API family for a given memory block, so that the risk of mixing different allocators is reduced to a minimum. The following code sequence contains two errors, one of which is labeled as _fatal_ because it mixes two different allocators operating on different heaps.

char \*buf1 \= PyMem\_New(char, BUFSIZ);
char \*buf2 \= (char \*) malloc(BUFSIZ);
char \*buf3 \= (char \*) PyMem\_Malloc(BUFSIZ);
...
PyMem\_Del(buf3);  /\* Wrong -- should be PyMem\_Free() \*/
free(buf2);       /\* Right -- allocated via malloc() \*/
free(buf1);       /\* Fatal -- should be PyMem\_Free()  \*/

In addition to the functions aimed at handling raw memory blocks from the Python heap, objects in Python are allocated and released with [`PyObject_New`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New")
, [`PyObject_NewVar`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar")
 and [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
.

These will be explained in the next chapter on defining and implementing new object types in C.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Memory Management](https://docs.python.org/3/c-api/memory.html#)
    *   [Overview](https://docs.python.org/3/c-api/memory.html#overview)
        
    *   [Allocator Domains](https://docs.python.org/3/c-api/memory.html#allocator-domains)
        
    *   [Raw Memory Interface](https://docs.python.org/3/c-api/memory.html#raw-memory-interface)
        
    *   [Memory Interface](https://docs.python.org/3/c-api/memory.html#memory-interface)
        *   [Deprecated aliases](https://docs.python.org/3/c-api/memory.html#deprecated-aliases)
            
    *   [Object allocators](https://docs.python.org/3/c-api/memory.html#object-allocators)
        
    *   [Default Memory Allocators](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
        
    *   [Customize Memory Allocators](https://docs.python.org/3/c-api/memory.html#customize-memory-allocators)
        
    *   [Debug hooks on the Python memory allocators](https://docs.python.org/3/c-api/memory.html#debug-hooks-on-the-python-memory-allocators)
        
    *   [The pymalloc allocator](https://docs.python.org/3/c-api/memory.html#the-pymalloc-allocator)
        *   [Customize pymalloc Arena Allocator](https://docs.python.org/3/c-api/memory.html#customize-pymalloc-arena-allocator)
            
    *   [The mimalloc allocator](https://docs.python.org/3/c-api/memory.html#the-mimalloc-allocator)
        
    *   [tracemalloc C API](https://docs.python.org/3/c-api/memory.html#tracemalloc-c-api)
        
    *   [Examples](https://docs.python.org/3/c-api/memory.html#examples)
        

#### Previous topic

[Python Initialization Configuration](https://docs.python.org/3/c-api/init_config.html "previous chapter")

#### Next topic

[Object Implementation Support](https://docs.python.org/3/c-api/objimpl.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Memory+Management&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fmemory.html&pagesource=c-api%2Fmemory.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/memory.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/objimpl.html "Object Implementation Support")
     |
*   [previous](https://docs.python.org/3/c-api/init_config.html "Python Initialization Configuration")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Memory Management](https://docs.python.org/3/c-api/memory.html)
    
*    
    
    |
*   Theme Auto Light Dark |