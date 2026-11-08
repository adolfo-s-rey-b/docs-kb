[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.real.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndarray.real[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.real.html#numpy-ndarray-real "Link to this heading")

==========================================================================================================================================

attribute

ndarray.real[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.real.html#numpy.ndarray.real "Link to this definition")

The real part of the array.

Usually returns a view into the original array, but returns elementwise `.real` for arrays of objects.

See also

[`numpy.real`](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "numpy.real")

equivalent function

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.sqrt(\[1+0j, 0+1j\])
\>>> x.real
array(\[ 1.        ,  0.70710678\])
\>>> x.real.dtype
dtype('float64')

Copy to clipboard

Go BackOpen In Tab

On this page