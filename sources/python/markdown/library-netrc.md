### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/plistlib.html "plistlib — Generate and parse Apple .plist files")
     |
*   [previous](https://docs.python.org/3/library/tomllib.html "tomllib — Parse TOML files")
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
*   [File Formats](https://docs.python.org/3/library/fileformats.html)
     »
*   [`netrc` — netrc file processing](https://docs.python.org/3/library/netrc.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`netrc` — netrc file processing[¶](https://docs.python.org/3/library/netrc.html#module-netrc "Link to this heading")

=====================================================================================================================

**Source code:** [Lib/netrc.py](https://github.com/python/cpython/tree/3.15/Lib/netrc.py)

* * *

The [`netrc`](https://docs.python.org/3/library/netrc.html#netrc.netrc "netrc.netrc")
 class parses and encapsulates the netrc file format used by the Unix **ftp** program and other FTP clients.

class netrc.netrc(\[_file_\])[¶](https://docs.python.org/3/library/netrc.html#netrc.netrc "Link to this definition")

A `netrc` instance or subclass instance encapsulates data from a netrc file. The initialization argument, if present, specifies the file to parse. If no argument is given, the file `.netrc` in the user’s home directory – as determined by [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser")
 – will be read. Otherwise, a [`FileNotFoundError`](https://docs.python.org/3/builtins/exceptions.html#FileNotFoundError "FileNotFoundError")
 exception will be raised. Parse errors will raise [`NetrcParseError`](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError "netrc.NetrcParseError")
 with diagnostic information including the file name, line number, and terminating token.

If no argument is specified on a POSIX system, the presence of passwords in the `.netrc` file will raise a [`NetrcParseError`](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError "netrc.NetrcParseError")
 if the file ownership or permissions are insecure (owned by a user other than the user running the process, or accessible for read or write by any other user). This implements security behavior equivalent to that of ftp and other programs that use `.netrc`. Such security checks are not available on platforms that do not support [`os.getuid()`](https://docs.python.org/3/library/os.html#os.getuid "os.getuid")
.

Changed in version 3.4: Added the POSIX permission check.

Changed in version 3.7: [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser "os.path.expanduser")
 is used to find the location of the `.netrc` file when _file_ is not passed as argument.

Changed in version 3.10: `netrc` try UTF-8 encoding before using locale specific encoding. The entry in the netrc file no longer needs to contain all tokens. The missing tokens’ value default to an empty string. All the tokens and their values now can contain arbitrary characters, like whitespace and non-ASCII characters. If the login name is anonymous, it won’t trigger the security check.

exception netrc.NetrcParseError[¶](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError "Link to this definition")

Exception raised by the [`netrc`](https://docs.python.org/3/library/netrc.html#netrc.netrc "netrc.netrc")
 class when syntactical errors are encountered in source text. Instances of this exception provide three interesting attributes:

msg[¶](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError.msg "Link to this definition")

Textual explanation of the error.

filename[¶](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError.filename "Link to this definition")

The name of the source file.

lineno[¶](https://docs.python.org/3/library/netrc.html#netrc.NetrcParseError.lineno "Link to this definition")

The line number on which the error was found.

netrc Objects[¶](https://docs.python.org/3/library/netrc.html#netrc-objects "Link to this heading")

----------------------------------------------------------------------------------------------------

A [`netrc`](https://docs.python.org/3/library/netrc.html#netrc.netrc "netrc.netrc")
 instance has the following methods:

netrc.authenticators(_host_)[¶](https://docs.python.org/3/library/netrc.html#netrc.netrc.authenticators "Link to this definition")

Return a 3-tuple `(login, account, password)` of authenticators for _host_. If the netrc file did not contain an entry for the given host, return the tuple associated with the ‘default’ entry. If neither matching host nor default entry is available, return `None`.

netrc.\_\_repr\_\_()[¶](https://docs.python.org/3/library/netrc.html#netrc.netrc.__repr__ "Link to this definition")

Dump the class data as a string in the format of a netrc file. (This discards comments and may reorder the entries.)

Instances of [`netrc`](https://docs.python.org/3/library/netrc.html#netrc.netrc "netrc.netrc")
 have public instance variables:

netrc.hosts[¶](https://docs.python.org/3/library/netrc.html#netrc.netrc.hosts "Link to this definition")

Dictionary mapping host names to `(login, account, password)` tuples. The ‘default’ entry, if any, is represented as a pseudo-host by that name.

netrc.macros[¶](https://docs.python.org/3/library/netrc.html#netrc.netrc.macros "Link to this definition")

Dictionary mapping macro names to string lists.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`netrc` — netrc file processing](https://docs.python.org/3/library/netrc.html#)
    *   [netrc Objects](https://docs.python.org/3/library/netrc.html#netrc-objects)
        

#### Previous topic

[`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html "previous chapter")

#### Next topic

[`plistlib` — Generate and parse Apple `.plist` files](https://docs.python.org/3/library/plistlib.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=netrc+%E2%80%94+netrc+file+processing&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fnetrc.html&pagesource=library%2Fnetrc.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/netrc.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/plistlib.html "plistlib — Generate and parse Apple .plist files")
     |
*   [previous](https://docs.python.org/3/library/tomllib.html "tomllib — Parse TOML files")
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
*   [File Formats](https://docs.python.org/3/library/fileformats.html)
     »
*   [`netrc` — netrc file processing](https://docs.python.org/3/library/netrc.html)
    
*    
    
    |
*   Theme Auto Light Dark |