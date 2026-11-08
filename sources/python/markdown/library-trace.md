### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tracemalloc.html "tracemalloc — Trace memory allocations")
     |
*   [previous](https://docs.python.org/3/library/timeit.html "timeit — Measure execution time of small code snippets")
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
*   [`trace` — Trace or track Python statement execution](https://docs.python.org/3/library/trace.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`trace` — Trace or track Python statement execution[¶](https://docs.python.org/3/library/trace.html#module-trace "Link to this heading")

=========================================================================================================================================

**Source code:** [Lib/trace.py](https://github.com/python/cpython/tree/3.15/Lib/trace.py)

* * *

The `trace` module allows you to trace program execution, generate annotated statement coverage listings, print caller/callee relationships and list functions executed during a program run. It can be used in another program or from the command line.

See also

[Coverage.py](https://coverage.readthedocs.io/)

A popular third-party coverage tool that provides HTML output along with advanced features such as branch coverage.

Command-Line Usage[¶](https://docs.python.org/3/library/trace.html#command-line-usage "Link to this heading")

--------------------------------------------------------------------------------------------------------------

The `trace` module can be invoked from the command line. It can be as simple as

Copy

python \-m trace \--count \-C . somefile.py ...

The above will execute `somefile.py` and generate annotated listings of all Python modules imported during the execution into the current directory.

\--help[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-help "Link to this definition")

Display usage and exit.

\--version[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-version "Link to this definition")

Display the version of the module and exit.

Added in version 3.8: Added `--module` option that allows running an executable module.

### Main options[¶](https://docs.python.org/3/library/trace.html#main-options "Link to this heading")

At least one of the following options must be specified when invoking `trace`. The [`--listfuncs`](https://docs.python.org/3/library/trace.html#cmdoption-trace-l)
 option is mutually exclusive with the [`--trace`](https://docs.python.org/3/library/trace.html#cmdoption-trace-t)
 and [`--count`](https://docs.python.org/3/library/trace.html#cmdoption-trace-c)
 options. When `--listfuncs` is provided, neither `--count` nor `--trace` are accepted, and vice versa.

\-c, \--count[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-c "Link to this definition")

Produce a set of annotated listing files upon program completion that shows how many times each statement was executed. See also [`--coverdir`](https://docs.python.org/3/library/trace.html#cmdoption-trace-C)
, [`--file`](https://docs.python.org/3/library/trace.html#cmdoption-trace-f)
 and [`--no-report`](https://docs.python.org/3/library/trace.html#cmdoption-trace-R)
 below.

\-t, \--trace[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-t "Link to this definition")

Display lines as they are executed.

\-l, \--listfuncs[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-l "Link to this definition")

Display the functions executed by running the program.

\-r, \--report[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-r "Link to this definition")

Produce an annotated list from an earlier program run that used the [`--count`](https://docs.python.org/3/library/trace.html#cmdoption-trace-c)
 and [`--file`](https://docs.python.org/3/library/trace.html#cmdoption-trace-f)
 option. This does not execute any code.

\-T, \--trackcalls[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-T "Link to this definition")

Display the calling relationships exposed by running the program.

### Modifiers[¶](https://docs.python.org/3/library/trace.html#modifiers "Link to this heading")

\-f, \--file\=<file>[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-f "Link to this definition")

Name of a file to accumulate counts over several tracing runs. Should be used with the [`--count`](https://docs.python.org/3/library/trace.html#cmdoption-trace-c)
 option.

\-C, \--coverdir\=<dir>[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-C "Link to this definition")

Directory where the report files go. The coverage report for `package.module` is written to file `_dir_/_package_/_module_.cover`.

\-m, \--missing[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-m "Link to this definition")

When generating annotated listings, mark lines which were not executed with `>>>>>>`.

\-s, \--summary[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-s "Link to this definition")

When using [`--count`](https://docs.python.org/3/library/trace.html#cmdoption-trace-c)
 or [`--report`](https://docs.python.org/3/library/trace.html#cmdoption-trace-r)
, write a brief summary to stdout for each file processed.

\-R, \--no-report[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-R "Link to this definition")

Do not generate annotated listings. This is useful if you intend to make several runs with [`--count`](https://docs.python.org/3/library/trace.html#cmdoption-trace-c)
, and then produce a single set of annotated listings at the end.

\-g, \--timing[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-g "Link to this definition")

Prefix each line with the time since the program started. Only used while tracing.

### Filters[¶](https://docs.python.org/3/library/trace.html#filters "Link to this heading")

These options may be repeated multiple times.

\--ignore-module\=<mod>[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-ignore-module "Link to this definition")

Ignore each of the given module names and its submodules (if it is a package). The argument can be a list of names separated by a comma.

\--ignore-dir\=<dir>[¶](https://docs.python.org/3/library/trace.html#cmdoption-trace-ignore-dir "Link to this definition")

Ignore all modules and packages in the named directory and subdirectories. The argument can be a list of directories separated by [`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep")
.

Programmatic Interface[¶](https://docs.python.org/3/library/trace.html#programmatic-interface "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

class trace.Trace(_count\=1_, _trace\=1_, _countfuncs\=0_, _countcallers\=0_, _ignoremods\=()_, _ignoredirs\=()_, _infile\=None_, _outfile\=None_, _timing\=False_)[¶](https://docs.python.org/3/library/trace.html#trace.Trace "Link to this definition")

Create an object to trace execution of a single statement or expression. All parameters are optional. _count_ enables counting of line numbers. _trace_ enables line execution tracing. _countfuncs_ enables listing of the functions called during the run. _countcallers_ enables call relationship tracking. _ignoremods_ is a list of modules or packages to ignore. _ignoredirs_ is a list of directories whose modules or packages should be ignored. _infile_ is the name of the file from which to read stored count information. _outfile_ is the name of the file in which to write updated count information. _timing_ enables a timestamp relative to when tracing was started to be displayed.

run(_cmd_)[¶](https://docs.python.org/3/library/trace.html#trace.Trace.run "Link to this definition")

Execute the command and gather statistics from the execution with the current tracing parameters. _cmd_ must be a string or code object, suitable for passing into [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
.

runctx(_cmd_, _globals\=None_, _locals\=None_)[¶](https://docs.python.org/3/library/trace.html#trace.Trace.runctx "Link to this definition")

Execute the command and gather statistics from the execution with the current tracing parameters, in the defined global and local environments. If not defined, _globals_ and _locals_ default to empty dictionaries.

runfunc(_func_, _/_, _\*args_, _\*\*kwds_)[¶](https://docs.python.org/3/library/trace.html#trace.Trace.runfunc "Link to this definition")

Call _func_ with the given arguments under control of the `Trace` object with the current tracing parameters.

results()[¶](https://docs.python.org/3/library/trace.html#trace.Trace.results "Link to this definition")

Return a [`CoverageResults`](https://docs.python.org/3/library/trace.html#trace.CoverageResults "trace.CoverageResults")
 object that contains the cumulative results of all previous calls to `run`, `runctx` and `runfunc` for the given `Trace` instance. Does not reset the accumulated trace results.

class trace.CoverageResults[¶](https://docs.python.org/3/library/trace.html#trace.CoverageResults "Link to this definition")

A container for coverage results, created by [`Trace.results()`](https://docs.python.org/3/library/trace.html#trace.Trace.results "trace.Trace.results")
. Should not be created directly by the user.

update(_other_)[¶](https://docs.python.org/3/library/trace.html#trace.CoverageResults.update "Link to this definition")

Merge in data from another `CoverageResults` object.

write\_results(_show\_missing\=True_, _summary\=False_, _coverdir\=None_, _\*_, _ignore\_missing\_files\=False_)[¶](https://docs.python.org/3/library/trace.html#trace.CoverageResults.write_results "Link to this definition")

Write coverage results. Set _show\_missing_ to show lines that had no hits. Set _summary_ to include in the output the coverage summary per module. _coverdir_ specifies the directory into which the coverage result files will be output. If `None`, the results for each source file are placed in its directory.

If _ignore\_missing\_files_ is `True`, coverage counts for files that no longer exist are silently ignored. Otherwise, a missing file will raise a [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
.

Changed in version 3.13: Added _ignore\_missing\_files_ parameter.

A simple example demonstrating the use of the programmatic interface:

Copy

import sys
import trace

\# create a Trace object, telling it what to ignore, and whether to
\# do tracing or line-counting or both.
tracer \= trace.Trace(
    ignoredirs\=\[sys.prefix, sys.exec\_prefix\],
    trace\=0,
    count\=1)

\# run the new command using the given tracer
tracer.run('main()')

\# make a report, placing output in the current directory
r \= tracer.results()
r.write\_results(show\_missing\=True, coverdir\=".")

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`trace` — Trace or track Python statement execution](https://docs.python.org/3/library/trace.html#)
    *   [Command-Line Usage](https://docs.python.org/3/library/trace.html#command-line-usage)
        *   [Main options](https://docs.python.org/3/library/trace.html#main-options)
            
        *   [Modifiers](https://docs.python.org/3/library/trace.html#modifiers)
            
        *   [Filters](https://docs.python.org/3/library/trace.html#filters)
            
    *   [Programmatic Interface](https://docs.python.org/3/library/trace.html#programmatic-interface)
        

#### Previous topic

[`timeit` — Measure execution time of small code snippets](https://docs.python.org/3/library/timeit.html "previous chapter")

#### Next topic

[`tracemalloc` — Trace memory allocations](https://docs.python.org/3/library/tracemalloc.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=trace+%E2%80%94+Trace+or+track+Python+statement+execution&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftrace.html&pagesource=library%2Ftrace.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/trace.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tracemalloc.html "tracemalloc — Trace memory allocations")
     |
*   [previous](https://docs.python.org/3/library/timeit.html "timeit — Measure execution time of small code snippets")
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
*   [`trace` — Trace or track Python statement execution](https://docs.python.org/3/library/trace.html)
    
*    
    
    |
*   Theme Auto Light Dark |