[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.solve.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.solve.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.solve.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.solve.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.solve.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.solve.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.solve.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.solve.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.solve.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.solve.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.solve.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.solve.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.solve.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.solve.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.solve.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.solve.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.solve.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.solve.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.solve.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.solve.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.solve[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html#numpy-linalg-solve "Link to this heading")

==========================================================================================================================================

linalg.solve(_a_, _b_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L374-L465)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve "Link to this definition")

Solve a linear matrix equation, or system of linear scalar equations.

Computes the “exact” solution, _x_, of the well-determined, i.e., full rank, linear matrix equation _ax = b_.

Parameters:

**a**(…, M, M) array\_like

Coefficient matrix.

**b**{(M,), (…, M, K)}, array\_like

Ordinate or “dependent variable” values.

Returns:

**x**{(…, M,), (…, M, K)} ndarray

Solution to the system a x = b. Returned shape is (…, M) if b is shape (M,) and (…, M, K) if b is (…, M, K), where the “…” part is broadcasted between a and b.

Raises:

LinAlgError

If _a_ is singular or not square.

See also

[`scipy.linalg.solve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html#scipy.linalg.solve "(in SciPy v1.18.0)")

Similar function in SciPy.

Notes

Broadcasting rules apply, see the [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html#module-numpy.linalg "numpy.linalg")
 documentation for details.

The solutions are computed using LAPACK routine `_gesv`.

_a_ must be square and of full-rank, i.e., all rows (or, equivalently, columns) must be linearly independent; if either is not true, use [`lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")
 for the least-squares best “solution” of the system/equation.

Changed in version 2.0: The b array is only treated as a shape (M,) column vector if it is exactly 1-dimensional. In all other instances it is treated as a stack of (M, K) matrices. Previously b would be treated as a stack of (M,) vectors if b.ndim was equal to a.ndim - 1.

References

\[1\]

G. Strang, _Linear Algebra and Its Applications_, 2nd Ed., Orlando, FL, Academic Press, Inc., 1980, pg. 22.

Examples

Try it in your browser!

Solve the system of equations: `x0 + 2 * x1 = 1` and `3 * x0 + 5 * x1 = 2`:

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 5\]\])
\>>> b \= np.array(\[1, 2\])
\>>> x \= np.linalg.solve(a, b)
\>>> x
array(\[-1.,  1.\])

Copy to clipboard

Check that the solution is correct:

\>>> np.allclose(np.dot(a, x), b)
True

Copy to clipboard

Go BackOpen In Tab

On this page