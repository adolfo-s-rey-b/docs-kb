[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermpow.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.hermite.hermpow.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermpow.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.hermite.hermpow.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.hermite.hermpow.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.hermite.hermpow.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.hermite.hermpow.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.hermite.hermpow.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.hermite.hermpow.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.hermite.hermpow[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermpow.html#numpy-polynomial-hermite-hermpow "Link to this heading")

====================================================================================================================================================================================

polynomial.hermite.hermpow(_c_, _pow_, _maxpower\=16_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/hermite.py#L560-L594)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermpow.html#numpy.polynomial.hermite.hermpow "Link to this definition")

Raise a Hermite series to a power.

Returns the Hermite series _c_ raised to the power [`pow`](https://numpy.org/doc/stable/reference/generated/numpy.pow.html#numpy.pow "numpy.pow")
. The argument _c_ is a sequence of coefficients ordered from low to high. i.e., \[1,2,3\] is the series `P_0 + 2*P_1 + 3*P_2.`

Parameters:

**c**array\_like

1-D array of Hermite series coefficients ordered from low to high.

**pow**integer

Power to which the series will be raised

**maxpower**integer, optional

Maximum power allowed. This is mainly to limit growth of the series to unmanageable size. Default is 16

Returns:

**coef**ndarray

Hermite series of power.

See also

[`hermadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermadd.html#numpy.polynomial.hermite.hermadd "numpy.polynomial.hermite.hermadd")
, [`hermsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermsub.html#numpy.polynomial.hermite.hermsub "numpy.polynomial.hermite.hermsub")
, [`hermmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmulx.html#numpy.polynomial.hermite.hermmulx "numpy.polynomial.hermite.hermmulx")
, [`hermmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermmul.html#numpy.polynomial.hermite.hermmul "numpy.polynomial.hermite.hermmul")
, [`hermdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.hermite.hermdiv.html#numpy.polynomial.hermite.hermdiv "numpy.polynomial.hermite.hermdiv")

Examples

Try it in your browser!

\>>> from numpy.polynomial.hermite import hermpow
\>>> hermpow(\[1, 2, 3\], 2)
array(\[81.,  52.,  82.,  12.,   9.\])

Copy to clipboard

Go BackOpen In Tab

On this page