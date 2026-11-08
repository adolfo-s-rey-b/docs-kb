[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cross.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.cross.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cross.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.cross.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.cross.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.cross.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.cross.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.cross.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.cross.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.cross.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.cross.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.cross.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.cross.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.cross.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.cross.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.cross.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.cross.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.cross.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.cross.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.cross.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.cross.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.cross.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.cross[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cross.html#numpy-linalg-cross "Link to this heading")

==========================================================================================================================================

linalg.cross(_x1_, _x2_, _/_, _\*_, _axis\=\-1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L3246-L3308)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cross.html#numpy.linalg.cross "Link to this definition")

Returns the cross product of 3-element vectors.

If `x1` and/or `x2` are multi-dimensional arrays, then the cross-product of each pair of corresponding 3-element vectors is independently computed.

This function is Array API compatible, contrary to [`numpy.cross`](https://numpy.org/doc/stable/reference/generated/numpy.cross.html#numpy.cross "numpy.cross")
.

Parameters:

**x1**array\_like

The first input array.

**x2**array\_like

The second input array. Must be compatible with `x1` for all non-compute axes. The size of the axis over which to compute the cross-product must be the same size as the respective axis in `x1`.

**axis**int, optional

The axis (dimension) of `x1` and `x2` containing the vectors for which to compute the cross-product. Default: `-1`.

Returns:

**out**ndarray

An array containing the cross products.

See also

[`numpy.cross`](https://numpy.org/doc/stable/reference/generated/numpy.cross.html#numpy.cross "numpy.cross")

Examples

Try it in your browser!

Vector cross-product.

\>>> x \= np.array(\[1, 2, 3\])
\>>> y \= np.array(\[4, 5, 6\])
\>>> np.linalg.cross(x, y)
array(\[-3,  6, -3\])

Copy to clipboard

Multiple vector cross-products. Note that the direction of the cross product vector is defined by the _right-hand rule_.

\>>> x \= np.array(\[\[1,2,3\], \[4,5,6\]\])
\>>> y \= np.array(\[\[4,5,6\], \[1,2,3\]\])
\>>> np.linalg.cross(x, y)
array(\[\[-3,  6, -3\],\
       \[ 3, -6,  3\]\])

Copy to clipboard

\>>> x \= np.array(\[\[1, 2\], \[3, 4\], \[5, 6\]\])
\>>> y \= np.array(\[\[4, 5\], \[6, 1\], \[2, 3\]\])
\>>> np.linalg.cross(x, y, axis\=0)
array(\[\[-24,  6\],\
       \[ 18, 24\],\
       \[-6,  -18\]\])

Copy to clipboard

Go BackOpen In Tab

On this page