[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_xor.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.bitwise_xor.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_xor.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.bitwise_xor.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.bitwise_xor.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.bitwise_xor.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.bitwise_xor.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.bitwise_xor.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.bitwise_xor.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.bitwise_xor.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.bitwise_xor.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.bitwise_xor.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.bitwise_xor.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.bitwise_xor.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.bitwise_xor.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.bitwise_xor.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.bitwise_xor.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.bitwise_xor.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.bitwise_xor.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.bitwise_xor.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.bitwise_xor.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.bitwise_xor.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.bitwise\_xor[#](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_xor.html#numpy-bitwise-xor "Link to this heading")

========================================================================================================================================

numpy.bitwise\_xor(_x1_, _x2_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'bitwise\_xor'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_xor.html#numpy.bitwise_xor "Link to this definition")

Compute the bit-wise XOR of two arrays element-wise.

Computes the bit-wise XOR of the underlying binary representation of the integers in the input arrays. This ufunc implements the C/Python operator `^`.

Parameters:

**x1, x2**array\_like

Only integer and boolean types are handled. If `x1.shape != x2.shape`, they must be broadcastable to a common shape (which becomes the shape of the output).

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**out**ndarray or scalar

Result. This is a scalar if both _x1_ and _x2_ are scalars.

See also

[`logical_xor`](https://numpy.org/doc/stable/reference/generated/numpy.logical_xor.html#numpy.logical_xor "numpy.logical_xor")

[`bitwise_and`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_and.html#numpy.bitwise_and "numpy.bitwise_and")

[`bitwise_or`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_or.html#numpy.bitwise_or "numpy.bitwise_or")

[`binary_repr`](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#numpy.binary_repr "numpy.binary_repr")

Return the binary representation of the input number as a string.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

The number 13 is represented by `00001101`. Likewise, 17 is represented by `00010001`. The bit-wise XOR of 13 and 17 is therefore `00011100`, or 28:

\>>> np.bitwise\_xor(13, 17)
28
\>>> np.binary\_repr(28)
'11100'

Copy to clipboard

\>>> np.bitwise\_xor(31, 5)
26
\>>> np.bitwise\_xor(\[31,3\], 5)
array(\[26,  6\])

Copy to clipboard

\>>> np.bitwise\_xor(\[31,3\], \[5,6\])
array(\[26,  5\])
\>>> np.bitwise\_xor(\[True, True\], \[False, True\])
array(\[ True, False\])

Copy to clipboard

The `^` operator can be used as a shorthand for `np.bitwise_xor` on ndarrays.

\>>> x1 \= np.array(\[True, True\])
\>>> x2 \= np.array(\[False, True\])
\>>> x1 ^ x2
array(\[ True, False\])

Copy to clipboard

Go BackOpen In Tab

On this page