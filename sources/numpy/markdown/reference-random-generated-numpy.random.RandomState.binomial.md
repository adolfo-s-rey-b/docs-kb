[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.binomial.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.binomial.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.binomial.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.binomial.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.binomial.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.binomial.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.binomial.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.binomial.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.binomial.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.binomial[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.binomial.html#numpy-random-randomstate-binomial "Link to this heading")

==============================================================================================================================================================================================

method

random.RandomState.binomial(_n_, _p_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.binomial.html#numpy.random.RandomState.binomial "Link to this definition")

Draw samples from a binomial distribution.

Samples are drawn from a binomial distribution with specified parameters, n trials and p probability of success where n an integer >= 0 and p is in the interval \[0,1\]. (n may be input as a float, but it is truncated to an integer in use)

Note

New code should use the [`binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.binomial.html#numpy.random.Generator.binomial "numpy.random.Generator.binomial")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**n**int or array\_like of ints

Parameter of the distribution, >= 0. Floats are also accepted, but they will be truncated to integers.

**p**float or array\_like of floats

Parameter of the distribution, >= 0 and <=1.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `n` and `p` are both scalars. Otherwise, `np.broadcast(n, p).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized binomial distribution, where each sample is equal to the number of successes over the n trials.

See also

[`scipy.stats.binom`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html#scipy.stats.binom "(in SciPy v1.18.0)")

probability density function, distribution or cumulative density function, etc.

[`random.Generator.binomial`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.binomial.html#numpy.random.Generator.binomial "numpy.random.Generator.binomial")

which should be used for new code.

Notes

The probability mass function (PMF) for the binomial distribution is

\\\[P(N) = \\binom{n}{N}p^N(1-p)^{n-N},\\\]

where \\(n\\) is the number of trials, \\(p\\) is the probability of success, and \\(N\\) is the number of successes.

When estimating the standard error of a proportion in a population by using a random sample, the normal distribution works well unless the product p\*n <=5, where p = population proportion estimate, and n = number of samples, in which case the binomial distribution is used instead. For example, a sample of 15 people shows 4 who are left handed, and 11 who are right handed. Then p = 4/15 = 27%. 0.27\*15 = 4, so the binomial distribution should be used in this case.

References

\[1\]

Dalgaard, Peter, “Introductory Statistics with R”, Springer-Verlag, 2002.

\[2\]

Glantz, Stanton A. “Primer of Biostatistics.”, McGraw-Hill, Fifth Edition, 2002.

\[3\]

Lentner, Marvin, “Elementary Applied Statistics”, Bogden and Quigley, 1972.

\[4\]

Weisstein, Eric W. “Binomial Distribution.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/BinomialDistribution.html](https://mathworld.wolfram.com/BinomialDistribution.html)

\[5\]

Wikipedia, “Binomial distribution”, [https://en.wikipedia.org/wiki/Binomial\_distribution](https://en.wikipedia.org/wiki/Binomial_distribution)

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> n, p \= 10, .5  \# number of trials, probability of each trial
\>>> s \= np.random.binomial(n, p, 1000)
\# result of flipping a coin 10 times, tested 1000 times.

Copy to clipboard

A real world example. A company drills 9 wild-cat oil exploration wells, each with an estimated probability of success of 0.1. All nine wells fail. What is the probability of that happening?

Let’s do 20,000 trials of the model, and count the number that generate zero positive results.

\>>> sum(np.random.binomial(9, 0.1, 20000) \== 0)/20000.
\# answer = 0.38885, or 38%.

Copy to clipboard

Go BackOpen In Tab

On this page