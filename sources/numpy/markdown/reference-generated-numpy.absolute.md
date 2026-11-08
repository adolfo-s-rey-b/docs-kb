[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.absolute.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.absolute.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.absolute.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.absolute.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.absolute.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.absolute.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.absolute.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.absolute.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.absolute.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.absolute.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.absolute.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.absolute.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.absolute.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.absolute.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.absolute.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.absolute.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.absolute.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.absolute.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.absolute.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.absolute.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.absolute[#](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html#numpy-absolute "Link to this heading")

==============================================================================================================================

numpy.absolute(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'absolute'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html#numpy.absolute "Link to this definition")

Calculate the absolute value element-wise.

`np.abs` is a shorthand for this function.

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

**absolute**ndarray

An ndarray containing the absolute value of each element in _x_. For complex input, `a + ib`, the absolute value is \\(\\sqrt{ a^2 + b^2 }\\). This is a scalar if _x_ is a scalar.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[\-1.2, 1.2\])
\>>> np.absolute(x)
array(\[ 1.2,  1.2\])
\>>> np.absolute(1.2 + 1j)
1.5620499351813308

Copy to clipboard

Plot the function over `[-10, 10]`:

\>>> import matplotlib.pyplot as plt

Copy to clipboard

\>>> x \= np.linspace(start\=-10, stop\=10, num\=101)
\>>> plt.plot(x, np.absolute(x))
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-absolute-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-absolute-1_00_00.png)

Plot the function over the complex plane:

\>>> xx \= x + 1j \* x\[:, np.newaxis\]
\>>> plt.imshow(np.abs(xx), extent\=\[\-10, 10, \-10, 10\], cmap\='gray')
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-absolute-1_01_00.png](https://numpy.org/doc/stable/_images/numpy-absolute-1_01_00.png)

The [`abs`](https://docs.python.org/3/library/functions.html#abs "(in Python v3.14)")
 function can be used as a shorthand for `np.absolute` on ndarrays.

\>>> x \= np.array(\[\-1.2, 1.2\])
\>>> abs(x)
array(\[1.2, 1.2\])

Copy to clipboard

Go BackOpen In Tab

On this page