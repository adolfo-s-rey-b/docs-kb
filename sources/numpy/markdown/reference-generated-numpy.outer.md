[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.outer.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.outer.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.outer.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.outer.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.outer.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.outer.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.outer.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.outer.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.outer.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.outer.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.outer.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.outer.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.outer.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.outer.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.outer.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.outer.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.outer.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.outer.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.outer.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.outer.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.outer.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.outer[#](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy-outer "Link to this heading")

=====================================================================================================================

numpy.outer(_a_, _b_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numeric.py#L904-L989)
[#](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "Link to this definition")

Compute the outer product of two vectors.

Given two vectors _a_ and _b_ of length `M` and `N`, respectively, the outer product [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#r14e6c54b746b-1)
 is:

\[\[a\_0\*b\_0  a\_0\*b\_1 ... a\_0\*b\_{N\-1} \]\
 \[a\_1\*b\_0    .\
 \[ ...          .\
 \[a\_{M\-1}\*b\_0            a\_{M\-1}\*b\_{N\-1} \]\]\
\
Copy to clipboard\
\
Parameters:\
\
**a**(M,) array\_like\
\
First input vector. Input is flattened if not already 1-dimensional.\
\
**b**(N,) array\_like\
\
Second input vector. Input is flattened if not already 1-dimensional.\
\
**out**(M, N) ndarray, optional\
\
A location where the result is stored\
\
Returns:\
\
**out**(M, N) ndarray\
\
`out[i, j] = a[i] * b[j]`\
\
See also\
\
[`inner`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner "numpy.inner")\
\
[`einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum "numpy.einsum")\
\
`einsum('i,j->ij', a.ravel(), b.ravel())` is the equivalent.\
\
[`ufunc.outer`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.outer.html#numpy.ufunc.outer "numpy.ufunc.outer")\
\
A generalization to dimensions other than 1D and other operations. `np.multiply.outer(a.ravel(), b.ravel())` is the equivalent.\
\
[`linalg.outer`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.outer.html#numpy.linalg.outer "numpy.linalg.outer")\
\
An Array API compatible variation of `np.outer`, which accepts 1-dimensional inputs only.\
\
[`tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "numpy.tensordot")\
\
`np.tensordot(a.ravel(), b.ravel(), axes=((), ()))` is the equivalent.\
\
References\
\
\[[1](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#id1)\
\]\
\
G. H. Golub and C. F. Van Loan, _Matrix Computations_, 3rd ed., Baltimore, MD, Johns Hopkins University Press, 1996, pg. 8.\
\
Examples\
\
Try it in your browser!\
\
Make a (_very_ coarse) grid for computing a Mandelbrot set:\
\
\>>> import numpy as np\
\>>> rl \= np.outer(np.ones((5,)), np.linspace(\-2, 2, 5))\
\>>> rl\
array(\[\[-2., -1.,  0.,  1.,  2.\],\
       \[-2., -1.,  0.,  1.,  2.\],\
       \[-2., -1.,  0.,  1.,  2.\],\
       \[-2., -1.,  0.,  1.,  2.\],\
       \[-2., -1.,  0.,  1.,  2.\]\])\
\>>> im \= np.outer(1j\*np.linspace(2, \-2, 5), np.ones((5,)))\
\>>> im\
array(\[\[0.+2.j, 0.+2.j, 0.+2.j, 0.+2.j, 0.+2.j\],\
       \[0.+1.j, 0.+1.j, 0.+1.j, 0.+1.j, 0.+1.j\],\
       \[0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j\],\
       \[0.-1.j, 0.-1.j, 0.-1.j, 0.-1.j, 0.-1.j\],\
       \[0.-2.j, 0.-2.j, 0.-2.j, 0.-2.j, 0.-2.j\]\])\
\>>> grid \= rl + im\
\>>> grid\
array(\[\[-2.+2.j, -1.+2.j,  0.+2.j,  1.+2.j,  2.+2.j\],\
       \[-2.+1.j, -1.+1.j,  0.+1.j,  1.+1.j,  2.+1.j\],\
       \[-2.+0.j, -1.+0.j,  0.+0.j,  1.+0.j,  2.+0.j\],\
       \[-2.-1.j, -1.-1.j,  0.-1.j,  1.-1.j,  2.-1.j\],\
       \[-2.-2.j, -1.-2.j,  0.-2.j,  1.-2.j,  2.-2.j\]\])\
\
Copy to clipboard\
\
An example using a “vector” of letters:\
\
\>>> x \= np.array(\['a', 'b', 'c'\], dtype\=np.object\_)\
\>>> np.outer(x, \[1, 2, 3\])\
array(\[\['a', 'aa', 'aaa'\],\
       \['b', 'bb', 'bbb'\],\
       \['c', 'cc', 'ccc'\]\], dtype=object)\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page