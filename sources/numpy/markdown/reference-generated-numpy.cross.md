[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.cross.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.cross.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.cross.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.cross.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.cross.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.cross.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.cross.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.cross.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.cross.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.cross.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.cross.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.cross.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.cross.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.cross.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.cross.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.cross.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.cross.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.cross.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.cross.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.cross.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.cross.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.cross.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.cross[#](https://numpy.org/doc/stable/reference/generated/numpy.cross.html#numpy-cross "Link to this heading")

=====================================================================================================================

numpy.cross(_a_, _b_, _axisa\=\-1_, _axisb\=\-1_, _axisc\=\-1_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L1562-L1719)
[#](https://numpy.org/doc/stable/reference/generated/numpy.cross.html#numpy.cross "Link to this definition")

Return the cross product of two (arrays of) vectors.

The cross product of _a_ and _b_ in \\(R^3\\) is a vector perpendicular to both _a_ and _b_. If _a_ and _b_ are arrays of vectors, the vectors are defined by the last axis of _a_ and _b_ by default, and these axes must have 3 dimensions.

Parameters:

**a**array\_like

Components of the first vector(s).

**b**array\_like

Components of the second vector(s).

**axisa**int, optional

Axis of _a_ that defines the vector(s). By default, the last axis.

**axisb**int, optional

Axis of _b_ that defines the vector(s). By default, the last axis.

**axisc**int, optional

Axis of _c_ containing the cross product vector(s). By default, the last axis.

**axis**int, optional

If defined, the axis of _a_, _b_ and _c_ that defines the vector(s) and cross product(s). Overrides _axisa_, _axisb_ and _axisc_.

Returns:

**c**ndarray

Vector cross product(s).

Raises:

ValueError

When the dimension of the vector(s) in _a_ or _b_ does not equal 3.

See also

[`inner`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner "numpy.inner")

Inner product

[`outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer")

Outer product.

[`linalg.cross`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cross.html#numpy.linalg.cross "numpy.linalg.cross")

An Array API compatible variation of `np.cross`.

[`ix_`](https://numpy.org/doc/stable/reference/generated/numpy.ix_.html#numpy.ix_ "numpy.ix_")

Construct index arrays.

Notes

Supports full broadcasting of the inputs.

Examples

Try it in your browser!

Vector cross-product.

\>>> import numpy as np
\>>> x \= \[1, 2, 3\]
\>>> y \= \[4, 5, 6\]
\>>> np.cross(x, y)
array(\[-3,  6, -3\])

Copy to clipboard

One vector with dimension 2.

\>>> x \= \[1, 2, 0\]
\>>> y \= \[4, 5, 6\]
\>>> np.cross(x, y)
array(\[12, -6, -3\])

Copy to clipboard

Both vectors with dimension 2.

\>>> x \= \[1, 2, 0\]
\>>> y \= \[4, 5, 0\]
\>>> np.cross(x, y)
array(\[0, 0, -3\])

Copy to clipboard

Multiple vector cross-products. Note that the direction of the cross product vector is defined by the _right-hand rule_.

\>>> x \= np.array(\[\[1,2,3\], \[4,5,6\]\])
\>>> y \= np.array(\[\[4,5,6\], \[1,2,3\]\])
\>>> np.cross(x, y)
array(\[\[-3,  6, -3\],\
       \[ 3, -6,  3\]\])

Copy to clipboard

The orientation of _c_ can be changed using the _axisc_ keyword.

\>>> np.cross(x, y, axisc\=0)
array(\[\[-3,  3\],\
       \[ 6, -6\],\
       \[-3,  3\]\])

Copy to clipboard

Change the vector definition of _x_ and _y_ using _axisa_ and _axisb_.

\>>> x \= np.array(\[\[1,2,3\], \[4,5,6\], \[7, 8, 9\]\])
\>>> y \= np.array(\[\[7, 8, 9\], \[4,5,6\], \[1,2,3\]\])
\>>> np.cross(x, y)
array(\[\[ -6,  12,  -6\],\
       \[  0,   0,   0\],\
       \[  6, -12,   6\]\])
\>>> np.cross(x, y, axisa\=0, axisb\=0)
array(\[\[-24,  48, -24\],\
       \[-30,  60, -30\],\
       \[-36,  72, -36\]\])

Copy to clipboard

Go BackOpen In Tab

On this page