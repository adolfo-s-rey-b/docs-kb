### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/fcntl.html "fcntl — The fcntl and ioctl system calls")
     |
*   [previous](https://docs.python.org/3/library/tty.html "tty — Terminal control functions")
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
*   [Unix-specific services](https://docs.python.org/3/library/unix.html)
     »
*   [`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`pty` — Pseudo-terminal utilities[¶](https://docs.python.org/3/library/pty.html#module-pty "Link to this heading")

===================================================================================================================

**Source code:** [Lib/pty.py](https://github.com/python/cpython/tree/3.15/Lib/pty.py)

* * *

The `pty` module defines operations for handling the pseudo-terminal concept: starting another process and being able to write to and read from its controlling terminal programmatically.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Pseudo-terminal handling is highly platform dependent. This code is mainly tested on Linux, FreeBSD, and macOS (it is supposed to work on other POSIX platforms but it’s not been thoroughly tested).

The `pty` module defines the following functions:

pty.fork()[¶](https://docs.python.org/3/library/pty.html#pty.fork "Link to this definition")

Fork. Connect the child’s controlling terminal to a pseudo-terminal. Return value is `(pid, fd)`. Note that the child gets _pid_ 0, and the _fd_ is _invalid_. The parent’s return value is the _pid_ of the child, and _fd_ is a file descriptor connected to the child’s controlling terminal (and also to the child’s standard input and output).

The returned file descriptor _fd_ is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

Warning

On macOS the use of this function is unsafe when mixed with using higher-level system APIs, and that includes using [`urllib.request`](https://docs.python.org/3/library/urllib.request.html#module-urllib.request "urllib.request: Extensible library for opening URLs.")
.

Changed in version 3.15: The returned file descriptor is now made non-inheritable.

pty.openpty()[¶](https://docs.python.org/3/library/pty.html#pty.openpty "Link to this definition")

Open a new pseudo-terminal pair, using [`os.openpty()`](https://docs.python.org/3/library/os.html#os.openpty "os.openpty")
 if possible, or emulation code for generic Unix systems. Return a pair of file descriptors `(master, slave)`, for the master and the slave end, respectively.

pty.spawn(_argv_\[, _master\_read_\[, _stdin\_read_\]\])[¶](https://docs.python.org/3/library/pty.html#pty.spawn "Link to this definition")

Spawn a process, and connect its controlling terminal with the current process’s standard io. This is often used to baffle programs which insist on reading from the controlling terminal. It is expected that the process spawned behind the pty will eventually terminate, and when it does _spawn_ will return.

A loop copies STDIN of the current process to the child and data received from the child to STDOUT of the current process. It is not signaled to the child if STDIN of the current process closes down.

The functions _master\_read_ and _stdin\_read_ are passed a file descriptor which they should read from, and they should always return a byte string. In order to force spawn to return before the child process exits an empty byte array should be returned to signal end of file.

The default implementation for both functions will read and return up to 1024 bytes each time the function is called. The _master\_read_ callback is passed the pseudoterminal’s master file descriptor to read output from the child process, and _stdin\_read_ is passed file descriptor 0, to read from the parent process’s standard input.

Returning an empty byte string from either callback is interpreted as an end-of-file (EOF) condition, and that callback will not be called after that. If _stdin\_read_ signals EOF the controlling terminal can no longer communicate with the parent process OR the child process. Unless the child process will quit without any input, _spawn_ will then loop forever. If _master\_read_ signals EOF the same behavior results (on linux at least).

Return the exit status value from [`os.waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
 on the child process.

[`os.waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode")
 can be used to convert the exit status into an exit code.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `pty.spawn` with argument `argv`.

Changed in version 3.4: `spawn()` now returns the status value from [`os.waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid")
 on the child process.

Example[¶](https://docs.python.org/3/library/pty.html#example "Link to this heading")

--------------------------------------------------------------------------------------

The following program acts like the Unix command _[script(1)](https://manpages.debian.org/script(1))
_, using a pseudo-terminal to record all input and output of a terminal session in a “typescript”.

Copy

import argparse
import os
import pty
import sys
import time

parser \= argparse.ArgumentParser()
parser.add\_argument('-a', dest\='append', action\='store\_true')
parser.add\_argument('-p', dest\='use\_python', action\='store\_true')
parser.add\_argument('filename', nargs\='?', default\='typescript')
options \= parser.parse\_args()

shell \= sys.executable if options.use\_python else os.environ.get('SHELL', 'sh')
filename \= options.filename
mode \= 'ab' if options.append else 'wb'

with open(filename, mode) as script:
    def read(fd):
        data \= os.read(fd, 1024)
        script.write(data)
        return data

    print('Script started, file is', filename)
    script.write(('Script started on %s\\n' % time.asctime()).encode())

    pty.spawn(shell, read)

    script.write(('Script done on %s\\n' % time.asctime()).encode())
    print('Script done, file is', filename)

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html#)
    *   [Example](https://docs.python.org/3/library/pty.html#example)
        

#### Previous topic

[`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html "previous chapter")

#### Next topic

[`fcntl` — The `fcntl` and `ioctl` system calls](https://docs.python.org/3/library/fcntl.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=pty+%E2%80%94+Pseudo-terminal+utilities&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fpty.html&pagesource=library%2Fpty.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/pty.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/fcntl.html "fcntl — The fcntl and ioctl system calls")
     |
*   [previous](https://docs.python.org/3/library/tty.html "tty — Terminal control functions")
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
*   [Unix-specific services](https://docs.python.org/3/library/unix.html)
     »
*   [`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html)
    
*    
    
    |
*   Theme Auto Light Dark |