[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfit.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polyfit.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polyfit.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polyfit[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfit.html#numpy-polynomial-polynomial-polyfit "Link to this heading")

=============================================================================================================================================================================================

polynomial.polynomial.polyfit(_x_, _y_, _deg_, _rcond\=None_, _full\=False_, _w\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L1348-L1499)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyfit.html#numpy.polynomial.polynomial.polyfit "Link to this definition")

Least-squares fit of a polynomial to data.

Return the coefficients of a polynomial of degree _deg_ that is the least squares fit to the data values _y_ given at points _x_. If _y_ is 1-D the returned coefficients will also be 1-D. If _y_ is 2-D multiple fits are done, one for each column of _y_, and the resulting coefficients are stored in the corresponding columns of a 2-D return. The fitted polynomial(s) are in the form

\\\[p(x) = c\_0 + c\_1 \* x + ... + c\_n \* x^n,\\\]

where _n_ is _deg_.

Parameters:

**x**array\_like, shape (_M_,)

x-coordinates of the _M_ sample (data) points `(x[i], y[i])`.

**y**array\_like, shape (_M_,) or (_M_, _K_)

y-coordinates of the sample points. Several sets of sample points sharing the same x-coordinates can be (independently) fit with one call to [`polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")
 by passing in for _y_ a 2-D array that contains one data set per column.

**deg**int or 1-D array\_like

Degree(s) of the fitting polynomials. If _deg_ is a single integer all terms up to and including the _deg_’th term are included in the fit. For NumPy versions >= 1.11.0 a list of integers specifying the degrees of the terms to include may be used instead.

**rcond**float, optional

Relative condition number of the fit. Singular values smaller than _rcond_, relative to the largest singular value, will be ignored. The default value is `len(x)*eps`, where _eps_ is the relative precision of the platform’s float type, about 2e-16 in most cases.

**full**bool, optional

Switch determining the nature of the return value. When `False` (the default) just the coefficients are returned; when `True`, diagnostic information from the singular value decomposition (used to solve the fit’s matrix equation) is also returned.

**w**array\_like, shape (_M_,), optional

Weights. If not None, the weight `w[i]` applies to the unsquared residual `y[i] - y_hat[i]` at `x[i]`. Ideally the weights are chosen so that the errors of the products `w[i]*y[i]` all have the same variance. When using inverse-variance weighting, use `w[i] = 1/sigma(y[i])`. The default value is None.

Returns:

**coef**ndarray, shape (_deg_ + 1,) or (_deg_ + 1, _K_)

Polynomial coefficients ordered from low to high. If _y_ was 2-D, the coefficients in column _k_ of _coef_ represent the polynomial fit to the data in _y_’s _k_\-th column.

**\[residuals, rank, singular\_values, rcond\]**list

These values are only returned if `full == True`

*   residuals – sum of squared residuals of the least squares fit
    
*   rank – the numerical rank of the scaled Vandermonde matrix
    
*   singular\_values – singular values of the scaled Vandermonde matrix
    
*   rcond – value of _rcond_.
    

For more details, see [`numpy.linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")
.

Raises:

RankWarning

Raised if the matrix in the least-squares fit is rank deficient. The warning is only raised if `full == False`. The warnings can be turned off by:

\>>> import warnings
\>>> warnings.simplefilter('ignore', np.exceptions.RankWarning)

Copy to clipboard

See also

[`numpy.polynomial.chebyshev.chebfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebfit.html#numpy.polynomial.chebyshev.chebfit "numpy.polynomial.chebyshev.chebfit")

[`numpy.polynomial.legendre.legfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.legfit.html#numpy.polynomial.legendre.legfit "numpy.polynomial.legendre.legfit")

[`numpy.polynomial.laguerre.lagfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.lagfit.html#numpy.polynomial.laguerre.lagfit "numpy.polynomial.laguerre.lagfit")

[`numpy.polynomial.hermite.hermfit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermfit.html#numpy.polynomial.hermite.hermfit "numpy.polynomial.hermite.hermfit")

[`numpy.polynomial.hermite_e.hermefit`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite_e.hermefit.html#numpy.polynomial.hermite_e.hermefit "numpy.polynomial.hermite_e.hermefit")

[`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")

Evaluates a polynomial.

[`polyvander`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyvander.html#numpy.polynomial.polynomial.polyvander "numpy.polynomial.polynomial.polyvander")

Vandermonde matrix for powers.

[`numpy.linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")

Computes a least-squares fit from the matrix.

[`scipy.interpolate.UnivariateSpline`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html#scipy.interpolate.UnivariateSpline "(in SciPy v1.18.0)")

Computes spline fits.

Notes

The solution is the coefficients of the polynomial _p_ that minimizes the sum of the weighted squared errors

\\\[E = \\sum\_j w\_j^2 \* |y\_j - p(x\_j)|^2,\\\]

where the \\(w\_j\\) are the weights. This problem is solved by setting up the (typically) over-determined matrix equation:

\\\[V(x) \* c = w \* y,\\\]

where _V_ is the weighted pseudo Vandermonde matrix of _x_, _c_ are the coefficients to be solved for, _w_ are the weights, and _y_ are the observed values. This equation is then solved using the singular value decomposition of _V_.

If some of the singular values of _V_ are so small that they are neglected (and [`full`](https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full "numpy.full")
 == `False`), a [`RankWarning`](https://numpy.org/doc/stable/reference/generated/numpy.exceptions.RankWarning.html#numpy.exceptions.RankWarning "numpy.exceptions.RankWarning")
 will be raised. This means that the coefficient values may be poorly determined. Fitting to a lower order polynomial will usually get rid of the warning (but may not be what you want, of course; if you have independent reason(s) for choosing the degree which isn’t working, you may have to: a) reconsider those reasons, and/or b) reconsider the quality of your data). The _rcond_ parameter can also be set to a value smaller than its default, but the resulting fit may be spurious and have large contributions from roundoff error.

Polynomial fits using double precision tend to “fail” at about (polynomial) degree 20. Fits using Chebyshev or Legendre series are generally better conditioned, but much can still depend on the distribution of the sample points and the smoothness of the data. If the quality of the fit is inadequate, splines may be a good alternative.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.polynomial import polynomial as P
\>>> x \= np.linspace(\-1,1,51)  \# x "data": \[-1, -0.96, ..., 0.96, 1\]
\>>> rng \= np.random.default\_rng()
\>>> err \= rng.normal(size\=len(x))
\>>> y \= x\*\*3 \- x + err  \# x^3 - x + Gaussian noise
\>>> c, stats \= P.polyfit(x,y,3,full\=True)
\>>> c \# c\[0\], c\[1\] approx. -1, c\[2\] should be approx. 0, c\[3\] approx. 1
array(\[ 0.23111996, -1.02785049, -0.2241444 ,  1.08405657\]) # may vary
\>>> stats \# note the large SSR, explaining the rather poor results
\[array(\[48.312088\]),                                        # may vary\
 4,\
 array(\[1.38446749, 1.32119158, 0.50443316, 0.28853036\]),\
 1.1324274851176597e-14\]

Copy to clipboard

Same thing without the added noise

\>>> y \= x\*\*3 \- x
\>>> c, stats \= P.polyfit(x,y,3,full\=True)
\>>> c \# c\[0\], c\[1\] ~= -1, c\[2\] should be "very close to 0", c\[3\] ~= 1
array(\[-6.73496154e-17, -1.00000000e+00,  0.00000000e+00,  1.00000000e+00\])
\>>> stats \# note the minuscule SSR
\[array(\[8.79579319e-31\]),\
 np.int32(4),\
 array(\[1.38446749, 1.32119158, 0.50443316, 0.28853036\]),\
 1.1324274851176597e-14\]

Copy to clipboard

Go BackOpen In Tab

On this page