[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all_like.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_all_like.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all_like.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_all_like.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_all_like.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_all_like.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_all_like.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_all_like.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_all_like.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_all_like.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_all_like.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_all_like.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_all_like.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_all_like.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_all_like.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_all_like.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_all_like.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_all_like.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_all_like.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_all_like.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_all_like.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_all_like.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.masked\_all\_like[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all_like.html#numpy-ma-masked-all-like "Link to this heading")

==============================================================================================================================================================

ma.masked\_all\_like(_arr_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L181-L242)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all_like.html#numpy.ma.masked_all_like "Link to this definition")

Empty masked array with the properties of an existing array.

Return an empty masked array of the same shape and dtype as the array _arr_, where all the data are masked.

Parameters:

**arr**ndarray

An array describing the shape and dtype of the required MaskedArray.

Returns:

**a**MaskedArray

A masked array with all data masked.

Raises:

AttributeError

If _arr_ doesn’t have a shape attribute (i.e. not an ndarray)

See also

[`masked_all`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all.html#numpy.ma.masked_all "numpy.ma.masked_all")

Empty masked array with all elements masked.

Notes

Unlike other masked array creation functions (e.g. [`numpy.ma.zeros_like`](https://numpy.org/doc/stable/reference/generated/numpy.ma.zeros_like.html#numpy.ma.zeros_like "numpy.ma.zeros_like")
, [`numpy.ma.ones_like`](https://numpy.org/doc/stable/reference/generated/numpy.ma.ones_like.html#numpy.ma.ones_like "numpy.ma.ones_like")
, _numpy.ma.full\_like_), [`masked_all_like`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all_like.html#numpy.ma.masked_all_like "numpy.ma.masked_all_like")
 does not initialize the values of the array, and may therefore be marginally faster. However, the values stored in the newly allocated array are arbitrary. For reproducible behavior, be sure to set each element of the array before reading.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> arr \= np.zeros((2, 3), dtype\=np.float32)
\>>> arr
array(\[\[0., 0., 0.\],\
       \[0., 0., 0.\]\], dtype=float32)
\>>> np.ma.masked\_all\_like(arr)
masked\_array(
  data=\[\[--, --, --\],\
        \[--, --, --\]\],
  mask=\[\[ True,  True,  True\],\
        \[ True,  True,  True\]\],
  fill\_value=np.float64(1e+20),
  dtype=float32)

Copy to clipboard

The dtype of the masked array matches the dtype of _arr_.

\>>> arr.dtype
dtype('float32')
\>>> np.ma.masked\_all\_like(arr).dtype
dtype('float32')

Copy to clipboard

Go BackOpen In Tab

On this page