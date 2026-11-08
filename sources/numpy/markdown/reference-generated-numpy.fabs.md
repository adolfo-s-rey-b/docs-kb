[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.fabs.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.fabs.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.fabs.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.fabs.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.fabs.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.fabs.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.fabs.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.fabs.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.fabs.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.fabs.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.fabs.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.fabs.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.fabs.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.fabs.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.fabs.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.fabs.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.fabs.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.fabs.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.fabs.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.fabs.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.fabs.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.fabs.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.fabs[#](https://numpy.org/doc/stable/reference/generated/numpy.fabs.html#numpy-fabs "Link to this heading")

==================================================================================================================

numpy.fabs(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'fabs'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.fabs.html#numpy.fabs "Link to this definition")

Compute the absolute values element-wise.

This function returns the absolute values (positive magnitude) of the data in _x_. Complex values are not handled, use [`absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html#numpy.absolute "numpy.absolute")
 to find the absolute values of complex data.

Parameters:

**x**array\_like

The array of numbers for which the absolute values are required. If _x_ is a scalar, the result _y_ will also be a scalar.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray or scalar

The absolute values of _x_, the returned values are always floats. This is a scalar if _x_ is a scalar.

See also

[`absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html#numpy.absolute "numpy.absolute")

Absolute values including _complex_ types.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.fabs(\-1)
1.0
\>>> np.fabs(\[\-1.2, 1.2\])
array(\[ 1.2,  1.2\])

Copy to clipboard

Go BackOpen In Tab

On this page