[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.cumprod.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.cumprod.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.cumprod.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.cumprod.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.cumprod.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.cumprod.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.cumprod.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.cumprod.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.cumprod.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.cumprod.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.cumprod.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.cumprod.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.cumprod.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.cumprod.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.cumprod.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.cumprod.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.cumprod.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.cumprod.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.cumprod.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.cumprod.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.cumprod[#](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy-cumprod "Link to this heading")

===========================================================================================================================

numpy.cumprod(_a_, _axis\=None_, _dtype\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L3450-L3513)
[#](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod "Link to this definition")

Return the cumulative product of elements along a given axis.

Parameters:

**a**array\_like

Input array.

**axis**int, optional

Axis along which the cumulative product is computed. By default the input is flattened.

**dtype**dtype, optional

Type of the returned array, as well as of the accumulator in which the elements are multiplied. If _dtype_ is not specified, it defaults to the dtype of _a_, unless _a_ has an integer dtype with a precision less than that of the default platform integer. In that case, the default platform integer is used instead.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output but the type of the resulting values will be cast if necessary.

Returns:

**cumprod**ndarray

A new array holding the result is returned unless _out_ is specified, in which case a reference to out is returned.

See also

[`cumulative_prod`](https://numpy.org/doc/stable/reference/generated/numpy.cumulative_prod.html#numpy.cumulative_prod "numpy.cumulative_prod")

Array API compatible alternative for `cumprod`.

[Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)

Notes

Arithmetic is modular when using integer types, and no error is raised on overflow.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[1,2,3\])
\>>> np.cumprod(a) \# intermediate results 1, 1\*2
...               \# total product 1\*2\*3 = 6
array(\[1, 2, 6\])
\>>> a \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\])
\>>> np.cumprod(a, dtype\=np.float64)  \# specify type of output
array(\[   1.,    2.,    6.,   24.,  120.,  720.\])

Copy to clipboard

The cumulative product for each column (i.e., over the rows) of _a_:

\>>> np.cumprod(a, axis\=0)
array(\[\[ 1,  2,  3\],\
       \[ 4, 10, 18\]\])

Copy to clipboard

The cumulative product for each row (i.e. over the columns) of _a_:

\>>> np.cumprod(a,axis\=1)
array(\[\[  1,   2,   6\],\
       \[  4,  20, 120\]\])

Copy to clipboard

Go BackOpen In Tab

On this page