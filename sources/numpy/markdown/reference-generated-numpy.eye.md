[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.eye.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.eye.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.eye.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.eye.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.eye.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.eye.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.eye.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.eye.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.eye.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.eye.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.eye.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.eye.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.eye.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.eye.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.eye.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.eye.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.eye.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.eye.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.eye.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.eye.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.eye.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.eye[#](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy-eye "Link to this heading")

===============================================================================================================

numpy.eye(_N_, _M=None_, _k=0_, _dtype=<class 'float'>_, _order='C'_, _\*_, _device=None_, _like=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L178-L250)
[#](https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye "Link to this definition")

Return a 2-D array with ones on the diagonal and zeros elsewhere.

Parameters:

**N**int

Number of rows in the output.

**M**int, optional

Number of columns in the output. If None, defaults to _N_.

**k**int, optional

Index of the diagonal: 0 (the default) refers to the main diagonal, a positive value refers to an upper diagonal, and a negative value to a lower diagonal.

**dtype**data-type, optional

Data-type of the returned array.

**order**{‘C’, ‘F’}, optional

Whether the output should be stored in row-major (C-style) or column-major (Fortran-style) order in memory.

**device**str, optional

The device on which to place the created array. Default: None. For Array-API interoperability only, so must be `"cpu"` if passed.

New in version 2.0.0.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**I**ndarray of shape (N,M)

An array where all elements are equal to zero, except for the _k_\-th diagonal, whose values are equal to one.

See also

[`identity`](https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy.identity "numpy.identity")

(almost) equivalent function

[`diag`](https://numpy.org/doc/stable/reference/generated/numpy.diag.html#numpy.diag "numpy.diag")

diagonal 2-D array from a 1-D array specified by the user.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.eye(2, dtype\=np.int\_)
array(\[\[1, 0\],\
       \[0, 1\]\])
\>>> np.eye(3, k\=1)
array(\[\[0.,  1.,  0.\],\
       \[0.,  0.,  1.\],\
       \[0.,  0.,  0.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page