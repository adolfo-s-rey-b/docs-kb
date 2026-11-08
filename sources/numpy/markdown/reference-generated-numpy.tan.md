[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.tan.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.tan.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.tan.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.tan.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.tan.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.tan.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.tan.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.tan.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.tan.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.tan.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.tan.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.tan.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.tan.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.tan.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.tan.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.tan.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.tan.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.tan.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.tan.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.tan.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.tan.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.tan.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.tan[#](https://numpy.org/doc/stable/reference/generated/numpy.tan.html#numpy-tan "Link to this heading")

===============================================================================================================

numpy.tan(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'tan'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.tan.html#numpy.tan "Link to this definition")

Compute tangent element-wise.

Equivalent to `np.sin(x)/np.cos(x)` element-wise.

Parameters:

**x**array\_like

Input array.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The corresponding tangent values. This is a scalar if _x_ is a scalar.

Notes

If _out_ is provided, the function writes the result into it, and returns a reference to _out_. (See Examples)

References

M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions. New York, NY: Dover, 1972.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from math import pi
\>>> np.tan(np.array(\[\-pi,pi/2,pi\]))
array(\[  1.22460635e-16,   1.63317787e+16,  -1.22460635e-16\])
\>>>
\>>> \# Example of providing the optional output parameter illustrating
\>>> \# that what is returned is a reference to said parameter
\>>> out1 \= np.array(\[0\], dtype\=np.float64)
\>>> out2 \= np.cos(\[0.1\], out1)
\>>> out2 is out1
True
\>>>
\>>> \# Example of ValueError due to provision of shape mis-matched \`out\`
\>>> np.cos(np.zeros((3,3)),np.zeros((2,2)))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operands could not be broadcast together with shapes (3,3) (2,2)

Copy to clipboard

Go BackOpen In Tab

On this page