[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.coords.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.flatiter.coords.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.coords.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.flatiter.coords.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.flatiter.coords.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.flatiter.coords.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.flatiter.coords.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.flatiter.coords.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.flatiter.coords.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.flatiter.coords.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.flatiter.coords.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.flatiter.coords.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.flatiter.coords.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.flatiter.coords.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.flatiter.coords.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.flatiter.coords.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.flatiter.coords.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.flatiter.coords.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.flatiter.coords.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.flatiter.coords.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.flatiter.coords.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.flatiter.coords.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.flatiter.coords[#](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.coords.html#numpy-flatiter-coords "Link to this heading")

===================================================================================================================================================

attribute

flatiter.coords[#](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.coords.html#numpy.flatiter.coords "Link to this definition")

An N-dimensional tuple of current coordinates.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(6).reshape(2, 3)
\>>> fl \= x.flat
\>>> fl.coords
(0, 0)
\>>> next(fl)
0
\>>> fl.coords
(0, 1)

Copy to clipboard

Go BackOpen In Tab

On this page