[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.iscomplex.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.iscomplex.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.iscomplex.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.iscomplex.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.iscomplex.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.iscomplex.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.iscomplex.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.iscomplex.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.iscomplex.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.iscomplex.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.iscomplex.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.iscomplex.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.iscomplex.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.iscomplex.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.iscomplex.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.iscomplex.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.iscomplex.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.iscomplex.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.iscomplex.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.iscomplex.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.iscomplex.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.iscomplex.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.iscomplex[#](https://numpy.org/doc/stable/reference/generated/numpy.iscomplex.html#numpy-iscomplex "Link to this heading")

=================================================================================================================================

numpy.iscomplex(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_type_check_impl.py#L176-L211)
[#](https://numpy.org/doc/stable/reference/generated/numpy.iscomplex.html#numpy.iscomplex "Link to this definition")

Returns a bool array, where True if input element is complex.

What is tested is whether the input has a non-zero imaginary part, not if the input type is complex.

Parameters:

**x**array\_like

Input array.

Returns:

**out**ndarray of bools

Output array.

See also

[`isreal`](https://numpy.org/doc/stable/reference/generated/numpy.isreal.html#numpy.isreal "numpy.isreal")

[`iscomplexobj`](https://numpy.org/doc/stable/reference/generated/numpy.iscomplexobj.html#numpy.iscomplexobj "numpy.iscomplexobj")

Return True if x is a complex type or an array of complex numbers.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.iscomplex(\[1+1j, 1+0j, 4.5, 3, 2, 2j\])
array(\[ True, False, False, False, False,  True\])

Copy to clipboard

Go BackOpen In Tab

On this page