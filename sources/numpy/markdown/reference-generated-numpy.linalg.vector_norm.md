[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.vector_norm.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.vector_norm.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.vector_norm.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.vector_norm.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.vector_norm.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.vector_norm.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.vector_norm.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.vector_norm.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.vector_norm.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.vector_norm.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.vector_norm.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.vector_norm.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.vector_norm.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.vector_norm.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.vector_norm.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.vector_norm.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.vector_norm.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.vector_norm.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.vector_norm.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.vector_norm.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.vector_norm.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.vector_norm.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.vector\_norm[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.vector_norm.html#numpy-linalg-vector-norm "Link to this heading")

=============================================================================================================================================================

linalg.vector\_norm(_x_, _/_, _\*_, _axis\=None_, _keepdims\=False_, _ord\=2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L3501-L3595)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.vector_norm.html#numpy.linalg.vector_norm "Link to this definition")

Computes the vector norm of a vector (or batch of vectors) `x`.

This function is Array API compatible.

Parameters:

**x**array\_like

Input array.

**axis**{None, int, 2-tuple of ints}, optional

If an integer, `axis` specifies the axis (dimension) along which to compute vector norms. If an n-tuple, `axis` specifies the axes (dimensions) along which to compute batched vector norms. If `None`, the vector norm must be computed over all array values (i.e., equivalent to computing the vector norm of a flattened array). Default: `None`.

**keepdims**bool, optional

If this is set to True, the axes which are normed over are left in the result as dimensions with size one. Default: False.

**ord**{int, float, inf, -inf}, optional

The order of the norm. For details see the table under `Notes` in [`numpy.linalg.norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm "numpy.linalg.norm")
.

See also

[`numpy.linalg.norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm "numpy.linalg.norm")

Generic norm function

Examples

Try it in your browser!

\>>> from numpy import linalg as LA
\>>> a \= np.arange(9) + 1
\>>> a
array(\[1, 2, 3, 4, 5, 6, 7, 8, 9\])
\>>> b \= a.reshape((3, 3))
\>>> b
array(\[\[1, 2, 3\],\
       \[4, 5, 6\],\
       \[7, 8, 9\]\])

Copy to clipboard

\>>> LA.vector\_norm(b)
16.881943016134134
\>>> LA.vector\_norm(b, ord\=np.inf)
9.0
\>>> LA.vector\_norm(b, ord\=-np.inf)
1.0

Copy to clipboard

\>>> LA.vector\_norm(b, ord\=0)
9.0
\>>> LA.vector\_norm(b, ord\=1)
45.0
\>>> LA.vector\_norm(b, ord\=-1)
0.3534857623790153
\>>> LA.vector\_norm(b, ord\=2)
16.881943016134134
\>>> LA.vector\_norm(b, ord\=-2)
0.8058837395885292

Copy to clipboard

Go BackOpen In Tab

On this page