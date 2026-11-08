[Skip to main content](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.weibull.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/generated/numpy.random.Generator.weibull.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.weibull.html)
[2.4](https://numpy.org/doc/2.4/reference/random/generated/numpy.random.Generator.weibull.html)
[2.3](https://numpy.org/doc/2.3/reference/random/generated/numpy.random.Generator.weibull.html)
[2.2](https://numpy.org/doc/2.2/reference/random/generated/numpy.random.Generator.weibull.html)
[2.1](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.Generator.weibull.html)
[2.0](https://numpy.org/doc/2.0/reference/random/generated/numpy.random.Generator.weibull.html)
[1.26](https://numpy.org/doc/1.26/reference/random/generated/numpy.random.Generator.weibull.html)
[1.25](https://numpy.org/doc/1.25/reference/random/generated/numpy.random.Generator.weibull.html)
[1.24](https://numpy.org/doc/1.24/reference/random/generated/numpy.random.Generator.weibull.html)
[1.23](https://numpy.org/doc/1.23/reference/random/generated/numpy.random.Generator.weibull.html)
[1.22](https://numpy.org/doc/1.22/reference/random/generated/numpy.random.Generator.weibull.html)
[1.21](https://numpy.org/doc/1.21/reference/random/generated/numpy.random.Generator.weibull.html)
[1.20](https://numpy.org/doc/1.20/reference/random/generated/numpy.random.Generator.weibull.html)
[1.19](https://numpy.org/doc/1.19/reference/random/generated/numpy.random.Generator.weibull.html)
[1.18](https://numpy.org/doc/1.18/reference/random/generated/numpy.random.Generator.weibull.html)
[1.17](https://numpy.org/doc/1.17/reference/random/generated/numpy.random.Generator.weibull.html)
[1.16](https://numpy.org/doc/1.16/reference/random/generated/numpy.random.Generator.weibull.html)
[1.15](https://numpy.org/doc/1.15/reference/random/generated/numpy.random.Generator.weibull.html)
[1.14](https://numpy.org/doc/1.14/reference/random/generated/numpy.random.Generator.weibull.html)
[1.13](https://numpy.org/doc/1.13/reference/random/generated/numpy.random.Generator.weibull.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.random.Generator.weibull[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.weibull.html#numpy-random-generator-weibull "Link to this heading")

=====================================================================================================================================================================================

method

random.Generator.weibull(_a_, _size\=None_)[#](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.weibull.html#numpy.random.Generator.weibull "Link to this definition")

Draw samples from a Weibull distribution.

Draw samples from a 1-parameter Weibull distribution with the given shape parameter _a_.

Here, U is drawn from the uniform distribution over (0,1\].

The more common 2-parameter Weibull, including a scale parameter \\lambda is just X = \\lambda(-ln(U))^{1/a}.

Parameters:

**a**float or array\_like of floats

Shape parameter of the distribution. Must be nonnegative.

**size**int or tuple of ints, optional

Output shape. If the given shape is, e.g., `(m, n, k)`, then `m * n * k` samples are drawn. If size is `None` (default), a single value is returned if `a` is a scalar. Otherwise, `np.array(a).size` samples are drawn.

Returns:

**out**ndarray or scalar

Drawn samples from the parameterized Weibull distribution.

See also

[`scipy.stats.weibull_max`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.weibull_max.html#scipy.stats.weibull_max "(in SciPy v1.18.0)")

[`scipy.stats.weibull_min`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.weibull_min.html#scipy.stats.weibull_min "(in SciPy v1.18.0)")

[`scipy.stats.genextreme`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.genextreme.html#scipy.stats.genextreme "(in SciPy v1.18.0)")

[`gumbel`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.gumbel.html#numpy.random.Generator.gumbel "numpy.random.Generator.gumbel")

Notes

The Weibull (or Type III asymptotic extreme value distribution for smallest values, SEV Type III, or Rosin-Rammler distribution) is one of a class of Generalized Extreme Value (GEV) distributions used in modeling extreme value problems. This class includes the Gumbel and Frechet distributions.

The probability density for the Weibull distribution is

p(x) = \\frac{a} {\\lambda}(\\frac{x}{\\lambda})^{a-1}e^{-(x/\\lambda)^a},

where a is the shape and \\lambda the scale.

The function has its peak (the mode) at \\lambda(\\frac{a-1}{a})^{1/a}.

When `a = 1`, the Weibull distribution reduces to the exponential distribution.

References

\[1\]

Waloddi Weibull, Royal Technical University, Stockholm, 1939 “A Statistical Theory Of The Strength Of Materials”, Ingeniorsvetenskapsakademiens Handlingar Nr 151, 1939, Generalstabens Litografiska Anstalts Forlag, Stockholm.

\[2\]

Waloddi Weibull, “A Statistical Distribution Function of Wide Applicability”, Journal Of Applied Mechanics ASME Paper 1951.

\[3\]

Wikipedia, “Weibull distribution”, [https://en.wikipedia.org/wiki/Weibull\_distribution](https://en.wikipedia.org/wiki/Weibull_distribution)

Examples

Try it in your browser!

Draw samples from the distribution:

\>>> rng \= np.random.default\_rng()
\>>> a \= 5. \# shape
\>>> s \= rng.weibull(a, 1000)

Copy to clipboard

Display the histogram of the samples, along with the probability density function:

\>>> import matplotlib.pyplot as plt
\>>> def weibull(x, n, a):
...     return (a / n) \* (x / n)\*\*(a \- 1) \* np.exp(\-(x / n)\*\*a)
\>>> count, bins, \_ \= plt.hist(rng.weibull(5., 1000))
\>>> x \= np.linspace(0, 2, 1000)
\>>> bin\_spacing \= np.mean(np.diff(bins))
\>>> plt.plot(x, weibull(x, 1., 5.) \* bin\_spacing \* s.size, label\='Weibull PDF')
\>>> plt.legend()
\>>> plt.show()

Copy to clipboard

![../../../_images/numpy-random-Generator-weibull-1.png](https://numpy.org/doc/stable/_images/numpy-random-Generator-weibull-1.png)

Go BackOpen In Tab

On this page