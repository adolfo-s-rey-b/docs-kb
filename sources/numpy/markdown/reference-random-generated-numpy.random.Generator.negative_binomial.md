[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.negative_binomial.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.negative\_binomial[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.negative_binomial.html#numpy-random-generator-negative-binomial "Link to this heading")

====================================================================================================================================================================================================================

method

random.Generator.negative\_binomial(_n_, _p_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.negative_binomial.html#numpy.random.Generator.negative_binomial "Link to this definition")

Draw samples from a negative binomial distribution.

Samples are drawn from a negative binomial distribution with specified parameters, _n_ successes and _p_ probability of success where _n_ is > 0 and _p_ is in the interval (0, 1\].

Parameters:

**n**float or array\_like of floats

Parameter of the distribution, > 0.

**p**float or array\_like of floats

Parameter of the distribution. Must satisfy 0 < p <= 1.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `n` and `p` are both scalars. Otherwise, `np.broadcast(n, p).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized negative binomial distribution, where each sample is equal to N, the number of failures that occurred before a total of n successes was reached.

Notes

The probability mass function of the negative binomial distribution is

\\\[P(N;n,p) = \\frac{\\Gamma(N+n)}{N!\\Gamma(n)}p^{n}(1-p)^{N},\\\]

where \\(n\\) is the number of successes, \\(p\\) is the probability of success, \\(N+n\\) is the number of trials, and \\(\\Gamma\\) is the gamma function. When \\(n\\) is an integer, \\(\\frac{\\Gamma(N+n)}{N!\\Gamma(n)} = \\binom{N+n-1}{N}\\), which is the more common form of this term in the pmf. The negative binomial distribution gives the probability of N failures given n successes, with a success on the last trial.

If one throws a die repeatedly until the third time a “1” appears, then the probability distribution of the number of non-“1”s that appear before the third “1” is a negative binomial distribution.

Because this method internally calls `Generator.poisson` with an intermediate random value, a ValueError is raised when the choice of \\(n\\) and \\(p\\) would result in the mean + 10 sigma of the sampled intermediate distribution exceeding the max acceptable value of the `Generator.poisson` method. This happens when \\(p\\) is too low (a lot of failures happen for every success) and \\(n\\) is too big ( a lot of successes are allowed). Therefore, the \\(n\\) and \\(p\\) values must satisfy the constraint:

\\\[n\\frac{1-p}{p}+10n\\sqrt{n}\\frac{1-p}{p}<2^{63}-1-10\\sqrt{2^{63}-1},\\\]

Where the left side of the equation is the derived mean + 10 sigma of a sample from the gamma distribution internally used as the \\(lam\\) parameter of a poisson sample, and the right side of the equation is the constraint for maximum value of \\(lam\\) in `Generator.poisson`.

References

\[1\]

Weisstein, Eric W. “Negative Binomial Distribution.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/NegativeBinomialDistribution.html](https://mathworld.wolfram.com/NegativeBinomialDistribution.html)

\[2\]

Wikipedia, “Negative binomial distribution”, [https://en.wikipedia.org/wiki/Negative\_binomial\_distribution](https://en.wikipedia.org/wiki/Negative_binomial_distribution)

Examples

Try it in your browser!

Draw samples from the distribution:

A real world example. A company drills wild-cat oil exploration wells, each with an estimated probability of success of 0.1. What is the probability of having one success for each successive well, that is what is the probability of a single success after drilling 5 wells, after 6 wells, etc.?

\>>> rng \= np.random.default\_rng()
\>>> s \= rng.negative\_binomial(1, 0.1, 100000)
\>>> for i in range(1, 11): 
...    probability \= sum(s<i) / 100000.
...    print(i, "wells drilled, probability of one success =", probability)

Copy to clipboard

Go BackOpen In Tab

On this page