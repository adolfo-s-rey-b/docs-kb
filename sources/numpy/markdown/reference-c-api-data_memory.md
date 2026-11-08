[Skip to main content](https://numpy.org/doc/stable/reference/c-api/data_memory.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/c-api/data_memory.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/c-api/data_memory.html)
[2.4](https://numpy.org/doc/2.4/reference/c-api/data_memory.html)
[2.3](https://numpy.org/doc/2.3/reference/c-api/data_memory.html)
[2.2](https://numpy.org/doc/2.2/reference/c-api/data_memory.html)
[2.1](https://numpy.org/doc/2.1/reference/c-api/data_memory.html)
[2.0](https://numpy.org/doc/2.0/reference/c-api/data_memory.html)
[1.26](https://numpy.org/doc/1.26/reference/c-api/data_memory.html)
[1.25](https://numpy.org/doc/1.25/reference/c-api/data_memory.html)
[1.24](https://numpy.org/doc/1.24/reference/c-api/data_memory.html)
[1.23](https://numpy.org/doc/1.23/reference/c-api/data_memory.html)
[1.22](https://numpy.org/doc/1.22/reference/c-api/data_memory.html)
[1.21](https://numpy.org/doc/1.21/reference/c-api/data_memory.html)
[1.20](https://numpy.org/doc/1.20/reference/c-api/data_memory.html)
[1.19](https://numpy.org/doc/1.19/reference/c-api/data_memory.html)
[1.18](https://numpy.org/doc/1.18/reference/c-api/data_memory.html)
[1.17](https://numpy.org/doc/1.17/reference/c-api/data_memory.html)
[1.16](https://numpy.org/doc/1.16/reference/c-api/data_memory.html)
[1.15](https://numpy.org/doc/1.15/reference/c-api/data_memory.html)
[1.14](https://numpy.org/doc/1.14/reference/c-api/data_memory.html)
[1.13](https://numpy.org/doc/1.13/reference/c-api/data_memory.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Memory management in NumPy[#](https://numpy.org/doc/stable/reference/c-api/data_memory.html#memory-management-in-numpy "Link to this heading")

===============================================================================================================================================

The [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 is a python class. It requires additional memory allocations to hold [`numpy.ndarray.strides`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.strides.html#numpy.ndarray.strides "numpy.ndarray.strides")
, [`numpy.ndarray.shape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "numpy.ndarray.shape")
 and [`numpy.ndarray.data`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.data.html#numpy.ndarray.data "numpy.ndarray.data")
 attributes. These attributes are specially allocated after creating the python object in [`__new__`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "(in Python v3.14)")
. The `strides` and `shape` are stored in a piece of memory allocated internally.

The `data` allocation used to store the actual array values (which could be pointers in the case of `object` arrays) can be very large, so NumPy has provided interfaces to manage its allocation and release. This document details how those interfaces work.

Historical overview[#](https://numpy.org/doc/stable/reference/c-api/data_memory.html#historical-overview "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Since version 1.7.0, NumPy has exposed a set of `PyDataMem_*` functions ([`PyDataMem_NEW`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataMem_NEW "PyDataMem_NEW")
, [`PyDataMem_FREE`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataMem_FREE "PyDataMem_FREE")
, [`PyDataMem_RENEW`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyDataMem_RENEW "PyDataMem_RENEW")
) which are backed by _alloc_, _free_, _realloc_ respectively.

Since those early days, Python also improved its memory management capabilities, and began providing various [management policies](https://docs.python.org/3/c-api/memory.html#memoryoverview "(in Python v3.14)")
 beginning in version 3.4. These routines are divided into a set of domains, each domain has a [`PyMemAllocatorEx`](https://docs.python.org/3/c-api/memory.html#c.PyMemAllocatorEx "(in Python v3.14)")
 structure of routines for memory management. Python also added a [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "(in Python v3.14)")
 module to trace calls to the various routines. These tracking hooks were added to the NumPy `PyDataMem_*` routines.

NumPy added a small cache of allocated memory in its internal `npy_alloc_cache`, `npy_alloc_cache_zero`, and `npy_free_cache` functions. These wrap `alloc`, `alloc-and-memset(0)` and `free` respectively, but when `npy_free_cache` is called, it adds the pointer to a short list of available blocks marked by size. These blocks can be re-used by subsequent calls to `npy_alloc*`, avoiding memory thrashing.

Configurable memory routines in NumPy (NEP 49)[#](https://numpy.org/doc/stable/reference/c-api/data_memory.html#configurable-memory-routines-in-numpy-nep-49 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Users may wish to override the internal data memory routines with ones of their own. Since NumPy does not use the Python domain strategy to manage data memory, it provides an alternative set of C-APIs to change memory routines. There are no Python domain-wide strategies for large chunks of object data, so those are less suited to NumPy’s needs. User who wish to change the NumPy data memory management routines can use [`PyDataMem_SetHandler`](https://numpy.org/doc/stable/reference/c-api/data_memory.html#c.PyDataMem_SetHandler "PyDataMem_SetHandler")
, which uses a [`PyDataMem_Handler`](https://numpy.org/doc/stable/reference/c-api/data_memory.html#c.PyDataMem_Handler "PyDataMem_Handler")
 structure to hold pointers to functions used to manage the data memory. The calls are still wrapped by internal routines to call [`PyTraceMalloc_Track`](https://docs.python.org/3/c-api/memory.html#c.PyTraceMalloc_Track "(in Python v3.14)")
, [`PyTraceMalloc_Untrack`](https://docs.python.org/3/c-api/memory.html#c.PyTraceMalloc_Untrack "(in Python v3.14)")
. Since the functions may change during the lifetime of the process, each `ndarray` carries with it the functions used at the time of its instantiation, and these will be used to reallocate or free the data memory of the instance.

type PyDataMem\_Handler[#](https://numpy.org/doc/stable/reference/c-api/data_memory.html#c.PyDataMem_Handler "Link to this definition")
  

A struct to hold function pointers used to manipulate memory

typedef struct {
    char name\[127\];  /\* multiple of 64 to keep the struct aligned \*/
    uint8\_t version; /\* currently 1 \*/
    PyDataMemAllocator allocator;
} PyDataMem\_Handler;

Copy to clipboard

where the allocator structure is

/\* The declaration of free differs from PyMemAllocatorEx \*/
typedef struct {
    void \*ctx;
    void\* (\*malloc) (void \*ctx, size\_t size);
    void\* (\*calloc) (void \*ctx, size\_t nelem, size\_t elsize);
    void\* (\*realloc) (void \*ctx, void \*ptr, size\_t new\_size);
    void (\*free) (void \*ctx, void \*ptr, size\_t size);
} PyDataMemAllocator;

Copy to clipboard

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyDataMem\_SetHandler([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*handler)[#](https://numpy.org/doc/stable/reference/c-api/data_memory.html#c.PyDataMem_SetHandler "Link to this definition")
  

Set a new allocation policy. If the input value is `NULL`, will reset the policy to the default. Return the previous policy, or return `NULL` if an error has occurred. We wrap the user-provided functions so they will still call the python and numpy memory management callback hooks.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "(in Python v3.14)")
 \*PyDataMem\_GetHandler()[#](https://numpy.org/doc/stable/reference/c-api/data_memory.html#c.PyDataMem_GetHandler "Link to this definition")
  

Return the current policy that will be used to allocate data for the next `PyArrayObject`. On failure, return `NULL`.

For an example of setting up and using the PyDataMem\_Handler, see the test in `numpy/_core/tests/test_mem_policy.py`

What happens when deallocating if there is no policy set[#](https://numpy.org/doc/stable/reference/c-api/data_memory.html#what-happens-when-deallocating-if-there-is-no-policy-set "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A rare but useful technique is to allocate a buffer outside NumPy, use [`PyArray_NewFromDescr`](https://numpy.org/doc/stable/reference/c-api/array.html#c.PyArray_NewFromDescr "PyArray_NewFromDescr")
 to wrap the buffer in a `ndarray`, then switch the `OWNDATA` flag to true. When the `ndarray` is released, the appropriate function from the `ndarray`’s `PyDataMem_Handler` should be called to free the buffer. But the `PyDataMem_Handler` field was never set, it will be `NULL`. For backward compatibility, NumPy will call `free()` to release the buffer. If `NUMPY_WARN_IF_NO_MEM_POLICY` is set to `1`, a warning will be emitted. The current default is not to emit a warning, this may change in a future version of NumPy.

A better technique would be to use a `PyCapsule` as a base object:

/\* define a PyCapsule\_Destructor, using the correct deallocator for buff \*/
void free\_wrap(void \*capsule){
    void \* obj \= PyCapsule\_GetPointer(capsule, PyCapsule\_GetName(capsule));
    free(obj);
};

/\* then inside the function that creates arr from buff \*/
...
arr \= PyArray\_NewFromDescr(... buf, ...);
if (arr \== NULL) {
    return NULL;
}
capsule \= PyCapsule\_New(buf, "my\_wrapped\_buffer",
                        (PyCapsule\_Destructor)&free\_wrap);
if (PyArray\_SetBaseObject(arr, capsule) \== \-1) {
    Py\_DECREF(arr);
    return NULL;
}
...

Copy to clipboard

Example of memory tracing with `np.lib.tracemalloc_domain`[#](https://numpy.org/doc/stable/reference/c-api/data_memory.html#example-of-memory-tracing-with-np-lib-tracemalloc-domain "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The builtin `tracemalloc` module can be used to track allocations inside NumPy. NumPy places its CPU memory allocations into the `np.lib.tracemalloc_domain` domain. For additional information, check: [https://docs.python.org/3/library/tracemalloc.html](https://docs.python.org/3/library/tracemalloc.html)
.

Here is an example on how to use `np.lib.tracemalloc_domain`:

"""
   The goal of this example is to show how to trace memory
   from an application that has NumPy and non-NumPy sections.
   We only select the sections using NumPy related calls.
"""

import tracemalloc
import numpy as np

\# Flag to determine if we select NumPy domain
use\_np\_domain \= True

nx \= 300
ny \= 500

\# Start to trace memory
tracemalloc.start()

\# Section 1
\# ---------

\# NumPy related call
a \= np.zeros((nx,ny))

\# non-NumPy related call
b \= \[i\*\*2 for i in range(nx\*ny)\]

snapshot1 \= tracemalloc.take\_snapshot()
\# We filter the snapshot to only select NumPy related calls
np\_domain \= np.lib.tracemalloc\_domain
dom\_filter \= tracemalloc.DomainFilter(inclusive\=use\_np\_domain,
                                      domain\=np\_domain)
snapshot1 \= snapshot1.filter\_traces(\[dom\_filter\])
top\_stats1 \= snapshot1.statistics('traceback')

print("================ SNAPSHOT 1 =================")
for stat in top\_stats1:
    print(f"{stat.count} memory blocks: {stat.size / 1024:.1f} KiB")
    print(stat.traceback.format()\[\-1\])

\# Clear traces of memory blocks allocated by Python
\# before moving to the next section.
tracemalloc.clear\_traces()

\# Section 2
#----------

\# We are only using NumPy
c \= np.sum(a\*a)

snapshot2 \= tracemalloc.take\_snapshot()
top\_stats2 \= snapshot2.statistics('traceback')

print()
print("================ SNAPSHOT 2 =================")
for stat in top\_stats2:
    print(f"{stat.count} memory blocks: {stat.size / 1024:.1f} KiB")
    print(stat.traceback.format()\[\-1\])

tracemalloc.stop()

print()
print("============================================")
print("\\nTracing Status : ", tracemalloc.is\_tracing())

try:
    print("\\nTrying to Take Snapshot After Tracing is Stopped.")
    snap \= tracemalloc.take\_snapshot()
except Exception as e:
    print("Exception : ", e)

Copy to clipboard

On this page