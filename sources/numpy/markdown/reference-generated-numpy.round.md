[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.round.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.round.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.round.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.round.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.round.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.round.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.round.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.round.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.round.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.round.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.round.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.round.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.round.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.round.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.round.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.round.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.round.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.round.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.round.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.round.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.round.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.round.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.round[#](https://numpy.org/doc/stable/reference/generated/numpy.round.html#numpy-round "Link to this heading")

=====================================================================================================================

numpy.round(_a_, _decimals\=0_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L3620-L3712)
[#](https://numpy.org/doc/stable/reference/generated/numpy.round.html#numpy.round "Link to this definition")

Evenly round to the given number of decimals.

Parameters:

**a**array\_like

Input data.

**decimals**int, optional

Number of decimal places to round to (default: 0). If decimals is negative, it specifies the number of positions to the left of the decimal point.

**out**ndarray, optional

Alternative output array in which to place the result. It must have the same shape as the expected output, but the type of the output values will be cast if necessary. See [Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)
 for more details.

Returns:

**rounded\_array**ndarray

An array of the same type as _a_, containing the rounded values. Unless _out_ was specified, a new array is created. A reference to the result is returned.

The real and imaginary parts of complex numbers are rounded separately. The result of rounding a float is a float.

See also

[`ndarray.round`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.round.html#numpy.ndarray.round "numpy.ndarray.round")

equivalent method

[`around`](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "numpy.around")

an alias for this function

[`ceil`](https://numpy.org/doc/stable/reference/generated/numpy.ceil.html#numpy.ceil "numpy.ceil")
, [`fix`](https://numpy.org/doc/stable/reference/generated/numpy.fix.html#numpy.fix "numpy.fix")
, [`floor`](https://numpy.org/doc/stable/reference/generated/numpy.floor.html#numpy.floor "numpy.floor")
, [`rint`](https://numpy.org/doc/stable/reference/generated/numpy.rint.html#numpy.rint "numpy.rint")
, [`trunc`](https://numpy.org/doc/stable/reference/generated/numpy.trunc.html#numpy.trunc "numpy.trunc")

Notes

For values exactly halfway between rounded decimal values, NumPy rounds to the nearest even value. Thus 1.5 and 2.5 round to 2.0, -0.5 and 0.5 round to 0.0, etc.

`np.round` uses a fast but sometimes inexact algorithm to round floating-point datatypes. For positive _decimals_ it is equivalent to `np.true_divide(np.rint(a * 10**decimals), 10**decimals)`, which has error due to the inexact representation of decimal fractions in the IEEE floating point standard [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.round.html#r25ee6110317b-1)
 and errors introduced when scaling by powers of ten. For instance, note the extra “1” in the following:

\>>> np.round(56294995342131.5, 3)
56294995342131.51

Copy to clipboard

If your goal is to print such values with a fixed number of decimals, it is preferable to use numpy’s float printing routines to limit the number of printed decimals:

\>>> np.format\_float\_positional(56294995342131.5, precision\=3)
'56294995342131.5'

Copy to clipboard

The float printing routines use an accurate but much more computationally demanding algorithm to compute the number of digits after the decimal point.

Alternatively, Python’s builtin [`round`](https://numpy.org/doc/stable/reference/generated/numpy.round.html#numpy.round "numpy.round")
 function uses a more accurate but slower algorithm for 64-bit floating point values:

\>>> round(56294995342131.5, 3)
56294995342131.5
\>>> np.round(16.055, 2), round(16.055, 2)  \# equals 16.0549999999999997
(16.06, 16.05)

Copy to clipboard

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.round.html#id1)\
\]

“Lecture Notes on the Status of IEEE 754”, William Kahan, [https://people.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF](https://people.eecs.berkeley.edu/~wkahan/ieee754status/IEEE754.PDF)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.round(\[0.37, 1.64\])
array(\[0., 2.\])
\>>> np.round(\[0.37, 1.64\], decimals\=1)
array(\[0.4, 1.6\])
\>>> np.round(\[.5, 1.5, 2.5, 3.5, 4.5\]) \# rounds to nearest even value
array(\[0., 2., 2., 4., 4.\])
\>>> np.round(\[1,2,3,11\], decimals\=1) \# ndarray of ints is returned
array(\[ 1,  2,  3, 11\])
\>>> np.round(\[1,2,3,11\], decimals\=-1)
array(\[ 0,  0,  0, 10\])

Copy to clipboard

Go BackOpen In Tab

On this page