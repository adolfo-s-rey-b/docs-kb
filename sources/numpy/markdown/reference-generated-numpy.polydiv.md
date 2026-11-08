[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polydiv.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polydiv.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polydiv.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polydiv.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polydiv.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polydiv.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polydiv.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polydiv.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polydiv.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polydiv.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polydiv.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polydiv.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polydiv.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polydiv.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polydiv.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polydiv.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polydiv.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polydiv.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polydiv.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polydiv.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polydiv.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polydiv.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polydiv[#](https://numpy.org/doc/stable/reference/generated/numpy.polydiv.html#numpy-polydiv "Link to this heading")

===========================================================================================================================

numpy.polydiv(_u_, _v_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L991-L1064)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polydiv.html#numpy.polydiv "Link to this definition")

Returns the quotient and remainder of polynomial division.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

The input arrays are the coefficients (including any coefficients equal to zero) of the “numerator” (dividend) and “denominator” (divisor) polynomials, respectively.

Parameters:

**u**array\_like or poly1d

Dividend polynomial’s coefficients.

**v**array\_like or poly1d

Divisor polynomial’s coefficients.

Returns:

**q**ndarray

Coefficients, including those equal to zero, of the quotient.

**r**ndarray

Coefficients, including those equal to zero, of the remainder.

See also

[`poly`](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#numpy.poly "numpy.poly")
, [`polyadd`](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html#numpy.polyadd "numpy.polyadd")
, [`polyder`](https://numpy.org/doc/stable/reference/generated/numpy.polyder.html#numpy.polyder "numpy.polyder")
, [`polydiv`](https://numpy.org/doc/stable/reference/generated/numpy.polydiv.html#numpy.polydiv "numpy.polydiv")
, [`polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")
, [`polyint`](https://numpy.org/doc/stable/reference/generated/numpy.polyint.html#numpy.polyint "numpy.polyint")
, [`polymul`](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul")
, [`polysub`](https://numpy.org/doc/stable/reference/generated/numpy.polysub.html#numpy.polysub "numpy.polysub")

[`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")

Notes

Both _u_ and _v_ must be 0-d or 1-d (ndim = 0 or 1), but _u.ndim_ need not equal _v.ndim_. In other words, all four possible combinations - `u.ndim = v.ndim = 0`, `u.ndim = v.ndim = 1`, `u.ndim = 1, v.ndim = 0`, and `u.ndim = 0, v.ndim = 1` - work.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> x \= np.array(\[3.0, 5.0, 2.0\])
\>>> y \= np.array(\[2.0, 1.0\])
\>>> np.polydiv(x, y)
(array(\[1.5 , 1.75\]), array(\[0.25\]))

Copy to clipboard

Go BackOpen In Tab

On this page