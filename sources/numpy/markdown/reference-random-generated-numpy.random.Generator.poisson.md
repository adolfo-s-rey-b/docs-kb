[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.poisson.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.poisson.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.poisson.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.poisson.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.poisson.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.poisson.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.poisson.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.poisson.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.poisson.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.poisson.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.poisson.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.poisson.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.poisson.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.poisson.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.poisson.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.poisson.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.poisson.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.poisson.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.poisson.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.poisson.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.poisson.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.poisson.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.poisson[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.poisson.html#numpy-random-generator-poisson "Link to this heading")

=====================================================================================================================================================================================

method

random.Generator.poisson(_lam\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.poisson.html#numpy.random.Generator.poisson "Link to this definition")

Draw samples from a Poisson distribution.

The Poisson distribution is the limit of the binomial distribution for large N.

Parameters:

**lam**float or array\_like of floats

Expected number of events occurring in a fixed-time interval, must be >= 0. A sequence must be broadcastable over the requested size.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `lam` is a scalar. Otherwise, `np.array(lam).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized Poisson distribution.

Notes

The probability mass function (PMF) of Poisson distribution is

\\\[f(k; \\lambda)=\\frac{\\lambda^k e^{-\\lambda}}{k!}\\\]

For events with an expected separation \\(\\lambda\\) the Poisson distribution \\(f(k; \\lambda)\\) describes the probability of \\(k\\) events occurring within the observed interval \\(\\lambda\\).

Because the output is limited to the range of the C int64 type, a ValueError is raised when _lam_ is within 10 sigma of the maximum representable value.

References

\[1\]

Weisstein, Eric W. “Poisson Distribution.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/PoissonDistribution.html](https://mathworld.wolfram.com/PoissonDistribution.html)

\[2\]

Wikipedia, “Poisson distribution”, [https://en.wikipedia.org/wiki/Poisson\_distribution](https://en.wikipedia.org/wiki/Poisson_distribution)

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> rng \= np.random.default\_rng()
\>>> lam, size \= 5, 10000
\>>> s \= rng.poisson(lam\=lam, size\=size)

Copy to clipboard

Verify the mean and variance, which should be approximately `lam`:

\>>> s.mean(), s.var()
(4.9917 5.1088311)  # may vary

Copy to clipboard

Display the histogram and probability mass function:

\>>> import matplotlib.pyplot as plt
\>>> from scipy import stats
\>>> x \= np.arange(0, 21)
\>>> pmf \= stats.poisson.pmf(x, mu\=lam)
\>>> plt.hist(s, bins\=x, density\=True, width\=0.5)
\>>> plt.stem(x, pmf, 'C1-')
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-poisson-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-poisson-1_00_00.png)

Draw each 100 values for lambda 100 and 500:

\>>> s \= rng.poisson(lam\=(100., 500.), size\=(100, 2))

Copy to clipboard

Go BackOpen In Tab

On this page