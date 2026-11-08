### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/perfmaps.html "Support for Perf Maps")
     |
*   [previous](https://docs.python.org/3/c-api/codec.html "Codec registry and support functions")
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
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [PyTime C API](https://docs.python.org/3/c-api/time.html)
    
*    
    
    |
*   Theme Auto Light Dark |

PyTime C API[¶](https://docs.python.org/3/c-api/time.html#pytime-c-api "Link to this heading")

===============================================================================================

Added in version 3.13.

The clock C API provides access to system clocks. It is similar to the Python [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.")
 module.

For C API related to the [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
 module, see [DateTime Objects](https://docs.python.org/3/c-api/datetime.html#datetimeobjects)
.

Types[¶](https://docs.python.org/3/c-api/time.html#types "Link to this heading")

---------------------------------------------------------------------------------

type PyTime\_t[¶](https://docs.python.org/3/c-api/time.html#c.PyTime_t "Link to this definition")
  

A timestamp or duration in nanoseconds, represented as a signed 64-bit integer.

The reference point for timestamps depends on the clock used. For example, [`PyTime_Time()`](https://docs.python.org/3/c-api/time.html#c.PyTime_Time "PyTime_Time")
 returns timestamps relative to the UNIX epoch.

The supported range is around \[-292.3 years; +292.3 years\]. Using the Unix epoch (January 1st, 1970) as reference, the supported date range is around \[1677-09-21; 2262-04-11\]. The exact limits are exposed as constants:

[PyTime\_t](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
 PyTime\_MIN[¶](https://docs.python.org/3/c-api/time.html#c.PyTime_MIN "Link to this definition")
  

Minimum value of [`PyTime_t`](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
.

[PyTime\_t](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
 PyTime\_MAX[¶](https://docs.python.org/3/c-api/time.html#c.PyTime_MAX "Link to this definition")
  

Maximum value of [`PyTime_t`](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
.

Clock Functions[¶](https://docs.python.org/3/c-api/time.html#clock-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------

The following functions take a pointer to a [PyTime\_t](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
 that they set to the value of a particular clock. Details of each clock are given in the documentation of the corresponding Python function.

The functions return `0` on success, or `-1` (with an exception set) on failure.

On integer overflow, they set the [`PyExc_OverflowError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_OverflowError "PyExc_OverflowError")
 exception and set `*result` to the value clamped to the `[PyTime_MIN; PyTime_MAX]` range. (On current systems, integer overflows are likely caused by misconfigured system time.)

As any other C API (unless otherwise specified), the functions must be called with an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

int PyTime\_Monotonic([PyTime\_t](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
 \*result)[¶](https://docs.python.org/3/c-api/time.html#c.PyTime_Monotonic "Link to this definition")
  

Read the monotonic clock. See [`time.monotonic()`](https://docs.python.org/3/library/time.html#time.monotonic "time.monotonic")
 for important details on this clock.

int PyTime\_PerfCounter([PyTime\_t](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
 \*result)[¶](https://docs.python.org/3/c-api/time.html#c.PyTime_PerfCounter "Link to this definition")
  

Read the performance counter. See [`time.perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter")
 for important details on this clock.

int PyTime\_Time([PyTime\_t](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
 \*result)[¶](https://docs.python.org/3/c-api/time.html#c.PyTime_Time "Link to this definition")
  

Read the “wall clock” time. See [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
 for details important on this clock.

Raw Clock Functions[¶](https://docs.python.org/3/c-api/time.html#raw-clock-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------

Similar to clock functions, but don’t set an exception on error and don’t require the caller to have an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

On success, the functions return `0`.

On failure, they set `*result` to `0` and return `-1`, _without_ setting an exception. To get the cause of the error, [attach](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 a [thread state](https://docs.python.org/3/glossary.html#term-thread-state)
, and call the regular (non-`Raw`) function. Note that the regular function may succeed after the `Raw` one failed.

int PyTime\_MonotonicRaw([PyTime\_t](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
 \*result)[¶](https://docs.python.org/3/c-api/time.html#c.PyTime_MonotonicRaw "Link to this definition")
  

Similar to [`PyTime_Monotonic()`](https://docs.python.org/3/c-api/time.html#c.PyTime_Monotonic "PyTime_Monotonic")
, but don’t set an exception on error and don’t require an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

int PyTime\_PerfCounterRaw([PyTime\_t](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
 \*result)[¶](https://docs.python.org/3/c-api/time.html#c.PyTime_PerfCounterRaw "Link to this definition")
  

Similar to [`PyTime_PerfCounter()`](https://docs.python.org/3/c-api/time.html#c.PyTime_PerfCounter "PyTime_PerfCounter")
, but don’t set an exception on error and don’t require an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

int PyTime\_TimeRaw([PyTime\_t](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
 \*result)[¶](https://docs.python.org/3/c-api/time.html#c.PyTime_TimeRaw "Link to this definition")
  

Similar to [`PyTime_Time()`](https://docs.python.org/3/c-api/time.html#c.PyTime_Time "PyTime_Time")
, but don’t set an exception on error and don’t require an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

Conversion functions[¶](https://docs.python.org/3/c-api/time.html#conversion-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------

double PyTime\_AsSecondsDouble([PyTime\_t](https://docs.python.org/3/c-api/time.html#c.PyTime_t "PyTime_t")
 t)[¶](https://docs.python.org/3/c-api/time.html#c.PyTime_AsSecondsDouble "Link to this definition")
  

Convert a timestamp to a number of seconds as a C double.

The function cannot fail, but note that double has limited accuracy for large values.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [PyTime C API](https://docs.python.org/3/c-api/time.html#)
    *   [Types](https://docs.python.org/3/c-api/time.html#types)
        
    *   [Clock Functions](https://docs.python.org/3/c-api/time.html#clock-functions)
        
    *   [Raw Clock Functions](https://docs.python.org/3/c-api/time.html#raw-clock-functions)
        
    *   [Conversion functions](https://docs.python.org/3/c-api/time.html#conversion-functions)
        

#### Previous topic

[Codec registry and support functions](https://docs.python.org/3/c-api/codec.html "previous chapter")

#### Next topic

[Support for Perf Maps](https://docs.python.org/3/c-api/perfmaps.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=PyTime+C+API&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Ftime.html&pagesource=c-api%2Ftime.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/time.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/perfmaps.html "Support for Perf Maps")
     |
*   [previous](https://docs.python.org/3/c-api/codec.html "Codec registry and support functions")
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
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [PyTime C API](https://docs.python.org/3/c-api/time.html)
    
*    
    
    |
*   Theme Auto Light Dark |