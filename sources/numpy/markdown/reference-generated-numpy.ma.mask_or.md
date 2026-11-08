[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_or.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.mask\_or[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_or.html#numpy-ma-mask-or "Link to this heading")

=====================================================================================================================================

ma.mask\_or(_m1_, _m2_, _copy\=False_, _shrink\=True_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L1759-L1813)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.mask_or.html#numpy.ma.mask_or "Link to this definition")

Combine two masks with the `logical_or` operator.

The result may be a view on _m1_ or _m2_ if the other is [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
 (i.e. False).

Parameters:

**m1, m2**array\_like

Input masks.

**copy**bool, optional

If copy is False and one of the inputs is [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
, return a view of the other input mask. Defaults to False.

**shrink**bool, optional

Whether to shrink the output to [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
 if all its values are False. Defaults to True.

Returns:

**mask**output mask

The result masks values that are masked in either _m1_ or _m2_.

Raises:

ValueError

If _m1_ and _m2_ have different flexible dtypes.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> m1 \= np.ma.make\_mask(\[0, 1, 1, 0\])
\>>> m2 \= np.ma.make\_mask(\[1, 0, 0, 0\])
\>>> np.ma.mask\_or(m1, m2)
array(\[ True,  True,  True, False\])

Copy to clipboard

Go BackOpen In Tab

On this page