[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__class_getitem__.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ndarray.__class_getitem__.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__class_getitem__.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ndarray.__class_getitem__.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ndarray.__class_getitem__.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ndarray.__class_getitem__.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ndarray.__class_getitem__.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ndarray.__class_getitem__.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ndarray.__class_getitem__.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ndarray.\_\_class\_getitem\_\_[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__class_getitem__.html#numpy-ndarray-class-getitem "Link to this heading")

==================================================================================================================================================================================

method

ndarray.\_\_class\_getitem\_\_(_$cls_, _item_, _/_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.__class_getitem__.html#numpy.ndarray.__class_getitem__ "Link to this definition")

ndarray\[shape, dtype\]

Return a parametrized wrapper around the [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 type.

New in version 1.22.

Returns:

**alias**types.GenericAlias

A parametrized [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 type.

See also

[**PEP 585**](https://peps.python.org/pep-0585/)

Type hinting generics in standard collections.

[`numpy.typing.NDArray`](https://numpy.org/doc/stable/reference/typing.html#numpy.typing.NDArray "numpy.typing.NDArray")

An ndarray alias [generic](https://docs.python.org/3/glossary.html#term-generic-type "(in Python v3.14)")
 w.r.t. its [`dtype.type`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.type.html#numpy.dtype.type "numpy.dtype.type")
.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

\>>> np.ndarray\[tuple\[int\], np.dtype\[np.uint8\]\]
numpy.ndarray\[tuple\[int\], numpy.dtype\[numpy.uint8\]\]

Copy to clipboard

Go BackOpen In Tab

On this page