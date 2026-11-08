[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matlib.repmat.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matlib.repmat.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matlib.repmat.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matlib.repmat.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matlib.repmat.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matlib.repmat.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matlib.repmat.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matlib.repmat.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matlib.repmat.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matlib.repmat.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matlib.repmat.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matlib.repmat.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matlib.repmat.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matlib.repmat.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matlib.repmat.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matlib.repmat.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matlib.repmat.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matlib.repmat.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matlib.repmat.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matlib.repmat.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matlib.repmat.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matlib.repmat.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matlib.repmat[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.repmat.html#numpy-matlib-repmat "Link to this heading")

=============================================================================================================================================

matlib.repmat(_a_, _m_, _n_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matlib.py#L332-L380)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.repmat.html#numpy.matlib.repmat "Link to this definition")

Repeat a 0-D to 2-D array or matrix MxN times.

Parameters:

**a**array\_like

The array or matrix to be repeated.

**m, n**int

The number of times _a_ is repeated along the first and second axes.

Returns:

**out**ndarray

The result of repeating _a_.

Examples

Try it in your browser!

\>>> import numpy.matlib
\>>> a0 \= np.array(1)
\>>> np.matlib.repmat(a0, 2, 3)
array(\[\[1, 1, 1\],\
       \[1, 1, 1\]\])

Copy to clipboard

\>>> a1 \= np.arange(4)
\>>> np.matlib.repmat(a1, 2, 2)
array(\[\[0, 1, 2, 3, 0, 1, 2, 3\],\
       \[0, 1, 2, 3, 0, 1, 2, 3\]\])

Copy to clipboard

\>>> a2 \= np.asmatrix(np.arange(6).reshape(2, 3))
\>>> np.matlib.repmat(a2, 2, 3)
matrix(\[\[0, 1, 2, 0, 1, 2, 0, 1, 2\],\
        \[3, 4, 5, 3, 4, 5, 3, 4, 5\],\
        \[0, 1, 2, 0, 1, 2, 0, 1, 2\],\
        \[3, 4, 5, 3, 4, 5, 3, 4, 5\]\])

Copy to clipboard

Go BackOpen In Tab

On this page