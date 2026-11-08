[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.sign.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.sign.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.sign.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.sign.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.sign.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.sign.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.sign.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.sign.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.sign.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.sign.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.sign.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.sign.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.sign.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.sign.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.sign.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.sign.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.sign.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.sign.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.sign.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.sign.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.sign.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.sign[#](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy-sign "Link to this heading")

==================================================================================================================

numpy.sign(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'sign'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy.sign "Link to this definition")

Returns an element-wise indication of the sign of a number.

The [`sign`](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy.sign "numpy.sign")
 function returns `-1 if x < 0, 0 if x==0, 1 if x > 0`. nan is returned for nan inputs.

For complex inputs, the [`sign`](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy.sign "numpy.sign")
 function returns `x / abs(x)`, the generalization of the above (and `0 if x==0`).

Changed in version 2.0.0: Definition of complex sign changed to follow the Array API standard.

Parameters:

**x**array\_like

Input values.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The sign of _x_. This is a scalar if _x_ is a scalar.

See also

[`signbit`](https://numpy.org/doc/stable/reference/generated/numpy.signbit.html#numpy.signbit "numpy.signbit")

[`copysign`](https://numpy.org/doc/stable/reference/generated/numpy.copysign.html#numpy.copysign "numpy.copysign")

Notes

There is more than one definition of sign in common use for complex numbers. The definition used here, \\(x/|x|\\), is the more common and useful one, but is different from the one used in numpy prior to version 2.0, \\(x/\\sqrt{x\*x}\\), which is equivalent to `sign(x.real) + 0j if x.real != 0 else sign(x.imag) + 0j`.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.sign(\[\-5., 4.5\])
array(\[-1.,  1.\])
\>>> np.sign(0)
0
\>>> np.sign(\[3\-4j, 8j\])
array(\[0.6-0.8j, 0. +1.j \])

Copy to clipboard

Go BackOpen In Tab

On this page