[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.where.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.where.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.where.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.where.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.where.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.where.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.where.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.where.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.where.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.where.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.where.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.where.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.where.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.where.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.where.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.where.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.where.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.where.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.where.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.where.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.where.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.where.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.where[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.where.html#numpy-ma-where "Link to this heading")

==============================================================================================================================

ma.where(_condition_, _x=<no value>_, _y=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7930-L8019)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.where.html#numpy.ma.where "Link to this definition")

Return a masked array with elements from _x_ or _y_, depending on condition.

Note

When only _condition_ is provided, this function is identical to [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
. The rest of this documentation covers only the case where all three arguments are provided.

Parameters:

**condition**array\_like, bool

Where True, yield _x_, otherwise yield _y_.

**x, y**array\_like, optional

Values from which to choose. _x_, _y_ and _condition_ need to be broadcastable to some shape.

Returns:

**out**MaskedArray

A masked array with [`masked`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.masked "numpy.ma.masked")
 elements where the condition is masked, elements from _x_ where _condition_ is True, and elements from _y_ elsewhere.

See also

[`numpy.where`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "numpy.where")

Equivalent function in the top-level NumPy module.

[`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")

The function that is called when x and y are omitted

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.array(np.arange(9.).reshape(3, 3), mask\=\[\[0, 1, 0\],\
...                                                    \[1, 0, 1\],\
...                                                    \[0, 1, 0\]\])
\>>> x
masked\_array(
  data=\[\[0.0, --, 2.0\],\
        \[--, 4.0, --\],\
        \[6.0, --, 8.0\]\],
  mask=\[\[False,  True, False\],\
        \[ True, False,  True\],\
        \[False,  True, False\]\],
  fill\_value=1e+20)
\>>> np.ma.where(x \> 5, x, \-3.1416)
masked\_array(
  data=\[\[-3.1416, --, -3.1416\],\
        \[--, -3.1416, --\],\
        \[6.0, --, 8.0\]\],
  mask=\[\[False,  True, False\],\
        \[ True, False,  True\],\
        \[False,  True, False\]\],
  fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page