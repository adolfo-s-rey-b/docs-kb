### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/termios.html "termios — POSIX style tty control")
     |
*   [previous](https://docs.python.org/3/library/pwd.html "pwd — The password database")
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
*   [`grp` — The group database](https://docs.python.org/3/library/grp.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`grp` — The group database[¶](https://docs.python.org/3/library/grp.html#module-grp "Link to this heading")

============================================================================================================

* * *

This module provides access to the Unix group database. It is available on all Unix versions.

[Availability](https://docs.python.org/3/library/intro.html#availability)
: Unix, not WASI, not Android, not iOS.

Group database entries are reported as a tuple-like object, whose attributes correspond to the members of the `group` structure (Attribute field below, see `<grp.h>`):

| Index | Attribute | Meaning |
| --- | --- | --- |
| 0   | gr\_name | the name of the group |
| 1   | gr\_passwd | the (encrypted) group password; often empty |
| 2   | gr\_gid | the numerical group ID |
| 3   | gr\_mem | all the group member’s user names |

The gid is an integer, name and password are strings, and the member list is a list of strings. (Note that most users are not explicitly listed as members of the group they are in according to the password database. Check both databases to get complete membership information. Also note that a `gr_name` that starts with a `+` or `-` is likely to be a YP/NIS reference and may not be accessible via [`getgrnam()`](https://docs.python.org/3/library/grp.html#grp.getgrnam "grp.getgrnam")
 or [`getgrgid()`](https://docs.python.org/3/library/grp.html#grp.getgrgid "grp.getgrgid")
.)

It defines the following items:

grp.getgrgid(_id_)[¶](https://docs.python.org/3/library/grp.html#grp.getgrgid "Link to this definition")

Return the group database entry for the given numeric group ID. [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is raised if the entry asked for cannot be found.

Changed in version 3.10: [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised for non-integer arguments like floats or strings.

grp.getgrnam(_name_)[¶](https://docs.python.org/3/library/grp.html#grp.getgrnam "Link to this definition")

Return the group database entry for the given group name. [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
 is raised if the entry asked for cannot be found.

grp.getgrall()[¶](https://docs.python.org/3/library/grp.html#grp.getgrall "Link to this definition")

Return a list of all available group entries, in arbitrary order.

See also

Module [`pwd`](https://docs.python.org/3/library/pwd.html#module-pwd "pwd: The password database (getpwnam() and friends).")

An interface to the user database, similar to this.

#### Previous topic

[`pwd` — The password database](https://docs.python.org/3/library/pwd.html "previous chapter")

#### Next topic

[`termios` — POSIX style tty control](https://docs.python.org/3/library/termios.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=grp+%E2%80%94+The+group+database&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fgrp.html&pagesource=library%2Fgrp.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/grp.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/termios.html "termios — POSIX style tty control")
     |
*   [previous](https://docs.python.org/3/library/pwd.html "pwd — The password database")
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
*   [`grp` — The group database](https://docs.python.org/3/library/grp.html)
    
*    
    
    |
*   Theme Auto Light Dark |