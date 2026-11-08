[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.vecdot.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.vecdot.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.vecdot.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.vecdot.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.vecdot.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.vecdot.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.vecdot.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.vecdot.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.vecdot.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.vecdot.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.vecdot.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.vecdot.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.vecdot.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.vecdot.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.vecdot.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.vecdot.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.vecdot.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.vecdot.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.vecdot.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.vecdot.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.vecdot.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.vecdot.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.vecdot[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.vecdot.html#numpy-linalg-vecdot "Link to this heading")

=============================================================================================================================================

linalg.vecdot(_x1_, _x2_, _/_, _\*_, _axis\=\-1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L3603-L3649)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.vecdot.html#numpy.linalg.vecdot "Link to this definition")

Computes the vector dot product.

This function is restricted to arguments compatible with the Array API, contrary to [`numpy.vecdot`](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#numpy.vecdot "numpy.vecdot")
.

Let be a vector in `x1` and \\mathbf{b} be a corresponding vector in `x2`. The dot product is defined as:

\\mathbf{a} \\cdot \\mathbf{b} = \\sum\_{i=0}^{n-1} \\overline{a\_i}b\_i

over the dimension specified by `axis` and where \\overline{a\_i} denotes the complex conjugate if a\_i is complex and the identity otherwise.

Parameters:

**x1**array\_like

First input array.

**x2**array\_like

Second input array.

**axis**int, optional

Axis over which to compute the dot product. Default: `-1`.

Returns:

**output**ndarray

The vector dot product of the input.

See also

[`numpy.vecdot`](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#numpy.vecdot "numpy.vecdot")

Examples

Try it in your browser!

Get the projected size along a given normal for an array of vectors.

\>>> v \= np.array(\[\[0., 5., 0.\], \[0., 0., 10.\], \[0., 6., 8.\]\])
\>>> n \= np.array(\[0., 0.6, 0.8\])
\>>> np.linalg.vecdot(v, n)
array(\[ 3.,  8., 10.\])

Copy to clipboard

Go BackOpen In Tab

On this page