[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmul.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.chebmul.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.chebmul.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebmul[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmul.html#numpy-polynomial-chebyshev-chebmul "Link to this heading")

==========================================================================================================================================================================================

polynomial.chebyshev.chebmul(_c1_, _c2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L699-L745)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmul.html#numpy.polynomial.chebyshev.chebmul "Link to this definition")

Multiply one Chebyshev series by another.

Returns the product of two Chebyshev series _c1_ \* _c2_. The arguments are sequences of coefficients, from lowest order “term” to highest, e.g., \[1,2,3\] represents the series `T_0 + 2*T_1 + 3*T_2`.

Parameters:

**c1, c2**array\_like

1-D arrays of Chebyshev series coefficients ordered from low to high.

Returns:

**out**ndarray

Of Chebyshev series coefficients representing their product.

See also

[`chebadd`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebadd.html#numpy.polynomial.chebyshev.chebadd "numpy.polynomial.chebyshev.chebadd")
, [`chebsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebsub.html#numpy.polynomial.chebyshev.chebsub "numpy.polynomial.chebyshev.chebsub")
, [`chebmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmulx.html#numpy.polynomial.chebyshev.chebmulx "numpy.polynomial.chebyshev.chebmulx")
, [`chebdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebdiv.html#numpy.polynomial.chebyshev.chebdiv "numpy.polynomial.chebyshev.chebdiv")
, [`chebpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebpow.html#numpy.polynomial.chebyshev.chebpow "numpy.polynomial.chebyshev.chebpow")

Notes

In general, the (polynomial) product of two C-series results in terms that are not in the Chebyshev polynomial basis set. Thus, to express the product as a C-series, it is typically necessary to “reproject” the product onto said basis set, which typically produces “unintuitive live” (but correct) results; see Examples section below.

Examples

Try it in your browser!

\>>> from numpy.polynomial import chebyshev as C
\>>> c1 \= (1,2,3)
\>>> c2 \= (3,2,1)
\>>> C.chebmul(c1,c2) \# multiplication requires "reprojection"
array(\[  6.5,  12. ,  12. ,   4. ,   1.5\])

Copy to clipboard

Go BackOpen In Tab

On this page