[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.itemsize.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.matrix.itemsize[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.itemsize.html#numpy-matrix-itemsize "Link to this heading")

===================================================================================================================================================

attribute

matrix.itemsize[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.itemsize.html#numpy.matrix.itemsize "Link to this definition")

Length of one array element in bytes.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1,2,3\], dtype\=np.float64)
\>>> x.itemsize
8
\>>> x \= np.array(\[1,2,3\], dtype\=np.complex128)
\>>> x.itemsize
16

Copy to clipboard

Go BackOpen In Tab

On this page