[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.imag.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.matrix.imag[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.imag.html#numpy-matrix-imag "Link to this heading")

=======================================================================================================================================

attribute

matrix.imag[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.imag.html#numpy.matrix.imag "Link to this definition")

The imaginary part of the array.

Returns a view into the original array for complex arrays. For non-complex arrays, returns a zero array of the same dtype. For `object` arrays returns elementwise `.imag` or `0` if `.imag` is undefined.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.sqrt(\[1+0j, 0+1j\])
\>>> x.imag
array(\[ 0.        ,  0.70710678\])
\>>> x.imag.dtype
dtype('float64')

Copy to clipboard

Go BackOpen In Tab

On this page