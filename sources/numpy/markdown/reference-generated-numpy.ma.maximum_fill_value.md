[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.maximum_fill_value.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.maximum_fill_value.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.maximum_fill_value.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.maximum_fill_value.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.maximum_fill_value.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.maximum_fill_value.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.maximum_fill_value.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.maximum_fill_value.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.maximum_fill_value.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.maximum_fill_value.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.maximum_fill_value.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.maximum_fill_value.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.maximum_fill_value.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.maximum_fill_value.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.maximum_fill_value.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.maximum_fill_value.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.maximum_fill_value.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.maximum_fill_value.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.maximum_fill_value.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.maximum_fill_value.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.maximum_fill_value.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.maximum_fill_value.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.maximum\_fill\_value[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.maximum_fill_value.html#numpy-ma-maximum-fill-value "Link to this heading")

=======================================================================================================================================================================

ma.maximum\_fill\_value(_obj_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L383-L432)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.maximum_fill_value.html#numpy.ma.maximum_fill_value "Link to this definition")

Return the minimum value that can be represented by the dtype of an object.

This function is useful for calculating a fill value suitable for taking the maximum of an array with a given dtype.

Parameters:

**obj**ndarray, dtype or scalar

An object that can be queried for it’s numeric type.

Returns:

**val**scalar

The minimum representable value.

Raises:

TypeError

If _obj_ isn’t a suitable numeric type.

See also

[`minimum_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.minimum_fill_value.html#numpy.ma.minimum_fill_value "numpy.ma.minimum_fill_value")

The inverse function.

[`set_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.set_fill_value.html#numpy.ma.set_fill_value "numpy.ma.set_fill_value")

Set the filling value of a masked array.

[`MaskedArray.fill_value`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.fill_value "numpy.ma.MaskedArray.fill_value")

Return current fill value.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= np.int8()
\>>> ma.maximum\_fill\_value(a)
\-128
\>>> a \= np.int32()
\>>> ma.maximum\_fill\_value(a)
\-2147483648

Copy to clipboard

An array of numeric data can also be passed.

\>>> a \= np.array(\[1, 2, 3\], dtype\=np.int8)
\>>> ma.maximum\_fill\_value(a)
\-128
\>>> a \= np.array(\[1, 2, 3\], dtype\=np.float32)
\>>> ma.maximum\_fill\_value(a)
\-inf

Copy to clipboard

Go BackOpen In Tab

On this page