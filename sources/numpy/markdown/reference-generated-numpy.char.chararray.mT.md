[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.mT.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.char.chararray.mT[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.mT.html#numpy-char-chararray-mt "Link to this heading")

=========================================================================================================================================================

attribute

char.chararray.mT[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.mT.html#numpy.char.chararray.mT "Link to this definition")

View of the matrix transposed array.

The matrix transpose is the transpose of the last two dimensions, even if the array is of higher dimension.

New in version 2.0.

Raises:

ValueError

If the array is of dimension less than 2.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> a
array(\[\[1, 2\],\
       \[3, 4\]\])
\>>> a.mT
array(\[\[1, 3\],\
       \[2, 4\]\])

Copy to clipboard

\>>> a \= np.arange(8).reshape((2, 2, 2))
\>>> a
array(\[\[\[0, 1\],\
        \[2, 3\]\],\
\
       \[\[4, 5\],\
        \[6, 7\]\]\])
\>>> a.mT
array(\[\[\[0, 2\],\
        \[1, 3\]\],\
\
       \[\[4, 6\],\
        \[5, 7\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page