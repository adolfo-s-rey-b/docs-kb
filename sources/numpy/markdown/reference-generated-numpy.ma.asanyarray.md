[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.asanyarray.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.asanyarray.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.asanyarray.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.asanyarray.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.asanyarray.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.asanyarray.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.asanyarray.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.asanyarray.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.asanyarray.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.asanyarray.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.asanyarray.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.asanyarray.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.asanyarray.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.asanyarray.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.asanyarray.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.asanyarray.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.asanyarray.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.asanyarray.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.asanyarray.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.asanyarray.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.asanyarray.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.asanyarray.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.asanyarray[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.asanyarray.html#numpy-ma-asanyarray "Link to this heading")

=============================================================================================================================================

ma.asanyarray(_a_, _dtype\=None_, _order\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L8676-L8736)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.asanyarray.html#numpy.ma.asanyarray "Link to this definition")

Convert the input to a masked array, conserving subclasses.

If _a_ is a subclass of [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
, its class is conserved. No copy is performed if the input is already an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.

Parameters:

**a**array\_like

Input data, in any form that can be converted to an array.

**dtype**dtype, optional

By default, the data-type is inferred from the input data.

**order**{‘C’, ‘F’, ‘A’, ‘K’}, optional

Memory layout. ‘A’ and ‘K’ depend on the order of input array `a`. ‘C’ row-major (C-style), ‘F’ column-major (Fortran-style) memory representation. ‘A’ (any) means ‘F’ if `a` is Fortran contiguous, ‘C’ otherwise ‘K’ (keep) preserve input order Defaults to ‘K’.

Returns:

**out**MaskedArray

MaskedArray interpretation of _a_.

See also

[`asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "numpy.asarray")

Similar to [`asanyarray`](https://numpy.org/doc/stable/reference/generated/numpy.asanyarray.html#numpy.asanyarray "numpy.asanyarray")
, but does not conserve subclass.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(10.).reshape(2, 5)
\>>> x
array(\[\[0., 1., 2., 3., 4.\],\
       \[5., 6., 7., 8., 9.\]\])
\>>> np.ma.asanyarray(x)
masked\_array(
  data=\[\[0., 1., 2., 3., 4.\],\
        \[5., 6., 7., 8., 9.\]\],
  mask=False,
  fill\_value=1e+20)
\>>> type(np.ma.asanyarray(x))
<class 'numpy.ma.MaskedArray'>

Copy to clipboard

Go BackOpen In Tab

On this page