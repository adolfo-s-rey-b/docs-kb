[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.set_fill_value.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.set_fill_value.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.set_fill_value.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.set_fill_value.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.set_fill_value.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.set_fill_value.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.set_fill_value.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.set_fill_value.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.set_fill_value.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.set_fill_value.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.set_fill_value.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.set_fill_value.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.set_fill_value.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.set_fill_value.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.set_fill_value.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.set_fill_value.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.set_fill_value.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.set_fill_value.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.set_fill_value.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.set_fill_value.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.set_fill_value.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.set_fill_value.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.set\_fill\_value[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.set_fill_value.html#numpy-ma-set-fill-value "Link to this heading")

===========================================================================================================================================================

ma.set\_fill\_value(_a_, _fill\_value_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L520-L582)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.set_fill_value.html#numpy.ma.set_fill_value "Link to this definition")

Set the filling value of a, if a is a masked array.

This function changes the fill value of the masked array _a_ in place. If _a_ is not a masked array, the function returns silently, without doing anything.

Parameters:

**a**array\_like

Input array.

**fill\_value**dtype

Filling value. A consistency test is performed to make sure the value is compatible with the dtype of _a_.

Returns:

None

Nothing returned by this function.

See also

[`maximum_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.maximum_fill_value.html#numpy.ma.maximum_fill_value "numpy.ma.maximum_fill_value")

Return the default fill value for a dtype.

[`MaskedArray.fill_value`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.fill_value "numpy.ma.MaskedArray.fill_value")

Return current fill value.

[`MaskedArray.set_fill_value`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.set_fill_value.html#numpy.ma.MaskedArray.set_fill_value "numpy.ma.MaskedArray.set_fill_value")

Equivalent method.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= np.arange(5)
\>>> a
array(\[0, 1, 2, 3, 4\])
\>>> a \= ma.masked\_where(a < 3, a)
\>>> a
masked\_array(data=\[--, --, --, 3, 4\],
             mask=\[ True,  True,  True, False, False\],
       fill\_value=999999)
\>>> ma.set\_fill\_value(a, \-999)
\>>> a
masked\_array(data=\[--, --, --, 3, 4\],
             mask=\[ True,  True,  True, False, False\],
       fill\_value=-999)

Copy to clipboard

Nothing happens if _a_ is not a masked array.

\>>> a \= list(range(5))
\>>> a
\[0, 1, 2, 3, 4\]
\>>> ma.set\_fill\_value(a, 100)
\>>> a
\[0, 1, 2, 3, 4\]
\>>> a \= np.arange(5)
\>>> a
array(\[0, 1, 2, 3, 4\])
\>>> ma.set\_fill\_value(a, 100)
\>>> a
array(\[0, 1, 2, 3, 4\])

Copy to clipboard

Go BackOpen In Tab

On this page