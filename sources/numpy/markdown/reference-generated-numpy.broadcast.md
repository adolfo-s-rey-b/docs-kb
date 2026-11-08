[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.broadcast.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.broadcast.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.broadcast.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.broadcast.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.broadcast.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.broadcast.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.broadcast.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.broadcast.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.broadcast.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.broadcast.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.broadcast.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.broadcast.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.broadcast.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.broadcast.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.broadcast.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.broadcast.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.broadcast.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.broadcast.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.broadcast.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.broadcast.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.broadcast[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.html#numpy-broadcast "Link to this heading")

=================================================================================================================================

_class_ numpy.broadcast(_\*arrays_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/__init__.py)
[#](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.html#numpy.broadcast "Link to this definition")

Produce an object that mimics broadcasting.

Parameters:

**in1, in2, …**array\_like

Input parameters.

Attributes:

[`index`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.index.html#numpy.broadcast.index "numpy.broadcast.index")

current index in broadcasted result

[`iters`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.iters.html#numpy.broadcast.iters "numpy.broadcast.iters")

tuple of iterators along `self`’s “components.”

[`nd`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.nd.html#numpy.broadcast.nd "numpy.broadcast.nd")

Number of dimensions of broadcasted result.

[`ndim`](https://numpy.org/doc/stable/reference/generated/numpy.ndim.html#numpy.ndim "numpy.ndim")

Number of dimensions of broadcasted result.

[`numiter`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.numiter.html#numpy.broadcast.numiter "numpy.broadcast.numiter")

Number of iterators possessed by the broadcasted result.

[`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")

Shape of broadcasted result.

[`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")

Total size of broadcasted result.

Methods

|     |     |
| --- | --- |
| [`reset`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast.reset.html#numpy.broadcast.reset "numpy.broadcast.reset")<br>() | Reset the broadcasted result's iterator(s). |

Returns:

**b**broadcast object

Broadcast the input parameters against one another, and return an object that encapsulates the result. Amongst others, it has `shape` and `nd` properties, and may be used as an iterator.

See also

[`broadcast_arrays`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_arrays.html#numpy.broadcast_arrays "numpy.broadcast_arrays")

[`broadcast_to`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_to.html#numpy.broadcast_to "numpy.broadcast_to")

[`broadcast_shapes`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_shapes.html#numpy.broadcast_shapes "numpy.broadcast_shapes")

Examples

Try it in your browser!

Manually adding two vectors, using broadcasting:

\>>> import numpy as np
\>>> x \= np.array(\[\[1\], \[2\], \[3\]\])
\>>> y \= np.array(\[4, 5, 6\])
\>>> b \= np.broadcast(x, y)

Copy to clipboard

\>>> out \= np.empty(b.shape)
\>>> out.flat \= \[u+v for (u,v) in b\]
\>>> out
array(\[\[5.,  6.,  7.\],\
       \[6.,  7.,  8.\],\
       \[7.,  8.,  9.\]\])

Copy to clipboard

Compare against built-in broadcasting:

\>>> x + y
array(\[\[5, 6, 7\],\
       \[6, 7, 8\],\
       \[7, 8, 9\]\])

Copy to clipboard

Go BackOpen In Tab

On this page