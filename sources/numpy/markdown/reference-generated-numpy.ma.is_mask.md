[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_mask.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.is_mask.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_mask.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.is_mask.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.is_mask.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.is_mask.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.is_mask.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.is_mask.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.is_mask.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.is_mask.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.is_mask.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.is_mask.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.is_mask.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.is_mask.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.is_mask.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.is_mask.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.is_mask.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.is_mask.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.is_mask.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.is_mask.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.is_mask.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.is_mask.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.is\_mask[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_mask.html#numpy-ma-is-mask "Link to this heading")

=====================================================================================================================================

ma.is\_mask(_m_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L1528-L1594)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.is_mask.html#numpy.ma.is_mask "Link to this definition")

Return True if m is a valid, standard mask.

This function does not check the contents of the input, only that the type is MaskType. In particular, this function returns False if the mask has a flexible dtype.

Parameters:

**m**array\_like

Array to test.

Returns:

**result**bool

True if _m.dtype.type_ is MaskType, False otherwise.

See also

[`ma.isMaskedArray`](https://numpy.org/doc/stable/reference/generated/numpy.ma.isMaskedArray.html#numpy.ma.isMaskedArray "numpy.ma.isMaskedArray")

Test whether input is an instance of MaskedArray.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> m \= ma.masked\_equal(\[0, 1, 0, 2, 3\], 0)
\>>> m
masked\_array(data=\[--, 1, --, 2, 3\],
             mask=\[ True, False,  True, False, False\],
       fill\_value=0)
\>>> ma.is\_mask(m)
False
\>>> ma.is\_mask(m.mask)
True

Copy to clipboard

Input must be an ndarray (or have similar attributes) for it to be considered a valid mask.

\>>> m \= \[False, True, False\]
\>>> ma.is\_mask(m)
False
\>>> m \= np.array(\[False, True, False\])
\>>> m
array(\[False,  True, False\])
\>>> ma.is\_mask(m)
True

Copy to clipboard

Arrays with complex dtypes don’t return True.

\>>> dtype \= np.dtype({'names':\['monty', 'pithon'\],
...                   'formats':\[bool, bool\]})
\>>> dtype
dtype(\[('monty', '|b1'), ('pithon', '|b1')\])
\>>> m \= np.array(\[(True, False), (False, True), (True, False)\],
...              dtype\=dtype)
\>>> m
array(\[( True, False), (False,  True), ( True, False)\],
      dtype=\[('monty', '?'), ('pithon', '?')\])
\>>> ma.is\_mask(m)
False

Copy to clipboard

Go BackOpen In Tab

On this page