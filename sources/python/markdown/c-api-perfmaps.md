### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/pyexpat.html "Expat C API")
     |
*   [previous](https://docs.python.org/3/c-api/time.html "PyTime C API")
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
*   [Support for Perf Maps](https://docs.python.org/3/c-api/perfmaps.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Support for Perf Maps[¶](https://docs.python.org/3/c-api/perfmaps.html#support-for-perf-maps "Link to this heading")

=====================================================================================================================

On supported platforms (Linux and macOS), the runtime can take advantage of _perf map files_ to make Python functions visible to an external profiling tool (such as [perf](https://perf.wiki.kernel.org/index.php/Main_Page)
 or [samply](https://github.com/mstange/samply/)
). A running process may create a file in the `/tmp` directory, which contains entries that can map a section of executable code to a name. This interface is described in the [documentation of the Linux Perf tool](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/tools/perf/Documentation/jit-interface.txt)
.

In Python, these helper APIs can be used by libraries and features that rely on generating machine code on the fly.

Note that holding an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
 is not required for these APIs.

int PyUnstable\_PerfMapState\_Init(void)[¶](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Init "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Open the `/tmp/perf-$pid.map` file, unless it’s already opened, and create a lock to ensure thread-safe writes to the file (provided the writes are done through [`PyUnstable_WritePerfMapEntry()`](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_WritePerfMapEntry "PyUnstable_WritePerfMapEntry")
). Normally, there’s no need to call this explicitly; just use `PyUnstable_WritePerfMapEntry()` and it will initialize the state on first call.

Returns `0` on success, `-1` on failure to create/open the perf map file, or `-2` on failure to create a lock. Check `errno` for more information about the cause of a failure.

int PyUnstable\_WritePerfMapEntry(const void \*code\_addr, size\_t code\_size, const char \*entry\_name)[¶](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_WritePerfMapEntry "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Write one single entry to the `/tmp/perf-$pid.map` file. This function is thread safe. Here is what an example entry looks like:

\# address      size  name
7f3529fcf759 b     py::bar:/run/t.py

Will call [`PyUnstable_PerfMapState_Init()`](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Init "PyUnstable_PerfMapState_Init")
 before writing the entry, if the perf map file is not already opened. Returns `0` on success, or the same error codes as `PyUnstable_PerfMapState_Init()` on failure.

void PyUnstable\_PerfMapState\_Fini(void)[¶](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Fini "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Close the perf map file opened by [`PyUnstable_PerfMapState_Init()`](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Init "PyUnstable_PerfMapState_Init")
. This is called by the runtime itself during interpreter shut-down. In general, there shouldn’t be a reason to explicitly call this, except to handle specific scenarios such as forking.

int PyUnstable\_CopyPerfMapFile(const char \*parent\_filename)[¶](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_CopyPerfMapFile "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Open the `/tmp/perf-$pid.map` file and append the content of _parent\_filename_ to it.

This function is available on all platforms but only generates output on platforms that support perf maps (currently only Linux). On other platforms, it does nothing.

Added in version 3.13.

int PyUnstable\_PerfTrampoline\_CompileCode([PyCodeObject](https://docs.python.org/3/c-api/code.html#c.PyCodeObject "PyCodeObject")
 \*code)[¶](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfTrampoline_CompileCode "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Compile the given code object using the current perf trampoline.

The “current” trampoline is the one set by the runtime or the most recent [`PyUnstable_PerfTrampoline_SetPersistAfterFork()`](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfTrampoline_SetPersistAfterFork "PyUnstable_PerfTrampoline_SetPersistAfterFork")
 call.

If no trampoline is set, falls back to normal compilation (no perf map entry).

Parameters:

*   **code** – The code object to compile.
    

Returns:

0 on success, -1 on failure.

Added in version 3.13.

int PyUnstable\_PerfTrampoline\_SetPersistAfterFork(int enable)[¶](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfTrampoline_SetPersistAfterFork "Link to this definition")
  

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api)
. It may change without warning in minor releases._

Set whether the perf trampoline should persist after a fork.

*   If `enable` is true (non-zero): perf map file remains open/valid post-fork. Child process inherits all existing perf map entries.
    
*   If `enable` is false (zero): perf map closes post-fork. Child process gets empty perf map.
    

Default: false (clears on fork).

Parameters:

*   **enable** – 1 to enable, 0 to disable.
    

Returns:

0 on success, -1 on failure.

Added in version 3.13.

#### Previous topic

[PyTime C API](https://docs.python.org/3/c-api/time.html "previous chapter")

#### Next topic

[Expat C API](https://docs.python.org/3/c-api/pyexpat.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Support+for+Perf+Maps&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fperfmaps.html&pagesource=c-api%2Fperfmaps.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/perfmaps.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/pyexpat.html "Expat C API")
     |
*   [previous](https://docs.python.org/3/c-api/time.html "PyTime C API")
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
*   [Support for Perf Maps](https://docs.python.org/3/c-api/perfmaps.html)
    
*    
    
    |
*   Theme Auto Light Dark |