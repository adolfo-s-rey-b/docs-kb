[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.isdtype.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.isdtype.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.isdtype.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.isdtype.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.isdtype.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.isdtype.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.isdtype.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.isdtype.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.isdtype.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.isdtype.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.isdtype.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.isdtype.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.isdtype.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.isdtype.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.isdtype.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.isdtype.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.isdtype.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.isdtype.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.isdtype.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.isdtype.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.isdtype.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.isdtype.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.isdtype[#](https://numpy.org/doc/stable/reference/generated/numpy.isdtype.html#numpy-isdtype "Link to this heading")

===========================================================================================================================

numpy.isdtype(_dtype_, _kind_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/numerictypes.py#L321-L408)
[#](https://numpy.org/doc/stable/reference/generated/numpy.isdtype.html#numpy.isdtype "Link to this definition")

Determine if a provided dtype is of a specified data type `kind`.

This function only supports built-in NumPy’s data types. Third-party dtypes are not yet supported.

Parameters:

**dtype**dtype

The input dtype.

**kind**dtype or str or tuple of dtypes/strs.

dtype or dtype kind. Allowed dtype kinds are: \* `'bool'` : boolean kind \* `'signed integer'` : signed integer data types \* `'unsigned integer'` : unsigned integer data types \* `'integral'` : integer data types \* `'real floating'` : real-valued floating-point data types \* `'complex floating'` : complex floating-point data types \* `'numeric'` : numeric data types

Returns:

**out**bool

See also

[`issubdtype`](https://numpy.org/doc/stable/reference/generated/numpy.issubdtype.html#numpy.issubdtype "numpy.issubdtype")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.isdtype(np.float32, np.float64)
False
\>>> np.isdtype(np.float32, "real floating")
True
\>>> np.isdtype(np.complex128, ("real floating", "complex floating"))
True

Copy to clipboard

Go BackOpen In Tab

On this page