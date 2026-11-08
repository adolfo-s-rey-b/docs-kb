[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.resize.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.resize.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.resize.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.resize.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.resize.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.resize.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.resize.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.resize.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.resize.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.resize[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.resize.html#numpy-ma-maskedarray-resize "Link to this heading")

=====================================================================================================================================================================

method

ma.MaskedArray.resize(_newshape_, _refcheck\=True_, _order\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L4819-L4835)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.resize.html#numpy.ma.MaskedArray.resize "Link to this definition")

Warning

This method does nothing, except raise a ValueError exception. A masked array does not own its data and therefore cannot safely be resized in place. Use the [`numpy.ma.resize`](https://numpy.org/doc/stable/reference/generated/numpy.ma.resize.html#numpy.ma.resize "numpy.ma.resize")
 function instead.

This method is difficult to implement safely and may be deprecated in future releases of NumPy.

On this page