[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ndarray.flatten.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ndarray.flatten.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ndarray.flatten.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ndarray.flatten.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ndarray.flatten.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ndarray.flatten.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ndarray.flatten.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ndarray.flatten.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ndarray.flatten.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ndarray.flatten.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ndarray.flatten.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ndarray.flatten.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ndarray.flatten.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ndarray.flatten.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ndarray.flatten.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ndarray.flatten.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ndarray.flatten.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ndarray.flatten.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ndarray.flatten.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ndarray.flatten.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndarray.flatten[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy-ndarray-flatten "Link to this heading")

===================================================================================================================================================

method

ndarray.flatten(_order\='C'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "Link to this definition")

Return a copy of the array collapsed into one dimension.

Parameters:

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

‘C’ means to flatten in row-major (C-style) order. ‘F’ means to flatten in column-major (Fortran- style) order. ‘A’ means to flatten in column-major order if _a_ is Fortran _contiguous_ in memory, row-major order otherwise. ‘K’ means to flatten _a_ in the order the elements occur in memory. The default is ‘C’.

Returns:

**y**ndarray

A copy of the input array, flattened to one dimension.

See also

[`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")

Return a flattened array.

[`flat`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat "numpy.ndarray.flat")

A 1-D flat iterator over the array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1,2\], \[3,4\]\])
\>>> a.flatten()
array(\[1, 2, 3, 4\])
\>>> a.flatten('F')
array(\[1, 3, 2, 4\])

Copy to clipboard

Go BackOpen In Tab

On this page