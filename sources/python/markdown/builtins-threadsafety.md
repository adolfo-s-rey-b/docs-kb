### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/builtins/time-complexity.html "Time complexity of operations on built-in types")
     |
*   [previous](https://docs.python.org/3/builtins/exceptions.html "Built-in Exceptions")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python built-ins reference](https://docs.python.org/3/builtins/index.html)
     »
*   [Thread Safety Guarantees](https://docs.python.org/3/builtins/threadsafety.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Thread Safety Guarantees[¶](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-guarantees "Link to this heading")

==================================================================================================================================

This page documents thread-safety guarantees for built-in types in Python’s free-threaded build. The guarantees described here apply when using Python with the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
 disabled (free-threaded mode). When the GIL is enabled, most operations are implicitly serialized.

For general guidance on writing thread-safe code in free-threaded Python, see [Python support for free threading](https://docs.python.org/3/howto/free-threading-python.html#freethreading-python-howto)
.

Thread safety levels[¶](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-levels "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

The C API documentation uses the following levels to describe the thread safety guarantees of each function. The levels are listed from least to most safe.

### Incompatible[¶](https://docs.python.org/3/builtins/threadsafety.html#incompatible "Link to this heading")

A function or operation that cannot be made safe for concurrent use even with external synchronization. Incompatible code typically accesses global state in an unsynchronized way and must only be called from a single thread throughout the program’s lifetime.

Example: a function that modifies process-wide state such as signal handlers or environment variables, where concurrent calls from any threads, even with external locking, can conflict with the runtime or other libraries.

### Compatible[¶](https://docs.python.org/3/builtins/threadsafety.html#compatible "Link to this heading")

A function or operation that is safe to call from multiple threads _provided_ the caller supplies appropriate external synchronization, for example by holding a [lock](https://docs.python.org/3/glossary.html#term-lock)
 for the duration of each call. Without such synchronization, concurrent calls may produce [race conditions](https://docs.python.org/3/glossary.html#term-race-condition)
 or [data races](https://docs.python.org/3/glossary.html#term-data-race)
.

Example: a function that reads from or writes to an object whose internal state is not protected by a lock. Callers must ensure that no two threads access the same object at the same time.

### Safe on distinct objects[¶](https://docs.python.org/3/builtins/threadsafety.html#safe-on-distinct-objects "Link to this heading")

A function or operation that is safe to call from multiple threads without external synchronization, as long as each thread operates on a **different** object. Two threads may call the function at the same time, but they must not pass the same object (or objects that share underlying state) as arguments.

Example: a function that modifies fields of a struct using non-atomic writes. Two threads can each call the function on their own struct instance safely, but concurrent calls on the _same_ instance require external synchronization.

### Safe on shared objects[¶](https://docs.python.org/3/builtins/threadsafety.html#safe-on-shared-objects "Link to this heading")

A function or operation that is safe for concurrent use on the **same** object. The implementation uses internal synchronization (such as [per-object locks](https://docs.python.org/3/glossary.html#term-per-object-lock)
 or [critical sections](https://docs.python.org/3/c-api/synchronization.html#python-critical-section-api)
) to protect shared mutable state, so callers do not need to supply their own locking.

Example: [`PyList_GetItemRef()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItemRef "PyList_GetItemRef")
 can be called from multiple threads on the same [`PyListObject`](https://docs.python.org/3/c-api/list.html#c.PyListObject "PyListObject")
 - it uses internal synchronization to serialize access.

### Atomic[¶](https://docs.python.org/3/builtins/threadsafety.html#atomic "Link to this heading")

A function or operation that appears [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
 with respect to other threads - it executes instantaneously from the perspective of other threads. This is the strongest form of thread safety.

Example: [`PyMutex_IsLocked()`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex_IsLocked "PyMutex_IsLocked")
 performs an atomic read of the mutex state and can be called from any thread at any time.

Thread safety for list objects[¶](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-list-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

Reading a single element from a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 is [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
:

Copy

lst\[i\]   \# list.\_\_getitem\_\_

The following methods traverse the list and use [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
 reads of each item to perform their function. That means that they may return results affected by concurrent modifications:

Copy

item in lst
lst.index(item)
lst.count(item)

All of the above operations avoid acquiring [per-object locks](https://docs.python.org/3/glossary.html#term-per-object-lock)
. They do not block concurrent modifications. Other operations that hold a lock will not block these from observing intermediate states.

All other operations from here on block using the [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock)
.

Writing a single item via `lst[i] = x` is safe to call from multiple threads and will not corrupt the list.

The following operations return new objects and appear [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
 to other threads:

Copy

lst1 + lst2    \# concatenates two lists into a new list
x \* lst        \# repeats lst x times into a new list
lst.copy()     \# returns a shallow copy of the list

The following methods that only operate on a single element with no shifting required are [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
:

Copy

lst.append(x)  \# append to the end of the list, no shifting required
lst.pop()      \# pop element from the end of the list, no shifting required

The [`clear()`](https://docs.python.org/3/builtins/stdtypes.html#list.clear "list.clear")
 method is also [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
. Other threads cannot observe elements being removed.

The [`sort()`](https://docs.python.org/3/builtins/stdtypes.html#list.sort "list.sort")
 method is not [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
. Other threads cannot observe intermediate states during sorting, but the list appears empty for the duration of the sort.

The following operations may allow [lock-free](https://docs.python.org/3/glossary.html#term-lock-free)
 operations to observe intermediate states since they modify multiple elements in place:

Copy

lst.insert(idx, item)  \# shifts elements
lst.pop(idx)           \# idx not at the end of the list, shifts elements
lst \*= x               \# copies elements in place

The [`remove()`](https://docs.python.org/3/builtins/stdtypes.html#list.remove "list.remove")
 method may allow concurrent modifications since element comparison may execute arbitrary Python code (via [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
).

[`extend()`](https://docs.python.org/3/builtins/stdtypes.html#list.extend "list.extend")
 is safe to call from multiple threads. However, its guarantees depend on the iterable passed to it. If it is a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
, a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
, a [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
, a [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
, a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [dictionary view object](https://docs.python.org/3/builtins/stdtypes.html#dict-views)
 (but not their subclasses), the `extend` operation is safe from concurrent modifications to the iterable. Otherwise, an iterator is created which can be concurrently modified by another thread. The same applies to inplace concatenation of a list with other iterables when using `lst += iterable`.

Similarly, assigning to a list slice with `lst[i:j] = iterable` is safe to call from multiple threads, but `iterable` is only locked when it is also a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 (but not its subclasses).

Operations that involve multiple accesses, as well as iteration, are never atomic. For example:

Copy

\# NOT atomic: read-modify-write
lst\[i\] \= lst\[i\] + 1

\# NOT atomic: check-then-act
if lst:
    item \= lst.pop()

\# NOT thread-safe: iteration while modifying
for item in lst:
    process(item)  \# another thread may modify lst

Consider external synchronization when sharing [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
 instances across threads.

Thread safety for dict objects[¶](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-dict-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

Creating a dictionary with the [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 constructor is atomic when the argument to it is a `dict` or a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
. When using the [`dict.fromkeys()`](https://docs.python.org/3/builtins/stdtypes.html#dict.fromkeys "dict.fromkeys")
 method, dictionary creation is atomic when the argument is a `dict`, `tuple`, [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 or [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
.

The following operations and functions are [lock-free](https://docs.python.org/3/glossary.html#term-lock-free)
 and [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
.

Copy

d\[key\]       \# dict.\_\_getitem\_\_
d.get(key)   \# dict.get
key in d     \# dict.\_\_contains\_\_
len(d)       \# dict.\_\_len\_\_

All other operations from here on hold the [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock)
.

Writing or removing a single item is safe to call from multiple threads and will not corrupt the dictionary:

Copy

d\[key\] \= value        \# write
del d\[key\]            \# delete
d.pop(key)            \# remove and return
d.popitem()           \# remove and return last item
d.setdefault(key, v)  \# insert if missing

These operations may compare keys using [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
, which can execute arbitrary Python code. During such comparisons, the dictionary may be modified by another thread. For built-in types like [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, and [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, that implement `__eq__()` in C, the underlying lock is not released during comparisons and this is not a concern.

The following operations return new objects and hold the [per-object lock](https://docs.python.org/3/glossary.html#term-per-object-lock)
 for the duration of the operation:

Copy

d.copy()      \# returns a shallow copy of the dictionary
d | other     \# merges two dicts into a new dict
d.keys()      \# returns a new dict\_keys view object
d.values()    \# returns a new dict\_values view object
d.items()     \# returns a new dict\_items view object

The [`clear()`](https://docs.python.org/3/builtins/stdtypes.html#dict.clear "dict.clear")
 method holds the lock for its duration. Other threads cannot observe elements being removed.

The following operations lock both dictionaries. For [`update()`](https://docs.python.org/3/builtins/stdtypes.html#dict.update "dict.update")
 and `|=`, this applies only when the other operand is a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 that uses the standard dict iterator (but not subclasses that override iteration). For equality comparison, this applies to `dict` and its subclasses:

Copy

d.update(other\_dict)  \# both locked when other\_dict is a dict
d |= other\_dict       \# both locked when other\_dict is a dict
d \== other\_dict       \# both locked for dict and subclasses

All comparison operations also compare values using [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
, so for non-built-in types the lock may be released during comparison.

[`fromkeys()`](https://docs.python.org/3/builtins/stdtypes.html#dict.fromkeys "dict.fromkeys")
 locks both the new dictionary and the iterable when the iterable is exactly a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
, [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
, or [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
 (not subclasses):

Copy

dict.fromkeys(a\_dict)      \# locks both
dict.fromkeys(a\_set)       \# locks both
dict.fromkeys(a\_frozenset) \# locks both

When updating from a non-dict iterable, only the target dictionary is locked. The iterable may be concurrently modified by another thread:

Copy

d.update(iterable)        \# iterable is not a dict: only d locked
d |= iterable             \# iterable is not a dict: only d locked
dict.fromkeys(iterable)   \# iterable is not a dict/set/frozenset: only result locked

Operations that involve multiple accesses, as well as iteration, are never atomic:

Copy

\# NOT atomic: read-modify-write
d\[key\] \= d\[key\] + 1

\# NOT atomic: check-then-act (TOCTOU)
if key in d:
    del d\[key\]

\# NOT thread-safe: iteration while modifying
for key, value in d.items():
    process(key)  \# another thread may modify d

To avoid time-of-check to time-of-use (TOCTOU) issues, use atomic operations or handle exceptions:

Copy

\# Use pop() with default instead of check-then-delete
d.pop(key, None)

\# Or handle the exception
try:
    del d\[key\]
except KeyError:
    pass

To safely iterate over a dictionary that may be modified by another thread, iterate over a copy:

Copy

\# Make a copy to iterate safely
for key, value in d.copy().items():
    process(key)

Consider external synchronization when sharing [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 instances across threads.

Thread safety for set objects[¶](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-set-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

The [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
 function is lock-free and [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
.

The following read operation is lock-free. It does not block concurrent modifications and may observe intermediate states from operations that hold the per-object lock:

Copy

elem in s    \# set.\_\_contains\_\_

This operation may compare elements using [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
, which can execute arbitrary Python code. During such comparisons, the set may be modified by another thread. For built-in types like [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
, [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
, and [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
, `__eq__()` does not release the underlying lock during comparisons and this is not a concern.

All other operations from here on hold the per-object lock.

Adding or removing a single element is safe to call from multiple threads and will not corrupt the set:

Copy

s.add(elem)      \# add element
s.remove(elem)   \# remove element, raise if missing
s.discard(elem)  \# remove element if present
s.pop()          \# remove and return arbitrary element

These operations also compare elements, so the same [`__eq__()`](https://docs.python.org/3/reference/datamodel.html#object.__eq__ "object.__eq__")
 considerations as above apply.

The [`copy()`](https://docs.python.org/3/builtins/stdtypes.html#set.copy "set.copy")
 method returns a new object and holds the per-object lock for the duration so that it is always atomic.

The [`clear()`](https://docs.python.org/3/builtins/stdtypes.html#set.clear "set.clear")
 method holds the lock for its duration. Other threads cannot observe elements being removed.

The following operations only accept [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 or [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
 as operands and always lock both objects:

Copy

s |= other                   \# other must be set/frozenset
s &= other                   \# other must be set/frozenset
s \-= other                   \# other must be set/frozenset
s ^= other                   \# other must be set/frozenset
s & other                    \# other must be set/frozenset
s | other                    \# other must be set/frozenset
s \- other                    \# other must be set/frozenset
s ^ other                    \# other must be set/frozenset

[`set.update()`](https://docs.python.org/3/builtins/stdtypes.html#set.update "set.update")
, [`set.union()`](https://docs.python.org/3/builtins/stdtypes.html#set.union "set.union")
, [`set.intersection()`](https://docs.python.org/3/builtins/stdtypes.html#set.intersection "set.intersection")
 and [`set.difference()`](https://docs.python.org/3/builtins/stdtypes.html#set.difference "set.difference")
 can take multiple iterables as arguments. They all iterate through all the passed iterables and do the following:

> *   [`set.update()`](https://docs.python.org/3/builtins/stdtypes.html#set.update "set.update")
>      and [`set.union()`](https://docs.python.org/3/builtins/stdtypes.html#set.union "set.union")
>      lock both objects only when the other operand is a [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
>     , [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
>     , or [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
>     .
>     
> *   [`set.intersection()`](https://docs.python.org/3/builtins/stdtypes.html#set.intersection "set.intersection")
>      and [`set.difference()`](https://docs.python.org/3/builtins/stdtypes.html#set.difference "set.difference")
>      always try to lock all objects.
>     

[`set.symmetric_difference()`](https://docs.python.org/3/builtins/stdtypes.html#set.symmetric_difference "set.symmetric_difference")
 tries to lock both objects.

The update variants of the above methods also have some differences between them:

> *   [`set.difference_update()`](https://docs.python.org/3/builtins/stdtypes.html#set.difference_update "set.difference_update")
>      and [`set.intersection_update()`](https://docs.python.org/3/builtins/stdtypes.html#set.intersection_update "set.intersection_update")
>      try to lock all objects one-by-one.
>     
> *   [`set.symmetric_difference_update()`](https://docs.python.org/3/builtins/stdtypes.html#set.symmetric_difference_update "set.symmetric_difference_update")
>      only locks the arguments if it is of type [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
>     , [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
>     , or [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
>     .
>     

The following methods always try to lock both objects:

Copy

s.isdisjoint(other)          \# both locked
s.issubset(other)            \# both locked
s.issuperset(other)          \# both locked

Operations that involve multiple accesses, as well as iteration, are never atomic:

Copy

\# NOT atomic: check-then-act
if elem in s:
      s.remove(elem)

\# NOT thread-safe: iteration while modifying
for elem in s:
      process(elem)  \# another thread may modify s

Consider external synchronization when sharing [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
 instances across threads. See [Python support for free threading](https://docs.python.org/3/howto/free-threading-python.html#freethreading-python-howto)
 for more information.

Thread safety for bytearray objects[¶](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-bytearray-objects "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

> The [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
>  function is lock-free and [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
> .
> 
> Concatenation and comparisons use the buffer protocol, which prevents resizing but does not hold the per-object lock. These operations may observe intermediate states from concurrent modifications:
> 
> Copy
> 
> ba + other    \# may observe concurrent writes
> ba \== other   \# may observe concurrent writes
> ba < other    \# may observe concurrent writes
> 
> All other operations from here on hold the per-object lock.
> 
> Reading a single element or slice is safe to call from multiple threads:
> 
> Copy
> 
> ba\[i\]        \# bytearray.\_\_getitem\_\_
> ba\[i:j\]      \# slice
> 
> The following operations are safe to call from multiple threads and will not corrupt the bytearray:
> 
> Copy
> 
> ba\[i\] \= x         \# write single byte
> ba\[i:j\] \= values  \# write slice
> ba.append(x)      \# append single byte
> ba.extend(other)  \# extend with iterable
> ba.insert(i, x)   \# insert single byte
> ba.pop()          \# remove and return last byte
> ba.pop(i)         \# remove and return byte at index
> ba.remove(x)      \# remove first occurrence
> ba.reverse()      \# reverse in place
> ba.clear()        \# remove all bytes
> 
> Slice assignment locks both objects when _values_ is a [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
> :
> 
> Copy
> 
> ba\[i:j\] \= other\_bytearray  \# both locked
> 
> The following operations return new objects and hold the per-object lock for the duration:
> 
> Copy
> 
> ba.copy()     \# returns a shallow copy
> ba \* n        \# repeat into new bytearray
> 
> The membership test holds the lock for its duration:
> 
> Copy
> 
> x in ba       \# bytearray.\_\_contains\_\_
> 
> All other bytearray methods (such as [`find()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.find "bytearray.find")
> , [`replace()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.replace "bytearray.replace")
> , [`split()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.split "bytearray.split")
> , [`decode()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.decode "bytearray.decode")
> , etc.) hold the per-object lock for their duration.
> 
> Operations that involve multiple accesses, as well as iteration, are never atomic:
> 
> Copy
> 
> \# NOT atomic: check-then-act
> if x in ba:
>     ba.remove(x)
> 
> \# NOT thread-safe: iteration while modifying
> for byte in ba:
>     process(byte)  \# another thread may modify ba
> 
> To safely iterate over a bytearray that may be modified by another thread, iterate over a copy:
> 
> Copy
> 
> \# Make a copy to iterate safely
> for byte in ba.copy():
>     process(byte)
> 
> Consider external synchronization when sharing [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
>  instances across threads. See [Python support for free threading](https://docs.python.org/3/howto/free-threading-python.html#freethreading-python-howto)
>  for more information.

Thread safety for memoryview objects[¶](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-memoryview-objects "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

[`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
 objects provide access to the internal data of an underlying object without copying. Thread safety depends on both the memoryview itself and the underlying buffer exporter.

The memoryview implementation uses atomic operations to track its own exports in the [free-threaded build](https://docs.python.org/3/glossary.html#term-free-threaded-build)
. Creating and releasing a memoryview are thread-safe. Attribute access (e.g., [`shape`](https://docs.python.org/3/builtins/stdtypes.html#memoryview.shape "memoryview.shape")
, [`format`](https://docs.python.org/3/builtins/stdtypes.html#memoryview.format "memoryview.format")
) reads fields that are immutable for the lifetime of the memoryview, so concurrent reads are safe as long as the memoryview has not been released.

However, the actual data accessed through the memoryview is owned by the underlying object. Concurrent access to this data is only safe if the underlying object supports it:

*   For immutable objects like [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
    , concurrent reads through multiple memoryviews are safe.
    
*   For mutable objects like [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
    , reading and writing the same memory region from multiple threads without external synchronization is not safe and may result in data corruption. Note that even read-only memoryviews of mutable objects do not prevent data races if the underlying object is modified from another thread.
    

Copy

\# NOT safe: concurrent writes to the same buffer
data \= bytearray(1000)
view \= memoryview(data)
\# Thread 1: view\[0:500\] = b'x' \* 500
\# Thread 2: view\[0:500\] = b'y' \* 500

Copy

\# Safe: use a lock for concurrent access
import threading
lock \= threading.Lock()
data \= bytearray(1000)
view \= memoryview(data)

with lock:
    view\[0:500\] \= b'x' \* 500

Resizing or reallocating the underlying object (such as calling [`bytearray.resize()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.resize "bytearray.resize")
) while a memoryview is exported raises [`BufferError`](https://docs.python.org/3/builtins/exceptions.html#BufferError "BufferError")
. This is enforced regardless of threading.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Thread Safety Guarantees](https://docs.python.org/3/builtins/threadsafety.html#)
    *   [Thread safety levels](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-levels)
        *   [Incompatible](https://docs.python.org/3/builtins/threadsafety.html#incompatible)
            
        *   [Compatible](https://docs.python.org/3/builtins/threadsafety.html#compatible)
            
        *   [Safe on distinct objects](https://docs.python.org/3/builtins/threadsafety.html#safe-on-distinct-objects)
            
        *   [Safe on shared objects](https://docs.python.org/3/builtins/threadsafety.html#safe-on-shared-objects)
            
        *   [Atomic](https://docs.python.org/3/builtins/threadsafety.html#atomic)
            
    *   [Thread safety for list objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-list-objects)
        
    *   [Thread safety for dict objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-dict-objects)
        
    *   [Thread safety for set objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-set-objects)
        
    *   [Thread safety for bytearray objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-bytearray-objects)
        
    *   [Thread safety for memoryview objects](https://docs.python.org/3/builtins/threadsafety.html#thread-safety-for-memoryview-objects)
        

#### Previous topic

[Built-in Exceptions](https://docs.python.org/3/builtins/exceptions.html "previous chapter")

#### Next topic

[Time complexity of operations on built-in types](https://docs.python.org/3/builtins/time-complexity.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Thread+Safety+Guarantees&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fbuiltins%2Fthreadsafety.html&pagesource=builtins%2Fthreadsafety.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/builtins/threadsafety.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/builtins/time-complexity.html "Time complexity of operations on built-in types")
     |
*   [previous](https://docs.python.org/3/builtins/exceptions.html "Built-in Exceptions")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python built-ins reference](https://docs.python.org/3/builtins/index.html)
     »
*   [Thread Safety Guarantees](https://docs.python.org/3/builtins/threadsafety.html)
    
*    
    
    |
*   Theme Auto Light Dark |