### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-queue.html "Queues")
     |
*   [previous](https://docs.python.org/3/library/asyncio-sync.html "Synchronization Primitives")
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
*   [Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Subprocesses[¶](https://docs.python.org/3/library/asyncio-subprocess.html#subprocesses "Link to this heading")

===============================================================================================================

**Source code:** [Lib/asyncio/subprocess.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/subprocess.py)
, [Lib/asyncio/base\_subprocess.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/base_subprocess.py)

* * *

This section describes high-level async/await asyncio APIs to create and manage subprocesses.

Here’s an example of how asyncio can run a shell command and obtain its result:

Copy

import asyncio

async def run(cmd):
    proc \= await asyncio.create\_subprocess\_shell(
        cmd,
        stdout\=asyncio.subprocess.PIPE,
        stderr\=asyncio.subprocess.PIPE)

    stdout, stderr \= await proc.communicate()

    print(f'\[{cmd!r} exited with {proc.returncode}\]')
    if stdout:
        print(f'\[stdout\]\\n{stdout.decode()}')
    if stderr:
        print(f'\[stderr\]\\n{stderr.decode()}')

asyncio.run(run('ls /zzz'))

will print:

Copy

\['ls /zzz' exited with 1\]
\[stderr\]
ls: /zzz: No such file or directory

Because all asyncio subprocess functions are asynchronous and asyncio provides many tools to work with such functions, it is easy to execute and monitor multiple subprocesses in parallel. It is indeed trivial to modify the above example to run several commands simultaneously:

Copy

async def main():
    await asyncio.gather(
        run('ls /zzz'),
        run('sleep 1; echo "hello"'))

asyncio.run(main())

See also the [Examples](https://docs.python.org/3/library/asyncio-subprocess.html#examples)
 subsection.

Creating Subprocesses[¶](https://docs.python.org/3/library/asyncio-subprocess.html#creating-subprocesses "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

async asyncio.create\_subprocess\_exec(_program_, _\*args_, _stdin\=None_, _stdout\=None_, _stderr\=None_, _limit\=65536_, _\*\*kwds_)[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "Link to this definition")

Create a subprocess.

The _limit_ argument sets the buffer limit for [`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")
 wrappers for [`stdout`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stdout "asyncio.subprocess.Process.stdout")
 and [`stderr`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stderr "asyncio.subprocess.Process.stderr")
 (if [`subprocess.PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE")
 is passed to _stdout_ and _stderr_ arguments).

Return a [`Process`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process "asyncio.subprocess.Process")
 instance.

See the documentation of [`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")
 for other parameters.

If the process object is garbage collected while the process is still running, the child process will be killed.

Changed in version 3.10: Removed the _loop_ parameter.

async asyncio.create\_subprocess\_shell(_cmd_, _stdin\=None_, _stdout\=None_, _stderr\=None_, _limit\=65536_, _\*\*kwds_)[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_shell "Link to this definition")

Run the _cmd_ shell command.

The _limit_ argument sets the buffer limit for [`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")
 wrappers for [`stdout`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stdout "asyncio.subprocess.Process.stdout")
 and [`stderr`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stderr "asyncio.subprocess.Process.stderr")
 (if [`subprocess.PIPE`](https://docs.python.org/3/library/subprocess.html#subprocess.PIPE "subprocess.PIPE")
 is passed to _stdout_ and _stderr_ arguments).

Return a [`Process`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process "asyncio.subprocess.Process")
 instance.

See the documentation of [`loop.subprocess_shell()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell")
 for other parameters.

If the process object is garbage collected while the process is still running, the child process will be killed.

Important

It is the application’s responsibility to ensure that all whitespace and special characters are quoted appropriately to avoid [shell injection](https://en.wikipedia.org/wiki/Shell_injection#Shell_injection)
 vulnerabilities. The [`shlex.quote()`](https://docs.python.org/3/library/shlex.html#shlex.quote "shlex.quote")
 function can be used to properly escape whitespace and special shell characters in strings that are going to be used to construct shell commands.

Changed in version 3.10: Removed the _loop_ parameter.

Note

Subprocesses are available for Windows if a [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
 is used. See [Subprocess Support on Windows](https://docs.python.org/3/library/asyncio-platforms.html#asyncio-windows-subprocess)
 for details.

See also

asyncio also has the following _low-level_ APIs to work with subprocesses: [`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec")
, [`loop.subprocess_shell()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell")
, [`loop.connect_read_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe")
, [`loop.connect_write_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe")
, as well as the [Subprocess Transports](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-subprocess-transports)
 and [Subprocess Protocols](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-subprocess-protocols)
.

Constants[¶](https://docs.python.org/3/library/asyncio-subprocess.html#constants "Link to this heading")

---------------------------------------------------------------------------------------------------------

asyncio.subprocess.PIPE[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.PIPE "Link to this definition")

Can be passed to the _stdin_, _stdout_ or _stderr_ parameters.

If _PIPE_ is passed to _stdin_ argument, the [`Process.stdin`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stdin "asyncio.subprocess.Process.stdin")
 attribute will point to a [`StreamWriter`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter")
 instance.

If _PIPE_ is passed to _stdout_ or _stderr_ arguments, the [`Process.stdout`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stdout "asyncio.subprocess.Process.stdout")
 and [`Process.stderr`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stderr "asyncio.subprocess.Process.stderr")
 attributes will point to [`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")
 instances.

asyncio.subprocess.STDOUT[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.STDOUT "Link to this definition")

Special value that can be used as the _stderr_ argument and indicates that standard error should be redirected into standard output.

asyncio.subprocess.DEVNULL[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.DEVNULL "Link to this definition")

Special value that can be used as the _stdin_, _stdout_ or _stderr_ argument to process creation functions. It indicates that the special file [`os.devnull`](https://docs.python.org/3/library/os.html#os.devnull "os.devnull")
 will be used for the corresponding subprocess stream.

Interacting with Subprocesses[¶](https://docs.python.org/3/library/asyncio-subprocess.html#interacting-with-subprocesses "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

Both [`create_subprocess_exec()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "asyncio.create_subprocess_exec")
 and [`create_subprocess_shell()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_shell "asyncio.create_subprocess_shell")
 functions return instances of the _Process_ class. _Process_ is a high-level wrapper that allows communicating with subprocesses and watching for their completion.

class asyncio.subprocess.Process[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process "Link to this definition")

An object that wraps OS processes created by the [`create_subprocess_exec()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "asyncio.create_subprocess_exec")
 and [`create_subprocess_shell()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_shell "asyncio.create_subprocess_shell")
 functions.

This class is designed to have a similar API to the [`subprocess.Popen`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen "subprocess.Popen")
 class, but there are some notable differences:

*   unlike Popen, Process instances do not have an equivalent to the [`poll()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.poll "subprocess.Popen.poll")
     method;
    
*   the [`communicate()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.communicate "asyncio.subprocess.Process.communicate")
     and [`wait()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.wait "asyncio.subprocess.Process.wait")
     methods don’t have a _timeout_ parameter: use the [`wait_for()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for "asyncio.wait_for")
     function;
    
*   the [`Process.wait()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.wait "asyncio.subprocess.Process.wait")
     method is asynchronous, whereas [`subprocess.Popen.wait()`](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.wait "subprocess.Popen.wait")
     method is implemented as a blocking busy loop;
    
*   the _universal\_newlines_ parameter is not supported.
    

This class is [not thread safe](https://docs.python.org/3/library/asyncio-dev.html#asyncio-multithreading)
.

See also the [Subprocess and Threads](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio-subprocess-threads)
 section.

async wait()[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.wait "Link to this definition")

Wait for the child process to terminate.

Set and return the [`returncode`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.returncode "asyncio.subprocess.Process.returncode")
 attribute.

Note

This method can deadlock when using `stdout=PIPE` or `stderr=PIPE` and the child process generates so much output that it blocks waiting for the OS pipe buffer to accept more data. Use the [`communicate()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.communicate "asyncio.subprocess.Process.communicate")
 method when using pipes to avoid this condition.

async communicate(_input\=None_)[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.communicate "Link to this definition")

Interact with process:

1.  send data to _stdin_ (if _input_ is not `None`);
    
2.  closes _stdin_;
    
3.  read data from _stdout_ and _stderr_, until EOF is reached;
    
4.  wait for process to terminate.
    

The optional _input_ argument is the data ([`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object) that will be sent to the child process.

Return a tuple `(stdout_data, stderr_data)`.

If either [`BrokenPipeError`](https://docs.python.org/3/builtins/exceptions.html#BrokenPipeError "BrokenPipeError")
 or [`ConnectionResetError`](https://docs.python.org/3/builtins/exceptions.html#ConnectionResetError "ConnectionResetError")
 exception is raised when writing _input_ into _stdin_, the exception is ignored. This condition occurs when the process exits before all data are written into _stdin_.

If it is desired to send data to the process’ _stdin_, the process needs to be created with `stdin=PIPE`. Similarly, to get anything other than `None` in the result tuple, the process has to be created with `stdout=PIPE` and/or `stderr=PIPE` arguments.

Note, that the data read is buffered in memory, so do not use this method if the data size is large or unlimited.

Changed in version 3.12: _stdin_ gets closed when `input=None` too.

send\_signal(_signal_)[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.send_signal "Link to this definition")

Sends the signal _signal_ to the child process.

Note

On Windows, [`SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "signal.SIGTERM")
 is an alias for [`terminate()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.terminate "asyncio.subprocess.Process.terminate")
. `CTRL_C_EVENT` and `CTRL_BREAK_EVENT` can be sent to processes started with a _creationflags_ parameter which includes `CREATE_NEW_PROCESS_GROUP`.

terminate()[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.terminate "Link to this definition")

Stop the child process.

On POSIX systems this method sends [`SIGTERM`](https://docs.python.org/3/library/signal.html#signal.SIGTERM "signal.SIGTERM")
 to the child process.

On Windows the Win32 API function `TerminateProcess()` is called to stop the child process.

kill()[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.kill "Link to this definition")

Kill the child process.

On POSIX systems this method sends [`SIGKILL`](https://docs.python.org/3/library/signal.html#signal.SIGKILL "signal.SIGKILL")
 to the child process.

On Windows this method is an alias for [`terminate()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.terminate "asyncio.subprocess.Process.terminate")
.

stdin[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stdin "Link to this definition")

Standard input stream ([`StreamWriter`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter")
) or `None` if the process was created with `stdin=None`.

stdout[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stdout "Link to this definition")

Standard output stream ([`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")
) or `None` if the process was created with `stdout=None`.

stderr[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stderr "Link to this definition")

Standard error stream ([`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")
) or `None` if the process was created with `stderr=None`.

Warning

Use the [`communicate()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.communicate "asyncio.subprocess.Process.communicate")
 method rather than [`process.stdin.write()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stdin "asyncio.subprocess.Process.stdin")
, [`await process.stdout.read()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stdout "asyncio.subprocess.Process.stdout")
 or [`await process.stderr.read()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.stderr "asyncio.subprocess.Process.stderr")
. This avoids deadlocks due to streams pausing reading or writing and blocking the child process.

pid[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.pid "Link to this definition")

Process identification number (PID).

Note that for processes created by the [`create_subprocess_shell()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_shell "asyncio.create_subprocess_shell")
 function, this attribute is the PID of the spawned shell.

returncode[¶](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process.returncode "Link to this definition")

Return code of the process when it exits.

A `None` value indicates that the process has not terminated yet.

For processes created with [`create_subprocess_exec()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "asyncio.create_subprocess_exec")
, a negative value `-N` indicates that the child was terminated by signal `N` (POSIX only).

For processes created with [`create_subprocess_shell()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_shell "asyncio.create_subprocess_shell")
, the return code reflects the exit status of the shell itself (e.g. `/bin/sh`), which may map signals to codes such as `128+N`. See the documentation of the shell (for example, the Bash manual’s Exit Status) for details.

### Subprocess and Threads[¶](https://docs.python.org/3/library/asyncio-subprocess.html#subprocess-and-threads "Link to this heading")

Standard asyncio event loop supports running subprocesses from different threads by default.

On Windows subprocesses are provided by [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop")
 only (default), [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
 has no subprocess support.

Note that alternative event loop implementations might have own limitations; please refer to their documentation.

See also

The [Concurrency and multithreading in asyncio](https://docs.python.org/3/library/asyncio-dev.html#asyncio-multithreading)
 section.

### Examples[¶](https://docs.python.org/3/library/asyncio-subprocess.html#examples "Link to this heading")

An example using the [`Process`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process "asyncio.subprocess.Process")
 class to control a subprocess and the [`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader")
 class to read from its standard output.

The subprocess is created by the [`create_subprocess_exec()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "asyncio.create_subprocess_exec")
 function:

Copy

import asyncio
import sys

async def get\_date():
    code \= 'import datetime as dt; print(dt.datetime.now())'

    \# Create the subprocess; redirect the standard output
    \# into a pipe.
    proc \= await asyncio.create\_subprocess\_exec(
        sys.executable, '-c', code,
        stdout\=asyncio.subprocess.PIPE)

    \# Read one line of output.
    data \= await proc.stdout.readline()
    line \= data.decode('ascii').rstrip()

    \# Wait for the subprocess exit.
    await proc.wait()
    return line

date \= asyncio.run(get\_date())
print(f"Current date: {date}")

See also the [same example](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-example-subprocess-proto)
 written using low-level APIs.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html#)
    *   [Creating Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html#creating-subprocesses)
        
    *   [Constants](https://docs.python.org/3/library/asyncio-subprocess.html#constants)
        
    *   [Interacting with Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html#interacting-with-subprocesses)
        *   [Subprocess and Threads](https://docs.python.org/3/library/asyncio-subprocess.html#subprocess-and-threads)
            
        *   [Examples](https://docs.python.org/3/library/asyncio-subprocess.html#examples)
            

#### Previous topic

[Synchronization Primitives](https://docs.python.org/3/library/asyncio-sync.html "previous chapter")

#### Next topic

[Queues](https://docs.python.org/3/library/asyncio-queue.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Subprocesses&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fasyncio-subprocess.html&pagesource=library%2Fasyncio-subprocess.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/asyncio-subprocess.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/asyncio-queue.html "Queues")
     |
*   [previous](https://docs.python.org/3/library/asyncio-sync.html "Synchronization Primitives")
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
*   [Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html)
    
*    
    
    |
*   Theme Auto Light Dark |