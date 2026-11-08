### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/sys.monitoring.html "sys.monitoring — Execution event monitoring")
     |
*   [previous](https://docs.python.org/3/library/python.html "Python Runtime Services")
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
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)
     »
*   [`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`sys` — System-specific parameters and functions[¶](https://docs.python.org/3/library/sys.html#module-sys "Link to this heading")

==================================================================================================================================

* * *

This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available. Unless explicitly noted otherwise, all variables are read-only.

sys.abi\_info[¶](https://docs.python.org/3/library/sys.html#sys.abi_info "Link to this definition")

Added in version 3.15.

An object containing information about the ABI of the currently running Python interpreter. It should include information that affect the CPython ABI in ways that require a specific build of the interpreter chosen from variants that can co-exist on a single machine. For example, it does not encode the base OS (Linux or Windows), but does include pointer size since some systems support both 32- and 64-bit builds. The available entries are the same on all platforms; e.g. _pointer\_size_ is available even on 64-bit-only architectures.

The following attributes are available:

abi\_info.pointer\_bits[¶](https://docs.python.org/3/library/sys.html#sys.abi_info.pointer_bits "Link to this definition")

The width of pointers in bits, as an integer, equivalent to `8 * sizeof(void *)`. Usually, this is `32` or `64`.

abi\_info.free\_threaded[¶](https://docs.python.org/3/library/sys.html#sys.abi_info.free_threaded "Link to this definition")

A Boolean indicating whether the interpreter was built with [free threading](https://docs.python.org/3/glossary.html#term-free-threading)
 support. This reflects either the presence of the [`--disable-gil`](https://docs.python.org/3/using/configure.html#cmdoption-disable-gil)
 `configure` option (on Unix) or setting the `DisableGil` property (on Windows).

abi\_info.debug[¶](https://docs.python.org/3/library/sys.html#sys.abi_info.debug "Link to this definition")

A Boolean indicating whether the interpreter was built in [debug mode](https://docs.python.org/3/using/configure.html#debug-build)
. This reflects either the presence of the [`--with-pydebug`](https://docs.python.org/3/using/configure.html#cmdoption-with-pydebug)
 `configure` option (on Unix) or the `Debug` configuration (on Windows).

abi\_info.byteorder[¶](https://docs.python.org/3/library/sys.html#sys.abi_info.byteorder "Link to this definition")

A string indicating the native byte order, either `'big'` or `'little'`. This is the same as the [`byteorder`](https://docs.python.org/3/library/sys.html#sys.byteorder "sys.byteorder")
 attribute.

sys.abiflags[¶](https://docs.python.org/3/library/sys.html#sys.abiflags "Link to this definition")

On POSIX systems where Python was built with the standard `configure` script, this contains the ABI flags as specified by [**PEP 3149**](https://peps.python.org/pep-3149/)
.

Added in version 3.2.

Changed in version 3.8: Default flags became an empty string (`m` flag for pymalloc has been removed).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

sys.addaudithook(_hook_)[¶](https://docs.python.org/3/library/sys.html#sys.addaudithook "Link to this definition")

Append the callable _hook_ to the list of active auditing hooks for the current (sub)interpreter.

When an auditing event is raised through the [`sys.audit()`](https://docs.python.org/3/library/sys.html#sys.audit "sys.audit")
 function, each hook will be called in the order it was added with the event name and the tuple of arguments. Native hooks added by [`PySys_AddAuditHook()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AddAuditHook "PySys_AddAuditHook")
 are called first, followed by hooks added in the current (sub)interpreter. Hooks can then log the event, raise an exception to abort the operation, or terminate the process entirely.

Note that audit hooks are primarily for collecting information about internal or otherwise unobservable actions, whether by Python or libraries written in Python. They are not suitable for implementing a “sandbox”. In particular, malicious code can trivially disable or bypass hooks added using this function. At a minimum, any security-sensitive hooks must be added using the C API [`PySys_AddAuditHook()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AddAuditHook "PySys_AddAuditHook")
 before initialising the runtime, and any modules allowing arbitrary memory modification (such as [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
) should be completely removed or closely monitored.

Calling `sys.addaudithook()` will itself raise an auditing event named `sys.addaudithook` with no arguments. If any existing hooks raise an exception derived from [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
, the new hook will not be added and the exception suppressed. As a result, callers cannot assume that their hook has been added unless they control all existing hooks.

See the [audit events table](https://docs.python.org/3/library/audit_events.html#audit-events)
 for all events raised by CPython, and [**PEP 578**](https://peps.python.org/pep-0578/)
 for the original design discussion.

Added in version 3.8.

Changed in version 3.8.1: Exceptions derived from [`Exception`](https://docs.python.org/3/builtins/exceptions.html#Exception "Exception")
 but not [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 are no longer suppressed.

**CPython implementation detail:** When tracing is enabled (see [`settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace")
), Python hooks are only traced if the callable has a `__cantrace__` member that is set to a true value. Otherwise, trace functions will skip the hook.

sys.argv[¶](https://docs.python.org/3/library/sys.html#sys.argv "Link to this definition")

The list of command line arguments passed to a Python script. `argv[0]` is the script name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c)
 command line option to the interpreter, `argv[0]` is set to the string `'-c'`. If no script name was passed to the Python interpreter, `argv[0]` is the empty string.

To loop over the standard input, or the list of files given on the command line, see the [`fileinput`](https://docs.python.org/3/library/fileinput.html#module-fileinput "fileinput: Loop over standard input or a list of files.")
 module.

See also [`sys.orig_argv`](https://docs.python.org/3/library/sys.html#sys.orig_argv "sys.orig_argv")
.

Note

On Unix, command line arguments are passed by bytes from OS. Python decodes them with filesystem encoding and “surrogateescape” error handler. When you need original bytes, you can get it by `[os.fsencode(arg) for arg in sys.argv]`.

sys.audit(_event_, _\*args_)[¶](https://docs.python.org/3/library/sys.html#sys.audit "Link to this definition")

Raise an auditing event and trigger any active auditing hooks. _event_ is a string identifying the event, and _args_ may contain optional arguments with more information about the event. The number and types of arguments for a given event are considered a public and stable API and should not be modified between releases.

For example, one auditing event is named `os.chdir`. This event has one argument called _path_ that will contain the requested new working directory.

`sys.audit()` will call the existing auditing hooks, passing the event name and arguments, and will re-raise the first exception from any hook. In general, if an exception is raised, it should not be handled and the process should be terminated as quickly as possible. This allows hook implementations to decide how to respond to particular events: they can merely log the event or abort the operation by raising an exception.

Hooks are added using the [`sys.addaudithook()`](https://docs.python.org/3/library/sys.html#sys.addaudithook "sys.addaudithook")
 or [`PySys_AddAuditHook()`](https://docs.python.org/3/c-api/sys.html#c.PySys_AddAuditHook "PySys_AddAuditHook")
 functions.

The native equivalent of this function is [`PySys_Audit()`](https://docs.python.org/3/c-api/sys.html#c.PySys_Audit "PySys_Audit")
. Using the native function is preferred when possible.

See the [audit events table](https://docs.python.org/3/library/audit_events.html#audit-events)
 for all events raised by CPython.

Added in version 3.8.

sys.base\_exec\_prefix[¶](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "Link to this definition")

Equivalent to [`exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix")
, but referring to the base Python installation.

When running under [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments)
, [`exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix")
 gets overwritten to the virtual environment prefix. `base_exec_prefix`, conversely, does not change, and always points to the base Python installation. Refer to [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments)
 for more information.

Added in version 3.3.

sys.base\_prefix[¶](https://docs.python.org/3/library/sys.html#sys.base_prefix "Link to this definition")

Equivalent to [`prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix")
, but referring to the base Python installation.

When running under [virtual environment](https://docs.python.org/3/library/venv.html#venv-def)
, [`prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix")
 gets overwritten to the virtual environment prefix. `base_prefix`, conversely, does not change, and always points to the base Python installation. Refer to [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments)
 for more information.

Added in version 3.3.

sys.byteorder[¶](https://docs.python.org/3/library/sys.html#sys.byteorder "Link to this definition")

An indicator of the native byte order. This will have the value `'big'` on big-endian (most-significant byte first) platforms, and `'little'` on little-endian (least-significant byte first) platforms.

sys.builtin\_module\_names[¶](https://docs.python.org/3/library/sys.html#sys.builtin_module_names "Link to this definition")

A tuple of strings containing the names of all modules that are compiled into this Python interpreter. (This information is not available in any other way — `modules.keys()` only lists the imported modules.)

See also the [`sys.stdlib_module_names`](https://docs.python.org/3/library/sys.html#sys.stdlib_module_names "sys.stdlib_module_names")
 list.

sys.call\_tracing(_func_, _args_)[¶](https://docs.python.org/3/library/sys.html#sys.call_tracing "Link to this definition")

Call `func(*args)`, while tracing is enabled. The tracing state is saved, and restored afterwards. This is intended to be called from a debugger from a checkpoint, to recursively debug or profile some other code.

Tracing is suspended while calling a tracing function set by [`settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace")
 or [`setprofile()`](https://docs.python.org/3/library/sys.html#sys.setprofile "sys.setprofile")
 to avoid infinite recursion. `call_tracing()` enables explicit recursion of the tracing function.

sys.copyright[¶](https://docs.python.org/3/library/sys.html#sys.copyright "Link to this definition")

A string containing the copyright pertaining to the Python interpreter.

sys.\_clear\_type\_cache()[¶](https://docs.python.org/3/library/sys.html#sys._clear_type_cache "Link to this definition")

Clear the internal type cache. The type cache is used to speed up attribute and method lookups. Use the function _only_ to drop unnecessary references during reference leak debugging.

This function should be used for internal and specialized purposes only.

Deprecated since version 3.13: Use the more general [`_clear_internal_caches()`](https://docs.python.org/3/library/sys.html#sys._clear_internal_caches "sys._clear_internal_caches")
 function instead.

sys.\_clear\_internal\_caches()[¶](https://docs.python.org/3/library/sys.html#sys._clear_internal_caches "Link to this definition")

Clear all internal performance-related caches. Use this function _only_ to release unnecessary references and memory blocks when hunting for leaks.

Added in version 3.13.

sys.\_current\_frames()[¶](https://docs.python.org/3/library/sys.html#sys._current_frames "Link to this definition")

Return a dictionary mapping each thread’s identifier to the topmost stack frame currently active in that thread at the time the function is called. Note that functions in the [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.")
 module can build the call stack given such a frame.

This is most useful for debugging deadlock: this function does not require the deadlocked threads’ cooperation, and such threads’ call stacks are frozen for as long as they remain deadlocked. The frame returned for a non-deadlocked thread may bear no relationship to that thread’s current activity by the time calling code examines the frame.

This function should be used for internal and specialized purposes only.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `sys._current_frames` with no arguments.

sys.\_current\_exceptions()[¶](https://docs.python.org/3/library/sys.html#sys._current_exceptions "Link to this definition")

Return a dictionary mapping each thread’s identifier to the topmost exception currently active in that thread at the time the function is called. If a thread is not currently handling an exception, it is not included in the result dictionary.

This is most useful for statistical profiling.

This function should be used for internal and specialized purposes only.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `sys._current_exceptions` with no arguments.

Changed in version 3.12: Each value in the dictionary is now a single exception instance, rather than a 3-tuple as returned from `sys.exc_info()`.

sys.breakpointhook()[¶](https://docs.python.org/3/library/sys.html#sys.breakpointhook "Link to this definition")

This hook function is called by built-in [`breakpoint()`](https://docs.python.org/3/builtins/functions.html#breakpoint "breakpoint")
. By default, it drops you into the [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")
 debugger, but it can be set to any other function so that you can choose which debugger gets used.

The signature of this function is dependent on what it calls. For example, the default binding (e.g. `pdb.set_trace()`) expects no arguments, but you might bind it to a function that expects additional arguments (positional and/or keyword). The built-in `breakpoint()` function passes its `*args` and `**kws` straight through. Whatever `breakpointhook()` returns is returned from `breakpoint()`.

The default implementation first consults the environment variable [`PYTHONBREAKPOINT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONBREAKPOINT)
. If that is set to `"0"` then this function returns immediately; i.e. it is a no-op. If the environment variable is not set, or is set to the empty string, `pdb.set_trace()` is called. Otherwise this variable should name a function to run, using Python’s dotted-import nomenclature, e.g. `package.subpackage.module.function`. In this case, `package.subpackage.module` would be imported and the resulting module must have a callable named `function()`. This is run, passing in `*args` and `**kws`, and whatever `function()` returns, `sys.breakpointhook()` returns to the built-in [`breakpoint()`](https://docs.python.org/3/builtins/functions.html#breakpoint "breakpoint")
 function.

Note that if anything goes wrong while importing the callable named by [`PYTHONBREAKPOINT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONBREAKPOINT)
, a [`RuntimeWarning`](https://docs.python.org/3/builtins/exceptions.html#RuntimeWarning "RuntimeWarning")
 is reported and the breakpoint is ignored.

Also note that if `sys.breakpointhook()` is overridden programmatically, [`PYTHONBREAKPOINT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONBREAKPOINT)
 is _not_ consulted.

Added in version 3.7.

sys.\_debugmallocstats()[¶](https://docs.python.org/3/library/sys.html#sys._debugmallocstats "Link to this definition")

Print low-level information to stderr about the state of CPython’s memory allocator.

If Python is [built in debug mode](https://docs.python.org/3/using/configure.html#debug-build)
 ([`configure --with-pydebug option`](https://docs.python.org/3/using/configure.html#cmdoption-with-pydebug)
), it also performs some expensive internal consistency checks.

Added in version 3.3.

**CPython implementation detail:** This function is specific to CPython. The exact output format is not defined here, and may change.

sys.dllhandle[¶](https://docs.python.org/3/library/sys.html#sys.dllhandle "Link to this definition")

Integer specifying the handle of the Python DLL.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

sys.displayhook(_value_)[¶](https://docs.python.org/3/library/sys.html#sys.displayhook "Link to this definition")

If _value_ is not `None`, this function prints `repr(value)` to `sys.stdout`, and saves _value_ in `builtins._`. If `repr(value)` is not encodable to `sys.stdout.encoding` with `sys.stdout.errors` error handler (which is probably `'strict'`), encode it to `sys.stdout.encoding` with `'backslashreplace'` error handler.

`sys.displayhook` is called on the result of evaluating an [expression](https://docs.python.org/3/glossary.html#term-expression)
 entered in an interactive Python session. The display of these values can be customized by assigning another one-argument function to `sys.displayhook`.

Pseudo-code:

Copy

def displayhook(value):
    if value is None:
        return
    \# Set '\_' to None to avoid recursion
    builtins.\_ \= None
    text \= repr(value)
    try:
        sys.stdout.write(text)
    except UnicodeEncodeError:
        bytes \= text.encode(sys.stdout.encoding, 'backslashreplace')
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout.buffer.write(bytes)
        else:
            text \= bytes.decode(sys.stdout.encoding, 'strict')
            sys.stdout.write(text)
    sys.stdout.write("\\n")
    builtins.\_ \= value

Changed in version 3.2: Use `'backslashreplace'` error handler on [`UnicodeEncodeError`](https://docs.python.org/3/builtins/exceptions.html#UnicodeEncodeError "UnicodeEncodeError")
.

sys.dont\_write\_bytecode[¶](https://docs.python.org/3/library/sys.html#sys.dont_write_bytecode "Link to this definition")

If this is true, Python won’t try to write `.pyc` files on the import of source modules. This value is initially set to `True` or `False` depending on the [`-B`](https://docs.python.org/3/using/cmdline.html#cmdoption-B)
 command line option and the [`PYTHONDONTWRITEBYTECODE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE)
 environment variable, but you can set it yourself to control bytecode file generation.

sys.\_emscripten\_info[¶](https://docs.python.org/3/library/sys.html#sys._emscripten_info "Link to this definition")

A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 holding information about the environment on the _wasm32-emscripten_ platform. The named tuple is provisional and may change in the future.

\_emscripten\_info.emscripten\_version[¶](https://docs.python.org/3/library/sys.html#sys._emscripten_info.emscripten_version "Link to this definition")

Emscripten version as tuple of ints (major, minor, micro), e.g. `(3, 1, 8)`.

\_emscripten\_info.runtime[¶](https://docs.python.org/3/library/sys.html#sys._emscripten_info.runtime "Link to this definition")

Runtime string, e.g. browser user agent, `'Node.js v14.18.2'`, or `'UNKNOWN'`.

\_emscripten\_info.pthreads[¶](https://docs.python.org/3/library/sys.html#sys._emscripten_info.pthreads "Link to this definition")

`True` if Python is compiled with Emscripten pthreads support.

\_emscripten\_info.shared\_memory[¶](https://docs.python.org/3/library/sys.html#sys._emscripten_info.shared_memory "Link to this definition")

`True` if Python is compiled with shared memory support.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Emscripten.

Added in version 3.11.

sys.pycache\_prefix[¶](https://docs.python.org/3/library/sys.html#sys.pycache_prefix "Link to this definition")

If this is set (not `None`), Python will write bytecode-cache `.pyc` files to (and read them from) a parallel directory tree rooted at this directory, rather than from `__pycache__` directories in the source code tree. Any `__pycache__` directories in the source code tree will be ignored and new `.pyc` files written within the pycache prefix. Thus if you use [`compileall`](https://docs.python.org/3/library/compileall.html#module-compileall "compileall: Tools for byte-compiling all Python source files in a directory tree.")
 as a pre-build step, you must ensure you run it with the same pycache prefix (if any) that you will use at runtime.

A relative path is interpreted relative to the current working directory.

This value is initially set based on the value of the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `pycache_prefix=PATH` command-line option or the [`PYTHONPYCACHEPREFIX`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPYCACHEPREFIX)
 environment variable (command-line takes precedence). If neither are set, it is `None`.

Added in version 3.8.

sys.excepthook(_type_, _value_, _traceback_)[¶](https://docs.python.org/3/library/sys.html#sys.excepthook "Link to this definition")

This function prints out a given traceback and exception to `sys.stderr`.

When an exception other than [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
 is raised and uncaught, the interpreter calls `sys.excepthook` with three arguments, the exception class, exception instance, and a traceback object. In an interactive session this happens just before control is returned to the prompt; in a Python program this happens just before the program exits. The handling of such top-level exceptions can be customized by assigning another three-argument function to `sys.excepthook`.

Raise an auditing event `sys.excepthook` with arguments `hook`, `type`, `value`, `traceback` when an uncaught exception occurs. If no hook has been set, `hook` may be `None`. If any hook raises an exception derived from [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError "RuntimeError")
 the call to the hook will be suppressed. Otherwise, the audit hook exception will be reported as unraisable and `sys.excepthook` will be called.

See also

The [`sys.unraisablehook()`](https://docs.python.org/3/library/sys.html#sys.unraisablehook "sys.unraisablehook")
 function handles unraisable exceptions and the [`threading.excepthook()`](https://docs.python.org/3/library/threading.html#threading.excepthook "threading.excepthook")
 function handles exception raised by [`threading.Thread.run()`](https://docs.python.org/3/library/threading.html#threading.Thread.run "threading.Thread.run")
.

sys.\_\_breakpointhook\_\_[¶](https://docs.python.org/3/library/sys.html#sys.__breakpointhook__ "Link to this definition")

sys.\_\_displayhook\_\_[¶](https://docs.python.org/3/library/sys.html#sys.__displayhook__ "Link to this definition")

sys.\_\_excepthook\_\_[¶](https://docs.python.org/3/library/sys.html#sys.__excepthook__ "Link to this definition")

sys.\_\_unraisablehook\_\_[¶](https://docs.python.org/3/library/sys.html#sys.__unraisablehook__ "Link to this definition")

These objects contain the original values of `breakpointhook`, `displayhook`, `excepthook`, and `unraisablehook` at the start of the program. They are saved so that `breakpointhook`, `displayhook` and `excepthook`, `unraisablehook` can be restored in case they happen to get replaced with broken or alternative objects.

Added in version 3.7: \_\_breakpointhook\_\_

Added in version 3.8: \_\_unraisablehook\_\_

sys.exception()[¶](https://docs.python.org/3/library/sys.html#sys.exception "Link to this definition")

This function, when called while an exception handler is executing (such as an `except` or `except*` clause), returns the exception instance that was caught by this handler. When exception handlers are nested within one another, only the exception handled by the innermost handler is accessible.

If no exception handler is executing, this function returns `None`.

Added in version 3.11.

sys.exc\_info()[¶](https://docs.python.org/3/library/sys.html#sys.exc_info "Link to this definition")

This function returns the old-style representation of the handled exception. If an exception `e` is currently handled (so [`exception()`](https://docs.python.org/3/library/sys.html#sys.exception "sys.exception")
 would return `e`), `exc_info()` returns the tuple `(type(e), e, e.__traceback__)`. That is, a tuple containing the type of the exception (a subclass of [`BaseException`](https://docs.python.org/3/builtins/exceptions.html#BaseException "BaseException")
), the exception itself, and a [traceback object](https://docs.python.org/3/reference/datamodel.html#traceback-objects)
 which typically encapsulates the call stack at the point where the exception last occurred.

If no exception is being handled anywhere on the stack, this function return a tuple containing three `None` values.

Changed in version 3.11: The `type` and `traceback` fields are now derived from the `value` (the exception instance), so when an exception is modified while it is being handled, the changes are reflected in the results of subsequent calls to `exc_info()`.

sys.exec\_prefix[¶](https://docs.python.org/3/library/sys.html#sys.exec_prefix "Link to this definition")

A string giving the site-specific directory prefix where the platform-dependent Python files are installed; by default, this is also `'/usr/local'`. This can be set at build time with the `--exec-prefix` argument to the **configure** script. Specifically, all configuration files (e.g. the `pyconfig.h` header file) are installed in the directory `_exec_prefix_/lib/python_X.Y_/config`, and shared library modules are installed in `_exec_prefix_/lib/python_X.Y_/lib-dynload`, where _X.Y_ is the version number of Python, for example `3.2`.

Note

If a [virtual environment](https://docs.python.org/3/library/venv.html#venv-def)
 is in effect, this `exec_prefix` will point to the virtual environment. The value for the Python installation will still be available, via [`base_exec_prefix`](https://docs.python.org/3/library/sys.html#sys.base_exec_prefix "sys.base_exec_prefix")
. Refer to [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments)
 for more information.

Changed in version 3.14: When running under a [virtual environment](https://docs.python.org/3/library/venv.html#venv-def)
, [`prefix`](https://docs.python.org/3/library/sys.html#sys.prefix "sys.prefix")
 and `exec_prefix` are now set to the virtual environment prefix by the [path initialization](https://docs.python.org/3/library/sys_path_init.html#sys-path-init)
, instead of [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")
. This means that `prefix` and `exec_prefix` always point to the virtual environment, even when `site` is disabled ([`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S)
).

sys.executable[¶](https://docs.python.org/3/library/sys.html#sys.executable "Link to this definition")

A string giving the absolute path of the executable binary for the Python interpreter, on systems where this makes sense. If Python is unable to retrieve the real path to its executable, `sys.executable` will be an empty string or `None`.

sys.exit(\[_arg_\])[¶](https://docs.python.org/3/library/sys.html#sys.exit "Link to this definition")

Raise a [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
 exception, signaling an intention to exit the interpreter.

The optional argument _arg_ can be an integer giving the exit status (defaulting to zero), or another type of object. If it is an integer, zero is considered “successful termination” and any nonzero value is considered “abnormal termination” by shells and the like. Most systems require it to be in the range 0–127, and produce undefined results otherwise. Some systems have a convention for assigning specific meanings to specific exit codes, but these are generally underdeveloped; Unix programs generally use 2 for command line syntax errors and 1 for all other kinds of errors. If another type of object is passed, `None` is equivalent to passing zero, and any other object is printed to [`stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr")
 and results in an exit code of 1. In particular, `sys.exit("some error message")` is a quick way to exit a program when an error occurs.

Since `exit()` ultimately “only” raises an exception, it will only exit the process when called from the main thread, and the exception is not intercepted. Cleanup actions specified by [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 clauses of [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 statements are honored, and it is possible to intercept the exit attempt at an outer level.

Changed in version 3.6: If an error occurs in the cleanup after the Python interpreter has caught [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
 (such as an error flushing buffered data in the standard streams), the exit status is changed to 120.

sys.flags[¶](https://docs.python.org/3/library/sys.html#sys.flags "Link to this definition")

The [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 _flags_ exposes the status of command line flags. Flags should only be accessed only by name and not by index. The attributes are read only.

|     |     |
| --- | --- |
| flags.debug[¶](https://docs.python.org/3/library/sys.html#sys.flags.debug "Link to this definition") | [`-d`](https://docs.python.org/3/using/cmdline.html#cmdoption-d) |
| flags.inspect[¶](https://docs.python.org/3/library/sys.html#sys.flags.inspect "Link to this definition") | [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i) |
| flags.interactive[¶](https://docs.python.org/3/library/sys.html#sys.flags.interactive "Link to this definition") | [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i) |
| flags.isolated[¶](https://docs.python.org/3/library/sys.html#sys.flags.isolated "Link to this definition") | [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I) |
| flags.optimize[¶](https://docs.python.org/3/library/sys.html#sys.flags.optimize "Link to this definition") | [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O)<br> or [`-OO`](https://docs.python.org/3/using/cmdline.html#cmdoption-OO) |
| flags.dont\_write\_bytecode[¶](https://docs.python.org/3/library/sys.html#sys.flags.dont_write_bytecode "Link to this definition") | [`-B`](https://docs.python.org/3/using/cmdline.html#cmdoption-B) |
| flags.no\_user\_site[¶](https://docs.python.org/3/library/sys.html#sys.flags.no_user_site "Link to this definition") | [`-s`](https://docs.python.org/3/using/cmdline.html#cmdoption-s) |
| flags.no\_site[¶](https://docs.python.org/3/library/sys.html#sys.flags.no_site "Link to this definition") | [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S) |
| flags.ignore\_environment[¶](https://docs.python.org/3/library/sys.html#sys.flags.ignore_environment "Link to this definition") | [`-E`](https://docs.python.org/3/using/cmdline.html#cmdoption-E) |
| flags.verbose[¶](https://docs.python.org/3/library/sys.html#sys.flags.verbose "Link to this definition") | [`-v`](https://docs.python.org/3/using/cmdline.html#cmdoption-v) |
| flags.bytes\_warning[¶](https://docs.python.org/3/library/sys.html#sys.flags.bytes_warning "Link to this definition") | [`-b`](https://docs.python.org/3/using/cmdline.html#cmdoption-b) |
| flags.quiet[¶](https://docs.python.org/3/library/sys.html#sys.flags.quiet "Link to this definition") | [`-q`](https://docs.python.org/3/using/cmdline.html#cmdoption-q) |
| flags.hash\_randomization[¶](https://docs.python.org/3/library/sys.html#sys.flags.hash_randomization "Link to this definition") | [`-R`](https://docs.python.org/3/using/cmdline.html#cmdoption-R) |
| flags.dev\_mode[¶](https://docs.python.org/3/library/sys.html#sys.flags.dev_mode "Link to this definition") | [`-X dev`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)<br> ([Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)<br>) |
| flags.utf8\_mode[¶](https://docs.python.org/3/library/sys.html#sys.flags.utf8_mode "Link to this definition") | [`-X utf8`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) |
| flags.safe\_path[¶](https://docs.python.org/3/library/sys.html#sys.flags.safe_path "Link to this definition") | [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P) |
| flags.int\_max\_str\_digits[¶](https://docs.python.org/3/library/sys.html#sys.flags.int_max_str_digits "Link to this definition") | [`-X int_max_str_digits`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)<br> ([integer string conversion length limitation](https://docs.python.org/3/builtins/stdtypes.html#int-max-str-digits)<br>) |
| flags.warn\_default\_encoding[¶](https://docs.python.org/3/library/sys.html#sys.flags.warn_default_encoding "Link to this definition") | [`-X warn_default_encoding`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) |
| flags.gil[¶](https://docs.python.org/3/library/sys.html#sys.flags.gil "Link to this definition") | [`-X gil`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)<br> and [`PYTHON_GIL`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_GIL) |
| flags.thread\_inherit\_context[¶](https://docs.python.org/3/library/sys.html#sys.flags.thread_inherit_context "Link to this definition") | [`-X thread_inherit_context`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)<br> and [`PYTHON_THREAD_INHERIT_CONTEXT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_THREAD_INHERIT_CONTEXT) |
| flags.context\_aware\_warnings[¶](https://docs.python.org/3/library/sys.html#sys.flags.context_aware_warnings "Link to this definition") | [`-X context_aware_warnings`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)<br> and [`PYTHON_CONTEXT_AWARE_WARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_CONTEXT_AWARE_WARNINGS) |
| flags.lazy\_imports[¶](https://docs.python.org/3/library/sys.html#sys.flags.lazy_imports "Link to this definition") | [`-X lazy_imports`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)<br> and [`PYTHON_LAZY_IMPORTS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_LAZY_IMPORTS)<br> (`1` for `all`, `-1` otherwise; not changed by [`set_lazy_imports()`](https://docs.python.org/3/library/sys.html#sys.set_lazy_imports "sys.set_lazy_imports")<br>) |

Changed in version 3.2: Added `quiet` attribute for the new [`-q`](https://docs.python.org/3/using/cmdline.html#cmdoption-q)
 flag.

Added in version 3.2.3: The `hash_randomization` attribute.

Changed in version 3.3: Removed obsolete `division_warning` attribute.

Changed in version 3.4: Added `isolated` attribute for [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I)
 `isolated` flag.

Changed in version 3.7: Added the `dev_mode` attribute for the new [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode)
 and the `utf8_mode` attribute for the new [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `utf8` flag.

Changed in version 3.10: Added `warn_default_encoding` attribute for [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `warn_default_encoding` flag.

Changed in version 3.11: Added the `safe_path` attribute for [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P)
 option.

Changed in version 3.11: Added the `int_max_str_digits` attribute.

Changed in version 3.13: Added the `gil` attribute.

Changed in version 3.14: Added the `thread_inherit_context` attribute.

Changed in version 3.14: Added the `context_aware_warnings` attribute.

Changed in version 3.15: Added the `lazy_imports` attribute.

sys.float\_info[¶](https://docs.python.org/3/library/sys.html#sys.float_info "Link to this definition")

A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 holding information about the float type. It contains low level information about the precision and internal representation. The values correspond to the various floating-point constants defined in the standard header file `float.h` for the ‘C’ programming language; see section 5.2.4.2.2 of the 1999 ISO/IEC C standard [\[C99\]](https://docs.python.org/3/library/sys.html#c99)
, ‘Characteristics of floating types’, for details.

|     |     |     |
| --- | --- | --- |Attributes of the `float_info` [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
[¶](https://docs.python.org/3/library/sys.html#id2 "Link to this table")
| attribute | float.h macro | explanation |
| --- | --- | --- |
| float\_info.epsilon[¶](https://docs.python.org/3/library/sys.html#sys.float_info.epsilon "Link to this definition") | `DBL_EPSILON` | difference between 1.0 and the least value greater than 1.0 that is representable as a float.<br><br>See also [`math.ulp()`](https://docs.python.org/3/library/math.html#math.ulp "math.ulp")<br>. |
| float\_info.dig[¶](https://docs.python.org/3/library/sys.html#sys.float_info.dig "Link to this definition") | `DBL_DIG` | The maximum number of decimal digits that can be faithfully represented in a float; see below. |
| float\_info.mant\_dig[¶](https://docs.python.org/3/library/sys.html#sys.float_info.mant_dig "Link to this definition") | `DBL_MANT_DIG` | Float precision: the number of base-`radix` digits in the significand of a float. |
| float\_info.max[¶](https://docs.python.org/3/library/sys.html#sys.float_info.max "Link to this definition") | `DBL_MAX` | The maximum representable positive finite float. |
| float\_info.max\_exp[¶](https://docs.python.org/3/library/sys.html#sys.float_info.max_exp "Link to this definition") | `DBL_MAX_EXP` | The maximum integer _e_ such that `radix**(e-1)` is a representable finite float. |
| float\_info.max\_10\_exp[¶](https://docs.python.org/3/library/sys.html#sys.float_info.max_10_exp "Link to this definition") | `DBL_MAX_10_EXP` | The maximum integer _e_ such that `10**e` is in the range of representable finite floats. |
| float\_info.min[¶](https://docs.python.org/3/library/sys.html#sys.float_info.min "Link to this definition") | `DBL_MIN` | The minimum representable positive _normalized_ float.<br><br>Use [`math.ulp(0.0)`](https://docs.python.org/3/library/math.html#math.ulp "math.ulp")<br> to get the smallest positive _denormalized_ representable float. |
| float\_info.min\_exp[¶](https://docs.python.org/3/library/sys.html#sys.float_info.min_exp "Link to this definition") | `DBL_MIN_EXP` | The minimum integer _e_ such that `radix**(e-1)` is a normalized float. |
| float\_info.min\_10\_exp[¶](https://docs.python.org/3/library/sys.html#sys.float_info.min_10_exp "Link to this definition") | `DBL_MIN_10_EXP` | The minimum integer _e_ such that `10**e` is a normalized float. |
| float\_info.radix[¶](https://docs.python.org/3/library/sys.html#sys.float_info.radix "Link to this definition") | `FLT_RADIX` | The radix of exponent representation. |
| float\_info.rounds[¶](https://docs.python.org/3/library/sys.html#sys.float_info.rounds "Link to this definition") | `FLT_ROUNDS` | An integer representing the rounding mode for floating-point arithmetic. This reflects the value of the system `FLT_ROUNDS` macro at interpreter startup time:<br><br>*   `-1`: indeterminable<br>    <br>*   `0`: toward zero<br>    <br>*   `1`: to nearest<br>    <br>*   `2`: toward positive infinity<br>    <br>*   `3`: toward negative infinity<br>    <br><br>All other values for `FLT_ROUNDS` characterize implementation-defined rounding behavior. |

The attribute [`sys.float_info.dig`](https://docs.python.org/3/library/sys.html#sys.float_info.dig "sys.float_info.dig")
 needs further explanation. If `s` is any string representing a decimal number with at most `sys.float_info.dig` significant digits, then converting `s` to a float and back again will recover a string representing the same decimal value:

Copy

\>>> import sys
\>>> sys.float\_info.dig
15
\>>> s \= '3.14159265358979'    \# decimal string with 15 significant digits
\>>> format(float(s), '.15g')  \# convert to float and back -> same value
'3.14159265358979'

But for strings with more than [`sys.float_info.dig`](https://docs.python.org/3/library/sys.html#sys.float_info.dig "sys.float_info.dig")
 significant digits, this isn’t always true:

Copy

\>>> s \= '9876543211234567'    \# 16 significant digits is too many!
\>>> format(float(s), '.16g')  \# conversion changes value
'9876543211234568'

sys.float\_repr\_style[¶](https://docs.python.org/3/library/sys.html#sys.float_repr_style "Link to this definition")

A string indicating how the [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
 function behaves for floats. If the string has value `'short'` then for a finite float `x`, `repr(x)` aims to produce a short string with the property that `float(repr(x)) == x`. This is the usual behaviour in Python 3.1 and later. Otherwise, `float_repr_style` has value `'legacy'` and `repr(x)` behaves in the same way as it did in versions of Python prior to 3.1.

Added in version 3.1.

sys.getallocatedblocks()[¶](https://docs.python.org/3/library/sys.html#sys.getallocatedblocks "Link to this definition")

Return the number of memory blocks currently allocated by the interpreter, regardless of their size. This function is mainly useful for tracking and debugging memory leaks. Because of the interpreter’s internal caches, the result can vary from call to call; you may have to call [`_clear_internal_caches()`](https://docs.python.org/3/library/sys.html#sys._clear_internal_caches "sys._clear_internal_caches")
 and [`gc.collect()`](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect")
 to get more predictable results.

If a Python build or implementation cannot reasonably compute this information, `getallocatedblocks()` is allowed to return 0 instead.

Added in version 3.4.

sys.getunicodeinternedsize()[¶](https://docs.python.org/3/library/sys.html#sys.getunicodeinternedsize "Link to this definition")

Return the number of unicode objects that have been interned.

Added in version 3.12.

sys.getandroidapilevel()[¶](https://docs.python.org/3/library/sys.html#sys.getandroidapilevel "Link to this definition")

Return the build-time API level of Android as an integer. This represents the minimum version of Android this build of Python can run on. For runtime version information, see [`platform.android_ver()`](https://docs.python.org/3/library/platform.html#platform.android_ver "platform.android_ver")
.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Android.

Added in version 3.7.

sys.getdefaultencoding()[¶](https://docs.python.org/3/library/sys.html#sys.getdefaultencoding "Link to this definition")

Return `'utf-8'`. This is the name of the default string encoding, used in methods like [`str.encode()`](https://docs.python.org/3/builtins/stdtypes.html#str.encode "str.encode")
.

sys.getdlopenflags()[¶](https://docs.python.org/3/library/sys.html#sys.getdlopenflags "Link to this definition")

Return the current value of the flags that are used for `dlopen()` calls. Symbolic names for the flag values can be found in the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
 module (`RTLD__xxx_` constants, e.g. [`os.RTLD_LAZY`](https://docs.python.org/3/library/os.html#os.RTLD_LAZY "os.RTLD_LAZY")
).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

sys.getfilesystemencoding()[¶](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "Link to this definition")

Get the [filesystem encoding](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
: the encoding used with the filesystem error handler to convert between Unicode filenames and bytes filenames. The filesystem error handler is returned from [`getfilesystemencodeerrors()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencodeerrors "sys.getfilesystemencodeerrors")
.

For best compatibility, str should be used for filenames in all cases, although representing filenames as bytes is also supported. Functions accepting or returning filenames should support either str or bytes and internally convert to the system’s preferred representation.

[`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode")
 and [`os.fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode")
 should be used to ensure that the correct encoding and errors mode are used.

The [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 are configured at Python startup by the [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read")
 function: see [`filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")
 and [`filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")
 members of [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
.

Changed in version 3.2: `getfilesystemencoding()` result cannot be `None` anymore.

Changed in version 3.6: Windows is no longer guaranteed to return `'mbcs'`. See [**PEP 529**](https://peps.python.org/pep-0529/)
 and [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3/library/sys.html#sys._enablelegacywindowsfsencoding "sys._enablelegacywindowsfsencoding")
 for more information.

Changed in version 3.7: Return `'utf-8'` if the [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)
 is enabled.

sys.getfilesystemencodeerrors()[¶](https://docs.python.org/3/library/sys.html#sys.getfilesystemencodeerrors "Link to this definition")

Get the [filesystem error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
: the error handler used with the filesystem encoding to convert between Unicode filenames and bytes filenames. The filesystem encoding is returned from [`getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding")
.

[`os.fsencode()`](https://docs.python.org/3/library/os.html#os.fsencode "os.fsencode")
 and [`os.fsdecode()`](https://docs.python.org/3/library/os.html#os.fsdecode "os.fsdecode")
 should be used to ensure that the correct encoding and errors mode are used.

The [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
 are configured at Python startup by the [`PyConfig_Read()`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig_Read "PyConfig_Read")
 function: see [`filesystem_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_encoding "PyConfig.filesystem_encoding")
 and [`filesystem_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.filesystem_errors "PyConfig.filesystem_errors")
 members of [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
.

Added in version 3.6.

sys.get\_int\_max\_str\_digits()[¶](https://docs.python.org/3/library/sys.html#sys.get_int_max_str_digits "Link to this definition")

Returns the current value for the [integer string conversion length limitation](https://docs.python.org/3/builtins/stdtypes.html#int-max-str-digits)
. See also [`set_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.set_int_max_str_digits "sys.set_int_max_str_digits")
.

Added in version 3.11.

sys.get\_lazy\_imports()[¶](https://docs.python.org/3/library/sys.html#sys.get_lazy_imports "Link to this definition")

Returns the current lazy imports mode as a string.

*   `"normal"`: Only imports explicitly marked with the `lazy` keyword are lazy
    
*   `"all"`: All top-level imports are potentially lazy
    

See also [`set_lazy_imports()`](https://docs.python.org/3/library/sys.html#sys.set_lazy_imports "sys.set_lazy_imports")
 and [**PEP 810**](https://peps.python.org/pep-0810/)
.

Added in version 3.15.

sys.get\_lazy\_imports\_filter()[¶](https://docs.python.org/3/library/sys.html#sys.get_lazy_imports_filter "Link to this definition")

Returns the current lazy imports filter function, or `None` if no filter is set.

The filter function is called for every potentially lazy import to determine whether it should actually be lazy. See [`set_lazy_imports_filter()`](https://docs.python.org/3/library/sys.html#sys.set_lazy_imports_filter "sys.set_lazy_imports_filter")
 for details on the filter function signature.

Added in version 3.15.

sys.getrefcount(_object_)[¶](https://docs.python.org/3/library/sys.html#sys.getrefcount "Link to this definition")

Return the reference count of the _object_. The count returned is generally one higher than you might expect, because it includes the (temporary) reference as an argument to `getrefcount()`.

Note that the returned value may not actually reflect how many references to the object are actually held. For example, some objects are [immortal](https://docs.python.org/3/glossary.html#term-immortal)
 and have a very high refcount that does not reflect the actual number of references. Consequently, do not rely on the returned value to be accurate, other than a value of 0 or 1.

**CPython implementation detail:** [Immortal](https://docs.python.org/3/glossary.html#term-immortal)
 objects with a large reference count can be identified via [`_is_immortal()`](https://docs.python.org/3/library/sys.html#sys._is_immortal "sys._is_immortal")
.

Changed in version 3.12: Immortal objects have very large refcounts that do not match the actual number of references to the object.

sys.getrecursionlimit()[¶](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit "Link to this definition")

Return the current value of the recursion limit, the maximum depth of the Python interpreter stack. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. It can be set by [`setrecursionlimit()`](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit "sys.setrecursionlimit")
.

sys.getsizeof(_object_\[, _default_\])[¶](https://docs.python.org/3/library/sys.html#sys.getsizeof "Link to this definition")

Return the size of an object in bytes. The object can be any type of object. All built-in objects will return correct results, but this does not have to hold true for third-party extensions as it is implementation specific.

Only the memory consumption directly attributed to the object is accounted for, not the memory consumption of objects it refers to.

If given, _default_ will be returned if the object does not provide means to retrieve the size. Otherwise a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 will be raised.

`getsizeof()` calls the object’s `__sizeof__` method and adds an additional garbage collector overhead if the object is managed by the garbage collector.

See [recursive sizeof recipe](https://code.activestate.com/recipes/577504-compute-memory-footprint-of-an-object-and-its-cont/)
 for an example of using `getsizeof()` recursively to find the size of containers and all their contents.

sys.getswitchinterval()[¶](https://docs.python.org/3/library/sys.html#sys.getswitchinterval "Link to this definition")

Return the interpreter’s “thread switch interval” in seconds; see [`setswitchinterval()`](https://docs.python.org/3/library/sys.html#sys.setswitchinterval "sys.setswitchinterval")
.

Added in version 3.2.

sys.\_getframe(\[_depth_\])[¶](https://docs.python.org/3/library/sys.html#sys._getframe "Link to this definition")

Return a frame object from the call stack. If optional integer _depth_ is given, return the frame object that many calls below the top of the stack. If that is deeper than the call stack, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. The default for _depth_ is zero, returning the frame at the top of the call stack.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `sys._getframe` with argument `frame`.

**CPython implementation detail:** This function should be used for internal and specialized purposes only. It is not guaranteed to exist in all implementations of Python.

sys.\_getframemodulename(\[_depth_\])[¶](https://docs.python.org/3/library/sys.html#sys._getframemodulename "Link to this definition")

Return the name of a module from the call stack. If optional integer _depth_ is given, return the module that many calls below the top of the stack. If that is deeper than the call stack, or if the module is unidentifiable, `None` is returned. The default for _depth_ is zero, returning the module at the top of the call stack.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)
 `sys._getframemodulename` with argument `depth`.

**CPython implementation detail:** This function should be used for internal and specialized purposes only. It is not guaranteed to exist in all implementations of Python.

Added in version 3.12.

sys.getobjects(_limit_\[, _type_\])[¶](https://docs.python.org/3/library/sys.html#sys.getobjects "Link to this definition")

This function only exists if CPython was built using the specialized configure option [`--with-trace-refs`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs)
. It is intended only for debugging garbage-collection issues.

Return a list of up to _limit_ dynamically allocated Python objects. If _type_ is given, only objects of that exact type (not subtypes) are included.

Objects from the list are not safe to use. Specifically, the result will include objects from all interpreters that share their object allocator state (that is, ones created with [`PyInterpreterConfig.use_main_obmalloc`](https://docs.python.org/3/c-api/subinterpreters.html#c.PyInterpreterConfig.use_main_obmalloc "PyInterpreterConfig.use_main_obmalloc")
 set to 1 or using [`Py_NewInterpreter()`](https://docs.python.org/3/c-api/subinterpreters.html#c.Py_NewInterpreter "Py_NewInterpreter")
, and the [main interpreter](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
). Mixing objects from different interpreters may lead to crashes or other unexpected behavior.

**CPython implementation detail:** This function should be used for specialized purposes only. It is not guaranteed to exist in all implementations of Python.

Changed in version 3.14: The result may include objects from other interpreters.

sys.getprofile()[¶](https://docs.python.org/3/library/sys.html#sys.getprofile "Link to this definition")

Get the profiler function as set by [`setprofile()`](https://docs.python.org/3/library/sys.html#sys.setprofile "sys.setprofile")
.

sys.gettrace()[¶](https://docs.python.org/3/library/sys.html#sys.gettrace "Link to this definition")

Get the trace function as set by [`settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace")
.

**CPython implementation detail:** The `gettrace()` function is intended only for implementing debuggers, profilers, coverage tools and the like. Its behavior is part of the implementation platform, rather than part of the language definition, and thus may not be available in all Python implementations.

sys.getwindowsversion()[¶](https://docs.python.org/3/library/sys.html#sys.getwindowsversion "Link to this definition")

Return a named tuple describing the Windows version currently running. The named elements are _major_, _minor_, _build_, _platform_, _service\_pack_, _service\_pack\_minor_, _service\_pack\_major_, _suite\_mask_, _product\_type_ and _platform\_version_. _service\_pack_ contains a string, _platform\_version_ a 3-tuple and all other values are integers. The components can also be accessed by name, so `sys.getwindowsversion()[0]` is equivalent to `sys.getwindowsversion().major`. For compatibility with prior versions, only the first 5 elements are retrievable by indexing.

_platform_ will be `2` (VER\_PLATFORM\_WIN32\_NT).

_product\_type_ may be one of the following values:

| Constant | Meaning |
| --- | --- |
| `1` (VER\_NT\_WORKSTATION) | The system is a workstation. |
| `2` (VER\_NT\_DOMAIN\_CONTROLLER) | The system is a domain controller. |
| `3` (VER\_NT\_SERVER) | The system is a server, but not a domain controller. |

This function wraps the Win32 `GetVersionEx()` function; see the Microsoft documentation on `OSVERSIONINFOEX()` for more information about these fields.

_platform\_version_ returns the major version, minor version and build number of the current operating system, rather than the version that is being emulated for the process. It is intended for use in logging rather than for feature detection.

Note

_platform\_version_ derives the version from kernel32.dll which can be of a different version than the OS version. Please use [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")
 module for achieving accurate OS version.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Windows.

Changed in version 3.2: Changed to a named tuple and added _service\_pack\_minor_, _service\_pack\_major_, _suite\_mask_, and _product\_type_.

Changed in version 3.6: Added _platform\_version_

sys.get\_asyncgen\_hooks()[¶](https://docs.python.org/3/library/sys.html#sys.get_asyncgen_hooks "Link to this definition")

Returns an _asyncgen\_hooks_ object, which is similar to a [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple")
 of the form `(firstiter, finalizer)`, where _firstiter_ and _finalizer_ are expected to be either `None` or functions which take an [asynchronous generator iterator](https://docs.python.org/3/glossary.html#term-asynchronous-generator-iterator)
 as an argument, and are used to schedule finalization of an asynchronous generator by an event loop.

Added in version 3.6: See [**PEP 525**](https://peps.python.org/pep-0525/)
 for more details.

Note

This function has been added on a provisional basis (see [**PEP 411**](https://peps.python.org/pep-0411/)
 for details.)

sys.get\_coroutine\_origin\_tracking\_depth()[¶](https://docs.python.org/3/library/sys.html#sys.get_coroutine_origin_tracking_depth "Link to this definition")

Get the current coroutine origin tracking depth, as set by [`set_coroutine_origin_tracking_depth()`](https://docs.python.org/3/library/sys.html#sys.set_coroutine_origin_tracking_depth "sys.set_coroutine_origin_tracking_depth")
.

Added in version 3.7.

Note

This function has been added on a provisional basis (see [**PEP 411**](https://peps.python.org/pep-0411/)
 for details.) Use it only for debugging purposes.

sys.hash\_info[¶](https://docs.python.org/3/library/sys.html#sys.hash_info "Link to this definition")

A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 giving parameters of the numeric hash implementation. For more details about hashing of numeric types, see [Hashing of numeric types](https://docs.python.org/3/builtins/stdtypes.html#numeric-hash)
.

hash\_info.width[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.width "Link to this definition")

The width in bits used for hash values

hash\_info.modulus[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.modulus "Link to this definition")

The prime modulus P used for numeric hash scheme

hash\_info.inf[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.inf "Link to this definition")

The hash value returned for a positive infinity

hash\_info.nan[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.nan "Link to this definition")

(This attribute is no longer used)

hash\_info.imag[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.imag "Link to this definition")

The multiplier used for the imaginary part of a complex number

hash\_info.algorithm[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.algorithm "Link to this definition")

The name of the algorithm for hashing of str, bytes, and memoryview

hash\_info.hash\_bits[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.hash_bits "Link to this definition")

The internal output size of the hash algorithm

hash\_info.seed\_bits[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.seed_bits "Link to this definition")

The size of the seed key of the hash algorithm

hash\_info.cutoff[¶](https://docs.python.org/3/library/sys.html#sys.hash_info.cutoff "Link to this definition")

Cutoff for small string DJBX33A optimization in range `[1, cutoff)`.\
\
Added in version 3.2.\
\
Changed in version 3.4: Added _algorithm_, _hash\_bits_, _seed\_bits_, and _cutoff_.\
\
sys.hexversion[¶](https://docs.python.org/3/library/sys.html#sys.hexversion "Link to this definition")\
\
The version number encoded as a single integer. This is guaranteed to increase with each version, including proper support for non-production releases. For example, to test that the Python interpreter is at least version 1.5.2, use:\
\
Copy\
\
if sys.hexversion \>= 0x010502F0:\
    \# use some advanced feature\
    ...\
else:\
    \# use an alternative implementation or warn the user\
    ...\
\
This is called `hexversion` since it only really looks meaningful when viewed as the result of passing it to the built-in [`hex()`](https://docs.python.org/3/builtins/functions.html#hex "hex")\
 function. The [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)\
 [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")\
 may be used for a more human-friendly encoding of the same information.\
\
More details of `hexversion` can be found at [API and ABI Versioning](https://docs.python.org/3/c-api/apiabiversion.html#apiabiversion)\
.\
\
sys.implementation[¶](https://docs.python.org/3/library/sys.html#sys.implementation "Link to this definition")\
\
An object containing information about the implementation of the currently running Python interpreter. The following attributes are required to exist in all Python implementations.\
\
_name_ is the implementation’s identifier, e.g. `'cpython'`. The actual string is defined by the Python implementation, but it is guaranteed to be lower case.\
\
_version_ is a named tuple, in the same format as [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")\
. It represents the version of the Python _implementation_. This has a distinct meaning from the specific version of the Python _language_ to which the currently running interpreter conforms, which `sys.version_info` represents. For example, for PyPy 1.8 `sys.implementation.version` might be `sys.version_info(1, 8, 0, 'final', 0)`, whereas `sys.version_info` would be `sys.version_info(2, 7, 2, 'final', 0)`. For CPython they are the same value, since it is the reference implementation.\
\
_hexversion_ is the implementation version in hexadecimal format, like [`sys.hexversion`](https://docs.python.org/3/library/sys.html#sys.hexversion "sys.hexversion")\
.\
\
_cache\_tag_ is the tag used by the import machinery in the filenames of cached modules. By convention, it would be a composite of the implementation’s name and version, like `'cpython-33'`. However, a Python implementation may use some other value if appropriate. If `cache_tag` is set to `None`, it indicates that module caching should be disabled.\
\
_supports\_isolated\_interpreters_ is a boolean value, whether this implementation supports multiple isolated interpreters. It is `True` for CPython on most platforms. Platforms with this support implement the low-level `_interpreters` module.\
\
See also\
\
[**PEP 684**](https://peps.python.org/pep-0684/)\
, [**PEP 734**](https://peps.python.org/pep-0734/)\
, and [`concurrent.interpreters`](https://docs.python.org/3/library/concurrent.interpreters.html#module-concurrent.interpreters "concurrent.interpreters: Multiple interpreters in the same process")\
.\
\
`sys.implementation` may contain additional attributes specific to the Python implementation. These non-standard attributes must start with an underscore, and are not described here. Regardless of its contents, `sys.implementation` will not change during a run of the interpreter, nor between implementation versions. (It may change between Python language versions, however.) See [**PEP 421**](https://peps.python.org/pep-0421/)\
 for more information.\
\
Added in version 3.3.\
\
Changed in version 3.14: Added `supports_isolated_interpreters` field.\
\
Note\
\
The addition of new required attributes must go through the normal PEP process. See [**PEP 421**](https://peps.python.org/pep-0421/)\
 for more information.\
\
sys.int\_info[¶](https://docs.python.org/3/library/sys.html#sys.int_info "Link to this definition")\
\
A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)\
 that holds information about Python’s internal representation of integers. The attributes are read only.\
\
int\_info.bits\_per\_digit[¶](https://docs.python.org/3/library/sys.html#sys.int_info.bits_per_digit "Link to this definition")\
\
The number of bits held in each digit. Python integers are stored internally in base `2**int_info.bits_per_digit`.\
\
int\_info.sizeof\_digit[¶](https://docs.python.org/3/library/sys.html#sys.int_info.sizeof_digit "Link to this definition")\
\
The size in bytes of the C type used to represent a digit.\
\
int\_info.default\_max\_str\_digits[¶](https://docs.python.org/3/library/sys.html#sys.int_info.default_max_str_digits "Link to this definition")\
\
The default value for [`sys.get_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.get_int_max_str_digits "sys.get_int_max_str_digits")\
 when it is not otherwise explicitly configured.\
\
int\_info.str\_digits\_check\_threshold[¶](https://docs.python.org/3/library/sys.html#sys.int_info.str_digits_check_threshold "Link to this definition")\
\
The minimum non-zero value for [`sys.set_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.set_int_max_str_digits "sys.set_int_max_str_digits")\
, [`PYTHONINTMAXSTRDIGITS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINTMAXSTRDIGITS)\
, or [`-X int_max_str_digits`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)\
.\
\
Added in version 3.1.\
\
Changed in version 3.11: Added [`default_max_str_digits`](https://docs.python.org/3/library/sys.html#sys.int_info.default_max_str_digits "sys.int_info.default_max_str_digits")\
 and [`str_digits_check_threshold`](https://docs.python.org/3/library/sys.html#sys.int_info.str_digits_check_threshold "sys.int_info.str_digits_check_threshold")\
.\
\
sys.\_\_interactivehook\_\_[¶](https://docs.python.org/3/library/sys.html#sys.__interactivehook__ "Link to this definition")\
\
When this attribute exists, its value is automatically called (with no arguments) when the interpreter is launched in [interactive mode](https://docs.python.org/3/tutorial/interpreter.html#tut-interactive)\
. This is done after the [`PYTHONSTARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP)\
 file is read, so that you can set this hook there. The [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")\
 module [sets this](https://docs.python.org/3/library/site.html#rlcompleter-config)\
.\
\
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)\
 `cpython.run_interactivehook` with the hook object as the argument when the hook is called on startup.\
\
Added in version 3.4.\
\
sys.intern(_string_)[¶](https://docs.python.org/3/library/sys.html#sys.intern "Link to this definition")\
\
Enter _string_ in the table of “interned” strings and return the interned string – which is _string_ itself or a copy. Interning strings is useful to gain a little performance on dictionary lookup – if the keys in a dictionary are interned, and the lookup key is interned, the key comparisons (after hashing) can be done by a pointer compare instead of a string compare. Normally, the names used in Python programs are automatically interned, and the dictionaries used to hold module, class or instance attributes have interned keys.\
\
Interned strings are not [immortal](https://docs.python.org/3/glossary.html#term-immortal)\
; you must keep a reference to the return value of `intern()` around to benefit from it.\
\
sys.\_is\_gil\_enabled()[¶](https://docs.python.org/3/library/sys.html#sys._is_gil_enabled "Link to this definition")\
\
Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")\
 if the [GIL](https://docs.python.org/3/glossary.html#term-GIL)\
 is enabled and [`False`](https://docs.python.org/3/builtins/constants.html#False "False")\
 if it is disabled.\
\
Added in version 3.13.\
\
**CPython implementation detail:** It is not guaranteed to exist in all implementations of Python.\
\
sys.is\_finalizing()[¶](https://docs.python.org/3/library/sys.html#sys.is_finalizing "Link to this definition")\
\
Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")\
 if the main Python interpreter is [shutting down](https://docs.python.org/3/glossary.html#term-interpreter-shutdown)\
. Return [`False`](https://docs.python.org/3/builtins/constants.html#False "False")\
 otherwise.\
\
See also the [`PythonFinalizationError`](https://docs.python.org/3/builtins/exceptions.html#PythonFinalizationError "PythonFinalizationError")\
 exception.\
\
Added in version 3.5.\
\
sys.\_jit[¶](https://docs.python.org/3/library/sys.html#sys._jit "Link to this definition")\
\
Utilities for observing just-in-time compilation.\
\
**CPython implementation detail:** JIT compilation is an _experimental implementation detail_ of CPython. `sys._jit` is not guaranteed to exist or behave the same way in all Python implementations, versions, or build configurations.\
\
Added in version 3.14.\
\
\_jit.is\_available()[¶](https://docs.python.org/3/library/sys.html#sys._jit.is_available "Link to this definition")\
\
Return `True` if the current Python executable supports JIT compilation, and `False` otherwise. This can be controlled by building CPython with the `--experimental-jit` option on Windows, and the [`--enable-experimental-jit`](https://docs.python.org/3/using/configure.html#cmdoption-enable-experimental-jit)\
 option on all other platforms.\
\
\_jit.is\_enabled()[¶](https://docs.python.org/3/library/sys.html#sys._jit.is_enabled "Link to this definition")\
\
Return `True` if JIT compilation is enabled for the current Python process (implies [`sys._jit.is_available()`](https://docs.python.org/3/library/sys.html#sys._jit.is_available "sys._jit.is_available")\
), and `False` otherwise. If JIT compilation is available, this can be controlled by setting the [`PYTHON_JIT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_JIT)\
 environment variable to `0` (disabled) or `1` (enabled) at interpreter startup.\
\
\_jit.is\_active()[¶](https://docs.python.org/3/library/sys.html#sys._jit.is_active "Link to this definition")\
\
Return `True` if the topmost Python frame is currently executing JIT code (implies [`sys._jit.is_enabled()`](https://docs.python.org/3/library/sys.html#sys._jit.is_enabled "sys._jit.is_enabled")\
), and `False` otherwise.\
\
Note\
\
This function is intended for testing and debugging the JIT itself. It should be avoided for any other purpose.\
\
Note\
\
Due to the nature of tracing JIT compilers, repeated calls to this function may give surprising results. For example, branching on its return value will likely lead to unexpected behavior (if doing so causes JIT code to be entered or exited):\
\
Copy\
\
\>>> for warmup in range(BIG\_NUMBER):\
...     \# This line is "hot", and is eventually JIT-compiled:\
...     if sys.\_jit.is\_active():\
...         \# This line is "cold", and is run in the interpreter:\
...         assert sys.\_jit.is\_active()\
...\
Traceback (most recent call last):\
  File "<stdin>", line 5, in <module>\
    assert sys.\_jit.is\_active()\
           \~~~~~~~~~~~~~~~~~~^^\
AssertionError\
\
sys.last\_exc[¶](https://docs.python.org/3/library/sys.html#sys.last_exc "Link to this definition")\
\
This variable is not always defined; it is set to the exception instance when an exception is not handled and the interpreter prints an error message and a stack traceback. Its intended use is to allow an interactive user to import a debugger module and engage in post-mortem debugging without having to re-execute the command that caused the error. (Typical use is `import pdb; pdb.pm()` to enter the post-mortem debugger; see [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")\
 module for more information.)\
\
Added in version 3.12.\
\
sys.\_is\_immortal(_op_)[¶](https://docs.python.org/3/library/sys.html#sys._is_immortal "Link to this definition")\
\
Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")\
 if the given object is [immortal](https://docs.python.org/3/glossary.html#term-immortal)\
, [`False`](https://docs.python.org/3/builtins/constants.html#False "False")\
 otherwise.\
\
Note\
\
Objects that are immortal (and thus return `True` upon being passed to this function) are not guaranteed to be immortal in future versions, and vice versa for mortal objects.\
\
Added in version 3.14.\
\
**CPython implementation detail:** This function should be used for specialized purposes only. It is not guaranteed to exist in all implementations of Python.\
\
sys.\_is\_interned(_string_)[¶](https://docs.python.org/3/library/sys.html#sys._is_interned "Link to this definition")\
\
Return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")\
 if the given string is “interned”, [`False`](https://docs.python.org/3/builtins/constants.html#False "False")\
 otherwise.\
\
Added in version 3.13.\
\
**CPython implementation detail:** It is not guaranteed to exist in all implementations of Python.\
\
sys.last\_type[¶](https://docs.python.org/3/library/sys.html#sys.last_type "Link to this definition")\
\
sys.last\_value[¶](https://docs.python.org/3/library/sys.html#sys.last_value "Link to this definition")\
\
sys.last\_traceback[¶](https://docs.python.org/3/library/sys.html#sys.last_traceback "Link to this definition")\
\
These three variables are deprecated; use [`sys.last_exc`](https://docs.python.org/3/library/sys.html#sys.last_exc "sys.last_exc")\
 instead. They hold the legacy representation of `sys.last_exc`, as returned from [`exc_info()`](https://docs.python.org/3/library/sys.html#sys.exc_info "sys.exc_info")\
 above.\
\
sys.lazy\_modules[¶](https://docs.python.org/3/library/sys.html#sys.lazy_modules "Link to this definition")\
\
A [`set`](https://docs.python.org/3/builtins/stdtypes.html#set "set")\
 of fully qualified module name strings that have been lazily imported in the current interpreter but not yet loaded. When a lazily imported module is accessed for the first time, its name is typically removed from this set.\
\
The set may contain some additional strings. It is intended for debugging and introspection, and consumers are expected to verify each entry’s status.\
\
**CPython implementation detail:** Currently, `lazy_modules` may also contain:\
\
*   names of _attributes_ (non-modules), such as `"pathlib.Path"` after running `lazy from pathlib import Path`, and\
    \
*   names of items than have already been accessed.\
    \
\
In future versions of Python, these may be removed, and/or additional extras may be added.\
\
See also [`set_lazy_imports()`](https://docs.python.org/3/library/sys.html#sys.set_lazy_imports "sys.set_lazy_imports")\
 and [**PEP 810**](https://peps.python.org/pep-0810/)\
.\
\
Added in version 3.15.\
\
sys.maxsize[¶](https://docs.python.org/3/library/sys.html#sys.maxsize "Link to this definition")\
\
An integer giving the maximum value a variable of type [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")\
 can take. It’s usually `2**31 - 1` on a 32-bit platform and `2**63 - 1` on a 64-bit platform.\
\
sys.maxunicode[¶](https://docs.python.org/3/library/sys.html#sys.maxunicode "Link to this definition")\
\
An integer giving the value of the largest Unicode code point, i.e. `1114111` (`0x10FFFF` in hexadecimal).\
\
Changed in version 3.3: Before [**PEP 393**](https://peps.python.org/pep-0393/)\
, `sys.maxunicode` used to be either `0xFFFF` or `0x10FFFF`, depending on the configuration option that specified whether Unicode characters were stored as UCS-2 or UCS-4.\
\
sys.meta\_path[¶](https://docs.python.org/3/library/sys.html#sys.meta_path "Link to this definition")\
\
A list of [meta path finder](https://docs.python.org/3/glossary.html#term-meta-path-finder)\
 objects that have their [`find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "importlib.abc.MetaPathFinder.find_spec")\
 methods called to see if one of the objects can find the module to be imported. By default, it holds entries that implement Python’s default import semantics. The `find_spec()` method is called with at least the absolute name of the module being imported. If the module to be imported is contained in a package, then the parent package’s [`__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__")\
 attribute is passed in as a second argument. The method returns a [module spec](https://docs.python.org/3/glossary.html#term-module-spec)\
, or `None` if the module cannot be found.\
\
See also\
\
[`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder")\
\
The abstract base class defining the interface of finder objects on `meta_path`.\
\
[`importlib.machinery.ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")\
\
The concrete class which [`find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "importlib.abc.MetaPathFinder.find_spec")\
 should return instances of.\
\
Changed in version 3.4: [Module specs](https://docs.python.org/3/glossary.html#term-module-spec)\
 were introduced in Python 3.4, by [**PEP 451**](https://peps.python.org/pep-0451/)\
.\
\
Changed in version 3.12: Removed the fallback that looked for a `find_module()` method if a `meta_path` entry didn’t have a [`find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "importlib.abc.MetaPathFinder.find_spec")\
 method.\
\
sys.modules[¶](https://docs.python.org/3/library/sys.html#sys.modules "Link to this definition")\
\
This is a dictionary that maps module names to modules which have already been loaded. This can be manipulated to force reloading of modules and other tricks. However, replacing the dictionary will not necessarily work as expected and deleting essential items from the dictionary may cause Python to fail. If you want to iterate over this global dictionary always use `sys.modules.copy()` or `tuple(sys.modules)` to avoid exceptions as its size may change during iteration as a side effect of code or activity in other threads.\
\
sys.orig\_argv[¶](https://docs.python.org/3/library/sys.html#sys.orig_argv "Link to this definition")\
\
The list of the original command line arguments passed to the Python executable.\
\
The elements of `sys.orig_argv` are the arguments to the Python interpreter, while the elements of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv")\
 are the arguments to the user’s program. Arguments consumed by the interpreter itself will be present in `sys.orig_argv` and missing from `sys.argv`.\
\
Added in version 3.10.\
\
sys.path[¶](https://docs.python.org/3/library/sys.html#sys.path "Link to this definition")\
\
A list of strings that specifies the search path for modules. Initialized from the environment variable [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)\
, plus an installation-dependent default.\
\
By default, as initialized upon program startup, a potentially unsafe path is prepended to `sys.path` (_before_ the entries inserted as a result of [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)\
):\
\
*   `python -m module` command line: prepend the current working directory.\
    \
*   `python script.py` command line: prepend the script’s directory. If it’s a symbolic link, resolve symbolic links.\
    \
*   `python -c code` and `python` (REPL) command lines: prepend an empty string, which means the current working directory.\
    \
\
To not prepend this potentially unsafe path, use the [`-P`](https://docs.python.org/3/using/cmdline.html#cmdoption-P)\
 command line option or the [`PYTHONSAFEPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSAFEPATH)\
 environment variable.\
\
A program is free to modify this list for its own purposes. Only strings should be added to `sys.path`; all other data types are ignored during import.\
\
See also\
\
*   Module [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")\
     This describes how to use .pth files to extend `sys.path`.\
    \
\
sys.path\_hooks[¶](https://docs.python.org/3/library/sys.html#sys.path_hooks "Link to this definition")\
\
A list of callables that take a path argument to try to create a [finder](https://docs.python.org/3/glossary.html#term-finder)\
 for the path. If a finder can be created, it is to be returned by the callable, else raise [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")\
.\
\
Originally specified in [**PEP 302**](https://peps.python.org/pep-0302/)\
.\
\
sys.path\_importer\_cache[¶](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "Link to this definition")\
\
A dictionary acting as a cache for [finder](https://docs.python.org/3/glossary.html#term-finder)\
 objects. The keys are paths that have been passed to [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks")\
 and the values are the finders that are found. If a path is a valid file system path but no finder is found on `sys.path_hooks` then `None` is stored.\
\
Originally specified in [**PEP 302**](https://peps.python.org/pep-0302/)\
.\
\
sys.platform[¶](https://docs.python.org/3/library/sys.html#sys.platform "Link to this definition")\
\
A string containing a platform identifier. Known values are:\
\
| System | `platform` value |\
| --- | --- |\
| AIX | `'aix'` |\
| Android | `'android'` |\
| Emscripten | `'emscripten'` |\
| FreeBSD | `'freebsd'` |\
| iOS | `'ios'` |\
| Linux | `'linux'` |\
| macOS | `'darwin'` |\
| Windows | `'win32'` |\
| Windows/Cygwin | `'cygwin'` |\
| WASI | `'wasi'` |\
\
On Unix systems not listed in the table, the value is the lowercased OS name as returned by `uname -s`, with the first part of the version as returned by `uname -r` appended, e.g. `'sunos5'`, _at the time when Python was built_. Unless you want to test for a specific system version, it is therefore recommended to use the following idiom:\
\
Copy\
\
if sys.platform.startswith('sunos'):\
    \# SunOS-specific code here...\
\
Changed in version 3.3: On Linux, `sys.platform` doesn’t contain the major version anymore. It is always `'linux'`, instead of `'linux2'` or `'linux3'`.\
\
Changed in version 3.8: On AIX, `sys.platform` doesn’t contain the major version anymore. It is always `'aix'`, instead of `'aix5'` or `'aix7'`.\
\
Changed in version 3.13: On Android, `sys.platform` now returns `'android'` rather than `'linux'`.\
\
Changed in version 3.14: On FreeBSD, `sys.platform` doesn’t contain the major version anymore. It is always `'freebsd'`, instead of `'freebsd13'` or `'freebsd14'`.\
\
See also\
\
[`os.name`](https://docs.python.org/3/library/os.html#os.name "os.name")\
 has a coarser granularity. [`os.uname()`](https://docs.python.org/3/library/os.html#os.uname "os.uname")\
 gives system-dependent version information.\
\
The [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")\
 module provides detailed checks for the system’s identity.\
\
sys.platlibdir[¶](https://docs.python.org/3/library/sys.html#sys.platlibdir "Link to this definition")\
\
Name of the platform-specific library directory. It is used to build the path of standard library and the paths of installed extension modules.\
\
It is equal to `"lib"` on most platforms. On Fedora and SuSE, it is equal to `"lib64"` on 64-bit platforms which gives the following `sys.path` paths (where `X.Y` is the Python `major.minor` version):\
\
*   `/usr/lib64/pythonX.Y/`: Standard library (like `os.py` of the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")\
     module)\
    \
*   `/usr/lib64/pythonX.Y/lib-dynload/`: C extension modules of the standard library (like the [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.")\
     module, the exact filename is platform specific)\
    \
*   `/usr/lib/pythonX.Y/site-packages/` (always use `lib`, not `sys.platlibdir`): Third-party modules\
    \
*   `/usr/lib64/pythonX.Y/site-packages/`: C extension modules of third-party packages\
    \
\
Added in version 3.9.\
\
sys.prefix[¶](https://docs.python.org/3/library/sys.html#sys.prefix "Link to this definition")\
\
A string giving the site-specific directory prefix where the platform independent Python files are installed; on Unix, the default is `/usr/local`. This can be set at build time with the [`--prefix`](https://docs.python.org/3/using/configure.html#cmdoption-prefix)\
 argument to the **configure** script. See [Installation paths](https://docs.python.org/3/library/sysconfig.html#installation-paths)\
 for derived paths.\
\
Note\
\
If a [virtual environment](https://docs.python.org/3/library/venv.html#venv-def)\
 is in effect, this `prefix` will point to the virtual environment. The value for the Python installation will still be available, via [`base_prefix`](https://docs.python.org/3/library/sys.html#sys.base_prefix "sys.base_prefix")\
. Refer to [Virtual Environments](https://docs.python.org/3/library/sys_path_init.html#sys-path-init-virtual-environments)\
 for more information.\
\
Changed in version 3.14: When running under a [virtual environment](https://docs.python.org/3/library/venv.html#venv-def)\
, `prefix` and [`exec_prefix`](https://docs.python.org/3/library/sys.html#sys.exec_prefix "sys.exec_prefix")\
 are now set to the virtual environment prefix by the [path initialization](https://docs.python.org/3/library/sys_path_init.html#sys-path-init)\
, instead of [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.")\
. This means that `prefix` and `exec_prefix` always point to the virtual environment, even when `site` is disabled ([`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S)\
).\
\
sys.ps1[¶](https://docs.python.org/3/library/sys.html#sys.ps1 "Link to this definition")\
\
sys.ps2[¶](https://docs.python.org/3/library/sys.html#sys.ps2 "Link to this definition")\
\
Strings specifying the primary and secondary prompt of the interpreter. These are only defined if the interpreter is in interactive mode. Their initial values in this case are `'>>> '` and `'... '`. If a non-string object is assigned to either variable, its [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")\
 is re-evaluated each time the interpreter prepares to read a new interactive command; this can be used to implement a dynamic prompt.\
\
sys.setdlopenflags(_n_)[¶](https://docs.python.org/3/library/sys.html#sys.setdlopenflags "Link to this definition")\
\
Set the flags used by the interpreter for `dlopen()` calls, such as when the interpreter loads extension modules. Among other things, this will enable a lazy resolving of symbols when importing a module, if called as `sys.setdlopenflags(0)`. To share symbols across extension modules, call as `sys.setdlopenflags(os.RTLD_GLOBAL)`. Symbolic names for the flag values can be found in the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")\
 module (`RTLD__xxx_` constants, e.g. [`os.RTLD_LAZY`](https://docs.python.org/3/library/os.html#os.RTLD_LAZY "os.RTLD_LAZY")\
).\
\
[Availability](https://docs.python.org/3/library/intro.html#availability)\
: Unix.\
\
sys.set\_int\_max\_str\_digits(_maxdigits_)[¶](https://docs.python.org/3/library/sys.html#sys.set_int_max_str_digits "Link to this definition")\
\
Set the [integer string conversion length limitation](https://docs.python.org/3/builtins/stdtypes.html#int-max-str-digits)\
 used by this interpreter. See also [`get_int_max_str_digits()`](https://docs.python.org/3/library/sys.html#sys.get_int_max_str_digits "sys.get_int_max_str_digits")\
.\
\
Added in version 3.11.\
\
sys.set\_lazy\_imports(_mode_)[¶](https://docs.python.org/3/library/sys.html#sys.set_lazy_imports "Link to this definition")\
\
Sets the global lazy imports mode. The _mode_ parameter must be one of the following strings:\
\
*   `"normal"`: Only imports explicitly marked with the `lazy` keyword are lazy\
    \
*   `"all"`: All top-level imports become potentially lazy\
    \
\
This function is intended for advanced users who need to control lazy imports across their entire application. Library developers should generally not use this function as it affects the runtime execution of applications.\
\
In addition to the mode, lazy imports can be controlled via the filter provided by [`set_lazy_imports_filter()`](https://docs.python.org/3/library/sys.html#sys.set_lazy_imports_filter "sys.set_lazy_imports_filter")\
.\
\
See also [`get_lazy_imports()`](https://docs.python.org/3/library/sys.html#sys.get_lazy_imports "sys.get_lazy_imports")\
 and [**PEP 810**](https://peps.python.org/pep-0810/)\
.\
\
Added in version 3.15.\
\
sys.set\_lazy\_imports\_filter(_filter_)[¶](https://docs.python.org/3/library/sys.html#sys.set_lazy_imports_filter "Link to this definition")\
\
Sets the lazy imports filter callback. The _filter_ parameter must be a callable or `None` to clear the filter.\
\
The filter function is called for every potentially lazy import to determine whether it should actually be lazy. It should have the following signature:\
\
Copy\
\
def filter(importing\_module: str, imported\_module: str,\
           fromlist: tuple\[str, ...\] | None) \-> bool\
\
The function is called with three positional arguments:\
\
*   _importing\_module_ is the name of the module doing the import\
    \
*   _imported\_module_ is the resolved name of the module being imported (for example, `lazy from .spam import eggs` passes `package.spam`)\
    \
*   _fromlist_ is the tuple of names being imported (for `from ... import` statements), or `None` for regular imports\
    \
\
The filter should return `True` to allow the import to be lazy, or `False` to force an eager import.\
\
This is an advanced feature intended for specialized users who need fine-grained control over lazy import behavior.\
\
See also [`get_lazy_imports_filter()`](https://docs.python.org/3/library/sys.html#sys.get_lazy_imports_filter "sys.get_lazy_imports_filter")\
 and [**PEP 810**](https://peps.python.org/pep-0810/)\
.\
\
Added in version 3.15.\
\
sys.setprofile(_profilefunc_)[¶](https://docs.python.org/3/library/sys.html#sys.setprofile "Link to this definition")\
\
Set the system’s profile function, which allows you to implement a Python source code profiler in Python. See chapter [profile — Pure Python profiler](https://docs.python.org/3/library/profile.html#profile)\
 for more information on the Python profiler. The system’s profile function is called similarly to the system’s trace function (see [`settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace")\
), but it is called with different events, for example it isn’t called for each executed line of code (only on call and return, but the return event is reported even when an exception has been set). The function is thread-specific, but there is no way for the profiler to know about context switches between threads, so it does not make sense to use this in the presence of multiple threads. Also, its return value is not used, so it can simply return `None`. Error in the profile function will cause itself unset.\
\
Note\
\
The same tracing mechanism is used for `setprofile()` as [`settrace()`](https://docs.python.org/3/library/sys.html#sys.settrace "sys.settrace")\
. To trace calls with `setprofile()` inside a tracing function (e.g. in a debugger breakpoint), see [`call_tracing()`](https://docs.python.org/3/library/sys.html#sys.call_tracing "sys.call_tracing")\
.\
\
Profile functions should have three arguments: _frame_, _event_, and _arg_. _frame_ is the current stack frame. _event_ is a string: `'call'`, `'return'`, `'c_call'`, `'c_return'`, or `'c_exception'`. _arg_ depends on the event type.\
\
The events have the following meaning:\
\
`'call'`\
\
A function is called (or some other code block entered). The profile function is called; _arg_ is `None`.\
\
`'return'`\
\
A function (or other code block) is about to return. The profile function is called; _arg_ is the value that will be returned, or `None` if the event is caused by an exception being raised.\
\
`'c_call'`\
\
A C function is about to be called. This may be an extension function or a built-in. _arg_ is the C function object.\
\
`'c_return'`\
\
A C function has returned. _arg_ is the C function object.\
\
`'c_exception'`\
\
A C function has raised an exception. _arg_ is the C function object.\
\
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)\
 `sys.setprofile` with no arguments.\
\
sys.setrecursionlimit(_limit_)[¶](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit "Link to this definition")\
\
Set the maximum depth of the Python interpreter stack to _limit_. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.\
\
The highest possible limit is platform-dependent. A user may need to set the limit higher when they have a program that requires deep recursion and a platform that supports a higher limit. This should be done with care, because a too-high limit can lead to a crash.\
\
If the new limit is too low at the current recursion depth, a [`RecursionError`](https://docs.python.org/3/builtins/exceptions.html#RecursionError "RecursionError")\
 exception is raised.\
\
Changed in version 3.5.1: A [`RecursionError`](https://docs.python.org/3/builtins/exceptions.html#RecursionError "RecursionError")\
 exception is now raised if the new limit is too low at the current recursion depth.\
\
sys.setswitchinterval(_interval_)[¶](https://docs.python.org/3/library/sys.html#sys.setswitchinterval "Link to this definition")\
\
Set the interpreter’s thread switch interval (in seconds). This floating-point value determines the ideal duration of the “timeslices” allocated to concurrently running Python threads. Please note that the actual value can be higher, especially if long-running internal functions or methods are used. Also, which thread becomes scheduled at the end of the interval is the operating system’s decision. The interpreter doesn’t have its own scheduler.\
\
Added in version 3.2.\
\
sys.settrace(_tracefunc_)[¶](https://docs.python.org/3/library/sys.html#sys.settrace "Link to this definition")\
\
Set the system’s trace function, which allows you to implement a Python source code debugger in Python. The function is thread-specific; for a debugger to support multiple threads, it must register a trace function using `settrace()` for each thread being debugged or use [`threading.settrace()`](https://docs.python.org/3/library/threading.html#threading.settrace "threading.settrace")\
.\
\
Trace functions should have three arguments: _frame_, _event_, and _arg_. _frame_ is the [current stack frame](https://docs.python.org/3/reference/datamodel.html#frame-objects)\
. _event_ is a string: `'call'`, `'line'`, `'return'`, `'exception'` or `'opcode'`. _arg_ depends on the event type.\
\
The trace function is invoked (with _event_ set to `'call'`) whenever a new local scope is entered; it should return a reference to a local trace function to be used for the new scope, or `None` if the scope shouldn’t be traced.\
\
The local trace function should return a reference to itself, or to another function which would then be used as the local trace function for the scope.\
\
If there is any error occurred in the trace function, it will be unset, just like `settrace(None)` is called.\
\
Note\
\
Tracing is disabled while calling the trace function (e.g. a function set by `settrace()`). For recursive tracing see [`call_tracing()`](https://docs.python.org/3/library/sys.html#sys.call_tracing "sys.call_tracing")\
.\
\
The events have the following meaning:\
\
`'call'`\
\
A function is called (or some other code block entered). The global trace function is called; _arg_ is `None`; the return value specifies the local trace function.\
\
`'line'`\
\
The interpreter is about to execute a new line of code or re-execute the condition of a loop. The local trace function is called; _arg_ is `None`; the return value specifies the new local trace function. See [InternalDocs/code\_objects.md](https://github.com/python/cpython/tree/3.15/InternalDocs/code_objects.md)\
 for a detailed explanation of how this works. Per-line events may be disabled for a frame by setting [`f_trace_lines`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_lines "frame.f_trace_lines")\
 to [`False`](https://docs.python.org/3/builtins/constants.html#False "False")\
 on that [frame](https://docs.python.org/3/reference/datamodel.html#frame-objects)\
.\
\
`'return'`\
\
A function (or other code block) is about to return. The local trace function is called; _arg_ is the value that will be returned, or `None` if the event is caused by an exception being raised. The trace function’s return value is ignored.\
\
`'exception'`\
\
An exception has occurred. The local trace function is called; _arg_ is a tuple `(exception, value, traceback)`; the return value specifies the new local trace function.\
\
`'opcode'`\
\
The interpreter is about to execute a new opcode (see [`dis`](https://docs.python.org/3/library/dis.html#module-dis "dis: Disassembler for Python bytecode.")\
 for opcode details). The local trace function is called; _arg_ is `None`; the return value specifies the new local trace function. Per-opcode events are not emitted by default: they must be explicitly requested by setting [`f_trace_opcodes`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_opcodes "frame.f_trace_opcodes")\
 to [`True`](https://docs.python.org/3/builtins/constants.html#True "True")\
 on the [frame](https://docs.python.org/3/reference/datamodel.html#frame-objects)\
.\
\
Note that as an exception is propagated down the chain of callers, an `'exception'` event is generated at each level.\
\
For more fine-grained usage, it’s possible to set a trace function by assigning `frame.f_trace = tracefunc` explicitly, rather than relying on it being set indirectly via the return value from an already installed trace function. This is also required for activating the trace function on the current frame, which `settrace()` doesn’t do. Note that in order for this to work, a global tracing function must have been installed with `settrace()` in order to enable the runtime tracing machinery, but it doesn’t need to be the same tracing function (e.g. it could be a low overhead tracing function that simply returns `None` to disable itself immediately on each frame).\
\
For more information on code and frame objects, refer to [The standard type hierarchy](https://docs.python.org/3/reference/datamodel.html#types)\
.\
\
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)\
 `sys.settrace` with no arguments.\
\
**CPython implementation detail:** The `settrace()` function is intended only for implementing debuggers, profilers, coverage tools and the like. Its behavior is part of the implementation platform, rather than part of the language definition, and thus may not be available in all Python implementations.\
\
Changed in version 3.7: `'opcode'` event type added; [`f_trace_lines`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_lines "frame.f_trace_lines")\
 and [`f_trace_opcodes`](https://docs.python.org/3/reference/datamodel.html#frame.f_trace_opcodes "frame.f_trace_opcodes")\
 attributes added to frames\
\
sys.set\_asyncgen\_hooks(_\[firstiter\] \[, finalizer\]_)[¶](https://docs.python.org/3/library/sys.html#sys.set_asyncgen_hooks "Link to this definition")\
\
Accepts two optional keyword arguments which are callables that accept an [asynchronous generator iterator](https://docs.python.org/3/glossary.html#term-asynchronous-generator-iterator)\
 as an argument. The _firstiter_ callable will be called when an asynchronous generator is iterated for the first time. The _finalizer_ will be called when an asynchronous generator is about to be garbage collected.\
\
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)\
 `sys.set_asyncgen_hooks_firstiter` with no arguments.\
\
Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)\
 `sys.set_asyncgen_hooks_finalizer` with no arguments.\
\
Two auditing events are raised because the underlying API consists of two calls, each of which must raise its own event.\
\
Added in version 3.6: See [**PEP 525**](https://peps.python.org/pep-0525/)\
 for more details, and for a reference example of a _finalizer_ method see the implementation of `asyncio.BaseEventLoop._asyncgen_finalizer_hook` in [Lib/asyncio/base\_events.py](https://github.com/python/cpython/tree/3.15/Lib/asyncio/base_events.py)\
\
Note\
\
This function has been added on a provisional basis (see [**PEP 411**](https://peps.python.org/pep-0411/)\
 for details.)\
\
sys.set\_coroutine\_origin\_tracking\_depth(_depth_)[¶](https://docs.python.org/3/library/sys.html#sys.set_coroutine_origin_tracking_depth "Link to this definition")\
\
Allows enabling or disabling coroutine origin tracking. When enabled, the `cr_origin` attribute on coroutine objects will contain a tuple of (filename, line number, function name) tuples describing the traceback where the coroutine object was created, with the most recent call first. When disabled, `cr_origin` will be `None`.\
\
To enable, pass a _depth_ value greater than zero; this sets the number of frames whose information will be captured. To disable, set _depth_ to zero.\
\
This setting is thread-specific.\
\
Added in version 3.7.\
\
Note\
\
This function has been added on a provisional basis (see [**PEP 411**](https://peps.python.org/pep-0411/)\
 for details.) Use it only for debugging purposes.\
\
sys.activate\_stack\_trampoline(_backend_, _/_)[¶](https://docs.python.org/3/library/sys.html#sys.activate_stack_trampoline "Link to this definition")\
\
Activate the stack profiler trampoline _backend_. The only supported backend is `"perf"`.\
\
Stack trampolines cannot be activated if the JIT is active.\
\
[Availability](https://docs.python.org/3/library/intro.html#availability)\
: Linux.\
\
Added in version 3.12.\
\
See also\
\
*   [Python support for the perf map compatible profilers](https://docs.python.org/3/howto/perf_profiling.html#perf-profiling)\
    \
*   [https://perf.wiki.kernel.org](https://perf.wiki.kernel.org/)\
    \
\
sys.deactivate\_stack\_trampoline()[¶](https://docs.python.org/3/library/sys.html#sys.deactivate_stack_trampoline "Link to this definition")\
\
Deactivate the current stack profiler trampoline backend.\
\
If no stack profiler is activated, this function has no effect.\
\
[Availability](https://docs.python.org/3/library/intro.html#availability)\
: Linux.\
\
Added in version 3.12.\
\
sys.is\_stack\_trampoline\_active()[¶](https://docs.python.org/3/library/sys.html#sys.is_stack_trampoline_active "Link to this definition")\
\
Return `True` if a stack profiler trampoline is active.\
\
[Availability](https://docs.python.org/3/library/intro.html#availability)\
: Linux.\
\
Added in version 3.12.\
\
sys.remote\_exec(_pid_, _script_)[¶](https://docs.python.org/3/library/sys.html#sys.remote_exec "Link to this definition")\
\
Executes _script_, a file containing Python code in the remote process with the given _pid_.\
\
This function returns immediately, and the code will be executed by the target process’s main thread at the next available opportunity, similarly to how signals are handled. There is no interface to determine when the code has been executed. The caller is responsible for making sure that the file still exists whenever the remote process tries to read it and that it hasn’t been overwritten.\
\
The remote process must be running a CPython interpreter of the same major and minor version as the local process. If either the local or remote interpreter is pre-release (alpha, beta, or release candidate) then the local and remote interpreters must be the same exact version.\
\
See [Remote debugging attachment protocol](https://docs.python.org/3/howto/remote_debugging.html#remote-debugging)\
 for more information about the remote debugging mechanism.\
\
When the code is executed in the remote process, an [auditing event](https://docs.python.org/3/library/sys.html#auditing)\
 `sys.remote_exec` is raised with the _pid_ and the path to the script file. This event is raised in the process that called `sys.remote_exec()`.\
\
When the script is executed in the remote process, an [auditing event](https://docs.python.org/3/library/sys.html#auditing)\
 `cpython.remote_debugger_script` is raised with the path in the remote process. This event is raised in the remote process, not the one that called `sys.remote_exec()`.\
\
[Availability](https://docs.python.org/3/library/intro.html#availability)\
: Unix, Windows.\
\
Added in version 3.14: See [**PEP 768**](https://peps.python.org/pep-0768/)\
 for more details.\
\
sys.\_enablelegacywindowsfsencoding()[¶](https://docs.python.org/3/library/sys.html#sys._enablelegacywindowsfsencoding "Link to this definition")\
\
Changes the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)\
 to ‘mbcs’ and ‘replace’ respectively, for consistency with versions of Python prior to 3.6.\
\
This is equivalent to defining the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING)\
 environment variable before launching Python.\
\
See also [`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding")\
 and [`sys.getfilesystemencodeerrors()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencodeerrors "sys.getfilesystemencodeerrors")\
.\
\
[Availability](https://docs.python.org/3/library/intro.html#availability)\
: Windows.\
\
Note\
\
Changing the filesystem encoding after Python startup is risky because the old fsencoding or paths encoded by the old fsencoding may be cached somewhere. Use [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING)\
 instead.\
\
Added in version 3.6: See [**PEP 529**](https://peps.python.org/pep-0529/)\
 for more details.\
\
Deprecated since version 3.13, will be removed in version 3.16: Use [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING)\
 instead.\
\
sys.stdin[¶](https://docs.python.org/3/library/sys.html#sys.stdin "Link to this definition")\
\
sys.stdout[¶](https://docs.python.org/3/library/sys.html#sys.stdout "Link to this definition")\
\
sys.stderr[¶](https://docs.python.org/3/library/sys.html#sys.stderr "Link to this definition")\
\
[File objects](https://docs.python.org/3/glossary.html#term-file-object)\
 used by the interpreter for standard input, output and errors:\
\
*   `stdin` is used for all interactive input (including calls to [`input()`](https://docs.python.org/3/builtins/functions.html#input "input")\
    );\
    \
*   `stdout` is used for the output of [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")\
     and [expression](https://docs.python.org/3/glossary.html#term-expression)\
     statements and for the prompts of [`input()`](https://docs.python.org/3/builtins/functions.html#input "input")\
    ;\
    \
*   The interpreter’s own prompts and its error messages go to `stderr`.\
    \
\
These streams are regular [text files](https://docs.python.org/3/glossary.html#term-text-file)\
 like those returned by the [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")\
 function. Their parameters are chosen as follows:\
\
*   The encoding and error handling are initialized from [`PyConfig.stdio_encoding`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdio_encoding "PyConfig.stdio_encoding")\
     and [`PyConfig.stdio_errors`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.stdio_errors "PyConfig.stdio_errors")\
    .\
    \
    On Windows, UTF-8 is used for the console device. Non-character devices such as disk files and pipes use the system locale encoding (i.e. the ANSI codepage). Non-console character devices such as NUL (i.e. where `isatty()` returns `True`) use the value of the console input and output codepages at startup, respectively for stdin and stdout/stderr. This defaults to the system [locale encoding](https://docs.python.org/3/glossary.html#term-locale-encoding)\
     if the process is not initially attached to a console.\
    \
    The special behaviour of the console can be overridden by setting the environment variable PYTHONLEGACYWINDOWSSTDIO before starting Python. In that case, the console codepages are used as for any other character device.\
    \
    Under all platforms, you can override the character encoding by setting the [`PYTHONIOENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONIOENCODING)\
     environment variable before starting Python or by using the new [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)\
     `utf8` command line option and [`PYTHONUTF8`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUTF8)\
     environment variable. However, for the Windows console, this only applies when [`PYTHONLEGACYWINDOWSSTDIO`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSSTDIO)\
     is also set.\
    \
*   When interactive, the `stdout` stream is line-buffered. Otherwise, it is block-buffered like regular text files. The `stderr` stream is line-buffered in both cases. You can make both streams unbuffered by passing the [`-u`](https://docs.python.org/3/using/cmdline.html#cmdoption-u)\
     command-line option or setting the [`PYTHONUNBUFFERED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED)\
     environment variable.\
    \
\
Changed in version 3.9: Non-interactive `stderr` is now line-buffered instead of fully buffered.\
\
Note\
\
To write or read binary data from/to the standard streams, use the underlying binary [`buffer`](https://docs.python.org/3/library/io.html#io.TextIOBase.buffer "io.TextIOBase.buffer")\
 object. For example, to write bytes to `stdout`, use `sys.stdout.buffer.write(b'abc')`.\
\
However, if you are writing a library (and do not control in which context its code will be executed), be aware that the standard streams may be replaced with file-like objects like [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO")\
 which do not support the `buffer` attribute.\
\
sys.\_\_stdin\_\_[¶](https://docs.python.org/3/library/sys.html#sys.__stdin__ "Link to this definition")\
\
sys.\_\_stdout\_\_[¶](https://docs.python.org/3/library/sys.html#sys.__stdout__ "Link to this definition")\
\
sys.\_\_stderr\_\_[¶](https://docs.python.org/3/library/sys.html#sys.__stderr__ "Link to this definition")\
\
These objects contain the original values of `stdin`, `stderr` and `stdout` at the start of the program. They are used during finalization, and could be useful to print to the actual standard stream no matter if the `sys.std*` object has been redirected.\
\
It can also be used to restore the actual files to known working file objects in case they have been overwritten with a broken object. However, the preferred way to do this is to explicitly save the previous stream before replacing it, and restore the saved object.\
\
Note\
\
Under some conditions `stdin`, `stdout` and `stderr` as well as the original values `__stdin__`, `__stdout__` and `__stderr__` can be `None`. It is usually the case for Windows GUI apps that aren’t connected to a console and Python apps started with **pythonw**.\
\
sys.stdlib\_module\_names[¶](https://docs.python.org/3/library/sys.html#sys.stdlib_module_names "Link to this definition")\
\
A frozenset of strings containing the names of standard library modules.\
\
It is the same on all platforms. Modules which are not available on some platforms and modules disabled at Python build are also listed. All module kinds are listed: pure Python, built-in, frozen and extension modules. Test modules are excluded.\
\
For packages, only the main package is listed: sub-packages and sub-modules are not listed. For example, the `email` package is listed, but the `email.mime` sub-package and the `email.message` sub-module are not listed.\
\
See also the [`sys.builtin_module_names`](https://docs.python.org/3/library/sys.html#sys.builtin_module_names "sys.builtin_module_names")\
 list.\
\
Added in version 3.10.\
\
sys.thread\_info[¶](https://docs.python.org/3/library/sys.html#sys.thread_info "Link to this definition")\
\
A [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)\
 holding information about the thread implementation.\
\
thread\_info.name[¶](https://docs.python.org/3/library/sys.html#sys.thread_info.name "Link to this definition")\
\
The name of the thread implementation:\
\
*   `"nt"`: Windows threads\
    \
*   `"pthread"`: POSIX threads\
    \
*   `"pthread-stubs"`: stub POSIX threads (on WebAssembly platforms without threading support)\
    \
*   `"solaris"`: Solaris threads\
    \
\
thread\_info.lock[¶](https://docs.python.org/3/library/sys.html#sys.thread_info.lock "Link to this definition")\
\
The name of the lock implementation:\
\
*   `"semaphore"`: a lock uses a semaphore (Python 3.14 and older)\
    \
*   `"mutex+cond"`: a lock uses a mutex and a condition variable (Python 3.14 and older)\
    \
*   `"pymutex"`: a lock uses the [`PyMutex`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex "PyMutex")\
     implementation (Python 3.15 and newer)\
    \
*   `None` if this information is unknown\
    \
\
thread\_info.version[¶](https://docs.python.org/3/library/sys.html#sys.thread_info.version "Link to this definition")\
\
The name and version of the thread library. It is a string, or `None` if this information is unknown.\
\
Added in version 3.3.\
\
sys.tracebacklimit[¶](https://docs.python.org/3/library/sys.html#sys.tracebacklimit "Link to this definition")\
\
When this variable is set to an integer value, it determines the maximum number of levels of traceback information printed when an unhandled exception occurs. The default is `1000`. When set to `0` or less, all traceback information is suppressed and only the exception type and value are printed.\
\
sys.unraisablehook(_unraisable_, _/_)[¶](https://docs.python.org/3/library/sys.html#sys.unraisablehook "Link to this definition")\
\
Handle an unraisable exception.\
\
Called when an exception has occurred but there is no way for Python to handle it. For example, when a destructor raises an exception or during garbage collection ([`gc.collect()`](https://docs.python.org/3/library/gc.html#gc.collect "gc.collect")\
).\
\
The _unraisable_ argument has the following attributes:\
\
*   `exc_type`: Exception type.\
    \
*   `exc_value`: Exception value, can be `None`.\
    \
*   `exc_traceback`: Exception traceback, can be `None`.\
    \
*   `err_msg`: Error message, can be `None`.\
    \
*   `object`: Object causing the exception, can be `None`.\
    \
\
The default hook formats `err_msg` and `object` as: `f'{err_msg}: {object!r}'`; use “Exception ignored in” error message if `err_msg` is `None`. Similar to the [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.")\
 module, this adds color to exceptions by default. This can be disabled using [environment variables](https://docs.python.org/3/using/cmdline.html#using-on-controlling-color)\
.\
\
`sys.unraisablehook()` can be overridden to control how unraisable exceptions are handled.\
\
Changed in version 3.15: Exceptions are now printed with colorful text.\
\
See also\
\
[`excepthook()`](https://docs.python.org/3/library/sys.html#sys.excepthook "sys.excepthook")\
 which handles uncaught exceptions.\
\
Warning\
\
Storing `exc_value` using a custom hook can create a reference cycle. It should be cleared explicitly to break the reference cycle when the exception is no longer needed.\
\
Storing `object` using a custom hook can resurrect it if it is set to an object which is being finalized. Avoid storing `object` after the custom hook completes to avoid resurrecting objects.\
\
Raise an auditing event `sys.unraisablehook` with arguments _hook_, _unraisable_ when an exception that cannot be handled occurs. The _unraisable_ object is the same as what will be passed to the hook. If no hook has been set, _hook_ may be `None`.\
\
Added in version 3.8.\
\
sys.version[¶](https://docs.python.org/3/library/sys.html#sys.version "Link to this definition")\
\
A string containing the version number of the Python interpreter plus additional information on the build number and compiler used. This string is displayed when the interactive interpreter is started. Do not extract version information out of it, rather, use [`version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")\
 and the functions provided by the [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.")\
 module.\
\
sys.api\_version[¶](https://docs.python.org/3/library/sys.html#sys.api_version "Link to this definition")\
\
The C API version, equivalent to the C macro [`PYTHON_API_VERSION`](https://docs.python.org/3/c-api/module.html#c.PYTHON_API_VERSION "PYTHON_API_VERSION")\
. Defined for backwards compatibility.\
\
Currently, this constant is not updated in new Python versions, and is not useful for versioning. This may change in the future.\
\
sys.version\_info[¶](https://docs.python.org/3/library/sys.html#sys.version_info "Link to this definition")\
\
A tuple containing the five components of the version number: _major_, _minor_, _micro_, _releaselevel_, and _serial_. All values except _releaselevel_ are integers; the release level is `'alpha'`, `'beta'`, `'candidate'`, or `'final'`. The `version_info` value corresponding to the Python version 2.0 is `(2, 0, 0, 'final', 0)`. The components can also be accessed by name, so `sys.version_info[0]` is equivalent to `sys.version_info.major` and so on.\
\
Changed in version 3.1: Added named component attributes.\
\
sys.warnoptions[¶](https://docs.python.org/3/library/sys.html#sys.warnoptions "Link to this definition")\
\
This is an implementation detail of the warnings framework; do not modify this value. Refer to the [`warnings`](https://docs.python.org/3/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.")\
 module for more information on the warnings framework.\
\
sys.winver[¶](https://docs.python.org/3/library/sys.html#sys.winver "Link to this definition")\
\
The version number used to form registry keys on Windows platforms. This is stored as string resource 1000 in the Python DLL. The value is normally the major and minor versions of the running Python interpreter. It is provided in the `sys` module for informational purposes; modifying this value has no effect on the registry keys used by Python.\
\
[Availability](https://docs.python.org/3/library/intro.html#availability)\
: Windows.\
\
sys.monitoring\
\
Namespace containing functions and constants for register callbacks and controlling monitoring events. See [`sys.monitoring`](https://docs.python.org/3/library/sys.monitoring.html#module-sys.monitoring "sys.monitoring: Access and control event monitoring")\
 for details.\
\
sys.\_xoptions[¶](https://docs.python.org/3/library/sys.html#sys._xoptions "Link to this definition")\
\
A dictionary of the various implementation-specific flags passed through the [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)\
 command-line option. Option names are either mapped to their values, if given explicitly, or to [`True`](https://docs.python.org/3/builtins/constants.html#True "True")\
. Example:\
\
Copy\
\
$ ./python \-Xa\=b \-Xc\
Python 3.2a3+ (py3k, Oct 16 2010, 20:14:50)\
\[GCC 4.4.3\] on linux2\
Type "help", "copyright", "credits" or "license" for more information.\
\>>> import sys\
\>>> sys.\_xoptions\
{'a': 'b', 'c': True}\
\
**CPython implementation detail:** This is a CPython-specific way of accessing options passed through [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)\
. Other implementations may export them through other means, or not at all.\
\
Added in version 3.2.\
\
Citations\
\
\[[C99](https://docs.python.org/3/library/sys.html#id1)\
\]\
\
ISO/IEC 9899:1999. “Programming languages – C.” A public draft of this standard is available at [https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf)\
.\
\
#### Previous topic\
\
[Python Runtime Services](https://docs.python.org/3/library/python.html "previous chapter")\
\
#### Next topic\
\
[`sys.monitoring` — Execution event monitoring](https://docs.python.org/3/library/sys.monitoring.html "next chapter")\
\
### This page\
\
*   [Report a bug](https://docs.python.org/3/bugs.html)\
    \
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=sys+%E2%80%94+System-specific+parameters+and+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsys.html&pagesource=library%2Fsys.rst)\
    \
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/sys.rst?plain=1)\
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
*   [next](https://docs.python.org/3/library/sys.monitoring.html "sys.monitoring — Execution event monitoring")\
     |\
*   [previous](https://docs.python.org/3/library/python.html "Python Runtime Services")\
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
*   [The Python standard library](https://docs.python.org/3/library/index.html)\
     »\
*   [Python Runtime Services](https://docs.python.org/3/library/python.html)\
     »\
*   [`sys` — System-specific parameters and functions](https://docs.python.org/3/library/sys.html)\
    \
*    \
    \
    |\
*   Theme Auto Light Dark |