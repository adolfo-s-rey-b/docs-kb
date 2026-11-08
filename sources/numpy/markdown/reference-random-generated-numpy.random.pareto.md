[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.pareto.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.pareto.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.pareto.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.pareto.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.pareto.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.pareto.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.pareto.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.pareto.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.pareto.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.pareto.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.pareto.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.pareto.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.pareto.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.pareto.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.pareto.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.pareto.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.pareto.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.pareto.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.pareto.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.pareto.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.pareto.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.pareto.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.pareto[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.pareto.html#numpy-random-pareto "Link to this heading")

====================================================================================================================================================

random.pareto(_a_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.pareto.html#numpy.random.pareto "Link to this definition")

Draw samples from a Pareto II or Lomax distribution with specified shape.

The Lomax or Pareto II distribution is a shifted Pareto distribution. The classical Pareto distribution can be obtained from the Lomax distribution by adding 1 and multiplying by the scale parameter `m` (see Notes). The smallest value of the Lomax distribution is zero while for the classical Pareto distribution it is `mu`, where the standard Pareto distribution has location `mu = 1`. Lomax can also be considered as a simplified version of the Generalized Pareto distribution (available in SciPy), with the scale set to one and the location set to zero.

The Pareto distribution must be greater than zero, and is unbounded above. It is also known as the “80-20 rule”. In this distribution, 80 percent of the weights are in the lowest 20 percent of the range, while the other 20 percent fill the remaining 80 percent of the range.

Note

New code should use the [`pareto`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.pareto.html#numpy.random.Generator.pareto "numpy.random.Generator.pareto")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**a**float or array\_like of floats

Shape of the distribution. Must be positive.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `a` is a scalar. Otherwise, `np.array(a).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized Pareto distribution.

See also

[`scipy.stats.lomax`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lomax.html#scipy.stats.lomax "(in SciPy v1.18.0)")

probability density function, distribution or cumulative density function, etc.

[`scipy.stats.genpareto`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genpareto.html#scipy.stats.genpareto "(in SciPy v1.18.0)")

probability density function, distribution or cumulative density function, etc.

[`random.Generator.pareto`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.pareto.html#numpy.random.Generator.pareto "numpy.random.Generator.pareto")

which should be used for new code.

Notes

The probability density for the Pareto II distribution is

\\\[p(x) = \\frac{a}{(x+1)^{a+1}} , x \\ge 0\\\]

where \\(a > 0\\) is the shape.

The Pareto II distribution is a shifted and scaled version of the Pareto I distribution, which can be found in [`scipy.stats.pareto`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pareto.html#scipy.stats.pareto "(in SciPy v1.18.0)")
.

The Pareto distribution, named after the Italian economist Vilfredo Pareto, is a power law probability distribution useful in many real world problems. Outside the field of economics it is generally referred to as the Bradford distribution. Pareto developed the distribution to describe the distribution of wealth in an economy. It has also found use in insurance, web page access statistics, oil field sizes, and many other problems, including the download frequency for projects in Sourceforge [\[1\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.pareto.html#r3973533a530a-1)
. It is one of the so-called “fat-tailed” distributions.

References

\[[1](https://numpy.org/doc/stable/reference/random/generated/numpy.random.pareto.html#id1)\
\]

Francis Hunt and Paul Johnson, On the Pareto Distribution of Sourceforge projects.

\[2\]

Pareto, V. (1896). Course of Political Economy. Lausanne.

\[3\]

Reiss, R.D., Thomas, M.(2001), Statistical Analysis of Extreme Values, Birkhauser Verlag, Basel, pp 23-30.

\[4\]

Wikipedia, “Pareto distribution”, [https://en.wikipedia.org/wiki/Pareto\_distribution](https://en.wikipedia.org/wiki/Pareto_distribution)

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> a, m \= 3., 2.  \# shape and mode
\>>> s \= (np.random.pareto(a, 1000) + 1) \* m

Copy to clipboard

Display the histogram of the samples, along with the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> count, bins, \_ \= plt.hist(s, 100, density\=True)
\>>> fit \= a\*m\*\*a / bins\*\*(a+1)
\>>> plt.plot(bins, max(count)\*fit/max(fit), linewidth\=2, color\='r')
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-pareto-1.png](https://numpy.org/doc/stable/_images/numpy-random-pareto-1.png)

Go BackOpen In Tab

On this page