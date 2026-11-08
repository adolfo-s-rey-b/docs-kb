### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pwd.html "pwd — The password database")
     |
*   [previous](https://docs.python.org/3/library/shlex.html "shlex — Simple lexical analysis")
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
*   [`posix` — The most common POSIX system calls](https://docs.python.org/3/library/posix.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`posix` — The most common POSIX system calls[¶](https://docs.python.org/3/library/posix.html#module-posix "Link to this heading")

==================================================================================================================================

* * *

This module provides access to operating system functionality that is standardized by the C Standard and the POSIX standard (a thinly disguised Unix interface).

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

**Do not import this module directly.** Instead, import the module [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
, which provides a _portable_ version of this interface. On Unix, the `os` module provides a superset of the `posix` interface. On non-Unix operating systems the `posix` module is not available, but a subset is always available through the `os` interface. Once `os` is imported, there is _no_ performance penalty in using it instead of `posix`. In addition, `os` provides some additional functionality, such as automatically calling [`putenv()`](https://docs.python.org/3/library/os.html#os.putenv "os.putenv")
 when an entry in `os.environ` is changed.

Errors are reported as exceptions; the usual exceptions are given for type errors, while errors reported by the system calls raise [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
.

Large File Support[¶](https://docs.python.org/3/library/posix.html#large-file-support "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Several operating systems (including AIX and Solaris) provide support for files that are larger than 2 GiB from a C programming model where int and long are 32-bit values. This is typically accomplished by defining the relevant size and offset types as 64-bit values. Such files are sometimes referred to as _large files_.

Large file support is enabled in Python when the size of an `off_t` is larger than a long and the long long is at least as large as an `off_t`. It may be necessary to configure and compile Python with certain compiler flags to enable this mode. For example, with Solaris 2.6 and 2.7 you need to do something like:

Copy

CFLAGS\="\`getconf LFS\_CFLAGS\`" OPT\="-g -O2 $CFLAGS" \\
        ./configure

On large-file-capable Linux systems, this might work:

Copy

CFLAGS\='-D\_LARGEFILE64\_SOURCE -D\_FILE\_OFFSET\_BITS=64' OPT\="-g -O2 $CFLAGS" \\
        ./configure

Notable Module Contents[¶](https://docs.python.org/3/library/posix.html#notable-module-contents "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

In addition to many functions described in the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
 module documentation, `posix` defines the following data item:

posix.environ[¶](https://docs.python.org/3/library/posix.html#posix.environ "Link to this definition")

A dictionary representing the string environment at the time the interpreter was started. Keys and values are bytes on Unix and str on Windows. For example, `environ[b'HOME']` (`environ['HOME']` on Windows) is the pathname of your home directory, equivalent to `getenv("HOME")` in C.

Modifying this dictionary does not affect the string environment passed on by [`execv()`](https://docs.python.org/3/library/os.html#os.execv "os.execv")
, [`popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen")
 or [`system()`](https://docs.python.org/3/library/os.html#os.system "os.system")
; if you need to change the environment, pass `environ` to [`execve()`](https://docs.python.org/3/library/os.html#os.execve "os.execve")
 or add variable assignments and export statements to the command string for `system()` or `popen()`.

Changed in version 3.2: On Unix, keys and values are bytes.

Note

The [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.")
 module provides an alternate implementation of `environ` which updates the environment on modification. Note also that updating [`os.environ`](https://docs.python.org/3/library/os.html#os.environ "os.environ")
 will render this dictionary obsolete. Use of the `os` module version of this is recommended over direct access to the `posix` module.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`posix` — The most common POSIX system calls](https://docs.python.org/3/library/posix.html#)
    *   [Large File Support](https://docs.python.org/3/library/posix.html#large-file-support)
        
    *   [Notable Module Contents](https://docs.python.org/3/library/posix.html#notable-module-contents)
        

#### Previous topic

[`shlex` — Simple lexical analysis](https://docs.python.org/3/library/shlex.html "previous chapter")

#### Next topic

[`pwd` — The password database](https://docs.python.org/3/library/pwd.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=posix+%E2%80%94+The+most+common+POSIX+system+calls&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fposix.html&pagesource=library%2Fposix.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/posix.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pwd.html "pwd — The password database")
     |
*   [previous](https://docs.python.org/3/library/shlex.html "shlex — Simple lexical analysis")
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
*   [`posix` — The most common POSIX system calls](https://docs.python.org/3/library/posix.html)
    
*    
    
    |
*   Theme Auto Light Dark |