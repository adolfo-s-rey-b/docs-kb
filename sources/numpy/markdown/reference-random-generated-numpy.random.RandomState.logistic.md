[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.logistic.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.logistic.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.logistic.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.logistic.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.logistic.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.logistic.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.logistic.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.logistic.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.logistic.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.logistic[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.logistic.html#numpy-random-randomstate-logistic "Link to this heading")

==============================================================================================================================================================================================

method

random.RandomState.logistic(_loc\=0.0_, _scale\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.logistic.html#numpy.random.RandomState.logistic "Link to this definition")

Draw samples from a logistic distribution.

Samples are drawn from a logistic distribution with specified parameters, loc (location or mean, also median), and scale (>0).

Note

New code should use the [`logistic`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logistic.html#numpy.random.Generator.logistic "numpy.random.Generator.logistic")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**loc**float or array\_like of floats, optional

Parameter of the distribution. Default is 0.

**scale**float or array\_like of floats, optional

Parameter of the distribution. Must be non-negative. Default is 1.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `loc` and `scale` are both scalars. Otherwise, `np.broadcast(loc, scale).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized logistic distribution.

See also

[`scipy.stats.logistic`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.logistic.html#scipy.stats.logistic "(in SciPy v1.18.0)")

probability density function, distribution or cumulative density function, etc.

[`random.Generator.logistic`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.logistic.html#numpy.random.Generator.logistic "numpy.random.Generator.logistic")

which should be used for new code.

Notes

The probability density for the Logistic distribution is

where \\mu = location and s = scale.

The Logistic distribution is used in Extreme Value problems where it can act as a mixture of Gumbel distributions, in Epidemiology, and by the World Chess Federation (FIDE) where it is used in the Elo ranking system, assuming the performance of each player is a logistically distributed random variable.

References

\[1\]

Reiss, R.-D. and Thomas M. (2001), “Statistical Analysis of Extreme Values, from Insurance, Finance, Hydrology and Other Fields,” Birkhauser Verlag, Basel, pp 132-133.

\[2\]

Weisstein, Eric W. “Logistic Distribution.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/LogisticDistribution.html](https://mathworld.wolfram.com/LogisticDistribution.html)

\[3\]

Wikipedia, “Logistic-distribution”, [https://en.wikipedia.org/wiki/Logistic\_distribution](https://en.wikipedia.org/wiki/Logistic_distribution)

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> loc, scale \= 10, 1
\>>> s \= np.random.logistic(loc, scale, 10000)
\>>> import matplotlib.pyplot as plt
\>>> count, bins, ignored \= plt.hist(s, bins\=50)

Copy to clipboard

\# plot against distribution

\>>> def logist(x, loc, scale):
...     return np.exp((loc\-x)/scale)/(scale\*(1+np.exp((loc\-x)/scale))\*\*2)
\>>> lgst\_val \= logist(bins, loc, scale)
\>>> plt.plot(bins, lgst\_val \* count.max() / lgst\_val.max())
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-RandomState-logistic-1.png](https://numpy.org/doc/stable/_images/numpy-random-RandomState-logistic-1.png)

Go BackOpen In Tab

On this page