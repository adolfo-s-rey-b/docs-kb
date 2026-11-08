[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.power.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.power.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.power.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.power.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.power.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.power.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.power.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.power.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.power.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.power.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.power.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.power.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.power.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.power.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.power.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.power.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.power.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.power.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.power.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.power.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.power.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.power.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.power[#](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy-power "Link to this heading")

=====================================================================================================================

numpy.power(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'power'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.power.html#numpy.power "Link to this definition")

First array elements raised to powers from second array, element-wise.

Raise each base in _x1_ to the positionally-corresponding power in _x2_. _x1_ and _x2_ must be broadcastable to the same shape.

An integer type raised to a negative integer power will raise a `ValueError`.

Negative values raised to a non-integral value will return `nan`. To get complex results, cast the input to complex, or specify the `dtype` to be `complex` (see the example below).

Parameters:

**x1**array\_like

The bases.

**x2**array\_like

The exponents. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The bases in _x1_ raised to the exponents in _x2_. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`float_power`](https://numpy.org/doc/stable/reference/generated/numpy.float_power.html#numpy.float_power "numpy.float_power")

power function that promotes integers to float

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Cube each element in an array.

\>>> x1 \= np.arange(6)
\>>> x1
\[0, 1, 2, 3, 4, 5\]
\>>> np.power(x1, 3)
array(\[  0,   1,   8,  27,  64, 125\])

Copy to clipboard

Raise the bases to different exponents.

\>>> x2 \= \[1.0, 2.0, 3.0, 3.0, 2.0, 1.0\]
\>>> np.power(x1, x2)
array(\[  0.,   1.,   8.,  27.,  16.,   5.\])

Copy to clipboard

The effect of broadcasting.

\>>> x2 \= np.array(\[\[1, 2, 3, 3, 2, 1\], \[1, 2, 3, 3, 2, 1\]\])
\>>> x2
array(\[\[1, 2, 3, 3, 2, 1\],\
       \[1, 2, 3, 3, 2, 1\]\])
\>>> np.power(x1, x2)
array(\[\[ 0,  1,  8, 27, 16,  5\],\
       \[ 0,  1,  8, 27, 16,  5\]\])

Copy to clipboard

The `**` operator can be used as a shorthand for `np.power` on ndarrays.

\>>> x2 \= np.array(\[1, 2, 3, 3, 2, 1\])
\>>> x1 \= np.arange(6)
\>>> x1 \*\* x2
array(\[ 0,  1,  8, 27, 16,  5\])

Copy to clipboard

Negative values raised to a non-integral value will result in `nan` (and a warning will be generated).

\>>> x3 \= np.array(\[\-1.0, \-4.0\])
\>>> with np.errstate(invalid\='ignore'):
...     p \= np.power(x3, 1.5)
...
\>>> p
array(\[nan, nan\])

Copy to clipboard

To get complex results, give the argument `dtype=np.complex128`.

\>>> np.power(x3, 1.5, dtype\=np.complex128)
array(\[-1.83697020e-16-1.j, -1.46957616e-15-8.j\])

Copy to clipboard

Go BackOpen In Tab

On this page