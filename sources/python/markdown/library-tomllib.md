### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/netrc.html "netrc — netrc file processing")
     |
*   [previous](https://docs.python.org/3/library/configparser.html "configparser — Configuration file parser")
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
*   [`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`tomllib` — Parse TOML files[¶](https://docs.python.org/3/library/tomllib.html#module-tomllib "Link to this heading")

======================================================================================================================

**Source code:** [Lib/tomllib](https://github.com/python/cpython/tree/3.15/Lib/tomllib)

* * *

This module provides an interface for parsing TOML 1.1.0 (Tom’s Obvious Minimal Language, [https://toml.io](https://toml.io/en/)
). This module does not support writing TOML.

Added in version 3.11: The module was added with support for TOML 1.0.0.

Changed in version 3.15: Added TOML 1.1.0 support. See the [What’s New](https://docs.python.org/3/whatsnew/3.15.html#whatsnew315-tomllib-1-1-0)
 for details.

Warning

Be cautious when parsing data from untrusted sources. A malicious TOML string may cause the decoder to consume considerable CPU and memory resources. Limiting the size of data to be parsed is recommended.

See also

The [Tomli-W package](https://pypi.org/project/tomli-w/)
 is a TOML writer that can be used in conjunction with this module, providing a write API familiar to users of the standard library [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).")
 and [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
 modules.

See also

The [TOML Kit package](https://pypi.org/project/tomlkit/)
 is a style-preserving TOML library with both read and write capability. It is a recommended replacement for this module for editing already existing TOML files.

This module defines the following functions:

tomllib.load(_fp_, _/_, _\*_, _parse\_float\=float_)[¶](https://docs.python.org/3/library/tomllib.html#tomllib.load "Link to this definition")

Read a TOML file. The first argument should be a readable and binary file object. Return a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
. Convert TOML types to Python using this [conversion table](https://docs.python.org/3/library/tomllib.html#toml-to-py-table)
.

_parse\_float_ will be called with the string of every TOML float to be decoded. By default, this is equivalent to `float(num_str)`. This can be used to use another datatype or parser for TOML floats (e.g. [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")
). The callable must not return a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
 or a [`list`](https://docs.python.org/3/builtins/stdtypes.html#list "list")
, else a [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised.

A [`TOMLDecodeError`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError "tomllib.TOMLDecodeError")
 will be raised on an invalid TOML document.

tomllib.loads(_s_, _/_, _\*_, _parse\_float\=float_)[¶](https://docs.python.org/3/library/tomllib.html#tomllib.loads "Link to this definition")

Load TOML from a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object. Return a [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
. Convert TOML types to Python using this [conversion table](https://docs.python.org/3/library/tomllib.html#toml-to-py-table)
. The _parse\_float_ argument has the same meaning as in [`load()`](https://docs.python.org/3/library/tomllib.html#tomllib.load "tomllib.load")
.

A [`TOMLDecodeError`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError "tomllib.TOMLDecodeError")
 will be raised on an invalid TOML document.

The following exceptions are available:

exception tomllib.TOMLDecodeError(_msg_, _doc_, _pos_)[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError "Link to this definition")

Subclass of [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 with the following additional attributes:

msg[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.msg "Link to this definition")

The unformatted error message.

doc[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.doc "Link to this definition")

The TOML document being parsed.

pos[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.pos "Link to this definition")

The index of _doc_ where parsing failed.

lineno[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.lineno "Link to this definition")

The line corresponding to _pos_.

colno[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.colno "Link to this definition")

The column corresponding to _pos_.

Changed in version 3.14: Added the _msg_, _doc_ and _pos_ parameters. Added the [`msg`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.msg "tomllib.TOMLDecodeError.msg")
, [`doc`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.doc "tomllib.TOMLDecodeError.doc")
, [`pos`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.pos "tomllib.TOMLDecodeError.pos")
, [`lineno`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.lineno "tomllib.TOMLDecodeError.lineno")
 and [`colno`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.colno "tomllib.TOMLDecodeError.colno")
 attributes.

Deprecated since version 3.14: Passing free-form positional arguments is deprecated.

Examples[¶](https://docs.python.org/3/library/tomllib.html#examples "Link to this heading")

--------------------------------------------------------------------------------------------

Parsing a TOML file:

Copy

import tomllib

with open("pyproject.toml", "rb") as f:
    data \= tomllib.load(f)

Parsing a TOML string:

Copy

import tomllib

toml\_str \= """
python-version = "3.11.0"
python-implementation = "CPython"
"""

data \= tomllib.loads(toml\_str)

Conversion Table[¶](https://docs.python.org/3/library/tomllib.html#conversion-table "Link to this heading")

------------------------------------------------------------------------------------------------------------

| TOML | Python |
| --- | --- |
| TOML document | dict |
| string | str |
| integer | int |
| float | float (configurable with _parse\_float_) |
| boolean | bool |
| offset date-time | datetime.datetime (`tzinfo` attribute set to an instance of `datetime.timezone`) |
| local date-time | datetime.datetime (`tzinfo` attribute set to `None`) |
| local date | datetime.date |
| local time | datetime.time |
| array | list |
| table | dict |
| inline table | dict |
| array of tables | list of dicts |

Limits and interoperability considerations[¶](https://docs.python.org/3/library/tomllib.html#limits-and-interoperability-considerations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

`tomllib` places some limits on the documents it can handle, and it preserves details that other TOML parsers are allowed to ignore. When writing portable TOML files, only use features that are guaranteed or recommended by the standard.

The implementation details listed here may change in future versions of Python.

Tables/dicts

The TOML spec does not guarantee key/value pairs in TOML documents and tables to be in any specific order.

**CPython implementation detail:** `tomllib` loads dictionary entries in the order they appear in the source.

Integers

TOML recommends supporting integers in `range(-2**63, 2**63)`.

**CPython implementation detail:** `tomllib` uses [Python’s limit on integer string conversion](https://docs.python.org/3/builtins/stdtypes.html#int-max-str-digits)
 (4300 digits by default).

Floats

TOML recommends supporting at least IEEE 754 binary64 values, which means that numbers with more than 15 significant decimal digits are likely to be rounded.

**CPython implementation detail:** `tomllib` uses Python [`float`](https://docs.python.org/3/builtins/functions.html#float "float")
 by default; on many common platforms this is the recommended binary64. See [`sys.float_info`](https://docs.python.org/3/library/sys.html#sys.float_info "sys.float_info")
 for details.

Nesting limit

TOML 1.1.0 does not recommend a limit on how deeply arrays and tables may be nested inside one another. (A limit of 100 has been proposed for a future version of TOML.)

**CPython implementation detail:** In `tomllib`, the nesting level is mainly limited by Python’s [`recursion limit`](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit "sys.getrecursionlimit")
. Note that code that calls `tomllib` may contribute to the limit.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html#)
    *   [Examples](https://docs.python.org/3/library/tomllib.html#examples)
        
    *   [Conversion Table](https://docs.python.org/3/library/tomllib.html#conversion-table)
        
    *   [Limits and interoperability considerations](https://docs.python.org/3/library/tomllib.html#limits-and-interoperability-considerations)
        

#### Previous topic

[`configparser` — Configuration file parser](https://docs.python.org/3/library/configparser.html "previous chapter")

#### Next topic

[`netrc` — netrc file processing](https://docs.python.org/3/library/netrc.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=tomllib+%E2%80%94+Parse+TOML+files&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftomllib.html&pagesource=library%2Ftomllib.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/tomllib.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/netrc.html "netrc — netrc file processing")
     |
*   [previous](https://docs.python.org/3/library/configparser.html "configparser — Configuration file parser")
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
*   [`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html)
    
*    
    
    |
*   Theme Auto Light Dark |