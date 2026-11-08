### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/logging.html "logging — Logging facility for Python")
     |
*   [previous](https://docs.python.org/3/library/io.html "io — Core tools for working with streams")
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
*   [Generic Operating System Services](https://docs.python.org/3/library/allos.html)
     »
*   [`time` — Time access and conversions](https://docs.python.org/3/library/time.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`time` — Time access and conversions[¶](https://docs.python.org/3/library/time.html#module-time "Link to this heading")

========================================================================================================================

* * *

This module provides various time-related functions. For related functionality, see also the [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
 and [`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.")
 modules.

Although this module is always available, not all functions are available on all platforms. Most of the functions defined in this module call platform C library functions with the same name. It may sometimes be helpful to consult the platform documentation, because the semantics of these functions varies among platforms.

An explanation of some terminology and conventions is in order.

*   The _epoch_ is the point where the time starts, the return value of `time.gmtime(0)`. It is January 1, 1970, 00:00:00 (UTC) on all platforms.
    

*   The term _seconds since the epoch_ refers to the total number of elapsed seconds since the epoch, typically excluding [leap seconds](https://en.wikipedia.org/wiki/Leap_second)
    . Leap seconds are excluded from this total on all POSIX-compliant platforms.
    

*   The functions in this module may not handle dates and times before the [epoch](https://docs.python.org/3/library/time.html#epoch)
     or far in the future. The cut-off point in the future is determined by the C library; for 32-bit systems, it is typically in 2038.
    

*   Function [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime")
     can parse 2-digit years when given `%y` format code. When 2-digit years are parsed, they are converted according to the POSIX and ISO C standards: values 69–99 are mapped to 1969–1999, and values 0–68 are mapped to 2000–2068.
    

*   UTC is [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)
     and superseded [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time)
     or GMT as the basis of international timekeeping. The acronym UTC is not a mistake but conforms to an earlier, language-agnostic naming scheme for time standards such as UT0, UT1, and UT2.
    

*   DST is Daylight Saving Time, an adjustment of the timezone by (usually) one hour during part of the year. DST rules are magic (determined by local law) and can change from year to year. The C library has a table containing the local rules (often it is read from a system file for flexibility) and is the only source of True Wisdom in this respect.
    
*   The precision of the various real-time functions may be less than suggested by the units in which their value or argument is expressed. E.g. on most Unix systems, the clock “ticks” only 50 or 100 times a second.
    
*   On the other hand, the precision of [`time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
     and [`sleep()`](https://docs.python.org/3/library/time.html#time.sleep "time.sleep")
     is better than their Unix equivalents: times are expressed as floating-point numbers, `time()` returns the most accurate time available (using Unix `gettimeofday()` where available), and `sleep()` will accept a time with a nonzero fraction (Unix `select()` is used to implement this, where available).
    
*   The time value as returned by [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")
    , [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
    , and [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime")
    , and accepted by [`asctime()`](https://docs.python.org/3/library/time.html#time.asctime "time.asctime")
    , [`mktime()`](https://docs.python.org/3/library/time.html#time.mktime "time.mktime")
     and [`strftime()`](https://docs.python.org/3/library/time.html#time.strftime "time.strftime")
    , is a sequence of 9 integers. The return values of `gmtime()`, `localtime()`, and `strptime()` also offer attribute names for individual fields.
    
    See [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")
     for a description of these objects.
    
    Changed in version 3.3: The [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")
     type was extended to provide the [`tm_gmtoff`](https://docs.python.org/3/library/time.html#time.struct_time.tm_gmtoff "time.struct_time.tm_gmtoff")
     and [`tm_zone`](https://docs.python.org/3/library/time.html#time.struct_time.tm_zone "time.struct_time.tm_zone")
     attributes when platform supports corresponding `struct tm` members.
    
    Changed in version 3.6: The [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")
     attributes [`tm_gmtoff`](https://docs.python.org/3/library/time.html#time.struct_time.tm_gmtoff "time.struct_time.tm_gmtoff")
     and [`tm_zone`](https://docs.python.org/3/library/time.html#time.struct_time.tm_zone "time.struct_time.tm_zone")
     are now available on all platforms.
    
*   Use the following functions to convert between time representations:
    
    | From | To  | Use |
    | --- | --- | --- |
    | seconds since the epoch | [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")<br> in UTC | [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime") |
    | seconds since the epoch | [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")<br> in local time | [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime") |
    | [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")<br> in UTC | seconds since the epoch | [`calendar.timegm()`](https://docs.python.org/3/library/calendar.html#calendar.timegm "calendar.timegm") |
    | [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")<br> in local time | seconds since the epoch | [`mktime()`](https://docs.python.org/3/library/time.html#time.mktime "time.mktime") |
    

Functions[¶](https://docs.python.org/3/library/time.html#functions "Link to this heading")

-------------------------------------------------------------------------------------------

time.asctime(\[_time\_tuple_\])[¶](https://docs.python.org/3/library/time.html#time.asctime "Link to this definition")

Convert a tuple or [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")
 representing a time as returned by [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")
 or [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
 to a string of the following form: `'Sun Jun 20 23:21:05 1993'`. The day field is two characters long and is space padded if the day is a single digit, for example: `'Wed Jun  9 04:26:40 1993'`.

If _time\_tuple_ is not provided, the current time as returned by [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
 is used. Locale information is not used by `asctime()`.

Note

Unlike the C function of the same name, `asctime()` does not add a trailing newline.

time.pthread\_getcpuclockid(_thread\_id_, _/_)[¶](https://docs.python.org/3/library/time.html#time.pthread_getcpuclockid "Link to this definition")

Return the _clk\_id_ of the thread-specific CPU-time clock for the specified _thread\_id_.

Use [`threading.get_ident()`](https://docs.python.org/3/library/threading.html#threading.get_ident "threading.get_ident")
 or the [`ident`](https://docs.python.org/3/library/threading.html#threading.Thread.ident "threading.Thread.ident")
 attribute of [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread")
 objects to get a suitable value for _thread\_id_.

Warning

Passing an invalid or expired _thread\_id_ may result in undefined behavior, such as segmentation fault.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix

See the man page for _[pthread\_getcpuclockid(3)](https://manpages.debian.org/pthread_getcpuclockid(3))
_ for further information.

Added in version 3.7.

time.clock\_getres(_clk\_id_, _/_)[¶](https://docs.python.org/3/library/time.html#time.clock_getres "Link to this definition")

Return the resolution (precision) of the specified clock _clk\_id_. Refer to [Clock ID Constants](https://docs.python.org/3/library/time.html#time-clock-id-constants)
 for a list of accepted values for _clk\_id_.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

time.clock\_gettime(_clk\_id_, _/_) → [float](https://docs.python.org/3/builtins/functions.html#float "float")
[¶](https://docs.python.org/3/library/time.html#time.clock_gettime "Link to this definition")

Return the time of the specified clock _clk\_id_. Refer to [Clock ID Constants](https://docs.python.org/3/library/time.html#time-clock-id-constants)
 for a list of accepted values for _clk\_id_.

Use [`clock_gettime_ns()`](https://docs.python.org/3/library/time.html#time.clock_gettime_ns "time.clock_gettime_ns")
 to avoid the precision loss caused by the [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 type.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

time.clock\_gettime\_ns(_clk\_id_, _/_) → [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/time.html#time.clock_gettime_ns "Link to this definition")

Similar to [`clock_gettime()`](https://docs.python.org/3/library/time.html#time.clock_gettime "time.clock_gettime")
 but return time as nanoseconds.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.7.

time.clock\_settime(_clk\_id_, _time_, _/_)[¶](https://docs.python.org/3/library/time.html#time.clock_settime "Link to this definition")

Set the time of the specified clock _clk\_id_. Currently, [`CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME")
 is the only accepted value for _clk\_id_.

Use [`clock_settime_ns()`](https://docs.python.org/3/library/time.html#time.clock_settime_ns "time.clock_settime_ns")
 to avoid the precision loss caused by the [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 type.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not Android, not iOS.

Added in version 3.3.

Changed in version 3.15: Accepts any real number as _time_, not only integer or float.

time.clock\_settime\_ns(_clk\_id_, _time: [int](https://docs.python.org/3/builtins/functions.html#int "int")
_, _/_)[¶](https://docs.python.org/3/library/time.html#time.clock_settime_ns "Link to this definition")

Similar to [`clock_settime()`](https://docs.python.org/3/library/time.html#time.clock_settime "time.clock_settime")
 but set time with nanoseconds.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not Android, not iOS.

Added in version 3.7.

time.ctime(_seconds\=None_, _/_)[¶](https://docs.python.org/3/library/time.html#time.ctime "Link to this definition")

Convert a time expressed in seconds since the [epoch](https://docs.python.org/3/library/time.html#epoch)
 to a string of a form: `'Sun Jun 20 23:21:05 1993'` representing local time. The day field is two characters long and is space padded if the day is a single digit, for example: `'Wed Jun  9 04:26:40 1993'`.

If _seconds_ is not provided or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
, the current time as returned by [`time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
 is used. `ctime(seconds)` is equivalent to `asctime(localtime(seconds))`. Locale information is not used by `ctime()`.

Changed in version 3.15: Accepts any real number, not only integer or float.

time.get\_clock\_info(_name_, _/_)[¶](https://docs.python.org/3/library/time.html#time.get_clock_info "Link to this definition")

Get information on the specified clock as a namespace object. Supported clock names and the corresponding functions to read their value are:

*   `'monotonic'`: [`time.monotonic()`](https://docs.python.org/3/library/time.html#time.monotonic "time.monotonic")
    
*   `'perf_counter'`: [`time.perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter")
    
*   `'process_time'`: [`time.process_time()`](https://docs.python.org/3/library/time.html#time.process_time "time.process_time")
    
*   `'thread_time'`: [`time.thread_time()`](https://docs.python.org/3/library/time.html#time.thread_time "time.thread_time")
    
*   `'time'`: [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
    

The result has the following attributes:

*   _adjustable_: `True` if the clock can be set to jump forward or backward in time, `False` otherwise. Does not refer to gradual NTP rate adjustments.
    
*   _implementation_: The name of the underlying C function used to get the clock value. Refer to [Clock ID Constants](https://docs.python.org/3/library/time.html#time-clock-id-constants)
     for possible values.
    
*   _monotonic_: `True` if the clock cannot go backward, `False` otherwise
    
*   _resolution_: The resolution of the clock in seconds ([`float`](https://docs.python.org/3/builtins/functions.html#float "float")
    )
    

Added in version 3.3.

time.gmtime(_seconds\=None_, _/_)[¶](https://docs.python.org/3/library/time.html#time.gmtime "Link to this definition")

Convert a time expressed in seconds since the [epoch](https://docs.python.org/3/library/time.html#epoch)
 to a [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")
 in UTC in which the dst flag is always zero. If _seconds_ is not provided or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
, the current time as returned by [`time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
 is used. Fractions of a second are ignored. See above for a description of the `struct_time` object. See [`calendar.timegm()`](https://docs.python.org/3/library/calendar.html#calendar.timegm "calendar.timegm")
 for the inverse of this function.

Changed in version 3.15: Accepts any real number, not only integer or float.

time.localtime(_seconds\=None_, _/_)[¶](https://docs.python.org/3/library/time.html#time.localtime "Link to this definition")

Like [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")
 but converts to local time. If _seconds_ is not provided or [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
, the current time as returned by [`time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
 is used. The dst flag is set to `1` when DST applies to the given time.

`localtime()` may raise [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
, if the timestamp is outside the range of values supported by the platform C `localtime()` or `gmtime()` functions, and [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 on `localtime()` or `gmtime()` failure. It’s common for this to be restricted to years between 1970 and 2038.

Changed in version 3.15: Accepts any real number, not only integer or float.

time.mktime(_time\_tuple_, _/_)[¶](https://docs.python.org/3/library/time.html#time.mktime "Link to this definition")

This is the inverse function of [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
. Its argument is the [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")
 or full 9-tuple (since the dst flag is needed; use `-1` as the dst flag if it is unknown) which expresses the time in _local_ time, not UTC. It returns a floating-point number, for compatibility with [`time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
. If the input value cannot be represented as a valid time, either [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
 or [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 will be raised (which depends on whether the invalid value is caught by Python or the underlying C libraries). The earliest date for which it can generate a time is platform-dependent.

time.monotonic() → [float](https://docs.python.org/3/builtins/functions.html#float "float")
[¶](https://docs.python.org/3/library/time.html#time.monotonic "Link to this definition")

Return the value (in fractional seconds) of a monotonic clock, i.e. a clock that cannot go backwards. The clock is not affected by system clock updates. The reference point of the returned value is undefined, so that only the difference between the results of two calls is valid.

Clock:

*   On Windows, call `QueryPerformanceCounter()` and `QueryPerformanceFrequency()`.
    
*   On macOS, call `mach_absolute_time()` and `mach_timebase_info()`.
    
*   On HP-UX, call `gethrtime()`.
    
*   Call `clock_gettime(CLOCK_HIGHRES)` if available.
    
*   Otherwise, call `clock_gettime(CLOCK_MONOTONIC)`.
    

Use [`monotonic_ns()`](https://docs.python.org/3/library/time.html#time.monotonic_ns "time.monotonic_ns")
 to avoid the precision loss caused by the [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 type.

Added in version 3.3.

Changed in version 3.5: The function is now always available and the clock is now the same for all processes.

Changed in version 3.10: On macOS, the clock is now the same for all processes.

time.monotonic\_ns() → [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/time.html#time.monotonic_ns "Link to this definition")

Similar to [`monotonic()`](https://docs.python.org/3/library/time.html#time.monotonic "time.monotonic")
, but return time as nanoseconds.

Added in version 3.7.

time.perf\_counter() → [float](https://docs.python.org/3/builtins/functions.html#float "float")
[¶](https://docs.python.org/3/library/time.html#time.perf_counter "Link to this definition")

Return the value (in fractional seconds) of a performance counter, i.e. a clock with the highest available resolution to measure a short duration. It does include time elapsed during sleep. The clock is the same for all processes. The reference point of the returned value is undefined, so that only the difference between the results of two calls is valid.

**CPython implementation detail:** On CPython, use the same clock as [`time.monotonic()`](https://docs.python.org/3/library/time.html#time.monotonic "time.monotonic")
 and is a monotonic clock, i.e. a clock that cannot go backwards.

Use [`perf_counter_ns()`](https://docs.python.org/3/library/time.html#time.perf_counter_ns "time.perf_counter_ns")
 to avoid the precision loss caused by the [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 type.

Added in version 3.3.

Changed in version 3.10: On Windows, the clock is now the same for all processes.

Changed in version 3.13: Use the same clock as [`time.monotonic()`](https://docs.python.org/3/library/time.html#time.monotonic "time.monotonic")
.

time.perf\_counter\_ns() → [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/time.html#time.perf_counter_ns "Link to this definition")

Similar to [`perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter")
, but return time as nanoseconds.

Added in version 3.7.

time.process\_time() → [float](https://docs.python.org/3/builtins/functions.html#float "float")
[¶](https://docs.python.org/3/library/time.html#time.process_time "Link to this definition")

Return the value (in fractional seconds) of the sum of the system and user CPU time of the current process. It does not include time elapsed during sleep. It is process-wide by definition. The reference point of the returned value is undefined, so that only the difference between the results of two calls is valid.

Use [`process_time_ns()`](https://docs.python.org/3/library/time.html#time.process_time_ns "time.process_time_ns")
 to avoid the precision loss caused by the [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 type.

Added in version 3.3.

time.process\_time\_ns() → [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/time.html#time.process_time_ns "Link to this definition")

Similar to [`process_time()`](https://docs.python.org/3/library/time.html#time.process_time "time.process_time")
 but return time as nanoseconds.

Added in version 3.7.

time.sleep(_seconds_, _/_)[¶](https://docs.python.org/3/library/time.html#time.sleep "Link to this definition")

Suspend execution of the calling thread for the given number of seconds. The argument may be a non-integer to indicate a more precise sleep time.

If the sleep is interrupted by a signal and no exception is raised by the signal handler, the sleep is restarted with a recomputed timeout.

The suspension time may be longer than requested by an arbitrary amount, because of the scheduling of other activity in the system.

Windows implementation

On Windows, if _seconds_ is zero, the thread relinquishes the remainder of its time slice to any other thread that is ready to run. If there are no other threads ready to run, the function returns immediately, and the thread continues execution. On Windows 10 and newer the implementation uses a [high-resolution timer](https://learn.microsoft.com/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerexw)
 which provides resolution of 100 nanoseconds. If _seconds_ is zero, `Sleep(0)` is used.

Unix implementation

*   Use `clock_nanosleep()` if available (resolution: 1 nanosecond);
    
*   Or use `nanosleep()` if available (resolution: 1 nanosecond);
    
*   Or use `select()` (resolution: 1 microsecond).
    

Note

To emulate a “no-op”, use [`pass`](https://docs.python.org/3/reference/simple_stmts.html#pass)
 instead of `time.sleep(0)`.

To voluntarily relinquish the CPU, specify a real-time [scheduling policy](https://docs.python.org/3/library/os.html#os-scheduling-policy)
 and use [`os.sched_yield()`](https://docs.python.org/3/library/os.html#os.sched_yield "os.sched_yield")
 instead.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `time.sleep` with argument `seconds`.

Changed in version 3.5: The function now sleeps at least _seconds_ even if the sleep is interrupted by a signal, except if the signal handler raises an exception (see [**PEP 475**](https://peps.python.org/pep-0475/)
 for the rationale).

Changed in version 3.11: On Unix, the `clock_nanosleep()` and `nanosleep()` functions are now used if available. On Windows, a waitable timer is now used.

Changed in version 3.13: Raises an auditing event.

Changed in version 3.15: Accepts any real number, not only integer or float.

time.strftime(_format_\[, _time\_tuple_\])[¶](https://docs.python.org/3/library/time.html#time.strftime "Link to this definition")

Convert a tuple or [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")
 representing a time as returned by [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")
 or [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
 to a string as specified by the _format_ argument. If _time\_tuple_ is not provided, the current time as returned by `localtime()` is used. _format_ must be a string. [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised if any field in _time\_tuple_ is outside of the allowed range.

0 is a legal argument for any position in the time tuple; if it is normally illegal the value is forced to a correct one.

The following directives can be embedded in the _format_ string. They are shown without the optional field width and precision specification, and are replaced by the indicated characters in the `strftime()` result:

| Directive | Meaning | Notes |
| --- | --- | --- |
| `%a` | Locale’s abbreviated weekday name. |     |
| `%A` | Locale’s full weekday name. |     |
| `%b` | Locale’s abbreviated month name. |     |
| `%B` | Locale’s full month name. |     |
| `%c` | Locale’s appropriate date and time representation. |     |
| `%d` | Day of the month as a decimal number \[01,31\]. |     |
| `%f` | Microseconds as a decimal number \[000000,999999\]. | (1) |
| `%H` | Hour (24-hour clock) as a decimal number \[00,23\]. |     |
| `%I` | Hour (12-hour clock) as a decimal number \[01,12\]. |     |
| `%j` | Day of the year as a decimal number \[001,366\]. |     |
| `%m` | Month as a decimal number \[01,12\]. |     |
| `%M` | Minute as a decimal number \[00,59\]. |     |
| `%p` | Locale’s equivalent of either AM or PM. | (2) |
| `%S` | Second as a decimal number \[00,61\]. | (3) |
| `%U` | Week number of the year (Sunday as the first day of the week) as a decimal number \[00,53\]. All days in a new year preceding the first Sunday are considered to be in week 0. | (4) |
| `%u` | Day of the week (Monday is 1; Sunday is 7) as a decimal number \[1, 7\]. |     |
| `%w` | Weekday as a decimal number \[0(Sunday),6\]. |     |
| `%W` | Week number of the year (Monday as the first day of the week) as a decimal number \[00,53\]. All days in a new year preceding the first Monday are considered to be in week 0. | (4) |
| `%x` | Locale’s appropriate date representation. |     |
| `%X` | Locale’s appropriate time representation. |     |
| `%y` | Year without century as a decimal number \[00,99\]. |     |
| `%Y` | Year with century as a decimal number. |     |
| `%z` | Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits \[-23:59, +23:59\]. [\[1\]](https://docs.python.org/3/library/time.html#id4) |     |
| `%Z` | Time zone name (no characters if no time zone exists). Deprecated. [\[1\]](https://docs.python.org/3/library/time.html#id4) |     |
| `%G` | ISO 8601 year (similar to `%Y` but follows the rules for the ISO 8601 calendar year). The year starts with the week that contains the first Thursday of the calendar year. |     |
| `%V` | ISO 8601 week number (as a decimal number \[01,53\]). The first week of the year is the one that contains the first Thursday of the year. Weeks start on Monday. |     |
| `%%` | A literal `'%'` character. |     |

Notes:

1.  The `%f` format directive only applies to [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime")
    , not to `strftime()`. However, see also [`datetime.datetime.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime")
     and [`datetime.datetime.strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime")
     where the `%f` format directive [applies to microseconds](https://docs.python.org/3/library/datetime.html#format-codes)
    .
    
2.  When used with the [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime")
     function, the `%p` directive only affects the output hour field if the `%I` directive is used to parse the hour.
    

3.  The range really is `0` to `61`; value `60` is valid in timestamps representing [leap seconds](https://en.wikipedia.org/wiki/Leap_second)
     and value `61` is supported for historical reasons.
    
4.  When used with the [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime")
     function, `%U` and `%W` are only used in calculations when the day of the week and the year are specified.
    

Here is an example, a format for dates compatible with that specified in the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
 Internet email standard. [\[1\]](https://docs.python.org/3/library/time.html#id4)

Copy

\>>> from time import gmtime, strftime
\>>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
'Thu, 28 Jun 2001 14:17:15 +0000'

Additional directives may be supported on certain platforms, but only the ones listed here have a meaning standardized by ANSI C. To see the full set of format codes supported on your platform, consult the _[strftime(3)](https://manpages.debian.org/strftime(3))
_ documentation.

On some platforms, an optional field width and precision specification can immediately follow the initial `'%'` of a directive in the following order; this is also not portable. The field width is normally 2 except for `%j` where it is 3.

time.strptime(_string_\[, _format_\])[¶](https://docs.python.org/3/library/time.html#time.strptime "Link to this definition")

Parse a string representing a time according to a format. The return value is a [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")
 as returned by [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")
 or [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
.

The _format_ parameter uses the same directives as those used by [`strftime()`](https://docs.python.org/3/library/time.html#time.strftime "time.strftime")
; it defaults to `"%a %b %d %H:%M:%S %Y"` which matches the formatting returned by [`ctime()`](https://docs.python.org/3/library/time.html#time.ctime "time.ctime")
. If _string_ cannot be parsed according to _format_, or if it has excess data after parsing, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. The default values used to fill in any missing data when more accurate values cannot be inferred are `(1900, 1, 1, 0, 0, 0, 0, 1, -1)`. Both _string_ and _format_ must be strings.

For example:

Copy

\>>> import time
\>>> time.strptime("30 Nov 00", "%d %b %y")
time.struct\_time(tm\_year=2000, tm\_mon=11, tm\_mday=30, tm\_hour=0, tm\_min=0,
                 tm\_sec=0, tm\_wday=3, tm\_yday=335, tm\_isdst=-1)

Support for the `%Z` directive is based on the values contained in `tzname` and whether `daylight` is true. Because of this, it is platform-specific except for recognizing UTC and GMT which are always known (and are considered to be non-daylight savings timezones).

Only the directives specified in the documentation are supported. Because `strftime()` is implemented per platform it can sometimes offer more directives than those listed. But `strptime()` is independent of any platform and thus does not necessarily support all directives available that are not documented as supported.

class time.struct\_time[¶](https://docs.python.org/3/library/time.html#time.struct_time "Link to this definition")

The type of the time value sequence returned by [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")
, [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
, and [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime")
. It is an object with a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 interface: values can be accessed by index and by attribute name. The following values are present:

|     |     |     |
| --- | --- | --- |
| Index | Attribute | Values |
| 0   | tm\_year[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_year "Link to this definition") | (for example, 1993) |
| 1   | tm\_mon[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_mon "Link to this definition") | range \[1, 12\] |
| 2   | tm\_mday[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_mday "Link to this definition") | range \[1, 31\] |
| 3   | tm\_hour[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_hour "Link to this definition") | range \[0, 23\] |
| 4   | tm\_min[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_min "Link to this definition") | range \[0, 59\] |
| 5   | tm\_sec[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_sec "Link to this definition") | range \[0, 61\]; see [Note (3)](https://docs.python.org/3/library/time.html#leap-second)<br> in [`strftime()`](https://docs.python.org/3/library/time.html#time.strftime "time.strftime") |
| 6   | tm\_wday[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_wday "Link to this definition") | range \[0, 6\]; Monday is 0 |
| 7   | tm\_yday[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_yday "Link to this definition") | range \[1, 366\] |
| 8   | tm\_isdst[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_isdst "Link to this definition") | 0, 1 or -1; see below |
| N/A | tm\_zone[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_zone "Link to this definition") | abbreviation of timezone name |
| N/A | tm\_gmtoff[¶](https://docs.python.org/3/library/time.html#time.struct_time.tm_gmtoff "Link to this definition") | offset east of UTC in seconds |

Note that unlike the C structure, the month value is a range of \[1, 12\], not \[0, 11\].

In calls to [`mktime()`](https://docs.python.org/3/library/time.html#time.mktime "time.mktime")
, [`tm_isdst`](https://docs.python.org/3/library/time.html#time.struct_time.tm_isdst "time.struct_time.tm_isdst")
 may be set to 1 when daylight savings time is in effect, and 0 when it is not. A value of -1 indicates that this is not known, and will usually result in the correct state being filled in.

When a tuple with an incorrect length is passed to a function expecting a `struct_time`, or having elements of the wrong type, a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised.

time.time() → [float](https://docs.python.org/3/builtins/functions.html#float "float")
[¶](https://docs.python.org/3/library/time.html#time.time "Link to this definition")

Return the time in seconds since the [epoch](https://docs.python.org/3/library/time.html#epoch)
 as a floating-point number. The handling of [leap seconds](https://en.wikipedia.org/wiki/Leap_second)
 is platform dependent. On Windows and most Unix systems, the leap seconds are not counted towards the time in seconds since the [epoch](https://docs.python.org/3/library/time.html#epoch)
. This is commonly referred to as [Unix time](https://en.wikipedia.org/wiki/Unix_time)
.

Note that even though the time is always returned as a floating-point number, not all systems provide time with a better precision than 1 second. While this function normally returns non-decreasing values, it can return a lower value than a previous call if the system clock has been set back between the two calls.

The number returned by `time()` may be converted into a more common time format (i.e. year, month, day, hour, etc…) in UTC by passing it to [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")
 function or in local time by passing it to the [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
 function. In both cases a [`struct_time`](https://docs.python.org/3/library/time.html#time.struct_time "time.struct_time")
 object is returned, from which the components of the calendar date may be accessed as attributes.

Clock:

*   On Windows, call `GetSystemTimePreciseAsFileTime()`.
    
*   Call `clock_gettime(CLOCK_REALTIME)` if available.
    
*   Otherwise, call `gettimeofday()`.
    

Use [`time_ns()`](https://docs.python.org/3/library/time.html#time.time_ns "time.time_ns")
 to avoid the precision loss caused by the [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 type.

Changed in version 3.13: On Windows, calls `GetSystemTimePreciseAsFileTime()` instead of `GetSystemTimeAsFileTime()`.

time.time\_ns() → [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/time.html#time.time_ns "Link to this definition")

Similar to [`time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
 but returns time as an integer number of nanoseconds since the [epoch](https://docs.python.org/3/library/time.html#epoch)
.

Added in version 3.7.

time.thread\_time() → [float](https://docs.python.org/3/builtins/functions.html#float "float")
[¶](https://docs.python.org/3/library/time.html#time.thread_time "Link to this definition")

Return the value (in fractional seconds) of the sum of the system and user CPU time of the current thread. It does not include time elapsed during sleep. It is thread-specific by definition. The reference point of the returned value is undefined, so that only the difference between the results of two calls in the same thread is valid.

Use [`thread_time_ns()`](https://docs.python.org/3/library/time.html#time.thread_time_ns "time.thread_time_ns")
 to avoid the precision loss caused by the [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 type.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux, Unix, Windows.

Unix systems supporting `CLOCK_THREAD_CPUTIME_ID`.

Added in version 3.7.

time.thread\_time\_ns() → [int](https://docs.python.org/3/builtins/functions.html#int "int")
[¶](https://docs.python.org/3/library/time.html#time.thread_time_ns "Link to this definition")

Similar to [`thread_time()`](https://docs.python.org/3/library/time.html#time.thread_time "time.thread_time")
 but return time as nanoseconds.

Added in version 3.7.

time.tzset()[¶](https://docs.python.org/3/library/time.html#time.tzset "Link to this definition")

Reset the time conversion rules used by the library routines. The environment variable `TZ` specifies how this is done. It will also set the variables `tzname` (from the `TZ` environment variable), `timezone` (non-DST seconds West of UTC), `altzone` (DST seconds west of UTC) and `daylight` (to 0 if this timezone does not have any daylight saving time rules, or to nonzero if there is a time, past, present or future when daylight saving time applies).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Note

Although in many cases, changing the `TZ` environment variable may affect the output of functions like [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
 without calling `tzset()`, this behavior should not be relied on.

The `TZ` environment variable should contain no whitespace.

The standard format of the `TZ` environment variable is (whitespace added for clarity):

Copy

std offset \[dst \[offset \[,start\[/time\], end\[/time\]\]\]\]

Where the components are:

`std` and `dst`

Three or more alphanumerics giving the timezone abbreviations. These will be propagated into time.tzname

`offset`

The offset has the form: `± hh[:mm[:ss]]`. This indicates the value added the local time to arrive at UTC. If preceded by a ‘-’, the timezone is east of the Prime Meridian; otherwise, it is west. If no offset follows dst, summer time is assumed to be one hour ahead of standard time.

`start[/time], end[/time]`

Indicates when to change to and back from DST. The format of the start and end dates are one of the following:

`J_n_`

The Julian day _n_ (1 <= _n_ <= 365). Leap days are not counted, so in all years February 28 is day 59 and March 1 is day 60.

`_n_`

The zero-based Julian day (0 <= _n_ <= 365). Leap days are counted, and it is possible to refer to February 29.

`M_m_._n_._d_`

The _d_’th day (0 <= _d_ <= 6) of week _n_ of month _m_ of the year (1 <= _n_ <= 5, 1 <= _m_ <= 12, where week 5 means “the last _d_ day in month _m_” which may occur in either the fourth or the fifth week). Week 1 is the first week in which the _d_’th day occurs. Day zero is a Sunday.

`time` has the same format as `offset` except that no leading sign (‘-’ or ‘+’) is allowed. The default, if time is not given, is 02:00:00.

Copy

\>>> os.environ\['TZ'\] \= 'EST+05EDT,M4.1.0,M10.5.0'
\>>> time.tzset()
\>>> time.strftime('%X %x %Z')
'02:07:36 05/08/03 EDT'
\>>> os.environ\['TZ'\] \= 'AEST-10AEDT-11,M10.5.0,M3.5.0'
\>>> time.tzset()
\>>> time.strftime('%X %x %Z')
'16:08:12 05/08/03 AEST'

On many Unix systems (including \*BSD, Linux, Solaris, and Darwin), it is more convenient to use the system’s zoneinfo (_[tzfile(5)](https://manpages.debian.org/tzfile(5))
_) database to specify the timezone rules. To do this, set the `TZ` environment variable to the path of the required timezone datafile, relative to the root of the systems ‘zoneinfo’ timezone database, usually located at `/usr/share/zoneinfo`. For example, `'US/Eastern'`, `'Australia/Melbourne'`, `'Egypt'` or `'Europe/Amsterdam'`.

Copy

\>>> os.environ\['TZ'\] \= 'US/Eastern'
\>>> time.tzset()
\>>> time.tzname
('EST', 'EDT')
\>>> os.environ\['TZ'\] \= 'Egypt'
\>>> time.tzset()
\>>> time.tzname
('EET', 'EEST')

Clock ID Constants[¶](https://docs.python.org/3/library/time.html#clock-id-constants "Link to this heading")

-------------------------------------------------------------------------------------------------------------

These constants are used as parameters for [`clock_getres()`](https://docs.python.org/3/library/time.html#time.clock_getres "time.clock_getres")
 and [`clock_gettime()`](https://docs.python.org/3/library/time.html#time.clock_gettime "time.clock_gettime")
.

time.CLOCK\_BOOTTIME[¶](https://docs.python.org/3/library/time.html#time.CLOCK_BOOTTIME "Link to this definition")

Identical to [`CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC")
, except it also includes any time that the system is suspended.

This allows applications to get a suspend-aware monotonic clock without having to deal with the complications of [`CLOCK_REALTIME`](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "time.CLOCK_REALTIME")
, which may have discontinuities if the time is changed using `settimeofday()` or similar.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.39.

Added in version 3.7.

time.CLOCK\_HIGHRES[¶](https://docs.python.org/3/library/time.html#time.CLOCK_HIGHRES "Link to this definition")

The Solaris OS has a `CLOCK_HIGHRES` timer that attempts to use an optimal hardware source, and may give close to nanosecond resolution. `CLOCK_HIGHRES` is the nonadjustable, high-resolution clock.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Solaris.

Added in version 3.3.

time.CLOCK\_MONOTONIC[¶](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "Link to this definition")

Clock that cannot be set and represents monotonic time since some unspecified starting point.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

time.CLOCK\_MONOTONIC\_RAW[¶](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC_RAW "Link to this definition")

Similar to [`CLOCK_MONOTONIC`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC "time.CLOCK_MONOTONIC")
, but provides access to a raw hardware-based time that is not subject to NTP adjustments.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux >= 2.6.28, macOS >= 10.12.

Added in version 3.3.

time.CLOCK\_MONOTONIC\_RAW\_APPROX[¶](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC_RAW_APPROX "Link to this definition")

Similar to [`CLOCK_MONOTONIC_RAW`](https://docs.python.org/3/library/time.html#time.CLOCK_MONOTONIC_RAW "time.CLOCK_MONOTONIC_RAW")
, but reads a value cached by the system at context switch and hence has less accuracy.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: macOS >= 10.12.

Added in version 3.13.

time.CLOCK\_PROCESS\_CPUTIME\_ID[¶](https://docs.python.org/3/library/time.html#time.CLOCK_PROCESS_CPUTIME_ID "Link to this definition")

High-resolution per-process timer from the CPU.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

time.CLOCK\_PROF[¶](https://docs.python.org/3/library/time.html#time.CLOCK_PROF "Link to this definition")

High-resolution per-process timer from the CPU.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD, NetBSD >= 7, OpenBSD.

Added in version 3.7.

time.CLOCK\_TAI[¶](https://docs.python.org/3/library/time.html#time.CLOCK_TAI "Link to this definition")

[International Atomic Time](https://www.nist.gov/pml/time-and-frequency-division/how-utcnist-related-coordinated-universal-time-utc-international)

The system must have a current leap second table in order for this to give the correct answer. PTP or NTP software can maintain a leap second table.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Linux.

Added in version 3.9.

time.CLOCK\_THREAD\_CPUTIME\_ID[¶](https://docs.python.org/3/library/time.html#time.CLOCK_THREAD_CPUTIME_ID "Link to this definition")

Thread-specific CPU-time clock.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

time.CLOCK\_UPTIME[¶](https://docs.python.org/3/library/time.html#time.CLOCK_UPTIME "Link to this definition")

Time whose absolute value is the time the system has been running and not suspended, providing accurate uptime measurement, both absolute and interval.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: FreeBSD, OpenBSD >= 5.5.

Added in version 3.7.

time.CLOCK\_UPTIME\_RAW[¶](https://docs.python.org/3/library/time.html#time.CLOCK_UPTIME_RAW "Link to this definition")

Clock that increments monotonically, tracking the time since an arbitrary point, unaffected by frequency or time adjustments and not incremented while the system is asleep.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: macOS >= 10.12.

Added in version 3.8.

time.CLOCK\_UPTIME\_RAW\_APPROX[¶](https://docs.python.org/3/library/time.html#time.CLOCK_UPTIME_RAW_APPROX "Link to this definition")

Like [`CLOCK_UPTIME_RAW`](https://docs.python.org/3/library/time.html#time.CLOCK_UPTIME_RAW "time.CLOCK_UPTIME_RAW")
, but the value is cached by the system at context switches and therefore has less accuracy.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: macOS >= 10.12.

Added in version 3.13.

The following constant is the only parameter that can be sent to [`clock_settime()`](https://docs.python.org/3/library/time.html#time.clock_settime "time.clock_settime")
.

time.CLOCK\_REALTIME[¶](https://docs.python.org/3/library/time.html#time.CLOCK_REALTIME "Link to this definition")

Real-time clock. Setting this clock requires appropriate privileges. The clock is the same for all processes.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Added in version 3.3.

Timezone Constants[¶](https://docs.python.org/3/library/time.html#timezone-constants "Link to this heading")

-------------------------------------------------------------------------------------------------------------

time.altzone[¶](https://docs.python.org/3/library/time.html#time.altzone "Link to this definition")

The offset of the local DST timezone, in seconds west of UTC, if one is defined. This is negative if the local DST timezone is east of UTC (as in Western Europe, including the UK). Only use this if `daylight` is nonzero. See note below.

time.daylight[¶](https://docs.python.org/3/library/time.html#time.daylight "Link to this definition")

Nonzero if a DST timezone is defined. See note below.

time.timezone[¶](https://docs.python.org/3/library/time.html#time.timezone "Link to this definition")

The offset of the local (non-DST) timezone, in seconds west of UTC (negative in most of Western Europe, positive in the US, zero in the UK). See note below.

time.tzname[¶](https://docs.python.org/3/library/time.html#time.tzname "Link to this definition")

A tuple of two strings: the first is the name of the local non-DST timezone, the second is the name of the local DST timezone. If no DST timezone is defined, the second string should not be used. See note below.

Note

For the above Timezone constants ([`altzone`](https://docs.python.org/3/library/time.html#time.altzone "time.altzone")
, [`daylight`](https://docs.python.org/3/library/time.html#time.daylight "time.daylight")
, [`timezone`](https://docs.python.org/3/library/time.html#time.timezone "time.timezone")
, and [`tzname`](https://docs.python.org/3/library/time.html#time.tzname "time.tzname")
), the value is determined by the timezone rules in effect at module load time or the last time [`tzset()`](https://docs.python.org/3/library/time.html#time.tzset "time.tzset")
 is called and may be incorrect for times in the past. It is recommended to use the [`tm_gmtoff`](https://docs.python.org/3/library/time.html#time.struct_time.tm_gmtoff "time.struct_time.tm_gmtoff")
 and [`tm_zone`](https://docs.python.org/3/library/time.html#time.struct_time.tm_zone "time.struct_time.tm_zone")
 results from [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime")
 to obtain timezone information.

See also

Module [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")

More object-oriented interface to dates and times.

Module [`locale`](https://docs.python.org/3/library/locale.html#module-locale "locale: Internationalization services.")

Internationalization services. The locale setting affects the interpretation of many format specifiers in [`strftime()`](https://docs.python.org/3/library/time.html#time.strftime "time.strftime")
 and [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime")
.

Module [`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.")

General calendar-related functions. [`timegm()`](https://docs.python.org/3/library/calendar.html#calendar.timegm "calendar.timegm")
 is the inverse of [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime")
 from this module.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`time` — Time access and conversions](https://docs.python.org/3/library/time.html#)
    *   [Functions](https://docs.python.org/3/library/time.html#functions)
        
    *   [Clock ID Constants](https://docs.python.org/3/library/time.html#clock-id-constants)
        
    *   [Timezone Constants](https://docs.python.org/3/library/time.html#timezone-constants)
        

#### Previous topic

[`io` — Core tools for working with streams](https://docs.python.org/3/library/io.html "previous chapter")

#### Next topic

[`logging` — Logging facility for Python](https://docs.python.org/3/library/logging.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=time+%E2%80%94+Time+access+and+conversions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftime.html&pagesource=library%2Ftime.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/time.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/logging.html "logging — Logging facility for Python")
     |
*   [previous](https://docs.python.org/3/library/io.html "io — Core tools for working with streams")
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
*   [Generic Operating System Services](https://docs.python.org/3/library/allos.html)
     »
*   [`time` — Time access and conversions](https://docs.python.org/3/library/time.html)
    
*    
    
    |
*   Theme Auto Light Dark |