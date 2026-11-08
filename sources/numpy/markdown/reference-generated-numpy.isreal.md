[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.isreal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.isreal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.isreal.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.isreal.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.isreal.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.isreal.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.isreal.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.isreal.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.isreal.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.isreal.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.isreal.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.isreal.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.isreal.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.isreal.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.isreal.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.isreal.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.isreal.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.isreal.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.isreal.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.isreal.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.isreal.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.isreal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.isreal[#](https://numpy.org/doc/stable/reference/generated/numpy.isreal.html#numpy-isreal "Link to this heading")

========================================================================================================================

numpy.isreal(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_type_check_impl.py#L214-L262)
[#](https://numpy.org/doc/stable/reference/generated/numpy.isreal.html#numpy.isreal "Link to this definition")

Returns a bool array, where True if input element is real.

If element has complex type with zero imaginary part, the return value for that element is True.

Parameters:

**x**array\_like

Input array.

Returns:

**out**ndarray, bool

Boolean array of same shape as _x_.

See also

[`iscomplex`](https://numpy.org/doc/stable/reference/generated/numpy.iscomplex.html#numpy.iscomplex "numpy.iscomplex")

[`isrealobj`](https://numpy.org/doc/stable/reference/generated/numpy.isrealobj.html#numpy.isrealobj "numpy.isrealobj")

Return True if x is not a complex type.

Notes

[`isreal`](https://numpy.org/doc/stable/reference/generated/numpy.isreal.html#numpy.isreal "numpy.isreal")
 may behave unexpectedly for string or object arrays (see examples)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[1+1j, 1+0j, 4.5, 3, 2, 2j\], dtype\=np.complex128)
\>>> np.isreal(a)
array(\[False,  True,  True,  True,  True, False\])

Copy to clipboard

The function does not work on string arrays.

\>>> a \= np.array(\[2j, "a"\], dtype\=np.str\_)
\>>> np.isreal(a)  \# returns the result of \`"" == 0\` currently.
array(\[False, False\])

Copy to clipboard

Returns True for all elements that either have no `.imag` attribute or for which that attribute is zero:

\>>> a \= np.array(\[1, "2", 3+4j\], dtype\=np.object\_)
\>>> np.isreal(a)
array(\[ True,  True,  False\])

Copy to clipboard

Go BackOpen In Tab

On this page