[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.kron.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.kron.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.kron.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.kron.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.kron.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.kron.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.kron.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.kron.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.kron.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.kron.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.kron.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.kron.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.kron.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.kron.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.kron.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.kron.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.kron.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.kron.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.kron.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.kron.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.kron.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.kron.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.kron[#](https://numpy.org/doc/stable/reference/generated/numpy.kron.html#numpy-kron "Link to this heading")

==================================================================================================================

numpy.kron(_a_, _b_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L1038-L1150)
[#](https://numpy.org/doc/stable/reference/generated/numpy.kron.html#numpy.kron "Link to this definition")

Kronecker product of two arrays.

Computes the Kronecker product, a composite array made of blocks of the second array scaled by the first.

Parameters:

**a, b**array\_like

Returns:

**out**ndarray

See also

[`outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer")

The outer product

Notes

The function assumes that the number of dimensions of _a_ and _b_ are the same, if necessary prepending the smallest with ones. If `a.shape = (r0,r1,...,rN)` and `b.shape = (s0,s1,...,sN)`, the Kronecker product has shape `(r0*s0, r1*s1, ..., rN*SN)`. The elements are products of elements from _a_ and _b_, organized explicitly by:

kron(a,b)\[k0,k1,...,kN\] \= a\[i0,i1,...,iN\] \* b\[j0,j1,...,jN\]

Copy to clipboard

where:

kt \= it \* st + jt,  t \= 0,...,N

Copy to clipboard

In the common 2-D case (N=1), the block structure can be visualized:

\[\[ a\[0,0\]\*b,   a\[0,1\]\*b,  ... , a\[0,\-1\]\*b  \],\
 \[  ...                              ...   \],\
 \[ a\[\-1,0\]\*b,  a\[\-1,1\]\*b, ... , a\[\-1,\-1\]\*b \]\]

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.kron(\[1,10,100\], \[5,6,7\])
array(\[  5,   6,   7, ..., 500, 600, 700\])
\>>> np.kron(\[5,6,7\], \[1,10,100\])
array(\[  5,  50, 500, ...,   7,  70, 700\])

Copy to clipboard

\>>> np.kron(np.eye(2), np.ones((2,2)))
array(\[\[1.,  1.,  0.,  0.\],\
       \[1.,  1.,  0.,  0.\],\
       \[0.,  0.,  1.,  1.\],\
       \[0.,  0.,  1.,  1.\]\])

Copy to clipboard

\>>> a \= np.arange(100).reshape((2,5,2,5))
\>>> b \= np.arange(24).reshape((2,3,4))
\>>> c \= np.kron(a,b)
\>>> c.shape
(2, 10, 6, 20)
\>>> I \= (1,3,0,2)
\>>> J \= (0,2,1)
\>>> J1 \= (0,) + J             \# extend to ndim=4
\>>> S1 \= (1,) + b.shape
\>>> K \= tuple(np.array(I) \* np.array(S1) + np.array(J1))
\>>> c\[K\] \== a\[I\]\*b\[J\]
True

Copy to clipboard

Go BackOpen In Tab

On this page