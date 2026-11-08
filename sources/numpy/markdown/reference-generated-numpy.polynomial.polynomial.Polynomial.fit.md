[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.Polynomial.fit[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html#numpy-polynomial-polynomial-polynomial-fit "Link to this heading")

==================================================================================================================================================================================================================

method

_classmethod_ polynomial.polynomial.Polynomial.fit(_x_, _y_, _deg_, _domain\=None_, _rcond\=None_, _full\=False_, _w\=None_, _window\=None_, _symbol\='x'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/_polybase.py#L945-L1034)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.fit.html#numpy.polynomial.polynomial.Polynomial.fit "Link to this definition")

Least squares fit to data.

Return a series instance that is the least squares fit to the data _y_ sampled at _x_. The domain of the returned instance can be specified and this will often result in a superior fit with less chance of ill conditioning.

Parameters:

**x**array\_like, shape (M,)

x-coordinates of the M sample points `(x[i], y[i])`.

**y**array\_like, shape (M,)

y-coordinates of the M sample points `(x[i], y[i])`.

**deg**int or 1-D array\_like

Degree(s) of the fitting polynomials. If _deg_ is a single integer all terms up to and including the _deg_’th term are included in the fit. For NumPy versions >= 1.11.0 a list of integers specifying the degrees of the terms to include may be used instead.

**domain**{None, \[beg, end\], \[\]}, optional

Domain to use for the returned series. If `None`, then a minimal domain that covers the points _x_ is chosen. If `[]` the class domain is used. The default value was the class domain in NumPy 1.4 and `None` in later versions. The `[]` option was added in numpy 1.5.0.

**rcond**float, optional

Relative condition number of the fit. Singular values smaller than this relative to the largest singular value will be ignored. The default value is `len(x)*eps`, where eps is the relative precision of the float type, about 2e-16 in most cases.

**full**bool, optional

Switch determining nature of return value. When it is False (the default) just the coefficients are returned, when True diagnostic information from the singular value decomposition is also returned.

**w**array\_like, shape (M,), optional

Weights. If not None, the weight `w[i]` applies to the unsquared residual `y[i] - y_hat[i]` at `x[i]`. Ideally the weights are chosen so that the errors of the products `w[i]*y[i]` all have the same variance. When using inverse-variance weighting, use `w[i] = 1/sigma(y[i])`. The default value is None.

**window**{\[beg, end\]}, optional

Window to use for the returned series. The default value is the default class domain

**symbol**str, optional

Symbol representing the independent variable. Default is ‘x’.

Returns:

**new\_series**series

A series that represents the least squares fit to the data and has the domain and window specified in the call. If the coefficients for the unscaled and unshifted basis polynomials are of interest, do `new_series.convert().coef`.

**\[resid, rank, sv, rcond\]**list

These values are only returned if `full == True`

*   resid – sum of squared residuals of the least squares fit
    
*   rank – the numerical rank of the scaled Vandermonde matrix
    
*   sv – singular values of the scaled Vandermonde matrix
    
*   rcond – value of _rcond_.
    

For more details, see [`linalg.lstsq`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq "numpy.linalg.lstsq")
.

On this page