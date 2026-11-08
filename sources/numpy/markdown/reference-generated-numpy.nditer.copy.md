[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.nditer.copy.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.nditer.copy.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.nditer.copy.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.nditer.copy.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.nditer.copy.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.nditer.copy.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.nditer.copy.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.nditer.copy.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.nditer.copy.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.nditer.copy.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.nditer.copy.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.nditer.copy.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.nditer.copy.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.nditer.copy.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.nditer.copy.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.nditer.copy.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.nditer.copy.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.nditer.copy.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.nditer.copy.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.nditer.copy.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.nditer.copy.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.nditer.copy.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.nditer.copy[#](https://numpy.org/doc/stable/reference/generated/numpy.nditer.copy.html#numpy-nditer-copy "Link to this heading")

=======================================================================================================================================

method

nditer.copy()[#](https://numpy.org/doc/stable/reference/generated/numpy.nditer.copy.html#numpy.nditer.copy "Link to this definition")

Get a copy of the iterator in its current state.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(10)
\>>> y \= x + 1
\>>> it \= np.nditer(\[x, y\])
\>>> next(it)
(array(0), array(1))
\>>> it2 \= it.copy()
\>>> next(it2)
(array(1), array(2))

Copy to clipboard

Go BackOpen In Tab

On this page