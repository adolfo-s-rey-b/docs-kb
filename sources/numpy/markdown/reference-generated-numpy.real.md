[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.real.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.real.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.real.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.real.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.real.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.real.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.real.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.real.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.real.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.real.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.real.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.real.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.real.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.real.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.real.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.real.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.real.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.real.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.real.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.real.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.real.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.real.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.real[#](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy-real "Link to this heading")

==================================================================================================================

numpy.real(_val_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_type_check_impl.py#L85-L125)
[#](https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real "Link to this definition")

Return the real part of the complex argument.

Parameters:

**val**array\_like

Input array.

Returns:

**out**ndarray or scalar

The real component of the complex argument. If _val_ is real, the type of _val_ is used for the output. If _val_ has complex elements, the returned type is float.

See also

[`real_if_close`](https://numpy.org/doc/stable/reference/generated/numpy.real_if_close.html#numpy.real_if_close "numpy.real_if_close")
, [`imag`](https://numpy.org/doc/stable/reference/generated/numpy.imag.html#numpy.imag "numpy.imag")
, [`angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html#numpy.angle "numpy.angle")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[1+2j, 3+4j, 5+6j\])
\>>> a.real
array(\[1.,  3.,  5.\])
\>>> a.real \= 9
\>>> a
array(\[9.+2.j,  9.+4.j,  9.+6.j\])
\>>> a.real \= np.array(\[9, 8, 7\])
\>>> a
array(\[9.+2.j,  8.+4.j,  7.+6.j\])
\>>> np.real(1 + 1j)
1.0

Copy to clipboard

Go BackOpen In Tab

On this page