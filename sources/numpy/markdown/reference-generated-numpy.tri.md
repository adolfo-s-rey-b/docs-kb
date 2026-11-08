[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.tri.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.tri[#](https://numpy.org/doc/stable/reference/generated/numpy.tri.html#numpy-tri "Link to this heading")

===============================================================================================================

numpy.tri(_N_, _M=None_, _k=0_, _dtype=<class 'float'>_, _\*_, _like=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L390-L471)
[#](https://numpy.org/doc/stable/reference/generated/numpy.tri.html#numpy.tri "Link to this definition")

An array with ones at and below the given diagonal and zeros elsewhere.

Parameters:

**N**int

Number of rows in the array.

**M**int, optional

Number of columns in the array. By default, _M_ is taken equal to _N_.

**k**int, optional

The sub-diagonal at and below which the array is filled. _k_ = 0 is the main diagonal, while _k_ < 0 is below it, and _k_ > 0 is above. The default is 0.

**dtype**dtype, optional

Data type of the returned array. The default is float.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**tri**ndarray of shape (N, M)

Array with its lower triangle filled with ones and zero elsewhere; in other words `T[i,j] == 1` for `j <= i + k`, 0 otherwise.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.tri(3, 5, 2, dtype\=np.int\_)
array(\[\[1, 1, 1, 0, 0\],\
       \[1, 1, 1, 1, 0\],\
       \[1, 1, 1, 1, 1\]\])

Copy to clipboard

\>>> np.tri(3, 5, \-1)
array(\[\[0.,  0.,  0.,  0.,  0.\],\
       \[1.,  0.,  0.,  0.,  0.\],\
       \[1.,  1.,  0.,  0.,  0.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page