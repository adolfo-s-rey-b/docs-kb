[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flatten.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.chararray.flatten[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flatten.html#numpy-char-chararray-flatten "Link to this heading")

========================================================================================================================================================================

method

char.chararray.flatten(_order\='C'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flatten.html#numpy.char.chararray.flatten "Link to this definition")

Return a copy of the array collapsed into one dimension.

Parameters:

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

‘C’ means to flatten in row-major (C-style) order. ‘F’ means to flatten in column-major (Fortran- style) order. ‘A’ means to flatten in column-major order if _a_ is Fortran _contiguous_ in memory, row-major order otherwise. ‘K’ means to flatten _a_ in the order the elements occur in memory. The default is ‘C’.

Returns:

**y**ndarray

A copy of the input array, flattened to one dimension.

See also

[`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")

Return a flattened array.

[`flat`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.flat.html#numpy.char.chararray.flat "numpy.char.chararray.flat")

A 1-D flat iterator over the array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1,2\], \[3,4\]\])
\>>> a.flatten()
array(\[1, 2, 3, 4\])
\>>> a.flatten('F')
array(\[1, 3, 2, 4\])

Copy to clipboard

Go BackOpen In Tab

On this page