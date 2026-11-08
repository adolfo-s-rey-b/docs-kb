[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.array_equiv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.array_equiv.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.array_equiv.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.array_equiv.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.array_equiv.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.array_equiv.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.array_equiv.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.array_equiv.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.array_equiv.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.array_equiv.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.array_equiv.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.array_equiv.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.array_equiv.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.array_equiv.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.array_equiv.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.array_equiv.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.array_equiv.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.array_equiv.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.array_equiv.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.array_equiv.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.array_equiv.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.array_equiv.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.array\_equiv[#](https://numpy.org/doc/stable/reference/generated/numpy.array_equiv.html#numpy-array-equiv "Link to this heading")

========================================================================================================================================

numpy.array\_equiv(_a1_, _a2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L2560-L2606)
[#](https://numpy.org/doc/stable/reference/generated/numpy.array_equiv.html#numpy.array_equiv "Link to this definition")

Returns True if input arrays are shape consistent and all elements equal.

Shape consistent means they are either the same shape, or one input array can be broadcasted to create the same shape as the other one.

Parameters:

**a1, a2**array\_like

Input arrays.

Returns:

**out**bool

True if equivalent, False otherwise.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.array\_equiv(\[1, 2\], \[1, 2\])
True
\>>> np.array\_equiv(\[1, 2\], \[1, 3\])
False

Copy to clipboard

Showing the shape equivalence:

\>>> np.array\_equiv(\[1, 2\], \[\[1, 2\], \[1, 2\]\])
True
\>>> np.array\_equiv(\[1, 2\], \[\[1, 2, 1, 2\], \[1, 2, 1, 2\]\])
False

Copy to clipboard

\>>> np.array\_equiv(\[1, 2\], \[\[1, 2\], \[1, 3\]\])
False

Copy to clipboard

Go BackOpen In Tab

On this page