[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.choice[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy-random-generator-choice "Link to this heading")

==================================================================================================================================================================================

method

random.Generator.choice(_a_, _size\=None_, _replace\=True_, _p\=None_, _axis\=0_, _shuffle\=True_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy.random.Generator.choice "Link to this definition")

Generates a random sample from a given array

Parameters:

**a**{array\_like, int}

If an ndarray, a random sample is generated from its elements. If an int, the random sample is generated from np.arange(a).

**size**{int, tuple\[int\]}, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn from the 1-d _a_. If _a_ has more than one dimension, the [`size`](https://numpy.org/doc/stable/reference/generated/numpy.size.html#numpy.size "numpy.size")
 shape will be inserted into the _axis_ dimension, so the output `ndim` will be `a.ndim - 1 + len(size)`. Default is None, in which case a single value is returned.

**replace**bool, optional

Whether the sample is with or without replacement. Default is True, meaning that a value of `a` can be selected multiple times.

**p**1-D array\_like, optional

The probabilities associated with each entry in a. If not given, the sample assumes a uniform distribution over all entries in `a`.

**axis**int, optional

The axis along which the selection is performed. The default, 0, selects by row.

**shuffle**bool, optional

Whether the sample is shuffled when sampling without replacement. Default is True, False provides a speedup.

Returns:

**samples**single item or ndarray

The generated random samples

Raises:

ValueError

If a is an int and less than zero, if p is not 1-dimensional, if a is array-like with a size 0, if p is not a vector of probabilities, if a and p have different lengths, or if replace=False and the sample size is greater than the population size.

See also

[`integers`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "numpy.random.Generator.integers")
, [`shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle "numpy.random.Generator.shuffle")
, [`permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html#numpy.random.Generator.permutation "numpy.random.Generator.permutation")

Notes

Setting user-specified probabilities through `p` uses a more general but less efficient sampler than the default. The general sampler produces a different sample than the optimized sampler even if each element of `p` is 1 / len(a).

`p` must sum to 1 when cast to `float64`. To ensure this, you may wish to normalize using `p = p / np.sum(p, dtype=np.float64)`.

When passing `a` as an integer type and `size` is not specified, the return type is a native Python `int`.

Examples

Try it in your browser!

Generate a uniform random sample from np.arange(5) of size 3:

\>>> rng \= np.random.default\_rng()
\>>> rng.choice(5, 3)
array(\[0, 3, 4\]) # random
\>>> #This is equivalent to rng.integers(0,5,3)

Copy to clipboard

Generate a non-uniform random sample from np.arange(5) of size 3:

\>>> rng.choice(5, 3, p\=\[0.1, 0, 0.3, 0.6, 0\])
array(\[3, 3, 0\]) # random

Copy to clipboard

Generate a uniform random sample from np.arange(5) of size 3 without replacement:

\>>> rng.choice(5, 3, replace\=False)
array(\[3,1,0\]) # random
\>>> #This is equivalent to rng.permutation(np.arange(5))\[:3\]

Copy to clipboard

Generate a uniform random sample from a 2-D array along the first axis (the default), without replacement:

\>>> rng.choice(\[\[0, 1, 2\], \[3, 4, 5\], \[6, 7, 8\]\], 2, replace\=False)
array(\[\[3, 4, 5\], # random\
       \[0, 1, 2\]\])

Copy to clipboard

Generate a non-uniform random sample from np.arange(5) of size 3 without replacement:

\>>> rng.choice(5, 3, replace\=False, p\=\[0.1, 0, 0.3, 0.6, 0\])
array(\[2, 3, 0\]) # random

Copy to clipboard

Any of the above can be repeated with an arbitrary array-like instead of just integers. For instance:

\>>> aa\_milne\_arr \= \['pooh', 'rabbit', 'piglet', 'Christopher'\]
\>>> rng.choice(aa\_milne\_arr, 5, p\=\[0.5, 0.1, 0.1, 0.3\])
array(\['pooh', 'pooh', 'pooh', 'Christopher', 'piglet'\], # random
      dtype='<U11')

Copy to clipboard

Go BackOpen In Tab

On this page