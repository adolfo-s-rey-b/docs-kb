[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polydiv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polynomial.polydiv.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polynomial.polydiv.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polynomial.polydiv[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polydiv.html#numpy-polynomial-polynomial-polydiv "Link to this heading")

=============================================================================================================================================================================================

polynomial.polynomial.polydiv(_c1_, _c2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polynomial.py#L369-L424)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polydiv.html#numpy.polynomial.polynomial.polydiv "Link to this definition")

Divide one polynomial by another.

Returns the quotient-with-remainder of two polynomials _c1_ / _c2_. The arguments are sequences of coefficients, from lowest order term to highest, e.g., \[1,2,3\] represents `1 + 2*x + 3*x**2`.

Parameters:

**c1, c2**array\_like

1-D arrays of polynomial coefficients ordered from low to high.

Returns:

**\[quo, rem\]**ndarrays

Of coefficient series representing the quotient and remainder.

See also

[`polyadd`](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html#numpy.polyadd "numpy.polyadd")
, [`polysub`](https://numpy.org/doc/stable/reference/generated/numpy.polysub.html#numpy.polysub "numpy.polysub")
, [`polymulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polymulx.html#numpy.polynomial.polynomial.polymulx "numpy.polynomial.polynomial.polymulx")
, [`polymul`](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul")
, [`polypow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polypow.html#numpy.polynomial.polynomial.polypow "numpy.polynomial.polynomial.polypow")

Examples

Try it in your browser!

\>>> from numpy.polynomial import polynomial as P
\>>> c1 \= (1, 2, 3)
\>>> c2 \= (3, 2, 1)
\>>> P.polydiv(c1, c2)
(array(\[3.\]), array(\[-8., -4.\]))
\>>> P.polydiv(c2, c1)
(array(\[ 0.33333333\]), array(\[ 2.66666667,  1.33333333\]))  # may vary

Copy to clipboard

Go BackOpen In Tab

On this page