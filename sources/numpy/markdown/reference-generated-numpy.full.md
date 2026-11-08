[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.full.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.full.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.full.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.full.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.full.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.full.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.full.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.full.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.full.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.full.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.full.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.full.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.full.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.full.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.full.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.full.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.full.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.full.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.full.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.full.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.full.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.full.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.full[#](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy-full "Link to this heading")

==================================================================================================================

numpy.full(_shape_, _fill\_value_, _dtype\=None_, _order\='C'_, _\*_, _device\=None_, _like\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L323-L387)
[#](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "Link to this definition")

Return a new array of given shape and type, filled with _fill\_value_.

Parameters:

**shape**int or sequence of ints

Shape of the new array, e.g., `(2, 3)` or `2`.

**fill\_value**scalar or array\_like

Fill value.

**dtype**data-type, optional

The desired data-type for the array The default, None, means

`np.array(fill_value).dtype`.

**order**{‘C’, ‘F’}, optional

Whether to store multidimensional data in C- or Fortran-contiguous (row- or column-wise) order in memory.

**device**str, optional

The device on which to place the created array. Default: None. For Array-API interoperability only, so must be `"cpu"` if passed.

New in version 2.0.0.

**like**array\_like, optional

Reference object to allow the creation of arrays which are not NumPy arrays. If an array-like passed in as `like` supports the `__array_function__` protocol, the result will be defined by it. In this case, it ensures the creation of an array object compatible with that passed in via this argument.

New in version 1.20.0.

Returns:

**out**ndarray

Array of _fill\_value_ with the given shape, dtype, and order.

See also

[`full_like`](https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like "numpy.full_like")

Return a new array with shape of input filled with value.

[`empty`](https://numpy.org/doc/stable/reference/generated/numpy.empty.html#numpy.empty "numpy.empty")

Return a new uninitialized array.

[`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")

Return a new array setting values to one.

[`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros")

Return a new array setting values to zero.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.full((2, 2), np.inf)
array(\[\[inf, inf\],\
       \[inf, inf\]\])
\>>> np.full((2, 2), 10)
array(\[\[10, 10\],\
       \[10, 10\]\])

Copy to clipboard

\>>> np.full((2, 2), \[1, 2\])
array(\[\[1, 2\],\
       \[1, 2\]\])

Copy to clipboard

Go BackOpen In Tab

On this page