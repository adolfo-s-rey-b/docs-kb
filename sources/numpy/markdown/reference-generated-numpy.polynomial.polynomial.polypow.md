[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polypow.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polypow.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polypow.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polypow.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polypow.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polypow.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polypow.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polypow.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polypow.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polypow[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polypow.html#numpy-polynomial-polynomial-polypow "Link to this heading")

=============================================================================================================================================================================================

polynomial.polynomial.polypow(_c_, _pow_, _maxpower\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L427-L463)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polypow.html#numpy.polynomial.polynomial.polypow "Link to this definition")

Raise a polynomial to a power.

Returns the polynomial _c_ raised to the power [`pow`](https://numpy.org/doc/stable/reference/generated/numpy.pow.html#numpy.pow "numpy.pow")
. The argument _c_ is a sequence of coefficients ordered from low to high. i.e., \[1,2,3\] is the series `1 + 2*x + 3*x**2.`

Parameters:

**c**array\_like

1-D array of array of series coefficients ordered from low to high degree.

**pow**integer

Power to which the series will be raised

**maxpower**integer, optional

Maximum power allowed. This is mainly to limit growth of the series to unmanageable size. Default is 16

Returns:

**coef**ndarray

Power series of power.

See also

[`polyadd`](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html#numpy.polyadd "numpy.polyadd")
, [`polysub`](https://numpy.org/doc/stable/reference/generated/numpy.polysub.html#numpy.polysub "numpy.polysub")
, [`polymulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polymulx.html#numpy.polynomial.polynomial.polymulx "numpy.polynomial.polynomial.polymulx")
, [`polymul`](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul")
, [`polydiv`](https://numpy.org/doc/stable/reference/generated/numpy.polydiv.html#numpy.polydiv "numpy.polydiv")

Examples

Try it in your browser!

\>>> from numpy.polynomial import polynomial as P
\>>> P.polypow(\[1, 2, 3\], 2)
array(\[ 1., 4., 10., 12., 9.\])

Copy to clipboard

Go BackOpen In Tab

On this page