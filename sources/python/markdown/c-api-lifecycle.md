### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/structures.html "Common Object Structures")
     |
*   [previous](https://docs.python.org/3/c-api/allocation.html "Allocating objects on the heap")
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
*   [Object Implementation Support](https://docs.python.org/3/c-api/objimpl.html)
     »
*   [Object Life Cycle](https://docs.python.org/3/c-api/lifecycle.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Object Life Cycle[¶](https://docs.python.org/3/c-api/lifecycle.html#object-life-cycle "Link to this heading")

==============================================================================================================

This section explains how a type’s slots relate to each other throughout the life of an object. It is not intended to be a complete canonical reference for the slots; instead, refer to the slot-specific documentation in [Type Object Structures](https://docs.python.org/3/c-api/typeobj.html#type-structs)
 for details about a particular slot.

Life Events[¶](https://docs.python.org/3/c-api/lifecycle.html#life-events "Link to this heading")

--------------------------------------------------------------------------------------------------

The figure below illustrates the order of events that can occur throughout an object’s life. An arrow from _A_ to _B_ indicates that event _B_ can occur after event _A_ has occurred, with the arrow’s label indicating the condition that must be true for _B_ to occur after _A_.

Life Events tp\_new tp\_new start->tp\_new    type call   tp\_alloc tp\_alloc tp\_new->tp\_alloc  direct call   tp\_init tp\_init tp\_new->tp\_init reachable reachable tp\_init->reachable reachable->tp\_init tp\_traverse tp\_traverse reachable->tp\_traverse  not in a    cyclic    isolate   reachable->tp\_traverse  periodic    cyclic isolate     detection   finalized? marked as finalized? reachable->finalized?  no refs   tp\_finalize tp\_finalize reachable->tp\_finalize  resurrected    (maybe remove    finalized mark)   uncollectable uncollectable (leaked) reachable->uncollectable  cyclic    isolate    (no GC    support)   tp\_dealloc tp\_dealloc reachable->tp\_dealloc  no refs tp\_traverse->finalized?  cyclic    isolate   finalized?->tp\_finalize  no (mark    as finalized)   tp\_clear tp\_clear finalized?->tp\_clear  yes   tp\_finalize->tp\_clear  no refs or     cyclic isolate   tp\_finalize->tp\_dealloc  recommended  call (see  explanation) tp\_finalize->tp\_dealloc   no refs   tp\_clear->uncollectable  cyclic    isolate   tp\_clear->tp\_dealloc  no refs   tp\_free tp\_free tp\_dealloc->tp\_free    direct call  

Explanation:

*   When a new object is constructed by calling its type:
    
    1.  [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
         is called to create a new object.
        
    2.  [`tp_alloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_alloc "PyTypeObject.tp_alloc")
         is directly called by [`tp_new`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_new "PyTypeObject.tp_new")
         to allocate the memory for the new object.
        
    3.  [`tp_init`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_init "PyTypeObject.tp_init")
         initializes the newly created object. `tp_init` can be called again to re-initialize an object, if desired. The `tp_init` call can also be skipped entirely, for example by Python code calling [`__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__")
        .
        
*   After `tp_init` completes, the object is ready to use.
    
*   Some time after the last reference to an object is removed:
    
    1.  If an object is not marked as _finalized_, it might be finalized by marking it as _finalized_ and calling its [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
         function. Python does _not_ finalize an object when the last reference to it is deleted; use [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")
         to ensure that `tp_finalize` is always called.
        
    2.  If the object is marked as finalized, [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
         might be called by the garbage collector to clear references held by the object. It is _not_ called when the object’s reference count reaches zero.
        
    3.  [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
         is called to destroy the object. To avoid code duplication, `tp_dealloc` typically calls into [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
         to free up the object’s references.
        
    4.  When [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
         finishes object destruction, it directly calls [`tp_free`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_free "PyTypeObject.tp_free")
         (usually set to [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free")
         or [`PyObject_GC_Del()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_Del "PyObject_GC_Del")
         automatically as appropriate for the type) to deallocate the memory.
        
*   The [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
     function is permitted to add a reference to the object if desired. If it does, the object is _resurrected_, preventing its pending destruction. (Only `tp_finalize` is allowed to resurrect an object; [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
     and [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
     cannot without calling into `tp_finalize`.) Resurrecting an object may or may not cause the object’s _finalized_ mark to be removed. Currently, Python does not remove the _finalized_ mark from a resurrected object if it supports garbage collection (i.e., the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
     flag is set) but does remove the mark if the object does not support garbage collection; either or both of these behaviors may change in the future.
    
*   [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
     can optionally call [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
     via [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")
     if it wishes to reuse that code to help with object destruction. This is recommended because it guarantees that `tp_finalize` is always called before destruction. See the `tp_dealloc` documentation for example code.
    
*   If the object is a member of a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
     and either [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
     fails to break the reference cycle or the cyclic isolate is not detected (perhaps [`gc.disable()`](https://docs.python.org/3/library/gc.html#gc.disable "gc.disable")
     was called, or the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
     flag was erroneously omitted in one of the involved types), the objects remain indefinitely uncollectable (they “leak”). See [`gc.garbage`](https://docs.python.org/3/library/gc.html#gc.garbage "gc.garbage")
    .
    

If the object is marked as supporting garbage collection (the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag is set in [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
), the following events are also possible:

*   The garbage collector occasionally calls [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")
     to identify [cyclic isolates](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
    .
    
*   When the garbage collector discovers a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
    , it finalizes one of the objects in the group by marking it as _finalized_ and calling its [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
     function, if it has one. This repeats until the cyclic isolate doesn’t exist or all of the objects have been finalized.
    
*   [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
     is permitted to resurrect the object by adding a reference from outside the [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
    . The new reference causes the group of objects to no longer form a cyclic isolate (the reference cycle may still exist, but if it does the objects are no longer isolated).
    
*   When the garbage collector discovers a [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
     and all of the objects in the group have already been marked as _finalized_, the garbage collector clears one or more of the uncleared objects in the group (possibly concurrently) by calling each’s [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
     function. This repeats as long as the cyclic isolate still exists and not all of the objects have been cleared.
    

Cyclic Isolate Destruction[¶](https://docs.python.org/3/c-api/lifecycle.html#cyclic-isolate-destruction "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Listed below are the stages of life of a hypothetical [cyclic isolate](https://docs.python.org/3/glossary.html#term-cyclic-isolate)
 that continues to exist after each member object is finalized or cleared. It is a memory leak if a cyclic isolate progresses through all of these stages; it should vanish once all objects are cleared, if not sooner. A cyclic isolate can vanish either because the reference cycle is broken or because the objects are no longer isolated due to finalizer resurrection (see [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
).

0.  **Reachable** (not yet a cyclic isolate): All objects are in their normal, reachable state. A reference cycle could exist, but an external reference means the objects are not yet isolated.
    
1.  **Unreachable but consistent:** The final reference from outside the cyclic group of objects has been removed, causing the objects to become isolated (thus a cyclic isolate is born). None of the group’s objects have been finalized or cleared yet. The cyclic isolate remains at this stage until some future run of the garbage collector (not necessarily the next run because the next run might not scan every object).
    
2.  **Mix of finalized and not finalized:** Objects in a cyclic isolate are finalized one at a time, which means that there is a period of time when the cyclic isolate is composed of a mix of finalized and non-finalized objects. Finalization order is unspecified, so it can appear random. A finalized object must behave in a sane manner when non-finalized objects interact with it, and a non-finalized object must be able to tolerate the finalization of an arbitrary subset of its referents.
    
3.  **All finalized:** All objects in a cyclic isolate are finalized before any of them are cleared.
    
4.  **Mix of finalized and cleared:** The objects can be cleared serially or concurrently (but with the [GIL](https://docs.python.org/3/glossary.html#term-GIL)
     held); either way, some will finish before others. A finalized object must be able to tolerate the clearing of a subset of its referents. [**PEP 442**](https://peps.python.org/pep-0442/)
     calls this stage “cyclic trash”.
    
5.  **Leaked:** If a cyclic isolate still exists after all objects in the group have been finalized and cleared, then the objects remain indefinitely uncollectable (see [`gc.garbage`](https://docs.python.org/3/library/gc.html#gc.garbage "gc.garbage")
    ). It is a bug if a cyclic isolate reaches this stage—it means the [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
     methods of the participating objects have failed to break the reference cycle as required.
    

If [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 did not exist, then Python would have no way to safely break a reference cycle. Simply destroying an object in a cyclic isolate would result in a dangling pointer, triggering undefined behavior when an object referencing the destroyed object is itself destroyed. The clearing step makes object destruction a two-phase process: first `tp_clear` is called to partially destroy the objects enough to detangle them from each other, then [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
 is called to complete the destruction.

Unlike clearing, finalization is not a phase of destruction. A finalized object must still behave properly by continuing to fulfill its design contracts. An object’s finalizer is allowed to execute arbitrary Python code, and is even allowed to prevent the impending destruction by adding a reference. The finalizer is only related to destruction by call order—if it runs, it runs before destruction, which starts with [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 (if called) and concludes with [`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
.

The finalization step is not necessary to safely reclaim the objects in a cyclic isolate, but its existence makes it easier to design types that behave in a sane manner when objects are cleared. Clearing an object might necessarily leave it in a broken, partially destroyed state—it might be unsafe to call any of the cleared object’s methods or access any of its attributes. With finalization, only finalized objects can possibly interact with cleared objects; non-finalized objects are guaranteed to interact with only non-cleared (but potentially finalized) objects.

To summarize the possible interactions:

*   A non-finalized object might have references to or from non-finalized and finalized objects, but not to or from cleared objects.
    
*   A finalized object might have references to or from non-finalized, finalized, and cleared objects.
    
*   A cleared object might have references to or from finalized and cleared objects, but not to or from non-finalized objects.
    

Without any reference cycles, an object can be simply destroyed once its last reference is deleted; the finalization and clearing steps are not necessary to safely reclaim unused objects. However, it can be useful to automatically call [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
 and [`tp_clear`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_clear "PyTypeObject.tp_clear")
 before destruction anyway because type design is simplified when all objects always experience the same series of events regardless of whether they participated in a cyclic isolate. Python currently only calls `tp_finalize` and `tp_clear` as needed to destroy a cyclic isolate; this may change in a future version.

Functions[¶](https://docs.python.org/3/c-api/lifecycle.html#functions "Link to this heading")

----------------------------------------------------------------------------------------------

To allocate and free memory, see [Allocating objects on the heap](https://docs.python.org/3/c-api/allocation.html#allocating-objects)
.

void PyObject\_CallFinalizer([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizer "Link to this definition")
  

Finalizes the object as described in [`tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize")
. Call this function (or [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")
) instead of calling `tp_finalize` directly because this function may deduplicate multiple calls to `tp_finalize`. Currently, calls are only deduplicated if the type supports garbage collection (i.e., the [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")
 flag is set); this may change in the future.

Added in version 3.4.

int PyObject\_CallFinalizerFromDealloc([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.15._

Same as [`PyObject_CallFinalizer()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizer "PyObject_CallFinalizer")
 but meant to be called at the beginning of the object’s destructor ([`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
). There must not be any references to the object. If the object’s finalizer resurrects the object, this function returns -1; no further destruction should happen. Otherwise, this function returns 0 and destruction can continue normally.

Added in version 3.4.

See also

[`tp_dealloc`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_dealloc "PyTypeObject.tp_dealloc")
 for example code.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Object Life Cycle](https://docs.python.org/3/c-api/lifecycle.html#)
    *   [Life Events](https://docs.python.org/3/c-api/lifecycle.html#life-events)
        
    *   [Cyclic Isolate Destruction](https://docs.python.org/3/c-api/lifecycle.html#cyclic-isolate-destruction)
        
    *   [Functions](https://docs.python.org/3/c-api/lifecycle.html#functions)
        

#### Previous topic

[Allocating objects on the heap](https://docs.python.org/3/c-api/allocation.html "previous chapter")

#### Next topic

[Common Object Structures](https://docs.python.org/3/c-api/structures.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Object+Life+Cycle&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Flifecycle.html&pagesource=c-api%2Flifecycle.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/lifecycle.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/structures.html "Common Object Structures")
     |
*   [previous](https://docs.python.org/3/c-api/allocation.html "Allocating objects on the heap")
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
*   [Object Implementation Support](https://docs.python.org/3/c-api/objimpl.html)
     »
*   [Object Life Cycle](https://docs.python.org/3/c-api/lifecycle.html)
    
*    
    
    |
*   Theme Auto Light Dark |