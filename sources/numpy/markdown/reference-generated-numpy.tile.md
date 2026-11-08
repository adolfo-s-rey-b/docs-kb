[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.tile.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.tile.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.tile.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.tile.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.tile.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.tile.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.tile.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.tile.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.tile.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.tile.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.tile.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.tile.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.tile.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.tile.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.tile.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.tile.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.tile.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.tile.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.tile.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.tile.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.tile.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.tile.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.tile[#](https://numpy.org/doc/stable/reference/generated/numpy.tile.html#numpy-tile "Link to this heading")

==================================================================================================================

numpy.tile(_A_, _reps_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L1157-L1247)
[#](https://numpy.org/doc/stable/reference/generated/numpy.tile.html#numpy.tile "Link to this definition")

Construct an array by repeating A the number of times given by reps.

If _reps_ has length `d`, the result will have dimension of `max(d, A.ndim)`.

If `A.ndim < d`, _A_ is promoted to be d-dimensional by prepending new axes. So a shape (3,) array is promoted to (1, 3) for 2-D replication, or shape (1, 1, 3) for 3-D replication. If this is not the desired behavior, promote _A_ to d-dimensions manually before calling this function.

If `A.ndim > d`, _reps_ is promoted to _A_.ndim by prepending 1’s to it. Thus for an _A_ of shape (2, 3, 4, 5), a _reps_ of (2, 2) is treated as (1, 1, 2, 2).

Note : Although tile may be used for broadcasting, it is strongly recommended to use numpy’s broadcasting operations and functions.

Parameters:

**A**array\_like

The input array.

**reps**array\_like

The number of repetitions of _A_ along each axis.

Returns:

**c**ndarray

The tiled output array.

See also

[`repeat`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat")

Repeat elements of an array.

[`broadcast_to`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to "numpy.broadcast_to")

Broadcast an array to a new shape

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[0, 1, 2\])
\>>> np.tile(a, 2)
array(\[0, 1, 2, 0, 1, 2\])
\>>> np.tile(a, (2, 2))
array(\[\[0, 1, 2, 0, 1, 2\],\
       \[0, 1, 2, 0, 1, 2\]\])
\>>> np.tile(a, (2, 1, 2))
array(\[\[\[0, 1, 2, 0, 1, 2\]\],\
       \[\[0, 1, 2, 0, 1, 2\]\]\])

Copy to clipboard

\>>> b \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> np.tile(b, 2)
array(\[\[1, 2, 1, 2\],\
       \[3, 4, 3, 4\]\])
\>>> np.tile(b, (2, 1))
array(\[\[1, 2\],\
       \[3, 4\],\
       \[1, 2\],\
       \[3, 4\]\])

Copy to clipboard

\>>> c \= np.array(\[1,2,3,4\])
\>>> np.tile(c,(4,1))
array(\[\[1, 2, 3, 4\],\
       \[1, 2, 3, 4\],\
       \[1, 2, 3, 4\],\
       \[1, 2, 3, 4\]\])

Copy to clipboard

Go BackOpen In Tab

On this page