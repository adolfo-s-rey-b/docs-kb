[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.transpose.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.transpose.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.transpose.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.transpose.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.transpose.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.transpose.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.transpose.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.transpose.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.transpose.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.transpose.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.transpose.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.transpose.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.transpose.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.transpose.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.transpose.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.transpose.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.transpose.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.transpose.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.transpose.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.transpose.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.transpose[#](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy-transpose "Link to this heading")

=================================================================================================================================

numpy.transpose(_a_, _axes\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/_core/fromnumeric.py#L604-L677)
[#](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html#numpy.transpose "Link to this definition")

Returns an array with axes transposed.

For a 1-D array, this returns an unchanged view of the original array, as a transposed vector is simply the same vector. To convert a 1-D array into a 2-D column vector, an additional dimension must be added, e.g., `np.atleast_2d(a).T` achieves this, as does `a[:, np.newaxis]`. For a 2-D array, this is the standard matrix transpose. For an n-D array, if axes are given, their order indicates how the axes are permuted (see Examples). If axes are not provided, then `transpose(a).shape == a.shape[::-1]`.

Parameters:

**a**array\_like

Input array.

**axes**tuple or list of ints, optional

If specified, it must be a tuple or list which contains a permutation of \[0, 1, …, N-1\] where N is the number of axes of _a_. Negative indices can also be used to specify axes. The i-th axis of the returned array will correspond to the axis numbered `axes[i]` of the input. If not specified, defaults to `range(a.ndim)[::-1]`, which reverses the order of the axes.

Returns:

**p**ndarray

_a_ with its axes permuted. A view is returned whenever possible.

See also

[`ndarray.transpose`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose "numpy.ndarray.transpose")

Equivalent method.

[`moveaxis`](https://numpy.org/doc/stable/reference/generated/numpy.moveaxis.html#numpy.moveaxis "numpy.moveaxis")

Move axes of an array to new positions.

[`argsort`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort")

Return the indices that would sort an array.

Notes

Use `transpose(a, argsort(axes))` to invert the transposition of tensors when using the _axes_ keyword argument.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[\[1, 2\], \[3, 4\]\])
\>>> a
array(\[\[1, 2\],\
       \[3, 4\]\])
\>>> np.transpose(a)
array(\[\[1, 3\],\
       \[2, 4\]\])

Copy to clipboard

\>>> a \= np.array(\[1, 2, 3, 4\])
\>>> a
array(\[1, 2, 3, 4\])
\>>> np.transpose(a)
array(\[1, 2, 3, 4\])

Copy to clipboard

\>>> a \= np.ones((1, 2, 3))
\>>> np.transpose(a, (1, 0, 2)).shape
(2, 1, 3)

Copy to clipboard

\>>> a \= np.ones((2, 3, 4, 5))
\>>> np.transpose(a).shape
(5, 4, 3, 2)

Copy to clipboard

\>>> a \= np.arange(3\*4\*5).reshape((3, 4, 5))
\>>> np.transpose(a, (\-1, 0, \-2)).shape
(5, 3, 4)

Copy to clipboard

Go BackOpen In Tab

On this page