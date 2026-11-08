[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polyint.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polyint.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polyint.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polyint.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polyint.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polyint.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polyint.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polyint.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polyint.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polyint.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polyint.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polyint.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polyint.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polyint.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polyint.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polyint.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polyint.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polyint.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polyint.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polyint.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polyint.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polyint.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polyint[#](https://numpy.org/doc/stable/reference/generated/numpy.polyint.html#numpy-polyint "Link to this heading")

===========================================================================================================================

numpy.polyint(_p_, _m\=1_, _k\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L269-L370)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polyint.html#numpy.polyint "Link to this definition")

Return an antiderivative (indefinite integral) of a polynomial.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

The returned order _m_ antiderivative _P_ of polynomial _p_ satisfies \\(\\frac{d^m}{dx^m}P(x) = p(x)\\) and is defined up to _m - 1_ integration constants _k_. The constants determine the low-order polynomial part

\\\[\\frac{k\_{m-1}}{0!} x^0 + \\ldots + \\frac{k\_0}{(m-1)!}x^{m-1}\\\]

of _P_ so that \\(P^{(j)}(0) = k\_{m-j-1}\\).

Parameters:

**p**array\_like or poly1d

Polynomial to integrate. A sequence is interpreted as polynomial coefficients, see [`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")
.

**m**int, optional

Order of the antiderivative. (Default: 1)

**k**list of _m_ scalars or scalar, optional

Integration constants. They are given in the order of integration: those corresponding to highest-order terms come first.

If `None` (default), all constants are assumed to be zero. If _m = 1_, a single scalar can be given instead of a list.

See also

[`polyder`](https://numpy.org/doc/stable/reference/generated/numpy.polyder.html#numpy.polyder "numpy.polyder")

derivative of a polynomial

[`poly1d.integ`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.integ.html#numpy.poly1d.integ "numpy.poly1d.integ")

equivalent method

Examples

Try it in your browser!

The defining property of the antiderivative:

\>>> import numpy as np

Copy to clipboard

\>>> p \= np.poly1d(\[1,1,1\])
\>>> P \= np.polyint(p)
\>>> P
 poly1d(\[ 0.33333333,  0.5       ,  1.        ,  0.        \]) # may vary
\>>> np.polyder(P) \== p
True

Copy to clipboard

The integration constants default to zero, but can be specified:

\>>> P \= np.polyint(p, 3)
\>>> P(0)
0.0
\>>> np.polyder(P)(0)
0.0
\>>> np.polyder(P, 2)(0)
0.0
\>>> P \= np.polyint(p, 3, k\=\[6,5,3\])
\>>> P
poly1d(\[ 0.01666667,  0.04166667,  0.16666667,  3. ,  5. ,  3. \]) # may vary

Copy to clipboard

Note that 3 = 6 / 2!, and that the constants are given in the order of integrations. Constant of the highest-order polynomial term comes first:

\>>> np.polyder(P, 2)(0)
6.0
\>>> np.polyder(P, 1)(0)
5.0
\>>> P(0)
3.0

Copy to clipboard

Go BackOpen In Tab

On this page