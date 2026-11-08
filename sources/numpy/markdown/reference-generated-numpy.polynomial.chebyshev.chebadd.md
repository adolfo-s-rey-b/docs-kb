[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebadd.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.chebyshev.chebadd.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.chebyshev.chebadd.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.chebyshev.chebadd[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebadd.html#numpy-polynomial-chebyshev-chebadd "Link to this heading")

==========================================================================================================================================================================================

polynomial.chebyshev.chebadd(_c1_, _c2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/chebyshev.py#L568-L607)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebadd.html#numpy.polynomial.chebyshev.chebadd "Link to this definition")

Add one Chebyshev series to another.

Returns the sum of two Chebyshev series _c1_ + _c2_. The arguments are sequences of coefficients ordered from lowest order term to highest, i.e., \[1,2,3\] represents the series `T_0 + 2*T_1 + 3*T_2`.

Parameters:

**c1, c2**array\_like

1-D arrays of Chebyshev series coefficients ordered from low to high.

Returns:

**out**ndarray

Array representing the Chebyshev series of their sum.

See also

[`chebsub`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebsub.html#numpy.polynomial.chebyshev.chebsub "numpy.polynomial.chebyshev.chebsub")
, [`chebmulx`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmulx.html#numpy.polynomial.chebyshev.chebmulx "numpy.polynomial.chebyshev.chebmulx")
, [`chebmul`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebmul.html#numpy.polynomial.chebyshev.chebmul "numpy.polynomial.chebyshev.chebmul")
, [`chebdiv`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebdiv.html#numpy.polynomial.chebyshev.chebdiv "numpy.polynomial.chebyshev.chebdiv")
, [`chebpow`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.chebyshev.chebpow.html#numpy.polynomial.chebyshev.chebpow "numpy.polynomial.chebyshev.chebpow")

Notes

Unlike multiplication, division, etc., the sum of two Chebyshev series is a Chebyshev series (without having to “reproject” the result onto the basis set) so addition, just like that of “standard” polynomials, is simply “component-wise.”

Examples

Try it in your browser!

\>>> from numpy.polynomial import chebyshev as C
\>>> c1 \= (1,2,3)
\>>> c2 \= (3,2,1)
\>>> C.chebadd(c1,c2)
array(\[4., 4., 4.\])

Copy to clipboard

Go BackOpen In Tab

On this page