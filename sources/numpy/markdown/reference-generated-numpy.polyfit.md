[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polyfit.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polyfit.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polyfit.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polyfit.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polyfit.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polyfit.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polyfit.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polyfit.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polyfit.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polyfit.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polyfit.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polyfit.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polyfit.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polyfit.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polyfit.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polyfit.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polyfit.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polyfit.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polyfit.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polyfit.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polyfit[#](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy-polyfit "Link to this heading")

===========================================================================================================================

numpy.polyfit(_x_, _y_, _deg_, _rcond\=None_, _full\=False_, _w\=None_, _cov\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L460-L706)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "Link to this definition")

Least squares polynomial fit.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

Fit a polynomial `p[0] * x**deg + ... + p[deg]` of degree _deg_ to points _(x, y)_. Returns a vector of coefficients _p_ that minimises the squared error in the order _deg_, _deg-1_, … _0_.

The [`Polynomial.fit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html#numpy.polynomial.polynomial.Polynomial.fit "numpy.polynomial.polynomial.Polynomial.fit")
 class method is recommended for new code as it is more stable numerically. See the documentation of the method for more information.

Parameters:

**x**array\_like, shape (M,)

x-coordinates of the M sample points `(x[i], y[i])`.

**y**array\_like, shape (M,) or (M, K)

y-coordinates of the sample points. Several data sets of sample points sharing the same x-coordinates can be fitted at once by passing in a 2D-array that contains one dataset per column.

**deg**int

Degree of the fitting polynomial

**rcond**float, optional

Relative condition number of the fit. Singular values smaller than this relative to the largest singular value will be ignored. The default value is len(x)\*eps, where eps is the relative precision of the float type, about 2e-16 in most cases.

**full**bool, optional

Switch determining nature of return value. When it is False (the default) just the coefficients are returned, when True diagnostic information from the singular value decomposition is also returned.

**w**array\_like, shape (M,), optional

Weights. If not None, the weight `w[i]` applies to the unsquared residual `y[i] - y_hat[i]` at `x[i]`. Ideally the weights are chosen so that the errors of the products `w[i]*y[i]` all have the same variance. When using inverse-variance weighting, use `w[i] = 1/sigma(y[i])`. The default value is None.

**cov**bool or str, optional

If given and not _False_, return not just the estimate but also its covariance matrix. By default, the covariance are scaled by chi2/dof, where dof = M - (deg + 1), i.e., the weights are presumed to be unreliable except in a relative sense and everything is scaled such that the reduced chi2 is unity. This scaling is omitted if `cov='unscaled'`, as is relevant for the case that the weights are w = 1/sigma, with sigma known to be a reliable estimate of the uncertainty.

Returns:

**p**ndarray, shape (deg + 1,) or (deg + 1, K)

Polynomial coefficients, highest power first. If _y_ was 2-D, the coefficients for _k_\-th data set are in `p[:,k]`.

residuals, rank, singular\_values, rcond

These values are only returned if `full == True`

*   residuals – sum of squared residuals of the least squares fit
    
*   rank – the effective rank of the scaled Vandermonde coefficient matrix
    
*   singular\_values – singular values of the scaled Vandermonde coefficient matrix
    
*   rcond – value of _rcond_.
    

For more details, see [`numpy.linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")
.

**V**ndarray, shape (deg + 1, deg + 1) or (deg + 1, deg + 1, K)

Present only if `full == False` and `cov == True`. The covariance matrix of the polynomial coefficient estimates. The diagonal of this matrix are the variance estimates for each coefficient. If y is a 2-D array, then the covariance matrix for the _k_\-th data set are in `V[:,:,k]`

Warns:

RankWarning

The rank of the coefficient matrix in the least-squares fit is deficient. The warning is only raised if `full == False`.

The warnings can be turned off by

\>>> import warnings
\>>> warnings.simplefilter('ignore', np.exceptions.RankWarning)

Copy to clipboard

See also

[`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")

Compute polynomial values.

[`linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")

Computes a least-squares fit.

[`scipy.interpolate.UnivariateSpline`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html#scipy.interpolate.UnivariateSpline "(in SciPy v1.18.0)")

Computes spline fits.

Notes

The solution minimizes the squared error

in the equations:

x\[0\]\*\*n \* p\[0\] + ... + x\[0\] \* p\[n\-1\] + p\[n\] \= y\[0\]
x\[1\]\*\*n \* p\[0\] + ... + x\[1\] \* p\[n\-1\] + p\[n\] \= y\[1\]
...
x\[k\]\*\*n \* p\[0\] + ... + x\[k\] \* p\[n\-1\] + p\[n\] \= y\[k\]

Copy to clipboard

The coefficient matrix of the coefficients _p_ is a Vandermonde matrix.

[`polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")
 issues a [`RankWarning`](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.RankWarning.html#numpy.exceptions.RankWarning "numpy.exceptions.RankWarning")
 when the least-squares fit is badly conditioned. This implies that the best fit is not well-defined due to numerical error. The results may be improved by lowering the polynomial degree or by replacing _x_ by _x_ - _x_.mean(). The _rcond_ parameter can also be set to a value smaller than its default, but the resulting fit may be spurious: including contributions from the small singular values can add numerical noise to the result.

Note that fitting polynomial coefficients is inherently badly conditioned when the degree of the polynomial is large or the interval of sample points is badly centered. The quality of the fit should always be checked in these cases. When polynomial fits are not satisfactory, splines may be a good alternative.

References

\[1\]

Wikipedia, “Curve fitting”, [https://en.wikipedia.org/wiki/Curve\_fitting](https://en.wikipedia.org/wiki/Curve_fitting)

\[2\]

Wikipedia, “Polynomial interpolation”, [https://en.wikipedia.org/wiki/Polynomial\_interpolation](https://en.wikipedia.org/wiki/Polynomial_interpolation)

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import warnings
\>>> x \= np.array(\[0.0, 1.0, 2.0, 3.0,  4.0,  5.0\])
\>>> y \= np.array(\[0.0, 0.8, 0.9, 0.1, \-0.8, \-1.0\])
\>>> z \= np.polyfit(x, y, 3)
\>>> z
array(\[ 0.08703704, -0.81349206,  1.69312169, -0.03968254\]) # may vary

Copy to clipboard

It is convenient to use [`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")
 objects for dealing with polynomials:

\>>> p \= np.poly1d(z)
\>>> p(0.5)
0.6143849206349179 # may vary
\>>> p(3.5)
\-0.34732142857143039 # may vary
\>>> p(10)
22.579365079365115 # may vary

Copy to clipboard

High-order polynomials may oscillate wildly:

\>>> with warnings.catch\_warnings():
...     warnings.simplefilter('ignore', np.exceptions.RankWarning)
...     p30 \= np.poly1d(np.polyfit(x, y, 30))
...
\>>> p30(4)
\-0.80000000000000204 # may vary
\>>> p30(5)
\-0.99999999999999445 # may vary
\>>> p30(4.5)
\-0.10547061179440398 # may vary

Copy to clipboard

Illustration:

\>>> import matplotlib.pyplot as plt
\>>> xp \= np.linspace(\-2, 6, 100)
\>>> \_ \= plt.plot(x, y, '.', xp, p(xp), '-', xp, p30(xp), '--')
\>>> plt.ylim(\-2,2)
(-2, 2)
\>>> plt.show()

Copy to clipboard

![../../_images/numpy-polyfit-1.png](https://numpy.org/doc/stable/_images/numpy-polyfit-1.png)

Go BackOpen In Tab

On this page