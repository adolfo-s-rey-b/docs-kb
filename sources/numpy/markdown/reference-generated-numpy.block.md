[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.block.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.block.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.block.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.block.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.block.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.block.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.block.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.block.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.block.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.block.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.block.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.block.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.block.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.block.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.block.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.block.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.block.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.block.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.block.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.block.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.block.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.block.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.block[#](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy-block "Link to this heading")

=====================================================================================================================

numpy.block(_arrays_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/shape_base.py#L778-L947)
[#](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "Link to this definition")

Assemble an nd-array from nested lists of blocks.

Blocks in the innermost lists are concatenated (see [`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")
) along the last dimension (-1), then these are concatenated along the second-last dimension (-2), and so on until the outermost list is reached.

Blocks can be of any dimension, but will not be broadcasted using the normal rules. Instead, leading axes of size 1 are inserted, to make `block.ndim` the same for all blocks. This is primarily useful for working with scalars, and means that code like `np.block([v, 1])` is valid, where `v.ndim == 1`.

When the nested list is two levels deep, this allows block matrices to be constructed from their components.

Parameters:

**arrays**nested list of array\_like or scalars (but not tuples)

If passed a single ndarray or scalar (a nested list of depth 0), this is returned unmodified (and not copied).

Elements shapes must match along the appropriate axes (without broadcasting), but leading 1s will be prepended to the shape as necessary to make the dimensions match.

Returns:

**block\_array**ndarray

The array assembled from the given blocks.

The dimensionality of the output is equal to the greatest of:

*   the dimensionality of all the inputs
    
*   the depth to which the input list is nested
    

Raises:

ValueError

*   If list depths are mismatched - for instance, `[[a, b], c]` is illegal, and should be spelt `[[a, b], [c]]`
    
*   If lists are empty - for instance, `[[a, b], []]`
    

See also

[`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate")

Join a sequence of arrays along an existing axis.

[`stack`](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")

Join a sequence of arrays along a new axis.

[`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")

Stack arrays in sequence vertically (row wise).

[`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")

Stack arrays in sequence horizontally (column wise).

[`dstack`](https://numpy.org/doc/stable/reference/generated/numpy.dstack.html#numpy.dstack "numpy.dstack")

Stack arrays in sequence depth wise (along third axis).

[`column_stack`](https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack")

Stack 1-D arrays as columns into a 2-D array.

[`vsplit`](https://numpy.org/doc/stable/reference/generated/numpy.vsplit.html#numpy.vsplit "numpy.vsplit")

Split an array into multiple sub-arrays vertically (row-wise).

[`unstack`](https://numpy.org/doc/stable/reference/generated/numpy.unstack.html#numpy.unstack "numpy.unstack")

Split an array into a tuple of sub-arrays along an axis.

Notes

When called with only scalars, `np.block` is equivalent to an ndarray call. So `np.block([[1, 2], [3, 4]])` is equivalent to `np.array([[1, 2], [3, 4]])`.

This function does not enforce that the blocks lie on a fixed grid. `np.block([[a, b], [c, d]])` is not restricted to arrays of the form:

AAAbb
AAAbb
cccDD

Copy to clipboard

But is also allowed to produce, for some `a, b, c, d`:

AAAbb
AAAbb
cDDDD

Copy to clipboard

Since concatenation happens along the last axis first, [`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")
 is _not_ capable of producing the following directly:

AAAbb
cccbb
cccDD

Copy to clipboard

Matlab’s “square bracket stacking”, `[A, B, ...; p, q, ...]`, is equivalent to `np.block([[A, B, ...], [p, q, ...]])`.

Examples

Try it in your browser!

The most common use of this function is to build a block matrix:

\>>> import numpy as np
\>>> A \= np.eye(2) \* 2
\>>> B \= np.eye(3) \* 3
\>>> np.block(\[\
...     \[A,               np.zeros((2, 3))\],\
...     \[np.ones((3, 2)), B               \]\
... \])
array(\[\[2., 0., 0., 0., 0.\],\
       \[0., 2., 0., 0., 0.\],\
       \[1., 1., 3., 0., 0.\],\
       \[1., 1., 0., 3., 0.\],\
       \[1., 1., 0., 0., 3.\]\])

Copy to clipboard

With a list of depth 1, [`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")
 can be used as [`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack")
:

\>>> np.block(\[1, 2, 3\])              \# hstack(\[1, 2, 3\])
array(\[1, 2, 3\])

Copy to clipboard

\>>> a \= np.array(\[1, 2, 3\])
\>>> b \= np.array(\[4, 5, 6\])
\>>> np.block(\[a, b, 10\])             \# hstack(\[a, b, 10\])
array(\[ 1,  2,  3,  4,  5,  6, 10\])

Copy to clipboard

\>>> A \= np.ones((2, 2), int)
\>>> B \= 2 \* A
\>>> np.block(\[A, B\])                 \# hstack(\[A, B\])
array(\[\[1, 1, 2, 2\],\
       \[1, 1, 2, 2\]\])

Copy to clipboard

With a list of depth 2, [`block`](https://numpy.org/doc/stable/reference/generated/numpy.block.html#numpy.block "numpy.block")
 can be used in place of [`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
:

\>>> a \= np.array(\[1, 2, 3\])
\>>> b \= np.array(\[4, 5, 6\])
\>>> np.block(\[\[a\], \[b\]\])             \# vstack(\[a, b\])
array(\[\[1, 2, 3\],\
       \[4, 5, 6\]\])

Copy to clipboard

\>>> A \= np.ones((2, 2), int)
\>>> B \= 2 \* A
\>>> np.block(\[\[A\], \[B\]\])             \# vstack(\[A, B\])
array(\[\[1, 1\],\
       \[1, 1\],\
       \[2, 2\],\
       \[2, 2\]\])

Copy to clipboard

It can also be used in place of [`atleast_1d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_1d.html#numpy.atleast_1d "numpy.atleast_1d")
 and [`atleast_2d`](https://numpy.org/doc/stable/reference/generated/numpy.atleast_2d.html#numpy.atleast_2d "numpy.atleast_2d")
:

\>>> a \= np.array(0)
\>>> b \= np.array(\[1\])
\>>> np.block(\[a\])                    \# atleast\_1d(a)
array(\[0\])
\>>> np.block(\[b\])                    \# atleast\_1d(b)
array(\[1\])

Copy to clipboard

\>>> np.block(\[\[a\]\])                  \# atleast\_2d(a)
array(\[\[0\]\])
\>>> np.block(\[\[b\]\])                  \# atleast\_2d(b)
array(\[\[1\]\])

Copy to clipboard

Go BackOpen In Tab

On this page