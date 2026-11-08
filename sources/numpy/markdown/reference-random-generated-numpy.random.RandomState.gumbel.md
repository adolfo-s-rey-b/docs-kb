[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.gumbel.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.gumbel.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.gumbel.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.gumbel.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.gumbel.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.gumbel.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.gumbel.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.gumbel.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.gumbel.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.gumbel[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.gumbel.html#numpy-random-randomstate-gumbel "Link to this heading")

========================================================================================================================================================================================

method

random.RandomState.gumbel(_loc\=0.0_, _scale\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.gumbel.html#numpy.random.RandomState.gumbel "Link to this definition")

Draw samples from a Gumbel distribution.

Draw samples from a Gumbel distribution with specified location and scale. For more information on the Gumbel distribution, see Notes and References below.

Note

New code should use the [`gumbel`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.gumbel.html#numpy.random.Generator.gumbel "numpy.random.Generator.gumbel")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**loc**float or array\_like of floats, optional

The location of the mode of the distribution. Default is 0.

**scale**float or array\_like of floats, optional

The scale parameter of the distribution. Default is 1. Must be non- negative.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `loc` and `scale` are both scalars. Otherwise, `np.broadcast(loc, scale).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized Gumbel distribution.

See also

[`scipy.stats.gumbel_l`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gumbel_l.html#scipy.stats.gumbel_l "(in SciPy v1.18.0)")

[`scipy.stats.gumbel_r`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gumbel_r.html#scipy.stats.gumbel_r "(in SciPy v1.18.0)")

[`scipy.stats.genextreme`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genextreme.html#scipy.stats.genextreme "(in SciPy v1.18.0)")

[`weibull`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.weibull.html#numpy.random.RandomState.weibull "numpy.random.RandomState.weibull")

[`random.Generator.gumbel`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.gumbel.html#numpy.random.Generator.gumbel "numpy.random.Generator.gumbel")

which should be used for new code.

Notes

The Gumbel (or Smallest Extreme Value (SEV) or the Smallest Extreme Value Type I) distribution is one of a class of Generalized Extreme Value (GEV) distributions used in modeling extreme value problems. The Gumbel is a special case of the Extreme Value Type I distribution for maximums from distributions with “exponential-like” tails.

The probability density for the Gumbel distribution is

where \\mu is the mode, a location parameter, and \\beta is the scale parameter.

The Gumbel (named for German mathematician Emil Julius Gumbel) was used very early in the hydrology literature, for modeling the occurrence of flood events. It is also used for modeling maximum wind speed and rainfall rates. It is a “fat-tailed” distribution - the probability of an event in the tail of the distribution is larger than if one used a Gaussian, hence the surprisingly frequent occurrence of 100-year floods. Floods were initially modeled as a Gaussian process, which underestimated the frequency of extreme events.

It is one of a class of extreme value distributions, the Generalized Extreme Value (GEV) distributions, which also includes the Weibull and Frechet.

The function has a mean of \\mu + 0.57721\\beta and a variance of \\frac{\\pi^2}{6}\\beta^2.

References

\[1\]

Gumbel, E. J., “Statistics of Extremes,” New York: Columbia University Press, 1958.

\[2\]

Reiss, R.-D. and Thomas, M., “Statistical Analysis of Extreme Values from Insurance, Finance, Hydrology and Other Fields,” Basel: Birkhauser Verlag, 2001.

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> mu, beta \= 0, 0.1 \# location and scale
\>>> s \= np.random.gumbel(mu, beta, 1000)

Copy to clipboard

Display the histogram of the samples, along with the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> count, bins, ignored \= plt.hist(s, 30, density\=True)
\>>> plt.plot(bins, (1/beta)\*np.exp(\-(bins \- mu)/beta)
...          \* np.exp( \-np.exp( \-(bins \- mu) /beta) ),
...          linewidth\=2, color\='r')
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-RandomState-gumbel-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-random-RandomState-gumbel-1_00_00.png)

Show how an extreme value distribution can arise from a Gaussian process and compare to a Gaussian:

\>>> means \= \[\]
\>>> maxima \= \[\]
\>>> for i in range(0,1000) :
...    a \= np.random.normal(mu, beta, 1000)
...    means.append(a.mean())
...    maxima.append(a.max())
\>>> count, bins, ignored \= plt.hist(maxima, 30, density\=True)
\>>> beta \= np.std(maxima) \* np.sqrt(6) / np.pi
\>>> mu \= np.mean(maxima) \- 0.57721\*beta
\>>> plt.plot(bins, (1/beta)\*np.exp(\-(bins \- mu)/beta)
...          \* np.exp(\-np.exp(\-(bins \- mu)/beta)),
...          linewidth\=2, color\='r')
\>>> plt.plot(bins, 1/(beta \* np.sqrt(2 \* np.pi))
...          \* np.exp(\-(bins \- mu)\*\*2 / (2 \* beta\*\*2)),
...          linewidth\=2, color\='g')
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-RandomState-gumbel-1_01_00.png](https://numpy.org/doc/stable/_images/numpy-random-RandomState-gumbel-1_01_00.png)

Go BackOpen In Tab

On this page