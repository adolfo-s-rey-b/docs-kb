[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.promote_types.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.promote_types.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.promote_types.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.promote_types.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.promote_types.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.promote_types.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.promote_types.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.promote_types.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.promote_types.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.promote_types.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.promote_types.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.promote_types.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.promote_types.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.promote_types.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.promote_types.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.promote_types.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.promote_types.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.promote_types.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.promote_types.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.promote_types.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.promote_types.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.promote_types.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.promote\_types[#](https://numpy.org/doc/stable/reference/generated/numpy.promote_types.html#numpy-promote-types "Link to this heading")

==============================================================================================================================================

numpy.promote\_types(_type1_, _type2_, _/_)[#](https://numpy.org/doc/stable/reference/generated/numpy.promote_types.html#numpy.promote_types "Link to this definition")

Returns the data type with the smallest size and smallest scalar kind to which both `type1` and `type2` may be safely cast. The returned data type is always considered “canonical”, this mainly means that the promoted dtype will always be in native byte order.

This function is symmetric, but rarely associative.

Parameters:

**type1**dtype or dtype specifier

First data type.

**type2**dtype or dtype specifier

Second data type.

Returns:

**out**dtype

The promoted data type.

See also

[`result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")
, [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, [`can_cast`](https://numpy.org/doc/stable/reference/generated/numpy.can_cast.html#numpy.can_cast "numpy.can_cast")

Notes

Please see [`numpy.result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")
 for additional information about promotion.

Starting in NumPy 1.9, promote\_types function now returns a valid string length when given an integer or float dtype as one argument and a string dtype as another argument. Previously it always returned the input string dtype, even if it wasn’t long enough to store the max integer/float value converted to a string.

Changed in version 1.23.0.

NumPy now supports promotion for more structured dtypes. It will now remove unnecessary padding from a structure dtype and promote included fields individually.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.promote\_types(np.float32, np.float64)
dtype('float64')

Copy to clipboard

\>>> np.promote\_types(np.int64, np.float32)
dtype('float64')

Copy to clipboard

\>>> np.promote\_types('>i8', '<c8')
dtype('complex128')

Copy to clipboard

\>>> np.promote\_types(np.int32, 'S8')
dtype('S11')

Copy to clipboard

An example of a non-associative case:

\>>> p \= np.promote\_types
\>>> p('S', p('i1', 'u1'))
dtype('S6')
\>>> p(p('S', 'i1'), 'u1')
dtype('S4')

Copy to clipboard

Go BackOpen In Tab

On this page