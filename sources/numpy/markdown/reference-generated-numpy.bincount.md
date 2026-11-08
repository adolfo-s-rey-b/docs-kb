[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.bincount.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.bincount.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.bincount.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.bincount.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.bincount.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.bincount.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.bincount.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.bincount.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.bincount.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.bincount.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.bincount.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.bincount.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.bincount.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.bincount.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.bincount.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.bincount.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.bincount.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.bincount.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.bincount.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.bincount.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.bincount[#](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html#numpy-bincount "Link to this heading")

==============================================================================================================================

numpy.bincount(_x_, _/_, _weights\=None_, _minlength\=0_)[#](https://numpy.org/doc/stable/reference/generated/numpy.bincount.html#numpy.bincount "Link to this definition")

Count number of occurrences of each value in array of non-negative ints.

The number of bins (of size 1) is one larger than the largest value in _x_. If _minlength_ is specified, there will be at least this number of bins in the output array (though it will be longer if necessary, depending on the contents of _x_). Each bin gives the number of occurrences of its index value in _x_. If _weights_ is specified the input array is weighted by it, i.e. if a value `n` is found at position `i`, `out[n] += weight[i]` instead of `out[n] += 1`.

Parameters:

**x**array\_like, 1 dimension, nonnegative ints

Input array.

**weights**array\_like, optional

Weights, array of the same shape as _x_.

**minlength**int, optional

A minimum number of bins for the output array.

Returns:

**out**ndarray of ints

The result of binning the input array. The length of _out_ is equal to `np.amax(x)+1`.

Raises:

ValueError

If the input is not 1-dimensional, or contains elements with negative values, or if _minlength_ is negative.

TypeError

If the type of the input is float or complex.

See also

[`histogram`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html#numpy.histogram "numpy.histogram")
, [`digitize`](https://numpy.org/doc/stable/reference/generated/numpy.digitize.html#numpy.digitize "numpy.digitize")
, [`unique`](https://numpy.org/doc/stable/reference/generated/numpy.unique.html#numpy.unique "numpy.unique")

Examples

Try it in your browser!

\>>> import numpy as np
\>>> np.bincount(np.arange(5))
array(\[1, 1, 1, 1, 1\])
\>>> np.bincount(np.array(\[0, 1, 1, 3, 2, 1, 7\]))
array(\[1, 3, 1, 1, 0, 0, 0, 1\])

Copy to clipboard

\>>> x \= np.array(\[0, 1, 1, 3, 2, 1, 7, 23\])
\>>> np.bincount(x).size \== np.amax(x)+1
True

Copy to clipboard

The input array needs to be of integer dtype, otherwise a TypeError is raised:

\>>> np.bincount(np.arange(5, dtype\=np.float64))
Traceback (most recent call last):
  ...
TypeError: Cannot cast array data from dtype('float64') to dtype('int64')
according to the rule 'safe'

Copy to clipboard

A possible use of `bincount` is to perform sums over variable-size chunks of an array, using the `weights` keyword.

\>>> w \= np.array(\[0.3, 0.5, 0.2, 0.7, 1., \-0.6\]) \# weights
\>>> x \= np.array(\[0, 1, 1, 2, 2, 2\])
\>>> np.bincount(x,  weights\=w)
array(\[ 0.3,  0.7,  1.1\])

Copy to clipboard

Go BackOpen In Tab

On this page