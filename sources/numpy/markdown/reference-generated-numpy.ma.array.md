[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.array.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.array.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.array.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.array.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.array.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.array.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.array.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.array.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.array.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.array.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.array.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.array.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.array.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.array.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.array.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.array.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.array.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.array.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.array.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.array.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.array.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.array.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.array[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.array.html#numpy-ma-array "Link to this heading")

==============================================================================================================================

ma.array(_data_, _dtype\=None_, _copy\=False_, _order\=None_, _mask\=np.False\__, _fill\_value\=None_, _keep\_mask\=True_, _hard\_mask\=False_, _shrink\=True_, _subok\=True_, _ndmin\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L6859-L6872)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.array.html#numpy.ma.array "Link to this definition")

An array class with possibly masked values.

Masked values of True exclude the corresponding element from any computation.

Construction:

x \= MaskedArray(data, mask\=nomask, dtype\=None, copy\=False, subok\=True,
                ndmin\=0, fill\_value\=None, keep\_mask\=True, hard\_mask\=None,
                shrink\=True, order\=None)

Copy to clipboard

Parameters:

**data**array\_like

Input data.

**mask**sequence, optional

Mask. Must be convertible to an array of booleans with the same shape as _data_. True indicates a masked (i.e. invalid) data.

**dtype**dtype, optional

Data type of the output. If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is None, the type of the data argument (`data.dtype`) is used. If [`dtype`](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype")
 is not None and different from `data.dtype`, a copy is performed.

**copy**bool, optional

Whether to copy the input data (True), or to use a reference instead. Default is False.

**subok**bool, optional

Whether to return a subclass of [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
 if possible (True) or a plain [`MaskedArray`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray")
. Default is True.

**ndmin**int, optional

Minimum number of dimensions. Default is 0.

**fill\_value**scalar, optional

Value used to fill in the masked values when necessary. If None, a default based on the data-type is used.

**keep\_mask**bool, optional

Whether to combine _mask_ with the mask of the input data, if any (True), or to use only _mask_ for the output (False). Default is True.

**hard\_mask**bool, optional

Whether to use a hard mask or not. With a hard mask, masked values cannot be unmasked. Default is False.

**shrink**bool, optional

Whether to force compression of an empty mask. Default is True.

**order**{‘C’, ‘F’, ‘A’}, optional

Specify the order of the array. If order is ‘C’, then the array will be in C-contiguous order (last-index varies the fastest). If order is ‘F’, then the returned array will be in Fortran-contiguous order (first-index varies the fastest). If order is ‘A’ (default), then the returned array may be in any order (either C-, Fortran-contiguous, or even discontiguous), unless a copy is required, in which case it will be C-contiguous.

Examples

Try it in your browser!

\>>> import numpy as np

Copy to clipboard

The `mask` can be initialized with an array of boolean values with the same shape as `data`.

\>>> data \= np.arange(6).reshape((2, 3))
\>>> np.ma.MaskedArray(data, mask\=\[\[False, True, False\],\
...                               \[False, False, True\]\])
masked\_array(
  data=\[\[0, --, 2\],\
        \[3, 4, --\]\],
  mask=\[\[False,  True, False\],\
        \[False, False,  True\]\],
  fill\_value=999999)

Copy to clipboard

Alternatively, the `mask` can be initialized to homogeneous boolean array with the same shape as `data` by passing in a scalar boolean value:

\>>> np.ma.MaskedArray(data, mask\=False)
masked\_array(
  data=\[\[0, 1, 2\],\
        \[3, 4, 5\]\],
  mask=\[\[False, False, False\],\
        \[False, False, False\]\],
  fill\_value=999999)

Copy to clipboard

\>>> np.ma.MaskedArray(data, mask\=True)
masked\_array(
  data=\[\[--, --, --\],\
        \[--, --, --\]\],
  mask=\[\[ True,  True,  True\],\
        \[ True,  True,  True\]\],
  fill\_value=999999,
  dtype=int64)

Copy to clipboard

Note

The recommended practice for initializing `mask` with a scalar boolean value is to use `True`/`False` rather than `np.True_`/`np.False_`. The reason is [`nomask`](https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#numpy.ma.nomask "numpy.ma.nomask")
 is represented internally as `np.False_`.

\>>> np.False\_ is np.ma.nomask
True

Copy to clipboard

Go BackOpen In Tab

On this page