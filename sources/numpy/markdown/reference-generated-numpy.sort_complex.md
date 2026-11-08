[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.sort_complex.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.sort_complex.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.sort_complex.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.sort_complex.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.sort_complex.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.sort_complex.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.sort_complex.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.sort_complex.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.sort_complex.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.sort_complex.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.sort_complex.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.sort_complex.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.sort_complex.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.sort_complex.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.sort_complex.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.sort_complex.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.sort_complex.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.sort_complex.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.sort_complex.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.sort_complex.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.sort_complex.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.sort_complex.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.sort\_complex[#](https://numpy.org/doc/stable/reference/generated/numpy.sort_complex.html#numpy-sort-complex "Link to this heading")

===========================================================================================================================================

numpy.sort\_complex(_a_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L1870-L1905)
[#](https://numpy.org/doc/stable/reference/generated/numpy.sort_complex.html#numpy.sort_complex "Link to this definition")

Sort a complex array using the real part first, then the imaginary part.

Parameters:

**a**array\_like

Input array

Returns:

**out**complex ndarray

Always returns a sorted complex array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.sort\_complex(\[5, 3, 6, 2, 1\])
array(\[1.+0.j, 2.+0.j, 3.+0.j, 5.+0.j, 6.+0.j\])

Copy to clipboard

\>>> np.sort\_complex(\[1 + 2j, 2 \- 1j, 3 \- 2j, 3 \- 3j, 3 + 5j\])
array(\[1.+2.j,  2.-1.j,  3.-3.j,  3.-2.j,  3.+5.j\])

Copy to clipboard

Go BackOpen In Tab

On this page