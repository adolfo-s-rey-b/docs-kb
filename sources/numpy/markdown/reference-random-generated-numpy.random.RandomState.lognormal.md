[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.lognormal.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.lognormal.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.lognormal.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.lognormal.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.lognormal.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.lognormal.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.lognormal.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.lognormal.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.lognormal.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.lognormal[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.lognormal.html#numpy-random-randomstate-lognormal "Link to this heading")

=================================================================================================================================================================================================

method

random.RandomState.lognormal(_mean\=0.0_, _sigma\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.lognormal.html#numpy.random.RandomState.lognormal "Link to this definition")

Draw samples from a log-normal distribution.

Draw samples from a log-normal distribution with specified mean, standard deviation, and array shape. Note that the mean and standard deviation are not the values for the distribution itself, but of the underlying normal distribution it is derived from.

Note

New code should use the [`lognormal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.lognormal.html#numpy.random.Generator.lognormal "numpy.random.Generator.lognormal")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**mean**float or array\_like of floats, optional

Mean value of the underlying normal distribution. Default is 0.

**sigma**float or array\_like of floats, optional

Standard deviation of the underlying normal distribution. Must be non-negative. Default is 1.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `mean` and `sigma` are both scalars. Otherwise, `np.broadcast(mean, sigma).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized log-normal distribution.

See also

[`scipy.stats.lognorm`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lognorm.html#scipy.stats.lognorm "(in SciPy v1.18.0)")

probability density function, distribution, cumulative density function, etc.

[`random.Generator.lognormal`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.lognormal.html#numpy.random.Generator.lognormal "numpy.random.Generator.lognormal")

which should be used for new code.

Notes

A variable _x_ has a log-normal distribution if _log(x)_ is normally distributed. The probability density function for the log-normal distribution is:

\\\[p(x) = \\frac{1}{\\sigma x \\sqrt{2\\pi}} e^{(-\\frac{(ln(x)-\\mu)^2}{2\\sigma^2})}\\\]

where \\(\\mu\\) is the mean and \\(\\sigma\\) is the standard deviation of the normally distributed logarithm of the variable. A log-normal distribution results if a random variable is the _product_ of a large number of independent, identically-distributed variables in the same way that a normal distribution results if the variable is the _sum_ of a large number of independent, identically-distributed variables.

References

\[1\]

Limpert, E., Stahel, W. A., and Abbt, M., “Log-normal Distributions across the Sciences: Keys and Clues,” BioScience, Vol. 51, No. 5, May, 2001. [https://stat.ethz.ch/~stahel/lognormal/bioscience.pdf](https://stat.ethz.ch/~stahel/lognormal/bioscience.pdf)

\[2\]

Reiss, R.D. and Thomas, M., “Statistical Analysis of Extreme Values,” Basel: Birkhauser Verlag, 2001, pp. 31-32.

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> mu, sigma \= 3., 1. \# mean and standard deviation
\>>> s \= np.random.lognormal(mu, sigma, 1000)

Copy to clipboard

Display the histogram of the samples, along with the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> count, bins, ignored \= plt.hist(s, 100, density\=True, align\='mid')

Copy to clipboard

\>>> x \= np.linspace(min(bins), max(bins), 10000)
\>>> pdf \= (np.exp(\-(np.log(x) \- mu)\*\*2 / (2 \* sigma\*\*2))
...        / (x \* sigma \* np.sqrt(2 \* np.pi)))

Copy to clipboard

\>>> plt.plot(x, pdf, linewidth\=2, color\='r')
\>>> plt.axis('tight')
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-RandomState-lognormal-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-random-RandomState-lognormal-1_00_00.png)

Demonstrate that taking the products of random samples from a uniform distribution can be fit well by a log-normal probability density function.

\>>> \# Generate a thousand samples: each is the product of 100 random
\>>> \# values, drawn from a normal distribution.
\>>> b \= \[\]
\>>> for i in range(1000):
...    a \= 10. + np.random.standard\_normal(100)
...    b.append(np.prod(a))

Copy to clipboard

\>>> b \= np.array(b) / np.min(b) \# scale values to be positive
\>>> count, bins, ignored \= plt.hist(b, 100, density\=True, align\='mid')
\>>> sigma \= np.std(np.log(b))
\>>> mu \= np.mean(np.log(b))

Copy to clipboard

\>>> x \= np.linspace(min(bins), max(bins), 10000)
\>>> pdf \= (np.exp(\-(np.log(x) \- mu)\*\*2 / (2 \* sigma\*\*2))
...        / (x \* sigma \* np.sqrt(2 \* np.pi)))

Copy to clipboard

\>>> plt.plot(x, pdf, color\='r', linewidth\=2)
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-RandomState-lognormal-1_01_00.png](https://numpy.org/doc/stable/_images/numpy-random-RandomState-lognormal-1_01_00.png)

Go BackOpen In Tab

On this page