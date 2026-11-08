### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/resource.html "resource — Resource usage information")
     |
*   [previous](https://docs.python.org/3/library/pty.html "pty — Pseudo-terminal utilities")
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
*   [`fcntl` — The `fcntl` and `ioctl` system calls](https://docs.python.org/3/library/fcntl.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`fcntl` — The `fcntl` and `ioctl` system calls[¶](https://docs.python.org/3/library/fcntl.html#module-fcntl "Link to this heading")

====================================================================================================================================

* * *

This module performs file and I/O control on file descriptors. It is an interface to the `fcntl()` and `ioctl()` Unix routines. See the _[fcntl(2)](https://manpages.debian.org/fcntl(2))
_ and _[ioctl(2)](https://manpages.debian.org/ioctl(2))
_ Unix manual pages for full details.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

All functions in this module take a file descriptor _fd_ as their first argument. This can be an integer file descriptor, such as returned by `sys.stdin.fileno()`, or an [`io.IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase")
 object, such as `sys.stdin` itself, which provides a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 that returns a genuine file descriptor.

Changed in version 3.3: Operations in this module used to raise an [`IOError`](https://docs.python.org/3/builtins/exceptions.html#IOError "IOError")
 where they now raise an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

Changed in version 3.8: The `fcntl` module now contains `F_ADD_SEALS`, `F_GET_SEALS`, and `F_SEAL_*` constants for sealing of [`os.memfd_create()`](https://docs.python.org/3/library/os.html#os.memfd_create "os.memfd_create")
 file descriptors.

Changed in version 3.9: On macOS, the `fcntl` module exposes the `F_GETPATH` constant, which obtains the path of a file from a file descriptor. On Linux(>=3.15), the `fcntl` module exposes the `F_OFD_GETLK`, `F_OFD_SETLK` and `F_OFD_SETLKW` constants, which are used when working with open file description locks.

Changed in version 3.10: On Linux >= 2.6.11, the `fcntl` module exposes the `F_GETPIPE_SZ` and `F_SETPIPE_SZ` constants, which allow to check and modify a pipe’s size respectively.

Changed in version 3.11: On FreeBSD, the `fcntl` module exposes the `F_DUP2FD` and `F_DUP2FD_CLOEXEC` constants, which allow to duplicate a file descriptor, the latter setting `FD_CLOEXEC` flag in addition.

Changed in version 3.12: On Linux >= 4.5, the `fcntl` module exposes the `FICLONE` and `FICLONERANGE` constants, which allow to share some data of one file with another file by reflinking on some filesystems (e.g., btrfs, OCFS2, and XFS). This behavior is commonly referred to as “copy-on-write”.

Changed in version 3.13: On Linux >= 2.6.32, the `fcntl` module exposes the `F_GETOWN_EX`, `F_SETOWN_EX`, `F_OWNER_TID`, `F_OWNER_PID`, `F_OWNER_PGRP` constants, which allow to direct I/O availability signals to a specific thread, process, or process group. On Linux >= 4.13, the `fcntl` module exposes the `F_GET_RW_HINT`, `F_SET_RW_HINT`, `F_GET_FILE_RW_HINT`, `F_SET_FILE_RW_HINT`, and `RWH_WRITE_LIFE_*` constants, which allow to inform the kernel about the relative expected lifetime of writes on a given inode or via a particular open file description. On Linux >= 5.1 and NetBSD, the `fcntl` module exposes the `F_SEAL_FUTURE_WRITE` constant for use with `F_ADD_SEALS` and `F_GET_SEALS` operations. On FreeBSD, the `fcntl` module exposes the `F_READAHEAD`, `F_ISUNIONSTACK`, and `F_KINFO` constants. On macOS and FreeBSD, the `fcntl` module exposes the `F_RDAHEAD` constant. On NetBSD and AIX, the `fcntl` module exposes the `F_CLOSEM` constant. On NetBSD, the `fcntl` module exposes the `F_MAXFD` constant. On macOS and NetBSD, the `fcntl` module exposes the `F_GETNOSIGPIPE` and `F_SETNOSIGPIPE` constant.

Changed in version 3.14: On Linux >= 6.1, the `fcntl` module exposes the `F_DUPFD_QUERY` to query a file descriptor pointing to the same file.

The module defines the following functions:

fcntl.fcntl(_fd_, _cmd_, _arg\=0_, _/_)[¶](https://docs.python.org/3/library/fcntl.html#fcntl.fcntl "Link to this definition")

Perform the operation _cmd_ on file descriptor _fd_ (file objects providing a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method are accepted as well). The values used for _cmd_ are operating system dependent, and are available as constants in the `fcntl` module, using the same names as used in the relevant C header files. The argument _arg_ can either be an integer value, a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
, or a string. The type and size of _arg_ must match the type and size of the argument of the operation as specified in the relevant C documentation.

When _arg_ is an integer, the function returns the integer return value of the C `fcntl()` call.

When the argument is bytes-like object, it represents a binary structure, for example, created by [`struct.pack()`](https://docs.python.org/3/library/struct.html#struct.pack "struct.pack")
. A string value is encoded to binary using the UTF-8 encoding. The binary data is copied to a buffer whose address is passed to the C `fcntl()` call. The return value after a successful call is the contents of the buffer, converted to a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object. The length of the returned object will be the same as the length of the _arg_ argument.

If the `fcntl()` call fails, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised.

Note

If the type or size of _arg_ does not match the type or size of the operation’s argument (for example, if an integer is passed when a pointer is expected, or the information returned in the buffer by the operating system is larger than the size of _arg_), this is most likely to result in a segmentation violation or a more subtle data corruption.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `fcntl.fcntl` with arguments `fd`, `cmd`, `arg`.

Changed in version 3.14: Add support of arbitrary [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
, not only [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
.

Changed in version 3.15: The size of bytes-like objects is no longer limited to 1024 bytes.

fcntl.ioctl(_fd_, _request_, _arg\=0_, _mutate\_flag\=True_, _/_)[¶](https://docs.python.org/3/library/fcntl.html#fcntl.ioctl "Link to this definition")

This function is identical to the [`fcntl()`](https://docs.python.org/3/library/fcntl.html#fcntl.fcntl "fcntl.fcntl")
 function, except that the argument handling is even more complicated.

The _request_ parameter is limited to values that can fit in 32-bits or 64-bits, depending on the platform. Additional constants of interest for use as the _request_ argument can be found in the [`termios`](https://docs.python.org/3/library/termios.html#module-termios "termios: POSIX style tty control.")
 module, under the same names as used in the relevant C header files.

The parameter _arg_ can be an integer, a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)
, or a string. The type and size of _arg_ must match the type and size of the argument of the operation as specified in the relevant C documentation.

If _arg_ does not support the read-write buffer interface or the _mutate\_flag_ is false, behavior is as for the [`fcntl()`](https://docs.python.org/3/library/fcntl.html#fcntl.fcntl "fcntl.fcntl")
 function.

If _arg_ supports the read-write buffer interface (like [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
) and _mutate\_flag_ is true (the default), then the buffer is (in effect) passed to the underlying `ioctl()` system call, the latter’s return code is passed back to the calling Python, and the buffer’s new contents reflect the action of the `ioctl()`. This is a slight simplification, because if the supplied buffer is less than 1024 bytes long it is first copied into a static buffer 1024 bytes long which is then passed to `ioctl()` and copied back into the supplied buffer.

If the `ioctl()` call fails, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exception is raised.

Note

If the type or size of _arg_ does not match the type or size of the operation’s argument (for example, if an integer is passed when a pointer is expected, or the information returned in the buffer by the operating system is larger than the size of _arg_), this is most likely to result in a segmentation violation or a more subtle data corruption.

An example:

Copy

\>>> import array, fcntl, struct, termios, os
\>>> os.getpgrp()
13341
\>>> struct.unpack('h', fcntl.ioctl(0, termios.TIOCGPGRP, "  "))\[0\]
13341
\>>> buf \= array.array('h', \[0\])
\>>> fcntl.ioctl(0, termios.TIOCGPGRP, buf, 1)
0
\>>> buf
array('h', \[13341\])

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `fcntl.ioctl` with arguments `fd`, `request`, `arg`.

Changed in version 3.14: The GIL is always released during a system call. System calls failing with EINTR are automatically retried.

Changed in version 3.15: The size of not mutated bytes-like objects is no longer limited to 1024 bytes.

fcntl.flock(_fd_, _operation_, _/_)[¶](https://docs.python.org/3/library/fcntl.html#fcntl.flock "Link to this definition")

Perform the lock operation _operation_ on file descriptor _fd_ (file objects providing a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method are accepted as well). See the Unix manual _[flock(2)](https://manpages.debian.org/flock(2))
_ for details. (On some systems, this function is emulated using `fcntl()`.)

If the `flock()` call fails, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exception is raised.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `fcntl.flock` with arguments `fd`, `operation`.

fcntl.lockf(_fd_, _cmd_, _len\=0_, _start\=0_, _whence\=0_, _/_)[¶](https://docs.python.org/3/library/fcntl.html#fcntl.lockf "Link to this definition")

This is essentially a wrapper around the [`fcntl()`](https://docs.python.org/3/library/fcntl.html#fcntl.fcntl "fcntl.fcntl")
 locking calls. _fd_ is the file descriptor (file objects providing a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method are accepted as well) of the file to lock or unlock, and _cmd_ is one of the following values:

fcntl.LOCK\_UN[¶](https://docs.python.org/3/library/fcntl.html#fcntl.LOCK_UN "Link to this definition")

Release an existing lock.

fcntl.LOCK\_SH[¶](https://docs.python.org/3/library/fcntl.html#fcntl.LOCK_SH "Link to this definition")

Acquire a shared lock.

fcntl.LOCK\_EX[¶](https://docs.python.org/3/library/fcntl.html#fcntl.LOCK_EX "Link to this definition")

Acquire an exclusive lock.

fcntl.LOCK\_NB[¶](https://docs.python.org/3/library/fcntl.html#fcntl.LOCK_NB "Link to this definition")

Bitwise OR with any of the other three `LOCK_*` constants to make the request non-blocking.

If `LOCK_NB` is used and the lock cannot be acquired, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 will be raised and the exception will have an _errno_ attribute set to [`EACCES`](https://docs.python.org/3/library/errno.html#errno.EACCES "errno.EACCES")
 or [`EAGAIN`](https://docs.python.org/3/library/errno.html#errno.EAGAIN "errno.EAGAIN")
 (depending on the operating system; for portability, check for both values). On at least some systems, `LOCK_EX` can only be used if the file descriptor refers to a file opened for writing.

_len_ is the number of bytes to lock, _start_ is the byte offset at which the lock starts, relative to _whence_, and _whence_ is as with [`io.IOBase.seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek")
, specifically:

*   `0` – relative to the start of the file ([`os.SEEK_SET`](https://docs.python.org/3/library/os.html#os.SEEK_SET "os.SEEK_SET")
    )
    
*   `1` – relative to the current buffer position ([`os.SEEK_CUR`](https://docs.python.org/3/library/os.html#os.SEEK_CUR "os.SEEK_CUR")
    )
    
*   `2` – relative to the end of the file ([`os.SEEK_END`](https://docs.python.org/3/library/os.html#os.SEEK_END "os.SEEK_END")
    )
    

The default for _start_ is 0, which means to start at the beginning of the file. The default for _len_ is 0 which means to lock to the end of the file. The default for _whence_ is also 0.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `fcntl.lockf` with arguments `fd`, `cmd`, `len`, `start`, `whence`.

Examples (all on a SVR4 compliant system):

Copy

import struct, fcntl, os

f \= open(...)
rv \= fcntl.fcntl(f, fcntl.F\_SETFL, os.O\_NDELAY)

lockdata \= struct.pack('hhllhh', fcntl.F\_WRLCK, 0, 0, 0, 0, 0)
rv \= fcntl.fcntl(f, fcntl.F\_SETLKW, lockdata)

Note that in the first example the return value variable _rv_ will hold an integer value; in the second example it will hold a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object. The structure lay-out for the _lockdata_ variable is system dependent — therefore using the [`flock()`](https://docs.python.org/3/library/fcntl.html#fcntl.flock "fcntl.flock")
 call may be better.

See also

Module [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")

If the locking flags [`O_SHLOCK`](https://docs.python.org/3/library/os.html#os.O_SHLOCK "os.O_SHLOCK")
 and [`O_EXLOCK`](https://docs.python.org/3/library/os.html#os.O_EXLOCK "os.O_EXLOCK")
 are present in the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
 module (on BSD only), the [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
 function provides an alternative to the [`lockf()`](https://docs.python.org/3/library/fcntl.html#fcntl.lockf "fcntl.lockf")
 and [`flock()`](https://docs.python.org/3/library/fcntl.html#fcntl.flock "fcntl.flock")
 functions.

#### Previous topic

[`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html "previous chapter")

#### Next topic

[`resource` — Resource usage information](https://docs.python.org/3/library/resource.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=fcntl+%E2%80%94+The+fcntl+and+ioctl+system+calls&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffcntl.html&pagesource=library%2Ffcntl.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/fcntl.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/resource.html "resource — Resource usage information")
     |
*   [previous](https://docs.python.org/3/library/pty.html "pty — Pseudo-terminal utilities")
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
*   [`fcntl` — The `fcntl` and `ioctl` system calls](https://docs.python.org/3/library/fcntl.html)
    
*    
    
    |
*   Theme Auto Light Dark |