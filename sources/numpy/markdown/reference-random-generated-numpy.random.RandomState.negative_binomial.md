[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.negative_binomial.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.negative\_binomial[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.negative_binomial.html#numpy-random-randomstate-negative-binomial "Link to this heading")

==========================================================================================================================================================================================================================

method

random.RandomState.negative\_binomial(_n_, _p_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.negative_binomial.html#numpy.random.RandomState.negative_binomial "Link to this definition")

Draw samples from a negative binomial distribution.

Samples are drawn from a negative binomial distribution with specified parameters, _n_ successes and _p_ probability of success where _n_ is > 0 and _p_ is in the interval \[0, 1\].

Note

New code should use the [`negative_binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.negative_binomial.html#numpy.random.Generator.negative_binomial "numpy.random.Generator.negative_binomial")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**n**float or array\_like of floats

Parameter of the distribution, > 0.

**p**float or array\_like of floats

Parameter of the distribution, >= 0 and <=1.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `n` and `p` are both scalars. Otherwise, `np.broadcast(n, p).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized negative binomial distribution, where each sample is equal to N, the number of failures that occurred before a total of n successes was reached.

Warning

This function returns the C-long dtype, which is 32bit on windows and otherwise 64bit on 64bit platforms (and 32bit on 32bit ones). Since NumPy 2.0, NumPy’s default integer is 32bit on 32bit platforms and 64bit on 64bit platforms.

See also

[`random.Generator.negative_binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.negative_binomial.html#numpy.random.Generator.negative_binomial "numpy.random.Generator.negative_binomial")

which should be used for new code.

Notes

The probability mass function of the negative binomial distribution is

\\\[P(N;n,p) = \\frac{\\Gamma(N+n)}{N!\\Gamma(n)}p^{n}(1-p)^{N},\\\]

where \\(n\\) is the number of successes, \\(p\\) is the probability of success, \\(N+n\\) is the number of trials, and \\(\\Gamma\\) is the gamma function. When \\(n\\) is an integer, \\(\\frac{\\Gamma(N+n)}{N!\\Gamma(n)} = \\binom{N+n-1}{N}\\), which is the more common form of this term in the pmf. The negative binomial distribution gives the probability of N failures given n successes, with a success on the last trial.

If one throws a die repeatedly until the third time a “1” appears, then the probability distribution of the number of non-“1”s that appear before the third “1” is a negative binomial distribution.

References

\[1\]

Weisstein, Eric W. “Negative Binomial Distribution.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/NegativeBinomialDistribution.html](https://mathworld.wolfram.com/NegativeBinomialDistribution.html)

\[2\]

Wikipedia, “Negative binomial distribution”, [https://en.wikipedia.org/wiki/Negative\_binomial\_distribution](https://en.wikipedia.org/wiki/Negative_binomial_distribution)

Examples

Try it in your browser!

Draw samples from the distribution:

A real world example. A company drills wild-cat oil exploration wells, each with an estimated probability of success of 0.1. What is the probability of having one success for each successive well, that is what is the probability of a single success after drilling 5 wells, after 6 wells, etc.?

\>>> s \= np.random.negative\_binomial(1, 0.1, 100000)
\>>> for i in range(1, 11): 
...    probability \= sum(s<i) / 100000.
...    print(i, "wells drilled, probability of one success =", probability)

Copy to clipboard

Go BackOpen In Tab

On this page