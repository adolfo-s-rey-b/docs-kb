[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.memmap.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.memmap.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.memmap.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.memmap.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.memmap.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.memmap.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.memmap.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.memmap.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.memmap.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.memmap.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.memmap.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.memmap.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.memmap.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.memmap.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.memmap.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.memmap.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.memmap.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.memmap.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.memmap.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.memmap.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.memmap[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy-memmap "Link to this heading")

========================================================================================================================

_class_ numpy.memmap(_filename_, _dtype=<class 'numpy.ubyte'>_, _mode='r+'_, _offset=0_, _shape=None_, _order='C'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/memmap.py#L23-L362)
[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "Link to this definition")

Create a memory-map to an array stored in a _binary_ file on disk.

Memory-mapped files are used for accessing small segments of large files on disk, without reading the entire file into memory. NumPy’s memmap’s are array-like objects. This differs from Python’s `mmap` module, which uses file-like objects.

This subclass of ndarray has some unpleasant interactions with some operations, because it doesn’t quite fit properly as a subclass. An alternative to using this subclass is to create the `mmap` object yourself, then create an ndarray with ndarray.\_\_new\_\_ directly, passing the object created in its ‘buffer=’ parameter.

This class may at some point be turned into a factory function which returns a view into an mmap buffer.

Flush the memmap instance to write the changes to the file. Currently there is no API to close the underlying `mmap`. It is tricky to ensure the resource is actually closed, since it may be shared between different memmap instances.

Parameters:

**filename**str, file-like object, or pathlib.Path instance

The file name or file object to be used as the array data buffer.

**dtype**data-type, optional

The data-type used to interpret the file contents. Default is [`uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "numpy.uint8")
.

**mode**{‘r+’, ‘r’, ‘w+’, ‘c’}, optional

The file is opened in this mode:

|     |     |
| --- | --- |
| ‘r’ | Open existing file for reading only. |
| ‘r+’ | Open existing file for reading and writing. |
| ‘w+’ | Create or overwrite existing file for reading and writing. If `mode == 'w+'` then [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")<br> must also be specified. |
| ‘c’ | Copy-on-write: assignments affect data in memory, but changes are not saved to disk. The file on disk is read-only. |

Default is ‘r+’.

**offset**int, optional

In the file, array data starts at this offset. Since _offset_ is measured in bytes, it should normally be a multiple of the byte-size of [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
. When `mode != 'r'`, even positive offsets beyond end of file are valid; The file will be extended to accommodate the additional data. By default, `memmap` will start at the beginning of the file, even if `filename` is a file pointer `fp` and `fp.tell() != 0`.

**shape**int or sequence of ints, optional

The desired shape of the array. If `mode == 'r'` and the number of remaining bytes after _offset_ is not a multiple of the byte-size of [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, you must specify [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")
. By default, the returned array will be 1-D with the number of elements determined by file size and data-type.

Changed in version 2.0: The shape parameter can now be any integer sequence type, previously types were limited to tuple and int.

**order**{‘C’, ‘F’}, optional

Specify the order of the ndarray memory layout: [row-major](https://numpy.org/doc/stable/glossary.html#term-row-major)
, C-style or [column-major](https://numpy.org/doc/stable/glossary.html#term-column-major)
, Fortran-style. This only has an effect if the shape is greater than 1-D. The default order is ‘C’.

Attributes:

**filename**str or pathlib.Path instance

Path to the mapped file.

**offset**int

Offset position in the file.

**mode**str

File mode.

Methods

|     |     |
| --- | --- |
| [`flush`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flush.html#numpy.memmap.flush "numpy.memmap.flush")<br>() | Write any changes in the array to the file on disk. |

See also

[`lib.format.open_memmap`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html#numpy.lib.format.open_memmap "numpy.lib.format.open_memmap")

Create or load a memory-mapped `.npy` file.

Notes

The memmap object can be used anywhere an ndarray is accepted. Given a memmap `fp`, `isinstance(fp, numpy.ndarray)` returns `True`.

Memory-mapped files cannot be larger than 2GB on 32-bit systems.

When a memmap causes a file to be created or extended beyond its current size in the filesystem, the contents of the new part are unspecified. On systems with POSIX filesystem semantics, the extended part will be filled with zero bytes.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> data \= np.arange(12, dtype\=np.float32).reshape((3, 4))

Copy to clipboard

This example uses a temporary file so that doctest doesn’t write files to your directory. You would use a ‘normal’ filename.

\>>> from tempfile import mkdtemp
\>>> import os.path as path
\>>> filename \= path.join(mkdtemp(), 'newfile.dat')

Copy to clipboard

Create a memmap with dtype and shape that matches our data:

\>>> fp \= np.memmap(filename, dtype\=np.float32, mode\='w+', shape\=(3,4))
\>>> fp
memmap(\[\[0., 0., 0., 0.\],\
        \[0., 0., 0., 0.\],\
        \[0., 0., 0., 0.\]\], dtype=float32)

Copy to clipboard

Write data to memmap array:

\>>> fp\[:\] \= data\[:\]
\>>> fp
memmap(\[\[  0.,   1.,   2.,   3.\],\
        \[  4.,   5.,   6.,   7.\],\
        \[  8.,   9.,  10.,  11.\]\], dtype=float32)

Copy to clipboard

\>>> fp.filename \== path.abspath(filename)
True

Copy to clipboard

Flushes memory changes to disk in order to read them back

\>>> fp.flush()

Copy to clipboard

Load the memmap and verify data was stored:

\>>> newfp \= np.memmap(filename, dtype\=np.float32, mode\='r', shape\=(3,4))
\>>> newfp
memmap(\[\[  0.,   1.,   2.,   3.\],\
        \[  4.,   5.,   6.,   7.\],\
        \[  8.,   9.,  10.,  11.\]\], dtype=float32)

Copy to clipboard

Read-only memmap:

\>>> fpr \= np.memmap(filename, dtype\=np.float32, mode\='r', shape\=(3,4))
\>>> fpr.flags.writeable
False

Copy to clipboard

Copy-on-write memmap:

\>>> fpc \= np.memmap(filename, dtype\=np.float32, mode\='c', shape\=(3,4))
\>>> fpc.flags.writeable
True

Copy to clipboard

It’s possible to assign to copy-on-write array, but values are only written into the memory copy of the array, and not written to disk:

\>>> fpc
memmap(\[\[  0.,   1.,   2.,   3.\],\
        \[  4.,   5.,   6.,   7.\],\
        \[  8.,   9.,  10.,  11.\]\], dtype=float32)
\>>> fpc\[0,:\] \= 0
\>>> fpc
memmap(\[\[  0.,   0.,   0.,   0.\],\
        \[  4.,   5.,   6.,   7.\],\
        \[  8.,   9.,  10.,  11.\]\], dtype=float32)

Copy to clipboard

File on disk is unchanged:

\>>> fpr
memmap(\[\[  0.,   1.,   2.,   3.\],\
        \[  4.,   5.,   6.,   7.\],\
        \[  8.,   9.,  10.,  11.\]\], dtype=float32)

Copy to clipboard

Offset into a memmap:

\>>> fpo \= np.memmap(filename, dtype\=np.float32, mode\='r', offset\=16)
\>>> fpo
memmap(\[  4.,   5.,   6.,   7.,   8.,   9.,  10.,  11.\], dtype=float32)

Copy to clipboard

Go BackOpen In Tab

On this page