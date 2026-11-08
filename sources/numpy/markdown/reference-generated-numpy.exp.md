[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.exp[#](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy-exp "Link to this heading")

===============================================================================================================

numpy.exp(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'exp'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.exp.html#numpy.exp "Link to this definition")

Calculate the exponential of all elements in the input array.

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

**out**ndarray or scalar

Output array, element-wise exponential of _x_. This is a scalar if _x_ is a scalar.

See also

[`expm1`](https://numpy.org/doc/stable/reference/generated/numpy.expm1.html#numpy.expm1 "numpy.expm1")

Calculate `exp(x) - 1` for all elements in the array.

[`exp2`](https://numpy.org/doc/stable/reference/generated/numpy.exp2.html#numpy.exp2 "numpy.exp2")

Calculate `2**x` for all elements in the array.

Notes

The irrational number `e` is also known as Euler’s number. It is approximately 2.718281, and is the base of the natural logarithm, `ln` (this means that, if \\(x = \\ln y = \\log\_e y\\), then \\(e^x = y\\). For real input, `exp(x)` is always positive.

For complex arguments, `x = a + ib`, we can write \\(e^x = e^a e^{ib}\\). The first term, \\(e^a\\), is already known (it is the real argument, described above). The second term, \\(e^{ib}\\), is \\(\\cos b + i \\sin b\\), a function with magnitude 1 and a periodic phase.

References

\[1\]

Wikipedia, “Exponential function”, [https://en.wikipedia.org/wiki/Exponential\_function](https://en.wikipedia.org/wiki/Exponential_function)

\[2\]

M. Abramovitz and I. A. Stegun, “Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables,” Dover, 1964, p. 69, [https://personal.math.ubc.ca/~cbm/aands/page\_69.htm](https://personal.math.ubc.ca/~cbm/aands/page_69.htm)

Examples

Try it in your browser!

Plot the magnitude and phase of `exp(x)` in the complex plane:

\>>> import numpy as np

Copy to clipboard

\>>> import matplotlib.pyplot as plt
\>>> import numpy as np

Copy to clipboard

\>>> x \= np.linspace(\-2\*np.pi, 2\*np.pi, 100)
\>>> xx \= x + 1j \* x\[:, np.newaxis\] \# a + ib over complex plane
\>>> out \= np.exp(xx)

Copy to clipboard

\>>> plt.subplot(121)
\>>> plt.imshow(np.abs(out),
...            extent\=\[\-2\*np.pi, 2\*np.pi, \-2\*np.pi, 2\*np.pi\], cmap\='gray')
\>>> plt.title('Magnitude of exp(x)')

Copy to clipboard

\>>> plt.subplot(122)
\>>> plt.imshow(np.angle(out),
...            extent\=\[\-2\*np.pi, 2\*np.pi, \-2\*np.pi, 2\*np.pi\], cmap\='hsv')
\>>> plt.title('Phase (angle) of exp(x)')
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-exp-1.png](https://numpy.org/doc/stable/_images/numpy-exp-1.png)

Go BackOpen In Tab

On this page