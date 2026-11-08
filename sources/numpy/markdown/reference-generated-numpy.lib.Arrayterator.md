[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.Arrayterator.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.Arrayterator.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.Arrayterator.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.Arrayterator.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.Arrayterator.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.Arrayterator.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.Arrayterator.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.Arrayterator.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.Arrayterator.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.Arrayterator.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.Arrayterator.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.Arrayterator.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.Arrayterator.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.Arrayterator.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.Arrayterator.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.Arrayterator.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.Arrayterator.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.Arrayterator.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.Arrayterator.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.Arrayterator.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.Arrayterator.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.Arrayterator.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.Arrayterator[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.Arrayterator.html#numpy-lib-arrayterator "Link to this heading")

======================================================================================================================================================

_class_ numpy.lib.Arrayterator(_var_, _buf\_size\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/__init__.py)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.Arrayterator.html#numpy.lib.Arrayterator "Link to this definition")

Buffered iterator for big arrays.

[`Arrayterator`](https://numpy.org/doc/stable/reference/generated/numpy.lib.Arrayterator.html#numpy.lib.Arrayterator "numpy.lib.Arrayterator")
 creates a buffered iterator for reading big arrays in small contiguous blocks. The class is useful for objects stored in the file system. It allows iteration over the object _without_ reading everything in memory; instead, small blocks are read and iterated over.

[`Arrayterator`](https://numpy.org/doc/stable/reference/generated/numpy.lib.Arrayterator.html#numpy.lib.Arrayterator "numpy.lib.Arrayterator")
 can be used with any object that supports multidimensional slices. This includes NumPy arrays, but also variables from Scientific.IO.NetCDF or pynetcdf for example.

Parameters:

**var**array\_like

The object to iterate over.

**buf\_size**int, optional

The buffer size. If _buf\_size_ is supplied, the maximum amount of data that will be read into memory is _buf\_size_ elements. Default is None, which will read as many element as possible into memory.

Attributes:

**var**

**buf\_size**

**start**

**stop**

**step**

[`shape`](https://numpy.org/doc/stable/reference/generated/numpy.lib.Arrayterator.shape.html#numpy.lib.Arrayterator.shape "numpy.lib.Arrayterator.shape")

The shape of the array to be iterated over.

[`flat`](https://numpy.org/doc/stable/reference/generated/numpy.lib.Arrayterator.flat.html#numpy.lib.Arrayterator.flat "numpy.lib.Arrayterator.flat")

A 1-D flat iterator for Arrayterator objects.

See also

[`numpy.ndenumerate`](https://numpy.org/doc/stable/reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "numpy.ndenumerate")

Multidimensional array iterator.

[`numpy.flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")

Flat array iterator.

[`numpy.memmap`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap")

Create a memory-map to an array stored in a binary file on disk.

Notes

The algorithm works by first finding a “running dimension”, along which the blocks will be extracted. Given an array of dimensions `(d1, d2, ..., dn)`, e.g. if _buf\_size_ is smaller than `d1`, the first dimension will be used. If, on the other hand, `d1 < buf_size < d1*d2` the second dimension will be used, and so on. Blocks are extracted along this dimension, and when the last block is returned the process continues from the next dimension, until all elements have been read.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(3 \* 4 \* 5 \* 6).reshape(3, 4, 5, 6)
\>>> a\_itor \= np.lib.Arrayterator(a, 2)
\>>> a\_itor.shape
(3, 4, 5, 6)

Copy to clipboard

Now we can iterate over `a_itor`, and it will return arrays of size two. Since _buf\_size_ was smaller than any dimension, the first dimension will be iterated over first:

\>>> for subarr in a\_itor:
...     if not subarr.all():
...         print(subarr, subarr.shape) 
\>>> \# \[\[\[\[0 1\]\]\]\] (1, 1, 1, 2)

Copy to clipboard

Go BackOpen In Tab

On this page