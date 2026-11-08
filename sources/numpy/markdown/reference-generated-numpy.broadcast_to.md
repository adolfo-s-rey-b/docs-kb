[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.broadcast_to.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.broadcast_to.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.broadcast_to.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.broadcast_to.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.broadcast_to.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.broadcast_to.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.broadcast_to.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.broadcast_to.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.broadcast_to.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.broadcast_to.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.broadcast_to.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.broadcast_to.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.broadcast_to.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.broadcast_to.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.broadcast_to.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.broadcast_to.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.broadcast_to.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.broadcast_to.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.broadcast_to.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.broadcast_to.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.broadcast\_to[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy-broadcast-to "Link to this heading")

===========================================================================================================================================

numpy.broadcast\_to(_array_, _shape_, _subok\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_stride_tricks_impl.py#L474-L517)
[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to "Link to this definition")

Broadcast an array to a new shape.

Parameters:

**array**array\_like

The array to broadcast.

**shape**tuple or int

The shape of the desired array. A single integer `i` is interpreted as `(i,)`.

**subok**bool, optional

If True, then sub-classes will be passed-through, otherwise the returned array will be forced to be a base-class array (default).

Returns:

**broadcast**array

A readonly view on the original array with the given shape. It is typically not contiguous. Furthermore, more than one element of a broadcasted array may refer to a single memory location.

Raises:

ValueError

If the array is not compatible with the new shape according to NumPy’s broadcasting rules.

See also

[`broadcast`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.html#numpy.broadcast "numpy.broadcast")

[`broadcast_arrays`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_arrays.html#numpy.broadcast_arrays "numpy.broadcast_arrays")

[`broadcast_shapes`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_shapes.html#numpy.broadcast_shapes "numpy.broadcast_shapes")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[1, 2, 3\])
\>>> np.broadcast\_to(x, (3, 3))
array(\[\[1, 2, 3\],\
       \[1, 2, 3\],\
       \[1, 2, 3\]\])

Copy to clipboard

Go BackOpen In Tab

On this page