[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_all.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_all.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_all.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_all.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_all.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_all.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_all.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_all.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_all.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_all.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_all.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_all.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_all.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_all.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_all.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_all.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_all.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_all.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_all.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_all.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.masked\_all[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all.html#numpy-ma-masked-all "Link to this heading")

==============================================================================================================================================

ma.masked\_all(_shape_, _dtype=<class 'float'>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L120-L178)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all.html#numpy.ma.masked_all "Link to this definition")

Empty masked array with all elements masked.

Return an empty masked array of the given shape and dtype, where all the data are masked.

Parameters:

**shape**int or tuple of ints

Shape of the required MaskedArray, e.g., `(2, 3)` or `2`.

**dtype**dtype, optional

Data type of the output.

Returns:

**a**MaskedArray

A masked array with all data masked.

See also

[`masked_all_like`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all_like.html#numpy.ma.masked_all_like "numpy.ma.masked_all_like")

Empty masked array modelled on an existing array.

Notes

Unlike other masked array creation functions (e.g. [`numpy.ma.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.ma.zeros.html#numpy.ma.zeros "numpy.ma.zeros")
, [`numpy.ma.ones`](https://numpy.org/doc/stable/reference/generated/numpy.ma.ones.html#numpy.ma.ones "numpy.ma.ones")
, _numpy.ma.full_), [`masked_all`](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_all.html#numpy.ma.masked_all "numpy.ma.masked_all")
 does not initialize the values of the array, and may therefore be marginally faster. However, the values stored in the newly allocated array are arbitrary. For reproducible behavior, be sure to set each element of the array before reading.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.ma.masked\_all((3, 3))
masked\_array(
  data=\[\[--, --, --\],\
        \[--, --, --\],\
        \[--, --, --\]\],
  mask=\[\[ True,  True,  True\],\
        \[ True,  True,  True\],\
        \[ True,  True,  True\]\],
  fill\_value=1e+20,
  dtype=float64)

Copy to clipboard

The [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 parameter defines the underlying data type.

\>>> a \= np.ma.masked\_all((3, 3))
\>>> a.dtype
dtype('float64')
\>>> a \= np.ma.masked\_all((3, 3), dtype\=np.int32)
\>>> a.dtype
dtype('int32')

Copy to clipboard

Go BackOpen In Tab

On this page