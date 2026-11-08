[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.roll.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.roll.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.roll.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.roll.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.roll.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.roll.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.roll.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.roll.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.roll.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.roll.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.roll.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.roll.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.roll.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.roll.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.roll.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.roll.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.roll.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.roll.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.roll.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.roll.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.roll.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.roll.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.roll[#](https://numpy.org/doc/stable/reference/generated/numpy.roll.html#numpy-roll "Link to this heading")

==================================================================================================================

numpy.roll(_a_, _shift_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L1225-L1328)
[#](https://numpy.org/doc/stable/reference/generated/numpy.roll.html#numpy.roll "Link to this definition")

Roll array elements along a given axis.

Elements that roll beyond the last position are re-introduced at the first.

Parameters:

**a**array\_like

Input array.

**shift**int or tuple of ints

The number of places by which elements are shifted. If a tuple, then _axis_ must be a tuple of the same size, and each of the given axes is shifted by the corresponding number. If an int while _axis_ is a tuple of ints, then the same value is used for all given axes.

**axis**int or tuple of ints, optional

Axis or axes along which elements are shifted. By default, the array is flattened before shifting, after which the original shape is restored.

Returns:

**res**ndarray

Output array, with the same shape as _a_.

See also

[`rollaxis`](https://numpy.org/doc/stable/reference/generated/numpy.rollaxis.html#numpy.rollaxis "numpy.rollaxis")

Roll the specified axis backwards, until it lies in a given position.

Notes

Supports rolling over multiple dimensions simultaneously.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(10)
\>>> np.roll(x, 2)
array(\[8, 9, 0, 1, 2, 3, 4, 5, 6, 7\])
\>>> np.roll(x, \-2)
array(\[2, 3, 4, 5, 6, 7, 8, 9, 0, 1\])

Copy to clipboard

\>>> x2 \= np.reshape(x, (2, 5))
\>>> x2
array(\[\[0, 1, 2, 3, 4\],\
       \[5, 6, 7, 8, 9\]\])
\>>> np.roll(x2, 1)
array(\[\[9, 0, 1, 2, 3\],\
       \[4, 5, 6, 7, 8\]\])
\>>> np.roll(x2, \-1)
array(\[\[1, 2, 3, 4, 5\],\
       \[6, 7, 8, 9, 0\]\])
\>>> np.roll(x2, 1, axis\=0)
array(\[\[5, 6, 7, 8, 9\],\
       \[0, 1, 2, 3, 4\]\])
\>>> np.roll(x2, \-1, axis\=0)
array(\[\[5, 6, 7, 8, 9\],\
       \[0, 1, 2, 3, 4\]\])
\>>> np.roll(x2, 1, axis\=1)
array(\[\[4, 0, 1, 2, 3\],\
       \[9, 5, 6, 7, 8\]\])
\>>> np.roll(x2, \-1, axis\=1)
array(\[\[1, 2, 3, 4, 0\],\
       \[6, 7, 8, 9, 5\]\])
\>>> np.roll(x2, (1, 1), axis\=(1, 0))
array(\[\[9, 5, 6, 7, 8\],\
       \[4, 0, 1, 2, 3\]\])
\>>> np.roll(x2, (2, 1), axis\=(1, 0))
array(\[\[8, 9, 5, 6, 7\],\
       \[3, 4, 0, 1, 2\]\])

Copy to clipboard

Go BackOpen In Tab

On this page