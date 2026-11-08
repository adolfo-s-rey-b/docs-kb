[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.dstack.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.dstack.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.dstack.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.dstack.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.dstack.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.dstack.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.dstack.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.dstack.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.dstack.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.dstack.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.dstack.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.dstack.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.dstack.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.dstack.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.dstack.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.dstack.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.dstack.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.dstack.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.dstack.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.dstack.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.dstack[#](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy-dstack "Link to this heading")

========================================================================================================================

numpy.dstack(_tup_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L655-L712)
[#](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack "Link to this definition")

Stack arrays in sequence depth wise (along third axis).

This is equivalent to concatenation along the third axis after 2-D arrays of shape _(M,N)_ have been reshaped to _(M,N,1)_ and 1-D arrays of shape _(N,)_ have been reshaped to _(1,N,1)_. Rebuilds arrays divided by [`dsplit`](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy.dsplit "numpy.dsplit")
.

This function makes most sense for arrays with up to 3 dimensions. For instance, for pixel-data with a height (first axis), width (second axis), and r/g/b channels (third axis). The functions [`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
, [`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")
 and [`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")
 provide more general stacking and concatenation operations.

Parameters:

**tup**sequence of arrays

The arrays must have the same shape along all but the third axis. 1-D or 2-D arrays must have the same shape.

Returns:

**stacked**ndarray

The array formed by stacking the given arrays, will be at least 3-D.

See also

[`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")

Join a sequence of arrays along an existing axis.

[`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")

Join a sequence of arrays along a new axis.

[`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")

Assemble an nd-array from nested lists of blocks.

[`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")

Stack arrays in sequence vertically (row wise).

[`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")

Stack arrays in sequence horizontally (column wise).

[`column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")

Stack 1-D arrays as columns into a 2-D array.

[`dsplit`](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy.dsplit "numpy.dsplit")

Split array along third axis.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array((1,2,3))
\>>> b \= np.array((4,5,6))
\>>> np.dstack((a,b))
array(\[\[\[1, 4\],\
        \[2, 5\],\
        \[3, 6\]\]\])

Copy to clipboard

\>>> a \= np.array(\[\[1\],\[2\],\[3\]\])
\>>> b \= np.array(\[\[4\],\[5\],\[6\]\])
\>>> np.dstack((a,b))
array(\[\[\[1, 4\]\],\
       \[\[2, 5\]\],\
       \[\[3, 6\]\]\])

Copy to clipboard

Go BackOpen In Tab

On this page