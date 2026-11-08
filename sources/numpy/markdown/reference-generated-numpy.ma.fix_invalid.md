[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.fix_invalid.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.fix_invalid.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.fix_invalid.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.fix_invalid.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.fix_invalid.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.fix_invalid.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.fix_invalid.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.fix_invalid.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.fix_invalid.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.fix_invalid.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.fix_invalid.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.fix_invalid.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.fix_invalid.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.fix_invalid.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.fix_invalid.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.fix_invalid.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.fix_invalid.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.fix_invalid.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.fix_invalid.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.fix_invalid.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.fix_invalid.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.fix_invalid.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.fix\_invalid[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.fix_invalid.html#numpy-ma-fix-invalid "Link to this heading")

=================================================================================================================================================

ma.fix\_invalid(_a_, _mask\=np.False\__, _copy\=True_, _fill\_value\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L775-L832)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.fix_invalid.html#numpy.ma.fix_invalid "Link to this definition")

Return input with invalid data masked and replaced by a fill value.

Invalid data means values of [`nan`](https://numpy.org/doc/stable/reference/constants.html#numpy.nan "numpy.nan")
, [`inf`](https://numpy.org/doc/stable/reference/constants.html#numpy.inf "numpy.inf")
, etc.

Parameters:

**a**array\_like

Input array, a (subclass of) ndarray.

**mask**sequence, optional

Mask. Must be convertible to an array of booleans with the same shape as _data_. True indicates a masked (i.e. invalid) data.

**copy**bool, optional

Whether to use a copy of _a_ (True) or to fix _a_ in place (False). Default is True.

**fill\_value**scalar, optional

Value used for fixing invalid data. Default is None, in which case the `a.fill_value` is used.

Returns:

**b**MaskedArray

The input array with invalid entries fixed.

Notes

A copy is performed by default.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(\[1., \-1, np.nan, np.inf\], mask\=\[1\] + \[0\]\*3)
\>>> x
masked\_array(data=\[--, -1.0, nan, inf\],
             mask=\[ True, False, False, False\],
       fill\_value=1e+20)
\>>> np.ma.fix\_invalid(x)
masked\_array(data=\[--, -1.0, --, --\],
             mask=\[ True, False,  True,  True\],
       fill\_value=1e+20)

Copy to clipboard

\>>> fixed \= np.ma.fix\_invalid(x)
\>>> fixed.data
array(\[ 1.e+00, -1.e+00,  1.e+20,  1.e+20\])
\>>> x.data
array(\[ 1., -1., nan, inf\])

Copy to clipboard

Go BackOpen In Tab

On this page