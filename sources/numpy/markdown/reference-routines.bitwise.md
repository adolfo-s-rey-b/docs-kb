[Skip to main content](https://numpy.org/doc/stable/reference/routines.bitwise.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.bitwise.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.bitwise.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.bitwise.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.bitwise.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.bitwise.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.bitwise.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.bitwise.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.bitwise.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.bitwise.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.bitwise.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.bitwise.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.bitwise.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.bitwise.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.bitwise.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.bitwise.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.bitwise.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.bitwise.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.bitwise.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.bitwise.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.bitwise.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.bitwise.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Bit-wise operations[#](https://numpy.org/doc/stable/reference/routines.bitwise.html#bit-wise-operations "Link to this heading")

================================================================================================================================

Elementwise bit operations[#](https://numpy.org/doc/stable/reference/routines.bitwise.html#elementwise-bit-operations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`bitwise_and`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_and.html#numpy.bitwise_and "numpy.bitwise_and")<br>(x1, x2, /\[, out, where, ...\]) | Compute the bit-wise AND of two arrays element-wise. |
| [`bitwise_or`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_or.html#numpy.bitwise_or "numpy.bitwise_or")<br>(x1, x2, /\[, out, where, casting, ...\]) | Compute the bit-wise OR of two arrays element-wise. |
| [`bitwise_xor`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_xor.html#numpy.bitwise_xor "numpy.bitwise_xor")<br>(x1, x2, /\[, out, where, ...\]) | Compute the bit-wise XOR of two arrays element-wise. |
| [`invert`](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#numpy.invert "numpy.invert")<br>(x, /\[, out, where, casting, order, ...\]) | Compute bit-wise inversion, or bit-wise NOT, element-wise. |
| [`bitwise_invert`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_invert.html#numpy.bitwise_invert "numpy.bitwise_invert")<br>(x, /\[, out, where, casting, ...\]) | Compute bit-wise inversion, or bit-wise NOT, element-wise. |
| [`left_shift`](https://numpy.org/doc/stable/reference/generated/numpy.left_shift.html#numpy.left_shift "numpy.left_shift")<br>(x1, x2, /\[, out, where, casting, ...\]) | Shift the bits of an integer to the left. |
| [`bitwise_left_shift`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_left_shift.html#numpy.bitwise_left_shift "numpy.bitwise_left_shift")<br>(x1, x2, /\[, out, where, ...\]) | Shift the bits of an integer to the left. |
| [`right_shift`](https://numpy.org/doc/stable/reference/generated/numpy.right_shift.html#numpy.right_shift "numpy.right_shift")<br>(x1, x2, /\[, out, where, ...\]) | Shift the bits of an integer to the right. |
| [`bitwise_right_shift`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_right_shift.html#numpy.bitwise_right_shift "numpy.bitwise_right_shift")<br>(x1, x2, /\[, out, where, ...\]) | Shift the bits of an integer to the right. |
| [`bitwise_count`](https://numpy.org/doc/stable/reference/generated/numpy.bitwise_count.html#numpy.bitwise_count "numpy.bitwise_count")<br>(x, /\[, out, where, casting, ...\]) | Computes the number of 1-bits in the absolute value of `x`. |

Bit packing[#](https://numpy.org/doc/stable/reference/routines.bitwise.html#bit-packing "Link to this heading")

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`packbits`](https://numpy.org/doc/stable/reference/generated/numpy.packbits.html#numpy.packbits "numpy.packbits")<br>(a, /\[, axis, bitorder\]) | Packs the elements of a binary-valued array into bits in a uint8 array. |
| [`unpackbits`](https://numpy.org/doc/stable/reference/generated/numpy.unpackbits.html#numpy.unpackbits "numpy.unpackbits")<br>(a, /\[, axis, count, bitorder\]) | Unpacks elements of a uint8 array into a binary-valued output array. |

Output formatting[#](https://numpy.org/doc/stable/reference/routines.bitwise.html#output-formatting "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`binary_repr`](https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html#numpy.binary_repr "numpy.binary_repr")<br>(num\[, width\]) | Return the binary representation of the input number as a string. |

On this page