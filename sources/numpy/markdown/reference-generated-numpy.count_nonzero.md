[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.count_nonzero.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.count_nonzero.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.count_nonzero.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.count_nonzero.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.count_nonzero.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.count_nonzero.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.count_nonzero.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.count_nonzero.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.count_nonzero.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.count_nonzero.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.count_nonzero.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.count_nonzero.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.count_nonzero.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.count_nonzero.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.count_nonzero.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.count_nonzero.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.count_nonzero.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.count_nonzero.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.count_nonzero.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.count_nonzero.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.count\_nonzero[#](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html#numpy-count-nonzero "Link to this heading")

==============================================================================================================================================

numpy.count\_nonzero(_a_, _axis\=None_, _\*_, _keepdims\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L483-L545)
[#](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html#numpy.count_nonzero "Link to this definition")

Counts the number of non-zero values in the array `a`.

A non-zero value is one that evaluates to truthful in a boolean context, including any non-zero number and any string that is not empty. This function recursively counts how many elements in `a` (and its sub-arrays) are non-zero values.

Parameters:

**a**array\_like

The array for which to count non-zeros.

**axis**int or tuple, optional

Axis or tuple of axes along which to count non-zeros. Default is None, meaning that non-zeros will be counted along a flattened version of `a`.

**keepdims**bool, optional

If this is set to True, the axes that are counted are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

Returns:

**count**int or array of int

Number of non-zero values in the array along a given axis. Otherwise, the total number of non-zero values in the array is returned.

See also

[`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")

Return the coordinates of all the non-zero values.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.count\_nonzero(np.eye(4))
np.int64(4)
\>>> a \= np.array(\[\[0, 1, 7, 0\],\
...               \[3, 0, 2, 19\]\])
\>>> np.count\_nonzero(a)
np.int64(5)
\>>> np.count\_nonzero(a, axis\=0)
array(\[1, 1, 2, 1\])
\>>> np.count\_nonzero(a, axis\=1)
array(\[2, 3\])
\>>> np.count\_nonzero(a, axis\=1, keepdims\=True)
array(\[\[2\],\
       \[3\]\])

Copy to clipboard

Go BackOpen In Tab

On this page