[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.hypergeometric.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.hypergeometric.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.hypergeometric.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.hypergeometric[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.hypergeometric.html#numpy-random-randomstate-hypergeometric "Link to this heading")

================================================================================================================================================================================================================

method

random.RandomState.hypergeometric(_ngood_, _nbad_, _nsample_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.hypergeometric.html#numpy.random.RandomState.hypergeometric "Link to this definition")

Draw samples from a Hypergeometric distribution.

Samples are drawn from a hypergeometric distribution with specified parameters, _ngood_ (ways to make a good selection), _nbad_ (ways to make a bad selection), and _nsample_ (number of items sampled, which is less than or equal to the sum `ngood + nbad`).

Note

New code should use the [`hypergeometric`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.hypergeometric.html#numpy.random.Generator.hypergeometric "numpy.random.Generator.hypergeometric")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**ngood**int or array\_like of ints

Number of ways to make a good selection. Must be nonnegative.

**nbad**int or array\_like of ints

Number of ways to make a bad selection. Must be nonnegative.

**nsample**int or array\_like of ints

Number of items sampled. Must be at least 1 and at most `ngood + nbad`.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if _ngood_, _nbad_, and _nsample_ are all scalars. Otherwise, `np.broadcast(ngood, nbad, nsample).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized hypergeometric distribution. Each sample is the number of good items within a randomly selected subset of size _nsample_ taken from a set of _ngood_ good items and _nbad_ bad items.

See also

[`scipy.stats.hypergeom`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.hypergeom.html#scipy.stats.hypergeom "(in SciPy v1.18.0)")

probability density function, distribution or cumulative density function, etc.

[`random.Generator.hypergeometric`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.hypergeometric.html#numpy.random.Generator.hypergeometric "numpy.random.Generator.hypergeometric")

which should be used for new code.

Notes

The probability mass function (PMF) for the Hypergeometric distribution is

\\\[P(x) = \\frac{\\binom{g}{x}\\binom{b}{n-x}}{\\binom{g+b}{n}},\\\]

where \\(0 \\le x \\le n\\) and \\(n-b \\le x \\le g\\)

for P(x) the probability of `x` good results in the drawn sample, g = _ngood_, b = _nbad_, and n = _nsample_.

Consider an urn with black and white marbles in it, _ngood_ of them are black and _nbad_ are white. If you draw _nsample_ balls without replacement, then the hypergeometric distribution describes the distribution of black balls in the drawn sample.

Note that this distribution is very similar to the binomial distribution, except that in this case, samples are drawn without replacement, whereas in the Binomial case samples are drawn with replacement (or the sample space is infinite). As the sample space becomes large, this distribution approaches the binomial.

References

\[1\]

Lentner, Marvin, “Elementary Applied Statistics”, Bogden and Quigley, 1972.

\[2\]

Weisstein, Eric W. “Hypergeometric Distribution.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/HypergeometricDistribution.html](https://mathworld.wolfram.com/HypergeometricDistribution.html)

\[3\]

Wikipedia, “Hypergeometric distribution”, [https://en.wikipedia.org/wiki/Hypergeometric\_distribution](https://en.wikipedia.org/wiki/Hypergeometric_distribution)

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> ngood, nbad, nsamp \= 100, 2, 10
\# number of good, number of bad, and number of samples
\>>> s \= np.random.hypergeometric(ngood, nbad, nsamp, 1000)
\>>> from matplotlib.pyplot import hist
\>>> hist(s)
\#   note that it is very unlikely to grab both bad items

Copy to clipboard

Suppose you have an urn with 15 white and 15 black marbles. If you pull 15 marbles at random, how likely is it that 12 or more of them are one color?

\>>> s \= np.random.hypergeometric(15, 15, 15, 100000)
\>>> sum(s\>=12)/100000. + sum(s<=3)/100000.
\#   answer = 0.003 ... pretty unlikely!

Copy to clipboard

Go BackOpen In Tab

On this page