### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pty.html "pty — Pseudo-terminal utilities")
     |
*   [previous](https://docs.python.org/3/library/termios.html "termios — POSIX style tty control")
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
*   [`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`tty` — Terminal control functions[¶](https://docs.python.org/3/library/tty.html#module-tty "Link to this heading")

====================================================================================================================

**Source code:** [Lib/tty.py](https://github.com/python/cpython/tree/3.15/Lib/tty.py)

* * *

The `tty` module defines functions for putting the tty into cbreak and raw modes.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

Because it requires the [`termios`](https://docs.python.org/3/library/termios.html#module-termios "termios: POSIX style tty control.")
 module, it will work only on Unix.

The `tty` module defines the following functions:

tty.cfmakeraw(_mode_)[¶](https://docs.python.org/3/library/tty.html#tty.cfmakeraw "Link to this definition")

Convert the tty attribute list _mode_, which is a list like the one returned by [`termios.tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr")
, to that of a tty in raw mode.

Added in version 3.12.

tty.cfmakecbreak(_mode_)[¶](https://docs.python.org/3/library/tty.html#tty.cfmakecbreak "Link to this definition")

Convert the tty attribute list _mode_, which is a list like the one returned by [`termios.tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr")
, to that of a tty in cbreak mode.

This clears the `ECHO` and `ICANON` local mode flags in _mode_ as well as setting the minimum input to 1 byte with no delay.

Added in version 3.12.

Changed in version 3.12.2: The `ICRNL` flag is no longer cleared. This matches Linux and macOS `stty cbreak` behavior and what [`setcbreak()`](https://docs.python.org/3/library/tty.html#tty.setcbreak "tty.setcbreak")
 historically did.

tty.setraw(_fd_, _when\=termios.TCSAFLUSH_)[¶](https://docs.python.org/3/library/tty.html#tty.setraw "Link to this definition")

Change the mode of the file descriptor _fd_ to raw. If _when_ is omitted, it defaults to [`termios.TCSAFLUSH`](https://docs.python.org/3/library/termios.html#termios.TCSAFLUSH "termios.TCSAFLUSH")
, and is passed to [`termios.tcsetattr()`](https://docs.python.org/3/library/termios.html#termios.tcsetattr "termios.tcsetattr")
. The return value of [`termios.tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr")
 is saved before setting _fd_ to raw mode; this value is returned.

Changed in version 3.12: The return value is now the original tty attributes, instead of `None`.

tty.setcbreak(_fd_, _when\=termios.TCSAFLUSH_)[¶](https://docs.python.org/3/library/tty.html#tty.setcbreak "Link to this definition")

Change the mode of file descriptor _fd_ to cbreak. If _when_ is omitted, it defaults to [`termios.TCSAFLUSH`](https://docs.python.org/3/library/termios.html#termios.TCSAFLUSH "termios.TCSAFLUSH")
, and is passed to [`termios.tcsetattr()`](https://docs.python.org/3/library/termios.html#termios.tcsetattr "termios.tcsetattr")
. The return value of [`termios.tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr")
 is saved before setting _fd_ to cbreak mode; this value is returned.

This clears the `ECHO` and `ICANON` local mode flags as well as setting the minimum input to 1 byte with no delay.

Changed in version 3.12: The return value is now the original tty attributes, instead of `None`.

Changed in version 3.12.2: The `ICRNL` flag is no longer cleared. This restores the behavior of Python 3.11 and earlier as well as matching what Linux, macOS, & BSDs describe in their `stty(1)` man pages regarding cbreak mode.

See also

Module [`termios`](https://docs.python.org/3/library/termios.html#module-termios "termios: POSIX style tty control.")

Low-level terminal control interface.

#### Previous topic

[`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html "previous chapter")

#### Next topic

[`pty` — Pseudo-terminal utilities](https://docs.python.org/3/library/pty.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tty+%E2%80%94+Terminal+control+functions&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftty.html&pagesource=library%2Ftty.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/tty.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pty.html "pty — Pseudo-terminal utilities")
     |
*   [previous](https://docs.python.org/3/library/termios.html "termios — POSIX style tty control")
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
*   [`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html)
    
*    
    
    |
*   Theme Auto Light Dark |