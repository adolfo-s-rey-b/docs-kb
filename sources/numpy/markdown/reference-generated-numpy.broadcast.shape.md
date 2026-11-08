[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.shape.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.broadcast.shape[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.shape.html#numpy-broadcast-shape "Link to this heading")

===================================================================================================================================================

attribute

broadcast.shape[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.shape.html#numpy.broadcast.shape "Link to this definition")

Shape of broadcasted result.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 3\])
\>>> y \= np.array(\[\[4\], \[5\], \[6\]\])
\>>> b \= np.broadcast(x, y)
\>>> b.shape
(3, 3)

Copy to clipboard

Go BackOpen In Tab

On this page