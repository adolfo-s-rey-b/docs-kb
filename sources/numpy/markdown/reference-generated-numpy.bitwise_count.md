[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_count.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.bitwise\_count[#](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_count.html#numpy-bitwise-count "Link to this heading")

==============================================================================================================================================

numpy.bitwise\_count(_x_, _/_, _out=None_, _\*_, _where=True_, _casting='same\_kind'_, _order='K'_, _dtype=None_, _subok=True_\[, _signature_\]) _\= <ufunc 'bitwise\_count'>_[#](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_count.html#numpy.bitwise_count "Link to this definition")

Computes the number of 1-bits in the absolute value of `x`. Analogous to the builtin _int.bit\_count_ or `popcount` in C++.

Parameters:

**x**array\_like, unsigned int

Input array.

**out**ndarray, None, or tuple of ndarray and None, optional

A location into which the result is stored. If provided, it must have a shape that the inputs broadcast to. If not provided or None, a freshly-allocated array is returned. A tuple (possible only as a keyword argument) must have length equal to the number of outputs.

**where**array\_like, optional

This condition is broadcast over the input. At locations where the condition is True, the _out_ array will be set to the ufunc result. Elsewhere, the _out_ array will retain its original value. Note that if an uninitialized _out_ array is created via the default `out=None`, locations within it where the condition is False will remain uninitialized.

**\*\*kwargs**

For other keyword-only arguments, see the [ufunc docs](https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs)
.

Returns:

**y**ndarray

The corresponding number of 1-bits in the input. Returns uint8 for all integer types This is a scalar if _x_ is a scalar.

References

\[1\]

[https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetParallel](https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetParallel)

\[2\]

Wikipedia, “Hamming weight”, [https://en.wikipedia.org/wiki/Hamming\_weight](https://en.wikipedia.org/wiki/Hamming_weight)

\[3\]

[http://aggregate.ee.engr.uky.edu/MAGIC/#Population%20Count%20(Ones%20Count](http://aggregate.ee.engr.uky.edu/MAGIC/#Population%20Count%20(Ones%20Count)
)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.bitwise\_count(1023)
np.uint8(10)
\>>> a \= np.array(\[2\*\*i \- 1 for i in range(16)\])
\>>> np.bitwise\_count(a)
array(\[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15\],
      dtype=uint8)

Copy to clipboard

Go BackOpen In Tab

On this page