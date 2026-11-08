[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.T.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.char.chararray.T[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.T.html#numpy-char-chararray-t "Link to this heading")

======================================================================================================================================================

attribute

char.chararray.T[#](https://numpy.org/doc/stable/reference/generated/numpy.char.chararray.T.html#numpy.char.chararray.T "Link to this definition")

View of the transposed array.

Same as `self.transpose()`.

See also

[`transpose`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> a
array(\[\[1, 2\],\
       \[3, 4\]\])
\>>> a.T
array(\[\[1, 3\],\
       \[2, 4\]\])

Copy to clipboard

\>>> a \= np.array(\[1, 2, 3, 4\])
\>>> a
array(\[1, 2, 3, 4\])
\>>> a.T
array(\[1, 2, 3, 4\])

Copy to clipboard

Go BackOpen In Tab

On this page