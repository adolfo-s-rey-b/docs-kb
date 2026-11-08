[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.harden_mask.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.harden_mask.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.harden_mask.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.harden\_mask[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.harden_mask.html#numpy-ma-maskedarray-harden-mask "Link to this heading")

=====================================================================================================================================================================================

method

ma.MaskedArray.harden\_mask()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L3620-L3636)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.harden_mask.html#numpy.ma.MaskedArray.harden_mask "Link to this definition")

Force the mask to hard, preventing unmasking by assignment.

Whether the mask of a masked array is hard or soft is determined by its [`hardmask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.hardmask "numpy.ma.MaskedArray.hardmask")
 property. [`harden_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.harden_mask.html#numpy.ma.MaskedArray.harden_mask "numpy.ma.MaskedArray.harden_mask")
 sets [`hardmask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.hardmask "numpy.ma.MaskedArray.hardmask")
 to `True` (and returns the modified self).

See also

[`ma.MaskedArray.hardmask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray.hardmask "numpy.ma.MaskedArray.hardmask")

[`ma.MaskedArray.soften_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.soften_mask.html#numpy.ma.MaskedArray.soften_mask "numpy.ma.MaskedArray.soften_mask")

On this page