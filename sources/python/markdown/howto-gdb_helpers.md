### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/enum.html "Enum HOWTO")
     |
*   [previous](https://docs.python.org/3/howto/descriptor.html "Descriptor Guide")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [Debugging C API extensions and CPython Internals with GDB](https://docs.python.org/3/howto/gdb_helpers.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Debugging C API extensions and CPython Internals with GDB[¶](https://docs.python.org/3/howto/gdb_helpers.html#debugging-c-api-extensions-and-cpython-internals-with-gdb "Link to this heading")

================================================================================================================================================================================================

This document explains how the Python GDB extension, `python-gdb.py`, can be used with the GDB debugger to debug CPython extensions and the CPython interpreter itself.

When debugging low-level problems such as crashes or deadlocks, a low-level debugger, such as GDB, is useful to diagnose and correct the issue. By default, GDB (or any of its front-ends) doesn’t support high-level information specific to the CPython interpreter.

The `python-gdb.py` extension adds CPython interpreter information to GDB. The extension helps introspect the stack of currently executing Python functions. Given a Python object represented by a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\* pointer, the extension surfaces the type and value of the object.

Developers who are working on CPython extensions or tinkering with parts of CPython that are written in C can use this document to learn how to use the `python-gdb.py` extension with GDB.

Note

This document assumes that you are familiar with the basics of GDB and the CPython C API. It consolidates guidance from the [devguide](https://devguide.python.org/)
 and the [Python wiki](https://wiki.python.org/moin/DebuggingWithGdb)
.

Prerequisites[¶](https://docs.python.org/3/howto/gdb_helpers.html#prerequisites "Link to this heading")

--------------------------------------------------------------------------------------------------------

You need to have:

*   GDB 7 or later. (For earlier versions of GDB, see `Misc/gdbinit` in the sources of Python 3.11 or earlier.)
    
*   GDB-compatible debugging information for Python and any extension you are debugging.
    
*   The `python-gdb.py` extension.
    

The extension is built with Python, but might be distributed separately or not at all. Below, we include tips for a few common systems as examples. Note that even if the instructions match your system, they might be outdated.

### Setup with Python built from source[¶](https://docs.python.org/3/howto/gdb_helpers.html#setup-with-python-built-from-source "Link to this heading")

When you build CPython from source, debugging information should be available, and the build should add a `python-gdb.py` file to the root directory of your repository.

To activate support, you must add the directory containing `python-gdb.py` to GDB’s “auto-load-safe-path”. If you haven’t done this, recent versions of GDB will print out a warning with instructions on how to do this.

Note

If you do not see instructions for your version of GDB, put this in your configuration file (`~/.gdbinit` or `~/.config/gdb/gdbinit`):

add-auto-load-safe-path /path/to/cpython

You can also add multiple paths, separated by `:`.

### Setup for Python from a Linux distro[¶](https://docs.python.org/3/howto/gdb_helpers.html#setup-for-python-from-a-linux-distro "Link to this heading")

Most Linux systems provide debug information for the system Python in a package called `python-debuginfo`, `python-dbg` or similar. For example:

*   Fedora:
    
    > sudo dnf install gdb
    > sudo dnf debuginfo-install python3
    
*   Ubuntu:
    
    > sudo apt install gdb python3-dbg
    

On several recent Linux systems, GDB can download debugging symbols automatically using _debuginfod_. However, this will not install the `python-gdb.py` extension; you generally do need to install the debug info package separately.

Using the Debug build and Development mode[¶](https://docs.python.org/3/howto/gdb_helpers.html#using-the-debug-build-and-development-mode "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------

For easier debugging, you might want to:

*   Use a [debug build](https://docs.python.org/3/using/configure.html#debug-build)
     of Python. (When building from source, use `configure --with-pydebug`. On Linux distros, install and run a package like `python-debug` or `python-dbg`, if available.)
    
*   Use the runtime [development mode](https://docs.python.org/3/library/devmode.html#devmode)
     (`-X dev`).
    

Both enable extra assertions and disable some optimizations. Sometimes this hides the bug you are trying to find, but in most cases they make the process easier.

Using the `python-gdb` extension[¶](https://docs.python.org/3/howto/gdb_helpers.html#using-the-python-gdb-extension "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

When the extension is loaded, it provides two main features: pretty printers for Python values, and additional commands.

### Pretty-printers[¶](https://docs.python.org/3/howto/gdb_helpers.html#pretty-printers "Link to this heading")

This is what a GDB backtrace looks like (truncated) when this extension is enabled:

#0  0x000000000041a6b1 in PyObject\_Malloc (nbytes=Cannot access memory at address 0x7fffff7fefe8
) at Objects/obmalloc.c:748
#1  0x000000000041b7c0 in \_PyObject\_DebugMallocApi (id=111 'o', nbytes=24) at Objects/obmalloc.c:1445
#2  0x000000000041b717 in \_PyObject\_DebugMalloc (nbytes=24) at Objects/obmalloc.c:1412
#3  0x000000000044060a in \_PyUnicode\_New (length=11) at Objects/unicodeobject.c:346
#4  0x00000000004466aa in PyUnicodeUCS2\_DecodeUTF8Stateful (s=0x5c2b8d "\_\_lltrace\_\_", size=11, errors=0x0, consumed=
    0x0) at Objects/unicodeobject.c:2531
#5  0x0000000000446647 in PyUnicodeUCS2\_DecodeUTF8 (s=0x5c2b8d "\_\_lltrace\_\_", size=11, errors=0x0)
    at Objects/unicodeobject.c:2495
#6  0x0000000000440d1b in PyUnicodeUCS2\_FromStringAndSize (u=0x5c2b8d "\_\_lltrace\_\_", size=11)
    at Objects/unicodeobject.c:551
#7  0x0000000000440d94 in PyUnicodeUCS2\_FromString (u=0x5c2b8d "\_\_lltrace\_\_") at Objects/unicodeobject.c:569
#8  0x0000000000584abd in PyDict\_GetItemString (v=
    {'Yuck': <type at remote 0xad4730>, '\_\_builtins\_\_': <module at remote 0x7ffff7fd5ee8>, '\_\_file\_\_': 'Lib/test/crashers/nasty\_eq\_vs\_dict.py', '\_\_package\_\_': None, 'y': <Yuck(i=0) at remote 0xaacd80>, 'dict': {0: 0, 1: 1, 2: 2, 3: 3}, '\_\_name\_\_': '\_\_main\_\_', 'z': <Yuck(i=0) at remote 0xaace60>, '\_\_doc\_\_': None}, key=
    0x5c2b8d "\_\_lltrace\_\_") at Objects/dictobject.c:2171

Notice how the dictionary argument to `PyDict_GetItemString` is displayed as its `repr()`, rather than an opaque `PyObject *` pointer.

The extension works by supplying a custom printing routine for values of type `PyObject *`. If you need to access lower-level details of an object, then cast the value to a pointer of the appropriate type. For example:

(gdb) p globals
$1 = {'\_\_builtins\_\_': <module at remote 0x7ffff7fb1868>, '\_\_name\_\_':
'\_\_main\_\_', 'ctypes': <module at remote 0x7ffff7f14360>, '\_\_doc\_\_': None,
'\_\_package\_\_': None}

(gdb) p \*(PyDictObject\*)globals
$2 = {ob\_refcnt = 3, ob\_type = 0x3dbdf85820, ma\_fill = 5, ma\_used = 5,
ma\_mask = 7, ma\_table = 0x63d0f8, ma\_lookup = 0x3dbdc7ea70
<lookdict\_string>, ma\_smalltable = {{me\_hash = 7065186196740147912,
me\_key = '\_\_builtins\_\_', me\_value = <module at remote 0x7ffff7fb1868>},
{me\_hash = -368181376027291943, me\_key = '\_\_name\_\_',
me\_value ='\_\_main\_\_'}, {me\_hash = 0, me\_key = 0x0, me\_value = 0x0},
{me\_hash = 0, me\_key = 0x0, me\_value = 0x0},
{me\_hash = -9177857982131165996, me\_key = 'ctypes',
me\_value = <module at remote 0x7ffff7f14360>},
{me\_hash = -8518757509529533123, me\_key = '\_\_doc\_\_', me\_value = None},
{me\_hash = 0, me\_key = 0x0, me\_value = 0x0}, {
  me\_hash = 6614918939584953775, me\_key = '\_\_package\_\_', me\_value = None}}}

Note that the pretty-printers do not actually call `repr()`. For basic types, they try to match its result closely.

An area that can be confusing is that the custom printer for some types look a lot like GDB’s built-in printer for standard types. For example, the pretty-printer for a Python `int` ([PyLongObject](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
\*) gives a representation that is not distinguishable from one of a regular machine-level integer:

(gdb) p some\_machine\_integer
$3 = 42

(gdb) p some\_python\_integer
$4 = 42

The internal structure can be revealed with a cast to [PyLongObject](https://docs.python.org/3/c-api/long.html#c.PyLongObject "PyLongObject")
\*:

(gdb) p \*(PyLongObject\*)some\_python\_integer
$5 = {ob\_base = {ob\_base = {ob\_refcnt = 8, ob\_type = 0x3dad39f5e0}, ob\_size = 1},
ob\_digit = {42}}

A similar confusion can arise with the `str` type, where the output looks a lot like gdb’s built-in printer for `char *`:

(gdb) p ptr\_to\_python\_str
$6 = '\_\_builtins\_\_'

The pretty-printer for `str` instances defaults to using single-quotes (as does Python’s `repr` for strings) whereas the standard printer for `char *` values uses double-quotes and contains a hexadecimal address:

(gdb) p ptr\_to\_char\_star
$7 = 0x6d72c0 "hello world"

Again, the implementation details can be revealed with a cast to [PyUnicodeObject](https://docs.python.org/3/c-api/unicode.html#c.PyUnicodeObject "PyUnicodeObject")
\*:

(gdb) p \*(PyUnicodeObject\*)$6
$8 = {ob\_base = {ob\_refcnt = 33, ob\_type = 0x3dad3a95a0}, length = 12,
str = 0x7ffff2128500, hash = 7065186196740147912, state = 1, defenc = 0x0}

### `py-list`[¶](https://docs.python.org/3/howto/gdb_helpers.html#py-list "Link to this heading")

> The extension adds a `py-list` command, which lists the Python source code (if any) for the current frame in the selected thread. The current line is marked with a “>”:
> 
> (gdb) py-list
>  901        if options.profile:
>  902            options.profile = False
>  903            profile\_me()
>  904            return
>  905
> >906        u = UI()
>  907        if not u.quit:
>  908            try:
>  909                gtk.main()
>  910            except KeyboardInterrupt:
>  911                # properly quit on a keyboard interrupt...
> 
> Use `py-list START` to list at a different line number within the Python source, and `py-list START,END` to list a specific range of lines within the Python source.

### `py-up` and `py-down`[¶](https://docs.python.org/3/howto/gdb_helpers.html#py-up-and-py-down "Link to this heading")

> The `py-up` and `py-down` commands are analogous to GDB’s regular `up` and `down` commands, but try to move at the level of CPython frames, rather than C frames.
> 
> GDB is not always able to read the relevant frame information, depending on the optimization level with which CPython was compiled. Internally, the commands look for C frames that are executing the default frame evaluation function (that is, the core bytecode interpreter loop within CPython) and look up the value of the related `PyFrameObject *`.
> 
> They emit the frame number (at the C level) within the thread.
> 
> For example:
> 
> (gdb) py-up
> #37 Frame 0x9420b04, for file /usr/lib/python2.6/site-packages/
> gnome\_sudoku/main.py, line 906, in start\_game ()
>     u = UI()
> (gdb) py-up
> #40 Frame 0x948e82c, for file /usr/lib/python2.6/site-packages/
> gnome\_sudoku/gnome\_sudoku.py, line 22, in start\_game(main=<module at remote 0xb771b7f4>)
>     main.start\_game()
> (gdb) py-up
> Unable to find an older python frame
> 
> so we’re at the top of the Python stack.
> 
> The frame numbers correspond to those displayed by GDB’s standard `backtrace` command. The command skips C frames which are not executing Python code.
> 
> Going back down:
> 
> (gdb) py-down
> #37 Frame 0x9420b04, for file /usr/lib/python2.6/site-packages/gnome\_sudoku/main.py, line 906, in start\_game ()
>     u = UI()
> (gdb) py-down
> #34 (unable to read python frame information)
> (gdb) py-down
> #23 (unable to read python frame information)
> (gdb) py-down
> #19 (unable to read python frame information)
> (gdb) py-down
> #14 Frame 0x99262ac, for file /usr/lib/python2.6/site-packages/gnome\_sudoku/game\_selector.py, line 201, in run\_swallowed\_dialog (self=<NewOrSavedGameSelector(new\_game\_model=<gtk.ListStore at remote 0x98fab44>, puzzle=None, saved\_games=\[{'gsd.auto\_fills': 0, 'tracking': {}, 'trackers': {}, 'notes': \[\], 'saved\_at': 1270084485, 'game': '7 8 0 0 0 0 0 5 6 0 0 9 0 8 0 1 0 0 0 4 6 0 0 0 0 7 0 6 5 0 0 0 4 7 9 2 0 0 0 9 0 1 0 0 0 3 9 7 6 0 0 0 1 8 0 6 0 0 0 0 2 8 0 0 0 5 0 4 0 6 0 0 2 1 0 0 0 0 0 4 5\\n7 8 0 0 0 0 0 5 6 0 0 9 0 8 0 1 0 0 0 4 6 0 0 0 0 7 0 6 5 1 8 3 4 7 9 2 0 0 0 9 0 1 0 0 0 3 9 7 6 0 0 0 1 8 0 6 0 0 0 0 2 8 0 0 0 5 0 4 0 6 0 0 2 1 0 0 0 0 0 4 5', 'gsd.impossible\_hints': 0, 'timer.\_\_absolute\_start\_time\_\_': <float at remote 0x984b474>, 'gsd.hints': 0, 'timer.active\_time': <float at remote 0x984b494>, 'timer.total\_time': <float at remote 0x984b464>}\], dialog=<gtk.Dialog at remote 0x98faaa4>, saved\_game\_model=<gtk.ListStore at remote 0x98fad24>, sudoku\_maker=<SudokuMaker(terminated=False, played=\[\], batch\_siz...(truncated)
>             swallower.run\_dialog(self.dialog)
> (gdb) py-down
> #11 Frame 0x9aead74, for file /usr/lib/python2.6/site-packages/gnome\_sudoku/dialog\_swallower.py, line 48, in run\_dialog (self=<SwappableArea(running=<gtk.Dialog at remote 0x98faaa4>, main\_page=0) at remote 0x98fa6e4>, d=<gtk.Dialog at remote 0x98faaa4>)
>             gtk.main()
> (gdb) py-down
> #8 (unable to read python frame information)
> (gdb) py-down
> Unable to find a newer python frame
> 
> and we’re at the bottom of the Python stack.
> 
> Note that in Python 3.12 and newer, the same C stack frame can be used for multiple Python stack frames. This means that `py-up` and `py-down` may move multiple Python frames at once. For example:
> 
> (gdb) py-up
> #6 Frame 0x7ffff7fb62b0, for file /tmp/rec.py, line 5, in recursive\_function (n=0)
>    time.sleep(5)
> #6 Frame 0x7ffff7fb6240, for file /tmp/rec.py, line 7, in recursive\_function (n=1)
>    recursive\_function(n-1)
> #6 Frame 0x7ffff7fb61d0, for file /tmp/rec.py, line 7, in recursive\_function (n=2)
>    recursive\_function(n-1)
> #6 Frame 0x7ffff7fb6160, for file /tmp/rec.py, line 7, in recursive\_function (n=3)
>    recursive\_function(n-1)
> #6 Frame 0x7ffff7fb60f0, for file /tmp/rec.py, line 7, in recursive\_function (n=4)
>    recursive\_function(n-1)
> #6 Frame 0x7ffff7fb6080, for file /tmp/rec.py, line 7, in recursive\_function (n=5)
>    recursive\_function(n-1)
> #6 Frame 0x7ffff7fb6020, for file /tmp/rec.py, line 9, in <module> ()
>    recursive\_function(5)
> (gdb) py-up
> Unable to find an older python frame

### `py-bt`[¶](https://docs.python.org/3/howto/gdb_helpers.html#py-bt "Link to this heading")

> The `py-bt` command attempts to display a Python-level backtrace of the current thread.
> 
> For example:
> 
> (gdb) py-bt
> #8 (unable to read python frame information)
> #11 Frame 0x9aead74, for file /usr/lib/python2.6/site-packages/gnome\_sudoku/dialog\_swallower.py, line 48, in run\_dialog (self=<SwappableArea(running=<gtk.Dialog at remote 0x98faaa4>, main\_page=0) at remote 0x98fa6e4>, d=<gtk.Dialog at remote 0x98faaa4>)
>             gtk.main()
> #14 Frame 0x99262ac, for file /usr/lib/python2.6/site-packages/gnome\_sudoku/game\_selector.py, line 201, in run\_swallowed\_dialog (self=<NewOrSavedGameSelector(new\_game\_model=<gtk.ListStore at remote 0x98fab44>, puzzle=None, saved\_games=\[{'gsd.auto\_fills': 0, 'tracking': {}, 'trackers': {}, 'notes': \[\], 'saved\_at': 1270084485, 'game': '7 8 0 0 0 0 0 5 6 0 0 9 0 8 0 1 0 0 0 4 6 0 0 0 0 7 0 6 5 0 0 0 4 7 9 2 0 0 0 9 0 1 0 0 0 3 9 7 6 0 0 0 1 8 0 6 0 0 0 0 2 8 0 0 0 5 0 4 0 6 0 0 2 1 0 0 0 0 0 4 5\\n7 8 0 0 0 0 0 5 6 0 0 9 0 8 0 1 0 0 0 4 6 0 0 0 0 7 0 6 5 1 8 3 4 7 9 2 0 0 0 9 0 1 0 0 0 3 9 7 6 0 0 0 1 8 0 6 0 0 0 0 2 8 0 0 0 5 0 4 0 6 0 0 2 1 0 0 0 0 0 4 5', 'gsd.impossible\_hints': 0, 'timer.\_\_absolute\_start\_time\_\_': <float at remote 0x984b474>, 'gsd.hints': 0, 'timer.active\_time': <float at remote 0x984b494>, 'timer.total\_time': <float at remote 0x984b464>}\], dialog=<gtk.Dialog at remote 0x98faaa4>, saved\_game\_model=<gtk.ListStore at remote 0x98fad24>, sudoku\_maker=<SudokuMaker(terminated=False, played=\[\], batch\_siz...(truncated)
>             swallower.run\_dialog(self.dialog)
> #19 (unable to read python frame information)
> #23 (unable to read python frame information)
> #34 (unable to read python frame information)
> #37 Frame 0x9420b04, for file /usr/lib/python2.6/site-packages/gnome\_sudoku/main.py, line 906, in start\_game ()
>     u = UI()
> #40 Frame 0x948e82c, for file /usr/lib/python2.6/site-packages/gnome\_sudoku/gnome\_sudoku.py, line 22, in start\_game (main=<module at remote 0xb771b7f4>)
>     main.start\_game()
> 
> The frame numbers correspond to those displayed by GDB’s standard `backtrace` command.

### `py-print`[¶](https://docs.python.org/3/howto/gdb_helpers.html#py-print "Link to this heading")

> The `py-print` command looks up a Python name and tries to print it. It looks in locals within the current thread, then globals, then finally builtins:
> 
> (gdb) py-print self
> local 'self' = <SwappableArea(running=<gtk.Dialog at remote 0x98faaa4>,
> main\_page=0) at remote 0x98fa6e4>
> (gdb) py-print \_\_name\_\_
> global '\_\_name\_\_' = 'gnome\_sudoku.dialog\_swallower'
> (gdb) py-print len
> builtin 'len' = <built-in function len>
> (gdb) py-print scarlet\_pimpernel
> 'scarlet\_pimpernel' not found
> 
> If the current C frame corresponds to multiple Python frames, `py-print` only considers the first one.

### `py-locals`[¶](https://docs.python.org/3/howto/gdb_helpers.html#py-locals "Link to this heading")

> The `py-locals` command looks up all Python locals within the current Python frame in the selected thread, and prints their representations:
> 
> (gdb) py-locals
> self = <SwappableArea(running=<gtk.Dialog at remote 0x98faaa4>,
> main\_page=0) at remote 0x98fa6e4>
> d = <gtk.Dialog at remote 0x98faaa4>
> 
> If the current C frame corresponds to multiple Python frames, locals from all of them will be shown:
> 
> (gdb) py-locals
> Locals for recursive\_function
> n = 0
> Locals for recursive\_function
> n = 1
> Locals for recursive\_function
> n = 2
> Locals for recursive\_function
> n = 3
> Locals for recursive\_function
> n = 4
> Locals for recursive\_function
> n = 5
> Locals for <module>

Use with GDB commands[¶](https://docs.python.org/3/howto/gdb_helpers.html#use-with-gdb-commands "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

The extension commands complement GDB’s built-in commands. For example, you can use a frame numbers shown by `py-bt` with the `frame` command to go a specific frame within the selected thread, like this:

(gdb) py-bt
(output snipped)
#68 Frame 0xaa4560, for file Lib/test/regrtest.py, line 1548, in <module> ()
        main()
(gdb) frame 68
#68 0x00000000004cd1e6 in PyEval\_EvalFrameEx (f=Frame 0xaa4560, for file Lib/test/regrtest.py, line 1548, in <module> (), throwflag=0) at Python/ceval.c:2665
2665                            x = call\_function(&sp, oparg);
(gdb) py-list
1543        # Run the tests in a context manager that temporary changes the CWD to a
1544        # temporary and writable directory. If it's not possible to create or
1545        # change the CWD, the original CWD will be used. The original CWD is
1546        # available from test\_support.SAVEDCWD.
1547        with test\_support.temp\_cwd(TESTCWD, quiet=True):
>1548            main()

The `info threads` command will give you a list of the threads within the process, and you can use the `thread` command to select a different one:

(gdb) info threads
  105 Thread 0x7fffefa18710 (LWP 10260)  sem\_wait () at ../nptl/sysdeps/unix/sysv/linux/x86\_64/sem\_wait.S:86
  104 Thread 0x7fffdf5fe710 (LWP 10259)  sem\_wait () at ../nptl/sysdeps/unix/sysv/linux/x86\_64/sem\_wait.S:86
\* 1 Thread 0x7ffff7fe2700 (LWP 10145)  0x00000038e46d73e3 in select () at ../sysdeps/unix/syscall-template.S:82

You can use `thread apply all COMMAND` or (`t a a COMMAND` for short) to run a command on all threads. With `py-bt`, this lets you see what every thread is doing at the Python level:

(gdb) t a a py-bt

Thread 105 (Thread 0x7fffefa18710 (LWP 10260)):
#5 Frame 0x7fffd00019d0, for file /home/david/coding/python-svn/Lib/threading.py, line 155, in \_acquire\_restore (self=<\_RLock(\_Verbose\_\_verbose=False, \_RLock\_\_owner=140737354016512, \_RLock\_\_block=<thread.lock at remote 0x858770>, \_RLock\_\_count=1) at remote 0xd7ff40>, count\_owner=(1, 140737213728528), count=1, owner=140737213728528)
        self.\_\_block.acquire()
#8 Frame 0x7fffac001640, for file /home/david/coding/python-svn/Lib/threading.py, line 269, in wait (self=<\_Condition(\_Condition\_\_lock=<\_RLock(\_Verbose\_\_verbose=False, \_RLock\_\_owner=140737354016512, \_RLock\_\_block=<thread.lock at remote 0x858770>, \_RLock\_\_count=1) at remote 0xd7ff40>, acquire=<instancemethod at remote 0xd80260>, \_is\_owned=<instancemethod at remote 0xd80160>, \_release\_save=<instancemethod at remote 0xd803e0>, release=<instancemethod at remote 0xd802e0>, \_acquire\_restore=<instancemethod at remote 0xd7ee60>, \_Verbose\_\_verbose=False, \_Condition\_\_waiters=\[\]) at remote 0xd7fd10>, timeout=None, waiter=<thread.lock at remote 0x858a90>, saved\_state=(1, 140737213728528))
            self.\_acquire\_restore(saved\_state)
#12 Frame 0x7fffb8001a10, for file /home/david/coding/python-svn/Lib/test/lock\_tests.py, line 348, in f ()
            cond.wait()
#16 Frame 0x7fffb8001c40, for file /home/david/coding/python-svn/Lib/test/lock\_tests.py, line 37, in task (tid=140737213728528)
                f()

Thread 104 (Thread 0x7fffdf5fe710 (LWP 10259)):
#5 Frame 0x7fffe4001580, for file /home/david/coding/python-svn/Lib/threading.py, line 155, in \_acquire\_restore (self=<\_RLock(\_Verbose\_\_verbose=False, \_RLock\_\_owner=140737354016512, \_RLock\_\_block=<thread.lock at remote 0x858770>, \_RLock\_\_count=1) at remote 0xd7ff40>, count\_owner=(1, 140736940992272), count=1, owner=140736940992272)
        self.\_\_block.acquire()
#8 Frame 0x7fffc8002090, for file /home/david/coding/python-svn/Lib/threading.py, line 269, in wait (self=<\_Condition(\_Condition\_\_lock=<\_RLock(\_Verbose\_\_verbose=False, \_RLock\_\_owner=140737354016512, \_RLock\_\_block=<thread.lock at remote 0x858770>, \_RLock\_\_count=1) at remote 0xd7ff40>, acquire=<instancemethod at remote 0xd80260>, \_is\_owned=<instancemethod at remote 0xd80160>, \_release\_save=<instancemethod at remote 0xd803e0>, release=<instancemethod at remote 0xd802e0>, \_acquire\_restore=<instancemethod at remote 0xd7ee60>, \_Verbose\_\_verbose=False, \_Condition\_\_waiters=\[\]) at remote 0xd7fd10>, timeout=None, waiter=<thread.lock at remote 0x858860>, saved\_state=(1, 140736940992272))
            self.\_acquire\_restore(saved\_state)
#12 Frame 0x7fffac001c90, for file /home/david/coding/python-svn/Lib/test/lock\_tests.py, line 348, in f ()
            cond.wait()
#16 Frame 0x7fffac0011c0, for file /home/david/coding/python-svn/Lib/test/lock\_tests.py, line 37, in task (tid=140736940992272)
                f()

Thread 1 (Thread 0x7ffff7fe2700 (LWP 10145)):
#5 Frame 0xcb5380, for file /home/david/coding/python-svn/Lib/test/lock\_tests.py, line 16, in \_wait ()
    time.sleep(0.01)
#8 Frame 0x7fffd00024a0, for file /home/david/coding/python-svn/Lib/test/lock\_tests.py, line 378, in \_check\_notify (self=<ConditionTests(\_testMethodName='test\_notify', \_resultForDoCleanups=<TestResult(\_original\_stdout=<cStringIO.StringO at remote 0xc191e0>, skipped=\[\], \_mirrorOutput=False, testsRun=39, buffer=False, \_original\_stderr=<file at remote 0x7ffff7fc6340>, \_stdout\_buffer=<cStringIO.StringO at remote 0xc9c7f8>, \_stderr\_buffer=<cStringIO.StringO at remote 0xc9c790>, \_moduleSetUpFailed=False, expectedFailures=\[\], errors=\[\], \_previousTestClass=<type at remote 0x928310>, unexpectedSuccesses=\[\], failures=\[\], shouldStop=False, failfast=False) at remote 0xc185a0>, \_threads=(0,), \_cleanups=\[\], \_type\_equality\_funcs={<type at remote 0x7eba00>: <instancemethod at remote 0xd750e0>, <type at remote 0x7e7820>: <instancemethod at remote 0xd75160>, <type at remote 0x7e30e0>: <instancemethod at remote 0xd75060>, <type at remote 0x7e7d20>: <instancemethod at remote 0xd751e0>, <type at remote 0x7f19e0...(truncated)
        \_wait()

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Debugging C API extensions and CPython Internals with GDB](https://docs.python.org/3/howto/gdb_helpers.html#)
    *   [Prerequisites](https://docs.python.org/3/howto/gdb_helpers.html#prerequisites)
        *   [Setup with Python built from source](https://docs.python.org/3/howto/gdb_helpers.html#setup-with-python-built-from-source)
            
        *   [Setup for Python from a Linux distro](https://docs.python.org/3/howto/gdb_helpers.html#setup-for-python-from-a-linux-distro)
            
    *   [Using the Debug build and Development mode](https://docs.python.org/3/howto/gdb_helpers.html#using-the-debug-build-and-development-mode)
        
    *   [Using the `python-gdb` extension](https://docs.python.org/3/howto/gdb_helpers.html#using-the-python-gdb-extension)
        *   [Pretty-printers](https://docs.python.org/3/howto/gdb_helpers.html#pretty-printers)
            
        *   [`py-list`](https://docs.python.org/3/howto/gdb_helpers.html#py-list)
            
        *   [`py-up` and `py-down`](https://docs.python.org/3/howto/gdb_helpers.html#py-up-and-py-down)
            
        *   [`py-bt`](https://docs.python.org/3/howto/gdb_helpers.html#py-bt)
            
        *   [`py-print`](https://docs.python.org/3/howto/gdb_helpers.html#py-print)
            
        *   [`py-locals`](https://docs.python.org/3/howto/gdb_helpers.html#py-locals)
            
    *   [Use with GDB commands](https://docs.python.org/3/howto/gdb_helpers.html#use-with-gdb-commands)
        

#### Previous topic

[Descriptor Guide](https://docs.python.org/3/howto/descriptor.html "previous chapter")

#### Next topic

[Enum HOWTO](https://docs.python.org/3/howto/enum.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Debugging+C+API+extensions+and+CPython+Internals+with+GDB&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fhowto%2Fgdb_helpers.html&pagesource=howto%2Fgdb_helpers.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/howto/gdb_helpers.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/howto/enum.html "Enum HOWTO")
     |
*   [previous](https://docs.python.org/3/howto/descriptor.html "Descriptor Guide")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python HOWTOs](https://docs.python.org/3/howto/index.html)
     »
*   [Debugging C API extensions and CPython Internals with GDB](https://docs.python.org/3/howto/gdb_helpers.html)
    
*    
    
    |
*   Theme Auto Light Dark |