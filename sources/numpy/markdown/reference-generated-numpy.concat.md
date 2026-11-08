[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.concat.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.concat.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.concat.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.concat.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.concat.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.concat.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.concat.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.concat.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.concat.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.concat.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.concat.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.concat.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.concat.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.concat.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.concat.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.concat.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.concat.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.concat.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.concat.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.concat.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.concat.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.concat.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.concat[#](https://numpy.org/doc/stable/reference/generated/numpy.concat.html#numpy-concat "Link to this heading")

========================================================================================================================

numpy.concat(_arrays_, _/_, _axis\=0_, _out\=None_, _\*_, _dtype\=None_, _casting\='same\_kind'_)[#](https://numpy.org/doc/stable/reference/generated/numpy.concat.html#numpy.concat "Link to this definition")

Join a sequence of arrays along an existing axis.

New in version 2.0: `numpy.concat` added as a shorthand for `numpy.concatenate`.

Parameters:

**a1, a2, …**sequence of array\_like

The arrays must have the same shape, except in the dimension corresponding to _axis_ (the first, by default).

**axis**int, optional

The axis along which the arrays will be joined. If axis is None, arrays are flattened before use. Default is 0.

**out**ndarray, optional

If provided, the destination to place the result. The shape must be correct, matching that of what concatenate would have returned if no out argument were specified.

**dtype**str or dtype

If provided, the destination array will have this dtype. Cannot be provided together with _out_.

New in version 1.20.0.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same\_kind’, ‘unsafe’}, optional

Controls what kind of data casting may occur. Defaults to ‘same\_kind’. For a description of the options, please see [casting](https://numpy.org/doc/stable/glossary.html#term-casting)
.

New in version 1.20.0.

Returns:

**res**ndarray

The concatenated array.

See also

[`ma.concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.ma.concatenate.html#numpy.ma.concatenate "numpy.ma.concatenate")

Concatenate function that preserves input masks.

[`array_split`](https://numpy.org/doc/stable/reference/generated/numpy.array_split.html#numpy.array_split "numpy.array_split")

Split an array into multiple sub-arrays of equal or near-equal size.

[`split`](https://numpy.org/doc/stable/reference/generated/numpy.split.html#numpy.split "numpy.split")

Split array into a list of multiple sub-arrays of equal size.

[`hsplit`](https://numpy.org/doc/stable/reference/generated/numpy.hsplit.html#numpy.hsplit "numpy.hsplit")

Split array into multiple sub-arrays horizontally (column wise).

[`vsplit`](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit "numpy.vsplit")

Split array into multiple sub-arrays vertically (row wise).

[`dsplit`](https://numpy.org/doc/stable/reference/generated/numpy.dsplit.html#numpy.dsplit "numpy.dsplit")

Split array into multiple sub-arrays along the 3rd axis (depth).

[`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")

Stack a sequence of arrays along a new axis.

[`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")

Assemble arrays from blocks.

[`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")

Stack arrays in sequence horizontally (column wise).

[`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")

Stack arrays in sequence vertically (row wise).

[`dstack`](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack "numpy.dstack")

Stack arrays in sequence depth wise (along third dimension).

[`column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")

Stack 1-D arrays as columns into a 2-D array.

Notes

When one or more of the arrays to be concatenated is a MaskedArray, this function will return a MaskedArray object instead of an ndarray, but the input masks are _not_ preserved. In cases where a MaskedArray is expected as input, use the ma.concatenate function from the masked array module instead.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> b \= np.array(\[\[5, 6\]\])
\>>> np.concatenate((a, b), axis\=0)
array(\[\[1, 2\],\
       \[3, 4\],\
       \[5, 6\]\])
\>>> np.concatenate((a, b.T), axis\=1)
array(\[\[1, 2, 5\],\
       \[3, 4, 6\]\])
\>>> np.concatenate((a, b), axis\=None)
array(\[1, 2, 3, 4, 5, 6\])

Copy to clipboard

This function will not preserve masking of MaskedArray inputs.

\>>> a \= np.ma.arange(3)
\>>> a\[1\] \= np.ma.masked
\>>> b \= np.arange(2, 5)
\>>> a
masked\_array(data=\[0, --, 2\],
             mask=\[False,  True, False\],
       fill\_value=999999)
\>>> b
array(\[2, 3, 4\])
\>>> np.concatenate(\[a, b\])
masked\_array(data=\[0, 1, 2, 2, 3, 4\],
             mask=False,
       fill\_value=999999)
\>>> np.ma.concatenate(\[a, b\])
masked\_array(data=\[0, --, 2, 2, 3, 4\],
             mask=\[False,  True, False, False, False, False\],
       fill\_value=999999)

Copy to clipboard

Go BackOpen In Tab

On this page