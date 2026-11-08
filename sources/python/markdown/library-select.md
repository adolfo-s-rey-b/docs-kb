### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/selectors.html "selectors — High-level I/O multiplexing")
     |
*   [previous](https://docs.python.org/3/library/ssl.html "ssl — TLS/SSL wrapper for socket objects")
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
*   [`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`select` — Waiting for I/O completion[¶](https://docs.python.org/3/library/select.html#module-select "Link to this heading")

=============================================================================================================================

* * *

This module provides access to the `select()` and `poll()` functions available in most operating systems, `devpoll()` available on Solaris and derivatives, `epoll()` available on Linux 2.5+ and `kqueue()` available on most BSD. Note that on Windows, it only works for sockets; on other operating systems, it also works for other file types (in particular, on Unix, it works on pipes). It cannot be used on regular files to determine whether a file has grown since it was last read.

Note

The [`selectors`](https://docs.python.org/3/library/selectors.html#module-selectors "selectors: High-level I/O multiplexing.")
 module allows high-level and efficient I/O multiplexing, built upon the `select` module primitives. Users are encouraged to use the `selectors` module instead, unless they want precise control over the OS-level primitives used.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

The module defines the following:

exception select.error[¶](https://docs.python.org/3/library/select.html#select.error "Link to this definition")

A deprecated alias of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

Changed in version 3.3: Following [**PEP 3151**](https://peps.python.org/pep-3151/)
, this class was made an alias of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

select.devpoll()[¶](https://docs.python.org/3/library/select.html#select.devpoll "Link to this definition")

Returns a `/dev/poll` polling object; see section [/dev/poll polling objects](https://docs.python.org/3/library/select.html#devpoll-objects)
 below for the methods supported by devpoll objects.

`devpoll()` objects are linked to the number of file descriptors allowed at the time of instantiation. If your program reduces this value, `devpoll()` will fail. If your program increases this value, `devpoll()` may return an incomplete list of active file descriptors.

The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

Added in version 3.3.

Changed in version 3.4: The new file descriptor is now non-inheritable.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Solaris.

select.epoll(_sizehint\=\-1_, _flags\=0_)[¶](https://docs.python.org/3/library/select.html#select.epoll "Link to this definition")

Return an edge polling object, which can be used as Edge or Level Triggered interface for I/O events.

_sizehint_ informs epoll about the expected number of events to be registered. It must be positive, or `-1` to use the default. It is only used on older systems where _[epoll\_create1(2)](https://manpages.debian.org/epoll_create1(2))
_ is not available; otherwise it has no effect (though its value is still checked).

_flags_ is deprecated and completely ignored. However, when supplied, its value must be `0` or `select.EPOLL_CLOEXEC`, otherwise `OSError` is raised.

See the [Edge and level trigger polling (epoll) objects](https://docs.python.org/3/library/select.html#epoll-objects)
 section below for the methods supported by epolling objects.

`epoll` objects support the context management protocol: when used in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement, the new file descriptor is automatically closed at the end of the block.

The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

Changed in version 3.3: Added the _flags_ parameter.

Changed in version 3.4: Support for the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement was added. The new file descriptor is now non-inheritable.

Deprecated since version 3.4: The _flags_ parameter. `select.EPOLL_CLOEXEC` is used by default now. Use [`os.set_inheritable()`](https://docs.python.org/3/library/os.html#os.set_inheritable "os.set_inheritable")
 to make the file descriptor inheritable.

Changed in version 3.15: When CPython is built, this function may be disabled using [`--disable-epoll`](https://docs.python.org/3/using/configure.html#cmdoption-disable-epoll)
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.5.44.

select.poll()[¶](https://docs.python.org/3/library/select.html#select.poll "Link to this definition")

Returns a polling object, which supports registering and unregistering file descriptors, and then polling them for I/O events; see section [Polling objects](https://docs.python.org/3/library/select.html#poll-objects)
 below for the methods supported by polling objects.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

select.kqueue()[¶](https://docs.python.org/3/library/select.html#select.kqueue "Link to this definition")

Returns a kernel queue object; see section [Kqueue objects](https://docs.python.org/3/library/select.html#kqueue-objects)
 below for the methods supported by kqueue objects.

The new file descriptor is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance)
.

Changed in version 3.4: The new file descriptor is now non-inheritable.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: BSD, macOS.

select.kevent(_ident_, _filter\=KQ\_FILTER\_READ_, _flags\=KQ\_EV\_ADD_, _fflags\=0_, _data\=0_, _udata\=0_)[¶](https://docs.python.org/3/library/select.html#select.kevent "Link to this definition")

Returns a kernel event object; see section [Kevent objects](https://docs.python.org/3/library/select.html#kevent-objects)
 below for the methods supported by kevent objects.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: BSD, macOS.

select.select(_rlist_, _wlist_, _xlist_, _timeout\=None_)[¶](https://docs.python.org/3/library/select.html#select.select "Link to this definition")

This is a straightforward interface to the Unix `select()` system call. The first three arguments are iterables of ‘waitable objects’: either integers representing file descriptors or objects with a parameterless method named [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 returning such an integer:

*   _rlist_: wait until ready for reading
    
*   _wlist_: wait until ready for writing
    
*   _xlist_: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
    

Empty iterables are allowed, but acceptance of three empty iterables is platform-dependent. (It is known to work on Unix but not on Windows.) The optional _timeout_ argument specifies a time-out in seconds; it may be a non-integer to specify fractions of seconds. When the _timeout_ argument is omitted or `None`, the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.

The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

Among the acceptable object types in the iterables are Python [file objects](https://docs.python.org/3/glossary.html#term-file-object)
 (e.g. `sys.stdin`, or objects returned by [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
 or [`os.popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")
), socket objects returned by [`socket.socket()`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
. You may also define a _wrapper_ class yourself, as long as it has an appropriate [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method (that really returns a file descriptor, not just a random integer).

Note

File objects on Windows are not acceptable, but sockets are. On Windows, the underlying `select()` function is provided by the WinSock library, and does not handle file descriptors that don’t originate from WinSock.

Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale), instead of raising [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
.

Changed in version 3.15: Accepts any real number as _timeout_, not only integer or float.

select.PIPE\_BUF[¶](https://docs.python.org/3/library/select.html#select.PIPE_BUF "Link to this definition")

The minimum number of bytes which can be written without blocking to a pipe when the pipe has been reported as ready for writing by [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select")
, `poll()` or another interface in this module. This doesn’t apply to other kinds of file-like objects such as sockets.

This value is guaranteed by POSIX to be at least 512.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix

Added in version 3.2.

`/dev/poll` polling objects[¶](https://docs.python.org/3/library/select.html#dev-poll-polling-objects "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

Solaris and derivatives have `/dev/poll`. While `select()` is _O_(_highest file descriptor_) and `poll()` is _O_(_number of file descriptors_), `/dev/poll` is _O_(_active file descriptors_).

`/dev/poll` behaviour is very close to the standard `poll()` object.

devpoll.close()[¶](https://docs.python.org/3/library/select.html#select.devpoll.close "Link to this definition")

Close the file descriptor of the polling object.

Added in version 3.4.

devpoll.closed[¶](https://docs.python.org/3/library/select.html#select.devpoll.closed "Link to this definition")

`True` if the polling object is closed.

Added in version 3.4.

devpoll.fileno()[¶](https://docs.python.org/3/library/select.html#select.devpoll.fileno "Link to this definition")

Return the file descriptor number of the polling object.

Added in version 3.4.

devpoll.register(_fd_\[, _eventmask_\])[¶](https://docs.python.org/3/library/select.html#select.devpoll.register "Link to this definition")

Register a file descriptor with the polling object. Future calls to the [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll")
 method will then check whether the file descriptor has any pending I/O events. _fd_ can be either an integer, or an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method that returns an integer. File objects implement `fileno()`, so they can also be used as the argument.

_eventmask_ is an optional bitmask describing the type of events you want to check for. The constants are the same as with `poll()` object. The default value is a combination of the constants `POLLIN`, `POLLPRI`, and `POLLOUT`.

Warning

Registering a file descriptor that’s already registered is not an error, but the result is undefined. The appropriate action is to unregister or modify it first. This is an important difference compared with `poll()`.

devpoll.modify(_fd_\[, _eventmask_\])[¶](https://docs.python.org/3/library/select.html#select.devpoll.modify "Link to this definition")

This method does an [`unregister()`](https://docs.python.org/3/library/select.html#select.devpoll.unregister "select.devpoll.unregister")
 followed by a [`register()`](https://docs.python.org/3/library/select.html#select.devpoll.register "select.devpoll.register")
. It is (a bit) more efficient than doing the same explicitly.

devpoll.unregister(_fd_)[¶](https://docs.python.org/3/library/select.html#select.devpoll.unregister "Link to this definition")

Remove a file descriptor being tracked by a polling object. Just like the [`register()`](https://docs.python.org/3/library/select.html#select.devpoll.register "select.devpoll.register")
 method, _fd_ can be an integer or an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method that returns an integer.

Attempting to remove a file descriptor that was never registered is safely ignored.

devpoll.poll(\[_timeout_\])[¶](https://docs.python.org/3/library/select.html#select.devpoll.poll "Link to this definition")

Polls the set of registered file descriptors, and returns a possibly empty list containing `(fd, event)` 2-tuples for the descriptors that have events or errors to report. _fd_ is the file descriptor, and _event_ is a bitmask with bits set for the reported events for that descriptor — `POLLIN` for waiting input, `POLLOUT` to indicate that the descriptor can be written to, and so forth. An empty list indicates that the call timed out and no file descriptors had any events to report. If _timeout_ is given, it specifies the length of time in milliseconds which the system will wait for events before returning. If _timeout_ is omitted, -1, or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
, the call will block until there is an event for this poll object.

Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale), instead of raising [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
.

Changed in version 3.15: Accepts any real number as _timeout_, not only integer or float.

Edge and level trigger polling (epoll) objects[¶](https://docs.python.org/3/library/select.html#edge-and-level-trigger-polling-epoll-objects "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

> [https://linux.die.net/man/4/epoll](https://linux.die.net/man/4/epoll)
> 
> The _eventmask_ is a bit mask using the following constants:
> 
> | Constant | Meaning |
> | --- | --- |
> | `EPOLLIN` | Available for read. |
> | `EPOLLOUT` | Available for write. |
> | `EPOLLPRI` | Urgent data for read. |
> | `EPOLLERR` | Error condition happened on the associated fd. |
> | `EPOLLHUP` | Hang up happened on the associated fd. |
> | `EPOLLET` | Set Edge Trigger behavior, the default is Level Trigger behavior. |
> | `EPOLLONESHOT` | Set one-shot behavior. After one event is pulled out, the fd is internally disabled. |
> | `EPOLLEXCLUSIVE` | Wake only one epoll object when the associated fd has an event. The default (if this flag is not set) is to wake all epoll objects polling on an fd. |
> | `EPOLLRDHUP` | Stream socket peer closed connection or shut down writing half of connection. |
> | `EPOLLRDNORM` | Equivalent to `EPOLLIN` |
> | `EPOLLRDBAND` | Priority data band can be read. |
> | `EPOLLWRNORM` | Equivalent to `EPOLLOUT`. |
> | `EPOLLWRBAND` | Priority data may be written. |
> | `EPOLLMSG` | Ignored. |
> | `EPOLLWAKEUP` | Prevents sleep during event waiting. |
> 
> Added in version 3.6: `EPOLLEXCLUSIVE` was added. It’s only supported by Linux Kernel 4.5 or later.
> 
> Added in version 3.14: `EPOLLWAKEUP` was added. It’s only supported by Linux Kernel 3.5 or later.

epoll.close()[¶](https://docs.python.org/3/library/select.html#select.epoll.close "Link to this definition")

Close the control file descriptor of the epoll object.

epoll.closed[¶](https://docs.python.org/3/library/select.html#select.epoll.closed "Link to this definition")

`True` if the epoll object is closed.

epoll.fileno()[¶](https://docs.python.org/3/library/select.html#select.epoll.fileno "Link to this definition")

Return the file descriptor number of the control fd.

epoll.fromfd(_fd_)[¶](https://docs.python.org/3/library/select.html#select.epoll.fromfd "Link to this definition")

Create an epoll object from a given file descriptor.

epoll.register(_fd_\[, _eventmask_\])[¶](https://docs.python.org/3/library/select.html#select.epoll.register "Link to this definition")

Register a file descriptor _fd_ with the epoll object.

epoll.modify(_fd_, _eventmask_)[¶](https://docs.python.org/3/library/select.html#select.epoll.modify "Link to this definition")

Modify a registered file descriptor _fd_.

epoll.unregister(_fd_)[¶](https://docs.python.org/3/library/select.html#select.epoll.unregister "Link to this definition")

Remove a registered file descriptor from the epoll object.

Changed in version 3.9: The method no longer ignores the [`EBADF`](https://docs.python.org/3/library/errno.html#errno.EBADF "errno.EBADF")
 error.

epoll.poll(_timeout\=None_, _maxevents\=\-1_)[¶](https://docs.python.org/3/library/select.html#select.epoll.poll "Link to this definition")

Wait for events. If _timeout_ is given, it specifies the length of time in seconds (may be non-integer) which the system will wait for events before returning.

Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale), instead of raising [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
.

Changed in version 3.15: Accepts any real number as _timeout_, not only integer or float.

Polling objects[¶](https://docs.python.org/3/library/select.html#polling-objects "Link to this heading")

---------------------------------------------------------------------------------------------------------

The `poll()` system call, supported on most Unix systems, provides better scalability for network servers that service many, many clients at the same time. `poll()` scales better because the system call only requires listing the file descriptors of interest, while `select()` builds a bitmap, turns on bits for the fds of interest, and then afterward the whole bitmap has to be linearly scanned again. `select()` is _O_(_highest file descriptor_), while `poll()` is _O_(_number of file descriptors_).

poll.register(_fd_\[, _eventmask_\])[¶](https://docs.python.org/3/library/select.html#select.poll.register "Link to this definition")

Register a file descriptor with the polling object. Future calls to the [`poll()`](https://docs.python.org/3/library/select.html#select.poll "select.poll")
 method will then check whether the file descriptor has any pending I/O events. _fd_ can be either an integer, or an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method that returns an integer. File objects implement `fileno()`, so they can also be used as the argument.

_eventmask_ is an optional bitmask describing the type of events you want to check for, and can be a combination of the constants `POLLIN`, `POLLPRI`, and `POLLOUT`, described in the table below. If not specified, the default value used will check for all 3 types of events.

| Constant | Meaning |
| --- | --- |
| `POLLIN` | There is data to read. |
| `POLLPRI` | There is urgent data to read. |
| `POLLOUT` | Ready for output: writing will not block. |
| `POLLERR` | Error condition of some sort. |
| `POLLHUP` | Hung up. |
| `POLLRDHUP` | Stream socket peer closed connection, or shut down writing half of connection. |
| `POLLNVAL` | Invalid request: descriptor not open. |

Registering a file descriptor that’s already registered is not an error, and has the same effect as registering the descriptor exactly once.

poll.modify(_fd_, _eventmask_)[¶](https://docs.python.org/3/library/select.html#select.poll.modify "Link to this definition")

Modifies an already registered fd. This has the same effect as `register(fd, eventmask)`. Attempting to modify a file descriptor that was never registered causes an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 exception with errno `ENOENT` to be raised.

poll.unregister(_fd_)[¶](https://docs.python.org/3/library/select.html#select.poll.unregister "Link to this definition")

Remove a file descriptor being tracked by a polling object. Just like the [`register()`](https://docs.python.org/3/library/select.html#select.poll.register "select.poll.register")
 method, _fd_ can be an integer or an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method that returns an integer.

Attempting to remove a file descriptor that was never registered causes a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 exception to be raised.

poll.poll(\[_timeout_\])[¶](https://docs.python.org/3/library/select.html#select.poll.poll "Link to this definition")

Polls the set of registered file descriptors, and returns a possibly empty list containing `(fd, event)` 2-tuples for the descriptors that have events or errors to report. _fd_ is the file descriptor, and _event_ is a bitmask with bits set for the reported events for that descriptor — `POLLIN` for waiting input, `POLLOUT` to indicate that the descriptor can be written to, and so forth. An empty list indicates that the call timed out and no file descriptors had any events to report. If _timeout_ is given, it specifies the length of time in milliseconds which the system will wait for events before returning. If _timeout_ is omitted, negative, or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
, the call will block until there is an event for this poll object.

Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale), instead of raising [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
.

Changed in version 3.15: Accepts any real number as _timeout_, not only integer or float. If `ppoll()` function is available, _timeout_ has a resolution of `1` ns (`1e-6` ms) instead of `1` ms.

Kqueue objects[¶](https://docs.python.org/3/library/select.html#kqueue-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------

kqueue.close()[¶](https://docs.python.org/3/library/select.html#select.kqueue.close "Link to this definition")

Close the control file descriptor of the kqueue object.

kqueue.closed[¶](https://docs.python.org/3/library/select.html#select.kqueue.closed "Link to this definition")

`True` if the kqueue object is closed.

kqueue.fileno()[¶](https://docs.python.org/3/library/select.html#select.kqueue.fileno "Link to this definition")

Return the file descriptor number of the control fd.

kqueue.fromfd(_fd_)[¶](https://docs.python.org/3/library/select.html#select.kqueue.fromfd "Link to this definition")

Create a kqueue object from a given file descriptor.

kqueue.control(_changelist_, _max\_events_\[, _timeout_\]) → eventlist[¶](https://docs.python.org/3/library/select.html#select.kqueue.control "Link to this definition")

Low level interface to kevent

*   changelist must be an iterable of kevent objects or `None`
    
*   max\_events must be 0 or a positive integer
    
*   timeout in seconds (non-integers are possible); the default is `None`, to wait forever
    

Changed in version 3.5: The function is now retried with a recomputed timeout when interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale), instead of raising [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
.

Changed in version 3.15: Accepts any real number as _timeout_, not only integer or float.

Kevent objects[¶](https://docs.python.org/3/library/select.html#kevent-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------

[https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2](https://man.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2)

kevent.ident[¶](https://docs.python.org/3/library/select.html#select.kevent.ident "Link to this definition")

Value used to identify the event. The interpretation depends on the filter but it’s usually the file descriptor. In the constructor ident can either be an int or an object with a [`fileno()`](https://docs.python.org/3/library/io.html#io.IOBase.fileno "io.IOBase.fileno")
 method. kevent stores the integer internally.

kevent.filter[¶](https://docs.python.org/3/library/select.html#select.kevent.filter "Link to this definition")

Name of the kernel filter.

| Constant | Meaning |
| --- | --- |
| `KQ_FILTER_READ` | Takes a descriptor and returns whenever there is data available to read. |
| `KQ_FILTER_WRITE` | Takes a descriptor and returns whenever there is data available to write. |
| `KQ_FILTER_AIO` | AIO requests. |
| `KQ_FILTER_VNODE` | Returns when one or more of the requested events watched in _fflags_ occurs. |
| `KQ_FILTER_PROC` | Watch for events on a process ID. |
| `KQ_FILTER_NETDEV` | Watch for events on a network device (not available on macOS). |
| `KQ_FILTER_SIGNAL` | Returns whenever the watched signal is delivered to the process. |
| `KQ_FILTER_TIMER` | Establishes an arbitrary timer. |

kevent.flags[¶](https://docs.python.org/3/library/select.html#select.kevent.flags "Link to this definition")

Filter action.

| Constant | Meaning |
| --- | --- |
| `KQ_EV_ADD` | Adds or modifies an event. |
| `KQ_EV_DELETE` | Removes an event from the queue. |
| `KQ_EV_ENABLE` | Permits control() to return the event. |
| `KQ_EV_DISABLE` | Disables event. |
| `KQ_EV_ONESHOT` | Removes event after first occurrence. |
| `KQ_EV_CLEAR` | Reset the state after an event is retrieved. |
| `KQ_EV_SYSFLAGS` | Internal event. |
| `KQ_EV_FLAG1` | Internal event. |
| `KQ_EV_EOF` | Filter-specific EOF condition. |
| `KQ_EV_ERROR` | See return values. |

kevent.fflags[¶](https://docs.python.org/3/library/select.html#select.kevent.fflags "Link to this definition")

Filter-specific flags.

`KQ_FILTER_READ` and `KQ_FILTER_WRITE` filter flags:

| Constant | Meaning |
| --- | --- |
| `KQ_NOTE_LOWAT` | Low water mark of a socket buffer. |

`KQ_FILTER_VNODE` filter flags:

| Constant | Meaning |
| --- | --- |
| `KQ_NOTE_DELETE` | _unlink()_ was called. |
| `KQ_NOTE_WRITE` | A write occurred. |
| `KQ_NOTE_EXTEND` | The file was extended. |
| `KQ_NOTE_ATTRIB` | An attribute was changed. |
| `KQ_NOTE_LINK` | The link count has changed. |
| `KQ_NOTE_RENAME` | The file was renamed. |
| `KQ_NOTE_REVOKE` | Access to the file was revoked. |

`KQ_FILTER_PROC` filter flags:

| Constant | Meaning |
| --- | --- |
| `KQ_NOTE_EXIT` | The process has exited. |
| `KQ_NOTE_FORK` | The process has called _fork()_. |
| `KQ_NOTE_EXEC` | The process has executed a new process. |
| `KQ_NOTE_PCTRLMASK` | Internal filter flag. |
| `KQ_NOTE_PDATAMASK` | Internal filter flag. |
| `KQ_NOTE_TRACK` | Follow a process across _fork()_. |
| `KQ_NOTE_CHILD` | Returned on the child process for _NOTE\_TRACK_. |
| `KQ_NOTE_TRACKERR` | Unable to attach to a child. |

`KQ_FILTER_NETDEV` filter flags (not available on macOS):

| Constant | Meaning |
| --- | --- |
| `KQ_NOTE_LINKUP` | Link is up. |
| `KQ_NOTE_LINKDOWN` | Link is down. |
| `KQ_NOTE_LINKINV` | Link state is invalid. |

kevent.data[¶](https://docs.python.org/3/library/select.html#select.kevent.data "Link to this definition")

Filter-specific data.

kevent.udata[¶](https://docs.python.org/3/library/select.html#select.kevent.udata "Link to this definition")

User-defined value.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html#)
    *   [`/dev/poll` polling objects](https://docs.python.org/3/library/select.html#dev-poll-polling-objects)
        
    *   [Edge and level trigger polling (epoll) objects](https://docs.python.org/3/library/select.html#edge-and-level-trigger-polling-epoll-objects)
        
    *   [Polling objects](https://docs.python.org/3/library/select.html#polling-objects)
        
    *   [Kqueue objects](https://docs.python.org/3/library/select.html#kqueue-objects)
        
    *   [Kevent objects](https://docs.python.org/3/library/select.html#kevent-objects)
        

#### Previous topic

[`ssl` — TLS/SSL wrapper for socket objects](https://docs.python.org/3/library/ssl.html "previous chapter")

#### Next topic

[`selectors` — High-level I/O multiplexing](https://docs.python.org/3/library/selectors.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=select+%E2%80%94+Waiting+for+I%2FO+completion&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fselect.html&pagesource=library%2Fselect.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/select.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/selectors.html "selectors — High-level I/O multiplexing")
     |
*   [previous](https://docs.python.org/3/library/ssl.html "ssl — TLS/SSL wrapper for socket objects")
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
*   [`select` — Waiting for I/O completion](https://docs.python.org/3/library/select.html)
    
*    
    
    |
*   Theme Auto Light Dark |