[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.count.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.count.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.count.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.count.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.count.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.count.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.count.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.count.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.count.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.count.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.count.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.count.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.count.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.count.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.count.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.count.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.count.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.count.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.count.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.count.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.count.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.count.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.count[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.count.html#numpy-ma-masked-array-count "Link to this heading")

======================================================================================================================================================================

method

ma.masked\_array.count(_axis=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L4594-L4688)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.count.html#numpy.ma.masked_array.count "Link to this definition")

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