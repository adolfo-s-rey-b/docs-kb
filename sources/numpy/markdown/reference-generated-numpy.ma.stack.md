[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.stack.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.ma.stack.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.ma.stack.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.ma.stack.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.ma.stack.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.ma.stack.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.ma.stack.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.ma.stack.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.ma.stack.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.ma.stack.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.ma.stack.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.ma.stack.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.ma.stack.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.ma.stack.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.ma.stack.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.ma.stack.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.ma.stack.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.ma.stack.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.ma.stack.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.ma.stack.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.ma.stack.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.ma.stack.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.ma.stack[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.stack.html#numpy-ma-stack "Link to this heading")

==============================================================================================================================

ma.stack(_arrays_, _axis\=0_, _out\=None_, _\*_, _dtype\=None_, _casting\='same\_kind'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/shape_base.py#L378-L466)
[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.stack.html#numpy.ma.stack "Link to this definition")

Join a sequence of arrays along a new axis.

The `axis` parameter specifies the index of the new axis in the dimensions of the result. For example, if `axis=0` it will be the first dimension and if `axis=-1` it will be the last dimension.

Parameters:

**arrays**sequence of ndarrays

Each array must have the same shape. In the case of a single ndarray array\_like input, it will be treated as a sequence of arrays; i.e., each element along the zeroth axis is treated as a separate array.

**axis**int, optional

The axis in the result array along which the input arrays are stacked.

**out**ndarray, optional

If provided, the destination to place the result. The shape must be correct, matching that of what stack would have returned if no out argument were specified.

**dtype**str or dtype

If provided, the destination array will have this dtype. Cannot be provided together with _out_.

New in version 1.24.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}, optional

Controls what kind of data casting may occur. Defaults to ‘same\_kind’.

New in version 1.24.

Returns:

**stacked**ndarray

The stacked array has one more dimension than the input arrays.

See also

[`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")

Join a sequence of arrays along an existing axis.

[`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")

Assemble an nd-array from nested lists of blocks.

[`split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split "numpy.split")

Split array into a list of multiple sub-arrays of equal size.

[`unstack`](https://numpy.org/doc/stable/reference/generated/numpy.unstack.html#numpy.unstack "numpy.unstack")

Split an array into a tuple of sub-arrays along an axis.

Notes

The function is applied to both the `_data` and the `_mask`, if any.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> rng \= np.random.default\_rng()
\>>> arrays \= \[rng.normal(size\=(3,4)) for \_ in range(10)\]
\>>> np.stack(arrays, axis\=0).shape
(10, 3, 4)

Copy to clipboard

\>>> np.stack(arrays, axis\=1).shape
(3, 10, 4)

Copy to clipboard

\>>> np.stack(arrays, axis\=2).shape
(3, 4, 10)

Copy to clipboard

\>>> a \= np.array(\[1, 2, 3\])
\>>> b \= np.array(\[4, 5, 6\])
\>>> np.stack((a, b))
array(\[\[1, 2, 3\],\
       \[4, 5, 6\]\])

Copy to clipboard

\>>> np.stack((a, b), axis\=-1)
array(\[\[1, 4\],\
       \[2, 5\],\
       \[3, 6\]\])

Copy to clipboard

Go BackOpen In Tab

On this page