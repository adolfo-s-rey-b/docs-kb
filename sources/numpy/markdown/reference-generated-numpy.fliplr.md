[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fliplr[#](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy-fliplr "Link to this heading")

========================================================================================================================

numpy.fliplr(_m_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_twodim_base_impl.py#L64-L117)
[#](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy.fliplr "Link to this definition")

Reverse the order of elements along axis 1 (left/right).

For a 2-D array, this flips the entries in each row in the left/right direction. Columns are preserved, but appear in a different order than before.

Parameters:

**m**array\_like

Input array, must be at least 2-D.

Returns:

**f**ndarray

A view of _m_ with the columns reversed. Since a view is returned, this operation is \\(\\mathcal O(1)\\).

See also

[`flipud`](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy.flipud "numpy.flipud")

Flip array in the up/down direction.

[`flip`](https://numpy.org/doc/stable/reference/generated/numpy.flip.html#numpy.flip "numpy.flip")

Flip array in one or more dimensions.

[`rot90`](https://numpy.org/doc/stable/reference/generated/numpy.rot90.html#numpy.rot90 "numpy.rot90")

Rotate array counterclockwise.

Notes

Equivalent to `m[:,::-1]` or `np.flip(m, axis=1)`. Requires the array to be at least 2-D.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> A \= np.diag(\[1.,2.,3.\])
\>>> A
array(\[\[1.,  0.,  0.\],\
       \[0.,  2.,  0.\],\
       \[0.,  0.,  3.\]\])
\>>> np.fliplr(A)
array(\[\[0.,  0.,  1.\],\
       \[0.,  2.,  0.\],\
       \[3.,  0.,  0.\]\])

Copy to clipboard

\>>> rng \= np.random.default\_rng()
\>>> A \= rng.normal(size\=(2,3,5))
\>>> np.all(np.fliplr(A) \== A\[:,::\-1,...\])
True

Copy to clipboard

Go BackOpen In Tab

On this page