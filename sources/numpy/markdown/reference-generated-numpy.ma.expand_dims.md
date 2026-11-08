[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.expand_dims.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.expand\_dims[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.expand_dims.html#numpy-ma-expand-dims "Link to this heading")

=================================================================================================================================================

ma.expand\_dims(_a_, _axis_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L513-L600)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.expand_dims.html#numpy.ma.expand_dims "Link to this definition")

Expand the shape of an array.

Insert a new axis that will appear at the _axis_ position in the expanded array shape.

Parameters:

**a**array\_like

Input array.

**axis**int or tuple of ints

Position in the expanded axes where the new axis (or axes) is placed.

Deprecated since version 1.13.0: Passing an axis where `axis > a.ndim` will be treated as `axis == a.ndim`, and passing `axis < -a.ndim - 1` will be treated as `axis == 0`. This behavior is deprecated.

Returns:

**result**ndarray

View of _a_ with the number of dimensions increased.

See also

[`squeeze`](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze "numpy.squeeze")

The inverse operation, removing singleton dimensions

[`reshape`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape")

Insert, remove, and combine dimensions, and resize existing ones

[`atleast_1d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_1d.html#numpy.atleast_1d "numpy.atleast_1d")
, [`atleast_2d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d "numpy.atleast_2d")
, [`atleast_3d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_3d.html#numpy.atleast_3d "numpy.atleast_3d")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2\])
\>>> x.shape
(2,)

Copy to clipboard

The following is equivalent to `x[np.newaxis, :]` or `x[np.newaxis]`:

\>>> y \= np.expand\_dims(x, axis\=0)
\>>> y
array(\[\[1, 2\]\])
\>>> y.shape
(1, 2)

Copy to clipboard

The following is equivalent to `x[:, np.newaxis]`:

\>>> y \= np.expand\_dims(x, axis\=1)
\>>> y
array(\[\[1\],\
       \[2\]\])
\>>> y.shape
(2, 1)

Copy to clipboard

`axis` may also be a tuple:

\>>> y \= np.expand\_dims(x, axis\=(0, 1))
\>>> y
array(\[\[\[1, 2\]\]\])

Copy to clipboard

\>>> y \= np.expand\_dims(x, axis\=(2, 0))
\>>> y
array(\[\[\[1\],\
        \[2\]\]\])

Copy to clipboard

Note that some examples may use `None` instead of `np.newaxis`. These are the same objects:

\>>> np.newaxis is None
True

Copy to clipboard

Go BackOpen In Tab

On this page