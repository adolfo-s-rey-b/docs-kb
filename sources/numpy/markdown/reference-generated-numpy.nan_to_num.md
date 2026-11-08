[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nan_to_num.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nan_to_num.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nan_to_num.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nan_to_num.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nan_to_num.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nan_to_num.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nan_to_num.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nan_to_num.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nan_to_num.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nan_to_num.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nan_to_num.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nan_to_num.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nan_to_num.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nan_to_num.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nan_to_num.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nan_to_num.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nan_to_num.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nan_to_num.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nan_to_num.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nan_to_num.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nan\_to\_num[#](https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html#numpy-nan-to-num "Link to this heading")

======================================================================================================================================

numpy.nan\_to\_num(_x_, _copy\=True_, _nan\=0.0_, _posinf\=None_, _neginf\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_type_check_impl.py#L368-L487)
[#](https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html#numpy.nan_to_num "Link to this definition")

Replace NaN with zero and infinity with large finite numbers (default behaviour) or with the numbers defined by the user using the [`nan`](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")
, _posinf_ and/or _neginf_ keywords.

If _x_ is inexact, NaN is replaced by zero or by the user defined value in [`nan`](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")
 keyword, infinity is replaced by the largest finite floating point values representable by `x.dtype` or by the user defined value in _posinf_ keyword and -infinity is replaced by the most negative finite floating point values representable by `x.dtype` or by the user defined value in _neginf_ keyword.

For complex dtypes, the above is applied to each of the real and imaginary components of _x_ separately.

If _x_ is not inexact, then no replacements are made.

Parameters:

**x**scalar or array\_like

Input data.

**copy**bool, optional

Whether to create a copy of _x_ (True) or to replace values in-place (False). The in-place operation only occurs if casting to an array does not require a copy. Default is True.

**nan**int, float, or bool or array\_like of int, float, or bool, optional

Values to be used to fill NaN values. If no values are passed then NaN values will be replaced with 0.0.

**posinf**int, float, or bool or array\_like of int, float, or bool, optional

Values to be used to fill positive infinity values. If no values are passed then positive infinity values will be replaced with a very large number.

**neginf**int, float, or bool or array\_like of int, float, or bool, optional

Values to be used to fill negative infinity values. If no values are passed then negative infinity values will be replaced with a very small (or negative) number.

Returns:

**out**ndarray

_x_, with the non-finite values replaced. If [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
 is False, this may be _x_ itself.

See also

[`isinf`](https://numpy.org/doc/stable/reference/generated/numpy.isinf.html#numpy.isinf "numpy.isinf")

Shows which elements are positive or negative infinity.

[`isneginf`](https://numpy.org/doc/stable/reference/generated/numpy.isneginf.html#numpy.isneginf "numpy.isneginf")

Shows which elements are negative infinity.

[`isposinf`](https://numpy.org/doc/stable/reference/generated/numpy.isposinf.html#numpy.isposinf "numpy.isposinf")

Shows which elements are positive infinity.

[`isnan`](https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan "numpy.isnan")

Shows which elements are Not a Number (NaN).

[`isfinite`](https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html#numpy.isfinite "numpy.isfinite")

Shows which elements are finite (not NaN, not infinity)

Notes

NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754). This means that Not a Number is not equivalent to infinity.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.nan\_to\_num(np.inf)
1.7976931348623157e+308
\>>> np.nan\_to\_num(\-np.inf)
\-1.7976931348623157e+308
\>>> np.nan\_to\_num(np.nan)
0.0
\>>> x \= np.array(\[np.inf, \-np.inf, np.nan, \-128, 128\])
\>>> np.nan\_to\_num(x)
array(\[ 1.79769313e+308, -1.79769313e+308,  0.00000000e+000, # may vary\
       -1.28000000e+002,  1.28000000e+002\])
\>>> np.nan\_to\_num(x, nan\=-9999, posinf\=33333333, neginf\=33333333)
array(\[ 3.3333333e+07,  3.3333333e+07, -9.9990000e+03,\
       -1.2800000e+02,  1.2800000e+02\])
\>>> nan \= np.array(\[11, 12, \-9999, 13, 14\])
\>>> posinf \= np.array(\[33333333, 11, 12, 13, 14\])
\>>> neginf \= np.array(\[11, 33333333, 12, 13, 14\])
\>>> np.nan\_to\_num(x, nan\=nan, posinf\=posinf, neginf\=neginf)
array(\[ 3.3333333e+07,  3.3333333e+07, -9.9990000e+03, -1.2800000e+02,\
        1.2800000e+02\])
\>>> y \= np.array(\[complex(np.inf, np.nan), np.nan, complex(np.nan, np.inf)\])
array(\[  1.79769313e+308,  -1.79769313e+308,   0.00000000e+000, # may vary\
     -1.28000000e+002,   1.28000000e+002\])
\>>> np.nan\_to\_num(y)
array(\[  1.79769313e+308 +0.00000000e+000j, # may vary\
         0.00000000e+000 +0.00000000e+000j,\
         0.00000000e+000 +1.79769313e+308j\])
\>>> np.nan\_to\_num(y, nan\=111111, posinf\=222222)
array(\[222222.+111111.j, 111111.     +0.j, 111111.+222222.j\])
\>>> nan \= np.array(\[11, 12, 13\])
\>>> posinf \= np.array(\[21, 22, 23\])
\>>> neginf \= np.array(\[31, 32, 33\])
\>>> np.nan\_to\_num(y, nan\=nan, posinf\=posinf, neginf\=neginf)
array(\[21.+11.j, 12. +0.j, 13.+23.j\])

Copy to clipboard

Go BackOpen In Tab

On this page