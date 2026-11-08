### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/3.14.html "What’s new in Python 3.14")
     |
*   [previous](https://docs.python.org/3/whatsnew/index.html "What’s New in Python")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [What’s New in Python](https://docs.python.org/3/whatsnew/index.html)
     »
*   [What’s new in Python 3.15](https://docs.python.org/3/whatsnew/3.15.html)
    
*    
    
    |
*   Theme Auto Light Dark |

What’s new in Python 3.15[¶](https://docs.python.org/3/whatsnew/3.15.html#what-s-new-in-python-3-15 "Link to this heading")

============================================================================================================================

Editor:

Hugo van Kemenade

This article explains the new features in Python 3.15, compared to 3.14. Python 3.15 was released on 9 October 2026. For full details, see the [changelog](https://docs.python.org/3/whatsnew/changelog.html#changelog)
.

See also

[**PEP 790**](https://peps.python.org/pep-0790/)
 – Python 3.15 release schedule

Summary – Release highlights[¶](https://docs.python.org/3/whatsnew/3.15.html#summary-release-highlights "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Python 3.15 is the latest stable release of the Python programming language, with a mix of changes to the language, the implementation, and the standard library. The biggest changes include [lazy imports](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-lazy-imports)
, [frozendict](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-frozendict)
 and [sentinel](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-sentinel)
 builtins, [UTF-8 as the default encoding](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-utf8-default)
, [unpacking in comprehensions](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-unpacking-in-comprehensions)
, and a [stable ABI for free-threaded builds](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-abi3t)
.

The library changes include a new [profiling package](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-profiling-package)
 with [Tachyon](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-sampling-profiler)
, a high-frequency statistical sampling profiler, [more color](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-more-color)
 in command-line output, as well as the usual deprecations and removals, and improvements in user-friendliness and correctness.

This article doesn’t attempt to provide a complete specification of all new features, but instead gives a convenient overview. For full details refer to the documentation, such as the [Library Reference](https://docs.python.org/3/library/index.html#library-index)
 and [Language Reference](https://docs.python.org/3/reference/index.html#reference-index)
. To understand the complete implementation and design rationale for a change, refer to the PEP for a particular new feature; but note that PEPs usually are not kept up-to-date once a feature has been fully implemented.

See [Porting to Python 3.15](https://docs.python.org/3/whatsnew/3.15.html#porting-to-python-3-15)
 for guidance on upgrading from earlier versions of Python.

* * *

Interpreter improvements:

*   [**PEP 661**](https://peps.python.org/pep-0661/)
    : [Add sentinel built-in type](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-sentinel)
    
*   [**PEP 686**](https://peps.python.org/pep-0686/)
    : [Python now uses UTF-8 as the default encoding](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-utf8-default)
    
*   [**PEP 798**](https://peps.python.org/pep-0798/)
    : [Unpacking in comprehensions](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-unpacking-in-comprehensions)
    
*   [**PEP 810**](https://peps.python.org/pep-0810/)
    : [Explicit lazy imports for faster startup times](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-lazy-imports)
    
*   [**PEP 814**](https://peps.python.org/pep-0814/)
    : [Add frozendict built-in type](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-frozendict)
    
*   [**PEP 829**](https://peps.python.org/pep-0829/)
    : [Package startup configuration files](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-startup-files)
    
*   [The experimental JIT compiler has been significantly upgraded](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-jit)
    
*   [Improved error messages](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-improved-error-messages)
    

Significant improvements in the standard library:

*   [**PEP 799**](https://peps.python.org/pep-0799/)
    : [A dedicated profiling package for organizing Python profiling tools](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-profiling-package)
    
*   [**PEP 799**](https://peps.python.org/pep-0799/)
    : [Tachyon: High-frequency statistical sampling profiler](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-sampling-profiler)
    
*   [More color](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-more-color)
    

New typing features:

*   [**PEP 728**](https://peps.python.org/pep-0728/)
    : [TypedDict with typed extra items](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-typeddict)
    
*   [**PEP 747**](https://peps.python.org/pep-0747/)
    : [Annotating type forms with TypeForm](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-typeform)
    
*   [**PEP 800**](https://peps.python.org/pep-0800/)
    : [Disjoint bases in the type system](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-disjoint-base)
    

C API improvements:

*   [**PEP 782**](https://peps.python.org/pep-0782/)
    : [A new PyBytesWriter C API to create a Python bytes object](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-pybyteswriter)
    
*   [**PEP 788**](https://peps.python.org/pep-0788/)
    : [Protection against finalization in the C API](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-c-api-interpreter-finalization)
    
*   [**PEP 803**](https://peps.python.org/pep-0803/)
    , [**820**](https://peps.python.org/pep-0820/)
    , [**793**](https://peps.python.org/pep-0793/)
    : [Stable ABI for free-threaded builds](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-abi3t)
     and related C API
    

Build changes:

*   [**PEP 831**](https://peps.python.org/pep-0831/)
    : [Frame pointers are enabled by default for improved system-level observability](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-frame-pointers)
    

Release changes:

*   [The official Windows 64-bit binaries now use the tail-calling interpreter](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-windows-tail-calling-interpreter)
    
*   The official macOS binaries now install free-threading support by default
    

New features[¶](https://docs.python.org/3/whatsnew/3.15.html#new-features "Link to this heading")

--------------------------------------------------------------------------------------------------

### [**PEP 810**](https://peps.python.org/pep-0810/)
: Explicit lazy imports[¶](https://docs.python.org/3/whatsnew/3.15.html#pep-810-explicit-lazy-imports "Link to this heading")

Large Python applications often suffer from slow startup times. A significant contributor to this problem is the import system: when a module is imported, Python must locate the file, read it from disk, compile it to bytecode, and execute all top-level code. For applications with deep dependency trees, this process can take seconds, even when most of the imported code is never actually used during a particular run.

Developers have worked around this by moving imports inside functions, using [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 to load modules on demand, or restructuring code to avoid unnecessary dependencies. These approaches work but make code harder to read and maintain, scatter import statements throughout the codebase, and require discipline to apply consistently.

Python now provides a cleaner solution through explicit [`lazy`](https://docs.python.org/3/reference/simple_stmts.html#lazy)
 imports using the new `lazy` soft keyword. When you mark an import as lazy, Python defers the actual module loading until the imported name is first used. This gives you the organizational benefits of declaring all imports at the top of the file while only paying the loading cost for modules you actually use.

The `lazy` keyword works with both `import` and `from ... import` statements. When you write `lazy import heavy_module`, Python does not immediately load the module. Instead, it creates a lightweight proxy object. The actual module loading happens transparently when you first access the name:

Copy

lazy import json
lazy from pathlib import Path

print("Starting up...")  \# json and pathlib are not fully imported yet

data \= json.loads('{"key": "value"}')  \# json gets fully imported here
p \= Path(".")  \# pathlib gets fully imported here

This mechanism is particularly useful for applications that import many modules at the top level but may only use a subset of them in any given run. The deferred loading reduces startup latency without requiring code restructuring or conditional imports scattered throughout the codebase.

In the case where loading a lazily imported module fails (for example, if the module does not exist), Python raises the exception at the point of first use rather than at import time. The associated traceback includes both the location where the name was accessed and the original import statement, making it straightforward to diagnose and debug the failure.

For cases where you want to enable lazy loading globally without modifying source code, Python provides the [`-X lazy_imports`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 command-line option and the [`PYTHON_LAZY_IMPORTS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_LAZY_IMPORTS)
 environment variable. Both accept two values: `all` makes all imports lazy by default, and `normal` (the default) respects the `lazy` keyword in source code. The [`sys.set_lazy_imports()`](https://docs.python.org/3/library/sys.html#sys.set_lazy_imports "sys.set_lazy_imports")
 and [`sys.get_lazy_imports()`](https://docs.python.org/3/library/sys.html#sys.get_lazy_imports "sys.get_lazy_imports")
 functions allow changing and querying this mode at runtime.

For more selective control, [`sys.set_lazy_imports_filter()`](https://docs.python.org/3/library/sys.html#sys.set_lazy_imports_filter "sys.set_lazy_imports_filter")
 accepts a callable that determines whether a specific module should be loaded lazily. The filter receives three arguments: the importing module’s name (or `None`), the imported module’s name, and the fromlist (or `None` for regular imports). It should return `True` to allow the import to be lazy, or `False` to force eager loading. This allows patterns like making only your own application’s modules lazy while keeping third-party dependencies eager:

Copy

import sys

def myapp\_filter(importing, imported, fromlist):
    return imported.startswith("myapp.")
sys.set\_lazy\_imports\_filter(myapp\_filter)
sys.set\_lazy\_imports("all")

import myapp.slow\_module  \# lazy (matches filter)
import json               \# eager (does not match filter)

The proxy type itself is available as [`types.LazyImportType`](https://docs.python.org/3/library/types.html#types.LazyImportType "types.LazyImportType")
 for code that needs to detect lazy imports programmatically.

There are some restrictions on where the `lazy` keyword can be used. Lazy imports are only permitted at module scope; using `lazy` inside a function, class body, or `try`/`except`/`finally` block raises a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
. Neither star imports nor future imports can be lazy (`lazy from module import *` and `lazy from __future__ import ...` both raise `SyntaxError`).

For code that cannot use the `lazy` keyword directly (for example, when supporting Python versions older than 3.15 while still using lazy imports on 3.15+), a module can define [`__lazy_modules__`](https://docs.python.org/3/reference/datamodel.html#module.__lazy_modules__ "module.__lazy_modules__")
 as a container of fully qualified module name strings. Regular `import` statements for those modules are then treated as lazy, with the same semantics as the `lazy` keyword:

Copy

\_\_lazy\_modules\_\_ \= \["json", "pathlib"\]

import json     \# lazy
import os       \# still eager

(Contributed by Pablo Galindo Salgado and Dino Viehland in [gh-142349](https://github.com/python/cpython/issues/142349)
.)

See also

[**PEP 810**](https://peps.python.org/pep-0810/)
 for the full specification and rationale.

### [**PEP 814**](https://peps.python.org/pep-0814/)
: Add frozendict built-in type[¶](https://docs.python.org/3/whatsnew/3.15.html#pep-814-add-frozendict-built-in-type "Link to this heading")

A new [immutable](https://docs.python.org/3/glossary.html#term-immutable)
 type, [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
, is added to the [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")
 module. It does not allow modification after creation. A `frozendict` is not a subclass of `dict`; it inherits directly from `object`. A `frozendict` is [hashable](https://docs.python.org/3/glossary.html#term-hashable)
 as long as all of its keys and values are hashable. A `frozendict` preserves insertion order, but comparison does not take order into account.

For example:

Copy

\>>> a \= frozendict(x\=1, y\=2)
\>>> a
frozendict({'x': 1, 'y': 2})
\>>> a\['z'\] \= 3
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    a\['z'\] \= 3
    ~^^^^^
TypeError: 'frozendict' object does not support item assignment
\>>> b \= frozendict(y\=2, x\=1)
\>>> hash(a) \== hash(b)
True
\>>> a \== b
True

The following standard library modules have been updated to accept `frozendict`: [`copy`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.")
, [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
, [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")
, [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).")
, [`plistlib`](https://docs.python.org/3/library/plistlib.html#module-plistlib "plistlib: Generate and parse Apple plist files.")
 (only for serialization), [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
, [`pprint`](https://docs.python.org/3/library/pprint.html#module-pprint "pprint: Data pretty printer.")
 and [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")
.

[`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
 and [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 accept `frozendict` for _globals_, and [`type()`](https://docs.python.org/3/builtins/functions.html#type "type")
 and [`str.maketrans()`](https://docs.python.org/3/builtins/stdtypes.html#str.maketrans "str.maketrans")
 accept `frozendict` for _dict_.

Code checking for [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 type using `isinstance(arg, dict)` can be updated to `isinstance(arg, (dict, frozendict))` to accept also the `frozendict` type, or to `isinstance(arg, collections.abc.Mapping)` to accept also other mapping types such as [`MappingProxyType`](https://docs.python.org/3/library/types.html#types.MappingProxyType "types.MappingProxyType")
.

(Contributed by Victor Stinner and Donghee Na in [gh-141510](https://github.com/python/cpython/issues/141510)
.)

See also

[**PEP 814**](https://peps.python.org/pep-0814/)
 for the full specification and rationale.

### [**PEP 661**](https://peps.python.org/pep-0661/)
: Add sentinel built-in type[¶](https://docs.python.org/3/whatsnew/3.15.html#pep-661-add-sentinel-built-in-type "Link to this heading")

A new [`sentinel`](https://docs.python.org/3/builtins/functions.html#sentinel "sentinel")
 type is added to the [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")
 module for creating unique sentinel values with a concise representation. Sentinel objects preserve identity when copied, support use in type expressions with the `|` operator, and can be pickled when they are importable by module and name.

(Contributed by Jelle Zijlstra in [gh-148829](https://github.com/python/cpython/issues/148829)
; PEP 661 written by Tal Einat.)

See also

[**PEP 661**](https://peps.python.org/pep-0661/)
 for further details.

### [**PEP 799**](https://peps.python.org/pep-0799/)
: A dedicated profiling package[¶](https://docs.python.org/3/whatsnew/3.15.html#pep-799-a-dedicated-profiling-package "Link to this heading")

A new [`profiling`](https://docs.python.org/3/library/profiling.html#module-profiling "profiling: Python profiling tools for performance analysis.")
 module has been added to organize Python’s built-in profiling tools under a single, coherent namespace. This module contains:

*   [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
    : deterministic function-call tracing (relocated from `cProfile`).
    
*   [`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")
    : a new statistical sampling profiler (named Tachyon).
    

The `cProfile` module remains as an alias for backwards compatibility. The [`profile`](https://docs.python.org/3/library/profile.html#module-profile "profile: Pure Python profiler (deprecated). (deprecated)")
 module is deprecated and will be removed in Python 3.17.

(Contributed by Pablo Galindo and László Kiss Kollár in [gh-138122](https://github.com/python/cpython/issues/138122)
.)

See also

[**PEP 799**](https://peps.python.org/pep-0799/)
 for further details.

### Tachyon: High-frequency statistical sampling profiler[¶](https://docs.python.org/3/whatsnew/3.15.html#tachyon-high-frequency-statistical-sampling-profiler "Link to this heading")

![Tachyon profiler logo](https://docs.python.org/3/_images/tachyon-logo.png)

A new statistical sampling profiler (Tachyon) has been added as [`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")
. This profiler enables low-overhead performance analysis of running Python processes without requiring code modification or process restart.

Tachyon follows earlier work on external sampling profilers such as [Austin](https://github.com/P403n1x87/austin)
, [py-spy](https://github.com/benfred/py-spy)
, [Pyflame](https://github.com/uber-archive/pyflame)
, and [rbspy](https://github.com/rbspy/rbspy)
. We thank their authors and the wider profiling community for their work and ideas.

Unlike deterministic profilers (such as [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")
) that instrument every function call, the sampling profiler periodically captures stack traces from running processes. This approach provides virtually zero overhead while achieving sampling rates of **up to 1,000,000 Hz**, making it the fastest sampling profiler available for Python (at the time of its contribution) and ideal for debugging performance issues in production environments. This capability is particularly valuable for debugging performance issues in production systems where traditional profiling approaches would be too intrusive.

Key features include:

*   **Zero-overhead profiling**: Attach to any running Python process without affecting its performance. Ideal for production debugging where you can’t afford to restart or slow down your application.
    
*   **No code modification required**: Profile existing applications without restart. Simply point the profiler at a running process by PID and start collecting data.
    
*   **Flexible target modes**:
    
    *   Profile running processes by PID (`attach`) - attach to already-running applications
        
    *   Run and profile scripts directly (`run`) - profile from the very start of execution
        
    *   Execute and profile modules (`run -m`) - profile packages run as `python -m module`
        
    *   Capture a one-shot snapshot of a running process (`dump`) - print a traceback-style stack of every thread (or all asyncio tasks with `--async-aware`). Useful for investigating hung processes.
        
*   **Multiple profiling modes**: Choose what to measure based on your performance investigation:
    
    *   **Wall-clock time** (`--mode wall`, default): Measures real elapsed time including I/O, network waits, and blocking operations. Use this to understand where your program spends calendar time, including when waiting for external resources.
        
    *   **CPU time** (`--mode cpu`): Measures only active CPU execution time, excluding I/O waits and blocking. Use this to identify CPU-bound bottlenecks and optimize computational work.
        
    *   **GIL-holding time** (`--mode gil`): Measures time spent holding Python’s Global Interpreter Lock. Use this to identify which threads dominate GIL usage in multi-threaded applications.
        
    *   **Exception handling time** (`--mode exception`): Captures samples only from threads with an active exception. Use this to analyze exception handling overhead.
        
*   **Thread-aware profiling**: Option to profile all threads (`-a`) or just the main thread, essential for understanding multi-threaded application behavior.
    
*   **Multiple output formats**: Choose the visualization that best fits your workflow:
    
    *   `--pstats`: Detailed tabular statistics compatible with [`pstats`](https://docs.python.org/3/library/pstats.html#module-pstats "pstats: Statistics object for analyzing profiler output.")
        . Shows function-level timing with direct and cumulative samples. Best for detailed analysis and integration with existing Python profiling tools.
        
    *   `--collapsed`: Generates collapsed stack traces (one line per stack). This format is specifically designed for creating flame graphs with external tools like Brendan Gregg’s FlameGraph scripts or speedscope.
        
    *   `--flamegraph`: Generates a self-contained interactive HTML flame graph using D3.js. Opens directly in your browser for immediate visual analysis. Flame graphs show the call hierarchy where width represents time spent, making it easy to spot bottlenecks at a glance.
        
    *   `--gecko`: Generates Gecko Profiler format compatible with [Firefox Profiler](https://profiler.firefox.com/)
        . Upload the output to Firefox Profiler for advanced timeline-based analysis with features like stack charts, markers, and network activity.
        
    *   `--heatmap`: Generates an interactive HTML heatmap visualization with line-level sample counts. Creates a directory with per-file heatmaps showing exactly where time is spent at the source code level.
        
*   **Live interactive mode**: Real-time TUI profiler with a top-like interface (`--live`). Monitor performance as your application runs with interactive sorting and filtering.
    
*   **Async-aware profiling**: Profile async/await code with task-based stack reconstruction (`--async-aware`). See which coroutines are consuming time, with options to show only running tasks or all tasks including those waiting.
    
*   **Opcode-level profiling**: Gather bytecode opcode information for instruction-level profiling (`--opcodes`). Shows which bytecode instructions are executing, including specializations from the adaptive interpreter.
    

See [`profiling.sampling`](https://docs.python.org/3/library/profiling.sampling.html#module-profiling.sampling "profiling.sampling: Statistical sampling profiler for Python processes.")
 for the complete documentation, including all available output formats, profiling modes, and configuration options.

(Contributed by Pablo Galindo and László Kiss Kollár in [gh-135953](https://github.com/python/cpython/issues/135953)
 and [gh-138122](https://github.com/python/cpython/issues/138122)
.)

### [**PEP 831**](https://peps.python.org/pep-0831/)
: Frame pointers enabled by default[¶](https://docs.python.org/3/whatsnew/3.15.html#pep-831-frame-pointers-enabled-by-default "Link to this heading")

CPython is now built with frame pointers by default on platforms that support them. This uses the compiler flags `-fno-omit-frame-pointer` and `-mno-omit-leaf-frame-pointer`, making native stack unwinding faster and more reliable for system profilers, debuggers, crash analysis tools, and eBPF-based observability tools.

The flags are exposed through [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")
, so extension modules built by tools that consume Python’s build configuration inherit frame pointers by default. This propagation is intentional: mixed Python/native profiling needs an unbroken frame-pointer chain through the interpreter, extension modules, embedding applications, and native libraries.

Important

Third-party build backends and native build systems should preserve these flags when they consume Python’s [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")
 values. Build systems that compile C, C++, Rust, or other native code without inheriting Python’s compiler flags should enable equivalent frame-pointer flags themselves. A single native component built without frame pointers can break stack unwinding for the whole Python process.

(Contributed by Pablo Galindo Salgado and Savannah Ostrowski in [gh-149201](https://github.com/python/cpython/issues/149201)
; PEP 831 written by Pablo Galindo Salgado, Ken Jin, Savannah Ostrowski, and Diego Russo.)

See also

[**PEP 831**](https://peps.python.org/pep-0831/)
 for further details.

### [**PEP 798**](https://peps.python.org/pep-0798/)
: Unpacking in comprehensions[¶](https://docs.python.org/3/whatsnew/3.15.html#pep-798-unpacking-in-comprehensions "Link to this heading")

List, set, and dictionary comprehensions, as well as generator expressions, now support unpacking with `*` and `**`. This extends the unpacking syntax from [**PEP 448**](https://peps.python.org/pep-0448/)
 to comprehensions, providing a new syntax for combining an arbitrary number of iterables or dictionaries into a single flat structure. This new syntax is a direct alternative to nested comprehensions, [`itertools.chain()`](https://docs.python.org/3/library/itertools.html#itertools.chain "itertools.chain")
, and [`itertools.chain.from_iterable()`](https://docs.python.org/3/library/itertools.html#itertools.chain.from_iterable "itertools.chain.from_iterable")
. For example:

Copy

\>>> lists \= \[\[1, 2\], \[3, 4\], \[5\]\]
\>>> \[\*L for L in lists\]  \# equivalent to \[x for L in lists for x in L\]
\[1, 2, 3, 4, 5\]

\>>> sets \= \[{1, 2}, {2, 3}, {3, 4}\]
\>>> {\*s for s in sets}  \# equivalent to {x for s in sets for x in s}
{1, 2, 3, 4}

\>>> dicts \= \[{'a': 1}, {'b': 2}, {'a': 3}\]
\>>> {\*\*d for d in dicts}  \# equivalent to {k: v for d in dicts for k,v in d.items()}
{'a': 3, 'b': 2}

Generator expressions can similarly use unpacking to yield values from multiple iterables:

Copy

\>>> gen \= (\*L for L in lists)  \# equivalent to (x for L in lists for x in L)
\>>> list(gen)
\[1, 2, 3, 4, 5\]

This change also extends to asynchronous generator expressions, such that, for example, `(*a async for a in agen())` is equivalent to `(x async for a in agen() for x in a)`.

(Contributed by Adam Hartz in [gh-143055](https://github.com/python/cpython/issues/143055)
.)

See also

[**PEP 798**](https://peps.python.org/pep-0798/)
 for further details.

### [**PEP 829**](https://peps.python.org/pep-0829/)
: Package startup configuration files[¶](https://docs.python.org/3/whatsnew/3.15.html#pep-829-package-startup-configuration-files "Link to this heading")

Loaded by the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module when `-S` is not given, [.pth files](https://docs.python.org/3/library/site.html#site-pth-files)
 can contain lines that both extend [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 and execute arbitrary code when the line starts with `import` (followed by a space or tab). The latter functionality can be problematic, since it is difficult to know exactly what gets executed when Python starts up.

As a step towards improving the ability to audit pre-start executable code, Python 3.15 introduces [.start files](https://docs.python.org/3/library/site.html#site-start-files)
 which contain entry point specifications of the form `pkg.mod:callable` where `pkg.mod` is the import path to the given callable. When Python starts up, the callable is located and called with no arguments.

`import` lines in `.pth` files are silently deprecated. When a matching `.start` file is found, `import` lines in `.pth` files are ignored. There is no change to [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
 extension lines in `.pth` files.

The [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
 module also provides [`site.StartupState`](https://docs.python.org/3/library/site.html#site.StartupState "site.StartupState")
 to batch startup processing for multiple site directories, ensuring all static path extensions are applied before any startup code is executed. [`site.main()`](https://docs.python.org/3/library/site.html#site.main "site.main")
 uses an instance of this class implicitly to batch process all startup configuration files during normal interpreter startup. Callers needing the same batching behavior can build a `StartupState` directly and drive it with [`addsitedir()`](https://docs.python.org/3/library/site.html#site.StartupState.addsitedir "site.StartupState.addsitedir")
, [`addusersitepackages()`](https://docs.python.org/3/library/site.html#site.StartupState.addusersitepackages "site.StartupState.addusersitepackages")
, and [`addsitepackages()`](https://docs.python.org/3/library/site.html#site.StartupState.addsitepackages "site.StartupState.addsitepackages")
, then call [`process()`](https://docs.python.org/3/library/site.html#site.StartupState.process "site.StartupState.process")
 once at the end of the batch.

(Contributed by Barry Warsaw in [gh-148641](https://github.com/python/cpython/issues/148641)
 and [gh-150228](https://github.com/python/cpython/issues/150228)
.)

### [**PEP 803**](https://peps.python.org/pep-0803/)
: Stable ABI for free-threaded builds[¶](https://docs.python.org/3/whatsnew/3.15.html#pep-803-stable-abi-for-free-threaded-builds "Link to this heading")

C extensions that target the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable-abi)
 can now be compiled for the new _Stable ABI for Free-Threaded Builds_ (also known as `abi3t`), which makes them compatible with [free-threaded builds](https://docs.python.org/3/glossary.html#term-free-threaded-build)
 of CPython. This usually requires some non-trivial changes to the source code; specifically:

*   Switching to API introduced in [**PEP 697**](https://peps.python.org/pep-0697/)
     (Python 3.12), such as negative [`basicsize`](https://docs.python.org/3/c-api/type.html#c.PyType_Spec.basicsize "PyType_Spec.basicsize")
     and [`PyObject_GetTypeData()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetTypeData "PyObject_GetTypeData")
    , rather than making [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
     part of the instance struct; and
    
*   Switching from a `PyInit_` function to a new export hook, [`PyModExport_*`](https://docs.python.org/3/c-api/extension-modules.html#c.PyModExport_modulename "PyModExport_modulename")
    , introduced for this purpose in [**PEP 793**](https://peps.python.org/pep-0793/)
    , with a new [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
     structure introduced in [**PEP 820**](https://peps.python.org/pep-0820/)
    .
    

Note that Stable ABI does not offer all the functionality that CPython has to offer. Extensions that cannot switch to `abi3t` should continue to build for the existing Stable ABI (`abi3`) and the version-specific ABI for free-threading (`cp315t`) separately.

Stable ABI for Free-Threaded Builds should typically be selected in a build tool. Tools with `abi3t` support include meson-python, scikit-build-core, and Maturin; see [Setting up the build](https://docs.python.org/3/howto/abi3t-migration.html#abi3t-migration-build)
 for links to their documentation on `abi3t` builds. If your build tool does not support `abi3t`, compile for `cp315t` separately. If not using a build tool – or when writing such a tool – you can select `abi3t` by setting the macro `Py_TARGET_ABI3T` as discussed in [Compiling for Stable ABI](https://docs.python.org/3/c-api/stable.html#abi3-compiling)
.

A practical [migration guide](https://docs.python.org/3/howto/abi3t-migration.html#abi3t-migration-howto)
 for switching to `abi3t` is available. The community-maintained [Python Free-Threading Guide](https://py-free-threading.github.io/abi3t/)
 provides examples of building and testing `abi3t` wheels.

See also

[**PEP 803**](https://peps.python.org/pep-0803/)
 for further details.

### [**PEP 788**](https://peps.python.org/pep-0788/)
: Protecting the C API from interpreter finalization[¶](https://docs.python.org/3/whatsnew/3.15.html#pep-788-protecting-the-c-api-from-interpreter-finalization "Link to this heading")

In the C API, [interpreter finalization](https://docs.python.org/3/glossary.html#term-interpreter-shutdown)
 can be problematic for many extensions, because [attaching](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 a thread state will permanently hang the thread, resulting in deadlocks and other spurious issues. Additionally, it has historically been impossible to safely check whether an interpreter is alive before using it, leading to crashes when a thread concurrently deletes an interpreter while another thread is trying to attach to it.

There are now several new suites of APIs to circumvent these problems:

*   [Interpreter guards](https://docs.python.org/3/c-api/interp-lifecycle.html#interpreter-guards)
    , which prevent an interpreter from finalizing.
    
*   [Interpreter views](https://docs.python.org/3/c-api/interp-lifecycle.html#interpreter-views)
    , which allow thread-safe access to an interpreter that may be concurrently finalizing or deleted.
    
*   [New APIs](https://docs.python.org/3/c-api/threads.html#c-api-attach-detach)
     to automatically attach and detach thread states that come with built-in protection against finalization.
    

In addition, APIs in the `PyGILState` family (most notably [`PyGILState_Ensure()`](https://docs.python.org/3/c-api/threads.html#c.PyGILState_Ensure "PyGILState_Ensure")
 and [`PyGILState_Release()`](https://docs.python.org/3/c-api/threads.html#c.PyGILState_Release "PyGILState_Release")
) have been [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
. There is **no** plan to remove them, and existing code will continue to work, but there will be no new `PyGILState` APIs in future versions of Python.

(Contributed by Peter Bierma in [gh-149101](https://github.com/python/cpython/issues/149101)
.)

See also

[**PEP 788**](https://peps.python.org/pep-0788/)
 for further details.

### Improved error messages[¶](https://docs.python.org/3/whatsnew/3.15.html#improved-error-messages "Link to this heading")

*   The interpreter now provides more helpful suggestions in [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
     exceptions when accessing an attribute on an object that does not exist, but a similar attribute is available through one of its members.
    
    For example, if the object has an attribute that itself exposes the requested name, the error message will suggest accessing it via that inner attribute:
    
    Copy
    
    from dataclasses import dataclass
    from math import pi
    
    @dataclass
    class Circle:
       radius: float
    
       @property
       def area(self) \-> float:
          return pi \* self.radius\*\*2
    
    class Container:
       def \_\_init\_\_(self, inner: Circle) \-> None:
          self.inner \= inner
    
    circle \= Circle(radius\=4.0)
    container \= Container(circle)
    print(container.area)
    
    Running this code now produces a clearer suggestion:
    
    Traceback (most recent call last):
      File "example.py", line 18, in <module>
        print(container.area)
              ^^^^^^^^^^^^^^
    AttributeError: 'Container' object has no attribute 'area'. Did you mean '.inner.area' instead of '.area'?
    
*   When an [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
     on a builtin type has no close match via Levenshtein distance, the error message now checks a static table of common method names from other languages (JavaScript, Java, Ruby, C#) and suggests the Python equivalent:
    
    Copy
    
    \>>> \[1, 2, 3\].push(4)
    Traceback (most recent call last):
    ...
    AttributeError: 'list' object has no attribute 'push'. Did you mean '.append'?
    
    \>>> 'hello'.toUpperCase()
    Traceback (most recent call last):
    ...
    AttributeError: 'str' object has no attribute 'toUpperCase'. Did you mean '.upper'?
    
    When the Python equivalent is a language construct rather than a method, the hint describes the construct directly:
    
    Copy
    
    \>>> {}.put("a", 1)
    Traceback (most recent call last):
    ...
    AttributeError: 'dict' object has no attribute 'put'. Use d\[k\] = v.
    
    When a mutable method is called on an immutable type, the hint suggests the mutable counterpart:
    
    Copy
    
    \>>> (1, 2, 3).append(4)
    Traceback (most recent call last):
    ...
    AttributeError: 'tuple' object has no attribute 'append'. Did you mean to use a 'list' object?
    
    These hints also work for subclasses of builtin types.
    
    (Contributed by Matt Van Horn in [gh-146406](https://github.com/python/cpython/issues/146406)
    .)
    
*   The interpreter now tries to provide a suggestion when [`delattr()`](https://docs.python.org/3/builtins/functions.html#delattr "delattr")
     fails due to a missing attribute. When an attribute name that closely resembles an existing attribute is used, the interpreter will suggest the correct attribute name in the error message. For example:
    
    Copy
    
    \>>> class A:
    ...     pass
    \>>> a \= A()
    \>>> a.abcde \= 1
    \>>> del a.abcdf
    Traceback (most recent call last):
    ...
    AttributeError: 'A' object has no attribute 'abcdf'. Did you mean: 'abcde'?
    
    (Contributed by Nikita Sobolev and Pranjal Prajapati in [gh-136588](https://github.com/python/cpython/issues/136588)
    .)
    
*   Several error messages incorrectly using the term “argument” have been corrected. (Contributed by Stan Ulbrych in [gh-133382](https://github.com/python/cpython/issues/133382)
    .)
    

Other language changes[¶](https://docs.python.org/3/whatsnew/3.15.html#other-language-changes "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

*   Python now uses [UTF-8](https://en.wikipedia.org/wiki/UTF-8)
     as the default encoding, independent of the system’s environment. This means that I/O operations without an explicit encoding, for example, `open('flying-circus.txt')`, will use UTF-8. UTF-8 is a widely-supported [Unicode](https://home.unicode.org/)
     character encoding that has become a _de facto_ standard for representing text, including nearly every webpage on the internet, many common file formats, programming languages, and more.
    
    This only applies when no `encoding` argument is given. For best compatibility between versions of Python, ensure that an explicit `encoding` argument is always provided. The [opt-in encoding warning](https://docs.python.org/3/library/io.html#io-encoding-warning)
     can be used to identify code that may be affected by this change. The special `encoding='locale'` argument uses the current locale encoding, and has been supported since Python 3.10.
    
    To retain the previous behaviour, Python’s UTF-8 mode may be disabled with the [`PYTHONUTF8=0`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8)
     environment variable or the [`-X utf8=0`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
     command-line option.
    
    (Contributed by Adam Turner in [gh-133711](https://github.com/python/cpython/issues/133711)
    ; PEP 686 written by Inada Naoki.)
    
    See also
    
    [**PEP 686**](https://peps.python.org/pep-0686/)
     for further details.
    
*   The interpreter help (such as `python --help`) is now in color. This can be controlled by [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Hugo van Kemenade in [gh-148766](https://github.com/python/cpython/issues/148766)
    .)
    
*   Unraisable exceptions are now highlighted with color by default. This can be controlled by [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Peter Bierma in [gh-134170](https://github.com/python/cpython/issues/134170)
    .)
    
*   More color in [argparse](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-argparse)
    , [ast](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-ast)
    , [calendar](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-calendar)
    , [difflib](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-difflib)
    , [http.server](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-http-server)
    , [pickletools](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-pickletools)
    , [PyREPL tab completion](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-pyrepl-completion)
    , [python –help](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-interpreter-help)
    , [sqlite3](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-sqlite3)
    , [timeit](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-timeit)
    , [tokenize](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-tokenize)
    , [unraisable exceptions](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-color-exceptions)
     and [stdlib](https://docs.python.org/3/glossary.html#term-stdlib)
     (ast, compileall, doctest, gzip, inspect, json.tool, pdb, profiling.sampling, random, regrtest, sqlite3, timeit, tokenize, trace, unittest, uuid, zipapp, zipfile) CLI help.
    
*   The [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__")
     of [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
     and [`ModuleNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#ModuleNotFoundError "ModuleNotFoundError")
     now shows “name” and “path” as `name=<name>` and `path=<path>` if they were given as keyword arguments at construction time. (Contributed by Serhiy Storchaka, Oleg Iarygin, and Yoav Nir in [gh-74185](https://github.com/python/cpython/issues/74185)
    .)
    
*   The [`__dict__`](https://docs.python.org/3/reference/datamodel.html#object.__dict__ "object.__dict__")
     and `__weakref__` descriptors now use a single descriptor instance per interpreter, shared across all types that need them. This speeds up class creation, and helps avoid reference cycles. (Contributed by Petr Viktorin in [gh-135228](https://github.com/python/cpython/issues/135228)
    .)
    
*   The [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W)
     option and the [`PYTHONWARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS)
     environment variable can now specify regular expressions instead of literal strings to match the warning message and the module name, if the corresponding field starts and ends with a forward slash (`/`). (Contributed by Serhiy Storchaka in [gh-134716](https://github.com/python/cpython/issues/134716)
    .)
    
*   Functions that take timestamp or timeout arguments now accept any real numbers (such as [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
     and [`Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction")
    ), not only integers or floats, although this does not improve precision. (Contributed by Serhiy Storchaka in [gh-67795](https://github.com/python/cpython/issues/67795)
    .)
    

*   Added [`bytearray.take_bytes(n=None, /)`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.take_bytes "bytearray.take_bytes")
     to take bytes out of a [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
     without copying. This enables optimizing code which must return [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     after working with a mutable buffer of bytes such as data buffering, network protocol parsing, encoding, decoding, and compression. Common code patterns which can be optimized with [`take_bytes()`](https://docs.python.org/3/builtins/stdtypes.html#bytearray.take_bytes "bytearray.take_bytes")
     are listed below.
    
    |     |     |     |
    | --- | --- | --- |Suggested optimizing refactors[¶](https://docs.python.org/3/whatsnew/3.15.html#id14 "Link to this table")
    | Description | Old | New |
    | --- | --- | --- |
    | Return [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")<br> after working with [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray") | Copy<br><br>def read() \-> bytes:<br>    buffer \= bytearray(1024)<br>    ...<br>    return bytes(buffer) | Copy<br><br>def read() \-> bytes:<br>    buffer \= bytearray(1024)<br>    ...<br>    return buffer.take\_bytes() |
    | Empty a buffer getting the bytes | Copy<br><br>buffer \= bytearray(1024)<br>...<br>data \= bytes(buffer)<br>buffer.clear() | Copy<br><br>buffer \= bytearray(1024)<br>...<br>data \= buffer.take\_bytes() |
    | Split a buffer at a specific separator | Copy<br><br>buffer \= bytearray(b'abc\\ndef')<br>n \= buffer.find(b'\\n')<br>data \= bytes(buffer\[:n + 1\])<br>del buffer\[:n + 1\]<br>assert data \== b'abc\\n'<br>assert buffer \== bytearray(b'def') | Copy<br><br>buffer \= bytearray(b'abc\\ndef')<br>n \= buffer.find(b'\\n')<br>data \= buffer.take\_bytes(n + 1) |
    | Split a buffer at a specific separator; discard after the separator | Copy<br><br>buffer \= bytearray(b'abc\\ndef')<br>n \= buffer.find(b'\\n')<br>data \= bytes(buffer\[:n\])<br>buffer.clear()<br>assert data \== b'abc'<br>assert len(buffer) \== 0 | Copy<br><br>buffer \= bytearray(b'abc\\ndef')<br>n \= buffer.find(b'\\n')<br>buffer.resize(n)<br>data \= buffer.take\_bytes() |
    
    (Contributed by Cody Maloney in [gh-139871](https://github.com/python/cpython/issues/139871)
    .)
    
*   Many functions related to compiling or parsing Python code, such as [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
    , [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse")
    , [`symtable.symtable()`](https://docs.python.org/3/library/symtable.html#symtable.symtable "symtable.symtable")
    , and [`importlib.abc.InspectLoader.source_to_code()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.source_to_code "importlib.abc.InspectLoader.source_to_code")
    , now allow the module name to be passed. It is needed to unambiguously [filter](https://docs.python.org/3/library/warnings.html#warning-filter)
     syntax warnings by module name. (Contributed by Serhiy Storchaka in [gh-135801](https://github.com/python/cpython/issues/135801)
    .)
    
*   Allowed defining the _\_\_dict\_\__ and _\_\_weakref\_\__ [\_\_slots\_\_](https://docs.python.org/3/reference/datamodel.html#slots)
     for any class. (Contributed by Serhiy Storchaka in [gh-41779](https://github.com/python/cpython/issues/41779)
    .)
    
*   Allowed defining any [\_\_slots\_\_](https://docs.python.org/3/reference/datamodel.html#slots)
     for a class derived from [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
     (including classes created by [`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
    ). (Contributed by Serhiy Storchaka in [gh-41779](https://github.com/python/cpython/issues/41779)
    .)
    
*   The [`slice`](https://docs.python.org/3/builtins/functions.html#slice "slice")
     type now supports subscription, making it a [generic type](https://docs.python.org/3/glossary.html#term-generic-type)
    . (Contributed by James Hilton-Balfe in [gh-128335](https://github.com/python/cpython/issues/128335)
    .)
    
*   The class [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
     now supports the float complex and double complex C types: formatting characters `'Zf'` and `'Zd'` respectively. (Contributed by Victor Stinner in [gh-146151](https://github.com/python/cpython/issues/146151)
     and [gh-148675](https://github.com/python/cpython/issues/148675)
    .)
    
*   Allow the _count_ argument of [`bytes.replace()`](https://docs.python.org/3/builtins/stdtypes.html#bytes.replace "bytes.replace")
     to be a keyword. (Contributed by Stan Ulbrych in [gh-147856](https://github.com/python/cpython/issues/147856)
    .)
    
*   Unary plus is now accepted in [`match`](https://docs.python.org/3/reference/compound_stmts.html#match)
     literal patterns, mirroring the existing support for unary minus. (Contributed by Bartosz Sławecki in [gh-145239](https://github.com/python/cpython/issues/145239)
    .)
    
*   The import system now acquires per-module locks in hierarchical order (parent packages before their submodules). This fixes a long-standing deadlock where one thread importing `pkg.sub` and another importing `pkg.sub.mod` could each block the other when `pkg/sub/__init__.py` imports `pkg.sub.mod`. (Contributed by Gregory P. Smith in [gh-83065](https://github.com/python/cpython/issues/83065)
    .)
    
*   File names of Stable ABI extensions that use the `.so` suffix may now include a multiarch tuple, for example, `foo.abi3-x86-64-linux-gnu.so`. This permits stable ABI extensions for multiple architectures to be co-installed into the same directory, without clashing with each other, as regular dynamic extensions do. (Contributed by Stefano Rivera in [gh-122931](https://github.com/python/cpython/issues/122931)
    .)
    
*   The `__cached__` attribute on modules, which was deprecated since version 3.13, is no longer set or taken into consideration by the import system or standard library. Use [`__spec__.cached`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.cached "importlib.machinery.ModuleSpec.cached")
     instead. (Contributed by Brett Cannon in [gh-97879](https://github.com/python/cpython/issues/97879)
    .)
    
    Note that the [`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")
     and [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__")
     attributes are also deprecated and scheduled for removal.
    

Default interactive shell[¶](https://docs.python.org/3/whatsnew/3.15.html#default-interactive-shell "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

*   Tab completions are now colored by object kind, based on [fancycompleter](https://pypi.org/project/fancycompleter/)
    . Set [`PYTHON_BASIC_COMPLETER`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_BASIC_COMPLETER)
     to fall back to [`rlcompleter`](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.")
    . Color can also be controlled by [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Antonio Cuni and Pablo Galindo in [gh-130472](https://github.com/python/cpython/issues/130472)
    .)
    
*   Tab completion now suggests module attributes in `from ... import` statements. Attributes can only be suggested once the module is imported, so [stdlib](https://docs.python.org/3/glossary.html#term-stdlib)
     modules are imported automatically, while for other modules the completer offers to import them when Tab is pressed a second time. (Contributed by Loïc Simon and Pablo Galindo in [gh-140870](https://github.com/python/cpython/issues/140870)
    .)
    

New modules[¶](https://docs.python.org/3/whatsnew/3.15.html#new-modules "Link to this heading")

------------------------------------------------------------------------------------------------

### math.integer[¶](https://docs.python.org/3/whatsnew/3.15.html#math-integer "Link to this heading")

This module provides access to the mathematical functions for integer arguments ([**PEP 791**](https://peps.python.org/pep-0791/)
). (Contributed by Serhiy Storchaka in [gh-81313](https://github.com/python/cpython/issues/81313)
.)

Improved modules[¶](https://docs.python.org/3/whatsnew/3.15.html#improved-modules "Link to this heading")

----------------------------------------------------------------------------------------------------------

### argparse[¶](https://docs.python.org/3/whatsnew/3.15.html#argparse "Link to this heading")

*   The [`BooleanOptionalAction`](https://docs.python.org/3/library/argparse.html#argparse.BooleanOptionalAction "argparse.BooleanOptionalAction")
     action now supports single-dash long options and alternate prefix characters. (Contributed by Serhiy Storchaka in [gh-138525](https://github.com/python/cpython/issues/138525)
    .)
    
*   Changed the _suggest\_on\_error_ parameter of [`argparse.ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
     to default to `True`. This enables suggestions for mistyped arguments by default. (Contributed by Jakob Schluse in [gh-140450](https://github.com/python/cpython/issues/140450)
    .)
    
*   Added backtick markup support in [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
     description and epilog text to highlight inline code when color output is enabled. (Contributed by Savannah Ostrowski in [gh-142390](https://github.com/python/cpython/issues/142390)
    .)
    
*   Extended backtick markup to argument `help` text and added support for double backticks (RST inline-literal style). (Contributed by Hugo van Kemenade in [gh-149375](https://github.com/python/cpython/issues/149375)
    .)
    

### array[¶](https://docs.python.org/3/whatsnew/3.15.html#array "Link to this heading")

*   Support the float complex and double complex C types: formatting characters `'Zf'` and `'Zd'` respectively. (Contributed by Victor Stinner in [gh-146151](https://github.com/python/cpython/issues/146151)
     and [gh-148675](https://github.com/python/cpython/issues/148675)
    .)
    
*   Support half-floats (16-bit IEEE 754 binary interchange format): formatting character `'e'`. (Contributed by Sergey B Kirpichev in [gh-146238](https://github.com/python/cpython/issues/146238)
    .)
    
*   The [`array.typecodes`](https://docs.python.org/3/library/array.html#array.typecodes "array.typecodes")
     type changed from [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     to [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
     to support type codes longer than 1 character (`Zf` and `Zd`). (Contributed by Victor Stinner in [gh-148675](https://github.com/python/cpython/issues/148675)
    .)
    

### ast[¶](https://docs.python.org/3/whatsnew/3.15.html#ast "Link to this heading")

*   Add _color_ parameter to [`dump()`](https://docs.python.org/3/library/ast.html#ast.dump "ast.dump")
    . If `True`, the returned string is syntax highlighted using ANSI escape sequences. If `False` (the default), colored output is always disabled. (Contributed by Stan Ulbrych in [gh-148981](https://github.com/python/cpython/issues/148981)
    .)
    
*   The [command-line](https://docs.python.org/3/library/ast.html#ast-cli)
     output is now syntax highlighted by default. This can be [controlled using environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Stan Ulbrych in [gh-148981](https://github.com/python/cpython/issues/148981)
    .)
    

### asyncio[¶](https://docs.python.org/3/whatsnew/3.15.html#asyncio "Link to this heading")

*   Added [`TaskGroup.cancel`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup.cancel "asyncio.TaskGroup.cancel")
     to allow early termination of a task group, for instance, when the goal of the tasks has been achieved or their services are no longer needed. Previously this would involve unintuitive boilerplate such as an extra task raising a custom exception which is then suppressed as it exits the task group. (Contributed by John Belmonte in [gh-127214](https://github.com/python/cpython/issues/127214)
    .)
    

### base64[¶](https://docs.python.org/3/whatsnew/3.15.html#base64 "Link to this heading")

*   Added the _pad_ parameter in [`z85encode()`](https://docs.python.org/3/library/base64.html#base64.z85encode "base64.z85encode")
    . (Contributed by Hauke Dämpfling in [gh-143103](https://github.com/python/cpython/issues/143103)
    .)
    
*   Added the _padded_ parameter in [`b32encode()`](https://docs.python.org/3/library/base64.html#base64.b32encode "base64.b32encode")
    , [`b32decode()`](https://docs.python.org/3/library/base64.html#base64.b32decode "base64.b32decode")
    , [`b32hexencode()`](https://docs.python.org/3/library/base64.html#base64.b32hexencode "base64.b32hexencode")
    , [`b32hexdecode()`](https://docs.python.org/3/library/base64.html#base64.b32hexdecode "base64.b32hexdecode")
    , [`b64encode()`](https://docs.python.org/3/library/base64.html#base64.b64encode "base64.b64encode")
    , [`b64decode()`](https://docs.python.org/3/library/base64.html#base64.b64decode "base64.b64decode")
    , [`urlsafe_b64encode()`](https://docs.python.org/3/library/base64.html#base64.urlsafe_b64encode "base64.urlsafe_b64encode")
    , and [`urlsafe_b64decode()`](https://docs.python.org/3/library/base64.html#base64.urlsafe_b64decode "base64.urlsafe_b64decode")
    . (Contributed by Serhiy Storchaka in [gh-73613](https://github.com/python/cpython/issues/73613)
    .)
    
*   Added the _wrapcol_ parameter in [`b16encode()`](https://docs.python.org/3/library/base64.html#base64.b16encode "base64.b16encode")
    , [`b32encode()`](https://docs.python.org/3/library/base64.html#base64.b32encode "base64.b32encode")
    , [`b32hexencode()`](https://docs.python.org/3/library/base64.html#base64.b32hexencode "base64.b32hexencode")
    , [`b64encode()`](https://docs.python.org/3/library/base64.html#base64.b64encode "base64.b64encode")
    , [`b85encode()`](https://docs.python.org/3/library/base64.html#base64.b85encode "base64.b85encode")
    , and [`z85encode()`](https://docs.python.org/3/library/base64.html#base64.z85encode "base64.z85encode")
    . (Contributed by Serhiy Storchaka in [gh-143214](https://github.com/python/cpython/issues/143214)
     and [gh-146431](https://github.com/python/cpython/issues/146431)
    .)
    
*   Added the _ignorechars_ parameter in [`b16decode()`](https://docs.python.org/3/library/base64.html#base64.b16decode "base64.b16decode")
    , [`b32decode()`](https://docs.python.org/3/library/base64.html#base64.b32decode "base64.b32decode")
    , [`b32hexdecode()`](https://docs.python.org/3/library/base64.html#base64.b32hexdecode "base64.b32hexdecode")
    , [`b64decode()`](https://docs.python.org/3/library/base64.html#base64.b64decode "base64.b64decode")
    , [`b85decode()`](https://docs.python.org/3/library/base64.html#base64.b85decode "base64.b85decode")
    , and [`z85decode()`](https://docs.python.org/3/library/base64.html#base64.z85decode "base64.z85decode")
    . (Contributed by Serhiy Storchaka in [gh-144001](https://github.com/python/cpython/issues/144001)
     and [gh-146431](https://github.com/python/cpython/issues/146431)
    .)
    
*   Added the _canonical_ parameter in [`b32decode()`](https://docs.python.org/3/library/base64.html#base64.b32decode "base64.b32decode")
    , [`b32hexdecode()`](https://docs.python.org/3/library/base64.html#base64.b32hexdecode "base64.b32hexdecode")
    , [`b64decode()`](https://docs.python.org/3/library/base64.html#base64.b64decode "base64.b64decode")
    , [`a85decode()`](https://docs.python.org/3/library/base64.html#base64.a85decode "base64.a85decode")
    , [`b85decode()`](https://docs.python.org/3/library/base64.html#base64.b85decode "base64.b85decode")
    , and [`z85decode()`](https://docs.python.org/3/library/base64.html#base64.z85decode "base64.z85decode")
    , to reject encodings with non-zero padding bits or other non-canonical forms. (Contributed by Gregory P. Smith in [gh-146311](https://github.com/python/cpython/issues/146311)
    .)
    

### binascii[¶](https://docs.python.org/3/whatsnew/3.15.html#binascii "Link to this heading")

*   Added functions for Base32 encoding:
    
    *   [`b2a_base32()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_base32 "binascii.b2a_base32")
         and [`a2b_base32()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base32 "binascii.a2b_base32")
        
    
    (Contributed by James Seo in [gh-146192](https://github.com/python/cpython/issues/146192)
    .)
    
*   Added functions for Ascii85, Base85, and Z85 encoding:
    
    *   [`b2a_ascii85()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_ascii85 "binascii.b2a_ascii85")
         and [`a2b_ascii85()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_ascii85 "binascii.a2b_ascii85")
        
    *   [`b2a_base85()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_base85 "binascii.b2a_base85")
         and [`a2b_base85()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base85 "binascii.a2b_base85")
        
    
    (Contributed by James Seo and Serhiy Storchaka in [gh-101178](https://github.com/python/cpython/issues/101178)
    .)
    
*   Added the _padded_ parameter in [`b2a_base32()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_base32 "binascii.b2a_base32")
    , [`a2b_base32()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base32 "binascii.a2b_base32")
    , [`b2a_base64()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_base64 "binascii.b2a_base64")
    , and [`a2b_base64()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base64 "binascii.a2b_base64")
    . (Contributed by Serhiy Storchaka in [gh-73613](https://github.com/python/cpython/issues/73613)
    .)
    
*   Added the _wrapcol_ parameter in [`b2a_base64()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_base64 "binascii.b2a_base64")
    . (Contributed by Serhiy Storchaka in [gh-143214](https://github.com/python/cpython/issues/143214)
    .)
    
*   Added the _alphabet_ parameter in [`b2a_base64()`](https://docs.python.org/3/library/binascii.html#binascii.b2a_base64 "binascii.b2a_base64")
     and [`a2b_base64()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base64 "binascii.a2b_base64")
    . (Contributed by Serhiy Storchaka in [gh-145980](https://github.com/python/cpython/issues/145980)
    .)
    
*   Added the _ignorechars_ parameter in [`a2b_hex()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_hex "binascii.a2b_hex")
    , [`unhexlify()`](https://docs.python.org/3/library/binascii.html#binascii.unhexlify "binascii.unhexlify")
    , and [`a2b_base64()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base64 "binascii.a2b_base64")
    . (Contributed by Serhiy Storchaka in [gh-144001](https://github.com/python/cpython/issues/144001)
     and [gh-146431](https://github.com/python/cpython/issues/146431)
    .)
    
*   Added the _canonical_ parameter in [`a2b_base64()`](https://docs.python.org/3/library/binascii.html#binascii.a2b_base64 "binascii.a2b_base64")
    , to reject encodings with non-zero padding bits. (Contributed by Gregory P. Smith in [gh-146311](https://github.com/python/cpython/issues/146311)
    .)
    

### calendar[¶](https://docs.python.org/3/whatsnew/3.15.html#calendar "Link to this heading")

*   [`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.")
    ’s [command-line](https://docs.python.org/3/library/calendar.html#calendar-cli)
     text output has more color. This can be controlled with [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Hugo van Kemenade in [gh-148352](https://github.com/python/cpython/issues/148352)
    .)
    
*   The [`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.")
    ’s [command-line](https://docs.python.org/3/library/calendar.html#calendar-cli)
     HTML output now accepts the year-month option: `python -m calendar -t html 2009 06`. (Contributed by Pål Grønås Drange in [gh-140212](https://github.com/python/cpython/issues/140212)
    .)
    
*   Calendar pages generated by the [`calendar.HTMLCalendar`](https://docs.python.org/3/library/calendar.html#calendar.HTMLCalendar "calendar.HTMLCalendar")
     class now support dark mode and have been migrated to the HTML5 standard for improved accessibility. (Contributed by Jiahao Li and Hugo van Kemenade in [gh-137634](https://github.com/python/cpython/issues/137634)
    .)
    

### collections[¶](https://docs.python.org/3/whatsnew/3.15.html#collections "Link to this heading")

*   Added `collections.Counter.__xor__()` and `collections.Counter.__ixor__()` to compute the symmetric difference between [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter")
     objects. (Contributed by Raymond Hettinger in [gh-138682](https://github.com/python/cpython/issues/138682)
    .)
    

### concurrent.futures[¶](https://docs.python.org/3/whatsnew/3.15.html#concurrent-futures "Link to this heading")

*   Improved error reporting when a child process in a [`concurrent.futures.ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor")
     terminates abruptly. The resulting traceback will now tell you the PID and exit code of the terminated process. (Contributed by Jonathan Berg in [gh-139486](https://github.com/python/cpython/issues/139486)
    .)
    

### contextlib[¶](https://docs.python.org/3/whatsnew/3.15.html#contextlib "Link to this heading")

*   Added support for arbitrary descriptors `__enter__()`, `__exit__()`, `__aenter__()`, and `__aexit__()` in [`ExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
     and [`contextlib.AsyncExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.AsyncExitStack "contextlib.AsyncExitStack")
    , for consistency with the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
     and [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
     statements. (Contributed by Serhiy Storchaka in [gh-144386](https://github.com/python/cpython/issues/144386)
    .)
    
*   [`ContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator "contextlib.ContextDecorator")
     and [`AsyncContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.AsyncContextDecorator "contextlib.AsyncContextDecorator")
     (and therefore [`contextmanager()`](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager "contextlib.contextmanager")
     and [`asynccontextmanager()`](https://docs.python.org/3/library/contextlib.html#contextlib.asynccontextmanager "contextlib.asynccontextmanager")
     used as decorators) now detect generator functions, coroutine functions, and asynchronous generator functions and keep the context manager open across iteration or await. Previously the context manager exited as soon as the generator or coroutine object was created. (Contributed by Alex Grönholm & Gregory P. Smith in [gh-125862](https://github.com/python/cpython/issues/125862)
    .)
    

### ctypes[¶](https://docs.python.org/3/whatsnew/3.15.html#ctypes "Link to this heading")

*   Change the [`_type_`](https://docs.python.org/3/library/ctypes.html#ctypes._SimpleCData._type_ "ctypes._SimpleCData._type_")
     of [`c_float_complex`](https://docs.python.org/3/library/ctypes.html#ctypes.c_float_complex "ctypes.c_float_complex")
    , [`c_double_complex`](https://docs.python.org/3/library/ctypes.html#ctypes.c_double_complex "ctypes.c_double_complex")
     and [`c_longdouble_complex`](https://docs.python.org/3/library/ctypes.html#ctypes.c_longdouble_complex "ctypes.c_longdouble_complex")
     from `F`, `D` and `G` to `Zf`, `Zd` and `Zg` for compatibility with NumPy. (Contributed by Victor Stinner in [gh-148675](https://github.com/python/cpython/issues/148675)
    .)
    

### dataclasses[¶](https://docs.python.org/3/whatsnew/3.15.html#dataclasses "Link to this heading")

*   Annotations for generated `__init__` methods no longer include internal type names. (Contributed by David Ellis in [gh-137530](https://github.com/python/cpython/issues/137530)
    .)
    

### dbm[¶](https://docs.python.org/3/whatsnew/3.15.html#dbm "Link to this heading")

*   Added new `reorganize()` methods to [`dbm.dumb`](https://docs.python.org/3/library/dbm.html#module-dbm.dumb "dbm.dumb: Portable implementation of the simple DBM interface.")
     and [`dbm.sqlite3`](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm")
     to recover unused free space previously occupied by deleted entries. (Contributed by Andrea Oliveri in [gh-134004](https://github.com/python/cpython/issues/134004)
    .)
    

### difflib[¶](https://docs.python.org/3/whatsnew/3.15.html#difflib "Link to this heading")

*   Introduced the optional _color_ parameter to [`difflib.unified_diff()`](https://docs.python.org/3/library/difflib.html#difflib.unified_diff "difflib.unified_diff")
    , enabling color output similar to **git diff**. This can be controlled by [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Douglas Thor in [gh-133725](https://github.com/python/cpython/issues/133725)
    .)
    
*   Improved the styling of HTML diff pages generated by the [`difflib.HtmlDiff`](https://docs.python.org/3/library/difflib.html#difflib.HtmlDiff "difflib.HtmlDiff")
     class, and migrated the output to the HTML5 standard. (Contributed by Jiahao Li in [gh-134580](https://github.com/python/cpython/issues/134580)
    .)
    

### email[¶](https://docs.python.org/3/whatsnew/3.15.html#email "Link to this heading")

*   Email generators now raise an error when an [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
     cannot be accurately flattened due to a non-ASCII email address (mailbox) in an address header. Options for supporting Email Address Internationalization (EAI) are discussed in [`EmailPolicy.utf8`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.utf8 "email.policy.EmailPolicy.utf8")
    . (Contributed by R David Murray and Mike Edmunds in [gh-122540](https://github.com/python/cpython/issues/122540)
    .)
    

### faulthandler[¶](https://docs.python.org/3/whatsnew/3.15.html#faulthandler "Link to this heading")

*   Added the _max\_threads_ parameter in [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable")
    , [`faulthandler.dump_traceback()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback "faulthandler.dump_traceback")
    , [`faulthandler.dump_traceback_later()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "faulthandler.dump_traceback_later")
    , and [`faulthandler.register()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.register "faulthandler.register")
    . (Contributed by Eric Froemling in [gh-149085](https://github.com/python/cpython/issues/149085)
    .)
    

### functools[¶](https://docs.python.org/3/whatsnew/3.15.html#functools "Link to this heading")

*   [`singledispatchmethod()`](https://docs.python.org/3/library/functools.html#functools.singledispatchmethod "functools.singledispatchmethod")
     now supports non-[descriptor](https://docs.python.org/3/glossary.html#term-descriptor)
     callables. (Contributed by Serhiy Storchaka in [gh-140873](https://github.com/python/cpython/issues/140873)
    .)
    
*   [`singledispatchmethod()`](https://docs.python.org/3/library/functools.html#functools.singledispatchmethod "functools.singledispatchmethod")
     now dispatches on the second argument if it wraps a regular method and is called as a class attribute. (Contributed by Bartosz Sławecki in [gh-143535](https://github.com/python/cpython/issues/143535)
    .)
    

### gc[¶](https://docs.python.org/3/whatsnew/3.15.html#gc "Link to this heading")

*   Python 3.14.0-3.14.4 shipped with a new incremental garbage collector. However, due to a number of [reports](https://github.com/python/cpython/issues/142516)
     of significant memory pressure in production environments, it has been reverted back to the generational GC from 3.13. This is the GC now used in Python 3.14.5 and later and Python 3.15. (Contributed by Sergey Miryanov in [gh-148726](https://github.com/python/cpython/issues/148726)
    .)
    

### hashlib[¶](https://docs.python.org/3/whatsnew/3.15.html#hashlib "Link to this heading")

*   Ensure that hash functions guaranteed to be always _available_ exist as attributes of [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
     even if they will not work at runtime due to missing backend implementations. For instance, `hashlib.md5` will no longer raise [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
     if OpenSSL is not available and Python has been built without MD5 support. (Contributed by Bénédikt Tran in [gh-136929](https://github.com/python/cpython/issues/136929)
    .)
    

### http.client[¶](https://docs.python.org/3/whatsnew/3.15.html#http-client "Link to this heading")

*   A new _max\_response\_headers_ keyword-only parameter has been added to [`HTTPConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection "http.client.HTTPConnection")
     and [`HTTPSConnection`](https://docs.python.org/3/library/http.client.html#http.client.HTTPSConnection "http.client.HTTPSConnection")
     constructors. This parameter overrides the default maximum number of allowed response headers. (Contributed by Alexander Enrique Urieles Nieto in [gh-131724](https://github.com/python/cpython/issues/131724)
    .)
    

### http.server[¶](https://docs.python.org/3/whatsnew/3.15.html#http-server "Link to this heading")

*   The logging of [`BaseHTTPRequestHandler`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler "http.server.BaseHTTPRequestHandler")
    , as used by the [command-line interface](https://docs.python.org/3/library/http.server.html#http-server-cli)
    , is colored by default. This can be controlled with [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Hugo van Kemenade in [gh-146292](https://github.com/python/cpython/issues/146292)
    .)
    
*   Added [`default_content_type`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.default_content_type "http.server.SimpleHTTPRequestHandler.default_content_type")
     and the [`--content-type`](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-content-type)
     command-line option to allow customizing the default `Content-Type` header for files with unknown extensions. (Contributed by John Comeau and Hugo van Kemenade in [gh-113471](https://github.com/python/cpython/issues/113471)
    .)
    
*   Add a new `extra_response_headers` keyword argument to [`SimpleHTTPRequestHandler`](https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler "http.server.SimpleHTTPRequestHandler")
     to support custom headers in HTTP responses. (Contributed by Anton I. Sipos in [gh-135057](https://github.com/python/cpython/issues/135057)
    .)
    
*   Add a [`-H/--header`](https://docs.python.org/3/library/http.server.html#cmdoption-http.server-H)
     option to the **python -m http.server** command-line interface to support custom headers in HTTP responses. (Contributed by Anton I. Sipos in [gh-135057](https://github.com/python/cpython/issues/135057)
    .)
    

### importlib.metadata[¶](https://docs.python.org/3/whatsnew/3.15.html#importlib-metadata "Link to this heading")

*   Previously, when accessing a distribution metadata directory not containing a metadata file, `metadata()` and `Distribution.metadata` would return an empty `PackageMetadata` object as if the file was present but empty. Now, a `MetadataNotFound` exception is raised. See [importlib\_metadata#493](https://github.com/python/importlib_metadata/issues/493)
     for background and rationale and [gh-143387](https://github.com/python/cpython/issues/143387)
     for rationale on the compatibility concerns. (Contributed by Jason R. Coombs.)
    

### inspect[¶](https://docs.python.org/3/whatsnew/3.15.html#inspect "Link to this heading")

*   Add parameters _inherit\_class\_doc_ and _fallback\_to\_class\_doc_ for [`getdoc()`](https://docs.python.org/3/library/inspect.html#inspect.getdoc "inspect.getdoc")
    . (Contributed by Serhiy Storchaka in [gh-132686](https://github.com/python/cpython/issues/132686)
    .)
    

### json[¶](https://docs.python.org/3/whatsnew/3.15.html#json "Link to this heading")

*   Add the _array\_hook_ parameter to [`load()`](https://docs.python.org/3/library/json.html#json.load "json.load")
     and [`loads()`](https://docs.python.org/3/library/json.html#json.loads "json.loads")
     functions: allow a callback for JSON literal array types to customize Python lists in the resulting decoded object. Passing combined [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")
     to _object\_pairs\_hook_ parameter and [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
     to _array\_hook_ will yield a deeply nested immutable Python structure representing the JSON data. (Contributed by Joao S. O. Bueno in [gh-146440](https://github.com/python/cpython/issues/146440)
    .)
    

### locale[¶](https://docs.python.org/3/whatsnew/3.15.html#locale "Link to this heading")

*   [`setlocale()`](https://docs.python.org/3/library/locale.html#locale.setlocale "locale.setlocale")
     now supports language codes with `@`\-modifiers. `@`\-modifiers are no longer silently removed in [`getlocale()`](https://docs.python.org/3/library/locale.html#locale.getlocale "locale.getlocale")
    , but included in the language code. (Contributed by Serhiy Storchaka in [gh-137729](https://github.com/python/cpython/issues/137729)
    .)
    
*   Undeprecate the [`locale.getdefaultlocale()`](https://docs.python.org/3/library/locale.html#locale.getdefaultlocale "locale.getdefaultlocale")
     function. (Contributed by Victor Stinner in [gh-130796](https://github.com/python/cpython/issues/130796)
    .)
    

### math[¶](https://docs.python.org/3/whatsnew/3.15.html#math "Link to this heading")

*   Add [`math.isnormal()`](https://docs.python.org/3/library/math.html#math.isnormal "math.isnormal")
     and [`math.issubnormal()`](https://docs.python.org/3/library/math.html#math.issubnormal "math.issubnormal")
     functions. (Contributed by Sergey B Kirpichev in [gh-132908](https://github.com/python/cpython/issues/132908)
    .)
    
*   Add [`math.fmax()`](https://docs.python.org/3/library/math.html#math.fmax "math.fmax")
    , [`math.fmin()`](https://docs.python.org/3/library/math.html#math.fmin "math.fmin")
     and [`math.signbit()`](https://docs.python.org/3/library/math.html#math.signbit "math.signbit")
     functions. (Contributed by Bénédikt Tran in [gh-135853](https://github.com/python/cpython/issues/135853)
    .)
    

### mimetypes[¶](https://docs.python.org/3/whatsnew/3.15.html#mimetypes "Link to this heading")

*   Add more MIME types. (Contributed by Benedikt Johannes, Charlie Lin, Foolbar, Gil Forcada and John Franey in [gh-144217](https://github.com/python/cpython/issues/144217)
    , [gh-145720](https://github.com/python/cpython/issues/145720)
    , [gh-140937](https://github.com/python/cpython/issues/140937)
    , [gh-139959](https://github.com/python/cpython/issues/139959)
    , [gh-145698](https://github.com/python/cpython/issues/145698)
    , [gh-145718](https://github.com/python/cpython/issues/145718)
    , [gh-145918](https://github.com/python/cpython/issues/145918)
    , and [gh-144213](https://github.com/python/cpython/issues/144213)
    .)
    
*   Rename `application/x-texinfo` to `application/texinfo`. (Contributed by Charlie Lin in [gh-140165](https://github.com/python/cpython/issues/140165)
    .)
    
*   Changed the MIME type for `.ai` files to `application/pdf`. (Contributed by Stan Ulbrych in [gh-141239](https://github.com/python/cpython/issues/141239)
    .)
    

### mmap[¶](https://docs.python.org/3/whatsnew/3.15.html#mmap "Link to this heading")

*   [`mmap.mmap`](https://docs.python.org/3/library/mmap.html#mmap.mmap "mmap.mmap")
     now has a _trackfd_ parameter on Windows; if it is `False`, the file handle corresponding to _fileno_ will not be duplicated. (Contributed by Serhiy Storchaka in [gh-78502](https://github.com/python/cpython/issues/78502)
    .)
    
*   Added the [`mmap.mmap.set_name()`](https://docs.python.org/3/library/mmap.html#mmap.mmap.set_name "mmap.mmap.set_name")
     method to annotate an anonymous memory mapping if Linux kernel supports _[PR\_SET\_VMA\_ANON\_NAME](https://manpages.debian.org/PR_SET_VMA(2const))
    _ (Linux 5.17 or newer). (Contributed by Donghee Na in [gh-142419](https://github.com/python/cpython/issues/142419)
    .)
    

### os[¶](https://docs.python.org/3/whatsnew/3.15.html#os "Link to this heading")

*   Add [`os.statx()`](https://docs.python.org/3/library/os.html#os.statx "os.statx")
     on Linux kernel versions 4.11 and later with glibc versions 2.28 and later. (Contributed by Jeffrey Bosboom and Victor Stinner in [gh-83714](https://github.com/python/cpython/issues/83714)
    .)
    
*   [`os.makedirs()`](https://docs.python.org/3/library/os.html#os.makedirs "os.makedirs")
     function now has a _parent\_mode_ parameter that allows specifying the mode for intermediate directories. This can be used to match the behavior from Python 3.6 and earlier by passing `parent_mode=mode`. (Contributed by Zackery Spytz and Gregory P. Smith in [gh-86533](https://github.com/python/cpython/issues/86533)
    .)
    

### os.path[¶](https://docs.python.org/3/whatsnew/3.15.html#os-path "Link to this heading")

*   Add support of the all-but-last mode in [`realpath()`](https://docs.python.org/3/library/os.path.html#os.path.realpath "os.path.realpath")
    . (Contributed by Serhiy Storchaka in [gh-71189](https://github.com/python/cpython/issues/71189)
    .)
    
*   The _strict_ parameter to [`os.path.realpath()`](https://docs.python.org/3/library/os.path.html#os.path.realpath "os.path.realpath")
     accepts a new value, [`os.path.ALLOW_MISSING`](https://docs.python.org/3/library/os.path.html#os.path.ALLOW_MISSING "os.path.ALLOW_MISSING")
    . If used, errors other than [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
     will be re-raised; the resulting path can be missing but it will be free of symlinks. (Contributed by Petr Viktorin for [**CVE 2025-4517**](https://www.cve.org/CVERecord?id=CVE-2025-4517)
    .)
    

### pathlib[¶](https://docs.python.org/3/whatsnew/3.15.html#pathlib "Link to this heading")

*   [`pathlib.Path.mkdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir "pathlib.Path.mkdir")
     now has a _parent\_mode_ parameter that allows specifying the mode for intermediate directories when `parents=True`. (Contributed by Gregory P. Smith in [gh-86533](https://github.com/python/cpython/issues/86533)
    .)
    

### pdb[¶](https://docs.python.org/3/whatsnew/3.15.html#pdb "Link to this heading")

*   Use the new interactive shell as the default input shell for [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")
    . (Contributed by Tian Gao in [gh-145379](https://github.com/python/cpython/issues/145379)
    .)
    

### pickle[¶](https://docs.python.org/3/whatsnew/3.15.html#pickle "Link to this heading")

*   Add support for pickling private methods and nested classes. (Contributed by Zackery Spytz and Serhiy Storchaka in [gh-77188](https://github.com/python/cpython/issues/77188)
    .)
    

### pickletools[¶](https://docs.python.org/3/whatsnew/3.15.html#pickletools "Link to this heading")

*   The output of the [`pickletools`](https://docs.python.org/3/library/pickletools.html#module-pickletools "pickletools: Contains extensive comments about the pickle protocols and pickle-machine opcodes, as well as some useful functions.")
     command-line interface is colored by default. This can be controlled with [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Hugo van Kemenade in [gh-149026](https://github.com/python/cpython/issues/149026)
    .)
    

### pprint[¶](https://docs.python.org/3/whatsnew/3.15.html#pprint "Link to this heading")

*   Add an _expand_ keyword argument for [`pprint.pprint()`](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint")
    , [`pprint.pformat()`](https://docs.python.org/3/library/pprint.html#pprint.pformat "pprint.pformat")
    , [`pprint.pp()`](https://docs.python.org/3/library/pprint.html#pprint.pp "pprint.pp")
    . If true, the output will be formatted similar to pretty-printed [`json.dumps()`](https://docs.python.org/3/library/json.html#json.dumps "json.dumps")
     when _indent_ is supplied. (Contributed by Stefan Todoran, Semyon Moroz and Hugo van Kemenade in [gh-112632](https://github.com/python/cpython/issues/112632)
    .)
    
*   Add t-string support to [`pprint`](https://docs.python.org/3/library/pprint.html#module-pprint "pprint: Data pretty printer.")
    . (Contributed by Loïc Simon and Hugo van Kemenade in [gh-134551](https://github.com/python/cpython/issues/134551)
    .)
    

### re[¶](https://docs.python.org/3/whatsnew/3.15.html#re "Link to this heading")

*   [`re.prefixmatch()`](https://docs.python.org/3/library/re.html#re.prefixmatch "re.prefixmatch")
     and a corresponding [`re.Pattern.prefixmatch()`](https://docs.python.org/3/library/re.html#re.Pattern.prefixmatch "re.Pattern.prefixmatch")
     have been added as alternate, more explicit names for the existing and now [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
     [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match")
     and [`re.Pattern.match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match")
     APIs. These are intended to be used to alleviate confusion around what _match_ means by following the Zen of Python’s _“Explicit is better than implicit”_ mantra. Most other language regular expression libraries use an API named _match_ to mean what Python has always called _search_. (Contributed by Gregory P. Smith in [gh-86519](https://github.com/python/cpython/issues/86519)
    .)
    

### resource[¶](https://docs.python.org/3/whatsnew/3.15.html#resource "Link to this heading")

*   Add new constants: [`RLIMIT_NTHR`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_NTHR "resource.RLIMIT_NTHR")
    , [`RLIMIT_UMTXP`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_UMTXP "resource.RLIMIT_UMTXP")
    , [`RLIMIT_THREADS`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_THREADS "resource.RLIMIT_THREADS")
    , [`RLIM_SAVED_CUR`](https://docs.python.org/3/library/resource.html#resource.RLIM_SAVED_CUR "resource.RLIM_SAVED_CUR")
    , and [`RLIM_SAVED_MAX`](https://docs.python.org/3/library/resource.html#resource.RLIM_SAVED_MAX "resource.RLIM_SAVED_MAX")
    . (Contributed by Serhiy Storchaka in [gh-137512](https://github.com/python/cpython/issues/137512)
    .)
    

### shelve[¶](https://docs.python.org/3/whatsnew/3.15.html#shelve "Link to this heading")

*   Added new `reorganize()` method to [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.")
     used to recover unused free space previously occupied by deleted entries. (Contributed by Andrea Oliveri in [gh-134004](https://github.com/python/cpython/issues/134004)
    .)
    
*   Add support for custom serialization and deserialization functions in the [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.")
     module. (Contributed by Furkan Onder in [gh-99631](https://github.com/python/cpython/issues/99631)
    .)
    

### socket[¶](https://docs.python.org/3/whatsnew/3.15.html#socket "Link to this heading")

*   Add constants for the ISO-TP CAN protocol. (Contributed by Patrick Menschel and Stefan Tatschner in [gh-86819](https://github.com/python/cpython/issues/86819)
    .)
    

### sqlite3[¶](https://docs.python.org/3/whatsnew/3.15.html#sqlite3 "Link to this heading")

*   The [command-line interface](https://docs.python.org/3/library/sqlite3.html#sqlite3-cli)
     has several new features:
    
    *   SQL keyword completion on Tab. (Contributed by Long Tan in [gh-133393](https://github.com/python/cpython/issues/133393)
        .)
        
    
    *   Prompts, error messages, and help text are now colored. This is enabled by default, see [Controlling color](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
         for details. (Contributed by Stan Ulbrych and Łukasz Langa in [gh-133461](https://github.com/python/cpython/issues/133461)
        .)
        
    *   Table, index, trigger, view, column, function, and schema completion on Tab. (Contributed by Long Tan in [gh-136101](https://github.com/python/cpython/issues/136101)
        .)
        

### ssl[¶](https://docs.python.org/3/whatsnew/3.15.html#ssl "Link to this heading")

*   Indicate through [`ssl.HAS_PSK_TLS13`](https://docs.python.org/3/library/ssl.html#ssl.HAS_PSK_TLS13 "ssl.HAS_PSK_TLS13")
     whether the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
     module supports “External PSKs” in TLSv1.3, as described in [**RFC 9258**](https://datatracker.ietf.org/doc/html/rfc9258.html)
    . (Contributed by Will Childs-Klein in [gh-133624](https://github.com/python/cpython/issues/133624)
    .)
    
*   Added new methods for managing groups used for SSL key agreement:
    
    *   [`ssl.SSLContext.set_groups()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_groups "ssl.SSLContext.set_groups")
         sets the groups allowed for doing key agreement, extending the previous [`ssl.SSLContext.set_ecdh_curve()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ecdh_curve "ssl.SSLContext.set_ecdh_curve")
         method. This new API provides the ability to list multiple groups and supports finite-field and post-quantum groups in addition to ECDH curves. This method can also be used to control what key shares are sent in the TLS handshake.
        
    *   [`ssl.SSLSocket.group()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.group "ssl.SSLSocket.group")
         returns the group selected for doing key agreement on the current connection after the TLS handshake completes. This call requires OpenSSL 3.2 or later.
        
    *   [`ssl.SSLContext.get_groups()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.get_groups "ssl.SSLContext.get_groups")
         returns a list of all available key agreement groups compatible with the minimum and maximum TLS versions currently set in the context. This call requires OpenSSL 3.5 or later.
        
    
    (Contributed by Ron Frederick in [gh-136306](https://github.com/python/cpython/issues/136306)
    .)
    
*   Added a new method [`ssl.SSLContext.set_ciphersuites()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ciphersuites "ssl.SSLContext.set_ciphersuites")
     for setting TLS 1.3 ciphers. For TLS 1.2 or earlier, [`ssl.SSLContext.set_ciphers()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ciphers "ssl.SSLContext.set_ciphers")
     should continue to be used. Both calls can be made on the same context and the selected cipher suite will depend on the TLS version negotiated when a connection is made. (Contributed by Ron Frederick in [gh-137197](https://github.com/python/cpython/issues/137197)
    .)
    
*   Added new methods for managing signature algorithms:
    
    *   [`ssl.get_sigalgs()`](https://docs.python.org/3/library/ssl.html#ssl.get_sigalgs "ssl.get_sigalgs")
         returns a list of all available TLS signature algorithms. This call requires OpenSSL 3.4 or later.
        
    *   [`ssl.SSLContext.set_client_sigalgs()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_client_sigalgs "ssl.SSLContext.set_client_sigalgs")
         sets the signature algorithms allowed for certificate-based client authentication.
        
    *   [`ssl.SSLContext.set_server_sigalgs()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_server_sigalgs "ssl.SSLContext.set_server_sigalgs")
         sets the signature algorithms allowed for the server to complete the TLS handshake.
        
    *   [`ssl.SSLSocket.client_sigalg()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.client_sigalg "ssl.SSLSocket.client_sigalg")
         returns the signature algorithm selected for client authentication on the current connection. This call requires OpenSSL 3.5 or later.
        
    *   [`ssl.SSLSocket.server_sigalg()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.server_sigalg "ssl.SSLSocket.server_sigalg")
         returns the signature algorithm selected for the server to complete the TLS handshake on the current connection. This call requires OpenSSL 3.5 or later.
        
    
    (Contributed by Ron Frederick in [gh-138252](https://github.com/python/cpython/issues/138252)
    .)
    

### subprocess[¶](https://docs.python.org/3/whatsnew/3.15.html#subprocess "Link to this heading")

*   [`subprocess.Popen.wait()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait "subprocess.Popen.wait")
    : when `timeout` is not `None` and the platform supports it, an efficient event-driven mechanism is used to wait for process termination:
    
    *   Linux >= 5.3 uses [`os.pidfd_open()`](https://docs.python.org/3/library/os.html#os.pidfd_open "os.pidfd_open")
         + [`select.poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll")
        .
        
    *   macOS and other BSD variants use [`select.kqueue()`](https://docs.python.org/3/library/select.html#select.kqueue "select.kqueue")
         + `KQ_FILTER_PROC` + `KQ_NOTE_EXIT`.
        
    *   Windows keeps using `WaitForSingleObject` (unchanged).
        
    
    If none of these mechanisms are available, the function falls back to the traditional busy loop (non-blocking call and short sleeps). (Contributed by Giampaolo Rodola in [gh-83069](https://github.com/python/cpython/issues/83069)
    .)
    

### symtable[¶](https://docs.python.org/3/whatsnew/3.15.html#symtable "Link to this heading")

*   Add [`symtable.Function.get_cells()`](https://docs.python.org/3/library/symtable.html#symtable.Function.get_cells "symtable.Function.get_cells")
     and [`symtable.Symbol.is_cell()`](https://docs.python.org/3/library/symtable.html#symtable.Symbol.is_cell "symtable.Symbol.is_cell")
     methods. (Contributed by Yashp002 in [gh-143504](https://github.com/python/cpython/issues/143504)
    .)
    

### sys[¶](https://docs.python.org/3/whatsnew/3.15.html#sys "Link to this heading")

*   Add [`sys.abi_info`](https://docs.python.org/3/library/sys.html#sys.abi_info "sys.abi_info")
     namespace to improve access to ABI information. (Contributed by Klaus Zimmermann in [gh-137476](https://github.com/python/cpython/issues/137476)
    .)
    

### sys.monitoring[¶](https://docs.python.org/3/whatsnew/3.15.html#sys-monitoring "Link to this heading")

*   The [other events](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-global)
     ([`PY_THROW`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_THROW)
    , [`PY_UNWIND`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-PY_UNWIND)
    , [`RAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RAISE)
    , [`EXCEPTION_HANDLED`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-EXCEPTION_HANDLED)
    , and [`RERAISE`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-RERAISE)
    ) can now be turned on and disabled on a per code object basis. Returning [`DISABLE`](https://docs.python.org/3/library/sys.monitoring.html#sys.monitoring.DISABLE "sys.monitoring.DISABLE")
     from a callback for one of these events disables the event for the entire code object (for the current tool), rather than raising [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     as in prior versions. (Contributed by Gabriele N. Tornetta in [gh-146182](https://github.com/python/cpython/issues/146182)
    .)
    

### tarfile[¶](https://docs.python.org/3/whatsnew/3.15.html#tarfile "Link to this heading")

*   [`data_filter()`](https://docs.python.org/3/library/tarfile.html#tarfile.data_filter "tarfile.data_filter")
     now normalizes symbolic link targets in order to avoid path traversal attacks. (Contributed by Petr Viktorin in [gh-127987](https://github.com/python/cpython/issues/127987)
     and [**CVE 2025-4138**](https://www.cve.org/CVERecord?id=CVE-2025-4138)
    .)
    
*   [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
     now skips fixing up directory attributes when a directory was removed or replaced by another kind of file. (Contributed by Petr Viktorin in [gh-127987](https://github.com/python/cpython/issues/127987)
     and [**CVE 2024-12718**](https://www.cve.org/CVERecord?id=CVE-2024-12718)
    .)
    
*   [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
     and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
     now (re-)apply the extraction filter when substituting a link (hard or symbolic) with a copy of another archive member, and when fixing up directory attributes. The former raises a new exception, [`LinkFallbackError`](https://docs.python.org/3/library/tarfile.html#tarfile.LinkFallbackError "tarfile.LinkFallbackError")
    . (Contributed by Petr Viktorin for [**CVE 2025-4330**](https://www.cve.org/CVERecord?id=CVE-2025-4330)
     and [**CVE 2024-12718**](https://www.cve.org/CVERecord?id=CVE-2024-12718)
    .)
    
*   [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
     and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
     no longer extract rejected members when [`errorlevel()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.errorlevel "tarfile.TarFile.errorlevel")
     is zero. (Contributed by Matt Prodani and Petr Viktorin in [gh-112887](https://github.com/python/cpython/issues/112887)
     and [**CVE 2025-4435**](https://www.cve.org/CVERecord?id=CVE-2025-4435)
    .)
    
*   [`extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract")
     and [`extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall")
     now replace slashes with backslashes in symlink targets on Windows to prevent creation of corrupted links. (Contributed by Christoph Walcher in [gh-57911](https://github.com/python/cpython/issues/57911)
    .)
    
*   [`gettarinfo()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.gettarinfo "tarfile.TarFile.gettarinfo")
     now replaces backslashes with slashes in symlink targets on Windows to conform to the tar format standard. (Contributed by Daniele Nicolodi in [gh-151669](https://github.com/python/cpython/issues/151669)
    .)
    

### threading[¶](https://docs.python.org/3/whatsnew/3.15.html#threading "Link to this heading")

*   Added [`serialize_iterator`](https://docs.python.org/3/library/threading.html#threading.serialize_iterator "threading.serialize_iterator")
    , [`synchronized_iterator()`](https://docs.python.org/3/library/threading.html#threading.synchronized_iterator "threading.synchronized_iterator")
    , and [`concurrent_tee()`](https://docs.python.org/3/library/threading.html#threading.concurrent_tee "threading.concurrent_tee")
     to support concurrent access to generators and iterators. (Contributed by Raymond Hettinger in [gh-124397](https://github.com/python/cpython/issues/124397)
    .)
    

### timeit[¶](https://docs.python.org/3/whatsnew/3.15.html#timeit "Link to this heading")

*   The output of the [`timeit`](https://docs.python.org/3/library/timeit.html#module-timeit "timeit: Measure the execution time of small code snippets.")
     command-line interface is colored by default. This can be controlled with [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Hugo van Kemenade in [gh-146609](https://github.com/python/cpython/issues/146609)
    .)
    
*   The command-line interface now colorizes error tracebacks by default. This can be controlled with [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Yi Hong in [gh-139374](https://github.com/python/cpython/issues/139374)
    .)
    
*   Make the target time of [`timeit.Timer.autorange()`](https://docs.python.org/3/library/timeit.html#timeit.Timer.autorange "timeit.Timer.autorange")
     configurable and add `--target-time` option to the command-line interface. (Contributed by Alessandro Cucci and Miikka Koskinen in [gh-80642](https://github.com/python/cpython/issues/80642)
    .)
    

### tkinter[¶](https://docs.python.org/3/whatsnew/3.15.html#tkinter "Link to this heading")

*   The `tkinter.Text.search()` method now supports two additional arguments: _nolinestop_ which allows the search to continue across line boundaries; and _strictlimits_ which restricts the search to within the specified range. (Contributed by Rihaan Meher in [gh-130848](https://github.com/python/cpython/issues/130848)
    .)
    
*   A new method `tkinter.Text.search_all()` has been introduced. This method allows for searching for all matches of a pattern using Tcl’s `-all` and `-overlap` options. (Contributed by Rihaan Meher in [gh-130848](https://github.com/python/cpython/issues/130848)
    .)
    
*   Added new methods `pack_content()`, `place_content()` and `grid_content()` which use Tk commands with new names (introduced in Tk 8.6) instead of `*_slaves()` methods which use Tk commands with outdated names. (Contributed by Serhiy Storchaka in [gh-143754](https://github.com/python/cpython/issues/143754)
    .)
    
*   Added `Event` attributes `user_data` for Tk virtual events and `detail` for `Enter`, `Leave`, `FocusIn`, `FocusOut`, and `ConfigureRequest` events. (Contributed by Matthias Kievernagel and Serhiy Storchaka in [gh-47655](https://github.com/python/cpython/issues/47655)
    .)
    

### tokenize[¶](https://docs.python.org/3/whatsnew/3.15.html#tokenize "Link to this heading")

*   The output of the [`tokenize`](https://docs.python.org/3/library/tokenize.html#module-tokenize "tokenize: Lexical scanner for Python source code.")
     [command-line interface](https://docs.python.org/3/library/tokenize.html#tokenize-cli)
     is colored by default. This can be controlled with [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)
    . (Contributed by Hugo van Kemenade in [gh-148991](https://github.com/python/cpython/issues/148991)
    .)
    

### tomllib[¶](https://docs.python.org/3/whatsnew/3.15.html#tomllib "Link to this heading")

*   The [`tomllib`](https://docs.python.org/3/library/tomllib.html#module-tomllib "tomllib: Parse TOML files.")
     module now supports TOML 1.1.0. This is a backwards compatible update, meaning that all valid TOML 1.0.0 documents are parsed the same way.
    
    The changes, according to the [official TOML changelog](https://github.com/toml-lang/toml/blob/main/CHANGELOG.md)
    , are:
    
    *   Allow newlines and trailing commas in inline tables.
        
        Previously an inline table had to be on a single line and couldn’t end with a trailing comma. This is now relaxed so that the following is valid:
        
        tbl \= {
           key      \= "a string",
           moar-tbl \=  {
              key \= 1,
           },
        }
        
    *   Add `\xHH` notation to basic strings for codepoints under 255, and the `\e` escape for the escape character:
        
        null \= "null byte: \\x00; letter a: \\x61"
        csi \= "\\e\["\
        \
    *   Seconds in datetime and time values are now optional. The following are now valid:\
        \
        dt \= 2010-02-03 14:15\
        t  \= 14:15\
        \
    \
    (Contributed by Taneli Hukkinen in [gh-142956](https://github.com/python/cpython/issues/142956)\
    .)\
    \
\
### types[¶](https://docs.python.org/3/whatsnew/3.15.html#types "Link to this heading")\
\
*   Expose the write-through [`locals()`](https://docs.python.org/3/builtins/functions.html#locals "locals")\
     proxy type as [`types.FrameLocalsProxyType`](https://docs.python.org/3/library/types.html#types.FrameLocalsProxyType "types.FrameLocalsProxyType")\
    . This represents the type of the [`frame.f_locals`](https://docs.python.org/3/reference/datamodel.html#frame.f_locals "frame.f_locals")\
     attribute, as described in [**PEP 667**](https://peps.python.org/pep-0667/)\
    . (Contributed by Peter Bierma in [gh-136492](https://github.com/python/cpython/issues/136492)\
    .)\
    \
\
### typing[¶](https://docs.python.org/3/whatsnew/3.15.html#typing "Link to this heading")\
\
*   [**PEP 747**](https://peps.python.org/pep-0747/)\
    : Add [`TypeForm`](https://docs.python.org/3/library/typing.html#typing.TypeForm "typing.TypeForm")\
    , a new special form for annotating values that are themselves type expressions. `TypeForm[T]` means “a type form object describing `T` (or a type assignable to `T`)”. At runtime, `TypeForm(x)` simply returns `x`, which allows explicit annotation of type-form values without changing behavior.\
    \
    This helps libraries that accept user-provided type expressions (for example `int`, `str | None`, [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict")\
     classes, or `list[int]`) expose precise signatures:\
    \
    Copy\
    \
    from typing import Any, TypeForm\
    \
    def cast\[T\](typ: TypeForm\[T\], value: Any) \-> T: ...\
    \
    (Contributed by Jelle Zijlstra in [gh-145033](https://github.com/python/cpython/issues/145033)\
    .)\
    \
\
*   [**PEP 728**](https://peps.python.org/pep-0728/)\
    : Add support in [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict")\
     for the _closed_ and _extra\_items_ class arguments. A closed `TypedDict` does not allow extra keys beyond those specified in the class body, while a `TypedDict` with `extra_items` allows arbitrary extra items where the values are of the specified type. (Contributed by Angela Liss in [gh-137840](https://github.com/python/cpython/issues/137840)\
    .)\
    \
*   Code like `class ExtraTypeVars(P1[S], Protocol[T, T2]): ...` now raises a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")\
    , because `S` is not listed in `Protocol` parameters. (Contributed by Nikita Sobolev in [gh-137191](https://github.com/python/cpython/issues/137191)\
    .)\
    \
*   Code like `class B2(A[T2], Protocol[T1, T2]): ...` now correctly handles type parameters order: it is `(T1, T2)`, not `(T2, T1)` as it was incorrectly inferred at runtime before. (Contributed by Nikita Sobolev in [gh-137191](https://github.com/python/cpython/issues/137191)\
    .)\
    \
*   [**PEP 800**](https://peps.python.org/pep-0800/)\
    : Add [`@typing.disjoint_base`](https://docs.python.org/3/library/typing.html#typing.disjoint_base "typing.disjoint_base")\
    , a new decorator marking a class as a disjoint base. This is an advanced feature primarily intended to allow type checkers to faithfully reflect the runtime semantics of types defined as builtins or in compiled extensions. If a class `C` is a disjoint base, then child classes of that class cannot inherit from other disjoint bases that are not parent or child classes of `C`. (Contributed by Jelle Zijlstra in [gh-148639](https://github.com/python/cpython/issues/148639)\
    .)\
    \
*   [`TypeVarTuple`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple")\
     now accepts `bound`, `covariant`, `contravariant`, and `infer_variance` keyword arguments, matching the interface of [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar")\
     and [`ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec")\
    . `bound` semantics remain undefined in the specification.\
    \
\
### unicodedata[¶](https://docs.python.org/3/whatsnew/3.15.html#unicodedata "Link to this heading")\
\
*   The Unicode database has been updated to Unicode 17.0.0. (Contributed by Benjamin Peterson in [gh-138706](https://github.com/python/cpython/issues/138706)\
    .)\
    \
*   Add [`unicodedata.isxidstart()`](https://docs.python.org/3/library/unicodedata.html#unicodedata.isxidstart "unicodedata.isxidstart")\
     and [`unicodedata.isxidcontinue()`](https://docs.python.org/3/library/unicodedata.html#unicodedata.isxidcontinue "unicodedata.isxidcontinue")\
     functions to check whether a character can start or continue a [Unicode Standard Annex #31](https://www.unicode.org/reports/tr31/)\
     identifier. (Contributed by Stan Ulbrych in [gh-129117](https://github.com/python/cpython/issues/129117)\
    .)\
    \
*   Add the [`iter_graphemes()`](https://docs.python.org/3/library/unicodedata.html#unicodedata.iter_graphemes "unicodedata.iter_graphemes")\
     function to iterate over grapheme clusters according to rules defined in [Unicode Standard Annex #29, “Unicode Text Segmentation”](https://www.unicode.org/reports/tr29/)\
    . Add [`grapheme_cluster_break()`](https://docs.python.org/3/library/unicodedata.html#unicodedata.grapheme_cluster_break "unicodedata.grapheme_cluster_break")\
    , [`indic_conjunct_break()`](https://docs.python.org/3/library/unicodedata.html#unicodedata.indic_conjunct_break "unicodedata.indic_conjunct_break")\
     and [`extended_pictographic()`](https://docs.python.org/3/library/unicodedata.html#unicodedata.extended_pictographic "unicodedata.extended_pictographic")\
     functions to get the properties of the character which are related to the above algorithm. (Contributed by Serhiy Storchaka and Guillaume Sanchez in [gh-74902](https://github.com/python/cpython/issues/74902)\
    .)\
    \
*   Add [`block()`](https://docs.python.org/3/library/unicodedata.html#unicodedata.block "unicodedata.block")\
     function to return the [Unicode block](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G64189)\
     assigned to a character. (Contributed by Stan Ulbrych in [gh-66802](https://github.com/python/cpython/issues/66802)\
    .)\
    \
\
### unittest[¶](https://docs.python.org/3/whatsnew/3.15.html#unittest "Link to this heading")\
\
*   [`unittest.TestCase.assertLogs()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs "unittest.TestCase.assertLogs")\
     will now accept a formatter to control how messages are formatted. (Contributed by Garry Cairns in [gh-134567](https://github.com/python/cpython/issues/134567)\
    .)\
    \
*   [`unittest.TestCase.assertWarns()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns")\
     and [`unittest.TestCase.assertWarnsRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "unittest.TestCase.assertWarnsRegex")\
     no longer swallow warnings that do not match the specified category or regex. Nested context managers are now supported. (Contributed by Serhiy Storchaka in [gh-143231](https://github.com/python/cpython/issues/143231)\
    .)\
    \
\
### urllib.parse[¶](https://docs.python.org/3/whatsnew/3.15.html#urllib-parse "Link to this heading")\
\
*   Add the _missing\_as\_none_ parameter to [`urlsplit()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlsplit "urllib.parse.urlsplit")\
    , [`urlparse()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse "urllib.parse.urlparse")\
     and [`urldefrag()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urldefrag "urllib.parse.urldefrag")\
     functions. Add the _keep\_empty_ parameter to [`urlunsplit()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlunsplit "urllib.parse.urlunsplit")\
     and [`urlunparse()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlunparse "urllib.parse.urlunparse")\
     functions. This allows distinguishing between empty and undefined URI components and preserving empty components. (Contributed by Serhiy Storchaka in [gh-67041](https://github.com/python/cpython/issues/67041)\
    .)\
    \
\
### venv[¶](https://docs.python.org/3/whatsnew/3.15.html#venv "Link to this heading")\
\
*   On POSIX platforms, platlib directories will be created if needed when creating virtual environments, instead of using a `lib64 -> lib` symlink. This means purelib and platlib of virtual environments no longer share the same `lib` directory on platforms where [`sys.platlibdir`](https://docs.python.org/3/library/sys.html#sys.platlibdir "sys.platlibdir")\
     is not equal to `lib`. (Contributed by Rui Xi in [gh-133951](https://github.com/python/cpython/issues/133951)\
    .)\
    \
\
### warnings[¶](https://docs.python.org/3/whatsnew/3.15.html#warnings "Link to this heading")\
\
*   Improve filtering by module in [`warnings.warn_explicit()`](https://docs.python.org/3/library/warnings.html#warnings.warn_explicit "warnings.warn_explicit")\
     if no _module_ argument is passed. It now tests the module regular expression in the warnings filter not only against the filename with `.py` stripped, but also against module names constructed starting from different parent directories of the filename (with `/__init__.py`, `.py` and, on Windows, `.pyw` stripped). (Contributed by Serhiy Storchaka in [gh-135801](https://github.com/python/cpython/issues/135801)\
    .)\
    \
\
### wave[¶](https://docs.python.org/3/whatsnew/3.15.html#wave "Link to this heading")\
\
*   Added support for IEEE floating-point WAVE audio (`WAVE_FORMAT_IEEE_FLOAT`) in [`wave`](https://docs.python.org/3/library/wave.html#module-wave "wave: Provide an interface to the WAV sound format.")\
    .\
    \
*   Added [`wave.Wave_read.getformat()`](https://docs.python.org/3/library/wave.html#wave.Wave_read.getformat "wave.Wave_read.getformat")\
    , [`wave.Wave_write.getformat()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.getformat "wave.Wave_write.getformat")\
    , and [`wave.Wave_write.setformat()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.setformat "wave.Wave_write.setformat")\
     for explicit frame format handling.\
    \
*   [`wave.Wave_write.setparams()`](https://docs.python.org/3/library/wave.html#wave.Wave_write.setparams "wave.Wave_write.setparams")\
     accepts both 7-item tuples including `format` and 6-item tuples for backwards compatibility (defaulting to `WAVE_FORMAT_PCM`).\
    \
*   `WAVE_FORMAT_IEEE_FLOAT` output now includes a `fact` chunk, as required for non-PCM WAVE formats.\
    \
\
(Contributed by Lionel Koenig and Michiel W. Beijen in [gh-60729](https://github.com/python/cpython/issues/60729)\
.)\
\
### webbrowser[¶](https://docs.python.org/3/whatsnew/3.15.html#webbrowser "Link to this heading")\
\
*   On macOS, the new `webbrowser.MacOS` class opens URLs via **/usr/bin/open** instead of constructing and executing AppleScript via **osascript**. The default browser is detected from the LaunchServices preferences file using [`plistlib`](https://docs.python.org/3/library/plistlib.html#module-plistlib "plistlib: Generate and parse Apple plist files.")\
    , with `com.apple.Safari` as the fallback on fresh installations. For non-HTTP(S) URLs, **open -b <bundle-id>** is used to route the URL through a browser rather than the OS file handler, preventing file injection attacks. (Contributed by Jeff Lyon in [gh-137586](https://github.com/python/cpython/issues/137586)\
    .)\
    \
\
### xml[¶](https://docs.python.org/3/whatsnew/3.15.html#xml "Link to this heading")\
\
*   Add the [`xml.is_valid_name()`](https://docs.python.org/3/library/xml.html#xml.is_valid_name "xml.is_valid_name")\
     function to check whether a string can be used as an element or attribute name in XML. (Contributed by Serhiy Storchaka in [gh-139489](https://github.com/python/cpython/issues/139489)\
    .)\
    \
*   Add the [`xml.is_valid_text()`](https://docs.python.org/3/library/xml.html#xml.is_valid_text "xml.is_valid_text")\
     function to check whether a string can be used in an XML document. (Contributed by Serhiy Storchaka in [gh-139489](https://github.com/python/cpython/issues/139489)\
    .)\
    \
\
### xml.parsers.expat[¶](https://docs.python.org/3/whatsnew/3.15.html#xml-parsers-expat "Link to this heading")\
\
*   Add [`SetAllocTrackerActivationThreshold()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold "xml.parsers.expat.xmlparser.SetAllocTrackerActivationThreshold")\
     and [`SetAllocTrackerMaximumAmplification()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetAllocTrackerMaximumAmplification "xml.parsers.expat.xmlparser.SetAllocTrackerMaximumAmplification")\
     to [xmlparser](https://docs.python.org/3/library/pyexpat.html#xmlparser-objects)\
     objects to tune protections against disproportional amounts of dynamic memory usage from within an Expat parser. (Contributed by Bénédikt Tran in [gh-90949](https://github.com/python/cpython/issues/90949)\
    .)\
    \
*   Add [`SetBillionLaughsAttackProtectionActivationThreshold()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBillionLaughsAttackProtectionActivationThreshold "xml.parsers.expat.xmlparser.SetBillionLaughsAttackProtectionActivationThreshold")\
     and [`SetBillionLaughsAttackProtectionMaximumAmplification()`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.SetBillionLaughsAttackProtectionMaximumAmplification "xml.parsers.expat.xmlparser.SetBillionLaughsAttackProtectionMaximumAmplification")\
     to [xmlparser](https://docs.python.org/3/library/pyexpat.html#xmlparser-objects)\
     objects to tune protections against [billion laughs](https://en.wikipedia.org/wiki/Billion_laughs_attack)\
     attacks. (Contributed by Bénédikt Tran in [gh-90949](https://github.com/python/cpython/issues/90949)\
    .)\
    \
\
### zlib[¶](https://docs.python.org/3/whatsnew/3.15.html#zlib "Link to this heading")\
\
*   Allow combining two Adler-32 checksums via [`adler32_combine()`](https://docs.python.org/3/library/zlib.html#zlib.adler32_combine "zlib.adler32_combine")\
    . (Contributed by Callum Attryde and Bénédikt Tran in [gh-134635](https://github.com/python/cpython/issues/134635)\
    .)\
    \
*   Allow combining two CRC-32 checksums via [`crc32_combine()`](https://docs.python.org/3/library/zlib.html#zlib.crc32_combine "zlib.crc32_combine")\
    . (Contributed by Bénédikt Tran in [gh-134635](https://github.com/python/cpython/issues/134635)\
    .)\
    \
\
Optimizations[¶](https://docs.python.org/3/whatsnew/3.15.html#optimizations "Link to this heading")\
\
----------------------------------------------------------------------------------------------------\
\
*   `mimalloc` is now used as the default allocator for raw memory allocations such as via [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")\
     for better performance on [free-threaded builds](https://docs.python.org/3/glossary.html#term-free-threaded-build)\
    . (Contributed by Kumar Aditya in [gh-144914](https://github.com/python/cpython/issues/144914)\
    .)\
    \
\
### base64 & binascii[¶](https://docs.python.org/3/whatsnew/3.15.html#base64-binascii "Link to this heading")\
\
*   CPython’s underlying base64 implementation now encodes 2x faster and decodes 3x faster thanks to simple CPU pipelining optimizations. (Contributed by Gregory P. Smith and Serhiy Storchaka in [gh-143262](https://github.com/python/cpython/issues/143262)\
    .)\
    \
*   Implementation for Ascii85, Base85, and Z85 encoding has been rewritten in C. Encoding and decoding is now two orders of magnitude faster and consumes two orders of magnitude less memory. (Contributed by James Seo and Serhiy Storchaka in [gh-101178](https://github.com/python/cpython/issues/101178)\
    .)\
    \
*   Implementation for Base32 has been rewritten in C. Encoding and decoding is now two orders of magnitude faster. (Contributed by James Seo in [gh-146192](https://github.com/python/cpython/issues/146192)\
    .)\
    \
\
### csv[¶](https://docs.python.org/3/whatsnew/3.15.html#csv "Link to this heading")\
\
*   [`csv.Sniffer.sniff()`](https://docs.python.org/3/library/csv.html#csv.Sniffer.sniff "csv.Sniffer.sniff")\
     delimiter detection is now up to 1.6x faster. (Contributed by Maurycy Pawłowski-Wieroński in [gh-137628](https://github.com/python/cpython/issues/137628)\
    .)\
    \
\
### Upgraded experimental JIT compiler[¶](https://docs.python.org/3/whatsnew/3.15.html#upgraded-experimental-jit-compiler "Link to this heading")\
\
Results from the [pyperformance](https://github.com/python/pyperformance)\
 benchmark suite report a [7-8%](https://www.doesjitgobrrr.com/run/2026-09-25)\
 geometric mean performance improvement for the JIT over the standard CPython interpreter built with all optimizations enabled on x86-64 Linux. On AArch64 macOS, the JIT has an [11-12%](https://www.doesjitgobrrr.com/run/2026-09-25)\
 speedup over the [tail calling interpreter](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-tail-call-interpreter)\
 with all optimizations enabled. The speedups for JIT builds versus no JIT builds range from roughly 15% slowdown to over 100% speedup (ignoring the `unpack_sequence` microbenchmark) on x86-64 Linux and AArch64 macOS systems.\
\
The major upgrades to the JIT are:\
\
*   LLVM 21 build-time dependency\
    \
*   New tracing frontend\
    \
*   Basic register allocation in the JIT\
    \
*   More JIT optimizations\
    \
*   GDB and GNU `backtrace()` unwinding support\
    \
*   Better machine code generation\
    \
\
LLVM 21 build-time dependency\
\
The JIT compiler now uses LLVM 21 for build-time stencil generation. As always, LLVM is only needed when building CPython with the JIT enabled; end users running Python do not need LLVM installed. Instructions for installing LLVM can be found in the [JIT compiler documentation](https://github.com/python/cpython/blob/main/Tools/jit/README.md)\
 for all supported platforms. (Contributed by Savannah Ostrowski in [gh-140973](https://github.com/python/cpython/issues/140973)\
.)\
\
A new tracing frontend\
\
The JIT compiler now supports significantly more bytecode operations and control flow than in Python 3.14, enabling speedups on a wider variety of code. For example, simple Python object creation is now understood by the 3.15 JIT compiler. Overloaded operations and generators are also partially supported. This was made possible by an overhauled JIT tracing frontend that records actual execution paths through code, rather than estimating them as the previous implementation did. (Contributed by Ken Jin in [gh-139109](https://github.com/python/cpython/issues/139109)\
. Support for Windows added by Mark Shannon in [gh-141703](https://github.com/python/cpython/issues/141703)\
.)\
\
Basic register allocation in the JIT\
\
A basic form of register allocation has been added to the JIT compiler’s optimizer. This allows the JIT compiler to avoid certain stack operations altogether and instead operate on registers. This allows the JIT to produce more efficient traces by avoiding reads and writes to memory. (Contributed by Mark Shannon in [gh-135379](https://github.com/python/cpython/issues/135379)\
.)\
\
More JIT optimizations\
\
More [constant-propagation](https://en.wikipedia.org/wiki/Constant_folding)\
 is now performed. This means when the JIT compiler detects that certain user code results in constants, the code can be simplified by the JIT. (Contributed by Ken Jin and Savannah Ostrowski in [gh-132732](https://github.com/python/cpython/issues/132732)\
.)\
\
[Reference counts](https://docs.python.org/3/glossary.html#term-reference-count)\
 are avoided whenever it is safe to do so. This generally reduces the cost of most operations in Python. (Contributed by Ken Jin, Donghee Na, Zheao Li, Hai Zhu, Savannah Ostrowski, Reiden Ong, Noam Cohen, Tomas Roun, PuQing, Cajetan Rodrigues, and Sacul in [gh-134584](https://github.com/python/cpython/issues/134584)\
.)\
\
By tracking unique references to objects, the JIT optimizer can now eliminate reference count updates and perform in-place operations on ints and floats. (Contributed by Reiden Ong, and Pieter Eendebak in [gh-143414](https://github.com/python/cpython/issues/143414)\
 and [gh-146306](https://github.com/python/cpython/issues/146306)\
.)\
\
The JIT optimizer now supports significantly more operations than in 3.14. (Contributed by Kumar Aditya, Ken Jin, Jiahao Li, and Sacul in [gh-131798](https://github.com/python/cpython/issues/131798)\
.)\
\
GDB and GNU `backtrace()` unwinding support\
\
The JIT compiler now publishes unwind information for generated machine code to the GDB interface on supported Linux ELF platforms. When libgcc frame registration is available, the same unwind information is also registered for GNU `backtrace()` stack walkers. This allows native debuggers, crash handlers, and diagnostic tools using these mechanisms to unwind through JIT frames instead of stopping at generated code. (Contributed by Diego Russo and Pablo Galindo Salgado in [gh-146071](https://github.com/python/cpython/issues/146071)\
 and [gh-149104](https://github.com/python/cpython/issues/149104)\
.)\
\
Better machine code generation\
\
The JIT compiler’s machine code generator now produces better machine code for x86-64 and AArch64 macOS and Linux targets. In general, users should experience lower memory usage for generated machine code and more efficient machine code versus 3.14. (Contributed by Brandt Bucher in [gh-136528](https://github.com/python/cpython/issues/136528)\
 and [gh-135905](https://github.com/python/cpython/issues/135905)\
. Implementation for AArch64 contributed by Mark Shannon in [gh-139855](https://github.com/python/cpython/issues/139855)\
. Additional optimizations for AArch64 contributed by Mark Shannon and Diego Russo in [gh-140683](https://github.com/python/cpython/issues/140683)\
 and [gh-142305](https://github.com/python/cpython/issues/142305)\
.)\
\
Maintainability\
\
The JIT optimizer’s operations have been simplified. This was made possible by a refactoring of JIT data structures. (Contributed by Zhongtian Zheng in [gh-148211](https://github.com/python/cpython/issues/148211)\
 and Hai Zhu in [gh-143421](https://github.com/python/cpython/issues/143421)\
.)\
\
Removed[¶](https://docs.python.org/3/whatsnew/3.15.html#removed "Link to this heading")\
\
----------------------------------------------------------------------------------------\
\
### ast[¶](https://docs.python.org/3/whatsnew/3.15.html#id1 "Link to this heading")\
\
*   The constructors of [AST nodes](https://docs.python.org/3/library/ast.html#ast-nodes)\
     now raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")\
     when a required argument is omitted or when a keyword argument that does not map to a field on the AST node is passed. These cases had previously raised a [`DeprecationWarning`](https://docs.python.org/3/builtins/exceptions.html#DeprecationWarning "DeprecationWarning")\
     since Python 3.13. (Contributed by Brian Schubert and Jelle Zijlstra in [gh-137600](https://github.com/python/cpython/issues/137600)\
     and [gh-105858](https://github.com/python/cpython/issues/105858)\
    .)\
    \
\
### collections.abc[¶](https://docs.python.org/3/whatsnew/3.15.html#collections-abc "Link to this heading")\
\
*   [`collections.abc.ByteString`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ByteString "collections.abc.ByteString")\
     has been removed from `collections.abc.__all__`. `collections.abc.ByteString` has been deprecated since Python 3.12, and is scheduled for removal in Python 3.17. (Contributed by Alex Waygood in [gh-118803](https://github.com/python/cpython/issues/118803)\
    .)\
    \
\
### ctypes[¶](https://docs.python.org/3/whatsnew/3.15.html#id2 "Link to this heading")\
\
*   Removed the undocumented function `ctypes.SetPointerType()`, which has been deprecated since Python 3.13. (Contributed by Bénédikt Tran in [gh-133866](https://github.com/python/cpython/issues/133866)\
    .)\
    \
\
### datetime[¶](https://docs.python.org/3/whatsnew/3.15.html#datetime "Link to this heading")\
\
*   [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime")\
     now raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")\
     when the format string contains `%d` (day of month) without a year directive. This has been deprecated since Python 3.13. (Contributed by Stan Ulbrych and Gregory P. Smith in [gh-70647](https://github.com/python/cpython/issues/70647)\
    .)\
    \
\
### glob[¶](https://docs.python.org/3/whatsnew/3.15.html#glob "Link to this heading")\
\
*   Removed the undocumented `glob.glob0()` and `glob.glob1()` functions, which have been deprecated since Python 3.13. Use [`glob.glob()`](https://docs.python.org/3/library/glob.html#glob.glob "glob.glob")\
     and pass a directory to its _root\_dir_ argument instead. (Contributed by Barney Gale in [gh-137466](https://github.com/python/cpython/issues/137466)\
    .)\
    \
\
### http.server[¶](https://docs.python.org/3/whatsnew/3.15.html#id3 "Link to this heading")\
\
*   Removed the `CGIHTTPRequestHandler` class and the `--cgi` flag from the **python -m http.server** command-line interface. They were deprecated in Python 3.13. (Contributed by Bénédikt Tran in [gh-133810](https://github.com/python/cpython/issues/133810)\
    .)\
    \
\
### importlib[¶](https://docs.python.org/3/whatsnew/3.15.html#importlib "Link to this heading")\
\
*   The `load_module()` methods of [`Loader`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader "importlib.abc.Loader")\
     and its subclasses is removed. The import system will no longer call it when defined on custom subclasses. The method has been deprecated in favor of [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module")\
     since Python 3.4. (Contributed by Brett Cannon in [gh-97850](https://github.com/python/cpython/issues/97850)\
    .)\
    \
\
### importlib.resources[¶](https://docs.python.org/3/whatsnew/3.15.html#importlib-resources "Link to this heading")\
\
*   Removed deprecated `package` parameter from [`importlib.resources.files()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files "importlib.resources.files")\
     function. (Contributed by Semyon Moroz in [gh-138044](https://github.com/python/cpython/issues/138044)\
    .)\
    \
\
### pathlib[¶](https://docs.python.org/3/whatsnew/3.15.html#id4 "Link to this heading")\
\
*   Removed deprecated `pathlib.PurePath.is_reserved()`. Use [`os.path.isreserved()`](https://docs.python.org/3/library/os.path.html#os.path.isreserved "os.path.isreserved")\
     to detect reserved paths on Windows. (Contributed by Nikita Sobolev in [gh-133875](https://github.com/python/cpython/issues/133875)\
    .)\
    \
\
### platform[¶](https://docs.python.org/3/whatsnew/3.15.html#platform "Link to this heading")\
\
*   Removed the `platform.java_ver()` function, which was deprecated since Python 3.13. (Contributed by Alexey Makridenko in [gh-133604](https://github.com/python/cpython/issues/133604)\
    .)\
    \
\
### sre\_\*[¶](https://docs.python.org/3/whatsnew/3.15.html#sre "Link to this heading")\
\
*   Removed `sre_compile`, `sre_constants` and `sre_parse` modules. (Contributed by Stan Ulbrych in [gh-135994](https://github.com/python/cpython/issues/135994)\
    .)\
    \
\
### sysconfig[¶](https://docs.python.org/3/whatsnew/3.15.html#sysconfig "Link to this heading")\
\
*   Removed the _check\_home_ parameter of [`sysconfig.is_python_build()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.is_python_build "sysconfig.is_python_build")\
    . (Contributed by Filipe Laíns in [gh-92897](https://github.com/python/cpython/issues/92897)\
    .)\
    \
\
### threading[¶](https://docs.python.org/3/whatsnew/3.15.html#id5 "Link to this heading")\
\
*   Remove support for arbitrary positional or keyword arguments in the C implementation of [`RLock`](https://docs.python.org/3/library/threading.html#threading.RLock "threading.RLock")\
     objects. This was deprecated in Python 3.14. (Contributed by Bénédikt Tran in [gh-134087](https://github.com/python/cpython/issues/134087)\
    .)\
    \
\
### types[¶](https://docs.python.org/3/whatsnew/3.15.html#id6 "Link to this heading")\
\
*   Removed `codeobject.co_lnotab` from [`types.CodeType`](https://docs.python.org/3/library/types.html#types.CodeType "types.CodeType")\
    , deprecated since Python 3.12 by [**PEP 626**](https://peps.python.org/pep-0626/)\
    . (Contributed by Nikita Sobolev in [gh-134690](https://github.com/python/cpython/issues/134690)\
    .)\
    \
\
### typing[¶](https://docs.python.org/3/whatsnew/3.15.html#id7 "Link to this heading")\
\
*   [`typing.ByteString`](https://docs.python.org/3/library/typing.html#typing.ByteString "typing.ByteString")\
     has been removed from `typing.__all__`. `typing.ByteString` has been deprecated since Python 3.9, and is scheduled for removal in Python 3.17. (Contributed by Alex Waygood in [gh-118803](https://github.com/python/cpython/issues/118803)\
    .)\
    \
*   The undocumented keyword argument syntax for creating [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple")\
     classes (for example, `Point = NamedTuple("Point", x=int, y=int)`) is no longer supported. Use the class-based syntax or the functional syntax instead. (Contributed by Bénédikt Tran in [gh-133817](https://github.com/python/cpython/issues/133817)\
    .)\
    \
*   Using `TD = TypedDict("TD")` or `TD = TypedDict("TD", None)` to construct a [`TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict")\
     type with zero fields is no longer supported. Use `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})` instead. (Contributed by Bénédikt Tran in [gh-133823](https://github.com/python/cpython/issues/133823)\
    .)\
    \
*   Deprecated `typing.no_type_check_decorator` has been removed. (Contributed by Nikita Sobolev in [gh-133601](https://github.com/python/cpython/issues/133601)\
    .)\
    \
\
### wave[¶](https://docs.python.org/3/whatsnew/3.15.html#id8 "Link to this heading")\
\
*   Removed the `getmark()`, `setmark()` and `getmarkers()` methods of the [`Wave_read`](https://docs.python.org/3/library/wave.html#wave.Wave_read "wave.Wave_read")\
     and [`Wave_write`](https://docs.python.org/3/library/wave.html#wave.Wave_write "wave.Wave_write")\
     classes, which were deprecated since Python 3.13. (Contributed by Bénédikt Tran in [gh-133873](https://github.com/python/cpython/issues/133873)\
    .)\
    \
\
### zipimport[¶](https://docs.python.org/3/whatsnew/3.15.html#zipimport "Link to this heading")\
\
*   Remove deprecated `zipimport.zipimporter.load_module()`. Use [`zipimport.zipimporter.exec_module()`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.exec_module "zipimport.zipimporter.exec_module")\
     instead. (Contributed by Jiahao Li in [gh-133656](https://github.com/python/cpython/issues/133656)\
    .)\
    \
\
Deprecated[¶](https://docs.python.org/3/whatsnew/3.15.html#deprecated "Link to this heading")\
\
----------------------------------------------------------------------------------------------\
\
### New deprecations[¶](https://docs.python.org/3/whatsnew/3.15.html#new-deprecations "Link to this heading")\
\
*   [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.")\
    :\
    \
    *   Creating instances of abstract AST nodes (such as [`ast.AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST")\
         or `ast.expr`) is deprecated and will raise an error in Python 3.20.\
        \
        (Contributed by Brian Schubert in [gh-116021](https://github.com/python/cpython/issues/116021)\
        .)\
        \
*   [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")\
    :\
    \
    *   Accepting the `+` and `/` characters with an alternative alphabet in [`b64decode()`](https://docs.python.org/3/library/base64.html#base64.b64decode "base64.b64decode")\
         and [`urlsafe_b64decode()`](https://docs.python.org/3/library/base64.html#base64.urlsafe_b64decode "base64.urlsafe_b64decode")\
         is now deprecated. In future Python versions they will be errors in the strict mode and discarded in the non-strict mode. (Contributed by Serhiy Storchaka in [gh-125346](https://github.com/python/cpython/issues/125346)\
        .)\
        \
*   CLI:\
    \
    *   Deprecate [`-b`](https://docs.python.org/3/using/cmdline.html#cmdoption-b)\
         and `-bb` command-line options and schedule them to become no-ops in Python 3.17. These were primarily helpers for the Python 2 -> 3 transition. Starting with Python 3.17, no [`BytesWarning`](https://docs.python.org/3/builtins/exceptions.html#BytesWarning "BytesWarning")\
         will be raised for these cases; use a type checker instead.\
        \
        (Contributed by Nikita Sobolev in [gh-136355](https://github.com/python/cpython/issues/136355)\
        .)\
        \
*   [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")\
    :\
    \
    *   The following statements now cause `DeprecationWarning`s to be emitted at runtime:\
        \
        *   `from collections.abc import ByteString`\
            \
        *   `import collections.abc; collections.abc.ByteString`.\
            \
        \
        `DeprecationWarning`s were already emitted if [`collections.abc.ByteString`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ByteString "collections.abc.ByteString")\
         was subclassed or used as the second argument to [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")\
         or [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")\
        , but warnings were not previously emitted if it was merely imported or accessed from the `collections.abc` module. (Contributed by Alex Waygood in [gh-118803](https://github.com/python/cpython/issues/118803)\
        .)\
        \
*   [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")\
    :\
    \
    *   In hash function constructors such as [`new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new")\
         or the direct hash-named constructors such as [`md5()`](https://docs.python.org/3/library/hashlib.html#hashlib.md5 "hashlib.md5")\
         and [`sha256()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha256 "hashlib.sha256")\
        , the optional initial data parameter could also be passed as a keyword argument named `data=` or `string=` in various [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")\
         implementations.\
        \
        Support for the `string` keyword argument name is now deprecated and is slated for removal in Python 3.19. Prefer passing the initial data as a positional argument for maximum backwards compatibility.\
        \
        (Contributed by Bénédikt Tran in [gh-134978](https://github.com/python/cpython/issues/134978)\
        .)\
        \
*   [`http.cookies`](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "http.cookies: Support for HTTP state management (cookies).")\
    :\
    \
    *   [`Morsel.js_output`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.js_output "http.cookies.Morsel.js_output")\
         and [`BaseCookie.js_output`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.js_output "http.cookies.BaseCookie.js_output")\
         are deprecated and will be removed in Python 3.19. Use [`Morsel.output`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.output "http.cookies.Morsel.output")\
         or [`BaseCookie.output`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.output "http.cookies.BaseCookie.output")\
         instead. (Contributed by kishorhange111 in [gh-148849](https://github.com/python/cpython/issues/148849)\
        .)\
        \
*   [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).")\
    :\
    \
    *   Altering [`IMAP4.file`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.file "imaplib.IMAP4.file")\
         is now deprecated and slated for removal in Python 3.19. This property is now unused and changing its value does _not_ explicitly close the current file. (Contributed by Bénédikt Tran in [gh-142307](https://github.com/python/cpython/issues/142307)\
        .)\
        \
*   [`profile`](https://docs.python.org/3/library/profile.html#module-profile "profile: Pure Python profiler (deprecated). (deprecated)")\
    :\
    \
    *   The `profile` module is deprecated and will be removed in Python 3.17. Use [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")\
         instead, which provides a compatible API. See [**PEP 799**](https://peps.python.org/pep-0799/)\
         for details. (Contributed by Pablo Galindo and László Kiss Kollár in [gh-138122](https://github.com/python/cpython/issues/138122)\
        .)\
        \
*   [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")\
    :\
    \
    *   [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match")\
         and [`re.Pattern.match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match")\
         are now [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
         in favor of the new [`re.prefixmatch()`](https://docs.python.org/3/library/re.html#re.prefixmatch "re.prefixmatch")\
         and [`re.Pattern.prefixmatch()`](https://docs.python.org/3/library/re.html#re.Pattern.prefixmatch "re.Pattern.prefixmatch")\
         APIs, which have been added as alternate, more explicit names. These are intended to be used to alleviate confusion around what _match_ means by following the Zen of Python’s _“Explicit is better than implicit”_ mantra. Most other language regular expression libraries use an API named _match_ to mean what Python has always called _search_.\
        \
        We **do not** plan to remove the older `match()` name, as it has been used in code for over 30 years. Code supporting older versions of Python should continue to use `match()`, while new code should prefer `prefixmatch()`. See [prefixmatch() vs. match()](https://docs.python.org/3/library/re.html#prefixmatch-vs-match)\
        .\
        \
        (Contributed by Gregory P. Smith in [gh-86519](https://github.com/python/cpython/issues/86519)\
         and Hugo van Kemenade in [gh-148100](https://github.com/python/cpython/issues/148100)\
        .)\
        \
*   [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")\
    :\
    \
    *   Calling `Struct.__new__()` without a required argument is now deprecated and will be removed in Python 3.20. Calling the [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")\
         method on an initialized [`Struct`](https://docs.python.org/3/library/struct.html#struct.Struct "struct.Struct")\
         object is deprecated and will be removed in Python 3.20.\
        \
        (Contributed by Sergey B Kirpichev and Serhiy Storchaka in [gh-143715](https://github.com/python/cpython/issues/143715)\
        .)\
        \
    *   The `'F'` and `'D'` type codes are now [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
         in favor of the two-letter forms `'Zf'` and `'Zd'`. (Contributed by Sergey B Kirpichev in [gh-121249](https://github.com/python/cpython/issues/121249)\
        .)\
        \
*   [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")\
    :\
    \
    *   The following statements now cause `DeprecationWarning`s to be emitted at runtime:\
        \
        *   `from typing import ByteString`\
            \
        *   `import typing; typing.ByteString`.\
            \
        \
        `DeprecationWarning`s were already emitted if [`typing.ByteString`](https://docs.python.org/3/library/typing.html#typing.ByteString "typing.ByteString")\
         was subclassed or used as the second argument to [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")\
         or [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")\
        , but warnings were not previously emitted if it was merely imported or accessed from the `typing` module. (Contributed by Alex Waygood in [gh-118803](https://github.com/python/cpython/issues/118803)\
        .)\
        \
    *   It is deprecated to call [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")\
         and [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")\
         checks on protocol classes that were not explicitly decorated with `runtime_checkable()` but that inherit from a runtime-checkable protocol class. This will raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")\
         in Python 3.20.\
        \
        (Contributed by Bartosz Sławecki in [gh-132604](https://github.com/python/cpython/issues/132604)\
        .)\
        \
*   [`webbrowser`](https://docs.python.org/3/library/webbrowser.html#module-webbrowser "webbrowser: Easy-to-use controller for web browsers.")\
    :\
    \
    *   `webbrowser.MacOSXOSAScript` is deprecated in favour of `webbrowser.MacOS` and scheduled for removal in Python 3.17. (Contributed by Jeff Lyon in [gh-137586](https://github.com/python/cpython/issues/137586)\
        .)\
        \
*   `__version__`:\
    \
    *   The `__version__`, `version` and `VERSION` attributes have been deprecated in these standard library modules and will be removed in Python 3.20. Use [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")\
         instead.\
        \
        *   [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")\
            \
        *   [`csv`](https://docs.python.org/3/library/csv.html#module-csv "csv: Write and read tabular data to and from delimited files.")\
            \
        *   [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")\
            \
        *   `ctypes.macholib`\
            \
        *   [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")\
             (use [`decimal.SPEC_VERSION`](https://docs.python.org/3/library/decimal.html#decimal.SPEC_VERSION "decimal.SPEC_VERSION")\
             instead)\
            \
        *   [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")\
            \
        *   [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).")\
            \
        *   [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.")\
            \
        *   [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")\
            \
        *   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")\
             (`__date__` also deprecated)\
            \
        *   [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")\
            \
        *   [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")\
            \
        *   [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")\
            \
        *   [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")\
            \
        *   [`socketserver`](https://docs.python.org/3/library/socketserver.html#module-socketserver "socketserver: A framework for network servers.")\
            \
        *   [`tabnanny`](https://docs.python.org/3/library/tabnanny.html#module-tabnanny "tabnanny: Tool for detecting white space related problems in Python source files in a directory tree.")\
            \
        *   [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")\
            \
        *   [`tkinter.font`](https://docs.python.org/3/library/tkinter.font.html#module-tkinter.font "tkinter.font: Tkinter font-wrapping class")\
            \
        *   [`tkinter.ttk`](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk "tkinter.ttk: Tk themed widget set")\
            \
        *   [`wsgiref.simple_server`](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.simple_server "wsgiref.simple_server: A simple WSGI HTTP server.")\
            \
        *   [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")\
            \
        *   `xml.sax.expatreader`\
            \
        *   [`xml.sax.handler`](https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.")\
            \
        *   [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")\
            \
        \
        (Contributed by Hugo van Kemenade and Stan Ulbrych in [gh-76007](https://github.com/python/cpython/issues/76007)\
        .)\
        \
\
### Pending removal in Python 3.16[¶](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-python-3-16 "Link to this heading")\
\
*   The import system:\
    \
    *   Setting [`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")\
         on a module while failing to set [`__spec__.loader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.loader "importlib.machinery.ModuleSpec.loader")\
         is deprecated. In Python 3.16, `__loader__` will cease to be set or taken into consideration by the import system or the standard library.\
        \
*   [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.")\
    :\
    \
    *   The `'u'` format code (`wchar_t`) has been deprecated in documentation since Python 3.3 and at runtime since Python 3.13. Use the `'w'` format code ([`Py_UCS4`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")\
        ) for Unicode characters instead.\
        \
*   [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")\
    :\
    \
    *   `asyncio.iscoroutinefunction()` is deprecated and will be removed in Python 3.16; use [`inspect.iscoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction "inspect.iscoroutinefunction")\
         instead. (Contributed by Jiahao Li and Kumar Aditya in [gh-122875](https://github.com/python/cpython/issues/122875)\
        .)\
        \
    *   [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")\
         policy system is deprecated and will be removed in Python 3.16. In particular, the following classes and functions are deprecated:\
        \
        *   [`asyncio.AbstractEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.AbstractEventLoopPolicy "asyncio.AbstractEventLoopPolicy")\
            \
        *   [`asyncio.DefaultEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.DefaultEventLoopPolicy "asyncio.DefaultEventLoopPolicy")\
            \
        *   [`asyncio.WindowsSelectorEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.WindowsSelectorEventLoopPolicy "asyncio.WindowsSelectorEventLoopPolicy")\
            \
        *   [`asyncio.WindowsProactorEventLoopPolicy`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.WindowsProactorEventLoopPolicy "asyncio.WindowsProactorEventLoopPolicy")\
            \
        *   [`asyncio.get_event_loop_policy()`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.get_event_loop_policy "asyncio.get_event_loop_policy")\
            \
        *   [`asyncio.set_event_loop_policy()`](https://docs.python.org/3/library/asyncio-policy.html#asyncio.set_event_loop_policy "asyncio.set_event_loop_policy")\
            \
        \
        Users should use [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run")\
         or [`asyncio.Runner`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.Runner "asyncio.Runner")\
         with _loop\_factory_ to use the desired event loop implementation.\
        \
        For example, to use [`asyncio.SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")\
         on Windows:\
        \
        Copy\
        \
        import asyncio\
        \
        async def main():\
            ...\
        \
        asyncio.run(main(), loop\_factory\=asyncio.SelectorEventLoop)\
        \
        (Contributed by Kumar Aditya in [gh-127949](https://github.com/python/cpython/issues/127949)\
        .)\
        \
*   [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")\
    :\
    \
    *   Bitwise inversion on boolean types, `~True` or `~False` has been deprecated since Python 3.12, as it produces surprising and unintuitive results (`-2` and `-1`). Use `not x` instead for the logical negation of a Boolean. In the rare case that you need the bitwise inversion of the underlying integer, convert to `int` explicitly (`~int(x)`).\
        \
*   [`functools`](https://docs.python.org/3/library/functools.html#module-functools "functools: Higher-order functions and operations on callable objects.")\
    :\
    \
    *   Calling the Python implementation of [`functools.reduce()`](https://docs.python.org/3/library/functools.html#functools.reduce "functools.reduce")\
         with _function_ or _sequence_ as keyword arguments has been deprecated since Python 3.14.\
        \
*   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")\
    :\
    \
    *   Support for custom logging handlers with the _strm_ argument is deprecated and scheduled for removal in Python 3.16. Define handlers with the _stream_ argument instead. (Contributed by Mariusz Felisiak in [gh-115032](https://github.com/python/cpython/issues/115032)\
        .)\
        \
*   [`mimetypes`](https://docs.python.org/3/library/mimetypes.html#module-mimetypes "mimetypes: Mapping of filename extensions to MIME types.")\
    :\
    \
    *   Valid extensions start with a ‘.’ or are empty for [`mimetypes.MimeTypes.add_type()`](https://docs.python.org/3/library/mimetypes.html#mimetypes.MimeTypes.add_type "mimetypes.MimeTypes.add_type")\
        . Undotted extensions are deprecated and will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")\
         in Python 3.16. (Contributed by Hugo van Kemenade in [gh-75223](https://github.com/python/cpython/issues/75223)\
        .)\
        \
*   [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")\
    :\
    \
    *   The `ExecError` exception has been deprecated since Python 3.14. It has not been used by any function in `shutil` since Python 3.4, and is now an alias of [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")\
        .\
        \
*   [`symtable`](https://docs.python.org/3/library/symtable.html#module-symtable "symtable: Interface to the compiler's internal symbol tables.")\
    :\
    \
    *   The [`Class.get_methods`](https://docs.python.org/3/library/symtable.html#symtable.Class.get_methods "symtable.Class.get_methods")\
         method has been deprecated since Python 3.14.\
        \
*   [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")\
    :\
    \
    *   The [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3/library/sys.html#sys._enablelegacywindowsfsencoding "sys._enablelegacywindowsfsencoding")\
         function has been deprecated since Python 3.13. Use the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING)\
         environment variable instead.\
        \
*   [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")\
    :\
    \
    *   The `sysconfig.expand_makefile_vars()` function has been deprecated since Python 3.14. Use the `vars` argument of [`sysconfig.get_paths()`](https://docs.python.org/3/library/sysconfig.html#sysconfig.get_paths "sysconfig.get_paths")\
         instead.\
        \
*   [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")\
    :\
    \
    *   The undocumented and unused `TarFile.tarfile` attribute has been deprecated since Python 3.13.\
        \
\
### Pending removal in Python 3.17[¶](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-python-3-17 "Link to this heading")\
\
*   [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")\
    :\
    \
    *   [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime")\
         calls using a format string containing `%e` (day of month) without a year. This has been deprecated since Python 3.15. (Contributed by Stan Ulbrych in [gh-70647](https://github.com/python/cpython/issues/70647)\
        .)\
        \
*   [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")\
    :\
    \
    *   [`collections.abc.ByteString`](https://docs.python.org/3/library/collections.abc.html#collections.abc.ByteString "collections.abc.ByteString")\
         is scheduled for removal in Python 3.17.\
        \
        Use `isinstance(obj, collections.abc.Buffer)` to test if `obj` implements the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)\
         at runtime. For use in type annotations, either use [`Buffer`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")\
         or a union that explicitly specifies the types your code supports (e.g., `bytes | bytearray | memoryview`).\
        \
        `ByteString` was originally intended to be an abstract class that would serve as a supertype of both [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")\
         and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")\
        . However, since the ABC never had any methods, knowing that an object was an instance of `ByteString` never actually told you anything useful about the object. Other common buffer types such as [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")\
         were also never understood as subtypes of `ByteString` (either at runtime or by static type checkers).\
        \
        See [**PEP 688**](https://peps.python.org/pep-0688/#current-options)\
         for more details. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896)\
        .)\
        \
*   [`encodings`](https://docs.python.org/3/library/codecs.html#module-encodings "encodings: Encodings package")\
    :\
    \
    *   Passing non-ascii _encoding_ names to [`encodings.normalize_encoding()`](https://docs.python.org/3/library/codecs.html#encodings.normalize_encoding "encodings.normalize_encoding")\
         is deprecated and scheduled for removal in Python 3.17. (Contributed by Stan Ulbrych in [gh-136702](https://github.com/python/cpython/issues/136702)\
        .)\
        \
*   [`profile`](https://docs.python.org/3/library/profile.html#module-profile "profile: Pure Python profiler (deprecated). (deprecated)")\
    :\
    \
    *   The `profile` module is deprecated and will be removed in Python 3.17. Use [`profiling.tracing`](https://docs.python.org/3/library/profiling.tracing.html#module-profiling.tracing "profiling.tracing: Deterministic tracing profiler for Python programs.")\
         instead, which provides a compatible API. See [**PEP 799**](https://peps.python.org/pep-0799/)\
         for details. (Contributed by Pablo Galindo and László Kiss Kollár in [gh-138122](https://github.com/python/cpython/issues/138122)\
        .)\
        \
*   [`webbrowser`](https://docs.python.org/3/library/webbrowser.html#module-webbrowser "webbrowser: Easy-to-use controller for web browsers.")\
    :\
    \
    *   `webbrowser.MacOSXOSAScript` is deprecated in favour of `webbrowser.MacOS`. ([gh-137586](https://github.com/python/cpython/issues/137586)\
        )\
        \
*   [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")\
    :\
    \
    *   Before Python 3.14, old-style unions were implemented using the private class `typing._UnionGenericAlias`. This class is no longer needed for the implementation, but it has been retained for backward compatibility, with removal scheduled for Python 3.17. Users should use documented introspection helpers like [`typing.get_origin()`](https://docs.python.org/3/library/typing.html#typing.get_origin "typing.get_origin")\
         and [`typing.get_args()`](https://docs.python.org/3/library/typing.html#typing.get_args "typing.get_args")\
         instead of relying on private implementation details.\
        \
    *   [`typing.ByteString`](https://docs.python.org/3/library/typing.html#typing.ByteString "typing.ByteString")\
        , deprecated since Python 3.9, is scheduled for removal in Python 3.17.\
        \
        Use `isinstance(obj, collections.abc.Buffer)` to test if `obj` implements the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)\
         at runtime. For use in type annotations, either use [`Buffer`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Buffer "collections.abc.Buffer")\
         or a union that explicitly specifies the types your code supports (e.g., `bytes | bytearray | memoryview`).\
        \
        `ByteString` was originally intended to be an abstract class that would serve as a supertype of both [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")\
         and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")\
        . However, since the ABC never had any methods, knowing that an object was an instance of `ByteString` never actually told you anything useful about the object. Other common buffer types such as [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")\
         were also never understood as subtypes of `ByteString` (either at runtime or by static type checkers).\
        \
        See [**PEP 688**](https://peps.python.org/pep-0688/#current-options)\
         for more details. (Contributed by Shantanu Jain in [gh-91896](https://github.com/python/cpython/issues/91896)\
        .)\
        \
*   [`tkinter`](https://docs.python.org/3/library/tkinter.html#module-tkinter "tkinter: Interface to Tcl/Tk for graphical user interfaces")\
    :\
    \
    *   The `tkinter.Variable` methods `trace_variable()`, `trace()` (an alias of `trace_variable()`), `trace_vdelete()` and `trace_vinfo()`, deprecated since Python 3.14, are scheduled for removal in Python 3.17. Use `trace_add()`, `trace_remove()` and `trace_info()` instead. (Contributed by Serhiy Storchaka in [gh-120220](https://github.com/python/cpython/issues/120220)\
        .)\
        \
\
### Pending removal in Python 3.18[¶](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-python-3-18 "Link to this heading")\
\
*   No longer accept a boolean value when a file descriptor is expected. (Contributed by Serhiy Storchaka in [gh-82626](https://github.com/python/cpython/issues/82626)\
    .)\
    \
*   [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")\
    :\
    \
    *   The non-standard and undocumented [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")\
         format specifier `'N'`, which is only supported in the `decimal` module’s C implementation, has been deprecated since Python 3.13. (Contributed by Serhiy Storchaka in [gh-89902](https://github.com/python/cpython/issues/89902)\
        .)\
        \
*   Deprecations defined by [**PEP 829**](https://peps.python.org/pep-0829/)\
    :\
    \
    *   `import` lines in `_name_.pth` files are silently ignored.\
        \
    \
    (Contributed by Barry Warsaw in [gh-148641](https://github.com/python/cpython/issues/148641)\
    .)\
    \
\
### Pending removal in Python 3.19[¶](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-python-3-19 "Link to this heading")\
\
*   [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")\
    :\
    \
    *   Implicitly switching to the MSVC-compatible struct layout by setting [`_pack_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._pack_ "ctypes.Structure._pack_")\
         but not [`_layout_`](https://docs.python.org/3/library/ctypes.html#ctypes.Structure._layout_ "ctypes.Structure._layout_")\
         on non-Windows platforms.\
        \
*   [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")\
    :\
    \
    *   In hash function constructors such as [`new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new")\
         or the direct hash-named constructors such as [`md5()`](https://docs.python.org/3/library/hashlib.html#hashlib.md5 "hashlib.md5")\
         and [`sha256()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha256 "hashlib.sha256")\
        , their optional initial data parameter could also be passed a keyword argument named `data=` or `string=` in various `hashlib` implementations.\
        \
        Support for the `string` keyword argument name is now deprecated and slated for removal in Python 3.19.\
        \
        Before Python 3.13, the `string` keyword parameter was not correctly supported depending on the backend implementation of hash functions. Prefer passing the initial data as a positional argument for maximum backwards compatibility.\
        \
*   [`http.cookies`](https://docs.python.org/3/library/http.cookies.html#module-http.cookies "http.cookies: Support for HTTP state management (cookies).")\
    :\
    \
    *   [`http.cookies.Morsel.js_output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.js_output "http.cookies.Morsel.js_output")\
         is deprecated and will be removed in Python 3.19.\
        \
    *   [`http.cookies.BaseCookie.js_output()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.BaseCookie.js_output "http.cookies.BaseCookie.js_output")\
         is deprecated and will be removed in Python 3.19.\
        \
*   [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).")\
    :\
    \
    *   Altering [`IMAP4.file`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.file "imaplib.IMAP4.file")\
         is now deprecated and slated for removal in Python 3.19. This property is now unused and changing its value does not automatically close the current file.\
        \
        Before Python 3.14, this property was used to implement the corresponding `read()` and `readline()` methods for [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4")\
         but this is no longer the case since then.\
        \
\
### Pending removal in Python 3.20[¶](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-python-3-20 "Link to this heading")\
\
*   Calling the `__new__()` method of [`struct.Struct`](https://docs.python.org/3/library/struct.html#struct.Struct "struct.Struct")\
     without the _format_ argument is deprecated and will be removed in Python 3.20. Calling [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__")\
     method on initialized `Struct` objects is deprecated and will be removed in Python 3.20.\
    \
    (Contributed by Sergey B Kirpichev and Serhiy Storchaka in [gh-143715](https://github.com/python/cpython/issues/143715)\
    .)\
    \
*   The `__version__`, `version` and `VERSION` attributes have been deprecated in these standard library modules and will be removed in Python 3.20. Use [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")\
     instead.\
    \
    *   [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")\
        \
    *   [`csv`](https://docs.python.org/3/library/csv.html#module-csv "csv: Write and read tabular data to and from delimited files.")\
        \
    *   [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")\
        \
    *   `ctypes.macholib`\
        \
    *   [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")\
         (use [`decimal.SPEC_VERSION`](https://docs.python.org/3/library/decimal.html#decimal.SPEC_VERSION "decimal.SPEC_VERSION")\
         instead)\
        \
    *   [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")\
        \
    *   [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).")\
        \
    *   [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.")\
        \
    *   [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")\
        \
    *   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")\
         (`__date__` also deprecated)\
        \
    *   [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.")\
        \
    *   [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")\
        \
    *   [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")\
        \
    *   [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")\
        \
    *   [`socketserver`](https://docs.python.org/3/library/socketserver.html#module-socketserver "socketserver: A framework for network servers.")\
        \
    *   [`tabnanny`](https://docs.python.org/3/library/tabnanny.html#module-tabnanny "tabnanny: Tool for detecting white space related problems in Python source files in a directory tree.")\
        \
    *   [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")\
        \
    *   [`tkinter.font`](https://docs.python.org/3/library/tkinter.font.html#module-tkinter.font "tkinter.font: Tkinter font-wrapping class")\
        \
    *   [`tkinter.ttk`](https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk "tkinter.ttk: Tk themed widget set")\
        \
    *   [`wsgiref.simple_server`](https://docs.python.org/3/library/wsgiref.html#module-wsgiref.simple_server "wsgiref.simple_server: A simple WSGI HTTP server.")\
        \
    *   [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")\
        \
    *   `xml.sax.expatreader`\
        \
    *   [`xml.sax.handler`](https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.")\
        \
    *   [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")\
        \
    \
    (Contributed by Hugo van Kemenade and Stan Ulbrych in [gh-76007](https://github.com/python/cpython/issues/76007)\
    .)\
    \
*   Deprecations defined by [**PEP 829**](https://peps.python.org/pep-0829/)\
    :\
    \
    *   Warnings are produced for `import` lines found in `_name_.pth` files.\
        \
    *   `_name_.pth` files are no longer decoded in the locale encoding by default. They **MUST** be encoded in `utf-8-sig`.\
        \
    \
    (Contributed by Barry Warsaw in [gh-148641](https://github.com/python/cpython/issues/148641)\
    .)\
    \
*   [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.")\
    :\
    \
    *   Creating instances of abstract AST nodes (such as [`ast.AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST")\
         or `ast.expr`) is deprecated and will raise an error in Python 3.20.\
        \
*   [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).")\
    :\
    \
    *   It is deprecated to call [`isinstance()`](https://docs.python.org/3/builtins/functions.html#isinstance "isinstance")\
         and [`issubclass()`](https://docs.python.org/3/builtins/functions.html#issubclass "issubclass")\
         checks on protocol classes that were not explicitly decorated with `runtime_checkable()` but that inherit from a runtime-checkable protocol class. This will raise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")\
         in Python 3.20.\
        \
        (Contributed by Bartosz Sławecki in [gh-132604](https://github.com/python/cpython/issues/132604)\
        .)\
        \
\
### Pending removal in future versions[¶](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-future-versions "Link to this heading")\
\
The following APIs will be removed in the future, although there is currently no date scheduled for their removal.\
\
*   [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")\
    :\
    \
    *   Nesting argument groups and nesting mutually exclusive groups are deprecated.\
        \
    *   Passing the undocumented keyword argument _prefix\_chars_ to [`add_argument_group()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "argparse.ArgumentParser.add_argument_group")\
         is now deprecated.\
        \
    *   The [`argparse.FileType`](https://docs.python.org/3/library/argparse.html#argparse.FileType "argparse.FileType")\
         type converter is deprecated.\
        \
*   [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.")\
    :\
    \
    *   Generators: `throw(type, exc, tb)` and `athrow(type, exc, tb)` signature is deprecated: use `throw(exc)` and `athrow(exc)` instead, the single argument signature.\
        \
    *   Currently Python accepts numeric literals immediately followed by keywords, for example `0in x`, `1or x`, `0if 1else 2`. It allows confusing and ambiguous expressions like `[0x1for x in y]` (which can be interpreted as `[0x1 for x in y]` or `[0x1f or x in y]`). A syntax warning is raised if the numeric literal is immediately followed by one of keywords [`and`](https://docs.python.org/3/reference/expressions.html#and)\
        , [`else`](https://docs.python.org/3/reference/compound_stmts.html#else)\
        , [`for`](https://docs.python.org/3/reference/compound_stmts.html#for)\
        , [`if`](https://docs.python.org/3/reference/compound_stmts.html#if)\
        , [`in`](https://docs.python.org/3/reference/expressions.html#in)\
        , [`is`](https://docs.python.org/3/reference/expressions.html#is)\
         and [`or`](https://docs.python.org/3/reference/expressions.html#or)\
        . In a future release it will be changed to a syntax error. ([gh-87999](https://github.com/python/cpython/issues/87999)\
        )\
        \
    *   Support for `__index__()` and `__int__()` method returning non-int type: these methods will be required to return an instance of a strict subclass of [`int`](https://docs.python.org/3/builtins/functions.html#int "int")\
        .\
        \
    *   Support for `__float__()` method returning a strict subclass of [`float`](https://docs.python.org/3/builtins/functions.html#float "float")\
        : these methods will be required to return an instance of `float`.\
        \
    *   Support for `__complex__()` method returning a strict subclass of [`complex`](https://docs.python.org/3/builtins/functions.html#complex "complex")\
        : these methods will be required to return an instance of `complex`.\
        \
    *   Passing a complex number as the _real_ or _imag_ argument in the [`complex()`](https://docs.python.org/3/builtins/functions.html#complex "complex")\
         constructor is now deprecated; it should only be passed as a single positional argument. (Contributed by Serhiy Storchaka in [gh-109218](https://github.com/python/cpython/issues/109218)\
        .)\
        \
*   [`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.")\
    : `calendar.January` and `calendar.February` constants are deprecated and replaced by [`calendar.JANUARY`](https://docs.python.org/3/library/calendar.html#calendar.JANUARY "calendar.JANUARY")\
     and [`calendar.FEBRUARY`](https://docs.python.org/3/library/calendar.html#calendar.FEBRUARY "calendar.FEBRUARY")\
    . (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636)\
    .)\
    \
*   [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")\
    : use [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")\
     instead of [`codecs.open()`](https://docs.python.org/3/library/codecs.html#codecs.open "codecs.open")\
    . ([gh-133038](https://github.com/python/cpython/issues/133038)\
    )\
    \
*   `codeobject.co_lnotab`: use the [`codeobject.co_lines()`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lines "codeobject.co_lines")\
     method instead.\
    \
*   [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")\
    :\
    \
    *   [`utcnow()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow "datetime.datetime.utcnow")\
        : use `datetime.datetime.now(tz=datetime.UTC)`.\
        \
    *   [`utcfromtimestamp()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcfromtimestamp "datetime.datetime.utcfromtimestamp")\
        : use `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`.\
        \
*   [`gettext`](https://docs.python.org/3/library/gettext.html#module-gettext "gettext: Multilingual internationalization services.")\
    : Plural value must be an integer.\
    \
*   [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")\
    :\
    \
    *   [`cache_from_source()`](https://docs.python.org/3/library/importlib.html#importlib.util.cache_from_source "importlib.util.cache_from_source")\
         _debug\_override_ parameter is deprecated: use the _optimization_ parameter instead.\
        \
*   [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html#module-importlib.metadata "importlib.metadata: Accessing package metadata")\
    :\
    \
    *   `EntryPoints` tuple interface.\
        \
    *   Implicit `None` on return values.\
        \
*   [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")\
    : the `warn()` method has been deprecated since Python 3.3, use [`warning()`](https://docs.python.org/3/library/logging.html#logging.warning "logging.warning")\
     instead.\
    \
*   [`mailbox`](https://docs.python.org/3/library/mailbox.html#module-mailbox "mailbox: Manipulate mailboxes in various formats")\
    : Use of StringIO input and text mode is deprecated, use BytesIO and binary mode instead.\
    \
*   [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")\
    : Calling [`os.register_at_fork()`](https://docs.python.org/3/library/os.html#os.register_at_fork "os.register_at_fork")\
     in a multi-threaded process.\
    \
*   [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path "os.path: Operations on pathnames.")\
    : [`os.path.commonprefix()`](https://docs.python.org/3/library/os.path.html#os.path.commonprefix "os.path.commonprefix")\
     is deprecated, use [`os.path.commonpath()`](https://docs.python.org/3/library/os.path.html#os.path.commonpath "os.path.commonpath")\
     for path prefixes. The `os.path.commonprefix()` function is being deprecated due to having a misleading name and module. The function is not safe to use for path prefixes despite being included in a module about path manipulation, meaning it is easy to accidentally introduce path traversal vulnerabilities into Python programs by using this function.\
    \
*   `pydoc.ErrorDuringImport`: A tuple value for _exc\_info_ parameter is deprecated, use an exception instance.\
    \
*   [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.")\
    : More strict rules are now applied for numerical group references and group names in regular expressions. Only sequence of ASCII digits is now accepted as a numerical reference. The group name in bytes patterns and replacement strings can now only contain ASCII letters and digits and underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760)\
    .)\
    \
*   [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")\
    : [`rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree")\
    ’s _onerror_ parameter is deprecated in Python 3.12; use the _onexc_ parameter instead.\
    \
*   [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")\
     options and protocols:\
    \
    *   [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")\
         without protocol argument is deprecated.\
        \
    *   [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")\
        : [`set_npn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_npn_protocols "ssl.SSLContext.set_npn_protocols")\
         and `selected_npn_protocol()` are deprecated: use ALPN instead.\
        \
    *   `ssl.OP_NO_SSL*` options\
        \
    *   `ssl.OP_NO_TLS*` options\
        \
    *   `ssl.PROTOCOL_SSLv3`\
        \
    *   `ssl.PROTOCOL_TLS`\
        \
    *   `ssl.PROTOCOL_TLSv1`\
        \
    *   `ssl.PROTOCOL_TLSv1_1`\
        \
    *   `ssl.PROTOCOL_TLSv1_2`\
        \
    *   `ssl.TLSVersion.SSLv3`\
        \
    *   `ssl.TLSVersion.TLSv1`\
        \
    *   `ssl.TLSVersion.TLSv1_1`\
        \
*   [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")\
     methods:\
    \
    *   `threading.Condition.notifyAll()`: use [`notify_all()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all")\
        .\
        \
    *   `threading.Event.isSet()`: use [`is_set()`](https://docs.python.org/3/library/threading.html#threading.Event.is_set "threading.Event.is_set")\
        .\
        \
    *   `threading.Thread.isDaemon()`, [`threading.Thread.setDaemon()`](https://docs.python.org/3/library/threading.html#threading.Thread.setDaemon "threading.Thread.setDaemon")\
        : use [`threading.Thread.daemon`](https://docs.python.org/3/library/threading.html#threading.Thread.daemon "threading.Thread.daemon")\
         attribute.\
        \
    *   `threading.Thread.getName()`, [`threading.Thread.setName()`](https://docs.python.org/3/library/threading.html#threading.Thread.setName "threading.Thread.setName")\
        : use [`threading.Thread.name`](https://docs.python.org/3/library/threading.html#threading.Thread.name "threading.Thread.name")\
         attribute.\
        \
    *   `threading.currentThread()`: use [`threading.current_thread()`](https://docs.python.org/3/library/threading.html#threading.current_thread "threading.current_thread")\
        .\
        \
    *   `threading.activeCount()`: use [`threading.active_count()`](https://docs.python.org/3/library/threading.html#threading.active_count "threading.active_count")\
        .\
        \
*   [`typing.Text`](https://docs.python.org/3/library/typing.html#typing.Text "typing.Text")\
     ([gh-92332](https://github.com/python/cpython/issues/92332)\
    ).\
    \
*   The internal class `typing._UnionGenericAlias` is no longer used to implement [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")\
    . To preserve compatibility with users using this private class, a compatibility shim will be provided until at least Python 3.17. (Contributed by Jelle Zijlstra in [gh-105499](https://github.com/python/cpython/issues/105499)\
    .)\
    \
*   [`unittest.IsolatedAsyncioTestCase`](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase "unittest.IsolatedAsyncioTestCase")\
    : it is deprecated to return a value that is not `None` from a test case.\
    \
*   [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse "urllib.parse: Parse URLs into or assemble them from components.")\
     deprecated functions: [`urlparse()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse "urllib.parse.urlparse")\
     instead\
    \
    *   `splitattr()`\
        \
    *   `splithost()`\
        \
    *   `splitnport()`\
        \
    *   `splitpasswd()`\
        \
    *   `splitport()`\
        \
    *   `splitquery()`\
        \
    *   `splittag()`\
        \
    *   `splittype()`\
        \
    *   `splituser()`\
        \
    *   `splitvalue()`\
        \
    *   `to_bytes()`\
        \
*   [`wsgiref`](https://docs.python.org/3/library/wsgiref.html#module-wsgiref "wsgiref: WSGI Utilities and Reference Implementation.")\
    : `SimpleHandler.stdout.write()` should not do partial writes.\
    \
*   [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")\
    : Testing the truth value of an [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")\
     is deprecated. In a future release it will always return `True`. Prefer explicit `len(elem)` or `elem is not None` tests instead.\
    \
*   [`sys._clear_type_cache()`](https://docs.python.org/3/library/sys.html#sys._clear_type_cache "sys._clear_type_cache")\
     is deprecated: use [`sys._clear_internal_caches()`](https://docs.python.org/3/library/sys.html#sys._clear_internal_caches "sys._clear_internal_caches")\
     instead.\
    \
\
### Soft deprecations[¶](https://docs.python.org/3/whatsnew/3.15.html#soft-deprecations "Link to this heading")\
\
There are no plans to remove [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
 APIs.\
\
*   [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match")\
     and [`re.Pattern.match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match")\
     are now [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
     in favor of the new [`re.prefixmatch()`](https://docs.python.org/3/library/re.html#re.prefixmatch "re.prefixmatch")\
     and [`re.Pattern.prefixmatch()`](https://docs.python.org/3/library/re.html#re.Pattern.prefixmatch "re.Pattern.prefixmatch")\
     APIs, which have been added as alternate, more explicit names. These are intended to be used to alleviate confusion around what _match_ means by following the Zen of Python’s _“Explicit is better than implicit”_ mantra. Most other language regular expression libraries use an API named _match_ to mean what Python has always called _search_.\
    \
    We **do not** plan to remove the older `match()` name, as it has been used in code for over 30 years. Code supporting older versions of Python should continue to use `match()`, while new code should prefer `prefixmatch()`. See [prefixmatch() vs. match()](https://docs.python.org/3/library/re.html#prefixmatch-vs-match)\
    .\
    \
    (Contributed by Gregory P. Smith in [gh-86519](https://github.com/python/cpython/issues/86519)\
     and Hugo van Kemenade in [gh-148100](https://github.com/python/cpython/issues/148100)\
    .)\
    \
*   Using `'F'` and `'D'` format type codes of the [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")\
     module now are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
     in favor of two-letter forms `'Zf'` and `'Zd'`. (Contributed by Sergey B Kirpichev in [gh-121249](https://github.com/python/cpython/issues/121249)\
    .)\
    \
\
C API changes[¶](https://docs.python.org/3/whatsnew/3.15.html#c-api-changes "Link to this heading")\
\
----------------------------------------------------------------------------------------------------\
\
### New features[¶](https://docs.python.org/3/whatsnew/3.15.html#id9 "Link to this heading")\
\
*   Add [`PyArg_ParseArray()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseArray "PyArg_ParseArray")\
     and [`PyArg_ParseArrayAndKeywords()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseArrayAndKeywords "PyArg_ParseArrayAndKeywords")\
     functions to parse arguments of functions using the [`METH_FASTCALL`](https://docs.python.org/3/c-api/structures.html#c.METH_FASTCALL "METH_FASTCALL")\
     calling convention. (Contributed by Victor Stinner in [gh-144175](https://github.com/python/cpython/issues/144175)\
    .)\
    \
*   Add the following functions for the new [`frozendict`](https://docs.python.org/3/builtins/stdtypes.html#frozendict "frozendict")\
     type:\
    \
    *   [`PyAnyDict_Check()`](https://docs.python.org/3/c-api/dict.html#c.PyAnyDict_Check "PyAnyDict_Check")\
        \
    *   [`PyAnyDict_CheckExact()`](https://docs.python.org/3/c-api/dict.html#c.PyAnyDict_CheckExact "PyAnyDict_CheckExact")\
        \
    *   [`PyFrozenDict_Check()`](https://docs.python.org/3/c-api/dict.html#c.PyFrozenDict_Check "PyFrozenDict_Check")\
        \
    *   [`PyFrozenDict_CheckExact()`](https://docs.python.org/3/c-api/dict.html#c.PyFrozenDict_CheckExact "PyFrozenDict_CheckExact")\
        \
    *   [`PyFrozenDict_New()`](https://docs.python.org/3/c-api/dict.html#c.PyFrozenDict_New "PyFrozenDict_New")\
        \
    \
    (Contributed by Victor Stinner in [gh-141510](https://github.com/python/cpython/issues/141510)\
    .)\
    \
*   Add [`PyObject_CallFinalizerFromDealloc()`](https://docs.python.org/3/c-api/lifecycle.html#c.PyObject_CallFinalizerFromDealloc "PyObject_CallFinalizerFromDealloc")\
     function to the limited C API. (Contributed by Victor Stinner in [gh-146063](https://github.com/python/cpython/issues/146063)\
    .)\
    \
*   Add [`PySys_GetAttr()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetAttr "PySys_GetAttr")\
    , [`PySys_GetAttrString()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetAttrString "PySys_GetAttrString")\
    , [`PySys_GetOptionalAttr()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetOptionalAttr "PySys_GetOptionalAttr")\
    , and [`PySys_GetOptionalAttrString()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetOptionalAttrString "PySys_GetOptionalAttrString")\
     functions as replacements for [`PySys_GetObject()`](https://docs.python.org/3/c-api/sys.html#c.PySys_GetObject "PySys_GetObject")\
    . (Contributed by Serhiy Storchaka in [gh-108512](https://github.com/python/cpython/issues/108512)\
    .)\
    \
*   Add [`PyUnstable_Unicode_GET_CACHED_HASH()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnstable_Unicode_GET_CACHED_HASH "PyUnstable_Unicode_GET_CACHED_HASH")\
     to get the cached hash of a string. See the documentation for caveats. (Contributed by Petr Viktorin in [gh-131510](https://github.com/python/cpython/issues/131510)\
    .)\
    \
*   Add API for checking an extension module’s ABI compatibility: [`Py_mod_abi`](https://docs.python.org/3/c-api/module.html#c.Py_mod_abi "Py_mod_abi")\
    , [`PyABIInfo_Check()`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_Check "PyABIInfo_Check")\
    , and [`PyABIInfo_VAR`](https://docs.python.org/3/c-api/stable.html#c.PyABIInfo_VAR "PyABIInfo_VAR")\
    . (Contributed by Petr Viktorin in [gh-137210](https://github.com/python/cpython/issues/137210)\
    .)\
    \
\
*   Implement [**PEP 782**](https://peps.python.org/pep-0782/)\
    , the [PyBytesWriter API](https://docs.python.org/3/c-api/bytes.html#pybyteswriter)\
    . Add functions:\
    \
    *   [`PyBytesWriter_Create()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Create "PyBytesWriter_Create")\
        \
    *   [`PyBytesWriter_Discard()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Discard "PyBytesWriter_Discard")\
        \
    *   [`PyBytesWriter_Finish()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Finish "PyBytesWriter_Finish")\
        \
    *   [`PyBytesWriter_FinishWithPointer()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_FinishWithPointer "PyBytesWriter_FinishWithPointer")\
        \
    *   [`PyBytesWriter_FinishWithSize()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_FinishWithSize "PyBytesWriter_FinishWithSize")\
        \
    *   [`PyBytesWriter_Format()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Format "PyBytesWriter_Format")\
        \
    *   [`PyBytesWriter_GetData()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_GetData "PyBytesWriter_GetData")\
        \
    *   [`PyBytesWriter_GetSize()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_GetSize "PyBytesWriter_GetSize")\
        \
    *   [`PyBytesWriter_Grow()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Grow "PyBytesWriter_Grow")\
        \
    *   [`PyBytesWriter_GrowAndUpdatePointer()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_GrowAndUpdatePointer "PyBytesWriter_GrowAndUpdatePointer")\
        \
    *   [`PyBytesWriter_Resize()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_Resize "PyBytesWriter_Resize")\
        \
    *   [`PyBytesWriter_WriteBytes()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter_WriteBytes "PyBytesWriter_WriteBytes")\
        \
    \
    (Contributed by Victor Stinner in [gh-129813](https://github.com/python/cpython/issues/129813)\
    .)\
    \
*   [`PyCriticalSection`](https://docs.python.org/3/c-api/synchronization.html#c.PyCriticalSection "PyCriticalSection")\
     and related functions are added to the Stable ABI. (Contributed by Petr Viktorin in [gh-149225](https://github.com/python/cpython/issues/149225)\
    .)\
    \
*   Add a new [`PyImport_CreateModuleFromInitfunc()`](https://docs.python.org/3/c-api/import.html#c.PyImport_CreateModuleFromInitfunc "PyImport_CreateModuleFromInitfunc")\
     C API for creating a module from a _spec_ and _initfunc_. (Contributed by Itamar Oren in [gh-116146](https://github.com/python/cpython/issues/116146)\
    .)\
    \
*   Add [`PyTuple_FromArray()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_FromArray "PyTuple_FromArray")\
     to create a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")\
     from an array. (Contributed by Victor Stinner in [gh-111489](https://github.com/python/cpython/issues/111489)\
    .)\
    \
*   Add a new module export hook, [`PyModExport_*`](https://docs.python.org/3/c-api/extension-modules.html#c.PyModExport_modulename "PyModExport_modulename")\
    .\
    \
    (Contributed by Petr Viktorin in [**PEP 793**](https://peps.python.org/pep-0793/)\
     and [gh-140550](https://github.com/python/cpython/issues/140550)\
    .)\
    \
*   Add functions that are guaranteed to be safe for use in [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse")\
     handlers: [`PyObject_GetTypeData_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GetTypeData_DuringGC "PyObject_GetTypeData_DuringGC")\
    , [`PyObject_GetItemData_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GetItemData_DuringGC "PyObject_GetItemData_DuringGC")\
    , [`PyType_GetModuleState_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetModuleState_DuringGC "PyType_GetModuleState_DuringGC")\
    , [`PyModule_GetState_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyModule_GetState_DuringGC "PyModule_GetState_DuringGC")\
    , [`PyModule_GetToken_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyModule_GetToken_DuringGC "PyModule_GetToken_DuringGC")\
    , [`PyType_GetBaseByToken_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetBaseByToken_DuringGC "PyType_GetBaseByToken_DuringGC")\
    , [`PyType_GetModule_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetModule_DuringGC "PyType_GetModule_DuringGC")\
    , [`PyType_GetModuleByToken_DuringGC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyType_GetModuleByToken_DuringGC "PyType_GetModuleByToken_DuringGC")\
    . (Contributed by Petr Viktorin in [gh-145925](https://github.com/python/cpython/issues/145925)\
    .)\
    \
*   Add [`PyObject_Dump()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Dump "PyObject_Dump")\
     to dump an object to `stderr`. It should only be used for debugging. (Contributed by Victor Stinner in [gh-141070](https://github.com/python/cpython/issues/141070)\
    .)\
    \
*   Implement [**PEP 820**](https://peps.python.org/pep-0820/)\
    : `PySlot` – Unified slot system for the C API. See [Definition slots](https://docs.python.org/3/c-api/slots.html#capi-slots)\
     for documentation.\
    \
    This adds:\
    \
    *   The [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")\
         struct;\
        \
    *   the [`PyType_FromSlots()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSlots "PyType_FromSlots")\
         function;\
        \
    *   new slot IDs: [`Py_slot_end`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_end "Py_slot_end")\
        , [`Py_slot_invalid`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_invalid "Py_slot_invalid")\
        ; [`Py_slot_subslots`](https://docs.python.org/3/c-api/slots.html#c.Py_slot_subslots "Py_slot_subslots")\
        , [`Py_tp_slots`](https://docs.python.org/3/c-api/type.html#c.Py_tp_slots "Py_tp_slots")\
        , [`Py_mod_slots`](https://docs.python.org/3/c-api/module.html#c.Py_mod_slots "Py_mod_slots")\
        ; [`Py_tp_name`](https://docs.python.org/3/c-api/type.html#c.Py_tp_name "Py_tp_name")\
        , [`Py_tp_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_basicsize "Py_tp_basicsize")\
        , [`Py_tp_extra_basicsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_extra_basicsize "Py_tp_extra_basicsize")\
        , [`Py_tp_itemsize`](https://docs.python.org/3/c-api/type.html#c.Py_tp_itemsize "Py_tp_itemsize")\
        , [`Py_tp_flags`](https://docs.python.org/3/c-api/type.html#c.Py_tp_flags "Py_tp_flags")\
        , [`Py_tp_metaclass`](https://docs.python.org/3/c-api/type.html#c.Py_tp_metaclass "Py_tp_metaclass")\
        , [`Py_tp_module`](https://docs.python.org/3/c-api/type.html#c.Py_tp_module "Py_tp_module")\
        ;\
        \
    *   convenience macros: [`PySlot_DATA`](https://docs.python.org/3/c-api/slots.html#c.PySlot_DATA "PySlot_DATA")\
        , [`PySlot_FUNC`](https://docs.python.org/3/c-api/slots.html#c.PySlot_FUNC "PySlot_FUNC")\
        , [`PySlot_SIZE`](https://docs.python.org/3/c-api/slots.html#c.PySlot_SIZE "PySlot_SIZE")\
        , [`PySlot_INT64`](https://docs.python.org/3/c-api/slots.html#c.PySlot_INT64 "PySlot_INT64")\
        , [`PySlot_UINT64`](https://docs.python.org/3/c-api/slots.html#c.PySlot_UINT64 "PySlot_UINT64")\
        , [`PySlot_STATIC_DATA`](https://docs.python.org/3/c-api/slots.html#c.PySlot_STATIC_DATA "PySlot_STATIC_DATA")\
        , [`PySlot_END`](https://docs.python.org/3/c-api/slots.html#c.PySlot_END "PySlot_END")\
        , [`PySlot_PTR`](https://docs.python.org/3/c-api/slots.html#c.PySlot_PTR "PySlot_PTR")\
        , [`PySlot_PTR_STATIC`](https://docs.python.org/3/c-api/slots.html#c.PySlot_PTR_STATIC "PySlot_PTR_STATIC")\
        .\
        \
    \
    The [`PyModule_FromSlotsAndSpec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromSlotsAndSpec "PyModule_FromSlotsAndSpec")\
     function and `PyModExport` [module export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)\
     also use the new `PySlot` struct.\
    \
    The following functions are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
    :\
    \
    *   [`PyType_FromSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec "PyType_FromSpec")\
        \
    *   [`PyType_FromSpecWithBases()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpecWithBases "PyType_FromSpecWithBases")\
        \
    *   [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec")\
        \
    *   [`PyType_FromMetaclass()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromMetaclass "PyType_FromMetaclass")\
        \
    *   [`PyModule_FromDefAndSpec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromDefAndSpec "PyModule_FromDefAndSpec")\
        \
    *   [`PyModule_FromDefAndSpec2()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromDefAndSpec2 "PyModule_FromDefAndSpec2")\
        \
    *   [`PyModule_ExecDef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_ExecDef "PyModule_ExecDef")\
        \
    \
    The slots [`Py_tp_bases`](https://docs.python.org/3/c-api/type.html#c.Py_tp_bases "Py_tp_bases")\
     and [`Py_tp_base`](https://docs.python.org/3/c-api/type.html#c.Py_tp_base "Py_tp_base")\
     are now equivalent: they can be set either to a single type or a tuple of types. The `Py_tp_bases` slot is preferred; the other is ignored if both are specified.\
    \
    (Contributed by Petr Viktorin in [gh-149044](https://github.com/python/cpython/issues/149044)\
    .)\
    \
*   Add [`PyUnstable_ThreadState_SetStackProtection()`](https://docs.python.org/3/c-api/threads.html#c.PyUnstable_ThreadState_SetStackProtection "PyUnstable_ThreadState_SetStackProtection")\
     and [`PyUnstable_ThreadState_ResetStackProtection()`](https://docs.python.org/3/c-api/threads.html#c.PyUnstable_ThreadState_ResetStackProtection "PyUnstable_ThreadState_ResetStackProtection")\
     functions to set the stack protection base address and stack protection size of a Python thread state. (Contributed by Victor Stinner in [gh-139653](https://github.com/python/cpython/issues/139653)\
    .)\
    \
*   Add [`PyUnstable_SetImmortal()`](https://docs.python.org/3/c-api/object.html#c.PyUnstable_SetImmortal "PyUnstable_SetImmortal")\
     C API function to mark objects as [immortal](https://docs.python.org/3/glossary.html#term-immortal)\
    . (Contributed by Kumar Aditya in [gh-143300](https://github.com/python/cpython/issues/143300)\
    .)\
    \
*   Restore private provisional `_Py_InitializeMain()` function removed in Python 3.14. (Contributed by Victor Stinner in [gh-142417](https://github.com/python/cpython/issues/142417)\
    .)\
    \
*   Add [`PyUnstable_DumpTraceback()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnstable_DumpTraceback "PyUnstable_DumpTraceback")\
     and [`PyUnstable_DumpTracebackThreads()`](https://docs.python.org/3/c-api/exceptions.html#c.PyUnstable_DumpTracebackThreads "PyUnstable_DumpTracebackThreads")\
     functions to output Python stacktraces. (Contributed by Alex Malyshev in [gh-145559](https://github.com/python/cpython/issues/145559)\
    .)\
    \
\
### Changed C APIs[¶](https://docs.python.org/3/whatsnew/3.15.html#changed-c-apis "Link to this heading")\
\
*   If the [`Py_TPFLAGS_MANAGED_DICT`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_DICT "Py_TPFLAGS_MANAGED_DICT")\
     or [`Py_TPFLAGS_MANAGED_WEAKREF`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MANAGED_WEAKREF "Py_TPFLAGS_MANAGED_WEAKREF")\
     flag is set then [`Py_TPFLAGS_HAVE_GC`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_GC "Py_TPFLAGS_HAVE_GC")\
     must be set too. (Contributed by Sergey Miryanov in [gh-134786](https://github.com/python/cpython/issues/134786)\
    .)\
    \
*   [`PyDateTime_IMPORT`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_IMPORT "PyDateTime_IMPORT")\
     is now thread safe. Code that directly checks `PyDateTimeAPI` for `NULL` should be updated to call `PyDateTime_IMPORT` instead. (Contributed by Kumar Aditya in [gh-141563](https://github.com/python/cpython/issues/141563)\
    .)\
    \
\
### Removed C APIs[¶](https://docs.python.org/3/whatsnew/3.15.html#removed-c-apis "Link to this heading")\
\
*   Remove deprecated `PyUnicode` functions:\
    \
    *   `PyUnicode_AsDecodedObject()`: Use [`PyCodec_Decode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")\
         instead.\
        \
    *   `PyUnicode_AsDecodedUnicode()`: Use [`PyCodec_Decode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Decode "PyCodec_Decode")\
         instead; note that some codecs (for example, “base64”) may return a type other than [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")\
        , such as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")\
        .\
        \
    *   `PyUnicode_AsEncodedObject()`: Use [`PyCodec_Encode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")\
         instead.\
        \
    *   `PyUnicode_AsEncodedUnicode()`: Use [`PyCodec_Encode()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Encode "PyCodec_Encode")\
         instead; note that some codecs (for example, “base64”) may return a type other than [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")\
        , such as [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")\
        .\
        \
    \
    (Contributed by Stan Ulbrych in [gh-133612](https://github.com/python/cpython/issues/133612)\
    .)\
    \
*   `PyImport_ImportModuleNoBlock()`: deprecated alias of [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")\
    . (Contributed by Bénédikt Tran in [gh-133644](https://github.com/python/cpython/issues/133644)\
    .)\
    \
*   `PyWeakref_GetObject()` and `PyWeakref_GET_OBJECT`: use [`PyWeakref_GetRef()`](https://docs.python.org/3/c-api/weakref.html#c.PyWeakref_GetRef "PyWeakref_GetRef")\
     instead. The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat)\
     can be used to get `PyWeakref_GetRef()` on Python 3.12 and older. (Contributed by Bénédikt Tran in [gh-133644](https://github.com/python/cpython/issues/133644)\
    .)\
    \
*   Remove deprecated `PySys_ResetWarnOptions()`. Clear [`sys.warnoptions`](https://docs.python.org/3/library/sys.html#sys.warnoptions "sys.warnoptions")\
     and `warnings.filters` instead.\
    \
    (Contributed by Nikita Sobolev in [gh-138886](https://github.com/python/cpython/issues/138886)\
    .)\
    \
\
The following functions are removed in favor of [`PyConfig_Get()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")\
. The [pythoncapi-compat project](https://github.com/python/pythoncapi-compat)\
 can be used to get `PyConfig_Get()` on Python 3.13 and older.\
\
*   Python initialization functions:\
    \
    *   `Py_GetExecPrefix()`: use [`PyConfig_Get("base_exec_prefix")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")\
         ([`sys.base_exec_prefix`](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix")\
        ) instead. Use `PyConfig_Get("exec_prefix")` ([`sys.exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix")\
        ) if [virtual environments](https://docs.python.org/3/library/venv.html#venv-def)\
         need to be handled.\
        \
    *   `Py_GetPath()`: use [`PyConfig_Get("module_search_paths")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")\
         ([`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")\
        ) instead.\
        \
    *   `Py_GetPrefix()`: use [`PyConfig_Get("base_prefix")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")\
         ([`sys.base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix")\
        ) instead. Use `PyConfig_Get("prefix")` ([`sys.prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix")\
        ) if [virtual environments](https://docs.python.org/3/library/venv.html#venv-def)\
         need to be handled.\
        \
    *   `Py_GetProgramFullPath()`: use [`PyConfig_Get("executable")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")\
         ([`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")\
        ) instead.\
        \
    *   `Py_GetProgramName()`: use [`PyConfig_Get("executable")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")\
         ([`sys.executable`](https://docs.python.org/3/library/sys.html#sys.executable "sys.executable")\
        ) instead.\
        \
    *   `Py_GetPythonHome()`: use [`PyConfig_Get("home")`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Get "PyConfig_Get")\
         or the [`PYTHONHOME`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHOME)\
         environment variable instead.\
        \
    \
    (Contributed by Bénédikt Tran in [gh-133644](https://github.com/python/cpython/issues/133644)\
    .)\
    \
\
### Deprecated C APIs[¶](https://docs.python.org/3/whatsnew/3.15.html#deprecated-c-apis "Link to this heading")\
\
*   Deprecate [**PEP 456**](https://peps.python.org/pep-0456/)\
     support for providing an external definition of the string hashing scheme. Removal is scheduled for Python 3.19.\
    \
    Previously, embedders could define [`Py_HASH_ALGORITHM`](https://docs.python.org/3/c-api/hash.html#c.Py_HASH_ALGORITHM "Py_HASH_ALGORITHM")\
     to be `Py_HASH_EXTERNAL` to indicate that the hashing scheme was provided externally but this feature was undocumented, untested and most likely unused.\
    \
    (Contributed by Bénédikt Tran in [gh-141226](https://github.com/python/cpython/issues/141226)\
    .)\
    \
*   For unsigned integer formats in [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")\
    , accepting Python integers with value that is larger than the maximal value for the C type or less than the minimal value for the corresponding signed integer type of the same size is now deprecated. (Contributed by Serhiy Storchaka in [gh-132629](https://github.com/python/cpython/issues/132629)\
    .)\
    \
*   [`PyBytes_FromStringAndSize(NULL, len)`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_FromStringAndSize "PyBytes_FromStringAndSize")\
     and [`_PyBytes_Resize()`](https://docs.python.org/3/c-api/bytes.html#c._PyBytes_Resize "_PyBytes_Resize")\
     are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
    , use the [`PyBytesWriter`](https://docs.python.org/3/c-api/bytes.html#c.PyBytesWriter "PyBytesWriter")\
     API instead. (Contributed by Victor Stinner in [gh-129813](https://github.com/python/cpython/issues/129813)\
    .)\
    \
*   `_PyObject_CallMethodId()`, `_PyObject_GetAttrId()` and `_PyUnicode_FromId()` are deprecated since Python 3.15 and will be removed in Python 3.20. Instead, use [`PyUnicode_InternFromString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternFromString "PyUnicode_InternFromString")\
     and cache the result in the module state, then call [`PyObject_CallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethod "PyObject_CallMethod")\
     or [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")\
    . (Contributed by Victor Stinner in [gh-141049](https://github.com/python/cpython/issues/141049)\
    .)\
    \
*   Deprecate [`cval`](https://docs.python.org/3/c-api/complex.html#c.PyComplexObject.cval "PyComplexObject.cval")\
     field of the [`PyComplexObject`](https://docs.python.org/3/c-api/complex.html#c.PyComplexObject "PyComplexObject")\
     type. Use [`PyComplex_AsCComplex()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_AsCComplex "PyComplex_AsCComplex")\
     and [`PyComplex_FromCComplex()`](https://docs.python.org/3/c-api/complex.html#c.PyComplex_FromCComplex "PyComplex_FromCComplex")\
     to convert a Python complex number to/from the C [`Py_complex`](https://docs.python.org/3/c-api/complex.html#c.Py_complex "Py_complex")\
     representation. (Contributed by Sergey B Kirpichev in [gh-128813](https://github.com/python/cpython/issues/128813)\
    .)\
    \
*   Functions [`_Py_c_sum()`](https://docs.python.org/3/c-api/complex.html#c._Py_c_sum "_Py_c_sum")\
    , [`_Py_c_diff()`](https://docs.python.org/3/c-api/complex.html#c._Py_c_diff "_Py_c_diff")\
    , [`_Py_c_neg()`](https://docs.python.org/3/c-api/complex.html#c._Py_c_neg "_Py_c_neg")\
    , [`_Py_c_prod()`](https://docs.python.org/3/c-api/complex.html#c._Py_c_prod "_Py_c_prod")\
    , [`_Py_c_quot()`](https://docs.python.org/3/c-api/complex.html#c._Py_c_quot "_Py_c_quot")\
    , [`_Py_c_pow()`](https://docs.python.org/3/c-api/complex.html#c._Py_c_pow "_Py_c_pow")\
     and [`_Py_c_abs()`](https://docs.python.org/3/c-api/complex.html#c._Py_c_abs "_Py_c_abs")\
     are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
    . (Contributed by Sergey B Kirpichev in [gh-128813](https://github.com/python/cpython/issues/128813)\
    .)\
    \
*   [`bytes_warning`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.bytes_warning "PyConfig.bytes_warning")\
     is deprecated since Python 3.15 and will be removed in Python 3.17. (Contributed by Nikita Sobolev in [gh-136355](https://github.com/python/cpython/issues/136355)\
    .)\
    \
*   `Py_INFINITY` macro is [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
    , use the C11 standard `<math.h>` `INFINITY` instead. (Contributed by Sergey B Kirpichev in [gh-141004](https://github.com/python/cpython/issues/141004)\
    .)\
    \
*   The following macros are [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
    :\
    \
    *   [`Py_ALIGNED`](https://docs.python.org/3/c-api/intro.html#c.Py_ALIGNED "Py_ALIGNED")\
        : Prefer `alignas` instead.\
        \
    *   [`PY_FORMAT_SIZE_T`](https://docs.python.org/3/c-api/intro.html#c.PY_FORMAT_SIZE_T "PY_FORMAT_SIZE_T")\
        : Use `"z"` directly.\
        \
    *   [`Py_LL`](https://docs.python.org/3/c-api/intro.html#c.Py_LL "Py_LL")\
         and [`Py_ULL`](https://docs.python.org/3/c-api/intro.html#c.Py_ULL "Py_ULL")\
        : Use standard suffixes, `LL` and `ULL`.\
        \
    *   [`PY_LONG_LONG`](https://docs.python.org/3/c-api/intro.html#c.PY_LONG_LONG "PY_LONG_LONG")\
        , [`PY_LLONG_MIN`](https://docs.python.org/3/c-api/intro.html#c.PY_LLONG_MIN "PY_LLONG_MIN")\
        , [`PY_LLONG_MAX`](https://docs.python.org/3/c-api/intro.html#c.PY_LLONG_MAX "PY_LLONG_MAX")\
        , [`PY_ULLONG_MAX`](https://docs.python.org/3/c-api/intro.html#c.PY_ULLONG_MAX "PY_ULLONG_MAX")\
        , [`PY_INT32_T`](https://docs.python.org/3/c-api/intro.html#c.PY_INT32_T "PY_INT32_T")\
        , [`PY_UINT32_T`](https://docs.python.org/3/c-api/intro.html#c.PY_UINT32_T "PY_UINT32_T")\
        , [`PY_INT64_T`](https://docs.python.org/3/c-api/intro.html#c.PY_INT64_T "PY_INT64_T")\
        , [`PY_UINT64_T`](https://docs.python.org/3/c-api/intro.html#c.PY_UINT64_T "PY_UINT64_T")\
        , [`PY_SIZE_MAX`](https://docs.python.org/3/c-api/intro.html#c.PY_SIZE_MAX "PY_SIZE_MAX")\
        : Use C99 types/limits.\
        \
    *   [`Py_UNICODE_SIZE`](https://docs.python.org/3/c-api/intro.html#c.Py_UNICODE_SIZE "Py_UNICODE_SIZE")\
        : Use `sizeof(wchar_t)` directly.\
        \
    *   [`Py_VA_COPY`](https://docs.python.org/3/c-api/intro.html#c.Py_VA_COPY "Py_VA_COPY")\
        : Use `va_copy` directly.\
        \
    \
    The macro [`Py_UNICODE_WIDE`](https://docs.python.org/3/c-api/intro.html#c.Py_UNICODE_WIDE "Py_UNICODE_WIDE")\
    , which was scheduled for removal, is [soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)\
     instead.\
    \
    (Contributed by Petr Viktorin in [gh-146175](https://github.com/python/cpython/issues/146175)\
    .)\
    \
*   `Py_MATH_El` and `Py_MATH_PIl` are deprecated since Python 3.15 and will be removed in Python 3.20. (Contributed by Sergey B Kirpichev in [gh-141004](https://github.com/python/cpython/issues/141004)\
    .)\
    \
\
Build changes[¶](https://docs.python.org/3/whatsnew/3.15.html#build-changes "Link to this heading")\
\
----------------------------------------------------------------------------------------------------\
\
*   Removed implicit fallback to the bundled copy of the `libmpdec` library. Now this should be explicitly enabled with [`--with-system-libmpdec`](https://docs.python.org/3/using/configure.html#cmdoption-with-system-libmpdec)\
     set to `no` or with `--without-system-libmpdec`. (Contributed by Sergey B Kirpichev in [gh-115119](https://github.com/python/cpython/issues/115119)\
    .)\
    \
*   The new configure option [`--with-missing-stdlib-config=FILE`](https://docs.python.org/3/using/configure.html#cmdoption-with-missing-stdlib-config)\
     allows distributors to pass a [JSON](https://www.json.org/json-en.html)\
     configuration file containing custom error messages for [standard library](https://docs.python.org/3/glossary.html#term-standard-library)\
     modules that are missing or packaged separately. (Contributed by Stan Ulbrych and Petr Viktorin in [gh-139707](https://github.com/python/cpython/issues/139707)\
    .)\
    \
*   The new configure option [`--with-pymalloc-hugepages`](https://docs.python.org/3/using/configure.html#cmdoption-with-pymalloc-hugepages)\
     enables huge page support for [pymalloc](https://docs.python.org/3/c-api/memory.html#pymalloc)\
     arenas. When enabled, arena size increases to 2 MiB and allocation uses `MAP_HUGETLB` (Linux) or `MEM_LARGE_PAGES` (Windows) with automatic fallback to regular pages. On Windows, use `build.bat --pymalloc-hugepages`. At runtime, huge pages must be explicitly enabled by setting the [`PYTHON_PYMALLOC_HUGEPAGES`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_PYMALLOC_HUGEPAGES)\
     environment variable to `1`. (Contributed by Pablo Galindo Salgado in [gh-144319](https://github.com/python/cpython/issues/144319)\
    .)\
    \
*   Annotating anonymous mmap usage is now supported if the Linux kernel supports _[PR\_SET\_VMA\_ANON\_NAME](https://manpages.debian.org/PR_SET_VMA(2const))\
    _ (Linux 5.17 or newer). Annotations are visible in `/proc/<pid>/maps` if the kernel supports the feature and [`-X dev`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)\
     is passed to Python, or Python is built in [debug mode](https://docs.python.org/3/using/configure.html#debug-build)\
    . (Contributed by Donghee Na in [gh-141770](https://github.com/python/cpython/issues/141770)\
    .)\
    \
*   CPython is now built with frame pointers enabled by default ([**PEP 831**](https://peps.python.org/pep-0831/)\
    ). Pass [`--without-frame-pointers`](https://docs.python.org/3/using/configure.html#cmdoption-without-frame-pointers)\
     to opt out.\
    \
    Authors of C extensions and native libraries built with custom build systems should ensure the unwind chain is intact. This is usually done by adding `-fno-omit-frame-pointer` and similar flags to `CFLAGS`. See [`--without-frame-pointers`](https://docs.python.org/3/using/configure.html#cmdoption-without-frame-pointers)\
     documentation for the specific flags Python uses.\
    \
    (Contributed by Pablo Galindo Salgado and Savannah Ostrowski in [gh-149201](https://github.com/python/cpython/issues/149201)\
    .)\
    \
\
*   64-bit builds using Visual Studio 2026 (MSVC 18) may now use the new [tail-calling interpreter](https://docs.python.org/3/whatsnew/3.14.html#whatsnew314-tail-call-interpreter)\
    . Results on Visual Studio 18.1.1 report between [15-20%](https://github.com/faster-cpython/ideas/blob/main/results/5800X-msvc.pgo2-vs-msvc.pgo.tc.svg)\
     speedup on the geometric mean of pyperformance on Windows x86-64 over the switch-case interpreter on an AMD Ryzen 7 5800X. We have observed speedups ranging from 14% for large pure-Python libraries to 40% for long-running small pure-Python scripts on Windows. This was made possible by a new feature introduced in MSVC 18, which the official Windows 64-bit binaries on [python.org](https://www.python.org/downloads/windows/)\
     now use. (Contributed by Chris Eibl, Ken Jin, and Brandt Bucher in [gh-143068](https://github.com/python/cpython/issues/143068)\
    . Special thanks to Steve Dower, and the MSVC team including Hulon Jenkins.)\
    \
\
Porting to Python 3.15[¶](https://docs.python.org/3/whatsnew/3.15.html#porting-to-python-3-15 "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------\
\
This section lists previously described changes and other bugfixes that may require changes to your code.\
\
*   [`sqlite3.Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection")\
     APIs have been cleaned up.\
    \
    *   All parameters of [`sqlite3.connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect")\
         except _database_ are now keyword-only.\
        \
    *   The first three parameters of methods [`create_function()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function "sqlite3.Connection.create_function")\
         and [`create_aggregate()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_aggregate "sqlite3.Connection.create_aggregate")\
         are now positional-only.\
        \
    *   The first parameter of methods [`set_authorizer()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_authorizer "sqlite3.Connection.set_authorizer")\
        , [`set_progress_handler()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_progress_handler "sqlite3.Connection.set_progress_handler")\
         and [`set_trace_callback()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_trace_callback "sqlite3.Connection.set_trace_callback")\
         is now positional-only.\
        \
    \
    (Contributed by Serhiy Storchaka in [gh-133595](https://github.com/python/cpython/issues/133595)\
    .)\
    \
*   [`resource.RLIM_INFINITY`](https://docs.python.org/3/library/resource.html#resource.RLIM_INFINITY "resource.RLIM_INFINITY")\
     is now always positive. Passing a negative integer value that corresponded to its old value (such as `-1` or `-3`, depending on platform) to [`resource.setrlimit()`](https://docs.python.org/3/library/resource.html#resource.setrlimit "resource.setrlimit")\
     and [`resource.prlimit()`](https://docs.python.org/3/library/resource.html#resource.prlimit "resource.prlimit")\
     is now deprecated. (Contributed by Serhiy Storchaka in [gh-137044](https://github.com/python/cpython/issues/137044)\
    .)\
    \
*   [`mmap.mmap.resize()`](https://docs.python.org/3/library/mmap.html#mmap.mmap.resize "mmap.mmap.resize")\
     has been removed on platforms that don’t support the underlying syscall, instead of raising a [`SystemError`](https://docs.python.org/3/builtins/exceptions.html#SystemError "SystemError")\
    . (Contributed by An Long in [gh-138205](https://github.com/python/cpython/issues/138205)\
    .)\
    \
*   A resource warning is now emitted for an unclosed [`xml.etree.ElementTree.iterparse()`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.iterparse "xml.etree.ElementTree.iterparse")\
     iterator if it opened a file. Use its `close()` method or the [`contextlib.closing()`](https://docs.python.org/3/library/contextlib.html#contextlib.closing "contextlib.closing")\
     context manager to close it. (Contributed by Osama Abdelkader and Serhiy Storchaka in [gh-140601](https://github.com/python/cpython/issues/140601)\
    .)\
    \
*   If a short option and a single-dash long option are passed to [`argparse.ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")\
    , _dest_ is now inferred from the single-dash long option. For example, in `add_argument('-f', '-foo')`, _dest_ is now `'foo'` instead of `'f'`. Pass an explicit _dest_ argument to preserve the old behavior. (Contributed by Serhiy Storchaka in [gh-138697](https://github.com/python/cpython/issues/138697)\
    .)\
    \
*   Padding of input no longer required in [`base64.urlsafe_b64decode()`](https://docs.python.org/3/library/base64.html#base64.urlsafe_b64decode "base64.urlsafe_b64decode")\
    . Pass a new argument `padded=True` or use [`base64.b64decode()`](https://docs.python.org/3/library/base64.html#base64.b64decode "base64.b64decode")\
     with argument `altchars=b'-_'` (this works with older Python versions) to make padding required. (Contributed by Serhiy Storchaka in [gh-73613](https://github.com/python/cpython/issues/73613)\
    .)\
    \
*   Since [`unittest.TestCase.assertWarns()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns")\
     and [`unittest.TestCase.assertWarnsRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "unittest.TestCase.assertWarnsRegex")\
     no longer swallow warnings that do not match the specified category or regex, your tests may start leaking some warnings that were previously masked. Use warning filters to silence them or additional `assertWarns*()` to catch and check them. (Contributed by Serhiy Storchaka in [gh-143231](https://github.com/python/cpython/issues/143231)\
    .)\
    \
\
Notable changes in 3.15.2[¶](https://docs.python.org/3/whatsnew/3.15.html#notable-changes-in-3-15-2 "Link to this heading")\
\
----------------------------------------------------------------------------------------------------------------------------\
\
### importlib[¶](https://docs.python.org/3/whatsnew/3.15.html#id12 "Link to this heading")\
\
*   Threads that simultaneously perform first-time `import package.submodule` imports no longer risk a deadlock or spurious import errors, a regression introduced in 3.15.0 by the fix for [gh-83065](https://github.com/python/cpython/issues/83065)\
    . A package’s import lock is now released as soon as its `__init__` returns. [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module")\
     now returns the partially initialized module in a circular import split across threads, as the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)\
     statement already did, instead of raising `_DeadlockError`. (Contributed by Gregory P. Smith in [gh-159963](https://github.com/python/cpython/issues/159963)\
    .)\
    \
\
### ssl[¶](https://docs.python.org/3/whatsnew/3.15.html#id13 "Link to this heading")\
\
*   The [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")\
     module now rejects TLS certificate chains that contain one of a set of compromised eMudhra intermediate CA certificates. The affected certificates are identified by their public key, so cross-signed copies that reuse the same key are blocked as well. It is a defense-in-depth backstop that applies even when an application supplies its own root CA bundle, and regardless of whether the platform trust store has removed trust. (Contributed by Christian Heimes in [gh-160040](https://github.com/python/cpython/issues/160040)\
     for [**CVE 2026-115557**](https://www.cve.org/CVERecord?id=CVE-2026-115557)\
    .)\
    \
\
### [Table of Contents](https://docs.python.org/3/contents.html)\
\
*   [What’s new in Python 3.15](https://docs.python.org/3/whatsnew/3.15.html#)\
    *   [Summary – Release highlights](https://docs.python.org/3/whatsnew/3.15.html#summary-release-highlights)\
        \
    *   [New features](https://docs.python.org/3/whatsnew/3.15.html#new-features)\
        *   [**PEP 810**: Explicit lazy imports](https://docs.python.org/3/whatsnew/3.15.html#pep-810-explicit-lazy-imports)\
            \
        *   [**PEP 814**: Add frozendict built-in type](https://docs.python.org/3/whatsnew/3.15.html#pep-814-add-frozendict-built-in-type)\
            \
        *   [**PEP 661**: Add sentinel built-in type](https://docs.python.org/3/whatsnew/3.15.html#pep-661-add-sentinel-built-in-type)\
            \
        *   [**PEP 799**: A dedicated profiling package](https://docs.python.org/3/whatsnew/3.15.html#pep-799-a-dedicated-profiling-package)\
            \
        *   [Tachyon: High-frequency statistical sampling profiler](https://docs.python.org/3/whatsnew/3.15.html#tachyon-high-frequency-statistical-sampling-profiler)\
            \
        *   [**PEP 831**: Frame pointers enabled by default](https://docs.python.org/3/whatsnew/3.15.html#pep-831-frame-pointers-enabled-by-default)\
            \
        *   [**PEP 798**: Unpacking in comprehensions](https://docs.python.org/3/whatsnew/3.15.html#pep-798-unpacking-in-comprehensions)\
            \
        *   [**PEP 829**: Package startup configuration files](https://docs.python.org/3/whatsnew/3.15.html#pep-829-package-startup-configuration-files)\
            \
        *   [**PEP 803**: Stable ABI for free-threaded builds](https://docs.python.org/3/whatsnew/3.15.html#pep-803-stable-abi-for-free-threaded-builds)\
            \
        *   [**PEP 788**: Protecting the C API from interpreter finalization](https://docs.python.org/3/whatsnew/3.15.html#pep-788-protecting-the-c-api-from-interpreter-finalization)\
            \
        *   [Improved error messages](https://docs.python.org/3/whatsnew/3.15.html#improved-error-messages)\
            \
    *   [Other language changes](https://docs.python.org/3/whatsnew/3.15.html#other-language-changes)\
        \
    *   [Default interactive shell](https://docs.python.org/3/whatsnew/3.15.html#default-interactive-shell)\
        \
    *   [New modules](https://docs.python.org/3/whatsnew/3.15.html#new-modules)\
        *   [math.integer](https://docs.python.org/3/whatsnew/3.15.html#math-integer)\
            \
    *   [Improved modules](https://docs.python.org/3/whatsnew/3.15.html#improved-modules)\
        *   [argparse](https://docs.python.org/3/whatsnew/3.15.html#argparse)\
            \
        *   [array](https://docs.python.org/3/whatsnew/3.15.html#array)\
            \
        *   [ast](https://docs.python.org/3/whatsnew/3.15.html#ast)\
            \
        *   [asyncio](https://docs.python.org/3/whatsnew/3.15.html#asyncio)\
            \
        *   [base64](https://docs.python.org/3/whatsnew/3.15.html#base64)\
            \
        *   [binascii](https://docs.python.org/3/whatsnew/3.15.html#binascii)\
            \
        *   [calendar](https://docs.python.org/3/whatsnew/3.15.html#calendar)\
            \
        *   [collections](https://docs.python.org/3/whatsnew/3.15.html#collections)\
            \
        *   [concurrent.futures](https://docs.python.org/3/whatsnew/3.15.html#concurrent-futures)\
            \
        *   [contextlib](https://docs.python.org/3/whatsnew/3.15.html#contextlib)\
            \
        *   [ctypes](https://docs.python.org/3/whatsnew/3.15.html#ctypes)\
            \
        *   [dataclasses](https://docs.python.org/3/whatsnew/3.15.html#dataclasses)\
            \
        *   [dbm](https://docs.python.org/3/whatsnew/3.15.html#dbm)\
            \
        *   [difflib](https://docs.python.org/3/whatsnew/3.15.html#difflib)\
            \
        *   [email](https://docs.python.org/3/whatsnew/3.15.html#email)\
            \
        *   [faulthandler](https://docs.python.org/3/whatsnew/3.15.html#faulthandler)\
            \
        *   [functools](https://docs.python.org/3/whatsnew/3.15.html#functools)\
            \
        *   [gc](https://docs.python.org/3/whatsnew/3.15.html#gc)\
            \
        *   [hashlib](https://docs.python.org/3/whatsnew/3.15.html#hashlib)\
            \
        *   [http.client](https://docs.python.org/3/whatsnew/3.15.html#http-client)\
            \
        *   [http.server](https://docs.python.org/3/whatsnew/3.15.html#http-server)\
            \
        *   [importlib.metadata](https://docs.python.org/3/whatsnew/3.15.html#importlib-metadata)\
            \
        *   [inspect](https://docs.python.org/3/whatsnew/3.15.html#inspect)\
            \
        *   [json](https://docs.python.org/3/whatsnew/3.15.html#json)\
            \
        *   [locale](https://docs.python.org/3/whatsnew/3.15.html#locale)\
            \
        *   [math](https://docs.python.org/3/whatsnew/3.15.html#math)\
            \
        *   [mimetypes](https://docs.python.org/3/whatsnew/3.15.html#mimetypes)\
            \
        *   [mmap](https://docs.python.org/3/whatsnew/3.15.html#mmap)\
            \
        *   [os](https://docs.python.org/3/whatsnew/3.15.html#os)\
            \
        *   [os.path](https://docs.python.org/3/whatsnew/3.15.html#os-path)\
            \
        *   [pathlib](https://docs.python.org/3/whatsnew/3.15.html#pathlib)\
            \
        *   [pdb](https://docs.python.org/3/whatsnew/3.15.html#pdb)\
            \
        *   [pickle](https://docs.python.org/3/whatsnew/3.15.html#pickle)\
            \
        *   [pickletools](https://docs.python.org/3/whatsnew/3.15.html#pickletools)\
            \
        *   [pprint](https://docs.python.org/3/whatsnew/3.15.html#pprint)\
            \
        *   [re](https://docs.python.org/3/whatsnew/3.15.html#re)\
            \
        *   [resource](https://docs.python.org/3/whatsnew/3.15.html#resource)\
            \
        *   [shelve](https://docs.python.org/3/whatsnew/3.15.html#shelve)\
            \
        *   [socket](https://docs.python.org/3/whatsnew/3.15.html#socket)\
            \
        *   [sqlite3](https://docs.python.org/3/whatsnew/3.15.html#sqlite3)\
            \
        *   [ssl](https://docs.python.org/3/whatsnew/3.15.html#ssl)\
            \
        *   [subprocess](https://docs.python.org/3/whatsnew/3.15.html#subprocess)\
            \
        *   [symtable](https://docs.python.org/3/whatsnew/3.15.html#symtable)\
            \
        *   [sys](https://docs.python.org/3/whatsnew/3.15.html#sys)\
            \
        *   [sys.monitoring](https://docs.python.org/3/whatsnew/3.15.html#sys-monitoring)\
            \
        *   [tarfile](https://docs.python.org/3/whatsnew/3.15.html#tarfile)\
            \
        *   [threading](https://docs.python.org/3/whatsnew/3.15.html#threading)\
            \
        *   [timeit](https://docs.python.org/3/whatsnew/3.15.html#timeit)\
            \
        *   [tkinter](https://docs.python.org/3/whatsnew/3.15.html#tkinter)\
            \
        *   [tokenize](https://docs.python.org/3/whatsnew/3.15.html#tokenize)\
            \
        *   [tomllib](https://docs.python.org/3/whatsnew/3.15.html#tomllib)\
            \
        *   [types](https://docs.python.org/3/whatsnew/3.15.html#types)\
            \
        *   [typing](https://docs.python.org/3/whatsnew/3.15.html#typing)\
            \
        *   [unicodedata](https://docs.python.org/3/whatsnew/3.15.html#unicodedata)\
            \
        *   [unittest](https://docs.python.org/3/whatsnew/3.15.html#unittest)\
            \
        *   [urllib.parse](https://docs.python.org/3/whatsnew/3.15.html#urllib-parse)\
            \
        *   [venv](https://docs.python.org/3/whatsnew/3.15.html#venv)\
            \
        *   [warnings](https://docs.python.org/3/whatsnew/3.15.html#warnings)\
            \
        *   [wave](https://docs.python.org/3/whatsnew/3.15.html#wave)\
            \
        *   [webbrowser](https://docs.python.org/3/whatsnew/3.15.html#webbrowser)\
            \
        *   [xml](https://docs.python.org/3/whatsnew/3.15.html#xml)\
            \
        *   [xml.parsers.expat](https://docs.python.org/3/whatsnew/3.15.html#xml-parsers-expat)\
            \
        *   [zlib](https://docs.python.org/3/whatsnew/3.15.html#zlib)\
            \
    *   [Optimizations](https://docs.python.org/3/whatsnew/3.15.html#optimizations)\
        *   [base64 & binascii](https://docs.python.org/3/whatsnew/3.15.html#base64-binascii)\
            \
        *   [csv](https://docs.python.org/3/whatsnew/3.15.html#csv)\
            \
        *   [Upgraded experimental JIT compiler](https://docs.python.org/3/whatsnew/3.15.html#upgraded-experimental-jit-compiler)\
            \
    *   [Removed](https://docs.python.org/3/whatsnew/3.15.html#removed)\
        *   [ast](https://docs.python.org/3/whatsnew/3.15.html#id1)\
            \
        *   [collections.abc](https://docs.python.org/3/whatsnew/3.15.html#collections-abc)\
            \
        *   [ctypes](https://docs.python.org/3/whatsnew/3.15.html#id2)\
            \
        *   [datetime](https://docs.python.org/3/whatsnew/3.15.html#datetime)\
            \
        *   [glob](https://docs.python.org/3/whatsnew/3.15.html#glob)\
            \
        *   [http.server](https://docs.python.org/3/whatsnew/3.15.html#id3)\
            \
        *   [importlib](https://docs.python.org/3/whatsnew/3.15.html#importlib)\
            \
        *   [importlib.resources](https://docs.python.org/3/whatsnew/3.15.html#importlib-resources)\
            \
        *   [pathlib](https://docs.python.org/3/whatsnew/3.15.html#id4)\
            \
        *   [platform](https://docs.python.org/3/whatsnew/3.15.html#platform)\
            \
        *   [sre\_\*](https://docs.python.org/3/whatsnew/3.15.html#sre)\
            \
        *   [sysconfig](https://docs.python.org/3/whatsnew/3.15.html#sysconfig)\
            \
        *   [threading](https://docs.python.org/3/whatsnew/3.15.html#id5)\
            \
        *   [types](https://docs.python.org/3/whatsnew/3.15.html#id6)\
            \
        *   [typing](https://docs.python.org/3/whatsnew/3.15.html#id7)\
            \
        *   [wave](https://docs.python.org/3/whatsnew/3.15.html#id8)\
            \
        *   [zipimport](https://docs.python.org/3/whatsnew/3.15.html#zipimport)\
            \
    *   [Deprecated](https://docs.python.org/3/whatsnew/3.15.html#deprecated)\
        *   [New deprecations](https://docs.python.org/3/whatsnew/3.15.html#new-deprecations)\
            \
        *   [Pending removal in Python 3.16](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-python-3-16)\
            \
        *   [Pending removal in Python 3.17](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-python-3-17)\
            \
        *   [Pending removal in Python 3.18](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-python-3-18)\
            \
        *   [Pending removal in Python 3.19](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-python-3-19)\
            \
        *   [Pending removal in Python 3.20](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-python-3-20)\
            \
        *   [Pending removal in future versions](https://docs.python.org/3/whatsnew/3.15.html#pending-removal-in-future-versions)\
            \
        *   [Soft deprecations](https://docs.python.org/3/whatsnew/3.15.html#soft-deprecations)\
            \
    *   [C API changes](https://docs.python.org/3/whatsnew/3.15.html#c-api-changes)\
        *   [New features](https://docs.python.org/3/whatsnew/3.15.html#id9)\
            \
        *   [Changed C APIs](https://docs.python.org/3/whatsnew/3.15.html#changed-c-apis)\
            \
        *   [Removed C APIs](https://docs.python.org/3/whatsnew/3.15.html#removed-c-apis)\
            \
        *   [Deprecated C APIs](https://docs.python.org/3/whatsnew/3.15.html#deprecated-c-apis)\
            \
    *   [Build changes](https://docs.python.org/3/whatsnew/3.15.html#build-changes)\
        \
    *   [Porting to Python 3.15](https://docs.python.org/3/whatsnew/3.15.html#porting-to-python-3-15)\
        \
    *   [Notable changes in 3.15.2](https://docs.python.org/3/whatsnew/3.15.html#notable-changes-in-3-15-2)\
        *   [importlib](https://docs.python.org/3/whatsnew/3.15.html#id12)\
            \
        *   [ssl](https://docs.python.org/3/whatsnew/3.15.html#id13)\
            \
\
#### Previous topic\
\
[What’s New in Python](https://docs.python.org/3/whatsnew/index.html "previous chapter")\
\
#### Next topic\
\
[What’s new in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=What%E2%80%99s+new+in+Python+3.15&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fwhatsnew%2F3.15.html&pagesource=whatsnew%2F3.15.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/whatsnew/3.15.rst?plain=1)\
    \
\
«\
\
### Navigation\
\
*   [index](https://docs.python.org/3/genindex.html "General Index")\
    \
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")\
     |\
*   [next](https://docs.python.org/3/whatsnew/3.14.html "What’s new in Python 3.14")\
     |\
*   [previous](https://docs.python.org/3/whatsnew/index.html "What’s New in Python")\
     |\
*   ![Python logo](https://docs.python.org/3/_static/py.svg)\
*   [Python](https://www.python.org/)\
     »\
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文\
    \
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6\
    \
\
*   [3.15.2 documentation](https://docs.python.org/3/index.html)\
     »\
*   [What’s New in Python](https://docs.python.org/3/whatsnew/index.html)\
     »\
*   [What’s new in Python 3.15](https://docs.python.org/3/whatsnew/3.15.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |