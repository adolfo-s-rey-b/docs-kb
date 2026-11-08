### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/fileinput.html "fileinput — Iterate over lines from multiple input streams")
     |
*   [previous](https://docs.python.org/3/library/optparse.html "optparse — Parser for command line options")
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
*   [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html)
     »
*   [`getpass` — Portable password input](https://docs.python.org/3/library/getpass.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`getpass` — Portable password input[¶](https://docs.python.org/3/library/getpass.html#module-getpass "Link to this heading")

=============================================================================================================================

**Source code:** [Lib/getpass.py](https://github.com/python/cpython/tree/3.15/Lib/getpass.py)

* * *

[Availability](https://docs.python.org/3/library/intro.html#availability)
: not WASI.

This module does not work or is not available on WebAssembly. See [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability)
 for more information.

The `getpass` module provides two functions:

getpass.getpass(_prompt\='Password: '_, _stream\=None_, _\*_, _echo\_char\=None_)[¶](https://docs.python.org/3/library/getpass.html#getpass.getpass "Link to this definition")

Prompt the user for a password without echoing. The user is prompted using the string _prompt_, which defaults to `'Password: '`. On Unix, the prompt is written to the file-like object _stream_ using the replace error handler if needed. _stream_ defaults to the controlling terminal (`/dev/tty`) or if that is unavailable to `sys.stderr` (this argument is ignored on Windows).

The _echo\_char_ argument controls how user input is displayed while typing. If _echo\_char_ is `None` (default), input remains hidden. Otherwise, _echo\_char_ must be a single printable ASCII character and each typed character is replaced by it. For example, `echo_char='*'` will display asterisks instead of the actual input.

If echo-free input is unavailable, `getpass()` falls back to printing a warning message to _stream_ and reading from [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin")
 and issuing a [`GetPassWarning`](https://docs.python.org/3/library/getpass.html#getpass.GetPassWarning "getpass.GetPassWarning")
.

Note

If you call `getpass()` from within IDLE, the input may be done in the terminal you launched IDLE from rather than the idle window itself.

Note

On Unix systems, when _echo\_char_ is set, the terminal will be configured to operate in _[noncanonical mode](https://manpages.debian.org/termios(3)#Canonical_and_noncanonical_mode)
_. Common terminal control characters are supported:

*   Ctrl+A - Move cursor to beginning of line
    
*   Ctrl+E - Move cursor to end of line
    
*   Ctrl+K - Kill (delete) from cursor to end of line
    
*   Ctrl+U - Kill (delete) entire line
    
*   Ctrl+W - Erase previous word
    
*   Ctrl+V - Insert next character literally (quote)
    
*   Backspace/DEL - Delete character before cursor
    

These shortcuts work by reading the terminal’s configured control character mappings from termios settings.

Changed in version 3.14: Added the _echo\_char_ parameter for keyboard feedback.

Changed in version 3.15: When using non-empty _echo\_char_ on Unix, keyboard shortcuts (including cursor movement and line editing) are now properly handled using the terminal’s control character configuration.

exception getpass.GetPassWarning[¶](https://docs.python.org/3/library/getpass.html#getpass.GetPassWarning "Link to this definition")

A [`UserWarning`](https://docs.python.org/3/builtins/exceptions.html#UserWarning "UserWarning")
 subclass issued when password input may be echoed.

getpass.getuser()[¶](https://docs.python.org/3/library/getpass.html#getpass.getuser "Link to this definition")

Return the “login name” of the user.

This function checks the environment variables `LOGNAME`, `USER`, `LNAME` and `USERNAME`, in order, and returns the value of the first one which is set to a non-empty string. If none are set, the login name from the password database is returned on systems which support the [`pwd`](https://docs.python.org/3/library/pwd.html#module-pwd "pwd: The password database (getpwnam() and friends).")
 module, otherwise, an [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 is raised.

In general, this function should be preferred over [`os.getlogin()`](https://docs.python.org/3/library/os.html#os.getlogin "os.getlogin")
.

Changed in version 3.13: Previously, various exceptions beyond just [`OSError`](https://docs.python.org/3/builtins/exceptions.html#OSError "OSError")
 were raised.

#### Previous topic

[`optparse` — Parser for command line options](https://docs.python.org/3/library/optparse.html "previous chapter")

#### Next topic

[`fileinput` — Iterate over lines from multiple input streams](https://docs.python.org/3/library/fileinput.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=getpass+%E2%80%94+Portable+password+input&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgetpass.html&pagesource=library%2Fgetpass.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/getpass.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/fileinput.html "fileinput — Iterate over lines from multiple input streams")
     |
*   [previous](https://docs.python.org/3/library/optparse.html "optparse — Parser for command line options")
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
*   [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html)
     »
*   [`getpass` — Portable password input](https://docs.python.org/3/library/getpass.html)
    
*    
    
    |
*   Theme Auto Light Dark |