[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.arctan.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.arctan.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.arctan.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.arctan.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.arctan.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.arctan.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.arctan.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.arctan.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.arctan.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.arctan.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.arctan.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.arctan.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.arctan.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.arctan.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.arctan.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.arctan.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.arctan.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.arctan.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.arctan.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.arctan.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.arctan[#](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy-arctan "Link to this heading")

========================================================================================================================

numpy.arctan(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'arctan'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "Link to this definition")

Trigonometric inverse tangent, element-wise.

The inverse of tan, so that if `y = tan(x)` then `x = arctan(y)`.

Parameters:

**x**array\_like

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**out**ndarray or scalar

Out has the same shape as _x_. Its real part is in `[-pi/2, pi/2]` (`arctan(+/-inf)` returns `+/-pi/2`). This is a scalar if _x_ is a scalar.

See also

[`arctan2`](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")

The “four quadrant” arctan of the angle formed by (_x_, _y_) and the positive _x_\-axis.

[`angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html#numpy.angle "numpy.angle")

Argument of complex values.

Notes

[`arctan`](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "numpy.arctan")
 is a multi-valued function: for each _x_ there are infinitely many numbers _z_ such that tan(_z_) = _x_. The convention is to return the angle _z_ whose real part lies in \[-pi/2, pi/2\].

For real-valued input data types, [`arctan`](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "numpy.arctan")
 always returns real output. For each value that cannot be expressed as a real number or infinity, it yields `nan` and sets the _invalid_ floating point error flag.

For complex-valued input, [`arctan`](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "numpy.arctan")
 is a complex analytic function that has \[`1j, infj`\] and \[`-1j, -infj`\] as branch cuts, and is continuous from the left on the former and from the right on the latter.

The inverse tangent is also known as [`atan`](https://numpy.org/doc/stable/reference/generated/numpy.atan.html#numpy.atan "numpy.atan")
 or tan^{-1}.

References

Abramowitz, M. and Stegun, I. A., _Handbook of Mathematical Functions_, 10th printing, New York: Dover, 1964, pp. 79. [https://personal.math.ubc.ca/~cbm/aands/page\_79.htm](https://personal.math.ubc.ca/~cbm/aands/page_79.htm)

Examples

Try it in your browser!

We expect the arctan of 0 to be 0, and of 1 to be pi/4:

\>>> import numpy as np
\>>> np.arctan(\[0, 1\])
array(\[ 0.        ,  0.78539816\])

Copy to clipboard

\>>> np.pi/4
0.78539816339744828

Copy to clipboard

Plot arctan:

\>>> import matplotlib.pyplot as plt
\>>> x \= np.linspace(\-10, 10)
\>>> plt.plot(x, np.arctan(x))
\>>> plt.axis('tight')
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-arctan-1.png](https://numpy.org/doc/stable/_images/numpy-arctan-1.png)

Go BackOpen In Tab

On this page