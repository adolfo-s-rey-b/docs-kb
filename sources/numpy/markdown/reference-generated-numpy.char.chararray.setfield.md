[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.setfield.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.char.chararray.setfield.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.setfield.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.char.chararray.setfield.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.char.chararray.setfield.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.char.chararray.setfield.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.char.chararray.setfield.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.char.chararray.setfield.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.char.chararray.setfield.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.char.chararray.setfield.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.char.chararray.setfield.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.char.chararray.setfield.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.char.chararray.setfield.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.char.chararray.setfield.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.char.chararray.setfield.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.char.chararray.setfield.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.char.chararray.setfield.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.char.chararray.setfield.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.char.chararray.setfield.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.char.chararray.setfield.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.char.chararray.setfield.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.char.chararray.setfield.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.char.chararray.setfield[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.setfield.html#numpy-char-chararray-setfield "Link to this heading")

===========================================================================================================================================================================

method

char.chararray.setfield(_val_, _dtype_, _offset\=0_)[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.setfield.html#numpy.char.chararray.setfield "Link to this definition")

Put a value into a specified place in a field defined by a data-type.

Place _val_ into _a_’s field defined by [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 and beginning _offset_ bytes into the field.

Parameters:

**val**object

Value to be placed in field.

**dtype**dtype object

Data-type of the field in which to place _val_.

**offset**int, optional

The number of bytes into the field at which to place _val_.

Returns:

None

See also

[`getfield`](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.getfield.html#numpy.char.chararray.getfield "numpy.char.chararray.getfield")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.eye(3)
\>>> x.getfield(np.float64)
array(\[\[1.,  0.,  0.\],\
       \[0.,  1.,  0.\],\
       \[0.,  0.,  1.\]\])
\>>> x.setfield(3, np.int32)
\>>> x.getfield(np.int32)
array(\[\[3, 3, 3\],\
       \[3, 3, 3\],\
       \[3, 3, 3\]\], dtype=int32)
\>>> x
array(\[\[1.0e+000, 1.5e-323, 1.5e-323\],\
       \[1.5e-323, 1.0e+000, 1.5e-323\],\
       \[1.5e-323, 1.5e-323, 1.0e+000\]\])
\>>> x.setfield(np.eye(3), np.int32)
\>>> x
array(\[\[1.,  0.,  0.\],\
       \[0.,  1.,  0.\],\
       \[0.,  0.,  1.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page