[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matlib.identity.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.matlib.identity.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.matlib.identity.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.matlib.identity.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.matlib.identity.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.matlib.identity.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.matlib.identity.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.matlib.identity.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.matlib.identity.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.matlib.identity.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.matlib.identity.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.matlib.identity.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.matlib.identity.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.matlib.identity.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.matlib.identity.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.matlib.identity.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.matlib.identity.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.matlib.identity.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.matlib.identity.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.matlib.identity.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.matlib.identity.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.matlib.identity.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.matlib.identity[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.identity.html#numpy-matlib-identity "Link to this heading")

===================================================================================================================================================

matlib.identity(_n_, _dtype\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/matlib.py#L155-L189)
[#](https://numpy.org/doc/stable/reference/generated/numpy.matlib.identity.html#numpy.matlib.identity "Link to this definition")

Returns the square identity matrix of given size.

Parameters:

**n**int

Size of the returned identity matrix.

**dtype**data-type, optional

Data-type of the output. Defaults to `float`.

Returns:

**out**matrix

_n_ x _n_ matrix with its main diagonal set to one, and all other elements zero.

See also

[`numpy.identity`](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy.identity "numpy.identity")

Equivalent array function.

[`matlib.eye`](https://numpy.org/doc/stable/reference/generated/numpy.matlib.eye.html#numpy.matlib.eye "numpy.matlib.eye")

More general matrix identity function.

Examples

Try it in your browser!

\>>> import numpy.matlib
\>>> np.matlib.identity(3, dtype\=np.int\_)
matrix(\[\[1, 0, 0\],\
        \[0, 1, 0\],\
        \[0, 0, 1\]\])

Copy to clipboard

Go BackOpen In Tab

On this page