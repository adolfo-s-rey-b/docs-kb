### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/3.2.html "What’s New In Python 3.2")
     |
*   [previous](https://docs.python.org/3/whatsnew/3.4.html "What’s New In Python 3.4")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [What’s New in Python](https://docs.python.org/3/whatsnew/index.html)
     »
*   [What’s New In Python 3.3](https://docs.python.org/3/whatsnew/3.3.html)
    
*    
    
    |
*   Theme Auto Light Dark |

What’s New In Python 3.3[¶](https://docs.python.org/3/whatsnew/3.3.html#what-s-new-in-python-3-3 "Link to this heading")

=========================================================================================================================

This article explains the new features in Python 3.3, compared to 3.2. Python 3.3 was released on September 29, 2012. For full details, see the [changelog](https://docs.python.org/3.3/whatsnew/changelog.html)
.

See also

[**PEP 398**](https://peps.python.org/pep-0398/)
 - Python 3.3 Release Schedule

Summary – Release highlights[¶](https://docs.python.org/3/whatsnew/3.3.html#summary-release-highlights "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

New syntax features:

*   New `yield from` expression for [generator delegation](https://docs.python.org/3/whatsnew/3.3.html#pep-380)
    .
    
*   The `u'unicode'` syntax is accepted again for [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     objects.
    

New library modules:

*   [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.")
     (helps debugging low-level crashes)
    
*   [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.")
     (high-level objects representing IP addresses and masks)
    
*   [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
     (compress data using the XZ / LZMA algorithm)
    
*   [`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock "unittest.mock: Mock object library.")
     (replace parts of your system under test with mock objects)
    
*   [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.")
     (Python [virtual environments](https://docs.python.org/3/whatsnew/3.3.html#pep-405)
    , as in the popular `virtualenv` package)
    

New built-in features:

*   Reworked [I/O exception hierarchy](https://docs.python.org/3/whatsnew/3.3.html#pep-3151)
    .
    

Implementation improvements:

*   Rewritten [import machinery](https://docs.python.org/3/whatsnew/3.3.html#importlib)
     based on [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
    .
    
*   More compact [unicode strings](https://docs.python.org/3/whatsnew/3.3.html#pep-393)
    .
    
*   More compact [attribute dictionaries](https://docs.python.org/3/whatsnew/3.3.html#pep-412)
    .
    

Significantly Improved Library Modules:

*   C Accelerator for the [decimal](https://docs.python.org/3/whatsnew/3.3.html#new-decimal)
     module.
    
*   Better unicode handling in the [email](https://docs.python.org/3/whatsnew/3.3.html#new-email)
     module ([provisional](https://docs.python.org/3/glossary.html#term-provisional-package)
    ).
    

Security improvements:

*   Hash randomization is switched on by default.
    

Please read on for a comprehensive list of user-facing changes.

PEP 405: Virtual Environments[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-405-virtual-environments "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Virtual environments help create separate Python setups while sharing a system-wide base install, for ease of maintenance. Virtual environments have their own set of private site packages (i.e. locally installed libraries), and are optionally segregated from the system-wide site packages. Their concept and implementation are inspired by the popular `virtualenv` third-party package, but benefit from tighter integration with the interpreter core.

This PEP adds the [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.")
 module for programmatic access, and the `pyvenv` script for command-line access and administration. The Python interpreter checks for a `pyvenv.cfg`, file whose existence signals the base of a virtual environment’s directory tree.

See also

[**PEP 405**](https://peps.python.org/pep-0405/)
 - Python Virtual Environments

PEP written by Carl Meyer; implementation by Carl Meyer and Vinay Sajip

PEP 420: Implicit Namespace Packages[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-420-implicit-namespace-packages "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Native support for package directories that don’t require `__init__.py` marker files and can automatically span multiple path segments (inspired by various third party approaches to namespace packages, as described in [**PEP 420**](https://peps.python.org/pep-0420/)
)

See also

[**PEP 420**](https://peps.python.org/pep-0420/)
 - Implicit Namespace Packages

PEP written by Eric V. Smith; implementation by Eric V. Smith and Barry Warsaw

PEP 3118: New memoryview implementation and buffer protocol documentation[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-3118-new-memoryview-implementation-and-buffer-protocol-documentation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The implementation of [**PEP 3118**](https://peps.python.org/pep-3118/)
 has been significantly improved.

The new memoryview implementation comprehensively fixes all ownership and lifetime issues of dynamically allocated fields in the Py\_buffer struct that led to multiple crash reports. Additionally, several functions that crashed or returned incorrect results for non-contiguous or multi-dimensional input have been fixed.

The memoryview object now has a PEP-3118 compliant getbufferproc() that checks the consumer’s request type. Many new features have been added, most of them work in full generality for non-contiguous arrays and arrays with suboffsets.

The documentation has been updated, clearly spelling out responsibilities for both exporters and consumers. Buffer request flags are grouped into basic and compound flags. The memory layout of non-contiguous and multi-dimensional NumPy-style arrays is explained.

### Features[¶](https://docs.python.org/3/whatsnew/3.3.html#features "Link to this heading")

*   All native single character format specifiers in struct module syntax (optionally prefixed with ‘@’) are now supported.
    
*   With some restrictions, the cast() method allows changing of format and shape of C-contiguous arrays.
    
*   Multi-dimensional list representations are supported for any array type.
    
*   Multi-dimensional comparisons are supported for any array type.
    
*   One-dimensional memoryviews of hashable (read-only) types with formats B, b or c are now hashable. (Contributed by Antoine Pitrou in [bpo-13411](https://bugs.python.org/issue?@action=redirect&bpo=13411)
    .)
    
*   Arbitrary slicing of any 1-D arrays type is supported. For example, it is now possible to reverse a memoryview in _O_(1) by using a negative step.
    

### API changes[¶](https://docs.python.org/3/whatsnew/3.3.html#api-changes "Link to this heading")

*   The maximum number of dimensions is officially limited to 64.
    
*   The representation of empty shape, strides and suboffsets is now an empty tuple instead of `None`.
    
*   Accessing a memoryview element with format ‘B’ (unsigned bytes) now returns an integer (in accordance with the struct module syntax). For returning a bytes object the view must be cast to ‘c’ first.
    
*   memoryview comparisons now use the logical structure of the operands and compare all array elements by value. All format strings in struct module syntax are supported. Views with unrecognised format strings are still permitted, but will always compare as unequal, regardless of view contents.
    
*   For further changes see [Build and C API Changes](https://docs.python.org/3/whatsnew/3.3.html#build-and-c-api-changes)
     and [Porting C code](https://docs.python.org/3/whatsnew/3.3.html#porting-c-code)
    .
    

(Contributed by Stefan Krah in [bpo-10181](https://bugs.python.org/issue?@action=redirect&bpo=10181)
.)

See also

[**PEP 3118**](https://peps.python.org/pep-3118/)
 - Revising the Buffer Protocol

PEP 393: Flexible String Representation[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-393-flexible-string-representation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

The Unicode string type is changed to support multiple internal representations, depending on the character with the largest Unicode ordinal (1, 2, or 4 bytes) in the represented string. This allows a space-efficient representation in common cases, but gives access to full UCS-4 on all systems. For compatibility with existing APIs, several representations may exist in parallel; over time, this compatibility should be phased out.

On the Python side, there should be no downside to this change.

On the C API side, [**PEP 393**](https://peps.python.org/pep-0393/)
 is fully backward compatible. The legacy API should remain available at least five years. Applications using the legacy API will not fully benefit of the memory reduction, or - worse - may use a bit more memory, because Python may have to maintain two versions of each string (in the legacy format and in the new efficient storage).

### Functionality[¶](https://docs.python.org/3/whatsnew/3.3.html#functionality "Link to this heading")

Changes introduced by [**PEP 393**](https://peps.python.org/pep-0393/)
 are the following:

*   Python now always supports the full range of Unicode code points, including non-BMP ones (i.e. from `U+0000` to `U+10FFFF`). The distinction between narrow and wide builds no longer exists and Python now behaves like a wide build, even under Windows.
    
*   With the death of narrow builds, the problems specific to narrow builds have also been fixed, for example:
    
    *   [`len()`](https://docs.python.org/3/builtins/functions.html#len "len")
         now always returns 1 for non-BMP characters, so `len('\U0010FFFF') == 1`;
        
    *   surrogate pairs are not recombined in string literals, so `'\uDBFF\uDFFF' != '\U0010FFFF'`;
        
    *   indexing or slicing non-BMP characters returns the expected value, so `'\U0010FFFF'[0]` now returns `'\U0010FFFF'` and not `'\uDBFF'`;
        
    *   all other functions in the standard library now correctly handle non-BMP code points.
        
*   The value of [`sys.maxunicode`](https://docs.python.org/3/library/sys.html#sys.maxunicode "sys.maxunicode")
     is now always `1114111` (`0x10FFFF` in hexadecimal). The `PyUnicode_GetMax()` function still returns either `0xFFFF` or `0x10FFFF` for backward compatibility, and it should not be used with the new Unicode API (see [bpo-13054](https://bugs.python.org/issue?@action=redirect&bpo=13054)
    ).
    
*   The `./configure` flag `--with-wide-unicode` has been removed.
    

### Performance and resource usage[¶](https://docs.python.org/3/whatsnew/3.3.html#performance-and-resource-usage "Link to this heading")

The storage of Unicode strings now depends on the highest code point in the string:

*   pure ASCII and Latin1 strings (`U+0000-U+00FF`) use 1 byte per code point;
    
*   BMP strings (`U+0000-U+FFFF`) use 2 bytes per code point;
    
*   non-BMP strings (`U+10000-U+10FFFF`) use 4 bytes per code point.
    

The net effect is that for most applications, memory usage of string storage should decrease significantly - especially compared to former wide unicode builds - as, in many cases, strings will be pure ASCII even in international contexts (because many strings store non-human language data, such as XML fragments, HTTP headers, JSON-encoded data, etc.). We also hope that it will, for the same reasons, increase CPU cache efficiency on non-trivial applications. The memory usage of Python 3.3 is two to three times smaller than Python 3.2, and a little bit better than Python 2.7, on a Django benchmark (see the PEP for details).

See also

[**PEP 393**](https://peps.python.org/pep-0393/)
 - Flexible String Representation

PEP written by Martin von Löwis; implementation by Torsten Becker and Martin von Löwis.

PEP 397: Python Launcher for Windows[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-397-python-launcher-for-windows "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

The Python 3.3 Windows installer now includes a `py` launcher application that can be used to launch Python applications in a version independent fashion.

This launcher is invoked implicitly when double-clicking `*.py` files. If only a single Python version is installed on the system, that version will be used to run the file. If multiple versions are installed, the most recent version is used by default, but this can be overridden by including a Unix-style “shebang line” in the Python script.

The launcher can also be used explicitly from the command line as the `py` application. Running `py` follows the same version selection rules as implicitly launching scripts, but a more specific version can be selected by passing appropriate arguments (such as `-3` to request Python 3 when Python 2 is also installed, or `-2.6` to specifically request an earlier Python version when a more recent version is installed).

In addition to the launcher, the Windows installer now includes an option to add the newly installed Python to the system PATH. (Contributed by Brian Curtin in [bpo-3561](https://bugs.python.org/issue?@action=redirect&bpo=3561)
.)

See also

[**PEP 397**](https://peps.python.org/pep-0397/)
 - Python Launcher for Windows

PEP written by Mark Hammond and Martin v. Löwis; implementation by Vinay Sajip.

Launcher documentation: [Python install manager](https://docs.python.org/3/using/windows.html#launcher)

Installer PATH modification: [Python install manager](https://docs.python.org/3/using/windows.html#windows-path-mod)

PEP 3151: Reworking the OS and IO exception hierarchy[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-3151-reworking-the-os-and-io-exception-hierarchy "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The hierarchy of exceptions raised by operating system errors is now both simplified and finer-grained.

You don’t have to worry anymore about choosing the appropriate exception type between [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
, [`IOError`](https://docs.python.org/3/builtins/exceptions.html#IOError "IOError")
, [`EnvironmentError`](https://docs.python.org/3/builtins/exceptions.html#EnvironmentError "EnvironmentError")
, [`WindowsError`](https://docs.python.org/3/builtins/exceptions.html#WindowsError "WindowsError")
, `mmap.error`, [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "socket.error")
 or [`select.error`](https://docs.python.org/3/library/select.html#select.error "select.error")
. All these exception types are now only one: `OSError`. The other names are kept as aliases for compatibility reasons.

Also, it is now easier to catch a specific error condition. Instead of inspecting the `errno` attribute (or `args[0]`) for a particular constant from the [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.")
 module, you can catch the adequate [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 subclass. The available subclasses are the following:

*   [`BlockingIOError`](https://docs.python.org/3/builtins/exceptions.html#BlockingIOError "BlockingIOError")
    
*   [`ChildProcessError`](https://docs.python.org/3/builtins/exceptions.html#ChildProcessError "ChildProcessError")
    
*   [`ConnectionError`](https://docs.python.org/3/builtins/exceptions.html#ConnectionError "ConnectionError")
    
*   [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")
    
*   [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
    
*   [`InterruptedError`](https://docs.python.org/3/builtins/exceptions.html#InterruptedError "InterruptedError")
    
*   [`IsADirectoryError`](https://docs.python.org/3/builtins/exceptions.html#IsADirectoryError "IsADirectoryError")
    
*   [`NotADirectoryError`](https://docs.python.org/3/builtins/exceptions.html#NotADirectoryError "NotADirectoryError")
    
*   [`PermissionError`](https://docs.python.org/3/builtins/exceptions.html#PermissionError "PermissionError")
    
*   [`ProcessLookupError`](https://docs.python.org/3/builtins/exceptions.html#ProcessLookupError "ProcessLookupError")
    
*   [`TimeoutError`](https://docs.python.org/3/builtins/exceptions.html#TimeoutError "TimeoutError")
    

And the [`ConnectionError`](https://docs.python.org/3/builtins/exceptions.html#ConnectionError "ConnectionError")
 itself has finer-grained subclasses:

*   [`BrokenPipeError`](https://docs.python.org/3/builtins/exceptions.html#BrokenPipeError "BrokenPipeError")
    
*   [`ConnectionAbortedError`](https://docs.python.org/3/builtins/exceptions.html#ConnectionAbortedError "ConnectionAbortedError")
    
*   [`ConnectionRefusedError`](https://docs.python.org/3/builtins/exceptions.html#ConnectionRefusedError "ConnectionRefusedError")
    
*   [`ConnectionResetError`](https://docs.python.org/3/builtins/exceptions.html#ConnectionResetError "ConnectionResetError")
    

Thanks to the new exceptions, common usages of the [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.")
 can now be avoided. For example, the following code written for Python 3.2:

Copy

from errno import ENOENT, EACCES, EPERM

try:
    with open("document.txt") as f:
        content \= f.read()
except IOError as err:
    if err.errno \== ENOENT:
        print("document.txt file is missing")
    elif err.errno in (EACCES, EPERM):
        print("You are not allowed to read document.txt")
    else:
        raise

can now be written without the [`errno`](https://docs.python.org/3/library/errno.html#module-errno "errno: Standard errno system symbols.")
 import and without manual inspection of exception attributes:

Copy

try:
    with open("document.txt") as f:
        content \= f.read()
except FileNotFoundError:
    print("document.txt file is missing")
except PermissionError:
    print("You are not allowed to read document.txt")

See also

[**PEP 3151**](https://peps.python.org/pep-3151/)
 - Reworking the OS and IO Exception Hierarchy

PEP written and implemented by Antoine Pitrou

PEP 380: Syntax for Delegating to a Subgenerator[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-380-syntax-for-delegating-to-a-subgenerator "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

PEP 380 adds the `yield from` expression, allowing a [generator](https://docs.python.org/3/glossary.html#term-generator)
 to delegate part of its operations to another generator. This allows a section of code containing [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield)
 to be factored out and placed in another generator. Additionally, the subgenerator is allowed to return with a value, and the value is made available to the delegating generator.

While designed primarily for use in delegating to a subgenerator, the `yield from` expression actually allows delegation to arbitrary subiterators.

For simple iterators, `yield from iterable` is essentially just a shortened form of `for item in iterable: yield item`:

Copy

\>>> def g(x):
...     yield from range(x, 0, \-1)
...     yield from range(x)
...
\>>> list(g(5))
\[5, 4, 3, 2, 1, 0, 1, 2, 3, 4\]

However, unlike an ordinary loop, `yield from` allows subgenerators to receive sent and thrown values directly from the calling scope, and return a final value to the outer generator:

Copy

\>>> def accumulate():
...     tally \= 0
...     while 1:
...         next \= yield
...         if next is None:
...             return tally
...         tally += next
...
\>>> def gather\_tallies(tallies):
...     while 1:
...         tally \= yield from accumulate()
...         tallies.append(tally)
...
\>>> tallies \= \[\]
\>>> acc \= gather\_tallies(tallies)
\>>> next(acc)  \# Ensure the accumulator is ready to accept values
\>>> for i in range(4):
...     acc.send(i)
...
\>>> acc.send(None)  \# Finish the first tally
\>>> for i in range(5):
...     acc.send(i)
...
\>>> acc.send(None)  \# Finish the second tally
\>>> tallies
\[6, 10\]

The main principle driving this change is to allow even generators that are designed to be used with the `send` and `throw` methods to be split into multiple subgenerators as easily as a single large function can be split into multiple subfunctions.

See also

[**PEP 380**](https://peps.python.org/pep-0380/)
 - Syntax for Delegating to a Subgenerator

PEP written by Greg Ewing; implementation by Greg Ewing, integrated into 3.3 by Renaud Blanch, Ryan Kelly and Nick Coghlan; documentation by Zbigniew Jędrzejewski-Szmek and Nick Coghlan

PEP 409: Suppressing exception context[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-409-suppressing-exception-context "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

PEP 409 introduces new syntax that allows the display of the chained exception context to be disabled. This allows cleaner error messages in applications that convert between exception types:

Copy

\>>> class D:
...     def \_\_init\_\_(self, extra):
...         self.\_extra\_attributes \= extra
...     def \_\_getattr\_\_(self, attr):
...         try:
...             return self.\_extra\_attributes\[attr\]
...         except KeyError:
...             raise AttributeError(attr) from None
...
\>>> D({}).x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in \_\_getattr\_\_
AttributeError: x

Without the `from None` suffix to suppress the cause, the original exception would be displayed by default:

Copy

\>>> class C:
...     def \_\_init\_\_(self, extra):
...         self.\_extra\_attributes \= extra
...     def \_\_getattr\_\_(self, attr):
...         try:
...             return self.\_extra\_attributes\[attr\]
...         except KeyError:
...             raise AttributeError(attr)
...
\>>> C({}).x
Traceback (most recent call last):
  File "<stdin>", line 6, in \_\_getattr\_\_
KeyError: 'x'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in \_\_getattr\_\_
AttributeError: x

No debugging capability is lost, as the original exception context remains available if needed (for example, if an intervening library has incorrectly suppressed valuable underlying details):

Copy

\>>> try:
...     D({}).x
... except AttributeError as exc:
...     print(repr(exc.\_\_context\_\_))
...
KeyError('x',)

See also

[**PEP 409**](https://peps.python.org/pep-0409/)
 - Suppressing exception context

PEP written by Ethan Furman; implemented by Ethan Furman and Nick Coghlan.

PEP 414: Explicit Unicode literals[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-414-explicit-unicode-literals "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

To ease the transition from Python 2 for Unicode aware Python applications that make heavy use of Unicode literals, Python 3.3 once again supports the “`u`” prefix for string literals. This prefix has no semantic significance in Python 3, it is provided solely to reduce the number of purely mechanical changes in migrating to Python 3, making it easier for developers to focus on the more significant semantic changes (such as the stricter default separation of binary and text data).

See also

[**PEP 414**](https://peps.python.org/pep-0414/)
 - Explicit Unicode literals

PEP written by Armin Ronacher.

PEP 3155: Qualified name for classes and functions[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-3155-qualified-name-for-classes-and-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Functions and class objects have a new [`__qualname__`](https://docs.python.org/3/builtins/stdtypes.html#definition.__qualname__ "definition.__qualname__")
 attribute representing the “path” from the module top-level to their definition. For global functions and classes, this is the same as [`__name__`](https://docs.python.org/3/builtins/stdtypes.html#definition.__name__ "definition.__name__")
. For other functions and classes, it provides better information about where they were actually defined, and how they might be accessible from the global scope.

Example with (non-bound) methods:

Copy

\>>> class C:
...     def meth(self):
...         pass
...
\>>> C.meth.\_\_name\_\_
'meth'
\>>> C.meth.\_\_qualname\_\_
'C.meth'

Example with nested classes:

Copy

\>>> class C:
...     class D:
...         def meth(self):
...             pass
...
\>>> C.D.\_\_name\_\_
'D'
\>>> C.D.\_\_qualname\_\_
'C.D'
\>>> C.D.meth.\_\_name\_\_
'meth'
\>>> C.D.meth.\_\_qualname\_\_
'C.D.meth'

Example with nested functions:

Copy

\>>> def outer():
...     def inner():
...         pass
...     return inner
...
\>>> outer().\_\_name\_\_
'inner'
\>>> outer().\_\_qualname\_\_
'outer.<locals>.inner'

The string representation of those objects is also changed to include the new, more precise information:

Copy

\>>> str(C.D)
"<class '\_\_main\_\_.C.D'>"
\>>> str(C.D.meth)
'<function C.D.meth at 0x7f46b9fe31e0>'

See also

[**PEP 3155**](https://peps.python.org/pep-3155/)
 - Qualified name for classes and functions

PEP written and implemented by Antoine Pitrou.

PEP 412: Key-Sharing Dictionary[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-412-key-sharing-dictionary "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Dictionaries used for the storage of objects’ attributes are now able to share part of their internal storage between each other (namely, the part which stores the keys and their respective hashes). This reduces the memory consumption of programs creating many instances of non-builtin types.

See also

[**PEP 412**](https://peps.python.org/pep-0412/)
 - Key-Sharing Dictionary

PEP written and implemented by Mark Shannon.

PEP 362: Function Signature Object[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-362-function-signature-object "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

A new function [`inspect.signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature")
 makes introspection of python callables easy and straightforward. A broad range of callables is supported: python functions, decorated or not, classes, and [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial")
 objects. New classes [`inspect.Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature")
, [`inspect.Parameter`](https://docs.python.org/3/library/inspect.html#inspect.Parameter "inspect.Parameter")
 and [`inspect.BoundArguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments "inspect.BoundArguments")
 hold information about the call signatures, such as, annotations, default values, parameters kinds, and bound arguments, which considerably simplifies writing decorators and any code that validates or amends calling signatures or arguments.

See also

[**PEP 362**](https://peps.python.org/pep-0362/)
: - Function Signature Object

PEP written by Brett Cannon, Yury Selivanov, Larry Hastings, Jiwon Seo; implemented by Yury Selivanov.

PEP 421: Adding sys.implementation[¶](https://docs.python.org/3/whatsnew/3.3.html#pep-421-adding-sys-implementation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

A new attribute on the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
 module exposes details specific to the implementation of the currently running interpreter. The initial set of attributes on [`sys.implementation`](https://docs.python.org/3/library/sys.html#sys.implementation "sys.implementation")
 are `name`, `version`, `hexversion`, and `cache_tag`.

The intention of `sys.implementation` is to consolidate into one namespace the implementation-specific data used by the standard library. This allows different Python implementations to share a single standard library code base much more easily. In its initial state, `sys.implementation` holds only a small portion of the implementation-specific data. Over time that ratio will shift in order to make the standard library more portable.

One example of improved standard library portability is `cache_tag`. As of Python 3.3, `sys.implementation.cache_tag` is used by [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 to support [**PEP 3147**](https://peps.python.org/pep-3147/)
 compliance. Any Python implementation that uses `importlib` for its built-in import system may use `cache_tag` to control the caching behavior for modules.

### SimpleNamespace[¶](https://docs.python.org/3/whatsnew/3.3.html#simplenamespace "Link to this heading")

The implementation of `sys.implementation` also introduces a new type to Python: [`types.SimpleNamespace`](https://docs.python.org/3/library/types.html#types.SimpleNamespace "types.SimpleNamespace")
. In contrast to a mapping-based namespace, like [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
, `SimpleNamespace` is attribute-based, like [`object`](https://docs.python.org/3/builtins/functions.html#object "object")
. However, unlike `object`, `SimpleNamespace` instances are writable. This means that you can add, remove, and modify the namespace through normal attribute access.

See also

[**PEP 421**](https://peps.python.org/pep-0421/)
 - Adding sys.implementation

PEP written and implemented by Eric Snow.

Using importlib as the Implementation of Import[¶](https://docs.python.org/3/whatsnew/3.3.html#using-importlib-as-the-implementation-of-import "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

[bpo-2377](https://bugs.python.org/issue?@action=redirect&bpo=2377)
 - Replace \_\_import\_\_ w/ importlib.\_\_import\_\_ [bpo-13959](https://bugs.python.org/issue?@action=redirect&bpo=13959)
 - Re-implement parts of `imp` in pure Python [bpo-14605](https://bugs.python.org/issue?@action=redirect&bpo=14605)
 - Make import machinery explicit [bpo-14646](https://bugs.python.org/issue?@action=redirect&bpo=14646)
 - Require loaders set \_\_loader\_\_ and \_\_package\_\_

The [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
 function is now powered by [`importlib.__import__()`](https://docs.python.org/3/library/importlib.html#importlib.__import__ "importlib.__import__")
. This work leads to the completion of “phase 2” of [**PEP 302**](https://peps.python.org/pep-0302/)
. There are multiple benefits to this change. First, it has allowed for more of the machinery powering import to be exposed instead of being implicit and hidden within the C code. It also provides a single implementation for all Python VMs supporting Python 3.3 to use, helping to end any VM-specific deviations in import semantics. And finally it eases the maintenance of import, allowing for future growth to occur.

For the common user, there should be no visible change in semantics. For those whose code currently manipulates import or calls import programmatically, the code changes that might possibly be required are covered in the [Porting Python code](https://docs.python.org/3/whatsnew/3.3.html#porting-python-code)
 section of this document.

### New APIs[¶](https://docs.python.org/3/whatsnew/3.3.html#new-apis "Link to this heading")

One of the large benefits of this work is the exposure of what goes into making the import statement work. That means the various importers that were once implicit are now fully exposed as part of the [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 package.

The abstract base classes defined in [`importlib.abc`](https://docs.python.org/3/library/importlib.html#module-importlib.abc "importlib.abc: Abstract base classes related to import")
 have been expanded to properly delineate between [meta path finders](https://docs.python.org/3/glossary.html#term-meta-path-finder)
 and [path entry finders](https://docs.python.org/3/glossary.html#term-path-entry-finder)
 by introducing [`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder")
 and [`importlib.abc.PathEntryFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder "importlib.abc.PathEntryFinder")
, respectively. The old ABC of `importlib.abc.Finder` is now only provided for backwards-compatibility and does not enforce any method requirements.

In terms of finders, [`importlib.machinery.FileFinder`](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder "importlib.machinery.FileFinder")
 exposes the mechanism used to search for source and bytecode files of a module. Previously this class was an implicit member of [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks")
.

For loaders, the new abstract base class [`importlib.abc.FileLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader "importlib.abc.FileLoader")
 helps write a loader that uses the file system as the storage mechanism for a module’s code. The loader for source files ([`importlib.machinery.SourceFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader "importlib.machinery.SourceFileLoader")
), sourceless bytecode files ([`importlib.machinery.SourcelessFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader "importlib.machinery.SourcelessFileLoader")
), and extension modules ([`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader "importlib.machinery.ExtensionFileLoader")
) are now available for direct use.

[`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
 now has `name` and `path` attributes which are set when there is relevant data to provide. The message for failed imports will also provide the full name of the module now instead of just the tail end of the module’s name.

The [`importlib.invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches "importlib.invalidate_caches")
 function will now call the method with the same name on all finders cached in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache")
 to help clean up any stored state as necessary.

### Visible Changes[¶](https://docs.python.org/3/whatsnew/3.3.html#visible-changes "Link to this heading")

For potential required changes to code, see the [Porting Python code](https://docs.python.org/3/whatsnew/3.3.html#porting-python-code)
 section.

Beyond the expanse of what [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 now exposes, there are other visible changes to import. The biggest is that [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path")
 and [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks")
 now store all of the meta path finders and path entry hooks used by import. Previously the finders were implicit and hidden within the C code of import instead of being directly exposed. This means that one can now easily remove or change the order of the various finders to fit one’s needs.

Another change is that all modules have a `__loader__` attribute, storing the loader used to create the module. [**PEP 302**](https://peps.python.org/pep-0302/)
 has been updated to make this attribute mandatory for loaders to implement, so in the future once 3rd-party loaders have been updated people will be able to rely on the existence of the attribute. Until such time, though, import is setting the module post-load.

Loaders are also now expected to set the `__package__` attribute from [**PEP 366**](https://peps.python.org/pep-0366/)
. Once again, import itself is already setting this on all loaders from [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
 and import itself is setting the attribute post-load.

`None` is now inserted into [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache")
 when no finder can be found on [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks")
. Since `imp.NullImporter` is not directly exposed on `sys.path_hooks` it could no longer be relied upon to always be available to use as a value representing no finder found.

All other changes relate to semantic changes which should be taken into consideration when updating code for Python 3.3, and thus should be read about in the [Porting Python code](https://docs.python.org/3/whatsnew/3.3.html#porting-python-code)
 section of this document.

(Implementation by Brett Cannon)

Other Language Changes[¶](https://docs.python.org/3/whatsnew/3.3.html#other-language-changes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

Some smaller changes made to the core Python language are:

*   Added support for Unicode name aliases and named sequences. Both [`unicodedata.lookup()`](https://docs.python.org/3/library/unicodedata.html#unicodedata.lookup "unicodedata.lookup")
     and `'\N{...}'` now resolve name aliases, and `unicodedata.lookup()` resolves named sequences too.
    
    (Contributed by Ezio Melotti in [bpo-12753](https://bugs.python.org/issue?@action=redirect&bpo=12753)
    .)
    
*   Unicode database updated to UCD version 6.1.0
    
*   Equality comparisons on [`range()`](https://docs.python.org/3/builtins/stdtypes.html#range "range")
     objects now return a result reflecting the equality of the underlying sequences generated by those range objects. ([bpo-13201](https://bugs.python.org/issue?@action=redirect&bpo=13201)
    )
    
*   The `count()`, `find()`, `rfind()`, `index()` and `rindex()` methods of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
     objects now accept an integer between 0 and 255 as their first argument.
    
    (Contributed by Petri Lehtinen in [bpo-12170](https://bugs.python.org/issue?@action=redirect&bpo=12170)
    .)
    
*   The `rjust()`, `ljust()`, and `center()` methods of [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
     and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
     now accept a `bytearray` for the `fill` argument. (Contributed by Petri Lehtinen in [bpo-12380](https://bugs.python.org/issue?@action=redirect&bpo=12380)
    .)
    
*   New methods have been added to [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
     and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
    : `copy()` and `clear()` ([bpo-10516](https://bugs.python.org/issue?@action=redirect&bpo=10516)
    ). Consequently, [`MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence")
     now also defines a `clear()` method ([bpo-11388](https://bugs.python.org/issue?@action=redirect&bpo=11388)
    ).
    
*   Raw bytes literals can now be written `rb"..."` as well as `br"..."`.
    
    (Contributed by Antoine Pitrou in [bpo-13748](https://bugs.python.org/issue?@action=redirect&bpo=13748)
    .)
    
*   [`dict.setdefault()`](https://docs.python.org/3/builtins/stdtypes.html#dict.setdefault "dict.setdefault")
     now does only one lookup for the given key, making it atomic when used with built-in types.
    
    (Contributed by Filip Gruszczyński in [bpo-13521](https://bugs.python.org/issue?@action=redirect&bpo=13521)
    .)
    
*   The error messages produced when a function call does not match the function signature have been significantly improved.
    
    (Contributed by Benjamin Peterson.)
    

A Finer-Grained Import Lock[¶](https://docs.python.org/3/whatsnew/3.3.html#a-finer-grained-import-lock "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

Previous versions of CPython have always relied on a global import lock. This led to unexpected annoyances, such as deadlocks when importing a module would trigger code execution in a different thread as a side-effect. Clumsy workarounds were sometimes employed, such as the `PyImport_ImportModuleNoBlock()` C API function.

In Python 3.3, importing a module takes a per-module lock. This correctly serializes importation of a given module from multiple threads (preventing the exposure of incompletely initialized modules), while eliminating the aforementioned annoyances.

(Contributed by Antoine Pitrou in [bpo-9260](https://bugs.python.org/issue?@action=redirect&bpo=9260)
.)

Builtin functions and types[¶](https://docs.python.org/3/whatsnew/3.3.html#builtin-functions-and-types "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

*   [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
     gets a new _opener_ parameter: the underlying file descriptor for the file object is then obtained by calling _opener_ with (_file_, _flags_). It can be used to use custom flags like [`os.O_CLOEXEC`](https://docs.python.org/3/library/os.html#os.O_CLOEXEC "os.O_CLOEXEC")
     for example. The `'x'` mode was added: open for exclusive creation, failing if the file already exists.
    
*   [`print()`](https://docs.python.org/3/builtins/functions.html#print "print")
    : added the _flush_ keyword argument. If the _flush_ keyword argument is true, the stream is forcibly flushed.
    
*   [`hash()`](https://docs.python.org/3/builtins/functions.html#hash "hash")
    : hash randomization is enabled by default, see [`object.__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
     and [`PYTHONHASHSEED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED)
    .
    
*   The [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     type gets a new [`casefold()`](https://docs.python.org/3/builtins/stdtypes.html#str.casefold "str.casefold")
     method: return a casefolded copy of the string, casefolded strings may be used for caseless matching. For example, `'ß'.casefold()` returns `'ss'`.
    
*   The sequence documentation has been substantially rewritten to better explain the binary/text sequence distinction and to provide specific documentation sections for the individual builtin sequence types ([bpo-4966](https://bugs.python.org/issue?@action=redirect&bpo=4966)
    ).
    

New Modules[¶](https://docs.python.org/3/whatsnew/3.3.html#new-modules "Link to this heading")

-----------------------------------------------------------------------------------------------

### faulthandler[¶](https://docs.python.org/3/whatsnew/3.3.html#faulthandler "Link to this heading")

This new debug module [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.")
 contains functions to dump Python tracebacks explicitly, on a fault (a crash like a segmentation fault), after a timeout, or on a user signal. Call [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable")
 to install fault handlers for the [`SIGSEGV`](https://docs.python.org/3/library/signal.html#signal.SIGSEGV "signal.SIGSEGV")
, [`SIGFPE`](https://docs.python.org/3/library/signal.html#signal.SIGFPE "signal.SIGFPE")
, [`SIGABRT`](https://docs.python.org/3/library/signal.html#signal.SIGABRT "signal.SIGABRT")
, [`SIGBUS`](https://docs.python.org/3/library/signal.html#signal.SIGBUS "signal.SIGBUS")
, and [`SIGILL`](https://docs.python.org/3/library/signal.html#signal.SIGILL "signal.SIGILL")
 signals. You can also enable them at startup by setting the [`PYTHONFAULTHANDLER`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER)
 environment variable or by using [`-X`](https://docs.python.org/3/using/cmdline.html#cmdoption-X)
 `faulthandler` command line option.

Example of a segmentation fault on Linux:

Copy

$ python \-q \-X faulthandler
\>>> import ctypes
\>>> ctypes.string\_at(0)
Fatal Python error: Segmentation fault

Current thread 0x00007fb899f39700:
  File "/home/python/cpython/Lib/ctypes/\_\_init\_\_.py", line 486 in string\_at
  File "<stdin>", line 1 in <module>
Segmentation fault

### ipaddress[¶](https://docs.python.org/3/whatsnew/3.3.html#ipaddress "Link to this heading")

The new [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.")
 module provides tools for creating and manipulating objects representing IPv4 and IPv6 addresses, networks and interfaces (i.e. an IP address associated with a specific IP subnet).

(Contributed by Google and Peter Moody in [**PEP 3144**](https://peps.python.org/pep-3144/)
.)

### lzma[¶](https://docs.python.org/3/whatsnew/3.3.html#lzma "Link to this heading")

The newly added [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
 module provides data compression and decompression using the LZMA algorithm, including support for the `.xz` and `.lzma` file formats.

(Contributed by Nadeem Vawda and Per Øyvind Karlsen in [bpo-6715](https://bugs.python.org/issue?@action=redirect&bpo=6715)
.)

Improved Modules[¶](https://docs.python.org/3/whatsnew/3.3.html#improved-modules "Link to this heading")

---------------------------------------------------------------------------------------------------------

### abc[¶](https://docs.python.org/3/whatsnew/3.3.html#abc "Link to this heading")

Improved support for abstract base classes containing descriptors composed with abstract methods. The recommended approach to declaring abstract descriptors is now to provide `__isabstractmethod__` as a dynamically updated property. The built-in descriptors have been updated accordingly.

*   [`@abc.abstractproperty`](https://docs.python.org/3/library/abc.html#abc.abstractproperty "abc.abstractproperty")
     has been deprecated, use [`@property`](https://docs.python.org/3/builtins/functions.html#property "property")
     with [`@abc.abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
     instead.
    
*   [`@abc.abstractclassmethod`](https://docs.python.org/3/library/abc.html#abc.abstractclassmethod "abc.abstractclassmethod")
     has been deprecated, use [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
     with [`@abc.abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
     instead.
    
*   [`@abc.abstractstaticmethod`](https://docs.python.org/3/library/abc.html#abc.abstractstaticmethod "abc.abstractstaticmethod")
     has been deprecated, use [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
     with [`@abc.abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
     instead.
    

(Contributed by Darren Dale in [bpo-11610](https://bugs.python.org/issue?@action=redirect&bpo=11610)
.)

[`abc.ABCMeta.register()`](https://docs.python.org/3/library/abc.html#abc.ABCMeta.register "abc.ABCMeta.register")
 now returns the registered subclass, which means it can now be used as a class decorator ([bpo-10868](https://bugs.python.org/issue?@action=redirect&bpo=10868)
).

### array[¶](https://docs.python.org/3/whatsnew/3.3.html#array "Link to this heading")

The [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.")
 module supports the long long type using `q` and `Q` type codes.

(Contributed by Oren Tirosh and Hirokazu Yamamoto in [bpo-1172711](https://bugs.python.org/issue?@action=redirect&bpo=1172711)
.)

### base64[¶](https://docs.python.org/3/whatsnew/3.3.html#base64 "Link to this heading")

ASCII-only Unicode strings are now accepted by the decoding functions of the [`base64`](https://docs.python.org/3/library/base64.html#module-base64 "base64: RFC 4648: Base16, Base32, Base64 Data Encodings; Base85 and Ascii85")
 modern interface. For example, `base64.b64decode('YWJj')` returns `b'abc'`. (Contributed by Catalin Iacob in [bpo-13641](https://bugs.python.org/issue?@action=redirect&bpo=13641)
.)

### binascii[¶](https://docs.python.org/3/whatsnew/3.3.html#binascii "Link to this heading")

In addition to the binary objects they normally accept, the `a2b_` functions now all also accept ASCII-only strings as input. (Contributed by Antoine Pitrou in [bpo-13637](https://bugs.python.org/issue?@action=redirect&bpo=13637)
.)

### bz2[¶](https://docs.python.org/3/whatsnew/3.3.html#bz2 "Link to this heading")

The [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
 module has been rewritten from scratch. In the process, several new features have been added:

*   New [`bz2.open()`](https://docs.python.org/3/library/bz2.html#bz2.open "bz2.open")
     function: open a bzip2-compressed file in binary or text mode.
    
*   [`bz2.BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File")
     can now read from and write to arbitrary file-like objects, by means of its constructor’s _fileobj_ argument.
    
    (Contributed by Nadeem Vawda in [bpo-5863](https://bugs.python.org/issue?@action=redirect&bpo=5863)
    .)
    
*   [`bz2.BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File")
     and [`bz2.decompress()`](https://docs.python.org/3/library/bz2.html#bz2.decompress "bz2.decompress")
     can now decompress multi-stream inputs (such as those produced by the **pbzip2** tool). `bz2.BZ2File` can now also be used to create this type of file, using the `'a'` (append) mode.
    
    (Contributed by Nir Aides in [bpo-1625](https://bugs.python.org/issue?@action=redirect&bpo=1625)
    .)
    
*   [`bz2.BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File")
     now implements all of the [`io.BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")
     API, except for the `detach()` and `truncate()` methods.
    

### codecs[¶](https://docs.python.org/3/whatsnew/3.3.html#codecs "Link to this heading")

The [`mbcs`](https://docs.python.org/3/library/codecs.html#module-encodings.mbcs "encodings.mbcs: Windows ANSI codepage")
 codec has been rewritten to handle correctly `replace` and `ignore` error handlers on all Windows versions. The `mbcs` codec now supports all error handlers, instead of only `replace` to encode and `ignore` to decode.

A new Windows-only codec has been added: `cp65001` ([bpo-13216](https://bugs.python.org/issue?@action=redirect&bpo=13216)
). It is the Windows code page 65001 (Windows UTF-8, `CP_UTF8`). For example, it is used by `sys.stdout` if the console output code page is set to cp65001 (e.g., using `chcp 65001` command).

Multibyte CJK decoders now resynchronize faster. They only ignore the first byte of an invalid byte sequence. For example, `b'\xff\n'.decode('gb2312', 'replace')` now returns a `\n` after the replacement character.

([bpo-12016](https://bugs.python.org/issue?@action=redirect&bpo=12016)
)

Incremental CJK codec encoders are no longer reset at each call to their encode() methods. For example:

Copy

\>>> import codecs
\>>> encoder \= codecs.getincrementalencoder('hz')('strict')
\>>> b''.join(encoder.encode(x) for x in '\\u52ff\\u65bd\\u65bc\\u4eba\\u3002 Bye.')
b'~{NpJ)l6HK!#~} Bye.'

This example gives `b'~{Np~}~{J)~}~{l6~}~{HK~}~{!#~} Bye.'` with older Python versions.

([bpo-12100](https://bugs.python.org/issue?@action=redirect&bpo=12100)
)

The `unicode_internal` codec has been deprecated.

### collections[¶](https://docs.python.org/3/whatsnew/3.3.html#collections "Link to this heading")

Addition of a new [`ChainMap`](https://docs.python.org/3/library/collections.html#collections.ChainMap "collections.ChainMap")
 class to allow treating a number of mappings as a single unit. (Written by Raymond Hettinger for [bpo-11089](https://bugs.python.org/issue?@action=redirect&bpo=11089)
, made public in [bpo-11297](https://bugs.python.org/issue?@action=redirect&bpo=11297)
.)

The abstract base classes have been moved in a new [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "collections.abc: Abstract base classes for containers")
 module, to better differentiate between the abstract and the concrete collections classes. Aliases for ABCs are still present in the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes")
 module to preserve existing imports. ([bpo-11085](https://bugs.python.org/issue?@action=redirect&bpo=11085)
)

The [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter")
 class now supports the unary `+` and `-` operators, as well as the in-place operators `+=`, `-=`, `|=`, and `&=`. (Contributed by Raymond Hettinger in [bpo-13121](https://bugs.python.org/issue?@action=redirect&bpo=13121)
.)

### contextlib[¶](https://docs.python.org/3/whatsnew/3.3.html#contextlib "Link to this heading")

[`ExitStack`](https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack "contextlib.ExitStack")
 now provides a solid foundation for programmatic manipulation of context managers and similar cleanup functionality. Unlike the previous `contextlib.nested` API (which was deprecated and removed), the new API is designed to work correctly regardless of whether context managers acquire their resources in their `__init__` method (for example, file objects) or in their `__enter__` method (for example, synchronisation objects from the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
 module).

([bpo-13585](https://bugs.python.org/issue?@action=redirect&bpo=13585)
)

### crypt[¶](https://docs.python.org/3/whatsnew/3.3.html#crypt "Link to this heading")

Addition of salt and modular crypt format (hashing method) and the `mksalt()` function to the `crypt` module.

([bpo-10924](https://bugs.python.org/issue?@action=redirect&bpo=10924)
)

### curses[¶](https://docs.python.org/3/whatsnew/3.3.html#curses "Link to this heading")

*   If the [`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling.")
     module is linked to the ncursesw library, use Unicode functions when Unicode strings or characters are passed (e.g. `waddwstr()`), and bytes functions otherwise (e.g. `waddstr()`).
    
*   Use the locale encoding instead of `utf-8` to encode Unicode strings.
    
*   [`curses.window`](https://docs.python.org/3/library/curses.html#curses.window "curses.window")
     has a new [`curses.window.encoding`](https://docs.python.org/3/library/curses.html#curses.window.encoding "curses.window.encoding")
     attribute.
    
*   The [`curses.window`](https://docs.python.org/3/library/curses.html#curses.window "curses.window")
     class has a new [`get_wch()`](https://docs.python.org/3/library/curses.html#curses.window.get_wch "curses.window.get_wch")
     method to get a wide character
    
*   The [`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling.")
     module has a new [`unget_wch()`](https://docs.python.org/3/library/curses.html#curses.unget_wch "curses.unget_wch")
     function to push a wide character so the next [`get_wch()`](https://docs.python.org/3/library/curses.html#curses.window.get_wch "curses.window.get_wch")
     will return it
    

(Contributed by Iñigo Serna in [bpo-6755](https://bugs.python.org/issue?@action=redirect&bpo=6755)
.)

### datetime[¶](https://docs.python.org/3/whatsnew/3.3.html#datetime "Link to this heading")

*   Equality comparisons between naive and aware [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
     instances now return [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
     instead of raising [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     ([bpo-15006](https://bugs.python.org/issue?@action=redirect&bpo=15006)
    ).
    
*   New [`datetime.datetime.timestamp()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp "datetime.datetime.timestamp")
     method: Return POSIX timestamp corresponding to the [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
     instance.
    
*   The [`datetime.datetime.strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime")
     method supports formatting years older than 1000.
    
*   The [`datetime.datetime.astimezone()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone "datetime.datetime.astimezone")
     method can now be called without arguments to convert datetime instance to the system timezone.
    

### decimal[¶](https://docs.python.org/3/whatsnew/3.3.html#decimal "Link to this heading")

[bpo-7652](https://bugs.python.org/issue?@action=redirect&bpo=7652)
 - integrate fast native decimal arithmetic.

C-module and libmpdec written by Stefan Krah.

The new C version of the decimal module integrates the high speed libmpdec library for arbitrary precision correctly rounded decimal floating-point arithmetic. libmpdec conforms to IBM’s General Decimal Arithmetic Specification.

Performance gains range from 10x for database applications to 100x for numerically intensive applications. These numbers are expected gains for standard precisions used in decimal floating-point arithmetic. Since the precision is user configurable, the exact figures may vary. For example, in integer bignum arithmetic the differences can be significantly higher.

The following table is meant as an illustration. Benchmarks are available at [https://www.bytereef.org/mpdecimal/quickstart.html](https://www.bytereef.org/mpdecimal/quickstart.html)
.

> |     | decimal.py | \_decimal | speedup |
> | --- | --- | --- | --- |
> | pi  | 42.02s | 0.345s | 120x |
> | telco | 172.19s | 5.68s | 30x |
> | psycopg | 3.57s | 0.29s | 12x |

#### Features[¶](https://docs.python.org/3/whatsnew/3.3.html#id1 "Link to this heading")

*   The [`FloatOperation`](https://docs.python.org/3/library/decimal.html#decimal.FloatOperation "decimal.FloatOperation")
     signal optionally enables stricter semantics for mixing floats and Decimals.
    
*   If Python is compiled without threads, the C version automatically disables the expensive thread local context machinery. In this case, the variable [`HAVE_THREADS`](https://docs.python.org/3/library/decimal.html#decimal.HAVE_THREADS "decimal.HAVE_THREADS")
     is set to `False`.
    

#### API changes[¶](https://docs.python.org/3/whatsnew/3.3.html#id2 "Link to this heading")

*   The C module has the following context limits, depending on the machine architecture:
    
    > |     | 32-bit | 64-bit |
    > | --- | --- | --- |
    > | [`MAX_PREC`](https://docs.python.org/3/library/decimal.html#decimal.MAX_PREC "decimal.MAX_PREC") | `425000000` | `999999999999999999` |
    > | [`MAX_EMAX`](https://docs.python.org/3/library/decimal.html#decimal.MAX_EMAX "decimal.MAX_EMAX") | `425000000` | `999999999999999999` |
    > | [`MIN_EMIN`](https://docs.python.org/3/library/decimal.html#decimal.MIN_EMIN "decimal.MIN_EMIN") | `-425000000` | `-999999999999999999` |
    
*   In the context templates ([`DefaultContext`](https://docs.python.org/3/library/decimal.html#decimal.DefaultContext "decimal.DefaultContext")
    , [`BasicContext`](https://docs.python.org/3/library/decimal.html#decimal.BasicContext "decimal.BasicContext")
     and [`ExtendedContext`](https://docs.python.org/3/library/decimal.html#decimal.ExtendedContext "decimal.ExtendedContext")
    ) the magnitude of [`Emax`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emax "decimal.Context.Emax")
     and [`Emin`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emin "decimal.Context.Emin")
     has changed to `999999`.
    
*   The [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
     constructor in decimal.py does not observe the context limits and converts values with arbitrary exponents or precision exactly. Since the C version has internal limits, the following scheme is used: If possible, values are converted exactly, otherwise [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation")
     is raised and the result is NaN. In the latter case it is always possible to use [`create_decimal()`](https://docs.python.org/3/library/decimal.html#decimal.Context.create_decimal "decimal.Context.create_decimal")
     in order to obtain a rounded or inexact value.
    
*   The power function in decimal.py is always correctly rounded. In the C version, it is defined in terms of the correctly rounded [`exp()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp "decimal.Decimal.exp")
     and [`ln()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.ln "decimal.Decimal.ln")
     functions, but the final result is only “almost always correctly rounded”.
    
*   In the C version, the context dictionary containing the signals is a [`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping")
    . For speed reasons, [`flags`](https://docs.python.org/3/library/decimal.html#decimal.Context.flags "decimal.Context.flags")
     and [`traps`](https://docs.python.org/3/library/decimal.html#decimal.Context.traps "decimal.Context.traps")
     always refer to the same `MutableMapping` that the context was initialized with. If a new signal dictionary is assigned, `flags` and `traps` are updated with the new values, but they do not reference the RHS dictionary.
    
*   Pickling a [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context")
     produces a different output in order to have a common interchange format for the Python and C versions.
    
*   The order of arguments in the [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context")
     constructor has been changed to match the order displayed by [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
    .
    
*   The `watchexp` parameter in the [`quantize()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.quantize "decimal.Decimal.quantize")
     method is deprecated.
    

### email[¶](https://docs.python.org/3/whatsnew/3.3.html#email "Link to this heading")

#### Policy Framework[¶](https://docs.python.org/3/whatsnew/3.3.html#policy-framework "Link to this heading")

The email package now has a [`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages")
 framework. A [`Policy`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy "email.policy.Policy")
 is an object with several methods and properties that control how the email package behaves. The primary policy for Python 3.3 is the [`Compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32")
 policy, which provides backward compatibility with the email package in Python 3.2. A `policy` can be specified when an email message is parsed by a [`parser`](https://docs.python.org/3/library/email.parser.html#module-email.parser "email.parser: Parse flat text email messages to produce a message object structure.")
, or when a [`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message")
 object is created, or when an email is serialized using a [`generator`](https://docs.python.org/3/library/email.generator.html#module-email.generator "email.generator: Generate flat text email messages from a message structure.")
. Unless overridden, a policy passed to a `parser` is inherited by all the `Message` object and sub-objects created by the `parser`. By default a `generator` will use the policy of the `Message` object it is serializing. The default policy is [`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.compat32 "email.policy.compat32")
.

The minimum set of controls implemented by all `policy` objects are:

|     |     |
| --- | --- |
| max\_line\_length | The maximum length, excluding the linesep character(s), individual lines may have when a `Message` is serialized. Defaults to 78. |
| linesep | The character used to separate individual lines when a `Message` is serialized. Defaults to `\n`. |
| cte\_type | `7bit` or `8bit`. `8bit` applies only to a `Bytes` `generator`, and means that non-ASCII may be used where allowed by the protocol (or where it exists in the original input). |
| raise\_on\_defect | Causes a `parser` to raise error when defects are encountered instead of adding them to the `Message` object’s `defects` list. |

A new policy instance, with new settings, is created using the [`clone()`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.clone "email.policy.Policy.clone")
 method of policy objects. `clone` takes any of the above controls as keyword arguments. Any control not specified in the call retains its default value. Thus you can create a policy that uses `\r\n` linesep characters like this:

Copy

mypolicy \= compat32.clone(linesep\='\\r\\n')

Policies can be used to make the generation of messages in the format needed by your application simpler. Instead of having to remember to specify `linesep='\r\n'` in all the places you call a `generator`, you can specify it once, when you set the policy used by the `parser` or the `Message`, whichever your program uses to create `Message` objects. On the other hand, if you need to generate messages in multiple forms, you can still specify the parameters in the appropriate `generator` call. Or you can have custom policy instances for your different cases, and pass those in when you create the `generator`.

#### Provisional Policy with New Header API[¶](https://docs.python.org/3/whatsnew/3.3.html#provisional-policy-with-new-header-api "Link to this heading")

While the policy framework is worthwhile all by itself, the main motivation for introducing it is to allow the creation of new policies that implement new features for the email package in a way that maintains backward compatibility for those who do not use the new policies. Because the new policies introduce a new API, we are releasing them in Python 3.3 as a [provisional policy](https://docs.python.org/3/glossary.html#term-provisional-package)
. Backwards incompatible changes (up to and including removal of the code) may occur if deemed necessary by the core developers.

The new policies are instances of [`EmailPolicy`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy "email.policy.EmailPolicy")
, and add the following additional controls:

|     |     |
| --- | --- |
| refold\_source | Controls whether or not headers parsed by a [`parser`](https://docs.python.org/3/library/email.parser.html#module-email.parser "email.parser: Parse flat text email messages to produce a message object structure.")<br> are refolded by the [`generator`](https://docs.python.org/3/library/email.generator.html#module-email.generator "email.generator: Generate flat text email messages from a message structure.")<br>. It can be `none`, `long`, or `all`. The default is `long`, which means that source headers with a line longer than `max_line_length` get refolded. `none` means no line get refolded, and `all` means that all lines get refolded. |
| header\_factory | A callable that take a `name` and `value` and produces a custom header object. |

The `header_factory` is the key to the new features provided by the new policies. When one of the new policies is used, any header retrieved from a `Message` object is an object produced by the `header_factory`, and any time you set a header on a `Message` it becomes an object produced by `header_factory`. All such header objects have a `name` attribute equal to the header name. Address and Date headers have additional attributes that give you access to the parsed data of the header. This means you can now do things like this:

Copy

\>>> m \= Message(policy\=SMTP)
\>>> m\['To'\] \= 'Éric <foo@example.com>'
\>>> m\['to'\]
'Éric <foo@example.com>'
\>>> m\['to'\].addresses
(Address(display\_name='Éric', username='foo', domain='example.com'),)
\>>> m\['to'\].addresses\[0\].username
'foo'
\>>> m\['to'\].addresses\[0\].display\_name
'Éric'
\>>> m\['Date'\] \= email.utils.localtime()
\>>> m\['Date'\].datetime
datetime.datetime(2012, 5, 25, 21, 39, 24, 465484, tzinfo=datetime.timezone(datetime.timedelta(-1, 72000), 'EDT'))
\>>> m\['Date'\]
'Fri, 25 May 2012 21:44:27 -0400'
\>>> print(m)
To: =?utf-8?q?=C3=89ric?= <foo@example.com>
Date: Fri, 25 May 2012 21:44:27 -0400

You will note that the unicode display name is automatically encoded as `utf-8` when the message is serialized, but that when the header is accessed directly, you get the unicode version. This eliminates any need to deal with the [`email.header`](https://docs.python.org/3/library/email.header.html#module-email.header "email.header: Representing non-ASCII headers")
 [`decode_header()`](https://docs.python.org/3/library/email.header.html#email.header.decode_header "email.header.decode_header")
 or [`make_header()`](https://docs.python.org/3/library/email.header.html#email.header.make_header "email.header.make_header")
 functions.

You can also create addresses from parts:

Copy

\>>> m\['cc'\] \= \[Group('pals', \[Address('Bob', 'bob', 'example.com'),\
...                           Address('Sally', 'sally', 'example.com')\]),\
...            Address('Bonzo', addr\_spec\='bonz@laugh.com')\]
\>>> print(m)
To: =?utf-8?q?=C3=89ric?= <foo@example.com>
Date: Fri, 25 May 2012 21:44:27 -0400
cc: pals: Bob <bob@example.com>, Sally <sally@example.com>;, Bonzo <bonz@laugh.com>

Decoding to unicode is done automatically:

Copy

\>>> m2 \= message\_from\_string(str(m))
\>>> m2\['to'\]
'Éric <foo@example.com>'

When you parse a message, you can use the `addresses` and `groups` attributes of the header objects to access the groups and individual addresses:

Copy

\>>> m2\['cc'\].addresses
(Address(display\_name='Bob', username='bob', domain='example.com'), Address(display\_name='Sally', username='sally', domain='example.com'), Address(display\_name='Bonzo', username='bonz', domain='laugh.com'))
\>>> m2\['cc'\].groups
(Group(display\_name='pals', addresses=(Address(display\_name='Bob', username='bob', domain='example.com'), Address(display\_name='Sally', username='sally', domain='example.com')), Group(display\_name=None, addresses=(Address(display\_name='Bonzo', username='bonz', domain='laugh.com'),))

In summary, if you use one of the new policies, header manipulation works the way it ought to: your application works with unicode strings, and the email package transparently encodes and decodes the unicode to and from the RFC standard Content Transfer Encodings.

#### Other API Changes[¶](https://docs.python.org/3/whatsnew/3.3.html#other-api-changes "Link to this heading")

New [`BytesHeaderParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesHeaderParser "email.parser.BytesHeaderParser")
, added to the [`parser`](https://docs.python.org/3/library/email.parser.html#module-email.parser "email.parser: Parse flat text email messages to produce a message object structure.")
 module to complement [`HeaderParser`](https://docs.python.org/3/library/email.parser.html#email.parser.HeaderParser "email.parser.HeaderParser")
 and complete the Bytes API.

New utility functions:

*   [`format_datetime()`](https://docs.python.org/3/library/email.utils.html#email.utils.format_datetime "email.utils.format_datetime")
    : given a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
    , produce a string formatted for use in an email header.
    
*   [`parsedate_to_datetime()`](https://docs.python.org/3/library/email.utils.html#email.utils.parsedate_to_datetime "email.utils.parsedate_to_datetime")
    : given a date string from an email header, convert it into an aware [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
    , or a naive `datetime` if the offset is `-0000`.
    
*   [`localtime()`](https://docs.python.org/3/library/email.utils.html#email.utils.localtime "email.utils.localtime")
    : With no argument, returns the current local time as an aware [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
     using the local [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone")
    . Given an aware `datetime`, converts it into an aware `datetime` using the local `timezone`.
    

### ftplib[¶](https://docs.python.org/3/whatsnew/3.3.html#ftplib "Link to this heading")

*   [`ftplib.FTP`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "ftplib.FTP")
     now accepts a `source_address` keyword argument to specify the `(host, port)` to use as the source address in the bind call when creating the outgoing socket. (Contributed by Giampaolo Rodolà in [bpo-8594](https://bugs.python.org/issue?@action=redirect&bpo=8594)
    .)
    
*   The [`FTP_TLS`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS "ftplib.FTP_TLS")
     class now provides a new [`ccc()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS.ccc "ftplib.FTP_TLS.ccc")
     function to revert control channel back to plaintext. This can be useful to take advantage of firewalls that know how to handle NAT with non-secure FTP without opening fixed ports. (Contributed by Giampaolo Rodolà in [bpo-12139](https://bugs.python.org/issue?@action=redirect&bpo=12139)
    .)
    
*   Added [`ftplib.FTP.mlsd()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.mlsd "ftplib.FTP.mlsd")
     method which provides a parsable directory listing format and deprecates [`ftplib.FTP.nlst()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.nlst "ftplib.FTP.nlst")
     and [`ftplib.FTP.dir()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.dir "ftplib.FTP.dir")
    . (Contributed by Giampaolo Rodolà in [bpo-11072](https://bugs.python.org/issue?@action=redirect&bpo=11072)
    .)
    

### functools[¶](https://docs.python.org/3/whatsnew/3.3.html#functools "Link to this heading")

The [`@functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache "functools.lru_cache")
 decorator now accepts a `typed` keyword argument (that defaults to `False` to ensure that it caches values of different types that compare equal in separate cache slots. (Contributed by Raymond Hettinger in [bpo-13227](https://bugs.python.org/issue?@action=redirect&bpo=13227)
.)

### gc[¶](https://docs.python.org/3/whatsnew/3.3.html#gc "Link to this heading")

It is now possible to register callbacks invoked by the garbage collector before and after collection using the new [`callbacks`](https://docs.python.org/3/library/gc.html#gc.callbacks "gc.callbacks")
 list.

### hmac[¶](https://docs.python.org/3/whatsnew/3.3.html#hmac "Link to this heading")

A new [`compare_digest()`](https://docs.python.org/3/library/hmac.html#hmac.compare_digest "hmac.compare_digest")
 function has been added to prevent side channel attacks on digests through timing analysis. (Contributed by Nick Coghlan and Christian Heimes in [bpo-15061](https://bugs.python.org/issue?@action=redirect&bpo=15061)
.)

### http[¶](https://docs.python.org/3/whatsnew/3.3.html#http "Link to this heading")

[`http.server.BaseHTTPRequestHandler`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler "http.server.BaseHTTPRequestHandler")
 now buffers the headers and writes them all at once when [`end_headers()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.end_headers "http.server.BaseHTTPRequestHandler.end_headers")
 is called. A new method [`flush_headers()`](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.flush_headers "http.server.BaseHTTPRequestHandler.flush_headers")
 can be used to directly manage when the accumulated headers are sent. (Contributed by Andrew Schaaf in [bpo-3709](https://bugs.python.org/issue?@action=redirect&bpo=3709)
.)

[`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
 now produces valid `HTML 4.01 strict` output. (Contributed by Ezio Melotti in [bpo-13295](https://bugs.python.org/issue?@action=redirect&bpo=13295)
.)

[`http.client.HTTPResponse`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse "http.client.HTTPResponse")
 now has a [`readinto()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPResponse.readinto "http.client.HTTPResponse.readinto")
 method, which means it can be used as an [`io.RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase")
 class. (Contributed by John Kuhn in [bpo-13464](https://bugs.python.org/issue?@action=redirect&bpo=13464)
.)

### html[¶](https://docs.python.org/3/whatsnew/3.3.html#html "Link to this heading")

[`html.parser.HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser")
 is now able to parse broken markup without raising errors, therefore the _strict_ argument of the constructor and the `HTMLParseError` exception are now deprecated. The ability to parse broken markup is the result of a number of bug fixes that are also available on the latest bug fix releases of Python 2.7/3.2. (Contributed by Ezio Melotti in [bpo-15114](https://bugs.python.org/issue?@action=redirect&bpo=15114)
, and [bpo-14538](https://bugs.python.org/issue?@action=redirect&bpo=14538)
, [bpo-13993](https://bugs.python.org/issue?@action=redirect&bpo=13993)
, [bpo-13960](https://bugs.python.org/issue?@action=redirect&bpo=13960)
, [bpo-13358](https://bugs.python.org/issue?@action=redirect&bpo=13358)
, [bpo-1745761](https://bugs.python.org/issue?@action=redirect&bpo=1745761)
, [bpo-755670](https://bugs.python.org/issue?@action=redirect&bpo=755670)
, [bpo-13357](https://bugs.python.org/issue?@action=redirect&bpo=13357)
, [bpo-12629](https://bugs.python.org/issue?@action=redirect&bpo=12629)
, [bpo-1200313](https://bugs.python.org/issue?@action=redirect&bpo=1200313)
, [bpo-670664](https://bugs.python.org/issue?@action=redirect&bpo=670664)
, [bpo-13273](https://bugs.python.org/issue?@action=redirect&bpo=13273)
, [bpo-12888](https://bugs.python.org/issue?@action=redirect&bpo=12888)
, [bpo-7311](https://bugs.python.org/issue?@action=redirect&bpo=7311)
.)

A new [`html5`](https://docs.python.org/3/library/html.entities.html#html.entities.html5 "html.entities.html5")
 dictionary that maps HTML5 named character references to the equivalent Unicode character(s) (e.g. `html5['gt;'] == '>'`) has been added to the [`html.entities`](https://docs.python.org/3/library/html.entities.html#module-html.entities "html.entities: Definitions of HTML general entities.")
 module. The dictionary is now also used by [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser")
. (Contributed by Ezio Melotti in [bpo-11113](https://bugs.python.org/issue?@action=redirect&bpo=11113)
 and [bpo-15156](https://bugs.python.org/issue?@action=redirect&bpo=15156)
.)

### imaplib[¶](https://docs.python.org/3/whatsnew/3.3.html#imaplib "Link to this heading")

The [`IMAP4_SSL`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_SSL "imaplib.IMAP4_SSL")
 constructor now accepts an SSLContext parameter to control parameters of the secure channel.

(Contributed by Sijin Joseph in [bpo-8808](https://bugs.python.org/issue?@action=redirect&bpo=8808)
.)

### inspect[¶](https://docs.python.org/3/whatsnew/3.3.html#inspect "Link to this heading")

A new [`getclosurevars()`](https://docs.python.org/3/library/inspect.html#inspect.getclosurevars "inspect.getclosurevars")
 function has been added. This function reports the current binding of all names referenced from the function body and where those names were resolved, making it easier to verify correct internal state when testing code that relies on stateful closures.

(Contributed by Meador Inge and Nick Coghlan in [bpo-13062](https://bugs.python.org/issue?@action=redirect&bpo=13062)
.)

A new [`getgeneratorlocals()`](https://docs.python.org/3/library/inspect.html#inspect.getgeneratorlocals "inspect.getgeneratorlocals")
 function has been added. This function reports the current binding of local variables in the generator’s stack frame, making it easier to verify correct internal state when testing generators.

(Contributed by Meador Inge in [bpo-15153](https://bugs.python.org/issue?@action=redirect&bpo=15153)
.)

### io[¶](https://docs.python.org/3/whatsnew/3.3.html#io "Link to this heading")

The [`open()`](https://docs.python.org/3/library/io.html#io.open "io.open")
 function has a new `'x'` mode that can be used to exclusively create a new file, and raise a [`FileExistsError`](https://docs.python.org/3/builtins/exceptions.html#FileExistsError "FileExistsError")
 if the file already exists. It is based on the C11 ‘x’ mode to fopen().

(Contributed by David Townshend in [bpo-12760](https://bugs.python.org/issue?@action=redirect&bpo=12760)
.)

The constructor of the [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
 class has a new _write\_through_ optional argument. If _write\_through_ is `True`, calls to `write()` are guaranteed not to be buffered: any data written on the `TextIOWrapper` object is immediately handled to its underlying binary buffer.

### itertools[¶](https://docs.python.org/3/whatsnew/3.3.html#itertools "Link to this heading")

[`accumulate()`](https://docs.python.org/3/library/itertools.html#itertools.accumulate "itertools.accumulate")
 now takes an optional `func` argument for providing a user-supplied binary function.

### logging[¶](https://docs.python.org/3/whatsnew/3.3.html#logging "Link to this heading")

The [`basicConfig()`](https://docs.python.org/3/library/logging.html#logging.basicConfig "logging.basicConfig")
 function now supports an optional `handlers` argument taking an iterable of handlers to be added to the root logger.

A class level attribute `append_nul` has been added to [`SysLogHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler "logging.handlers.SysLogHandler")
 to allow control of the appending of the `NUL` (`\000`) byte to syslog records, since for some daemons it is required while for others it is passed through to the log.

### math[¶](https://docs.python.org/3/whatsnew/3.3.html#math "Link to this heading")

The [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).")
 module has a new function, [`log2()`](https://docs.python.org/3/library/math.html#math.log2 "math.log2")
, which returns the base-2 logarithm of _x_.

(Written by Mark Dickinson in [bpo-11888](https://bugs.python.org/issue?@action=redirect&bpo=11888)
.)

### mmap[¶](https://docs.python.org/3/whatsnew/3.3.html#mmap "Link to this heading")

The [`read()`](https://docs.python.org/3/library/mmap.html#mmap.mmap.read "mmap.mmap.read")
 method is now more compatible with other file-like objects: if the argument is omitted or specified as `None`, it returns the bytes from the current file position to the end of the mapping. (Contributed by Petri Lehtinen in [bpo-12021](https://bugs.python.org/issue?@action=redirect&bpo=12021)
.)

### multiprocessing[¶](https://docs.python.org/3/whatsnew/3.3.html#multiprocessing "Link to this heading")

The new [`multiprocessing.connection.wait()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.wait "multiprocessing.connection.wait")
 function allows polling multiple objects (such as connections, sockets and pipes) with a timeout. (Contributed by Richard Oudkerk in [bpo-12328](https://bugs.python.org/issue?@action=redirect&bpo=12328)
.)

[`multiprocessing.connection.Connection`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.connection.Connection "multiprocessing.connection.Connection")
 objects can now be transferred over multiprocessing connections. (Contributed by Richard Oudkerk in [bpo-4892](https://bugs.python.org/issue?@action=redirect&bpo=4892)
.)

[`multiprocessing.Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process")
 now accepts a `daemon` keyword argument to override the default behavior of inheriting the `daemon` flag from the parent process ([bpo-6064](https://bugs.python.org/issue?@action=redirect&bpo=6064)
).

New attribute [`multiprocessing.Process.sentinel`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process.sentinel "multiprocessing.Process.sentinel")
 allows a program to wait on multiple [`Process`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Process "multiprocessing.Process")
 objects at one time using the appropriate OS primitives (for example, [`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.")
 on posix systems).

New methods [`multiprocessing.pool.Pool.starmap()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap "multiprocessing.pool.Pool.starmap")
 and [`starmap_async()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap_async "multiprocessing.pool.Pool.starmap_async")
 provide [`itertools.starmap()`](https://docs.python.org/3/library/itertools.html#itertools.starmap "itertools.starmap")
 equivalents to the existing [`multiprocessing.pool.Pool.map()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map "multiprocessing.pool.Pool.map")
 and [`map_async()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.map_async "multiprocessing.pool.Pool.map_async")
 functions. (Contributed by Hynek Schlawack in [bpo-12708](https://bugs.python.org/issue?@action=redirect&bpo=12708)
.)

### nntplib[¶](https://docs.python.org/3/whatsnew/3.3.html#nntplib "Link to this heading")

The `nntplib.NNTP` class now supports the context management protocol to unconditionally consume [`socket.error`](https://docs.python.org/3/library/socket.html#socket.error "socket.error")
 exceptions and to close the NNTP connection when done:

Copy

\>>> from nntplib import NNTP
\>>> with NNTP('news.gmane.org') as n:
...     n.group('gmane.comp.python.committers')
...
('211 1755 1 1755 gmane.comp.python.committers', 1755, 1, 1755, 'gmane.comp.python.committers')
\>>>

(Contributed by Giampaolo Rodolà in [bpo-9795](https://bugs.python.org/issue?@action=redirect&bpo=9795)
.)

### os[¶](https://docs.python.org/3/whatsnew/3.3.html#os "Link to this heading")

*   The [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
     module has a new [`pipe2()`](https://docs.python.org/3/library/os.html#os.pipe2 "os.pipe2")
     function that makes it possible to create a pipe with [`O_CLOEXEC`](https://docs.python.org/3/library/os.html#os.O_CLOEXEC "os.O_CLOEXEC")
     or [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK")
     flags set atomically. This is especially useful to avoid race conditions in multi-threaded programs.
    
*   The [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
     module has a new [`sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile")
     function which provides an efficient “zero-copy” way for copying data from one file (or socket) descriptor to another. The phrase “zero-copy” refers to the fact that all of the copying of data between the two descriptors is done entirely by the kernel, with no copying of data into userspace buffers. `sendfile()` can be used to efficiently copy data from a file on disk to a network socket, e.g. for downloading a file.
    
    (Patch submitted by Ross Lagerwall and Giampaolo Rodolà in [bpo-10882](https://bugs.python.org/issue?@action=redirect&bpo=10882)
    .)
    
*   To avoid race conditions like symlink attacks and issues with temporary files and directories, it is more reliable (and also faster) to manipulate file descriptors instead of file names. Python 3.3 enhances existing functions and introduces new functions to work on file descriptors ([bpo-4761](https://bugs.python.org/issue?@action=redirect&bpo=4761)
    , [bpo-10755](https://bugs.python.org/issue?@action=redirect&bpo=10755)
     and [bpo-14626](https://bugs.python.org/issue?@action=redirect&bpo=14626)
    ).
    
    *   The [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
         module has a new [`fwalk()`](https://docs.python.org/3/library/os.html#os.fwalk "os.fwalk")
         function similar to [`walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk")
         except that it also yields file descriptors referring to the directories visited. This is especially useful to avoid symlink races.
        
    *   The following functions get new optional _dir\_fd_ ([paths relative to directory descriptors](https://docs.python.org/3/library/os.html#dir-fd)
        ) and/or _follow\_symlinks_ ([not following symlinks](https://docs.python.org/3/library/os.html#follow-symlinks)
        ): [`access()`](https://docs.python.org/3/library/os.html#os.access "os.access")
        , [`chflags()`](https://docs.python.org/3/library/os.html#os.chflags "os.chflags")
        , [`chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")
        , [`chown()`](https://docs.python.org/3/library/os.html#os.chown "os.chown")
        , [`link()`](https://docs.python.org/3/library/os.html#os.link "os.link")
        , [`lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat")
        , [`mkdir()`](https://docs.python.org/3/library/os.html#os.mkdir "os.mkdir")
        , [`mkfifo()`](https://docs.python.org/3/library/os.html#os.mkfifo "os.mkfifo")
        , [`mknod()`](https://docs.python.org/3/library/os.html#os.mknod "os.mknod")
        , [`open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
        , [`readlink()`](https://docs.python.org/3/library/os.html#os.readlink "os.readlink")
        , [`remove()`](https://docs.python.org/3/library/os.html#os.remove "os.remove")
        , [`rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename")
        , [`replace()`](https://docs.python.org/3/library/os.html#os.replace "os.replace")
        , [`rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir")
        , [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
        , [`symlink()`](https://docs.python.org/3/library/os.html#os.symlink "os.symlink")
        , [`unlink()`](https://docs.python.org/3/library/os.html#os.unlink "os.unlink")
        , [`utime()`](https://docs.python.org/3/library/os.html#os.utime "os.utime")
        . Platform support for using these parameters can be checked via the sets [`os.supports_dir_fd`](https://docs.python.org/3/library/os.html#os.supports_dir_fd "os.supports_dir_fd")
         and [`os.supports_follow_symlinks`](https://docs.python.org/3/library/os.html#os.supports_follow_symlinks "os.supports_follow_symlinks")
        .
        
    *   The following functions now support a file descriptor for their path argument: [`chdir()`](https://docs.python.org/3/library/os.html#os.chdir "os.chdir")
        , [`chmod()`](https://docs.python.org/3/library/os.html#os.chmod "os.chmod")
        , [`chown()`](https://docs.python.org/3/library/os.html#os.chown "os.chown")
        , [`execve()`](https://docs.python.org/3/library/os.html#os.execve "os.execve")
        , [`listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir")
        , [`pathconf()`](https://docs.python.org/3/library/os.html#os.pathconf "os.pathconf")
        , [`exists()`](https://docs.python.org/3/library/os.path.html#os.path.exists "os.path.exists")
        , [`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
        , [`statvfs()`](https://docs.python.org/3/library/os.html#os.statvfs "os.statvfs")
        , [`utime()`](https://docs.python.org/3/library/os.html#os.utime "os.utime")
        . Platform support for this can be checked via the [`os.supports_fd`](https://docs.python.org/3/library/os.html#os.supports_fd "os.supports_fd")
         set.
        
*   [`access()`](https://docs.python.org/3/library/os.html#os.access "os.access")
     accepts an `effective_ids` keyword argument to turn on using the effective uid/gid rather than the real uid/gid in the access check. Platform support for this can be checked via the [`supports_effective_ids`](https://docs.python.org/3/library/os.html#os.supports_effective_ids "os.supports_effective_ids")
     set.
    
*   The [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
     module has two new functions: [`getpriority()`](https://docs.python.org/3/library/os.html#os.getpriority "os.getpriority")
     and [`setpriority()`](https://docs.python.org/3/library/os.html#os.setpriority "os.setpriority")
    . They can be used to get or set process niceness/priority in a fashion similar to [`os.nice()`](https://docs.python.org/3/library/os.html#os.nice "os.nice")
     but extended to all processes instead of just the current one.
    
    (Patch submitted by Giampaolo Rodolà in [bpo-10784](https://bugs.python.org/issue?@action=redirect&bpo=10784)
    .)
    
*   The new [`os.replace()`](https://docs.python.org/3/library/os.html#os.replace "os.replace")
     function allows cross-platform renaming of a file with overwriting the destination. With [`os.rename()`](https://docs.python.org/3/library/os.html#os.rename "os.rename")
    , an existing destination file is overwritten under POSIX, but raises an error under Windows. (Contributed by Antoine Pitrou in [bpo-8828](https://bugs.python.org/issue?@action=redirect&bpo=8828)
    .)
    
*   The stat family of functions ([`stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
    , [`fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat")
    , and [`lstat()`](https://docs.python.org/3/library/os.html#os.lstat "os.lstat")
    ) now support reading a file’s timestamps with nanosecond precision. Symmetrically, [`utime()`](https://docs.python.org/3/library/os.html#os.utime "os.utime")
     can now write file timestamps with nanosecond precision. (Contributed by Larry Hastings in [bpo-14127](https://bugs.python.org/issue?@action=redirect&bpo=14127)
    .)
    
*   The new [`os.get_terminal_size()`](https://docs.python.org/3/library/os.html#os.get_terminal_size "os.get_terminal_size")
     function queries the size of the terminal attached to a file descriptor. See also [`shutil.get_terminal_size()`](https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size "shutil.get_terminal_size")
    . (Contributed by Zbigniew Jędrzejewski-Szmek in [bpo-13609](https://bugs.python.org/issue?@action=redirect&bpo=13609)
    .)
    

*   New functions to support Linux extended attributes ([bpo-12720](https://bugs.python.org/issue?@action=redirect&bpo=12720)
    ): [`getxattr()`](https://docs.python.org/3/library/os.html#os.getxattr "os.getxattr")
    , [`listxattr()`](https://docs.python.org/3/library/os.html#os.listxattr "os.listxattr")
    , [`removexattr()`](https://docs.python.org/3/library/os.html#os.removexattr "os.removexattr")
    , [`setxattr()`](https://docs.python.org/3/library/os.html#os.setxattr "os.setxattr")
    .
    
*   New interface to the scheduler. These functions control how a process is allocated CPU time by the operating system. New functions: [`sched_get_priority_max()`](https://docs.python.org/3/library/os.html#os.sched_get_priority_max "os.sched_get_priority_max")
    , [`sched_get_priority_min()`](https://docs.python.org/3/library/os.html#os.sched_get_priority_min "os.sched_get_priority_min")
    , [`sched_getaffinity()`](https://docs.python.org/3/library/os.html#os.sched_getaffinity "os.sched_getaffinity")
    , [`sched_getparam()`](https://docs.python.org/3/library/os.html#os.sched_getparam "os.sched_getparam")
    , [`sched_getscheduler()`](https://docs.python.org/3/library/os.html#os.sched_getscheduler "os.sched_getscheduler")
    , [`sched_rr_get_interval()`](https://docs.python.org/3/library/os.html#os.sched_rr_get_interval "os.sched_rr_get_interval")
    , [`sched_setaffinity()`](https://docs.python.org/3/library/os.html#os.sched_setaffinity "os.sched_setaffinity")
    , [`sched_setparam()`](https://docs.python.org/3/library/os.html#os.sched_setparam "os.sched_setparam")
    , [`sched_setscheduler()`](https://docs.python.org/3/library/os.html#os.sched_setscheduler "os.sched_setscheduler")
    , [`sched_yield()`](https://docs.python.org/3/library/os.html#os.sched_yield "os.sched_yield")
    ,
    
*   New functions to control the file system:
    
    *   [`posix_fadvise()`](https://docs.python.org/3/library/os.html#os.posix_fadvise "os.posix_fadvise")
        : Announces an intention to access data in a specific pattern thus allowing the kernel to make optimizations.
        
    *   [`posix_fallocate()`](https://docs.python.org/3/library/os.html#os.posix_fallocate "os.posix_fallocate")
        : Ensures that enough disk space is allocated for a file.
        
    *   [`sync()`](https://docs.python.org/3/library/os.html#os.sync "os.sync")
        : Force write of everything to disk.
        
*   Additional new posix functions:
    
    *   [`lockf()`](https://docs.python.org/3/library/os.html#os.lockf "os.lockf")
        : Apply, test or remove a POSIX lock on an open file descriptor.
        
    *   [`pread()`](https://docs.python.org/3/library/os.html#os.pread "os.pread")
        : Read from a file descriptor at an offset, the file offset remains unchanged.
        
    *   [`pwrite()`](https://docs.python.org/3/library/os.html#os.pwrite "os.pwrite")
        : Write to a file descriptor from an offset, leaving the file offset unchanged.
        
    *   [`readv()`](https://docs.python.org/3/library/os.html#os.readv "os.readv")
        : Read from a file descriptor into a number of writable buffers.
        
    *   [`truncate()`](https://docs.python.org/3/library/os.html#os.truncate "os.truncate")
        : Truncate the file corresponding to _path_, so that it is at most _length_ bytes in size.
        
    *   [`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid")
        : Wait for the completion of one or more child processes.
        
    *   [`writev()`](https://docs.python.org/3/library/os.html#os.writev "os.writev")
        : Write the contents of _buffers_ to a file descriptor, where _buffers_ is an arbitrary sequence of buffers.
        
    *   [`getgrouplist()`](https://docs.python.org/3/library/os.html#os.getgrouplist "os.getgrouplist")
         ([bpo-9344](https://bugs.python.org/issue?@action=redirect&bpo=9344)
        ): Return list of group ids that specified user belongs to.
        
*   [`times()`](https://docs.python.org/3/library/os.html#os.times "os.times")
     and [`uname()`](https://docs.python.org/3/library/os.html#os.uname "os.uname")
    : Return type changed from a tuple to a tuple-like object with named attributes.
    
*   Some platforms now support additional constants for the [`lseek()`](https://docs.python.org/3/library/os.html#os.lseek "os.lseek")
     function, such as `os.SEEK_HOLE` and `os.SEEK_DATA`.
    
*   New constants [`RTLD_LAZY`](https://docs.python.org/3/library/os.html#os.RTLD_LAZY "os.RTLD_LAZY")
    , [`RTLD_NOW`](https://docs.python.org/3/library/os.html#os.RTLD_NOW "os.RTLD_NOW")
    , [`RTLD_GLOBAL`](https://docs.python.org/3/library/os.html#os.RTLD_GLOBAL "os.RTLD_GLOBAL")
    , [`RTLD_LOCAL`](https://docs.python.org/3/library/os.html#os.RTLD_LOCAL "os.RTLD_LOCAL")
    , [`RTLD_NODELETE`](https://docs.python.org/3/library/os.html#os.RTLD_NODELETE "os.RTLD_NODELETE")
    , [`RTLD_NOLOAD`](https://docs.python.org/3/library/os.html#os.RTLD_NOLOAD "os.RTLD_NOLOAD")
    , and [`RTLD_DEEPBIND`](https://docs.python.org/3/library/os.html#os.RTLD_DEEPBIND "os.RTLD_DEEPBIND")
     are available on platforms that support them. These are for use with the [`sys.setdlopenflags()`](https://docs.python.org/3/library/sys.html#sys.setdlopenflags "sys.setdlopenflags")
     function, and supersede the similar constants defined in [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.")
     and `DLFCN`. (Contributed by Victor Stinner in [bpo-13226](https://bugs.python.org/issue?@action=redirect&bpo=13226)
    .)
    
*   [`os.symlink()`](https://docs.python.org/3/library/os.html#os.symlink "os.symlink")
     now accepts (and ignores) the `target_is_directory` keyword argument on non-Windows platforms, to ease cross-platform support.
    

### pdb[¶](https://docs.python.org/3/whatsnew/3.3.html#pdb "Link to this heading")

Tab-completion is now available not only for command names, but also their arguments. For example, for the `break` command, function and file names are completed.

(Contributed by Georg Brandl in [bpo-14210](https://bugs.python.org/issue?@action=redirect&bpo=14210)
)

### pickle[¶](https://docs.python.org/3/whatsnew/3.3.html#pickle "Link to this heading")

[`pickle.Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler")
 objects now have an optional [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table")
 attribute allowing per-pickler reduction functions to be set.

(Contributed by Richard Oudkerk in [bpo-14166](https://bugs.python.org/issue?@action=redirect&bpo=14166)
.)

### pydoc[¶](https://docs.python.org/3/whatsnew/3.3.html#pydoc "Link to this heading")

The Tk GUI and the `serve()` function have been removed from the [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
 module: `pydoc -g` and `serve()` have been deprecated in Python 3.2.

### re[¶](https://docs.python.org/3/whatsnew/3.3.html#re "Link to this heading")

[`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 regular expressions now support `\u` and `\U` escapes.

(Contributed by Serhiy Storchaka in [bpo-3665](https://bugs.python.org/issue?@action=redirect&bpo=3665)
.)

### sched[¶](https://docs.python.org/3/whatsnew/3.3.html#sched "Link to this heading")

*   [`run()`](https://docs.python.org/3/library/sched.html#sched.scheduler.run "sched.scheduler.run")
     now accepts a _blocking_ parameter which when set to false makes the method execute the scheduled events due to expire soonest (if any) and then return immediately. This is useful in case you want to use the [`scheduler`](https://docs.python.org/3/library/sched.html#sched.scheduler "sched.scheduler")
     in non-blocking applications. (Contributed by Giampaolo Rodolà in [bpo-13449](https://bugs.python.org/issue?@action=redirect&bpo=13449)
    .)
    
*   [`scheduler`](https://docs.python.org/3/library/sched.html#sched.scheduler "sched.scheduler")
     class can now be safely used in multi-threaded environments. (Contributed by Josiah Carlson and Giampaolo Rodolà in [bpo-8684](https://bugs.python.org/issue?@action=redirect&bpo=8684)
    .)
    
*   _timefunc_ and _delayfunct_ parameters of [`scheduler`](https://docs.python.org/3/library/sched.html#sched.scheduler "sched.scheduler")
     class constructor are now optional and defaults to [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time")
     and [`time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep "time.sleep")
     respectively. (Contributed by Chris Clark in [bpo-13245](https://bugs.python.org/issue?@action=redirect&bpo=13245)
    .)
    
*   [`enter()`](https://docs.python.org/3/library/sched.html#sched.scheduler.enter "sched.scheduler.enter")
     and [`enterabs()`](https://docs.python.org/3/library/sched.html#sched.scheduler.enterabs "sched.scheduler.enterabs")
     _argument_ parameter is now optional. (Contributed by Chris Clark in [bpo-13245](https://bugs.python.org/issue?@action=redirect&bpo=13245)
    .)
    
*   [`enter()`](https://docs.python.org/3/library/sched.html#sched.scheduler.enter "sched.scheduler.enter")
     and [`enterabs()`](https://docs.python.org/3/library/sched.html#sched.scheduler.enterabs "sched.scheduler.enterabs")
     now accept a _kwargs_ parameter. (Contributed by Chris Clark in [bpo-13245](https://bugs.python.org/issue?@action=redirect&bpo=13245)
    .)
    

### select[¶](https://docs.python.org/3/whatsnew/3.3.html#select "Link to this heading")

Solaris and derivative platforms have a new class [`select.devpoll`](https://docs.python.org/3/library/select.html#select.devpoll "select.devpoll")
 for high performance asynchronous sockets via `/dev/poll`. (Contributed by Jesús Cea Avión in [bpo-6397](https://bugs.python.org/issue?@action=redirect&bpo=6397)
.)

### shlex[¶](https://docs.python.org/3/whatsnew/3.3.html#shlex "Link to this heading")

The previously undocumented helper function `quote` from the `pipes` modules has been moved to the [`shlex`](https://docs.python.org/3/library/shlex.html#module-shlex "shlex: Simple lexical analysis for Unix shell-like languages.")
 module and documented. [`quote()`](https://docs.python.org/3/library/shlex.html#shlex.quote "shlex.quote")
 properly escapes all characters in a string that might be otherwise given special meaning by the shell.

### shutil[¶](https://docs.python.org/3/whatsnew/3.3.html#shutil "Link to this heading")

*   New functions:
    
    *   [`disk_usage()`](https://docs.python.org/3/library/shutil.html#shutil.disk_usage "shutil.disk_usage")
        : provides total, used and free disk space statistics. (Contributed by Giampaolo Rodolà in [bpo-12442](https://bugs.python.org/issue?@action=redirect&bpo=12442)
        .)
        
    *   [`chown()`](https://docs.python.org/3/library/shutil.html#shutil.chown "shutil.chown")
        : allows one to change user and/or group of the given path also specifying the user/group names and not only their numeric ids. (Contributed by Sandro Tosi in [bpo-12191](https://bugs.python.org/issue?@action=redirect&bpo=12191)
        .)
        
    *   [`shutil.get_terminal_size()`](https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size "shutil.get_terminal_size")
        : returns the size of the terminal window to which the interpreter is attached. (Contributed by Zbigniew Jędrzejewski-Szmek in [bpo-13609](https://bugs.python.org/issue?@action=redirect&bpo=13609)
        .)
        
*   [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2")
     and [`copystat()`](https://docs.python.org/3/library/shutil.html#shutil.copystat "shutil.copystat")
     now preserve file timestamps with nanosecond precision on platforms that support it. They also preserve file “extended attributes” on Linux. (Contributed by Larry Hastings in [bpo-14127](https://bugs.python.org/issue?@action=redirect&bpo=14127)
     and [bpo-15238](https://bugs.python.org/issue?@action=redirect&bpo=15238)
    .)
    
*   Several functions now take an optional `symlinks` argument: when that parameter is true, symlinks aren’t dereferenced and the operation instead acts on the symlink itself (or creates one, if relevant). (Contributed by Hynek Schlawack in [bpo-12715](https://bugs.python.org/issue?@action=redirect&bpo=12715)
    .)
    
*   When copying files to a different file system, [`move()`](https://docs.python.org/3/library/shutil.html#shutil.move "shutil.move")
     now handles symlinks the way the posix `mv` command does, recreating the symlink rather than copying the target file contents. (Contributed by Jonathan Niehof in [bpo-9993](https://bugs.python.org/issue?@action=redirect&bpo=9993)
    .) `move()` now also returns the `dst` argument as its result.
    
*   [`rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree")
     is now resistant to symlink attacks on platforms which support the new `dir_fd` parameter in [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open")
     and [`os.unlink()`](https://docs.python.org/3/library/os.html#os.unlink "os.unlink")
    . (Contributed by Martin von Löwis and Hynek Schlawack in [bpo-4489](https://bugs.python.org/issue?@action=redirect&bpo=4489)
    .)
    

### signal[¶](https://docs.python.org/3/whatsnew/3.3.html#signal "Link to this heading")

*   The [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")
     module has new functions:
    
    *   [`pthread_sigmask()`](https://docs.python.org/3/library/signal.html#signal.pthread_sigmask "signal.pthread_sigmask")
        : fetch and/or change the signal mask of the calling thread (Contributed by Jean-Paul Calderone in [bpo-8407](https://bugs.python.org/issue?@action=redirect&bpo=8407)
        );
        
    *   [`pthread_kill()`](https://docs.python.org/3/library/signal.html#signal.pthread_kill "signal.pthread_kill")
        : send a signal to a thread;
        
    *   [`sigpending()`](https://docs.python.org/3/library/signal.html#signal.sigpending "signal.sigpending")
        : examine pending functions;
        
    *   [`sigwait()`](https://docs.python.org/3/library/signal.html#signal.sigwait "signal.sigwait")
        : wait a signal;
        
    *   [`sigwaitinfo()`](https://docs.python.org/3/library/signal.html#signal.sigwaitinfo "signal.sigwaitinfo")
        : wait for a signal, returning detailed information about it;
        
    *   [`sigtimedwait()`](https://docs.python.org/3/library/signal.html#signal.sigtimedwait "signal.sigtimedwait")
        : like [`sigwaitinfo()`](https://docs.python.org/3/library/signal.html#signal.sigwaitinfo "signal.sigwaitinfo")
         but with a timeout.
        
*   The signal handler writes the signal number as a single byte instead of a nul byte into the wakeup file descriptor. So it is possible to wait more than one signal and know which signals were raised.
    
*   [`signal.signal()`](https://docs.python.org/3/library/signal.html#signal.signal "signal.signal")
     and [`signal.siginterrupt()`](https://docs.python.org/3/library/signal.html#signal.siginterrupt "signal.siginterrupt")
     raise an OSError, instead of a RuntimeError: OSError has an errno attribute.
    

### smtpd[¶](https://docs.python.org/3/whatsnew/3.3.html#smtpd "Link to this heading")

The `smtpd` module now supports [**RFC 5321**](https://datatracker.ietf.org/doc/html/rfc5321.html)
 (extended SMTP) and [**RFC 1870**](https://datatracker.ietf.org/doc/html/rfc1870.html)
 (size extension). Per the standard, these extensions are enabled if and only if the client initiates the session with an `EHLO` command.

(Initial `ELHO` support by Alberto Trevino. Size extension by Juhana Jauhiainen. Substantial additional work on the patch contributed by Michele Orrù and Dan Boswell. [bpo-8739](https://bugs.python.org/issue?@action=redirect&bpo=8739)
)

### smtplib[¶](https://docs.python.org/3/whatsnew/3.3.html#smtplib "Link to this heading")

The [`SMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "smtplib.SMTP")
, [`SMTP_SSL`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP_SSL "smtplib.SMTP_SSL")
, and [`LMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.LMTP "smtplib.LMTP")
 classes now accept a `source_address` keyword argument to specify the `(host, port)` to use as the source address in the bind call when creating the outgoing socket. (Contributed by Paulo Scardine in [bpo-11281](https://bugs.python.org/issue?@action=redirect&bpo=11281)
.)

[`SMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "smtplib.SMTP")
 now supports the context management protocol, allowing an `SMTP` instance to be used in a `with` statement. (Contributed by Giampaolo Rodolà in [bpo-11289](https://bugs.python.org/issue?@action=redirect&bpo=11289)
.)

The [`SMTP_SSL`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP_SSL "smtplib.SMTP_SSL")
 constructor and the [`starttls()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls "smtplib.SMTP.starttls")
 method now accept an SSLContext parameter to control parameters of the secure channel. (Contributed by Kasun Herath in [bpo-8809](https://bugs.python.org/issue?@action=redirect&bpo=8809)
.)

### socket[¶](https://docs.python.org/3/whatsnew/3.3.html#socket "Link to this heading")

*   The [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
     class now exposes additional methods to process ancillary data when supported by the underlying platform:
    
    *   [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg")
        
    *   [`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg")
        
    *   [`recvmsg_into()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg_into "socket.socket.recvmsg_into")
        
    
    (Contributed by David Watson in [bpo-6560](https://bugs.python.org/issue?@action=redirect&bpo=6560)
    , based on an earlier patch by Heiko Wundram)
    
*   The [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
     class now supports the PF\_CAN protocol family ([https://en.wikipedia.org/wiki/Socketcan](https://en.wikipedia.org/wiki/Socketcan)
    ), on Linux ([https://lwn.net/Articles/253425](https://lwn.net/Articles/253425)
    ).
    
    (Contributed by Matthias Fuchs, updated by Tiago Gonçalves in [bpo-10141](https://bugs.python.org/issue?@action=redirect&bpo=10141)
    .)
    
*   The [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
     class now supports the PF\_RDS protocol family ([https://en.wikipedia.org/wiki/Reliable\_Datagram\_Sockets](https://en.wikipedia.org/wiki/Reliable_Datagram_Sockets)
     and [https://oss.oracle.com/projects/rds](https://web.archive.org/web/20130115155505/https://oss.oracle.com/projects/rds/)
    ).
    
*   The [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket")
     class now supports the `PF_SYSTEM` protocol family on OS X. (Contributed by Michael Goderbauer in [bpo-13777](https://bugs.python.org/issue?@action=redirect&bpo=13777)
    .)
    
*   New function [`sethostname()`](https://docs.python.org/3/library/socket.html#socket.sethostname "socket.sethostname")
     allows the hostname to be set on Unix systems if the calling process has sufficient privileges. (Contributed by Ross Lagerwall in [bpo-10866](https://bugs.python.org/issue?@action=redirect&bpo=10866)
    .)
    

### socketserver[¶](https://docs.python.org/3/whatsnew/3.3.html#socketserver "Link to this heading")

[`BaseServer`](https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer "socketserver.BaseServer")
 now has an overridable method [`service_actions()`](https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.service_actions "socketserver.BaseServer.service_actions")
 that is called by the [`serve_forever()`](https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.serve_forever "socketserver.BaseServer.serve_forever")
 method in the service loop. [`ForkingMixIn`](https://docs.python.org/3/library/socketserver.html#socketserver.ForkingMixIn "socketserver.ForkingMixIn")
 now uses this to clean up zombie child processes. (Contributed by Justin Warkentin in [bpo-11109](https://bugs.python.org/issue?@action=redirect&bpo=11109)
.)

### sqlite3[¶](https://docs.python.org/3/whatsnew/3.3.html#sqlite3 "Link to this heading")

New [`sqlite3.Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection")
 method [`set_trace_callback()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_trace_callback "sqlite3.Connection.set_trace_callback")
 can be used to capture a trace of all sql commands processed by sqlite. (Contributed by Torsten Landschoff in [bpo-11688](https://bugs.python.org/issue?@action=redirect&bpo=11688)
.)

### ssl[¶](https://docs.python.org/3/whatsnew/3.3.html#ssl "Link to this heading")

*   The [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
     module has two new random generation functions:
    
    *   [`RAND_bytes()`](https://docs.python.org/3/library/ssl.html#ssl.RAND_bytes "ssl.RAND_bytes")
        : generate cryptographically strong pseudo-random bytes.
        
    *   `RAND_pseudo_bytes()`: generate pseudo-random bytes.
        
    
    (Contributed by Victor Stinner in [bpo-12049](https://bugs.python.org/issue?@action=redirect&bpo=12049)
    .)
    
*   The [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects")
     module now exposes a finer-grained exception hierarchy in order to make it easier to inspect the various kinds of errors. (Contributed by Antoine Pitrou in [bpo-11183](https://bugs.python.org/issue?@action=redirect&bpo=11183)
    .)
    
*   [`load_cert_chain()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_cert_chain "ssl.SSLContext.load_cert_chain")
     now accepts a _password_ argument to be used if the private key is encrypted. (Contributed by Adam Simpkins in [bpo-12803](https://bugs.python.org/issue?@action=redirect&bpo=12803)
    .)
    
*   Diffie-Hellman key exchange, both regular and Elliptic Curve-based, is now supported through the [`load_dh_params()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_dh_params "ssl.SSLContext.load_dh_params")
     and [`set_ecdh_curve()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_ecdh_curve "ssl.SSLContext.set_ecdh_curve")
     methods. (Contributed by Antoine Pitrou in [bpo-13626](https://bugs.python.org/issue?@action=redirect&bpo=13626)
     and [bpo-13627](https://bugs.python.org/issue?@action=redirect&bpo=13627)
    .)
    
*   SSL sockets have a new [`get_channel_binding()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.get_channel_binding "ssl.SSLSocket.get_channel_binding")
     method allowing the implementation of certain authentication mechanisms such as SCRAM-SHA-1-PLUS. (Contributed by Jacek Konieczny in [bpo-12551](https://bugs.python.org/issue?@action=redirect&bpo=12551)
    .)
    
*   You can query the SSL compression algorithm used by an SSL socket, thanks to its new [`compression()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.compression "ssl.SSLSocket.compression")
     method. The new attribute [`OP_NO_COMPRESSION`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_COMPRESSION "ssl.OP_NO_COMPRESSION")
     can be used to disable compression. (Contributed by Antoine Pitrou in [bpo-13634](https://bugs.python.org/issue?@action=redirect&bpo=13634)
    .)
    
*   Support has been added for the Next Protocol Negotiation extension using the [`ssl.SSLContext.set_npn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_npn_protocols "ssl.SSLContext.set_npn_protocols")
     method. (Contributed by Colin Marc in [bpo-14204](https://bugs.python.org/issue?@action=redirect&bpo=14204)
    .)
    
*   SSL errors can now be introspected more easily thanks to [`library`](https://docs.python.org/3/library/ssl.html#ssl.SSLError.library "ssl.SSLError.library")
     and [`reason`](https://docs.python.org/3/library/ssl.html#ssl.SSLError.reason "ssl.SSLError.reason")
     attributes. (Contributed by Antoine Pitrou in [bpo-14837](https://bugs.python.org/issue?@action=redirect&bpo=14837)
    .)
    
*   The [`get_server_certificate()`](https://docs.python.org/3/library/ssl.html#ssl.get_server_certificate "ssl.get_server_certificate")
     function now supports IPv6. (Contributed by Charles-François Natali in [bpo-11811](https://bugs.python.org/issue?@action=redirect&bpo=11811)
    .)
    
*   New attribute [`OP_CIPHER_SERVER_PREFERENCE`](https://docs.python.org/3/library/ssl.html#ssl.OP_CIPHER_SERVER_PREFERENCE "ssl.OP_CIPHER_SERVER_PREFERENCE")
     allows setting SSLv3 server sockets to use the server’s cipher ordering preference rather than the client’s ([bpo-13635](https://bugs.python.org/issue?@action=redirect&bpo=13635)
    ).
    

### stat[¶](https://docs.python.org/3/whatsnew/3.3.html#stat "Link to this heading")

The undocumented tarfile.filemode function has been moved to [`stat.filemode()`](https://docs.python.org/3/library/stat.html#stat.filemode "stat.filemode")
. It can be used to convert a file’s mode to a string of the form ‘-rwxrwxrwx’.

(Contributed by Giampaolo Rodolà in [bpo-14807](https://bugs.python.org/issue?@action=redirect&bpo=14807)
.)

### struct[¶](https://docs.python.org/3/whatsnew/3.3.html#struct "Link to this heading")

The [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")
 module now supports `ssize_t` and `size_t` via the new codes `n` and `N`, respectively. (Contributed by Antoine Pitrou in [bpo-3163](https://bugs.python.org/issue?@action=redirect&bpo=3163)
.)

### subprocess[¶](https://docs.python.org/3/whatsnew/3.3.html#subprocess "Link to this heading")

Command strings can now be bytes objects on posix platforms. (Contributed by Victor Stinner in [bpo-8513](https://bugs.python.org/issue?@action=redirect&bpo=8513)
.)

A new constant [`DEVNULL`](https://docs.python.org/3/library/subprocess.html#subprocess.DEVNULL "subprocess.DEVNULL")
 allows suppressing output in a platform-independent fashion. (Contributed by Ross Lagerwall in [bpo-5870](https://bugs.python.org/issue?@action=redirect&bpo=5870)
.)

### sys[¶](https://docs.python.org/3/whatsnew/3.3.html#sys "Link to this heading")

The [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
 module has a new [`thread_info`](https://docs.python.org/3/library/sys.html#sys.thread_info "sys.thread_info")
 [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple)
 holding information about the thread implementation ([bpo-11223](https://bugs.python.org/issue?@action=redirect&bpo=11223)
).

### tarfile[¶](https://docs.python.org/3/whatsnew/3.3.html#tarfile "Link to this heading")

[`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.")
 now supports `lzma` encoding via the [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
 module. (Contributed by Lars Gustäbel in [bpo-5689](https://bugs.python.org/issue?@action=redirect&bpo=5689)
.)

### tempfile[¶](https://docs.python.org/3/whatsnew/3.3.html#tempfile "Link to this heading")

[`tempfile.SpooledTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.SpooledTemporaryFile "tempfile.SpooledTemporaryFile")
's `truncate()` method now accepts a `size` parameter. (Contributed by Ryan Kelly in [bpo-9957](https://bugs.python.org/issue?@action=redirect&bpo=9957)
.)

### textwrap[¶](https://docs.python.org/3/whatsnew/3.3.html#textwrap "Link to this heading")

The [`textwrap`](https://docs.python.org/3/library/textwrap.html#module-textwrap "textwrap: Text wrapping and filling")
 module has a new [`indent()`](https://docs.python.org/3/library/textwrap.html#textwrap.indent "textwrap.indent")
 that makes it straightforward to add a common prefix to selected lines in a block of text ([bpo-13857](https://bugs.python.org/issue?@action=redirect&bpo=13857)
).

### threading[¶](https://docs.python.org/3/whatsnew/3.3.html#threading "Link to this heading")

[`threading.Condition`](https://docs.python.org/3/library/threading.html#threading.Condition "threading.Condition")
, [`threading.Semaphore`](https://docs.python.org/3/library/threading.html#threading.Semaphore "threading.Semaphore")
, [`threading.BoundedSemaphore`](https://docs.python.org/3/library/threading.html#threading.BoundedSemaphore "threading.BoundedSemaphore")
, [`threading.Event`](https://docs.python.org/3/library/threading.html#threading.Event "threading.Event")
, and [`threading.Timer`](https://docs.python.org/3/library/threading.html#threading.Timer "threading.Timer")
, all of which used to be factory functions returning a class instance, are now classes and may be subclassed. (Contributed by Éric Araujo in [bpo-10968](https://bugs.python.org/issue?@action=redirect&bpo=10968)
.)

The [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread")
 constructor now accepts a `daemon` keyword argument to override the default behavior of inheriting the `daemon` flag value from the parent thread ([bpo-6064](https://bugs.python.org/issue?@action=redirect&bpo=6064)
).

The formerly private function `_thread.get_ident` is now available as the public function [`threading.get_ident()`](https://docs.python.org/3/library/threading.html#threading.get_ident "threading.get_ident")
. This eliminates several cases of direct access to the `_thread` module in the stdlib. Third party code that used `_thread.get_ident` should likewise be changed to use the new public interface.

### time[¶](https://docs.python.org/3/whatsnew/3.3.html#time "Link to this heading")

The [**PEP 418**](https://peps.python.org/pep-0418/)
 added new functions to the [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.")
 module:

*   [`get_clock_info()`](https://docs.python.org/3/library/time.html#time.get_clock_info "time.get_clock_info")
    : Get information on a clock.
    
*   [`monotonic()`](https://docs.python.org/3/library/time.html#time.monotonic "time.monotonic")
    : Monotonic clock (cannot go backward), not affected by system clock updates.
    
*   [`perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter")
    : Performance counter with the highest available resolution to measure a short duration.
    
*   [`process_time()`](https://docs.python.org/3/library/time.html#time.process_time "time.process_time")
    : Sum of the system and user CPU time of the current process.
    

Other new functions:

*   [`clock_getres()`](https://docs.python.org/3/library/time.html#time.clock_getres "time.clock_getres")
    , [`clock_gettime()`](https://docs.python.org/3/library/time.html#time.clock_gettime "time.clock_gettime")
     and [`clock_settime()`](https://docs.python.org/3/library/time.html#time.clock_settime "time.clock_settime")
     functions with `CLOCK__xxx_` constants. (Contributed by Victor Stinner in [bpo-10278](https://bugs.python.org/issue?@action=redirect&bpo=10278)
    .)
    

To improve cross platform consistency, [`sleep()`](https://docs.python.org/3/library/time.html#time.sleep "time.sleep")
 now raises a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 when passed a negative sleep value. Previously this was an error on posix, but produced an infinite sleep on Windows.

### types[¶](https://docs.python.org/3/whatsnew/3.3.html#types "Link to this heading")

Add a new [`types.MappingProxyType`](https://docs.python.org/3/library/types.html#types.MappingProxyType "types.MappingProxyType")
 class: Read-only proxy of a mapping. ([bpo-14386](https://bugs.python.org/issue?@action=redirect&bpo=14386)
)

The new functions [`types.new_class()`](https://docs.python.org/3/library/types.html#types.new_class "types.new_class")
 and [`types.prepare_class()`](https://docs.python.org/3/library/types.html#types.prepare_class "types.prepare_class")
 provide support for [**PEP 3115**](https://peps.python.org/pep-3115/)
 compliant dynamic type creation. ([bpo-14588](https://bugs.python.org/issue?@action=redirect&bpo=14588)
)

### unittest[¶](https://docs.python.org/3/whatsnew/3.3.html#unittest "Link to this heading")

[`assertRaises()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "unittest.TestCase.assertRaises")
, [`assertRaisesRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaisesRegex "unittest.TestCase.assertRaisesRegex")
, [`assertWarns()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarns "unittest.TestCase.assertWarns")
, and [`assertWarnsRegex()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertWarnsRegex "unittest.TestCase.assertWarnsRegex")
 now accept a keyword argument _msg_ when used as context managers. (Contributed by Ezio Melotti and Winston Ewert in [bpo-10775](https://bugs.python.org/issue?@action=redirect&bpo=10775)
.)

[`unittest.TestCase.run()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.run "unittest.TestCase.run")
 now returns the [`TestResult`](https://docs.python.org/3/library/unittest.html#unittest.TestResult "unittest.TestResult")
 object.

### urllib[¶](https://docs.python.org/3/whatsnew/3.3.html#urllib "Link to this heading")

The [`Request`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request "urllib.request.Request")
 class, now accepts a _method_ argument used by [`get_method()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request.get_method "urllib.request.Request.get_method")
 to determine what HTTP method should be used. For example, this will send a `'HEAD'` request:

Copy

\>>> urlopen(Request('https://www.python.org', method\='HEAD'))

([bpo-1673007](https://bugs.python.org/issue?@action=redirect&bpo=1673007)
)

### webbrowser[¶](https://docs.python.org/3/whatsnew/3.3.html#webbrowser "Link to this heading")

The [`webbrowser`](https://docs.python.org/3/library/webbrowser.html#module-webbrowser "webbrowser: Easy-to-use controller for web browsers.")
 module supports more “browsers”: Google Chrome (named **chrome**, **chromium**, **chrome-browser** or **chromium-browser** depending on the version and operating system), and the generic launchers **xdg-open**, from the FreeDesktop.org project, and **gvfs-open**, which is the default URI handler for GNOME 3. (The former contributed by Arnaud Calmettes in [bpo-13620](https://bugs.python.org/issue?@action=redirect&bpo=13620)
, the latter by Matthias Klose in [bpo-14493](https://bugs.python.org/issue?@action=redirect&bpo=14493)
.)

### xml.etree.ElementTree[¶](https://docs.python.org/3/whatsnew/3.3.html#xml-etree-elementtree "Link to this heading")

The [`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")
 module now imports its C accelerator by default; there is no longer a need to explicitly import `xml.etree.cElementTree` (this module stays for backwards compatibility, but is now deprecated). In addition, the `iter` family of methods of [`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element")
 has been optimized (rewritten in C). The module’s documentation has also been greatly improved with added examples and a more detailed reference.

### zlib[¶](https://docs.python.org/3/whatsnew/3.3.html#zlib "Link to this heading")

New attribute [`zlib.Decompress.eof`](https://docs.python.org/3/library/zlib.html#zlib.Decompress.eof "zlib.Decompress.eof")
 makes it possible to distinguish between a properly formed compressed stream and an incomplete or truncated one. (Contributed by Nadeem Vawda in [bpo-12646](https://bugs.python.org/issue?@action=redirect&bpo=12646)
.)

New attribute [`zlib.ZLIB_RUNTIME_VERSION`](https://docs.python.org/3/library/zlib.html#zlib.ZLIB_RUNTIME_VERSION "zlib.ZLIB_RUNTIME_VERSION")
 reports the version string of the underlying `zlib` library that is loaded at runtime. (Contributed by Torsten Landschoff in [bpo-12306](https://bugs.python.org/issue?@action=redirect&bpo=12306)
.)

Optimizations[¶](https://docs.python.org/3/whatsnew/3.3.html#optimizations "Link to this heading")

---------------------------------------------------------------------------------------------------

Major performance enhancements have been added:

*   Thanks to [**PEP 393**](https://peps.python.org/pep-0393/)
    , some operations on Unicode strings have been optimized:
    
    *   the memory footprint is divided by 2 to 4 depending on the text
        
    *   encode an ASCII string to UTF-8 doesn’t need to encode characters anymore, the UTF-8 representation is shared with the ASCII representation
        
    *   the UTF-8 encoder has been optimized
        
    *   repeating a single ASCII letter and getting a substring of an ASCII string is 4 times faster
        
*   UTF-8 is now 2x to 4x faster. UTF-16 encoding is now up to 10x faster.
    
    (Contributed by Serhiy Storchaka, [bpo-14624](https://bugs.python.org/issue?@action=redirect&bpo=14624)
    , [bpo-14738](https://bugs.python.org/issue?@action=redirect&bpo=14738)
     and [bpo-15026](https://bugs.python.org/issue?@action=redirect&bpo=15026)
    .)
    

Build and C API Changes[¶](https://docs.python.org/3/whatsnew/3.3.html#build-and-c-api-changes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Changes to Python’s build process and to the C API include:

*   New [**PEP 3118**](https://peps.python.org/pep-3118/)
     related function:
    
    *   [`PyMemoryView_FromMemory()`](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromMemory "PyMemoryView_FromMemory")
        
*   [**PEP 393**](https://peps.python.org/pep-0393/)
     added new Unicode types, macros and functions:
    
    *   High-level API:
        
        *   [`PyUnicode_CopyCharacters()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CopyCharacters "PyUnicode_CopyCharacters")
            
        *   [`PyUnicode_FindChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FindChar "PyUnicode_FindChar")
            
        *   [`PyUnicode_GetLength()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetLength "PyUnicode_GetLength")
            , [`PyUnicode_GET_LENGTH`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GET_LENGTH "PyUnicode_GET_LENGTH")
            
        *   [`PyUnicode_New()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_New "PyUnicode_New")
            
        *   [`PyUnicode_Substring()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Substring "PyUnicode_Substring")
            
        *   [`PyUnicode_ReadChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_ReadChar "PyUnicode_ReadChar")
            , [`PyUnicode_WriteChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_WriteChar "PyUnicode_WriteChar")
            
    *   Low-level API:
        
        *   [`Py_UCS1`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS1 "Py_UCS1")
            , [`Py_UCS2`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS2 "Py_UCS2")
            , [`Py_UCS4`](https://docs.python.org/3/c-api/unicode.html#c.Py_UCS4 "Py_UCS4")
             types
            
        *   [`PyASCIIObject`](https://docs.python.org/3/c-api/unicode.html#c.PyASCIIObject "PyASCIIObject")
             and [`PyCompactUnicodeObject`](https://docs.python.org/3/c-api/unicode.html#c.PyCompactUnicodeObject "PyCompactUnicodeObject")
             structures
            
        *   [`PyUnicode_READY`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READY "PyUnicode_READY")
            
        *   [`PyUnicode_FromKindAndData()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromKindAndData "PyUnicode_FromKindAndData")
            
        *   [`PyUnicode_AsUCS4()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUCS4 "PyUnicode_AsUCS4")
            , [`PyUnicode_AsUCS4Copy()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUCS4Copy "PyUnicode_AsUCS4Copy")
            
        *   [`PyUnicode_DATA`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DATA "PyUnicode_DATA")
            , [`PyUnicode_1BYTE_DATA`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_1BYTE_DATA "PyUnicode_1BYTE_DATA")
            , [`PyUnicode_2BYTE_DATA`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_2BYTE_DATA "PyUnicode_2BYTE_DATA")
            , [`PyUnicode_4BYTE_DATA`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_4BYTE_DATA "PyUnicode_4BYTE_DATA")
            
        *   [`PyUnicode_KIND`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_KIND "PyUnicode_KIND")
             with `PyUnicode_Kind` enum: `PyUnicode_WCHAR_KIND`, [`PyUnicode_1BYTE_KIND`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_1BYTE_KIND "PyUnicode_1BYTE_KIND")
            , [`PyUnicode_2BYTE_KIND`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_2BYTE_KIND "PyUnicode_2BYTE_KIND")
            , [`PyUnicode_4BYTE_KIND`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_4BYTE_KIND "PyUnicode_4BYTE_KIND")
            
        *   [`PyUnicode_READ`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READ "PyUnicode_READ")
            , [`PyUnicode_READ_CHAR`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READ_CHAR "PyUnicode_READ_CHAR")
            , [`PyUnicode_WRITE`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_WRITE "PyUnicode_WRITE")
            
        *   [`PyUnicode_MAX_CHAR_VALUE`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_MAX_CHAR_VALUE "PyUnicode_MAX_CHAR_VALUE")
            
*   [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
     now accepts a [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
     for the `c` format ([bpo-12380](https://bugs.python.org/issue?@action=redirect&bpo=12380)
    ).
    

Deprecated[¶](https://docs.python.org/3/whatsnew/3.3.html#deprecated "Link to this heading")

---------------------------------------------------------------------------------------------

### Unsupported Operating Systems[¶](https://docs.python.org/3/whatsnew/3.3.html#unsupported-operating-systems "Link to this heading")

OS/2 and VMS are no longer supported due to the lack of a maintainer.

Windows 2000 and Windows platforms which set `COMSPEC` to `command.com` are no longer supported due to maintenance burden.

OSF support, which was deprecated in 3.2, has been completely removed.

### Deprecated Python modules, functions and methods[¶](https://docs.python.org/3/whatsnew/3.3.html#deprecated-python-modules-functions-and-methods "Link to this heading")

*   Passing a non-empty string to `object.__format__()` is deprecated, and will produce a [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
     in Python 3.4 ([bpo-9856](https://bugs.python.org/issue?@action=redirect&bpo=9856)
    ).
    
*   The `unicode_internal` codec has been deprecated because of the [**PEP 393**](https://peps.python.org/pep-0393/)
    , use UTF-8, UTF-16 (`utf-16-le` or `utf-16-be`), or UTF-32 (`utf-32-le` or `utf-32-be`)
    
*   [`ftplib.FTP.nlst()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.nlst "ftplib.FTP.nlst")
     and [`ftplib.FTP.dir()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.dir "ftplib.FTP.dir")
    : use [`ftplib.FTP.mlsd()`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP.mlsd "ftplib.FTP.mlsd")
    
*   `platform.popen()`: use the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.")
     module. Check especially the [Replacing Older Functions with the subprocess Module](https://docs.python.org/3/library/subprocess.html#subprocess-replacements)
     section ([bpo-11377](https://bugs.python.org/issue?@action=redirect&bpo=11377)
    ).
    
*   [bpo-13374](https://bugs.python.org/issue?@action=redirect&bpo=13374)
    : The Windows bytes API has been deprecated in the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
     module. Use Unicode filenames, instead of bytes filenames, to not depend on the ANSI code page anymore and to support any filename.
    
*   [bpo-13988](https://bugs.python.org/issue?@action=redirect&bpo=13988)
    : The `xml.etree.cElementTree` module is deprecated. The accelerator is used automatically whenever available.
    
*   The behaviour of `time.clock()` depends on the platform: use the new [`time.perf_counter()`](https://docs.python.org/3/library/time.html#time.perf_counter "time.perf_counter")
     or [`time.process_time()`](https://docs.python.org/3/library/time.html#time.process_time "time.process_time")
     function instead, depending on your requirements, to have a well defined behaviour.
    
*   The `os.stat_float_times()` function is deprecated.
    
*   [`abc`](https://docs.python.org/3/library/abc.html#module-abc "abc: Abstract base classes according to :pep:`3119`.")
     module:
    
    *   [`@abc.abstractproperty`](https://docs.python.org/3/library/abc.html#abc.abstractproperty "abc.abstractproperty")
         has been deprecated, use [`@property`](https://docs.python.org/3/builtins/functions.html#property "property")
         with [`@abc.abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
         instead.
        
    *   [`@abc.abstractclassmethod`](https://docs.python.org/3/library/abc.html#abc.abstractclassmethod "abc.abstractclassmethod")
         has been deprecated, use [`@classmethod`](https://docs.python.org/3/builtins/functions.html#classmethod "classmethod")
         with [`@abc.abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
         instead.
        
    *   [`@abc.abstractstaticmethod`](https://docs.python.org/3/library/abc.html#abc.abstractstaticmethod "abc.abstractstaticmethod")
         has been deprecated, use [`@staticmethod`](https://docs.python.org/3/builtins/functions.html#staticmethod "staticmethod")
         with [`@abc.abstractmethod`](https://docs.python.org/3/library/abc.html#abc.abstractmethod "abc.abstractmethod")
         instead.
        
*   [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
     package:
    
    *   [`importlib.abc.SourceLoader.path_mtime()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.path_mtime "importlib.abc.SourceLoader.path_mtime")
         is now deprecated in favour of [`importlib.abc.SourceLoader.path_stats()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.path_stats "importlib.abc.SourceLoader.path_stats")
         as bytecode files now store both the modification time and size of the source file the bytecode file was compiled from.
        

### Deprecated functions and types of the C API[¶](https://docs.python.org/3/whatsnew/3.3.html#deprecated-functions-and-types-of-the-c-api "Link to this heading")

The [`Py_UNICODE`](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE "Py_UNICODE")
 has been deprecated by [**PEP 393**](https://peps.python.org/pep-0393/)
 and will be removed in Python 4. All functions using this type are deprecated:

Unicode functions and methods using [`Py_UNICODE`](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE "Py_UNICODE")
 and [Py\_UNICODE](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE "Py_UNICODE")
\* types:

*   `PyUnicode_FromUnicode`: use [`PyUnicode_FromWideChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromWideChar "PyUnicode_FromWideChar")
     or [`PyUnicode_FromKindAndData()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromKindAndData "PyUnicode_FromKindAndData")
    
*   `PyUnicode_AS_UNICODE`, `PyUnicode_AsUnicode()`, `PyUnicode_AsUnicodeAndSize()`: use [`PyUnicode_AsWideCharString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsWideCharString "PyUnicode_AsWideCharString")
    
*   `PyUnicode_AS_DATA`: use [`PyUnicode_DATA`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_DATA "PyUnicode_DATA")
     with [`PyUnicode_READ`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_READ "PyUnicode_READ")
     and [`PyUnicode_WRITE`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_WRITE "PyUnicode_WRITE")
    
*   `PyUnicode_GET_SIZE`, `PyUnicode_GetSize()`: use [`PyUnicode_GET_LENGTH`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GET_LENGTH "PyUnicode_GET_LENGTH")
     or [`PyUnicode_GetLength()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetLength "PyUnicode_GetLength")
    
*   `PyUnicode_GET_DATA_SIZE`: use `PyUnicode_GET_LENGTH(str) * PyUnicode_KIND(str)` (only work on ready strings)
    
*   `PyUnicode_AsUnicodeCopy()`: use [`PyUnicode_AsUCS4Copy()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUCS4Copy "PyUnicode_AsUCS4Copy")
     or [`PyUnicode_AsWideCharString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsWideCharString "PyUnicode_AsWideCharString")
    
*   `PyUnicode_GetMax()`
    

Functions and macros manipulating Py\_UNICODE\* strings:

*   `Py_UNICODE_strlen()`: use [`PyUnicode_GetLength()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetLength "PyUnicode_GetLength")
     or [`PyUnicode_GET_LENGTH`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GET_LENGTH "PyUnicode_GET_LENGTH")
    
*   `Py_UNICODE_strcat()`: use [`PyUnicode_CopyCharacters()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CopyCharacters "PyUnicode_CopyCharacters")
     or [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
    
*   `Py_UNICODE_strcpy()`, `Py_UNICODE_strncpy()`, `Py_UNICODE_COPY()`: use [`PyUnicode_CopyCharacters()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CopyCharacters "PyUnicode_CopyCharacters")
     or [`PyUnicode_Substring()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Substring "PyUnicode_Substring")
    
*   `Py_UNICODE_strcmp()`: use [`PyUnicode_Compare()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Compare "PyUnicode_Compare")
    
*   `Py_UNICODE_strncmp()`: use [`PyUnicode_Tailmatch()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Tailmatch "PyUnicode_Tailmatch")
    
*   `Py_UNICODE_strchr()`, `Py_UNICODE_strrchr()`: use [`PyUnicode_FindChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FindChar "PyUnicode_FindChar")
    
*   `Py_UNICODE_FILL()`: use [`PyUnicode_Fill()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Fill "PyUnicode_Fill")
    
*   `Py_UNICODE_MATCH`
    

Encoders:

*   `PyUnicode_Encode()`: use `PyUnicode_AsEncodedObject()`
    
*   `PyUnicode_EncodeUTF7()`
    
*   `PyUnicode_EncodeUTF8()`: use [`PyUnicode_AsUTF8()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8 "PyUnicode_AsUTF8")
     or [`PyUnicode_AsUTF8String()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8String "PyUnicode_AsUTF8String")
    
*   `PyUnicode_EncodeUTF32()`
    
*   `PyUnicode_EncodeUTF16()`
    
*   `PyUnicode_EncodeUnicodeEscape()` use [`PyUnicode_AsUnicodeEscapeString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUnicodeEscapeString "PyUnicode_AsUnicodeEscapeString")
    
*   `PyUnicode_EncodeRawUnicodeEscape()` use [`PyUnicode_AsRawUnicodeEscapeString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsRawUnicodeEscapeString "PyUnicode_AsRawUnicodeEscapeString")
    
*   `PyUnicode_EncodeLatin1()`: use [`PyUnicode_AsLatin1String()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsLatin1String "PyUnicode_AsLatin1String")
    
*   `PyUnicode_EncodeASCII()`: use [`PyUnicode_AsASCIIString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsASCIIString "PyUnicode_AsASCIIString")
    
*   `PyUnicode_EncodeCharmap()`
    
*   `PyUnicode_TranslateCharmap()`
    
*   `PyUnicode_EncodeMBCS()`: use [`PyUnicode_AsMBCSString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsMBCSString "PyUnicode_AsMBCSString")
     or [`PyUnicode_EncodeCodePage()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_EncodeCodePage "PyUnicode_EncodeCodePage")
     (with `CP_ACP` code\_page)
    
*   `PyUnicode_EncodeDecimal()`, `PyUnicode_TransformDecimalToASCII()`
    

### Deprecated features[¶](https://docs.python.org/3/whatsnew/3.3.html#deprecated-features "Link to this heading")

The [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.")
 module’s `'u'` format code is now deprecated and will be removed in Python 4 together with the rest of the ([`Py_UNICODE`](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE "Py_UNICODE")
) API.

Porting to Python 3.3[¶](https://docs.python.org/3/whatsnew/3.3.html#porting-to-python-3-3 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

This section lists previously described changes and other bugfixes that may require changes to your code.

### Porting Python code[¶](https://docs.python.org/3/whatsnew/3.3.html#porting-python-code "Link to this heading")

*   Hash randomization is enabled by default. Set the [`PYTHONHASHSEED`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED)
     environment variable to `0` to disable hash randomization. See also the [`object.__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__")
     method.
    
*   [bpo-12326](https://bugs.python.org/issue?@action=redirect&bpo=12326)
    : On Linux, sys.platform doesn’t contain the major version anymore. It is now always ‘linux’, instead of ‘linux2’ or ‘linux3’ depending on the Linux version used to build Python. Replace sys.platform == ‘linux2’ with sys.platform.startswith(‘linux’), or directly sys.platform == ‘linux’ if you don’t need to support older Python versions.
    
*   [bpo-13847](https://bugs.python.org/issue?@action=redirect&bpo=13847)
    , [bpo-14180](https://bugs.python.org/issue?@action=redirect&bpo=14180)
    : [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.")
     and [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
    : [`OverflowError`](https://docs.python.org/3/builtins/exceptions.html#OverflowError "OverflowError")
     is now raised instead of [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
     if a timestamp is out of range. [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
     is now raised if C functions `gmtime()` or `localtime()` failed.
    
*   The default finders used by import now utilize a cache of what is contained within a specific directory. If you create a Python source file or sourceless bytecode file, make sure to call [`importlib.invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches "importlib.invalidate_caches")
     to clear out the cache for the finders to notice the new file.
    
*   [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
     now uses the full name of the module that was attempted to be imported. Doctests that check ImportErrors’ message will need to be updated to use the full name of the module instead of just the tail of the name.
    
*   The _index_ argument to [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
     now defaults to 0 instead of -1 and no longer support negative values. It was an oversight when [**PEP 328**](https://peps.python.org/pep-0328/)
     was implemented that the default value remained -1. If you need to continue to perform a relative import followed by an absolute import, then perform the relative import using an index of 1, followed by another import using an index of 0. It is preferred, though, that you use [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module")
     rather than call `__import__()` directly.
    
*   [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
     no longer allows one to use an index value other than 0 for top-level modules. E.g. `__import__('sys', level=1)` is now an error.
    
*   Because [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path")
     and [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks")
     now have finders on them by default, you will most likely want to use [`list.insert()`](https://docs.python.org/3/builtins/stdtypes.html#list.insert "list.insert")
     instead of [`list.append()`](https://docs.python.org/3/builtins/stdtypes.html#list.append "list.append")
     to add to those lists.
    
*   Because `None` is now inserted into [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache")
    , if you are clearing out entries in the dictionary of paths that do not have a finder, you will need to remove keys paired with values of `None` **and** `imp.NullImporter` to be backwards-compatible. This will lead to extra overhead on older versions of Python that re-insert `None` into `sys.path_importer_cache` where it represents the use of implicit finders, but semantically it should not change anything.
    
*   `importlib.abc.Finder` no longer specifies a `find_module()` abstract method that must be implemented. If you were relying on subclasses to implement that method, make sure to check for the method’s existence first. You will probably want to check for `find_loader()` first, though, in the case of working with [path entry finders](https://docs.python.org/3/glossary.html#term-path-entry-finder)
    .
    
*   [`pkgutil`](https://docs.python.org/3/library/pkgutil.html#module-pkgutil "pkgutil: Utilities for the import system.")
     has been converted to use [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")
     internally. This eliminates many edge cases where the old behaviour of the [**PEP 302**](https://peps.python.org/pep-0302/)
     import emulation failed to match the behaviour of the real import system. The import emulation itself is still present, but is now deprecated. The [`pkgutil.iter_importers()`](https://docs.python.org/3/library/pkgutil.html#pkgutil.iter_importers "pkgutil.iter_importers")
     and [`pkgutil.walk_packages()`](https://docs.python.org/3/library/pkgutil.html#pkgutil.walk_packages "pkgutil.walk_packages")
     functions special case the standard import hooks so they are still supported even though they do not provide the non-standard `iter_modules()` method.
    
*   A longstanding RFC-compliance bug ([bpo-1079](https://bugs.python.org/issue?@action=redirect&bpo=1079)
    ) in the parsing done by [`email.header.decode_header()`](https://docs.python.org/3/library/email.header.html#email.header.decode_header "email.header.decode_header")
     has been fixed. Code that uses the standard idiom to convert encoded headers into unicode (`str(make_header(decode_header(h))`) will see no change, but code that looks at the individual tuples returned by decode\_header will see that whitespace that precedes or follows `ASCII` sections is now included in the `ASCII` section. Code that builds headers using `make_header` should also continue to work without change, since `make_header` continues to add whitespace between `ASCII` and non-`ASCII` sections if it is not already present in the input strings.
    
*   [`email.utils.formataddr()`](https://docs.python.org/3/library/email.utils.html#email.utils.formataddr "email.utils.formataddr")
     now does the correct content transfer encoding when passed non-`ASCII` display names. Any code that depended on the previous buggy behavior that preserved the non-`ASCII` unicode in the formatted output string will need to be changed ([bpo-1690608](https://bugs.python.org/issue?@action=redirect&bpo=1690608)
    ).
    
*   [`poplib.POP3.quit()`](https://docs.python.org/3/library/poplib.html#poplib.POP3.quit "poplib.POP3.quit")
     may now raise protocol errors like all other `poplib` methods. Code that assumes `quit` does not raise [`poplib.error_proto`](https://docs.python.org/3/library/poplib.html#poplib.error_proto "poplib.error_proto")
     errors may need to be changed if errors on `quit` are encountered by a particular application ([bpo-11291](https://bugs.python.org/issue?@action=redirect&bpo=11291)
    ).
    
*   The `strict` argument to [`email.parser.Parser`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "email.parser.Parser")
    , deprecated since Python 2.4, has finally been removed.
    
*   The deprecated method `unittest.TestCase.assertSameElements` has been removed.
    
*   The deprecated variable `time.accept2dyear` has been removed.
    
*   The deprecated `Context._clamp` attribute has been removed from the [`decimal`](https://docs.python.org/3/library/decimal.html#module-decimal "decimal: Implementation of the General Decimal Arithmetic Specification.")
     module. It was previously replaced by the public attribute [`clamp`](https://docs.python.org/3/library/decimal.html#decimal.Context.clamp "decimal.Context.clamp")
    . (See [bpo-8540](https://bugs.python.org/issue?@action=redirect&bpo=8540)
    .)
    
*   The undocumented internal helper class `SSLFakeFile` has been removed from [`smtplib`](https://docs.python.org/3/library/smtplib.html#module-smtplib "smtplib: SMTP protocol client (requires sockets).")
    , since its functionality has long been provided directly by [`socket.socket.makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile")
    .
    
*   Passing a negative value to [`time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep "time.sleep")
     on Windows now raises an error instead of sleeping forever. It has always raised an error on posix.
    
*   The `ast.__version__` constant has been removed. If you need to make decisions affected by the AST version, use [`sys.version_info`](https://docs.python.org/3/library/sys.html#sys.version_info "sys.version_info")
     to make the decision.
    
*   Code that used to work around the fact that the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
     module used factory functions by subclassing the private classes will need to change to subclass the now-public classes.
    
*   The undocumented debugging machinery in the threading module has been removed, simplifying the code. This should have no effect on production code, but is mentioned here in case any application debug frameworks were interacting with it ([bpo-13550](https://bugs.python.org/issue?@action=redirect&bpo=13550)
    ).
    

### Porting C code[¶](https://docs.python.org/3/whatsnew/3.3.html#porting-c-code "Link to this heading")

*   In the course of changes to the buffer API the undocumented `smalltable` member of the [`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
     structure has been removed and the layout of the `PyMemoryViewObject` has changed.
    
    All extensions relying on the relevant parts in `memoryobject.h` or `object.h` must be rebuilt.
    
*   Due to [PEP 393](https://docs.python.org/3/whatsnew/3.3.html#pep-393)
    , the [`Py_UNICODE`](https://docs.python.org/3/c-api/unicode.html#c.Py_UNICODE "Py_UNICODE")
     type and all functions using this type are deprecated (but will stay available for at least five years). If you were using low-level Unicode APIs to construct and access unicode objects and you want to benefit of the memory footprint reduction provided by [**PEP 393**](https://peps.python.org/pep-0393/)
    , you have to convert your code to the new [Unicode API](https://docs.python.org/3/c-api/unicode.html)
    .
    
    However, if you only have been using high-level functions such as [`PyUnicode_Concat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Concat "PyUnicode_Concat")
    , [`PyUnicode_Join()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Join "PyUnicode_Join")
     or [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")
    , your code will automatically take advantage of the new unicode representations.
    
*   [`PyImport_GetMagicNumber()`](https://docs.python.org/3/c-api/import.html#c.PyImport_GetMagicNumber "PyImport_GetMagicNumber")
     now returns `-1` upon failure.
    
*   As a negative value for the _level_ argument to [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
     is no longer valid, the same now holds for [`PyImport_ImportModuleLevel()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleLevel "PyImport_ImportModuleLevel")
    . This also means that the value of _level_ used by [`PyImport_ImportModuleEx()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleEx "PyImport_ImportModuleEx")
     is now `0` instead of `-1`.
    

### Building C extensions[¶](https://docs.python.org/3/whatsnew/3.3.html#building-c-extensions "Link to this heading")

*   The range of possible file names for C extensions has been narrowed. Very rarely used spellings have been suppressed: under POSIX, files named `xxxmodule.so`, `xxxmodule.abi3.so` and `xxxmodule.cpython-*.so` are no longer recognized as implementing the `xxx` module. If you had been generating such files, you have to switch to the other spellings (i.e., remove the `module` string from the file names).
    
    (implemented in [bpo-14040](https://bugs.python.org/issue?@action=redirect&bpo=14040)
    .)
    

### Command Line Switch Changes[¶](https://docs.python.org/3/whatsnew/3.3.html#command-line-switch-changes "Link to this heading")

*   The -Q command-line flag and related artifacts have been removed. Code checking sys.flags.division\_warning will need updating.
    
    ([bpo-10998](https://bugs.python.org/issue?@action=redirect&bpo=10998)
    , contributed by Éric Araujo.)
    
*   When **python** is started with [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S)
    , `import site` will no longer add site-specific paths to the module search paths. In previous versions, it did.
    
    ([bpo-11591](https://bugs.python.org/issue?@action=redirect&bpo=11591)
    , contributed by Carl Meyer with editions by Éric Araujo.)
    

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [What’s New In Python 3.3](https://docs.python.org/3/whatsnew/3.3.html#)
    *   [Summary – Release highlights](https://docs.python.org/3/whatsnew/3.3.html#summary-release-highlights)
        
    *   [PEP 405: Virtual Environments](https://docs.python.org/3/whatsnew/3.3.html#pep-405-virtual-environments)
        
    *   [PEP 420: Implicit Namespace Packages](https://docs.python.org/3/whatsnew/3.3.html#pep-420-implicit-namespace-packages)
        
    *   [PEP 3118: New memoryview implementation and buffer protocol documentation](https://docs.python.org/3/whatsnew/3.3.html#pep-3118-new-memoryview-implementation-and-buffer-protocol-documentation)
        *   [Features](https://docs.python.org/3/whatsnew/3.3.html#features)
            
        *   [API changes](https://docs.python.org/3/whatsnew/3.3.html#api-changes)
            
    *   [PEP 393: Flexible String Representation](https://docs.python.org/3/whatsnew/3.3.html#pep-393-flexible-string-representation)
        *   [Functionality](https://docs.python.org/3/whatsnew/3.3.html#functionality)
            
        *   [Performance and resource usage](https://docs.python.org/3/whatsnew/3.3.html#performance-and-resource-usage)
            
    *   [PEP 397: Python Launcher for Windows](https://docs.python.org/3/whatsnew/3.3.html#pep-397-python-launcher-for-windows)
        
    *   [PEP 3151: Reworking the OS and IO exception hierarchy](https://docs.python.org/3/whatsnew/3.3.html#pep-3151-reworking-the-os-and-io-exception-hierarchy)
        
    *   [PEP 380: Syntax for Delegating to a Subgenerator](https://docs.python.org/3/whatsnew/3.3.html#pep-380-syntax-for-delegating-to-a-subgenerator)
        
    *   [PEP 409: Suppressing exception context](https://docs.python.org/3/whatsnew/3.3.html#pep-409-suppressing-exception-context)
        
    *   [PEP 414: Explicit Unicode literals](https://docs.python.org/3/whatsnew/3.3.html#pep-414-explicit-unicode-literals)
        
    *   [PEP 3155: Qualified name for classes and functions](https://docs.python.org/3/whatsnew/3.3.html#pep-3155-qualified-name-for-classes-and-functions)
        
    *   [PEP 412: Key-Sharing Dictionary](https://docs.python.org/3/whatsnew/3.3.html#pep-412-key-sharing-dictionary)
        
    *   [PEP 362: Function Signature Object](https://docs.python.org/3/whatsnew/3.3.html#pep-362-function-signature-object)
        
    *   [PEP 421: Adding sys.implementation](https://docs.python.org/3/whatsnew/3.3.html#pep-421-adding-sys-implementation)
        *   [SimpleNamespace](https://docs.python.org/3/whatsnew/3.3.html#simplenamespace)
            
    *   [Using importlib as the Implementation of Import](https://docs.python.org/3/whatsnew/3.3.html#using-importlib-as-the-implementation-of-import)
        *   [New APIs](https://docs.python.org/3/whatsnew/3.3.html#new-apis)
            
        *   [Visible Changes](https://docs.python.org/3/whatsnew/3.3.html#visible-changes)
            
    *   [Other Language Changes](https://docs.python.org/3/whatsnew/3.3.html#other-language-changes)
        
    *   [A Finer-Grained Import Lock](https://docs.python.org/3/whatsnew/3.3.html#a-finer-grained-import-lock)
        
    *   [Builtin functions and types](https://docs.python.org/3/whatsnew/3.3.html#builtin-functions-and-types)
        
    *   [New Modules](https://docs.python.org/3/whatsnew/3.3.html#new-modules)
        *   [faulthandler](https://docs.python.org/3/whatsnew/3.3.html#faulthandler)
            
        *   [ipaddress](https://docs.python.org/3/whatsnew/3.3.html#ipaddress)
            
        *   [lzma](https://docs.python.org/3/whatsnew/3.3.html#lzma)
            
    *   [Improved Modules](https://docs.python.org/3/whatsnew/3.3.html#improved-modules)
        *   [abc](https://docs.python.org/3/whatsnew/3.3.html#abc)
            
        *   [array](https://docs.python.org/3/whatsnew/3.3.html#array)
            
        *   [base64](https://docs.python.org/3/whatsnew/3.3.html#base64)
            
        *   [binascii](https://docs.python.org/3/whatsnew/3.3.html#binascii)
            
        *   [bz2](https://docs.python.org/3/whatsnew/3.3.html#bz2)
            
        *   [codecs](https://docs.python.org/3/whatsnew/3.3.html#codecs)
            
        *   [collections](https://docs.python.org/3/whatsnew/3.3.html#collections)
            
        *   [contextlib](https://docs.python.org/3/whatsnew/3.3.html#contextlib)
            
        *   [crypt](https://docs.python.org/3/whatsnew/3.3.html#crypt)
            
        *   [curses](https://docs.python.org/3/whatsnew/3.3.html#curses)
            
        *   [datetime](https://docs.python.org/3/whatsnew/3.3.html#datetime)
            
        *   [decimal](https://docs.python.org/3/whatsnew/3.3.html#decimal)
            *   [Features](https://docs.python.org/3/whatsnew/3.3.html#id1)
                
            *   [API changes](https://docs.python.org/3/whatsnew/3.3.html#id2)
                
        *   [email](https://docs.python.org/3/whatsnew/3.3.html#email)
            *   [Policy Framework](https://docs.python.org/3/whatsnew/3.3.html#policy-framework)
                
            *   [Provisional Policy with New Header API](https://docs.python.org/3/whatsnew/3.3.html#provisional-policy-with-new-header-api)
                
            *   [Other API Changes](https://docs.python.org/3/whatsnew/3.3.html#other-api-changes)
                
        *   [ftplib](https://docs.python.org/3/whatsnew/3.3.html#ftplib)
            
        *   [functools](https://docs.python.org/3/whatsnew/3.3.html#functools)
            
        *   [gc](https://docs.python.org/3/whatsnew/3.3.html#gc)
            
        *   [hmac](https://docs.python.org/3/whatsnew/3.3.html#hmac)
            
        *   [http](https://docs.python.org/3/whatsnew/3.3.html#http)
            
        *   [html](https://docs.python.org/3/whatsnew/3.3.html#html)
            
        *   [imaplib](https://docs.python.org/3/whatsnew/3.3.html#imaplib)
            
        *   [inspect](https://docs.python.org/3/whatsnew/3.3.html#inspect)
            
        *   [io](https://docs.python.org/3/whatsnew/3.3.html#io)
            
        *   [itertools](https://docs.python.org/3/whatsnew/3.3.html#itertools)
            
        *   [logging](https://docs.python.org/3/whatsnew/3.3.html#logging)
            
        *   [math](https://docs.python.org/3/whatsnew/3.3.html#math)
            
        *   [mmap](https://docs.python.org/3/whatsnew/3.3.html#mmap)
            
        *   [multiprocessing](https://docs.python.org/3/whatsnew/3.3.html#multiprocessing)
            
        *   [nntplib](https://docs.python.org/3/whatsnew/3.3.html#nntplib)
            
        *   [os](https://docs.python.org/3/whatsnew/3.3.html#os)
            
        *   [pdb](https://docs.python.org/3/whatsnew/3.3.html#pdb)
            
        *   [pickle](https://docs.python.org/3/whatsnew/3.3.html#pickle)
            
        *   [pydoc](https://docs.python.org/3/whatsnew/3.3.html#pydoc)
            
        *   [re](https://docs.python.org/3/whatsnew/3.3.html#re)
            
        *   [sched](https://docs.python.org/3/whatsnew/3.3.html#sched)
            
        *   [select](https://docs.python.org/3/whatsnew/3.3.html#select)
            
        *   [shlex](https://docs.python.org/3/whatsnew/3.3.html#shlex)
            
        *   [shutil](https://docs.python.org/3/whatsnew/3.3.html#shutil)
            
        *   [signal](https://docs.python.org/3/whatsnew/3.3.html#signal)
            
        *   [smtpd](https://docs.python.org/3/whatsnew/3.3.html#smtpd)
            
        *   [smtplib](https://docs.python.org/3/whatsnew/3.3.html#smtplib)
            
        *   [socket](https://docs.python.org/3/whatsnew/3.3.html#socket)
            
        *   [socketserver](https://docs.python.org/3/whatsnew/3.3.html#socketserver)
            
        *   [sqlite3](https://docs.python.org/3/whatsnew/3.3.html#sqlite3)
            
        *   [ssl](https://docs.python.org/3/whatsnew/3.3.html#ssl)
            
        *   [stat](https://docs.python.org/3/whatsnew/3.3.html#stat)
            
        *   [struct](https://docs.python.org/3/whatsnew/3.3.html#struct)
            
        *   [subprocess](https://docs.python.org/3/whatsnew/3.3.html#subprocess)
            
        *   [sys](https://docs.python.org/3/whatsnew/3.3.html#sys)
            
        *   [tarfile](https://docs.python.org/3/whatsnew/3.3.html#tarfile)
            
        *   [tempfile](https://docs.python.org/3/whatsnew/3.3.html#tempfile)
            
        *   [textwrap](https://docs.python.org/3/whatsnew/3.3.html#textwrap)
            
        *   [threading](https://docs.python.org/3/whatsnew/3.3.html#threading)
            
        *   [time](https://docs.python.org/3/whatsnew/3.3.html#time)
            
        *   [types](https://docs.python.org/3/whatsnew/3.3.html#types)
            
        *   [unittest](https://docs.python.org/3/whatsnew/3.3.html#unittest)
            
        *   [urllib](https://docs.python.org/3/whatsnew/3.3.html#urllib)
            
        *   [webbrowser](https://docs.python.org/3/whatsnew/3.3.html#webbrowser)
            
        *   [xml.etree.ElementTree](https://docs.python.org/3/whatsnew/3.3.html#xml-etree-elementtree)
            
        *   [zlib](https://docs.python.org/3/whatsnew/3.3.html#zlib)
            
    *   [Optimizations](https://docs.python.org/3/whatsnew/3.3.html#optimizations)
        
    *   [Build and C API Changes](https://docs.python.org/3/whatsnew/3.3.html#build-and-c-api-changes)
        
    *   [Deprecated](https://docs.python.org/3/whatsnew/3.3.html#deprecated)
        *   [Unsupported Operating Systems](https://docs.python.org/3/whatsnew/3.3.html#unsupported-operating-systems)
            
        *   [Deprecated Python modules, functions and methods](https://docs.python.org/3/whatsnew/3.3.html#deprecated-python-modules-functions-and-methods)
            
        *   [Deprecated functions and types of the C API](https://docs.python.org/3/whatsnew/3.3.html#deprecated-functions-and-types-of-the-c-api)
            
        *   [Deprecated features](https://docs.python.org/3/whatsnew/3.3.html#deprecated-features)
            
    *   [Porting to Python 3.3](https://docs.python.org/3/whatsnew/3.3.html#porting-to-python-3-3)
        *   [Porting Python code](https://docs.python.org/3/whatsnew/3.3.html#porting-python-code)
            
        *   [Porting C code](https://docs.python.org/3/whatsnew/3.3.html#porting-c-code)
            
        *   [Building C extensions](https://docs.python.org/3/whatsnew/3.3.html#building-c-extensions)
            
        *   [Command Line Switch Changes](https://docs.python.org/3/whatsnew/3.3.html#command-line-switch-changes)
            

#### Previous topic

[What’s New In Python 3.4](https://docs.python.org/3/whatsnew/3.4.html "previous chapter")

#### Next topic

[What’s New In Python 3.2](https://docs.python.org/3/whatsnew/3.2.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=What%E2%80%99s+New+In+Python+3.3&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fwhatsnew%2F3.3.html&pagesource=whatsnew%2F3.3.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/whatsnew/3.3.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/whatsnew/3.2.html "What’s New In Python 3.2")
     |
*   [previous](https://docs.python.org/3/whatsnew/3.4.html "What’s New In Python 3.4")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [What’s New in Python](https://docs.python.org/3/whatsnew/index.html)
     »
*   [What’s New In Python 3.3](https://docs.python.org/3/whatsnew/3.3.html)
    
*    
    
    |
*   Theme Auto Light Dark |