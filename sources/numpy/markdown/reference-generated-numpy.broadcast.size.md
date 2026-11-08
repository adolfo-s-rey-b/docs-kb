[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.size.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.broadcast.size[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.size.html#numpy-broadcast-size "Link to this heading")

================================================================================================================================================

attribute

broadcast.size[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.size.html#numpy.broadcast.size "Link to this definition")

Total size of broadcasted result.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 3\])
\>>> y \= np.array(\[\[4\], \[5\], \[6\]\])
\>>> b \= np.broadcast(x, y)
\>>> b.size
9

Copy to clipboard

Go BackOpen In Tab

On this page