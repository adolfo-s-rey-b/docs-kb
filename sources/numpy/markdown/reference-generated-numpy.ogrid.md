[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ogrid.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ogrid.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ogrid.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ogrid.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ogrid.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ogrid.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ogrid.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ogrid.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ogrid.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ogrid.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ogrid.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ogrid.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ogrid.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ogrid.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ogrid.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ogrid.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ogrid.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ogrid.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ogrid.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ogrid.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ogrid[#](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy-ogrid "Link to this heading")

=====================================================================================================================

numpy.ogrid _\= <numpy.lib.\_index\_tricks\_impl.OGridClass object>_[#](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "Link to this definition")

An instance which returns an open multi-dimensional “meshgrid”.

An instance which returns an open (i.e. not fleshed out) mesh-grid when indexed, so that only one dimension of each returned array is greater than 1. The dimension and number of the output arrays are equal to the number of indexing dimensions. If the step length is not a complex number, then the stop is not inclusive.

However, if the step length is a **complex number** (e.g. 5j), then the integer part of its magnitude is interpreted as specifying the number of points to create between the start and stop values, where the stop value **is inclusive**.

Returns:

**mesh-grid**ndarray or tuple of ndarrays

If the input is a single slice, returns an array. If the input is multiple slices, returns a tuple of arrays, with only one dimension not equal to 1.

See also

[`mgrid`](https://numpy.org/doc/stable/reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")

like [`ogrid`](https://numpy.org/doc/stable/reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid")
 but returns dense (or fleshed out) mesh grids

[`meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")

return coordinate matrices from coordinate vectors

[`r_`](https://numpy.org/doc/stable/reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")

array concatenator

[How to create arrays with regularly-spaced values](https://numpy.org/doc/stable/user/how-to-partition.html#how-to-partition)

Examples

Try it in your browser!

\>>> from numpy import ogrid
\>>> ogrid\[\-1:1:5j\]
array(\[-1. , -0.5,  0. ,  0.5,  1. \])
\>>> ogrid\[0:5, 0:5\]
(array(\[\[0\],\
        \[1\],\
        \[2\],\
        \[3\],\
        \[4\]\]),
 array(\[\[0, 1, 2, 3, 4\]\]))

Copy to clipboard

Go BackOpen In Tab

On this page