[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.acos.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.acos.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.acos.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.acos.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.acos.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.acos.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.acos.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.acos.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.acos.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.acos.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.acos.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.acos.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.acos.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.acos.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.acos.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.acos.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.acos.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.acos.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.acos.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.acos.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.acos.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.acos.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.acos[#](https://numpy.org/doc/stable/reference/generated/numpy.acos.html#numpy-acos "Link to this heading")

==================================================================================================================

numpy.acos(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'arccos'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.acos.html#numpy.acos "Link to this definition")

Trigonometric inverse cosine, element-wise.

The inverse of [`cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
 so that, if `y = cos(x)`, then `x = arccos(y)`.

Parameters:

**x**array\_like

_x_\-coordinate on the unit circle. For real arguments, the domain is \[-1, 1\].

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**angle**ndarray

The angle of the ray intersecting the unit circle at the given _x_\-coordinate in radians \[0, pi\]. This is a scalar if _x_ is a scalar.

See also

[`cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
, [`arctan`](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "numpy.arctan")
, [`arcsin`](https://numpy.org/doc/stable/reference/generated/numpy.arcsin.html#numpy.arcsin "numpy.arcsin")
, [`emath.arccos`](https://numpy.org/doc/stable/reference/generated/numpy.emath.arccos.html#numpy.emath.arccos "numpy.emath.arccos")

Notes

[`arccos`](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html#numpy.arccos "numpy.arccos")
 is a multivalued function: for each _x_ there are infinitely many numbers _z_ such that `cos(z) = x`. The convention is to return the angle _z_ whose real part lies in _\[0, pi\]_.

For real-valued input data types, [`arccos`](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html#numpy.arccos "numpy.arccos")
 always returns real output. For each value that cannot be expressed as a real number or infinity, it yields `nan` and sets the _invalid_ floating point error flag.

For complex-valued input, [`arccos`](https://numpy.org/doc/stable/reference/generated/numpy.arccos.html#numpy.arccos "numpy.arccos")
 is a complex analytic function that has branch cuts `[-inf, -1]` and _\[1, inf\]_ and is continuous from above on the former and from below on the latter.

The inverse [`cos`](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
 is also known as [`acos`](https://numpy.org/doc/stable/reference/generated/numpy.acos.html#numpy.acos "numpy.acos")
 or cos^-1.

References

M. Abramowitz and I.A. Stegun, “Handbook of Mathematical Functions”, 10th printing, 1964, pp. 79. [https://personal.math.ubc.ca/~cbm/aands/page\_79.htm](https://personal.math.ubc.ca/~cbm/aands/page_79.htm)

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

We expect the arccos of 1 to be 0, and of -1 to be pi:

\>>> np.arccos(\[1, \-1\])
array(\[ 0.        ,  3.14159265\])

Copy to clipboard

Plot arccos:

\>>> import matplotlib.pyplot as plt
\>>> x \= np.linspace(\-1, 1, num\=100)
\>>> plt.plot(x, np.arccos(x))
\>>> plt.axis('tight')
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-acos-1.png](https://numpy.org/doc/stable/_images/numpy-acos-1.png)

Go BackOpen In Tab

On this page