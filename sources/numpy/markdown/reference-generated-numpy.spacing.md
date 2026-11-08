[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.spacing.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.spacing.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.spacing.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.spacing.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.spacing.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.spacing.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.spacing.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.spacing.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.spacing.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.spacing.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.spacing.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.spacing.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.spacing.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.spacing.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.spacing.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.spacing.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.spacing.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.spacing.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.spacing.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.spacing.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.spacing.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.spacing.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.spacing[#](https://numpy.org/doc/stable/reference/generated/numpy.spacing.html#numpy-spacing "Link to this heading")

===========================================================================================================================

numpy.spacing(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'spacing'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.spacing.html#numpy.spacing "Link to this definition")

Return the distance between x and the nearest adjacent number.

Parameters:

**x**array\_like

Values to find the spacing of.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**out**ndarray or scalar

The spacing of values of _x_. This is a scalar if _x_ is a scalar.

Notes

It can be considered as a generalization of EPS: `spacing(np.float64(1)) == np.finfo(np.float64).eps`, and there should not be any representable number between `x + spacing(x)` and x for any finite x.

Spacing of +- inf and NaN is NaN.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.spacing(1) \== np.finfo(np.float64).eps
True

Copy to clipboard

Go BackOpen In Tab

On this page