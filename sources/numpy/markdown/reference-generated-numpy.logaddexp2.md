[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp2.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.logaddexp2[#](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp2.html#numpy-logaddexp2 "Link to this heading")

====================================================================================================================================

numpy.logaddexp2(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'logaddexp2'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp2.html#numpy.logaddexp2 "Link to this definition")

Logarithm of the sum of exponentiations of the inputs in base-2.

Calculates `log2(2**x1 + 2**x2)`. This function is useful in machine learning when the calculated probabilities of events may be so small as to exceed the range of normal floating point numbers. In such cases the base-2 logarithm of the calculated probability can be used instead. This function allows adding probabilities stored in such a fashion.

Parameters:

**x1, x2**array\_like

Input values. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**result**ndarray

Base-2 logarithm of `2**x1 + 2**x2`. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`logaddexp`](https://numpy.org/doc/stable/reference/generated/numpy.logaddexp.html#numpy.logaddexp "numpy.logaddexp")

Logarithm of the sum of exponentiations of the inputs.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> prob1 \= np.log2(1e-50)
\>>> prob2 \= np.log2(2.5e-50)
\>>> prob12 \= np.logaddexp2(prob1, prob2)
\>>> prob1, prob2, prob12
(-166.09640474436813, -164.77447664948076, -164.28904982231052)
\>>> 2\*\*prob12
3.4999999999999914e-50

Copy to clipboard

Go BackOpen In Tab

On this page