[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_object.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_object.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_object.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_object.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_object.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_object.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_object.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_object.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_object.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_object.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_object.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_object.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_object.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_object.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_object.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_object.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_object.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_object.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_object.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_object.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_object.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_object.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.masked\_object[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_object.html#numpy-ma-masked-object "Link to this heading")

=======================================================================================================================================================

ma.masked\_object(_x_, _value_, _copy\=True_, _shrink\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L2258-L2324)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_object.html#numpy.ma.masked_object "Link to this definition")

Mask the array _x_ where the data are exactly equal to value.

This function is similar to [`masked_values`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#numpy.ma.masked_values "numpy.ma.masked_values")
, but only suitable for object arrays: for floating point, use [`masked_values`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#numpy.ma.masked_values "numpy.ma.masked_values")
 instead.

Parameters:

**x**array\_like

Array to mask

**value**object

Comparison value

**copy**{True, False}, optional

Whether to return a copy of _x_.

**shrink**{True, False}, optional

Whether to collapse a mask full of False to nomask

Returns:

**result**MaskedArray

The result of masking _x_ where equal to _value_.

See also

[`masked_where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")

Mask where a condition is met.

[`masked_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_equal.html#numpy.ma.masked_equal "numpy.ma.masked_equal")

Mask where equal to a given value (integers).

[`masked_values`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#numpy.ma.masked_values "numpy.ma.masked_values")

Mask using floating point equality.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> food \= np.array(\['green\_eggs', 'ham'\], dtype\=np.object\_)
\>>> \# don't eat spoiled food
\>>> eat \= ma.masked\_object(food, 'green\_eggs')
\>>> eat
masked\_array(data=\[--, 'ham'\],
             mask=\[ True, False\],
       fill\_value='green\_eggs',
            dtype=object)
\>>> \# plain ol\` ham is boring
\>>> fresh\_food \= np.array(\['cheese', 'ham', 'pineapple'\], dtype\=np.object\_)
\>>> eat \= ma.masked\_object(fresh\_food, 'green\_eggs')
\>>> eat
masked\_array(data=\['cheese', 'ham', 'pineapple'\],
             mask=False,
       fill\_value='green\_eggs',
            dtype=object)

Copy to clipboard

Note that _mask_ is set to `nomask` if possible.

\>>> eat
masked\_array(data=\['cheese', 'ham', 'pineapple'\],
             mask=False,
       fill\_value='green\_eggs',
            dtype=object)

Copy to clipboard

Go BackOpen In Tab

On this page