### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/type.html "Type Objects")
     |
*   [previous](https://docs.python.org/3/c-api/buffer.html "Buffer Protocol")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Concrete Objects Layer[¶](https://docs.python.org/3/c-api/concrete.html#concrete-objects-layer "Link to this heading")

=======================================================================================================================

The functions in this chapter are specific to certain Python object types. Passing them an object of the wrong type is not a good idea; if you receive an object from a Python program and you are not sure that it has the right type, you must perform a type check first; for example, to check that an object is a dictionary, use [`PyDict_Check()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_Check "PyDict_Check")
. The chapter is structured like the “family tree” of Python object types.

Warning

While the functions described in this chapter carefully check the type of the objects which are passed in, many of them do not check for `NULL` being passed instead of a valid object. Allowing `NULL` to be passed in can cause memory access violations and immediate termination of the interpreter.

Fundamental Objects[¶](https://docs.python.org/3/c-api/concrete.html#fundamental-objects "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

This section describes Python type objects and the singleton object `None`.

*   [Type Objects](https://docs.python.org/3/c-api/type.html)
    *   [Creating Heap-Allocated Types](https://docs.python.org/3/c-api/type.html#creating-heap-allocated-types)
        *   [Type slot IDs](https://docs.python.org/3/c-api/type.html#type-slot-ids)
            
    *   [Soft-deprecated API](https://docs.python.org/3/c-api/type.html#soft-deprecated-api)
        
*   [The `None` Object](https://docs.python.org/3/c-api/none.html)
    

Numeric Objects[¶](https://docs.python.org/3/c-api/concrete.html#numeric-objects "Link to this heading")

---------------------------------------------------------------------------------------------------------

*   [Integer Objects](https://docs.python.org/3/c-api/long.html)
    *   [Build configuration](https://docs.python.org/3/c-api/long.html#build-configuration)
        
    *   [Export API](https://docs.python.org/3/c-api/long.html#export-api)
        
    *   [PyLongWriter API](https://docs.python.org/3/c-api/long.html#pylongwriter-api)
        
    *   [Deprecated API](https://docs.python.org/3/c-api/long.html#deprecated-api)
        
*   [Boolean Objects](https://docs.python.org/3/c-api/bool.html)
    
*   [Floating-Point Objects](https://docs.python.org/3/c-api/float.html)
    *   [Pack and Unpack functions](https://docs.python.org/3/c-api/float.html#pack-and-unpack-functions)
        *   [Pack functions](https://docs.python.org/3/c-api/float.html#pack-functions)
            
        *   [Unpack functions](https://docs.python.org/3/c-api/float.html#unpack-functions)
            
*   [Complex Number Objects](https://docs.python.org/3/c-api/complex.html)
    *   [Complex Numbers as C Structures](https://docs.python.org/3/c-api/complex.html#complex-numbers-as-c-structures)
        

Sequence Objects[¶](https://docs.python.org/3/c-api/concrete.html#sequence-objects "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Generic operations on sequence objects were discussed in the previous chapter; this section deals with the specific kinds of sequence objects that are intrinsic to the Python language.

*   [Bytes Objects](https://docs.python.org/3/c-api/bytes.html)
    
*   [PyBytesWriter](https://docs.python.org/3/c-api/bytes.html#pybyteswriter)
    *   [Create, Finish, Discard](https://docs.python.org/3/c-api/bytes.html#create-finish-discard)
        
    *   [High-level API](https://docs.python.org/3/c-api/bytes.html#high-level-api)
        
    *   [Getters](https://docs.python.org/3/c-api/bytes.html#getters)
        
    *   [Low-level API](https://docs.python.org/3/c-api/bytes.html#low-level-api)
        
    *   [Example creating the string `b'abc'`](https://docs.python.org/3/c-api/bytes.html#example-creating-the-string-b-abc)
        
    *   [Update `PyBytes_FromStringAndSize()` code](https://docs.python.org/3/c-api/bytes.html#update-pybytes-fromstringandsize-code)
        
    *   [Update `_PyBytes_Resize()` code](https://docs.python.org/3/c-api/bytes.html#update-pybytes-resize-code)
        
*   [Byte Array Objects](https://docs.python.org/3/c-api/bytearray.html)
    *   [Type check macros](https://docs.python.org/3/c-api/bytearray.html#type-check-macros)
        
    *   [Direct API functions](https://docs.python.org/3/c-api/bytearray.html#direct-api-functions)
        
    *   [Macros](https://docs.python.org/3/c-api/bytearray.html#macros)
        
*   [Unicode Objects and Codecs](https://docs.python.org/3/c-api/unicode.html)
    *   [Unicode Objects](https://docs.python.org/3/c-api/unicode.html#unicode-objects)
        *   [Unicode Type](https://docs.python.org/3/c-api/unicode.html#unicode-type)
            
        *   [Unicode Character Properties](https://docs.python.org/3/c-api/unicode.html#unicode-character-properties)
            
        *   [Creating and accessing Unicode strings](https://docs.python.org/3/c-api/unicode.html#creating-and-accessing-unicode-strings)
            
        *   [Locale Encoding](https://docs.python.org/3/c-api/unicode.html#locale-encoding)
            
        *   [File System Encoding](https://docs.python.org/3/c-api/unicode.html#file-system-encoding)
            
        *   [wchar\_t Support](https://docs.python.org/3/c-api/unicode.html#wchar-t-support)
            
    *   [Built-in Codecs](https://docs.python.org/3/c-api/unicode.html#built-in-codecs)
        *   [Generic Codecs](https://docs.python.org/3/c-api/unicode.html#generic-codecs)
            
        *   [UTF-8 Codecs](https://docs.python.org/3/c-api/unicode.html#utf-8-codecs)
            
        *   [UTF-32 Codecs](https://docs.python.org/3/c-api/unicode.html#utf-32-codecs)
            
        *   [UTF-16 Codecs](https://docs.python.org/3/c-api/unicode.html#utf-16-codecs)
            
        *   [UTF-7 Codecs](https://docs.python.org/3/c-api/unicode.html#utf-7-codecs)
            
        *   [Unicode-Escape Codecs](https://docs.python.org/3/c-api/unicode.html#unicode-escape-codecs)
            
        *   [Raw-Unicode-Escape Codecs](https://docs.python.org/3/c-api/unicode.html#raw-unicode-escape-codecs)
            
        *   [Latin-1 Codecs](https://docs.python.org/3/c-api/unicode.html#latin-1-codecs)
            
        *   [ASCII Codecs](https://docs.python.org/3/c-api/unicode.html#ascii-codecs)
            
        *   [Character Map Codecs](https://docs.python.org/3/c-api/unicode.html#character-map-codecs)
            
        *   [MBCS codecs for Windows](https://docs.python.org/3/c-api/unicode.html#mbcs-codecs-for-windows)
            
    *   [Methods and Slot Functions](https://docs.python.org/3/c-api/unicode.html#methods-and-slot-functions)
        
    *   [PyUnicodeWriter](https://docs.python.org/3/c-api/unicode.html#pyunicodewriter)
        
    *   [Deprecated API](https://docs.python.org/3/c-api/unicode.html#deprecated-api)
        
*   [Tuple Objects](https://docs.python.org/3/c-api/tuple.html)
    
*   [Struct Sequence Objects](https://docs.python.org/3/c-api/tuple.html#struct-sequence-objects)
    
*   [List Objects](https://docs.python.org/3/c-api/list.html)
    

Container Objects[¶](https://docs.python.org/3/c-api/concrete.html#container-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------------

*   [Dictionary objects](https://docs.python.org/3/c-api/dict.html)
    *   [Dictionary view objects](https://docs.python.org/3/c-api/dict.html#dictionary-view-objects)
        
    *   [Frozen dictionary objects](https://docs.python.org/3/c-api/dict.html#frozen-dictionary-objects)
        
    *   [Ordered dictionaries](https://docs.python.org/3/c-api/dict.html#ordered-dictionaries)
        
*   [Set Objects](https://docs.python.org/3/c-api/set.html)
    *   [Deprecated API](https://docs.python.org/3/c-api/set.html#deprecated-api)
        

Function Objects[¶](https://docs.python.org/3/c-api/concrete.html#function-objects "Link to this heading")

-----------------------------------------------------------------------------------------------------------

*   [Function Objects](https://docs.python.org/3/c-api/function.html)
    
*   [Instance Method Objects](https://docs.python.org/3/c-api/method.html)
    
*   [Method Objects](https://docs.python.org/3/c-api/method.html#method-objects)
    
*   [Cell Objects](https://docs.python.org/3/c-api/cell.html)
    
*   [Code Objects](https://docs.python.org/3/c-api/code.html)
    
*   [Code Object Flags](https://docs.python.org/3/c-api/code.html#code-object-flags)
    
*   [Extra information](https://docs.python.org/3/c-api/code.html#extra-information)
    

Other Objects[¶](https://docs.python.org/3/c-api/concrete.html#other-objects "Link to this heading")

-----------------------------------------------------------------------------------------------------

*   [File objects](https://docs.python.org/3/c-api/file.html)
    *   [Soft-deprecated API](https://docs.python.org/3/c-api/file.html#soft-deprecated-api)
        
*   [Module Objects](https://docs.python.org/3/c-api/module.html)
    *   [Module definition](https://docs.python.org/3/c-api/module.html#module-definition)
        *   [Metadata slots](https://docs.python.org/3/c-api/module.html#metadata-slots)
            
        *   [Feature slots](https://docs.python.org/3/c-api/module.html#feature-slots)
            
        *   [Creation and initialization slots](https://docs.python.org/3/c-api/module.html#creation-and-initialization-slots)
            
    *   [Module state](https://docs.python.org/3/c-api/module.html#module-state)
        *   [Slots for defining module state](https://docs.python.org/3/c-api/module.html#slots-for-defining-module-state)
            
        *   [Module token](https://docs.python.org/3/c-api/module.html#module-token)
            
    *   [Creating extension modules dynamically](https://docs.python.org/3/c-api/module.html#creating-extension-modules-dynamically)
        
    *   [Module definition struct](https://docs.python.org/3/c-api/module.html#module-definition-struct)
        
    *   [Support functions](https://docs.python.org/3/c-api/module.html#support-functions)
        *   [Module lookup (single-phase initialization)](https://docs.python.org/3/c-api/module.html#module-lookup-single-phase-initialization)
            
*   [Iterator Objects](https://docs.python.org/3/c-api/iterator.html)
    *   [Range Objects](https://docs.python.org/3/c-api/iterator.html#range-objects)
        
    *   [Builtin Iterator Types](https://docs.python.org/3/c-api/iterator.html#builtin-iterator-types)
        
    *   [Other Iterator Objects](https://docs.python.org/3/c-api/iterator.html#other-iterator-objects)
        
*   [Descriptor Objects](https://docs.python.org/3/c-api/descriptor.html)
    *   [Built-in descriptors](https://docs.python.org/3/c-api/descriptor.html#built-in-descriptors)
        
*   [Slice Objects](https://docs.python.org/3/c-api/slice.html)
    *   [Ellipsis Object](https://docs.python.org/3/c-api/slice.html#ellipsis-object)
        
*   [MemoryView objects](https://docs.python.org/3/c-api/memoryview.html)
    
*   [Pickle buffer objects](https://docs.python.org/3/c-api/picklebuffer.html)
    
*   [Weak Reference Objects](https://docs.python.org/3/c-api/weakref.html)
    
*   [Capsules](https://docs.python.org/3/c-api/capsule.html)
    
*   [Sentinel objects](https://docs.python.org/3/c-api/sentinel.html)
    
*   [Frame objects](https://docs.python.org/3/c-api/frame.html)
    *   [Frame locals proxies](https://docs.python.org/3/c-api/frame.html#frame-locals-proxies)
        
    *   [Legacy local variable APIs](https://docs.python.org/3/c-api/frame.html#legacy-local-variable-apis)
        
    *   [Internal frames](https://docs.python.org/3/c-api/frame.html#internal-frames)
        
*   [Generator Objects](https://docs.python.org/3/c-api/gen.html)
    *   [Asynchronous Generator Objects](https://docs.python.org/3/c-api/gen.html#asynchronous-generator-objects)
        
    *   [Deprecated API](https://docs.python.org/3/c-api/gen.html#deprecated-api)
        
*   [Coroutine Objects](https://docs.python.org/3/c-api/coro.html)
    
*   [Context Variables Objects](https://docs.python.org/3/c-api/contextvars.html)
    
*   [Objects for Type Hinting](https://docs.python.org/3/c-api/typehints.html)
    

C API for extension modules[¶](https://docs.python.org/3/c-api/concrete.html#c-api-for-extension-modules "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

*   [Curses C API](https://docs.python.org/3/c-api/curses.html)
    
*   [Internal data](https://docs.python.org/3/c-api/curses.html#internal-data)
    
*   [DateTime Objects](https://docs.python.org/3/c-api/datetime.html)
    
*   [Internal data](https://docs.python.org/3/c-api/datetime.html#internal-data)
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html#)
    *   [Fundamental Objects](https://docs.python.org/3/c-api/concrete.html#fundamental-objects)
        
    *   [Numeric Objects](https://docs.python.org/3/c-api/concrete.html#numeric-objects)
        
    *   [Sequence Objects](https://docs.python.org/3/c-api/concrete.html#sequence-objects)
        
    *   [Container Objects](https://docs.python.org/3/c-api/concrete.html#container-objects)
        
    *   [Function Objects](https://docs.python.org/3/c-api/concrete.html#function-objects)
        
    *   [Other Objects](https://docs.python.org/3/c-api/concrete.html#other-objects)
        
    *   [C API for extension modules](https://docs.python.org/3/c-api/concrete.html#c-api-for-extension-modules)
        

#### Previous topic

[Buffer Protocol](https://docs.python.org/3/c-api/buffer.html "previous chapter")

#### Next topic

[Type Objects](https://docs.python.org/3/c-api/type.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Concrete+Objects+Layer&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fconcrete.html&pagesource=c-api%2Fconcrete.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/concrete.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/type.html "Type Objects")
     |
*   [previous](https://docs.python.org/3/c-api/buffer.html "Buffer Protocol")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
    
*    
    
    |
*   Theme Auto Light Dark |