[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.innerproduct.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.innerproduct.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.innerproduct.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.innerproduct.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.innerproduct.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.innerproduct.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.innerproduct.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.innerproduct.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.innerproduct.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.innerproduct.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.innerproduct.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.innerproduct.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.innerproduct.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.innerproduct.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.innerproduct.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.innerproduct.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.innerproduct.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.innerproduct.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.innerproduct.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.innerproduct.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.innerproduct.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.innerproduct.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.innerproduct[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.innerproduct.html#numpy-ma-innerproduct "Link to this heading")

===================================================================================================================================================

ma.innerproduct(_a_, _b_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8310-L8324)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.innerproduct.html#numpy.ma.innerproduct "Link to this definition")

Inner product of two arrays.

Ordinary inner product of vectors for 1-D arrays (without complex conjugation), in higher dimensions a sum product over the last axes.

Parameters:

**a, b**array\_like

If _a_ and _b_ are nonscalar, their last dimensions must match.

Returns:

**out**ndarray

If _a_ and _b_ are both scalars or both 1-D arrays then a scalar is returned; otherwise an array is returned. `out.shape = (*a.shape[:-1], *b.shape[:-1])`

Raises:

ValueError

If both _a_ and _b_ are nonscalar and their last dimensions have different sizes.

See also

[`tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "numpy.tensordot")

Sum products over arbitrary axes.

[`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")

Generalised matrix product, using second last dimension of _b_.

[`vecdot`](https://numpy.org/doc/stable/reference/generated/numpy.vecdot.html#numpy.vecdot "numpy.vecdot")

Vector dot product of two arrays.

[`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")

Einstein summation convention.

Notes

Masked values are replaced by 0.

For vectors (1-D arrays) it computes the ordinary inner-product:

np.inner(a, b) \= sum(a\[:\]\*b\[:\])

Copy to clipboard

More generally, if `ndim(a) = r > 0` and `ndim(b) = s > 0`:

np.inner(a, b) \= np.tensordot(a, b, axes\=(\-1,\-1))

Copy to clipboard

or explicitly:

np.inner(a, b)\[i0,...,ir\-2,j0,...,js\-2\]
     \= sum(a\[i0,...,ir\-2,:\]\*b\[j0,...,js\-2,:\])

Copy to clipboard

In addition _a_ or _b_ may be scalars, in which case:

np.inner(a,b) \= a\*b

Copy to clipboard

Examples

Try it in your browser!

Ordinary inner product for vectors:

\>>> import numpy as np
\>>> a \= np.array(\[1,2,3\])
\>>> b \= np.array(\[0,1,0\])
\>>> np.inner(a, b)
2

Copy to clipboard

Some multidimensional examples:

\>>> a \= np.arange(24).reshape((2,3,4))
\>>> b \= np.arange(4)
\>>> c \= np.inner(a, b)
\>>> c.shape
(2, 3)
\>>> c
array(\[\[ 14,  38,  62\],\
       \[ 86, 110, 134\]\])

Copy to clipboard

\>>> a \= np.arange(2).reshape((1,1,2))
\>>> b \= np.arange(6).reshape((3,2))
\>>> c \= np.inner(a, b)
\>>> c.shape
(1, 1, 3)
\>>> c
array(\[\[\[1, 3, 5\]\]\])

Copy to clipboard

An example where _b_ is a scalar:

\>>> np.inner(np.eye(2), 7)
array(\[\[7., 0.\],\
       \[0., 7.\]\])

Copy to clipboard

Go BackOpen In Tab

On this page