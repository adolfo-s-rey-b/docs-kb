### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/weakref.html "Weak Reference Objects")
     |
*   [previous](https://docs.python.org/3/c-api/memoryview.html "MemoryView objects")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Pickle buffer objects](https://docs.python.org/3/c-api/picklebuffer.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Pickle buffer objects[¶](https://docs.python.org/3/c-api/picklebuffer.html#pickle-buffer-objects "Link to this heading")

=========================================================================================================================

Added in version 3.8.

A [`pickle.PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer")
 object wraps a [buffer-providing object](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
 for out-of-band data transfer with the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
 module.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyPickleBuffer\_Type[¶](https://docs.python.org/3/c-api/picklebuffer.html#c.PyPickleBuffer_Type "Link to this definition")
  

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python pickle buffer type. This is the same object as [`pickle.PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer")
 in the Python layer.

int PyPickleBuffer\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*op)[¶](https://docs.python.org/3/c-api/picklebuffer.html#c.PyPickleBuffer_Check "Link to this definition")
  

Return true if _op_ is a pickle buffer instance. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyPickleBuffer\_FromObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/picklebuffer.html#c.PyPickleBuffer_FromObject "Link to this definition")
  

Create a pickle buffer from the object _obj_.

This function will fail if _obj_ doesn’t support the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
.

On success, return a new pickle buffer instance. On failure, set an exception and return `NULL`.

Analogous to calling [`pickle.PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer")
 with _obj_ in Python.

const [Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 \*PyPickleBuffer\_GetBuffer([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*picklebuf)[¶](https://docs.python.org/3/c-api/picklebuffer.html#c.PyPickleBuffer_GetBuffer "Link to this definition")
  

Get a pointer to the underlying [`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 that the pickle buffer wraps.

The returned pointer is valid as long as _picklebuf_ is alive and has not been released. The caller must not modify or free the returned [`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
. If the pickle buffer has been released, raise [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
.

On success, return a pointer to the buffer view. On failure, set an exception and return `NULL`.

int PyPickleBuffer\_Release([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*picklebuf)[¶](https://docs.python.org/3/c-api/picklebuffer.html#c.PyPickleBuffer_Release "Link to this definition")
  

Release the underlying buffer held by the pickle buffer.

Return `0` on success. On failure, set an exception and return `-1`.

Analogous to calling [`pickle.PickleBuffer.release()`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer.release "pickle.PickleBuffer.release")
 in Python.

#### Previous topic

[MemoryView objects](https://docs.python.org/3/c-api/memoryview.html "previous chapter")

#### Next topic

[Weak Reference Objects](https://docs.python.org/3/c-api/weakref.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Pickle+buffer+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fpicklebuffer.html&pagesource=c-api%2Fpicklebuffer.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/picklebuffer.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/weakref.html "Weak Reference Objects")
     |
*   [previous](https://docs.python.org/3/c-api/memoryview.html "MemoryView objects")
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
*   [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html)
     »
*   [Pickle buffer objects](https://docs.python.org/3/c-api/picklebuffer.html)
    
*    
    
    |
*   Theme Auto Light Dark |