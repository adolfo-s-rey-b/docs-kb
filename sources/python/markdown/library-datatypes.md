### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/datetime.html "datetime — Basic date and time types")
     |
*   [previous](https://docs.python.org/3/library/codecs.html "codecs — Codec registry and base classes")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Data Types](https://docs.python.org/3/library/datatypes.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Data Types[¶](https://docs.python.org/3/library/datatypes.html#data-types "Link to this heading")

==================================================================================================

The modules described in this chapter provide a variety of specialized data types such as dates and times, fixed-type arrays, heap queues, double-ended queues, and enumerations.

Python also provides [some built-in data types](https://docs.python.org/3/builtins/stdtypes.html#bltin-types)
, in particular, [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
, [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
, [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
, [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
, [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")
, and [`frozenset`](https://docs.python.org/3/builtins/stdtypes.html#frozenset "frozenset")
. The [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 class is used to hold Unicode strings, and the [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 classes are used to hold binary data.

The following modules are documented in this chapter:

*   [`datetime` — Basic date and time types](https://docs.python.org/3/library/datetime.html)
    *   [Aware and naive objects](https://docs.python.org/3/library/datetime.html#aware-and-naive-objects)
        
    *   [Constants](https://docs.python.org/3/library/datetime.html#constants)
        
    *   [Available types](https://docs.python.org/3/library/datetime.html#available-types)
        *   [Common properties](https://docs.python.org/3/library/datetime.html#common-properties)
            
        *   [Determining if an object is aware or naive](https://docs.python.org/3/library/datetime.html#determining-if-an-object-is-aware-or-naive)
            
    *   [`timedelta` objects](https://docs.python.org/3/library/datetime.html#timedelta-objects)
        *   [Examples of usage: `timedelta`](https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta)
            
    *   [`date` objects](https://docs.python.org/3/library/datetime.html#date-objects)
        *   [Examples of usage: `date`](https://docs.python.org/3/library/datetime.html#examples-of-usage-date)
            
    *   [`datetime` objects](https://docs.python.org/3/library/datetime.html#datetime-objects)
        *   [Examples of usage: `datetime`](https://docs.python.org/3/library/datetime.html#examples-of-usage-datetime)
            
    *   [`time` objects](https://docs.python.org/3/library/datetime.html#time-objects)
        *   [Examples of usage: `time`](https://docs.python.org/3/library/datetime.html#examples-of-usage-time)
            
    *   [`tzinfo` objects](https://docs.python.org/3/library/datetime.html#tzinfo-objects)
        
    *   [`timezone` objects](https://docs.python.org/3/library/datetime.html#timezone-objects)
        
    *   [`strftime()` and `strptime()` behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
        *   [`strftime()` and `strptime()` format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
            
        *   [Technical detail](https://docs.python.org/3/library/datetime.html#technical-detail)
            
*   [`zoneinfo` — IANA time zone support](https://docs.python.org/3/library/zoneinfo.html)
    *   [Using `ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#using-zoneinfo)
        
    *   [Data sources](https://docs.python.org/3/library/zoneinfo.html#data-sources)
        *   [Configuring the data sources](https://docs.python.org/3/library/zoneinfo.html#configuring-the-data-sources)
            *   [Compile-time configuration](https://docs.python.org/3/library/zoneinfo.html#compile-time-configuration)
                
            *   [Environment configuration](https://docs.python.org/3/library/zoneinfo.html#environment-configuration)
                
            *   [Runtime configuration](https://docs.python.org/3/library/zoneinfo.html#runtime-configuration)
                
    *   [The `ZoneInfo` class](https://docs.python.org/3/library/zoneinfo.html#the-zoneinfo-class)
        *   [String representations](https://docs.python.org/3/library/zoneinfo.html#string-representations)
            
        *   [Pickle serialization](https://docs.python.org/3/library/zoneinfo.html#pickle-serialization)
            
    *   [Functions](https://docs.python.org/3/library/zoneinfo.html#functions)
        
    *   [Globals](https://docs.python.org/3/library/zoneinfo.html#globals)
        
    *   [Exceptions and warnings](https://docs.python.org/3/library/zoneinfo.html#exceptions-and-warnings)
        
*   [`calendar` — General calendar-related functions](https://docs.python.org/3/library/calendar.html)
    *   [Command-line usage](https://docs.python.org/3/library/calendar.html#command-line-usage)
        
*   [`collections` — Container datatypes](https://docs.python.org/3/library/collections.html)
    *   [`ChainMap` objects](https://docs.python.org/3/library/collections.html#chainmap-objects)
        *   [`ChainMap` Examples and Recipes](https://docs.python.org/3/library/collections.html#chainmap-examples-and-recipes)
            
    *   [`Counter` objects](https://docs.python.org/3/library/collections.html#counter-objects)
        
    *   [`deque` objects](https://docs.python.org/3/library/collections.html#deque-objects)
        *   [`deque` Recipes](https://docs.python.org/3/library/collections.html#deque-recipes)
            
    *   [`defaultdict` objects](https://docs.python.org/3/library/collections.html#defaultdict-objects)
        *   [`defaultdict` Examples](https://docs.python.org/3/library/collections.html#defaultdict-examples)
            
    *   [`namedtuple()` Factory Function for Tuples with Named Fields](https://docs.python.org/3/library/collections.html#namedtuple-factory-function-for-tuples-with-named-fields)
        
    *   [`OrderedDict` objects](https://docs.python.org/3/library/collections.html#ordereddict-objects)
        *   [`OrderedDict` Examples and Recipes](https://docs.python.org/3/library/collections.html#ordereddict-examples-and-recipes)
            
    *   [`UserDict` objects](https://docs.python.org/3/library/collections.html#userdict-objects)
        
    *   [`UserList` objects](https://docs.python.org/3/library/collections.html#userlist-objects)
        
    *   [`UserString` objects](https://docs.python.org/3/library/collections.html#userstring-objects)
        
*   [`collections.abc` — Abstract Base Classes for Containers](https://docs.python.org/3/library/collections.abc.html)
    *   [Collections Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes)
        
    *   [Collections Abstract Base Classes – Detailed Descriptions](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes-detailed-descriptions)
        
    *   [Examples and Recipes](https://docs.python.org/3/library/collections.abc.html#examples-and-recipes)
        
*   [`heapq` — Heap queue algorithm](https://docs.python.org/3/library/heapq.html)
    *   [Basic Examples](https://docs.python.org/3/library/heapq.html#basic-examples)
        
    *   [Other Applications](https://docs.python.org/3/library/heapq.html#other-applications)
        
    *   [Priority Queue Implementation Notes](https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes)
        
    *   [Theory](https://docs.python.org/3/library/heapq.html#theory)
        
*   [`bisect` — Array bisection algorithm](https://docs.python.org/3/library/bisect.html)
    *   [Performance Notes](https://docs.python.org/3/library/bisect.html#performance-notes)
        
    *   [Searching Sorted Lists](https://docs.python.org/3/library/bisect.html#searching-sorted-lists)
        
    *   [Examples](https://docs.python.org/3/library/bisect.html#examples)
        
*   [`array` — Efficient arrays of numeric values](https://docs.python.org/3/library/array.html)
    
*   [`weakref` — Weak references](https://docs.python.org/3/library/weakref.html)
    *   [Weak Reference Objects](https://docs.python.org/3/library/weakref.html#weak-reference-objects)
        
    *   [Example](https://docs.python.org/3/library/weakref.html#example)
        
    *   [Finalizer Objects](https://docs.python.org/3/library/weakref.html#finalizer-objects)
        
    *   [Comparing finalizers with `__del__()` methods](https://docs.python.org/3/library/weakref.html#comparing-finalizers-with-del-methods)
        
*   [`types` — Dynamic type creation and names for built-in types](https://docs.python.org/3/library/types.html)
    *   [Dynamic Type Creation](https://docs.python.org/3/library/types.html#dynamic-type-creation)
        
    *   [Standard Interpreter Types](https://docs.python.org/3/library/types.html#standard-interpreter-types)
        
    *   [Additional Utility Classes and Functions](https://docs.python.org/3/library/types.html#additional-utility-classes-and-functions)
        
    *   [Coroutine Utility Functions](https://docs.python.org/3/library/types.html#coroutine-utility-functions)
        
*   [`copy` — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html)
    
*   [`pprint` — Data pretty printer](https://docs.python.org/3/library/pprint.html)
    *   [Functions](https://docs.python.org/3/library/pprint.html#functions)
        
    *   [PrettyPrinter Objects](https://docs.python.org/3/library/pprint.html#prettyprinter-objects)
        
    *   [Example](https://docs.python.org/3/library/pprint.html#example)
        
*   [`reprlib` — Alternate `repr()` implementation](https://docs.python.org/3/library/reprlib.html)
    *   [Repr Objects](https://docs.python.org/3/library/reprlib.html#repr-objects)
        
    *   [Subclassing Repr Objects](https://docs.python.org/3/library/reprlib.html#subclassing-repr-objects)
        
*   [`enum` — Support for enumerations](https://docs.python.org/3/library/enum.html)
    *   [Module contents](https://docs.python.org/3/library/enum.html#module-contents)
        
    *   [Data types](https://docs.python.org/3/library/enum.html#data-types)
        *   [Supported `__dunder__` names](https://docs.python.org/3/library/enum.html#supported-dunder-names)
            
        *   [Supported `_sunder_` names](https://docs.python.org/3/library/enum.html#supported-sunder-names)
            
    *   [Utilities and decorators](https://docs.python.org/3/library/enum.html#utilities-and-decorators)
        
    *   [Notes](https://docs.python.org/3/library/enum.html#notes)
        
*   [`graphlib` — Functionality to operate with graph-like structures](https://docs.python.org/3/library/graphlib.html)
    *   [Exceptions](https://docs.python.org/3/library/graphlib.html#exceptions)
        

#### Previous topic

[`codecs` — Codec registry and base classes](https://docs.python.org/3/library/codecs.html "previous chapter")

#### Next topic

[`datetime` — Basic date and time types](https://docs.python.org/3/library/datetime.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Data+Types&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdatatypes.html&pagesource=library%2Fdatatypes.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/datatypes.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/datetime.html "datetime — Basic date and time types")
     |
*   [previous](https://docs.python.org/3/library/codecs.html "codecs — Codec registry and base classes")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Data Types](https://docs.python.org/3/library/datatypes.html)
    
*    
    
    |
*   Theme Auto Light Dark |