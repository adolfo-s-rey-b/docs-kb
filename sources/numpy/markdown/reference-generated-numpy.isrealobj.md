[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.isrealobj.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.isrealobj.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.isrealobj.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.isrealobj.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.isrealobj.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.isrealobj.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.isrealobj.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.isrealobj.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.isrealobj.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.isrealobj.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.isrealobj.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.isrealobj.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.isrealobj.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.isrealobj.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.isrealobj.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.isrealobj.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.isrealobj.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.isrealobj.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.isrealobj.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.isrealobj.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.isrealobj.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.isrealobj.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.isrealobj[#](https://numpy.org/doc/stable/reference/generated/numpy.isrealobj.html#numpy-isrealobj "Link to this heading")

=================================================================================================================================

numpy.isrealobj(_x_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_type_check_impl.py#L307-L354)
[#](https://numpy.org/doc/stable/reference/generated/numpy.isrealobj.html#numpy.isrealobj "Link to this definition")

Return True if x is a not complex type or an array of complex numbers.

The type of the input is checked, not the value. So even if the input has an imaginary part equal to zero, [`isrealobj`](https://numpy.org/doc/stable/reference/generated/numpy.isrealobj.html#numpy.isrealobj "numpy.isrealobj")
 evaluates to False if the data type is complex.

Parameters:

**x**any

The input can be of any type and shape.

Returns:

**y**bool

The return value, False if _x_ is of a complex type.

See also

[`iscomplexobj`](https://numpy.org/doc/stable/reference/generated/numpy.iscomplexobj.html#numpy.iscomplexobj "numpy.iscomplexobj")
, [`isreal`](https://numpy.org/doc/stable/reference/generated/numpy.isreal.html#numpy.isreal "numpy.isreal")

Notes

The function is only meant for arrays with numerical values but it accepts all other objects. Since it assumes array input, the return value of other objects may be True.

\>>> np.isrealobj('A string')
True
\>>> np.isrealobj(False)
True
\>>> np.isrealobj(None)
True

Copy to clipboard

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.isrealobj(1)
True
\>>> np.isrealobj(1+0j)
False
\>>> np.isrealobj(\[3, 1+0j, True\])
False

Copy to clipboard

Go BackOpen In Tab

On this page