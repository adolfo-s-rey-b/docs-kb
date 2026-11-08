[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polysub.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polysub.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polysub.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polysub.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polysub.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polysub.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polysub.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polysub.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polysub.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polysub.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polysub.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polysub.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polysub.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polysub.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polysub.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polysub.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polysub.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polysub.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polysub.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polysub.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polysub.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polysub.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polysub[#](https://numpy.org/doc/stable/reference/generated/numpy.polysub.html#numpy-polysub "Link to this heading")

===========================================================================================================================

numpy.polysub(_a1_, _a2_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_polynomial_impl.py#L866-L920)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polysub.html#numpy.polysub "Link to this definition")

Difference (subtraction) of two polynomials.

Note

This forms part of the old polynomial API. Since version 1.4, the new polynomial API defined in [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#module-numpy.polynomial "numpy.polynomial")
 is preferred. A summary of the differences can be found in the [transition guide](https://numpy.org/doc/stable/reference/routines.polynomials.html)
.

Given two polynomials _a1_ and _a2_, returns `a1 - a2`. _a1_ and _a2_ can be either array\_like sequences of the polynomials’ coefficients (including coefficients equal to zero), or [`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")
 objects.

Parameters:

**a1, a2**array\_like or poly1d

Minuend and subtrahend polynomials, respectively.

Returns:

**out**ndarray or poly1d

Array or [`poly1d`](https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html#numpy.poly1d "numpy.poly1d")
 object of the difference polynomial’s coefficients.

See also

[`polyval`](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html#numpy.polyval "numpy.polyval")
, [`polydiv`](https://numpy.org/doc/stable/reference/generated/numpy.polydiv.html#numpy.polydiv "numpy.polydiv")
, [`polymul`](https://numpy.org/doc/stable/reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul")
, [`polyadd`](https://numpy.org/doc/stable/reference/generated/numpy.polyadd.html#numpy.polyadd "numpy.polyadd")

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.polysub(\[2, 10, \-2\], \[3, 10, \-4\])
array(\[-1,  0,  2\])

Copy to clipboard

Go BackOpen In Tab

On this page