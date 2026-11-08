### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/abi3t-migration.html "Migrating to Stable ABI for free threading (abi3t)")
     |
*   [previous](https://docs.python.org/3/howto/free-threading-python.html "Python support for free threading")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [C API Extension Support for Free Threading](https://docs.python.org/3/howto/free-threading-extensions.html)
    
*    
    
    |
*   Theme Auto Light Dark |

C API Extension Support for Free Threading[¶](https://docs.python.org/3/howto/free-threading-extensions.html#c-api-extension-support-for-free-threading "Link to this heading")

================================================================================================================================================================================

Starting with the 3.13 release, CPython has support for running with the [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
 (GIL) disabled in a configuration called [free threading](https://docs.python.org/3/glossary.html#term-free-threading)
. This document describes how to adapt C API extensions to support free threading.

Identifying the Free-Threaded Build in C[¶](https://docs.python.org/3/howto/free-threading-extensions.html#identifying-the-free-threaded-build-in-c "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The CPython C API exposes the `Py_GIL_DISABLED` macro: in the free-threaded build it’s defined to `1`, and in the regular build it’s not defined. You can use it to enable code that only runs under the free-threaded build:

#ifdef Py\_GIL\_DISABLED
/\* code that only runs in the free-threaded build \*/
#endif

Note

On Windows, this macro is not defined automatically, but must be specified to the compiler when building. The [`sysconfig.get_config_var()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_config_var "sysconfig.get_config_var")
 function can be used to determine whether the current running interpreter had the macro defined.

Module Initialization[¶](https://docs.python.org/3/howto/free-threading-extensions.html#module-initialization "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Extension modules need to explicitly indicate that they support running with the GIL disabled; otherwise importing the extension will raise a warning and enable the GIL at runtime.

There are two ways to indicate that an extension module supports running with the GIL disabled depending on whether the extension uses multi-phase or single-phase initialization.

### Multi-Phase Initialization[¶](https://docs.python.org/3/howto/free-threading-extensions.html#multi-phase-initialization "Link to this heading")

Extensions that use [multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
 (functions like [`PyModuleDef_Init()`](https://docs.python.org/3/c-api/extension-modules.html#c.PyModuleDef_Init "PyModuleDef_Init")
, [`PyModExport_*`](https://docs.python.org/3/c-api/extension-modules.html#c.PyModExport_modulename "PyModExport_modulename")
 export hook, [`PyModule_FromSlotsAndSpec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromSlotsAndSpec "PyModule_FromSlotsAndSpec")
) should add a [`Py_mod_gil`](https://docs.python.org/3/c-api/module.html#c.Py_mod_gil "Py_mod_gil")
 slot in the module definition. If your extension supports older versions of CPython, you should guard the slot with a [`PY_VERSION_HEX`](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_VERSION_HEX "PY_VERSION_HEX")
 check.

static struct PyModuleDef\_Slot module\_slots\[\] \= {
    ...
#if PY\_VERSION\_HEX >= 0x030D0000
    {Py\_mod\_gil, Py\_MOD\_GIL\_NOT\_USED},
#endif
    {0, NULL}
};

### Single-Phase Initialization[¶](https://docs.python.org/3/howto/free-threading-extensions.html#single-phase-initialization "Link to this heading")

Extensions that use legacy [single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#single-phase-initialization)
 (that is, [`PyModule_Create()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Create "PyModule_Create")
) should call [`PyUnstable_Module_SetGIL()`](https://docs.python.org/3/c-api/module.html#c.PyUnstable_Module_SetGIL "PyUnstable_Module_SetGIL")
 to indicate that they support running with the GIL disabled. The function is only defined in the free-threaded build, so you should guard the call with `#ifdef Py_GIL_DISABLED` to avoid compilation errors in the regular build.

static struct PyModuleDef moduledef \= {
    PyModuleDef\_HEAD\_INIT,
    ...
};

PyMODINIT\_FUNC
PyInit\_mymodule(void)
{
    PyObject \*m \= PyModule\_Create(&moduledef);
    if (m \== NULL) {
        return NULL;
    }
#ifdef Py\_GIL\_DISABLED
    PyUnstable\_Module\_SetGIL(m, Py\_MOD\_GIL\_NOT\_USED);
#endif
    return m;
}

General API Guidelines[¶](https://docs.python.org/3/howto/free-threading-extensions.html#general-api-guidelines "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

Most of the C API is thread-safe, but there are some exceptions.

*   **Struct Fields**: Accessing fields in Python C API objects or structs directly is not thread-safe if the field may be concurrently modified.
    
*   **Macros**: Accessor macros like [`PyList_GET_ITEM`](https://docs.python.org/3/c-api/list.html#c.PyList_GET_ITEM "PyList_GET_ITEM")
    , [`PyList_SET_ITEM`](https://docs.python.org/3/c-api/list.html#c.PyList_SET_ITEM "PyList_SET_ITEM")
    , and macros like [`PySequence_Fast_GET_SIZE`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast_GET_SIZE "PySequence_Fast_GET_SIZE")
     that use the object returned by [`PySequence_Fast()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Fast "PySequence_Fast")
     do not perform any error checking or locking. These macros are not thread-safe if the container object may be modified concurrently.
    
*   **Borrowed References**: C API functions that return [borrowed references](https://docs.python.org/3/glossary.html#term-borrowed-reference)
     may not be thread-safe if the containing object is modified concurrently. See the section on [borrowed references](https://docs.python.org/3/howto/free-threading-extensions.html#id2)
     for more information.
    

### Container Thread Safety[¶](https://docs.python.org/3/howto/free-threading-extensions.html#container-thread-safety "Link to this heading")

Containers like [`PyListObject`](https://docs.python.org/3/c-api/list.html#c.PyListObject "PyListObject")
, [`PyDictObject`](https://docs.python.org/3/c-api/dict.html#c.PyDictObject "PyDictObject")
, and [`PySetObject`](https://docs.python.org/3/c-api/set.html#c.PySetObject "PySetObject")
 perform internal locking in the free-threaded build. For example, the [`PyList_Append()`](https://docs.python.org/3/c-api/list.html#c.PyList_Append "PyList_Append")
 will lock the list before appending an item.

#### `PyDict_Next`[¶](https://docs.python.org/3/howto/free-threading-extensions.html#pydict-next "Link to this heading")

A notable exception is [`PyDict_Next()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Next "PyDict_Next")
, which does not lock the dictionary. You should use [`Py_BEGIN_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION "Py_BEGIN_CRITICAL_SECTION")
 to protect the dictionary while iterating over it if the dictionary may be concurrently modified:

Py\_BEGIN\_CRITICAL\_SECTION(dict);
PyObject \*key, \*value;
Py\_ssize\_t pos \= 0;
while (PyDict\_Next(dict, &pos, &key, &value)) {
    ...
}
Py\_END\_CRITICAL\_SECTION();

Borrowed References[¶](https://docs.python.org/3/howto/free-threading-extensions.html#borrowed-references "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Some C API functions return [borrowed references](https://docs.python.org/3/glossary.html#term-borrowed-reference)
. These APIs are not thread-safe if the containing object is modified concurrently. For example, it’s not safe to use [`PyList_GetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem "PyList_GetItem")
 if the list may be modified concurrently.

The following table lists some borrowed reference APIs and their replacements that return [strong references](https://docs.python.org/3/glossary.html#term-strong-reference)
.

| Borrowed reference API | Strong reference API |
| --- | --- |
| [`PyList_GetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem "PyList_GetItem") | [`PyList_GetItemRef()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItemRef "PyList_GetItemRef") |
| [`PyList_GET_ITEM()`](https://docs.python.org/3/c-api/list.html#c.PyList_GET_ITEM "PyList_GET_ITEM") | [`PyList_GetItemRef()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItemRef "PyList_GetItemRef") |
| [`PyDict_GetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem "PyDict_GetItem") | [`PyDict_GetItemRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemRef "PyDict_GetItemRef") |
| [`PyDict_GetItemWithError()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemWithError "PyDict_GetItemWithError") | [`PyDict_GetItemRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemRef "PyDict_GetItemRef") |
| [`PyDict_GetItemString()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemString "PyDict_GetItemString") | [`PyDict_GetItemStringRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItemStringRef "PyDict_GetItemStringRef") |
| [`PyDict_SetDefault()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetDefault "PyDict_SetDefault") | [`PyDict_SetDefaultRef()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetDefaultRef "PyDict_SetDefaultRef") |
| [`PyDict_Next()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Next "PyDict_Next") | none (see [PyDict\_Next](https://docs.python.org/3/howto/free-threading-extensions.html#pydict-next)<br>) |
| `PyWeakref_GetObject()` | [`PyWeakref_GetRef()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef") |
| `PyWeakref_GET_OBJECT()` | [`PyWeakref_GetRef()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef") |
| [`PyImport_AddModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModule "PyImport_AddModule") | [`PyImport_AddModuleRef()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModuleRef "PyImport_AddModuleRef") |
| [`PyCell_GET()`](https://docs.python.org/3/c-api/cell.html#c.PyCell_GET "PyCell_GET") | [`PyCell_Get()`](https://docs.python.org/3/c-api/cell.html#c.PyCell_Get "PyCell_Get") |

Not all APIs that return borrowed references are problematic. For example, [`PyTuple_GetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_GetItem "PyTuple_GetItem")
 is safe because tuples are immutable. Similarly, not all uses of the above APIs are problematic. For example, [`PyDict_GetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem "PyDict_GetItem")
 is often used for parsing keyword argument dictionaries in function calls; those keyword argument dictionaries are effectively private (not accessible by other threads), so using borrowed references in that context is safe.

Some of these functions were added in Python 3.13. You can use the [pythoncapi-compat](https://github.com/python/pythoncapi-compat)
 package to provide implementations of these functions for older Python versions.

Memory Allocation APIs[¶](https://docs.python.org/3/howto/free-threading-extensions.html#memory-allocation-apis "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

Python’s memory management C API provides functions in three different [allocation domains](https://docs.python.org/3/c-api/memory.html#id1)
: “raw”, “mem”, and “object”. For thread-safety, the free-threaded build requires that only Python objects are allocated using the object domain, and that all Python objects are allocated using that domain. This differs from the prior Python versions, where this was only a best practice and not a hard requirement.

Note

Search for uses of [`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc")
 in your extension and check that the allocated memory is used for Python objects. Use [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
 to allocate buffers instead of `PyObject_Malloc()`.

Thread State and GIL APIs[¶](https://docs.python.org/3/howto/free-threading-extensions.html#thread-state-and-gil-apis "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

Python provides a set of functions and macros to manage thread state and the GIL, such as:

*   [`PyThreadState_Ensure()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_Ensure "PyThreadState_Ensure")
    , [`PyThreadState_EnsureFromView()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_EnsureFromView "PyThreadState_EnsureFromView")
    , and [`PyThreadState_Release()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_Release "PyThreadState_Release")
    
*   [`PyGILState_Ensure()`](https://docs.python.org/3/c-api/threads.html#c.PyGILState_Ensure "PyGILState_Ensure")
     and [`PyGILState_Release()`](https://docs.python.org/3/c-api/threads.html#c.PyGILState_Release "PyGILState_Release")
    
*   [`PyEval_SaveThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_SaveThread "PyEval_SaveThread")
     and [`PyEval_RestoreThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_RestoreThread "PyEval_RestoreThread")
    
*   [`Py_BEGIN_ALLOW_THREADS`](https://docs.python.org/3/c-api/threads.html#c.Py_BEGIN_ALLOW_THREADS "Py_BEGIN_ALLOW_THREADS")
     and [`Py_END_ALLOW_THREADS`](https://docs.python.org/3/c-api/threads.html#c.Py_END_ALLOW_THREADS "Py_END_ALLOW_THREADS")
    

These functions should still be used in the free-threaded build to manage thread state even when the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
 is disabled. For example, if you create a thread outside of Python, you must call [`PyThreadState_Ensure()`](https://docs.python.org/3/c-api/threads.html#c.PyThreadState_Ensure "PyThreadState_Ensure")
 before calling into the Python API to ensure that the thread has a valid Python thread state.

You should continue to call [`PyEval_SaveThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_SaveThread "PyEval_SaveThread")
 or [`Py_BEGIN_ALLOW_THREADS`](https://docs.python.org/3/c-api/threads.html#c.Py_BEGIN_ALLOW_THREADS "Py_BEGIN_ALLOW_THREADS")
 around blocking operations, such as I/O or lock acquisitions, to allow other threads to run the [cyclic garbage collector](https://docs.python.org/3/glossary.html#term-garbage-collection)
.

Protecting Internal Extension State[¶](https://docs.python.org/3/howto/free-threading-extensions.html#protecting-internal-extension-state "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Your extension may have internal state that was previously protected by the GIL. You may need to add locking to protect this state. The approach will depend on your extension, but some common patterns include:

*   **Caches**: global caches are a common source of shared state. Consider using a lock to protect the cache or disabling it in the free-threaded build if the cache is not critical for performance.
    
*   **Global State**: global state may need to be protected by a lock or moved to thread local storage. C11 and C++11 provide the `thread_local` or `_Thread_local` for [thread-local storage](https://en.cppreference.com/w/c/language/storage_duration)
    .
    

Critical Sections[¶](https://docs.python.org/3/howto/free-threading-extensions.html#critical-sections "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

In the free-threaded build, CPython provides a mechanism called “critical sections” to protect data that would otherwise be protected by the GIL. While extension authors may not interact with the internal critical section implementation directly, understanding their behavior is crucial when using certain C API functions or managing shared state in the free-threaded build.

### What Are Critical Sections?[¶](https://docs.python.org/3/howto/free-threading-extensions.html#what-are-critical-sections "Link to this heading")

Conceptually, critical sections act as a deadlock avoidance layer built on top of simple mutexes. Each thread maintains a stack of active critical sections. When a thread needs to acquire a lock associated with a critical section (e.g., implicitly when calling a thread-safe C API function like [`PyDict_SetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_SetItem "PyDict_SetItem")
, or explicitly using macros), it attempts to acquire the underlying mutex.

### Using Critical Sections[¶](https://docs.python.org/3/howto/free-threading-extensions.html#using-critical-sections "Link to this heading")

The primary APIs for using critical sections are:

*   [`Py_BEGIN_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION "Py_BEGIN_CRITICAL_SECTION")
     and [`Py_END_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_END_CRITICAL_SECTION "Py_END_CRITICAL_SECTION")
     - For locking a single object
    
*   [`Py_BEGIN_CRITICAL_SECTION2`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2 "Py_BEGIN_CRITICAL_SECTION2")
     and [`Py_END_CRITICAL_SECTION2`](https://docs.python.org/3/c-api/synchronization.html#c.Py_END_CRITICAL_SECTION2 "Py_END_CRITICAL_SECTION2")
     - For locking two objects simultaneously
    

These macros must be used in matching pairs and must appear in the same C scope, since they establish a new local scope. These macros are no-ops in non-free-threaded builds, so they can be safely added to code that needs to support both build types.

A common use of a critical section would be to lock an object while accessing an internal attribute of it. For example, if an extension type has an internal count field, you could use a critical section while reading or writing that field:

// read the count, returns new reference to internal count value
PyObject \*result;
Py\_BEGIN\_CRITICAL\_SECTION(obj);
result \= Py\_NewRef(obj\->count);
Py\_END\_CRITICAL\_SECTION();
return result;

// write the count, consumes reference from new\_count
Py\_BEGIN\_CRITICAL\_SECTION(obj);
obj\->count \= new\_count;
Py\_END\_CRITICAL\_SECTION();

### How Critical Sections Work[¶](https://docs.python.org/3/howto/free-threading-extensions.html#how-critical-sections-work "Link to this heading")

Unlike traditional locks, critical sections do not guarantee exclusive access throughout their entire duration. If a thread would block while holding a critical section (e.g., by acquiring another lock or performing I/O), the critical section is temporarily suspended—all locks are released—and then resumed when the blocking operation completes.

This behavior is similar to what happens with the GIL when a thread makes a blocking call. The key differences are:

*   Critical sections operate on a per-object basis rather than globally
    
*   Critical sections follow a stack discipline within each thread (the “begin” and “end” macros enforce this since they must be paired and within the same scope)
    
*   Critical sections automatically release and reacquire locks around potential blocking operations
    

### Deadlock Avoidance[¶](https://docs.python.org/3/howto/free-threading-extensions.html#deadlock-avoidance "Link to this heading")

Critical sections help avoid deadlocks in two ways:

1.  If a thread tries to acquire a lock that’s already held by another thread, it first suspends all of its active critical sections, temporarily releasing their locks
    
2.  When the blocking operation completes, only the top-most critical section is reacquired first
    

This means you cannot rely on nested critical sections to lock multiple objects at once, as the inner critical section may suspend the outer ones. Instead, use [`Py_BEGIN_CRITICAL_SECTION2`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2 "Py_BEGIN_CRITICAL_SECTION2")
 to lock two objects simultaneously.

Note that the locks described above are only [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 based locks. The critical section implementation does not know about or affect other locking mechanisms that might be in use, like POSIX mutexes. Also note that while blocking on any `PyMutex` causes the critical sections to be suspended, only the mutexes that are part of the critical sections are released. If `PyMutex` is used without a critical section, it will not be released and therefore does not get the same deadlock avoidance.

### Important Considerations[¶](https://docs.python.org/3/howto/free-threading-extensions.html#important-considerations "Link to this heading")

*   Critical sections may temporarily release their locks, allowing other threads to modify the protected data. Be careful about making assumptions about the state of the data after operations that might block.
    
*   Because locks can be temporarily released (suspended), entering a critical section does not guarantee exclusive access to the protected resource throughout the section’s duration. If code within a critical section calls another function that blocks (e.g., acquires another lock, performs blocking I/O), all locks held by the thread via critical sections will be released. This is similar to how the GIL can be released during blocking calls.
    
*   Only the lock(s) associated with the most recently entered (top-most) critical section are guaranteed to be held at any given time. Locks for outer, nested critical sections might have been suspended.
    
*   You can lock at most two objects simultaneously with these APIs. If you need to lock more objects, you’ll need to restructure your code.
    
*   While critical sections will not deadlock if you attempt to lock the same object twice, they are less efficient than purpose-built reentrant locks for this use case.
    
*   When using [`Py_BEGIN_CRITICAL_SECTION2`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2 "Py_BEGIN_CRITICAL_SECTION2")
    , the order of the objects doesn’t affect correctness (the implementation handles deadlock avoidance), but it’s good practice to always lock objects in a consistent order.
    
*   Remember that the critical section macros are primarily for protecting access to _Python objects_ that might be involved in internal CPython operations susceptible to the deadlock scenarios described above. For protecting purely internal extension state, standard mutexes or other synchronization primitives might be more appropriate.
    

### Per-Object Locks (`ob_mutex`)[¶](https://docs.python.org/3/howto/free-threading-extensions.html#per-object-locks-ob-mutex "Link to this heading")

In the free-threaded build, each Python object contains a [`ob_mutex`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_mutex "PyObject.ob_mutex")
 field of type [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
. This mutex is **reserved for use by the critical section API** ([`Py_BEGIN_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION "Py_BEGIN_CRITICAL_SECTION")
 / [`Py_END_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_END_CRITICAL_SECTION "Py_END_CRITICAL_SECTION")
).

Warning

Do **not** lock `ob_mutex` directly with `PyMutex_Lock(&obj->ob_mutex)`. Mixing direct `PyMutex_Lock` calls with the critical section API on the same mutex can cause deadlocks.

Even if your own code never uses critical sections on a particular object type, **CPython internals may use the critical section API on any Python object**.

If your extension type needs its own lock, add a separate [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 field (or another synchronization primitive) to your object struct. `PyMutex` is very lightweight, so there is negligible cost to having an additional one.

Building Extensions for the Free-Threaded Build[¶](https://docs.python.org/3/howto/free-threading-extensions.html#building-extensions-for-the-free-threaded-build "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

C API extensions need to be built specifically for the free-threaded build. The wheels, shared libraries, and binaries are indicated by a `t` suffix.

*   [pypa/manylinux](https://github.com/pypa/manylinux)
     supports the free-threaded build, with the `t` suffix, such as `python3.14t`.
    
*   [pypa/cibuildwheel](https://github.com/pypa/cibuildwheel)
     supports building wheels for the free-threaded build of Python 3.14 and newer.
    

### Limited C API and Stable ABI[¶](https://docs.python.org/3/howto/free-threading-extensions.html#limited-c-api-and-stable-abi "Link to this heading")

The free-threaded build does not currently support the [Limited C API](https://docs.python.org/3/c-api/stable.html#limited-c-api)
 or the stable ABI. If you use [setuptools](https://setuptools.pypa.io/en/latest/setuptools.html)
 to build your extension and currently set `py_limited_api=True` you can use `py_limited_api=not sysconfig.get_config_var("Py_GIL_DISABLED")` to opt out of the limited API when building with the free-threaded build.

Note

You will need to build separate wheels specifically for the free-threaded build. If you currently use the stable ABI, you can continue to build a single wheel for multiple non-free-threaded Python versions.

### Windows[¶](https://docs.python.org/3/howto/free-threading-extensions.html#windows "Link to this heading")

Due to a limitation of the official Windows installer, you will need to manually define `Py_GIL_DISABLED=1` when building extensions from source.

See also

[Porting Extension Modules to Support Free-Threading](https://py-free-threading.github.io/porting/)
: A community-maintained porting guide for extension authors.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [C API Extension Support for Free Threading](https://docs.python.org/3/howto/free-threading-extensions.html#)
    *   [Identifying the Free-Threaded Build in C](https://docs.python.org/3/howto/free-threading-extensions.html#identifying-the-free-threaded-build-in-c)
        
    *   [Module Initialization](https://docs.python.org/3/howto/free-threading-extensions.html#module-initialization)
        *   [Multi-Phase Initialization](https://docs.python.org/3/howto/free-threading-extensions.html#multi-phase-initialization)
            
        *   [Single-Phase Initialization](https://docs.python.org/3/howto/free-threading-extensions.html#single-phase-initialization)
            
    *   [General API Guidelines](https://docs.python.org/3/howto/free-threading-extensions.html#general-api-guidelines)
        *   [Container Thread Safety](https://docs.python.org/3/howto/free-threading-extensions.html#container-thread-safety)
            *   [`PyDict_Next`](https://docs.python.org/3/howto/free-threading-extensions.html#pydict-next)
                
    *   [Borrowed References](https://docs.python.org/3/howto/free-threading-extensions.html#borrowed-references)
        
    *   [Memory Allocation APIs](https://docs.python.org/3/howto/free-threading-extensions.html#memory-allocation-apis)
        
    *   [Thread State and GIL APIs](https://docs.python.org/3/howto/free-threading-extensions.html#thread-state-and-gil-apis)
        
    *   [Protecting Internal Extension State](https://docs.python.org/3/howto/free-threading-extensions.html#protecting-internal-extension-state)
        
    *   [Critical Sections](https://docs.python.org/3/howto/free-threading-extensions.html#critical-sections)
        *   [What Are Critical Sections?](https://docs.python.org/3/howto/free-threading-extensions.html#what-are-critical-sections)
            
        *   [Using Critical Sections](https://docs.python.org/3/howto/free-threading-extensions.html#using-critical-sections)
            
        *   [How Critical Sections Work](https://docs.python.org/3/howto/free-threading-extensions.html#how-critical-sections-work)
            
        *   [Deadlock Avoidance](https://docs.python.org/3/howto/free-threading-extensions.html#deadlock-avoidance)
            
        *   [Important Considerations](https://docs.python.org/3/howto/free-threading-extensions.html#important-considerations)
            
        *   [Per-Object Locks (`ob_mutex`)](https://docs.python.org/3/howto/free-threading-extensions.html#per-object-locks-ob-mutex)
            
    *   [Building Extensions for the Free-Threaded Build](https://docs.python.org/3/howto/free-threading-extensions.html#building-extensions-for-the-free-threaded-build)
        *   [Limited C API and Stable ABI](https://docs.python.org/3/howto/free-threading-extensions.html#limited-c-api-and-stable-abi)
            
        *   [Windows](https://docs.python.org/3/howto/free-threading-extensions.html#windows)
            

#### Previous topic

[Python support for free threading](https://docs.python.org/3/howto/free-threading-python.html "previous chapter")

#### Next topic

[Migrating to Stable ABI for free threading (`abi3t`)](https://docs.python.org/3/howto/abi3t-migration.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=C+API+Extension+Support+for+Free+Threading&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fhowto%2Ffree-threading-extensions.html&pagesource=howto%2Ffree-threading-extensions.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/howto/free-threading-extensions.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/abi3t-migration.html "Migrating to Stable ABI for free threading (abi3t)")
     |
*   [previous](https://docs.python.org/3/howto/free-threading-python.html "Python support for free threading")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [C API Extension Support for Free Threading](https://docs.python.org/3/howto/free-threading-extensions.html)
    
*    
    
    |
*   Theme Auto Light Dark |