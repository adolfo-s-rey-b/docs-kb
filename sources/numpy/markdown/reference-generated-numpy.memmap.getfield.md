[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.memmap.getfield.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.memmap.getfield.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.memmap.getfield.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.memmap.getfield.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.memmap.getfield.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.memmap.getfield.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.memmap.getfield.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.memmap.getfield.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.memmap.getfield.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.memmap.getfield.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.memmap.getfield.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.memmap.getfield.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.memmap.getfield.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.memmap.getfield.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.memmap.getfield.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.memmap.getfield.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.memmap.getfield.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.memmap.getfield.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.memmap.getfield.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.memmap.getfield.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.memmap.getfield.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.memmap.getfield.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.memmap.getfield[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.getfield.html#numpy-memmap-getfield "Link to this heading")

===================================================================================================================================================

method

memmap.getfield(_dtype_, _offset\=0_)[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.getfield.html#numpy.memmap.getfield "Link to this definition")

Returns a field of the given array as a certain type.

A field is a view of the array data with a given data-type. The values in the view are determined by the given type and the offset into the current array in bytes. The offset needs to be such that the view dtype fits in the array dtype; for example an array of dtype complex128 has 16-byte elements. If taking a view with a 32-bit integer (4 bytes), the offset needs to be between 0 and 12 bytes.

Parameters:

**dtype**str or dtype

The data type of the view. The dtype size of the view can not be larger than that of the array itself.

**offset**int

Number of bytes to skip before beginning the element view.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.diag(\[1.+1.j\]\*2)
\>>> x\[1, 1\] \= 2 + 4.j
\>>> x
array(\[\[1.+1.j,  0.+0.j\],\
       \[0.+0.j,  2.+4.j\]\])
\>>> x.getfield(np.float64)
array(\[\[1.,  0.\],\
       \[0.,  2.\]\])

Copy to clipboard

By choosing an offset of 8 bytes we can select the complex part of the array for our view:

\>>> x.getfield(np.float64, offset\=8)
array(\[\[1.,  0.\],\
       \[0.,  4.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page