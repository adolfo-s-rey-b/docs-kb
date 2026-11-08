[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.normal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.normal.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.normal.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.normal.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.normal.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.normal.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.normal.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.normal.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.normal.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.normal.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.normal.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.normal.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.normal.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.normal.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.normal.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.normal.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.normal.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.normal.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.normal.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.normal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.normal[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html#numpy-random-randomstate-normal "Link to this heading")

========================================================================================================================================================================================

method

random.RandomState.normal(_loc\=0.0_, _scale\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html#numpy.random.RandomState.normal "Link to this definition")

Draw random samples from a normal (Gaussian) distribution.

The probability density function of the normal distribution, first derived by De Moivre and 200 years later by both Gauss and Laplace independently [\[2\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html#ra2e838c5ea87-2)
, is often called the bell curve because of its characteristic shape (see the example below).

The normal distributions occurs often in nature. For example, it describes the commonly occurring distribution of samples influenced by a large number of tiny, random disturbances, each with its own unique distribution [\[2\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html#ra2e838c5ea87-2)
.

Note

New code should use the [`normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal "numpy.random.Generator.normal")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**loc**float or array\_like of floats

Mean (“centre”) of the distribution.

**scale**float or array\_like of floats

Standard deviation (spread or “width”) of the distribution. Must be non-negative.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `loc` and `scale` are both scalars. Otherwise, `np.broadcast(loc, scale).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized normal distribution.

See also

[`scipy.stats.norm`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm "(in SciPy v1.18.0)")

probability density function, distribution or cumulative density function, etc.

[`random.Generator.normal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal "numpy.random.Generator.normal")

which should be used for new code.

Notes

The probability density for the Gaussian distribution is

\\\[p(x) = \\frac{1}{\\sqrt{ 2 \\pi \\sigma^2 }} e^{ - \\frac{ (x - \\mu)^2 } {2 \\sigma^2} },\\\]

where \\(\\mu\\) is the mean and \\(\\sigma\\) the standard deviation. The square of the standard deviation, \\(\\sigma^2\\), is called the variance.

The function has its peak at the mean, and its “spread” increases with the standard deviation (the function reaches 0.607 times its maximum at \\(x + \\sigma\\) and \\(x - \\sigma\\) [\[2\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html#ra2e838c5ea87-2)
). This implies that normal is more likely to return samples lying close to the mean, rather than those far away.

References

\[1\]

Wikipedia, “Normal distribution”, [https://en.wikipedia.org/wiki/Normal\_distribution](https://en.wikipedia.org/wiki/Normal_distribution)

\[2\] ([1](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html#id1)
,[2](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html#id2)
,[3](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.normal.html#id3)
)

P. R. Peebles Jr., “Central Limit Theorem” in “Probability, Random Variables and Random Signal Principles”, 4th ed., 2001, pp. 51, 51, 125.

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> mu, sigma \= 0, 0.1 \# mean and standard deviation
\>>> s \= np.random.normal(mu, sigma, 1000)

Copy to clipboard

Verify the mean and the standard deviation:

\>>> abs(mu \- np.mean(s))
0.0  # may vary

Copy to clipboard

\>>> abs(sigma \- np.std(s, ddof\=1))
0.0  # may vary

Copy to clipboard

Display the histogram of the samples, along with the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> count, bins, ignored \= plt.hist(s, 30, density\=True)
\>>> plt.plot(bins, 1/(sigma \* np.sqrt(2 \* np.pi)) \*
...                np.exp( \- (bins \- mu)\*\*2 / (2 \* sigma\*\*2) ),
...          linewidth\=2, color\='r')
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-RandomState-normal-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-random-RandomState-normal-1_00_00.png)

Two-by-four array of samples from the normal distribution with mean 3 and standard deviation 2.5:

\>>> np.random.normal(3, 2.5, size\=(2, 4))
array(\[\[-4.49401501,  4.00950034, -1.81814867,  7.29718677\],   # random\
       \[ 0.39924804,  4.68456316,  4.99394529,  4.84057254\]\])  # random

Copy to clipboard

Go BackOpen In Tab

On this page