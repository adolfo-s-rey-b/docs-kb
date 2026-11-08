[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.recarray.tobytes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.recarray.tobytes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.recarray.tobytes.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.recarray.tobytes.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.recarray.tobytes.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.recarray.tobytes.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.recarray.tobytes.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.recarray.tobytes.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.recarray.tobytes.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.recarray.tobytes.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.recarray.tobytes.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.recarray.tobytes.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.recarray.tobytes.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.recarray.tobytes.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.recarray.tobytes.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.recarray.tobytes.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.recarray.tobytes.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.recarray.tobytes.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.recarray.tobytes.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.recarray.tobytes.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.recarray.tobytes.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.recarray.tobytes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.recarray.tobytes[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.tobytes.html#numpy-recarray-tobytes "Link to this heading")

======================================================================================================================================================

method

recarray.tobytes(_order\='C'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.recarray.tobytes.html#numpy.recarray.tobytes "Link to this definition")

Construct Python bytes containing the raw data bytes in the array.

Constructs Python bytes showing a copy of the raw contents of data memory. The bytes object is produced in C-order by default. This behavior is controlled by the `order` parameter.

Parameters:

**order**{‘C’, ‘F’, ‘A’}, optional

Controls the memory layout of the bytes object. ‘C’ means C-order, ‘F’ means F-order, ‘A’ (short for _Any_) means ‘F’ if _a_ is Fortran contiguous, ‘C’ otherwise. Default is ‘C’.

Returns:

**s**bytes

Python bytes exhibiting a copy of _a_’s raw data.

See also

[`frombuffer`](https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html#numpy.frombuffer "numpy.frombuffer")

Inverse of this operation, construct a 1-dimensional array from Python bytes.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[\[0, 1\], \[2, 3\]\], dtype\='<u2')
\>>> x.tobytes()
b'\\x00\\x00\\x01\\x00\\x02\\x00\\x03\\x00'
\>>> x.tobytes('C') \== x.tobytes()
True
\>>> x.tobytes('F')
b'\\x00\\x00\\x02\\x00\\x01\\x00\\x03\\x00'

Copy to clipboard

Go BackOpen In Tab

On this page