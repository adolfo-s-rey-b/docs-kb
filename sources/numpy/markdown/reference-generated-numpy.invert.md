[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.invert.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.invert.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.invert.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.invert.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.invert.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.invert.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.invert.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.invert.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.invert.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.invert.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.invert.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.invert.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.invert.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.invert.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.invert.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.invert.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.invert.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.invert.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.invert.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.invert.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.invert.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.invert[#](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#numpy-invert "Link to this heading")

========================================================================================================================

numpy.invert(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'invert'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#numpy.invert "Link to this definition")

Compute bit-wise inversion, or bit-wise NOT, element-wise.

Computes the bit-wise NOT of the underlying binary representation of the integers in the input arrays. This ufunc implements the C/Python operator `~`.

For signed integer inputs, the bit-wise NOT of the absolute value is returned. In a two’s-complement system, this operation effectively flips all the bits, resulting in a representation that corresponds to the negative of the input plus one. This is the most common method of representing signed integers on computers [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#rde927b304c4f-1)
. An N-bit two’s-complement system can represent every integer in the range \\(-2^{N-1}\\) to \\(+2^{N-1}-1\\).

Parameters:

**x**array\_like

Only integer and boolean types are handled.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**out**ndarray or scalar

Result. This is a scalar if _x_ is a scalar.

See also

[`bitwise_and`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_and.html#numpy.bitwise_and "numpy.bitwise_and")
, [`bitwise_or`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_or.html#numpy.bitwise_or "numpy.bitwise_or")
, [`bitwise_xor`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_xor.html#numpy.bitwise_xor "numpy.bitwise_xor")

[`logical_not`](https://numpy.org/doc/stable/reference/generated/numpy.logical_not.html#numpy.logical_not "numpy.logical_not")

[`binary_repr`](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#numpy.binary_repr "numpy.binary_repr")

Return the binary representation of the input number as a string.

Notes

`numpy.bitwise_not` is an alias for [`invert`](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#numpy.invert "numpy.invert")
:

\>>> np.bitwise\_not is np.invert
True

Copy to clipboard

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#id1)\
\]

Wikipedia, “Two’s complement”, [https://en.wikipedia.org/wiki/Two’s\_complement](https://en.wikipedia.org/wiki/Two's_complement)

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

We’ve seen that 13 is represented by `00001101`. The invert or bit-wise NOT of 13 is then:

\>>> x \= np.invert(np.array(13, dtype\=np.uint8))
\>>> x
np.uint8(242)
\>>> np.binary\_repr(x, width\=8)
'11110010'

Copy to clipboard

The result depends on the bit-width:

\>>> x \= np.invert(np.array(13, dtype\=np.uint16))
\>>> x
np.uint16(65522)
\>>> np.binary\_repr(x, width\=16)
'1111111111110010'

Copy to clipboard

When using signed integer types, the result is the bit-wise NOT of the unsigned type, interpreted as a signed integer:

\>>> np.invert(np.array(\[13\], dtype\=np.int8))
array(\[-14\], dtype=int8)
\>>> np.binary\_repr(\-14, width\=8)
'11110010'

Copy to clipboard

Booleans are accepted as well:

\>>> np.invert(np.array(\[True, False\]))
array(\[False,  True\])

Copy to clipboard

The `~` operator can be used as a shorthand for `np.invert` on ndarrays.

\>>> x1 \= np.array(\[True, False\])
\>>> ~x1
array(\[False,  True\])

Copy to clipboard

Go BackOpen In Tab

On this page