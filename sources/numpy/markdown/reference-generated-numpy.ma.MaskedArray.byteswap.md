[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.byteswap.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.byteswap.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.byteswap.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.byteswap[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.byteswap.html#numpy-ma-maskedarray-byteswap "Link to this heading")

===========================================================================================================================================================================

method

ma.MaskedArray.byteswap(_inplace\=False_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.byteswap.html#numpy.ma.MaskedArray.byteswap "Link to this definition")

Swap the bytes of the array elements

Toggle between low-endian and big-endian data representation by returning a byteswapped array, optionally swapped in-place. Arrays of byte-strings are not swapped. The real and imaginary parts of a complex number are swapped individually.

Parameters:

**inplace**bool, optional

If `True`, swap bytes in-place, default is `False`.

Returns:

**out**ndarray

The byteswapped array. If _inplace_ is `True`, this is a view to self.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> A \= np.array(\[1, 256, 8755\], dtype\=np.int16)
\>>> list(map(hex, A))
\['0x1', '0x100', '0x2233'\]
\>>> A.byteswap(inplace\=True)
array(\[  256,     1, 13090\], dtype=int16)
\>>> list(map(hex, A))
\['0x100', '0x1', '0x3322'\]

Copy to clipboard

Arrays of byte-strings are not swapped

\>>> A \= np.array(\[b'ceg', b'fac'\])
\>>> A.byteswap()
array(\[b'ceg', b'fac'\], dtype='|S3')

Copy to clipboard

`A.view(A.dtype.newbyteorder()).byteswap()` produces an array with the same values but different representation in memory

\>>> A \= np.array(\[1, 2, 3\],dtype\=np.int64)
\>>> A.view(np.uint8)
array(\[1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0,\
       0, 0\], dtype=uint8)
\>>> A.view(A.dtype.newbyteorder()).byteswap(inplace\=True)
array(\[1, 2, 3\], dtype='>i8')
\>>> A.view(np.uint8)
array(\[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,\
       0, 3\], dtype=uint8)

Copy to clipboard

Go BackOpen In Tab

On this page