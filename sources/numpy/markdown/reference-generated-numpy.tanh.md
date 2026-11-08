[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.tanh.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.tanh.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.tanh.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.tanh.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.tanh.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.tanh.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.tanh.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.tanh.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.tanh.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.tanh.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.tanh.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.tanh.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.tanh.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.tanh.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.tanh.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.tanh.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.tanh.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.tanh.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.tanh.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.tanh.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.tanh.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.tanh.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.tanh[#](https://numpy.org/doc/stable/reference/generated/numpy.tanh.html#numpy-tanh "Link to this heading")

==================================================================================================================

numpy.tanh(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'tanh'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.tanh.html#numpy.tanh "Link to this definition")

Hyperbolic tangent, element-wise.

Equivalent to `np.sinh(x)/np.cosh(x)` or `-1j * np.tan(1j*x)`.

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

The corresponding hyperbolic tangent values. This is a scalar if _x_ is a scalar.

Notes

If _out_ is provided, the function writes the result into it, and returns a reference to _out_. (See Examples)

References

\[1\]

M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions. New York, NY: Dover, 1972, pg. 83. [https://personal.math.ubc.ca/~cbm/aands/page\_83.htm](https://personal.math.ubc.ca/~cbm/aands/page_83.htm)

\[2\]

Wikipedia, “Hyperbolic function”, [https://en.wikipedia.org/wiki/Hyperbolic\_function](https://en.wikipedia.org/wiki/Hyperbolic_function)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.tanh((0, np.pi\*1j, np.pi\*1j/2))
array(\[ 0. +0.00000000e+00j,  0. -1.22460635e-16j,  0. +1.63317787e+16j\])

Copy to clipboard

\>>> \# Example of providing the optional output parameter illustrating
\>>> \# that what is returned is a reference to said parameter
\>>> out1 \= np.array(\[0\], dtype\=np.float64)
\>>> out2 \= np.tanh(\[0.1\], out1)
\>>> out2 is out1
True

Copy to clipboard

\>>> \# Example of ValueError due to provision of shape mis-matched \`out\`
\>>> np.tanh(np.zeros((3,3)),np.zeros((2,2)))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operands could not be broadcast together with shapes (3,3) (2,2)

Copy to clipboard

Go BackOpen In Tab

On this page