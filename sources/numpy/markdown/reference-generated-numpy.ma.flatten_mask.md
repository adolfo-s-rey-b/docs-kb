[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatten_mask.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.flatten_mask.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatten_mask.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.flatten_mask.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.flatten_mask.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.flatten_mask.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.flatten_mask.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.flatten_mask.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.flatten_mask.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.flatten_mask.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.flatten_mask.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.flatten_mask.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.flatten_mask.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.flatten_mask.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.flatten_mask.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.flatten_mask.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.flatten_mask.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.flatten_mask.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.flatten_mask.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.flatten_mask.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.flatten_mask.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.flatten_mask.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.flatten\_mask[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatten_mask.html#numpy-ma-flatten-mask "Link to this heading")

====================================================================================================================================================

ma.flatten\_mask(_mask_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L1816-L1870)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.flatten_mask.html#numpy.ma.flatten_mask "Link to this definition")

Returns a completely flattened version of the mask, where nested fields are collapsed.

Parameters:

**mask**array\_like

Input array, which will be interpreted as booleans.

Returns:

**flattened\_mask**ndarray of bools

The flattened input.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> mask \= np.array(\[0, 0, 1\])
\>>> np.ma.flatten\_mask(mask)
array(\[False, False,  True\])

Copy to clipboard

\>>> mask \= np.array(\[(0, 0), (0, 1)\], dtype\=\[('a', bool), ('b', bool)\])
\>>> np.ma.flatten\_mask(mask)
array(\[False, False, False,  True\])

Copy to clipboard

\>>> mdtype \= \[('a', bool), ('b', \[('ba', bool), ('bb', bool)\])\]
\>>> mask \= np.array(\[(0, (0, 0)), (0, (0, 1))\], dtype\=mdtype)
\>>> np.ma.flatten\_mask(mask)
array(\[False, False, False, False, False,  True\])

Copy to clipboard

Go BackOpen In Tab

On this page