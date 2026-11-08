[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndarray.tobytes[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy-ndarray-tobytes "Link to this heading")

===================================================================================================================================================

method

ndarray.tobytes(_order\='C'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes "Link to this definition")

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