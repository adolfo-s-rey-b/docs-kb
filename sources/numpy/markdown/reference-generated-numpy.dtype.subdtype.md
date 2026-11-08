[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtype.subdtype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dtype.subdtype.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dtype.subdtype.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dtype.subdtype.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dtype.subdtype.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dtype.subdtype.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dtype.subdtype.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dtype.subdtype.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dtype.subdtype.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dtype.subdtype.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dtype.subdtype.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dtype.subdtype.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dtype.subdtype.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dtype.subdtype.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dtype.subdtype.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dtype.subdtype.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dtype.subdtype.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dtype.subdtype.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dtype.subdtype.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dtype.subdtype.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dtype.subdtype.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dtype.subdtype.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtype.subdtype[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.subdtype.html#numpy-dtype-subdtype "Link to this heading")

================================================================================================================================================

attribute

dtype.subdtype[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.subdtype.html#numpy.dtype.subdtype "Link to this definition")

Tuple `(item_dtype, shape)` if this [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 describes a sub-array, and None otherwise.

The _shape_ is the fixed shape of the sub-array described by this data type, and _item\_dtype_ the data type of the array.

If a field whose dtype object has this attribute is retrieved, then the extra dimensions implied by _shape_ are tacked on to the end of the retrieved array.

See also

[`dtype.base`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.base.html#numpy.dtype.base "numpy.dtype.base")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.dtype('8f')
\>>> x.subdtype
(dtype('float32'), (8,))

Copy to clipboard

\>>> x \=  np.dtype(np.int16)
\>>> x.subdtype
\>>>

Copy to clipboard

Go BackOpen In Tab

On this page