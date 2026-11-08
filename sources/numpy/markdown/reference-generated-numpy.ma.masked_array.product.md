[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.product.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.product.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.product.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.product.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.product.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.product.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.product.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.product.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.product.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.product.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.product.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.product.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.product.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.product.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.product.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.product.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.product.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.product.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.product.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.product.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.product.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.product.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.product[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.product.html#numpy-ma-masked-array-product "Link to this heading")

============================================================================================================================================================================

method

ma.masked\_array.product(_axis=None_, _dtype=None_, _out=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5303-L5342)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.product.html#numpy.ma.masked_array.product "Link to this definition")

Return the product of the array elements over the given axis.

Masked elements are set to 1 internally for computation.

Refer to [`numpy.prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod")
 for full documentation.

See also

[`numpy.ndarray.prod`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.prod.html#numpy.ndarray.prod "numpy.ndarray.prod")

corresponding function for ndarrays

[`numpy.prod`](https://numpy.org/doc/stable/reference/generated/numpy.prod.html#numpy.prod "numpy.prod")

equivalent function

Notes

Arithmetic is modular when using integer types, and no error is raised on overflow.

On this page