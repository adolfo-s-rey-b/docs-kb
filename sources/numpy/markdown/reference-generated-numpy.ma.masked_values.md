[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_values.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_values.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_values.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_values.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_values.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_values.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_values.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_values.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_values.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_values.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_values.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_values.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_values.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_values.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_values.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_values.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_values.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_values.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_values.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_values.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.masked\_values[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#numpy-ma-masked-values "Link to this heading")

=======================================================================================================================================================

ma.masked\_values(_x_, _value_, _rtol\=1e-05_, _atol\=1e-08_, _copy\=True_, _shrink\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L2327-L2397)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#numpy.ma.masked_values "Link to this definition")

Mask using floating point equality.

Return a MaskedArray, masked where the data in array _x_ are approximately equal to _value_, determined using [`isclose`](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose "numpy.isclose")
. The default tolerances for [`masked_values`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#numpy.ma.masked_values "numpy.ma.masked_values")
 are the same as those for [`isclose`](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose "numpy.isclose")
.

For integer types, exact equality is used, in the same way as [`masked_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_equal.html#numpy.ma.masked_equal "numpy.ma.masked_equal")
.

The fill\_value is set to _value_ and the mask is set to `nomask` if possible.

Parameters:

**x**array\_like

Array to mask.

**value**float

Masking value.

**rtol, atol**float, optional

Tolerance parameters passed on to [`isclose`](https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose "numpy.isclose")

**copy**bool, optional

Whether to return a copy of _x_.

**shrink**bool, optional

Whether to collapse a mask full of False to `nomask`.

Returns:

**result**MaskedArray

The result of masking _x_ where approximately equal to _value_.

See also

[`masked_where`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_where.html#numpy.ma.masked_where "numpy.ma.masked_where")

Mask where a condition is met.

[`masked_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_equal.html#numpy.ma.masked_equal "numpy.ma.masked_equal")

Mask where equal to a given value (integers).

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= np.array(\[1, 1.1, 2, 1.1, 3\])
\>>> ma.masked\_values(x, 1.1)
masked\_array(data=\[1.0, --, 2.0, --, 3.0\],
             mask=\[False,  True, False,  True, False\],
       fill\_value=1.1)

Copy to clipboard

Note that _mask_ is set to `nomask` if possible.

\>>> ma.masked\_values(x, 2.1)
masked\_array(data=\[1. , 1.1, 2. , 1.1, 3. \],
             mask=False,
       fill\_value=2.1)

Copy to clipboard

Unlike [`masked_equal`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_equal.html#numpy.ma.masked_equal "numpy.ma.masked_equal")
, [`masked_values`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html#numpy.ma.masked_values "numpy.ma.masked_values")
 can perform approximate equalities.

\>>> ma.masked\_values(x, 2.1, atol\=1e-1)
masked\_array(data=\[1.0, 1.1, --, 1.1, 3.0\],
             mask=\[False, False,  True, False, False\],
       fill\_value=2.1)

Copy to clipboard

Go BackOpen In Tab

On this page