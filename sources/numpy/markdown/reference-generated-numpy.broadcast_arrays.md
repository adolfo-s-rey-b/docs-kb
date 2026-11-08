[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_arrays.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.broadcast_arrays.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_arrays.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.broadcast_arrays.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.broadcast_arrays.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.broadcast_arrays.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.broadcast_arrays.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.broadcast_arrays.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.broadcast_arrays.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.broadcast_arrays.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.broadcast_arrays.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.broadcast_arrays.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.broadcast_arrays.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.broadcast_arrays.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.broadcast_arrays.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.broadcast_arrays.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.broadcast_arrays.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.broadcast_arrays.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.broadcast_arrays.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.broadcast_arrays.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.broadcast_arrays.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.broadcast_arrays.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.broadcast\_arrays[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_arrays.html#numpy-broadcast-arrays "Link to this heading")

=======================================================================================================================================================

numpy.broadcast\_arrays(_\*args_, _subok\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_stride_tricks_impl.py#L588-L656)
[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_arrays.html#numpy.broadcast_arrays "Link to this definition")

Broadcast any number of arrays against each other.

Parameters:

**\*args**array\_likes

The arrays to broadcast.

**subok**bool, optional

If True, then sub-classes will be passed-through, otherwise the returned arrays will be forced to be a base-class array (default).

Returns:

**broadcasted**tuple of arrays

These arrays are views on the original arrays. They are typically not contiguous. Furthermore, more than one element of a broadcasted array may refer to a single memory location. If you need to write to the arrays, make copies first. While you can set the `writable` flag True, writing to a single output value may end up changing more than one location in the output array.

Deprecated since version 1.17: The output is currently marked so that if written to, a deprecation warning will be emitted. A future version will set the `writable` flag False so writing to it will raise an error.

See also

[`broadcast`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.html#numpy.broadcast "numpy.broadcast")

[`broadcast_to`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to "numpy.broadcast_to")

[`broadcast_shapes`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_shapes.html#numpy.broadcast_shapes "numpy.broadcast_shapes")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[\[1,2,3\]\])
\>>> y \= np.array(\[\[4\],\[5\]\])
\>>> np.broadcast\_arrays(x, y)
(array(\[\[1, 2, 3\],\
        \[1, 2, 3\]\]),
 array(\[\[4, 4, 4\],\
        \[5, 5, 5\]\]))

Copy to clipboard

Here is a useful idiom for getting contiguous copies instead of non-contiguous views.

\>>> \[np.array(a) for a in np.broadcast\_arrays(x, y)\]
\[array(\[\[1, 2, 3\],\
        \[1, 2, 3\]\]),\
 array(\[\[4, 4, 4\],\
        \[5, 5, 5\]\])\]

Copy to clipboard

Go BackOpen In Tab

On this page