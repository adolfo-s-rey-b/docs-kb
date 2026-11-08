### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/audit_events.html "Audit events table")
     |
*   [previous](https://docs.python.org/3/library/test.html "test — Regression tests package for Python")
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
*   [Debugging and profiling](https://docs.python.org/3/library/debug.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Debugging and profiling[¶](https://docs.python.org/3/library/debug.html#debugging-and-profiling "Link to this heading")

========================================================================================================================

These libraries help you with Python development: the debugger enables you to step through code, analyze stack frames and set breakpoints etc., and the profilers run code and give you a detailed breakdown of execution times, allowing you to identify bottlenecks in your programs. Auditing events provide visibility into runtime behaviors that would otherwise require intrusive debugging or patching.

*   [Audit events table](https://docs.python.org/3/library/audit_events.html)
    
*   [`bdb` — Debugger framework](https://docs.python.org/3/library/bdb.html)
    
*   [`faulthandler` — Dump the Python traceback](https://docs.python.org/3/library/faulthandler.html)
    *   [Dumping the traceback](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback)
        
    *   [Dumping the C stack](https://docs.python.org/3/library/faulthandler.html#dumping-the-c-stack)
        *   [C Stack Compatibility](https://docs.python.org/3/library/faulthandler.html#c-stack-compatibility)
            
    *   [Fault handler state](https://docs.python.org/3/library/faulthandler.html#fault-handler-state)
        
    *   [Dumping the tracebacks after a timeout](https://docs.python.org/3/library/faulthandler.html#dumping-the-tracebacks-after-a-timeout)
        
    *   [Dumping the traceback on a user signal](https://docs.python.org/3/library/faulthandler.html#dumping-the-traceback-on-a-user-signal)
        
    *   [Issue with file descriptors](https://docs.python.org/3/library/faulthandler.html#issue-with-file-descriptors)
        
    *   [Example](https://docs.python.org/3/library/faulthandler.html#example)
        
*   [`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html)
    *   [Command-line interface](https://docs.python.org/3/library/pdb.html#command-line-interface)
        
    *   [Debugger commands](https://docs.python.org/3/library/pdb.html#debugger-commands)
        
*   [`profiling` — Python profilers](https://docs.python.org/3/library/profiling.html)
    *   [Introduction to profiling](https://docs.python.org/3/library/profiling.html#introduction-to-profiling)
        
    *   [Choosing a profiler](https://docs.python.org/3/library/profiling.html#choosing-a-profiler)
        *   [When to use statistical sampling](https://docs.python.org/3/library/profiling.html#when-to-use-statistical-sampling)
            
        *   [When to use deterministic tracing](https://docs.python.org/3/library/profiling.html#when-to-use-deterministic-tracing)
            
    *   [Quick start](https://docs.python.org/3/library/profiling.html#quick-start)
        *   [Statistical profiling](https://docs.python.org/3/library/profiling.html#statistical-profiling)
            
        *   [Deterministic profiling](https://docs.python.org/3/library/profiling.html#deterministic-profiling)
            
    *   [Understanding profile output](https://docs.python.org/3/library/profiling.html#understanding-profile-output)
        
    *   [Legacy compatibility](https://docs.python.org/3/library/profiling.html#legacy-compatibility)
        *   [`profiling.tracing` — Deterministic profiler](https://docs.python.org/3/library/profiling.tracing.html)
            *   [What is deterministic profiling?](https://docs.python.org/3/library/profiling.tracing.html#what-is-deterministic-profiling)
                
            *   [Command-line interface](https://docs.python.org/3/library/profiling.tracing.html#command-line-interface)
                
            *   [Programmatic usage examples](https://docs.python.org/3/library/profiling.tracing.html#programmatic-usage-examples)
                *   [Basic profiling](https://docs.python.org/3/library/profiling.tracing.html#basic-profiling)
                    
                *   [Using the `Profile` class](https://docs.python.org/3/library/profiling.tracing.html#using-the-profile-class)
                    
            *   [Module reference](https://docs.python.org/3/library/profiling.tracing.html#module-reference)
                
            *   [Using a custom timer](https://docs.python.org/3/library/profiling.tracing.html#using-a-custom-timer)
                
            *   [Limitations](https://docs.python.org/3/library/profiling.tracing.html#limitations)
                
        *   [`profiling.sampling` — Statistical profiler](https://docs.python.org/3/library/profiling.sampling.html)
            *   [What is statistical profiling?](https://docs.python.org/3/library/profiling.sampling.html#what-is-statistical-profiling)
                *   [How time is estimated](https://docs.python.org/3/library/profiling.sampling.html#how-time-is-estimated)
                    
                *   [When to use a different approach](https://docs.python.org/3/library/profiling.sampling.html#when-to-use-a-different-approach)
                    
            *   [Quick examples](https://docs.python.org/3/library/profiling.sampling.html#quick-examples)
                
            *   [Commands](https://docs.python.org/3/library/profiling.sampling.html#commands)
                *   [The `run` command](https://docs.python.org/3/library/profiling.sampling.html#the-run-command)
                    
                *   [The `attach` command](https://docs.python.org/3/library/profiling.sampling.html#the-attach-command)
                    
                *   [The `dump` command](https://docs.python.org/3/library/profiling.sampling.html#the-dump-command)
                    
                *   [The `replay` command](https://docs.python.org/3/library/profiling.sampling.html#the-replay-command)
                    
                *   [Profiling in production](https://docs.python.org/3/library/profiling.sampling.html#profiling-in-production)
                    
                *   [Platform requirements](https://docs.python.org/3/library/profiling.sampling.html#platform-requirements)
                    
                *   [Version compatibility](https://docs.python.org/3/library/profiling.sampling.html#version-compatibility)
                    
            *   [Sampling configuration](https://docs.python.org/3/library/profiling.sampling.html#sampling-configuration)
                *   [Sampling rate and duration](https://docs.python.org/3/library/profiling.sampling.html#sampling-rate-and-duration)
                    
                *   [Thread selection](https://docs.python.org/3/library/profiling.sampling.html#thread-selection)
                    
                *   [Blocking mode](https://docs.python.org/3/library/profiling.sampling.html#blocking-mode)
                    
                *   [Special frames](https://docs.python.org/3/library/profiling.sampling.html#special-frames)
                    
                *   [Opcode-aware profiling](https://docs.python.org/3/library/profiling.sampling.html#opcode-aware-profiling)
                    
                *   [Real-time statistics](https://docs.python.org/3/library/profiling.sampling.html#real-time-statistics)
                    
                *   [Subprocess profiling](https://docs.python.org/3/library/profiling.sampling.html#subprocess-profiling)
                    
                *   [Sampling efficiency](https://docs.python.org/3/library/profiling.sampling.html#sampling-efficiency)
                    
            *   [Profiling modes](https://docs.python.org/3/library/profiling.sampling.html#profiling-modes)
                *   [Wall-clock mode](https://docs.python.org/3/library/profiling.sampling.html#wall-clock-mode)
                    
                *   [CPU mode](https://docs.python.org/3/library/profiling.sampling.html#cpu-mode)
                    
                *   [Comparing wall-clock and CPU profiles](https://docs.python.org/3/library/profiling.sampling.html#comparing-wall-clock-and-cpu-profiles)
                    
                *   [GIL mode](https://docs.python.org/3/library/profiling.sampling.html#gil-mode)
                    
                *   [Exception mode](https://docs.python.org/3/library/profiling.sampling.html#exception-mode)
                    
            *   [Output formats](https://docs.python.org/3/library/profiling.sampling.html#output-formats)
                *   [pstats format](https://docs.python.org/3/library/profiling.sampling.html#pstats-format)
                    
                *   [Collapsed stacks format](https://docs.python.org/3/library/profiling.sampling.html#collapsed-stacks-format)
                    
                *   [Flame graph format](https://docs.python.org/3/library/profiling.sampling.html#flame-graph-format)
                    *   [Differential flame graphs](https://docs.python.org/3/library/profiling.sampling.html#differential-flame-graphs)
                        
                *   [Gecko format](https://docs.python.org/3/library/profiling.sampling.html#gecko-format)
                    
                *   [Heatmap format](https://docs.python.org/3/library/profiling.sampling.html#heatmap-format)
                    
                *   [Binary format](https://docs.python.org/3/library/profiling.sampling.html#binary-format)
                    
            *   [Record and replay workflow](https://docs.python.org/3/library/profiling.sampling.html#record-and-replay-workflow)
                
            *   [Live mode](https://docs.python.org/3/library/profiling.sampling.html#live-mode)
                *   [Keyboard commands](https://docs.python.org/3/library/profiling.sampling.html#keyboard-commands)
                    
            *   [Async-aware profiling](https://docs.python.org/3/library/profiling.sampling.html#async-aware-profiling)
                *   [Async modes](https://docs.python.org/3/library/profiling.sampling.html#async-modes)
                    
                *   [Task markers and stack reconstruction](https://docs.python.org/3/library/profiling.sampling.html#task-markers-and-stack-reconstruction)
                    
                *   [Option restrictions](https://docs.python.org/3/library/profiling.sampling.html#option-restrictions)
                    
            *   [Command-line interface](https://docs.python.org/3/library/profiling.sampling.html#command-line-interface)
                *   [Global options](https://docs.python.org/3/library/profiling.sampling.html#global-options)
                    
                *   [Dump options](https://docs.python.org/3/library/profiling.sampling.html#dump-options)
                    
                *   [Sampling options](https://docs.python.org/3/library/profiling.sampling.html#sampling-options)
                    
                *   [Mode options](https://docs.python.org/3/library/profiling.sampling.html#mode-options)
                    
                *   [Output options](https://docs.python.org/3/library/profiling.sampling.html#output-options)
                    
                *   [pstats display options](https://docs.python.org/3/library/profiling.sampling.html#pstats-display-options)
                    
                *   [Run command options](https://docs.python.org/3/library/profiling.sampling.html#run-command-options)
                    
*   [`pstats` — Statistics for profilers](https://docs.python.org/3/library/pstats.html)
    *   [Reading and displaying profile data](https://docs.python.org/3/library/pstats.html#reading-and-displaying-profile-data)
        *   [Working with statistics](https://docs.python.org/3/library/pstats.html#working-with-statistics)
            
        *   [Filtering output](https://docs.python.org/3/library/pstats.html#filtering-output)
            
        *   [Analyzing call relationships](https://docs.python.org/3/library/pstats.html#analyzing-call-relationships)
            
        *   [Combining multiple profiles](https://docs.python.org/3/library/pstats.html#combining-multiple-profiles)
            
    *   [The `Stats` class](https://docs.python.org/3/library/pstats.html#the-stats-class)
        
    *   [Command-line interface](https://docs.python.org/3/library/pstats.html#command-line-interface)
        
*   [`timeit` — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html)
    *   [Basic examples](https://docs.python.org/3/library/timeit.html#basic-examples)
        
    *   [Python interface](https://docs.python.org/3/library/timeit.html#python-interface)
        
    *   [Command-line interface](https://docs.python.org/3/library/timeit.html#command-line-interface)
        
    *   [Examples](https://docs.python.org/3/library/timeit.html#examples)
        
*   [`trace` — Trace or track Python statement execution](https://docs.python.org/3/library/trace.html)
    *   [Command-Line Usage](https://docs.python.org/3/library/trace.html#command-line-usage)
        *   [Main options](https://docs.python.org/3/library/trace.html#main-options)
            
        *   [Modifiers](https://docs.python.org/3/library/trace.html#modifiers)
            
        *   [Filters](https://docs.python.org/3/library/trace.html#filters)
            
    *   [Programmatic Interface](https://docs.python.org/3/library/trace.html#programmatic-interface)
        
*   [`tracemalloc` — Trace memory allocations](https://docs.python.org/3/library/tracemalloc.html)
    *   [Examples](https://docs.python.org/3/library/tracemalloc.html#examples)
        *   [Display the top 10](https://docs.python.org/3/library/tracemalloc.html#display-the-top-10)
            
        *   [Compute differences](https://docs.python.org/3/library/tracemalloc.html#compute-differences)
            
        *   [Get the traceback of a memory block](https://docs.python.org/3/library/tracemalloc.html#get-the-traceback-of-a-memory-block)
            
        *   [Pretty top](https://docs.python.org/3/library/tracemalloc.html#pretty-top)
            *   [Record the current and peak size of all traced memory blocks](https://docs.python.org/3/library/tracemalloc.html#record-the-current-and-peak-size-of-all-traced-memory-blocks)
                
    *   [API](https://docs.python.org/3/library/tracemalloc.html#api)
        *   [Functions](https://docs.python.org/3/library/tracemalloc.html#functions)
            
        *   [DomainFilter](https://docs.python.org/3/library/tracemalloc.html#domainfilter)
            
        *   [Filter](https://docs.python.org/3/library/tracemalloc.html#filter)
            
        *   [Frame](https://docs.python.org/3/library/tracemalloc.html#frame)
            
        *   [Snapshot](https://docs.python.org/3/library/tracemalloc.html#snapshot)
            
        *   [Statistic](https://docs.python.org/3/library/tracemalloc.html#statistic)
            
        *   [StatisticDiff](https://docs.python.org/3/library/tracemalloc.html#statisticdiff)
            
        *   [Trace](https://docs.python.org/3/library/tracemalloc.html#trace)
            
        *   [Traceback](https://docs.python.org/3/library/tracemalloc.html#traceback)
            

#### Previous topic

[`test` — Regression tests package for Python](https://docs.python.org/3/library/test.html "previous chapter")

#### Next topic

[Audit events table](https://docs.python.org/3/library/audit_events.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Debugging+and+profiling&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdebug.html&pagesource=library%2Fdebug.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/debug.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/audit_events.html "Audit events table")
     |
*   [previous](https://docs.python.org/3/library/test.html "test — Regression tests package for Python")
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
*   [Debugging and profiling](https://docs.python.org/3/library/debug.html)
    
*    
    
    |
*   Theme Auto Light Dark |