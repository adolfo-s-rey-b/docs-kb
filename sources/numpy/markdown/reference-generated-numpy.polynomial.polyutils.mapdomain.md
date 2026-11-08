[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapdomain.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polyutils.mapdomain.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polyutils.mapdomain.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polyutils.mapdomain[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapdomain.html#numpy-polynomial-polyutils-mapdomain "Link to this heading")

================================================================================================================================================================================================

polynomial.polyutils.mapdomain(_x_, _old_, _new_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polyutils.py#L288-L355)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapdomain.html#numpy.polynomial.polyutils.mapdomain "Link to this definition")

Apply linear map to input points.

The linear map `offset + scale*x` that maps the domain _old_ to the domain _new_ is applied to the points _x_.

Parameters:

**x**array\_like

Points to be mapped. If _x_ is a subtype of ndarray the subtype will be preserved.

**old, new**array\_like

The two domains that determine the map. Each must (successfully) convert to 1-d arrays containing precisely two values.

Returns:

**x\_out**ndarray

Array of points of the same shape as _x_, after application of the linear map between the two domains.

See also

[`getdomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.getdomain.html#numpy.polynomial.polyutils.getdomain "numpy.polynomial.polyutils.getdomain")
, [`mapparms`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapparms.html#numpy.polynomial.polyutils.mapparms "numpy.polynomial.polyutils.mapparms")

Notes

Effectively, this implements:

\\\[x\\\_out = new\[0\] + m(x - old\[0\])\\\]

where

\\\[m = \\frac{new\[1\]-new\[0\]}{old\[1\]-old\[0\]}\\\]

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.polynomial import polyutils as pu
\>>> old\_domain \= (\-1,1)
\>>> new\_domain \= (0,2\*np.pi)
\>>> x \= np.linspace(\-1,1,6); x
array(\[-1. , -0.6, -0.2,  0.2,  0.6,  1. \])
\>>> x\_out \= pu.mapdomain(x, old\_domain, new\_domain); x\_out
array(\[ 0.        ,  1.25663706,  2.51327412,  3.76991118,  5.02654825, # may vary\
        6.28318531\])
\>>> x \- pu.mapdomain(x\_out, new\_domain, old\_domain)
array(\[0., 0., 0., 0., 0., 0.\])

Copy to clipboard

Also works for complex numbers (and thus can be used to map any line in the complex plane to any other line therein).

\>>> i \= complex(0,1)
\>>> old \= (\-1 \- i, 1 + i)
\>>> new \= (\-1 + i, 1 \- i)
\>>> z \= np.linspace(old\[0\], old\[1\], 6); z
array(\[-1. -1.j , -0.6-0.6j, -0.2-0.2j,  0.2+0.2j,  0.6+0.6j,  1. +1.j \])
\>>> new\_z \= pu.mapdomain(z, old, new); new\_z
array(\[-1.0+1.j , -0.6+0.6j, -0.2+0.2j,  0.2-0.2j,  0.6-0.6j,  1.0-1.j \]) # may vary

Copy to clipboard

Go BackOpen In Tab

On this page