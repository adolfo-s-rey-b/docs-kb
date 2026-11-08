[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.laplace.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.laplace.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.laplace.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.laplace.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.laplace.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.laplace.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.laplace.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.laplace.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.laplace.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.laplace.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.laplace.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.laplace.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.laplace.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.laplace.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.laplace.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.laplace.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.laplace.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.laplace.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.laplace.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.laplace.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.laplace.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.laplace.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.laplace[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.laplace.html#numpy-random-laplace "Link to this heading")

=======================================================================================================================================================

random.laplace(_loc\=0.0_, _scale\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.laplace.html#numpy.random.laplace "Link to this definition")

Draw samples from the Laplace or double exponential distribution with specified location (or mean) and scale (decay).

The Laplace distribution is similar to the Gaussian/normal distribution, but is sharper at the peak and has fatter tails. It represents the difference between two independent, identically distributed exponential random variables.

Note

New code should use the [`laplace`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.laplace.html#numpy.random.Generator.laplace "numpy.random.Generator.laplace")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**loc**float or array\_like of floats, optional

The position, \\(\\mu\\), of the distribution peak. Default is 0.

**scale**float or array\_like of floats, optional

\\(\\lambda\\), the exponential decay. Default is 1. Must be non- negative.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `loc` and `scale` are both scalars. Otherwise, `np.broadcast(loc, scale).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized Laplace distribution.

See also

[`random.Generator.laplace`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.laplace.html#numpy.random.Generator.laplace "numpy.random.Generator.laplace")

which should be used for new code.

Notes

It has the probability density function

\\\[f(x; \\mu, \\lambda) = \\frac{1}{2\\lambda} \\exp\\left(-\\frac{|x - \\mu|}{\\lambda}\\right).\\\]

The first law of Laplace, from 1774, states that the frequency of an error can be expressed as an exponential function of the absolute magnitude of the error, which leads to the Laplace distribution. For many problems in economics and health sciences, this distribution seems to model the data better than the standard Gaussian distribution.

References

\[1\]

Abramowitz, M. and Stegun, I. A. (Eds.). “Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables, 9th printing,” New York: Dover, 1972.

\[2\]

Kotz, Samuel, et. al. “The Laplace Distribution and Generalizations, “ Birkhauser, 2001.

\[3\]

Weisstein, Eric W. “Laplace Distribution.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/LaplaceDistribution.html](https://mathworld.wolfram.com/LaplaceDistribution.html)

\[4\]

Wikipedia, “Laplace distribution”, [https://en.wikipedia.org/wiki/Laplace\_distribution](https://en.wikipedia.org/wiki/Laplace_distribution)

Examples

Try it in your browser!

Draw samples from the distribution

\>>> loc, scale \= 0., 1.
\>>> s \= np.random.laplace(loc, scale, 1000)

Copy to clipboard

Display the histogram of the samples, along with the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> count, bins, ignored \= plt.hist(s, 30, density\=True)
\>>> x \= np.arange(\-8., 8., .01)
\>>> pdf \= np.exp(\-abs(x\-loc)/scale)/(2.\*scale)
\>>> plt.plot(x, pdf)

Copy to clipboard

Plot Gaussian for comparison:

\>>> g \= (1/(scale \* np.sqrt(2 \* np.pi)) \*
...      np.exp(\-(x \- loc)\*\*2 / (2 \* scale\*\*2)))
\>>> plt.plot(x,g)

Copy to clipboard

![../../../_images/numpy-random-laplace-1.png](https://numpy.org/doc/stable/_images/numpy-random-laplace-1.png)

Go BackOpen In Tab

On this page