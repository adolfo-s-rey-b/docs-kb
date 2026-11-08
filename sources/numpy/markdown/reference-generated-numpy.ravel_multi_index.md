[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ravel_multi_index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ravel_multi_index.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ravel_multi_index.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ravel_multi_index.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ravel_multi_index.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ravel_multi_index.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ravel_multi_index.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ravel_multi_index.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ravel_multi_index.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ravel_multi_index.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ravel_multi_index.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ravel_multi_index.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ravel_multi_index.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ravel_multi_index.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ravel_multi_index.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ravel_multi_index.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ravel_multi_index.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ravel_multi_index.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ravel_multi_index.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ravel_multi_index.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ravel_multi_index.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ravel_multi_index.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ravel\_multi\_index[#](https://numpy.org/doc/stable/reference/generated/numpy.ravel_multi_index.html#numpy-ravel-multi-index "Link to this heading")

===========================================================================================================================================================

numpy.ravel\_multi\_index(_multi\_index_, _dims_, _mode\='raise'_, _order\='C'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ravel_multi_index.html#numpy.ravel_multi_index "Link to this definition")

Converts a tuple of index arrays into an array of flat indices, applying boundary modes to the multi-index.

Parameters:

**multi\_index**tuple of array\_like

A tuple of integer arrays, one array for each dimension.

**dims**tuple of ints

The shape of array into which the indices from `multi_index` apply.

**mode**{‘raise’, ‘wrap’, ‘clip’}, optional

Specifies how out-of-bounds indices are handled. Can specify either one mode or a tuple of modes, one mode per index.

*   ‘raise’ – raise an error (default)
    
*   ‘wrap’ – wrap around
    
*   ‘clip’ – clip to the range
    

In ‘clip’ mode, a negative index which would normally wrap will clip to 0 instead.

**order**{‘C’, ‘F’}, optional

Determines whether the multi-index should be viewed as indexing in row-major (C-style) or column-major (Fortran-style) order.

Returns:

**raveled\_indices**ndarray

An array of indices into the flattened version of an array of dimensions `dims`.

See also

[`unravel_index`](https://numpy.org/doc/stable/reference/generated/numpy.unravel_index.html#numpy.unravel_index "numpy.unravel_index")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= np.array(\[\[3,6,6\],\[4,5,1\]\])
\>>> np.ravel\_multi\_index(arr, (7,6))
array(\[22, 41, 37\])
\>>> np.ravel\_multi\_index(arr, (7,6), order\='F')
array(\[31, 41, 13\])
\>>> np.ravel\_multi\_index(arr, (4,6), mode\='clip')
array(\[22, 23, 19\])
\>>> np.ravel\_multi\_index(arr, (4,4), mode\=('clip','wrap'))
array(\[12, 13, 13\])

Copy to clipboard

\>>> np.ravel\_multi\_index((3,1,4,1), (6,7,8,9))
1621

Copy to clipboard

Go BackOpen In Tab

On this page