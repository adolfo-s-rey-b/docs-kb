[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.cos[#](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy-cos "Link to this heading")

===============================================================================================================

numpy.cos(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'cos'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "Link to this definition")

Cosine element-wise.

Parameters:

**x**array\_like

Input array in radians.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The corresponding cosine values. This is a scalar if _x_ is a scalar.

Notes

If _out_ is provided, the function writes the result into it, and returns a reference to _out_. (See Examples)

References

M. Abramowitz and I. A. Stegun, Handbook of Mathematical Functions. New York, NY: Dover, 1972.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.cos(np.array(\[0, np.pi/2, np.pi\]))
array(\[  1.00000000e+00,   6.12303177e-17,  -1.00000000e+00\])
\>>>
\>>> \# Example of providing the optional output parameter
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