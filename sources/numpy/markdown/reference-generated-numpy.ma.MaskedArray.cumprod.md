[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumprod.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.MaskedArray.cumprod.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.MaskedArray.cumprod.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.MaskedArray.cumprod[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumprod.html#numpy-ma-maskedarray-cumprod "Link to this heading")

========================================================================================================================================================================

method

ma.MaskedArray.cumprod(_axis\=None_, _dtype\=None_, _out\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5345-L5374)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.cumprod.html#numpy.ma.MaskedArray.cumprod "Link to this definition")

Return the cumulative product of the array elements over the given axis.

Masked values are set to 1 internally during the computation. However, their position is saved, and the result will be masked at the same locations.

Refer to [`numpy.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod "numpy.cumprod")
 for full documentation.

See also

[`numpy.ndarray.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.cumprod.html#numpy.ndarray.cumprod "numpy.ndarray.cumprod")

corresponding function for ndarrays

[`numpy.cumprod`](https://numpy.org/doc/stable/reference/generated/numpy.cumprod.html#numpy.cumprod "numpy.cumprod")

equivalent function

Notes

The mask is lost if _out_ is not a valid MaskedArray !

Arithmetic is modular when using integer types, and no error is raised on overflow.

On this page