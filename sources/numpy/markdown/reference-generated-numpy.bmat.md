[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.bmat.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.bmat.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.bmat.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.bmat.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.bmat.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.bmat.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.bmat.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.bmat.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.bmat.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.bmat.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.bmat.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.bmat.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.bmat.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.bmat.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.bmat.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.bmat.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.bmat.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.bmat.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.bmat.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.bmat.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.bmat.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.bmat.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.bmat[#](https://numpy.org/doc/stable/reference/generated/numpy.bmat.html#numpy-bmat "Link to this heading")

==================================================================================================================

numpy.bmat(_obj_, _ldict\=None_, _gdict\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L1040-L1117)
[#](https://numpy.org/doc/stable/reference/generated/numpy.bmat.html#numpy.bmat "Link to this definition")

Build a matrix object from a string, nested sequence, or array.

Parameters:

**obj**str or array\_like

Input data. If a string, variables in the current scope may be referenced by name.

**ldict**dict, optional

A dictionary that replaces local operands in current frame. Ignored if _obj_ is not a string or _gdict_ is None.

**gdict**dict, optional

A dictionary that replaces global operands in current frame. Ignored if _obj_ is not a string.

Returns:

**out**matrix

Returns a matrix object, which is a specialized 2-D array.

See also

[`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")

A generalization of this function for N-d arrays, that returns normal ndarrays.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> A \= np.asmatrix('1 1; 1 1')
\>>> B \= np.asmatrix('2 2; 2 2')
\>>> C \= np.asmatrix('3 4; 5 6')
\>>> D \= np.asmatrix('7 8; 9 0')

Copy to clipboard

All the following expressions construct the same block matrix:

\>>> np.bmat(\[\[A, B\], \[C, D\]\])
matrix(\[\[1, 1, 2, 2\],\
        \[1, 1, 2, 2\],\
        \[3, 4, 7, 8\],\
        \[5, 6, 9, 0\]\])
\>>> np.bmat(np.r\_\[np.c\_\[A, B\], np.c\_\[C, D\]\])
matrix(\[\[1, 1, 2, 2\],\
        \[1, 1, 2, 2\],\
        \[3, 4, 7, 8\],\
        \[5, 6, 9, 0\]\])
\>>> np.bmat('A,B; C,D')
matrix(\[\[1, 1, 2, 2\],\
        \[1, 1, 2, 2\],\
        \[3, 4, 7, 8\],\
        \[5, 6, 9, 0\]\])

Copy to clipboard

Go BackOpen In Tab

On this page