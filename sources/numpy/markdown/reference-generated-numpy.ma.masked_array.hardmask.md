[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.hardmask.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.hardmask.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.hardmask.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.hardmask.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.hardmask.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.hardmask.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.hardmask.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.hardmask.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.hardmask.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.hardmask[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.hardmask.html#numpy-ma-masked-array-hardmask "Link to this heading")

===============================================================================================================================================================================

property

_property_ ma.masked\_array.hardmask[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.hardmask.html#numpy.ma.masked_array.hardmask "Link to this definition")

Specifies whether values can be unmasked through assignments.

By default, assigning definite values to masked array entries will unmask them. When [`hardmask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.hardmask.html#numpy.ma.masked_array.hardmask "numpy.ma.masked_array.hardmask")
 is `True`, the mask will not change through assignments.

See also

[`ma.MaskedArray.harden_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.harden_mask.html#numpy.ma.MaskedArray.harden_mask "numpy.ma.MaskedArray.harden_mask")

[`ma.MaskedArray.soften_mask`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.soften_mask.html#numpy.ma.MaskedArray.soften_mask "numpy.ma.MaskedArray.soften_mask")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(10)
\>>> m \= np.ma.masked\_array(x, x\>5)
\>>> assert not m.hardmask

Copy to clipboard

Since _m_ has a soft mask, assigning an element value unmasks that element:

\>>> m\[8\] \= 42
\>>> m
masked\_array(data=\[0, 1, 2, 3, 4, 5, --, --, 42, --\],
             mask=\[False, False, False, False, False, False,\
                   True, True, False, True\],
       fill\_value=999999)

Copy to clipboard

After hardening, the mask is not affected by assignments:

\>>> hardened \= np.ma.harden\_mask(m)
\>>> assert m.hardmask and hardened is m
\>>> m\[:\] \= 23
\>>> m
masked\_array(data=\[23, 23, 23, 23, 23, 23, --, --, 23, --\],
             mask=\[False, False, False, False, False, False,\
                   True, True, False, True\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page