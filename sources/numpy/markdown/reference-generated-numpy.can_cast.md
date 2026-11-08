[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.can_cast.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.can_cast.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.can_cast.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.can_cast.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.can_cast.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.can_cast.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.can_cast.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.can_cast.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.can_cast.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.can_cast.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.can_cast.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.can_cast.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.can_cast.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.can_cast.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.can_cast.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.can_cast.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.can_cast.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.can_cast.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.can_cast.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.can_cast.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.can_cast.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.can_cast.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.can\_cast[#](https://numpy.org/doc/stable/reference/generated/numpy.can_cast.html#numpy-can-cast "Link to this heading")

===============================================================================================================================

numpy.can\_cast(_from\__, _to_, _casting\='safe'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.can_cast.html#numpy.can_cast "Link to this definition")

Returns True if cast between data types can occur according to the casting rule.

Parameters:

**from\_**dtype, dtype specifier, NumPy scalar, or array

Data type, NumPy scalar, or array to cast from.

**to**dtype or dtype specifier

Data type to cast to.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}, optional

Controls what kind of data casting may occur.

*   ‘no’ means the data types should not be cast at all.
    
*   ‘equiv’ means only byte-order changes are allowed.
    
*   ‘safe’ means only casts which can preserve values are allowed.
    
*   ‘same\_kind’ means only safe casts or casts within a kind, like float64 to float32, are allowed.
    
*   ‘unsafe’ means any data conversions may be done.
    

Returns:

**out**bool

True if cast can occur according to the casting rule.

See also

[`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
, [`result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")

Notes

Changed in version 2.0: This function does not support Python scalars anymore and does not apply any value-based logic for 0-D arrays and NumPy scalars.

Examples

Try it in your browser!

Basic examples

\>>> import numpy as np
\>>> np.can\_cast(np.int32, np.int64)
True
\>>> np.can\_cast(np.float64, complex)
True
\>>> np.can\_cast(complex, float)
False

Copy to clipboard

\>>> np.can\_cast('i8', 'f8')
True
\>>> np.can\_cast('i8', 'f4')
False
\>>> np.can\_cast('i4', 'S4')
False

Copy to clipboard

Go BackOpen In Tab

On this page