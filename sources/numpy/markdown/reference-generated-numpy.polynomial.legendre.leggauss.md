[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggauss.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.legendre.leggauss.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggauss.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.legendre.leggauss.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.legendre.leggauss.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.legendre.leggauss.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.legendre.leggauss.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.legendre.leggauss.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.legendre.leggauss.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.legendre.leggauss[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggauss.html#numpy-polynomial-legendre-leggauss "Link to this heading")

==========================================================================================================================================================================================

polynomial.legendre.leggauss(_deg_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/legendre.py#L1522-L1584)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.legendre.leggauss.html#numpy.polynomial.legendre.leggauss "Link to this definition")

Gauss-Legendre quadrature.

Computes the sample points and weights for Gauss-Legendre quadrature. These sample points and weights will correctly integrate polynomials of degree \\(2\*deg - 1\\) or less over the interval \\(\[-1, 1\]\\) with the weight function \\(f(x) = 1\\).

Parameters:

**deg**int

Number of sample points and weights. It must be >= 1.

Returns:

**x**ndarray

1-D ndarray containing the sample points.

**y**ndarray

1-D ndarray containing the weights.

Notes

The results have only been tested up to degree 100, higher degrees may be problematic. The weights are determined by using the fact that

\\\[w\_k = c / (L'\_n(x\_k) \* L\_{n-1}(x\_k))\\\]

where \\(c\\) is a constant independent of \\(k\\) and \\(x\_k\\) is the k’th root of \\(L\_n\\), and then scaling the results to get the right value when integrating 1.

On this page