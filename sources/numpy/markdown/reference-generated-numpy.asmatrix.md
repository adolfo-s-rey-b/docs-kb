[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.asmatrix.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.asmatrix.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.asmatrix.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.asmatrix.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.asmatrix.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.asmatrix.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.asmatrix.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.asmatrix.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.asmatrix.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.asmatrix.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.asmatrix.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.asmatrix.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.asmatrix.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.asmatrix.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.asmatrix.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.asmatrix.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.asmatrix.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.asmatrix.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.asmatrix.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.asmatrix.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.asmatrix.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.asmatrix.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.asmatrix[#](https://numpy.org/doc/stable/reference/generated/numpy.asmatrix.html#numpy-asmatrix "Link to this heading")

==============================================================================================================================

numpy.asmatrix(_data_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matrixlib/defmatrix.py#L36-L70)
[#](https://numpy.org/doc/stable/reference/generated/numpy.asmatrix.html#numpy.asmatrix "Link to this definition")

Interpret the input as a matrix.

Unlike [`matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
, [`asmatrix`](https://numpy.org/doc/stable/reference/generated/numpy.asmatrix.html#numpy.asmatrix "numpy.asmatrix")
 does not make a copy if the input is already a matrix or an ndarray. Equivalent to `matrix(data, copy=False)`.

Parameters:

**data**array\_like

Input data.

**dtype**data-type

Data-type of the output matrix.

Returns:

**mat**matrix

_data_ interpreted as a matrix.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[\[1, 2\], \[3, 4\]\])

Copy to clipboard

\>>> m \= np.asmatrix(x)

Copy to clipboard

\>>> x\[0,0\] \= 5

Copy to clipboard

\>>> m
matrix(\[\[5, 2\],\
        \[3, 4\]\])

Copy to clipboard

Go BackOpen In Tab

On this page