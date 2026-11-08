[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.unstack.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.unstack.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.unstack.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.unstack.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.unstack.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.unstack.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.unstack.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.unstack.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.unstack.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.unstack.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.unstack.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.unstack.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.unstack.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.unstack.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.unstack.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.unstack.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.unstack.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.unstack.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.unstack.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.unstack.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.unstack.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.unstack.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.unstack[#](https://numpy.org/doc/stable/reference/generated/numpy.unstack.html#numpy-unstack "Link to this heading")

===========================================================================================================================

numpy.unstack(_x_, _/_, _\*_, _axis\=0_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/shape_base.py#L471-L537)
[#](https://numpy.org/doc/stable/reference/generated/numpy.unstack.html#numpy.unstack "Link to this definition")

Split an array into a sequence of arrays along the given axis.

The `axis` parameter specifies the dimension along which the array will be split. For example, if `axis=0` (the default) it will be the first dimension and if `axis=-1` it will be the last dimension.

The result is a tuple of arrays split along `axis`.

New in version 2.1.0.

Parameters:

**x**ndarray

The array to be unstacked.

**axis**int, optional

Axis along which the array will be split. Default: `0`.

Returns:

**unstacked**tuple of ndarrays

The unstacked arrays.

See also

[`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")

Join a sequence of arrays along a new axis.

[`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")

Join a sequence of arrays along an existing axis.

[`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")

Assemble an nd-array from nested lists of blocks.

[`split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split "numpy.split")

Split array into a list of multiple sub-arrays of equal size.

Notes

`unstack` serves as the reverse operation of [`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")
, i.e., `stack(unstack(x, axis=axis), axis=axis) == x`.

This function is equivalent to `tuple(np.moveaxis(x, axis, 0))`, since iterating on an array iterates along the first axis.

Examples

Try it in your browser!

\>>> arr \= np.arange(24).reshape((2, 3, 4))
\>>> np.unstack(arr)
(array(\[\[ 0,  1,  2,  3\],\
        \[ 4,  5,  6,  7\],\
        \[ 8,  9, 10, 11\]\]),
 array(\[\[12, 13, 14, 15\],\
        \[16, 17, 18, 19\],\
        \[20, 21, 22, 23\]\]))
\>>> np.unstack(arr, axis\=1)
(array(\[\[ 0,  1,  2,  3\],\
        \[12, 13, 14, 15\]\]),
 array(\[\[ 4,  5,  6,  7\],\
        \[16, 17, 18, 19\]\]),
 array(\[\[ 8,  9, 10, 11\],\
        \[20, 21, 22, 23\]\]))
\>>> arr2 \= np.stack(np.unstack(arr, axis\=1), axis\=1)
\>>> arr2.shape
(2, 3, 4)
\>>> np.all(arr \== arr2)
np.True\_

Copy to clipboard

Go BackOpen In Tab

On this page