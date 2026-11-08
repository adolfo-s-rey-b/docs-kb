[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.size.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.size.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.size.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.size.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.size.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.size.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.size.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.size.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.size.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.size.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.size.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.size.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.size.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.size.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.size.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.size.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.size.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.size.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.size.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.size.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.size.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.size.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.size[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.size.html#numpy-ma-masked-array-size "Link to this heading")

===================================================================================================================================================================

attribute

ma.masked\_array.size[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.size.html#numpy.ma.masked_array.size "Link to this definition")

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