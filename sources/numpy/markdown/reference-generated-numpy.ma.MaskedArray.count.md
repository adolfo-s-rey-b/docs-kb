[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.count.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.count[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.count.html#numpy-ma-maskedarray-count "Link to this heading")

==================================================================================================================================================================

method

ma.MaskedArray.count(_axis=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L4594-L4688)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.count.html#numpy.ma.MaskedArray.count "Link to this definition")

Count the non-masked elements of the array along the given axis.

Parameters:

**axis**None or int or tuple of ints, optional

Axis or axes along which the count is performed. The default, None, performs the count over all the dimensions of the input array. _axis_ may be negative, in which case it counts from the last to the first axis. If this is a tuple of ints, the count is performed on multiple axes, instead of a single axis or all the axes as before.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the array.

Returns:

**result**ndarray or scalar

An array with the same shape as the input array, with the specified axis removed. If the array is a 0-d array, or if _axis_ is None, a scalar is returned.

See also

[`ma.count_masked`](https://numpy.org/doc/stable/reference/generated/numpy.ma.count_masked.html#numpy.ma.count_masked "numpy.ma.count_masked")

Count masked elements in array or along a given axis.

Examples

Try it in your browser!

\>>> import numpy.ma as ma
\>>> a \= ma.arange(6).reshape((2, 3))
\>>> a\[1, :\] \= ma.masked
\>>> a
masked\_array(
  data=\[\[0, 1, 2\],\
        \[--, --, --\]\],
  mask=\[\[False, False, False\],\
        \[ True,  True,  True\]\],
  fill\_value=999999)
\>>> a.count()
3

Copy to clipboard

When the _axis_ keyword is specified an array of appropriate size is returned.

\>>> a.count(axis\=0)
array(\[1, 1, 1\])
\>>> a.count(axis\=1)
array(\[3, 0\])

Copy to clipboard

Go BackOpen In Tab

On this page