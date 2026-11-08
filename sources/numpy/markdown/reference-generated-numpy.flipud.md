[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.flipud.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.flipud.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.flipud.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.flipud.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.flipud.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.flipud.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.flipud.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.flipud.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.flipud.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.flipud.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.flipud.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.flipud.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.flipud.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.flipud.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.flipud.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.flipud.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.flipud.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.flipud.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.flipud.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.flipud.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.flipud[#](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy-flipud "Link to this heading")

========================================================================================================================

numpy.flipud(_m_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L120-L175)
[#](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy.flipud "Link to this definition")

Reverse the order of elements along axis 0 (up/down).

For a 2-D array, this flips the entries in each column in the up/down direction. Rows are preserved, but appear in a different order than before.

Parameters:

**m**array\_like

Input array.

Returns:

**out**array\_like

A view of _m_ with the rows reversed. Since a view is returned, this operation is \\(\\mathcal O(1)\\).

See also

[`fliplr`](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy.fliplr "numpy.fliplr")

Flip array in the left/right direction.

[`flip`](https://numpy.org/doc/stable/reference/generated/numpy.flip.html#numpy.flip "numpy.flip")

Flip array in one or more dimensions.

[`rot90`](https://numpy.org/doc/stable/reference/generated/numpy.rot90.html#numpy.rot90 "numpy.rot90")

Rotate array counterclockwise.

Notes

Equivalent to `m[::-1, ...]` or `np.flip(m, axis=0)`. Requires the array to be at least 1-D.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> A \= np.diag(\[1.0, 2, 3\])
\>>> A
array(\[\[1.,  0.,  0.\],\
       \[0.,  2.,  0.\],\
       \[0.,  0.,  3.\]\])
\>>> np.flipud(A)
array(\[\[0.,  0.,  3.\],\
       \[0.,  2.,  0.\],\
       \[1.,  0.,  0.\]\])

Copy to clipboard

\>>> rng \= np.random.default\_rng()
\>>> A \= rng.normal(size\=(2,3,5))
\>>> np.all(np.flipud(A) \== A\[::\-1,...\])
True

Copy to clipboard

\>>> np.flipud(\[1,2\])
array(\[2, 1\])

Copy to clipboard

Go BackOpen In Tab

On this page