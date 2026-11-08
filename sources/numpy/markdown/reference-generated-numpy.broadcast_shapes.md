[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_shapes.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.broadcast_shapes.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_shapes.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.broadcast_shapes.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.broadcast_shapes.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.broadcast_shapes.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.broadcast_shapes.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.broadcast_shapes.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.broadcast_shapes.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.broadcast_shapes.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.broadcast_shapes.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.broadcast_shapes.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.broadcast_shapes.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.broadcast_shapes.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.broadcast_shapes.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.broadcast_shapes.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.broadcast_shapes.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.broadcast_shapes.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.broadcast_shapes.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.broadcast_shapes.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.broadcast_shapes.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.broadcast_shapes.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.broadcast\_shapes[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_shapes.html#numpy-broadcast-shapes "Link to this heading")

=======================================================================================================================================================

numpy.broadcast\_shapes(_\*args_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_stride_tricks_impl.py#L540-L581)
[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_shapes.html#numpy.broadcast_shapes "Link to this definition")

Broadcast the input shapes into a single shape.

[Learn more about broadcasting here](https://numpy.org/doc/stable/user/basics.broadcasting.html#basics-broadcasting)
.

New in version 1.20.0.

Parameters:

**\*args**tuples of ints, or ints

The shapes to be broadcast against each other.

Returns:

tuple

Broadcasted shape.

Raises:

ValueError

If the shapes are not compatible and cannot be broadcast according to NumPy’s broadcasting rules.

See also

[`broadcast`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.html#numpy.broadcast "numpy.broadcast")

[`broadcast_arrays`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_arrays.html#numpy.broadcast_arrays "numpy.broadcast_arrays")

[`broadcast_to`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to "numpy.broadcast_to")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.broadcast\_shapes((1, 2), (3, 1), (3, 2))
(3, 2)

Copy to clipboard

\>>> np.broadcast\_shapes((6, 7), (5, 6, 1), (7,), (5, 1, 7))
(5, 6, 7)

Copy to clipboard

Go BackOpen In Tab

On this page