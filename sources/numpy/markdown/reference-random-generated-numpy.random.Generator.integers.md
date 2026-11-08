[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.integers.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.integers.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.integers.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.integers.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.integers.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.integers.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.integers.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.integers.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.integers.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.integers.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.integers.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.integers.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.integers.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.integers.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.integers.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.integers.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.integers.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.integers.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.integers.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.integers.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.integers[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy-random-generator-integers "Link to this heading")

========================================================================================================================================================================================

method

random.Generator.integers(_low_, _high\=None_, _size\=None_, _dtype\=np.int64_, _endpoint\=False_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "Link to this definition")

Return random integers from _low_ (inclusive) to _high_ (exclusive), or if endpoint=True, _low_ (inclusive) to _high_ (inclusive). Replaces _RandomState.randint_ (with endpoint=False) and _RandomState.random\_integers_ (with endpoint=True)

Return random integers from the “discrete uniform” distribution of the specified dtype. If _high_ is None (the default), then results are from 0 to _low_.

Parameters:

**low**int or array-like of ints

Lowest (signed) integers to be drawn from the distribution (unless `high=None`, in which case this parameter is 0 and this value is used for _high_).

**high**int or array-like of ints, optional

If provided, one above the largest (signed) integer to be drawn from the distribution (see above for behavior if `high=None`). If array-like, must contain integer values

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.

**dtype**dtype, optional

Desired dtype of the result. Byteorder must be native. The default value is np.int64.

**endpoint**bool, optional

If true, sample from the interval \[low, high\] instead of the default \[low, high) Defaults to False\
\
Returns:\
\
**out**int or ndarray of ints\
\
[`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")\
\-shaped array of random integers from the appropriate distribution, or a single such random int if [`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")\
 not provided.\
\
Notes\
\
When using broadcasting with uint64 dtypes, the maximum value (2\*\*64) cannot be represented as a standard integer type. The high array (or low if high is None) must have object dtype, e.g., array(\[2\*\*64\]).\
\
References\
\
\[1\]\
\
Daniel Lemire., “Fast Random Integer Generation in an Interval”, ACM Transactions on Modeling and Computer Simulation 29 (1), 2019, [https://arxiv.org/abs/1805.10941](https://arxiv.org/abs/1805.10941)\
.\
\
Examples\
\
Try it in your browser!\
\
\>>> rng \= np.random.default\_rng()\
\>>> rng.integers(2, size\=10)\
array(\[1, 0, 0, 0, 1, 1, 0, 0, 1, 0\])  # random\
\>>> rng.integers(1, size\=10)\
array(\[0, 0, 0, 0, 0, 0, 0, 0, 0, 0\])\
\
Copy to clipboard\
\
Generate a 2 x 4 array of ints between 0 and 4, inclusive:\
\
\>>> rng.integers(5, size\=(2, 4))\
array(\[\[4, 0, 2, 1\],\
       \[3, 2, 2, 0\]\])  # random\
\
Copy to clipboard\
\
Generate a 1 x 3 array with 3 different upper bounds\
\
\>>> rng.integers(1, \[3, 5, 10\])\
array(\[2, 2, 9\])  # random\
\
Copy to clipboard\
\
Generate a 1 by 3 array with 3 different lower bounds\
\
\>>> rng.integers(\[1, 5, 7\], 10)\
array(\[9, 8, 7\])  # random\
\
Copy to clipboard\
\
Generate a 2 by 4 array using broadcasting with dtype of uint8\
\
\>>> rng.integers(\[1, 3, 5, 7\], \[\[10\], \[20\]\], dtype\=np.uint8)\
array(\[\[ 8,  6,  9,  7\],\
       \[ 1, 16,  9, 12\]\], dtype=uint8)  # random\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page