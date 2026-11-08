[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtype.alignment.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtype.alignment[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.alignment.html#numpy-dtype-alignment "Link to this heading")

===================================================================================================================================================

attribute

dtype.alignment[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.alignment.html#numpy.dtype.alignment "Link to this definition")

The required alignment (bytes) of this data-type according to the compiler.

More information is available in the C-API section of the manual.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.dtype(np.int32)
\>>> x.alignment
4

Copy to clipboard

\>>> x \= np.dtype(np.float64)
\>>> x.alignment
8

Copy to clipboard

Go BackOpen In Tab

On this page