### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/subinterpreters.html "Multiple interpreters in a Python process")
     |
*   [previous](https://docs.python.org/3/c-api/synchronization.html "Synchronization primitives")
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
*   [Thread-local storage support](https://docs.python.org/3/c-api/tls.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Thread-local storage support[¶](https://docs.python.org/3/c-api/tls.html#thread-local-storage-support "Link to this heading")

==============================================================================================================================

The Python interpreter provides low-level support for thread-local storage (TLS) which wraps the underlying native TLS implementation to support the Python-level thread-local storage API ([`threading.local`](https://docs.python.org/3/library/threading.html#threading.local "threading.local")
). The CPython C level APIs are similar to those offered by pthreads and Windows: use a thread key and functions to associate a void\* value per thread.

A [thread state](https://docs.python.org/3/glossary.html#term-thread-state)
 does _not_ need to be [attached](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 when calling these functions; they supply their own locking.

Note that `Python.h` does not include the declaration of the TLS APIs, you need to include `pythread.h` to use thread-local storage.

Note

None of these API functions handle memory management on behalf of the void\* values. You need to allocate and deallocate them yourself. If the void\* values happen to be [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*, these functions don’t do refcount operations on them either.

Thread-specific storage API[¶](https://docs.python.org/3/c-api/tls.html#thread-specific-storage-api "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

The thread-specific storage (TSS) API was introduced to supersede the use of the existing TLS API within the CPython interpreter. This API uses a new type [`Py_tss_t`](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 instead of int to represent thread keys.

Added in version 3.7.

See also

“A New C-API for Thread-Local Storage in CPython” ([**PEP 539**](https://peps.python.org/pep-0539/)
)

type Py\_tss\_t[¶](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Link to this definition")
  

This data structure represents the state of a thread key, the definition of which may depend on the underlying TLS implementation, and it has an internal field representing the key’s initialization state. There are no public members in this structure.

When [Py\_LIMITED\_API](https://docs.python.org/3/c-api/stable.html#stable)
 is not defined, static allocation of this type by [`Py_tss_NEEDS_INIT`](https://docs.python.org/3/c-api/tls.html#c.Py_tss_NEEDS_INIT "Py_tss_NEEDS_INIT")
 is allowed.

Py\_tss\_NEEDS\_INIT[¶](https://docs.python.org/3/c-api/tls.html#c.Py_tss_NEEDS_INIT "Link to this definition")
  

This macro expands to the initializer for [`Py_tss_t`](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 variables. Note that this macro won’t be defined with [Py\_LIMITED\_API](https://docs.python.org/3/c-api/stable.html#stable)
.

Dynamic allocation[¶](https://docs.python.org/3/c-api/tls.html#dynamic-allocation "Link to this heading")

----------------------------------------------------------------------------------------------------------

Dynamic allocation of the [`Py_tss_t`](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
, required in extension modules built with [Py\_LIMITED\_API](https://docs.python.org/3/c-api/stable.html#stable)
, where static allocation of this type is not possible due to its implementation being opaque at build time.

[Py\_tss\_t](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 \*PyThread\_tss\_alloc()[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_alloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return a value which is the same state as a value initialized with [`Py_tss_NEEDS_INIT`](https://docs.python.org/3/c-api/tls.html#c.Py_tss_NEEDS_INIT "Py_tss_NEEDS_INIT")
, or `NULL` in the case of dynamic allocation failure.

void PyThread\_tss\_free([Py\_tss\_t](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 \*key)[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_free "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Free the given _key_ allocated by [`PyThread_tss_alloc()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_alloc "PyThread_tss_alloc")
, after first calling [`PyThread_tss_delete()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_delete "PyThread_tss_delete")
 to ensure any associated thread locals have been unassigned. This is a no-op if the _key_ argument is `NULL`.

Note

A freed key becomes a dangling pointer. You should reset the key to `NULL`.

Methods[¶](https://docs.python.org/3/c-api/tls.html#methods "Link to this heading")

------------------------------------------------------------------------------------

The parameter _key_ of these functions must not be `NULL`. Moreover, the behaviors of [`PyThread_tss_set()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_set "PyThread_tss_set")
 and [`PyThread_tss_get()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_get "PyThread_tss_get")
 are undefined if the given [`Py_tss_t`](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 has not been initialized by [`PyThread_tss_create()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_create "PyThread_tss_create")
.

int PyThread\_tss\_is\_created([Py\_tss\_t](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 \*key)[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_is_created "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return a non-zero value if the given [`Py_tss_t`](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 has been initialized by [`PyThread_tss_create()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_create "PyThread_tss_create")
.

int PyThread\_tss\_create([Py\_tss\_t](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 \*key)[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_create "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return a zero value on successful initialization of a TSS key. The behavior is undefined if the value pointed to by the _key_ argument is not initialized by [`Py_tss_NEEDS_INIT`](https://docs.python.org/3/c-api/tls.html#c.Py_tss_NEEDS_INIT "Py_tss_NEEDS_INIT")
. This function can be called repeatedly on the same key – calling it on an already initialized key is a no-op and immediately returns success.

void PyThread\_tss\_delete([Py\_tss\_t](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 \*key)[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_delete "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Destroy a TSS key to forget the values associated with the key across all threads, and change the key’s initialization state to uninitialized. A destroyed key is able to be initialized again by [`PyThread_tss_create()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_create "PyThread_tss_create")
. This function can be called repeatedly on the same key – calling it on an already destroyed key is a no-op.

int PyThread\_tss\_set([Py\_tss\_t](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 \*key, void \*value)[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_set "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return a zero value to indicate successfully associating a void\* value with a TSS key in the current thread. Each thread has a distinct mapping of the key to a void\* value.

void \*PyThread\_tss\_get([Py\_tss\_t](https://docs.python.org/3/c-api/tls.html#c.Py_tss_t "Py_tss_t")
 \*key)[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_tss_get "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Return the void\* value associated with a TSS key in the current thread. This returns `NULL` if no value is associated with the key in the current thread.

Legacy APIs[¶](https://docs.python.org/3/c-api/tls.html#legacy-apis "Link to this heading")

--------------------------------------------------------------------------------------------

Deprecated since version 3.7: This API is superseded by the [thread-specific storage (TSS) API](https://docs.python.org/3/c-api/tls.html#thread-specific-storage-api)
.

Note

This version of the API does not support platforms where the native TLS key is defined in a way that cannot be safely cast to `int`. On such platforms, [`PyThread_create_key()`](https://docs.python.org/3/c-api/tls.html#c.PyThread_create_key "PyThread_create_key")
 will return immediately with a failure status, and the other TLS functions will all be no-ops on such platforms.

Due to the compatibility problem noted above, this version of the API should not be used in new code.

int PyThread\_create\_key()[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_create_key "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

void PyThread\_delete\_key(int key)[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_delete_key "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

int PyThread\_set\_key\_value(int key, void \*value)[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_set_key_value "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

void \*PyThread\_get\_key\_value(int key)[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_get_key_value "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

void PyThread\_delete\_key\_value(int key)[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_delete_key_value "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

void PyThread\_ReInitTLS()[¶](https://docs.python.org/3/c-api/tls.html#c.PyThread_ReInitTLS "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Thread-local storage support](https://docs.python.org/3/c-api/tls.html#)
    *   [Thread-specific storage API](https://docs.python.org/3/c-api/tls.html#thread-specific-storage-api)
        
    *   [Dynamic allocation](https://docs.python.org/3/c-api/tls.html#dynamic-allocation)
        
    *   [Methods](https://docs.python.org/3/c-api/tls.html#methods)
        
    *   [Legacy APIs](https://docs.python.org/3/c-api/tls.html#legacy-apis)
        

#### Previous topic

[Synchronization primitives](https://docs.python.org/3/c-api/synchronization.html "previous chapter")

#### Next topic

[Multiple interpreters in a Python process](https://docs.python.org/3/c-api/subinterpreters.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Thread-local+storage+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Ftls.html&pagesource=c-api%2Ftls.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/tls.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/subinterpreters.html "Multiple interpreters in a Python process")
     |
*   [previous](https://docs.python.org/3/c-api/synchronization.html "Synchronization primitives")
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
*   [Thread-local storage support](https://docs.python.org/3/c-api/tls.html)
    
*    
    
    |
*   Theme Auto Light Dark |