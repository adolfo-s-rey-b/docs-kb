[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.packbits.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.packbits.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.packbits.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.packbits.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.packbits.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.packbits.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.packbits.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.packbits.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.packbits.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.packbits.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.packbits.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.packbits.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.packbits.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.packbits.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.packbits.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.packbits.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.packbits.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.packbits.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.packbits.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.packbits.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.packbits.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.packbits.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.packbits[#](https://numpy.org/doc/stable/reference/generated/numpy.packbits.html#numpy-packbits "Link to this heading")

==============================================================================================================================

numpy.packbits(_a_, _/_, _axis\=None_, _bitorder\='big'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.packbits.html#numpy.packbits "Link to this definition")

Packs the elements of a binary-valued array into bits in a uint8 array.

The result is padded to full bytes by inserting zero bits at the end.

Parameters:

**a**array\_like

An array of integers or booleans whose elements should be packed to bits.

**axis**int, optional

The dimension over which bit-packing is done. `None` implies packing the flattened array.

**bitorder**{‘big’, ‘little’}, optional

The order of the input bits. ‘big’ will mimic bin(val), `[0, 0, 0, 0, 0, 0, 1, 1] => 3 = 0b00000011`, ‘little’ will reverse the order so `[1, 1, 0, 0, 0, 0, 0, 0] => 3`. Defaults to ‘big’.

Returns:

**packed**ndarray

Array of type uint8 whose elements represent bits corresponding to the logical (0 or nonzero) value of the input elements. The shape of _packed_ has the same number of dimensions as the input (unless _axis_ is None, in which case the output is 1-D).

See also

[`unpackbits`](https://numpy.org/doc/stable/reference/generated/numpy.unpackbits.html#numpy.unpackbits "numpy.unpackbits")

Unpacks elements of a uint8 array into a binary-valued output array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[\[1,0,1\],\
...                \[0,1,0\]\],\
...               \[\[1,1,0\],\
...                \[0,0,1\]\]\])
\>>> b \= np.packbits(a, axis\=-1)
\>>> b
array(\[\[\[160\],\
        \[ 64\]\],\
       \[\[192\],\
        \[ 32\]\]\], dtype=uint8)

Copy to clipboard

Note that in binary 160 = 1010 0000, 64 = 0100 0000, 192 = 1100 0000, and 32 = 0010 0000.

Go BackOpen In Tab

On this page