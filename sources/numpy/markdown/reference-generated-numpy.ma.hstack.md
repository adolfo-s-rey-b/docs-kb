[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.hstack.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.hstack.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.hstack.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.hstack.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.hstack.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.hstack.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.hstack.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.hstack.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.hstack.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.hstack.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.hstack.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.hstack.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.hstack.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.hstack.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.hstack.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.hstack.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.hstack.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.hstack.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.hstack.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.hstack.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.hstack.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.hstack.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.hstack[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.hstack.html#numpy-ma-hstack "Link to this heading")

=================================================================================================================================

ma.hstack(_tup_, _\*_, _dtype\=None_, _casting\='same\_kind'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/shape_base.py#L293-L365)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.hstack.html#numpy.ma.hstack "Link to this definition")

Stack arrays in sequence horizontally (column wise).

This is equivalent to concatenation along the second axis, except for 1-D arrays where it concatenates along the first axis. Rebuilds arrays divided by [`hsplit`](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit "numpy.hsplit")
.

This function makes most sense for arrays with up to 3 dimensions. For instance, for pixel-data with a height (first axis), width (second axis), and r/g/b channels (third axis). The functions [`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
, [`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")
 and [`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")
 provide more general stacking and concatenation operations.

Parameters:

**tup**sequence of ndarrays

The arrays must have the same shape along all but the second axis, except 1-D arrays which can be any length. In the case of a single array\_like input, it will be treated as a sequence of arrays; i.e., each element along the zeroth axis is treated as a separate array.

**dtype**str or dtype

If provided, the destination array will have this dtype. Cannot be provided together with _out_.

New in version 1.24.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}, optional

Controls what kind of data casting may occur. Defaults to ‘same\_kind’.

New in version 1.24.

Returns:

**stacked**ndarray

The array formed by stacking the given arrays.

See also

[`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")

Join a sequence of arrays along an existing axis.

[`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")

Join a sequence of arrays along a new axis.

[`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")

Assemble an nd-array from nested lists of blocks.

[`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")

Stack arrays in sequence vertically (row wise).

[`dstack`](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack "numpy.dstack")

Stack arrays in sequence depth wise (along third axis).

[`column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")

Stack 1-D arrays as columns into a 2-D array.

[`hsplit`](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit "numpy.hsplit")

Split an array into multiple sub-arrays horizontally (column-wise).

[`unstack`](https://numpy.org/doc/stable/reference/generated/numpy.unstack.html#numpy.unstack "numpy.unstack")

Split an array into a tuple of sub-arrays along an axis.

Notes

The function is applied to both the `_data` and the `_mask`, if any.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array((1,2,3))
\>>> b \= np.array((4,5,6))
\>>> np.hstack((a,b))
array(\[1, 2, 3, 4, 5, 6\])
\>>> a \= np.array(\[\[1\],\[2\],\[3\]\])
\>>> b \= np.array(\[\[4\],\[5\],\[6\]\])
\>>> np.hstack((a,b))
array(\[\[1, 4\],\
       \[2, 5\],\
       \[3, 6\]\])

Copy to clipboard

Go BackOpen In Tab

On this page