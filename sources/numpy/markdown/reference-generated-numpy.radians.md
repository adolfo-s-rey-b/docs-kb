[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.radians.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.radians[#](https://numpy.org/doc/stable/reference/generated/numpy.radians.html#numpy-radians "Link to this heading")

===========================================================================================================================

numpy.radians(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'radians'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.radians.html#numpy.radians "Link to this definition")

Convert angles from degrees to radians.

Parameters:

**x**array\_like

Input array in degrees.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The corresponding radian values. This is a scalar if _x_ is a scalar.

See also

[`deg2rad`](https://numpy.org/doc/stable/reference/generated/numpy.deg2rad.html#numpy.deg2rad "numpy.deg2rad")

equivalent function

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Convert a degree array to radians

\>>> deg \= np.arange(12.) \* 30.
\>>> np.radians(deg)
array(\[ 0.        ,  0.52359878,  1.04719755,  1.57079633,  2.0943951 ,\
        2.61799388,  3.14159265,  3.66519143,  4.1887902 ,  4.71238898,\
        5.23598776,  5.75958653\])

Copy to clipboard

\>>> out \= np.zeros((deg.shape))
\>>> ret \= np.radians(deg, out)
\>>> ret is out
True

Copy to clipboard

Go BackOpen In Tab

On this page