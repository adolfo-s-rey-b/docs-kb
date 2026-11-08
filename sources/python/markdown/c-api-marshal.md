### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/arg.html "Parsing arguments and building values")
     |
*   [previous](https://docs.python.org/3/c-api/import.html "Importing Modules")
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
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Data marshalling support](https://docs.python.org/3/c-api/marshal.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Data marshalling support[¶](https://docs.python.org/3/c-api/marshal.html#data-marshalling-support "Link to this heading")

==========================================================================================================================

These routines allow C code to work with serialized objects using the same data format as the [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).")
 module. There are functions to write data into the serialization format, and additional functions that can be used to read the data back. Files used to store marshalled data must be opened in binary mode.

Numeric values are stored with the least significant byte first.

The module supports several versions of the data format; see the [`Python module documentation`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).")
 for details.

Py\_MARSHAL\_VERSION[¶](https://docs.python.org/3/c-api/marshal.html#c.Py_MARSHAL_VERSION "Link to this definition")
  

The current format version. See [`marshal.version`](https://docs.python.org/3/library/marshal.html#marshal.version "marshal.version")
.

void PyMarshal\_WriteLongToFile(long value, FILE \*file, int version)[¶](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_WriteLongToFile "Link to this definition")
  

Marshal a long integer, _value_, to _file_. This will only write the least-significant 32 bits of _value_; regardless of the size of the native long type. _version_ indicates the file format.

This function can fail, in which case it sets the error indicator. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to check for that.

Note

In Python 3.15 and earlier, this function does not set the error indicator if writing to _file_ fails. The same caveat applies as for [`PyMarshal_WriteObjectToFile()`](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_WriteObjectToFile "PyMarshal_WriteObjectToFile")
.

void PyMarshal\_WriteObjectToFile([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value, FILE \*file, int version)[¶](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_WriteObjectToFile "Link to this definition")
  

Marshal a Python object, _value_, to _file_. _version_ indicates the file format.

This function can fail, in which case it sets the error indicator. Use [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 to check for that.

Note

In Python 3.15 and earlier, this function can write only part of the data to _file_ and return without setting the error indicator, for example if _value_ contains an object which cannot be marshalled or if writing to _file_ fails (see [gh-155907](https://github.com/python/cpython/issues/155907)
). Code which has to support these versions cannot rely on [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred")
 alone to know that all the data was written. It can use [`PyMarshal_WriteObjectToString()`](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_WriteObjectToString "PyMarshal_WriteObjectToString")
 and write the result itself, or validate what was written.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMarshal\_WriteObjectToString([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*value, int version)[¶](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_WriteObjectToString "Link to this definition")
  

_Return value: New reference._

Return a bytes object containing the marshalled representation of _value_. _version_ indicates the file format.

The following functions allow marshalled values to be read back in.

long PyMarshal\_ReadLongFromFile(FILE \*file)[¶](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_ReadLongFromFile "Link to this definition")
  

Return a C long from the data stream in a FILE\* opened for reading. Only a 32-bit value can be read in using this function, regardless of the native size of long.

On error, sets the appropriate exception ([`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
) and returns `-1`.

int PyMarshal\_ReadShortFromFile(FILE \*file)[¶](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_ReadShortFromFile "Link to this definition")
  

Return a C short from the data stream in a FILE\* opened for reading. Only a 16-bit value can be read in using this function, regardless of the native size of short.

On error, sets the appropriate exception ([`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
) and returns `-1`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMarshal\_ReadObjectFromFile(FILE \*file)[¶](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_ReadObjectFromFile "Link to this definition")
  

_Return value: New reference._

Return a Python object from the data stream in a FILE\* opened for reading.

On error, sets the appropriate exception ([`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 or [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
) and returns `NULL`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMarshal\_ReadLastObjectFromFile(FILE \*file)[¶](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_ReadLastObjectFromFile "Link to this definition")
  

_Return value: New reference._

Return a Python object from the data stream in a FILE\* opened for reading. Unlike [`PyMarshal_ReadObjectFromFile()`](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_ReadObjectFromFile "PyMarshal_ReadObjectFromFile")
, this function assumes that no further objects will be read from the file, allowing it to aggressively load file data into memory so that the de-serialization can operate from data in memory rather than reading a byte at a time from the file. Only use this variant if you are certain that you won’t be reading anything else from the file.

On error, sets the appropriate exception ([`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 or [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
) and returns `NULL`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMarshal\_ReadObjectFromString(const char \*data, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len)[¶](https://docs.python.org/3/c-api/marshal.html#c.PyMarshal_ReadObjectFromString "Link to this definition")
  

_Return value: New reference._

Return a Python object from the data stream in a byte buffer containing _len_ bytes pointed to by _data_.

On error, sets the appropriate exception ([`EOFError`](https://docs.python.org/3/builtins/exceptions.html#EOFError "EOFError")
, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 or [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
) and returns `NULL`.

#### Previous topic

[Importing Modules](https://docs.python.org/3/c-api/import.html "previous chapter")

#### Next topic

[Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Data+marshalling+support&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fmarshal.html&pagesource=c-api%2Fmarshal.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/marshal.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/arg.html "Parsing arguments and building values")
     |
*   [previous](https://docs.python.org/3/c-api/import.html "Importing Modules")
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
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Data marshalling support](https://docs.python.org/3/c-api/marshal.html)
    
*    
    
    |
*   Theme Auto Light Dark |