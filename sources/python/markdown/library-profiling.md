### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/profiling.tracing.html "profiling.tracing — Deterministic profiler")
     |
*   [previous](https://docs.python.org/3/library/pdb.html "pdb — The Python Debugger")
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
     »
*   [`profiling` — Python profilers](https://docs.python.org/3/library/profiling.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`profiling` — Python profilers[¶](https://docs.python.org/3/library/profiling.html#module-profiling "Link to this heading")

============================================================================================================================

Added in version 3.15.

**Source code:** [Lib/profiling/](https://github.com/python/cpython/tree/3.15/Lib/profiling/)

* * *

Introduction to profiling[¶](https://docs.python.org/3/library/profiling.html#introduction-to-profiling "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

A _profile_ is a set of statistics that describes how often and for how long various parts of a program execute. These statistics help identify performance bottlenecks and guide optimization efforts. Python provides two fundamentally different approaches to collecting this information: statistical sampling and deterministic tracing.

The `profiling` package organizes Python’s built-in profiling tools under a single namespace. It contains two submodules, each implementing a different profiling methodology:

[`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")

A statistical profiler that periodically samples the call stack. Run scripts directly or attach to running processes by PID. Provides multiple output formats (flame graphs, heatmaps, Firefox Profiler), GIL analysis, GC tracking, and multiple profiling modes (wall-clock, CPU, GIL) with virtually no overhead.

[`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")

A deterministic profiler that traces every function call, return, and exception event. Provides exact call counts and precise timing information, capturing every invocation including very fast functions.

Note

The profiler modules are designed to provide an execution profile for a given program, not for benchmarking purposes. For benchmarking, use the [`timeit`](https://docs.python.org/3/library/timeit.html#module-timeit "timeit: Measure the execution time of small code snippets.")
 module, which provides reasonably accurate timing measurements. This distinction is particularly important when comparing Python code against C code: deterministic profilers introduce overhead for Python code but not for C-level functions, which can skew comparisons.

Choosing a profiler[¶](https://docs.python.org/3/library/profiling.html#choosing-a-profiler "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

For most performance analysis, use the statistical profiler ([`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")
). It has minimal overhead, works for both development and production, and provides rich visualization options including flame graphs, heatmaps, GIL analysis, and more.

Use the deterministic profiler ([`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
) when you need **exact call counts** and cannot afford to miss any function calls. Since it instruments every function call and return, it will capture even very fast functions that complete between sampling intervals. The tradeoff is higher overhead.

The following table summarizes the key differences:

| Feature | Statistical sampling ([`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")<br>) | Deterministic ([`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")<br>) |
| --- | --- | --- |
| **Overhead** | Virtually none | Moderate |
| **Accuracy** | Statistical estimate | Exact call counts |
| **Output formats** | pstats, flame graph, heatmap, gecko, collapsed | pstats |
| **Profiling modes** | Wall-clock, CPU, GIL | Wall-clock |
| **Special frames** | GC, native (C extensions) | N/A |
| **Attach to PID** | Yes | No  |

### When to use statistical sampling[¶](https://docs.python.org/3/library/profiling.html#when-to-use-statistical-sampling "Link to this heading")

The statistical profiler ([`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")
) is recommended for most performance analysis tasks. Use it the same way you would use [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
:

Copy

python \-m profiling.sampling run script.py

One of the main strengths of the sampling profiler is its variety of output formats. Beyond traditional pstats tables, it can generate interactive flame graphs that visualize call hierarchies, line-level source heatmaps that show exactly where time is spent in your code, and Firefox Profiler output for timeline-based analysis.

The profiler also provides insight into Python interpreter behavior that deterministic profiling cannot capture. Use `--mode gil` to identify GIL contention in multi-threaded code, `--mode cpu` to measure actual CPU time excluding I/O waits, or inspect `<GC>` frames to understand garbage collection overhead. The `--native` option reveals time spent in C extensions, helping distinguish Python overhead from library performance.

For multi-threaded applications, the `-a` option samples all threads simultaneously, showing how work is distributed. And for production debugging, the `attach` command connects to any running Python process by PID without requiring a restart or code changes.

### When to use deterministic tracing[¶](https://docs.python.org/3/library/profiling.html#when-to-use-deterministic-tracing "Link to this heading")

The deterministic profiler ([`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
) instruments every function call and return. This approach has higher overhead than sampling, but guarantees complete coverage of program execution.

The primary reason to choose deterministic tracing is when you need exact call counts. Statistical profiling estimates frequency based on sampling, which may undercount short-lived functions that complete between samples. If you need to verify that an optimization actually reduced the number of function calls, or if you want to trace the complete call graph to understand caller-callee relationships, deterministic tracing is the right choice.

Deterministic tracing also excels at capturing functions that execute in microseconds. Such functions may not appear frequently enough in statistical samples, but deterministic tracing records every invocation regardless of duration.

Quick start[¶](https://docs.python.org/3/library/profiling.html#quick-start "Link to this heading")

----------------------------------------------------------------------------------------------------

This section provides the minimal steps needed to start profiling. For complete documentation, see the dedicated pages for each profiler.

### Statistical profiling[¶](https://docs.python.org/3/library/profiling.html#statistical-profiling "Link to this heading")

To profile a script, use the [`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")
 module with the `run` command:

Copy

python \-m profiling.sampling run script.py
python \-m profiling.sampling run \-m mypackage.module

This runs the script under the profiler and prints a summary of where time was spent. For an interactive flame graph:

Copy

python \-m profiling.sampling run \--flamegraph script.py

To profile an already-running process, use the `attach` command with the process ID:

Copy

python \-m profiling.sampling attach 1234

For custom settings, specify the sampling interval (in microseconds) and duration (in seconds):

Copy

python \-m profiling.sampling run \-i 50 \-d 30 script.py

### Deterministic profiling[¶](https://docs.python.org/3/library/profiling.html#deterministic-profiling "Link to this heading")

To profile a script from the command line:

Copy

python \-m profiling.tracing script.py

To profile a piece of code programmatically:

Copy

import profiling.tracing
profiling.tracing.run('my\_function()')

This executes the given code under the profiler and prints a summary showing exact function call counts and timing.

Understanding profile output[¶](https://docs.python.org/3/library/profiling.html#understanding-profile-output "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Both profilers collect function-level statistics, though they present them in different formats. The sampling profiler offers multiple visualizations (flame graphs, heatmaps, Firefox Profiler, pstats tables), while the deterministic profiler produces pstats-compatible output. Regardless of format, the underlying concepts are the same.

Key profiling concepts:

**Direct time** (also called _self time_ or _tottime_)

Time spent executing code in the function itself, excluding time spent in functions it called. High direct time indicates the function contains expensive operations.

**Cumulative time** (also called _total time_ or _cumtime_)

Time spent in the function and all functions it called. This measures the total cost of calling a function, including its entire call subtree.

**Call count** (also called _ncalls_ or _samples_)

How many times the function was called (deterministic) or sampled (statistical). In deterministic profiling, this is exact. In statistical profiling, it represents the number of times the function appeared in a stack sample.

**Primitive calls**

Calls that are not induced by recursion. When a function recurses, the total call count includes recursive invocations, but primitive calls counts only the initial entry. Displayed as `total/primitive` (for example, `3/1` means three total calls, one primitive).

**Caller/Callee relationships**

Which functions called a given function (callers) and which functions it called (callees). Flame graphs visualize this as nested rectangles; pstats can display it via the [`print_callers()`](https://docs.python.org/3/library/pstats.html#pstats.Stats.print_callers "pstats.Stats.print_callers")
 and [`print_callees()`](https://docs.python.org/3/library/pstats.html#pstats.Stats.print_callees "pstats.Stats.print_callees")
 methods.

Legacy compatibility[¶](https://docs.python.org/3/library/profiling.html#legacy-compatibility "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

For backward compatibility, the `cProfile` module remains available as an alias to [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
. Existing code using `import cProfile` will continue to work without modification in all future Python versions.

Deprecated since version 3.15: The pure Python [`profile`](https://docs.python.org/3/library/profile.html#module-profile "profile: Pure Python profiler (deprecated). (deprecated)")
 module is deprecated and will be removed in Python 3.17. Use [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
 (or its alias `cProfile`) instead. See `profile` for migration guidance.

See also

[`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")

Statistical sampling profiler with flame graphs, heatmaps, and GIL analysis. Recommended for most users.

[`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")

Deterministic tracing profiler for exact call counts.

[`pstats`](https://docs.python.org/3/library/pstats.html#module-pstats "pstats: Statistics object for analyzing profiler output.")

Statistics analysis and formatting for profile data.

[`timeit`](https://docs.python.org/3/library/timeit.html#module-timeit "timeit: Measure the execution time of small code snippets.")

Module for measuring execution time of small code snippets.

Submodules

*   [`profiling.tracing` — Deterministic profiler](https://docs.python.org/3/library/profiling.tracing.html)
    
*   [`profiling.sampling` — Statistical profiler](https://docs.python.org/3/library/profiling.sampling.html)
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`profiling` — Python profilers](https://docs.python.org/3/library/profiling.html#)
    *   [Introduction to profiling](https://docs.python.org/3/library/profiling.html#introduction-to-profiling)
        
    *   [Choosing a profiler](https://docs.python.org/3/library/profiling.html#choosing-a-profiler)
        *   [When to use statistical sampling](https://docs.python.org/3/library/profiling.html#when-to-use-statistical-sampling)
            
        *   [When to use deterministic tracing](https://docs.python.org/3/library/profiling.html#when-to-use-deterministic-tracing)
            
    *   [Quick start](https://docs.python.org/3/library/profiling.html#quick-start)
        *   [Statistical profiling](https://docs.python.org/3/library/profiling.html#statistical-profiling)
            
        *   [Deterministic profiling](https://docs.python.org/3/library/profiling.html#deterministic-profiling)
            
    *   [Understanding profile output](https://docs.python.org/3/library/profiling.html#understanding-profile-output)
        
    *   [Legacy compatibility](https://docs.python.org/3/library/profiling.html#legacy-compatibility)
        

#### Previous topic

[`pdb` — The Python Debugger](https://docs.python.org/3/library/pdb.html "previous chapter")

#### Next topic

[`profiling.tracing` — Deterministic profiler](https://docs.python.org/3/library/profiling.tracing.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=profiling+%E2%80%94+Python+profilers&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fprofiling.html&pagesource=library%2Fprofiling.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/profiling.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/profiling.tracing.html "profiling.tracing — Deterministic profiler")
     |
*   [previous](https://docs.python.org/3/library/pdb.html "pdb — The Python Debugger")
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
     »
*   [`profiling` — Python profilers](https://docs.python.org/3/library/profiling.html)
    
*    
    
    |
*   Theme Auto Light Dark |