### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/profiling.sampling.html "profiling.sampling — Statistical profiler")
     |
*   [previous](https://docs.python.org/3/library/profiling.html "profiling — Python profilers")
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
     »
*   [`profiling.tracing` — Deterministic profiler](https://docs.python.org/3/library/profiling.tracing.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`profiling.tracing` — Deterministic profiler[¶](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "Link to this heading")

==========================================================================================================================================================

Added in version 3.15.

**Source code:** [Lib/profiling/tracing/](https://github.com/python/cpython/tree/3.15/Lib/profiling/tracing/)

* * *

The `profiling.tracing` module provides deterministic profiling of Python programs. It monitors every function call, function return, and exception event, recording precise timing for each. This approach provides exact call counts and complete visibility into program execution, making it ideal for development and testing scenarios.

Note

This module is also available as `cProfile` for backward compatibility. The `cProfile` name will continue to work in all future Python versions. Use whichever import style suits your codebase:

Copy

\# Preferred (new style)
import profiling.tracing
profiling.tracing.run('my\_function()')

\# Also works (backward compatible)
import cProfile
cProfile.run('my\_function()')

What is deterministic profiling?[¶](https://docs.python.org/3/library/profiling.tracing.html#what-is-deterministic-profiling "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

_Deterministic profiling_ captures every function call, function return, and exception event during program execution. The profiler measures the precise time intervals between these events, providing exact statistics about how the program behaves.

In contrast to [statistical profiling](https://docs.python.org/3/library/profiling.sampling.html#profiling-sampling)
, which samples the call stack periodically to estimate where time is spent, deterministic profiling records every event. This means you get exact call counts rather than statistical approximations. The trade-off is that instrumenting every event introduces overhead that can slow down program execution.

Python’s interpreted nature makes deterministic profiling practical. The interpreter already dispatches events for function calls and returns, so the profiler can hook into this mechanism without requiring code modification. The overhead tends to be moderate relative to the inherent cost of interpretation, making deterministic profiling suitable for most development workflows.

Deterministic profiling helps answer questions like:

*   How many times was this function called?
    
*   What is the complete call graph of my program?
    
*   Which functions are called by a particular function?
    
*   Are there unexpected function calls happening?
    

Call count statistics can identify bugs (surprising counts) and inline expansion opportunities (high call counts). Internal time statistics reveal “hot loops” that warrant optimization. Cumulative time statistics help identify algorithmic inefficiencies. The handling of cumulative times in this profiler allows direct comparison of recursive and iterative implementations.

Command-line interface[¶](https://docs.python.org/3/library/profiling.tracing.html#command-line-interface "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The `profiling.tracing` module can be invoked as a script to profile another script or module:

Copy

python -m profiling.tracing \[-o output\_file\] \[-s sort\_order\] (-m module | script.py)

This runs the specified script or module under the profiler and prints the results to standard output (or saves them to a file).

\-o <output\_file>[¶](https://docs.python.org/3/library/profiling.tracing.html#cmdoption-profiling.tracing-o "Link to this definition")

Write the profile results to a file instead of standard output. The output file can be read by the [`pstats`](https://docs.python.org/3/library/pstats.html#module-pstats "pstats: Statistics object for analyzing profiler output.")
 module for later analysis.

\-s <sort\_order>[¶](https://docs.python.org/3/library/profiling.tracing.html#cmdoption-profiling.tracing-s "Link to this definition")

Sort the output by the specified key. This accepts any of the sort keys recognized by [`pstats.Stats.sort_stats()`](https://docs.python.org/3/library/pstats.html#pstats.Stats.sort_stats "pstats.Stats.sort_stats")
, such as `cumulative`, `time`, `calls`, or `name`. This option only applies when [`-o`](https://docs.python.org/3/library/profiling.tracing.html#cmdoption-profiling.tracing-o)
 is not specified.

\-m <module>[¶](https://docs.python.org/3/library/profiling.tracing.html#cmdoption-profiling.tracing-m "Link to this definition")

Profile a module instead of a script. The module is located using the standard import mechanism.

Added in version 3.7: The `-m` option for `cProfile`.

Added in version 3.8: The `-m` option for [`profile`](https://docs.python.org/3/library/profile.html#module-profile "profile: Pure Python profiler (deprecated). (deprecated)")
.

Programmatic usage examples[¶](https://docs.python.org/3/library/profiling.tracing.html#programmatic-usage-examples "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

For more control over profiling, use the module’s functions and classes directly.

### Basic profiling[¶](https://docs.python.org/3/library/profiling.tracing.html#basic-profiling "Link to this heading")

The simplest approach uses the `run()` function:

Copy

import profiling.tracing
profiling.tracing.run('my\_function()')

This profiles the given code string and prints a summary to standard output. To save results for later analysis:

Copy

profiling.tracing.run('my\_function()', 'output.prof')

### Using the `Profile` class[¶](https://docs.python.org/3/library/profiling.tracing.html#using-the-profile-class "Link to this heading")

The `Profile` class provides fine-grained control:

Copy

import profiling.tracing
import pstats
from io import StringIO

pr \= profiling.tracing.Profile()
pr.enable()
\# ... code to profile ...
pr.disable()

\# Print results
s \= StringIO()
ps \= pstats.Stats(pr, stream\=s).sort\_stats(pstats.SortKey.CUMULATIVE)
ps.print\_stats()
print(s.getvalue())

The `Profile` class also works as a context manager:

Copy

import profiling.tracing

with profiling.tracing.Profile() as pr:
    \# ... code to profile ...

pr.print\_stats()

Module reference[¶](https://docs.python.org/3/library/profiling.tracing.html#module-reference "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

profiling.tracing.run(_command_, _filename\=None_, _sort\=\-1_)[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.run "Link to this definition")

Profile execution of a command and print or save the results.

This function executes the _command_ string using [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 in the `__main__` module’s namespace:

Copy

exec(command, \_\_main\_\_.\_\_dict\_\_, \_\_main\_\_.\_\_dict\_\_)

If _filename_ is not provided, the function creates a [`pstats.Stats`](https://docs.python.org/3/library/pstats.html#pstats.Stats "pstats.Stats")
 instance and prints a summary to standard output. If _filename_ is provided, the raw profile data is saved to that file for later analysis with [`pstats`](https://docs.python.org/3/library/pstats.html#module-pstats "pstats: Statistics object for analyzing profiler output.")
.

The _sort_ argument specifies the sort order for printed output, accepting any value recognized by [`pstats.Stats.sort_stats()`](https://docs.python.org/3/library/pstats.html#pstats.Stats.sort_stats "pstats.Stats.sort_stats")
.

profiling.tracing.runctx(_command_, _globals_, _locals_, _filename\=None_, _sort\=\-1_)[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.runctx "Link to this definition")

Profile execution of a command with explicit namespaces.

Like [`run()`](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.run "profiling.tracing.run")
, but executes the command with the specified _globals_ and _locals_ mappings instead of using the `__main__` module’s namespace:

Copy

exec(command, globals, locals)

class profiling.tracing.Profile(_timer\=None_, _timeunit\=0.0_, _subcalls\=True_, _builtins\=True_)[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile "Link to this definition")

A profiler object that collects execution statistics.

The optional _timer_ argument specifies a custom timing function. If not provided, the profiler uses a platform-appropriate default timer. When supplying a custom timer, it must return a single number representing the current time. If the timer returns integers, use _timeunit_ to specify the duration of one time unit (for example, `0.001` for milliseconds).

The _subcalls_ argument controls whether the profiler tracks call relationships between functions. The _builtins_ argument controls whether built-in functions are profiled.

Changed in version 3.8: Added context manager support.

enable()[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile.enable "Link to this definition")

Start collecting profiling data.

disable()[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile.disable "Link to this definition")

Stop collecting profiling data.

create\_stats()[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile.create_stats "Link to this definition")

Stop collecting data and record the results internally as the current profile.

print\_stats(_sort\=\-1_)[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile.print_stats "Link to this definition")

Create a [`pstats.Stats`](https://docs.python.org/3/library/pstats.html#pstats.Stats "pstats.Stats")
 object from the current profile and print the results to standard output.

The _sort_ argument specifies the sorting order. It accepts a single key or a tuple of keys for multi-level sorting, using the same values as [`pstats.Stats.sort_stats()`](https://docs.python.org/3/library/pstats.html#pstats.Stats.sort_stats "pstats.Stats.sort_stats")
.

Added in version 3.13: Support for a tuple of sort keys.

dump\_stats(_filename_)[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile.dump_stats "Link to this definition")

Write the current profile data to _filename_. The file can be read by [`pstats.Stats`](https://docs.python.org/3/library/pstats.html#pstats.Stats "pstats.Stats")
 for later analysis.

run(_cmd_)[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile.run "Link to this definition")

Profile the command string via [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
.

runctx(_cmd_, _globals_, _locals_)[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile.runctx "Link to this definition")

Profile the command string via [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 with the specified namespaces.

runcall(_func_, _/_, _\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile.runcall "Link to this definition")

Profile a function call. Returns whatever _func_ returns:

Copy

result \= pr.runcall(my\_function, arg1, arg2, keyword\=value)

Note

Profiling requires that the profiled code returns normally. If the interpreter terminates (for example, via [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit")
) during profiling, no results will be available.

Using a custom timer[¶](https://docs.python.org/3/library/profiling.tracing.html#using-a-custom-timer "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

The [`Profile`](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile "profiling.tracing.Profile")
 class accepts a custom timing function, allowing you to measure different aspects of execution such as wall-clock time or CPU time. Pass the timing function to the constructor:

Copy

pr \= profiling.tracing.Profile(my\_timer\_function)

The timer function must return a single number representing the current time. If it returns integers, also specify _timeunit_ to indicate the duration of one unit:

Copy

\# Timer returns time in milliseconds
pr \= profiling.tracing.Profile(my\_ms\_timer, 0.001)

For best performance, the timer function should be as fast as possible. The profiler calls it frequently, so timer overhead directly affects profiling overhead.

The [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.")
 module provides several functions suitable for use as custom timers:

*   [`time.perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter")
     for high-resolution wall-clock time
    
*   [`time.process_time()`](https://docs.python.org/3/library/time.html#time.process_time "time.process_time")
     for CPU time (excluding sleep)
    
*   [`time.monotonic()`](https://docs.python.org/3/library/time.html#time.monotonic "time.monotonic")
     for monotonic clock time
    

Limitations[¶](https://docs.python.org/3/library/profiling.tracing.html#limitations "Link to this heading")

------------------------------------------------------------------------------------------------------------

Deterministic profiling has inherent limitations related to timing accuracy.

The underlying timer typically has a resolution of about one millisecond. Measurements cannot be more accurate than this resolution. With enough measurements, timing errors tend to average out, but individual measurements may be imprecise.

There is also latency between when an event occurs and when the profiler captures the timestamp. Similarly, there is latency after reading the timestamp before user code resumes. Functions called frequently accumulate this latency, which can make them appear slower than they actually are. This error is typically less than one clock tick per call but can become significant for functions called many times.

The `profiling.tracing` module (and its `cProfile` alias) is implemented as a C extension with low overhead, so these timing issues are less pronounced than with the deprecated pure Python [`profile`](https://docs.python.org/3/library/profile.html#module-profile "profile: Pure Python profiler (deprecated). (deprecated)")
 module.

See also

[`profiling`](https://docs.python.org/3/library/profiling.html#module-profiling "profiling: Python profiling tools for performance analysis.")

Overview of Python profiling tools and guidance on choosing a profiler.

[`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")

Statistical sampling profiler for production use.

[`pstats`](https://docs.python.org/3/library/pstats.html#module-pstats "pstats: Statistics object for analyzing profiler output.")

Statistics analysis and formatting for profile data.

[`profile`](https://docs.python.org/3/library/profile.html#module-profile "profile: Pure Python profiler (deprecated). (deprecated)")

Deprecated pure Python profiler (includes calibration documentation).

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`profiling.tracing` — Deterministic profiler](https://docs.python.org/3/library/profiling.tracing.html#)
    *   [What is deterministic profiling?](https://docs.python.org/3/library/profiling.tracing.html#what-is-deterministic-profiling)
        
    *   [Command-line interface](https://docs.python.org/3/library/profiling.tracing.html#command-line-interface)
        
    *   [Programmatic usage examples](https://docs.python.org/3/library/profiling.tracing.html#programmatic-usage-examples)
        *   [Basic profiling](https://docs.python.org/3/library/profiling.tracing.html#basic-profiling)
            
        *   [Using the `Profile` class](https://docs.python.org/3/library/profiling.tracing.html#using-the-profile-class)
            
    *   [Module reference](https://docs.python.org/3/library/profiling.tracing.html#module-reference)
        
    *   [Using a custom timer](https://docs.python.org/3/library/profiling.tracing.html#using-a-custom-timer)
        
    *   [Limitations](https://docs.python.org/3/library/profiling.tracing.html#limitations)
        

#### Previous topic

[`profiling` — Python profilers](https://docs.python.org/3/library/profiling.html "previous chapter")

#### Next topic

[`profiling.sampling` — Statistical profiler](https://docs.python.org/3/library/profiling.sampling.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=profiling.tracing+%E2%80%94+Deterministic+profiler&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fprofiling.tracing.html&pagesource=library%2Fprofiling.tracing.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/profiling.tracing.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/profiling.sampling.html "profiling.sampling — Statistical profiler")
     |
*   [previous](https://docs.python.org/3/library/profiling.html "profiling — Python profilers")
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
     »
*   [`profiling.tracing` — Deterministic profiler](https://docs.python.org/3/library/profiling.tracing.html)
    
*    
    
    |
*   Theme Auto Light Dark |