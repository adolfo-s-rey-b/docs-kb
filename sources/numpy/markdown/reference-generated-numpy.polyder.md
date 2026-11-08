[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polyder.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polyder.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polyder.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polyder.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polyder.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polyder.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polyder.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polyder.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polyder.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polyder.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polyder.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polyder.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polyder.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polyder.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polyder.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polyder.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polyder.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polyder.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polyder.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polyder.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polyder.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polyder.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polyder[#](https://numpy.org/doc/stable/reference/generated/numpy.polyder.html#numpy-polyder "Link to this heading")

===========================================================================================================================

numpy.polyder(_p_, _m\=1_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L377-L453)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polyder.html#numpy.polyder "Link to this definition")

Return the derivative of the specified order of a polynomial.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

Parameters:

**p**poly1d or sequence

Polynomial to differentiate. A sequence is interpreted as polynomial coefficients, see [`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")
.

**m**int, optional

Order of differentiation (default: 1)

Returns:

**der**poly1d

A new polynomial representing the derivative.

See also

[`polyint`](https://numpy.org/doc/stable/reference/generated/numpy.polyint.html#numpy.polyint "numpy.polyint")

Anti-derivative of a polynomial.

[`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")

Class for one-dimensional polynomials.

Examples

Try it in your browser!

The derivative of the polynomial \\(x^3 + x^2 + x^1 + 1\\) is:

\>>> import numpy as np

Copy to clipboard

\>>> p \= np.poly1d(\[1,1,1,1\])
\>>> p2 \= np.polyder(p)
\>>> p2
poly1d(\[3, 2, 1\])

Copy to clipboard

which evaluates to:

\>>> p2(2.)
17.0

Copy to clipboard

We can verify this, approximating the derivative with `(f(x + h) - f(x))/h`:

\>>> (p(2. + 0.001) \- p(2.)) / 0.001
17.007000999997857

Copy to clipboard

The fourth-order derivative of a 3rd-order polynomial is zero:

\>>> np.polyder(p, 2)
poly1d(\[6, 2\])
\>>> np.polyder(p, 3)
poly1d(\[6\])
\>>> np.polyder(p, 4)
poly1d(\[0\])

Copy to clipboard

Go BackOpen In Tab

On this page