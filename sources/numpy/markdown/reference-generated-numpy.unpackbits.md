[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.unpackbits.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.unpackbits.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.unpackbits.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.unpackbits.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.unpackbits.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.unpackbits.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.unpackbits.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.unpackbits.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.unpackbits.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.unpackbits.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.unpackbits.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.unpackbits.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.unpackbits.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.unpackbits.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.unpackbits.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.unpackbits.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.unpackbits.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.unpackbits.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.unpackbits.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.unpackbits.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.unpackbits.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.unpackbits.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.unpackbits[#](https://numpy.org/doc/stable/reference/generated/numpy.unpackbits.html#numpy-unpackbits "Link to this heading")

====================================================================================================================================

numpy.unpackbits(_a_, _/_, _axis\=None_, _count\=None_, _bitorder\='big'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.unpackbits.html#numpy.unpackbits "Link to this definition")

Unpacks elements of a uint8 array into a binary-valued output array.

Each element of _a_ represents a bit-field that should be unpacked into a binary-valued output array. The shape of the output array is either 1-D (if _axis_ is `None`) or the same shape as the input array with unpacking done along the axis specified.

Parameters:

**a**ndarray, uint8 type

Input array.

**axis**int, optional

The dimension over which bit-unpacking is done. `None` implies unpacking the flattened array.

**count**int or None, optional

The number of elements to unpack along _axis_, provided as a way of undoing the effect of packing a size that is not a multiple of eight. A non-negative number means to only unpack _count_ bits. A negative number means to trim off that many bits from the end. `None` means to unpack the entire array (the default). Counts larger than the available number of bits will add zero padding to the output. Negative counts must not exceed the available number of bits.

**bitorder**{‘big’, ‘little’}, optional

The order of the returned bits. ‘big’ will mimic bin(val), `3 = 0b00000011 => [0, 0, 0, 0, 0, 0, 1, 1]`, ‘little’ will reverse the order to `[1, 1, 0, 0, 0, 0, 0, 0]`. Defaults to ‘big’.

Returns:

**unpacked**ndarray, uint8 type

The elements are binary-valued (0 or 1).

See also

[`packbits`](https://numpy.org/doc/stable/reference/generated/numpy.packbits.html#numpy.packbits "numpy.packbits")

Packs the elements of a binary-valued array into bits in a uint8 array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[2\], \[7\], \[23\]\], dtype\=np.uint8)
\>>> a
array(\[\[ 2\],\
       \[ 7\],\
       \[23\]\], dtype=uint8)
\>>> b \= np.unpackbits(a, axis\=1)
\>>> b
array(\[\[0, 0, 0, 0, 0, 0, 1, 0\],\
       \[0, 0, 0, 0, 0, 1, 1, 1\],\
       \[0, 0, 0, 1, 0, 1, 1, 1\]\], dtype=uint8)
\>>> c \= np.unpackbits(a, axis\=1, count\=-3)
\>>> c
array(\[\[0, 0, 0, 0, 0\],\
       \[0, 0, 0, 0, 0\],\
       \[0, 0, 0, 1, 0\]\], dtype=uint8)

Copy to clipboard

\>>> p \= np.packbits(b, axis\=0)
\>>> np.unpackbits(p, axis\=0)
array(\[\[0, 0, 0, 0, 0, 0, 1, 0\],\
       \[0, 0, 0, 0, 0, 1, 1, 1\],\
       \[0, 0, 0, 1, 0, 1, 1, 1\],\
       \[0, 0, 0, 0, 0, 0, 0, 0\],\
       \[0, 0, 0, 0, 0, 0, 0, 0\],\
       \[0, 0, 0, 0, 0, 0, 0, 0\],\
       \[0, 0, 0, 0, 0, 0, 0, 0\],\
       \[0, 0, 0, 0, 0, 0, 0, 0\]\], dtype=uint8)
\>>> np.array\_equal(b, np.unpackbits(p, axis\=0, count\=b.shape\[0\]))
True

Copy to clipboard

Go BackOpen In Tab

On this page