[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.mT.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.mT.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.mT.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.mT.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.mT.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.mT.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.mT.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.mT.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.mT.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.mT.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.mT.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.mT.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.mT.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.mT.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.mT.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.mT.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.mT.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.mT.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.mT.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.mT.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.mT.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.mT.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.mT[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.mT.html#numpy-ma-masked-array-mt "Link to this heading")

=============================================================================================================================================================

property

_property_ ma.masked\_array.mT[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.mT.html#numpy.ma.masked_array.mT "Link to this definition")

Return the matrix-transpose of the masked array.

The matrix transpose is the transpose of the last two dimensions, even if the array is of higher dimension.

New in version 2.0.

Returns:

result: MaskedArray

The masked array with the last two dimensions transposed

Raises:

ValueError

If the array is of dimension less than 2.

See also

[`ndarray.mT`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.mT.html#numpy.ndarray.mT "numpy.ndarray.mT")

Equivalent method for arrays

On this page