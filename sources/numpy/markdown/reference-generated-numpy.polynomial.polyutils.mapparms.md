[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapparms.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.polynomial.polyutils.mapparms.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.polynomial.polyutils.mapparms.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.polynomial.polyutils.mapparms[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapparms.html#numpy-polynomial-polyutils-mapparms "Link to this heading")

=============================================================================================================================================================================================

polynomial.polyutils.mapparms(_old_, _new_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/polynomial/polyutils.py#L241-L286)
[#](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapparms.html#numpy.polynomial.polyutils.mapparms "Link to this definition")

Linear map parameters between domains.

Return the parameters of the linear map `offset + scale*x` that maps _old_ to _new_ such that `old[i] -> new[i]`, `i = 0, 1`.

Parameters:

**old, new**array\_like

Domains. Each domain must (successfully) convert to a 1-d array containing precisely two values.

Returns:

**offset, scale**scalars

The map `L(x) = offset + scale*x` maps the first domain to the second.

See also

[`getdomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.getdomain.html#numpy.polynomial.polyutils.getdomain "numpy.polynomial.polyutils.getdomain")
, [`mapdomain`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polyutils.mapdomain.html#numpy.polynomial.polyutils.mapdomain "numpy.polynomial.polyutils.mapdomain")

Notes

Also works for complex numbers, and thus can be used to calculate the parameters required to map any line in the complex plane to any other line therein.

Examples

Try it in your browser!

\>>> from numpy.polynomial import polyutils as pu
\>>> pu.mapparms((\-1,1),(\-1,1))
(0.0, 1.0)
\>>> pu.mapparms((1,\-1),(\-1,1))
(-0.0, -1.0)
\>>> i \= complex(0,1)
\>>> pu.mapparms((\-i,\-1),(1,i))
((1+1j), (1-0j))

Copy to clipboard

Go BackOpen In Tab

On this page