[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_cauchy.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.standard_cauchy.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_cauchy.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.standard_cauchy.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.standard_cauchy.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.standard_cauchy.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.standard_cauchy.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.standard_cauchy.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.standard_cauchy.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.standard_cauchy.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.standard_cauchy.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.standard_cauchy.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.standard_cauchy.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.standard_cauchy.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.standard_cauchy.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.standard_cauchy.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.standard_cauchy.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.standard_cauchy.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.standard_cauchy.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.standard_cauchy.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.standard_cauchy.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.standard_cauchy.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.standard\_cauchy[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_cauchy.html#numpy-random-standard-cauchy "Link to this heading")

================================================================================================================================================================================

random.standard\_cauchy(_size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_cauchy.html#numpy.random.standard_cauchy "Link to this definition")

Draw samples from a standard Cauchy distribution with mode = 0.

Also known as the Lorentz distribution.

Note

New code should use the [`standard_cauchy`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_cauchy.html#numpy.random.Generator.standard_cauchy "numpy.random.Generator.standard_cauchy")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. Default is None, in which case a single value is returned.

Returns:

**samples**ndarray or scalar

The drawn samples.

See also

[`random.Generator.standard_cauchy`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.standard_cauchy.html#numpy.random.Generator.standard_cauchy "numpy.random.Generator.standard_cauchy")

which should be used for new code.

Notes

The probability density function for the full Cauchy distribution is

\\\[P(x; x\_0, \\gamma) = \\frac{1}{\\pi \\gamma \\bigl\[ 1+ (\\frac{x-x\_0}{\\gamma})^2 \\bigr\] }\\\]

and the Standard Cauchy distribution just sets \\(x\_0=0\\) and \\(\\gamma=1\\)

The Cauchy distribution arises in the solution to the driven harmonic oscillator problem, and also describes spectral line broadening. It also describes the distribution of values at which a line tilted at a random angle will cut the x axis.

When studying hypothesis tests that assume normality, seeing how the tests perform on data from a Cauchy distribution is a good indicator of their sensitivity to a heavy-tailed distribution, since the Cauchy looks very much like a Gaussian distribution, but with heavier tails.

References

\[1\]

NIST/SEMATECH e-Handbook of Statistical Methods, “Cauchy Distribution”, [https://www.itl.nist.gov/div898/handbook/eda/section3/eda3663.htm](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3663.htm)

\[2\]

Weisstein, Eric W. “Cauchy Distribution.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/CauchyDistribution.html](https://mathworld.wolfram.com/CauchyDistribution.html)

\[3\]

Wikipedia, “Cauchy distribution” [https://en.wikipedia.org/wiki/Cauchy\_distribution](https://en.wikipedia.org/wiki/Cauchy_distribution)

Examples

Try it in your browser!

Draw samples and plot the distribution:

\>>> import matplotlib.pyplot as plt
\>>> s \= np.random.standard\_cauchy(1000000)
\>>> s \= s\[(s\>-25) & (s<25)\]  \# truncate distribution so it plots well
\>>> plt.hist(s, bins\=100)
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-standard_cauchy-1.png](https://numpy.org/doc/stable/_images/numpy-random-standard_cauchy-1.png)

Go BackOpen In Tab

On this page