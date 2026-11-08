[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.laggauss.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.laguerre.laggauss.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.laguerre.laggauss.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.laguerre.laggauss[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.laggauss.html#numpy-polynomial-laguerre-laggauss "Link to this heading")

==========================================================================================================================================================================================

polynomial.laguerre.laggauss(_deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/laguerre.py#L1587-L1651)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.laguerre.laggauss.html#numpy.polynomial.laguerre.laggauss "Link to this definition")

Gauss-Laguerre quadrature.

Computes the sample points and weights for Gauss-Laguerre quadrature. These sample points and weights will correctly integrate polynomials of degree or less over the interval \[0, \\inf\] with the weight function f(x) = \\exp(-x).

Parameters:

**deg**int

Number of sample points and weights. It must be >= 1.

Returns:

**x**ndarray

1-D ndarray containing the sample points.

**y**ndarray

1-D ndarray containing the weights.

Notes

The results have only been tested up to degree 100 higher degrees may be problematic. The weights are determined by using the fact that

w\_k = c / (L'\_n(x\_k) \* L\_{n-1}(x\_k))

where c is a constant independent of k and x\_k is the k’th root of L\_n, and then scaling the results to get the right value when integrating 1.

Examples

Try it in your browser!

\>>> from numpy.polynomial.laguerre import laggauss
\>>> laggauss(2)
(array(\[0.58578644, 3.41421356\]), array(\[0.85355339, 0.14644661\]))

Copy to clipboard

Go BackOpen In Tab

On this page