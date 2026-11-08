[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.identity.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.identity.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.identity.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.identity.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.identity.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.identity.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.identity.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.identity.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.identity.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.identity.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.identity.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.identity.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.identity.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.identity.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.identity.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.identity.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.identity.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.identity.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.identity.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.identity.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.identity.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.identity[#](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy-identity "Link to this heading")

==============================================================================================================================

numpy.identity(_n_, _dtype\=None_, _\*_, _like\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L2177-L2215)
[#](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy.identity "Link to this definition")

Return the identity array.

The identity array is a square array with ones on the main diagonal.

Parameters:

**n**int

Number of rows (and columns) in _n_ x _n_ output.

**dtype**data-type, optional

Data-type of the output. Defaults to `float`.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**ndarray

_n_ x _n_ array with its main diagonal set to one, and all other elements 0.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.identity(3)
array(\[\[1.,  0.,  0.\],\
       \[0.,  1.,  0.\],\
       \[0.,  0.,  1.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page