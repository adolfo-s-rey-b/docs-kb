[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.flatnonzero.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.flatnonzero.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.flatnonzero.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.flatnonzero.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.flatnonzero.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.flatnonzero.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.flatnonzero.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.flatnonzero.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.flatnonzero.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.flatnonzero.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.flatnonzero.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.flatnonzero.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.flatnonzero.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.flatnonzero.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.flatnonzero.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.flatnonzero.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.flatnonzero.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.flatnonzero.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.flatnonzero.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.flatnonzero.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.flatnonzero[#](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy-flatnonzero "Link to this heading")

=======================================================================================================================================

numpy.flatnonzero(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L674-L713)
[#](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "Link to this definition")

Return indices that are non-zero in the flattened version of a.

This is equivalent to `np.nonzero(np.ravel(a))[0]`.

Parameters:

**a**array\_like

Input data.

Returns:

**res**ndarray

Output array, containing the indices of the elements of `a.ravel()` that are non-zero.

See also

[`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")

Return the indices of the non-zero elements of the input array.

[`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")

Return a 1-D array containing the elements of the input array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(\-2, 3)
\>>> x
array(\[-2, -1,  0,  1,  2\])
\>>> np.flatnonzero(x)
array(\[0, 1, 3, 4\])

Copy to clipboard

Use the indices of the non-zero elements as an index array to extract these elements:

\>>> x.ravel()\[np.flatnonzero(x)\]
array(\[-2, -1,  1,  2\])

Copy to clipboard

Go BackOpen In Tab

On this page