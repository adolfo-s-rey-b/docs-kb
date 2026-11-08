[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.ptp.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.ptp.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.ptp.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.ptp.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.ptp.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.ptp.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.ptp.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.ptp.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.ptp.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.ptp.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.ptp.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.ptp.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.ptp.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.ptp.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.ptp.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.ptp.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.ptp.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.ptp.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.ptp.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.ptp.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.ptp.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.ptp.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.ptp[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.ptp.html#numpy-ma-ptp "Link to this heading")

========================================================================================================================

ma.ptp(_obj_, _axis=None_, _out=None_, _fill\_value=None_, _keepdims=<no value>_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/ma/core.py#L7034-L7042)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.ptp.html#numpy.ma.ptp "Link to this definition")

Return (maximum - minimum) along the given dimension (i.e. peak-to-peak value).

Warning

[`ptp`](https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp")
 preserves the data type of the array. This means the return value for an input of signed integers with n bits (e.g. _np.int8_, _np.int16_, etc) is also a signed integer with n bits. In that case, peak-to-peak values greater than `2**(n-1)-1` will be returned as negative values. An example with a work-around is shown below.

Parameters:

**axis**{None, int}, optional

Axis along which to find the peaks. If None (default) the flattened array is used.

**out**{None, array\_like}, optional

Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output but the type will be cast if necessary.

**fill\_value**scalar or None, optional

Value used to fill in the masked values.

**keepdims**bool, optional

If this is set to True, the axes which are reduced are left in the result as dimensions with size one. With this option, the result will broadcast correctly against the array.

Returns:

**ptp**ndarray.

A new array holding the result, unless `out` was specified, in which case a reference to `out` is returned.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.ma.MaskedArray(\[\[4, 9, 2, 10\],\
...                        \[6, 9, 7, 12\]\])

Copy to clipboard

\>>> x.ptp(axis\=1)
masked\_array(data=\[8, 6\],
             mask=False,
       fill\_value=999999)

Copy to clipboard

\>>> x.ptp(axis\=0)
masked\_array(data=\[2, 0, 5, 2\],
             mask=False,
       fill\_value=999999)

Copy to clipboard

\>>> x.ptp()
10

Copy to clipboard

This example shows that a negative value can be returned when the input is an array of signed integers.

\>>> y \= np.ma.MaskedArray(\[\[1, 127\],\
...                        \[0, 127\],\
...                        \[\-1, 127\],\
...                        \[\-2, 127\]\], dtype\=np.int8)
\>>> y.ptp(axis\=1)
masked\_array(data=\[ 126,  127, -128, -127\],
             mask=False,
       fill\_value=np.int64(999999),
            dtype=int8)

Copy to clipboard

A work-around is to use the _view()_ method to view the result as unsigned integers with the same bit width:

\>>> y.ptp(axis\=1).view(np.uint8)
masked\_array(data=\[126, 127, 128, 129\],
             mask=False,
       fill\_value=np.uint64(999999),
            dtype=uint8)

Copy to clipboard

Go BackOpen In Tab

On this page