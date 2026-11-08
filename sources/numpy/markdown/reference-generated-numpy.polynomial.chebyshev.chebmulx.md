[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmulx.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.chebmulx.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebmulx[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmulx.html#numpy-polynomial-chebyshev-chebmulx "Link to this heading")

=============================================================================================================================================================================================

polynomial.chebyshev.chebmulx(_c_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L654-L696)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmulx.html#numpy.polynomial.chebyshev.chebmulx "Link to this definition")

Multiply a Chebyshev series by x.

Multiply the polynomial _c_ by x, where x is the independent variable.

Parameters:

**c**array\_like

1-D array of Chebyshev series coefficients ordered from low to high.

Returns:

**out**ndarray

Array representing the result of the multiplication.

See also

[`chebadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebadd.html#numpy.polynomial.chebyshev.chebadd "numpy.polynomial.chebyshev.chebadd")
, [`chebsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebsub.html#numpy.polynomial.chebyshev.chebsub "numpy.polynomial.chebyshev.chebsub")
, [`chebmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmul.html#numpy.polynomial.chebyshev.chebmul "numpy.polynomial.chebyshev.chebmul")
, [`chebdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebdiv.html#numpy.polynomial.chebyshev.chebdiv "numpy.polynomial.chebyshev.chebdiv")
, [`chebpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebpow.html#numpy.polynomial.chebyshev.chebpow "numpy.polynomial.chebyshev.chebpow")

Examples

Try it in your browser!

\>>> from numpy.polynomial import chebyshev as C
\>>> C.chebmulx(\[1,2,3\])
array(\[1. , 2.5, 1. , 1.5\])

Copy to clipboard

Go BackOpen In Tab

On this page