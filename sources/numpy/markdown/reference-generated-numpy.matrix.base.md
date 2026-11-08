[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.matrix.base.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.matrix.base[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.base.html#numpy-matrix-base "Link to this heading")

=======================================================================================================================================

attribute

matrix.base[#](https://numpy.org/doc/stable/reference/generated/numpy.matrix.base.html#numpy.matrix.base "Link to this definition")

Base object if memory is from some other object.

Examples

Try it in your browser!

The base of an array that owns its memory is None:

\>>> import numpy as np
\>>> x \= np.array(\[1,2,3,4\])
\>>> x.base is None
True

Copy to clipboard

Slicing creates a view, whose memory is shared with x:

\>>> y \= x\[2:\]
\>>> y.base is x
True

Copy to clipboard

Go BackOpen In Tab

On this page