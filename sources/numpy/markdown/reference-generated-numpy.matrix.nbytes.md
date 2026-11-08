[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.nbytes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.matrix.nbytes[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.nbytes.html#numpy-matrix-nbytes "Link to this heading")

=============================================================================================================================================

attribute

matrix.nbytes[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.nbytes.html#numpy.matrix.nbytes "Link to this definition")

Total bytes consumed by the elements of the array.

See also

[`sys.getsizeof`](https://docs.python.org/3/library/sys.html#sys.getsizeof "(in Python v3.14)")

Memory consumed by the object itself without parents in case view. This does include memory consumed by non-element attributes.

Notes

Does not include memory consumed by non-element attributes of the array object.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.zeros((3,5,2), dtype\=np.complex128)
\>>> x.nbytes
480
\>>> np.prod(x.shape) \* x.itemsize
480

Copy to clipboard

Go BackOpen In Tab

On this page