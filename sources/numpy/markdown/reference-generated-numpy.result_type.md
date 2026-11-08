[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.result_type.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.result_type.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.result_type.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.result_type.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.result_type.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.result_type.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.result_type.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.result_type.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.result_type.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.result_type.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.result_type.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.result_type.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.result_type.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.result_type.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.result_type.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.result_type.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.result_type.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.result_type.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.result_type.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.result_type.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.result\_type[#](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy-result-type "Link to this heading")

========================================================================================================================================

numpy.result\_type(_\*arrays\_and\_dtypes_)[#](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "Link to this definition")

Returns the type that results from applying the NumPy [type promotion](https://numpy.org/doc/stable/reference/arrays.promotion.html#arrays-promotion)
 rules to the arguments.

Parameters:

**arrays\_and\_dtypes**list of arrays and dtypes

The operands of some operation whose result type is needed.

Returns:

**out**dtype

The result type.

See also

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, [`promote_types`](https://numpy.org/doc/stable/reference/generated/numpy.promote_types.html#numpy.promote_types "numpy.promote_types")
, [`min_scalar_type`](https://numpy.org/doc/stable/reference/generated/numpy.min_scalar_type.html#numpy.min_scalar_type "numpy.min_scalar_type")
, [`can_cast`](https://numpy.org/doc/stable/reference/generated/numpy.can_cast.html#numpy.can_cast "numpy.can_cast")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.result\_type(3, np.arange(7, dtype\=np.int8))
dtype('int8')

Copy to clipboard

\>>> np.result\_type(np.int32, np.complex64)
dtype('complex128')

Copy to clipboard

\>>> np.result\_type(3.0, \-2)
dtype('float64')

Copy to clipboard

Go BackOpen In Tab

On this page