[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.f.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.f.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.f.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.f.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.f.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.f.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.f.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.f.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.f.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.f.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.f.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.f.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.f.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.f.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.f.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.f.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.f.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.f.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.f.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.f.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.f.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.f.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.f[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.f.html#numpy-random-generator-f "Link to this heading")

===================================================================================================================================================================

method

random.Generator.f(_dfnum_, _dfden_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.f.html#numpy.random.Generator.f "Link to this definition")

Draw samples from an F distribution.

Samples are drawn from an F distribution with specified parameters, _dfnum_ (degrees of freedom in numerator) and _dfden_ (degrees of freedom in denominator), where both parameters must be greater than zero.

The random variate of the F distribution (also known as the Fisher distribution) is a continuous probability distribution that arises in ANOVA tests, and is the ratio of two chi-square variates.

Parameters:

**dfnum**float or array\_like of floats

Degrees of freedom in numerator, must be > 0.

**dfden**float or array\_like of float

Degrees of freedom in denominator, must be > 0.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `dfnum` and `dfden` are both scalars. Otherwise, `np.broadcast(dfnum, dfden).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized Fisher distribution.

See also

[`scipy.stats.f`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f.html#scipy.stats.f "(in SciPy v1.18.0)")

probability density function, distribution or cumulative density function, etc.

Notes

The F statistic is used to compare in-group variances to between-group variances. Calculating the distribution depends on the sampling, and so it is a function of the respective degrees of freedom in the problem. The variable _dfnum_ is the number of samples minus one, the between-groups degrees of freedom, while _dfden_ is the within-groups degrees of freedom, the sum of the number of samples in each group minus the number of groups.

References

\[[1](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.f.html#id3)\
\]

Glantz, Stanton A. “Primer of Biostatistics.”, McGraw-Hill, Fifth Edition, 2002.

\[2\]

Wikipedia, “F-distribution”, [https://en.wikipedia.org/wiki/F-distribution](https://en.wikipedia.org/wiki/F-distribution)

Examples

Try it in your browser!

An example from Glantz [\[1\]](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.f.html#r499d2c9e74c3-1)
, pp 47-40:

Two groups, children of diabetics (25 people) and children from people without diabetes (25 controls). Fasting blood glucose was measured, case group had a mean value of 86.1, controls had a mean value of 82.2. Standard deviations were 2.09 and 2.49 respectively. Are these data consistent with the null hypothesis that the parents diabetic status does not affect their children’s blood glucose levels? Calculating the F statistic from the data gives a value of 36.01.

Draw samples from the distribution:

\>>> dfnum \= 1. \# between group degrees of freedom
\>>> dfden \= 48. \# within groups degrees of freedom
\>>> rng \= np.random.default\_rng()
\>>> s \= rng.f(dfnum, dfden, 1000)

Copy to clipboard

The lower bound for the top 1% of the samples is :

\>>> np.sort(s)\[\-10\]
7.61988120985 # random

Copy to clipboard

So there is about a 1% chance that the F statistic will exceed 7.62, the measured value is 36, so the null hypothesis is rejected at the 1% level.

The corresponding probability density function for `n = 20` and `m = 20` is:

\>>> import matplotlib.pyplot as plt
\>>> from scipy import stats
\>>> dfnum, dfden, size \= 20, 20, 10000
\>>> s \= rng.f(dfnum\=dfnum, dfden\=dfden, size\=size)
\>>> bins, density, \_ \= plt.hist(s, 30, density\=True)
\>>> x \= np.linspace(0, 5, 1000)
\>>> plt.plot(x, stats.f.pdf(x, dfnum, dfden))
\>>> plt.xlim(\[0, 5\])
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-f-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-f-1.png)

Go BackOpen In Tab

On this page