[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.noncentral_f.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.noncentral_f.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.noncentral_f.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.noncentral\_f[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.noncentral_f.html#numpy-random-generator-noncentral-f "Link to this heading")

=====================================================================================================================================================================================================

method

random.Generator.noncentral\_f(_dfnum_, _dfden_, _nonc_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.noncentral_f.html#numpy.random.Generator.noncentral_f "Link to this definition")

Draw samples from the noncentral F distribution.

Samples are drawn from an F distribution with specified parameters, _dfnum_ (degrees of freedom in numerator) and _dfden_ (degrees of freedom in denominator), where both parameters > 1. _nonc_ is the non-centrality parameter.

Parameters:

**dfnum**float or array\_like of floats

Numerator degrees of freedom, must be > 0.

**dfden**float or array\_like of floats

Denominator degrees of freedom, must be > 0.

**nonc**float or array\_like of floats

Non-centrality parameter, the sum of the squares of the numerator means, must be >= 0.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `dfnum`, `dfden`, and `nonc` are all scalars. Otherwise, `np.broadcast(dfnum, dfden, nonc).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized noncentral Fisher distribution.

Notes

When calculating the power of an experiment (power = probability of rejecting the null hypothesis when a specific alternative is true) the non-central F statistic becomes important. When the null hypothesis is true, the F statistic follows a central F distribution. When the null hypothesis is not true, then it follows a non-central F statistic.

References

\[1\]

Weisstein, Eric W. “Noncentral F-Distribution.” From MathWorld–A Wolfram Web Resource. [https://mathworld.wolfram.com/NoncentralF-Distribution.html](https://mathworld.wolfram.com/NoncentralF-Distribution.html)

\[2\]

Wikipedia, “Noncentral F-distribution”, [https://en.wikipedia.org/wiki/Noncentral\_F-distribution](https://en.wikipedia.org/wiki/Noncentral_F-distribution)

Examples

Try it in your browser!

In a study, testing for a specific alternative to the null hypothesis requires use of the Noncentral F distribution. We need to calculate the area in the tail of the distribution that exceeds the value of the F distribution for the null hypothesis. We’ll plot the two probability distributions for comparison.

\>>> rng \= np.random.default\_rng()
\>>> dfnum \= 3 \# between group deg of freedom
\>>> dfden \= 20 \# within groups degrees of freedom
\>>> nonc \= 3.0
\>>> nc\_vals \= rng.noncentral\_f(dfnum, dfden, nonc, 1000000)
\>>> NF \= np.histogram(nc\_vals, bins\=50, density\=True)
\>>> c\_vals \= rng.f(dfnum, dfden, 1000000)
\>>> F \= np.histogram(c\_vals, bins\=50, density\=True)
\>>> import matplotlib.pyplot as plt
\>>> plt.plot(F\[1\]\[1:\], F\[0\])
\>>> plt.plot(NF\[1\]\[1:\], NF\[0\])
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-noncentral_f-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-noncentral_f-1.png)

Go BackOpen In Tab

On this page