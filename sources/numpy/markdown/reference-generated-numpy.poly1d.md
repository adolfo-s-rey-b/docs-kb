[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.poly1d.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.poly1d.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.poly1d.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.poly1d.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.poly1d.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.poly1d.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.poly1d.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.poly1d.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.poly1d.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.poly1d.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.poly1d.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.poly1d.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.poly1d.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.poly1d.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.poly1d.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.poly1d.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.poly1d.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.poly1d.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.poly1d.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.poly1d.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.poly1d[#](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy-poly1d "Link to this heading")

========================================================================================================================

_class_ numpy.poly1d(_c\_or\_r_, _r\=False_, _variable\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L1095-L1462)
[#](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "Link to this definition")

A one-dimensional polynomial class.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

A convenience class, used to encapsulate “natural” operations on polynomials so that said operations may take on their customary form in code (see Examples).

Parameters:

**c\_or\_r**array\_like

The polynomial’s coefficients, in decreasing powers, or if the value of the second parameter is True, the polynomial’s roots (values where the polynomial evaluates to 0). For example, `poly1d([1, 2, 3])` returns an object that represents \\(x^2 + 2x + 3\\), whereas `poly1d([1, 2, 3], True)` returns one that represents \\((x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x -6\\).

**r**bool, optional

If True, _c\_or\_r_ specifies the polynomial’s roots; the default is False.

**variable**str, optional

Changes the variable used when printing _p_ from _x_ to [`variable`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.variable.html#numpy.poly1d.variable "numpy.poly1d.variable")
 (see Examples).

Attributes:

[`c`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.c.html#numpy.poly1d.c "numpy.poly1d.c")

The polynomial coefficients

[`coef`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.coef.html#numpy.poly1d.coef "numpy.poly1d.coef")

The polynomial coefficients

[`coefficients`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.coefficients.html#numpy.poly1d.coefficients "numpy.poly1d.coefficients")

The polynomial coefficients

[`coeffs`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.coeffs.html#numpy.poly1d.coeffs "numpy.poly1d.coeffs")

The polynomial coefficients

[`o`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.o.html#numpy.poly1d.o "numpy.poly1d.o")

The order or degree of the polynomial

[`order`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.order.html#numpy.poly1d.order "numpy.poly1d.order")

The order or degree of the polynomial

[`r`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.r.html#numpy.poly1d.r "numpy.poly1d.r")

The roots of the polynomial, where self(x) == 0

[`roots`](https://numpy.org/doc/stable/reference/generated/numpy.roots.html#numpy.roots "numpy.roots")

The roots of the polynomial, where self(x) == 0

[`variable`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.variable.html#numpy.poly1d.variable "numpy.poly1d.variable")

The name of the polynomial variable

Methods

|     |     |
| --- | --- |
| [`__call__`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.__call__.html#numpy.poly1d.__call__ "numpy.poly1d.__call__")<br>(val) | Call self as a function. |
| [`deriv`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.deriv.html#numpy.poly1d.deriv "numpy.poly1d.deriv")<br>(\[m\]) | Return a derivative of this polynomial. |
| [`integ`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.integ.html#numpy.poly1d.integ "numpy.poly1d.integ")<br>(\[m, k\]) | Return an antiderivative (indefinite integral) of this polynomial. |

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

Construct the polynomial \\(x^2 + 2x + 3\\):

\>>> import numpy as np

Copy to clipboard

\>>> p \= np.poly1d(\[1, 2, 3\])
\>>> print(np.poly1d(p))
   2
1 x + 2 x + 3

Copy to clipboard

Evaluate the polynomial at \\(x = 0.5\\):

\>>> p(0.5)
4.25

Copy to clipboard

Find the roots:

\>>> p.r
array(\[-1.+1.41421356j, -1.-1.41421356j\])
\>>> p(p.r)
array(\[ -4.44089210e-16+0.j,  -4.44089210e-16+0.j\]) # may vary

Copy to clipboard

These numbers in the previous line represent (0, 0) to machine precision

Show the coefficients:

\>>> p.c
array(\[1, 2, 3\])

Copy to clipboard

Display the order (the leading zero-coefficients are removed):

\>>> p.order
2

Copy to clipboard

Show the coefficient of the k-th power in the polynomial (which is equivalent to `p.c[-(i+1)]`):

\>>> p\[1\]
2

Copy to clipboard

Polynomials can be added, subtracted, multiplied, and divided (returns quotient and remainder):

\>>> p \* p
poly1d(\[ 1,  4, 10, 12,  9\])

Copy to clipboard

\>>> (p\*\*3 + 4) / p
(poly1d(\[ 1.,  4., 10., 12.,  9.\]), poly1d(\[4.\]))

Copy to clipboard

`asarray(p)` gives the coefficient array, so polynomials can be used in all functions that accept arrays:

\>>> p\*\*2 \# square of polynomial
poly1d(\[ 1,  4, 10, 12,  9\])

Copy to clipboard

\>>> np.square(p) \# square of individual coefficients
array(\[1, 4, 9\])

Copy to clipboard

The variable used in the string representation of _p_ can be modified, using the [`variable`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.variable.html#numpy.poly1d.variable "numpy.poly1d.variable")
 parameter:

\>>> p \= np.poly1d(\[1,2,3\], variable\='z')
\>>> print(p)
   2
1 z + 2 z + 3

Copy to clipboard

Construct a polynomial from its roots:

\>>> np.poly1d(\[1, 2\], True)
poly1d(\[ 1., -3.,  2.\])

Copy to clipboard

This is the same polynomial as obtained by:

\>>> np.poly1d(\[1, \-1\]) \* np.poly1d(\[1, \-2\])
poly1d(\[ 1, -3,  2\])

Copy to clipboard

Go BackOpen In Tab

On this page