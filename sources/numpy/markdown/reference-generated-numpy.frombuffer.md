[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.frombuffer.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.frombuffer.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.frombuffer.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.frombuffer.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.frombuffer.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.frombuffer.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.frombuffer.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.frombuffer.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.frombuffer.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.frombuffer.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.frombuffer.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.frombuffer.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.frombuffer.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.frombuffer.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.frombuffer.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.frombuffer.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.frombuffer.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.frombuffer.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.frombuffer.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.frombuffer[#](https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html#numpy-frombuffer "Link to this heading")

====================================================================================================================================

numpy.frombuffer(_buffer_, _dtype\=np.float64_, _count\=\-1_, _offset\=0_, _\*_, _like\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html#numpy.frombuffer "Link to this definition")

Interpret a buffer as a 1-dimensional array.

Parameters:

**buffer**buffer\_like

An object that exposes the buffer interface.

**dtype**data-type, optional

Data-type of the returned array. Default is [`numpy.float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
.

**count**int, optional

Number of items to read. `-1` means all data in the buffer.

**offset**int, optional

Start reading the buffer from this offset (in bytes); default: 0.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**ndarray

See also

[`ndarray.tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes "numpy.ndarray.tobytes")

Inverse of this operation, construct Python bytes from the raw data bytes in the array.

Notes

If the buffer has data that is not in machine byte-order, this should be specified as part of the data-type, e.g.:

\>>> dt \= np.dtype(np.int\_)
\>>> dt \= dt.newbyteorder('>')
\>>> np.frombuffer(buf, dtype\=dt) 

Copy to clipboard

The data of the resulting array will not be byteswapped, but will be interpreted correctly.

This function creates a view into the original object. This should be safe in general, but it may make sense to copy the result when the original object is mutable or untrusted.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> s \= b'hello world'
\>>> np.frombuffer(s, dtype\='S1', count\=5, offset\=6)
array(\[b'w', b'o', b'r', b'l', b'd'\], dtype='|S1')

Copy to clipboard

\>>> np.frombuffer(b'\\x01\\x02', dtype\=np.uint8)
array(\[1, 2\], dtype=uint8)
\>>> np.frombuffer(b'\\x01\\x02\\x03\\x04\\x05', dtype\=np.uint8, count\=3)
array(\[1, 2, 3\], dtype=uint8)

Copy to clipboard

Go BackOpen In Tab

On this page