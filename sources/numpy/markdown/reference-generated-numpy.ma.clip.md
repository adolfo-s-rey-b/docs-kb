[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.clip.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.clip.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.clip.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.clip.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.clip.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.clip.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.clip.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.clip.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.clip.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.clip.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.clip.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.clip.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.clip.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.clip.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.clip.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.clip.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.clip.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.clip.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.clip.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.clip.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.clip.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.clip.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.clip[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.clip.html#numpy-ma-clip "Link to this heading")

===========================================================================================================================

ma.clip(_a_, _a\_min=<no value>_, _a\_max=<no value>_, _out=None_, _\*_, _min=<no value>_, _max=<no value>_, _fill\_value=None_, _hardmask=False_, _\*\*kwargs_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8820-L8832)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.clip.html#numpy.ma.clip "Link to this definition")

Clip (limit) the values in an array.

Given an interval, values outside the interval are clipped to the interval edges. For example, if an interval of `[0, 1]` is specified, values smaller than 0 become 0, and values larger than 1 become 1.

Equivalent to but faster than `np.minimum(a_max, np.maximum(a, a_min))`.

No check is performed to ensure `a_min < a_max`.

Parameters:

**a**array\_like

Array containing elements to clip.

**a\_min, a\_max**array\_like or None

Minimum and maximum value. If `None`, clipping is not performed on the corresponding edge. If both `a_min` and `a_max` are `None`, the elements of the returned array stay the same. Both are broadcasted against `a`.

**out**ndarray, optional

The results will be placed in this array. It may be the input array for in-place clipping. _out_ must be of the right shape to hold the output. Its type is preserved.

**min, max**array\_like or None

Array API compatible alternatives for `a_min` and `a_max` arguments. Either `a_min` and `a_max` or `min` and `max` can be passed at the same time. Default: `None`.

New in version 2.1.0.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**clipped\_array**MaskedArray

An array with the elements of _a_, but where values < _a\_min_ are replaced with _a\_min_, and those > _a\_max_ with _a\_max_.

See also

[Output type determination](https://numpy.org/doc/stable/user/basics.ufuncs.html#ufuncs-output-type)

Notes

When _a\_min_ is greater than _a\_max_, [`clip`](https://numpy.org/doc/stable/reference/generated/numpy.clip.html#numpy.clip "numpy.clip")
 returns an array in which all values are equal to _a\_max_, as shown in the second example.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.arange(10)
\>>> a
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\])
\>>> np.clip(a, 1, 8)
array(\[1, 1, 2, 3, 4, 5, 6, 7, 8, 8\])
\>>> np.clip(a, 8, 1)
array(\[1, 1, 1, 1, 1, 1, 1, 1, 1, 1\])
\>>> np.clip(a, 3, 6, out\=a)
array(\[3, 3, 3, 3, 4, 5, 6, 6, 6, 6\])
\>>> a
array(\[3, 3, 3, 3, 4, 5, 6, 6, 6, 6\])
\>>> a \= np.arange(10)
\>>> a
array(\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\])
\>>> np.clip(a, \[3, 4, 1, 1, 1, 4, 4, 4, 4, 4\], 8)
array(\[3, 4, 2, 3, 4, 5, 6, 7, 8, 8\])

Copy to clipboard

Go BackOpen In Tab

On this page