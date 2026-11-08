[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.getdomain.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polyutils.getdomain.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polyutils.getdomain.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polyutils.getdomain[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.getdomain.html#numpy-polynomial-polyutils-getdomain "Link to this heading")

================================================================================================================================================================================================

polynomial.polyutils.getdomain(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polyutils.py#L194-L239)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.getdomain.html#numpy.polynomial.polyutils.getdomain "Link to this definition")

Return a domain suitable for given abscissae.

Find a domain suitable for a polynomial or Chebyshev series defined at the values supplied.

Parameters:

**x**array\_like

1-d array of abscissae whose domain will be determined.

Returns:

**domain**ndarray

1-d array containing two values. If the inputs are complex, then the two returned points are the lower left and upper right corners of the smallest rectangle (aligned with the axes) in the complex plane containing the points _x_. If the inputs are real, then the two points are the ends of the smallest interval containing the points _x_.

See also

[`mapparms`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapparms.html#numpy.polynomial.polyutils.mapparms "numpy.polynomial.polyutils.mapparms")
, [`mapdomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapdomain.html#numpy.polynomial.polyutils.mapdomain "numpy.polynomial.polyutils.mapdomain")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.polynomial import polyutils as pu
\>>> points \= np.arange(4)\*\*2 \- 5; points
array(\[-5, -4, -1,  4\])
\>>> pu.getdomain(points)
array(\[-5.,  4.\])
\>>> c \= np.exp(complex(0,1)\*np.pi\*np.arange(12)/6) \# unit circle
\>>> pu.getdomain(c)
array(\[-1.-1.j,  1.+1.j\])

Copy to clipboard

Go BackOpen In Tab

On this page