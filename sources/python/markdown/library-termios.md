### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tty.html "tty — Terminal control functions")
     |
*   [previous](https://docs.python.org/3/library/grp.html "grp — The group database")
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
*   [`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`termios` — POSIX style tty control[¶](https://docs.python.org/3/library/termios.html#module-termios "Link to this heading")

=============================================================================================================================

* * *

This module provides an interface to the POSIX calls for tty I/O control. For a complete description of these calls, see _[termios(3)](https://manpages.debian.org/termios(3))
_ Unix manual page. It is only available for those Unix versions that support POSIX _termios_ style tty I/O control configured during installation.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix.

All functions in this module take a file descriptor _fd_ as their first argument. This can be an integer file descriptor, such as returned by `sys.stdin.fileno()`, or a [file object](https://docs.python.org/3/glossary.html#term-file-object)
, such as `sys.stdin` itself.

This module also defines all the constants needed to work with the functions provided here; these have the same name as their counterparts in C. Please refer to your system documentation for more information on using these terminal control interfaces.

The module defines the following functions:

termios.tcgetattr(_fd_)[¶](https://docs.python.org/3/library/termios.html#termios.tcgetattr "Link to this definition")

Return a list containing the tty attributes for file descriptor _fd_, as follows: `[iflag, oflag, cflag, lflag, ispeed, ospeed, cc]` where _cc_ is a list of the tty special characters (each a string of length 1, except the items with indices [`VMIN`](https://docs.python.org/3/library/termios.html#termios.VMIN "termios.VMIN")
 and [`VTIME`](https://docs.python.org/3/library/termios.html#termios.VTIME "termios.VTIME")
, which are integers when these fields are defined). The interpretation of the flags and the speeds as well as the indexing in the _cc_ array must be done using the symbolic constants defined in the `termios` module.

termios.VMIN[¶](https://docs.python.org/3/library/termios.html#termios.VMIN "Link to this definition")

termios.VTIME[¶](https://docs.python.org/3/library/termios.html#termios.VTIME "Link to this definition")

Indices into the _cc_ array controlling a non-canonical read: the minimum number of characters to read and the timeout in tenths of a second, respectively.

termios.tcsetattr(_fd_, _when_, _attributes_)[¶](https://docs.python.org/3/library/termios.html#termios.tcsetattr "Link to this definition")

Set the tty attributes for file descriptor _fd_ from the _attributes_, which is a list like the one returned by [`tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr")
. The _when_ argument determines when the attributes are changed:

termios.TCSANOW[¶](https://docs.python.org/3/library/termios.html#termios.TCSANOW "Link to this definition")

Change attributes immediately.

termios.TCSADRAIN[¶](https://docs.python.org/3/library/termios.html#termios.TCSADRAIN "Link to this definition")

Change attributes after transmitting all queued output.

termios.TCSAFLUSH[¶](https://docs.python.org/3/library/termios.html#termios.TCSAFLUSH "Link to this definition")

Change attributes after transmitting all queued output and discarding all queued input.

termios.tcsendbreak(_fd_, _duration_)[¶](https://docs.python.org/3/library/termios.html#termios.tcsendbreak "Link to this definition")

Send a break on file descriptor _fd_. A zero _duration_ sends a break for 0.25–0.5 seconds; a nonzero _duration_ has a system dependent meaning.

termios.tcdrain(_fd_)[¶](https://docs.python.org/3/library/termios.html#termios.tcdrain "Link to this definition")

Wait until all output written to file descriptor _fd_ has been transmitted.

termios.tcflush(_fd_, _queue_)[¶](https://docs.python.org/3/library/termios.html#termios.tcflush "Link to this definition")

Discard queued data on file descriptor _fd_. The _queue_ selector specifies which queue: [`TCIFLUSH`](https://docs.python.org/3/library/termios.html#termios.TCIFLUSH "termios.TCIFLUSH")
 for the input queue, [`TCOFLUSH`](https://docs.python.org/3/library/termios.html#termios.TCOFLUSH "termios.TCOFLUSH")
 for the output queue, or [`TCIOFLUSH`](https://docs.python.org/3/library/termios.html#termios.TCIOFLUSH "termios.TCIOFLUSH")
 for both queues.

termios.TCIFLUSH[¶](https://docs.python.org/3/library/termios.html#termios.TCIFLUSH "Link to this definition")

termios.TCOFLUSH[¶](https://docs.python.org/3/library/termios.html#termios.TCOFLUSH "Link to this definition")

termios.TCIOFLUSH[¶](https://docs.python.org/3/library/termios.html#termios.TCIOFLUSH "Link to this definition")

Values for the _queue_ selector: the input queue, the output queue, or both queues, respectively.

termios.tcflow(_fd_, _action_)[¶](https://docs.python.org/3/library/termios.html#termios.tcflow "Link to this definition")

Suspend or resume input or output on file descriptor _fd_. The _action_ argument can be [`TCOOFF`](https://docs.python.org/3/library/termios.html#termios.TCOOFF "termios.TCOOFF")
 to suspend output, [`TCOON`](https://docs.python.org/3/library/termios.html#termios.TCOON "termios.TCOON")
 to restart output, [`TCIOFF`](https://docs.python.org/3/library/termios.html#termios.TCIOFF "termios.TCIOFF")
 to suspend input, or [`TCION`](https://docs.python.org/3/library/termios.html#termios.TCION "termios.TCION")
 to restart input.

termios.TCOOFF[¶](https://docs.python.org/3/library/termios.html#termios.TCOOFF "Link to this definition")

termios.TCOON[¶](https://docs.python.org/3/library/termios.html#termios.TCOON "Link to this definition")

termios.TCIOFF[¶](https://docs.python.org/3/library/termios.html#termios.TCIOFF "Link to this definition")

termios.TCION[¶](https://docs.python.org/3/library/termios.html#termios.TCION "Link to this definition")

Values for the _action_ argument: suspend output, restart output, suspend input, or restart input, respectively.

termios.tcgetwinsize(_fd_)[¶](https://docs.python.org/3/library/termios.html#termios.tcgetwinsize "Link to this definition")

Return a tuple `(ws_row, ws_col)` containing the tty window size for file descriptor _fd_. Requires [`termios.TIOCGWINSZ`](https://docs.python.org/3/library/termios.html#termios.TIOCGWINSZ "termios.TIOCGWINSZ")
 or [`termios.TIOCGSIZE`](https://docs.python.org/3/library/termios.html#termios.TIOCGSIZE "termios.TIOCGSIZE")
.

Added in version 3.11.

termios.TIOCGWINSZ[¶](https://docs.python.org/3/library/termios.html#termios.TIOCGWINSZ "Link to this definition")

termios.TIOCGSIZE[¶](https://docs.python.org/3/library/termios.html#termios.TIOCGSIZE "Link to this definition")

`ioctl()` requests for querying the tty window size. Not defined on all platforms; `tcgetwinsize()` requires at least one of them.

termios.tcsetwinsize(_fd_, _winsize_)[¶](https://docs.python.org/3/library/termios.html#termios.tcsetwinsize "Link to this definition")

Set the tty window size for file descriptor _fd_ from _winsize_, which is a two-item tuple `(ws_row, ws_col)` like the one returned by [`tcgetwinsize()`](https://docs.python.org/3/library/termios.html#termios.tcgetwinsize "termios.tcgetwinsize")
. Requires at least one of the pairs ([`termios.TIOCGWINSZ`](https://docs.python.org/3/library/termios.html#termios.TIOCGWINSZ "termios.TIOCGWINSZ")
, [`termios.TIOCSWINSZ`](https://docs.python.org/3/library/termios.html#termios.TIOCSWINSZ "termios.TIOCSWINSZ")
); ([`termios.TIOCGSIZE`](https://docs.python.org/3/library/termios.html#termios.TIOCGSIZE "termios.TIOCGSIZE")
, [`termios.TIOCSSIZE`](https://docs.python.org/3/library/termios.html#termios.TIOCSSIZE "termios.TIOCSSIZE")
) to be defined.

Added in version 3.11.

termios.TIOCSWINSZ[¶](https://docs.python.org/3/library/termios.html#termios.TIOCSWINSZ "Link to this definition")

termios.TIOCSSIZE[¶](https://docs.python.org/3/library/termios.html#termios.TIOCSSIZE "Link to this definition")

`ioctl()` requests for setting the tty window size. Not defined on all platforms; see `tcsetwinsize()` for the required pairs.

See also

Module [`tty`](https://docs.python.org/3/library/tty.html#module-tty "tty: Utility functions that perform common terminal control operations.")

Convenience functions for common terminal control operations.

Example[¶](https://docs.python.org/3/library/termios.html#example "Link to this heading")

------------------------------------------------------------------------------------------

Here’s a function that prompts for a password with echoing turned off. Note the technique using a separate [`tcgetattr()`](https://docs.python.org/3/library/termios.html#termios.tcgetattr "termios.tcgetattr")
 call and a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
 … [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally)
 statement to ensure that the old tty attributes are restored exactly no matter what happens:

Copy

def getpass(prompt\="Password: "):
    import termios, sys
    fd \= sys.stdin.fileno()
    old \= termios.tcgetattr(fd)
    new \= termios.tcgetattr(fd)
    new\[3\] \= new\[3\] & ~termios.ECHO          \# lflags
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd \= input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return passwd

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html#)
    *   [Example](https://docs.python.org/3/library/termios.html#example)
        

#### Previous topic

[`grp` — The group database](https://docs.python.org/3/library/grp.html "previous chapter")

#### Next topic

[`tty` — Terminal control functions](https://docs.python.org/3/library/tty.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=termios+%E2%80%94+POSIX+style+tty+control&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftermios.html&pagesource=library%2Ftermios.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/termios.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tty.html "tty — Terminal control functions")
     |
*   [previous](https://docs.python.org/3/library/grp.html "grp — The group database")
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
*   [`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html)
    
*    
    
    |
*   Theme Auto Light Dark |