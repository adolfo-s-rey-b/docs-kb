### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/picklebuffer.html "Pickle buffer objects")
     |
*   [previous](https://docs.python.org/3/c-api/slice.html "Slice Objects")
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
*   [MemoryView objects](https://docs.python.org/3/c-api/memoryview.html)
    
*    
    
    |
*   Theme Auto Light Dark |

MemoryView objects[¶](https://docs.python.org/3/c-api/memoryview.html#index-0 "Link to this heading")

======================================================================================================

A [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
 object exposes the C level [buffer interface](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
 as a Python object which can then be passed around like any other object.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 PyMemoryView\_Type[¶](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_Type "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")
 represents the Python memoryview type. This is the same object as [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
 in the Python layer.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMemoryView\_FromObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a memoryview object from an object that provides the buffer interface. If _obj_ supports writable buffer exports, the memoryview object will be read/write, otherwise it may be either read-only or read/write at the discretion of the exporter.

PyBUF\_READ[¶](https://docs.python.org/3/c-api/memoryview.html#c.PyBUF_READ "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Flag to request a readonly buffer.

PyBUF\_WRITE[¶](https://docs.python.org/3/c-api/memoryview.html#c.PyBUF_WRITE "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Flag to request a writable buffer.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMemoryView\_FromMemory(char \*mem, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 size, int flags)[¶](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromMemory "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Create a memoryview object using _mem_ as the underlying buffer. _flags_ can be one of [`PyBUF_READ`](https://docs.python.org/3/c-api/memoryview.html#c.PyBUF_READ "PyBUF_READ")
 or [`PyBUF_WRITE`](https://docs.python.org/3/c-api/memoryview.html#c.PyBUF_WRITE "PyBUF_WRITE")
.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMemoryView\_FromBuffer(const [Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 \*view)[¶](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromBuffer "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Create a memoryview object wrapping the given buffer structure _view_. For simple byte buffers, [`PyMemoryView_FromMemory()`](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromMemory "PyMemoryView_FromMemory")
 is the preferred function.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMemoryView\_GetContiguous([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj, int buffertype, char order)[¶](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_GetContiguous "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Create a memoryview object to a [contiguous](https://docs.python.org/3/glossary.html#term-contiguous)
 chunk of memory (in either ‘C’ or ‘F’ortran _order_) from an object that defines the buffer interface. If memory is contiguous, the memoryview object points to the original memory. Otherwise, a copy is made and the memoryview points to a new bytes object.

_buffertype_ can be one of [`PyBUF_READ`](https://docs.python.org/3/c-api/memoryview.html#c.PyBUF_READ "PyBUF_READ")
 or [`PyBUF_WRITE`](https://docs.python.org/3/c-api/memoryview.html#c.PyBUF_WRITE "PyBUF_WRITE")
.

int PyMemoryView\_Check([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_Check "Link to this definition")
  

Return true if the object _obj_ is a memoryview object. It is not currently allowed to create subclasses of [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
. This function always succeeds.

[Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 \*PyMemoryView\_GET\_BUFFER([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*mview)[¶](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_GET_BUFFER "Link to this definition")
  

Return a pointer to the memoryview’s private copy of the exporter’s buffer. _mview_ **must** be a memoryview instance; this macro doesn’t check its type, you must do it yourself or you will risk crashes.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyMemoryView\_GET\_BASE([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*mview)[¶](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_GET_BASE "Link to this definition")
  

Return either a pointer to the exporting object that the memoryview is based on or `NULL` if the memoryview has been created by one of the functions [`PyMemoryView_FromMemory()`](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromMemory "PyMemoryView_FromMemory")
 or [`PyMemoryView_FromBuffer()`](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromBuffer "PyMemoryView_FromBuffer")
. _mview_ **must** be a memoryview instance.

#### Previous topic

[Slice Objects](https://docs.python.org/3/c-api/slice.html "previous chapter")

#### Next topic

[Pickle buffer objects](https://docs.python.org/3/c-api/picklebuffer.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=MemoryView+objects&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fmemoryview.html&pagesource=c-api%2Fmemoryview.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/memoryview.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/picklebuffer.html "Pickle buffer objects")
     |
*   [previous](https://docs.python.org/3/c-api/slice.html "Slice Objects")
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
*   [MemoryView objects](https://docs.python.org/3/c-api/memoryview.html)
    
*    
    
    |
*   Theme Auto Light Dark |