[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nancumsum.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nancumsum.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nancumsum.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nancumsum.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nancumsum.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nancumsum.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nancumsum.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nancumsum.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nancumsum.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nancumsum.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nancumsum.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nancumsum.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nancumsum.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nancumsum.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nancumsum.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nancumsum.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nancumsum.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nancumsum.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nancumsum.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nancumsum.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nancumsum.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nancumsum.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nancumsum[#](https://numpy.org/doc/stable/reference/generated/numpy.nancumsum.html#numpy-nancumsum "Link to this heading")

=================================================================================================================================

numpy.nancumsum(_a_, _axis\=None_, _dtype\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_nanfunctions_impl.py#L816-L878)
[#](https://numpy.org/doc/stable/reference/generated/numpy.nancumsum.html#numpy.nancumsum "Link to this definition")

Return the cumulative sum of array elements over a given axis treating Not a Numbers (NaNs) as zero. The cumulative sum does not change when NaNs are encountered and leading NaNs are replaced by zeros.

Zeros are returned for slices that are all-NaN or empty.

Parameters:

**a**array\_like

Input array.

**axis**int, optional

Axis along which the cumulative sum is computed. The default (None) is to compute the cumsum over the flattened array.

**dtype**dtype, optional

Type of the returned array and of the accumulator in which the elements are summed. If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is not specified, it defaults to the dtype of _a_, unless _a_ has an integer dtype with a precision less than that of the default platform integer. In that case, the default platform integer is used.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output but the type will be cast if necessary. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

Returns:

**nancumsum**ndarray.

A new array holding the result is returned unless _out_ is specified, in which it is returned. The result has the same size as _a_, and the same shape as _a_ if _axis_ is not None or _a_ is a 1-d array.

See also

[`numpy.cumsum`](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum")

Cumulative sum across array propagating NaNs.

[`isnan`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan "numpy.isnan")

Show which elements are NaN.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.nancumsum(1)
array(\[1\])
\>>> np.nancumsum(\[1\])
array(\[1\])
\>>> np.nancumsum(\[1, np.nan\])
array(\[1.,  1.\])
\>>> a \= np.array(\[\[1, 2\], \[3, np.nan\]\])
\>>> np.nancumsum(a)
array(\[1.,  3.,  6.,  6.\])
\>>> np.nancumsum(a, axis\=0)
array(\[\[1.,  2.\],\
       \[4.,  2.\]\])
\>>> np.nancumsum(a, axis\=1)
array(\[\[1.,  3.\],\
       \[3.,  3.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page