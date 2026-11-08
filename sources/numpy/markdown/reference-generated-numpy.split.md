[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.split.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.split.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.split.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.split.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.split.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.split.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.split.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.split.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.split.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.split.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.split.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.split.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.split.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.split.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.split.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.split.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.split.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.split.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.split.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.split.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.split.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.split.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.split[#](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy-split "Link to this heading")

=====================================================================================================================

numpy.split(_ary_, _indices\_or\_sections_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_shape_base_impl.py#L780-L856)
[#](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split "Link to this definition")

Split an array into multiple sub-arrays as views into _ary_.

Parameters:

**ary**ndarray

Array to be divided into sub-arrays.

**indices\_or\_sections**int or 1-D array

If _indices\_or\_sections_ is an integer, N, the array will be divided into N equal arrays along _axis_. If such a split is not possible, an error is raised.

If _indices\_or\_sections_ is a 1-D array of sorted integers, the entries indicate where along _axis_ the array is split. For example, `[2, 3]` would, for `axis=0`, result in

*   ary\[:2\]
    
*   ary\[2:3\]
    
*   ary\[3:\]
    

If an index exceeds the dimension of the array along _axis_, an empty sub-array is returned correspondingly.

**axis**int, optional

The axis along which to split, default is 0.

Returns:

**sub-arrays**list of ndarrays

A list of sub-arrays as views into _ary_.

Raises:

ValueError

If _indices\_or\_sections_ is given as an integer, but a split does not result in equal division.

See also

[`array_split`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split "numpy.array_split")

Split an array into multiple sub-arrays of equal or near-equal size. Does not raise an exception if an equal division cannot be made.

[`hsplit`](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit "numpy.hsplit")

Split array into multiple sub-arrays horizontally (column-wise).

[`vsplit`](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit "numpy.vsplit")

Split array into multiple sub-arrays vertically (row wise).

[`dsplit`](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy.dsplit "numpy.dsplit")

Split array into multiple sub-arrays along the 3rd axis (depth).

[`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")

Join a sequence of arrays along an existing axis.

[`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")

Join a sequence of arrays along a new axis.

[`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")

Stack arrays in sequence horizontally (column wise).

[`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")

Stack arrays in sequence vertically (row wise).

[`dstack`](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack "numpy.dstack")

Stack arrays in sequence depth wise (along third dimension).

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.arange(9.0)
\>>> np.split(x, 3)
\[array(\[0.,  1.,  2.\]), array(\[3.,  4.,  5.\]), array(\[6.,  7.,  8.\])\]

Copy to clipboard

\>>> x \= np.arange(8.0)
\>>> np.split(x, \[3, 5, 6, 10\])
\[array(\[0.,  1.,  2.\]),\
 array(\[3.,  4.\]),\
 array(\[5.\]),\
 array(\[6.,  7.\]),\
 array(\[\], dtype=float64)\]

Copy to clipboard

Go BackOpen In Tab

On this page