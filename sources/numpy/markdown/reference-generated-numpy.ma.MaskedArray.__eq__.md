[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__eq__.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.__eq__.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.__eq__.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.\_\_eq\_\_[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__eq__.html#numpy-ma-maskedarray-eq "Link to this heading")

=====================================================================================================================================================================

method

ma.MaskedArray.\_\_eq\_\_(_other_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L4267-L4278)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__eq__.html#numpy.ma.MaskedArray.__eq__ "Link to this definition")

Check whether other equals self elementwise.

When either of the elements is masked, the result is masked as well, but the underlying boolean data are still set, with self and other considered equal if both are masked, and unequal otherwise.

For structured arrays, all fields are combined, with masked values ignored. The result is masked if all fields were masked, with self and other considered equal only if both were fully masked.

On this page