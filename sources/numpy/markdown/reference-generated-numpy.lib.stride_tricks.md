[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.lib.stride_tricks.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.lib.stride_tricks.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.lib.stride_tricks.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.lib.stride_tricks.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.lib.stride_tricks.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.lib.stride_tricks.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.lib.stride_tricks.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.lib.stride_tricks.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.lib.stride_tricks.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.lib.stride_tricks.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.lib.stride_tricks.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.lib.stride_tricks.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.lib.stride_tricks.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.lib.stride_tricks.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.lib.stride_tricks.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.lib.stride_tricks.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.lib.stride_tricks.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.lib.stride_tricks.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.lib.stride_tricks.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.lib.stride_tricks.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.lib.stride\_tricks[#](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.html#module-numpy.lib.stride_tricks "Link to this heading")

=================================================================================================================================================================

Utilities that manipulate strides to achieve desirable effects.

An explanation of strides can be found in the [The N-dimensional array (ndarray)](https://numpy.org/doc/stable/reference/arrays.ndarray.html#arrays-ndarray)
.

Functions

|     |     |
| --- | --- |
| [`as_strided`](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.as_strided.html#numpy.lib.stride_tricks.as_strided "numpy.lib.stride_tricks.as_strided")<br>(x\[, shape, strides, subok, ...\]) | Create a view into the array with the given shape and strides. |
| [`sliding_window_view`](https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html#numpy.lib.stride_tricks.sliding_window_view "numpy.lib.stride_tricks.sliding_window_view")<br>(x, window\_shape\[, axis, ...\]) | Create a sliding window view into the array with the given window shape. |