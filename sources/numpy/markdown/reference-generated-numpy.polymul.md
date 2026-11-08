[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polymul[#](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy-polymul "Link to this heading")

===========================================================================================================================

numpy.polymul(_a1_, _a2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L923-L984)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy.polymul "Link to this definition")

Find the product of two polynomials.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

Finds the polynomial resulting from the multiplication of the two input polynomials. Each input must be either a poly1d object or a 1D sequence of polynomial coefficients, from highest to lowest degree.

Parameters:

**a1, a2**array\_like or poly1d object

Input polynomials.

Returns:

**out**ndarray or poly1d object

The polynomial resulting from the multiplication of the inputs. If either inputs is a poly1d object, then the output is also a poly1d object. Otherwise, it is a 1D array of polynomial coefficients from highest to lowest degree.

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

[`convolve`](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")

Array convolution. Same output as polymul, but has parameter for overlap mode.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.polymul(\[1, 2, 3\], \[9, 5, 1\])
array(\[ 9, 23, 38, 17,  3\])

Copy to clipboard

Using poly1d objects:

\>>> p1 \= np.poly1d(\[1, 2, 3\])
\>>> p2 \= np.poly1d(\[9, 5, 1\])
\>>> print(p1)
   2
1 x + 2 x + 3
\>>> print(p2)
   2
9 x + 5 x + 1
\>>> print(np.polymul(p1, p2))
   4      3      2
9 x + 23 x + 38 x + 17 x + 3

Copy to clipboard

Go BackOpen In Tab

On this page