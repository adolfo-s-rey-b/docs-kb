[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.transpose.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.transpose.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.transpose.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.transpose.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.transpose.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.transpose.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.transpose.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.transpose.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.transpose.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.transpose[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.transpose.html#numpy-ma-maskedarray-transpose "Link to this heading")

==============================================================================================================================================================================

method

ma.MaskedArray.transpose(_\*axes_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L2642-L2652)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.transpose.html#numpy.ma.MaskedArray.transpose "Link to this definition")

Returns a view of the array with axes transposed.

Refer to [`numpy.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")
 for full documentation.

Parameters:

**axes**None, tuple of ints, or _n_ ints

*   None or no argument: reverses the order of the axes.
    
*   tuple of ints: _i_ in the _j_\-th place in the tuple means that the array’s _i_\-th axis becomes the transposed array’s _j_\-th axis.
    
*   _n_ ints: same as an n-tuple of the same ints (this form is intended simply as a “convenience” alternative to the tuple form).
    

Returns:

**p**ndarray

View of the array with its axes suitably permuted.

See also

[`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")

Equivalent function.

[`ndarray.T`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T "numpy.ndarray.T")

Array property returning the array transposed.

[`ndarray.reshape`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.reshape.html#numpy.ndarray.reshape "numpy.ndarray.reshape")

Return a reshaped ndarray without changing data.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> a
array(\[\[1, 2\],\
       \[3, 4\]\])
\>>> a.transpose()
array(\[\[1, 3\],\
       \[2, 4\]\])
\>>> a.transpose((1, 0))
array(\[\[1, 3\],\
       \[2, 4\]\])
\>>> a.transpose(1, 0)
array(\[\[1, 3\],\
       \[2, 4\]\])

Copy to clipboard

\>>> a \= np.array(\[1, 2, 3, 4\])
\>>> a
array(\[1, 2, 3, 4\])
\>>> a.transpose()
array(\[1, 2, 3, 4\])

Copy to clipboard

Go BackOpen In Tab

On this page