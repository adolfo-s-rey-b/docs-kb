[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.normalize_axis_index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.array_utils.normalize_axis_index.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.array\_utils.normalize\_axis\_index[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.normalize_axis_index.html#numpy-lib-array-utils-normalize-axis-index "Link to this heading")

=====================================================================================================================================================================================================================

lib.array\_utils.normalize\_axis\_index(_axis_, _ndim_, _msg\_prefix\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.array_utils.normalize_axis_index.html#numpy.lib.array_utils.normalize_axis_index "Link to this definition")

Normalizes an axis index, _axis_, such that is a valid positive index into the shape of array with [`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "numpy.ndim")
 dimensions. Raises an AxisError with an appropriate message if this is not possible.

Used internally by all axis-checking logic.

Parameters:

**axis**int

The un-normalized index of the axis. Can be negative

**ndim**int

The number of dimensions of the array that _axis_ should be normalized against

**msg\_prefix**str

A prefix to put before the message, typically the name of the argument

Returns:

**normalized\_axis**int

The normalized axis index, such that _0 <= normalized\_axis < ndim_

Raises:

AxisError

If the axis index is invalid, when _\-ndim <= axis < ndim_ is false.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib.array\_utils import normalize\_axis\_index
\>>> normalize\_axis\_index(0, ndim\=3)
0
\>>> normalize\_axis\_index(1, ndim\=3)
1
\>>> normalize\_axis\_index(\-1, ndim\=3)
2

Copy to clipboard

\>>> normalize\_axis\_index(3, ndim\=3)
Traceback (most recent call last):
...
numpy.exceptions.AxisError: axis 3 is out of bounds for array ...
\>>> normalize\_axis\_index(\-4, ndim\=3, msg\_prefix\='axes\_arg')
Traceback (most recent call last):
...
numpy.exceptions.AxisError: axes\_arg: axis -4 is out of bounds ...

Copy to clipboard

Go BackOpen In Tab

On this page