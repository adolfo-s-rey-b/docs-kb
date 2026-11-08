### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/syslog.html "syslog — Unix syslog library routines")
     |
*   [previous](https://docs.python.org/3/library/fcntl.html "fcntl — The fcntl and ioctl system calls")
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
*   [`resource` — Resource usage information](https://docs.python.org/3/library/resource.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`resource` — Resource usage information[¶](https://docs.python.org/3/library/resource.html#module-resource "Link to this heading")

===================================================================================================================================

* * *

This module provides basic mechanisms for measuring and controlling system resources utilized by a program.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI.

Symbolic constants are used to specify particular system resources and to request usage information about either the current process or its children.

An [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised on syscall failure.

exception resource.error[¶](https://docs.python.org/3/library/resource.html#resource.error "Link to this definition")

A deprecated alias of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

Changed in version 3.3: Following [**PEP 3151**](https://peps.python.org/pep-3151/)
, this class was made an alias of [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

Resource Limits[¶](https://docs.python.org/3/library/resource.html#resource-limits "Link to this heading")

-----------------------------------------------------------------------------------------------------------

Resources usage can be limited using the [`setrlimit()`](https://docs.python.org/3/library/resource.html#resource.setrlimit "resource.setrlimit")
 function described below. Each resource is controlled by a pair of limits: a soft limit and a hard limit. The soft limit is the current limit, and may be lowered or raised by a process over time. The soft limit can never exceed the hard limit. The hard limit can be lowered to any value greater than the soft limit, but not raised. (Only processes with the effective UID of the super-user can raise a hard limit.)

The specific resources that can be limited are system dependent. They are described in the _[getrlimit(2)](https://manpages.debian.org/getrlimit(2))
_ man page. The resources listed below are supported when the underlying operating system supports them; resources which cannot be checked or controlled by the operating system are not defined in this module for those platforms.

resource.RLIM\_INFINITY[¶](https://docs.python.org/3/library/resource.html#resource.RLIM_INFINITY "Link to this definition")

Constant used to represent the limit for an unlimited resource.

Changed in version 3.15: It is now always positive. Previously, it could be negative, such as -1 or -3.

resource.RLIM\_SAVED\_CUR[¶](https://docs.python.org/3/library/resource.html#resource.RLIM_SAVED_CUR "Link to this definition")

resource.RLIM\_SAVED\_MAX[¶](https://docs.python.org/3/library/resource.html#resource.RLIM_SAVED_MAX "Link to this definition")

Constants used to represent the soft and hard limit values if they cannot be represented in the `rlim_t` value in C. Can be equal to [`RLIM_INFINITY`](https://docs.python.org/3/library/resource.html#resource.RLIM_INFINITY "resource.RLIM_INFINITY")
.

Added in version 3.15.

resource.getrlimit(_resource_)[¶](https://docs.python.org/3/library/resource.html#resource.getrlimit "Link to this definition")

Returns a tuple `(soft, hard)` with the current soft and hard limits of _resource_. Raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if an invalid resource is specified, or [`error`](https://docs.python.org/3/library/resource.html#resource.error "resource.error")
 if the underlying system call fails unexpectedly.

resource.setrlimit(_resource_, _limits_)[¶](https://docs.python.org/3/library/resource.html#resource.setrlimit "Link to this definition")

Sets new limits of consumption of _resource_. The _limits_ argument must be a tuple `(soft, hard)` of two integers describing the new limits. A value of [`RLIM_INFINITY`](https://docs.python.org/3/library/resource.html#resource.RLIM_INFINITY "resource.RLIM_INFINITY")
 can be used to request a limit that is unlimited.

Raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if an invalid resource is specified, if the new soft limit exceeds the hard limit, or if a process tries to raise its hard limit. Specifying a limit of [`RLIM_INFINITY`](https://docs.python.org/3/library/resource.html#resource.RLIM_INFINITY "resource.RLIM_INFINITY")
 when the hard or system limit for that resource is not unlimited will result in a `ValueError`. A process with the effective UID of super-user can request any valid limit value, including unlimited, but `ValueError` will still be raised if the requested limit exceeds the system imposed limit.

`setrlimit` may also raise [`error`](https://docs.python.org/3/library/resource.html#resource.error "resource.error")
 if the underlying system call fails.

VxWorks only supports setting [`RLIMIT_NOFILE`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_NOFILE "resource.RLIMIT_NOFILE")
.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `resource.setrlimit` with arguments `resource`, `limits`.

resource.prlimit(_pid_, _resource_\[, _limits_\])[¶](https://docs.python.org/3/library/resource.html#resource.prlimit "Link to this definition")

Combines [`setrlimit()`](https://docs.python.org/3/library/resource.html#resource.setrlimit "resource.setrlimit")
 and [`getrlimit()`](https://docs.python.org/3/library/resource.html#resource.getrlimit "resource.getrlimit")
 in one function and supports to get and set the resources limits of an arbitrary process. If _pid_ is 0, then the call applies to the current process. _resource_ and _limits_ have the same meaning as in `setrlimit()`, except that _limits_ is optional.

When _limits_ is not given the function returns the _resource_ limit of the process _pid_. When _limits_ is given the _resource_ limit of the process is set and the former resource limit is returned.

Raises [`ProcessLookupError`](https://docs.python.org/3/builtins/exceptions.html#ProcessLookupError "ProcessLookupError")
 when _pid_ can’t be found and [`PermissionError`](https://docs.python.org/3/builtins/exceptions.html#PermissionError "PermissionError")
 when the user doesn’t have `CAP_SYS_RESOURCE` for the process.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `resource.prlimit` with arguments `pid`, `resource`, `limits`.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.36 with glibc >= 2.13.

Added in version 3.4.

These symbols define resources whose consumption can be controlled using the [`setrlimit()`](https://docs.python.org/3/library/resource.html#resource.setrlimit "resource.setrlimit")
 and [`getrlimit()`](https://docs.python.org/3/library/resource.html#resource.getrlimit "resource.getrlimit")
 functions described below. The values of these symbols are exactly the constants used by C programs.

The Unix man page for _[getrlimit(2)](https://manpages.debian.org/getrlimit(2))
_ lists the available resources. Note that not all systems use the same symbol or same value to denote the same resource. This module does not attempt to mask platform differences — symbols not defined for a platform will not be available from this module on that platform.

resource.RLIMIT\_CORE[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_CORE "Link to this definition")

The maximum size (in bytes) of a core file that the current process can create. This may result in the creation of a partial core file if a larger core would be required to contain the entire process image.

resource.RLIMIT\_CPU[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_CPU "Link to this definition")

The maximum amount of processor time (in seconds) that a process can use. If this limit is exceeded, a [`SIGXCPU`](https://docs.python.org/3/library/signal.html#signal.SIGXCPU "signal.SIGXCPU")
 signal is sent to the process. (See the [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")
 module documentation for information about how to catch this signal and do something useful, e.g. flush open files to disk.)

resource.RLIMIT\_FSIZE[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_FSIZE "Link to this definition")

The maximum size of a file which the process may create.

resource.RLIMIT\_DATA[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_DATA "Link to this definition")

The maximum size (in bytes) of the process’s heap.

resource.RLIMIT\_STACK[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_STACK "Link to this definition")

The maximum size (in bytes) of the call stack for the current process. This only affects the stack of the main thread in a multi-threaded process.

resource.RLIMIT\_RSS[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_RSS "Link to this definition")

The maximum resident set size that should be made available to the process.

resource.RLIMIT\_NPROC[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_NPROC "Link to this definition")

The maximum number of processes the current process may create.

resource.RLIMIT\_NOFILE[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_NOFILE "Link to this definition")

The maximum number of open file descriptors for the current process.

resource.RLIMIT\_OFILE[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_OFILE "Link to this definition")

The BSD name for [`RLIMIT_NOFILE`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_NOFILE "resource.RLIMIT_NOFILE")
.

resource.RLIMIT\_MEMLOCK[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_MEMLOCK "Link to this definition")

The maximum address space which may be locked in memory.

resource.RLIMIT\_VMEM[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_VMEM "Link to this definition")

The largest area of mapped memory which the process may occupy. Usually an alias of [`RLIMIT_AS`](https://docs.python.org/3/library/resource.html#resource.RLIMIT_AS "resource.RLIMIT_AS")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Solaris, FreeBSD, NetBSD.

resource.RLIMIT\_AS[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_AS "Link to this definition")

The maximum area (in bytes) of address space which may be taken by the process.

resource.RLIMIT\_MSGQUEUE[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_MSGQUEUE "Link to this definition")

The number of bytes that can be allocated for POSIX message queues.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.8.

Added in version 3.4.

resource.RLIMIT\_NICE[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_NICE "Link to this definition")

The ceiling for the process’s nice level (calculated as 20 - rlim\_cur).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.12.

Added in version 3.4.

resource.RLIMIT\_RTPRIO[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_RTPRIO "Link to this definition")

The ceiling of the real-time priority.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.12.

Added in version 3.4.

resource.RLIMIT\_RTTIME[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_RTTIME "Link to this definition")

The time limit (in microseconds) on CPU time that a process can spend under real-time scheduling without making a blocking syscall.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.25.

Added in version 3.4.

resource.RLIMIT\_SIGPENDING[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_SIGPENDING "Link to this definition")

The number of signals which the process may queue.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.8.

Added in version 3.4.

resource.RLIMIT\_SBSIZE[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_SBSIZE "Link to this definition")

The maximum size (in bytes) of socket buffer usage for this user. This limits the amount of network memory, and hence the amount of mbufs, that this user may hold at any time.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD, NetBSD.

Added in version 3.4.

resource.RLIMIT\_SWAP[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_SWAP "Link to this definition")

The maximum size (in bytes) of the swap space that may be reserved or used by all of this user id’s processes. This limit is enforced only if bit 1 of the vm.overcommit sysctl is set. Please see [tuning(7)](https://man.freebsd.org/cgi/man.cgi?query=tuning&sektion=7)
 for a complete description of this sysctl.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD >= 8.

Added in version 3.4.

resource.RLIMIT\_NPTS[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_NPTS "Link to this definition")

The maximum number of pseudo-terminals created by this user id.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD >= 8.

Added in version 3.4.

resource.RLIMIT\_KQUEUES[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_KQUEUES "Link to this definition")

The maximum number of kqueues this user id is allowed to create.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD >= 11.

Added in version 3.10.

resource.RLIMIT\_NTHR[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_NTHR "Link to this definition")

The maximum number of threads for this user id, not counting the main and kernel threads.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: NetBSD >= 7.0.

Added in version 3.15.

resource.RLIMIT\_PIPEBUF[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_PIPEBUF "Link to this definition")

The maximum total size of in-kernel buffers for bi-directional pipes/fifos that this user id is allowed to consume.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD >= 14.2.

Added in version 3.15.

resource.RLIMIT\_THREADS[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_THREADS "Link to this definition")

The maximum number of threads each process can create.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: AIX.

Added in version 3.15.

resource.RLIMIT\_UMTXP[¶](https://docs.python.org/3/library/resource.html#resource.RLIMIT_UMTXP "Link to this definition")

The limit of the number of process-shared Posix thread library objects allocated by user id.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD >= 11.

Added in version 3.15.

Resource Usage[¶](https://docs.python.org/3/library/resource.html#resource-usage "Link to this heading")

---------------------------------------------------------------------------------------------------------

These functions are used to retrieve resource usage information:

resource.getrusage(_who_)[¶](https://docs.python.org/3/library/resource.html#resource.getrusage "Link to this definition")

This function returns an object that describes the resources consumed by either the current process or its children, as specified by the _who_ parameter. The _who_ parameter should be specified using one of the `RUSAGE_*` constants described below.

A simple example:

Copy

from resource import \*
import time

\# a non CPU-bound task
time.sleep(3)
print(getrusage(RUSAGE\_SELF))

\# a CPU-bound task
for i in range(10 \*\* 8):
   \_ \= 1 + 1
print(getrusage(RUSAGE\_SELF))

The fields of the return value each describe how a particular system resource has been used, e.g. amount of time spent running in user mode or number of times the process was swapped out of main memory. Some values are dependent on the clock tick interval, e.g. the amount of memory the process is using.

For backward compatibility, the return value is also accessible as a tuple of 16 elements.

The fields `ru_utime` and `ru_stime` of the return value are floating-point values representing the amount of time spent executing in user mode and the amount of time spent executing in system mode, respectively. The remaining values are integers. Consult the _[getrusage(2)](https://manpages.debian.org/getrusage(2))
_ man page for detailed information about these values. A brief summary is presented here:

| Index | Field | Resource |
| --- | --- | --- |
| `0` | `ru_utime` | time in user mode (float seconds) |
| `1` | `ru_stime` | time in system mode (float seconds) |
| `2` | `ru_maxrss` | maximum resident set size |
| `3` | `ru_ixrss` | shared memory size |
| `4` | `ru_idrss` | unshared memory size |
| `5` | `ru_isrss` | unshared stack size |
| `6` | `ru_minflt` | page faults not requiring I/O |
| `7` | `ru_majflt` | page faults requiring I/O |
| `8` | `ru_nswap` | number of swap outs |
| `9` | `ru_inblock` | block input operations |
| `10` | `ru_oublock` | block output operations |
| `11` | `ru_msgsnd` | messages sent |
| `12` | `ru_msgrcv` | messages received |
| `13` | `ru_nsignals` | signals received |
| `14` | `ru_nvcsw` | voluntary context switches |
| `15` | `ru_nivcsw` | involuntary context switches |

This function will raise a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 if an invalid _who_ parameter is specified. It may also raise [`error`](https://docs.python.org/3/library/resource.html#resource.error "resource.error")
 exception in unusual circumstances.

resource.getpagesize()[¶](https://docs.python.org/3/library/resource.html#resource.getpagesize "Link to this definition")

Returns the number of bytes in a system page. (This need not be the same as the hardware page size.)

The following `RUSAGE_*` symbols are passed to the [`getrusage()`](https://docs.python.org/3/library/resource.html#resource.getrusage "resource.getrusage")
 function to specify which processes information should be provided for.

resource.RUSAGE\_SELF[¶](https://docs.python.org/3/library/resource.html#resource.RUSAGE_SELF "Link to this definition")

Pass to [`getrusage()`](https://docs.python.org/3/library/resource.html#resource.getrusage "resource.getrusage")
 to request resources consumed by the calling process, which is the sum of resources used by all threads in the process.

resource.RUSAGE\_CHILDREN[¶](https://docs.python.org/3/library/resource.html#resource.RUSAGE_CHILDREN "Link to this definition")

Pass to [`getrusage()`](https://docs.python.org/3/library/resource.html#resource.getrusage "resource.getrusage")
 to request resources consumed by child processes of the calling process which have been terminated and waited for.

resource.RUSAGE\_BOTH[¶](https://docs.python.org/3/library/resource.html#resource.RUSAGE_BOTH "Link to this definition")

Pass to [`getrusage()`](https://docs.python.org/3/library/resource.html#resource.getrusage "resource.getrusage")
 to request resources consumed by both the current process and child processes. May not be available on all systems.

resource.RUSAGE\_THREAD[¶](https://docs.python.org/3/library/resource.html#resource.RUSAGE_THREAD "Link to this definition")

Pass to [`getrusage()`](https://docs.python.org/3/library/resource.html#resource.getrusage "resource.getrusage")
 to request resources consumed by the current thread. May not be available on all systems.

Added in version 3.2.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`resource` — Resource usage information](https://docs.python.org/3/library/resource.html#)
    *   [Resource Limits](https://docs.python.org/3/library/resource.html#resource-limits)
        
    *   [Resource Usage](https://docs.python.org/3/library/resource.html#resource-usage)
        

#### Previous topic

[`fcntl` — The `fcntl` and `ioctl` system calls](https://docs.python.org/3/library/fcntl.html "previous chapter")

#### Next topic

[`syslog` — Unix syslog library routines](https://docs.python.org/3/library/syslog.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=resource+%E2%80%94+Resource+usage+information&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fresource.html&pagesource=library%2Fresource.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/resource.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/syslog.html "syslog — Unix syslog library routines")
     |
*   [previous](https://docs.python.org/3/library/fcntl.html "fcntl — The fcntl and ioctl system calls")
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
*   [`resource` — Resource usage information](https://docs.python.org/3/library/resource.html)
    
*    
    
    |
*   Theme Auto Light Dark |