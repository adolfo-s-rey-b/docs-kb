### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/tls.html "Thread-local storage support")
     |
*   [previous](https://docs.python.org/3/c-api/threads.html "Thread states and the global interpreter lock")
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
*   [Synchronization primitives](https://docs.python.org/3/c-api/synchronization.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Synchronization primitives[¶](https://docs.python.org/3/c-api/synchronization.html#synchronization-primitives "Link to this heading")

======================================================================================================================================

The C-API provides a basic mutual exclusion lock.

type PyMutex[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "Link to this definition")
  

A mutual exclusion lock. The `PyMutex` should be initialized to zero to represent the unlocked state. For example:

PyMutex mutex \= {0};

Instances of `PyMutex` should not be copied or moved. Both the contents and address of a `PyMutex` are meaningful, and it must remain at a fixed, writable location in memory.

Note

A `PyMutex` currently occupies one byte, but the size should be considered unstable. The size may change in future Python releases without a deprecation period.

Added in version 3.13.

void PyMutex\_Lock([PyMutex](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 \*m)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex_Lock "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Lock mutex _m_. If another thread has already locked it, the calling thread will block until the mutex is unlocked. While blocked, the thread will temporarily detach the [thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 if one exists.

Added in version 3.13.

void PyMutex\_Unlock([PyMutex](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 \*m)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex_Unlock "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Unlock mutex _m_. The mutex must be locked — otherwise, the function will issue a fatal error.

Added in version 3.13.

int PyMutex\_IsLocked([PyMutex](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 \*m)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex_IsLocked "Link to this definition")
  

_Thread safety: [Atomic](https://docs.python.org/3/builtins/threadsafety.html#threadsafety-level-atomic)
._

Returns non-zero if the mutex _m_ is currently locked, zero otherwise.

Note

This function is intended for use in assertions and debugging only and should not be used to make concurrency control decisions, as the lock state may change immediately after the check.

Added in version 3.14.

Python critical section API[¶](https://docs.python.org/3/c-api/synchronization.html#python-critical-section-api "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

The critical section API provides a deadlock avoidance layer on top of per-object locks for [free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 CPython. They are intended to replace reliance on the [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)
, and are no-ops in versions of Python with the global interpreter lock.

Critical sections are intended to be used for custom types implemented in C-API extensions. They should generally not be used with built-in types like [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 and [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 because their public C-APIs already use critical sections internally, with the notable exception of [`PyDict_Next()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Next "PyDict_Next")
, which requires critical section to be acquired externally.

Critical sections avoid deadlocks by implicitly suspending active critical sections, hence, they do not provide exclusive access such as provided by traditional locks like [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
. When a critical section is started, the per-object lock for the object is acquired. If the code executed inside the critical section calls C-API functions then it can suspend the critical section thereby releasing the per-object lock, so other threads can acquire the per-object lock for the same object.

Variants that accept [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 pointers rather than Python objects are also available. Use these variants to start a critical section in a situation where there is no [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 – for example, when working with a C type that does not extend or wrap `PyObject` but still needs to call into the C API in a manner that might lead to deadlocks.

Note

Operations that need to lock two objects at once must use [`Py_BEGIN_CRITICAL_SECTION2`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2 "Py_BEGIN_CRITICAL_SECTION2")
. You _cannot_ use nested critical sections to lock more than one object at once, because the inner critical section may suspend the outer critical sections. This API does not provide a way to lock more than two objects at once.

Example usage:

static PyObject \*
set\_field(MyObject \*self, PyObject \*value)
{
   Py\_BEGIN\_CRITICAL\_SECTION(self);
   Py\_SETREF(self\->field, Py\_XNewRef(value));
   Py\_END\_CRITICAL\_SECTION();
   Py\_RETURN\_NONE;
}

In the above example, [`Py_SETREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_SETREF "Py_SETREF")
 calls [`Py_DECREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")
, which can call arbitrary code through an object’s deallocation function. The critical section API avoids potential deadlocks due to reentrancy and lock ordering by allowing the runtime to temporarily suspend the critical section if the code triggered by the finalizer blocks and calls [`PyEval_SaveThread()`](https://docs.python.org/3/c-api/threads.html#c.PyEval_SaveThread "PyEval_SaveThread")
.

Py\_BEGIN\_CRITICAL\_SECTION(op)[¶](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Acquires the per-object lock for the object _op_ and begins a critical section.

In the free-threaded build, and when building for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable-abi)
, this macro expands to:

{
    PyCriticalSection \_py\_cs;
    PyCriticalSection\_Begin(&\_py\_cs, (PyObject\*)(op))

In the default build, this macro expands to `{`.

Added in version 3.13.

Py\_BEGIN\_CRITICAL\_SECTION\_MUTEX(m)[¶](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION_MUTEX "Link to this definition")
  

Locks the mutex _m_ and begins a critical section.

In the free-threaded build, this macro expands to:

{
     PyCriticalSection \_py\_cs;
     PyCriticalSection\_BeginMutex(&\_py\_cs, m)

Note that unlike [`Py_BEGIN_CRITICAL_SECTION`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION "Py_BEGIN_CRITICAL_SECTION")
, there is no cast for the argument of the macro - it must be a [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 pointer.

On the default build, this macro expands to `{`.

Added in version 3.14.

Py\_END\_CRITICAL\_SECTION()[¶](https://docs.python.org/3/c-api/synchronization.html#c.Py_END_CRITICAL_SECTION "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Ends the critical section and releases the per-object lock.

In the free-threaded build, and when building for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable-abi)
, this macro expands to:

    PyCriticalSection\_End(&\_py\_cs);
}

In the default build, this macro expands to `}`.

Added in version 3.13.

Py\_BEGIN\_CRITICAL\_SECTION2(a, b)[¶](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2 "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Acquires the per-object locks for the objects _a_ and _b_ and begins a critical section. The locks are acquired in a consistent order (lowest address first) to avoid lock ordering deadlocks.

In the free-threaded build, this macro expands to:

{
    PyCriticalSection2 \_py\_cs2;
    PyCriticalSection2\_Begin(&\_py\_cs2, (PyObject\*)(a), (PyObject\*)(b))

In the default build, this macro expands to `{`.

Added in version 3.13.

Py\_BEGIN\_CRITICAL\_SECTION2\_MUTEX(m1, m2)[¶](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2_MUTEX "Link to this definition")
  

Locks the mutexes _m1_ and _m2_ and begins a critical section.

In the free-threaded build, and when building for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable-abi)
, this macro expands to:

{
     PyCriticalSection2 \_py\_cs2;
     PyCriticalSection2\_BeginMutex(&\_py\_cs2, m1, m2)

Note that unlike [`Py_BEGIN_CRITICAL_SECTION2`](https://docs.python.org/3/c-api/synchronization.html#c.Py_BEGIN_CRITICAL_SECTION2 "Py_BEGIN_CRITICAL_SECTION2")
, there is no cast for the arguments of the macro - they must be [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 pointers.

On the default build, this macro expands to `{`.

Added in version 3.14.

Py\_END\_CRITICAL\_SECTION2()[¶](https://docs.python.org/3/c-api/synchronization.html#c.Py_END_CRITICAL_SECTION2 "Link to this definition")
  

_This macro is available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Ends the critical section and releases the per-object locks.

In the free-threaded build, and when building for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable-abi)
, this macro expands to:

    PyCriticalSection2\_End(&\_py\_cs2);
}

In the default build, this macro expands to `}`.

Added in version 3.13.

### Low-level critical section API[¶](https://docs.python.org/3/c-api/synchronization.html#low-level-critical-section-api "Link to this heading")

The following functions and structs are exposed for cases where C macros are not available.

void PyCriticalSection\_Begin([PyCriticalSection](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection "PyCriticalSection")
 \*c, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection_Begin "Link to this definition")
  

void PyCriticalSection\_End([PyCriticalSection](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection "PyCriticalSection")
 \*c)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection_End "Link to this definition")
  

void PyCriticalSection2\_Begin([PyCriticalSection2](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection2 "PyCriticalSection2")
 \*c, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*a, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*b)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection2_Begin "Link to this definition")
  

void PyCriticalSection2\_End([PyCriticalSection2](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection2 "PyCriticalSection2")
 \*c);[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection2_End "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

To be used only as in the macro expansions listed [earlier in this section](https://docs.python.org/3/c-api/synchronization.html#critical-section-macros)
.

In non-[free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 builds of CPython, these functions do nothing.

Added in version 3.13.

type PyCriticalSection[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection "Link to this definition")
  

type PyCriticalSection2[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection2 "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members) since version 3.15._

To be used only as in the macro expansions listed [earlier in this section](https://docs.python.org/3/c-api/synchronization.html#critical-section-macros)
. Note that the contents of the structures are private and their meaning may change in future Python versions.

Added in version 3.13.

void PyCriticalSection\_BeginMutex([PyCriticalSection](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection "PyCriticalSection")
 \*c, [PyMutex](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 \*m);[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection_BeginMutex "Link to this definition")
  

void PyCriticalSection2\_BeginMutex([PyCriticalSection2](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection2 "PyCriticalSection2")
 \*c, [PyMutex](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 \*m1, [PyMutex](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
 \*m2);[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection2_BeginMutex "Link to this definition")
  

To be used only as in the macro expansions listed [earlier in this section](https://docs.python.org/3/c-api/synchronization.html#critical-section-macros)
.

In non-[free-threaded](https://docs.python.org/3/glossary.html#term-free-threading)
 builds of CPython, these functions do nothing.

Added in version 3.14.

Legacy locking APIs[¶](https://docs.python.org/3/c-api/synchronization.html#legacy-locking-apis "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

These APIs are obsolete since Python 3.13 with the introduction of [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
.

Changed in version 3.15: These APIs are now a simple wrapper around `PyMutex`.

type PyThread\_type\_lock[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_type_lock "Link to this definition")
  

A pointer to a mutual exclusion lock.

PY\_TIMEOUT\_T[¶](https://docs.python.org/3/c-api/synchronization.html#c.PY_TIMEOUT_T "Link to this definition")
  

A [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 alias to long long, the integer type used for the timeout argument of [`PyThread_acquire_lock_timed()`](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_acquire_lock_timed "PyThread_acquire_lock_timed")
.

[Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
 since version 3.15.2.

const long long PY\_TIMEOUT\_MAX[¶](https://docs.python.org/3/c-api/synchronization.html#c.PY_TIMEOUT_MAX "Link to this definition")
  

The maximum timeout, in microseconds, supported by [`PyThread_acquire_lock_timed()`](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_acquire_lock_timed "PyThread_acquire_lock_timed")
.

Note

This differs from [`_thread.TIMEOUT_MAX`](https://docs.python.org/3/library/_thread.html#thread.TIMEOUT_MAX "_thread.TIMEOUT_MAX")
, which is expressed in seconds.

type PyLockStatus[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyLockStatus "Link to this definition")
  

The result of acquiring a lock with a timeout.

enumerator PY\_LOCK\_FAILURE[¶](https://docs.python.org/3/c-api/synchronization.html#c.PY_LOCK_FAILURE "Link to this definition")
  

Failed to acquire the lock.

enumerator PY\_LOCK\_ACQUIRED[¶](https://docs.python.org/3/c-api/synchronization.html#c.PY_LOCK_ACQUIRED "Link to this definition")
  

The lock was successfully acquired.

enumerator PY\_LOCK\_INTR[¶](https://docs.python.org/3/c-api/synchronization.html#c.PY_LOCK_INTR "Link to this definition")
  

The lock was interrupted by a signal.

[PyThread\_type\_lock](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_type_lock "PyThread_type_lock")
 PyThread\_allocate\_lock(void)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_allocate_lock "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Allocate a new lock.

On success, this function returns a lock; on failure, this function returns `0` without an exception set.

The caller does not need to hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

Changed in version 3.15: This function now always uses [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")
. In prior versions, this would use a lock provided by the operating system.

void PyThread\_free\_lock([PyThread\_type\_lock](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_type_lock "PyThread_type_lock")
 lock)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_free_lock "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Destroy _lock_. The lock should not be held by any thread when calling this.

The caller does not need to hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

[PyLockStatus](https://docs.python.org/3/c-api/synchronization.html#c.PyLockStatus "PyLockStatus")
 PyThread\_acquire\_lock\_timed([PyThread\_type\_lock](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_type_lock "PyThread_type_lock")
 lock, long long microseconds, int intr\_flag)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_acquire_lock_timed "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Acquire _lock_ with a timeout.

This will wait for _microseconds_ microseconds to acquire the lock. If the timeout expires, this function returns [`PY_LOCK_FAILURE`](https://docs.python.org/3/c-api/synchronization.html#c.PY_LOCK_FAILURE "PY_LOCK_FAILURE")
. If _microseconds_ is `-1`, this will wait indefinitely until the lock has been released.

If _intr\_flag_ is `1`, acquiring the lock may be interrupted by a signal, in which case this function returns [`PY_LOCK_INTR`](https://docs.python.org/3/c-api/synchronization.html#c.PY_LOCK_INTR "PY_LOCK_INTR")
. Upon interruption, it’s generally expected that the caller makes a call to [`Py_MakePendingCalls()`](https://docs.python.org/3/c-api/threads.html#c.Py_MakePendingCalls "Py_MakePendingCalls")
 to propagate an exception to Python code.

If the lock is successfully acquired, this function returns [`PY_LOCK_ACQUIRED`](https://docs.python.org/3/c-api/synchronization.html#c.PY_LOCK_ACQUIRED "PY_LOCK_ACQUIRED")
.

The caller does not need to hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

int PyThread\_acquire\_lock([PyThread\_type\_lock](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_type_lock "PyThread_type_lock")
 lock, int waitflag)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_acquire_lock "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Acquire _lock_.

If _waitflag_ is `1` and another thread currently holds the lock, this function will wait until the lock can be acquired and will always return `1`.

If _waitflag_ is `0` and another thread holds the lock, this function will not wait and instead return `0`. If the lock is not held by any other thread, then this function will acquire it and return `1`.

Unlike [`PyThread_acquire_lock_timed()`](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_acquire_lock_timed "PyThread_acquire_lock_timed")
, acquiring the lock cannot be interrupted by a signal.

The caller does not need to hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

int PyThread\_release\_lock([PyThread\_type\_lock](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_type_lock "PyThread_type_lock")
 lock)[¶](https://docs.python.org/3/c-api/synchronization.html#c.PyThread_release_lock "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Release _lock_. If _lock_ is not held, then this function issues a fatal error.

The caller does not need to hold an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Synchronization primitives](https://docs.python.org/3/c-api/synchronization.html#)
    *   [Python critical section API](https://docs.python.org/3/c-api/synchronization.html#python-critical-section-api)
        *   [Low-level critical section API](https://docs.python.org/3/c-api/synchronization.html#low-level-critical-section-api)
            
    *   [Legacy locking APIs](https://docs.python.org/3/c-api/synchronization.html#legacy-locking-apis)
        

#### Previous topic

[Thread states and the global interpreter lock](https://docs.python.org/3/c-api/threads.html "previous chapter")

#### Next topic

[Thread-local storage support](https://docs.python.org/3/c-api/tls.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Synchronization+primitives&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fsynchronization.html&pagesource=c-api%2Fsynchronization.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/synchronization.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/tls.html "Thread-local storage support")
     |
*   [previous](https://docs.python.org/3/c-api/threads.html "Thread states and the global interpreter lock")
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
*   [Synchronization primitives](https://docs.python.org/3/c-api/synchronization.html)
    
*    
    
    |
*   Theme Auto Light Dark |