[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.atan2.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.atan2[#](https://numpy.org/doc/stable/reference/generated/numpy.atan2.html#numpy-atan2 "Link to this heading")

=====================================================================================================================

numpy.atan2(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'arctan2'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.atan2.html#numpy.atan2 "Link to this definition")

Element-wise arc tangent of `x1/x2` choosing the quadrant correctly.

The quadrant (i.e., branch) is chosen so that `arctan2(x1, x2)` is the signed angle in radians between the ray ending at the origin and passing through the point (1,0), and the ray ending at the origin and passing through the point (_x2_, _x1_). (Note the role reversal: the “_y_\-coordinate” is the first function parameter, the “_x_\-coordinate” is the second.) By IEEE convention, this function is defined for _x2_ = +/-0 and for either or both of _x1_ and _x2_ = +/-inf (see Notes for specific values).

This function is not defined for complex-valued arguments; for the so-called argument of complex values, use [`angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html#numpy.angle "numpy.angle")
.

Parameters:

**x1**array\_like, real-valued

_y_\-coordinates.

**x2**array\_like, real-valued

_x_\-coordinates. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**angle**ndarray

Array of angles in radians, in the range `[-pi, pi]`. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`arctan`](https://numpy.org/doc/stable/reference/generated/numpy.arctan.html#numpy.arctan "numpy.arctan")
, [`tan`](https://numpy.org/doc/stable/reference/generated/numpy.tan.html#numpy.tan "numpy.tan")
, [`angle`](https://numpy.org/doc/stable/reference/generated/numpy.angle.html#numpy.angle "numpy.angle")

Notes

_arctan2_ is identical to the [`atan2`](https://numpy.org/doc/stable/reference/generated/numpy.atan2.html#numpy.atan2 "numpy.atan2")
 function of the underlying C library. The following special values are defined in the C standard: [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.atan2.html#r20c8bad59052-1)

| _x1_ | _x2_ | _arctan2(x1,x2)_ |
| --- | --- | --- |
| +/- 0 | +0  | +/- 0 |
| +/- 0 | \-0 | +/- pi |
| \> 0 | +/-inf | +0 / +pi |
| < 0 | +/-inf | \-0 / -pi |
| +/-inf | +inf | +/- (pi/4) |
| +/-inf | \-inf | +/- (3\*pi/4) |

Note that +0 and -0 are distinct floating point numbers, as are +inf and -inf.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.atan2.html#id1)\
\]

ISO/IEC standard 9899:1999, “Programming language C.”

Examples

Try it in your browser!

Consider four points in different quadrants:

\>>> import numpy as np
\>>> x \= np.array(\[\-1, +1, +1, \-1\])
\>>> y \= np.array(\[\-1, \-1, +1, +1\])
\>>> np.arctan2(y, x) \* 180 / np.pi
array(\[-135.,  -45.,   45.,  135.\])

Copy to clipboard

Note the order of the parameters. [`arctan2`](https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html#numpy.arctan2 "numpy.arctan2")
 is defined also when _x2_ = 0 and at several other special points, obtaining values in the range `[-pi, pi]`:

\>>> np.arctan2(\[1., \-1.\], \[0., 0.\])
array(\[ 1.57079633, -1.57079633\])
\>>> np.arctan2(\[0., 0., np.inf\], \[+0., \-0., np.inf\])
array(\[0.        , 3.14159265, 0.78539816\])

Copy to clipboard

Go BackOpen In Tab

On this page