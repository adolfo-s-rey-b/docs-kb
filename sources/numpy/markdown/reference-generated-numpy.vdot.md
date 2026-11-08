[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.vdot.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.vdot.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.vdot.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.vdot.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.vdot.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.vdot.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.vdot.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.vdot.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.vdot.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.vdot.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.vdot.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.vdot.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.vdot.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.vdot.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.vdot.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.vdot.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.vdot.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.vdot.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.vdot.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.vdot.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.vdot[#](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy-vdot "Link to this heading")

==================================================================================================================

numpy.vdot(_a_, _b_, _/_)[#](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot "Link to this definition")

Return the dot product of two vectors.

The [`vdot`](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot "numpy.vdot")
 function handles complex numbers differently than [`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
: if the first argument is complex, it is replaced by its complex conjugate in the dot product calculation. [`vdot`](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot "numpy.vdot")
 also handles multidimensional arrays differently than [`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")
: it does not perform a matrix product, but flattens the arguments to 1-D arrays before taking a vector dot product.

Consequently, when the arguments are 2-D arrays of the same shape, this function effectively returns their [Frobenius inner product](https://en.wikipedia.org/wiki/Frobenius_inner_product)
 (also known as the _trace inner product_ or the _standard inner product_ on a vector space of matrices).

Parameters:

**a**array\_like

If _a_ is complex the complex conjugate is taken before calculation of the dot product.

**b**array\_like

Second argument to the dot product.

Returns:

**output**ndarray

Dot product of _a_ and _b_. Can be an int, float, or complex depending on the types of _a_ and _b_.

See also

[`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot "numpy.dot")

Return the dot product without using the complex conjugate of the first argument.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[1+2j,3+4j\])
\>>> b \= np.array(\[5+6j,7+8j\])
\>>> np.vdot(a, b)
(70-8j)
\>>> np.vdot(b, a)
(70+8j)

Copy to clipboard

Note that higher-dimensional arrays are flattened!

\>>> a \= np.array(\[\[1, 4\], \[5, 6\]\])
\>>> b \= np.array(\[\[4, 1\], \[2, 2\]\])
\>>> np.vdot(a, b)
30
\>>> np.vdot(b, a)
30
\>>> 1\*4 + 4\*1 + 5\*2 + 6\*2
30

Copy to clipboard

Go BackOpen In Tab

On this page