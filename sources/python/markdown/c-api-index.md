### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/intro.html "Introduction")
     |
*   [previous](https://docs.python.org/3/extending/embedding.html "Embedding Python in Another Application")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Python/C API reference manual[¶](https://docs.python.org/3/c-api/index.html#python-c-api-reference-manual "Link to this heading")

==================================================================================================================================

This manual documents the API used by C and C++ programmers who want to write extension modules or embed Python. It is a companion to [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html#extending-index)
, which describes the general principles of extension writing but does not document the API functions in detail.

*   [Introduction](https://docs.python.org/3/c-api/intro.html)
    *   [Language version compatibility](https://docs.python.org/3/c-api/intro.html#language-version-compatibility)
        
    *   [Coding standards](https://docs.python.org/3/c-api/intro.html#coding-standards)
        
    *   [Include Files](https://docs.python.org/3/c-api/intro.html#include-files)
        
    *   [Useful macros](https://docs.python.org/3/c-api/intro.html#useful-macros)
        
    *   [Objects, Types and Reference Counts](https://docs.python.org/3/c-api/intro.html#objects-types-and-reference-counts)
        
    *   [Exceptions](https://docs.python.org/3/c-api/intro.html#exceptions)
        
    *   [Embedding Python](https://docs.python.org/3/c-api/intro.html#embedding-python)
        
    *   [Debugging Builds](https://docs.python.org/3/c-api/intro.html#debugging-builds)
        
    *   [Recommended third party tools](https://docs.python.org/3/c-api/intro.html#recommended-third-party-tools)
        
*   [C API and ABI Stability](https://docs.python.org/3/c-api/stable.html)
    *   [Unstable C API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
        
    *   [Stable Application Binary Interfaces](https://docs.python.org/3/c-api/stable.html#stable-application-binary-interfaces)
        
    *   [Platform Considerations](https://docs.python.org/3/c-api/stable.html#platform-considerations)
        
    *   [ABI Checking](https://docs.python.org/3/c-api/stable.html#abi-checking)
        
    *   [Contents of Limited API](https://docs.python.org/3/c-api/stable.html#contents-of-limited-api)
        
*   [The Very High Level Layer](https://docs.python.org/3/c-api/veryhigh.html)
    *   [Available start symbols](https://docs.python.org/3/c-api/veryhigh.html#available-start-symbols)
        
    *   [Stack Effects](https://docs.python.org/3/c-api/veryhigh.html#stack-effects)
        
*   [Reference Counting](https://docs.python.org/3/c-api/refcounting.html)
    
*   [Exception Handling](https://docs.python.org/3/c-api/exceptions.html)
    *   [Printing and clearing](https://docs.python.org/3/c-api/exceptions.html#printing-and-clearing)
        
    *   [Raising exceptions](https://docs.python.org/3/c-api/exceptions.html#raising-exceptions)
        
    *   [Issuing warnings](https://docs.python.org/3/c-api/exceptions.html#issuing-warnings)
        
    *   [Querying the error indicator](https://docs.python.org/3/c-api/exceptions.html#querying-the-error-indicator)
        
    *   [Signal Handling](https://docs.python.org/3/c-api/exceptions.html#signal-handling)
        
    *   [Exception Classes](https://docs.python.org/3/c-api/exceptions.html#exception-classes)
        
    *   [Exception Objects](https://docs.python.org/3/c-api/exceptions.html#exception-objects)
        
    *   [Unicode Exception Objects](https://docs.python.org/3/c-api/exceptions.html#unicode-exception-objects)
        
    *   [Recursion Control](https://docs.python.org/3/c-api/exceptions.html#recursion-control)
        
    *   [Exception and warning types](https://docs.python.org/3/c-api/exceptions.html#exception-and-warning-types)
        
    *   [Tracebacks](https://docs.python.org/3/c-api/exceptions.html#tracebacks)
        
*   [Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html)
    *   [Extension export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
        
    *   [Multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
        
    *   [Multiple module instances](https://docs.python.org/3/c-api/extension-modules.html#multiple-module-instances)
        
    *   [`PyInit` function](https://docs.python.org/3/c-api/extension-modules.html#pyinit-function)
        
*   [Definition slots](https://docs.python.org/3/c-api/slots.html)
    *   [Convenience macros](https://docs.python.org/3/c-api/slots.html#convenience-macros)
        
    *   [Common slot IDs](https://docs.python.org/3/c-api/slots.html#common-slot-ids)
        
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
    *   [Operating System Utilities](https://docs.python.org/3/c-api/sys.html)
        
    *   [System Functions](https://docs.python.org/3/c-api/sys.html#system-functions)
        
    *   [Process Control](https://docs.python.org/3/c-api/sys.html#process-control)
        
    *   [Importing Modules](https://docs.python.org/3/c-api/import.html)
        
    *   [Data marshalling support](https://docs.python.org/3/c-api/marshal.html)
        
    *   [Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html)
        
    *   [String conversion and formatting](https://docs.python.org/3/c-api/conversion.html)
        
    *   [Character classification and conversion](https://docs.python.org/3/c-api/conversion.html#character-classification-and-conversion)
        
    *   [PyHash API](https://docs.python.org/3/c-api/hash.html)
        
    *   [Reflection](https://docs.python.org/3/c-api/reflection.html)
        
    *   [Codec registry and support functions](https://docs.python.org/3/c-api/codec.html)
        
    *   [PyTime C API](https://docs.python.org/3/c-api/time.html)
        
    *   [Support for Perf Maps](https://docs.python.org/3/c-api/perfmaps.html)
        
    *   [Expat C API](https://docs.python.org/3/c-api/pyexpat.html)
        
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
    *   [Object Protocol](https://docs.python.org/3/c-api/object.html)
        
    *   [Call Protocol](https://docs.python.org/3/c-api/call.html)
        
    *   [Number Protocol](https://docs.python.org/3/c-api/number.html)
        
    *   [Sequence Protocol](https://docs.python.org/3/c-api/sequence.html)
        
    *   [Mapping Protocol](https://docs.python.org/3/c-api/mapping.html)
        
    *   [Iterator Protocol](https://docs.python.org/3/c-api/iter.html)
        
    *   [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html)
        
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
    *   [Fundamental Objects](https://docs.python.org/3/c-api/concrete.html#fundamental-objects)
        
    *   [Numeric Objects](https://docs.python.org/3/c-api/concrete.html#numeric-objects)
        
    *   [Sequence Objects](https://docs.python.org/3/c-api/concrete.html#sequence-objects)
        
    *   [Container Objects](https://docs.python.org/3/c-api/concrete.html#container-objects)
        
    *   [Function Objects](https://docs.python.org/3/c-api/concrete.html#function-objects)
        
    *   [Other Objects](https://docs.python.org/3/c-api/concrete.html#other-objects)
        
    *   [C API for extension modules](https://docs.python.org/3/c-api/concrete.html#c-api-for-extension-modules)
        
*   [Interpreter initialization and finalization](https://docs.python.org/3/c-api/interp-lifecycle.html)
    *   [Before Python initialization](https://docs.python.org/3/c-api/interp-lifecycle.html#before-python-initialization)
        
    *   [Global configuration variables](https://docs.python.org/3/c-api/interp-lifecycle.html#global-configuration-variables)
        
    *   [Initializing and finalizing the interpreter](https://docs.python.org/3/c-api/interp-lifecycle.html#initializing-and-finalizing-the-interpreter)
        
    *   [Cautions regarding interpreter finalization](https://docs.python.org/3/c-api/interp-lifecycle.html#cautions-regarding-interpreter-finalization)
        
    *   [Interpreter views](https://docs.python.org/3/c-api/interp-lifecycle.html#interpreter-views)
        
    *   [Process-wide parameters](https://docs.python.org/3/c-api/interp-lifecycle.html#process-wide-parameters)
        
*   [Thread states and the global interpreter lock](https://docs.python.org/3/c-api/threads.html)
    *   [Detaching the thread state from extension code](https://docs.python.org/3/c-api/threads.html#detaching-the-thread-state-from-extension-code)
        
    *   [Using the C API from foreign threads](https://docs.python.org/3/c-api/threads.html#using-the-c-api-from-foreign-threads)
        
    *   [GIL-state APIs](https://docs.python.org/3/c-api/threads.html#gil-state-apis)
        
    *   [Cautions about fork()](https://docs.python.org/3/c-api/threads.html#cautions-about-fork)
        
    *   [High-level APIs](https://docs.python.org/3/c-api/threads.html#high-level-apis)
        
    *   [Low-level APIs](https://docs.python.org/3/c-api/threads.html#low-level-apis)
        
*   [Asynchronous notifications](https://docs.python.org/3/c-api/threads.html#asynchronous-notifications)
    
*   [Operating system thread APIs](https://docs.python.org/3/c-api/threads.html#operating-system-thread-apis)
    
*   [Synchronization primitives](https://docs.python.org/3/c-api/synchronization.html)
    *   [Python critical section API](https://docs.python.org/3/c-api/synchronization.html#python-critical-section-api)
        
    *   [Legacy locking APIs](https://docs.python.org/3/c-api/synchronization.html#legacy-locking-apis)
        
*   [Thread-local storage support](https://docs.python.org/3/c-api/tls.html)
    *   [Thread-specific storage API](https://docs.python.org/3/c-api/tls.html#thread-specific-storage-api)
        
    *   [Dynamic allocation](https://docs.python.org/3/c-api/tls.html#dynamic-allocation)
        
    *   [Methods](https://docs.python.org/3/c-api/tls.html#methods)
        
    *   [Legacy APIs](https://docs.python.org/3/c-api/tls.html#legacy-apis)
        
*   [Multiple interpreters in a Python process](https://docs.python.org/3/c-api/subinterpreters.html)
    *   [A per-interpreter GIL](https://docs.python.org/3/c-api/subinterpreters.html#a-per-interpreter-gil)
        
    *   [Bugs and caveats](https://docs.python.org/3/c-api/subinterpreters.html#bugs-and-caveats)
        
    *   [High-level APIs](https://docs.python.org/3/c-api/subinterpreters.html#high-level-apis)
        
    *   [Low-level APIs](https://docs.python.org/3/c-api/subinterpreters.html#low-level-apis)
        
    *   [Advanced debugger support](https://docs.python.org/3/c-api/subinterpreters.html#advanced-debugger-support)
        
*   [Profiling and tracing](https://docs.python.org/3/c-api/profiling.html)
    
*   [Reference tracing](https://docs.python.org/3/c-api/profiling.html#reference-tracing)
    
*   [Performance statistics](https://docs.python.org/3/c-api/profiling.html#performance-statistics)
    
*   [Python Initialization Configuration](https://docs.python.org/3/c-api/init_config.html)
    *   [PyInitConfig C API](https://docs.python.org/3/c-api/init_config.html#pyinitconfig-c-api)
        
    *   [Configuration Options](https://docs.python.org/3/c-api/init_config.html#configuration-options)
        
    *   [Runtime Python configuration API](https://docs.python.org/3/c-api/init_config.html#runtime-python-configuration-api)
        
    *   [PyConfig C API](https://docs.python.org/3/c-api/init_config.html#pyconfig-c-api)
        
    *   [Py\_GetArgcArgv()](https://docs.python.org/3/c-api/init_config.html#py-getargcargv)
        
    *   [Multi-Phase Initialization Private Provisional API](https://docs.python.org/3/c-api/init_config.html#multi-phase-initialization-private-provisional-api)
        
*   [Memory Management](https://docs.python.org/3/c-api/memory.html)
    *   [Overview](https://docs.python.org/3/c-api/memory.html#overview)
        
    *   [Allocator Domains](https://docs.python.org/3/c-api/memory.html#allocator-domains)
        
    *   [Raw Memory Interface](https://docs.python.org/3/c-api/memory.html#raw-memory-interface)
        
    *   [Memory Interface](https://docs.python.org/3/c-api/memory.html#memory-interface)
        
    *   [Object allocators](https://docs.python.org/3/c-api/memory.html#object-allocators)
        
    *   [Default Memory Allocators](https://docs.python.org/3/c-api/memory.html#default-memory-allocators)
        
    *   [Customize Memory Allocators](https://docs.python.org/3/c-api/memory.html#customize-memory-allocators)
        
    *   [Debug hooks on the Python memory allocators](https://docs.python.org/3/c-api/memory.html#debug-hooks-on-the-python-memory-allocators)
        
    *   [The pymalloc allocator](https://docs.python.org/3/c-api/memory.html#the-pymalloc-allocator)
        
    *   [The mimalloc allocator](https://docs.python.org/3/c-api/memory.html#the-mimalloc-allocator)
        
    *   [tracemalloc C API](https://docs.python.org/3/c-api/memory.html#tracemalloc-c-api)
        
    *   [Examples](https://docs.python.org/3/c-api/memory.html#examples)
        
*   [Object Implementation Support](https://docs.python.org/3/c-api/objimpl.html)
    *   [Allocating objects on the heap](https://docs.python.org/3/c-api/allocation.html)
        
    *   [Object Life Cycle](https://docs.python.org/3/c-api/lifecycle.html)
        
    *   [Common Object Structures](https://docs.python.org/3/c-api/structures.html)
        
    *   [Type Object Structures](https://docs.python.org/3/c-api/typeobj.html)
        
    *   [Supporting Cyclic Garbage Collection](https://docs.python.org/3/c-api/gcsupport.html)
        
*   [API and ABI Versioning](https://docs.python.org/3/c-api/apiabiversion.html)
    *   [Build-time version constants](https://docs.python.org/3/c-api/apiabiversion.html#build-time-version-constants)
        
    *   [Run-time version](https://docs.python.org/3/c-api/apiabiversion.html#run-time-version)
        
    *   [Bit-packing macros](https://docs.python.org/3/c-api/apiabiversion.html#bit-packing-macros)
        
*   [Monitoring C API](https://docs.python.org/3/c-api/monitoring.html)
    
*   [Generating Execution Events](https://docs.python.org/3/c-api/monitoring.html#generating-execution-events)
    *   [Managing the Monitoring State](https://docs.python.org/3/c-api/monitoring.html#managing-the-monitoring-state)
        

#### Previous topic

[Embedding Python in Another Application](https://docs.python.org/3/extending/embedding.html "previous chapter")

#### Next topic

[Introduction](https://docs.python.org/3/c-api/intro.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Python%2FC+API+reference+manual&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Findex.html&pagesource=c-api%2Findex.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/index.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/intro.html "Introduction")
     |
*   [previous](https://docs.python.org/3/extending/embedding.html "Embedding Python in Another Application")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
    
*    
    
    |
*   Theme Auto Light Dark |