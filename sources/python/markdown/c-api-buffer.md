### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/concrete.html "Concrete Objects Layer")
     |
*   [previous](https://docs.python.org/3/c-api/iter.html "Iterator Protocol")
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
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
     »
*   [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Buffer Protocol[¶](https://docs.python.org/3/c-api/buffer.html#buffer-protocol "Link to this heading")

=======================================================================================================

Certain objects available in Python wrap access to an underlying memory array or _buffer_. Such objects include the built-in [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
, and some extension types like [`array.array`](https://docs.python.org/3/library/array.html#array.array "array.array")
. Third-party libraries may define their own types for special purposes, such as image processing or numeric analysis.

While each of these types have their own semantics, they share the common characteristic of being backed by a possibly large memory buffer. It is then desirable, in some situations, to access that buffer directly and without intermediate copying.

Python provides such a facility at the C and Python level in the form of the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects)
. This protocol has two sides:

*   on the producer side, a type can export a “buffer interface” which allows objects of that type to expose information about their underlying buffer. This interface is described in the section [Buffer Object Structures](https://docs.python.org/3/c-api/typeobj.html#buffer-structs)
    ; for Python see [Emulating buffer types](https://docs.python.org/3/reference/datamodel.html#python-buffer-protocol)
    .
    
*   on the consumer side, several means are available to obtain a pointer to the raw underlying data of an object (for example a method parameter). For Python see [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
    .
    

Simple objects such as [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 and [`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 expose their underlying buffer in byte-oriented form. Other forms are possible; for example, the elements exposed by an [`array.array`](https://docs.python.org/3/library/array.html#array.array "array.array")
 can be multi-byte values.

An example consumer of the buffer interface is the [`write()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "io.BufferedIOBase.write")
 method of file objects: any object that can export a series of bytes through the buffer interface can be written to a file. While `write()` only needs read-only access to the internal contents of the object passed to it, other methods such as [`readinto()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto")
 need write access to the contents of their argument. The buffer interface allows objects to selectively allow or reject exporting of read-write and read-only buffers.

There are two ways for a consumer of the buffer interface to acquire a buffer over a target object:

*   call [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
     with the right parameters;
    
*   call [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple")
     (or one of its siblings) with one of the `y*`, `w*` or `s*` [format codes](https://docs.python.org/3/c-api/arg.html#arg-parsing)
    .
    

In both cases, [`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
 must be called when the buffer isn’t needed anymore. Failure to do so could lead to various issues such as resource leaks.

Added in version 3.12: The buffer protocol is now accessible in Python, see [Emulating buffer types](https://docs.python.org/3/reference/datamodel.html#python-buffer-protocol)
 and [`memoryview`](https://docs.python.org/3/builtins/stdtypes.html#memoryview "memoryview")
.

Buffer structure[¶](https://docs.python.org/3/c-api/buffer.html#buffer-structure "Link to this heading")

---------------------------------------------------------------------------------------------------------

Buffer structures (or simply “buffers”) are useful as a way to expose the binary data from another object to the Python programmer. They can also be used as a zero-copy slicing mechanism. Using their ability to reference a block of memory, it is possible to expose any data to the Python programmer quite easily. The memory could be a large, constant array in a C extension, it could be a raw block of memory for manipulation before passing to an operating system library, or it could be used to pass around structured data in its native, in-memory format.

Contrary to most data types exposed by the Python interpreter, buffers are not [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 pointers but rather simple C structures. This allows them to be created and copied very simply. When a generic wrapper around a buffer is needed, a [memoryview](https://docs.python.org/3/c-api/memoryview.html#memoryview-objects)
 object can be created.

For short instructions how to write an exporting object, see [Buffer Object Structures](https://docs.python.org/3/c-api/typeobj.html#buffer-structs)
. For obtaining a buffer, see [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
.

type Py\_buffer[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 (including all members) since version 3.11._

void \*buf[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.buf "Link to this definition")
  

A pointer to the start of the logical structure described by the buffer fields. This can be any location within the underlying physical memory block of the exporter. For example, with negative [`strides`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.strides "Py_buffer.strides")
 the value may point to the end of the memory block.

For [contiguous](https://docs.python.org/3/glossary.html#term-contiguous)
 arrays, the value points to the beginning of the memory block.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.obj "Link to this definition")
  

A new reference to the exporting object. The reference is owned by the consumer and automatically released (i.e. reference count decremented) and set to `NULL` by [`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
. The field is the equivalent of the return value of any standard C-API function.

As a special case, for _temporary_ buffers that are wrapped by [`PyMemoryView_FromBuffer()`](https://docs.python.org/3/c-api/memoryview.html#c.PyMemoryView_FromBuffer "PyMemoryView_FromBuffer")
 or [`PyBuffer_FillInfo()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_FillInfo "PyBuffer_FillInfo")
 this field is `NULL`. In general, exporting objects MUST NOT use this scheme.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.len "Link to this definition")
  

`product(shape) * itemsize`. For contiguous arrays, this is the length of the underlying memory block. For non-contiguous arrays, it is the length that the logical structure would have if it were copied to a contiguous representation.

Accessing `((char *)buf)[0] up to ((char *)buf)[len-1]` is only valid if the buffer has been obtained by a request that guarantees contiguity. In most cases such a request will be [`PyBUF_SIMPLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_SIMPLE "PyBUF_SIMPLE")
 or [`PyBUF_WRITABLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITABLE "PyBUF_WRITABLE")
.

int readonly[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.readonly "Link to this definition")
  

An indicator of whether the buffer is read-only. This field is controlled by the [`PyBUF_WRITABLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITABLE "PyBUF_WRITABLE")
 flag.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 itemsize[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.itemsize "Link to this definition")
  

Item size in bytes of a single element. Same as the value of [`struct.calcsize()`](https://docs.python.org/3/library/struct.html#struct.calcsize "struct.calcsize")
 called on non-`NULL` [`format`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.format "Py_buffer.format")
 values.

Important exception: If a consumer requests a buffer without the [`PyBUF_FORMAT`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_FORMAT "PyBUF_FORMAT")
 flag, [`format`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.format "Py_buffer.format")
 will be set to `NULL`, but [`itemsize`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.itemsize "Py_buffer.itemsize")
 still has the value for the original format.

If [`shape`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.shape "Py_buffer.shape")
 is present, the equality `product(shape) * itemsize == len` still holds and the consumer can use [`itemsize`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.itemsize "Py_buffer.itemsize")
 to navigate the buffer.

If [`shape`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.shape "Py_buffer.shape")
 is `NULL` as a result of a [`PyBUF_SIMPLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_SIMPLE "PyBUF_SIMPLE")
 or a [`PyBUF_WRITABLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITABLE "PyBUF_WRITABLE")
 request, the consumer must disregard [`itemsize`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.itemsize "Py_buffer.itemsize")
 and assume `itemsize == 1`.

char \*format[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.format "Link to this definition")
  

A _NULL_ terminated string in [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")
 module style syntax describing the contents of a single item. If this is `NULL`, `"B"` (unsigned bytes) is assumed.

This field is controlled by the [`PyBUF_FORMAT`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_FORMAT "PyBUF_FORMAT")
 flag.

int ndim[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.ndim "Link to this definition")
  

The number of dimensions the memory represents as an n-dimensional array. If it is `0`, [`buf`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.buf "Py_buffer.buf")
 points to a single item representing a scalar. In this case, [`shape`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.shape "Py_buffer.shape")
, [`strides`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.strides "Py_buffer.strides")
 and [`suboffsets`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.suboffsets "Py_buffer.suboffsets")
 MUST be `NULL`. The maximum number of dimensions is given by [`PyBUF_MAX_NDIM`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_MAX_NDIM "PyBUF_MAX_NDIM")
.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*shape[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.shape "Link to this definition")
  

An array of [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 of length [`ndim`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.ndim "Py_buffer.ndim")
 indicating the shape of the memory as an n-dimensional array. Note that `shape[0] * ... * shape[ndim-1] * itemsize` MUST be equal to [`len`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.len "Py_buffer.len")
.

Shape values are restricted to `shape[n] >= 0`. The case `shape[n] == 0` requires special attention. See [complex arrays](https://docs.python.org/3/c-api/buffer.html#complex-arrays)
 for further information.

The shape array is read-only for the consumer.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*strides[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.strides "Link to this definition")
  

An array of [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 of length [`ndim`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.ndim "Py_buffer.ndim")
 giving the number of bytes to skip to get to a new element in each dimension.

Stride values can be any integer. For regular arrays, strides are usually positive, but a consumer MUST be able to handle the case `strides[n] <= 0`. See [complex arrays](https://docs.python.org/3/c-api/buffer.html#complex-arrays)
 for further information.

The strides array is read-only for the consumer.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*suboffsets[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.suboffsets "Link to this definition")
  

An array of [`Py_ssize_t`](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 of length [`ndim`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.ndim "Py_buffer.ndim")
. If `suboffsets[n] >= 0`, the values stored along the nth dimension are pointers and the suboffset value dictates how many bytes to add to each pointer after de-referencing. A suboffset value that is negative indicates that no de-referencing should occur (striding in a contiguous memory block).

If all suboffsets are negative (i.e. no de-referencing is needed), then this field must be `NULL` (the default value).

This type of array representation is used by the Python Imaging Library (PIL). See [complex arrays](https://docs.python.org/3/c-api/buffer.html#complex-arrays)
 for further information how to access elements of such an array.

The suboffsets array is read-only for the consumer.

void \*internal[¶](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.internal "Link to this definition")
  

This is for use internally by the exporting object. For example, this might be re-cast as an integer by the exporter and used to store flags about whether or not the shape, strides, and suboffsets arrays must be freed when the buffer is released. The consumer MUST NOT alter this value.

Constants:

PyBUF\_MAX\_NDIM[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_MAX_NDIM "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

The maximum number of dimensions the memory represents. Exporters MUST respect this limit, consumers of multi-dimensional buffers SHOULD be able to handle up to `PyBUF_MAX_NDIM` dimensions. Currently set to 64.

Buffer request types[¶](https://docs.python.org/3/c-api/buffer.html#buffer-request-types "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Buffers are usually obtained by sending a buffer request to an exporting object via [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
. Since the complexity of the logical structure of the memory can vary drastically, the consumer uses the _flags_ argument to specify the exact buffer type it can handle.

All [`Py_buffer`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 fields are unambiguously defined by the request type.

### request-independent fields[¶](https://docs.python.org/3/c-api/buffer.html#request-independent-fields "Link to this heading")

The following fields are not influenced by _flags_ and must always be filled in with the correct values: [`obj`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.obj "Py_buffer.obj")
, [`buf`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.buf "Py_buffer.buf")
, [`len`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.len "Py_buffer.len")
, [`itemsize`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.itemsize "Py_buffer.itemsize")
, [`ndim`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.ndim "Py_buffer.ndim")
.

### readonly, format[¶](https://docs.python.org/3/c-api/buffer.html#readonly-format "Link to this heading")

> PyBUF\_WRITABLE[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITABLE "Link to this definition")
>   
> 
> _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
>  since version 3.11._
> 
> Controls the [`readonly`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.readonly "Py_buffer.readonly")
>  field. If set, the exporter MUST provide a writable buffer or else report failure. Otherwise, the exporter MAY provide either a read-only or writable buffer, but the choice MUST be consistent for all consumers. For example, [PyBUF\_SIMPLE](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_SIMPLE "PyBUF_SIMPLE")
>  | [PyBUF\_WRITABLE](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITABLE "PyBUF_WRITABLE")
>  can be used to request a simple writable buffer.
> 
> PyBUF\_WRITEABLE[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITEABLE "Link to this definition")
>   
> 
> This is an alias to [`PyBUF_WRITABLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITABLE "PyBUF_WRITABLE")
> .
> 
> [Soft deprecated](https://docs.python.org/3/glossary.html#term-soft-deprecated)
>  since version 3.13.
> 
> PyBUF\_FORMAT[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_FORMAT "Link to this definition")
>   
> 
> _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
>  since version 3.11._
> 
> Controls the [`format`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.format "Py_buffer.format")
>  field. If set, this field MUST be filled in correctly. Otherwise, this field MUST be `NULL`.

[`PyBUF_WRITABLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITABLE "PyBUF_WRITABLE")
 can be |’d to any of the flags in the next section. Since [`PyBUF_SIMPLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_SIMPLE "PyBUF_SIMPLE")
 is defined as 0, `PyBUF_WRITABLE` can be used as a stand-alone flag to request a simple writable buffer.

[`PyBUF_FORMAT`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_FORMAT "PyBUF_FORMAT")
 must be |’d to any of the flags except [`PyBUF_SIMPLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_SIMPLE "PyBUF_SIMPLE")
, because the latter already implies format `B` (unsigned bytes). `PyBUF_FORMAT` cannot be used on its own.

### shape, strides, suboffsets[¶](https://docs.python.org/3/c-api/buffer.html#shape-strides-suboffsets "Link to this heading")

The flags that control the logical structure of the memory are listed in decreasing order of complexity. Note that each flag contains all bits of the flags below it.

These values are available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11.

| Request | shape | strides | suboffsets |
| --- | --- | --- | --- |
| PyBUF\_INDIRECT[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_INDIRECT "Link to this definition") | yes | yes | if needed |
| PyBUF\_STRIDES[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_STRIDES "Link to this definition") | yes | yes | NULL |
| PyBUF\_ND[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_ND "Link to this definition") | yes | NULL | NULL |
| PyBUF\_SIMPLE[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_SIMPLE "Link to this definition") | NULL | NULL | NULL |

### contiguity requests[¶](https://docs.python.org/3/c-api/buffer.html#contiguity-requests "Link to this heading")

C or Fortran [contiguity](https://docs.python.org/3/glossary.html#term-contiguous)
 can be explicitly requested, with and without stride information. Without stride information, the buffer must be C-contiguous.

These values are available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11.

| Request | shape | strides | suboffsets | contig |
| --- | --- | --- | --- | --- |
| PyBUF\_C\_CONTIGUOUS[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_C_CONTIGUOUS "Link to this definition") | yes | yes | NULL | C   |
| PyBUF\_F\_CONTIGUOUS[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_F_CONTIGUOUS "Link to this definition") | yes | yes | NULL | F   |
| PyBUF\_ANY\_CONTIGUOUS[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_ANY_CONTIGUOUS "Link to this definition") | yes | yes | NULL | C or F |
| [`PyBUF_ND`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_ND "PyBUF_ND") | yes | NULL | NULL | C   |

### compound requests[¶](https://docs.python.org/3/c-api/buffer.html#compound-requests "Link to this heading")

All possible requests are fully defined by some combination of the flags in the previous section. For convenience, the buffer protocol provides frequently used combinations as single flags.

In the following table _U_ stands for undefined contiguity. The consumer would have to call [`PyBuffer_IsContiguous()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_IsContiguous "PyBuffer_IsContiguous")
 to determine contiguity.

These values are available when compiling for the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11.

| Request | shape | strides | suboffsets | contig | readonly | format |
| --- | --- | --- | --- | --- | --- | --- |
| PyBUF\_FULL[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_FULL "Link to this definition") | yes | yes | if needed | U   | 0   | yes |
| PyBUF\_FULL\_RO[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_FULL_RO "Link to this definition") | yes | yes | if needed | U   | 1 or 0 | yes |
| PyBUF\_RECORDS[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_RECORDS "Link to this definition") | yes | yes | NULL | U   | 0   | yes |
| PyBUF\_RECORDS\_RO[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_RECORDS_RO "Link to this definition") | yes | yes | NULL | U   | 1 or 0 | yes |
| PyBUF\_STRIDED[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_STRIDED "Link to this definition") | yes | yes | NULL | U   | 0   | NULL |
| PyBUF\_STRIDED\_RO[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_STRIDED_RO "Link to this definition") | yes | yes | NULL | U   | 1 or 0 | NULL |
| PyBUF\_CONTIG[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_CONTIG "Link to this definition") | yes | NULL | NULL | C   | 0   | NULL |
| PyBUF\_CONTIG\_RO[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_CONTIG_RO "Link to this definition") | yes | NULL | NULL | C   | 1 or 0 | NULL |

Complex arrays[¶](https://docs.python.org/3/c-api/buffer.html#complex-arrays "Link to this heading")

-----------------------------------------------------------------------------------------------------

### NumPy-style: shape and strides[¶](https://docs.python.org/3/c-api/buffer.html#numpy-style-shape-and-strides "Link to this heading")

The logical structure of NumPy-style arrays is defined by [`itemsize`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.itemsize "Py_buffer.itemsize")
, [`ndim`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.ndim "Py_buffer.ndim")
, [`shape`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.shape "Py_buffer.shape")
 and [`strides`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.strides "Py_buffer.strides")
.

If `ndim == 0`, the memory location pointed to by [`buf`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.buf "Py_buffer.buf")
 is interpreted as a scalar of size [`itemsize`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.itemsize "Py_buffer.itemsize")
. In that case, both [`shape`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.shape "Py_buffer.shape")
 and [`strides`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.strides "Py_buffer.strides")
 are `NULL`.

If [`strides`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.strides "Py_buffer.strides")
 is `NULL`, the array is interpreted as a standard n-dimensional C-array. Otherwise, the consumer must access an n-dimensional array as follows:

ptr \= (char \*)buf + indices\[0\] \* strides\[0\] + ... + indices\[n\-1\] \* strides\[n\-1\];
item \= \*((typeof(item) \*)ptr);

As noted above, [`buf`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.buf "Py_buffer.buf")
 can point to any location within the actual memory block. An exporter can check the validity of a buffer with this function:

Copy

def verify\_structure(memlen, itemsize, ndim, shape, strides, offset):
    """Verify that the parameters represent a valid array within
       the bounds of the allocated memory:
           char \*mem: start of the physical memory block
           memlen: length of the physical memory block
           offset: (char \*)buf - mem
    """
    if offset % itemsize:
        return False
    if offset < 0 or offset+itemsize \> memlen:
        return False
    if any(v % itemsize for v in strides):
        return False

    if ndim <= 0:
        return ndim \== 0 and not shape and not strides
    if 0 in shape:
        return True

    imin \= sum(strides\[j\]\*(shape\[j\]\-1) for j in range(ndim)
               if strides\[j\] <= 0)
    imax \= sum(strides\[j\]\*(shape\[j\]\-1) for j in range(ndim)
               if strides\[j\] \> 0)

    return 0 <= offset+imin and offset+imax+itemsize <= memlen

### PIL-style: shape, strides and suboffsets[¶](https://docs.python.org/3/c-api/buffer.html#pil-style-shape-strides-and-suboffsets "Link to this heading")

In addition to the regular items, PIL-style arrays can contain pointers that must be followed in order to get to the next element in a dimension. For example, the regular three-dimensional C-array `char v[2][2][3]` can also be viewed as an array of 2 pointers to 2 two-dimensional arrays: `char (*v[2])[2][3]`. In suboffsets representation, those two pointers can be embedded at the start of [`buf`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.buf "Py_buffer.buf")
, pointing to two `char x[2][3]` arrays that can be located anywhere in memory.

Here is a function that returns a pointer to the element in an N-D array pointed to by an N-dimensional index when there are both non-`NULL` strides and suboffsets:

void \*get\_item\_pointer(int ndim, void \*buf, Py\_ssize\_t \*strides,
                       Py\_ssize\_t \*suboffsets, Py\_ssize\_t \*indices) {
    char \*pointer \= (char\*)buf;
    int i;
    for (i \= 0; i < ndim; i++) {
        pointer += strides\[i\] \* indices\[i\];
        if (suboffsets\[i\] \>=0 ) {
            pointer \= \*((char\*\*)pointer) + suboffsets\[i\];
        }
    }
    return (void\*)pointer;
}

Buffer-related functions[¶](https://docs.python.org/3/c-api/buffer.html#buffer-related-functions "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

int PyObject\_CheckBuffer([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*obj)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyObject_CheckBuffer "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Return `1` if _obj_ supports the buffer interface otherwise `0`. When `1` is returned, it doesn’t guarantee that [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
 will succeed. This function always succeeds.

int PyObject\_GetBuffer([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exporter, [Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 \*view, int flags)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Send a request to _exporter_ to fill in _view_ as specified by _flags_. If the exporter cannot provide a buffer of the exact type, it MUST raise [`BufferError`](https://docs.python.org/3/builtins/exceptions.html#BufferError "BufferError")
, set `view->obj` to `NULL` and return `-1`.

On success, fill in _view_, set `view->obj` to a new reference to _exporter_ and return 0. In the case of chained buffer providers that redirect requests to a single object, `view->obj` MAY refer to this object instead of _exporter_ (See [Buffer Object Structures](https://docs.python.org/3/c-api/typeobj.html#buffer-structs)
).

Successful calls to [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
 must be paired with calls to [`PyBuffer_Release()`](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "PyBuffer_Release")
, similar to `malloc()` and `free()`. Thus, after the consumer is done with the buffer, `PyBuffer_Release()` must be called exactly once.

void PyBuffer\_Release([Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 \*view)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_Release "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Release the buffer _view_ and release the [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 (i.e. decrement the reference count) to the view’s supporting object, `view->obj`. This function MUST be called when the buffer is no longer being used, otherwise reference leaks may occur.

It is an error to call this function on a buffer that was not obtained via [`PyObject_GetBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_GetBuffer "PyObject_GetBuffer")
.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 PyBuffer\_SizeFromFormat(const char \*format)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_SizeFromFormat "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Return the implied [`itemsize`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.itemsize "Py_buffer.itemsize")
 from [`format`](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer.format "Py_buffer.format")
. On error, raise an exception and return -1.

Added in version 3.9.

int PyBuffer\_IsContiguous(const [Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 \*view, char order)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_IsContiguous "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Return `1` if the memory defined by the _view_ is C-style (_order_ is `'C'`) or Fortran-style (_order_ is `'F'`) [contiguous](https://docs.python.org/3/glossary.html#term-contiguous)
 or either one (_order_ is `'A'`). Return `0` otherwise. This function always succeeds.

void \*PyBuffer\_GetPointer(const [Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 \*view, const [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*indices)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_GetPointer "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Get the memory area pointed to by the _indices_ inside the given _view_. _indices_ must point to an array of `view->ndim` indices.

int PyBuffer\_FromContiguous(const [Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 \*view, const void \*buf, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len, char order)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_FromContiguous "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Copy contiguous _len_ bytes from _buf_ to _view_. _order_ can be `'C'` or `'F'` or `'A'` (for C-style or Fortran-style ordering or either one). `0` is returned on success, `-1` on error.

int PyBuffer\_ToContiguous(void \*buf, const [Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 \*src, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len, char order)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_ToContiguous "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Copy _len_ bytes from _src_ to its contiguous representation in _buf_. _order_ can be `'C'` or `'F'` or `'A'` (for C-style or Fortran-style ordering or either one). `0` is returned on success, `-1` on error.

This function fails if _len_ != _src->len_.

int PyObject\_CopyData([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*dest, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*src)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyObject_CopyData "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Copy data from _src_ to _dest_ buffer. Can convert between C-style and or Fortran-style buffers.

`0` is returned on success, `-1` on error.

void PyBuffer\_FillContiguousStrides(int ndims, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*shape, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 \*strides, int itemsize, char order)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_FillContiguousStrides "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Fill the _strides_ array with byte-strides of a [contiguous](https://docs.python.org/3/glossary.html#term-contiguous)
 (C-style if _order_ is `'C'` or Fortran-style if _order_ is `'F'`) array of the given shape with the given number of bytes per element.

int PyBuffer\_FillInfo([Py\_buffer](https://docs.python.org/3/c-api/buffer.html#c.Py_buffer "Py_buffer")
 \*view, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*exporter, void \*buf, [Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t")
 len, int readonly, int flags)[¶](https://docs.python.org/3/c-api/buffer.html#c.PyBuffer_FillInfo "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.11._

Handle buffer requests for an exporter that wants to expose _buf_ of size _len_ with writability set according to _readonly_. _buf_ is interpreted as a sequence of unsigned bytes.

The _flags_ argument indicates the request type. This function always fills in _view_ as specified by flags, unless _buf_ has been designated as read-only and [`PyBUF_WRITABLE`](https://docs.python.org/3/c-api/buffer.html#c.PyBUF_WRITABLE "PyBUF_WRITABLE")
 is set in _flags_.

On success, set `view->obj` to a new reference to _exporter_ and return 0. Otherwise, raise [`BufferError`](https://docs.python.org/3/builtins/exceptions.html#BufferError "BufferError")
, set `view->obj` to `NULL` and return `-1`;

If this function is used as part of a [getbufferproc](https://docs.python.org/3/c-api/typeobj.html#buffer-structs)
, _exporter_ MUST be set to the exporting object and _flags_ must be passed unmodified. Otherwise, _exporter_ MUST be `NULL`.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html#)
    *   [Buffer structure](https://docs.python.org/3/c-api/buffer.html#buffer-structure)
        
    *   [Buffer request types](https://docs.python.org/3/c-api/buffer.html#buffer-request-types)
        *   [request-independent fields](https://docs.python.org/3/c-api/buffer.html#request-independent-fields)
            
        *   [readonly, format](https://docs.python.org/3/c-api/buffer.html#readonly-format)
            
        *   [shape, strides, suboffsets](https://docs.python.org/3/c-api/buffer.html#shape-strides-suboffsets)
            
        *   [contiguity requests](https://docs.python.org/3/c-api/buffer.html#contiguity-requests)
            
        *   [compound requests](https://docs.python.org/3/c-api/buffer.html#compound-requests)
            
    *   [Complex arrays](https://docs.python.org/3/c-api/buffer.html#complex-arrays)
        *   [NumPy-style: shape and strides](https://docs.python.org/3/c-api/buffer.html#numpy-style-shape-and-strides)
            
        *   [PIL-style: shape, strides and suboffsets](https://docs.python.org/3/c-api/buffer.html#pil-style-shape-strides-and-suboffsets)
            
    *   [Buffer-related functions](https://docs.python.org/3/c-api/buffer.html#buffer-related-functions)
        

#### Previous topic

[Iterator Protocol](https://docs.python.org/3/c-api/iter.html "previous chapter")

#### Next topic

[Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Buffer+Protocol&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fbuffer.html&pagesource=c-api%2Fbuffer.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/buffer.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/concrete.html "Concrete Objects Layer")
     |
*   [previous](https://docs.python.org/3/c-api/iter.html "Iterator Protocol")
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
*   [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html)
     »
*   [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html)
    
*    
    
    |
*   Theme Auto Light Dark |