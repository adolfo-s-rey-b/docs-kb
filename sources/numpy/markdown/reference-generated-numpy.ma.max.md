[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.max.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.max.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.max.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.max.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.max.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.max.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.max.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.max.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.max.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.max.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.max.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.max.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.max.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.max.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.max.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.max.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.max.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.max.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.max.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.max.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.max.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.max.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.max[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.max.html#numpy-ma-max "Link to this heading")

========================================================================================================================

ma.max(_obj_, _axis=None_, _out=None_, _fill\_value=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7019-L7028)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.max.html#numpy.ma.max "Link to this definition")

Return the maximum along a given axis.

Parameters:

**axis**None or int or tuple of ints, optional

Axis along which to operate. By default, `axis` is None and the flattened input is used. If this is a tuple of ints, the maximum is selected over multiple axes, instead of a single axis or all the axes as before.

**out**array\_like, optional

Alternative output array in which to place the result. Must be of the same shape and buffer length as the expected output.

**fill\_value**scalar or None, optional

Value used to fill in the masked values. If None, use the output of maximum\_fill\_value().

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the array.

Returns:

**amax**array\_like

New array holding the result. If `out` was specified, `out` is returned.

See also

[`ma.maximum_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.maximum_fill_value.html#numpy.ma.maximum_fill_value "numpy.ma.maximum_fill_value")

Returns the maximum filling value for a given datatype.

Examples

Try it in your browser!

\>>> import numpy.ma as ma
\>>> x \= \[\[\-1., 2.5\], \[4., \-2.\], \[3., 0.\]\]
\>>> mask \= \[\[0, 0\], \[1, 0\], \[1, 0\]\]
\>>> masked\_x \= ma.masked\_array(x, mask)
\>>> masked\_x
masked\_array(
  data=\[\[-1.0, 2.5\],\
        \[--, -2.0\],\
        \[--, 0.0\]\],
  mask=\[\[False, False\],\
        \[ True, False\],\
        \[ True, False\]\],
  fill\_value=1e+20)
\>>> ma.max(masked\_x)
2.5
\>>> ma.max(masked\_x, axis\=0)
masked\_array(data=\[-1.0, 2.5\],
             mask=\[False, False\],
       fill\_value=1e+20)
\>>> ma.max(masked\_x, axis\=1, keepdims\=True)
masked\_array(
  data=\[\[2.5\],\
        \[-2.0\],\
        \[0.0\]\],
  mask=\[\[False\],\
        \[False\],\
        \[False\]\],
  fill\_value=1e+20)
\>>> mask \= \[\[1, 1\], \[1, 1\], \[1, 1\]\]
\>>> masked\_x \= ma.masked\_array(x, mask)
\>>> ma.max(masked\_x, axis\=1)
masked\_array(data=\[--, --, --\],
             mask=\[ True,  True,  True\],
       fill\_value=1e+20,
            dtype=float64)

Copy to clipboard

Go BackOpen In Tab

On this page