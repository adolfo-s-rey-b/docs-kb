[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__class_getitem__.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dtype.__class_getitem__.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__class_getitem__.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dtype.__class_getitem__.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dtype.__class_getitem__.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dtype.__class_getitem__.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dtype.__class_getitem__.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dtype.__class_getitem__.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dtype.__class_getitem__.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dtype.__class_getitem__.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dtype.__class_getitem__.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dtype.__class_getitem__.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dtype.__class_getitem__.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dtype.__class_getitem__.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dtype.__class_getitem__.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dtype.__class_getitem__.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dtype.__class_getitem__.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dtype.__class_getitem__.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dtype.__class_getitem__.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dtype.__class_getitem__.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dtype.__class_getitem__.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dtype.__class_getitem__.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dtype.\_\_class\_getitem\_\_[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__class_getitem__.html#numpy-dtype-class-getitem "Link to this heading")

============================================================================================================================================================================

method

dtype.\_\_class\_getitem\_\_(_item_, _/_)[#](https://numpy.org/doc/stable/reference/generated/numpy.dtype.__class_getitem__.html#numpy.dtype.__class_getitem__ "Link to this definition")

Return a parametrized wrapper around the [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 type.

New in version 1.22.

Returns:

**alias**types.GenericAlias

A parametrized [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 type.

See also

[**PEP 585**](https://peps.python.org/pep-0585/)

Type hinting generics in standard collections.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.dtype\[np.int64\]
numpy.dtype\[numpy.int64\]

Copy to clipboard

Go BackOpen In Tab

On this page