[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.sin.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.sin.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.sin.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.sin.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.sin.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.sin.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.sin.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.sin.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.sin.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.sin.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.sin.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.sin.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.sin.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.sin.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.sin.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.sin.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.sin.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.sin.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.sin.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.sin.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.sin.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.sin[#](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy-sin "Link to this heading")

===============================================================================================================

numpy.sin(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'sin'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "Link to this definition")

Trigonometric sine, element-wise.

Parameters:

**x**array\_like

Angle, in radians (\\(2 \\pi\\) rad equals 360 degrees).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**array\_like

The sine of each element of x. This is a scalar if _x_ is a scalar.

See also

[`arcsin`](https://numpy.org/doc/stable/reference/generated/numpy.arcsin.html#numpy.arcsin "numpy.arcsin")
, [`sinh`](https://numpy.org/doc/stable/reference/generated/numpy.sinh.html#numpy.sinh "numpy.sinh")
, [`cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")

Notes

The sine is one of the fundamental functions of trigonometry (the mathematical study of triangles). Consider a circle of radius 1 centered on the origin. A ray comes in from the \\(+x\\) axis, makes an angle at the origin (measured counter-clockwise from that axis), and departs from the origin. The \\(y\\) coordinate of the outgoing ray’s intersection with the unit circle is the sine of that angle. It ranges from -1 for \\(x=3\\pi / 2\\) to +1 for \\(\\pi / 2.\\) The function has zeroes where the angle is a multiple of \\(\\pi\\). Sines of angles between \\(\\pi\\) and \\(2\\pi\\) are negative. The numerous properties of the sine and related functions are included in any standard trigonometry text.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Print sine of one angle:

\>>> np.sin(np.pi/2.)
1.0

Copy to clipboard

Print sines of an array of angles given in degrees:

\>>> np.sin(np.array((0., 30., 45., 60., 90.)) \* np.pi / 180. )
array(\[ 0.        ,  0.5       ,  0.70710678,  0.8660254 ,  1.        \])

Copy to clipboard

Plot the sine function:

\>>> import matplotlib.pylab as plt
\>>> x \= np.linspace(\-np.pi, np.pi, 201)
\>>> plt.plot(x, np.sin(x))
\>>> plt.xlabel('Angle \[rad\]')
\>>> plt.ylabel('sin(x)')
\>>> plt.axis('tight')
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-sin-1.png](https://numpy.org/doc/stable/_images/numpy-sin-1.png)

Go BackOpen In Tab

On this page