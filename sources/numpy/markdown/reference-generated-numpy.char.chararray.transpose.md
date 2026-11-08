[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.transpose.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.chararray.transpose[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.transpose.html#numpy-char-chararray-transpose "Link to this heading")

==============================================================================================================================================================================

method

char.chararray.transpose(_\*axes_)[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.transpose.html#numpy.char.chararray.transpose "Link to this definition")

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