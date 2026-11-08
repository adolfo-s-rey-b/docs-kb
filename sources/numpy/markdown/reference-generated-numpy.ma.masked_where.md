[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_where.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_where.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_where.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_where.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_where.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_where.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_where.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_where.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_where.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_where.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_where.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_where.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_where.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_where.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_where.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_where.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_where.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_where.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_where.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_where.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.masked\_where[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy-ma-masked-where "Link to this heading")

====================================================================================================================================================

ma.masked\_where(_condition_, _a_, _copy\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L1885-L2005)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "Link to this definition")

Mask an array where a condition is met.

Return _a_ as an array masked where _condition_ is True. Any masked values of _a_ or _condition_ are also masked in the output.

Parameters:

**condition**array\_like

Masking condition. When _condition_ tests floating point values for equality, consider using `masked_values` instead.

**a**array\_like

Array to mask.

**copy**bool

If True (default) make a copy of _a_ in the result. If False modify _a_ in place and return a view.

Returns:

**result**MaskedArray

The result of masking _a_ where _condition_ is True.

See also

[`masked_values`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#numpy.ma.masked_values "numpy.ma.masked_values")

Mask using floating point equality.

[`masked_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_equal.html#numpy.ma.masked_equal "numpy.ma.masked_equal")

Mask where equal to a given value.

[`masked_not_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_not_equal.html#numpy.ma.masked_not_equal "numpy.ma.masked_not_equal")

Mask where _not_ equal to a given value.

[`masked_less_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less_equal.html#numpy.ma.masked_less_equal "numpy.ma.masked_less_equal")

Mask where less than or equal to a given value.

[`masked_greater_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater_equal.html#numpy.ma.masked_greater_equal "numpy.ma.masked_greater_equal")

Mask where greater than or equal to a given value.

[`masked_less`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_less.html#numpy.ma.masked_less "numpy.ma.masked_less")

Mask where less than a given value.

[`masked_greater`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_greater.html#numpy.ma.masked_greater "numpy.ma.masked_greater")

Mask where greater than a given value.

[`masked_inside`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_inside.html#numpy.ma.masked_inside "numpy.ma.masked_inside")

Mask inside a given interval.

[`masked_outside`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_outside.html#numpy.ma.masked_outside "numpy.ma.masked_outside")

Mask outside a given interval.

[`masked_invalid`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_invalid.html#numpy.ma.masked_invalid "numpy.ma.masked_invalid")

Mask invalid values (NaNs or infs).

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> a \= np.arange(4)
\>>> a
array(\[0, 1, 2, 3\])
\>>> ma.masked\_where(a <= 2, a)
masked\_array(data=\[--, --, --, 3\],
             mask=\[ True,  True,  True, False\],
       fill\_value=999999)

Copy to clipboard

Mask array _b_ conditional on _a_.

\>>> b \= \['a', 'b', 'c', 'd'\]
\>>> ma.masked\_where(a \== 2, b)
masked\_array(data=\['a', 'b', --, 'd'\],
             mask=\[False, False,  True, False\],
       fill\_value='N/A',
            dtype='<U1')

Copy to clipboard

Effect of the [`copy`](https://numpy.org/doc/stable/reference/generated/numpy.copy.html#numpy.copy "numpy.copy")
 argument.

\>>> c \= ma.masked\_where(a <= 2, a)
\>>> c
masked\_array(data=\[--, --, --, 3\],
             mask=\[ True,  True,  True, False\],
       fill\_value=999999)
\>>> c\[0\] \= 99
\>>> c
masked\_array(data=\[99, --, --, 3\],
             mask=\[False,  True,  True, False\],
       fill\_value=999999)
\>>> a
array(\[0, 1, 2, 3\])
\>>> c \= ma.masked\_where(a <= 2, a, copy\=False)
\>>> c\[0\] \= 99
\>>> c
masked\_array(data=\[99, --, --, 3\],
             mask=\[False,  True,  True, False\],
       fill\_value=999999)
\>>> a
array(\[99,  1,  2,  3\])

Copy to clipboard

When _condition_ or _a_ contain masked values.

\>>> a \= np.arange(4)
\>>> a \= ma.masked\_where(a \== 2, a)
\>>> a
masked\_array(data=\[0, 1, --, 3\],
             mask=\[False, False,  True, False\],
       fill\_value=999999)
\>>> b \= np.arange(4)
\>>> b \= ma.masked\_where(b \== 0, b)
\>>> b
masked\_array(data=\[--, 1, 2, 3\],
             mask=\[ True, False, False, False\],
       fill\_value=999999)
\>>> ma.masked\_where(a \== 3, b)
masked\_array(data=\[--, 1, --, --\],
             mask=\[ True, False,  True,  True\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page