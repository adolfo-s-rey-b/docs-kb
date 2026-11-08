[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.memmap.size.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.memmap.size[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.size.html#numpy-memmap-size "Link to this heading")

=======================================================================================================================================

attribute

memmap.size[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.size.html#numpy.memmap.size "Link to this definition")

Number of elements in the array.

Equal to `np.prod(a.shape)`, i.e., the product of the array’s dimensions.

Notes

_a.size_ returns a standard arbitrary precision Python integer. This may not be the case with other methods of obtaining the same value (like the suggested `np.prod(a.shape)`, which returns an instance of `np.int_`), and may be relevant if the value is used further in calculations that may overflow a fixed size integer type.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.zeros((3, 5, 2), dtype\=np.complex128)
\>>> x.size
30
\>>> np.prod(x.shape)
30

Copy to clipboard

Go BackOpen In Tab

On this page