[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.flip.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.flip[#](https://numpy.org/doc/stable/reference/generated/numpy.flip.html#numpy-flip "Link to this heading")

==================================================================================================================

numpy.flip(_m_, _axis\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L283-L371)
[#](https://numpy.org/doc/stable/reference/generated/numpy.flip.html#numpy.flip "Link to this definition")

Reverse the order of elements in an array along the given axis.

The shape of the array is preserved, but the elements are reordered.

Parameters:

**m**array\_like

Input array.

**axis**None or int or tuple of ints, optional

Axis or axes along which to flip over. The default, axis=None, will flip over all of the axes of the input array. If axis is negative it counts from the last to the first axis.

If axis is a tuple of ints, flipping is performed on all of the axes specified in the tuple.

Returns:

**out**array\_like

A view of _m_ with the entries of axis reversed. Since a view is returned, this operation is done in constant time.

See also

[`flipud`](https://numpy.org/doc/stable/reference/generated/numpy.flipud.html#numpy.flipud "numpy.flipud")

Flip an array vertically (axis=0).

[`fliplr`](https://numpy.org/doc/stable/reference/generated/numpy.fliplr.html#numpy.fliplr "numpy.fliplr")

Flip an array horizontally (axis=1).

Notes

flip(m, 0) is equivalent to flipud(m).

flip(m, 1) is equivalent to fliplr(m).

flip(m, n) corresponds to `m[...,::-1,...]` with `::-1` at position n.

flip(m) corresponds to `m[::-1,::-1,...,::-1]` with `::-1` at all positions.

flip(m, (0, 1)) corresponds to `m[::-1,::-1,...]` with `::-1` at position 0 and position 1.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> A \= np.arange(8).reshape((2,2,2))
\>>> A
array(\[\[\[0, 1\],\
        \[2, 3\]\],\
       \[\[4, 5\],\
        \[6, 7\]\]\])
\>>> np.flip(A, 0)
array(\[\[\[4, 5\],\
        \[6, 7\]\],\
       \[\[0, 1\],\
        \[2, 3\]\]\])
\>>> np.flip(A, 1)
array(\[\[\[2, 3\],\
        \[0, 1\]\],\
       \[\[6, 7\],\
        \[4, 5\]\]\])
\>>> np.flip(A)
array(\[\[\[7, 6\],\
        \[5, 4\]\],\
       \[\[3, 2\],\
        \[1, 0\]\]\])
\>>> np.flip(A, (0, 2))
array(\[\[\[5, 4\],\
        \[7, 6\]\],\
       \[\[1, 0\],\
        \[3, 2\]\]\])
\>>> rng \= np.random.default\_rng()
\>>> A \= rng.normal(size\=(3,4,5))
\>>> np.all(np.flip(A,2) \== A\[:,:,::\-1,...\])
True

Copy to clipboard

Go BackOpen In Tab

On this page