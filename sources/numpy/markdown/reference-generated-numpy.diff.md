[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.diff.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.diff.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.diff.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.diff.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.diff.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.diff.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.diff.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.diff.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.diff.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.diff.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.diff.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.diff.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.diff.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.diff.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.diff.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.diff.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.diff.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.diff.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.diff.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.diff.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.diff.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.diff[#](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy-diff "Link to this heading")

==================================================================================================================

numpy.diff(_a_, _n=1_, _axis=-1_, _prepend=<no value>_, _append=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L1413-L1542)
[#](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "Link to this definition")

Calculate the n-th discrete difference along the given axis.

The first difference is given by `out[i] = a[i+1] - a[i]` along the given axis, higher differences are calculated by using [`diff`](https://numpy.org/doc/stable/reference/generated/numpy.diff.html#numpy.diff "numpy.diff")
 recursively.

Parameters:

**a**array\_like

Input array

**n**int, optional

The number of times values are differenced. If zero, the input is returned as-is.

**axis**int, optional

The axis along which the difference is taken, default is the last axis.

**prepend, append**array\_like, optional

Values to prepend or append to _a_ along axis prior to performing the difference. Scalar values are expanded to arrays with length 1 in the direction of axis and the shape of the input array in along all other axes. Otherwise the dimension and shape must match _a_ except along axis.

Returns:

**diff**ndarray

The n-th differences. The shape of the output is the same as _a_ except along _axis_ where the dimension is smaller by _n_. The type of the output is the same as the type of the difference between any two elements of _a_. This is the same as the type of _a_ in most cases. A notable exception is [`datetime64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.datetime64 "numpy.datetime64")
, which results in a [`timedelta64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.timedelta64 "numpy.timedelta64")
 output array.

See also

[`gradient`](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html#numpy.gradient "numpy.gradient")
, [`ediff1d`](https://numpy.org/doc/stable/reference/generated/numpy.ediff1d.html#numpy.ediff1d "numpy.ediff1d")
, [`cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")

Notes

Type is preserved for boolean arrays, so the result will contain _False_ when consecutive elements are the same and _True_ when they differ.

For unsigned integer arrays, the results will also be unsigned. This should not be surprising, as the result is consistent with calculating the difference directly:

\>>> u8\_arr \= np.array(\[1, 0\], dtype\=np.uint8)
\>>> np.diff(u8\_arr)
array(\[255\], dtype=uint8)
\>>> u8\_arr\[1,...\] \- u8\_arr\[0,...\]
np.uint8(255)

Copy to clipboard

If this is not desirable, then the array should be cast to a larger integer type first:

\>>> i16\_arr \= u8\_arr.astype(np.int16)
\>>> np.diff(i16\_arr)
array(\[-1\], dtype=int16)

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 4, 7, 0\])
\>>> np.diff(x)
array(\[ 1,  2,  3, -7\])
\>>> np.diff(x, n\=2)
array(\[  1,   1, -10\])

Copy to clipboard

\>>> x \= np.array(\[\[1, 3, 6, 10\], \[0, 5, 6, 8\]\])
\>>> np.diff(x)
array(\[\[2, 3, 4\],\
       \[5, 1, 2\]\])
\>>> np.diff(x, axis\=0)
array(\[\[-1,  2,  0, -2\]\])

Copy to clipboard

\>>> x \= np.arange('1066-10-13', '1066-10-16', dtype\=np.datetime64)
\>>> np.diff(x)
array(\[1, 1\], dtype='timedelta64\[D\]')

Copy to clipboard

Go BackOpen In Tab

On this page