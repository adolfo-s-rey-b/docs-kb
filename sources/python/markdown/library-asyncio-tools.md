### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-eventloop.html "Event loop")
     |
*   [previous](https://docs.python.org/3/library/asyncio-graph.html "Call graph introspection")
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
*   [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html)
     »
*   [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
     »
*   [Command-line introspection tools](https://docs.python.org/3/library/asyncio-tools.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Command-line introspection tools[¶](https://docs.python.org/3/library/asyncio-tools.html#command-line-introspection-tools "Link to this heading")

==================================================================================================================================================

**Source code:** [Lib/asyncio/tools.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/tools.py)

* * *

The `asyncio` module can be invoked as a script via `python -m asyncio` to inspect the task graph of another running Python process without modifying it or restarting it. The `asyncio.tools` submodule implements this interface.

The following commands inspect the process identified by `PID`:

Copy

$ python \-m asyncio pstree \[\--retries N\] PID
$ python \-m asyncio ps \[\--retries N\] PID

The commands read the target process state without executing any code in it. They are only available on supported platforms and may require permission to inspect another process. See the [permission requirements](https://docs.python.org/3/howto/remote_debugging.html#permission-requirements)
 for details.

See also

[Call graph introspection](https://docs.python.org/3/library/asyncio-graph.html#asyncio-graph)

Programmatic APIs for inspecting the async call graph of a task or future in the current process.

The command examples below use this program, which creates a task hierarchy suitable for inspection and prints its process ID:

example.py[¶](https://docs.python.org/3/library/asyncio-tools.html#id1 "Link to this code")

Copy

import asyncio
import os

async def play(track):
    await asyncio.sleep(3600)
    print(f"🎵 Finished: {track}")

async def album(name, tracks):
    async with asyncio.TaskGroup() as tg:
        for track in tracks:
            tg.create\_task(play(track), name\=track)

async def main():
    print(f"PID: {os.getpid()}")
    async with asyncio.TaskGroup() as tg:
        tg.create\_task(
            album("Sundowning", \["TNDNBTG", "Levitate"\]),
            name\="Sundowning",
        )
        tg.create\_task(
            album("TMBTE", \["DYWTYLM", "Aqua Regia"\]),
            name\="TMBTE",
        )

asyncio.run(main())

Run the program in one terminal and leave it running:

Copy

$ python example.py
PID: 12345

Then pass the printed process ID to the commands from another terminal. Thread IDs, task IDs, file paths, and line numbers vary between runs and source layouts.

Added in version 3.14.

Command-line options[¶](https://docs.python.org/3/library/asyncio-tools.html#command-line-options "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

pstree PID[¶](https://docs.python.org/3/library/asyncio-tools.html#cmdoption-arg-pstree "Link to this definition")

Display task and coroutine relationships as a tree. Each task is shown with its full coroutine stack, nested under the task (if any) that is awaiting it. This subcommand is useful for quickly identifying which branch of a task hierarchy is blocked and where in its coroutine stack execution has paused:

Copy

$ python \-m asyncio pstree 12345
└── (T) Task-1
    └──  main example.py:12
        └──  TaskGroup.\_\_aexit\_\_ Lib/asyncio/taskgroups.py:75
            └──  TaskGroup.\_aexit Lib/asyncio/taskgroups.py:124
                ├── (T) Sundowning
                │   └──  album example.py:7
                │       └──  TaskGroup.\_\_aexit\_\_ Lib/asyncio/taskgroups.py:75
                │           └──  TaskGroup.\_aexit Lib/asyncio/taskgroups.py:124
                │               ├── (T) TNDNBTG
                │               │   └──  play example.py:4
                │               │       └──  sleep Lib/asyncio/tasks.py:702
                │               └── (T) Levitate
                │                   └──  play example.py:4
                │                       └──  sleep Lib/asyncio/tasks.py:702
                └── (T) TMBTE
                    └──  album example.py:7
                        └──  TaskGroup.\_\_aexit\_\_ Lib/asyncio/taskgroups.py:75
                            └──  TaskGroup.\_aexit Lib/asyncio/taskgroups.py:124
                                ├── (T) DYWTYLM
                                │   └──  play example.py:4
                                │       └──  sleep Lib/asyncio/tasks.py:702
                                └── (T) Aqua Regia
                                    └──  play example.py:4
                                        └──  sleep Lib/asyncio/tasks.py:702

If the await graph contains a cycle, `pstree` reports an error instead of printing a tree. A cycle in the await graph is unusual and typically indicates a programming error:

Copy

$ python \-m asyncio pstree 12345
ERROR: await-graph contains cycles - cannot print a tree!

cycle: Task-2 → Task-3 → Task-2

ps PID[¶](https://docs.python.org/3/library/asyncio-tools.html#cmdoption-arg-ps "Link to this definition")

Display a flat table of all pending tasks in the process _PID_. Each row shows the event-loop thread ID, task ID and name, coroutine stack, and the awaiting task’s stack, name, and ID, if any.

This subcommand prints all tasks regardless of whether the await graph contains cycles:

Copy

$ python \-m asyncio ps 12345
tid        task id              task name            coroutine stack                                    awaiter chain                                      awaiter name    awaiter id
\------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
18445801   0x10a456060          Task-1               TaskGroup.\_aexit -> TaskGroup.\_\_aexit\_\_ -> main                                                                       0x0
18445801   0x10a439f60          Sundowning           TaskGroup.\_aexit -> TaskGroup.\_\_aexit\_\_ -> album   TaskGroup.\_aexit -> TaskGroup.\_\_aexit\_\_ -> main    Task-1          0x10a456060
18445801   0x10a439d70          TMBTE                TaskGroup.\_aexit -> TaskGroup.\_\_aexit\_\_ -> album   TaskGroup.\_aexit -> TaskGroup.\_\_aexit\_\_ -> main    Task-1          0x10a456060
18445801   0x10a2a3a80          TNDNBTG              sleep -> play                                      TaskGroup.\_aexit -> TaskGroup.\_\_aexit\_\_ -> album   Sundowning      0x10a439f60
18445801   0x10a2a38a0          Levitate             sleep -> play                                      TaskGroup.\_aexit -> TaskGroup.\_\_aexit\_\_ -> album   Sundowning      0x10a439f60
18445801   0x10a2d7150          DYWTYLM              sleep -> play                                      TaskGroup.\_aexit -> TaskGroup.\_\_aexit\_\_ -> album   TMBTE           0x10a439d70
18445801   0x10a6bdaa0          Aqua Regia           sleep -> play                                      TaskGroup.\_aexit -> TaskGroup.\_\_aexit\_\_ -> album   TMBTE           0x10a439d70

\--retries N[¶](https://docs.python.org/3/library/asyncio-tools.html#cmdoption-retries "Link to this definition")

Retry failed attempts to inspect the target process up to _N_ times. This can help when the target process changes while its state is being read.

Added in version 3.15.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Command-line introspection tools](https://docs.python.org/3/library/asyncio-tools.html#)
    *   [Command-line options](https://docs.python.org/3/library/asyncio-tools.html#command-line-options)
        

#### Previous topic

[Call graph introspection](https://docs.python.org/3/library/asyncio-graph.html "previous chapter")

#### Next topic

[Event loop](https://docs.python.org/3/library/asyncio-eventloop.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Command-line+introspection+tools&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-tools.html&pagesource=library%2Fasyncio-tools.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-tools.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-eventloop.html "Event loop")
     |
*   [previous](https://docs.python.org/3/library/asyncio-graph.html "Call graph introspection")
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
*   [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html)
     »
*   [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
     »
*   [Command-line introspection tools](https://docs.python.org/3/library/asyncio-tools.html)
    
*    
    
    |
*   Theme Auto Light Dark |