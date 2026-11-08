[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.stride\_tricks.sliding\_window\_view[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html#numpy-lib-stride-tricks-sliding-window-view "Link to this heading")

========================================================================================================================================================================================================================

lib.stride\_tricks.sliding\_window\_view(_x_, _window\_shape_, _axis\=None_, _\*_, _subok\=False_, _writeable\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_stride_tricks_impl.py#L177-L444)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html#numpy.lib.stride_tricks.sliding_window_view "Link to this definition")

Create a sliding window view into the array with the given window shape.

Also known as rolling or moving window, the window slides across all dimensions of the array and extracts subsets of the array at all window positions.

New in version 1.20.0.

Parameters:

**x**array\_like

Array to create the sliding window view from.

**window\_shape**int or tuple of int

Size of window over each axis that takes part in the sliding window. If _axis_ is not present, must have same length as the number of input array dimensions. Single integers _i_ are treated as if they were the tuple _(i,)_.

**axis**int or tuple of int, optional

Axis or axes along which the sliding window is applied. By default, the sliding window is applied to all axes and _window\_shape\[i\]_ will refer to axis _i_ of _x_. If _axis_ is given as a _tuple of int_, _window\_shape\[i\]_ will refer to the axis _axis\[i\]_ of _x_. Single integers _i_ are treated as if they were the tuple _(i,)_.

**subok**bool, optional

If True, sub-classes will be passed-through, otherwise the returned array will be forced to be a base-class array (default).

**writeable**bool, optional

When true, allow writing to the returned view. The default is false, as this should be used with caution: the returned view contains the same memory location multiple times, so writing to one location will cause others to change.

Returns:

**view**ndarray

Sliding window view of the array. The sliding window dimensions are inserted at the end, and the original dimensions are trimmed as required by the size of the sliding window. That is, `view.shape = x_shape_trimmed + window_shape`, where `x_shape_trimmed` is `x.shape` with every entry reduced by one less than the corresponding window size.

See also

[`lib.stride_tricks.as_strided`](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html#numpy.lib.stride_tricks.as_strided "numpy.lib.stride_tricks.as_strided")

A lower-level and less safe routine for creating arbitrary views from custom shape and strides. Use the `check_bounds` parameter for bounds validation.

[`broadcast_to`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to "numpy.broadcast_to")

broadcast an array to a given shape.

Notes

Warning

This function creates views with overlapping memory. When `writeable=True`, writing to the view will modify the original array and may affect multiple view positions. See the examples below and [this guide](https://numpy.org/doc/stable/user/basics.copies.html)
 about the difference between copies and views.

For many applications using a sliding window view can be convenient, but potentially very slow. Often specialized solutions exist, for example:

*   [`scipy.signal.fftconvolve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.fftconvolve.html#scipy.signal.fftconvolve "(in SciPy v1.18.0)")
    
*   filtering functions in [`scipy.ndimage`](https://docs.scipy.org/doc/scipy/reference/ndimage.html#module-scipy.ndimage "(in SciPy v1.18.0)")
    
*   moving window functions provided by [bottleneck](https://github.com/pydata/bottleneck)
    .
    

As a rough estimate, a sliding window approach with an input size of _N_ and a window size of _W_ will scale as _O(N\*W)_ where frequently a special algorithm can achieve _O(N)_. That means that the sliding window variant for a window size of 100 can be a 100 times slower than a more specialized version.

Nevertheless, for small window sizes, when no custom algorithm exists, or as a prototyping and developing tool, this function can be a good solution.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> from numpy.lib.stride\_tricks import sliding\_window\_view
\>>> x \= np.arange(6)
\>>> x.shape
(6,)
\>>> v \= sliding\_window\_view(x, 3)
\>>> v.shape
(4, 3)
\>>> v
array(\[\[0, 1, 2\],\
       \[1, 2, 3\],\
       \[2, 3, 4\],\
       \[3, 4, 5\]\])

Copy to clipboard

This also works in more dimensions, e.g.

\>>> i, j \= np.ogrid\[:3, :4\]
\>>> x \= 10\*i + j
\>>> x.shape
(3, 4)
\>>> x
array(\[\[ 0,  1,  2,  3\],\
       \[10, 11, 12, 13\],\
       \[20, 21, 22, 23\]\])
\>>> shape \= (2,2)
\>>> v \= sliding\_window\_view(x, shape)
\>>> v.shape
(2, 3, 2, 2)
\>>> v
array(\[\[\[\[ 0,  1\],\
         \[10, 11\]\],\
        \[\[ 1,  2\],\
         \[11, 12\]\],\
        \[\[ 2,  3\],\
         \[12, 13\]\]\],\
       \[\[\[10, 11\],\
         \[20, 21\]\],\
        \[\[11, 12\],\
         \[21, 22\]\],\
        \[\[12, 13\],\
         \[22, 23\]\]\]\])

Copy to clipboard

The axis can be specified explicitly:

\>>> v \= sliding\_window\_view(x, 3, 0)
\>>> v.shape
(1, 4, 3)
\>>> v
array(\[\[\[ 0, 10, 20\],\
        \[ 1, 11, 21\],\
        \[ 2, 12, 22\],\
        \[ 3, 13, 23\]\]\])

Copy to clipboard

The same axis can be used several times. In that case, every use reduces the corresponding original dimension:

\>>> v \= sliding\_window\_view(x, (2, 3), (1, 1))
\>>> v.shape
(3, 1, 2, 3)
\>>> v
array(\[\[\[\[ 0,  1,  2\],\
         \[ 1,  2,  3\]\]\],\
       \[\[\[10, 11, 12\],\
         \[11, 12, 13\]\]\],\
       \[\[\[20, 21, 22\],\
         \[21, 22, 23\]\]\]\])

Copy to clipboard

Combining with stepped slicing (_::step_), this can be used to take sliding views which skip elements:

\>>> x \= np.arange(7)
\>>> sliding\_window\_view(x, 5)\[:, ::2\]
array(\[\[0, 2, 4\],\
       \[1, 3, 5\],\
       \[2, 4, 6\]\])

Copy to clipboard

or views which move by multiple elements

\>>> x \= np.arange(7)
\>>> sliding\_window\_view(x, 3)\[::2, :\]
array(\[\[0, 1, 2\],\
       \[2, 3, 4\],\
       \[4, 5, 6\]\])

Copy to clipboard

A common application of [`sliding_window_view`](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html#numpy.lib.stride_tricks.sliding_window_view "numpy.lib.stride_tricks.sliding_window_view")
 is the calculation of running statistics. The simplest example is the [moving average](https://en.wikipedia.org/wiki/Moving_average)
:

\>>> x \= np.arange(6)
\>>> x.shape
(6,)
\>>> v \= sliding\_window\_view(x, 3)
\>>> v.shape
(4, 3)
\>>> v
array(\[\[0, 1, 2\],\
       \[1, 2, 3\],\
       \[2, 3, 4\],\
       \[3, 4, 5\]\])
\>>> moving\_average \= v.mean(axis\=-1)
\>>> moving\_average
array(\[1., 2., 3., 4.\])

Copy to clipboard

To adjust the step size of the sliding window, index the output view along the desired dimension(s). Using the array shown above:

\>>> v\[::2\]
array(\[\[0, 1, 2\],\
       \[2, 3, 4\]\])

Copy to clipboard

You can slide in the reverse direction using the same technique:

\>>> v\[::\-1\]
array(\[\[3, 4, 5\],\
       \[2, 3, 4\],\
       \[1, 2, 3\],\
       \[0, 1, 2\]\])

Copy to clipboard

The two examples below demonstrate the effect of `writeable=True`.

Creating a view with the default `writeable=False` and then writing to it raises an error.

\>>> v \= sliding\_window\_view(x, 3)
\>>> v\[0,1\] \= 10
Traceback (most recent call last):
...
ValueError: assignment destination is read-only

Copy to clipboard

Creating a view with `writeable=True` and then writing to it changes the original array and multiple view positions.

\>>> x \= np.arange(6)  \# reset x for the second example
\>>> v \= sliding\_window\_view(x, 3, writeable\=True)
\>>> v\[0,1\] \= 10
\>>> x
array(\[ 0, 10,  2,  3,  4,  5\])
\>>> v
array(\[\[ 0, 10,  2\],\
       \[10,  2,  3\],\
       \[ 2,  3,  4\],\
       \[ 3,  4,  5\]\])

Copy to clipboard

Note that a sliding window approach is often **not** optimal (see Notes).

Go BackOpen In Tab

On this page