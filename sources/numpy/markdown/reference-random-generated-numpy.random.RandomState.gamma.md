[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.gamma.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.RandomState.gamma.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.gamma.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.RandomState.gamma.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.RandomState.gamma.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.RandomState.gamma.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.RandomState.gamma.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.RandomState.gamma.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.RandomState.gamma.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.RandomState.gamma[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.gamma.html#numpy-random-randomstate-gamma "Link to this heading")

=====================================================================================================================================================================================

method

random.RandomState.gamma(_shape_, _scale\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.RandomState.gamma.html#numpy.random.RandomState.gamma "Link to this definition")

Draw samples from a Gamma distribution.

Samples are drawn from a Gamma distribution with specified parameters, [`shape`](https://numpy.org/doc/stable/reference/generated/numpy.shape.html#numpy.shape "numpy.shape")
 (sometimes designated “k”) and _scale_ (sometimes designated “theta”), where both parameters are > 0.

Note

New code should use the [`gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.gamma.html#numpy.random.Generator.gamma "numpy.random.Generator.gamma")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**shape**float or array\_like of floats

The shape of the gamma distribution. Must be non-negative.

**scale**float or array\_like of floats, optional

The scale of the gamma distribution. Must be non-negative. Default is equal to 1.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `shape` and `scale` are both scalars. Otherwise, `np.broadcast(shape, scale).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized gamma distribution.

See also

[`scipy.stats.gamma`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.gamma.html#scipy.stats.gamma "(in SciPy v1.18.0)")

probability density function, distribution or cumulative density function, etc.

[`random.Generator.gamma`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.gamma.html#numpy.random.Generator.gamma "numpy.random.Generator.gamma")

which should be used for new code.

Notes

The probability density for the Gamma distribution is

where k is the shape and \\theta the scale, and \\Gamma is the Gamma function.

The Gamma distribution is often used to model the times to failure of electronic components, and arises naturally in processes for which the waiting times between Poisson distributed events are relevant.

References

\[1\]

Weisstein, Eric W. “Gamma Distribution.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/GammaDistribution.html](https://mathworld.wolfram.com/GammaDistribution.html)

\[2\]

Wikipedia, “Gamma distribution”, [https://en.wikipedia.org/wiki/Gamma\_distribution](https://en.wikipedia.org/wiki/Gamma_distribution)

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> shape, scale \= 2., 2.  \# mean=4, std=2\*sqrt(2)
\>>> s \= np.random.gamma(shape, scale, 1000)

Copy to clipboard

Display the histogram of the samples, along with the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> import scipy.special as sps  
\>>> count, bins, ignored \= plt.hist(s, 50, density\=True)
\>>> y \= bins\*\*(shape\-1)\*(np.exp(\-bins/scale) /  
...                      (sps.gamma(shape)\*scale\*\*shape))
\>>> plt.plot(bins, y, linewidth\=2, color\='r')  
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-RandomState-gamma-1.png](https://numpy.org/doc/stable/_images/numpy-random-RandomState-gamma-1.png)

Go BackOpen In Tab

On this page