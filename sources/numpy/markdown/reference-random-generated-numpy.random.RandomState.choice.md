[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.choice.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.choice.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.choice.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.choice.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.choice.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.choice.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.choice.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.choice.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.choice.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.choice.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.choice.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.choice.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.choice.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.choice.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.choice.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.choice.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.choice.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.choice.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.choice.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.choice.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.choice.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.choice.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.choice[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.choice.html#numpy-random-randomstate-choice "Link to this heading")

========================================================================================================================================================================================

method

random.RandomState.choice(_a_, _size\=None_, _replace\=True_, _p\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.choice.html#numpy.random.RandomState.choice "Link to this definition")

Generates a random sample from a given 1-D array

Note

New code should use the [`choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy.random.Generator.choice "numpy.random.Generator.choice")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Warning

This function uses the C-long dtype, which is 32bit on windows and otherwise 64bit on 64bit platforms (and 32bit on 32bit ones). Since NumPy 2.0, NumPy’s default integer is 32bit on 32bit platforms and 64bit on 64bit platforms.

Parameters:

**a**1-D array-like or int

If an ndarray, a random sample is generated from its elements. If an int, the random sample is generated as if it were `np.arange(a)`

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.

**replace**boolean, optional

Whether the sample is with or without replacement. Default is True, meaning that a value of `a` can be selected multiple times.

**p**1-D array-like, optional

The probabilities associated with each entry in a. If not given, the sample assumes a uniform distribution over all entries in `a`.

Returns:

**samples**single item or ndarray

The generated random samples

Raises:

ValueError

If a is an int and less than zero, if a or p are not 1-dimensional, if a is an array-like of size 0, if p is not a vector of probabilities, if a and p have different lengths, or if replace=False and the sample size is greater than the population size

See also

[`randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.randint.html#numpy.random.RandomState.randint "numpy.random.RandomState.randint")
, [`shuffle`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.shuffle.html#numpy.random.RandomState.shuffle "numpy.random.RandomState.shuffle")
, [`permutation`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.permutation.html#numpy.random.RandomState.permutation "numpy.random.RandomState.permutation")

[`random.Generator.choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html#numpy.random.Generator.choice "numpy.random.Generator.choice")

which should be used in new code

Notes

Setting user-specified probabilities through `p` uses a more general but less efficient sampler than the default. The general sampler produces a different sample than the optimized sampler even if each element of `p` is 1 / len(a).

Sampling random rows from a 2-D array is not possible with this function, but is possible with _Generator.choice_ through its `axis` keyword.

Examples

Try it in your browser!

Generate a uniform random sample from np.arange(5) of size 3:

\>>> np.random.choice(5, 3)
array(\[0, 3, 4\]) # random
\>>> #This is equivalent to np.random.randint(0,5,3)

Copy to clipboard

Generate a non-uniform random sample from np.arange(5) of size 3:

\>>> np.random.choice(5, 3, p\=\[0.1, 0, 0.3, 0.6, 0\])
array(\[3, 3, 0\]) # random

Copy to clipboard

Generate a uniform random sample from np.arange(5) of size 3 without replacement:

\>>> np.random.choice(5, 3, replace\=False)
array(\[3,1,0\]) # random
\>>> #This is equivalent to np.random.permutation(np.arange(5))\[:3\]

Copy to clipboard

Generate a non-uniform random sample from np.arange(5) of size 3 without replacement:

\>>> np.random.choice(5, 3, replace\=False, p\=\[0.1, 0, 0.3, 0.6, 0\])
array(\[2, 3, 0\]) # random

Copy to clipboard

Any of the above can be repeated with an arbitrary array-like instead of just integers. For instance:

\>>> aa\_milne\_arr \= \['pooh', 'rabbit', 'piglet', 'Christopher'\]
\>>> np.random.choice(aa\_milne\_arr, 5, p\=\[0.5, 0.1, 0.1, 0.3\])
array(\['pooh', 'pooh', 'pooh', 'Christopher', 'piglet'\], # random
      dtype='<U11')

Copy to clipboard

Go BackOpen In Tab

On this page