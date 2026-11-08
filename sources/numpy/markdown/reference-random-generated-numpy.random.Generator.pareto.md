[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.pareto.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.pareto.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.pareto.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.pareto.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.pareto.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.pareto.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.pareto.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.pareto.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.pareto.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.pareto.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.pareto.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.pareto.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.pareto.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.pareto.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.pareto.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.pareto.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.pareto.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.pareto.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.pareto.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.pareto.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.pareto.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.pareto.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.pareto[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.pareto.html#numpy-random-generator-pareto "Link to this heading")

==================================================================================================================================================================================

method

random.Generator.pareto(_a_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.pareto.html#numpy.random.Generator.pareto "Link to this definition")

Draw samples from a Pareto II (AKA Lomax) distribution with specified shape.

Parameters:

**a**float or array\_like of floats

Shape of the distribution. Must be positive.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `a` is a scalar. Otherwise, `np.array(a).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the Pareto II distribution.

See also

[`scipy.stats.pareto`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pareto.html#scipy.stats.pareto "(in SciPy v1.18.0)")

Pareto I distribution

[`scipy.stats.lomax`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.lomax.html#scipy.stats.lomax "(in SciPy v1.18.0)")

Lomax (Pareto II) distribution

[`scipy.stats.genpareto`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genpareto.html#scipy.stats.genpareto "(in SciPy v1.18.0)")

Generalized Pareto distribution

Notes

The probability density for the Pareto II distribution is

\\\[p(x) = \\frac{a}{(x+1)^{a+1}} , x \\ge 0\\\]

where \\(a > 0\\) is the shape.

The Pareto II distribution is a shifted and scaled version of the Pareto I distribution, which can be found in [`scipy.stats.pareto`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pareto.html#scipy.stats.pareto "(in SciPy v1.18.0)")
.

References

\[1\]

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

\>>> a \= 3.
\>>> rng \= np.random.default\_rng()
\>>> s \= rng.pareto(a, 10000)

Copy to clipboard

Display the histogram of the samples, along with the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> x \= np.linspace(0, 3, 50)
\>>> pdf \= a / (x+1)\*\*(a+1)
\>>> plt.hist(s, bins\=x, density\=True, label\='histogram')
\>>> plt.plot(x, pdf, linewidth\=2, color\='r', label\='pdf')
\>>> plt.xlim(x.min(), x.max())
\>>> plt.legend()
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-pareto-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-pareto-1.png)

Go BackOpen In Tab

On this page