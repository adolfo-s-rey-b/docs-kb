[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.mgrid.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.mgrid.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.mgrid.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.mgrid.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.mgrid.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.mgrid.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.mgrid.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.mgrid.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.mgrid.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.mgrid.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.mgrid.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.mgrid.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.mgrid.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.mgrid.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.mgrid.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.mgrid.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.mgrid.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.mgrid.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.mgrid.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.mgrid.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.mgrid[#](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy-mgrid "Link to this heading")

=====================================================================================================================

numpy.mgrid _\= <numpy.lib.\_index\_tricks\_impl.MGridClass object>_[#](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "Link to this definition")

An instance which returns a dense multi-dimensional “meshgrid”.

An instance which returns a dense (or fleshed out) mesh-grid when indexed, so that each returned argument has the same shape. The dimensions and number of the output arrays are equal to the number of indexing dimensions. If the step length is not a complex number, then the stop is not inclusive.

However, if the step length is a **complex number** (e.g. 5j), then the integer part of its magnitude is interpreted as specifying the number of points to create between the start and stop values, where the stop value **is inclusive**.

Returns:

**mesh-grid**ndarray

A single array, containing a set of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
s all of the same dimensions. stacked along the first axis.

See also

[`ogrid`](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid")

like [`mgrid`](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")
 but returns open (not fleshed out) mesh grids

[`meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")

return coordinate matrices from coordinate vectors

[`r_`](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")

array concatenator

[How to create arrays with regularly-spaced values](https://numpy.org/doc/stable/user/how-to-partition.html#how-to-partition)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.mgrid\[0:5, 0:5\]
array(\[\[\[0, 0, 0, 0, 0\],\
        \[1, 1, 1, 1, 1\],\
        \[2, 2, 2, 2, 2\],\
        \[3, 3, 3, 3, 3\],\
        \[4, 4, 4, 4, 4\]\],\
       \[\[0, 1, 2, 3, 4\],\
        \[0, 1, 2, 3, 4\],\
        \[0, 1, 2, 3, 4\],\
        \[0, 1, 2, 3, 4\],\
        \[0, 1, 2, 3, 4\]\]\])
\>>> np.mgrid\[\-1:1:5j\]
array(\[-1. , -0.5,  0. ,  0.5,  1. \])

Copy to clipboard

\>>> np.mgrid\[0:4\].shape
(4,)
\>>> np.mgrid\[0:4, 0:5\].shape
(2, 4, 5)
\>>> np.mgrid\[0:4, 0:5, 0:6\].shape
(3, 4, 5, 6)

Copy to clipboard

Go BackOpen In Tab

On this page