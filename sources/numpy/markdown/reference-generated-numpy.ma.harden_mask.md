[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.harden_mask.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.harden\_mask[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.harden_mask.html#numpy-ma-harden-mask "Link to this heading")

=================================================================================================================================================

ma.harden\_mask(_self_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7079-L7080)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.harden_mask.html#numpy.ma.harden_mask "Link to this definition")

Force the mask to hard, preventing unmasking by assignment.

Whether the mask of a masked array is hard or soft is determined by its [`hardmask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.hardmask "numpy.ma.MaskedArray.hardmask")
 property. [`harden_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.harden_mask.html#numpy.ma.harden_mask "numpy.ma.harden_mask")
 sets [`hardmask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.hardmask "numpy.ma.MaskedArray.hardmask")
 to `True` (and returns the modified self).

See also

[`ma.MaskedArray.hardmask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.hardmask "numpy.ma.MaskedArray.hardmask")

[`ma.MaskedArray.soften_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.soften_mask.html#numpy.ma.MaskedArray.soften_mask "numpy.ma.MaskedArray.soften_mask")

On this page