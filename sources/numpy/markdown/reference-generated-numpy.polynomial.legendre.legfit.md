[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfit.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.legfit.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfit.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.legfit.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.legfit.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.legfit.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.legfit.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.legfit.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.legfit.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.legfit[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfit.html#numpy-polynomial-legendre-legfit "Link to this heading")

====================================================================================================================================================================================

polynomial.legendre.legfit(_x_, _y_, _deg_, _rcond\=None_, _full\=False_, _w\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L1296-L1420)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfit.html#numpy.polynomial.legendre.legfit "Link to this definition")

Least squares fit of Legendre series to data.

Return the coefficients of a Legendre series of degree _deg_ that is the least squares fit to the data values _y_ given at points _x_. If _y_ is 1-D the returned coefficients will also be 1-D. If _y_ is 2-D multiple fits are done, one for each column of _y_, and the resulting coefficients are stored in the corresponding columns of a 2-D return. The fitted polynomial(s) are in the form

\\\[p(x) = c\_0 + c\_1 \* L\_1(x) + ... + c\_n \* L\_n(x),\\\]

where _n_ is _deg_.

Parameters:

**x**array\_like, shape (M,)

x-coordinates of the M sample points `(x[i], y[i])`.

**y**array\_like, shape (M,) or (M, K)

y-coordinates of the sample points. Several data sets of sample points sharing the same x-coordinates can be fitted at once by passing in a 2D-array that contains one dataset per column.

**deg**int or 1-D array\_like

Degree(s) of the fitting polynomials. If _deg_ is a single integer all terms up to and including the _deg_’th term are included in the fit. For NumPy versions >= 1.11.0 a list of integers specifying the degrees of the terms to include may be used instead.

**rcond**float, optional

Relative condition number of the fit. Singular values smaller than this relative to the largest singular value will be ignored. The default value is len(x)\*eps, where eps is the relative precision of the float type, about 2e-16 in most cases.

**full**bool, optional

Switch determining nature of return value. When it is False (the default) just the coefficients are returned, when True diagnostic information from the singular value decomposition is also returned.

**w**array\_like, shape (_M_,), optional

Weights. If not None, the weight `w[i]` applies to the unsquared residual `y[i] - y_hat[i]` at `x[i]`. Ideally the weights are chosen so that the errors of the products `w[i]*y[i]` all have the same variance. When using inverse-variance weighting, use `w[i] = 1/sigma(y[i])`. The default value is None.

Returns:

**coef**ndarray, shape (M,) or (M, K)

Legendre coefficients ordered from low to high. If _y_ was 2-D, the coefficients for the data in column k of _y_ are in column _k_. If _deg_ is specified as a list, coefficients for terms not included in the fit are set equal to zero in the returned _coef_.

**\[residuals, rank, singular\_values, rcond\]**list

These values are only returned if `full == True`

*   residuals – sum of squared residuals of the least squares fit
    
*   rank – the numerical rank of the scaled Vandermonde matrix
    
*   singular\_values – singular values of the scaled Vandermonde matrix
    
*   rcond – value of _rcond_.
    

For more details, see [`numpy.linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")
.

Warns:

RankWarning

The rank of the coefficient matrix in the least-squares fit is deficient. The warning is only raised if `full == False`. The warnings can be turned off by

\>>> import warnings
\>>> warnings.simplefilter('ignore', np.exceptions.RankWarning)

Copy to clipboard

See also

[`numpy.polynomial.polynomial.polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfit.html#numpy.polynomial.polynomial.polyfit "numpy.polynomial.polynomial.polyfit")

[`numpy.polynomial.chebyshev.chebfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebfit.html#numpy.polynomial.chebyshev.chebfit "numpy.polynomial.chebyshev.chebfit")

[`numpy.polynomial.laguerre.lagfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagfit.html#numpy.polynomial.laguerre.lagfit "numpy.polynomial.laguerre.lagfit")

[`numpy.polynomial.hermite.hermfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermfit.html#numpy.polynomial.hermite.hermfit "numpy.polynomial.hermite.hermfit")

[`numpy.polynomial.hermite_e.hermefit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermefit.html#numpy.polynomial.hermite_e.hermefit "numpy.polynomial.hermite_e.hermefit")

[`legval`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legval.html#numpy.polynomial.legendre.legval "numpy.polynomial.legendre.legval")

Evaluates a Legendre series.

[`legvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legvander.html#numpy.polynomial.legendre.legvander "numpy.polynomial.legendre.legvander")

Vandermonde matrix of Legendre series.

[`legweight`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legweight.html#numpy.polynomial.legendre.legweight "numpy.polynomial.legendre.legweight")

Legendre weight function (= 1).

[`numpy.linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")

Computes a least-squares fit from the matrix.

[`scipy.interpolate.UnivariateSpline`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html#scipy.interpolate.UnivariateSpline "(in SciPy v1.18.0)")

Computes spline fits.

Notes

The solution is the coefficients of the Legendre series _p_ that minimizes the sum of the weighted squared errors

\\\[E = \\sum\_j w\_j^2 \* |y\_j - p(x\_j)|^2,\\\]

where \\(w\_j\\) are the weights. This problem is solved by setting up as the (typically) overdetermined matrix equation

\\\[V(x) \* c = w \* y,\\\]

where _V_ is the weighted pseudo Vandermonde matrix of _x_, _c_ are the coefficients to be solved for, _w_ are the weights, and _y_ are the observed values. This equation is then solved using the singular value decomposition of _V_.

If some of the singular values of _V_ are so small that they are neglected, then a [`RankWarning`](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.RankWarning.html#numpy.exceptions.RankWarning "numpy.exceptions.RankWarning")
 will be issued. This means that the coefficient values may be poorly determined. Using a lower order fit will usually get rid of the warning. The _rcond_ parameter can also be set to a value smaller than its default, but the resulting fit may be spurious and have large contributions from roundoff error.

Fits using Legendre series are usually better conditioned than fits using power series, but much can depend on the distribution of the sample points and the smoothness of the data. If the quality of the fit is inadequate splines may be a good alternative.

References

\[1\]

Wikipedia, “Curve fitting”, [https://en.wikipedia.org/wiki/Curve\_fitting](https://en.wikipedia.org/wiki/Curve_fitting)

On this page