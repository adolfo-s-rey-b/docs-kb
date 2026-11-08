[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.identity.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ufunc.identity.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.identity.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ufunc.identity.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ufunc.identity.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ufunc.identity.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ufunc.identity.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ufunc.identity.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ufunc.identity.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ufunc.identity.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ufunc.identity.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ufunc.identity.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ufunc.identity.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ufunc.identity.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ufunc.identity.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ufunc.identity.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ufunc.identity.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ufunc.identity.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ufunc.identity.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ufunc.identity.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ufunc.identity.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ufunc.identity.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ufunc.identity[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.identity.html#numpy-ufunc-identity "Link to this heading")

================================================================================================================================================

attribute

ufunc.identity[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.identity.html#numpy.ufunc.identity "Link to this definition")

The identity value.

Data attribute containing the identity element for the ufunc, if it has one. If it does not, the attribute value is None.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.add.identity
0
\>>> np.multiply.identity
1
\>>> print(np.power.identity)
None
\>>> print(np.exp.identity)
None

Copy to clipboard

Go BackOpen In Tab

On this page