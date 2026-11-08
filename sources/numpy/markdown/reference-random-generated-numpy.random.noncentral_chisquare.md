[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.noncentral_chisquare.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.noncentral_chisquare.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.noncentral_chisquare.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.noncentral_chisquare.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.noncentral_chisquare.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.noncentral_chisquare.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.noncentral_chisquare.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.noncentral_chisquare.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.noncentral_chisquare.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.noncentral\_chisquare[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.noncentral_chisquare.html#numpy-random-noncentral-chisquare "Link to this heading")

===============================================================================================================================================================================================

random.noncentral\_chisquare(_df_, _nonc_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.noncentral_chisquare.html#numpy.random.noncentral_chisquare "Link to this definition")

Draw samples from a noncentral chi-square distribution.

The noncentral \\(\\chi^2\\) distribution is a generalization of the \\(\\chi^2\\) distribution.

Note

New code should use the [`noncentral_chisquare`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.noncentral_chisquare.html#numpy.random.Generator.noncentral_chisquare "numpy.random.Generator.noncentral_chisquare")
 method of a [`Generator`](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 instance instead; please see the [Quick start](https://numpy.org/doc/stable/reference/random/index.html#random-quick-start)
.

Parameters:

**df**float or array\_like of floats

Degrees of freedom, must be > 0.

**nonc**float or array\_like of floats

Non-centrality, must be non-negative.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `df` and `nonc` are both scalars. Otherwise, `np.broadcast(df, nonc).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized noncentral chi-square distribution.

See also

[`random.Generator.noncentral_chisquare`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.noncentral_chisquare.html#numpy.random.Generator.noncentral_chisquare "numpy.random.Generator.noncentral_chisquare")

which should be used for new code.

Notes

The probability density function for the noncentral Chi-square distribution is

\\\[P(x;df,nonc) = \\sum^{\\infty}\_{i=0} \\frac{e^{-nonc/2}(nonc/2)^{i}}{i!} P\_{Y\_{df+2i}}(x),\\\]

where \\(Y\_{q}\\) is the Chi-square with q degrees of freedom.

References

\[1\]

Wikipedia, “Noncentral chi-squared distribution” [https://en.wikipedia.org/wiki/Noncentral\_chi-squared\_distribution](https://en.wikipedia.org/wiki/Noncentral_chi-squared_distribution)

Examples

Try it in your browser!

Draw values from the distribution and plot the histogram

\>>> import matplotlib.pyplot as plt
\>>> values \= plt.hist(np.random.noncentral\_chisquare(3, 20, 100000),
...                   bins\=200, density\=True)
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-noncentral_chisquare-1_00_00.png](https://numpy.org/doc/stable/_images/numpy-random-noncentral_chisquare-1_00_00.png)

Draw values from a noncentral chisquare with very small noncentrality, and compare to a chisquare.

\>>> plt.figure()
\>>> values \= plt.hist(np.random.noncentral\_chisquare(3, .0000001, 100000),
...                   bins\=np.arange(0., 25, .1), density\=True)
\>>> values2 \= plt.hist(np.random.chisquare(3, 100000),
...                    bins\=np.arange(0., 25, .1), density\=True)
\>>> plt.plot(values\[1\]\[0:\-1\], values\[0\]\-values2\[0\], 'ob')
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-noncentral_chisquare-1_01_00.png](https://numpy.org/doc/stable/_images/numpy-random-noncentral_chisquare-1_01_00.png)

Demonstrate how large values of non-centrality lead to a more symmetric distribution.

\>>> plt.figure()
\>>> values \= plt.hist(np.random.noncentral\_chisquare(3, 20, 100000),
...                   bins\=200, density\=True)
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-noncentral_chisquare-1_02_00.png](https://numpy.org/doc/stable/_images/numpy-random-noncentral_chisquare-1_02_00.png)

Go BackOpen In Tab

On this page