[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.average.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.average.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.average.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.average.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.average.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.average.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.average.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.average.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.average.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.average.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.average.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.average.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.average.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.average.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.average.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.average.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.average.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.average.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.average.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.average.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.average.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.average.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.average[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.average.html#numpy-ma-average "Link to this heading")

====================================================================================================================================

ma.average(_a_, _axis=None_, _weights=None_, _returned=False_, _\*_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/extras.py#L510-L675)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.average.html#numpy.ma.average "Link to this definition")

Return the weighted average of array over the given axis.

Parameters:

**a**array\_like

Data to be averaged. Masked entries are not taken into account in the computation.

**axis**None or int or tuple of ints, optional

Axis or axes along which to average _a_. The default, _axis=None_, will average over all of the elements of the input array. If axis is a tuple of ints, averaging is performed on all of the axes specified in the tuple instead of a single axis or all the axes as before.

**weights**array\_like, optional

An array of weights associated with the values in _a_. Each value in _a_ contributes to the average according to its associated weight. The array of weights must be the same shape as _a_ if no axis is specified, otherwise the weights must have dimensions and shape consistent with _a_ along the specified axis. If _weights=None_, then all data in _a_ are assumed to have a weight equal to one. The calculation is:

avg \= sum(a \* weights) / sum(weights)

Copy to clipboard

where the sum is over all included elements. The only constraint on the values of _weights_ is that _sum(weights)_ must not be 0.

**returned**bool, optional

Flag indicating whether a tuple `(result, sum of weights)` should be returned as output (True), or just the result (False). Default is False.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original _a_. _Note:_ _keepdims_ will not work with instances of [`numpy.matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 or other classes whose methods do not support _keepdims_.

New in version 1.23.0.

Returns:

**average, \[sum\_of\_weights\]**(tuple of) scalar or MaskedArray

The average along the specified axis. When returned is _True_, return a tuple with the average as the first element and the sum of the weights as the second element. The return type is _np.float64_ if _a_ is of integer type and floats smaller than [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, or the input data-type, otherwise. If returned, _sum\_of\_weights_ is always [`float64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
.

Raises:

ZeroDivisionError

When all weights along axis are zero. See [`numpy.ma.average`](https://numpy.org/doc/stable/reference/generated/numpy.ma.average.html#numpy.ma.average "numpy.ma.average")
 for a version robust to this type of error.

TypeError

When _weights_ does not have the same shape as _a_, and _axis=None_.

ValueError

When _weights_ does not have dimensions and shape consistent with _a_ along specified _axis_.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.ma.array(\[1., 2., 3., 4.\], mask\=\[False, False, True, True\])
\>>> np.ma.average(a, weights\=\[3, 1, 0, 0\])
1.25

Copy to clipboard

\>>> x \= np.ma.arange(6.).reshape(3, 2)
\>>> x
masked\_array(
  data=\[\[0., 1.\],\
        \[2., 3.\],\
        \[4., 5.\]\],
  mask=False,
  fill\_value=1e+20)
\>>> data \= np.arange(8).reshape((2, 2, 2))
\>>> data
array(\[\[\[0, 1\],\
        \[2, 3\]\],\
       \[\[4, 5\],\
        \[6, 7\]\]\])
\>>> np.ma.average(data, axis\=(0, 1), weights\=\[\[1./4, 3./4\], \[1., 1./2\]\])
masked\_array(data=\[3.4, 4.4\],
         mask=\[False, False\],
   fill\_value=1e+20)
\>>> np.ma.average(data, axis\=0, weights\=\[\[1./4, 3./4\], \[1., 1./2\]\])
Traceback (most recent call last):
    ...
ValueError: Shape of weights must be consistent
with shape of a along specified axis.

Copy to clipboard

\>>> avg, sumweights \= np.ma.average(x, axis\=0, weights\=\[1, 2, 3\],
...                                 returned\=True)
\>>> avg
masked\_array(data=\[2.6666666666666665, 3.6666666666666665\],
             mask=\[False, False\],
       fill\_value=1e+20)

Copy to clipboard

With `keepdims=True`, the following result has shape (3, 1).

\>>> np.ma.average(x, axis\=1, keepdims\=True)
masked\_array(
  data=\[\[0.5\],\
        \[2.5\],\
        \[4.5\]\],
  mask=False,
  fill\_value=1e+20)

Copy to clipboard

Go BackOpen In Tab

On this page