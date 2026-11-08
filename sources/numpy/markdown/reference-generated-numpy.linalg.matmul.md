[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matmul.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.matmul.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matmul.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.matmul.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.matmul.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.matmul.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.matmul.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.matmul.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.matmul.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.matmul.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.matmul.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.matmul.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.matmul.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.matmul.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.matmul.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.matmul.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.matmul.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.matmul.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.matmul.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.matmul.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.matmul.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.matmul.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.matmul[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matmul.html#numpy-linalg-matmul "Link to this heading")

=============================================================================================================================================

linalg.matmul(_x1_, _x2_, _/_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L3317-L3398)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matmul.html#numpy.linalg.matmul "Link to this definition")

Computes the matrix product.

This function is Array API compatible, contrary to [`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")
.

Parameters:

**x1**array\_like

The first input array.

**x2**array\_like

The second input array.

Returns:

**out**ndarray

The matrix product of the inputs. This is a scalar only when both `x1`, `x2` are 1-d vectors.

Raises:

ValueError

If the last dimension of `x1` is not the same size as the second-to-last dimension of `x2`.

If a scalar value is passed in.

See also

[`numpy.matmul`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul")

Examples

Try it in your browser!

For 2-D arrays it is the matrix product:

\>>> a \= np.array(\[\[1, 0\],\
...               \[0, 1\]\])
\>>> b \= np.array(\[\[4, 1\],\
...               \[2, 2\]\])
\>>> np.linalg.matmul(a, b)
array(\[\[4, 1\],\
       \[2, 2\]\])

Copy to clipboard

For 2-D mixed with 1-D, the result is the usual.

\>>> a \= np.array(\[\[1, 0\],\
...               \[0, 1\]\])
\>>> b \= np.array(\[1, 2\])
\>>> np.linalg.matmul(a, b)
array(\[1, 2\])
\>>> np.linalg.matmul(b, a)
array(\[1, 2\])

Copy to clipboard

Broadcasting is conventional for stacks of arrays

\>>> a \= np.arange(2 \* 2 \* 4).reshape((2, 2, 4))
\>>> b \= np.arange(2 \* 2 \* 4).reshape((2, 4, 2))
\>>> np.linalg.matmul(a,b).shape
(2, 2, 2)
\>>> np.linalg.matmul(a, b)\[0, 1, 1\]
98
\>>> sum(a\[0, 1, :\] \* b\[0 , :, 1\])
98

Copy to clipboard

Vector, vector returns the scalar inner product, but neither argument is complex-conjugated:

\>>> np.linalg.matmul(\[2j, 3j\], \[2j, 3j\])
(-13+0j)

Copy to clipboard

Scalar multiplication raises an error.

\>>> np.linalg.matmul(\[1,2\], 3)
Traceback (most recent call last):
...
ValueError: matmul: Input operand 1 does not have enough dimensions ...

Copy to clipboard

Go BackOpen In Tab

On this page