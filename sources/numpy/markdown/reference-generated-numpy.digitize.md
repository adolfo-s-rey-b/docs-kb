[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.digitize.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.digitize.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.digitize.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.digitize.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.digitize.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.digitize.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.digitize.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.digitize.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.digitize.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.digitize.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.digitize.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.digitize.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.digitize.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.digitize.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.digitize.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.digitize.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.digitize.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.digitize.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.digitize.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.digitize.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.digitize[#](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html#numpy-digitize "Link to this heading")

==============================================================================================================================

numpy.digitize(_x_, _bins_, _right\=False_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_function_base_impl.py#L5666-L5775)
[#](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html#numpy.digitize "Link to this definition")

Return the indices of the bins to which each value in input array belongs.

| _right_ | order of bins | returned index _i_ satisfies |
| --- | --- | --- |
| `False` | increasing | `bins[i-1] <= x < bins[i]` |
| `True` | increasing | `bins[i-1] < x <= bins[i]` |
| `False` | decreasing | `bins[i-1] > x >= bins[i]` |
| `True` | decreasing | `bins[i-1] >= x > bins[i]` |

If values in _x_ are beyond the bounds of _bins_, 0 or `len(bins)` is returned as appropriate.

Parameters:

**x**array\_like

Input array to be binned. Prior to NumPy 1.10.0, this array had to be 1-dimensional, but can now have any shape.

**bins**array\_like

Array of bins. It has to be 1-dimensional and monotonic.

**right**bool, optional

Indicating whether the intervals include the right or the left bin edge. Default behavior is (right==False) indicating that the interval does not include the right edge. The left bin end is open in this case, i.e., bins\[i-1\] <= x < bins\[i\] is the default behavior for monotonically increasing bins.

Returns:

**indices**ndarray of ints

Output array of indices, of same shape as _x_.

Raises:

ValueError

If _bins_ is not monotonic.

TypeError

If the type of the input is complex.

See also

[`bincount`](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html#numpy.bincount "numpy.bincount")
, [`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")
, [`unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")
, [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")

Notes

If values in _x_ are such that they fall outside the bin range, attempting to index _bins_ with the indices that [`digitize`](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html#numpy.digitize "numpy.digitize")
 returns will result in an IndexError.

New in version 1.10.0.

[`numpy.digitize`](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html#numpy.digitize "numpy.digitize")
 is implemented in terms of [`numpy.searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")
. This means that a binary search is used to bin the values, which scales much better for larger number of bins than the previous linear search. It also removes the requirement for the input array to be 1-dimensional.

For monotonically _increasing_ _bins_, the following are equivalent:

np.digitize(x, bins, right\=True)
np.searchsorted(bins, x, side\='left')

Copy to clipboard

Note that as the order of the arguments are reversed, the side must be too. The [`searchsorted`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted")
 call is marginally faster, as it does not do any monotonicity checks. Perhaps more importantly, it supports all dtypes.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= np.array(\[0.2, 6.4, 3.0, 1.6\])
\>>> bins \= np.array(\[0.0, 1.0, 2.5, 4.0, 10.0\])
\>>> inds \= np.digitize(x, bins)
\>>> inds
array(\[1, 4, 3, 2\])
\>>> for n in range(x.size):
...   print(bins\[inds\[n\]\-1\], "<=", x\[n\], "<", bins\[inds\[n\]\])
...
0.0 <= 0.2 < 1.0
4.0 <= 6.4 < 10.0
2.5 <= 3.0 < 4.0
1.0 <= 1.6 < 2.5

Copy to clipboard

\>>> x \= np.array(\[1.2, 10.0, 12.4, 15.5, 20.\])
\>>> bins \= np.array(\[0, 5, 10, 15, 20\])
\>>> np.digitize(x,bins,right\=True)
array(\[1, 2, 3, 4, 4\])
\>>> np.digitize(x,bins,right\=False)
array(\[1, 3, 3, 4, 5\])

Copy to clipboard

Go BackOpen In Tab

On this page