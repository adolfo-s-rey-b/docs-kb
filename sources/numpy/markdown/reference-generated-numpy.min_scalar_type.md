[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.min_scalar_type.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.min\_scalar\_type[#](https://numpy.org/doc/stable/reference/generated/numpy.min_scalar_type.html#numpy-min-scalar-type "Link to this heading")

=====================================================================================================================================================

numpy.min\_scalar\_type(_a_, _/_)[#](https://numpy.org/doc/stable/reference/generated/numpy.min_scalar_type.html#numpy.min_scalar_type "Link to this definition")

For scalar `a`, returns the data type with the smallest size and smallest scalar kind which can hold its value. For non-scalar array `a`, returns the vector’s dtype unmodified.

Floating point values are not demoted to integers, and complex values are not demoted to floats.

Parameters:

**a**scalar or array\_like

The value whose minimal data type is to be found.

Returns:

**out**dtype

The minimal data type.

See also

[`result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")
, [`promote_types`](https://numpy.org/doc/stable/reference/generated/numpy.promote_types.html#numpy.promote_types "numpy.promote_types")
, [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, [`can_cast`](https://numpy.org/doc/stable/reference/generated/numpy.can_cast.html#numpy.can_cast "numpy.can_cast")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.min\_scalar\_type(10)
dtype('uint8')

Copy to clipboard

\>>> np.min\_scalar\_type(\-260)
dtype('int16')

Copy to clipboard

\>>> np.min\_scalar\_type(3.1)
dtype('float16')

Copy to clipboard

\>>> np.min\_scalar\_type(1e50)
dtype('float64')

Copy to clipboard

\>>> np.min\_scalar\_type(np.arange(4, dtype\=np.float64))
dtype('float64')

Copy to clipboard

Go BackOpen In Tab

On this page