[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.binary_repr.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.binary_repr.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.binary_repr.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.binary_repr.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.binary_repr.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.binary_repr.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.binary_repr.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.binary_repr.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.binary_repr.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.binary_repr.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.binary_repr.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.binary_repr.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.binary_repr.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.binary_repr.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.binary_repr.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.binary_repr.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.binary_repr.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.binary_repr.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.binary_repr.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.binary_repr.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.binary\_repr[#](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#numpy-binary-repr "Link to this heading")

========================================================================================================================================

numpy.binary\_repr(_num_, _width\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L1997-L2101)
[#](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#numpy.binary_repr "Link to this definition")

Return the binary representation of the input number as a string.

For negative numbers, if width is not given, a minus sign is added to the front. If width is given, the two’s complement of the number is returned, with respect to that width.

In a two’s-complement system negative numbers are represented by the two’s complement of the absolute value. This is the most common method of representing signed integers on computers [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#r962252997619-1)
. An N-bit two’s-complement system can represent every integer in the range to +2^{N-1}-1.

Parameters:

**num**int

Only an integer decimal number can be used.

**width**int, optional

The length of the returned string if _num_ is positive, or the length of the two’s complement if _num_ is negative, provided that _width_ is at least a sufficient number of bits for _num_ to be represented in the designated form. If the _width_ value is insufficient, an error is raised.

Returns:

**bin**str

Binary representation of _num_ or two’s complement of _num_.

See also

[`base_repr`](https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html#numpy.base_repr "numpy.base_repr")

Return a string representation of a number in the given base system.

[`bin`](https://docs.python.org/3/library/functions.html#bin "(in Python v3.14)")

Python’s built-in binary representation generator of an integer.

Notes

[`binary_repr`](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#numpy.binary_repr "numpy.binary_repr")
 is equivalent to using [`base_repr`](https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html#numpy.base_repr "numpy.base_repr")
 with base 2, but about 25x faster.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#id1)\
\]

Wikipedia, “Two’s complement”, [https://en.wikipedia.org/wiki/Two’s\_complement](https://en.wikipedia.org/wiki/Two's_complement)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.binary\_repr(3)
'11'
\>>> np.binary\_repr(\-3)
'-11'
\>>> np.binary\_repr(3, width\=4)
'0011'

Copy to clipboard

The two’s complement is returned when the input number is negative and width is specified:

\>>> np.binary\_repr(\-3, width\=3)
'101'
\>>> np.binary\_repr(\-3, width\=5)
'11101'

Copy to clipboard

Go BackOpen In Tab

On this page