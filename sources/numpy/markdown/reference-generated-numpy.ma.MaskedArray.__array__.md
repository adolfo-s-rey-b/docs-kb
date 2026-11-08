[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__array__.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.__array__.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__array__.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.__array__.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.__array__.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.__array__.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.__array__.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.__array__.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.__array__.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.\_\_array\_\_[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__array__.html#numpy-ma-maskedarray-array "Link to this heading")

==============================================================================================================================================================================

method

ma.MaskedArray.\_\_array\_\_(\[_dtype_, \]_\*_, _copy=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.__array__.html#numpy.ma.MaskedArray.__array__ "Link to this definition")

For `dtype` parameter it returns a new reference to self if `dtype` is not given or it matches array’s data type. A new array of provided data type is returned if `dtype` is different from the current data type of the array. For `copy` parameter it returns a new reference to self if `copy=False` or `copy=None` and copying isn’t enforced by `dtype` parameter. The method returns a new array for `copy=True`, regardless of `dtype` parameter.

A more detailed explanation of the `__array__` interface can be found in [The \_\_array\_\_() method](https://numpy.org/doc/stable/user/basics.interoperability.html#dunder-array-interface)
.

On this page