[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.randint.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.randint.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.randint.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.randint.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.randint.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.randint.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.randint.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.randint.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.randint.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.randint.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.randint.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.randint.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.randint.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.randint.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.randint.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.randint.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.randint.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.randint.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.randint.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.randint.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.randint[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy-random-randint "Link to this heading")

=======================================================================================================================================================

random.randint(_low_, _high\=None_, _size\=None_, _dtype\=int_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "Link to this definition")

Return random integers from _low_ (inclusive) to _high_ (exclusive).

Return random integers from the “discrete uniform” distribution of the specified dtype in the “half-open” interval \[_low_, _high_). If _high_ is None (the default), then results are from \[0, _low_).\
\
Note\
\
New code should use the [`integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "numpy.random.Generator.integers")\
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")\
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)\
.\
\
Parameters:\
\
**low**int or array-like of ints\
\
Lowest (signed) integers to be drawn from the distribution (unless `high=None`, in which case this parameter is one above the _highest_ such integer).\
\
**high**int or array-like of ints, optional\
\
If provided, one above the largest (signed) integer to be drawn from the distribution (see above for behavior if `high=None`). If array-like, must contain integer values\
\
**size**int or tuple of ints, optional\
\
Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.\
\
**dtype**dtype, optional\
\
Desired dtype of the result. Byteorder must be native. The default value is long.\
\
Warning\
\
This function defaults to the C-long dtype, which is 32bit on windows and otherwise 64bit on 64bit platforms (and 32bit on 32bit ones). Since NumPy 2.0, NumPy’s default integer is 32bit on 32bit platforms and 64bit on 64bit platforms. Which corresponds to _np.intp_. (_dtype=int_ is not the same as in most NumPy functions.)\
\
Returns:\
\
**out**int or ndarray of ints\
\
[`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")\
\-shaped array of random integers from the appropriate distribution, or a single such random int if [`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")\
 not provided.\
\
See also\
\
[`random_integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random_integers.html#numpy.random.random_integers "numpy.random.random_integers")\
\
similar to [`randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")\
, only for the closed interval \[_low_, _high_\], and 1 is the lowest value if _high_ is omitted.\
\
[`random.Generator.integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "numpy.random.Generator.integers")\
\
which should be used for new code.\
\
Examples\
\
Try it in your browser!\
\
\>>> np.random.randint(2, size\=10)\
array(\[1, 0, 0, 0, 1, 1, 0, 0, 1, 0\]) # random\
\>>> np.random.randint(1, size\=10)\
array(\[0, 0, 0, 0, 0, 0, 0, 0, 0, 0\])\
\
Copy to clipboard\
\
Generate a 2 x 4 array of ints between 0 and 4, inclusive:\
\
\>>> np.random.randint(5, size\=(2, 4))\
array(\[\[4, 0, 2, 1\], # random\
       \[3, 2, 2, 0\]\])\
\
Copy to clipboard\
\
Generate a 1 x 3 array with 3 different upper bounds\
\
\>>> np.random.randint(1, \[3, 5, 10\])\
array(\[2, 2, 9\]) # random\
\
Copy to clipboard\
\
Generate a 1 by 3 array with 3 different lower bounds\
\
\>>> np.random.randint(\[1, 5, 7\], 10)\
array(\[9, 8, 7\]) # random\
\
Copy to clipboard\
\
Generate a 2 by 4 array using broadcasting with dtype of uint8\
\
\>>> np.random.randint(\[1, 3, 5, 7\], \[\[10\], \[20\]\], dtype\=np.uint8)\
array(\[\[ 8,  6,  9,  7\], # random\
       \[ 1, 16,  9, 12\]\], dtype=uint8)\
\
Copy to clipboard\
\
Go BackOpen In Tab\
\
On this page