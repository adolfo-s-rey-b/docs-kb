[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.base_repr.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.base_repr.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.base_repr.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.base_repr.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.base_repr.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.base_repr.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.base_repr.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.base_repr.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.base_repr.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.base_repr.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.base_repr.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.base_repr.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.base_repr.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.base_repr.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.base_repr.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.base_repr.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.base_repr.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.base_repr.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.base_repr.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.base_repr.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.base\_repr[#](https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html#numpy-base-repr "Link to this heading")

==================================================================================================================================

numpy.base\_repr(_number_, _base\=2_, _padding\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L2104-L2159)
[#](https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html#numpy.base_repr "Link to this definition")

Return a string representation of a number in the given base system.

Parameters:

**number**int

The value to convert. Positive and negative values are handled.

**base**int, optional

Convert [`number`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.number "numpy.number")
 to the _base_ number system. The valid range is 2-36, the default value is 2.

**padding**int, optional

Number of zeros padded on the left. Default is 0 (no padding).

Returns:

**out**str

String representation of [`number`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.number "numpy.number")
 in _base_ system.

See also

[`binary_repr`](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#numpy.binary_repr "numpy.binary_repr")

Faster version of [`base_repr`](https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html#numpy.base_repr "numpy.base_repr")
 for base 2.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.base\_repr(5)
'101'
\>>> np.base\_repr(6, 5)
'11'
\>>> np.base\_repr(7, base\=5, padding\=3)
'00012'

Copy to clipboard

\>>> np.base\_repr(10, base\=16)
'A'
\>>> np.base\_repr(32, base\=16)
'20'

Copy to clipboard

Go BackOpen In Tab

On this page