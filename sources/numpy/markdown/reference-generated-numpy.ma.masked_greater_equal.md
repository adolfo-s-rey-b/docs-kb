[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater_equal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.masked\_greater\_equal[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater_equal.html#numpy-ma-masked-greater-equal "Link to this heading")

=============================================================================================================================================================================

ma.masked\_greater\_equal(_x_, _value_, _copy\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L2035-L2059)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater_equal.html#numpy.ma.masked_greater_equal "Link to this definition")

Mask an array where greater than or equal to a given value.

This function is a shortcut to `masked_where`, with _condition_ = (x >= value).

See also

[`masked_where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")

Mask where a condition is met.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= np.arange(4)
\>>> a
array(\[0, 1, 2, 3\])
\>>> ma.masked\_greater\_equal(a, 2)
masked\_array(data=\[0, 1, --, --\],
             mask=\[False, False,  True,  True\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page