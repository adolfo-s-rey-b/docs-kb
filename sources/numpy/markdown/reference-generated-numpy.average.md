[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.average.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.average.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.average.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.average.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.average.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.average.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.average.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.average.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.average.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.average.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.average.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.average.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.average.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.average.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.average.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.average.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.average.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.average.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.average.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.average.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.average.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.average.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.average[#](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy-average "Link to this heading")

===========================================================================================================================

numpy.average(_a_, _axis=None_, _weights=None_, _returned=False_, _\*_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L450-L611)
[#](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "Link to this definition")

Compute the weighted average along the specified axis.

Parameters:

**a**array\_like

Array containing data to be averaged. If _a_ is not an array, a conversion is attempted.

**axis**None or int or tuple of ints, optional

Axis or axes along which to average _a_. The default, _axis=None_, will average over all of the elements of the input array. If axis is negative it counts from the last to the first axis. If axis is a tuple of ints, averaging is performed on all of the axes specified in the tuple instead of a single axis or all the axes as before.

**weights**array\_like, optional

An array of weights associated with the values in _a_. Each value in _a_ contributes to the average according to its associated weight. The array of weights must be the same shape as _a_ if no axis is specified, otherwise the weights must have dimensions and shape consistent with _a_ along the specified axis. If _weights=None_, then all data in _a_ are assumed to have a weight equal to one. The calculation is:

avg \= sum(a \* weights) / sum(weights)

Copy to clipboard

where the sum is over all included elements. The only constraint on the values of _weights_ is that _sum(weights)_ must not be 0.

**returned**bool, optional

Default is _False_. If _True_, the tuple ([`average`](https://numpy.org/doc/stable/reference/generated/numpy.average.html#numpy.average "numpy.average")
, _sum\_of\_weights_) is returned, otherwise only the average is returned. If _weights=None_, _sum\_of\_weights_ is equivalent to the number of elements over which the average is taken.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the original _a_. _Note:_ _keepdims_ will not work with instances of [`numpy.matrix`](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html#numpy.matrix "numpy.matrix")
 or other classes whose methods do not support _keepdims_.

New in version 1.23.0.

Returns:

**retval, \[sum\_of\_weights\]**array\_type or double

Return the average along the specified axis. When _returned_ is _True_, return a tuple with the average as the first element and the sum of the weights as the second element. _sum\_of\_weights_ is of the same type as _retval_. The result dtype follows a general pattern. If _weights_ is None, the result dtype will be that of _a_ , or `float64` if _a_ is integral. Otherwise, if _weights_ is not None and _a_ is non- integral, the result type will be the type of lowest precision capable of representing values of both _a_ and _weights_. If _a_ happens to be integral, the previous rules still applies but the result dtype will at least be `float64`.

Raises:

ZeroDivisionError

When all weights along axis are zero. See [`numpy.ma.average`](https://numpy.org/doc/stable/reference/generated/numpy.ma.average.html#numpy.ma.average "numpy.ma.average")
 for a version robust to this type of error.

TypeError

When _weights_ does not have the same shape as _a_, and _axis=None_.

ValueError

When _weights_ does not have dimensions and shape consistent with _a_ along specified _axis_.

See also

[`mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "numpy.mean")

[`ma.average`](https://numpy.org/doc/stable/reference/generated/numpy.ma.average.html#numpy.ma.average "numpy.ma.average")

average for masked arrays – useful if your data contains “missing” values

[`numpy.result_type`](https://numpy.org/doc/stable/reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type")

Returns the type that results from applying the numpy type promotion rules to the arguments.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> data \= np.arange(1, 5)
\>>> data
array(\[1, 2, 3, 4\])
\>>> np.average(data)
2.5
\>>> np.average(np.arange(1, 11), weights\=np.arange(10, 0, \-1))
4.0

Copy to clipboard

\>>> data \= np.arange(6).reshape((3, 2))
\>>> data
array(\[\[0, 1\],\
       \[2, 3\],\
       \[4, 5\]\])
\>>> np.average(data, axis\=1, weights\=\[1./4, 3./4\])
array(\[0.75, 2.75, 4.75\])
\>>> np.average(data, weights\=\[1./4, 3./4\])
Traceback (most recent call last):
    ...
TypeError: Axis must be specified when shapes of a and weights differ.

Copy to clipboard

With `keepdims=True`, the following result has shape (3, 1).

\>>> np.average(data, axis\=1, keepdims\=True)
array(\[\[0.5\],\
       \[2.5\],\
       \[4.5\]\])

Copy to clipboard

\>>> data \= np.arange(8).reshape((2, 2, 2))
\>>> data
array(\[\[\[0, 1\],\
        \[2, 3\]\],\
       \[\[4, 5\],\
        \[6, 7\]\]\])
\>>> np.average(data, axis\=(0, 1), weights\=\[\[1./4, 3./4\], \[1., 1./2\]\])
array(\[3.4, 4.4\])
\>>> np.average(data, axis\=0, weights\=\[\[1./4, 3./4\], \[1., 1./2\]\])
Traceback (most recent call last):
    ...
ValueError: Shape of weights must be consistent
with shape of a along specified axis.

Copy to clipboard

Go BackOpen In Tab

On this page