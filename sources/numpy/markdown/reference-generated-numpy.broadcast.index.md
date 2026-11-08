[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.broadcast.index.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.index.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.broadcast.index.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.broadcast.index.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.broadcast.index.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.broadcast.index.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.broadcast.index.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.broadcast.index.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.broadcast.index.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.broadcast.index.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.broadcast.index.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.broadcast.index.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.broadcast.index.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.broadcast.index.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.broadcast.index.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.broadcast.index.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.broadcast.index.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.broadcast.index.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.broadcast.index.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.broadcast.index.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.broadcast.index.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.broadcast.index[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.index.html#numpy-broadcast-index "Link to this heading")

===================================================================================================================================================

attribute

broadcast.index[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.index.html#numpy.broadcast.index "Link to this definition")

current index in broadcasted result

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[\[1\], \[2\], \[3\]\])
\>>> y \= np.array(\[4, 5, 6\])
\>>> b \= np.broadcast(x, y)
\>>> b.index
0
\>>> next(b), next(b), next(b)
((1, 4), (1, 5), (1, 6))
\>>> b.index
3

Copy to clipboard

Go BackOpen In Tab

On this page