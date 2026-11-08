[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polyadd.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polyadd.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polyadd.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polyadd.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polyadd.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polyadd.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polyadd.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polyadd.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polyadd.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polyadd.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polyadd.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polyadd.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polyadd.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polyadd.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polyadd.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polyadd.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polyadd.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polyadd.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polyadd.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polyadd.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polyadd[#](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html#numpy-polyadd "Link to this heading")

===========================================================================================================================

numpy.polyadd(_a1_, _a2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L797-L863)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html#numpy.polyadd "Link to this definition")

Find the sum of two polynomials.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

Returns the polynomial resulting from the sum of two input polynomials. Each input must be either a poly1d object or a 1D sequence of polynomial coefficients, from highest to lowest degree.

Parameters:

**a1, a2**array\_like or poly1d object

Input polynomials.

Returns:

**out**ndarray or poly1d object

The sum of the inputs. If either input is a poly1d object, then the output is also a poly1d object. Otherwise, it is a 1D array of polynomial coefficients from highest to lowest degree.

See also

[`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")

A one-dimensional polynomial class.

[`poly`](https://numpy.org/doc/stable/reference/generated/numpy.poly.html#numpy.poly "numpy.poly")
, [`polyadd`](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html#numpy.polyadd "numpy.polyadd")
, [`polyder`](https://numpy.org/doc/stable/reference/generated/numpy.polyder.html#numpy.polyder "numpy.polyder")
, [`polydiv`](https://numpy.org/doc/stable/reference/generated/numpy.polydiv.html#numpy.polydiv "numpy.polydiv")
, [`polyfit`](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html#numpy.polyfit "numpy.polyfit")
, [`polyint`](https://numpy.org/doc/stable/reference/generated/numpy.polyint.html#numpy.polyint "numpy.polyint")
, [`polysub`](https://numpy.org/doc/stable/reference/generated/numpy.polysub.html#numpy.polysub "numpy.polysub")
, [`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.polyadd(\[1, 2\], \[9, 5, 4\])
array(\[9, 6, 6\])

Copy to clipboard

Using poly1d objects:

\>>> p1 \= np.poly1d(\[1, 2\])
\>>> p2 \= np.poly1d(\[9, 5, 4\])
\>>> print(p1)
1 x + 2
\>>> print(p2)
   2
9 x + 5 x + 4
\>>> print(np.polyadd(p1, p2))
   2
9 x + 6 x + 6

Copy to clipboard

Go BackOpen In Tab

On this page