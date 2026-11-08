[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.rayleigh.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.rayleigh.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.rayleigh.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.rayleigh.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.rayleigh.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.rayleigh.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.rayleigh.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.rayleigh.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.rayleigh.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.rayleigh[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.rayleigh.html#numpy-random-generator-rayleigh "Link to this heading")

========================================================================================================================================================================================

method

random.Generator.rayleigh(_scale\=1.0_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.rayleigh.html#numpy.random.Generator.rayleigh "Link to this definition")

Draw samples from a Rayleigh distribution.

The \\(\\chi\\) and Weibull distributions are generalizations of the Rayleigh.

Parameters:

**scale**float or array\_like of floats, optional

Scale, also equals the mode. Must be non-negative. Default is 1.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `scale` is a scalar. Otherwise, `np.array(scale).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized Rayleigh distribution.

Notes

The probability density function for the Rayleigh distribution is

\\\[P(x;scale) = \\frac{x}{scale^2}e^{\\frac{-x^2}{2 \\cdotp scale^2}}\\\]

The Rayleigh distribution would arise, for example, if the East and North components of the wind velocity had identical zero-mean Gaussian distributions. Then the wind speed would have a Rayleigh distribution.

References

\[1\]

Brighton Webs Ltd., “Rayleigh Distribution,” [https://web.archive.org/web/20090514091424/http://brighton-webs.co.uk:80/distributions/rayleigh.asp](https://web.archive.org/web/20090514091424/http://brighton-webs.co.uk:80/distributions/rayleigh.asp)

\[2\]

Wikipedia, “Rayleigh distribution” [https://en.wikipedia.org/wiki/Rayleigh\_distribution](https://en.wikipedia.org/wiki/Rayleigh_distribution)

Examples

Try it in your browser!

Draw values from the distribution and plot the histogram

\>>> from matplotlib.pyplot import hist
\>>> rng \= np.random.default\_rng()
\>>> values \= hist(rng.rayleigh(3, 100000), bins\=200, density\=True)

Copy to clipboard

Wave heights tend to follow a Rayleigh distribution. If the mean wave height is 1 meter, what fraction of waves are likely to be larger than 3 meters?

\>>> meanvalue \= 1
\>>> modevalue \= np.sqrt(2 / np.pi) \* meanvalue
\>>> s \= rng.rayleigh(modevalue, 1000000)

Copy to clipboard

The percentage of waves larger than 3 meters is:

\>>> 100.\*sum(s\>3)/1000000.
0.087300000000000003 # random

Copy to clipboard

Go BackOpen In Tab

On this page