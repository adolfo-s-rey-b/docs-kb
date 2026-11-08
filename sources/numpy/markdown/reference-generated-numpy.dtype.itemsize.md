[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtype.itemsize.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtype.itemsize[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.itemsize.html#numpy-dtype-itemsize "Link to this heading")

================================================================================================================================================

attribute

dtype.itemsize[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.itemsize.html#numpy.dtype.itemsize "Link to this definition")

The element size of this data-type object.

For 18 of the 21 types this number is fixed by the data-type. For the flexible data-types, this number can be anything.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> arr.dtype
dtype('int64')
\>>> arr.itemsize
8

Copy to clipboard

\>>> dt \= np.dtype(\[('name', np.str\_, 16), ('grades', np.float64, (2,))\])
\>>> dt.itemsize
80

Copy to clipboard

Go BackOpen In Tab

On this page