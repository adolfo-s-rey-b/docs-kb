### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/allocation.html "Allocating objects on the heap")
     |
*   [previous](https://docs.python.org/3/c-api/memory.html "Memory Management")
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
    
*    
    
    |
*   Theme Auto Light Dark |

Object Implementation Support[¶](https://docs.python.org/3/c-api/objimpl.html#object-implementation-support "Link to this heading")

====================================================================================================================================

This chapter describes the functions, types, and macros used when defining new object types.

*   [Allocating objects on the heap](https://docs.python.org/3/c-api/allocation.html)
    *   [Soft-deprecated aliases](https://docs.python.org/3/c-api/allocation.html#soft-deprecated-aliases)
        
*   [Object Life Cycle](https://docs.python.org/3/c-api/lifecycle.html)
    *   [Life Events](https://docs.python.org/3/c-api/lifecycle.html#life-events)
        
    *   [Cyclic Isolate Destruction](https://docs.python.org/3/c-api/lifecycle.html#cyclic-isolate-destruction)
        
    *   [Functions](https://docs.python.org/3/c-api/lifecycle.html#functions)
        
*   [Common Object Structures](https://docs.python.org/3/c-api/structures.html)
    *   [Base object types and macros](https://docs.python.org/3/c-api/structures.html#base-object-types-and-macros)
        
    *   [Implementing functions and methods](https://docs.python.org/3/c-api/structures.html#implementing-functions-and-methods)
        
    *   [Accessing attributes of extension types](https://docs.python.org/3/c-api/structures.html#accessing-attributes-of-extension-types)
        *   [Member flags](https://docs.python.org/3/c-api/structures.html#member-flags)
            
        *   [Member types](https://docs.python.org/3/c-api/structures.html#member-types)
            
        *   [Defining Getters and Setters](https://docs.python.org/3/c-api/structures.html#defining-getters-and-setters)
            
*   [Type Object Structures](https://docs.python.org/3/c-api/typeobj.html)
    *   [Quick Reference](https://docs.python.org/3/c-api/typeobj.html#quick-reference)
        *   [“tp slots”](https://docs.python.org/3/c-api/typeobj.html#tp-slots)
            
        *   [sub-slots](https://docs.python.org/3/c-api/typeobj.html#sub-slots)
            
        *   [slot typedefs](https://docs.python.org/3/c-api/typeobj.html#slot-typedefs)
            
    *   [PyTypeObject Definition](https://docs.python.org/3/c-api/typeobj.html#pytypeobject-definition)
        
    *   [PyObject Slots](https://docs.python.org/3/c-api/typeobj.html#pyobject-slots)
        
    *   [PyVarObject Slots](https://docs.python.org/3/c-api/typeobj.html#pyvarobject-slots)
        
    *   [PyTypeObject Slots](https://docs.python.org/3/c-api/typeobj.html#pytypeobject-slots)
        
    *   [Static Types](https://docs.python.org/3/c-api/typeobj.html#static-types)
        
    *   [Heap Types](https://docs.python.org/3/c-api/typeobj.html#heap-types)
        
    *   [Number Object Structures](https://docs.python.org/3/c-api/typeobj.html#number-object-structures)
        
    *   [Mapping Object Structures](https://docs.python.org/3/c-api/typeobj.html#mapping-object-structures)
        
    *   [Sequence Object Structures](https://docs.python.org/3/c-api/typeobj.html#sequence-object-structures)
        
    *   [Buffer Object Structures](https://docs.python.org/3/c-api/typeobj.html#buffer-object-structures)
        
    *   [Async Object Structures](https://docs.python.org/3/c-api/typeobj.html#async-object-structures)
        
    *   [Slot Type typedefs](https://docs.python.org/3/c-api/typeobj.html#slot-type-typedefs)
        
    *   [Examples](https://docs.python.org/3/c-api/typeobj.html#examples)
        
*   [Supporting Cyclic Garbage Collection](https://docs.python.org/3/c-api/gcsupport.html)
    *   [Traversal](https://docs.python.org/3/c-api/gcsupport.html#traversal)
        *   [Traversal-safe functions](https://docs.python.org/3/c-api/gcsupport.html#traversal-safe-functions)
            
        *   [“DuringGC” functions](https://docs.python.org/3/c-api/gcsupport.html#duringgc-functions)
            
    *   [Controlling the Garbage Collector State](https://docs.python.org/3/c-api/gcsupport.html#controlling-the-garbage-collector-state)
        
    *   [Querying Garbage Collector State](https://docs.python.org/3/c-api/gcsupport.html#querying-garbage-collector-state)
        

#### Previous topic

[Memory Management](https://docs.python.org/3/c-api/memory.html "previous chapter")

#### Next topic

[Allocating objects on the heap](https://docs.python.org/3/c-api/allocation.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Object+Implementation+Support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fobjimpl.html&pagesource=c-api%2Fobjimpl.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/objimpl.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/allocation.html "Allocating objects on the heap")
     |
*   [previous](https://docs.python.org/3/c-api/memory.html "Memory Management")
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
    
*    
    
    |
*   Theme Auto Light Dark |