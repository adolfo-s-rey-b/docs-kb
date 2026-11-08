### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/removed.html "Removed Modules")
     |
*   [previous](https://docs.python.org/3/library/getopt.html "getopt — C-style parser for command line options")
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
*   [Superseded modules](https://docs.python.org/3/library/superseded.html)
     »
*   [`profile` — Pure Python profiler](https://docs.python.org/3/library/profile.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`profile` — Pure Python profiler[¶](https://docs.python.org/3/library/profile.html#module-profile "Link to this heading")

==========================================================================================================================

**Source code:** [Lib/profile.py](https://github.com/python/cpython/tree/3.15/Lib/profile.py)

* * *

Deprecated since version 3.15, will be removed in version 3.17.

The `profile` module is deprecated and will be removed in Python 3.17. Use [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
 instead.

The `profile` module provides a pure Python implementation of a deterministic profiler. While useful for understanding profiler internals or extending profiler behavior through subclassing, its pure Python implementation introduces significant overhead compared to the C-based [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
 module.

For most profiling tasks, use:

*   [`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")
     for production debugging with zero overhead
    
*   [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
     for development and testing
    

Migration[¶](https://docs.python.org/3/library/profile.html#migration "Link to this heading")

----------------------------------------------------------------------------------------------

Migrating from `profile` to [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
 is straightforward. The APIs are compatible:

Copy

\# Old (deprecated)
import profile
profile.run('my\_function()')

\# New (recommended)
import profiling.tracing
profiling.tracing.run('my\_function()')

For most code, replacing `import profile` with `import profiling.tracing` (and using `profiling.tracing` instead of `profile` throughout) provides a straightforward migration path.

Note

The `cProfile` module remains available as a backward-compatible alias to [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
. Existing code using `import cProfile` will continue to work without modification.

`profile` and `profiling.tracing` module reference[¶](https://docs.python.org/3/library/profile.html#profile-and-profiling-tracing-module-reference "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Both the `profile` and [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
 modules provide the following functions:

profile.run(_command_, _filename\=None_, _sort\=\-1_)[¶](https://docs.python.org/3/library/profile.html#profile.run "Link to this definition")

This function takes a single argument that can be passed to the [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 function, and an optional file name. In all cases this routine executes:

Copy

exec(command, \_\_main\_\_.\_\_dict\_\_, \_\_main\_\_.\_\_dict\_\_)

and gathers profiling statistics from the execution. If no file name is present, then this function automatically creates a [`Stats`](https://docs.python.org/3/library/pstats.html#pstats.Stats "pstats.Stats")
 instance and prints a simple profiling report. If the sort value is specified, it is passed to this `Stats` instance to control how the results are sorted.

profile.runctx(_command_, _globals_, _locals_, _filename\=None_, _sort\=\-1_)[¶](https://docs.python.org/3/library/profile.html#profile.runctx "Link to this definition")

This function is similar to [`run()`](https://docs.python.org/3/library/profile.html#profile.run "profile.run")
, with added arguments to supply the globals and locals mappings for the _command_ string. This routine executes:

Copy

exec(command, globals, locals)

and gathers profiling statistics as in the [`run()`](https://docs.python.org/3/library/profile.html#profile.run "profile.run")
 function above.

class profile.Profile(_timer\=None_, _timeunit\=0.0_, _subcalls\=True_, _builtins\=True_)[¶](https://docs.python.org/3/library/profile.html#profile.Profile "Link to this definition")

This class is normally only used if more precise control over profiling is needed than what the [`profiling.tracing.run()`](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.run "profiling.tracing.run")
 function provides.

A custom timer can be supplied for measuring how long code takes to run via the _timer_ argument. This must be a function that returns a single number representing the current time. If the number is an integer, the _timeunit_ specifies a multiplier that specifies the duration of each unit of time. For example, if the timer returns times measured in thousandths of seconds, the time unit would be `.001`.

Directly using the `Profile` class allows formatting profile results without writing the profile data to a file:

Copy

import profiling.tracing
import pstats
import io
from pstats import SortKey

pr \= profiling.tracing.Profile()
pr.enable()
\# ... do something ...
pr.disable()
s \= io.StringIO()
sortby \= SortKey.CUMULATIVE
ps \= pstats.Stats(pr, stream\=s).sort\_stats(sortby)
ps.print\_stats()
print(s.getvalue())

The `Profile` class can also be used as a context manager (supported only in [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
, not in the deprecated `profile` module; see [Context Manager Types](https://docs.python.org/3/builtins/stdtypes.html#typecontextmanager)
):

Copy

import profiling.tracing

with profiling.tracing.Profile() as pr:
    \# ... do something ...

    pr.print\_stats()

Changed in version 3.8: Added context manager support.

enable()[¶](https://docs.python.org/3/library/profile.html#profile.Profile.enable "Link to this definition")

Start collecting profiling data. Only in [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
.

disable()[¶](https://docs.python.org/3/library/profile.html#profile.Profile.disable "Link to this definition")

Stop collecting profiling data. Only in [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
.

create\_stats()[¶](https://docs.python.org/3/library/profile.html#profile.Profile.create_stats "Link to this definition")

Stop collecting profiling data and record the results internally as the current profile.

print\_stats(_sort\=\-1_)[¶](https://docs.python.org/3/library/profile.html#profile.Profile.print_stats "Link to this definition")

Create a [`Stats`](https://docs.python.org/3/library/pstats.html#pstats.Stats "pstats.Stats")
 object based on the current profile and print the results to stdout.

The _sort_ parameter specifies the sorting order of the displayed statistics. It accepts a single key or a tuple of keys to enable multi-level sorting, as in [`pstats.Stats.sort_stats()`](https://docs.python.org/3/library/pstats.html#pstats.Stats.sort_stats "pstats.Stats.sort_stats")
.

Added in version 3.13: `print_stats()` now accepts a tuple of keys.

dump\_stats(_filename_)[¶](https://docs.python.org/3/library/profile.html#profile.Profile.dump_stats "Link to this definition")

Write the results of the current profile to _filename_.

run(_cmd_)[¶](https://docs.python.org/3/library/profile.html#profile.Profile.run "Link to this definition")

Profile the cmd via [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
.

runctx(_cmd_, _globals_, _locals_)[¶](https://docs.python.org/3/library/profile.html#profile.Profile.runctx "Link to this definition")

Profile the cmd via [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 with the specified global and local environment.

runcall(_func_, _/_, _\*args_, _\*\*kwargs_)[¶](https://docs.python.org/3/library/profile.html#profile.Profile.runcall "Link to this definition")

Profile `func(*args, **kwargs)`

Note that profiling will only work if the called command/function actually returns. If the interpreter is terminated (e.g. via a [`sys.exit()`](https://docs.python.org/3/library/sys.html#sys.exit "sys.exit")
 call during the called command/function execution) no profiling results will be printed.

Differences from `profiling.tracing`[¶](https://docs.python.org/3/library/profile.html#differences-from-profiling-tracing "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

The `profile` module differs from [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
 in several ways:

**Higher overhead.** The pure Python implementation is significantly slower than the C implementation, making it unsuitable for profiling long-running programs or performance-sensitive code.

**Calibration support.** The `profile` module supports calibration to compensate for profiling overhead. This is not needed in [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
 because the C implementation has negligible overhead.

**Custom timers.** Both modules support custom timers, but `profile` accepts timer functions that return tuples (like [`os.times()`](https://docs.python.org/3/library/os.html#os.times "os.times")
), while [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
 requires a function returning a single number.

**Subclassing.** The pure Python implementation is easier to subclass and extend for custom profiling behavior.

What is deterministic profiling?[¶](https://docs.python.org/3/library/profile.html#what-is-deterministic-profiling "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

_Deterministic profiling_ is meant to reflect the fact that all _function call_, _function return_, and _exception_ events are monitored, and precise timings are made for the intervals between these events (during which time the user’s code is executing). In contrast, _statistical profiling_ (which is provided by the [`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")
 module) periodically samples the effective instruction pointer, and deduces where time is being spent. The latter technique traditionally involves less overhead (as the code does not need to be instrumented), but provides only relative indications of where time is being spent.

In Python, since there is an interpreter active during execution, the presence of instrumented code is not required in order to do deterministic profiling. Python automatically provides a _hook_ (optional callback) for each event. In addition, the interpreted nature of Python tends to add so much overhead to execution, that deterministic profiling tends to only add small processing overhead in typical applications. The result is that deterministic profiling is not that expensive, yet provides extensive run time statistics about the execution of a Python program.

Call count statistics can be used to identify bugs in code (surprising counts), and to identify possible inline-expansion points (high call counts). Internal time statistics can be used to identify “hot loops” that should be carefully optimized. Cumulative time statistics should be used to identify high level errors in the selection of algorithms. Note that the unusual handling of cumulative times in this profiler allows statistics for recursive implementations of algorithms to be directly compared to iterative implementations.

Limitations[¶](https://docs.python.org/3/library/profile.html#limitations "Link to this heading")

--------------------------------------------------------------------------------------------------

One limitation has to do with accuracy of timing information. There is a fundamental problem with deterministic profilers involving accuracy. The most obvious restriction is that the underlying “clock” is only ticking at a rate (typically) of about .001 seconds. Hence no measurements will be more accurate than the underlying clock. If enough measurements are taken, then the “error” will tend to average out. Unfortunately, removing this first error induces a second source of error.

The second problem is that it “takes a while” from when an event is dispatched until the profiler’s call to get the time actually _gets_ the state of the clock. Similarly, there is a certain lag when exiting the profiler event handler from the time that the clock’s value was obtained (and then squirreled away), until the user’s code is once again executing. As a result, functions that are called many times, or call many functions, will typically accumulate this error. The error that accumulates in this fashion is typically less than the accuracy of the clock (less than one clock tick), but it _can_ accumulate and become very significant.

The problem is more important with the deprecated `profile` module than with the lower-overhead [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
. For this reason, `profile` provides a means of calibrating itself for a given platform so that this error can be probabilistically (on the average) removed. After the profiler is calibrated, it will be more accurate (in a least square sense), but it will sometimes produce negative numbers (when call counts are exceptionally low, and the gods of probability work against you :-). ) Do _not_ be alarmed by negative numbers in the profile. They should _only_ appear if you have calibrated your profiler, and the results are actually better than without calibration.

Calibration[¶](https://docs.python.org/3/library/profile.html#calibration "Link to this heading")

--------------------------------------------------------------------------------------------------

The profiler of the `profile` module subtracts a constant from each event handling time to compensate for the overhead of calling the time function, and socking away the results. By default, the constant is 0. The following procedure can be used to obtain a better constant for a given platform (see [Limitations](https://docs.python.org/3/library/profile.html#profile-limitations)
).

Copy

import profile
pr \= profile.Profile()
for i in range(5):
    print(pr.calibrate(10000))

The method executes the number of Python calls given by the argument, directly and again under the profiler, measuring the time for both. It then computes the hidden overhead per profiler event, and returns that as a float. For example, on a 1.8Ghz Intel Core i5 running macOS, and using Python’s time.process\_time() as the timer, the magical number is about 4.04e-6.

The object of this exercise is to get a fairly consistent result. If your computer is _very_ fast, or your timer function has poor resolution, you might have to pass 100000, or even 1000000, to get consistent results.

When you have a consistent answer, there are three ways you can use it:

Copy

import profile

\# 1. Apply computed bias to all Profile instances created hereafter.
profile.Profile.bias \= your\_computed\_bias

\# 2. Apply computed bias to a specific Profile instance.
pr \= profile.Profile()
pr.bias \= your\_computed\_bias

\# 3. Specify computed bias in instance constructor.
pr \= profile.Profile(bias\=your\_computed\_bias)

If you have a choice, you are better off choosing a smaller constant, and then your results will “less often” show up as negative in profile statistics.

Using a custom timer[¶](https://docs.python.org/3/library/profile.html#using-a-custom-timer "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

If you want to change how current time is determined (for example, to force use of wall-clock time or elapsed process time), pass the timing function you want to the [`Profile`](https://docs.python.org/3/library/profile.html#profile.Profile "profile.Profile")
 class constructor:

Copy

pr \= profile.Profile(your\_time\_func)

The resulting profiler will then call `your_time_func`. Depending on whether you are using [`profile.Profile`](https://docs.python.org/3/library/profile.html#profile.Profile "profile.Profile")
 or [`profiling.tracing.Profile`](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile "profiling.tracing.Profile")
, `your_time_func`’s return value will be interpreted differently:

[`profile.Profile`](https://docs.python.org/3/library/profile.html#profile.Profile "profile.Profile")

`your_time_func` should return a single number, or a list of numbers whose sum is the current time (like what [`os.times()`](https://docs.python.org/3/library/os.html#os.times "os.times")
 returns). If the function returns a single time number, or the list of returned numbers has length 2, then you will get an especially fast version of the dispatch routine.

Be warned that you should calibrate the profiler class for the timer function that you choose (see [Calibration](https://docs.python.org/3/library/profile.html#profile-calibration)
). For most machines, a timer that returns a lone integer value will provide the best results in terms of low overhead during profiling. ([`os.times()`](https://docs.python.org/3/library/os.html#os.times "os.times")
 is _pretty_ bad, as it returns a tuple of floating-point values). If you want to substitute a better timer in the cleanest fashion, derive a class and hardwire a replacement dispatch method that best handles your timer call, along with the appropriate calibration constant.

[`profiling.tracing.Profile`](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile "profiling.tracing.Profile")

`your_time_func` should return a single number. If it returns integers, you can also invoke the class constructor with a second argument specifying the real duration of one unit of time. For example, if `your_integer_time_func` returns times measured in thousandths of seconds, you would construct the [`Profile`](https://docs.python.org/3/library/profile.html#profile.Profile "profile.Profile")
 instance as follows:

Copy

pr \= profiling.tracing.Profile(your\_integer\_time\_func, 0.001)

As the [`profiling.tracing.Profile`](https://docs.python.org/3/library/profiling.tracing.html#profiling.tracing.Profile "profiling.tracing.Profile")
 class cannot be calibrated, custom timer functions should be used with care and should be as fast as possible. For the best results with a custom timer, it might be necessary to hard-code it in the C source of the internal `_lsprof` module.

Python 3.3 adds several new functions in [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.")
 that can be used to make precise measurements of process or wall-clock time. For example, see [`time.perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter")
.

See also

[`profiling`](https://docs.python.org/3/library/profiling.html#module-profiling "profiling: Python profiling tools for performance analysis.")

Overview of Python profiling tools.

[`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")

Recommended replacement for this module.

[`pstats`](https://docs.python.org/3/library/pstats.html#module-pstats "pstats: Statistics object for analyzing profiler output.")

Statistical analysis and formatting for profile data.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`profile` — Pure Python profiler](https://docs.python.org/3/library/profile.html#)
    *   [Migration](https://docs.python.org/3/library/profile.html#migration)
        
    *   [`profile` and `profiling.tracing` module reference](https://docs.python.org/3/library/profile.html#profile-and-profiling-tracing-module-reference)
        
    *   [Differences from `profiling.tracing`](https://docs.python.org/3/library/profile.html#differences-from-profiling-tracing)
        
    *   [What is deterministic profiling?](https://docs.python.org/3/library/profile.html#what-is-deterministic-profiling)
        
    *   [Limitations](https://docs.python.org/3/library/profile.html#limitations)
        
    *   [Calibration](https://docs.python.org/3/library/profile.html#calibration)
        
    *   [Using a custom timer](https://docs.python.org/3/library/profile.html#using-a-custom-timer)
        

#### Previous topic

[`getopt` — C-style parser for command line options](https://docs.python.org/3/library/getopt.html "previous chapter")

#### Next topic

[Removed Modules](https://docs.python.org/3/library/removed.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=profile+%E2%80%94+Pure+Python+profiler&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fprofile.html&pagesource=library%2Fprofile.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/profile.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/removed.html "Removed Modules")
     |
*   [previous](https://docs.python.org/3/library/getopt.html "getopt — C-style parser for command line options")
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
*   [Superseded modules](https://docs.python.org/3/library/superseded.html)
     »
*   [`profile` — Pure Python profiler](https://docs.python.org/3/library/profile.html)
    
*    
    
    |
*   Theme Auto Light Dark |