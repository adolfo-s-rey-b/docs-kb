[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ptp[#](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy-ptp "Link to this heading")

===============================================================================================================

numpy.ptp(_a_, _axis=None_, _out=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L2959-L3041)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "Link to this definition")

Range of values (maximum - minimum) along an axis.

The name of the function comes from the acronym for ‘peak to peak’.

Warning

[`ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")
 preserves the data type of the array. This means the return value for an input of signed integers with n bits (e.g. [`numpy.int8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int8 "numpy.int8")
, [`numpy.int16`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int16 "numpy.int16")
, etc) is also a signed integer with n bits. In that case, peak-to-peak values greater than `2**(n-1)-1` will be returned as negative values. An example with a work-around is shown below.

Parameters:

**a**array\_like

Input values.

**axis**None or int or tuple of ints, optional

Axis along which to find the peaks. By default, flatten the array. _axis_ may be negative, in which case it counts from the last to the first axis. If this is a tuple of ints, a reduction is performed on multiple axes, instead of a single axis or all the axes as before.

**out**array\_like

Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output, but the type of the output values will be cast if necessary.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the input array.

If the default value is passed, then _keepdims_ will not be passed through to the [`ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")
 method of sub-classes of [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, however any non-default value will be. If the sub-class’ method does not implement _keepdims_ any exceptions will be raised.

Returns:

**ptp**ndarray or scalar

The range of a given array - _scalar_ if array is one-dimensional or a new array holding the result along the given axis

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[\[4, 9, 2, 10\],\
...               \[6, 9, 7, 12\]\])

Copy to clipboard

\>>> np.ptp(x, axis\=1)
array(\[8, 6\])

Copy to clipboard

\>>> np.ptp(x, axis\=0)
array(\[2, 0, 5, 2\])

Copy to clipboard

\>>> np.ptp(x)
10

Copy to clipboard

This example shows that a negative value can be returned when the input is an array of signed integers.

\>>> y \= np.array(\[\[1, 127\],\
...               \[0, 127\],\
...               \[\-1, 127\],\
...               \[\-2, 127\]\], dtype\=np.int8)
\>>> np.ptp(y, axis\=1)
array(\[ 126,  127, -128, -127\], dtype=int8)

Copy to clipboard

A work-around is to use the _view()_ method to view the result as unsigned integers with the same bit width:

\>>> np.ptp(y, axis\=1).view(np.uint8)
array(\[126, 127, 128, 129\], dtype=uint8)

Copy to clipboard

Go BackOpen In Tab

On this page