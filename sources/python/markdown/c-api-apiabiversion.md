### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/monitoring.html "Monitoring C API")
     |
*   [previous](https://docs.python.org/3/c-api/gcsupport.html "Supporting Cyclic Garbage Collection")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [API and ABI Versioning](https://docs.python.org/3/c-api/apiabiversion.html)
    
*    
    
    |
*   Theme Auto Light Dark |

API and ABI Versioning[¶](https://docs.python.org/3/c-api/apiabiversion.html#api-and-abi-versioning "Link to this heading")

============================================================================================================================

Build-time version constants[¶](https://docs.python.org/3/c-api/apiabiversion.html#build-time-version-constants "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

CPython exposes its version number in the following macros. Note that these correspond to the version code is **built** with. See [`Py_Version`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_Version "Py_Version")
 for the version used at **run time**.

See [C API and ABI Stability](https://docs.python.org/3/c-api/stable.html#stable)
 for a discussion of API and ABI stability across versions.

PY\_MAJOR\_VERSION[¶](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_MAJOR_VERSION "Link to this definition")
  

The `3` in `3.4.1a2`.

PY\_MINOR\_VERSION[¶](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_MINOR_VERSION "Link to this definition")
  

The `4` in `3.4.1a2`.

PY\_MICRO\_VERSION[¶](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_MICRO_VERSION "Link to this definition")
  

The `1` in `3.4.1a2`.

PY\_RELEASE\_LEVEL[¶](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_RELEASE_LEVEL "Link to this definition")
  

The `a` in `3.4.1a2`. This can be `0xA` for alpha, `0xB` for beta, `0xC` for release candidate or `0xF` for final.

For completeness, the values are available as macros: `PY_RELEASE_LEVEL_ALPHA` (`0xA`), `PY_RELEASE_LEVEL_BETA` (`0xB`), `PY_RELEASE_LEVEL_GAMMA` (`0xC`), and `PY_RELEASE_LEVEL_FINAL` (`0xF`).

PY\_RELEASE\_SERIAL[¶](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_RELEASE_SERIAL "Link to this definition")
  

The `2` in `3.4.1a2`. Zero for final releases.

PY\_VERSION\_HEX[¶](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_VERSION_HEX "Link to this definition")
  

The Python version number encoded in a single integer. See [`Py_PACK_FULL_VERSION()`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_PACK_FULL_VERSION "Py_PACK_FULL_VERSION")
 for the encoding details.

Use this for numeric comparisons, for example, `#if PY_VERSION_HEX >= ...`.

PY\_VERSION[¶](https://docs.python.org/3/c-api/apiabiversion.html#c.PY_VERSION "Link to this definition")
  

The Python version as a string, for example, `"3.4.1a2"`.

These macros are defined in [Include/patchlevel.h](https://github.com/python/cpython/tree/3.15/Include/patchlevel.h)
.

Run-time version[¶](https://docs.python.org/3/c-api/apiabiversion.html#run-time-version "Link to this heading")

----------------------------------------------------------------------------------------------------------------

const unsigned long Py\_Version[¶](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_Version "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

The Python runtime version number encoded in a single constant integer. See [`Py_PACK_FULL_VERSION()`](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_PACK_FULL_VERSION "Py_PACK_FULL_VERSION")
 for the encoding details. This contains the Python version used at run time.

Use this for numeric comparisons, for example, `if (Py_Version >= ...)`.

Added in version 3.11.

Bit-packing macros[¶](https://docs.python.org/3/c-api/apiabiversion.html#bit-packing-macros "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

uint32\_t Py\_PACK\_FULL\_VERSION(int major, int minor, int micro, int release\_level, int release\_serial)[¶](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_PACK_FULL_VERSION "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Return the given version, encoded as a single 32-bit integer with the following structure:

| Argument | No. of bits | Bit mask | Bit shift | Example values |     |
| --- | --- | --- | --- | --- | --- |
| `3.4.1a2` | `3.10.0` |
| --- | --- | --- | --- | --- | --- |
| _major_ | 8   | `0xFF000000` | 24  | `0x03` | `0x03` |
| _minor_ | 8   | `0x00FF0000` | 16  | `0x04` | `0x0A` |
| _micro_ | 8   | `0x0000FF00` | 8   | `0x01` | `0x00` |
| _release\_level_ | 4   | `0x000000F0` | 4   | `0xA` | `0xF` |
| _release\_serial_ | 4   | `0x0000000F` | 0   | `0x2` | `0x0` |

For example:

| Version | `Py_PACK_FULL_VERSION` arguments | Encoded version |
| --- | --- | --- |
| `3.4.1a2` | `(3, 4, 1, 0xA, 2)` | `0x030401a2` |
| `3.10.0` | `(3, 10, 0, 0xF, 0)` | `0x030a00f0` |

Out-of range bits in the arguments are ignored. That is, the macro can be defined as:

#ifndef Py\_PACK\_FULL\_VERSION
#define Py\_PACK\_FULL\_VERSION(X, Y, Z, LEVEL, SERIAL) ( \\
   (((X) & 0xff) << 24) |                              \\
   (((Y) & 0xff) << 16) |                              \\
   (((Z) & 0xff) << 8) |                               \\
   (((LEVEL) & 0xf) << 4) |                            \\
   (((SERIAL) & 0xf) << 0))
#endif

`Py_PACK_FULL_VERSION` is primarily a macro, intended for use in `#if` directives, but it is also available as an exported function.

Added in version 3.14.

uint32\_t Py\_PACK\_VERSION(int major, int minor)[¶](https://docs.python.org/3/c-api/apiabiversion.html#c.Py_PACK_VERSION "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.14._

Equivalent to `Py_PACK_FULL_VERSION(major, minor, 0, 0, 0)`. The result does not correspond to any Python release, but is useful in numeric comparisons.

Added in version 3.14.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [API and ABI Versioning](https://docs.python.org/3/c-api/apiabiversion.html#)
    *   [Build-time version constants](https://docs.python.org/3/c-api/apiabiversion.html#build-time-version-constants)
        
    *   [Run-time version](https://docs.python.org/3/c-api/apiabiversion.html#run-time-version)
        
    *   [Bit-packing macros](https://docs.python.org/3/c-api/apiabiversion.html#bit-packing-macros)
        

#### Previous topic

[Supporting Cyclic Garbage Collection](https://docs.python.org/3/c-api/gcsupport.html "previous chapter")

#### Next topic

[Monitoring C API](https://docs.python.org/3/c-api/monitoring.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=API+and+ABI+Versioning&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fapiabiversion.html&pagesource=c-api%2Fapiabiversion.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/apiabiversion.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/monitoring.html "Monitoring C API")
     |
*   [previous](https://docs.python.org/3/c-api/gcsupport.html "Supporting Cyclic Garbage Collection")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [API and ABI Versioning](https://docs.python.org/3/c-api/apiabiversion.html)
    
*    
    
    |
*   Theme Auto Light Dark |