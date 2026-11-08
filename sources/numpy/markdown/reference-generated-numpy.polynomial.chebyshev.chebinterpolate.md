[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebinterpolate[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html#numpy-polynomial-chebyshev-chebinterpolate "Link to this heading")

==================================================================================================================================================================================================================

polynomial.chebyshev.chebinterpolate(_func_, _deg_, _args\=()_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L1779-L1840)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebinterpolate.html#numpy.polynomial.chebyshev.chebinterpolate "Link to this definition")

Interpolate a function at the Chebyshev points of the first kind.

Returns the Chebyshev series that interpolates _func_ at the Chebyshev points of the first kind in the interval \[-1, 1\]. The interpolating series tends to a minmax approximation to _func_ with increasing _deg_ if the function is continuous in the interval.

Parameters:

**func**function

The function to be approximated. It must be a function of a single variable of the form `f(x, a, b, c...)`, where `a, b, c...` are extra arguments passed in the _args_ parameter.

**deg**int

Degree of the interpolating polynomial

**args**tuple, optional

Extra arguments to be used in the function call. Default is no extra arguments.

Returns:

**coef**ndarray, shape (deg + 1,)

Chebyshev coefficients of the interpolating series ordered from low to high.

Notes

The Chebyshev polynomials used in the interpolation are orthogonal when sampled at the Chebyshev points of the first kind. If it is desired to constrain some of the coefficients they can simply be set to the desired value after the interpolation, no new interpolation or fit is needed. This is especially useful if it is known apriori that some of coefficients are zero. For instance, if the function is even then the coefficients of the terms of odd degree in the result can be set to zero.

Examples

Try it in your browser!

\>>> import numpy.polynomial.chebyshev as C
\>>> C.chebinterpolate(lambda x: np.tanh(x) + 0.5, 8)
array(\[  5.00000000e-01,   8.11675684e-01,  -9.86864911e-17,\
        -5.42457905e-02,  -2.71387850e-16,   4.51658839e-03,\
         2.46716228e-17,  -3.79694221e-04,  -3.26899002e-16\])

Copy to clipboard

Go BackOpen In Tab

On this page