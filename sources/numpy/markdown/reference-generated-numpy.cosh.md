[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.cosh.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.cosh[#](https://numpy.org/doc/stable/reference/generated/numpy.cosh.html#numpy-cosh "Link to this heading")

==================================================================================================================

numpy.cosh(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'cosh'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.cosh.html#numpy.cosh "Link to this definition")

Hyperbolic cosine, element-wise.

Equivalent to `1/2 * (np.exp(x) + np.exp(-x))` and `np.cos(1j*x)`.

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

**out**ndarray or scalar

Output array of same shape as _x_. This is a scalar if _x_ is a scalar.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.cosh(0)
1.0

Copy to clipboard

The hyperbolic cosine describes the shape of a hanging cable:

\>>> import matplotlib.pyplot as plt
\>>> x \= np.linspace(\-4, 4, 1000)
\>>> plt.plot(x, np.cosh(x))
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-cosh-1.png](https://numpy.org/doc/stable/_images/numpy-cosh-1.png)

Go BackOpen In Tab

On this page