[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.outer.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ufunc.outer.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.outer.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ufunc.outer.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ufunc.outer.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ufunc.outer.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ufunc.outer.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ufunc.outer.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ufunc.outer.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ufunc.outer.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ufunc.outer.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ufunc.outer.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ufunc.outer.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ufunc.outer.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ufunc.outer.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ufunc.outer.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ufunc.outer.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ufunc.outer.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ufunc.outer.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ufunc.outer.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ufunc.outer.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ufunc.outer.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ufunc.outer[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.outer.html#numpy-ufunc-outer "Link to this heading")

=======================================================================================================================================

method

ufunc.outer(_A_, _B_, _/_, _\*\*kwargs_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.outer.html#numpy.ufunc.outer "Link to this definition")

Apply the ufunc _op_ to all pairs (a, b) with a in _A_ and b in _B_.

Let `M = A.ndim`, `N = B.ndim`. Then the result, _C_, of `op.outer(A, B)` is an array of dimension M + N such that:

\\\[C\[i\_0, ..., i\_{M-1}, j\_0, ..., j\_{N-1}\] = op(A\[i\_0, ..., i\_{M-1}\], B\[j\_0, ..., j\_{N-1}\])\\\]

For _A_ and _B_ one-dimensional, this is equivalent to:

r \= empty(len(A),len(B))
for i in range(len(A)):
    for j in range(len(B)):
        r\[i,j\] \= op(A\[i\], B\[j\])  \# op = ufunc in question

Copy to clipboard

Parameters:

**A**array\_like

First array

**B**array\_like

Second array

**kwargs**any

Arguments to pass on to the ufunc. Typically [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 or _out_. See [`ufunc`](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
 for a comprehensive overview of all available arguments.

Returns:

**r**ndarray

Output array

See also

[`numpy.outer`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer "numpy.outer")

A less powerful version of `np.multiply.outer` that [`ravel`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")
s all inputs to 1D. This exists primarily for compatibility with old code.

[`tensordot`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot "numpy.tensordot")

`np.tensordot(a, b, axes=((), ()))` and `np.multiply.outer(a, b)` behave same for all dimensions of a and b.

Examples

Try it in your browser!

\>>> np.multiply.outer(\[1, 2, 3\], \[4, 5, 6\])
array(\[\[ 4,  5,  6\],\
       \[ 8, 10, 12\],\
       \[12, 15, 18\]\])

Copy to clipboard

A multi-dimensional example:

\>>> A \= np.array(\[\[1, 2, 3\], \[4, 5, 6\]\])
\>>> A.shape
(2, 3)
\>>> B \= np.array(\[\[1, 2, 3, 4\]\])
\>>> B.shape
(1, 4)
\>>> C \= np.multiply.outer(A, B)
\>>> C.shape; C
(2, 3, 1, 4)
array(\[\[\[\[ 1,  2,  3,  4\]\],\
        \[\[ 2,  4,  6,  8\]\],\
        \[\[ 3,  6,  9, 12\]\]\],\
       \[\[\[ 4,  8, 12, 16\]\],\
        \[\[ 5, 10, 15, 20\]\],\
        \[\[ 6, 12, 18, 24\]\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page