[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nansum.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nansum.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nansum.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nansum.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nansum.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nansum.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nansum.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nansum.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nansum.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nansum.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nansum.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nansum.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nansum.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nansum.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nansum.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nansum.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nansum.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nansum.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nansum.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nansum.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nansum.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nansum.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nansum[#](https://numpy.org/doc/stable/reference/generated/numpy.nansum.html#numpy-nansum "Link to this heading")

========================================================================================================================

numpy.nansum(_a_, _axis=None_, _dtype=None_, _out=None_, _keepdims=<no value>_, _initial=<no value>_, _where=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_nanfunctions_impl.py#L634-L727)
[#](https://numpy.org/doc/stable/reference/generated/numpy.nansum.html#numpy.nansum "Link to this definition")

Return the sum of array elements over a given axis treating Not a Numbers (NaNs) as zero.

In NumPy versions <= 1.9.0 Nan is returned for slices that are all-NaN or empty. In later versions zero is returned.

Parameters:

**a**array\_like

Array containing numbers whose sum is desired. If _a_ is not an array, a conversion is attempted.

**axis**{int, tuple of int, None}, optional

Axis or axes along which the sum is computed. The default is to compute the sum of the flattened array.

**dtype**data-type, optional

The type of the returned array and of the accumulator in which the elements are summed. By default, the dtype of _a_ is used. An exception is when _a_ has an integer type with less precision than the platform (u)intp. In that case, the default will be either (u)int32 or (u)int64 depending on whether the platform is 32 or 64 bits. For inexact inputs, dtype must be inexact.

**out**ndarray, optional

Alternate output array in which to place the result. The default is `None`. If provided, it must have the same shape as the expected output, but the type will be cast if necessary. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details. The casting of NaN to integer can yield unexpected results.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original _a_.

If the value is anything but the default, then _keepdims_ will be passed through to the [`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")
 or [`sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
 methods of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
. If the sub-classes methods does not implement _keepdims_ any exceptions will be raised.

**initial**scalar, optional

Starting value for the sum. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

New in version 1.22.0.

**where**array\_like of bool, optional

Elements to include in the sum. See [`reduce`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce")
 for details.

New in version 1.22.0.

Returns:

**nansum**ndarray.

A new array holding the result is returned unless _out_ is specified, in which it is returned. The result has the same size as _a_, and the same shape as _a_ if _axis_ is not None or _a_ is a 1-d array.

See also

[`numpy.sum`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")

Sum across array propagating NaNs.

[`isnan`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan "numpy.isnan")

Show which elements are NaN.

[`isfinite`](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy.isfinite "numpy.isfinite")

Show which elements are not NaN or +/-inf.

Notes

If both positive and negative infinity are present, the sum will be Not A Number (NaN).

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.nansum(1)
1
\>>> np.nansum(\[1\])
1
\>>> np.nansum(\[1, np.nan\])
1.0
\>>> a \= np.array(\[\[1, 1\], \[1, np.nan\]\])
\>>> np.nansum(a)
3.0
\>>> np.nansum(a, axis\=0)
array(\[2.,  1.\])
\>>> np.nansum(\[1, np.nan, np.inf\])
inf
\>>> np.nansum(\[1, np.nan, \-np.inf\])
\-inf
\>>> with np.errstate(invalid\="ignore"):
...     np.nansum(\[1, np.nan, np.inf, \-np.inf\]) \# both +/- infinity present
np.float64(nan)

Copy to clipboard

Go BackOpen In Tab

On this page