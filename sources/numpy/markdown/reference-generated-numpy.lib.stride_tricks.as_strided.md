[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.stride_tricks.as_strided.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.stride_tricks.as_strided.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.stride\_tricks.as\_strided[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html#numpy-lib-stride-tricks-as-strided "Link to this heading")

============================================================================================================================================================================================

lib.stride\_tricks.as\_strided(_x_, _shape\=None_, _strides\=None_, _subok\=False_, _writeable\=True_, _\*_, _check\_bounds\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_stride_tricks_impl.py#L38-L169)
[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html#numpy.lib.stride_tricks.as_strided "Link to this definition")

Create a view into the array with the given shape and strides.

Warning

This function has to be used with extreme care, see notes.

Parameters:

**x**ndarray

Array to create a new.

**shape**sequence of int, optional

The shape of the new array. Defaults to `x.shape`.

**strides**sequence of int, optional

The strides of the new array. Defaults to `x.strides`.

**subok**bool, optional

If True, subclasses are preserved.

**writeable**bool, optional

If set to False, the returned array will always be readonly. Otherwise it will be writable if the original array was. It is advisable to set this to False if possible (see Notes).

**check\_bounds**bool or None

Check new stride and shape for potential out of bound memory access.

Returns:

**view**ndarray

Raises:

ValueError

If _check\_bounds_ is True the given shape and strides could result in out-of-bounds memory access.

See also

[`broadcast_to`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to "numpy.broadcast_to")

broadcast an array to a given shape.

[`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")

reshape an array.

[`lib.stride_tricks.sliding_window_view`](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html#numpy.lib.stride_tricks.sliding_window_view "numpy.lib.stride_tricks.sliding_window_view")

userfriendly and safe function for a creation of sliding window views.

Notes

[`as_strided`](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html#numpy.lib.stride_tricks.as_strided "numpy.lib.stride_tricks.as_strided")
 creates a view into the array given the exact strides and shape. This means it manipulates the internal data structure of ndarray and, if done incorrectly, the array elements can point to invalid memory and can corrupt results or crash your program. It is advisable to always use the original `x.strides` when calculating new strides to avoid reliance on a contiguous memory layout.

Furthermore, arrays created with this function often contain self overlapping memory, so that two elements are identical. Vectorized write operations on such arrays will typically be unpredictable. They may even give different results for small, large, or transposed arrays.

Since writing to these arrays has to be tested and done with great care, you may want to use `writeable=False` to avoid accidental write operations.

For these reasons it is advisable to avoid [`as_strided`](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html#numpy.lib.stride_tricks.as_strided "numpy.lib.stride_tricks.as_strided")
 when possible.

Examples

Try it in your browser!

\>>> import numpy as np
... from numpy.lib.stride\_tricks import as\_strided
... x \= np.arange(10)
... y \= as\_strided(x, shape\=(5,), strides\=(8,), check\_bounds\=True)
... y
array(\[0, 1, 2, 3, 4\])

Copy to clipboard

Attempting to create an out-of-bounds view and use `check_bounds=True` as\_strided will raises an error:

\>>> as\_strided(x, shape\=(20,), strides\=(8,), check\_bounds\=True)
Traceback (most recent call last):
...
ValueError: Given shape and strides would access memory out of bounds...

Copy to clipboard

When working with views, bounds are checked against the base array:

\>>> a \= np.arange(1000)
... b \= a\[:2\]
... c \= as\_strided(b, shape\=(2,), strides\=(400,), check\_bounds\=True)
... c\[0\], c\[1\]
(0, 50)

Copy to clipboard

Go BackOpen In Tab

On this page