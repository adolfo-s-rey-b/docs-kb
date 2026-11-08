[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebpow.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.chebpow.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.chebpow.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebpow[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebpow.html#numpy-polynomial-chebyshev-chebpow "Link to this heading")

==========================================================================================================================================================================================

polynomial.chebyshev.chebpow(_c_, _pow_, _maxpower\=16_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L815-L870)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebpow.html#numpy.polynomial.chebyshev.chebpow "Link to this definition")

Raise a Chebyshev series to a power.

Returns the Chebyshev series _c_ raised to the power [`pow`](https://numpy.org/doc/stable/reference/generated/numpy.pow.html#numpy.pow "numpy.pow")
. The argument _c_ is a sequence of coefficients ordered from low to high. i.e., \[1,2,3\] is the series `T_0 + 2*T_1 + 3*T_2.`

Parameters:

**c**array\_like

1-D array of Chebyshev series coefficients ordered from low to high.

**pow**integer

Power to which the series will be raised

**maxpower**integer, optional

Maximum power allowed. This is mainly to limit growth of the series to unmanageable size. Default is 16

Returns:

**coef**ndarray

Chebyshev series of power.

See also

[`chebadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebadd.html#numpy.polynomial.chebyshev.chebadd "numpy.polynomial.chebyshev.chebadd")
, [`chebsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebsub.html#numpy.polynomial.chebyshev.chebsub "numpy.polynomial.chebyshev.chebsub")
, [`chebmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmulx.html#numpy.polynomial.chebyshev.chebmulx "numpy.polynomial.chebyshev.chebmulx")
, [`chebmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmul.html#numpy.polynomial.chebyshev.chebmul "numpy.polynomial.chebyshev.chebmul")
, [`chebdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebdiv.html#numpy.polynomial.chebyshev.chebdiv "numpy.polynomial.chebyshev.chebdiv")

Examples

Try it in your browser!

\>>> from numpy.polynomial import chebyshev as C
\>>> C.chebpow(\[1, 2, 3, 4\], 2)
array(\[15.5, 22. , 16. , ..., 12.5, 12. ,  8. \])

Copy to clipboard

Go BackOpen In Tab

On this page