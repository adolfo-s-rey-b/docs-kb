[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.rollaxis.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.rollaxis.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.rollaxis.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.rollaxis.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.rollaxis.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.rollaxis.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.rollaxis.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.rollaxis.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.rollaxis.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.rollaxis.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.rollaxis.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.rollaxis.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.rollaxis.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.rollaxis.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.rollaxis.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.rollaxis.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.rollaxis.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.rollaxis.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.rollaxis.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.rollaxis.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.rollaxis.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.rollaxis.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.rollaxis[#](https://numpy.org/doc/stable/reference/generated/numpy.rollaxis.html#numpy-rollaxis "Link to this heading")

==============================================================================================================================

numpy.rollaxis(_a_, _axis_, _start\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L1335-L1423)
[#](https://numpy.org/doc/stable/reference/generated/numpy.rollaxis.html#numpy.rollaxis "Link to this definition")

Roll the specified axis backwards, until it lies in a given position.

This function continues to be supported for backward compatibility, but you should prefer [`moveaxis`](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html#numpy.moveaxis "numpy.moveaxis")
. The [`moveaxis`](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html#numpy.moveaxis "numpy.moveaxis")
 function was added in NumPy 1.11.

Parameters:

**a**ndarray

Input array.

**axis**int

The axis to be rolled. The positions of the other axes do not change relative to one another.

**start**int, optional

When `start <= axis`, the axis is rolled back until it lies in this position. When `start > axis`, the axis is rolled until it lies before this position. The default, 0, results in a “complete” roll. The following table describes how negative values of `start` are interpreted:

| `start` | Normalized `start` |
| --- | --- |
| `-(arr.ndim+1)` | raise `AxisError` |
| `-arr.ndim` | 0   |
| ⋮   | ⋮   |
| `-1` | `arr.ndim-1` |
| `0` | `0` |
| ⋮   | ⋮   |
| `arr.ndim` | `arr.ndim` |
| `arr.ndim + 1` | raise `AxisError` |

Returns:

**res**ndarray

For NumPy >= 1.10.0 a view of _a_ is always returned. For earlier NumPy versions a view of _a_ is returned only if the order of the axes is changed, otherwise the input array is returned.

See also

[`moveaxis`](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html#numpy.moveaxis "numpy.moveaxis")

Move array axes to new positions.

[`roll`](https://numpy.org/doc/stable/reference/generated/numpy.roll.html#numpy.roll "numpy.roll")

Roll the elements of an array by a number of positions along a given axis.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ones((3,4,5,6))
\>>> np.rollaxis(a, 3, 1).shape
(3, 6, 4, 5)
\>>> np.rollaxis(a, 2).shape
(5, 3, 4, 6)
\>>> np.rollaxis(a, 1, 4).shape
(3, 5, 6, 4)

Copy to clipboard

Go BackOpen In Tab

On this page