[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.allclose.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.allclose.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.allclose.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.allclose.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.allclose.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.allclose.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.allclose.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.allclose.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.allclose.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.allclose.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.allclose.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.allclose.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.allclose.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.allclose.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.allclose.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.allclose.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.allclose.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.allclose.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.allclose.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.allclose.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.allclose[#](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy-allclose "Link to this heading")

==============================================================================================================================

numpy.allclose(_a_, _b_, _rtol\=1e-05_, _atol\=1e-08_, _equal\_nan\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L2225-L2312)
[#](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "Link to this definition")

Returns True if two arrays are element-wise equal within a tolerance.

The tolerance values are positive, typically very small numbers. The relative difference (_rtol_ \* abs(_b_)) and the absolute difference _atol_ are added together to compare against the absolute difference between _a_ and _b_.

Warning

The default _atol_ is not appropriate for comparing numbers with magnitudes much smaller than one (see Notes).

NaNs are treated as equal if they are in the same place and if `equal_nan=True`. Infs are treated as equal if they are in the same place and of the same sign in both arrays.

Parameters:

**a, b**array\_like

Input arrays to compare.

**rtol**array\_like

The relative tolerance parameter (see Notes).

**atol**array\_like

The absolute tolerance parameter (see Notes).

**equal\_nan**bool

Whether to compare NaN’s as equal. If True, NaN’s in _a_ will be considered equal to NaN’s in _b_ in the output array.

Returns:

**allclose**bool

Returns True if the two arrays are equal within the given tolerance; False otherwise.

See also

[`isclose`](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose "numpy.isclose")
, [`all`](https://numpy.org/doc/stable/reference/generated/numpy.all.html#numpy.all "numpy.all")
, [`any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "numpy.any")
, [`equal`](https://numpy.org/doc/stable/reference/generated/numpy.equal.html#numpy.equal "numpy.equal")

Notes

If the following equation is element-wise True, then allclose returns True.:

absolute(a \- b) <= (atol + rtol \* absolute(b))

Copy to clipboard

The above equation is not symmetric in _a_ and _b_, so that `allclose(a, b)` might be different from `allclose(b, a)` in some rare cases.

The default value of _atol_ is not appropriate when the reference value _b_ has magnitude smaller than one. For example, it is unlikely that `a = 1e-9` and `b = 2e-9` should be considered “close”, yet `allclose(1e-9, 2e-9)` is `True` with default settings. Be sure to select _atol_ for the use case at hand, especially for defining the threshold below which a non-zero value in _a_ will be considered “close” to a very small or zero value in _b_.

The comparison of _a_ and _b_ uses standard broadcasting, which means that _a_ and _b_ need not have the same shape in order for `allclose(a, b)` to evaluate to True. The same is true for [`equal`](https://numpy.org/doc/stable/reference/generated/numpy.equal.html#numpy.equal "numpy.equal")
 but not [`array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html#numpy.array_equal "numpy.array_equal")
.

[`allclose`](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose "numpy.allclose")
 is not defined for non-numeric data types. [`bool`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.bool "numpy.bool")
 is considered a numeric data-type for this purpose.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.allclose(\[1e10,1e-7\], \[1.00001e10,1e-8\])
False

Copy to clipboard

\>>> np.allclose(\[1e10,1e-8\], \[1.00001e10,1e-9\])
True

Copy to clipboard

\>>> np.allclose(\[1e10,1e-8\], \[1.0001e10,1e-9\])
False

Copy to clipboard

\>>> np.allclose(\[1.0, np.nan\], \[1.0, np.nan\])
False

Copy to clipboard

\>>> np.allclose(\[1.0, np.nan\], \[1.0, np.nan\], equal\_nan\=True)
True

Copy to clipboard

Go BackOpen In Tab

On this page