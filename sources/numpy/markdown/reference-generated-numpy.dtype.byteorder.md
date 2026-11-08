[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtype.byteorder.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dtype.byteorder.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dtype.byteorder.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dtype.byteorder.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dtype.byteorder.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dtype.byteorder.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dtype.byteorder.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dtype.byteorder.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dtype.byteorder.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dtype.byteorder.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dtype.byteorder.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dtype.byteorder.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dtype.byteorder.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dtype.byteorder.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dtype.byteorder.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dtype.byteorder.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dtype.byteorder.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dtype.byteorder.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dtype.byteorder.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dtype.byteorder.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dtype.byteorder.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dtype.byteorder.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtype.byteorder[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.byteorder.html#numpy-dtype-byteorder "Link to this heading")

===================================================================================================================================================

attribute

dtype.byteorder[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.byteorder.html#numpy.dtype.byteorder "Link to this definition")

A character indicating the byte-order of this data-type object.

One of:

|     |     |
| --- | --- |
| ‘=’ | native |
| ‘<’ | little-endian |
| ‘>’ | big-endian |
| ‘\|’ | not applicable |

All built-in data-type objects have byteorder either ‘=’ or ‘|’.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> dt \= np.dtype(np.int16)
\>>> dt.byteorder
'='
\>>> \# endian is not relevant for 8 bit numbers
\>>> np.dtype(np.int8).byteorder
'|'
\>>> \# or ASCII strings
\>>> np.dtype('S2').byteorder
'|'
\>>> \# Even if specific code is given, and it is native
\>>> \# '=' is the byteorder
\>>> import sys
\>>> sys\_is\_le \= sys.byteorder \== 'little'
\>>> native\_code \= '<' if sys\_is\_le else '>'
\>>> swapped\_code \= '>' if sys\_is\_le else '<'
\>>> dt \= np.dtype(native\_code + 'i2')
\>>> dt.byteorder
'='
\>>> \# Swapped code shows up as itself
\>>> dt \= np.dtype(swapped\_code + 'i2')
\>>> dt.byteorder \== swapped\_code
True

Copy to clipboard

Go BackOpen In Tab

On this page