[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.nonzero.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.masked_array.nonzero.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.nonzero.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.masked_array.nonzero.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.masked_array.nonzero.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.masked_array.nonzero.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.masked_array.nonzero.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.masked_array.nonzero.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.masked_array.nonzero.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.nonzero[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.nonzero.html#numpy-ma-masked-array-nonzero "Link to this heading")

============================================================================================================================================================================

method

ma.masked\_array.nonzero()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L5049-L5146)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.nonzero.html#numpy.ma.masked_array.nonzero "Link to this definition")

Return the indices of unmasked elements that are not zero.

Returns a tuple of arrays, one for each dimension, containing the indices of the non-zero elements in that dimension. The corresponding non-zero values can be obtained with:

a\[a.nonzero()\]

Copy to clipboard

To group the indices by element, rather than dimension, use instead:

np.transpose(a.nonzero())

Copy to clipboard

The result of this is always a 2d array, with a row for each non-zero element.

Parameters:

**None**

Returns:

**tuple\_of\_arrays**tuple

Indices of elements that are non-zero.

See also

[`numpy.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")

Function operating on ndarrays.

[`flatnonzero`](https://numpy.org/doc/stable/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero")

Return indices that are non-zero in the flattened version of the input array.

[`numpy.ndarray.nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.nonzero.html#numpy.ndarray.nonzero "numpy.ndarray.nonzero")

Equivalent ndarray method.

[`count_nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.count_nonzero.html#numpy.count_nonzero "numpy.count_nonzero")

Counts the number of non-zero elements in the input array.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> import numpy.ma as ma
\>>> x \= ma.array(np.eye(3))
\>>> x
masked\_array(
  data=\[\[1., 0., 0.\],\
        \[0., 1., 0.\],\
        \[0., 0., 1.\]\],
  mask=False,
  fill\_value=1e+20)
\>>> x.nonzero()
(array(\[0, 1, 2\]), array(\[0, 1, 2\]))

Copy to clipboard

Masked elements are ignored.

\>>> x\[1, 1\] \= ma.masked
\>>> x
masked\_array(
  data=\[\[1.0, 0.0, 0.0\],\
        \[0.0, --, 0.0\],\
        \[0.0, 0.0, 1.0\]\],
  mask=\[\[False, False, False\],\
        \[False,  True, False\],\
        \[False, False, False\]\],
  fill\_value=1e+20)
\>>> x.nonzero()
(array(\[0, 2\]), array(\[0, 2\]))

Copy to clipboard

Indices can also be grouped by element.

\>>> np.transpose(x.nonzero())
array(\[\[0, 0\],\
       \[2, 2\]\])

Copy to clipboard

A common use for `nonzero` is to find the indices of an array, where a condition is True. Given an array _a_, the condition _a_ > 3 is a boolean array and since False is interpreted as 0, ma.nonzero(a > 3) yields the indices of the _a_ where the condition is true.

\>>> a \= ma.array(\[\[1,2,3\],\[4,5,6\],\[7,8,9\]\])
\>>> a \> 3
masked\_array(
  data=\[\[False, False, False\],\
        \[ True,  True,  True\],\
        \[ True,  True,  True\]\],
  mask=False,
  fill\_value=True)
\>>> ma.nonzero(a \> 3)
(array(\[1, 1, 1, 2, 2, 2\]), array(\[0, 1, 2, 0, 1, 2\]))

Copy to clipboard

The `nonzero` method of the condition array can also be called.

\>>> (a \> 3).nonzero()
(array(\[1, 1, 1, 2, 2, 2\]), array(\[0, 1, 2, 0, 1, 2\]))

Copy to clipboard

Go BackOpen In Tab

On this page