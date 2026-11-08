[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.linalg.lstsq.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.linalg.lstsq.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.linalg.lstsq.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.linalg.lstsq.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.lstsq.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.linalg.lstsq.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.linalg.lstsq.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.linalg.lstsq.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.linalg.lstsq.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.linalg.lstsq.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.linalg.lstsq.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.linalg.lstsq.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.linalg.lstsq.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.linalg.lstsq.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.linalg.lstsq.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.linalg.lstsq.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.linalg.lstsq.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.linalg.lstsq.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.linalg.lstsq.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.linalg.lstsq.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.linalg.lstsq[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy-linalg-lstsq "Link to this heading")

==========================================================================================================================================

linalg.lstsq(_a_, _b_, _rcond\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/linalg/_linalg.py#L2417-L2563)
[#](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "Link to this definition")

Return the least-squares solution to a linear matrix equation.

Computes the vector _x_ that approximately solves the equation `a @ x = b`. The equation may be under-, well-, or over-determined (i.e., the number of linearly independent rows of _a_ can be less than, equal to, or greater than its number of linearly independent columns). If _a_ is square and of full rank, then _x_ (but for round-off error) is the “exact” solution of the equation. Else, _x_ minimizes the Euclidean 2-norm \\(||b - ax||\\). If there are multiple minimizing solutions, the one with the smallest 2-norm \\(||x||\\) is returned.

Parameters:

**a**(M, N) array\_like

“Coefficient” matrix.

**b**{(M,), (M, K)} array\_like

Ordinate or “dependent variable” values. If _b_ is two-dimensional, the least-squares solution is calculated for each of the _K_ columns of _b_.

**rcond**float, optional

Cut-off ratio for small singular values of _a_. For the purposes of rank determination, singular values are treated as zero if they are smaller than _rcond_ times the largest singular value of _a_. The default uses the machine precision times `max(M, N)`. Passing `-1` will use machine precision.

Changed in version 2.0: Previously, the default was `-1`, but a warning was given that this would change.

Returns:

**x**{(N,), (N, K)} ndarray

Least-squares solution. If _b_ is two-dimensional, the solutions are in the _K_ columns of _x_.

**residuals**{(1,), (K,), (0,)} ndarray

Sums of squared residuals: Squared Euclidean 2-norm for each column in `b - a @ x`. If the rank of _a_ is < N or M <= N, this is an empty array. If _b_ is 1-dimensional, this is a (1,) shape array. Otherwise the shape is (K,).

**rank**int

Rank of matrix _a_.

**s**(min(M, N),) ndarray

Singular values of _a_.

Raises:

LinAlgError

If computation does not converge.

See also

[`scipy.linalg.lstsq`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lstsq.html#scipy.linalg.lstsq "(in SciPy v1.18.0)")

Similar function in SciPy.

Notes

If _b_ is a matrix, then all array results are returned as matrices.

Examples

Try it in your browser!

Fit a line, `y = mx + c`, through some noisy data-points:

\>>> import numpy as np
\>>> x \= np.array(\[0, 1, 2, 3\])
\>>> y \= np.array(\[\-1, 0.2, 0.9, 2.1\])

Copy to clipboard

By examining the coefficients, we see that the line should have a gradient of roughly 1 and cut the y-axis at, more or less, -1.

We can rewrite the line equation as `y = Ap`, where `A = [[x 1]]` and `p = [[m], [c]]`. Now use [`lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")
 to solve for _p_:

\>>> A \= np.vstack(\[x, np.ones(len(x))\]).T
\>>> A
array(\[\[ 0.,  1.\],\
       \[ 1.,  1.\],\
       \[ 2.,  1.\],\
       \[ 3.,  1.\]\])

Copy to clipboard

\>>> m, c \= np.linalg.lstsq(A, y)\[0\]
\>>> m, c
(1.0 -0.95) # may vary

Copy to clipboard

Plot the data along with the fitted line:

\>>> import matplotlib.pyplot as plt
\>>> \_ \= plt.plot(x, y, 'o', label\='Original data', markersize\=10)
\>>> \_ \= plt.plot(x, m\*x + c, 'r', label\='Fitted line')
\>>> \_ \= plt.legend()
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-linalg-lstsq-1.png](https://numpy.org/doc/stable/_images/numpy-linalg-lstsq-1.png)

Go BackOpen In Tab

On this page