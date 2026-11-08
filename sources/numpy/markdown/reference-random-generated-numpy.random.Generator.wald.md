[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.wald.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.wald.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.wald.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.wald.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.wald.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.wald.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.wald.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.wald.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.wald.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.wald.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.wald.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.wald.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.wald.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.wald.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.wald.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.wald.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.wald.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.wald.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.wald.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.wald.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.wald.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.wald.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.wald[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.wald.html#numpy-random-generator-wald "Link to this heading")

============================================================================================================================================================================

method

random.Generator.wald(_mean_, _scale_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.wald.html#numpy.random.Generator.wald "Link to this definition")

Draw samples from a Wald, or inverse Gaussian, distribution.

As the scale approaches infinity, the distribution becomes more like a Gaussian. Some references claim that the Wald is an inverse Gaussian with mean equal to 1, but this is by no means universal.

The inverse Gaussian distribution was first studied in relationship to Brownian motion. In 1956 M.C.K. Tweedie used the name inverse Gaussian because there is an inverse relationship between the time to cover a unit distance and distance covered in unit time.

Parameters:

**mean**float or array\_like of floats

Distribution mean, must be > 0.

**scale**float or array\_like of floats

Scale parameter, must be > 0.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `mean` and `scale` are both scalars. Otherwise, `np.broadcast(mean, scale).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized Wald distribution.

Notes

The probability density function for the Wald distribution is

As noted above the inverse Gaussian distribution first arise from attempts to model Brownian motion. It is also a competitor to the Weibull for use in reliability modeling and modeling stock returns and interest rate processes.

References

\[1\]

Brighton Webs Ltd., Wald Distribution, [https://web.archive.org/web/20090423014010/http://www.brighton-webs.co.uk:80/distributions/wald.asp](https://web.archive.org/web/20090423014010/http://www.brighton-webs.co.uk:80/distributions/wald.asp)

\[2\]

Chhikara, Raj S., and Folks, J. Leroy, “The Inverse Gaussian Distribution: Theory : Methodology, and Applications”, CRC Press, 1988.

\[3\]

Wikipedia, “Inverse Gaussian distribution” [https://en.wikipedia.org/wiki/Inverse\_Gaussian\_distribution](https://en.wikipedia.org/wiki/Inverse_Gaussian_distribution)

Examples

Try it in your browser!

Draw values from the distribution and plot the histogram:

\>>> import matplotlib.pyplot as plt
\>>> rng \= np.random.default\_rng()
\>>> h \= plt.hist(rng.wald(3, 2, 100000), bins\=200, density\=True)
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-wald-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-wald-1.png)

Go BackOpen In Tab

On this page