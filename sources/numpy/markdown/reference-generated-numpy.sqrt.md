[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.sqrt[#](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy-sqrt "Link to this heading")

==================================================================================================================

numpy.sqrt(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'sqrt'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.sqrt.html#numpy.sqrt "Link to this definition")

Return the non-negative square-root of an array, element-wise.

Parameters:

**x**array\_like

The values whose square-roots are required.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

An array of the same shape as _x_, containing the positive square-root of each element in _x_. If any element in _x_ is complex, a complex array is returned (and the square-roots of negative reals are calculated). If all of the elements in _x_ are real, so is _y_, with negative elements returning `nan`. If _out_ was provided, _y_ is a reference to it. This is a scalar if _x_ is a scalar.

See also

[`emath.sqrt`](https://numpy.org/doc/stable/reference/generated/numpy.emath.sqrt.html#numpy.emath.sqrt "numpy.emath.sqrt")

A version which returns complex numbers when given negative reals. Note that 0.0 and -0.0 are handled differently for complex inputs.

Notes

_sqrt_ has–consistent with common convention–as its branch cut the real “interval” \[_\-inf_, 0), and is continuous from above on it. A branch cut is a curve in the complex plane across which a given complex function fails to be continuous.\
\
Examples\
\
Try it in your browser!\
\
\>>> import numpy as np\
\>>> np.sqrt(\[1,4,9\])\
array(\[ 1.,  2.,  3.\])\
\
Copy to clipboard\
\
\>>> np.sqrt(\[4, \-1, \-3+4J\])\
array(\[ 2.+0.j,  0.+1.j,  1.+2.j\])\
\
Copy to clipboard\
\
\>>> np.sqrt(\[4, \-1, np.inf\])\
array(\[ 2., nan, inf\])\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page