[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.min.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.min.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.min.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.min.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.min.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.min.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.min.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.min.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.min.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.min.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.min.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.min.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.min.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.min.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.min.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.min.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.min.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.min.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.min.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.min.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.min.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.min.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.min[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.min.html#numpy-ma-masked-array-min "Link to this heading")

================================================================================================================================================================

method

ma.masked\_array.min(_axis=None_, _out=None_, _fill\_value=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5875-L5971)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.min.html#numpy.ma.masked_array.min "Link to this definition")

Return the minimum along a given axis.

Parameters:

**axis**None or int or tuple of ints, optional

Axis along which to operate. By default, `axis` is None and the flattened input is used. If this is a tuple of ints, the minimum is selected over multiple axes, instead of a single axis or all the axes as before.

**out**array\_like, optional

Alternative output array in which to place the result. Must be of the same shape and buffer length as the expected output.

**fill\_value**scalar or None, optional

Value used to fill in the masked values. If None, use the output of _minimum\_fill\_value_.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the array.

Returns:

**amin**array\_like

New array holding the result. If `out` was specified, `out` is returned.

See also

[`ma.minimum_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.minimum_fill_value.html#numpy.ma.minimum_fill_value "numpy.ma.minimum_fill_value")

Returns the minimum filling value for a given datatype.

Examples

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= \[\[1., \-2., 3.\], \[0.2, \-0.7, 0.1\]\]
\>>> mask \= \[\[1, 1, 0\], \[0, 0, 1\]\]
\>>> masked\_x \= ma.masked\_array(x, mask)
\>>> masked\_x
masked\_array(
  data=\[\[--, --, 3.0\],\
        \[0.2, -0.7, --\]\],
  mask=\[\[ True,  True, False\],\
        \[False, False,  True\]\],
  fill\_value=1e+20)
\>>> ma.min(masked\_x)
\-0.7
\>>> ma.min(masked\_x, axis\=-1)
masked\_array(data=\[3.0, -0.7\],
             mask=\[False, False\],
        fill\_value=1e+20)
\>>> ma.min(masked\_x, axis\=0, keepdims\=True)
masked\_array(data=\[\[0.2, -0.7, 3.0\]\],
             mask=\[\[False, False, False\]\],
        fill\_value=1e+20)
\>>> mask \= \[\[1, 1, 1,\], \[1, 1, 1\]\]
\>>> masked\_x \= ma.masked\_array(x, mask)
\>>> ma.min(masked\_x, axis\=0)
masked\_array(data=\[--, --, --\],
             mask=\[ True,  True,  True\],
        fill\_value=1e+20,
            dtype=float64)

Copy to clipboard

Go BackOpen In Tab

On this page