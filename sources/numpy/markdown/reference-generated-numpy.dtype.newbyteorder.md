[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtype.newbyteorder.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dtype.newbyteorder.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dtype.newbyteorder.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dtype.newbyteorder.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dtype.newbyteorder.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dtype.newbyteorder.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dtype.newbyteorder.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dtype.newbyteorder.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dtype.newbyteorder.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dtype.newbyteorder.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dtype.newbyteorder.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dtype.newbyteorder.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dtype.newbyteorder.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dtype.newbyteorder.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dtype.newbyteorder.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dtype.newbyteorder.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dtype.newbyteorder.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dtype.newbyteorder.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dtype.newbyteorder.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dtype.newbyteorder.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dtype.newbyteorder.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dtype.newbyteorder.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtype.newbyteorder[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.newbyteorder.html#numpy-dtype-newbyteorder "Link to this heading")

============================================================================================================================================================

method

dtype.newbyteorder(_new\_order\='S'_, _/_)[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.newbyteorder.html#numpy.dtype.newbyteorder "Link to this definition")

Return a new dtype with a different byte order.

Changes are also made in all fields and sub-arrays of the data type.

Parameters:

**new\_order**string, optional

Byte order to force; a value from the byte order specifications below. The default value (‘S’) results in swapping the current byte order. _new\_order_ codes can be any of:

*   ‘S’ - swap dtype from current to opposite endian
    
*   {‘<’, ‘little’} - little endian
    
*   {‘>’, ‘big’} - big endian
    
*   {‘=’, ‘native’} - native order
    
*   {‘|’, ‘I’} - ignore (no change to byte order)
    

Returns:

**new\_dtype**dtype

New dtype object with the given change to the byte order.

Notes

Changes are also made in all fields and sub-arrays of the data type.

Examples

Try it in your browser!

\>>> import sys
\>>> sys\_is\_le \= sys.byteorder \== 'little'
\>>> native\_code \= '<' if sys\_is\_le else '>'
\>>> swapped\_code \= '>' if sys\_is\_le else '<'
\>>> import numpy as np
\>>> native\_dt \= np.dtype(native\_code+'i2')
\>>> swapped\_dt \= np.dtype(swapped\_code+'i2')
\>>> native\_dt.newbyteorder('S') \== swapped\_dt
True
\>>> native\_dt.newbyteorder() \== swapped\_dt
True
\>>> native\_dt \== swapped\_dt.newbyteorder('S')
True
\>>> native\_dt \== swapped\_dt.newbyteorder('=')
True
\>>> native\_dt \== swapped\_dt.newbyteorder('N')
True
\>>> native\_dt \== native\_dt.newbyteorder('|')
True
\>>> np.dtype('<i2') \== native\_dt.newbyteorder('<')
True
\>>> np.dtype('<i2') \== native\_dt.newbyteorder('L')
True
\>>> np.dtype('>i2') \== native\_dt.newbyteorder('>')
True
\>>> np.dtype('>i2') \== native\_dt.newbyteorder('B')
True

Copy to clipboard

Go BackOpen In Tab

On this page