[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.iters.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.broadcast.iters[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.iters.html#numpy-broadcast-iters "Link to this heading")

===================================================================================================================================================

attribute

broadcast.iters[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.iters.html#numpy.broadcast.iters "Link to this definition")

tuple of iterators along `self`’s “components.”

Returns a tuple of [`numpy.flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
 objects, one for each “component” of `self`.

See also

[`numpy.flatiter`](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 3\])
\>>> y \= np.array(\[\[4\], \[5\], \[6\]\])
\>>> b \= np.broadcast(x, y)
\>>> row, col \= b.iters
\>>> next(row), next(col)
(1, 4)

Copy to clipboard

Go BackOpen In Tab

On this page