[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.angle.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.angle.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.angle.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.angle.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.angle.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.angle.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.angle.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.angle.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.angle.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.angle.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.angle.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.angle.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.angle.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.angle.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.angle.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.angle.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.angle.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.angle.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.angle.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.angle.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.angle.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.angle.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.angle[#](https://numpy.org/doc/stable/reference/generated/numpy.angle.html#numpy-angle "Link to this heading")

=====================================================================================================================

numpy.angle(_z_, _deg\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L1693-L1744)
[#](https://numpy.org/doc/stable/reference/generated/numpy.angle.html#numpy.angle "Link to this definition")

Return the angle of the complex argument.

Parameters:

**z**array\_like

A complex number or sequence of complex numbers.

**deg**bool, optional

Return angle in degrees if True, radians if False (default).

Returns:

**angle**ndarray or scalar

The counterclockwise angle from the positive real axis on the complex plane in the range `(-pi, pi]`, with dtype as numpy.float64.

See also

[`arctan2`](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")

[`absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html#numpy.absolute "numpy.absolute")

Notes

This function passes the imaginary and real parts of the argument to [`arctan2`](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")
 to compute the result; consequently, it follows the convention of [`arctan2`](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")
 when the magnitude of the argument is zero. See example.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.angle(\[1.0, 1.0j, 1+1j\])               \# in radians
array(\[ 0.        ,  1.57079633,  0.78539816\]) # may vary
\>>> np.angle(1+1j, deg\=True)                  \# in degrees
45.0
\>>> np.angle(\[0., \-0., complex(0., \-0.), complex(\-0., \-0.)\])  \# convention
array(\[ 0.        ,  3.14159265, -0.        , -3.14159265\])

Copy to clipboard

Go BackOpen In Tab

On this page