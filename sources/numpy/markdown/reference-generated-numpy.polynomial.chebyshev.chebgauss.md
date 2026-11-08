[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgauss.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebgauss[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgauss.html#numpy-polynomial-chebyshev-chebgauss "Link to this heading")

================================================================================================================================================================================================

polynomial.chebyshev.chebgauss(_deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L1843-L1882)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebgauss.html#numpy.polynomial.chebyshev.chebgauss "Link to this definition")

Gauss-Chebyshev quadrature.

Computes the sample points and weights for Gauss-Chebyshev quadrature. These sample points and weights will correctly integrate polynomials of degree \\(2\*deg - 1\\) or less over the interval \\(\[-1, 1\]\\) with the weight function \\(f(x) = 1/\\sqrt{1 - x^2}\\).

Parameters:

**deg**int

Number of sample points and weights. It must be >= 1.

Returns:

**x**ndarray

1-D ndarray containing the sample points.

**y**ndarray

1-D ndarray containing the weights.

Notes

The results have only been tested up to degree 100, higher degrees may be problematic. For Gauss-Chebyshev there are closed form solutions for the sample points and weights. If n = _deg_, then

\\\[x\_i = \\cos(\\pi (2 i - 1) / (2 n))\\\]

\\\[w\_i = \\pi / n\\\]

On this page